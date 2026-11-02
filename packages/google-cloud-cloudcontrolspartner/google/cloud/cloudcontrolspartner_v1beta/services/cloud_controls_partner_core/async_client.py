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
import warnings
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

from google.cloud.cloudcontrolspartner_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.cloudcontrolspartner_v1beta.services.cloud_controls_partner_core import (
    pagers,
)
from google.cloud.cloudcontrolspartner_v1beta.types import (
    access_approval_requests,
    customer_workloads,
    customers,
    ekm_connections,
    partner_permissions,
    partners,
)

from .client import CloudControlsPartnerCoreClient
from .transports.base import DEFAULT_CLIENT_INFO, CloudControlsPartnerCoreTransport
from .transports.grpc_asyncio import CloudControlsPartnerCoreGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class CloudControlsPartnerCoreAsyncClient:
    """Service describing handlers for resources"""

    _client: CloudControlsPartnerCoreClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = CloudControlsPartnerCoreClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CloudControlsPartnerCoreClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        CloudControlsPartnerCoreClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = CloudControlsPartnerCoreClient._DEFAULT_UNIVERSE

    access_approval_request_path = staticmethod(
        CloudControlsPartnerCoreClient.access_approval_request_path
    )
    parse_access_approval_request_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_access_approval_request_path
    )
    customer_path = staticmethod(CloudControlsPartnerCoreClient.customer_path)
    parse_customer_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_customer_path
    )
    ekm_connections_path = staticmethod(
        CloudControlsPartnerCoreClient.ekm_connections_path
    )
    parse_ekm_connections_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_ekm_connections_path
    )
    partner_path = staticmethod(CloudControlsPartnerCoreClient.partner_path)
    parse_partner_path = staticmethod(CloudControlsPartnerCoreClient.parse_partner_path)
    partner_permissions_path = staticmethod(
        CloudControlsPartnerCoreClient.partner_permissions_path
    )
    parse_partner_permissions_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_partner_permissions_path
    )
    workload_path = staticmethod(CloudControlsPartnerCoreClient.workload_path)
    parse_workload_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_workload_path
    )
    common_billing_account_path = staticmethod(
        CloudControlsPartnerCoreClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(CloudControlsPartnerCoreClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        CloudControlsPartnerCoreClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        CloudControlsPartnerCoreClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        CloudControlsPartnerCoreClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        CloudControlsPartnerCoreClient.parse_common_location_path
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
            CloudControlsPartnerCoreAsyncClient: The constructed client.
        """
        sa_info_func = (
            CloudControlsPartnerCoreClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(CloudControlsPartnerCoreAsyncClient, info, *args, **kwargs)

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
            CloudControlsPartnerCoreAsyncClient: The constructed client.
        """
        sa_file_func = (
            CloudControlsPartnerCoreClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            CloudControlsPartnerCoreAsyncClient, filename, *args, **kwargs
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
        return CloudControlsPartnerCoreClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> CloudControlsPartnerCoreTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudControlsPartnerCoreTransport: The transport used by the client instance.
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

    get_transport_class = CloudControlsPartnerCoreClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                CloudControlsPartnerCoreTransport,
                Callable[..., CloudControlsPartnerCoreTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud controls partner core async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CloudControlsPartnerCoreTransport,Callable[..., CloudControlsPartnerCoreTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CloudControlsPartnerCoreTransport constructor.
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
        self._client = CloudControlsPartnerCoreClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
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
                    "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                    "credentialsType": None,
                },
            )

    async def get_workload(
        self,
        request: Optional[Union[customer_workloads.GetWorkloadRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> customer_workloads.Workload:
        r"""Gets details of a single workload

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_get_workload():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.GetWorkloadRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_workload(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.GetWorkloadRequest, dict]]):
                The request object. Message for getting a customer
                workload.
            name (:class:`str`):
                Required. Format:
                ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}``

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
            google.cloud.cloudcontrolspartner_v1beta.types.Workload:
                Contains metadata around the [Workload
                   resource](https://cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/Workload)
                   in the Assured Workloads API.

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
        if not isinstance(request, customer_workloads.GetWorkloadRequest):
            request = customer_workloads.GetWorkloadRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_workload
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

    async def list_workloads(
        self,
        request: Optional[Union[customer_workloads.ListWorkloadsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListWorkloadsAsyncPager:
        r"""Lists customer workloads for a given customer org id

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_list_workloads():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.ListWorkloadsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_workloads(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.ListWorkloadsRequest, dict]]):
                The request object. Request to list customer workloads.
            parent (:class:`str`):
                Required. Parent resource Format:
                ``organizations/{organization}/locations/{location}/customers/{customer}``

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
            google.cloud.cloudcontrolspartner_v1beta.services.cloud_controls_partner_core.pagers.ListWorkloadsAsyncPager:
                Response message for list customer
                workloads requests.
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
        if not isinstance(request, customer_workloads.ListWorkloadsRequest):
            request = customer_workloads.ListWorkloadsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_workloads
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
        response = pagers.ListWorkloadsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_customer(
        self,
        request: Optional[Union[customers.GetCustomerRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> customers.Customer:
        r"""Gets details of a single customer

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_get_customer():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.GetCustomerRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_customer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.GetCustomerRequest, dict]]):
                The request object. Message for getting a customer
            name (:class:`str`):
                Required. Format:
                ``organizations/{organization}/locations/{location}/customers/{customer}``

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
            google.cloud.cloudcontrolspartner_v1beta.types.Customer:
                Contains metadata around a Cloud
                Controls Partner Customer

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
        if not isinstance(request, customers.GetCustomerRequest):
            request = customers.GetCustomerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_customer
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

    async def list_customers(
        self,
        request: Optional[Union[customers.ListCustomersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListCustomersAsyncPager:
        r"""Lists customers of a partner identified by its Google
        Cloud organization ID

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_list_customers():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.ListCustomersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_customers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.ListCustomersRequest, dict]]):
                The request object. Request to list customers
            parent (:class:`str`):
                Required. Parent resource Format:
                ``organizations/{organization}/locations/{location}``

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
            google.cloud.cloudcontrolspartner_v1beta.services.cloud_controls_partner_core.pagers.ListCustomersAsyncPager:
                Response message for list customer
                Customers requests
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
        if not isinstance(request, customers.ListCustomersRequest):
            request = customers.ListCustomersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_customers
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
        response = pagers.ListCustomersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_ekm_connections(
        self,
        request: Optional[Union[ekm_connections.GetEkmConnectionsRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ekm_connections.EkmConnections:
        r"""Gets the EKM connections associated with a workload

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_get_ekm_connections():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.GetEkmConnectionsRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_ekm_connections(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.GetEkmConnectionsRequest, dict]]):
                The request object. Request for getting the EKM
                connections associated with a workload
            name (:class:`str`):
                Required. Format:
                ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections``

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
            google.cloud.cloudcontrolspartner_v1beta.types.EkmConnections:
                The EKM connections associated with a
                workload

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
        if not isinstance(request, ekm_connections.GetEkmConnectionsRequest):
            request = ekm_connections.GetEkmConnectionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_ekm_connections
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

    async def get_partner_permissions(
        self,
        request: Optional[
            Union[partner_permissions.GetPartnerPermissionsRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> partner_permissions.PartnerPermissions:
        r"""Gets the partner permissions granted for a workload

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_get_partner_permissions():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.GetPartnerPermissionsRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_partner_permissions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.GetPartnerPermissionsRequest, dict]]):
                The request object. Request for getting the partner
                permissions granted for a workload
            name (:class:`str`):
                Required. Name of the resource to get in the format:
                ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions``

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
            google.cloud.cloudcontrolspartner_v1beta.types.PartnerPermissions:
                The permissions granted to the
                partner for a workload

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
        if not isinstance(request, partner_permissions.GetPartnerPermissionsRequest):
            request = partner_permissions.GetPartnerPermissionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_partner_permissions
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

    async def list_access_approval_requests(
        self,
        request: Optional[
            Union[access_approval_requests.ListAccessApprovalRequestsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAccessApprovalRequestsAsyncPager:
        r"""Deprecated: Only returns access approval requests
        directly associated with an assured workload folder.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_list_access_approval_requests():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.ListAccessApprovalRequestsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_access_approval_requests(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.ListAccessApprovalRequestsRequest, dict]]):
                The request object. Request for getting the access
                requests associated with a workload.
            parent (:class:`str`):
                Required. Parent resource Format:
                ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}``

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
            google.cloud.cloudcontrolspartner_v1beta.services.cloud_controls_partner_core.pagers.ListAccessApprovalRequestsAsyncPager:
                Response message for list access
                requests.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        warnings.warn(
            "CloudControlsPartnerCoreAsyncClient.list_access_approval_requests is deprecated",
            DeprecationWarning,
        )

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
            request, access_approval_requests.ListAccessApprovalRequestsRequest
        ):
            request = access_approval_requests.ListAccessApprovalRequestsRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_access_approval_requests
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
        response = pagers.ListAccessApprovalRequestsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_partner(
        self,
        request: Optional[Union[partners.GetPartnerRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> partners.Partner:
        r"""Get details of a Partner.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_get_partner():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.GetPartnerRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_partner(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.GetPartnerRequest, dict]]):
                The request object. Message for getting a Partner
            name (:class:`str`):
                Required. Format:
                ``organizations/{organization}/locations/{location}/partner``

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
            google.cloud.cloudcontrolspartner_v1beta.types.Partner:
                Message describing Partner resource
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
        if not isinstance(request, partners.GetPartnerRequest):
            request = partners.GetPartnerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_partner
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

    async def create_customer(
        self,
        request: Optional[Union[customers.CreateCustomerRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        customer: Optional[customers.Customer] = None,
        customer_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> customers.Customer:
        r"""Creates a new customer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_create_customer():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                customer = cloudcontrolspartner_v1beta.Customer()
                customer.display_name = "display_name_value"

                request = cloudcontrolspartner_v1beta.CreateCustomerRequest(
                    parent="parent_value",
                    customer=customer,
                    customer_id="customer_id_value",
                )

                # Make the request
                response = await client.create_customer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.CreateCustomerRequest, dict]]):
                The request object. Request to create a customer
            parent (:class:`str`):
                Required. Parent resource Format:
                ``organizations/{organization}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            customer (:class:`google.cloud.cloudcontrolspartner_v1beta.types.Customer`):
                Required. The customer to create.
                This corresponds to the ``customer`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            customer_id (:class:`str`):
                Required. The customer id to use for
                the customer, which will become the
                final component of the customer's
                resource name. The specified value must
                be a valid Google cloud organization id.

                This corresponds to the ``customer_id`` field
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
            google.cloud.cloudcontrolspartner_v1beta.types.Customer:
                Contains metadata around a Cloud
                Controls Partner Customer

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, customer, customer_id]
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
        if not isinstance(request, customers.CreateCustomerRequest):
            request = customers.CreateCustomerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if customer is not None:
            request.customer = customer
        if customer_id is not None:
            request.customer_id = customer_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_customer
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

    async def update_customer(
        self,
        request: Optional[Union[customers.UpdateCustomerRequest, dict]] = None,
        *,
        customer: Optional[customers.Customer] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> customers.Customer:
        r"""Update details of a single customer

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_update_customer():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                customer = cloudcontrolspartner_v1beta.Customer()
                customer.display_name = "display_name_value"

                request = cloudcontrolspartner_v1beta.UpdateCustomerRequest(
                    customer=customer,
                )

                # Make the request
                response = await client.update_customer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.UpdateCustomerRequest, dict]]):
                The request object. Request to update a customer
            customer (:class:`google.cloud.cloudcontrolspartner_v1beta.types.Customer`):
                Required. The customer to update Format:
                ``organizations/{organization}/locations/{location}/customers/{customer}``

                This corresponds to the ``customer`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to
                update

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
            google.cloud.cloudcontrolspartner_v1beta.types.Customer:
                Contains metadata around a Cloud
                Controls Partner Customer

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [customer, update_mask]
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
        if not isinstance(request, customers.UpdateCustomerRequest):
            request = customers.UpdateCustomerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if customer is not None:
            request.customer = customer
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_customer
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("customer.name", request.customer.name),)
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

    async def delete_customer(
        self,
        request: Optional[Union[customers.DeleteCustomerRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete details of a single customer

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1beta

            async def sample_delete_customer():
                # Create a client
                client = cloudcontrolspartner_v1beta.CloudControlsPartnerCoreAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1beta.DeleteCustomerRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_customer(request=request)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1beta.types.DeleteCustomerRequest, dict]]):
                The request object. Message for deleting customer
            name (:class:`str`):
                Required. name of the resource to be deleted format:
                name=organizations/*/locations/*/customers/\*

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
        if not isinstance(request, customers.DeleteCustomerRequest):
            request = customers.DeleteCustomerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_customer
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

    async def __aenter__(self) -> "CloudControlsPartnerCoreAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("CloudControlsPartnerCoreAsyncClient",)
