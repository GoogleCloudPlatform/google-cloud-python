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
import json
import logging as std_logging
import pickle
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

import google.auth  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.contact_center_insights_v1.types import (
    contact_center_insights,
    resources,
)

from .base import DEFAULT_CLIENT_INFO, ContactCenterInsightsTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class _LoggingClientInterceptor(grpc.UnaryUnaryClientInterceptor):  # pragma: NO COVER
    def intercept_unary_unary(self, continuation, client_call_details, request):
        logging_enabled = CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        )
        if logging_enabled:  # pragma: NO COVER
            request_metadata = client_call_details.metadata
            if isinstance(request, proto.Message):
                request_payload = type(request).to_json(request)
            elif isinstance(request, google.protobuf.message.Message):
                request_payload = MessageToJson(request)
            else:
                request_payload = f"{type(request).__name__}: {pickle.dumps(request)!r}"

            request_metadata = {
                key: value.decode("utf-8") if isinstance(value, bytes) else value
                for key, value in request_metadata
            }
            grpc_request = {
                "payload": request_payload,
                "requestMethod": "grpc",
                "metadata": dict(request_metadata),
            }
            _LOGGER.debug(
                f"Sending request for {client_call_details.method}",
                extra={
                    "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                    "rpcName": str(client_call_details.method),
                    "request": grpc_request,
                    "metadata": grpc_request["metadata"],
                },
            )
        response = continuation(client_call_details, request)
        if logging_enabled:  # pragma: NO COVER
            response_metadata = response.trailing_metadata()
            # Convert gRPC metadata `<class 'grpc.aio._metadata.Metadata'>` to list of tuples
            metadata = (
                dict([(k, str(v)) for k, v in response_metadata])
                if response_metadata
                else None
            )
            result = response.result()
            if isinstance(result, proto.Message):
                response_payload = type(result).to_json(result)
            elif isinstance(result, google.protobuf.message.Message):
                response_payload = MessageToJson(result)
            else:
                response_payload = f"{type(result).__name__}: {pickle.dumps(result)!r}"
            grpc_response = {
                "payload": response_payload,
                "metadata": metadata,
                "status": "OK",
            }
            _LOGGER.debug(
                f"Received response for {client_call_details.method}.",
                extra={
                    "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ContactCenterInsightsGrpcTransport(ContactCenterInsightsTransport):
    """gRPC backend transport for ContactCenterInsights.

    An API that lets users analyze and explore their business
    conversation data.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "contactcenterinsights.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'contactcenterinsights.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
                This argument will be removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if a ``channel`` instance is provided.
            channel (Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]]):
                A ``Channel`` instance through which to make calls, or a Callable
                that constructs and returns one. If set to None, ``self.create_channel``
                is used to create the channel. If a Callable is given, it will be called
                with the same arguments as used in ``self.create_channel``.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if a ``channel`` instance is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if a ``channel`` instance or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, grpc.Channel):
            # Ignore credentials if a channel was passed.
            credentials = None
            self._ignore_credentials = True
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            # initialize with the provided callable or the default channel
            channel_init = channel or type(self).create_channel
            self._grpc_channel = channel_init(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        self._interceptor = _LoggingClientInterceptor()
        self._logged_channel = grpc.intercept_channel(
            self._grpc_channel, self._interceptor
        )

        # Wrap messages. This must be done after self._logged_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "contactcenterinsights.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.  This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(
                self._logged_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def create_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.CreateConversationRequest], resources.Conversation
    ]:
        r"""Return a callable for the create conversation method over gRPC.

        Creates a conversation. Note that this method does not support
        audio transcription or redaction. Use ``conversations.upload``
        instead.

        Returns:
            Callable[[~.CreateConversationRequest],
                    ~.Conversation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_conversation" not in self._stubs:
            self._stubs["create_conversation"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateConversation",
                request_serializer=contact_center_insights.CreateConversationRequest.serialize,
                response_deserializer=resources.Conversation.deserialize,
            )
        return self._stubs["create_conversation"]

    @property
    def upload_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.UploadConversationRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the upload conversation method over gRPC.

        Create a long-running conversation upload operation. This method
        differs from ``CreateConversation`` by allowing audio
        transcription and optional DLP redaction.

        Returns:
            Callable[[~.UploadConversationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "upload_conversation" not in self._stubs:
            self._stubs["upload_conversation"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UploadConversation",
                request_serializer=contact_center_insights.UploadConversationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["upload_conversation"]

    @property
    def update_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateConversationRequest], resources.Conversation
    ]:
        r"""Return a callable for the update conversation method over gRPC.

        Updates a conversation.

        Returns:
            Callable[[~.UpdateConversationRequest],
                    ~.Conversation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_conversation" not in self._stubs:
            self._stubs["update_conversation"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateConversation",
                request_serializer=contact_center_insights.UpdateConversationRequest.serialize,
                response_deserializer=resources.Conversation.deserialize,
            )
        return self._stubs["update_conversation"]

    @property
    def get_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.GetConversationRequest], resources.Conversation
    ]:
        r"""Return a callable for the get conversation method over gRPC.

        Gets a conversation.

        Returns:
            Callable[[~.GetConversationRequest],
                    ~.Conversation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_conversation" not in self._stubs:
            self._stubs["get_conversation"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetConversation",
                request_serializer=contact_center_insights.GetConversationRequest.serialize,
                response_deserializer=resources.Conversation.deserialize,
            )
        return self._stubs["get_conversation"]

    @property
    def list_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.ListConversationsRequest],
        contact_center_insights.ListConversationsResponse,
    ]:
        r"""Return a callable for the list conversations method over gRPC.

        Lists conversations.

        Returns:
            Callable[[~.ListConversationsRequest],
                    ~.ListConversationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_conversations" not in self._stubs:
            self._stubs["list_conversations"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListConversations",
                request_serializer=contact_center_insights.ListConversationsRequest.serialize,
                response_deserializer=contact_center_insights.ListConversationsResponse.deserialize,
            )
        return self._stubs["list_conversations"]

    @property
    def delete_conversation(
        self,
    ) -> Callable[[contact_center_insights.DeleteConversationRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete conversation method over gRPC.

        Deletes a conversation.

        Returns:
            Callable[[~.DeleteConversationRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_conversation" not in self._stubs:
            self._stubs["delete_conversation"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteConversation",
                request_serializer=contact_center_insights.DeleteConversationRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_conversation"]

    @property
    def create_analysis(
        self,
    ) -> Callable[
        [contact_center_insights.CreateAnalysisRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create analysis method over gRPC.

        Creates an analysis. The long running operation is
        done when the analysis has completed.

        Returns:
            Callable[[~.CreateAnalysisRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_analysis" not in self._stubs:
            self._stubs["create_analysis"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateAnalysis",
                request_serializer=contact_center_insights.CreateAnalysisRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_analysis"]

    @property
    def get_analysis(
        self,
    ) -> Callable[[contact_center_insights.GetAnalysisRequest], resources.Analysis]:
        r"""Return a callable for the get analysis method over gRPC.

        Gets an analysis.

        Returns:
            Callable[[~.GetAnalysisRequest],
                    ~.Analysis]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_analysis" not in self._stubs:
            self._stubs["get_analysis"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetAnalysis",
                request_serializer=contact_center_insights.GetAnalysisRequest.serialize,
                response_deserializer=resources.Analysis.deserialize,
            )
        return self._stubs["get_analysis"]

    @property
    def list_analyses(
        self,
    ) -> Callable[
        [contact_center_insights.ListAnalysesRequest],
        contact_center_insights.ListAnalysesResponse,
    ]:
        r"""Return a callable for the list analyses method over gRPC.

        Lists analyses.

        Returns:
            Callable[[~.ListAnalysesRequest],
                    ~.ListAnalysesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_analyses" not in self._stubs:
            self._stubs["list_analyses"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListAnalyses",
                request_serializer=contact_center_insights.ListAnalysesRequest.serialize,
                response_deserializer=contact_center_insights.ListAnalysesResponse.deserialize,
            )
        return self._stubs["list_analyses"]

    @property
    def delete_analysis(
        self,
    ) -> Callable[[contact_center_insights.DeleteAnalysisRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete analysis method over gRPC.

        Deletes an analysis.

        Returns:
            Callable[[~.DeleteAnalysisRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_analysis" not in self._stubs:
            self._stubs["delete_analysis"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteAnalysis",
                request_serializer=contact_center_insights.DeleteAnalysisRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_analysis"]

    @property
    def bulk_analyze_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.BulkAnalyzeConversationsRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the bulk analyze conversations method over gRPC.

        Analyzes multiple conversations in a single request.

        Returns:
            Callable[[~.BulkAnalyzeConversationsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "bulk_analyze_conversations" not in self._stubs:
            self._stubs["bulk_analyze_conversations"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/BulkAnalyzeConversations",
                    request_serializer=contact_center_insights.BulkAnalyzeConversationsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["bulk_analyze_conversations"]

    @property
    def bulk_delete_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.BulkDeleteConversationsRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the bulk delete conversations method over gRPC.

        Deletes multiple conversations in a single request.

        Returns:
            Callable[[~.BulkDeleteConversationsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "bulk_delete_conversations" not in self._stubs:
            self._stubs["bulk_delete_conversations"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/BulkDeleteConversations",
                request_serializer=contact_center_insights.BulkDeleteConversationsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["bulk_delete_conversations"]

    @property
    def ingest_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.IngestConversationsRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the ingest conversations method over gRPC.

        Imports conversations and processes them according to
        the user's configuration.

        Returns:
            Callable[[~.IngestConversationsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "ingest_conversations" not in self._stubs:
            self._stubs["ingest_conversations"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/IngestConversations",
                request_serializer=contact_center_insights.IngestConversationsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["ingest_conversations"]

    @property
    def export_insights_data(
        self,
    ) -> Callable[
        [contact_center_insights.ExportInsightsDataRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the export insights data method over gRPC.

        Export insights data to a destination defined in the
        request body.

        Returns:
            Callable[[~.ExportInsightsDataRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_insights_data" not in self._stubs:
            self._stubs["export_insights_data"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ExportInsightsData",
                request_serializer=contact_center_insights.ExportInsightsDataRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_insights_data"]

    @property
    def create_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.CreateIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create issue model method over gRPC.

        Creates an issue model.

        Returns:
            Callable[[~.CreateIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_issue_model" not in self._stubs:
            self._stubs["create_issue_model"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateIssueModel",
                request_serializer=contact_center_insights.CreateIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_issue_model"]

    @property
    def update_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateIssueModelRequest], resources.IssueModel
    ]:
        r"""Return a callable for the update issue model method over gRPC.

        Updates an issue model.

        Returns:
            Callable[[~.UpdateIssueModelRequest],
                    ~.IssueModel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_issue_model" not in self._stubs:
            self._stubs["update_issue_model"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateIssueModel",
                request_serializer=contact_center_insights.UpdateIssueModelRequest.serialize,
                response_deserializer=resources.IssueModel.deserialize,
            )
        return self._stubs["update_issue_model"]

    @property
    def get_issue_model(
        self,
    ) -> Callable[[contact_center_insights.GetIssueModelRequest], resources.IssueModel]:
        r"""Return a callable for the get issue model method over gRPC.

        Gets an issue model.

        Returns:
            Callable[[~.GetIssueModelRequest],
                    ~.IssueModel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_issue_model" not in self._stubs:
            self._stubs["get_issue_model"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetIssueModel",
                request_serializer=contact_center_insights.GetIssueModelRequest.serialize,
                response_deserializer=resources.IssueModel.deserialize,
            )
        return self._stubs["get_issue_model"]

    @property
    def list_issue_models(
        self,
    ) -> Callable[
        [contact_center_insights.ListIssueModelsRequest],
        contact_center_insights.ListIssueModelsResponse,
    ]:
        r"""Return a callable for the list issue models method over gRPC.

        Lists issue models.

        Returns:
            Callable[[~.ListIssueModelsRequest],
                    ~.ListIssueModelsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_issue_models" not in self._stubs:
            self._stubs["list_issue_models"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListIssueModels",
                request_serializer=contact_center_insights.ListIssueModelsRequest.serialize,
                response_deserializer=contact_center_insights.ListIssueModelsResponse.deserialize,
            )
        return self._stubs["list_issue_models"]

    @property
    def delete_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete issue model method over gRPC.

        Deletes an issue model.

        Returns:
            Callable[[~.DeleteIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_issue_model" not in self._stubs:
            self._stubs["delete_issue_model"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteIssueModel",
                request_serializer=contact_center_insights.DeleteIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_issue_model"]

    @property
    def deploy_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.DeployIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the deploy issue model method over gRPC.

        Deploys an issue model. Returns an error if a model
        is already deployed. An issue model can only be used in
        analysis after it has been deployed.

        Returns:
            Callable[[~.DeployIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_issue_model" not in self._stubs:
            self._stubs["deploy_issue_model"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeployIssueModel",
                request_serializer=contact_center_insights.DeployIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["deploy_issue_model"]

    @property
    def undeploy_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.UndeployIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the undeploy issue model method over gRPC.

        Undeploys an issue model.
        An issue model can not be used in analysis after it has
        been undeployed.

        Returns:
            Callable[[~.UndeployIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undeploy_issue_model" not in self._stubs:
            self._stubs["undeploy_issue_model"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UndeployIssueModel",
                request_serializer=contact_center_insights.UndeployIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undeploy_issue_model"]

    @property
    def export_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.ExportIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the export issue model method over gRPC.

        Exports an issue model to the provided destination.

        Returns:
            Callable[[~.ExportIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_issue_model" not in self._stubs:
            self._stubs["export_issue_model"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ExportIssueModel",
                request_serializer=contact_center_insights.ExportIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_issue_model"]

    @property
    def import_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.ImportIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the import issue model method over gRPC.

        Imports an issue model from a Cloud Storage bucket.

        Returns:
            Callable[[~.ImportIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_issue_model" not in self._stubs:
            self._stubs["import_issue_model"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ImportIssueModel",
                request_serializer=contact_center_insights.ImportIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_issue_model"]

    @property
    def get_issue(
        self,
    ) -> Callable[[contact_center_insights.GetIssueRequest], resources.Issue]:
        r"""Return a callable for the get issue method over gRPC.

        Gets an issue.

        Returns:
            Callable[[~.GetIssueRequest],
                    ~.Issue]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_issue" not in self._stubs:
            self._stubs["get_issue"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetIssue",
                request_serializer=contact_center_insights.GetIssueRequest.serialize,
                response_deserializer=resources.Issue.deserialize,
            )
        return self._stubs["get_issue"]

    @property
    def list_issues(
        self,
    ) -> Callable[
        [contact_center_insights.ListIssuesRequest],
        contact_center_insights.ListIssuesResponse,
    ]:
        r"""Return a callable for the list issues method over gRPC.

        Lists issues.

        Returns:
            Callable[[~.ListIssuesRequest],
                    ~.ListIssuesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_issues" not in self._stubs:
            self._stubs["list_issues"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListIssues",
                request_serializer=contact_center_insights.ListIssuesRequest.serialize,
                response_deserializer=contact_center_insights.ListIssuesResponse.deserialize,
            )
        return self._stubs["list_issues"]

    @property
    def update_issue(
        self,
    ) -> Callable[[contact_center_insights.UpdateIssueRequest], resources.Issue]:
        r"""Return a callable for the update issue method over gRPC.

        Updates an issue.

        Returns:
            Callable[[~.UpdateIssueRequest],
                    ~.Issue]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_issue" not in self._stubs:
            self._stubs["update_issue"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateIssue",
                request_serializer=contact_center_insights.UpdateIssueRequest.serialize,
                response_deserializer=resources.Issue.deserialize,
            )
        return self._stubs["update_issue"]

    @property
    def delete_issue(
        self,
    ) -> Callable[[contact_center_insights.DeleteIssueRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete issue method over gRPC.

        Deletes an issue.

        Returns:
            Callable[[~.DeleteIssueRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_issue" not in self._stubs:
            self._stubs["delete_issue"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteIssue",
                request_serializer=contact_center_insights.DeleteIssueRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_issue"]

    @property
    def calculate_issue_model_stats(
        self,
    ) -> Callable[
        [contact_center_insights.CalculateIssueModelStatsRequest],
        contact_center_insights.CalculateIssueModelStatsResponse,
    ]:
        r"""Return a callable for the calculate issue model stats method over gRPC.

        Gets an issue model's statistics.

        Returns:
            Callable[[~.CalculateIssueModelStatsRequest],
                    ~.CalculateIssueModelStatsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "calculate_issue_model_stats" not in self._stubs:
            self._stubs["calculate_issue_model_stats"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CalculateIssueModelStats",
                    request_serializer=contact_center_insights.CalculateIssueModelStatsRequest.serialize,
                    response_deserializer=contact_center_insights.CalculateIssueModelStatsResponse.deserialize,
                )
            )
        return self._stubs["calculate_issue_model_stats"]

    @property
    def create_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.CreatePhraseMatcherRequest], resources.PhraseMatcher
    ]:
        r"""Return a callable for the create phrase matcher method over gRPC.

        Creates a phrase matcher.

        Returns:
            Callable[[~.CreatePhraseMatcherRequest],
                    ~.PhraseMatcher]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_phrase_matcher" not in self._stubs:
            self._stubs["create_phrase_matcher"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreatePhraseMatcher",
                request_serializer=contact_center_insights.CreatePhraseMatcherRequest.serialize,
                response_deserializer=resources.PhraseMatcher.deserialize,
            )
        return self._stubs["create_phrase_matcher"]

    @property
    def get_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.GetPhraseMatcherRequest], resources.PhraseMatcher
    ]:
        r"""Return a callable for the get phrase matcher method over gRPC.

        Gets a phrase matcher.

        Returns:
            Callable[[~.GetPhraseMatcherRequest],
                    ~.PhraseMatcher]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_phrase_matcher" not in self._stubs:
            self._stubs["get_phrase_matcher"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetPhraseMatcher",
                request_serializer=contact_center_insights.GetPhraseMatcherRequest.serialize,
                response_deserializer=resources.PhraseMatcher.deserialize,
            )
        return self._stubs["get_phrase_matcher"]

    @property
    def list_phrase_matchers(
        self,
    ) -> Callable[
        [contact_center_insights.ListPhraseMatchersRequest],
        contact_center_insights.ListPhraseMatchersResponse,
    ]:
        r"""Return a callable for the list phrase matchers method over gRPC.

        Lists phrase matchers.

        Returns:
            Callable[[~.ListPhraseMatchersRequest],
                    ~.ListPhraseMatchersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_phrase_matchers" not in self._stubs:
            self._stubs["list_phrase_matchers"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListPhraseMatchers",
                request_serializer=contact_center_insights.ListPhraseMatchersRequest.serialize,
                response_deserializer=contact_center_insights.ListPhraseMatchersResponse.deserialize,
            )
        return self._stubs["list_phrase_matchers"]

    @property
    def delete_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.DeletePhraseMatcherRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete phrase matcher method over gRPC.

        Deletes a phrase matcher.

        Returns:
            Callable[[~.DeletePhraseMatcherRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_phrase_matcher" not in self._stubs:
            self._stubs["delete_phrase_matcher"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeletePhraseMatcher",
                request_serializer=contact_center_insights.DeletePhraseMatcherRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_phrase_matcher"]

    @property
    def update_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.UpdatePhraseMatcherRequest], resources.PhraseMatcher
    ]:
        r"""Return a callable for the update phrase matcher method over gRPC.

        Updates a phrase matcher.

        Returns:
            Callable[[~.UpdatePhraseMatcherRequest],
                    ~.PhraseMatcher]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_phrase_matcher" not in self._stubs:
            self._stubs["update_phrase_matcher"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdatePhraseMatcher",
                request_serializer=contact_center_insights.UpdatePhraseMatcherRequest.serialize,
                response_deserializer=resources.PhraseMatcher.deserialize,
            )
        return self._stubs["update_phrase_matcher"]

    @property
    def calculate_stats(
        self,
    ) -> Callable[
        [contact_center_insights.CalculateStatsRequest],
        contact_center_insights.CalculateStatsResponse,
    ]:
        r"""Return a callable for the calculate stats method over gRPC.

        Gets conversation statistics.

        Returns:
            Callable[[~.CalculateStatsRequest],
                    ~.CalculateStatsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "calculate_stats" not in self._stubs:
            self._stubs["calculate_stats"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CalculateStats",
                request_serializer=contact_center_insights.CalculateStatsRequest.serialize,
                response_deserializer=contact_center_insights.CalculateStatsResponse.deserialize,
            )
        return self._stubs["calculate_stats"]

    @property
    def get_settings(
        self,
    ) -> Callable[[contact_center_insights.GetSettingsRequest], resources.Settings]:
        r"""Return a callable for the get settings method over gRPC.

        Gets project-level settings.

        Returns:
            Callable[[~.GetSettingsRequest],
                    ~.Settings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_settings" not in self._stubs:
            self._stubs["get_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetSettings",
                request_serializer=contact_center_insights.GetSettingsRequest.serialize,
                response_deserializer=resources.Settings.deserialize,
            )
        return self._stubs["get_settings"]

    @property
    def update_settings(
        self,
    ) -> Callable[[contact_center_insights.UpdateSettingsRequest], resources.Settings]:
        r"""Return a callable for the update settings method over gRPC.

        Updates project-level settings.

        Returns:
            Callable[[~.UpdateSettingsRequest],
                    ~.Settings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_settings" not in self._stubs:
            self._stubs["update_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateSettings",
                request_serializer=contact_center_insights.UpdateSettingsRequest.serialize,
                response_deserializer=resources.Settings.deserialize,
            )
        return self._stubs["update_settings"]

    @property
    def create_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.CreateAnalysisRuleRequest], resources.AnalysisRule
    ]:
        r"""Return a callable for the create analysis rule method over gRPC.

        Creates a analysis rule.

        Returns:
            Callable[[~.CreateAnalysisRuleRequest],
                    ~.AnalysisRule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_analysis_rule" not in self._stubs:
            self._stubs["create_analysis_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateAnalysisRule",
                request_serializer=contact_center_insights.CreateAnalysisRuleRequest.serialize,
                response_deserializer=resources.AnalysisRule.deserialize,
            )
        return self._stubs["create_analysis_rule"]

    @property
    def get_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.GetAnalysisRuleRequest], resources.AnalysisRule
    ]:
        r"""Return a callable for the get analysis rule method over gRPC.

        Get a analysis rule.

        Returns:
            Callable[[~.GetAnalysisRuleRequest],
                    ~.AnalysisRule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_analysis_rule" not in self._stubs:
            self._stubs["get_analysis_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetAnalysisRule",
                request_serializer=contact_center_insights.GetAnalysisRuleRequest.serialize,
                response_deserializer=resources.AnalysisRule.deserialize,
            )
        return self._stubs["get_analysis_rule"]

    @property
    def list_analysis_rules(
        self,
    ) -> Callable[
        [contact_center_insights.ListAnalysisRulesRequest],
        contact_center_insights.ListAnalysisRulesResponse,
    ]:
        r"""Return a callable for the list analysis rules method over gRPC.

        Lists analysis rules.

        Returns:
            Callable[[~.ListAnalysisRulesRequest],
                    ~.ListAnalysisRulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_analysis_rules" not in self._stubs:
            self._stubs["list_analysis_rules"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListAnalysisRules",
                request_serializer=contact_center_insights.ListAnalysisRulesRequest.serialize,
                response_deserializer=contact_center_insights.ListAnalysisRulesResponse.deserialize,
            )
        return self._stubs["list_analysis_rules"]

    @property
    def update_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateAnalysisRuleRequest], resources.AnalysisRule
    ]:
        r"""Return a callable for the update analysis rule method over gRPC.

        Updates a analysis rule.

        Returns:
            Callable[[~.UpdateAnalysisRuleRequest],
                    ~.AnalysisRule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_analysis_rule" not in self._stubs:
            self._stubs["update_analysis_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateAnalysisRule",
                request_serializer=contact_center_insights.UpdateAnalysisRuleRequest.serialize,
                response_deserializer=resources.AnalysisRule.deserialize,
            )
        return self._stubs["update_analysis_rule"]

    @property
    def delete_analysis_rule(
        self,
    ) -> Callable[[contact_center_insights.DeleteAnalysisRuleRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete analysis rule method over gRPC.

        Deletes a analysis rule.

        Returns:
            Callable[[~.DeleteAnalysisRuleRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_analysis_rule" not in self._stubs:
            self._stubs["delete_analysis_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteAnalysisRule",
                request_serializer=contact_center_insights.DeleteAnalysisRuleRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_analysis_rule"]

    @property
    def get_encryption_spec(
        self,
    ) -> Callable[
        [contact_center_insights.GetEncryptionSpecRequest], resources.EncryptionSpec
    ]:
        r"""Return a callable for the get encryption spec method over gRPC.

        Gets location-level encryption key specification.

        Returns:
            Callable[[~.GetEncryptionSpecRequest],
                    ~.EncryptionSpec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_encryption_spec" not in self._stubs:
            self._stubs["get_encryption_spec"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetEncryptionSpec",
                request_serializer=contact_center_insights.GetEncryptionSpecRequest.serialize,
                response_deserializer=resources.EncryptionSpec.deserialize,
            )
        return self._stubs["get_encryption_spec"]

    @property
    def initialize_encryption_spec(
        self,
    ) -> Callable[
        [contact_center_insights.InitializeEncryptionSpecRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the initialize encryption spec method over gRPC.

        Initializes a location-level encryption key
        specification. An error will result if the location has
        resources already created before the initialization.
        After the encryption specification is initialized at a
        location, it is immutable and all newly created
        resources under the location will be encrypted with the
        existing specification.

        Returns:
            Callable[[~.InitializeEncryptionSpecRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "initialize_encryption_spec" not in self._stubs:
            self._stubs["initialize_encryption_spec"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/InitializeEncryptionSpec",
                    request_serializer=contact_center_insights.InitializeEncryptionSpecRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["initialize_encryption_spec"]

    @property
    def create_view(
        self,
    ) -> Callable[[contact_center_insights.CreateViewRequest], resources.View]:
        r"""Return a callable for the create view method over gRPC.

        Creates a view.

        Returns:
            Callable[[~.CreateViewRequest],
                    ~.View]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_view" not in self._stubs:
            self._stubs["create_view"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateView",
                request_serializer=contact_center_insights.CreateViewRequest.serialize,
                response_deserializer=resources.View.deserialize,
            )
        return self._stubs["create_view"]

    @property
    def get_view(
        self,
    ) -> Callable[[contact_center_insights.GetViewRequest], resources.View]:
        r"""Return a callable for the get view method over gRPC.

        Gets a view.

        Returns:
            Callable[[~.GetViewRequest],
                    ~.View]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_view" not in self._stubs:
            self._stubs["get_view"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetView",
                request_serializer=contact_center_insights.GetViewRequest.serialize,
                response_deserializer=resources.View.deserialize,
            )
        return self._stubs["get_view"]

    @property
    def list_views(
        self,
    ) -> Callable[
        [contact_center_insights.ListViewsRequest],
        contact_center_insights.ListViewsResponse,
    ]:
        r"""Return a callable for the list views method over gRPC.

        Lists views.

        Returns:
            Callable[[~.ListViewsRequest],
                    ~.ListViewsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_views" not in self._stubs:
            self._stubs["list_views"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListViews",
                request_serializer=contact_center_insights.ListViewsRequest.serialize,
                response_deserializer=contact_center_insights.ListViewsResponse.deserialize,
            )
        return self._stubs["list_views"]

    @property
    def update_view(
        self,
    ) -> Callable[[contact_center_insights.UpdateViewRequest], resources.View]:
        r"""Return a callable for the update view method over gRPC.

        Updates a view.

        Returns:
            Callable[[~.UpdateViewRequest],
                    ~.View]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_view" not in self._stubs:
            self._stubs["update_view"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateView",
                request_serializer=contact_center_insights.UpdateViewRequest.serialize,
                response_deserializer=resources.View.deserialize,
            )
        return self._stubs["update_view"]

    @property
    def delete_view(
        self,
    ) -> Callable[[contact_center_insights.DeleteViewRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete view method over gRPC.

        Deletes a view.

        Returns:
            Callable[[~.DeleteViewRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_view" not in self._stubs:
            self._stubs["delete_view"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteView",
                request_serializer=contact_center_insights.DeleteViewRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_view"]

    @property
    def query_metrics(
        self,
    ) -> Callable[
        [contact_center_insights.QueryMetricsRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the query metrics method over gRPC.

        Query metrics.

        Returns:
            Callable[[~.QueryMetricsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_metrics" not in self._stubs:
            self._stubs["query_metrics"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/QueryMetrics",
                request_serializer=contact_center_insights.QueryMetricsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["query_metrics"]

    @property
    def create_qa_question(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaQuestionRequest], resources.QaQuestion
    ]:
        r"""Return a callable for the create qa question method over gRPC.

        Create a QaQuestion.

        Returns:
            Callable[[~.CreateQaQuestionRequest],
                    ~.QaQuestion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_qa_question" not in self._stubs:
            self._stubs["create_qa_question"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateQaQuestion",
                request_serializer=contact_center_insights.CreateQaQuestionRequest.serialize,
                response_deserializer=resources.QaQuestion.deserialize,
            )
        return self._stubs["create_qa_question"]

    @property
    def get_qa_question(
        self,
    ) -> Callable[[contact_center_insights.GetQaQuestionRequest], resources.QaQuestion]:
        r"""Return a callable for the get qa question method over gRPC.

        Gets a QaQuestion.

        Returns:
            Callable[[~.GetQaQuestionRequest],
                    ~.QaQuestion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_qa_question" not in self._stubs:
            self._stubs["get_qa_question"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetQaQuestion",
                request_serializer=contact_center_insights.GetQaQuestionRequest.serialize,
                response_deserializer=resources.QaQuestion.deserialize,
            )
        return self._stubs["get_qa_question"]

    @property
    def update_qa_question(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateQaQuestionRequest], resources.QaQuestion
    ]:
        r"""Return a callable for the update qa question method over gRPC.

        Updates a QaQuestion.

        Returns:
            Callable[[~.UpdateQaQuestionRequest],
                    ~.QaQuestion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_qa_question" not in self._stubs:
            self._stubs["update_qa_question"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateQaQuestion",
                request_serializer=contact_center_insights.UpdateQaQuestionRequest.serialize,
                response_deserializer=resources.QaQuestion.deserialize,
            )
        return self._stubs["update_qa_question"]

    @property
    def delete_qa_question(
        self,
    ) -> Callable[[contact_center_insights.DeleteQaQuestionRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete qa question method over gRPC.

        Deletes a QaQuestion.

        Returns:
            Callable[[~.DeleteQaQuestionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_qa_question" not in self._stubs:
            self._stubs["delete_qa_question"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteQaQuestion",
                request_serializer=contact_center_insights.DeleteQaQuestionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_qa_question"]

    @property
    def list_qa_questions(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaQuestionsRequest],
        contact_center_insights.ListQaQuestionsResponse,
    ]:
        r"""Return a callable for the list qa questions method over gRPC.

        Lists QaQuestions.

        Returns:
            Callable[[~.ListQaQuestionsRequest],
                    ~.ListQaQuestionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_qa_questions" not in self._stubs:
            self._stubs["list_qa_questions"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListQaQuestions",
                request_serializer=contact_center_insights.ListQaQuestionsRequest.serialize,
                response_deserializer=contact_center_insights.ListQaQuestionsResponse.deserialize,
            )
        return self._stubs["list_qa_questions"]

    @property
    def create_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaScorecardRequest], resources.QaScorecard
    ]:
        r"""Return a callable for the create qa scorecard method over gRPC.

        Create a QaScorecard.

        Returns:
            Callable[[~.CreateQaScorecardRequest],
                    ~.QaScorecard]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_qa_scorecard" not in self._stubs:
            self._stubs["create_qa_scorecard"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateQaScorecard",
                request_serializer=contact_center_insights.CreateQaScorecardRequest.serialize,
                response_deserializer=resources.QaScorecard.deserialize,
            )
        return self._stubs["create_qa_scorecard"]

    @property
    def get_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.GetQaScorecardRequest], resources.QaScorecard
    ]:
        r"""Return a callable for the get qa scorecard method over gRPC.

        Gets a QaScorecard.

        Returns:
            Callable[[~.GetQaScorecardRequest],
                    ~.QaScorecard]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_qa_scorecard" not in self._stubs:
            self._stubs["get_qa_scorecard"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetQaScorecard",
                request_serializer=contact_center_insights.GetQaScorecardRequest.serialize,
                response_deserializer=resources.QaScorecard.deserialize,
            )
        return self._stubs["get_qa_scorecard"]

    @property
    def update_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateQaScorecardRequest], resources.QaScorecard
    ]:
        r"""Return a callable for the update qa scorecard method over gRPC.

        Updates a QaScorecard.

        Returns:
            Callable[[~.UpdateQaScorecardRequest],
                    ~.QaScorecard]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_qa_scorecard" not in self._stubs:
            self._stubs["update_qa_scorecard"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateQaScorecard",
                request_serializer=contact_center_insights.UpdateQaScorecardRequest.serialize,
                response_deserializer=resources.QaScorecard.deserialize,
            )
        return self._stubs["update_qa_scorecard"]

    @property
    def delete_qa_scorecard(
        self,
    ) -> Callable[[contact_center_insights.DeleteQaScorecardRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete qa scorecard method over gRPC.

        Deletes a QaScorecard.

        Returns:
            Callable[[~.DeleteQaScorecardRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_qa_scorecard" not in self._stubs:
            self._stubs["delete_qa_scorecard"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteQaScorecard",
                request_serializer=contact_center_insights.DeleteQaScorecardRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_qa_scorecard"]

    @property
    def list_qa_scorecards(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaScorecardsRequest],
        contact_center_insights.ListQaScorecardsResponse,
    ]:
        r"""Return a callable for the list qa scorecards method over gRPC.

        Lists QaScorecards.

        Returns:
            Callable[[~.ListQaScorecardsRequest],
                    ~.ListQaScorecardsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_qa_scorecards" not in self._stubs:
            self._stubs["list_qa_scorecards"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListQaScorecards",
                request_serializer=contact_center_insights.ListQaScorecardsRequest.serialize,
                response_deserializer=contact_center_insights.ListQaScorecardsResponse.deserialize,
            )
        return self._stubs["list_qa_scorecards"]

    @property
    def create_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaScorecardRevisionRequest],
        resources.QaScorecardRevision,
    ]:
        r"""Return a callable for the create qa scorecard revision method over gRPC.

        Creates a QaScorecardRevision.

        Returns:
            Callable[[~.CreateQaScorecardRevisionRequest],
                    ~.QaScorecardRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_qa_scorecard_revision" not in self._stubs:
            self._stubs["create_qa_scorecard_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateQaScorecardRevision",
                    request_serializer=contact_center_insights.CreateQaScorecardRevisionRequest.serialize,
                    response_deserializer=resources.QaScorecardRevision.deserialize,
                )
            )
        return self._stubs["create_qa_scorecard_revision"]

    @property
    def get_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.GetQaScorecardRevisionRequest],
        resources.QaScorecardRevision,
    ]:
        r"""Return a callable for the get qa scorecard revision method over gRPC.

        Gets a QaScorecardRevision.

        Returns:
            Callable[[~.GetQaScorecardRevisionRequest],
                    ~.QaScorecardRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_qa_scorecard_revision" not in self._stubs:
            self._stubs["get_qa_scorecard_revision"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetQaScorecardRevision",
                request_serializer=contact_center_insights.GetQaScorecardRevisionRequest.serialize,
                response_deserializer=resources.QaScorecardRevision.deserialize,
            )
        return self._stubs["get_qa_scorecard_revision"]

    @property
    def tune_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.TuneQaScorecardRevisionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the tune qa scorecard revision method over gRPC.

        Fine tune one or more QaModels.

        Returns:
            Callable[[~.TuneQaScorecardRevisionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "tune_qa_scorecard_revision" not in self._stubs:
            self._stubs["tune_qa_scorecard_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/TuneQaScorecardRevision",
                    request_serializer=contact_center_insights.TuneQaScorecardRevisionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["tune_qa_scorecard_revision"]

    @property
    def deploy_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.DeployQaScorecardRevisionRequest],
        resources.QaScorecardRevision,
    ]:
        r"""Return a callable for the deploy qa scorecard revision method over gRPC.

        Deploy a QaScorecardRevision.

        Returns:
            Callable[[~.DeployQaScorecardRevisionRequest],
                    ~.QaScorecardRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_qa_scorecard_revision" not in self._stubs:
            self._stubs["deploy_qa_scorecard_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeployQaScorecardRevision",
                    request_serializer=contact_center_insights.DeployQaScorecardRevisionRequest.serialize,
                    response_deserializer=resources.QaScorecardRevision.deserialize,
                )
            )
        return self._stubs["deploy_qa_scorecard_revision"]

    @property
    def undeploy_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.UndeployQaScorecardRevisionRequest],
        resources.QaScorecardRevision,
    ]:
        r"""Return a callable for the undeploy qa scorecard revision method over gRPC.

        Undeploy a QaScorecardRevision.

        Returns:
            Callable[[~.UndeployQaScorecardRevisionRequest],
                    ~.QaScorecardRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undeploy_qa_scorecard_revision" not in self._stubs:
            self._stubs["undeploy_qa_scorecard_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UndeployQaScorecardRevision",
                    request_serializer=contact_center_insights.UndeployQaScorecardRevisionRequest.serialize,
                    response_deserializer=resources.QaScorecardRevision.deserialize,
                )
            )
        return self._stubs["undeploy_qa_scorecard_revision"]

    @property
    def delete_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteQaScorecardRevisionRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete qa scorecard revision method over gRPC.

        Deletes a QaScorecardRevision.

        Returns:
            Callable[[~.DeleteQaScorecardRevisionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_qa_scorecard_revision" not in self._stubs:
            self._stubs["delete_qa_scorecard_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteQaScorecardRevision",
                    request_serializer=contact_center_insights.DeleteQaScorecardRevisionRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_qa_scorecard_revision"]

    @property
    def list_qa_scorecard_revisions(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaScorecardRevisionsRequest],
        contact_center_insights.ListQaScorecardRevisionsResponse,
    ]:
        r"""Return a callable for the list qa scorecard revisions method over gRPC.

        Lists all revisions under the parent QaScorecard.

        Returns:
            Callable[[~.ListQaScorecardRevisionsRequest],
                    ~.ListQaScorecardRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_qa_scorecard_revisions" not in self._stubs:
            self._stubs["list_qa_scorecard_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListQaScorecardRevisions",
                    request_serializer=contact_center_insights.ListQaScorecardRevisionsRequest.serialize,
                    response_deserializer=contact_center_insights.ListQaScorecardRevisionsResponse.deserialize,
                )
            )
        return self._stubs["list_qa_scorecard_revisions"]

    @property
    def create_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.CreateFeedbackLabelRequest], resources.FeedbackLabel
    ]:
        r"""Return a callable for the create feedback label method over gRPC.

        Create feedback label.

        Returns:
            Callable[[~.CreateFeedbackLabelRequest],
                    ~.FeedbackLabel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_feedback_label" not in self._stubs:
            self._stubs["create_feedback_label"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateFeedbackLabel",
                request_serializer=contact_center_insights.CreateFeedbackLabelRequest.serialize,
                response_deserializer=resources.FeedbackLabel.deserialize,
            )
        return self._stubs["create_feedback_label"]

    @property
    def list_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.ListFeedbackLabelsRequest],
        contact_center_insights.ListFeedbackLabelsResponse,
    ]:
        r"""Return a callable for the list feedback labels method over gRPC.

        List feedback labels.

        Returns:
            Callable[[~.ListFeedbackLabelsRequest],
                    ~.ListFeedbackLabelsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_feedback_labels" not in self._stubs:
            self._stubs["list_feedback_labels"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListFeedbackLabels",
                request_serializer=contact_center_insights.ListFeedbackLabelsRequest.serialize,
                response_deserializer=contact_center_insights.ListFeedbackLabelsResponse.deserialize,
            )
        return self._stubs["list_feedback_labels"]

    @property
    def get_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.GetFeedbackLabelRequest], resources.FeedbackLabel
    ]:
        r"""Return a callable for the get feedback label method over gRPC.

        Get feedback label.

        Returns:
            Callable[[~.GetFeedbackLabelRequest],
                    ~.FeedbackLabel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_feedback_label" not in self._stubs:
            self._stubs["get_feedback_label"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetFeedbackLabel",
                request_serializer=contact_center_insights.GetFeedbackLabelRequest.serialize,
                response_deserializer=resources.FeedbackLabel.deserialize,
            )
        return self._stubs["get_feedback_label"]

    @property
    def update_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateFeedbackLabelRequest], resources.FeedbackLabel
    ]:
        r"""Return a callable for the update feedback label method over gRPC.

        Update feedback label.

        Returns:
            Callable[[~.UpdateFeedbackLabelRequest],
                    ~.FeedbackLabel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_feedback_label" not in self._stubs:
            self._stubs["update_feedback_label"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateFeedbackLabel",
                request_serializer=contact_center_insights.UpdateFeedbackLabelRequest.serialize,
                response_deserializer=resources.FeedbackLabel.deserialize,
            )
        return self._stubs["update_feedback_label"]

    @property
    def delete_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteFeedbackLabelRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete feedback label method over gRPC.

        Delete feedback label.

        Returns:
            Callable[[~.DeleteFeedbackLabelRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_feedback_label" not in self._stubs:
            self._stubs["delete_feedback_label"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteFeedbackLabel",
                request_serializer=contact_center_insights.DeleteFeedbackLabelRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_feedback_label"]

    @property
    def list_all_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.ListAllFeedbackLabelsRequest],
        contact_center_insights.ListAllFeedbackLabelsResponse,
    ]:
        r"""Return a callable for the list all feedback labels method over gRPC.

        List all feedback labels by project number.

        Returns:
            Callable[[~.ListAllFeedbackLabelsRequest],
                    ~.ListAllFeedbackLabelsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_all_feedback_labels" not in self._stubs:
            self._stubs["list_all_feedback_labels"] = self._logged_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListAllFeedbackLabels",
                request_serializer=contact_center_insights.ListAllFeedbackLabelsRequest.serialize,
                response_deserializer=contact_center_insights.ListAllFeedbackLabelsResponse.deserialize,
            )
        return self._stubs["list_all_feedback_labels"]

    @property
    def bulk_upload_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.BulkUploadFeedbackLabelsRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the bulk upload feedback labels method over gRPC.

        Upload feedback labels in bulk.

        Returns:
            Callable[[~.BulkUploadFeedbackLabelsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "bulk_upload_feedback_labels" not in self._stubs:
            self._stubs["bulk_upload_feedback_labels"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/BulkUploadFeedbackLabels",
                    request_serializer=contact_center_insights.BulkUploadFeedbackLabelsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["bulk_upload_feedback_labels"]

    @property
    def bulk_download_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.BulkDownloadFeedbackLabelsRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the bulk download feedback labels method over gRPC.

        Download feedback labels in bulk.

        Returns:
            Callable[[~.BulkDownloadFeedbackLabelsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "bulk_download_feedback_labels" not in self._stubs:
            self._stubs["bulk_download_feedback_labels"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/BulkDownloadFeedbackLabels",
                    request_serializer=contact_center_insights.BulkDownloadFeedbackLabelsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["bulk_download_feedback_labels"]

    def close(self):
        self._logged_channel.close()

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None]:
        r"""Return a callable for the cancel_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_operation" not in self._stubs:
            self._stubs["cancel_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/CancelOperation",
                request_serializer=operations_pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["cancel_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse
    ]:
        r"""Return a callable for the list_operations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("ContactCenterInsightsGrpcTransport",)
