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

from google.cloud.monitoring_dashboard_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.cloud.monitoring_dashboard_v1.services.dashboards_service import pagers
from google.cloud.monitoring_dashboard_v1.types import (
    dashboard,
    dashboard_filter,
    dashboards_service,
    layouts,
)
from google.cloud.monitoring_dashboard_v1.types import dashboard as gmd_dashboard

from .client import DashboardsServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DashboardsServiceTransport
from .transports.grpc_asyncio import DashboardsServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DashboardsServiceAsyncClient:
    """Manages Stackdriver dashboards. A dashboard is an arrangement
    of data display widgets in a specific layout.
    """

    _client: DashboardsServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DashboardsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DashboardsServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DashboardsServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DashboardsServiceClient._DEFAULT_UNIVERSE

    alert_policy_path = staticmethod(DashboardsServiceClient.alert_policy_path)
    parse_alert_policy_path = staticmethod(
        DashboardsServiceClient.parse_alert_policy_path
    )
    dashboard_path = staticmethod(DashboardsServiceClient.dashboard_path)
    parse_dashboard_path = staticmethod(DashboardsServiceClient.parse_dashboard_path)
    common_billing_account_path = staticmethod(
        DashboardsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DashboardsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DashboardsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DashboardsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DashboardsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DashboardsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DashboardsServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DashboardsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DashboardsServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DashboardsServiceClient.parse_common_location_path
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
            DashboardsServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            DashboardsServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DashboardsServiceAsyncClient, info, *args, **kwargs)

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
            DashboardsServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            DashboardsServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DashboardsServiceAsyncClient, filename, *args, **kwargs)

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
        return DashboardsServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DashboardsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DashboardsServiceTransport: The transport used by the client instance.
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

    get_transport_class = DashboardsServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                DashboardsServiceTransport,
                Callable[..., DashboardsServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the dashboards service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DashboardsServiceTransport,Callable[..., DashboardsServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DashboardsServiceTransport constructor.
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
        self._client = DashboardsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.monitoring.dashboard_v1.DashboardsServiceAsyncClient`.",
                extra={
                    "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
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
                    "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                    "credentialsType": None,
                },
            )

    async def create_dashboard(
        self,
        request: Optional[
            Union[dashboards_service.CreateDashboardRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        dashboard: Optional[gmd_dashboard.Dashboard] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gmd_dashboard.Dashboard:
        r"""Creates a new custom dashboard. For examples on how you can use
        this API to create dashboards, see `Managing dashboards by
        API <https://cloud.google.com/monitoring/dashboards/api-dashboard>`__.
        This method requires the ``monitoring.dashboards.create``
        permission on the specified project. For more information about
        permissions, see `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import monitoring_dashboard_v1

            async def sample_create_dashboard():
                # Create a client
                client = monitoring_dashboard_v1.DashboardsServiceAsyncClient()

                # Initialize request argument(s)
                dashboard = monitoring_dashboard_v1.Dashboard()
                dashboard.display_name = "display_name_value"

                request = monitoring_dashboard_v1.CreateDashboardRequest(
                    parent="parent_value",
                    dashboard=dashboard,
                )

                # Make the request
                response = await client.create_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.monitoring_dashboard_v1.types.CreateDashboardRequest, dict]]):
                The request object. The ``CreateDashboard`` request.
            parent (:class:`str`):
                Required. The project on which to execute the request.
                The format is:

                ::

                    projects/[PROJECT_ID_OR_NUMBER]

                The ``[PROJECT_ID_OR_NUMBER]`` must match the dashboard
                resource name.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            dashboard (:class:`google.cloud.monitoring_dashboard_v1.types.Dashboard`):
                Required. The initial dashboard
                specification.

                This corresponds to the ``dashboard`` field
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
            google.cloud.monitoring_dashboard_v1.types.Dashboard:
                A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, dashboard]
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
        if not isinstance(request, dashboards_service.CreateDashboardRequest):
            request = dashboards_service.CreateDashboardRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if dashboard is not None:
            request.dashboard = dashboard

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_dashboard
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

    async def list_dashboards(
        self,
        request: Optional[Union[dashboards_service.ListDashboardsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDashboardsAsyncPager:
        r"""Lists the existing dashboards.

        This method requires the ``monitoring.dashboards.list``
        permission on the specified project. For more information, see
        `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import monitoring_dashboard_v1

            async def sample_list_dashboards():
                # Create a client
                client = monitoring_dashboard_v1.DashboardsServiceAsyncClient()

                # Initialize request argument(s)
                request = monitoring_dashboard_v1.ListDashboardsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_dashboards(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.monitoring_dashboard_v1.types.ListDashboardsRequest, dict]]):
                The request object. The ``ListDashboards`` request.
            parent (:class:`str`):
                Required. The scope of the dashboards to list. The
                format is:

                ::

                    projects/[PROJECT_ID_OR_NUMBER]

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
            google.cloud.monitoring_dashboard_v1.services.dashboards_service.pagers.ListDashboardsAsyncPager:
                The ListDashboards request.

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
        if not isinstance(request, dashboards_service.ListDashboardsRequest):
            request = dashboards_service.ListDashboardsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_dashboards
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
        response = pagers.ListDashboardsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_dashboard(
        self,
        request: Optional[Union[dashboards_service.GetDashboardRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> dashboard.Dashboard:
        r"""Fetches a specific dashboard.

        This method requires the ``monitoring.dashboards.get``
        permission on the specified dashboard. For more information, see
        `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import monitoring_dashboard_v1

            async def sample_get_dashboard():
                # Create a client
                client = monitoring_dashboard_v1.DashboardsServiceAsyncClient()

                # Initialize request argument(s)
                request = monitoring_dashboard_v1.GetDashboardRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.monitoring_dashboard_v1.types.GetDashboardRequest, dict]]):
                The request object. The ``GetDashboard`` request.
            name (:class:`str`):
                Required. The resource name of the Dashboard. The format
                is one of:

                - ``dashboards/[DASHBOARD_ID]`` (for system dashboards)
                - ``projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]``
                  (for custom dashboards).

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
            google.cloud.monitoring_dashboard_v1.types.Dashboard:
                A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

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
        if not isinstance(request, dashboards_service.GetDashboardRequest):
            request = dashboards_service.GetDashboardRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_dashboard
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

    async def delete_dashboard(
        self,
        request: Optional[
            Union[dashboards_service.DeleteDashboardRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing custom dashboard.

        This method requires the ``monitoring.dashboards.delete``
        permission on the specified dashboard. For more information, see
        `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import monitoring_dashboard_v1

            async def sample_delete_dashboard():
                # Create a client
                client = monitoring_dashboard_v1.DashboardsServiceAsyncClient()

                # Initialize request argument(s)
                request = monitoring_dashboard_v1.DeleteDashboardRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_dashboard(request=request)

        Args:
            request (Optional[Union[google.cloud.monitoring_dashboard_v1.types.DeleteDashboardRequest, dict]]):
                The request object. The ``DeleteDashboard`` request.
            name (:class:`str`):
                Required. The resource name of the Dashboard. The format
                is:

                ::

                    projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]

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
        if not isinstance(request, dashboards_service.DeleteDashboardRequest):
            request = dashboards_service.DeleteDashboardRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_dashboard
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

    async def update_dashboard(
        self,
        request: Optional[
            Union[dashboards_service.UpdateDashboardRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> dashboard.Dashboard:
        r"""Replaces an existing custom dashboard with a new definition.

        This method requires the ``monitoring.dashboards.update``
        permission on the specified dashboard. For more information, see
        `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import monitoring_dashboard_v1

            async def sample_update_dashboard():
                # Create a client
                client = monitoring_dashboard_v1.DashboardsServiceAsyncClient()

                # Initialize request argument(s)
                dashboard = monitoring_dashboard_v1.Dashboard()
                dashboard.display_name = "display_name_value"

                request = monitoring_dashboard_v1.UpdateDashboardRequest(
                    dashboard=dashboard,
                )

                # Make the request
                response = await client.update_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.monitoring_dashboard_v1.types.UpdateDashboardRequest, dict]]):
                The request object. The ``UpdateDashboard`` request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.monitoring_dashboard_v1.types.Dashboard:
                A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, dashboards_service.UpdateDashboardRequest):
            request = dashboards_service.UpdateDashboardRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_dashboard
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("dashboard.name", request.dashboard.name),)
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

    async def __aenter__(self) -> "DashboardsServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DashboardsServiceAsyncClient",)
