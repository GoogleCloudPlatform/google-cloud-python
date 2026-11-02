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
from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.chronicle_v1.types import rule
from google.cloud.chronicle_v1.types import rule as gcc_rule

from .base import DEFAULT_CLIENT_INFO, RuleServiceTransport
from .grpc import RuleServiceGrpcTransport

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
                    "serviceName": "google.cloud.chronicle.v1.RuleService",
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
                    "serviceName": "google.cloud.chronicle.v1.RuleService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class RuleServiceGrpcAsyncIOTransport(RuleServiceTransport):
    """gRPC AsyncIO backend transport for RuleService.

    RuleService provides interface for user-created rules.

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
        host: str = "chronicle.googleapis.com",
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
        host: str = "chronicle.googleapis.com",
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
                 The hostname to connect to (default: 'chronicle.googleapis.com').
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
        self._operations_client: Optional[operations_v1.OperationsAsyncClient] = None

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
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self._logged_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def create_rule(
        self,
    ) -> Callable[[gcc_rule.CreateRuleRequest], Awaitable[gcc_rule.Rule]]:
        r"""Return a callable for the create rule method over gRPC.

        Creates a new Rule.

        Returns:
            Callable[[~.CreateRuleRequest],
                    Awaitable[~.Rule]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_rule" not in self._stubs:
            self._stubs["create_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/CreateRule",
                request_serializer=gcc_rule.CreateRuleRequest.serialize,
                response_deserializer=gcc_rule.Rule.deserialize,
            )
        return self._stubs["create_rule"]

    @property
    def get_rule(self) -> Callable[[rule.GetRuleRequest], Awaitable[rule.Rule]]:
        r"""Return a callable for the get rule method over gRPC.

        Gets a Rule.

        Returns:
            Callable[[~.GetRuleRequest],
                    Awaitable[~.Rule]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_rule" not in self._stubs:
            self._stubs["get_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/GetRule",
                request_serializer=rule.GetRuleRequest.serialize,
                response_deserializer=rule.Rule.deserialize,
            )
        return self._stubs["get_rule"]

    @property
    def list_rules(
        self,
    ) -> Callable[[rule.ListRulesRequest], Awaitable[rule.ListRulesResponse]]:
        r"""Return a callable for the list rules method over gRPC.

        Lists Rules.

        Returns:
            Callable[[~.ListRulesRequest],
                    Awaitable[~.ListRulesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_rules" not in self._stubs:
            self._stubs["list_rules"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/ListRules",
                request_serializer=rule.ListRulesRequest.serialize,
                response_deserializer=rule.ListRulesResponse.deserialize,
            )
        return self._stubs["list_rules"]

    @property
    def update_rule(
        self,
    ) -> Callable[[gcc_rule.UpdateRuleRequest], Awaitable[gcc_rule.Rule]]:
        r"""Return a callable for the update rule method over gRPC.

        Updates a Rule.

        Returns:
            Callable[[~.UpdateRuleRequest],
                    Awaitable[~.Rule]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_rule" not in self._stubs:
            self._stubs["update_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/UpdateRule",
                request_serializer=gcc_rule.UpdateRuleRequest.serialize,
                response_deserializer=gcc_rule.Rule.deserialize,
            )
        return self._stubs["update_rule"]

    @property
    def delete_rule(
        self,
    ) -> Callable[[rule.DeleteRuleRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete rule method over gRPC.

        Deletes a Rule.

        Returns:
            Callable[[~.DeleteRuleRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_rule" not in self._stubs:
            self._stubs["delete_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/DeleteRule",
                request_serializer=rule.DeleteRuleRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_rule"]

    @property
    def verify_rule_text(
        self,
    ) -> Callable[[rule.VerifyRuleTextRequest], Awaitable[rule.VerifyRuleTextResponse]]:
        r"""Return a callable for the verify rule text method over gRPC.

        Verifies the given rule text.

        Returns:
            Callable[[~.VerifyRuleTextRequest],
                    Awaitable[~.VerifyRuleTextResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "verify_rule_text" not in self._stubs:
            self._stubs["verify_rule_text"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/VerifyRuleText",
                request_serializer=rule.VerifyRuleTextRequest.serialize,
                response_deserializer=rule.VerifyRuleTextResponse.deserialize,
            )
        return self._stubs["verify_rule_text"]

    @property
    def list_rule_revisions(
        self,
    ) -> Callable[
        [rule.ListRuleRevisionsRequest], Awaitable[rule.ListRuleRevisionsResponse]
    ]:
        r"""Return a callable for the list rule revisions method over gRPC.

        Lists all revisions of the rule.

        Returns:
            Callable[[~.ListRuleRevisionsRequest],
                    Awaitable[~.ListRuleRevisionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_rule_revisions" not in self._stubs:
            self._stubs["list_rule_revisions"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/ListRuleRevisions",
                request_serializer=rule.ListRuleRevisionsRequest.serialize,
                response_deserializer=rule.ListRuleRevisionsResponse.deserialize,
            )
        return self._stubs["list_rule_revisions"]

    @property
    def create_retrohunt(
        self,
    ) -> Callable[[rule.CreateRetrohuntRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create retrohunt method over gRPC.

        Create a Retrohunt.

        Returns:
            Callable[[~.CreateRetrohuntRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_retrohunt" not in self._stubs:
            self._stubs["create_retrohunt"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/CreateRetrohunt",
                request_serializer=rule.CreateRetrohuntRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_retrohunt"]

    @property
    def get_retrohunt(
        self,
    ) -> Callable[[rule.GetRetrohuntRequest], Awaitable[rule.Retrohunt]]:
        r"""Return a callable for the get retrohunt method over gRPC.

        Get a Retrohunt.

        Returns:
            Callable[[~.GetRetrohuntRequest],
                    Awaitable[~.Retrohunt]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_retrohunt" not in self._stubs:
            self._stubs["get_retrohunt"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/GetRetrohunt",
                request_serializer=rule.GetRetrohuntRequest.serialize,
                response_deserializer=rule.Retrohunt.deserialize,
            )
        return self._stubs["get_retrohunt"]

    @property
    def list_retrohunts(
        self,
    ) -> Callable[[rule.ListRetrohuntsRequest], Awaitable[rule.ListRetrohuntsResponse]]:
        r"""Return a callable for the list retrohunts method over gRPC.

        List Retrohunts.

        Returns:
            Callable[[~.ListRetrohuntsRequest],
                    Awaitable[~.ListRetrohuntsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_retrohunts" not in self._stubs:
            self._stubs["list_retrohunts"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/ListRetrohunts",
                request_serializer=rule.ListRetrohuntsRequest.serialize,
                response_deserializer=rule.ListRetrohuntsResponse.deserialize,
            )
        return self._stubs["list_retrohunts"]

    @property
    def get_rule_deployment(
        self,
    ) -> Callable[[rule.GetRuleDeploymentRequest], Awaitable[rule.RuleDeployment]]:
        r"""Return a callable for the get rule deployment method over gRPC.

        Gets a RuleDeployment.

        Returns:
            Callable[[~.GetRuleDeploymentRequest],
                    Awaitable[~.RuleDeployment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_rule_deployment" not in self._stubs:
            self._stubs["get_rule_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/GetRuleDeployment",
                request_serializer=rule.GetRuleDeploymentRequest.serialize,
                response_deserializer=rule.RuleDeployment.deserialize,
            )
        return self._stubs["get_rule_deployment"]

    @property
    def list_rule_deployments(
        self,
    ) -> Callable[
        [rule.ListRuleDeploymentsRequest], Awaitable[rule.ListRuleDeploymentsResponse]
    ]:
        r"""Return a callable for the list rule deployments method over gRPC.

        Lists RuleDeployments across all Rules.

        Returns:
            Callable[[~.ListRuleDeploymentsRequest],
                    Awaitable[~.ListRuleDeploymentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_rule_deployments" not in self._stubs:
            self._stubs["list_rule_deployments"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/ListRuleDeployments",
                request_serializer=rule.ListRuleDeploymentsRequest.serialize,
                response_deserializer=rule.ListRuleDeploymentsResponse.deserialize,
            )
        return self._stubs["list_rule_deployments"]

    @property
    def update_rule_deployment(
        self,
    ) -> Callable[[rule.UpdateRuleDeploymentRequest], Awaitable[rule.RuleDeployment]]:
        r"""Return a callable for the update rule deployment method over gRPC.

        Updates a RuleDeployment.
        Failures are not necessarily atomic. If there is a
        request to update multiple fields, and any update to a
        single field fails, an error will be returned, but other
        fields may remain successfully updated.

        Returns:
            Callable[[~.UpdateRuleDeploymentRequest],
                    Awaitable[~.RuleDeployment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_rule_deployment" not in self._stubs:
            self._stubs["update_rule_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.chronicle.v1.RuleService/UpdateRuleDeployment",
                request_serializer=rule.UpdateRuleDeploymentRequest.serialize,
                response_deserializer=rule.RuleDeployment.deserialize,
            )
        return self._stubs["update_rule_deployment"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_rule: self._wrap_method(
                self.create_rule,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_rule: self._wrap_method(
                self.get_rule,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_rules: self._wrap_method(
                self.list_rules,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=600.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_rule: self._wrap_method(
                self.update_rule,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_rule: self._wrap_method(
                self.delete_rule,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.verify_rule_text: self._wrap_method(
                self.verify_rule_text,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_rule_revisions: self._wrap_method(
                self.list_rule_revisions,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=600.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.create_retrohunt: self._wrap_method(
                self.create_retrohunt,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_retrohunt: self._wrap_method(
                self.get_retrohunt,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_retrohunts: self._wrap_method(
                self.list_retrohunts,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_rule_deployment: self._wrap_method(
                self.get_rule_deployment,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=600.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_rule_deployments: self._wrap_method(
                self.list_rule_deployments,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=600.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_rule_deployment: self._wrap_method(
                self.update_rule_deployment,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
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
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

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


__all__ = ("RuleServiceGrpcAsyncIOTransport",)
