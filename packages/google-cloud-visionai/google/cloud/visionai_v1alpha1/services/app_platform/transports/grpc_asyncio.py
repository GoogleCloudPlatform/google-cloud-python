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

import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.visionai_v1alpha1.types import platform

from .base import DEFAULT_CLIENT_INFO, AppPlatformTransport
from .grpc import AppPlatformGrpcTransport

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
                    "serviceName": "google.cloud.visionai.v1alpha1.AppPlatform",
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
                    "serviceName": "google.cloud.visionai.v1alpha1.AppPlatform",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AppPlatformGrpcAsyncIOTransport(AppPlatformTransport):
    """gRPC AsyncIO backend transport for AppPlatform.

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
        host: str = "visionai.googleapis.com",
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
        host: str = "visionai.googleapis.com",
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
                 The hostname to connect to (default: 'visionai.googleapis.com').
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
    def list_applications(
        self,
    ) -> Callable[
        [platform.ListApplicationsRequest], Awaitable[platform.ListApplicationsResponse]
    ]:
        r"""Return a callable for the list applications method over gRPC.

        Lists Applications in a given project and location.

        Returns:
            Callable[[~.ListApplicationsRequest],
                    Awaitable[~.ListApplicationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_applications" not in self._stubs:
            self._stubs["list_applications"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/ListApplications",
                request_serializer=platform.ListApplicationsRequest.serialize,
                response_deserializer=platform.ListApplicationsResponse.deserialize,
            )
        return self._stubs["list_applications"]

    @property
    def get_application(
        self,
    ) -> Callable[[platform.GetApplicationRequest], Awaitable[platform.Application]]:
        r"""Return a callable for the get application method over gRPC.

        Gets details of a single Application.

        Returns:
            Callable[[~.GetApplicationRequest],
                    Awaitable[~.Application]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_application" not in self._stubs:
            self._stubs["get_application"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/GetApplication",
                request_serializer=platform.GetApplicationRequest.serialize,
                response_deserializer=platform.Application.deserialize,
            )
        return self._stubs["get_application"]

    @property
    def create_application(
        self,
    ) -> Callable[
        [platform.CreateApplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create application method over gRPC.

        Creates a new Application in a given project and
        location.

        Returns:
            Callable[[~.CreateApplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_application" not in self._stubs:
            self._stubs["create_application"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/CreateApplication",
                request_serializer=platform.CreateApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_application"]

    @property
    def update_application(
        self,
    ) -> Callable[
        [platform.UpdateApplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update application method over gRPC.

        Updates the parameters of a single Application.

        Returns:
            Callable[[~.UpdateApplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_application" not in self._stubs:
            self._stubs["update_application"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/UpdateApplication",
                request_serializer=platform.UpdateApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_application"]

    @property
    def delete_application(
        self,
    ) -> Callable[
        [platform.DeleteApplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete application method over gRPC.

        Deletes a single Application.

        Returns:
            Callable[[~.DeleteApplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_application" not in self._stubs:
            self._stubs["delete_application"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/DeleteApplication",
                request_serializer=platform.DeleteApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_application"]

    @property
    def deploy_application(
        self,
    ) -> Callable[
        [platform.DeployApplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the deploy application method over gRPC.

        Deploys a single Application.

        Returns:
            Callable[[~.DeployApplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_application" not in self._stubs:
            self._stubs["deploy_application"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/DeployApplication",
                request_serializer=platform.DeployApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["deploy_application"]

    @property
    def undeploy_application(
        self,
    ) -> Callable[
        [platform.UndeployApplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the undeploy application method over gRPC.

        Undeploys a single Application.

        Returns:
            Callable[[~.UndeployApplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undeploy_application" not in self._stubs:
            self._stubs["undeploy_application"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/UndeployApplication",
                request_serializer=platform.UndeployApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undeploy_application"]

    @property
    def add_application_stream_input(
        self,
    ) -> Callable[
        [platform.AddApplicationStreamInputRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the add application stream input method over gRPC.

        Adds target stream input to the Application.
        If the Application is deployed, the corresponding new
        Application instance will be created. If the stream has
        already been in the Application, the RPC will fail.

        Returns:
            Callable[[~.AddApplicationStreamInputRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_application_stream_input" not in self._stubs:
            self._stubs["add_application_stream_input"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.visionai.v1alpha1.AppPlatform/AddApplicationStreamInput",
                    request_serializer=platform.AddApplicationStreamInputRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["add_application_stream_input"]

    @property
    def remove_application_stream_input(
        self,
    ) -> Callable[
        [platform.RemoveApplicationStreamInputRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the remove application stream
        input method over gRPC.

        Remove target stream input to the Application, if the
        Application is deployed, the corresponding instance
        based will be deleted. If the stream is not in the
        Application, the RPC will fail.

        Returns:
            Callable[[~.RemoveApplicationStreamInputRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_application_stream_input" not in self._stubs:
            self._stubs["remove_application_stream_input"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.visionai.v1alpha1.AppPlatform/RemoveApplicationStreamInput",
                    request_serializer=platform.RemoveApplicationStreamInputRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["remove_application_stream_input"]

    @property
    def update_application_stream_input(
        self,
    ) -> Callable[
        [platform.UpdateApplicationStreamInputRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update application stream
        input method over gRPC.

        Update target stream input to the Application, if the
        Application is deployed, the corresponding instance based will
        be deployed. For CreateOrUpdate behavior, set allow_missing to
        true.

        Returns:
            Callable[[~.UpdateApplicationStreamInputRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_application_stream_input" not in self._stubs:
            self._stubs["update_application_stream_input"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.visionai.v1alpha1.AppPlatform/UpdateApplicationStreamInput",
                    request_serializer=platform.UpdateApplicationStreamInputRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_application_stream_input"]

    @property
    def list_instances(
        self,
    ) -> Callable[
        [platform.ListInstancesRequest], Awaitable[platform.ListInstancesResponse]
    ]:
        r"""Return a callable for the list instances method over gRPC.

        Lists Instances in a given project and location.

        Returns:
            Callable[[~.ListInstancesRequest],
                    Awaitable[~.ListInstancesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_instances" not in self._stubs:
            self._stubs["list_instances"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/ListInstances",
                request_serializer=platform.ListInstancesRequest.serialize,
                response_deserializer=platform.ListInstancesResponse.deserialize,
            )
        return self._stubs["list_instances"]

    @property
    def get_instance(
        self,
    ) -> Callable[[platform.GetInstanceRequest], Awaitable[platform.Instance]]:
        r"""Return a callable for the get instance method over gRPC.

        Gets details of a single Instance.

        Returns:
            Callable[[~.GetInstanceRequest],
                    Awaitable[~.Instance]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_instance" not in self._stubs:
            self._stubs["get_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/GetInstance",
                request_serializer=platform.GetInstanceRequest.serialize,
                response_deserializer=platform.Instance.deserialize,
            )
        return self._stubs["get_instance"]

    @property
    def create_application_instances(
        self,
    ) -> Callable[
        [platform.CreateApplicationInstancesRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create application instances method over gRPC.

        Adds target stream input to the Application.
        If the Application is deployed, the corresponding new
        Application instance will be created. If the stream has
        already been in the Application, the RPC will fail.

        Returns:
            Callable[[~.CreateApplicationInstancesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_application_instances" not in self._stubs:
            self._stubs["create_application_instances"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.visionai.v1alpha1.AppPlatform/CreateApplicationInstances",
                    request_serializer=platform.CreateApplicationInstancesRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_application_instances"]

    @property
    def delete_application_instances(
        self,
    ) -> Callable[
        [platform.DeleteApplicationInstancesRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete application instances method over gRPC.

        Remove target stream input to the Application, if the
        Application is deployed, the corresponding instance
        based will be deleted. If the stream is not in the
        Application, the RPC will fail.

        Returns:
            Callable[[~.DeleteApplicationInstancesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_application_instances" not in self._stubs:
            self._stubs["delete_application_instances"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.visionai.v1alpha1.AppPlatform/DeleteApplicationInstances",
                    request_serializer=platform.DeleteApplicationInstancesRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_application_instances"]

    @property
    def update_application_instances(
        self,
    ) -> Callable[
        [platform.UpdateApplicationInstancesRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update application instances method over gRPC.

        Adds target stream input to the Application.
        If the Application is deployed, the corresponding new
        Application instance will be created. If the stream has
        already been in the Application, the RPC will fail.

        Returns:
            Callable[[~.UpdateApplicationInstancesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_application_instances" not in self._stubs:
            self._stubs["update_application_instances"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.visionai.v1alpha1.AppPlatform/UpdateApplicationInstances",
                    request_serializer=platform.UpdateApplicationInstancesRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_application_instances"]

    @property
    def list_drafts(
        self,
    ) -> Callable[[platform.ListDraftsRequest], Awaitable[platform.ListDraftsResponse]]:
        r"""Return a callable for the list drafts method over gRPC.

        Lists Drafts in a given project and location.

        Returns:
            Callable[[~.ListDraftsRequest],
                    Awaitable[~.ListDraftsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_drafts" not in self._stubs:
            self._stubs["list_drafts"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/ListDrafts",
                request_serializer=platform.ListDraftsRequest.serialize,
                response_deserializer=platform.ListDraftsResponse.deserialize,
            )
        return self._stubs["list_drafts"]

    @property
    def get_draft(
        self,
    ) -> Callable[[platform.GetDraftRequest], Awaitable[platform.Draft]]:
        r"""Return a callable for the get draft method over gRPC.

        Gets details of a single Draft.

        Returns:
            Callable[[~.GetDraftRequest],
                    Awaitable[~.Draft]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_draft" not in self._stubs:
            self._stubs["get_draft"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/GetDraft",
                request_serializer=platform.GetDraftRequest.serialize,
                response_deserializer=platform.Draft.deserialize,
            )
        return self._stubs["get_draft"]

    @property
    def create_draft(
        self,
    ) -> Callable[[platform.CreateDraftRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create draft method over gRPC.

        Creates a new Draft in a given project and location.

        Returns:
            Callable[[~.CreateDraftRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_draft" not in self._stubs:
            self._stubs["create_draft"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/CreateDraft",
                request_serializer=platform.CreateDraftRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_draft"]

    @property
    def update_draft(
        self,
    ) -> Callable[[platform.UpdateDraftRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update draft method over gRPC.

        Updates the parameters of a single Draft.

        Returns:
            Callable[[~.UpdateDraftRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_draft" not in self._stubs:
            self._stubs["update_draft"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/UpdateDraft",
                request_serializer=platform.UpdateDraftRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_draft"]

    @property
    def delete_draft(
        self,
    ) -> Callable[[platform.DeleteDraftRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete draft method over gRPC.

        Deletes a single Draft.

        Returns:
            Callable[[~.DeleteDraftRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_draft" not in self._stubs:
            self._stubs["delete_draft"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/DeleteDraft",
                request_serializer=platform.DeleteDraftRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_draft"]

    @property
    def list_processors(
        self,
    ) -> Callable[
        [platform.ListProcessorsRequest], Awaitable[platform.ListProcessorsResponse]
    ]:
        r"""Return a callable for the list processors method over gRPC.

        Lists Processors in a given project and location.

        Returns:
            Callable[[~.ListProcessorsRequest],
                    Awaitable[~.ListProcessorsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_processors" not in self._stubs:
            self._stubs["list_processors"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/ListProcessors",
                request_serializer=platform.ListProcessorsRequest.serialize,
                response_deserializer=platform.ListProcessorsResponse.deserialize,
            )
        return self._stubs["list_processors"]

    @property
    def list_prebuilt_processors(
        self,
    ) -> Callable[
        [platform.ListPrebuiltProcessorsRequest],
        Awaitable[platform.ListPrebuiltProcessorsResponse],
    ]:
        r"""Return a callable for the list prebuilt processors method over gRPC.

        ListPrebuiltProcessors is a custom pass-through verb
        that Lists Prebuilt Processors.

        Returns:
            Callable[[~.ListPrebuiltProcessorsRequest],
                    Awaitable[~.ListPrebuiltProcessorsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_prebuilt_processors" not in self._stubs:
            self._stubs["list_prebuilt_processors"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/ListPrebuiltProcessors",
                request_serializer=platform.ListPrebuiltProcessorsRequest.serialize,
                response_deserializer=platform.ListPrebuiltProcessorsResponse.deserialize,
            )
        return self._stubs["list_prebuilt_processors"]

    @property
    def get_processor(
        self,
    ) -> Callable[[platform.GetProcessorRequest], Awaitable[platform.Processor]]:
        r"""Return a callable for the get processor method over gRPC.

        Gets details of a single Processor.

        Returns:
            Callable[[~.GetProcessorRequest],
                    Awaitable[~.Processor]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_processor" not in self._stubs:
            self._stubs["get_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/GetProcessor",
                request_serializer=platform.GetProcessorRequest.serialize,
                response_deserializer=platform.Processor.deserialize,
            )
        return self._stubs["get_processor"]

    @property
    def create_processor(
        self,
    ) -> Callable[
        [platform.CreateProcessorRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create processor method over gRPC.

        Creates a new Processor in a given project and
        location.

        Returns:
            Callable[[~.CreateProcessorRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_processor" not in self._stubs:
            self._stubs["create_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/CreateProcessor",
                request_serializer=platform.CreateProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_processor"]

    @property
    def update_processor(
        self,
    ) -> Callable[
        [platform.UpdateProcessorRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update processor method over gRPC.

        Updates the parameters of a single Processor.

        Returns:
            Callable[[~.UpdateProcessorRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_processor" not in self._stubs:
            self._stubs["update_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/UpdateProcessor",
                request_serializer=platform.UpdateProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_processor"]

    @property
    def delete_processor(
        self,
    ) -> Callable[
        [platform.DeleteProcessorRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete processor method over gRPC.

        Deletes a single Processor.

        Returns:
            Callable[[~.DeleteProcessorRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_processor" not in self._stubs:
            self._stubs["delete_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.visionai.v1alpha1.AppPlatform/DeleteProcessor",
                request_serializer=platform.DeleteProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_processor"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_applications: self._wrap_method(
                self.list_applications,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_application: self._wrap_method(
                self.get_application,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_application: self._wrap_method(
                self.create_application,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_application: self._wrap_method(
                self.update_application,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_application: self._wrap_method(
                self.delete_application,
                default_timeout=None,
                client_info=client_info,
            ),
            self.deploy_application: self._wrap_method(
                self.deploy_application,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undeploy_application: self._wrap_method(
                self.undeploy_application,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_application_stream_input: self._wrap_method(
                self.add_application_stream_input,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_application_stream_input: self._wrap_method(
                self.remove_application_stream_input,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_application_stream_input: self._wrap_method(
                self.update_application_stream_input,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_instances: self._wrap_method(
                self.list_instances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_instance: self._wrap_method(
                self.get_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_application_instances: self._wrap_method(
                self.create_application_instances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_application_instances: self._wrap_method(
                self.delete_application_instances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_application_instances: self._wrap_method(
                self.update_application_instances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_drafts: self._wrap_method(
                self.list_drafts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_draft: self._wrap_method(
                self.get_draft,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_draft: self._wrap_method(
                self.create_draft,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_draft: self._wrap_method(
                self.update_draft,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_draft: self._wrap_method(
                self.delete_draft,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_processors: self._wrap_method(
                self.list_processors,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_prebuilt_processors: self._wrap_method(
                self.list_prebuilt_processors,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_processor: self._wrap_method(
                self.get_processor,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_processor: self._wrap_method(
                self.create_processor,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_processor: self._wrap_method(
                self.update_processor,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_processor: self._wrap_method(
                self.delete_processor,
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


__all__ = ("AppPlatformGrpcAsyncIOTransport",)
