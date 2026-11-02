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

from google.devicesandservices.health_v4 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore

from google.devicesandservices.health_v4.services.data_points_service import pagers
from google.devicesandservices.health_v4.types import (
    data_model,
    data_points,
    data_source,
)

from .client import DataPointsServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DataPointsServiceTransport
from .transports.grpc_asyncio import DataPointsServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DataPointsServiceAsyncClient:
    """Data Points Service exposing the user's health and fitness
    measured and derived data.
    """

    _client: DataPointsServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DataPointsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataPointsServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DataPointsServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DataPointsServiceClient._DEFAULT_UNIVERSE

    data_point_path = staticmethod(DataPointsServiceClient.data_point_path)
    parse_data_point_path = staticmethod(DataPointsServiceClient.parse_data_point_path)
    data_type_path = staticmethod(DataPointsServiceClient.data_type_path)
    parse_data_type_path = staticmethod(DataPointsServiceClient.parse_data_type_path)
    common_billing_account_path = staticmethod(
        DataPointsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DataPointsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DataPointsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DataPointsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DataPointsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DataPointsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DataPointsServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DataPointsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DataPointsServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DataPointsServiceClient.parse_common_location_path
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
            DataPointsServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            DataPointsServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DataPointsServiceAsyncClient, info, *args, **kwargs)

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
            DataPointsServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            DataPointsServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DataPointsServiceAsyncClient, filename, *args, **kwargs)

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
        return DataPointsServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DataPointsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataPointsServiceTransport: The transport used by the client instance.
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

    get_transport_class = DataPointsServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                DataPointsServiceTransport,
                Callable[..., DataPointsServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the data points service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DataPointsServiceTransport,Callable[..., DataPointsServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DataPointsServiceTransport constructor.
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
        self._client = DataPointsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.devicesandservices.health_v4.DataPointsServiceAsyncClient`.",
                extra={
                    "serviceName": "google.devicesandservices.health.v4.DataPointsService",
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
                    "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                    "credentialsType": None,
                },
            )

    async def get_data_point(
        self,
        request: Optional[Union[data_points.GetDataPointRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> data_points.DataPoint:
        r"""Get a single identifyable data point.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_get_data_point():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.GetDataPointRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_data_point(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.GetDataPointRequest, dict]]):
                The request object. Request for getting a single data
                point
            name (:class:`str`):
                Required. The name of the data point to retrieve.

                Format:
                ``users/{user}/dataTypes/{data_type}/dataPoints/{data_point}``

                See
                [DataPoint.name][google.devicesandservices.health.v4.DataPoint.name]
                for examples and possible values.

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
            google.devicesandservices.health_v4.types.DataPoint:
                A computed or recorded metric.
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
        if not isinstance(request, data_points.GetDataPointRequest):
            request = data_points.GetDataPointRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_data_point
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

    async def list_data_points(
        self,
        request: Optional[Union[data_points.ListDataPointsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDataPointsAsyncPager:
        r"""Query user health and fitness data points.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_list_data_points():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.ListDataPointsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_data_points(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.ListDataPointsRequest, dict]]):
                The request object. Request for listing raw data points
            parent (:class:`str`):
                Required. Parent data type of the Data Point collection.

                Format: ``users/me/dataTypes/{data_type}``, e.g.:

                - ``users/me/dataTypes/steps``
                - ``users/me/dataTypes/weight``

                For a list of the supported data types see the
                [DataPoint
                data][google.devicesandservices.health.v4.DataPoint]
                union field.

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
            google.devicesandservices.health_v4.services.data_points_service.pagers.ListDataPointsAsyncPager:
                Response containing raw data points
                matching the query
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
        if not isinstance(request, data_points.ListDataPointsRequest):
            request = data_points.ListDataPointsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_data_points
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
        response = pagers.ListDataPointsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_data_point(
        self,
        request: Optional[Union[data_points.CreateDataPointRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        data_point: Optional[data_points.DataPoint] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a single identifiable data point.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_create_data_point():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.CreateDataPointRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = await client.create_data_point(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.CreateDataPointRequest, dict]]):
                The request object. Request to create an identifiable
                data point.
            parent (:class:`str`):
                Required. The parent resource name where the data point
                will be created. Format:
                ``users/{user}/dataTypes/{data_type}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            data_point (:class:`google.devicesandservices.health_v4.types.DataPoint`):
                Required. The data point to create.
                This corresponds to the ``data_point`` field
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
                :class:`google.devicesandservices.health_v4.types.DataPoint`
                A computed or recorded metric.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, data_point]
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
        if not isinstance(request, data_points.CreateDataPointRequest):
            request = data_points.CreateDataPointRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if data_point is not None:
            request.data_point = data_point

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_data_point
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
            data_points.DataPoint,
            metadata_type=data_points.CreateDataPointOperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_data_point(
        self,
        request: Optional[Union[data_points.UpdateDataPointRequest, dict]] = None,
        *,
        data_point: Optional[data_points.DataPoint] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates a single identifiable data point. If a data point with
        the specified ``name`` is not found, the request will fail.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_update_data_point():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.UpdateDataPointRequest(
                )

                # Make the request
                operation = await client.update_data_point(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.UpdateDataPointRequest, dict]]):
                The request object. Request to update an identifiable
                data point.
            data_point (:class:`google.devicesandservices.health_v4.types.DataPoint`):
                Required. The data point to update

                The data point's ``name`` field is used to identify the
                data point to update.

                Format:
                ``users/{user}/dataTypes/{data_type}/dataPoints/{data_point}``

                This corresponds to the ``data_point`` field
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
                :class:`google.devicesandservices.health_v4.types.DataPoint`
                A computed or recorded metric.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [data_point]
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
        if not isinstance(request, data_points.UpdateDataPointRequest):
            request = data_points.UpdateDataPointRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if data_point is not None:
            request.data_point = data_point

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_data_point
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("data_point.name", request.data_point.name),)
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
            data_points.DataPoint,
            metadata_type=data_points.UpdateDataPointOperationMetadata,
        )

        # Done; return the response.
        return response

    async def batch_delete_data_points(
        self,
        request: Optional[Union[data_points.BatchDeleteDataPointsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Delete a batch of identifyable data points.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_batch_delete_data_points():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.BatchDeleteDataPointsRequest(
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                operation = await client.batch_delete_data_points(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.BatchDeleteDataPointsRequest, dict]]):
                The request object. Request to delete a batch of
                identifiable data points.
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
                :class:`google.devicesandservices.health_v4.types.BatchDeleteDataPointsResponse`
                Response containing the list of possibly soft-deleted
                DataPoints.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, data_points.BatchDeleteDataPointsRequest):
            request = data_points.BatchDeleteDataPointsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_delete_data_points
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
            data_points.BatchDeleteDataPointsResponse,
            metadata_type=data_points.BatchDeleteDataPointsOperationMetadata,
        )

        # Done; return the response.
        return response

    async def reconcile_data_points(
        self,
        request: Optional[Union[data_points.ReconcileDataPointsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ReconcileDataPointsAsyncPager:
        r"""Reconcile data points from multiple data sources into
        a single data stream.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_reconcile_data_points():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.ReconcileDataPointsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.reconcile_data_points(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.ReconcileDataPointsRequest, dict]]):
                The request object. Request to reconcile data points from
                multiple data sources.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.devicesandservices.health_v4.services.data_points_service.pagers.ReconcileDataPointsAsyncPager:
                Response containing the list of
                reconciled DataPoints.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, data_points.ReconcileDataPointsRequest):
            request = data_points.ReconcileDataPointsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reconcile_data_points
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
        response = pagers.ReconcileDataPointsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def roll_up_data_points(
        self,
        request: Optional[Union[data_points.RollUpDataPointsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.RollUpDataPointsAsyncPager:
        r"""Roll up data points over physical time intervals for
        supported data types.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_roll_up_data_points():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.RollUpDataPointsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.roll_up_data_points(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.RollUpDataPointsRequest, dict]]):
                The request object. Request to roll up data points by
                physical time intervals.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.devicesandservices.health_v4.services.data_points_service.pagers.RollUpDataPointsAsyncPager:
                Response containing the list of
                rolled up data points.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, data_points.RollUpDataPointsRequest):
            request = data_points.RollUpDataPointsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.roll_up_data_points
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
        response = pagers.RollUpDataPointsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def daily_roll_up_data_points(
        self,
        request: Optional[Union[data_points.DailyRollUpDataPointsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> data_points.DailyRollUpDataPointsResponse:
        r"""Roll up data points over civil time intervals for
        supported data types.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_daily_roll_up_data_points():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.DailyRollUpDataPointsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.daily_roll_up_data_points(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.DailyRollUpDataPointsRequest, dict]]):
                The request object. Request to roll up data points by
                civil time intervals.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.devicesandservices.health_v4.types.DailyRollUpDataPointsResponse:
                Response containing the list of
                rolled up data points.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, data_points.DailyRollUpDataPointsRequest):
            request = data_points.DailyRollUpDataPointsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.daily_roll_up_data_points
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

    async def export_exercise_tcx(
        self,
        request: Optional[Union[data_points.ExportExerciseTcxRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> data_points.ExportExerciseTcxResponse:
        r"""Exports exercise data in TCX format.

        **IMPORTANT:** HTTP clients must append ``?alt=media`` to the
        request URL to download the raw TCX file.

        Example:
        ``https://health.googleapis.com/v4/users/me/dataTypes/exercise/dataPoints/EXERCISE_ID:exportExerciseTcx?alt=media``

        Without ``alt=media``, the server returns a JSON response
        (``ExportExerciseTcxResponse``) which is intended primarily for
        gRPC clients.

        **Note:** While the Authorization section below states that any
        one of the listed scopes is accepted, this specific method
        requires the user to provide both one of the
        ``activity_and_fitness`` scopes (``normal`` or ``readonly``) AND
        one of the ``location`` scopes (``normal`` or ``readonly``) in
        their access token to succeed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_export_exercise_tcx():
                # Create a client
                client = health_v4.DataPointsServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.ExportExerciseTcxRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.export_exercise_tcx(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.ExportExerciseTcxRequest, dict]]):
                The request object. Represents a request to export
                exercise data in TCX format.
            name (:class:`str`):
                Required. The resource name of the exercise data point
                to export.

                Format:
                ``users/{user}/dataTypes/exercise/dataPoints/{data_point}``
                Example:
                ``users/me/dataTypes/exercise/dataPoints/2026443605080188808``

                The ``{user}`` is the alias ``"me"`` currently. Future
                versions may support user IDs. The ``{data_point}`` ID
                maps to the exercise ID, which is a long integer.

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
            google.devicesandservices.health_v4.types.ExportExerciseTcxResponse:
                Represents a Response for exporting
                exercise data in TCX format.

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
        if not isinstance(request, data_points.ExportExerciseTcxRequest):
            request = data_points.ExportExerciseTcxRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_exercise_tcx
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

    async def __aenter__(self) -> "DataPointsServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DataPointsServiceAsyncClient",)
