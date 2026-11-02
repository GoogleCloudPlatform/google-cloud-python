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

from google.ads.datamanager_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.ads.datamanager_v1.types import (
    ingestion_service,
    processing_errors,
    request_status_per_destination,
)

from .client import IngestionServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, IngestionServiceTransport
from .transports.grpc_asyncio import IngestionServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class IngestionServiceAsyncClient:
    """Service for sending audience data to supported destinations."""

    _client: IngestionServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = IngestionServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = IngestionServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = IngestionServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = IngestionServiceClient._DEFAULT_UNIVERSE

    common_billing_account_path = staticmethod(
        IngestionServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        IngestionServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(IngestionServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        IngestionServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        IngestionServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        IngestionServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(IngestionServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        IngestionServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(IngestionServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        IngestionServiceClient.parse_common_location_path
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
            IngestionServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            IngestionServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(IngestionServiceAsyncClient, info, *args, **kwargs)

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
            IngestionServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            IngestionServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(IngestionServiceAsyncClient, filename, *args, **kwargs)

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
        return IngestionServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> IngestionServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            IngestionServiceTransport: The transport used by the client instance.
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

    get_transport_class = IngestionServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str, IngestionServiceTransport, Callable[..., IngestionServiceTransport]
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the ingestion service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,IngestionServiceTransport,Callable[..., IngestionServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the IngestionServiceTransport constructor.
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
        self._client = IngestionServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.ads.datamanager_v1.IngestionServiceAsyncClient`.",
                extra={
                    "serviceName": "google.ads.datamanager.v1.IngestionService",
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
                    "serviceName": "google.ads.datamanager.v1.IngestionService",
                    "credentialsType": None,
                },
            )

    async def ingest_audience_members(
        self,
        request: Optional[
            Union[ingestion_service.IngestAudienceMembersRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ingestion_service.IngestAudienceMembersResponse:
        r"""Uploads a list of
        [AudienceMember][google.ads.datamanager.v1.AudienceMember]
        resources to the provided
        [Destination][google.ads.datamanager.v1.Destination].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_ingest_audience_members():
                # Create a client
                client = datamanager_v1.IngestionServiceAsyncClient()

                # Initialize request argument(s)
                destinations = datamanager_v1.Destination()
                destinations.operating_account.account_id = "account_id_value"
                destinations.operating_account.account_type = "GOOGLE_AD_MANAGER"

                audience_members = datamanager_v1.AudienceMember()
                audience_members.user_data.user_identifiers.email_address = "email_address_value"

                request = datamanager_v1.IngestAudienceMembersRequest(
                    destinations=destinations,
                    audience_members=audience_members,
                )

                # Make the request
                response = await client.ingest_audience_members(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.IngestAudienceMembersRequest, dict]]):
                The request object. Request to upload audience members to the provided
                destinations. Returns an
                [IngestAudienceMembersResponse][google.ads.datamanager.v1.IngestAudienceMembersResponse].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.datamanager_v1.types.IngestAudienceMembersResponse:
                Response from the
                   [IngestAudienceMembersRequest][google.ads.datamanager.v1.IngestAudienceMembersRequest].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, ingestion_service.IngestAudienceMembersRequest):
            request = ingestion_service.IngestAudienceMembersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.ingest_audience_members
        ]

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

    async def remove_audience_members(
        self,
        request: Optional[
            Union[ingestion_service.RemoveAudienceMembersRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ingestion_service.RemoveAudienceMembersResponse:
        r"""Removes a list of
        [AudienceMember][google.ads.datamanager.v1.AudienceMember]
        resources from the provided
        [Destination][google.ads.datamanager.v1.Destination].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_remove_audience_members():
                # Create a client
                client = datamanager_v1.IngestionServiceAsyncClient()

                # Initialize request argument(s)
                destinations = datamanager_v1.Destination()
                destinations.operating_account.account_id = "account_id_value"
                destinations.operating_account.account_type = "GOOGLE_AD_MANAGER"

                audience_members = datamanager_v1.AudienceMember()
                audience_members.user_data.user_identifiers.email_address = "email_address_value"

                request = datamanager_v1.RemoveAudienceMembersRequest(
                    destinations=destinations,
                    audience_members=audience_members,
                )

                # Make the request
                response = await client.remove_audience_members(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.RemoveAudienceMembersRequest, dict]]):
                The request object. Request to remove users from an audience in the provided
                destinations. Returns a
                [RemoveAudienceMembersResponse][google.ads.datamanager.v1.RemoveAudienceMembersResponse].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.datamanager_v1.types.RemoveAudienceMembersResponse:
                Response from the
                   [RemoveAudienceMembersRequest][google.ads.datamanager.v1.RemoveAudienceMembersRequest].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, ingestion_service.RemoveAudienceMembersRequest):
            request = ingestion_service.RemoveAudienceMembersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.remove_audience_members
        ]

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

    async def remove_all_audience_members(
        self,
        request: Optional[
            Union[ingestion_service.RemoveAllAudienceMembersRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ingestion_service.RemoveAllAudienceMembersResponse:
        r"""Removes all audience members from the provided
        destinations.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_remove_all_audience_members():
                # Create a client
                client = datamanager_v1.IngestionServiceAsyncClient()

                # Initialize request argument(s)
                destinations = datamanager_v1.Destination()
                destinations.operating_account.account_id = "account_id_value"
                destinations.operating_account.account_type = "GOOGLE_AD_MANAGER"

                request = datamanager_v1.RemoveAllAudienceMembersRequest(
                    destinations=destinations,
                )

                # Make the request
                response = await client.remove_all_audience_members(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.RemoveAllAudienceMembersRequest, dict]]):
                The request object. Request to remove all users from an audience in the
                provided destinations. Returns a
                [RemoveAllAudienceMembersResponse][google.ads.datamanager.v1.RemoveAllAudienceMembersResponse].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.datamanager_v1.types.RemoveAllAudienceMembersResponse:
                Response from the
                   [RemoveAllAudienceMembersRequest][google.ads.datamanager.v1.RemoveAllAudienceMembersRequest].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, ingestion_service.RemoveAllAudienceMembersRequest):
            request = ingestion_service.RemoveAllAudienceMembersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.remove_all_audience_members
        ]

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

    async def ingest_events(
        self,
        request: Optional[Union[ingestion_service.IngestEventsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ingestion_service.IngestEventsResponse:
        r"""Uploads a list of [Event][google.ads.datamanager.v1.Event]
        resources from the provided
        [Destination][google.ads.datamanager.v1.Destination].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_ingest_events():
                # Create a client
                client = datamanager_v1.IngestionServiceAsyncClient()

                # Initialize request argument(s)
                destinations = datamanager_v1.Destination()
                destinations.operating_account.account_id = "account_id_value"
                destinations.operating_account.account_type = "GOOGLE_AD_MANAGER"

                request = datamanager_v1.IngestEventsRequest(
                    destinations=destinations,
                )

                # Make the request
                response = await client.ingest_events(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.IngestEventsRequest, dict]]):
                The request object. Request to upload audience members to the provided
                destinations. Returns an
                [IngestEventsResponse][google.ads.datamanager.v1.IngestEventsResponse].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.datamanager_v1.types.IngestEventsResponse:
                Response from the
                   [IngestEventsRequest][google.ads.datamanager.v1.IngestEventsRequest].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, ingestion_service.IngestEventsRequest):
            request = ingestion_service.IngestEventsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.ingest_events
        ]

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

    async def ingest_users(
        self,
        request: Optional[Union[ingestion_service.IngestUsersRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ingestion_service.IngestUsersResponse:
        r"""Uploads a list of users to the provided destinations. Unlike
        [IngestAudienceMembers][google.ads.datamanager.v1.IngestionService.IngestAudienceMembers]
        (which adds users to specific advertiser audience lists for
        targeting), ``IngestUsers`` ingests account level identity
        linkage data (for example, user identifiers linked to mobile
        IDs) independent of specific audience segments.

        This feature is only available to accounts on an allowlist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_ingest_users():
                # Create a client
                client = datamanager_v1.IngestionServiceAsyncClient()

                # Initialize request argument(s)
                destinations = datamanager_v1.Destination()
                destinations.operating_account.account_id = "account_id_value"
                destinations.operating_account.account_type = "GOOGLE_AD_MANAGER"

                users = datamanager_v1.User()
                users.user_data.user_identifiers.email_address = "email_address_value"
                users.mobile_data.mobile_ids = ['mobile_ids_value1', 'mobile_ids_value2']

                request = datamanager_v1.IngestUsersRequest(
                    destinations=destinations,
                    users=users,
                    encoding="BASE64",
                )

                # Make the request
                response = await client.ingest_users(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.IngestUsersRequest, dict]]):
                The request object. Request to upload users to the
                provided destinations.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.datamanager_v1.types.IngestUsersResponse:
                Response from the IngestUsersRequest.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, ingestion_service.IngestUsersRequest):
            request = ingestion_service.IngestUsersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.ingest_users
        ]

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

    async def remove_users(
        self,
        request: Optional[Union[ingestion_service.RemoveUsersRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ingestion_service.RemoveUsersResponse:
        r"""Removes a list of users from the provided
        destinations.
        This feature is only available to accounts on an
        allowlist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_remove_users():
                # Create a client
                client = datamanager_v1.IngestionServiceAsyncClient()

                # Initialize request argument(s)
                destinations = datamanager_v1.Destination()
                destinations.operating_account.account_id = "account_id_value"
                destinations.operating_account.account_type = "GOOGLE_AD_MANAGER"

                user_data = datamanager_v1.UserData()
                user_data.user_identifiers.email_address = "email_address_value"

                request = datamanager_v1.RemoveUsersRequest(
                    destinations=destinations,
                    user_data=user_data,
                    encoding="BASE64",
                )

                # Make the request
                response = await client.remove_users(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.RemoveUsersRequest, dict]]):
                The request object. Request to remove users from the
                provided destinations.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.datamanager_v1.types.RemoveUsersResponse:
                Response from the RemoveUsersRequest.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, ingestion_service.RemoveUsersRequest):
            request = ingestion_service.RemoveUsersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.remove_users
        ]

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

    async def ingest_ad_events(
        self,
        request: Optional[Union[ingestion_service.IngestAdEventsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ingestion_service.IngestAdEventsResponse:
        r"""Uploads a list of [AdEvent][google.ads.datamanager.v1.AdEvent]
        resources to Google Analytics.

        This feature is only available to accounts on an allowlist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_ingest_ad_events():
                # Create a client
                client = datamanager_v1.IngestionServiceAsyncClient()

                # Initialize request argument(s)
                ad_events = datamanager_v1.AdEvent()
                ad_events.event_subtype = "EVENT_SUBTYPE_OUTBOUND_CLICK"
                ad_events.ad_type = "AD_TYPE_VIDEO"
                ad_events.ad_format = "AD_FORMAT_VIDEO"
                ad_events.ad_placement = "AD_PLACEMENT_STORY"
                ad_events.targeting_type = "TARGETING_TYPE_REMARKETING"
                ad_events.platform_type = "PLATFORM_TYPE_TABLET"
                ad_events.platform = "PLATFORM_WEB"
                ad_events.advertiser_id = "advertiser_id_value"
                ad_events.event_type = "EVENT_TYPE_CLICK"
                ad_events.campaign_id = "campaign_id_value"
                ad_events.campaign_name = "campaign_name_value"
                ad_events.source = "source_value"
                ad_events.medium = "medium_value"
                ad_events.viewability_info.view_type = "VIEW_TYPE_MRC_RENDERED"

                request = datamanager_v1.IngestAdEventsRequest(
                    ad_events=ad_events,
                )

                # Make the request
                response = await client.ingest_ad_events(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.IngestAdEventsRequest, dict]]):
                The request object. Request to upload ad events.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.datamanager_v1.types.IngestAdEventsResponse:
                Response from an ad event ingestion
                operation.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, ingestion_service.IngestAdEventsRequest):
            request = ingestion_service.IngestAdEventsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.ingest_ad_events
        ]

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

    async def retrieve_request_status(
        self,
        request: Optional[
            Union[ingestion_service.RetrieveRequestStatusRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ingestion_service.RetrieveRequestStatusResponse:
        r"""Gets the status of a request given request id.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_retrieve_request_status():
                # Create a client
                client = datamanager_v1.IngestionServiceAsyncClient()

                # Initialize request argument(s)
                request = datamanager_v1.RetrieveRequestStatusRequest(
                    request_id="request_id_value",
                )

                # Make the request
                response = await client.retrieve_request_status(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.RetrieveRequestStatusRequest, dict]]):
                The request object. Request to get the status of request made to the DM API
                for a given request ID. Returns a
                [RetrieveRequestStatusResponse][google.ads.datamanager.v1.RetrieveRequestStatusResponse].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.datamanager_v1.types.RetrieveRequestStatusResponse:
                Response from the
                   [RetrieveRequestStatusRequest][google.ads.datamanager.v1.RetrieveRequestStatusRequest].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, ingestion_service.RetrieveRequestStatusRequest):
            request = ingestion_service.RetrieveRequestStatusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.retrieve_request_status
        ]

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

    async def __aenter__(self) -> "IngestionServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("IngestionServiceAsyncClient",)
