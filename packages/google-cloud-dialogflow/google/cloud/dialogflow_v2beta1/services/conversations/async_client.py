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

from google.cloud.dialogflow_v2beta1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.dialogflow_v2beta1.services.conversations import pagers
from google.cloud.dialogflow_v2beta1.types import (
    conversation,
    conversation_profile,
    generator,
    participant,
)
from google.cloud.dialogflow_v2beta1.types import conversation as gcd_conversation

from .client import ConversationsClient
from .transports.base import DEFAULT_CLIENT_INFO, ConversationsTransport
from .transports.grpc_asyncio import ConversationsGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class ConversationsAsyncClient:
    """Service for managing
    [Conversations][google.cloud.dialogflow.v2beta1.Conversation].
    """

    _client: ConversationsClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = ConversationsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ConversationsClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = ConversationsClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = ConversationsClient._DEFAULT_UNIVERSE

    agent_path = staticmethod(ConversationsClient.agent_path)
    parse_agent_path = staticmethod(ConversationsClient.parse_agent_path)
    answer_record_path = staticmethod(ConversationsClient.answer_record_path)
    parse_answer_record_path = staticmethod(
        ConversationsClient.parse_answer_record_path
    )
    app_path = staticmethod(ConversationsClient.app_path)
    parse_app_path = staticmethod(ConversationsClient.parse_app_path)
    ces_tool_path = staticmethod(ConversationsClient.ces_tool_path)
    parse_ces_tool_path = staticmethod(ConversationsClient.parse_ces_tool_path)
    companion_agent_path = staticmethod(ConversationsClient.companion_agent_path)
    parse_companion_agent_path = staticmethod(
        ConversationsClient.parse_companion_agent_path
    )
    conversation_path = staticmethod(ConversationsClient.conversation_path)
    parse_conversation_path = staticmethod(ConversationsClient.parse_conversation_path)
    conversation_profile_path = staticmethod(
        ConversationsClient.conversation_profile_path
    )
    parse_conversation_profile_path = staticmethod(
        ConversationsClient.parse_conversation_profile_path
    )
    cx_security_settings_path = staticmethod(
        ConversationsClient.cx_security_settings_path
    )
    parse_cx_security_settings_path = staticmethod(
        ConversationsClient.parse_cx_security_settings_path
    )
    data_store_path = staticmethod(ConversationsClient.data_store_path)
    parse_data_store_path = staticmethod(ConversationsClient.parse_data_store_path)
    document_path = staticmethod(ConversationsClient.document_path)
    parse_document_path = staticmethod(ConversationsClient.parse_document_path)
    generator_path = staticmethod(ConversationsClient.generator_path)
    parse_generator_path = staticmethod(ConversationsClient.parse_generator_path)
    knowledge_base_path = staticmethod(ConversationsClient.knowledge_base_path)
    parse_knowledge_base_path = staticmethod(
        ConversationsClient.parse_knowledge_base_path
    )
    message_path = staticmethod(ConversationsClient.message_path)
    parse_message_path = staticmethod(ConversationsClient.parse_message_path)
    phrase_set_path = staticmethod(ConversationsClient.phrase_set_path)
    parse_phrase_set_path = staticmethod(ConversationsClient.parse_phrase_set_path)
    tool_path = staticmethod(ConversationsClient.tool_path)
    parse_tool_path = staticmethod(ConversationsClient.parse_tool_path)
    toolset_path = staticmethod(ConversationsClient.toolset_path)
    parse_toolset_path = staticmethod(ConversationsClient.parse_toolset_path)
    common_billing_account_path = staticmethod(
        ConversationsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ConversationsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ConversationsClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ConversationsClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ConversationsClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ConversationsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ConversationsClient.common_project_path)
    parse_common_project_path = staticmethod(
        ConversationsClient.parse_common_project_path
    )
    common_location_path = staticmethod(ConversationsClient.common_location_path)
    parse_common_location_path = staticmethod(
        ConversationsClient.parse_common_location_path
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
            ConversationsAsyncClient: The constructed client.
        """
        sa_info_func = (
            ConversationsClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(ConversationsAsyncClient, info, *args, **kwargs)

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
            ConversationsAsyncClient: The constructed client.
        """
        sa_file_func = (
            ConversationsClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(ConversationsAsyncClient, filename, *args, **kwargs)

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
        return ConversationsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ConversationsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ConversationsTransport: The transport used by the client instance.
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

    get_transport_class = ConversationsClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, ConversationsTransport, Callable[..., ConversationsTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the conversations async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ConversationsTransport,Callable[..., ConversationsTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ConversationsTransport constructor.
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
        self._client = ConversationsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.dialogflow_v2beta1.ConversationsAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
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
                    "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                    "credentialsType": None,
                },
            )

    async def create_conversation(
        self,
        request: Optional[
            Union[gcd_conversation.CreateConversationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        conversation: Optional[gcd_conversation.Conversation] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_conversation.Conversation:
        r"""Creates a new conversation. Conversations are auto-completed
        after 24 hours.

        Conversation Lifecycle: There are two stages during a
        conversation: Automated Agent Stage and Assist Stage.

        For Automated Agent Stage, there will be a dialogflow agent
        responding to user queries.

        For Assist Stage, there's no dialogflow agent responding to user
        queries. But we will provide suggestions which are generated
        from conversation.

        If
        [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile]
        is configured for a dialogflow agent, conversation will start
        from ``Automated Agent Stage``, otherwise, it will start from
        ``Assist Stage``. And during ``Automated Agent Stage``, once an
        [Intent][google.cloud.dialogflow.v2beta1.Intent] with
        [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff]
        is triggered, conversation will transfer to Assist Stage.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_create_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                conversation = dialogflow_v2beta1.Conversation()
                conversation.conversation_profile = "conversation_profile_value"

                request = dialogflow_v2beta1.CreateConversationRequest(
                    parent="parent_value",
                    conversation=conversation,
                )

                # Make the request
                response = await client.create_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.CreateConversationRequest, dict]]):
                The request object. The request message for
                [Conversations.CreateConversation][google.cloud.dialogflow.v2beta1.Conversations.CreateConversation].
            parent (:class:`str`):
                Required. Resource identifier of the project creating
                the conversation. Format:
                ``projects/<Project ID>/locations/<Location ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation (:class:`google.cloud.dialogflow_v2beta1.types.Conversation`):
                Required. The conversation to create.
                This corresponds to the ``conversation`` field
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
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, conversation]
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
        if not isinstance(request, gcd_conversation.CreateConversationRequest):
            request = gcd_conversation.CreateConversationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if conversation is not None:
            request.conversation = conversation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_conversation
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

    async def list_conversations(
        self,
        request: Optional[Union[conversation.ListConversationsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListConversationsAsyncPager:
        r"""Returns the list of all conversations in the
        specified project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_list_conversations():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListConversationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.ListConversationsRequest, dict]]):
                The request object. The request message for
                [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].
            parent (:class:`str`):
                Required. The project from which to list all
                conversation. Format:
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
            google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListConversationsAsyncPager:
                The response message for
                   [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].

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
        if not isinstance(request, conversation.ListConversationsRequest):
            request = conversation.ListConversationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_conversations
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
        response = pagers.ListConversationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_conversation(
        self,
        request: Optional[Union[conversation.GetConversationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.Conversation:
        r"""Retrieves the specific conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_get_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.GetConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.GetConversationRequest, dict]]):
                The request object. The request message for
                [Conversations.GetConversation][google.cloud.dialogflow.v2beta1.Conversations.GetConversation].
            name (:class:`str`):
                Required. The name of the conversation. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

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
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

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
        if not isinstance(request, conversation.GetConversationRequest):
            request = conversation.GetConversationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_conversation
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

    async def complete_conversation(
        self,
        request: Optional[Union[conversation.CompleteConversationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.Conversation:
        r"""Completes the specified conversation. Finished
        conversations are purged from the database after 30
        days.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_complete_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.CompleteConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.complete_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.CompleteConversationRequest, dict]]):
                The request object. The request message for
                [Conversations.CompleteConversation][google.cloud.dialogflow.v2beta1.Conversations.CompleteConversation].
            name (:class:`str`):
                Required. Resource identifier of the conversation to
                close. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

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
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

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
        if not isinstance(request, conversation.CompleteConversationRequest):
            request = conversation.CompleteConversationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.complete_conversation
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

    async def ingest_context_references(
        self,
        request: Optional[
            Union[gcd_conversation.IngestContextReferencesRequest, dict]
        ] = None,
        *,
        conversation: Optional[str] = None,
        context_references: Optional[
            MutableMapping[str, gcd_conversation.Conversation.ContextReference]
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_conversation.IngestContextReferencesResponse:
        r"""Data ingestion API.
        Ingests context references for an existing conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_ingest_context_references():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.IngestContextReferencesRequest(
                    conversation="conversation_value",
                )

                # Make the request
                response = await client.ingest_context_references(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.IngestContextReferencesRequest, dict]]):
                The request object. The request message for
                [ConversationsService.IngestContextReferences][].
            conversation (:class:`str`):
                Required. Resource identifier of the conversation to
                ingest context information for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``conversation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            context_references (:class:`MutableMapping[str, google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference]`):
                Required. The context references to
                ingest. The key is the name of the
                context reference and the value contains
                the contents of the context reference.
                The key is used to incorporate ingested
                context references to enhance the
                generator.

                This corresponds to the ``context_references`` field
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
            google.cloud.dialogflow_v2beta1.types.IngestContextReferencesResponse:
                The response message for
                [ConversationsService.IngestContextReferences][].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation, context_references]
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
        if not isinstance(request, gcd_conversation.IngestContextReferencesRequest):
            request = gcd_conversation.IngestContextReferencesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if conversation is not None:
            request.conversation = conversation

        if context_references:
            request.context_references.update(context_references)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.ingest_context_references
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation", request.conversation),)
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

    async def batch_create_messages(
        self,
        request: Optional[Union[conversation.BatchCreateMessagesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        requests: Optional[MutableSequence[conversation.CreateMessageRequest]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.BatchCreateMessagesResponse:
        r"""Batch ingests messages to conversation. Customers can
        use this RPC to ingest historical messages to
        conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_batch_create_messages():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                requests = dialogflow_v2beta1.CreateMessageRequest()
                requests.parent = "parent_value"

                request = dialogflow_v2beta1.BatchCreateMessagesRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = await client.batch_create_messages(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.BatchCreateMessagesRequest, dict]]):
                The request object. The request message for
                [Conversations.BatchCreateMessagesRequest][].
            parent (:class:`str`):
                Required. Resource identifier of the conversation to
                create message. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (:class:`MutableSequence[google.cloud.dialogflow_v2beta1.types.CreateMessageRequest]`):
                Required. A maximum of 300 messages can be created in a
                batch. [CreateMessageRequest.message.send_time][] is
                required. All created messages will have identical
                [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].

                This corresponds to the ``requests`` field
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
            google.cloud.dialogflow_v2beta1.types.BatchCreateMessagesResponse:
                The request message for
                [Conversations.BatchCreateMessagesResponse][].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, requests]
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
        if not isinstance(request, conversation.BatchCreateMessagesRequest):
            request = conversation.BatchCreateMessagesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if requests:
            request.requests.extend(requests)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_create_messages
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

    async def list_messages(
        self,
        request: Optional[Union[conversation.ListMessagesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListMessagesAsyncPager:
        r"""Lists messages that belong to a given conversation. ``messages``
        are ordered by ``create_time`` in descending order. To fetch
        updates without duplication, send request with filter
        ``create_time_epoch_microseconds > [first item's create_time of previous request]``
        and empty page_token.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_list_messages():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListMessagesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_messages(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.ListMessagesRequest, dict]]):
                The request object. The request message for
                [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].
            parent (:class:`str`):
                Required. The name of the conversation to list messages
                for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``

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
            google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListMessagesAsyncPager:
                The response message for
                   [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].

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
        if not isinstance(request, conversation.ListMessagesRequest):
            request = conversation.ListMessagesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_messages
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
        response = pagers.ListMessagesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def suggest_conversation_summary(
        self,
        request: Optional[
            Union[gcd_conversation.SuggestConversationSummaryRequest, dict]
        ] = None,
        *,
        conversation: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_conversation.SuggestConversationSummaryResponse:
        r"""Suggest summary for a conversation based on specific
        historical messages. The range of the messages to be
        used for summary can be specified in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_suggest_conversation_summary():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestConversationSummaryRequest(
                    conversation="conversation_value",
                )

                # Make the request
                response = await client.suggest_conversation_summary(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryRequest, dict]]):
                The request object. The request message for
                [Conversations.SuggestConversationSummary][google.cloud.dialogflow.v2beta1.Conversations.SuggestConversationSummary].
            conversation (:class:`str`):
                Required. The conversation to fetch suggestion for.
                Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``conversation`` field
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
            google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryResponse:
                The response message for
                   [Conversations.SuggestConversationSummary][google.cloud.dialogflow.v2beta1.Conversations.SuggestConversationSummary].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation]
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
        if not isinstance(request, gcd_conversation.SuggestConversationSummaryRequest):
            request = gcd_conversation.SuggestConversationSummaryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if conversation is not None:
            request.conversation = conversation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.suggest_conversation_summary
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation", request.conversation),)
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

    async def generate_stateless_summary(
        self,
        request: Optional[
            Union[conversation.GenerateStatelessSummaryRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.GenerateStatelessSummaryResponse:
        r"""Generates and returns a summary for a conversation
        that does not have a resource created for it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_generate_stateless_summary():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                stateless_conversation = dialogflow_v2beta1.MinimalConversation()
                stateless_conversation.parent = "parent_value"

                conversation_profile = dialogflow_v2beta1.ConversationProfile()
                conversation_profile.display_name = "display_name_value"

                request = dialogflow_v2beta1.GenerateStatelessSummaryRequest(
                    stateless_conversation=stateless_conversation,
                    conversation_profile=conversation_profile,
                )

                # Make the request
                response = await client.generate_stateless_summary(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest, dict]]):
                The request object. The request message for
                [Conversations.GenerateStatelessSummary][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSummary].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryResponse:
                The response message for
                   [Conversations.GenerateStatelessSummary][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSummary].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, conversation.GenerateStatelessSummaryRequest):
            request = conversation.GenerateStatelessSummaryRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_stateless_summary
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "stateless_conversation.parent",
                        request.stateless_conversation.parent,
                    ),
                )
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

    async def generate_stateless_suggestion(
        self,
        request: Optional[
            Union[conversation.GenerateStatelessSuggestionRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.GenerateStatelessSuggestionResponse:
        r"""Generates and returns a suggestion for a conversation
        that does not have a resource created for it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_generate_stateless_suggestion():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                generator = dialogflow_v2beta1.Generator()
                generator.published_model = "published_model_value"

                request = dialogflow_v2beta1.GenerateStatelessSuggestionRequest(
                    generator=generator,
                    parent="parent_value",
                )

                # Make the request
                response = await client.generate_stateless_suggestion(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.GenerateStatelessSuggestionRequest, dict]]):
                The request object. The request message for
                [Conversations.GenerateStatelessSuggestion][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.types.GenerateStatelessSuggestionResponse:
                The response message for
                   [Conversations.GenerateStatelessSuggestion][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, conversation.GenerateStatelessSuggestionRequest):
            request = conversation.GenerateStatelessSuggestionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_stateless_suggestion
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

    async def search_knowledge(
        self,
        request: Optional[Union[conversation.SearchKnowledgeRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.SearchKnowledgeResponse:
        r"""Get answers for the given query based on knowledge
        documents.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_search_knowledge():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SearchKnowledgeRequest(
                    parent="parent_value",
                    conversation_profile="conversation_profile_value",
                    session_id="session_id_value",
                )

                # Make the request
                response = await client.search_knowledge(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest, dict]]):
                The request object. The request message for
                [Conversations.SearchKnowledge][google.cloud.dialogflow.v2beta1.Conversations.SearchKnowledge].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.types.SearchKnowledgeResponse:
                The response message for
                   [Conversations.SearchKnowledge][google.cloud.dialogflow.v2beta1.Conversations.SearchKnowledge].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, conversation.SearchKnowledgeRequest):
            request = conversation.SearchKnowledgeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_knowledge
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

    async def generate_suggestions(
        self,
        request: Optional[
            Union[gcd_conversation.GenerateSuggestionsRequest, dict]
        ] = None,
        *,
        conversation: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> participant.GenerateSuggestionsResponse:
        r"""Generates all the suggestions using generators
        configured in the conversation profile. A generator is
        used only if its trigger event is matched.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            async def sample_generate_suggestions():
                # Create a client
                client = dialogflow_v2beta1.ConversationsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.GenerateSuggestionsRequest(
                    conversation="conversation_value",
                )

                # Make the request
                response = await client.generate_suggestions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsRequest, dict]]):
                The request object. The request message for
                [Conversations.GenerateSuggestions][google.cloud.dialogflow.v2beta1.Conversations.GenerateSuggestions].
            conversation (:class:`str`):
                Required. The conversation for which the suggestions are
                generated. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                The conversation must be created with a conversation
                profile which has generators configured in it to be able
                to get suggestions.

                This corresponds to the ``conversation`` field
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
            google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsResponse:
                The response message for
                   [Conversations.GenerateSuggestions][google.cloud.dialogflow.v2beta1.Conversations.GenerateSuggestions].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation]
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
        if not isinstance(request, gcd_conversation.GenerateSuggestionsRequest):
            request = gcd_conversation.GenerateSuggestionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if conversation is not None:
            request.conversation = conversation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_suggestions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation", request.conversation),)
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

    async def __aenter__(self) -> "ConversationsAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("ConversationsAsyncClient",)
