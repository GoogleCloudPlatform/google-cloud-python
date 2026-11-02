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
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.parametermanager_v1.types import service

from .base import DEFAULT_CLIENT_INFO, ParameterManagerTransport
from .grpc import ParameterManagerGrpcTransport

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
                    "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
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
                    "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ParameterManagerGrpcAsyncIOTransport(ParameterManagerTransport):
    """gRPC AsyncIO backend transport for ParameterManager.

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
        host: str = "parametermanager.googleapis.com",
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
        host: str = "parametermanager.googleapis.com",
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
                 The hostname to connect to (default: 'parametermanager.googleapis.com').
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
    def list_parameters(
        self,
    ) -> Callable[
        [service.ListParametersRequest], Awaitable[service.ListParametersResponse]
    ]:
        r"""Return a callable for the list parameters method over gRPC.

        Lists Parameters in a given project and location.

        Returns:
            Callable[[~.ListParametersRequest],
                    Awaitable[~.ListParametersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_parameters" not in self._stubs:
            self._stubs["list_parameters"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/ListParameters",
                request_serializer=service.ListParametersRequest.serialize,
                response_deserializer=service.ListParametersResponse.deserialize,
            )
        return self._stubs["list_parameters"]

    @property
    def get_parameter(
        self,
    ) -> Callable[[service.GetParameterRequest], Awaitable[service.Parameter]]:
        r"""Return a callable for the get parameter method over gRPC.

        Gets details of a single Parameter.

        Returns:
            Callable[[~.GetParameterRequest],
                    Awaitable[~.Parameter]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_parameter" not in self._stubs:
            self._stubs["get_parameter"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/GetParameter",
                request_serializer=service.GetParameterRequest.serialize,
                response_deserializer=service.Parameter.deserialize,
            )
        return self._stubs["get_parameter"]

    @property
    def create_parameter(
        self,
    ) -> Callable[[service.CreateParameterRequest], Awaitable[service.Parameter]]:
        r"""Return a callable for the create parameter method over gRPC.

        Creates a new Parameter in a given project and
        location.

        Returns:
            Callable[[~.CreateParameterRequest],
                    Awaitable[~.Parameter]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_parameter" not in self._stubs:
            self._stubs["create_parameter"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/CreateParameter",
                request_serializer=service.CreateParameterRequest.serialize,
                response_deserializer=service.Parameter.deserialize,
            )
        return self._stubs["create_parameter"]

    @property
    def update_parameter(
        self,
    ) -> Callable[[service.UpdateParameterRequest], Awaitable[service.Parameter]]:
        r"""Return a callable for the update parameter method over gRPC.

        Updates a single Parameter.

        Returns:
            Callable[[~.UpdateParameterRequest],
                    Awaitable[~.Parameter]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_parameter" not in self._stubs:
            self._stubs["update_parameter"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/UpdateParameter",
                request_serializer=service.UpdateParameterRequest.serialize,
                response_deserializer=service.Parameter.deserialize,
            )
        return self._stubs["update_parameter"]

    @property
    def delete_parameter(
        self,
    ) -> Callable[[service.DeleteParameterRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete parameter method over gRPC.

        Deletes a single Parameter.

        Returns:
            Callable[[~.DeleteParameterRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_parameter" not in self._stubs:
            self._stubs["delete_parameter"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/DeleteParameter",
                request_serializer=service.DeleteParameterRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_parameter"]

    @property
    def list_parameter_versions(
        self,
    ) -> Callable[
        [service.ListParameterVersionsRequest],
        Awaitable[service.ListParameterVersionsResponse],
    ]:
        r"""Return a callable for the list parameter versions method over gRPC.

        Lists ParameterVersions in a given project, location,
        and parameter.

        Returns:
            Callable[[~.ListParameterVersionsRequest],
                    Awaitable[~.ListParameterVersionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_parameter_versions" not in self._stubs:
            self._stubs["list_parameter_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/ListParameterVersions",
                request_serializer=service.ListParameterVersionsRequest.serialize,
                response_deserializer=service.ListParameterVersionsResponse.deserialize,
            )
        return self._stubs["list_parameter_versions"]

    @property
    def get_parameter_version(
        self,
    ) -> Callable[
        [service.GetParameterVersionRequest], Awaitable[service.ParameterVersion]
    ]:
        r"""Return a callable for the get parameter version method over gRPC.

        Gets details of a single ParameterVersion.

        Returns:
            Callable[[~.GetParameterVersionRequest],
                    Awaitable[~.ParameterVersion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_parameter_version" not in self._stubs:
            self._stubs["get_parameter_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/GetParameterVersion",
                request_serializer=service.GetParameterVersionRequest.serialize,
                response_deserializer=service.ParameterVersion.deserialize,
            )
        return self._stubs["get_parameter_version"]

    @property
    def render_parameter_version(
        self,
    ) -> Callable[
        [service.RenderParameterVersionRequest],
        Awaitable[service.RenderParameterVersionResponse],
    ]:
        r"""Return a callable for the render parameter version method over gRPC.

        Gets rendered version of a ParameterVersion.

        Returns:
            Callable[[~.RenderParameterVersionRequest],
                    Awaitable[~.RenderParameterVersionResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "render_parameter_version" not in self._stubs:
            self._stubs["render_parameter_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/RenderParameterVersion",
                request_serializer=service.RenderParameterVersionRequest.serialize,
                response_deserializer=service.RenderParameterVersionResponse.deserialize,
            )
        return self._stubs["render_parameter_version"]

    @property
    def create_parameter_version(
        self,
    ) -> Callable[
        [service.CreateParameterVersionRequest], Awaitable[service.ParameterVersion]
    ]:
        r"""Return a callable for the create parameter version method over gRPC.

        Creates a new ParameterVersion in a given project,
        location, and parameter.

        Returns:
            Callable[[~.CreateParameterVersionRequest],
                    Awaitable[~.ParameterVersion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_parameter_version" not in self._stubs:
            self._stubs["create_parameter_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/CreateParameterVersion",
                request_serializer=service.CreateParameterVersionRequest.serialize,
                response_deserializer=service.ParameterVersion.deserialize,
            )
        return self._stubs["create_parameter_version"]

    @property
    def update_parameter_version(
        self,
    ) -> Callable[
        [service.UpdateParameterVersionRequest], Awaitable[service.ParameterVersion]
    ]:
        r"""Return a callable for the update parameter version method over gRPC.

        Updates a single ParameterVersion.

        Returns:
            Callable[[~.UpdateParameterVersionRequest],
                    Awaitable[~.ParameterVersion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_parameter_version" not in self._stubs:
            self._stubs["update_parameter_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/UpdateParameterVersion",
                request_serializer=service.UpdateParameterVersionRequest.serialize,
                response_deserializer=service.ParameterVersion.deserialize,
            )
        return self._stubs["update_parameter_version"]

    @property
    def delete_parameter_version(
        self,
    ) -> Callable[[service.DeleteParameterVersionRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete parameter version method over gRPC.

        Deletes a single ParameterVersion.

        Returns:
            Callable[[~.DeleteParameterVersionRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_parameter_version" not in self._stubs:
            self._stubs["delete_parameter_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/DeleteParameterVersion",
                request_serializer=service.DeleteParameterVersionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_parameter_version"]

    @property
    def list_templates(
        self,
    ) -> Callable[
        [service.ListTemplatesRequest], Awaitable[service.ListTemplatesResponse]
    ]:
        r"""Return a callable for the list templates method over gRPC.

        Lists Templates in a given project and location.

        Returns:
            Callable[[~.ListTemplatesRequest],
                    Awaitable[~.ListTemplatesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_templates" not in self._stubs:
            self._stubs["list_templates"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/ListTemplates",
                request_serializer=service.ListTemplatesRequest.serialize,
                response_deserializer=service.ListTemplatesResponse.deserialize,
            )
        return self._stubs["list_templates"]

    @property
    def get_template(
        self,
    ) -> Callable[[service.GetTemplateRequest], Awaitable[service.Template]]:
        r"""Return a callable for the get template method over gRPC.

        Gets details of a single Template.

        Returns:
            Callable[[~.GetTemplateRequest],
                    Awaitable[~.Template]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_template" not in self._stubs:
            self._stubs["get_template"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/GetTemplate",
                request_serializer=service.GetTemplateRequest.serialize,
                response_deserializer=service.Template.deserialize,
            )
        return self._stubs["get_template"]

    @property
    def create_template(
        self,
    ) -> Callable[[service.CreateTemplateRequest], Awaitable[service.Template]]:
        r"""Return a callable for the create template method over gRPC.

        Creates a new Template in a given project and
        location.

        Returns:
            Callable[[~.CreateTemplateRequest],
                    Awaitable[~.Template]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_template" not in self._stubs:
            self._stubs["create_template"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/CreateTemplate",
                request_serializer=service.CreateTemplateRequest.serialize,
                response_deserializer=service.Template.deserialize,
            )
        return self._stubs["create_template"]

    @property
    def update_template(
        self,
    ) -> Callable[[service.UpdateTemplateRequest], Awaitable[service.Template]]:
        r"""Return a callable for the update template method over gRPC.

        Updates a single Template.

        Returns:
            Callable[[~.UpdateTemplateRequest],
                    Awaitable[~.Template]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_template" not in self._stubs:
            self._stubs["update_template"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/UpdateTemplate",
                request_serializer=service.UpdateTemplateRequest.serialize,
                response_deserializer=service.Template.deserialize,
            )
        return self._stubs["update_template"]

    @property
    def delete_template(
        self,
    ) -> Callable[[service.DeleteTemplateRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete template method over gRPC.

        Deletes a single Template.

        Returns:
            Callable[[~.DeleteTemplateRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_template" not in self._stubs:
            self._stubs["delete_template"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/DeleteTemplate",
                request_serializer=service.DeleteTemplateRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_template"]

    @property
    def list_template_versions(
        self,
    ) -> Callable[
        [service.ListTemplateVersionsRequest],
        Awaitable[service.ListTemplateVersionsResponse],
    ]:
        r"""Return a callable for the list template versions method over gRPC.

        Lists TemplateVersions in a given project, location,
        and template.

        Returns:
            Callable[[~.ListTemplateVersionsRequest],
                    Awaitable[~.ListTemplateVersionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_template_versions" not in self._stubs:
            self._stubs["list_template_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/ListTemplateVersions",
                request_serializer=service.ListTemplateVersionsRequest.serialize,
                response_deserializer=service.ListTemplateVersionsResponse.deserialize,
            )
        return self._stubs["list_template_versions"]

    @property
    def get_template_version(
        self,
    ) -> Callable[
        [service.GetTemplateVersionRequest], Awaitable[service.TemplateVersion]
    ]:
        r"""Return a callable for the get template version method over gRPC.

        Gets details of a single TemplateVersion.

        Returns:
            Callable[[~.GetTemplateVersionRequest],
                    Awaitable[~.TemplateVersion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_template_version" not in self._stubs:
            self._stubs["get_template_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/GetTemplateVersion",
                request_serializer=service.GetTemplateVersionRequest.serialize,
                response_deserializer=service.TemplateVersion.deserialize,
            )
        return self._stubs["get_template_version"]

    @property
    def create_template_version(
        self,
    ) -> Callable[
        [service.CreateTemplateVersionRequest], Awaitable[service.TemplateVersion]
    ]:
        r"""Return a callable for the create template version method over gRPC.

        Creates a new TemplateVersion in a given project,
        location, and template.

        Returns:
            Callable[[~.CreateTemplateVersionRequest],
                    Awaitable[~.TemplateVersion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_template_version" not in self._stubs:
            self._stubs["create_template_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/CreateTemplateVersion",
                request_serializer=service.CreateTemplateVersionRequest.serialize,
                response_deserializer=service.TemplateVersion.deserialize,
            )
        return self._stubs["create_template_version"]

    @property
    def update_template_version(
        self,
    ) -> Callable[
        [service.UpdateTemplateVersionRequest], Awaitable[service.TemplateVersion]
    ]:
        r"""Return a callable for the update template version method over gRPC.

        Updates a single TemplateVersion.

        Returns:
            Callable[[~.UpdateTemplateVersionRequest],
                    Awaitable[~.TemplateVersion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_template_version" not in self._stubs:
            self._stubs["update_template_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/UpdateTemplateVersion",
                request_serializer=service.UpdateTemplateVersionRequest.serialize,
                response_deserializer=service.TemplateVersion.deserialize,
            )
        return self._stubs["update_template_version"]

    @property
    def delete_template_version(
        self,
    ) -> Callable[[service.DeleteTemplateVersionRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete template version method over gRPC.

        Deletes a single TemplateVersion.

        Returns:
            Callable[[~.DeleteTemplateVersionRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_template_version" not in self._stubs:
            self._stubs["delete_template_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/DeleteTemplateVersion",
                request_serializer=service.DeleteTemplateVersionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_template_version"]

    @property
    def render_template_version(
        self,
    ) -> Callable[
        [service.RenderTemplateVersionRequest],
        Awaitable[service.RenderTemplateVersionResponse],
    ]:
        r"""Return a callable for the render template version method over gRPC.

        Gets rendered version of a TemplateVersion.

        Returns:
            Callable[[~.RenderTemplateVersionRequest],
                    Awaitable[~.RenderTemplateVersionResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "render_template_version" not in self._stubs:
            self._stubs["render_template_version"] = self._logged_channel.unary_unary(
                "/google.cloud.parametermanager.v1.ParameterManager/RenderTemplateVersion",
                request_serializer=service.RenderTemplateVersionRequest.serialize,
                response_deserializer=service.RenderTemplateVersionResponse.deserialize,
            )
        return self._stubs["render_template_version"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_parameters: self._wrap_method(
                self.list_parameters,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_parameter: self._wrap_method(
                self.get_parameter,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_parameter: self._wrap_method(
                self.create_parameter,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_parameter: self._wrap_method(
                self.update_parameter,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_parameter: self._wrap_method(
                self.delete_parameter,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_parameter_versions: self._wrap_method(
                self.list_parameter_versions,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_parameter_version: self._wrap_method(
                self.get_parameter_version,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.render_parameter_version: self._wrap_method(
                self.render_parameter_version,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_parameter_version: self._wrap_method(
                self.create_parameter_version,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_parameter_version: self._wrap_method(
                self.update_parameter_version,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_parameter_version: self._wrap_method(
                self.delete_parameter_version,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_templates: self._wrap_method(
                self.list_templates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_template: self._wrap_method(
                self.get_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_template: self._wrap_method(
                self.create_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_template: self._wrap_method(
                self.update_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_template: self._wrap_method(
                self.delete_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_template_versions: self._wrap_method(
                self.list_template_versions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_template_version: self._wrap_method(
                self.get_template_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_template_version: self._wrap_method(
                self.create_template_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_template_version: self._wrap_method(
                self.update_template_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_template_version: self._wrap_method(
                self.delete_template_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.render_template_version: self._wrap_method(
                self.render_template_version,
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


__all__ = ("ParameterManagerGrpcAsyncIOTransport",)
