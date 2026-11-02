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

from google.cloud.chronicle_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.chronicle_v1.services.native_dashboard_service import pagers
from google.cloud.chronicle_v1.types import dashboard_chart, native_dashboard
from google.cloud.chronicle_v1.types import dashboard_chart as gcc_dashboard_chart
from google.cloud.chronicle_v1.types import dashboard_query as gcc_dashboard_query
from google.cloud.chronicle_v1.types import native_dashboard as gcc_native_dashboard

from .client import NativeDashboardServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, NativeDashboardServiceTransport
from .transports.grpc_asyncio import NativeDashboardServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class NativeDashboardServiceAsyncClient:
    """A service providing functionality for managing native
    dashboards.
    """

    _client: NativeDashboardServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = NativeDashboardServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = NativeDashboardServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = NativeDashboardServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = NativeDashboardServiceClient._DEFAULT_UNIVERSE

    dashboard_chart_path = staticmethod(
        NativeDashboardServiceClient.dashboard_chart_path
    )
    parse_dashboard_chart_path = staticmethod(
        NativeDashboardServiceClient.parse_dashboard_chart_path
    )
    dashboard_query_path = staticmethod(
        NativeDashboardServiceClient.dashboard_query_path
    )
    parse_dashboard_query_path = staticmethod(
        NativeDashboardServiceClient.parse_dashboard_query_path
    )
    native_dashboard_path = staticmethod(
        NativeDashboardServiceClient.native_dashboard_path
    )
    parse_native_dashboard_path = staticmethod(
        NativeDashboardServiceClient.parse_native_dashboard_path
    )
    common_billing_account_path = staticmethod(
        NativeDashboardServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        NativeDashboardServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(NativeDashboardServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        NativeDashboardServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        NativeDashboardServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        NativeDashboardServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(NativeDashboardServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        NativeDashboardServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        NativeDashboardServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        NativeDashboardServiceClient.parse_common_location_path
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
            NativeDashboardServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            NativeDashboardServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(NativeDashboardServiceAsyncClient, info, *args, **kwargs)

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
            NativeDashboardServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            NativeDashboardServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            NativeDashboardServiceAsyncClient, filename, *args, **kwargs
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
        return NativeDashboardServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> NativeDashboardServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            NativeDashboardServiceTransport: The transport used by the client instance.
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

    get_transport_class = NativeDashboardServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                NativeDashboardServiceTransport,
                Callable[..., NativeDashboardServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the native dashboard service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,NativeDashboardServiceTransport,Callable[..., NativeDashboardServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the NativeDashboardServiceTransport constructor.
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
        self._client = NativeDashboardServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.chronicle_v1.NativeDashboardServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
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
                    "serviceName": "google.cloud.chronicle.v1.NativeDashboardService",
                    "credentialsType": None,
                },
            )

    async def create_native_dashboard(
        self,
        request: Optional[
            Union[gcc_native_dashboard.CreateNativeDashboardRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        native_dashboard: Optional[gcc_native_dashboard.NativeDashboard] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcc_native_dashboard.NativeDashboard:
        r"""Create a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_create_native_dashboard():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                native_dashboard = chronicle_v1.NativeDashboard()
                native_dashboard.display_name = "display_name_value"

                request = chronicle_v1.CreateNativeDashboardRequest(
                    parent="parent_value",
                    native_dashboard=native_dashboard,
                )

                # Make the request
                response = await client.create_native_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.CreateNativeDashboardRequest, dict]]):
                The request object. Request message to create a
                dashboard.
            parent (:class:`str`):
                Required. The parent resource where
                this dashboard will be created. Format:
                projects/{project}/locations/{location}/instances/{instance}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            native_dashboard (:class:`google.cloud.chronicle_v1.types.NativeDashboard`):
                Required. The dashboard to create.
                This corresponds to the ``native_dashboard`` field
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
            google.cloud.chronicle_v1.types.NativeDashboard:
                NativeDashboard resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, native_dashboard]
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
        if not isinstance(request, gcc_native_dashboard.CreateNativeDashboardRequest):
            request = gcc_native_dashboard.CreateNativeDashboardRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if native_dashboard is not None:
            request.native_dashboard = native_dashboard

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_native_dashboard
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

    async def get_native_dashboard(
        self,
        request: Optional[
            Union[native_dashboard.GetNativeDashboardRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> native_dashboard.NativeDashboard:
        r"""Get a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_get_native_dashboard():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                request = chronicle_v1.GetNativeDashboardRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_native_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.GetNativeDashboardRequest, dict]]):
                The request object. Request message to get a dashboard.
            name (:class:`str`):
                Required. The dashboard name to
                fetch. Format:

                projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}

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
            google.cloud.chronicle_v1.types.NativeDashboard:
                NativeDashboard resource.
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
        if not isinstance(request, native_dashboard.GetNativeDashboardRequest):
            request = native_dashboard.GetNativeDashboardRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_native_dashboard
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

    async def list_native_dashboards(
        self,
        request: Optional[
            Union[native_dashboard.ListNativeDashboardsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListNativeDashboardsAsyncPager:
        r"""List all dashboards.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_list_native_dashboards():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                request = chronicle_v1.ListNativeDashboardsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_native_dashboards(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.ListNativeDashboardsRequest, dict]]):
                The request object. Request message to list dashboards.
            parent (:class:`str`):
                Required. The parent owning this
                dashboard collection. Format:
                projects/{project}/locations/{location}/instances/{instance}

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
            google.cloud.chronicle_v1.services.native_dashboard_service.pagers.ListNativeDashboardsAsyncPager:
                Response message for listing
                dashboards.
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
        if not isinstance(request, native_dashboard.ListNativeDashboardsRequest):
            request = native_dashboard.ListNativeDashboardsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_native_dashboards
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
        response = pagers.ListNativeDashboardsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_native_dashboard(
        self,
        request: Optional[
            Union[gcc_native_dashboard.UpdateNativeDashboardRequest, dict]
        ] = None,
        *,
        native_dashboard: Optional[gcc_native_dashboard.NativeDashboard] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcc_native_dashboard.NativeDashboard:
        r"""Update a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_update_native_dashboard():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                native_dashboard = chronicle_v1.NativeDashboard()
                native_dashboard.display_name = "display_name_value"

                request = chronicle_v1.UpdateNativeDashboardRequest(
                    native_dashboard=native_dashboard,
                )

                # Make the request
                response = await client.update_native_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.UpdateNativeDashboardRequest, dict]]):
                The request object. Request message to update a
                dashboard.
            native_dashboard (:class:`google.cloud.chronicle_v1.types.NativeDashboard`):
                Required. The dashboard to update.

                The dashboard's ``name`` field is used to identify the
                dashboard to update. Format:
                projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}

                This corresponds to the ``native_dashboard`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. LINT.IfChange(update_mask_values) The list of
                fields to update. Supported paths are - display_name
                description definition.filters definition.charts type
                access dashboard_user_data.is_pinned

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
            google.cloud.chronicle_v1.types.NativeDashboard:
                NativeDashboard resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [native_dashboard, update_mask]
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
        if not isinstance(request, gcc_native_dashboard.UpdateNativeDashboardRequest):
            request = gcc_native_dashboard.UpdateNativeDashboardRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if native_dashboard is not None:
            request.native_dashboard = native_dashboard
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_native_dashboard
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("native_dashboard.name", request.native_dashboard.name),)
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

    async def duplicate_native_dashboard(
        self,
        request: Optional[
            Union[gcc_native_dashboard.DuplicateNativeDashboardRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        native_dashboard: Optional[gcc_native_dashboard.NativeDashboard] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcc_native_dashboard.NativeDashboard:
        r"""Duplicate a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_duplicate_native_dashboard():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                native_dashboard = chronicle_v1.NativeDashboard()
                native_dashboard.display_name = "display_name_value"

                request = chronicle_v1.DuplicateNativeDashboardRequest(
                    name="name_value",
                    native_dashboard=native_dashboard,
                )

                # Make the request
                response = await client.duplicate_native_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.DuplicateNativeDashboardRequest, dict]]):
                The request object. Request message to duplicate a
                dashboard.
            name (:class:`str`):
                Required. The dashboard name to
                duplicate. Format:

                projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            native_dashboard (:class:`google.cloud.chronicle_v1.types.NativeDashboard`):
                Required. Any fields that need
                modification can be passed through this
                like name, description etc.

                This corresponds to the ``native_dashboard`` field
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
            google.cloud.chronicle_v1.types.NativeDashboard:
                NativeDashboard resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, native_dashboard]
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
            request, gcc_native_dashboard.DuplicateNativeDashboardRequest
        ):
            request = gcc_native_dashboard.DuplicateNativeDashboardRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if native_dashboard is not None:
            request.native_dashboard = native_dashboard

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.duplicate_native_dashboard
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

    async def delete_native_dashboard(
        self,
        request: Optional[
            Union[native_dashboard.DeleteNativeDashboardRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_delete_native_dashboard():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                request = chronicle_v1.DeleteNativeDashboardRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_native_dashboard(request=request)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.DeleteNativeDashboardRequest, dict]]):
                The request object. Request message to delete a
                dashboard.
            name (:class:`str`):
                Required. The dashboard name to
                delete. Format:

                projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}

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
        if not isinstance(request, native_dashboard.DeleteNativeDashboardRequest):
            request = native_dashboard.DeleteNativeDashboardRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_native_dashboard
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

    async def add_chart(
        self,
        request: Optional[Union[native_dashboard.AddChartRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        dashboard_query: Optional[gcc_dashboard_query.DashboardQuery] = None,
        dashboard_chart: Optional[gcc_dashboard_chart.DashboardChart] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> native_dashboard.AddChartResponse:
        r"""Add chart in a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_add_chart():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                dashboard_chart = chronicle_v1.DashboardChart()
                dashboard_chart.display_name = "display_name_value"

                request = chronicle_v1.AddChartRequest(
                    name="name_value",
                    dashboard_chart=dashboard_chart,
                )

                # Make the request
                response = await client.add_chart(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.AddChartRequest, dict]]):
                The request object. Request message to add chart in a
                dashboard.
            name (:class:`str`):
                Required. The dashboard name to add
                chart in. Format:

                projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            dashboard_query (:class:`google.cloud.chronicle_v1.types.DashboardQuery`):
                Optional. Query used to create the
                chart.

                This corresponds to the ``dashboard_query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            dashboard_chart (:class:`google.cloud.chronicle_v1.types.DashboardChart`):
                Required. Chart to be added to the
                dashboard.

                This corresponds to the ``dashboard_chart`` field
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
            google.cloud.chronicle_v1.types.AddChartResponse:
                Response message for adding chart in
                a dashboard.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, dashboard_query, dashboard_chart]
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
        if not isinstance(request, native_dashboard.AddChartRequest):
            request = native_dashboard.AddChartRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if dashboard_query is not None:
            request.dashboard_query = dashboard_query
        if dashboard_chart is not None:
            request.dashboard_chart = dashboard_chart

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.add_chart
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

    async def remove_chart(
        self,
        request: Optional[Union[native_dashboard.RemoveChartRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> native_dashboard.NativeDashboard:
        r"""Remove chart from a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_remove_chart():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                request = chronicle_v1.RemoveChartRequest(
                    name="name_value",
                    dashboard_chart="dashboard_chart_value",
                )

                # Make the request
                response = await client.remove_chart(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.RemoveChartRequest, dict]]):
                The request object. Request message to remove chart from
                a dashboard.
            name (:class:`str`):
                Required. The dashboard name to
                remove chart from. Format:

                projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}

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
            google.cloud.chronicle_v1.types.NativeDashboard:
                NativeDashboard resource.
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
        if not isinstance(request, native_dashboard.RemoveChartRequest):
            request = native_dashboard.RemoveChartRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.remove_chart
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

    async def edit_chart(
        self,
        request: Optional[Union[native_dashboard.EditChartRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        dashboard_query: Optional[gcc_dashboard_query.DashboardQuery] = None,
        dashboard_chart: Optional[gcc_dashboard_chart.DashboardChart] = None,
        edit_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> native_dashboard.EditChartResponse:
        r"""Edit chart in a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_edit_chart():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                request = chronicle_v1.EditChartRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.edit_chart(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.EditChartRequest, dict]]):
                The request object. Request message to edit chart in a
                dashboard.
            name (:class:`str`):
                Required. The dashboard name to edit
                chart in. Format:

                projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            dashboard_query (:class:`google.cloud.chronicle_v1.types.DashboardQuery`):
                Optional. Query for the edited chart.
                This corresponds to the ``dashboard_query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            dashboard_chart (:class:`google.cloud.chronicle_v1.types.DashboardChart`):
                Optional. Edited chart.
                This corresponds to the ``dashboard_chart`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            edit_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to edit for chart and
                query. Supported paths in chart are -
                dashboard_chart.display_name dashboard_chart.description
                dashboard_chart.chart_datasource.data_sources
                dashboard_chart.visualization
                dashboard_chart.visualization.button
                dashboard_chart.visualization.markdown
                dashboard_chart.drill_down_config Supported paths in
                query are - dashboard_query.query dashboard_query.input

                This corresponds to the ``edit_mask`` field
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
            google.cloud.chronicle_v1.types.EditChartResponse:
                Response message for editing chart in
                a dashboard.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, dashboard_query, dashboard_chart, edit_mask]
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
        if not isinstance(request, native_dashboard.EditChartRequest):
            request = native_dashboard.EditChartRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if dashboard_query is not None:
            request.dashboard_query = dashboard_query
        if dashboard_chart is not None:
            request.dashboard_chart = dashboard_chart
        if edit_mask is not None:
            request.edit_mask = edit_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.edit_chart
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

    async def duplicate_chart(
        self,
        request: Optional[Union[native_dashboard.DuplicateChartRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> native_dashboard.DuplicateChartResponse:
        r"""Duplicate chart in a dashboard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_duplicate_chart():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                request = chronicle_v1.DuplicateChartRequest(
                    name="name_value",
                    dashboard_chart="dashboard_chart_value",
                )

                # Make the request
                response = await client.duplicate_chart(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.DuplicateChartRequest, dict]]):
                The request object. Request message to duplicate chart in
                a dashboard.
            name (:class:`str`):
                Required. The dashboard name that
                involves chart duplication. Format:

                projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}

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
            google.cloud.chronicle_v1.types.DuplicateChartResponse:
                Response message for duplicating
                chart in a dashboard.

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
        if not isinstance(request, native_dashboard.DuplicateChartRequest):
            request = native_dashboard.DuplicateChartRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.duplicate_chart
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

    async def export_native_dashboards(
        self,
        request: Optional[
            Union[native_dashboard.ExportNativeDashboardsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> native_dashboard.ExportNativeDashboardsResponse:
        r"""Exports the dashboards.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_export_native_dashboards():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                request = chronicle_v1.ExportNativeDashboardsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = await client.export_native_dashboards(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.ExportNativeDashboardsRequest, dict]]):
                The request object. Request message to export list of
                dashboard.
            parent (:class:`str`):
                Required. The parent resource that
                the dashboards to be exported belong to.
                Format:
                projects/{project}/locations/{location}/instances/{instance}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (:class:`MutableSequence[str]`):
                Required. The resource names of the
                dashboards to export.

                This corresponds to the ``names`` field
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
            google.cloud.chronicle_v1.types.ExportNativeDashboardsResponse:
                Response message for exporting a
                dashboard.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, native_dashboard.ExportNativeDashboardsRequest):
            request = native_dashboard.ExportNativeDashboardsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if names:
            request.names.extend(names)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_native_dashboards
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

    async def import_native_dashboards(
        self,
        request: Optional[
            Union[native_dashboard.ImportNativeDashboardsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        source: Optional[native_dashboard.ImportNativeDashboardsInlineSource] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> native_dashboard.ImportNativeDashboardsResponse:
        r"""Imports the dashboards.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import chronicle_v1

            async def sample_import_native_dashboards():
                # Create a client
                client = chronicle_v1.NativeDashboardServiceAsyncClient()

                # Initialize request argument(s)
                request = chronicle_v1.ImportNativeDashboardsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.import_native_dashboards(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.chronicle_v1.types.ImportNativeDashboardsRequest, dict]]):
                The request object. Request message to import dashboards.
            parent (:class:`str`):
                Required. The parent resource where
                this dashboard will be created. Format:
                projects/{project}/locations/{location}/instances/{instance}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            source (:class:`google.cloud.chronicle_v1.types.ImportNativeDashboardsInlineSource`):
                Required. The data will imported from
                this proto.

                This corresponds to the ``source`` field
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
            google.cloud.chronicle_v1.types.ImportNativeDashboardsResponse:
                Response message for importing
                dashboards.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, source]
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
        if not isinstance(request, native_dashboard.ImportNativeDashboardsRequest):
            request = native_dashboard.ImportNativeDashboardsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if source is not None:
            request.source = source

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.import_native_dashboards
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

    async def delete_operation(
        self,
        request: Optional[Union[operations_pb2.DeleteOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a long-running operation.

        This method indicates that the client is no longer interested
        in the operation result. It does not cancel the operation.
        If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.DeleteOperationRequest`):
                The request object. Request message for
                `DeleteOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.DeleteOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.DeleteOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.delete_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def cancel_operation(
        self,
        request: Optional[Union[operations_pb2.CancelOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.CancelOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.CancelOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self) -> "NativeDashboardServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("NativeDashboardServiceAsyncClient",)
