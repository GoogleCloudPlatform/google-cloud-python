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

from google.analytics.data_v1alpha import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.analytics.data_v1alpha.services.alpha_analytics_data import pagers
from google.analytics.data_v1alpha.types import analytics_data_api, data

from .client import AlphaAnalyticsDataClient
from .transports.base import DEFAULT_CLIENT_INFO, AlphaAnalyticsDataTransport
from .transports.grpc_asyncio import AlphaAnalyticsDataGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class AlphaAnalyticsDataAsyncClient:
    """Google Analytics reporting data service."""

    _client: AlphaAnalyticsDataClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = AlphaAnalyticsDataClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AlphaAnalyticsDataClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = AlphaAnalyticsDataClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = AlphaAnalyticsDataClient._DEFAULT_UNIVERSE

    audience_list_path = staticmethod(AlphaAnalyticsDataClient.audience_list_path)
    parse_audience_list_path = staticmethod(
        AlphaAnalyticsDataClient.parse_audience_list_path
    )
    metadata_path = staticmethod(AlphaAnalyticsDataClient.metadata_path)
    parse_metadata_path = staticmethod(AlphaAnalyticsDataClient.parse_metadata_path)
    property_path = staticmethod(AlphaAnalyticsDataClient.property_path)
    parse_property_path = staticmethod(AlphaAnalyticsDataClient.parse_property_path)
    property_quotas_snapshot_path = staticmethod(
        AlphaAnalyticsDataClient.property_quotas_snapshot_path
    )
    parse_property_quotas_snapshot_path = staticmethod(
        AlphaAnalyticsDataClient.parse_property_quotas_snapshot_path
    )
    recurring_audience_list_path = staticmethod(
        AlphaAnalyticsDataClient.recurring_audience_list_path
    )
    parse_recurring_audience_list_path = staticmethod(
        AlphaAnalyticsDataClient.parse_recurring_audience_list_path
    )
    report_task_path = staticmethod(AlphaAnalyticsDataClient.report_task_path)
    parse_report_task_path = staticmethod(
        AlphaAnalyticsDataClient.parse_report_task_path
    )
    common_billing_account_path = staticmethod(
        AlphaAnalyticsDataClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AlphaAnalyticsDataClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AlphaAnalyticsDataClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        AlphaAnalyticsDataClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        AlphaAnalyticsDataClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        AlphaAnalyticsDataClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AlphaAnalyticsDataClient.common_project_path)
    parse_common_project_path = staticmethod(
        AlphaAnalyticsDataClient.parse_common_project_path
    )
    common_location_path = staticmethod(AlphaAnalyticsDataClient.common_location_path)
    parse_common_location_path = staticmethod(
        AlphaAnalyticsDataClient.parse_common_location_path
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
            AlphaAnalyticsDataAsyncClient: The constructed client.
        """
        sa_info_func = (
            AlphaAnalyticsDataClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(AlphaAnalyticsDataAsyncClient, info, *args, **kwargs)

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
            AlphaAnalyticsDataAsyncClient: The constructed client.
        """
        sa_file_func = (
            AlphaAnalyticsDataClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(AlphaAnalyticsDataAsyncClient, filename, *args, **kwargs)

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
        return AlphaAnalyticsDataClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> AlphaAnalyticsDataTransport:
        """Returns the transport used by the client instance.

        Returns:
            AlphaAnalyticsDataTransport: The transport used by the client instance.
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

    get_transport_class = AlphaAnalyticsDataClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                AlphaAnalyticsDataTransport,
                Callable[..., AlphaAnalyticsDataTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the alpha analytics data async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AlphaAnalyticsDataTransport,Callable[..., AlphaAnalyticsDataTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AlphaAnalyticsDataTransport constructor.
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
        self._client = AlphaAnalyticsDataClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.analytics.data_v1alpha.AlphaAnalyticsDataAsyncClient`.",
                extra={
                    "serviceName": "google.analytics.data.v1alpha.AlphaAnalyticsData",
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
                    "serviceName": "google.analytics.data.v1alpha.AlphaAnalyticsData",
                    "credentialsType": None,
                },
            )

    async def run_funnel_report(
        self,
        request: Optional[
            Union[analytics_data_api.RunFunnelReportRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RunFunnelReportResponse:
        r"""Returns a customized funnel report of your Google Analytics
        event data. The data returned from the API is as a table with
        columns for the requested dimensions and metrics.

        Funnel exploration lets you visualize the steps your users take
        to complete a task and quickly see how well they are succeeding
        or failing at each step. For example, how do prospects become
        shoppers and then become buyers? How do one time buyers become
        repeat buyers? With this information, you can improve
        inefficient or abandoned customer journeys. To learn more, see
        `GA4 Funnel
        Explorations <https://support.google.com/analytics/answer/9327974>`__.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Data API Funnel Reporting
        Feedback <https://docs.google.com/forms/d/e/1FAIpQLSdwOlQDJAUoBiIgUZZ3S_Lwi8gr7Bb0k1jhvc-DEg7Rol3UjA/viewform>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_run_funnel_report():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.RunFunnelReportRequest(
                )

                # Make the request
                response = await client.run_funnel_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.RunFunnelReportRequest, dict]]):
                The request object. The request for a funnel report.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1alpha.types.RunFunnelReportResponse:
                The funnel report response contains
                two sub reports. The two sub reports are
                different combinations of dimensions and
                metrics.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.RunFunnelReportRequest):
            request = analytics_data_api.RunFunnelReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_funnel_report
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

    async def create_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.CreateAudienceListRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        audience_list: Optional[analytics_data_api.AudienceList] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates an audience list for later retrieval. This method
        quickly returns the audience list's resource name and initiates
        a long running asynchronous request to form an audience list. To
        list the users in an audience list, first create the audience
        list through this method and then send the audience resource
        name to the ``QueryAudienceList`` method.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        An audience list is a snapshot of the users currently in the
        audience at the time of audience list creation. Creating
        audience lists for one audience on different days will return
        different results as users enter and exit the audience.

        Audiences in Google Analytics 4 allow you to segment your users
        in the ways that are important to your business. To learn more,
        see https://support.google.com/analytics/answer/9267572.
        Audience lists contain the users in each audience.

        This method is available at beta stability at
        `audienceExports.create <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/create>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_create_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                audience_list = data_v1alpha.AudienceList()
                audience_list.audience = "audience_value"

                request = data_v1alpha.CreateAudienceListRequest(
                    parent="parent_value",
                    audience_list=audience_list,
                )

                # Make the request
                operation = await client.create_audience_list(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.CreateAudienceListRequest, dict]]):
                The request object. A request to create a new audience
                list.
            parent (:class:`str`):
                Required. The parent resource where this audience list
                will be created. Format: ``properties/{property}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audience_list (:class:`google.analytics.data_v1alpha.types.AudienceList`):
                Required. The audience list to
                create.

                This corresponds to the ``audience_list`` field
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

                The result type for the operation will be :class:`google.analytics.data_v1alpha.types.AudienceList` An audience list is a list of users in an audience at the time of the list's
                   creation. One audience may have multiple audience
                   lists created for different days.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, audience_list]
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
        if not isinstance(request, analytics_data_api.CreateAudienceListRequest):
            request = analytics_data_api.CreateAudienceListRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if audience_list is not None:
            request.audience_list = audience_list

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_audience_list
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
            analytics_data_api.AudienceList,
            metadata_type=analytics_data_api.AudienceListMetadata,
        )

        # Done; return the response.
        return response

    async def query_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.QueryAudienceListRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.QueryAudienceListResponse:
        r"""Retrieves an audience list of users. After creating an audience,
        the users are not immediately available for listing. First, a
        request to ``CreateAudienceList`` is necessary to create an
        audience list of users, and then second, this method is used to
        retrieve the users in the audience list.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        Audiences in Google Analytics 4 allow you to segment your users
        in the ways that are important to your business. To learn more,
        see https://support.google.com/analytics/answer/9267572.

        This method is available at beta stability at
        `audienceExports.query <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/query>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_query_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.QueryAudienceListRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.query_audience_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.QueryAudienceListRequest, dict]]):
                The request object. A request to list users in an
                audience list.
            name (:class:`str`):
                Required. The name of the audience list to retrieve
                users from. Format:
                ``properties/{property}/audienceLists/{audience_list}``

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
            google.analytics.data_v1alpha.types.QueryAudienceListResponse:
                A list of users in an audience list.
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
        if not isinstance(request, analytics_data_api.QueryAudienceListRequest):
            request = analytics_data_api.QueryAudienceListRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.query_audience_list
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

    async def get_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.GetAudienceListRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.AudienceList:
        r"""Gets configuration metadata about a specific audience list. This
        method can be used to understand an audience list after it has
        been created.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        This method is available at beta stability at
        `audienceExports.get <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/get>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_get_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetAudienceListRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_audience_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.GetAudienceListRequest, dict]]):
                The request object. A request to retrieve configuration
                metadata about a specific audience list.
            name (:class:`str`):
                Required. The audience list resource name. Format:
                ``properties/{property}/audienceLists/{audience_list}``

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
            google.analytics.data_v1alpha.types.AudienceList:
                An audience list is a list of users
                in an audience at the time of the list's
                creation. One audience may have multiple
                audience lists created for different
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
        if not isinstance(request, analytics_data_api.GetAudienceListRequest):
            request = analytics_data_api.GetAudienceListRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_audience_list
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

    async def list_audience_lists(
        self,
        request: Optional[
            Union[analytics_data_api.ListAudienceListsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAudienceListsAsyncPager:
        r"""Lists all audience lists for a property. This method can be used
        for you to find and reuse existing audience lists rather than
        creating unnecessary new audience lists. The same audience can
        have multiple audience lists that represent the list of users
        that were in an audience on different days.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        This method is available at beta stability at
        `audienceExports.list <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/list>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_list_audience_lists():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.ListAudienceListsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_audience_lists(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.ListAudienceListsRequest, dict]]):
                The request object. A request to list all audience lists
                for a property.
            parent (:class:`str`):
                Required. All audience lists for this property will be
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
            google.analytics.data_v1alpha.services.alpha_analytics_data.pagers.ListAudienceListsAsyncPager:
                A list of all audience lists for a
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
        if not isinstance(request, analytics_data_api.ListAudienceListsRequest):
            request = analytics_data_api.ListAudienceListsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_audience_lists
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
        response = pagers.ListAudienceListsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_recurring_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.CreateRecurringAudienceListRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        recurring_audience_list: Optional[
            analytics_data_api.RecurringAudienceList
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RecurringAudienceList:
        r"""Creates a recurring audience list. Recurring audience lists
        produces new audience lists each day. Audience lists are users
        in an audience at the time of the list's creation.

        A recurring audience list ensures that you have audience list
        based on the most recent data available for use each day. If you
        manually create audience list, you don't know when an audience
        list based on an additional day's data is available. This
        recurring audience list automates the creation of an audience
        list when an additional day's data is available. You will
        consume fewer quota tokens by using recurring audience list
        versus manually creating audience list at various times of day
        trying to guess when an additional day's data is ready.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_create_recurring_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                recurring_audience_list = data_v1alpha.RecurringAudienceList()
                recurring_audience_list.audience = "audience_value"

                request = data_v1alpha.CreateRecurringAudienceListRequest(
                    parent="parent_value",
                    recurring_audience_list=recurring_audience_list,
                )

                # Make the request
                response = await client.create_recurring_audience_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.CreateRecurringAudienceListRequest, dict]]):
                The request object. A request to create a new recurring
                audience list.
            parent (:class:`str`):
                Required. The parent resource where this recurring
                audience list will be created. Format:
                ``properties/{property}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            recurring_audience_list (:class:`google.analytics.data_v1alpha.types.RecurringAudienceList`):
                Required. The recurring audience list
                to create.

                This corresponds to the ``recurring_audience_list`` field
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
            google.analytics.data_v1alpha.types.RecurringAudienceList:
                A recurring audience list produces
                new audience lists each day. Audience
                lists are users in an audience at the
                time of the list's creation. A recurring
                audience list ensures that you have
                audience list based on the most recent
                data available for use each day.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, recurring_audience_list]
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
            request, analytics_data_api.CreateRecurringAudienceListRequest
        ):
            request = analytics_data_api.CreateRecurringAudienceListRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if recurring_audience_list is not None:
            request.recurring_audience_list = recurring_audience_list

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_recurring_audience_list
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

    async def get_recurring_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.GetRecurringAudienceListRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RecurringAudienceList:
        r"""Gets configuration metadata about a specific recurring audience
        list. This method can be used to understand a recurring audience
        list's state after it has been created. For example, a recurring
        audience list resource will generate audience list instances for
        each day, and this method can be used to get the resource name
        of the most recent audience list instance.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_get_recurring_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetRecurringAudienceListRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_recurring_audience_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.GetRecurringAudienceListRequest, dict]]):
                The request object. A request to retrieve configuration
                metadata about a specific recurring
                audience list.
            name (:class:`str`):
                Required. The recurring audience list resource name.
                Format:
                ``properties/{property}/recurringAudienceLists/{recurring_audience_list}``

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
            google.analytics.data_v1alpha.types.RecurringAudienceList:
                A recurring audience list produces
                new audience lists each day. Audience
                lists are users in an audience at the
                time of the list's creation. A recurring
                audience list ensures that you have
                audience list based on the most recent
                data available for use each day.

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
        if not isinstance(request, analytics_data_api.GetRecurringAudienceListRequest):
            request = analytics_data_api.GetRecurringAudienceListRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_recurring_audience_list
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

    async def list_recurring_audience_lists(
        self,
        request: Optional[
            Union[analytics_data_api.ListRecurringAudienceListsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRecurringAudienceListsAsyncPager:
        r"""Lists all recurring audience lists for a property. This method
        can be used for you to find and reuse existing recurring
        audience lists rather than creating unnecessary new recurring
        audience lists. The same audience can have multiple recurring
        audience lists that represent different dimension combinations;
        for example, just the dimension ``deviceId`` or both the
        dimensions ``deviceId`` and ``userId``.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_list_recurring_audience_lists():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.ListRecurringAudienceListsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_recurring_audience_lists(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.ListRecurringAudienceListsRequest, dict]]):
                The request object. A request to list all recurring
                audience lists for a property.
            parent (:class:`str`):
                Required. All recurring audience lists for this property
                will be listed in the response. Format:
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
            google.analytics.data_v1alpha.services.alpha_analytics_data.pagers.ListRecurringAudienceListsAsyncPager:
                A list of all recurring audience
                lists for a property.
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
            request, analytics_data_api.ListRecurringAudienceListsRequest
        ):
            request = analytics_data_api.ListRecurringAudienceListsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_recurring_audience_lists
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
        response = pagers.ListRecurringAudienceListsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_property_quotas_snapshot(
        self,
        request: Optional[
            Union[analytics_data_api.GetPropertyQuotasSnapshotRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.PropertyQuotasSnapshot:
        r"""Get all property quotas organized by quota category
        for a given property. This will charge 1 property quota
        from the category with the most quota.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_get_property_quotas_snapshot():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetPropertyQuotasSnapshotRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_property_quotas_snapshot(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.GetPropertyQuotasSnapshotRequest, dict]]):
                The request object. A request to return the
                PropertyQuotasSnapshot for a given
                category.
            name (:class:`str`):
                Required. Quotas from this property will be listed in
                the response. Format:
                ``properties/{property}/propertyQuotasSnapshot``

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
            google.analytics.data_v1alpha.types.PropertyQuotasSnapshot:
                Current state of all Property Quotas
                organized by quota category.

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
        if not isinstance(request, analytics_data_api.GetPropertyQuotasSnapshotRequest):
            request = analytics_data_api.GetPropertyQuotasSnapshotRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_property_quotas_snapshot
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

    async def create_report_task(
        self,
        request: Optional[
            Union[analytics_data_api.CreateReportTaskRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        report_task: Optional[analytics_data_api.ReportTask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Initiates the creation of a report task. This method
        quickly returns a report task and initiates a long
        running asynchronous request to form a customized report
        of your Google Analytics event data.

        A report task will be retained and available for
        querying for 72 hours after it has been created.

        A report task created by one user can be listed and
        queried by all users who have access to the property.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_create_report_task():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.CreateReportTaskRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = await client.create_report_task(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.CreateReportTaskRequest, dict]]):
                The request object. A request to create a report task.
            parent (:class:`str`):
                Required. The parent resource where this report task
                will be created. Format: ``properties/{propertyId}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            report_task (:class:`google.analytics.data_v1alpha.types.ReportTask`):
                Required. The report task
                configuration to create.

                This corresponds to the ``report_task`` field
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

                The result type for the operation will be
                :class:`google.analytics.data_v1alpha.types.ReportTask`
                A specific report task configuration.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, report_task]
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
        if not isinstance(request, analytics_data_api.CreateReportTaskRequest):
            request = analytics_data_api.CreateReportTaskRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if report_task is not None:
            request.report_task = report_task

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_report_task
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
            analytics_data_api.ReportTask,
            metadata_type=analytics_data_api.ReportTaskMetadata,
        )

        # Done; return the response.
        return response

    async def query_report_task(
        self,
        request: Optional[
            Union[analytics_data_api.QueryReportTaskRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.QueryReportTaskResponse:
        r"""Retrieves a report task's content. After requesting the
        ``CreateReportTask``, you are able to retrieve the report
        content once the report is ACTIVE. This method will return an
        error if the report task's state is not ``ACTIVE``. A query
        response will return the tabular row & column values of the
        report.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_query_report_task():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.QueryReportTaskRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.query_report_task(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.QueryReportTaskRequest, dict]]):
                The request object. A request to fetch the report content
                for a report task.
            name (:class:`str`):
                Required. The report source name. Format:
                ``properties/{property}/reportTasks/{report}``

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
            google.analytics.data_v1alpha.types.QueryReportTaskResponse:
                The report content corresponding to a
                report task.

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
        if not isinstance(request, analytics_data_api.QueryReportTaskRequest):
            request = analytics_data_api.QueryReportTaskRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.query_report_task
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

    async def get_report_task(
        self,
        request: Optional[Union[analytics_data_api.GetReportTaskRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.ReportTask:
        r"""Gets report metadata about a specific report task.
        After creating a report task, use this method to check
        its processing state or inspect its report definition.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_get_report_task():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetReportTaskRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_report_task(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.GetReportTaskRequest, dict]]):
                The request object. A request to retrieve configuration
                metadata about a specific report task.
            name (:class:`str`):
                Required. The report task resource name. Format:
                ``properties/{property}/reportTasks/{report_task}``

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
            google.analytics.data_v1alpha.types.ReportTask:
                A specific report task configuration.
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
        if not isinstance(request, analytics_data_api.GetReportTaskRequest):
            request = analytics_data_api.GetReportTaskRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_report_task
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

    async def list_report_tasks(
        self,
        request: Optional[
            Union[analytics_data_api.ListReportTasksRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListReportTasksAsyncPager:
        r"""Lists all report tasks for a property.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_list_report_tasks():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.ListReportTasksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_report_tasks(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.ListReportTasksRequest, dict]]):
                The request object. A request to list all report tasks
                for a property.
            parent (:class:`str`):
                Required. All report tasks for this property will be
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
            google.analytics.data_v1alpha.services.alpha_analytics_data.pagers.ListReportTasksAsyncPager:
                A list of all report tasks for a
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
        if not isinstance(request, analytics_data_api.ListReportTasksRequest):
            request = analytics_data_api.ListReportTasksRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_report_tasks
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
        response = pagers.ListReportTasksAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def chat(
        self,
        request: Optional[Union[analytics_data_api.ChatRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.ChatResponse:
        r"""Provides a chat interface for interacting with Google Analytics
        data through the API.

        This product uses AI and may display inaccurate info. Your chat
        activity may be used to improve the product and your use is
        subject to Google's
        `Terms <https://policies.google.com/terms>`__, `AI Use
        Policy <https://policies.google.com/terms/generative-ai/use-policy>`__,
        and `Privacy Policy <https://policies.google.com/privacy>`__.
        `Learn more about Chat AI
        Privacy <https://support.google.com/helpguide/answer/14185196>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_chat():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.ChatRequest(
                    property="property_value",
                    user_query="user_query_value",
                )

                # Make the request
                response = await client.chat(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.ChatRequest, dict]]):
                The request object. Request message for the Chat method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1alpha.types.ChatResponse:
                Response message for the Chat method.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.ChatRequest):
            request = analytics_data_api.ChatRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.chat]

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

    async def run_report(
        self,
        request: Optional[Union[analytics_data_api.RunReportRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RunReportResponse:
        r"""Returns a customized report of your Google Analytics
        event data. Reports contain statistics derived from data
        collected by the Google Analytics tracking code. The
        data returned from the API is as a table with columns
        for the requested dimensions and metrics. Metrics are
        individual measurements of user activity on your
        property, such as active users or event count.
        Dimensions break down metrics across some common
        criteria, such as country or event name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            async def sample_run_report():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.RunReportRequest(
                    property="property_value",
                )

                # Make the request
                response = await client.run_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.RunReportRequest, dict]]):
                The request object. The request to generate a report.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1alpha.types.RunReportResponse:
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
            from google.analytics import data_v1alpha

            async def sample_get_metadata():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetMetadataRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_metadata(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1alpha.types.GetMetadataRequest, dict]]):
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
            google.analytics.data_v1alpha.types.Metadata:
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

    async def __aenter__(self) -> "AlphaAnalyticsDataAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("AlphaAnalyticsDataAsyncClient",)
