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

from google.cloud.dialogflow_v2 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.dialogflow_v2.services.conversation_profiles import pagers
from google.cloud.dialogflow_v2.types import (
    audio_config,
    conversation_profile,
    participant,
)
from google.cloud.dialogflow_v2.types import (
    conversation_profile as gcd_conversation_profile,
)

from .client import ConversationProfilesClient
from .transports.base import DEFAULT_CLIENT_INFO, ConversationProfilesTransport
from .transports.grpc_asyncio import ConversationProfilesGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class ConversationProfilesAsyncClient:
    """Service for managing
    [ConversationProfiles][google.cloud.dialogflow.v2.ConversationProfile].
    """

    _client: ConversationProfilesClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = ConversationProfilesClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ConversationProfilesClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = ConversationProfilesClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = ConversationProfilesClient._DEFAULT_UNIVERSE

    agent_path = staticmethod(ConversationProfilesClient.agent_path)
    parse_agent_path = staticmethod(ConversationProfilesClient.parse_agent_path)
    companion_agent_path = staticmethod(ConversationProfilesClient.companion_agent_path)
    parse_companion_agent_path = staticmethod(
        ConversationProfilesClient.parse_companion_agent_path
    )
    conversation_model_path = staticmethod(
        ConversationProfilesClient.conversation_model_path
    )
    parse_conversation_model_path = staticmethod(
        ConversationProfilesClient.parse_conversation_model_path
    )
    conversation_profile_path = staticmethod(
        ConversationProfilesClient.conversation_profile_path
    )
    parse_conversation_profile_path = staticmethod(
        ConversationProfilesClient.parse_conversation_profile_path
    )
    cx_security_settings_path = staticmethod(
        ConversationProfilesClient.cx_security_settings_path
    )
    parse_cx_security_settings_path = staticmethod(
        ConversationProfilesClient.parse_cx_security_settings_path
    )
    document_path = staticmethod(ConversationProfilesClient.document_path)
    parse_document_path = staticmethod(ConversationProfilesClient.parse_document_path)
    generator_path = staticmethod(ConversationProfilesClient.generator_path)
    parse_generator_path = staticmethod(ConversationProfilesClient.parse_generator_path)
    knowledge_base_path = staticmethod(ConversationProfilesClient.knowledge_base_path)
    parse_knowledge_base_path = staticmethod(
        ConversationProfilesClient.parse_knowledge_base_path
    )
    phrase_set_path = staticmethod(ConversationProfilesClient.phrase_set_path)
    parse_phrase_set_path = staticmethod(
        ConversationProfilesClient.parse_phrase_set_path
    )
    common_billing_account_path = staticmethod(
        ConversationProfilesClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ConversationProfilesClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ConversationProfilesClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ConversationProfilesClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ConversationProfilesClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ConversationProfilesClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ConversationProfilesClient.common_project_path)
    parse_common_project_path = staticmethod(
        ConversationProfilesClient.parse_common_project_path
    )
    common_location_path = staticmethod(ConversationProfilesClient.common_location_path)
    parse_common_location_path = staticmethod(
        ConversationProfilesClient.parse_common_location_path
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
            ConversationProfilesAsyncClient: The constructed client.
        """
        sa_info_func = (
            ConversationProfilesClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(ConversationProfilesAsyncClient, info, *args, **kwargs)

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
            ConversationProfilesAsyncClient: The constructed client.
        """
        sa_file_func = (
            ConversationProfilesClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(ConversationProfilesAsyncClient, filename, *args, **kwargs)

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
        return ConversationProfilesClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> ConversationProfilesTransport:
        """Returns the transport used by the client instance.

        Returns:
            ConversationProfilesTransport: The transport used by the client instance.
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

    get_transport_class = ConversationProfilesClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                ConversationProfilesTransport,
                Callable[..., ConversationProfilesTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the conversation profiles async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ConversationProfilesTransport,Callable[..., ConversationProfilesTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ConversationProfilesTransport constructor.
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
        self._client = ConversationProfilesClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.dialogflow_v2.ConversationProfilesAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.dialogflow.v2.ConversationProfiles",
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
                    "serviceName": "google.cloud.dialogflow.v2.ConversationProfiles",
                    "credentialsType": None,
                },
            )

    async def list_conversation_profiles(
        self,
        request: Optional[
            Union[conversation_profile.ListConversationProfilesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListConversationProfilesAsyncPager:
        r"""Returns the list of all conversation profiles in the
        specified project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2

            async def sample_list_conversation_profiles():
                # Create a client
                client = dialogflow_v2.ConversationProfilesAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ListConversationProfilesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversation_profiles(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2.types.ListConversationProfilesRequest, dict]]):
                The request object. The request message for
                [ConversationProfiles.ListConversationProfiles][google.cloud.dialogflow.v2.ConversationProfiles.ListConversationProfiles].
            parent (:class:`str`):
                Required. The project to list all conversation profiles
                from. Format:
                ``projects/<Project ID>/locations/<Location ID>``.

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
            google.cloud.dialogflow_v2.services.conversation_profiles.pagers.ListConversationProfilesAsyncPager:
                The response message for
                   [ConversationProfiles.ListConversationProfiles][google.cloud.dialogflow.v2.ConversationProfiles.ListConversationProfiles].

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
        if not isinstance(
            request, conversation_profile.ListConversationProfilesRequest
        ):
            request = conversation_profile.ListConversationProfilesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_conversation_profiles
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
        response = pagers.ListConversationProfilesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_conversation_profile(
        self,
        request: Optional[
            Union[conversation_profile.GetConversationProfileRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation_profile.ConversationProfile:
        r"""Retrieves the specified conversation profile.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2

            async def sample_get_conversation_profile():
                # Create a client
                client = dialogflow_v2.ConversationProfilesAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.GetConversationProfileRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_conversation_profile(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2.types.GetConversationProfileRequest, dict]]):
                The request object. The request message for
                [ConversationProfiles.GetConversationProfile][google.cloud.dialogflow.v2.ConversationProfiles.GetConversationProfile].
            name (:class:`str`):
                Required. The resource name of the conversation profile.
                Format:
                ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.

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
            google.cloud.dialogflow_v2.types.ConversationProfile:
                Defines the services to connect to
                incoming Dialogflow conversations.

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
        if not isinstance(request, conversation_profile.GetConversationProfileRequest):
            request = conversation_profile.GetConversationProfileRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_conversation_profile
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

    async def create_conversation_profile(
        self,
        request: Optional[
            Union[gcd_conversation_profile.CreateConversationProfileRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        conversation_profile: Optional[
            gcd_conversation_profile.ConversationProfile
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_conversation_profile.ConversationProfile:
        r"""Creates a conversation profile in the specified project.

        [ConversationProfile.create_time][google.cloud.dialogflow.v2.ConversationProfile.create_time]
        and
        [ConversationProfile.update_time][google.cloud.dialogflow.v2.ConversationProfile.update_time]
        aren't populated in the response. You can retrieve them via
        [GetConversationProfile][google.cloud.dialogflow.v2.ConversationProfiles.GetConversationProfile]
        API.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2

            async def sample_create_conversation_profile():
                # Create a client
                client = dialogflow_v2.ConversationProfilesAsyncClient()

                # Initialize request argument(s)
                conversation_profile = dialogflow_v2.ConversationProfile()
                conversation_profile.display_name = "display_name_value"

                request = dialogflow_v2.CreateConversationProfileRequest(
                    parent="parent_value",
                    conversation_profile=conversation_profile,
                )

                # Make the request
                response = await client.create_conversation_profile(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2.types.CreateConversationProfileRequest, dict]]):
                The request object. The request message for
                [ConversationProfiles.CreateConversationProfile][google.cloud.dialogflow.v2.ConversationProfiles.CreateConversationProfile].
            parent (:class:`str`):
                Required. The project to create a conversation profile
                for. Format:
                ``projects/<Project ID>/locations/<Location ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation_profile (:class:`google.cloud.dialogflow_v2.types.ConversationProfile`):
                Required. The conversation profile to
                create.

                This corresponds to the ``conversation_profile`` field
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
            google.cloud.dialogflow_v2.types.ConversationProfile:
                Defines the services to connect to
                incoming Dialogflow conversations.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, conversation_profile]
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
            request, gcd_conversation_profile.CreateConversationProfileRequest
        ):
            request = gcd_conversation_profile.CreateConversationProfileRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if conversation_profile is not None:
            request.conversation_profile = conversation_profile

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_conversation_profile
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

    async def update_conversation_profile(
        self,
        request: Optional[
            Union[gcd_conversation_profile.UpdateConversationProfileRequest, dict]
        ] = None,
        *,
        conversation_profile: Optional[
            gcd_conversation_profile.ConversationProfile
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_conversation_profile.ConversationProfile:
        r"""Updates the specified conversation profile.

        [ConversationProfile.create_time][google.cloud.dialogflow.v2.ConversationProfile.create_time]
        and
        [ConversationProfile.update_time][google.cloud.dialogflow.v2.ConversationProfile.update_time]
        aren't populated in the response. You can retrieve them via
        [GetConversationProfile][google.cloud.dialogflow.v2.ConversationProfiles.GetConversationProfile]
        API.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2

            async def sample_update_conversation_profile():
                # Create a client
                client = dialogflow_v2.ConversationProfilesAsyncClient()

                # Initialize request argument(s)
                conversation_profile = dialogflow_v2.ConversationProfile()
                conversation_profile.display_name = "display_name_value"

                request = dialogflow_v2.UpdateConversationProfileRequest(
                    conversation_profile=conversation_profile,
                )

                # Make the request
                response = await client.update_conversation_profile(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2.types.UpdateConversationProfileRequest, dict]]):
                The request object. The request message for
                [ConversationProfiles.UpdateConversationProfile][google.cloud.dialogflow.v2.ConversationProfiles.UpdateConversationProfile].
            conversation_profile (:class:`google.cloud.dialogflow_v2.types.ConversationProfile`):
                Required. The conversation profile to
                update.

                This corresponds to the ``conversation_profile`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The mask to control which
                fields to update.

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
            google.cloud.dialogflow_v2.types.ConversationProfile:
                Defines the services to connect to
                incoming Dialogflow conversations.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation_profile, update_mask]
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
            request, gcd_conversation_profile.UpdateConversationProfileRequest
        ):
            request = gcd_conversation_profile.UpdateConversationProfileRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if conversation_profile is not None:
            request.conversation_profile = conversation_profile
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_conversation_profile
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation_profile.name", request.conversation_profile.name),)
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

    async def delete_conversation_profile(
        self,
        request: Optional[
            Union[conversation_profile.DeleteConversationProfileRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified conversation profile.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2

            async def sample_delete_conversation_profile():
                # Create a client
                client = dialogflow_v2.ConversationProfilesAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DeleteConversationProfileRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_conversation_profile(request=request)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2.types.DeleteConversationProfileRequest, dict]]):
                The request object. The request message for
                [ConversationProfiles.DeleteConversationProfile][google.cloud.dialogflow.v2.ConversationProfiles.DeleteConversationProfile].

                This operation fails if the conversation profile is
                still referenced from a phone number.
            name (:class:`str`):
                Required. The name of the conversation profile to
                delete. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.

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
        if not isinstance(
            request, conversation_profile.DeleteConversationProfileRequest
        ):
            request = conversation_profile.DeleteConversationProfileRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_conversation_profile
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

    async def set_suggestion_feature_config(
        self,
        request: Optional[
            Union[gcd_conversation_profile.SetSuggestionFeatureConfigRequest, dict]
        ] = None,
        *,
        conversation_profile: Optional[str] = None,
        participant_role: Optional[participant.Participant.Role] = None,
        suggestion_feature_config: Optional[
            gcd_conversation_profile.HumanAgentAssistantConfig.SuggestionFeatureConfig
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Adds or updates a suggestion feature in a conversation profile.
        If the conversation profile contains the type of suggestion
        feature for the participant role, it will update it. Otherwise
        it will insert the suggestion feature.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        - ``metadata``:
          [SetSuggestionFeatureConfigOperationMetadata][google.cloud.dialogflow.v2.SetSuggestionFeatureConfigOperationMetadata]
        - ``response``:
          [ConversationProfile][google.cloud.dialogflow.v2.ConversationProfile]

        If a long running operation to add or update suggestion feature
        config for the same conversation profile, participant role and
        suggestion feature type exists, please cancel the existing long
        running operation before sending such request, otherwise the
        request will be rejected.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2

            async def sample_set_suggestion_feature_config():
                # Create a client
                client = dialogflow_v2.ConversationProfilesAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.SetSuggestionFeatureConfigRequest(
                    conversation_profile="conversation_profile_value",
                    participant_role="END_USER",
                )

                # Make the request
                operation = await client.set_suggestion_feature_config(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2.types.SetSuggestionFeatureConfigRequest, dict]]):
                The request object. The request message for
                [ConversationProfiles.SetSuggestionFeatureConfig][google.cloud.dialogflow.v2.ConversationProfiles.SetSuggestionFeatureConfig].
            conversation_profile (:class:`str`):
                Required. The Conversation Profile to add or update the
                suggestion feature config. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.

                This corresponds to the ``conversation_profile`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            participant_role (:class:`google.cloud.dialogflow_v2.types.Participant.Role`):
                Required. The participant role to add or update the
                suggestion feature config. Only HUMAN_AGENT or END_USER
                can be used.

                This corresponds to the ``participant_role`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            suggestion_feature_config (:class:`google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionFeatureConfig`):
                Required. The suggestion feature
                config to add or update.

                This corresponds to the ``suggestion_feature_config`` field
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
                :class:`google.cloud.dialogflow_v2.types.ConversationProfile`
                Defines the services to connect to incoming Dialogflow
                conversations.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            conversation_profile,
            participant_role,
            suggestion_feature_config,
        ]
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
            request, gcd_conversation_profile.SetSuggestionFeatureConfigRequest
        ):
            request = gcd_conversation_profile.SetSuggestionFeatureConfigRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if conversation_profile is not None:
            request.conversation_profile = conversation_profile
        if participant_role is not None:
            request.participant_role = participant_role
        if suggestion_feature_config is not None:
            request.suggestion_feature_config = suggestion_feature_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.set_suggestion_feature_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation_profile", request.conversation_profile),)
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
            gcd_conversation_profile.ConversationProfile,
            metadata_type=gcd_conversation_profile.SetSuggestionFeatureConfigOperationMetadata,
        )

        # Done; return the response.
        return response

    async def clear_suggestion_feature_config(
        self,
        request: Optional[
            Union[gcd_conversation_profile.ClearSuggestionFeatureConfigRequest, dict]
        ] = None,
        *,
        conversation_profile: Optional[str] = None,
        participant_role: Optional[participant.Participant.Role] = None,
        suggestion_feature_type: Optional[
            gcd_conversation_profile.SuggestionFeature.Type
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Clears a suggestion feature from a conversation profile for the
        given participant role.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        - ``metadata``:
          [ClearSuggestionFeatureConfigOperationMetadata][google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigOperationMetadata]
        - ``response``:
          [ConversationProfile][google.cloud.dialogflow.v2.ConversationProfile]

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2

            async def sample_clear_suggestion_feature_config():
                # Create a client
                client = dialogflow_v2.ConversationProfilesAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ClearSuggestionFeatureConfigRequest(
                    conversation_profile="conversation_profile_value",
                    participant_role="END_USER",
                    suggestion_feature_type="KNOWLEDGE_ASSIST",
                )

                # Make the request
                operation = await client.clear_suggestion_feature_config(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2.types.ClearSuggestionFeatureConfigRequest, dict]]):
                The request object. The request message for
                [ConversationProfiles.ClearSuggestionFeatureConfig][google.cloud.dialogflow.v2.ConversationProfiles.ClearSuggestionFeatureConfig].
            conversation_profile (:class:`str`):
                Required. The Conversation Profile to add or update the
                suggestion feature config. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.

                This corresponds to the ``conversation_profile`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            participant_role (:class:`google.cloud.dialogflow_v2.types.Participant.Role`):
                Required. The participant role to remove the suggestion
                feature config. Only HUMAN_AGENT or END_USER can be
                used.

                This corresponds to the ``participant_role`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            suggestion_feature_type (:class:`google.cloud.dialogflow_v2.types.SuggestionFeature.Type`):
                Required. The type of the suggestion
                feature to remove.

                This corresponds to the ``suggestion_feature_type`` field
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
                :class:`google.cloud.dialogflow_v2.types.ConversationProfile`
                Defines the services to connect to incoming Dialogflow
                conversations.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            conversation_profile,
            participant_role,
            suggestion_feature_type,
        ]
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
            request, gcd_conversation_profile.ClearSuggestionFeatureConfigRequest
        ):
            request = gcd_conversation_profile.ClearSuggestionFeatureConfigRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if conversation_profile is not None:
            request.conversation_profile = conversation_profile
        if participant_role is not None:
            request.participant_role = participant_role
        if suggestion_feature_type is not None:
            request.suggestion_feature_type = suggestion_feature_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.clear_suggestion_feature_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation_profile", request.conversation_profile),)
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
            gcd_conversation_profile.ConversationProfile,
            metadata_type=gcd_conversation_profile.ClearSuggestionFeatureConfigOperationMetadata,
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

    async def get_location(
        self,
        request: Optional[Union[locations_pb2.GetLocationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.Location:
        r"""Gets information about a location.

        Args:
            request (:class:`~.location_pb2.GetLocationRequest`):
                The request object. Request message for
                `GetLocation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.Location:
                Location object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.GetLocationRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.GetLocationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_location]

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

    async def list_locations(
        self,
        request: Optional[Union[locations_pb2.ListLocationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.ListLocationsResponse:
        r"""Lists information about the supported locations for this service.

        Args:
            request (:class:`~.location_pb2.ListLocationsRequest`):
                The request object. Request message for
                `ListLocations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.ListLocationsResponse:
                Response message for ``ListLocations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.ListLocationsRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.ListLocationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_locations]

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

    async def __aenter__(self) -> "ConversationProfilesAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("ConversationProfilesAsyncClient",)
