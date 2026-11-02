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
import inspect
import json
import logging as std_logging
import pickle
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.agentidentity_v1beta.types import auth_provider_service

from .base import DEFAULT_CLIENT_INFO, AuthProviderServiceTransport
from .grpc import AuthProviderServiceGrpcTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class _LoggingClientAIOInterceptor(
    grpc.aio.UnaryUnaryClientInterceptor
):  # pragma: NO COVER
    async def intercept_unary_unary(self, continuation, client_call_details, request):
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
                    "serviceName": "google.cloud.agentidentity.v1beta.AuthProviderService",
                    "rpcName": str(client_call_details.method),
                    "request": grpc_request,
                    "metadata": grpc_request["metadata"],
                },
            )
        response = await continuation(client_call_details, request)
        if logging_enabled:  # pragma: NO COVER
            response_metadata = await response.trailing_metadata()
            # Convert gRPC metadata `<class 'grpc.aio._metadata.Metadata'>` to list of tuples
            metadata = (
                dict([(k, str(v)) for k, v in response_metadata])
                if response_metadata
                else None
            )
            result = await response
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
                f"Received response to rpc {client_call_details.method}.",
                extra={
                    "serviceName": "google.cloud.agentidentity.v1beta.AuthProviderService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AuthProviderServiceGrpcAsyncIOTransport(AuthProviderServiceTransport):
    """gRPC AsyncIO backend transport for AuthProviderService.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "agentidentity.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "agentidentity.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[aio.Channel, Callable[..., aio.Channel]]] = None,
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
                 The hostname to connect to (default: 'agentidentity.googleapis.com').
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
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[Union[aio.Channel, Callable[..., aio.Channel]]]):
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
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, aio.Channel):
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

        self._interceptor = _LoggingClientAIOInterceptor()
        self._grpc_channel._unary_unary_interceptors.append(self._interceptor)
        self._logged_channel = self._grpc_channel
        self._wrap_with_kind = (
            "kind" in inspect.signature(gapic_v1.method_async.wrap_method).parameters
        )
        # Wrap messages. This must be done after self._logged_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def list_auth_providers(
        self,
    ) -> Callable[
        [auth_provider_service.ListAuthProvidersRequest],
        Awaitable[auth_provider_service.ListAuthProvidersResponse],
    ]:
        r"""Return a callable for the list auth providers method over gRPC.

        Lists AuthProviders in a given project and location.

        Returns:
            Callable[[~.ListAuthProvidersRequest],
                    Awaitable[~.ListAuthProvidersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_auth_providers" not in self._stubs:
            self._stubs["list_auth_providers"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/ListAuthProviders",
                request_serializer=auth_provider_service.ListAuthProvidersRequest.serialize,
                response_deserializer=auth_provider_service.ListAuthProvidersResponse.deserialize,
            )
        return self._stubs["list_auth_providers"]

    @property
    def get_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.GetAuthProviderRequest],
        Awaitable[auth_provider_service.AuthProvider],
    ]:
        r"""Return a callable for the get auth provider method over gRPC.

        Gets details of a single AuthProvider.

        Returns:
            Callable[[~.GetAuthProviderRequest],
                    Awaitable[~.AuthProvider]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_auth_provider" not in self._stubs:
            self._stubs["get_auth_provider"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/GetAuthProvider",
                request_serializer=auth_provider_service.GetAuthProviderRequest.serialize,
                response_deserializer=auth_provider_service.AuthProvider.deserialize,
            )
        return self._stubs["get_auth_provider"]

    @property
    def create_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.CreateAuthProviderRequest],
        Awaitable[auth_provider_service.AuthProvider],
    ]:
        r"""Return a callable for the create auth provider method over gRPC.

        Creates a new AuthProvider in a given project and
        location.

        Returns:
            Callable[[~.CreateAuthProviderRequest],
                    Awaitable[~.AuthProvider]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_auth_provider" not in self._stubs:
            self._stubs["create_auth_provider"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/CreateAuthProvider",
                request_serializer=auth_provider_service.CreateAuthProviderRequest.serialize,
                response_deserializer=auth_provider_service.AuthProvider.deserialize,
            )
        return self._stubs["create_auth_provider"]

    @property
    def update_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.UpdateAuthProviderRequest],
        Awaitable[auth_provider_service.AuthProvider],
    ]:
        r"""Return a callable for the update auth provider method over gRPC.

        Updates the parameters of a single AuthProvider.

        Returns:
            Callable[[~.UpdateAuthProviderRequest],
                    Awaitable[~.AuthProvider]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_auth_provider" not in self._stubs:
            self._stubs["update_auth_provider"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/UpdateAuthProvider",
                request_serializer=auth_provider_service.UpdateAuthProviderRequest.serialize,
                response_deserializer=auth_provider_service.AuthProvider.deserialize,
            )
        return self._stubs["update_auth_provider"]

    @property
    def delete_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.DeleteAuthProviderRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete auth provider method over gRPC.

        Deletes a single AuthProvider.

        Returns:
            Callable[[~.DeleteAuthProviderRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_auth_provider" not in self._stubs:
            self._stubs["delete_auth_provider"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/DeleteAuthProvider",
                request_serializer=auth_provider_service.DeleteAuthProviderRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_auth_provider"]

    @property
    def undelete_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.UndeleteAuthProviderRequest],
        Awaitable[auth_provider_service.AuthProvider],
    ]:
        r"""Return a callable for the undelete auth provider method over gRPC.

        Undeletes a single AuthProvider.

        Returns:
            Callable[[~.UndeleteAuthProviderRequest],
                    Awaitable[~.AuthProvider]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undelete_auth_provider" not in self._stubs:
            self._stubs["undelete_auth_provider"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/UndeleteAuthProvider",
                request_serializer=auth_provider_service.UndeleteAuthProviderRequest.serialize,
                response_deserializer=auth_provider_service.AuthProvider.deserialize,
            )
        return self._stubs["undelete_auth_provider"]

    @property
    def query_auth_providers(
        self,
    ) -> Callable[
        [auth_provider_service.QueryAuthProvidersRequest],
        Awaitable[auth_provider_service.QueryAuthProvidersResponse],
    ]:
        r"""Return a callable for the query auth providers method over gRPC.

        Queries what all auth_providers are used by a given workload_id.

        Returns:
            Callable[[~.QueryAuthProvidersRequest],
                    Awaitable[~.QueryAuthProvidersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_auth_providers" not in self._stubs:
            self._stubs["query_auth_providers"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/QueryAuthProviders",
                request_serializer=auth_provider_service.QueryAuthProvidersRequest.serialize,
                response_deserializer=auth_provider_service.QueryAuthProvidersResponse.deserialize,
            )
        return self._stubs["query_auth_providers"]

    @property
    def query_workloads(
        self,
    ) -> Callable[
        [auth_provider_service.QueryWorkloadsRequest],
        Awaitable[auth_provider_service.QueryWorkloadsResponse],
    ]:
        r"""Return a callable for the query workloads method over gRPC.

        Queries what all workloads are using a given auth_provider.

        Returns:
            Callable[[~.QueryWorkloadsRequest],
                    Awaitable[~.QueryWorkloadsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_workloads" not in self._stubs:
            self._stubs["query_workloads"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/QueryWorkloads",
                request_serializer=auth_provider_service.QueryWorkloadsRequest.serialize,
                response_deserializer=auth_provider_service.QueryWorkloadsResponse.deserialize,
            )
        return self._stubs["query_workloads"]

    @property
    def list_authorizations(
        self,
    ) -> Callable[
        [auth_provider_service.ListAuthorizationsRequest],
        Awaitable[auth_provider_service.ListAuthorizationsResponse],
    ]:
        r"""Return a callable for the list authorizations method over gRPC.

        Lists Authorizations in a given project and location.

        Returns:
            Callable[[~.ListAuthorizationsRequest],
                    Awaitable[~.ListAuthorizationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_authorizations" not in self._stubs:
            self._stubs["list_authorizations"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/ListAuthorizations",
                request_serializer=auth_provider_service.ListAuthorizationsRequest.serialize,
                response_deserializer=auth_provider_service.ListAuthorizationsResponse.deserialize,
            )
        return self._stubs["list_authorizations"]

    @property
    def get_authorization(
        self,
    ) -> Callable[
        [auth_provider_service.GetAuthorizationRequest],
        Awaitable[auth_provider_service.Authorization],
    ]:
        r"""Return a callable for the get authorization method over gRPC.

        Gets details of a single Authorization.

        Returns:
            Callable[[~.GetAuthorizationRequest],
                    Awaitable[~.Authorization]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_authorization" not in self._stubs:
            self._stubs["get_authorization"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/GetAuthorization",
                request_serializer=auth_provider_service.GetAuthorizationRequest.serialize,
                response_deserializer=auth_provider_service.Authorization.deserialize,
            )
        return self._stubs["get_authorization"]

    @property
    def delete_authorization(
        self,
    ) -> Callable[
        [auth_provider_service.DeleteAuthorizationRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete authorization method over gRPC.

        Deletes a single Authorization.

        Returns:
            Callable[[~.DeleteAuthorizationRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_authorization" not in self._stubs:
            self._stubs["delete_authorization"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/DeleteAuthorization",
                request_serializer=auth_provider_service.DeleteAuthorizationRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_authorization"]

    @property
    def list_access_summaries(
        self,
    ) -> Callable[
        [auth_provider_service.ListAccessSummariesRequest],
        Awaitable[auth_provider_service.ListAccessSummariesResponse],
    ]:
        r"""Return a callable for the list access summaries method over gRPC.

        Lists AccessSummaries in a given project and location. Supported
        Filters:

        - ``workload_id``: Filter by the SPIFFE ID of the agent.
          Example:
          ``workload_id="spiffe://example.com/ns/default/sa/my-agent"``

        Returns:
            Callable[[~.ListAccessSummariesRequest],
                    Awaitable[~.ListAccessSummariesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_access_summaries" not in self._stubs:
            self._stubs["list_access_summaries"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/ListAccessSummaries",
                request_serializer=auth_provider_service.ListAccessSummariesRequest.serialize,
                response_deserializer=auth_provider_service.ListAccessSummariesResponse.deserialize,
            )
        return self._stubs["list_access_summaries"]

    @property
    def get_access_summary(
        self,
    ) -> Callable[
        [auth_provider_service.GetAccessSummaryRequest],
        Awaitable[auth_provider_service.AccessSummary],
    ]:
        r"""Return a callable for the get access summary method over gRPC.

        Gets details of a single AccessSummary.

        Returns:
            Callable[[~.GetAccessSummaryRequest],
                    Awaitable[~.AccessSummary]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_access_summary" not in self._stubs:
            self._stubs["get_access_summary"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/GetAccessSummary",
                request_serializer=auth_provider_service.GetAccessSummaryRequest.serialize,
                response_deserializer=auth_provider_service.AccessSummary.deserialize,
            )
        return self._stubs["get_access_summary"]

    @property
    def revoke_authorization(
        self,
    ) -> Callable[
        [auth_provider_service.RevokeAuthorizationRequest],
        Awaitable[auth_provider_service.RevokeAuthorizationResponse],
    ]:
        r"""Return a callable for the revoke authorization method over gRPC.

        Revokes all authorizations for a specific user on an
        AuthProvider. This deletes all authorization records
        associated with the user and AuthProvider, effectively
        revoking access across all agents.

        Returns:
            Callable[[~.RevokeAuthorizationRequest],
                    Awaitable[~.RevokeAuthorizationResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "revoke_authorization" not in self._stubs:
            self._stubs["revoke_authorization"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/RevokeAuthorization",
                request_serializer=auth_provider_service.RevokeAuthorizationRequest.serialize,
                response_deserializer=auth_provider_service.RevokeAuthorizationResponse.deserialize,
            )
        return self._stubs["revoke_authorization"]

    @property
    def enable_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.EnableAuthProviderRequest],
        Awaitable[auth_provider_service.AuthProvider],
    ]:
        r"""Return a callable for the enable auth provider method over gRPC.

        Enables a single AuthProvider.

        Returns:
            Callable[[~.EnableAuthProviderRequest],
                    Awaitable[~.AuthProvider]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "enable_auth_provider" not in self._stubs:
            self._stubs["enable_auth_provider"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/EnableAuthProvider",
                request_serializer=auth_provider_service.EnableAuthProviderRequest.serialize,
                response_deserializer=auth_provider_service.AuthProvider.deserialize,
            )
        return self._stubs["enable_auth_provider"]

    @property
    def disable_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.DisableAuthProviderRequest],
        Awaitable[auth_provider_service.AuthProvider],
    ]:
        r"""Return a callable for the disable auth provider method over gRPC.

        Disables a single AuthProvider.

        Returns:
            Callable[[~.DisableAuthProviderRequest],
                    Awaitable[~.AuthProvider]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "disable_auth_provider" not in self._stubs:
            self._stubs["disable_auth_provider"] = self._logged_channel.unary_unary(
                "/google.cloud.agentidentity.v1beta.AuthProviderService/DisableAuthProvider",
                request_serializer=auth_provider_service.DisableAuthProviderRequest.serialize,
                response_deserializer=auth_provider_service.AuthProvider.deserialize,
            )
        return self._stubs["disable_auth_provider"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_auth_providers: self._wrap_method(
                self.list_auth_providers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_auth_provider: self._wrap_method(
                self.get_auth_provider,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_auth_provider: self._wrap_method(
                self.create_auth_provider,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_auth_provider: self._wrap_method(
                self.update_auth_provider,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_auth_provider: self._wrap_method(
                self.delete_auth_provider,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undelete_auth_provider: self._wrap_method(
                self.undelete_auth_provider,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_auth_providers: self._wrap_method(
                self.query_auth_providers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_workloads: self._wrap_method(
                self.query_workloads,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_authorizations: self._wrap_method(
                self.list_authorizations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_authorization: self._wrap_method(
                self.get_authorization,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_authorization: self._wrap_method(
                self.delete_authorization,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_access_summaries: self._wrap_method(
                self.list_access_summaries,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_access_summary: self._wrap_method(
                self.get_access_summary,
                default_timeout=None,
                client_info=client_info,
            ),
            self.revoke_authorization: self._wrap_method(
                self.revoke_authorization,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enable_auth_provider: self._wrap_method(
                self.enable_auth_provider,
                default_timeout=None,
                client_info=client_info,
            ),
            self.disable_auth_provider: self._wrap_method(
                self.disable_auth_provider,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def close(self):
        return self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc_asyncio"

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest], locations_pb2.ListLocationsResponse
    ]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_locations" not in self._stubs:
            self._stubs["list_locations"] = self._logged_channel.unary_unary(
                "/google.cloud.location.Locations/ListLocations",
                request_serializer=locations_pb2.ListLocationsRequest.SerializeToString,
                response_deserializer=locations_pb2.ListLocationsResponse.FromString,
            )
        return self._stubs["list_locations"]

    @property
    def get_location(
        self,
    ) -> Callable[[locations_pb2.GetLocationRequest], locations_pb2.Location]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_location" not in self._stubs:
            self._stubs["get_location"] = self._logged_channel.unary_unary(
                "/google.cloud.location.Locations/GetLocation",
                request_serializer=locations_pb2.GetLocationRequest.SerializeToString,
                response_deserializer=locations_pb2.Location.FromString,
            )
        return self._stubs["get_location"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.
        Sets the IAM access control policy on the specified
        function. Replaces any existing policy.
        Returns:
            Callable[[~.SetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.
        Gets the IAM access control policy for a function.
        Returns an empty policy if the function exists and does
        not have a policy set.
        Returns:
            Callable[[~.GetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.
        Tests the specified permissions against the IAM access control
        policy for a function. If the function does not exist, this will
        return an empty set of permissions, not a NOT_FOUND error.
        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    ~.TestIamPermissionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]


__all__ = ("AuthProviderServiceGrpcAsyncIOTransport",)
