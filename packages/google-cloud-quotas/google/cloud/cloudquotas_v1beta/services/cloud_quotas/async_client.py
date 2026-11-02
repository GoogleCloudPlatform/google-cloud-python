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

from google.cloud.cloudquotas_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.cloudquotas_v1beta.services.cloud_quotas import pagers
from google.cloud.cloudquotas_v1beta.types import cloudquotas, resources

from .client import CloudQuotasClient
from .transports.base import DEFAULT_CLIENT_INFO, CloudQuotasTransport
from .transports.grpc_asyncio import CloudQuotasGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class CloudQuotasAsyncClient:
    """The Cloud Quotas API is an infrastructure service for Google
    Cloud that lets service consumers list and manage their resource
    usage limits.

    - List/Get the metadata and current status of the quotas for a
      service.
    - Create/Update quota preferencess that declare the preferred
      quota values.
    - Check the status of a quota preference request.
    - List/Get pending and historical quota preference.
    """

    _client: CloudQuotasClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = CloudQuotasClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CloudQuotasClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = CloudQuotasClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = CloudQuotasClient._DEFAULT_UNIVERSE

    quota_info_path = staticmethod(CloudQuotasClient.quota_info_path)
    parse_quota_info_path = staticmethod(CloudQuotasClient.parse_quota_info_path)
    quota_preference_path = staticmethod(CloudQuotasClient.quota_preference_path)
    parse_quota_preference_path = staticmethod(
        CloudQuotasClient.parse_quota_preference_path
    )
    common_billing_account_path = staticmethod(
        CloudQuotasClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CloudQuotasClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(CloudQuotasClient.common_folder_path)
    parse_common_folder_path = staticmethod(CloudQuotasClient.parse_common_folder_path)
    common_organization_path = staticmethod(CloudQuotasClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        CloudQuotasClient.parse_common_organization_path
    )
    common_project_path = staticmethod(CloudQuotasClient.common_project_path)
    parse_common_project_path = staticmethod(
        CloudQuotasClient.parse_common_project_path
    )
    common_location_path = staticmethod(CloudQuotasClient.common_location_path)
    parse_common_location_path = staticmethod(
        CloudQuotasClient.parse_common_location_path
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
            CloudQuotasAsyncClient: The constructed client.
        """
        sa_info_func = (
            CloudQuotasClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(CloudQuotasAsyncClient, info, *args, **kwargs)

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
            CloudQuotasAsyncClient: The constructed client.
        """
        sa_file_func = (
            CloudQuotasClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(CloudQuotasAsyncClient, filename, *args, **kwargs)

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
        return CloudQuotasClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> CloudQuotasTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudQuotasTransport: The transport used by the client instance.
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

    get_transport_class = CloudQuotasClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, CloudQuotasTransport, Callable[..., CloudQuotasTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud quotas async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CloudQuotasTransport,Callable[..., CloudQuotasTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CloudQuotasTransport constructor.
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
        self._client = CloudQuotasClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.api.cloudquotas_v1beta.CloudQuotasAsyncClient`.",
                extra={
                    "serviceName": "google.api.cloudquotas.v1beta.CloudQuotas",
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
                    "serviceName": "google.api.cloudquotas.v1beta.CloudQuotas",
                    "credentialsType": None,
                },
            )

    async def list_quota_infos(
        self,
        request: Optional[Union[cloudquotas.ListQuotaInfosRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListQuotaInfosAsyncPager:
        r"""Lists QuotaInfos of all quotas for a given project,
        folder or organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudquotas_v1beta

            async def sample_list_quota_infos():
                # Create a client
                client = cloudquotas_v1beta.CloudQuotasAsyncClient()

                # Initialize request argument(s)
                request = cloudquotas_v1beta.ListQuotaInfosRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_quota_infos(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.cloudquotas_v1beta.types.ListQuotaInfosRequest, dict]]):
                The request object. Message for requesting list of
                QuotaInfos
            parent (:class:`str`):
                Required. Parent value of QuotaInfo resources. Listing
                across different resource containers (such as
                'projects/-') is not allowed.

                Example names:
                ``projects/123/locations/global/services/compute.googleapis.com``
                ``folders/234/locations/global/services/compute.googleapis.com``
                ``organizations/345/locations/global/services/compute.googleapis.com``

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
            google.cloud.cloudquotas_v1beta.services.cloud_quotas.pagers.ListQuotaInfosAsyncPager:
                Message for response to listing
                QuotaInfos
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
        if not isinstance(request, cloudquotas.ListQuotaInfosRequest):
            request = cloudquotas.ListQuotaInfosRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_quota_infos
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
        response = pagers.ListQuotaInfosAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_quota_info(
        self,
        request: Optional[Union[cloudquotas.GetQuotaInfoRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QuotaInfo:
        r"""Retrieve the QuotaInfo of a quota for a project,
        folder or organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudquotas_v1beta

            async def sample_get_quota_info():
                # Create a client
                client = cloudquotas_v1beta.CloudQuotasAsyncClient()

                # Initialize request argument(s)
                request = cloudquotas_v1beta.GetQuotaInfoRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_quota_info(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudquotas_v1beta.types.GetQuotaInfoRequest, dict]]):
                The request object. Message for getting a QuotaInfo
            name (:class:`str`):
                Required. The resource name of the quota info.

                An example name:
                ``projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion``

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
            google.cloud.cloudquotas_v1beta.types.QuotaInfo:
                QuotaInfo represents information
                about a particular quota for a given
                project, folder or organization.

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
        if not isinstance(request, cloudquotas.GetQuotaInfoRequest):
            request = cloudquotas.GetQuotaInfoRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_quota_info
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

    async def list_quota_preferences(
        self,
        request: Optional[Union[cloudquotas.ListQuotaPreferencesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListQuotaPreferencesAsyncPager:
        r"""Lists QuotaPreferences in a given project, folder or
        organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudquotas_v1beta

            async def sample_list_quota_preferences():
                # Create a client
                client = cloudquotas_v1beta.CloudQuotasAsyncClient()

                # Initialize request argument(s)
                request = cloudquotas_v1beta.ListQuotaPreferencesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_quota_preferences(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.cloudquotas_v1beta.types.ListQuotaPreferencesRequest, dict]]):
                The request object. Message for requesting list of
                QuotaPreferences
            parent (:class:`str`):
                Required. Parent value of QuotaPreference resources.
                Listing across different resource containers (such as
                'projects/-') is not allowed.

                When the value starts with 'folders' or 'organizations',
                it lists the QuotaPreferences for org quotas in the
                container. It does not list the QuotaPreferences in the
                descendant projects of the container.

                Example parents: ``projects/123/locations/global``

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
            google.cloud.cloudquotas_v1beta.services.cloud_quotas.pagers.ListQuotaPreferencesAsyncPager:
                Message for response to listing
                QuotaPreferences
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
        if not isinstance(request, cloudquotas.ListQuotaPreferencesRequest):
            request = cloudquotas.ListQuotaPreferencesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_quota_preferences
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
        response = pagers.ListQuotaPreferencesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_quota_preference(
        self,
        request: Optional[Union[cloudquotas.GetQuotaPreferenceRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QuotaPreference:
        r"""Gets details of a single QuotaPreference.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudquotas_v1beta

            async def sample_get_quota_preference():
                # Create a client
                client = cloudquotas_v1beta.CloudQuotasAsyncClient()

                # Initialize request argument(s)
                request = cloudquotas_v1beta.GetQuotaPreferenceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_quota_preference(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudquotas_v1beta.types.GetQuotaPreferenceRequest, dict]]):
                The request object. Message for getting a QuotaPreference
            name (:class:`str`):
                Required. Name of the resource

                Example name:
                ``projects/123/locations/global/quota_preferences/my-config-for-us-east1``

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
            google.cloud.cloudquotas_v1beta.types.QuotaPreference:
                QuotaPreference represents the
                preferred quota configuration specified
                for a project, folder or organization.
                There is only one QuotaPreference
                resource for a quota value targeting a
                unique set of dimensions.

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
        if not isinstance(request, cloudquotas.GetQuotaPreferenceRequest):
            request = cloudquotas.GetQuotaPreferenceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_quota_preference
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

    async def create_quota_preference(
        self,
        request: Optional[Union[cloudquotas.CreateQuotaPreferenceRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        quota_preference: Optional[resources.QuotaPreference] = None,
        quota_preference_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QuotaPreference:
        r"""Creates a new QuotaPreference that declares the
        desired value for a quota.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudquotas_v1beta

            async def sample_create_quota_preference():
                # Create a client
                client = cloudquotas_v1beta.CloudQuotasAsyncClient()

                # Initialize request argument(s)
                quota_preference = cloudquotas_v1beta.QuotaPreference()
                quota_preference.quota_config.preferred_value = 1595
                quota_preference.service = "service_value"
                quota_preference.quota_id = "quota_id_value"

                request = cloudquotas_v1beta.CreateQuotaPreferenceRequest(
                    parent="parent_value",
                    quota_preference=quota_preference,
                )

                # Make the request
                response = await client.create_quota_preference(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudquotas_v1beta.types.CreateQuotaPreferenceRequest, dict]]):
                The request object. Message for creating a
                QuotaPreference
            parent (:class:`str`):
                Required. Value for parent.

                Example: ``projects/123/locations/global``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            quota_preference (:class:`google.cloud.cloudquotas_v1beta.types.QuotaPreference`):
                Required. The resource being created
                This corresponds to the ``quota_preference`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            quota_preference_id (:class:`str`):
                Optional. Id of the requesting
                object, must be unique under its parent.
                If client does not set this field, the
                service will generate one.

                This corresponds to the ``quota_preference_id`` field
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
            google.cloud.cloudquotas_v1beta.types.QuotaPreference:
                QuotaPreference represents the
                preferred quota configuration specified
                for a project, folder or organization.
                There is only one QuotaPreference
                resource for a quota value targeting a
                unique set of dimensions.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, quota_preference, quota_preference_id]
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
        if not isinstance(request, cloudquotas.CreateQuotaPreferenceRequest):
            request = cloudquotas.CreateQuotaPreferenceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if quota_preference is not None:
            request.quota_preference = quota_preference
        if quota_preference_id is not None:
            request.quota_preference_id = quota_preference_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_quota_preference
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

    async def update_quota_preference(
        self,
        request: Optional[Union[cloudquotas.UpdateQuotaPreferenceRequest, dict]] = None,
        *,
        quota_preference: Optional[resources.QuotaPreference] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QuotaPreference:
        r"""Updates the parameters of a single QuotaPreference.
        It can updates the config in any states, not just the
        ones pending approval.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudquotas_v1beta

            async def sample_update_quota_preference():
                # Create a client
                client = cloudquotas_v1beta.CloudQuotasAsyncClient()

                # Initialize request argument(s)
                quota_preference = cloudquotas_v1beta.QuotaPreference()
                quota_preference.quota_config.preferred_value = 1595
                quota_preference.service = "service_value"
                quota_preference.quota_id = "quota_id_value"

                request = cloudquotas_v1beta.UpdateQuotaPreferenceRequest(
                    quota_preference=quota_preference,
                )

                # Make the request
                response = await client.update_quota_preference(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudquotas_v1beta.types.UpdateQuotaPreferenceRequest, dict]]):
                The request object. Message for updating a
                QuotaPreference
            quota_preference (:class:`google.cloud.cloudquotas_v1beta.types.QuotaPreference`):
                Required. The resource being updated
                This corresponds to the ``quota_preference`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Field mask is used to specify the fields to be
                overwritten in the QuotaPreference resource by the
                update. The fields specified in the update_mask are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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
            google.cloud.cloudquotas_v1beta.types.QuotaPreference:
                QuotaPreference represents the
                preferred quota configuration specified
                for a project, folder or organization.
                There is only one QuotaPreference
                resource for a quota value targeting a
                unique set of dimensions.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [quota_preference, update_mask]
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
        if not isinstance(request, cloudquotas.UpdateQuotaPreferenceRequest):
            request = cloudquotas.UpdateQuotaPreferenceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if quota_preference is not None:
            request.quota_preference = quota_preference
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_quota_preference
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("quota_preference.name", request.quota_preference.name),)
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

    async def __aenter__(self) -> "CloudQuotasAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("CloudQuotasAsyncClient",)
