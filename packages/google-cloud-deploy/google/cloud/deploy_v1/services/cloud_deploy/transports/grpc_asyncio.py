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

from google.cloud.deploy_v1.types import cloud_deploy

from .base import DEFAULT_CLIENT_INFO, CloudDeployTransport
from .grpc import CloudDeployGrpcTransport

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
                    "serviceName": "google.cloud.deploy.v1.CloudDeploy",
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
                    "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class CloudDeployGrpcAsyncIOTransport(CloudDeployTransport):
    """gRPC AsyncIO backend transport for CloudDeploy.

    CloudDeploy service creates and manages Continuous Delivery
    operations on Google Cloud Platform via Skaffold
    (https://skaffold.dev).

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
        host: str = "clouddeploy.googleapis.com",
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
        host: str = "clouddeploy.googleapis.com",
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
                 The hostname to connect to (default: 'clouddeploy.googleapis.com').
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
    def list_delivery_pipelines(
        self,
    ) -> Callable[
        [cloud_deploy.ListDeliveryPipelinesRequest],
        Awaitable[cloud_deploy.ListDeliveryPipelinesResponse],
    ]:
        r"""Return a callable for the list delivery pipelines method over gRPC.

        Lists DeliveryPipelines in a given project and
        location.

        Returns:
            Callable[[~.ListDeliveryPipelinesRequest],
                    Awaitable[~.ListDeliveryPipelinesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_delivery_pipelines" not in self._stubs:
            self._stubs["list_delivery_pipelines"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListDeliveryPipelines",
                request_serializer=cloud_deploy.ListDeliveryPipelinesRequest.serialize,
                response_deserializer=cloud_deploy.ListDeliveryPipelinesResponse.deserialize,
            )
        return self._stubs["list_delivery_pipelines"]

    @property
    def get_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.GetDeliveryPipelineRequest],
        Awaitable[cloud_deploy.DeliveryPipeline],
    ]:
        r"""Return a callable for the get delivery pipeline method over gRPC.

        Gets details of a single DeliveryPipeline.

        Returns:
            Callable[[~.GetDeliveryPipelineRequest],
                    Awaitable[~.DeliveryPipeline]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_delivery_pipeline" not in self._stubs:
            self._stubs["get_delivery_pipeline"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetDeliveryPipeline",
                request_serializer=cloud_deploy.GetDeliveryPipelineRequest.serialize,
                response_deserializer=cloud_deploy.DeliveryPipeline.deserialize,
            )
        return self._stubs["get_delivery_pipeline"]

    @property
    def create_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.CreateDeliveryPipelineRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create delivery pipeline method over gRPC.

        Creates a new DeliveryPipeline in a given project and
        location.

        Returns:
            Callable[[~.CreateDeliveryPipelineRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_delivery_pipeline" not in self._stubs:
            self._stubs["create_delivery_pipeline"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CreateDeliveryPipeline",
                request_serializer=cloud_deploy.CreateDeliveryPipelineRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_delivery_pipeline"]

    @property
    def update_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateDeliveryPipelineRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update delivery pipeline method over gRPC.

        Updates the parameters of a single DeliveryPipeline.

        Returns:
            Callable[[~.UpdateDeliveryPipelineRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_delivery_pipeline" not in self._stubs:
            self._stubs["update_delivery_pipeline"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/UpdateDeliveryPipeline",
                request_serializer=cloud_deploy.UpdateDeliveryPipelineRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_delivery_pipeline"]

    @property
    def delete_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteDeliveryPipelineRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete delivery pipeline method over gRPC.

        Deletes a single DeliveryPipeline.

        Returns:
            Callable[[~.DeleteDeliveryPipelineRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_delivery_pipeline" not in self._stubs:
            self._stubs["delete_delivery_pipeline"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/DeleteDeliveryPipeline",
                request_serializer=cloud_deploy.DeleteDeliveryPipelineRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_delivery_pipeline"]

    @property
    def list_targets(
        self,
    ) -> Callable[
        [cloud_deploy.ListTargetsRequest], Awaitable[cloud_deploy.ListTargetsResponse]
    ]:
        r"""Return a callable for the list targets method over gRPC.

        Lists Targets in a given project and location.

        Returns:
            Callable[[~.ListTargetsRequest],
                    Awaitable[~.ListTargetsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_targets" not in self._stubs:
            self._stubs["list_targets"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListTargets",
                request_serializer=cloud_deploy.ListTargetsRequest.serialize,
                response_deserializer=cloud_deploy.ListTargetsResponse.deserialize,
            )
        return self._stubs["list_targets"]

    @property
    def rollback_target(
        self,
    ) -> Callable[
        [cloud_deploy.RollbackTargetRequest],
        Awaitable[cloud_deploy.RollbackTargetResponse],
    ]:
        r"""Return a callable for the rollback target method over gRPC.

        Creates a ``Rollout`` to roll back the specified target.

        Returns:
            Callable[[~.RollbackTargetRequest],
                    Awaitable[~.RollbackTargetResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rollback_target" not in self._stubs:
            self._stubs["rollback_target"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/RollbackTarget",
                request_serializer=cloud_deploy.RollbackTargetRequest.serialize,
                response_deserializer=cloud_deploy.RollbackTargetResponse.deserialize,
            )
        return self._stubs["rollback_target"]

    @property
    def get_target(
        self,
    ) -> Callable[[cloud_deploy.GetTargetRequest], Awaitable[cloud_deploy.Target]]:
        r"""Return a callable for the get target method over gRPC.

        Gets details of a single Target.

        Returns:
            Callable[[~.GetTargetRequest],
                    Awaitable[~.Target]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_target" not in self._stubs:
            self._stubs["get_target"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetTarget",
                request_serializer=cloud_deploy.GetTargetRequest.serialize,
                response_deserializer=cloud_deploy.Target.deserialize,
            )
        return self._stubs["get_target"]

    @property
    def create_target(
        self,
    ) -> Callable[
        [cloud_deploy.CreateTargetRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create target method over gRPC.

        Creates a new Target in a given project and location.

        Returns:
            Callable[[~.CreateTargetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_target" not in self._stubs:
            self._stubs["create_target"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CreateTarget",
                request_serializer=cloud_deploy.CreateTargetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_target"]

    @property
    def update_target(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateTargetRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update target method over gRPC.

        Updates the parameters of a single Target.

        Returns:
            Callable[[~.UpdateTargetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_target" not in self._stubs:
            self._stubs["update_target"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/UpdateTarget",
                request_serializer=cloud_deploy.UpdateTargetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_target"]

    @property
    def delete_target(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteTargetRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete target method over gRPC.

        Deletes a single Target.

        Returns:
            Callable[[~.DeleteTargetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_target" not in self._stubs:
            self._stubs["delete_target"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/DeleteTarget",
                request_serializer=cloud_deploy.DeleteTargetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_target"]

    @property
    def list_custom_target_types(
        self,
    ) -> Callable[
        [cloud_deploy.ListCustomTargetTypesRequest],
        Awaitable[cloud_deploy.ListCustomTargetTypesResponse],
    ]:
        r"""Return a callable for the list custom target types method over gRPC.

        Lists CustomTargetTypes in a given project and
        location.

        Returns:
            Callable[[~.ListCustomTargetTypesRequest],
                    Awaitable[~.ListCustomTargetTypesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_custom_target_types" not in self._stubs:
            self._stubs["list_custom_target_types"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListCustomTargetTypes",
                request_serializer=cloud_deploy.ListCustomTargetTypesRequest.serialize,
                response_deserializer=cloud_deploy.ListCustomTargetTypesResponse.deserialize,
            )
        return self._stubs["list_custom_target_types"]

    @property
    def get_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.GetCustomTargetTypeRequest],
        Awaitable[cloud_deploy.CustomTargetType],
    ]:
        r"""Return a callable for the get custom target type method over gRPC.

        Gets details of a single CustomTargetType.

        Returns:
            Callable[[~.GetCustomTargetTypeRequest],
                    Awaitable[~.CustomTargetType]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_custom_target_type" not in self._stubs:
            self._stubs["get_custom_target_type"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetCustomTargetType",
                request_serializer=cloud_deploy.GetCustomTargetTypeRequest.serialize,
                response_deserializer=cloud_deploy.CustomTargetType.deserialize,
            )
        return self._stubs["get_custom_target_type"]

    @property
    def create_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.CreateCustomTargetTypeRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create custom target type method over gRPC.

        Creates a new CustomTargetType in a given project and
        location.

        Returns:
            Callable[[~.CreateCustomTargetTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_custom_target_type" not in self._stubs:
            self._stubs["create_custom_target_type"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CreateCustomTargetType",
                request_serializer=cloud_deploy.CreateCustomTargetTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_custom_target_type"]

    @property
    def update_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateCustomTargetTypeRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update custom target type method over gRPC.

        Updates a single CustomTargetType.

        Returns:
            Callable[[~.UpdateCustomTargetTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_custom_target_type" not in self._stubs:
            self._stubs["update_custom_target_type"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/UpdateCustomTargetType",
                request_serializer=cloud_deploy.UpdateCustomTargetTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_custom_target_type"]

    @property
    def delete_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteCustomTargetTypeRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete custom target type method over gRPC.

        Deletes a single CustomTargetType.

        Returns:
            Callable[[~.DeleteCustomTargetTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_custom_target_type" not in self._stubs:
            self._stubs["delete_custom_target_type"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/DeleteCustomTargetType",
                request_serializer=cloud_deploy.DeleteCustomTargetTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_custom_target_type"]

    @property
    def list_releases(
        self,
    ) -> Callable[
        [cloud_deploy.ListReleasesRequest], Awaitable[cloud_deploy.ListReleasesResponse]
    ]:
        r"""Return a callable for the list releases method over gRPC.

        Lists Releases in a given project and location.

        Returns:
            Callable[[~.ListReleasesRequest],
                    Awaitable[~.ListReleasesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_releases" not in self._stubs:
            self._stubs["list_releases"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListReleases",
                request_serializer=cloud_deploy.ListReleasesRequest.serialize,
                response_deserializer=cloud_deploy.ListReleasesResponse.deserialize,
            )
        return self._stubs["list_releases"]

    @property
    def get_release(
        self,
    ) -> Callable[[cloud_deploy.GetReleaseRequest], Awaitable[cloud_deploy.Release]]:
        r"""Return a callable for the get release method over gRPC.

        Gets details of a single Release.

        Returns:
            Callable[[~.GetReleaseRequest],
                    Awaitable[~.Release]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_release" not in self._stubs:
            self._stubs["get_release"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetRelease",
                request_serializer=cloud_deploy.GetReleaseRequest.serialize,
                response_deserializer=cloud_deploy.Release.deserialize,
            )
        return self._stubs["get_release"]

    @property
    def create_release(
        self,
    ) -> Callable[
        [cloud_deploy.CreateReleaseRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create release method over gRPC.

        Creates a new Release in a given project and
        location.

        Returns:
            Callable[[~.CreateReleaseRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_release" not in self._stubs:
            self._stubs["create_release"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CreateRelease",
                request_serializer=cloud_deploy.CreateReleaseRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_release"]

    @property
    def abandon_release(
        self,
    ) -> Callable[
        [cloud_deploy.AbandonReleaseRequest],
        Awaitable[cloud_deploy.AbandonReleaseResponse],
    ]:
        r"""Return a callable for the abandon release method over gRPC.

        Abandons a Release in the Delivery Pipeline.

        Returns:
            Callable[[~.AbandonReleaseRequest],
                    Awaitable[~.AbandonReleaseResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "abandon_release" not in self._stubs:
            self._stubs["abandon_release"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/AbandonRelease",
                request_serializer=cloud_deploy.AbandonReleaseRequest.serialize,
                response_deserializer=cloud_deploy.AbandonReleaseResponse.deserialize,
            )
        return self._stubs["abandon_release"]

    @property
    def create_deploy_policy(
        self,
    ) -> Callable[
        [cloud_deploy.CreateDeployPolicyRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create deploy policy method over gRPC.

        Creates a new DeployPolicy in a given project and
        location.

        Returns:
            Callable[[~.CreateDeployPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_deploy_policy" not in self._stubs:
            self._stubs["create_deploy_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CreateDeployPolicy",
                request_serializer=cloud_deploy.CreateDeployPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_deploy_policy"]

    @property
    def update_deploy_policy(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateDeployPolicyRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update deploy policy method over gRPC.

        Updates the parameters of a single DeployPolicy.

        Returns:
            Callable[[~.UpdateDeployPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_deploy_policy" not in self._stubs:
            self._stubs["update_deploy_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/UpdateDeployPolicy",
                request_serializer=cloud_deploy.UpdateDeployPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_deploy_policy"]

    @property
    def delete_deploy_policy(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteDeployPolicyRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete deploy policy method over gRPC.

        Deletes a single DeployPolicy.

        Returns:
            Callable[[~.DeleteDeployPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_deploy_policy" not in self._stubs:
            self._stubs["delete_deploy_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/DeleteDeployPolicy",
                request_serializer=cloud_deploy.DeleteDeployPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_deploy_policy"]

    @property
    def list_deploy_policies(
        self,
    ) -> Callable[
        [cloud_deploy.ListDeployPoliciesRequest],
        Awaitable[cloud_deploy.ListDeployPoliciesResponse],
    ]:
        r"""Return a callable for the list deploy policies method over gRPC.

        Lists DeployPolicies in a given project and location.

        Returns:
            Callable[[~.ListDeployPoliciesRequest],
                    Awaitable[~.ListDeployPoliciesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deploy_policies" not in self._stubs:
            self._stubs["list_deploy_policies"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListDeployPolicies",
                request_serializer=cloud_deploy.ListDeployPoliciesRequest.serialize,
                response_deserializer=cloud_deploy.ListDeployPoliciesResponse.deserialize,
            )
        return self._stubs["list_deploy_policies"]

    @property
    def get_deploy_policy(
        self,
    ) -> Callable[
        [cloud_deploy.GetDeployPolicyRequest], Awaitable[cloud_deploy.DeployPolicy]
    ]:
        r"""Return a callable for the get deploy policy method over gRPC.

        Gets details of a single DeployPolicy.

        Returns:
            Callable[[~.GetDeployPolicyRequest],
                    Awaitable[~.DeployPolicy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deploy_policy" not in self._stubs:
            self._stubs["get_deploy_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetDeployPolicy",
                request_serializer=cloud_deploy.GetDeployPolicyRequest.serialize,
                response_deserializer=cloud_deploy.DeployPolicy.deserialize,
            )
        return self._stubs["get_deploy_policy"]

    @property
    def approve_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.ApproveRolloutRequest],
        Awaitable[cloud_deploy.ApproveRolloutResponse],
    ]:
        r"""Return a callable for the approve rollout method over gRPC.

        Approves a Rollout.

        Returns:
            Callable[[~.ApproveRolloutRequest],
                    Awaitable[~.ApproveRolloutResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "approve_rollout" not in self._stubs:
            self._stubs["approve_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ApproveRollout",
                request_serializer=cloud_deploy.ApproveRolloutRequest.serialize,
                response_deserializer=cloud_deploy.ApproveRolloutResponse.deserialize,
            )
        return self._stubs["approve_rollout"]

    @property
    def advance_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.AdvanceRolloutRequest],
        Awaitable[cloud_deploy.AdvanceRolloutResponse],
    ]:
        r"""Return a callable for the advance rollout method over gRPC.

        Advances a Rollout in a given project and location.

        Returns:
            Callable[[~.AdvanceRolloutRequest],
                    Awaitable[~.AdvanceRolloutResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "advance_rollout" not in self._stubs:
            self._stubs["advance_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/AdvanceRollout",
                request_serializer=cloud_deploy.AdvanceRolloutRequest.serialize,
                response_deserializer=cloud_deploy.AdvanceRolloutResponse.deserialize,
            )
        return self._stubs["advance_rollout"]

    @property
    def cancel_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.CancelRolloutRequest],
        Awaitable[cloud_deploy.CancelRolloutResponse],
    ]:
        r"""Return a callable for the cancel rollout method over gRPC.

        Cancels a Rollout in a given project and location.

        Returns:
            Callable[[~.CancelRolloutRequest],
                    Awaitable[~.CancelRolloutResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_rollout" not in self._stubs:
            self._stubs["cancel_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CancelRollout",
                request_serializer=cloud_deploy.CancelRolloutRequest.serialize,
                response_deserializer=cloud_deploy.CancelRolloutResponse.deserialize,
            )
        return self._stubs["cancel_rollout"]

    @property
    def list_rollouts(
        self,
    ) -> Callable[
        [cloud_deploy.ListRolloutsRequest], Awaitable[cloud_deploy.ListRolloutsResponse]
    ]:
        r"""Return a callable for the list rollouts method over gRPC.

        Lists Rollouts in a given project and location.

        Returns:
            Callable[[~.ListRolloutsRequest],
                    Awaitable[~.ListRolloutsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_rollouts" not in self._stubs:
            self._stubs["list_rollouts"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListRollouts",
                request_serializer=cloud_deploy.ListRolloutsRequest.serialize,
                response_deserializer=cloud_deploy.ListRolloutsResponse.deserialize,
            )
        return self._stubs["list_rollouts"]

    @property
    def get_rollout(
        self,
    ) -> Callable[[cloud_deploy.GetRolloutRequest], Awaitable[cloud_deploy.Rollout]]:
        r"""Return a callable for the get rollout method over gRPC.

        Gets details of a single Rollout.

        Returns:
            Callable[[~.GetRolloutRequest],
                    Awaitable[~.Rollout]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_rollout" not in self._stubs:
            self._stubs["get_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetRollout",
                request_serializer=cloud_deploy.GetRolloutRequest.serialize,
                response_deserializer=cloud_deploy.Rollout.deserialize,
            )
        return self._stubs["get_rollout"]

    @property
    def create_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.CreateRolloutRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create rollout method over gRPC.

        Creates a new Rollout in a given project and
        location.

        Returns:
            Callable[[~.CreateRolloutRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_rollout" not in self._stubs:
            self._stubs["create_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CreateRollout",
                request_serializer=cloud_deploy.CreateRolloutRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_rollout"]

    @property
    def ignore_job(
        self,
    ) -> Callable[
        [cloud_deploy.IgnoreJobRequest], Awaitable[cloud_deploy.IgnoreJobResponse]
    ]:
        r"""Return a callable for the ignore job method over gRPC.

        Ignores the specified Job in a Rollout.

        Returns:
            Callable[[~.IgnoreJobRequest],
                    Awaitable[~.IgnoreJobResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "ignore_job" not in self._stubs:
            self._stubs["ignore_job"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/IgnoreJob",
                request_serializer=cloud_deploy.IgnoreJobRequest.serialize,
                response_deserializer=cloud_deploy.IgnoreJobResponse.deserialize,
            )
        return self._stubs["ignore_job"]

    @property
    def retry_job(
        self,
    ) -> Callable[
        [cloud_deploy.RetryJobRequest], Awaitable[cloud_deploy.RetryJobResponse]
    ]:
        r"""Return a callable for the retry job method over gRPC.

        Retries the specified Job in a Rollout.

        Returns:
            Callable[[~.RetryJobRequest],
                    Awaitable[~.RetryJobResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retry_job" not in self._stubs:
            self._stubs["retry_job"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/RetryJob",
                request_serializer=cloud_deploy.RetryJobRequest.serialize,
                response_deserializer=cloud_deploy.RetryJobResponse.deserialize,
            )
        return self._stubs["retry_job"]

    @property
    def list_job_runs(
        self,
    ) -> Callable[
        [cloud_deploy.ListJobRunsRequest], Awaitable[cloud_deploy.ListJobRunsResponse]
    ]:
        r"""Return a callable for the list job runs method over gRPC.

        Lists JobRuns in a given project and location.

        Returns:
            Callable[[~.ListJobRunsRequest],
                    Awaitable[~.ListJobRunsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_job_runs" not in self._stubs:
            self._stubs["list_job_runs"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListJobRuns",
                request_serializer=cloud_deploy.ListJobRunsRequest.serialize,
                response_deserializer=cloud_deploy.ListJobRunsResponse.deserialize,
            )
        return self._stubs["list_job_runs"]

    @property
    def get_job_run(
        self,
    ) -> Callable[[cloud_deploy.GetJobRunRequest], Awaitable[cloud_deploy.JobRun]]:
        r"""Return a callable for the get job run method over gRPC.

        Gets details of a single JobRun.

        Returns:
            Callable[[~.GetJobRunRequest],
                    Awaitable[~.JobRun]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_job_run" not in self._stubs:
            self._stubs["get_job_run"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetJobRun",
                request_serializer=cloud_deploy.GetJobRunRequest.serialize,
                response_deserializer=cloud_deploy.JobRun.deserialize,
            )
        return self._stubs["get_job_run"]

    @property
    def terminate_job_run(
        self,
    ) -> Callable[
        [cloud_deploy.TerminateJobRunRequest],
        Awaitable[cloud_deploy.TerminateJobRunResponse],
    ]:
        r"""Return a callable for the terminate job run method over gRPC.

        Terminates a Job Run in a given project and location.

        Returns:
            Callable[[~.TerminateJobRunRequest],
                    Awaitable[~.TerminateJobRunResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "terminate_job_run" not in self._stubs:
            self._stubs["terminate_job_run"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/TerminateJobRun",
                request_serializer=cloud_deploy.TerminateJobRunRequest.serialize,
                response_deserializer=cloud_deploy.TerminateJobRunResponse.deserialize,
            )
        return self._stubs["terminate_job_run"]

    @property
    def get_config(
        self,
    ) -> Callable[[cloud_deploy.GetConfigRequest], Awaitable[cloud_deploy.Config]]:
        r"""Return a callable for the get config method over gRPC.

        Gets the configuration for a location.

        Returns:
            Callable[[~.GetConfigRequest],
                    Awaitable[~.Config]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_config" not in self._stubs:
            self._stubs["get_config"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetConfig",
                request_serializer=cloud_deploy.GetConfigRequest.serialize,
                response_deserializer=cloud_deploy.Config.deserialize,
            )
        return self._stubs["get_config"]

    @property
    def create_automation(
        self,
    ) -> Callable[
        [cloud_deploy.CreateAutomationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create automation method over gRPC.

        Creates a new Automation in a given project and
        location.

        Returns:
            Callable[[~.CreateAutomationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_automation" not in self._stubs:
            self._stubs["create_automation"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CreateAutomation",
                request_serializer=cloud_deploy.CreateAutomationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_automation"]

    @property
    def update_automation(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateAutomationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update automation method over gRPC.

        Updates the parameters of a single Automation
        resource.

        Returns:
            Callable[[~.UpdateAutomationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_automation" not in self._stubs:
            self._stubs["update_automation"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/UpdateAutomation",
                request_serializer=cloud_deploy.UpdateAutomationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_automation"]

    @property
    def delete_automation(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteAutomationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete automation method over gRPC.

        Deletes a single Automation resource.

        Returns:
            Callable[[~.DeleteAutomationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_automation" not in self._stubs:
            self._stubs["delete_automation"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/DeleteAutomation",
                request_serializer=cloud_deploy.DeleteAutomationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_automation"]

    @property
    def get_automation(
        self,
    ) -> Callable[
        [cloud_deploy.GetAutomationRequest], Awaitable[cloud_deploy.Automation]
    ]:
        r"""Return a callable for the get automation method over gRPC.

        Gets details of a single Automation.

        Returns:
            Callable[[~.GetAutomationRequest],
                    Awaitable[~.Automation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_automation" not in self._stubs:
            self._stubs["get_automation"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetAutomation",
                request_serializer=cloud_deploy.GetAutomationRequest.serialize,
                response_deserializer=cloud_deploy.Automation.deserialize,
            )
        return self._stubs["get_automation"]

    @property
    def list_automations(
        self,
    ) -> Callable[
        [cloud_deploy.ListAutomationsRequest],
        Awaitable[cloud_deploy.ListAutomationsResponse],
    ]:
        r"""Return a callable for the list automations method over gRPC.

        Lists Automations in a given project and location.

        Returns:
            Callable[[~.ListAutomationsRequest],
                    Awaitable[~.ListAutomationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_automations" not in self._stubs:
            self._stubs["list_automations"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListAutomations",
                request_serializer=cloud_deploy.ListAutomationsRequest.serialize,
                response_deserializer=cloud_deploy.ListAutomationsResponse.deserialize,
            )
        return self._stubs["list_automations"]

    @property
    def get_automation_run(
        self,
    ) -> Callable[
        [cloud_deploy.GetAutomationRunRequest], Awaitable[cloud_deploy.AutomationRun]
    ]:
        r"""Return a callable for the get automation run method over gRPC.

        Gets details of a single AutomationRun.

        Returns:
            Callable[[~.GetAutomationRunRequest],
                    Awaitable[~.AutomationRun]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_automation_run" not in self._stubs:
            self._stubs["get_automation_run"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/GetAutomationRun",
                request_serializer=cloud_deploy.GetAutomationRunRequest.serialize,
                response_deserializer=cloud_deploy.AutomationRun.deserialize,
            )
        return self._stubs["get_automation_run"]

    @property
    def list_automation_runs(
        self,
    ) -> Callable[
        [cloud_deploy.ListAutomationRunsRequest],
        Awaitable[cloud_deploy.ListAutomationRunsResponse],
    ]:
        r"""Return a callable for the list automation runs method over gRPC.

        Lists AutomationRuns in a given project and location.

        Returns:
            Callable[[~.ListAutomationRunsRequest],
                    Awaitable[~.ListAutomationRunsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_automation_runs" not in self._stubs:
            self._stubs["list_automation_runs"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/ListAutomationRuns",
                request_serializer=cloud_deploy.ListAutomationRunsRequest.serialize,
                response_deserializer=cloud_deploy.ListAutomationRunsResponse.deserialize,
            )
        return self._stubs["list_automation_runs"]

    @property
    def cancel_automation_run(
        self,
    ) -> Callable[
        [cloud_deploy.CancelAutomationRunRequest],
        Awaitable[cloud_deploy.CancelAutomationRunResponse],
    ]:
        r"""Return a callable for the cancel automation run method over gRPC.

        Cancels an AutomationRun. The ``state`` of the ``AutomationRun``
        after cancelling is ``CANCELLED``. ``CancelAutomationRun`` can
        be called on AutomationRun in the state ``IN_PROGRESS`` and
        ``PENDING``; AutomationRun in a different state returns an
        ``FAILED_PRECONDITION`` error.

        Returns:
            Callable[[~.CancelAutomationRunRequest],
                    Awaitable[~.CancelAutomationRunResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_automation_run" not in self._stubs:
            self._stubs["cancel_automation_run"] = self._logged_channel.unary_unary(
                "/google.cloud.deploy.v1.CloudDeploy/CancelAutomationRun",
                request_serializer=cloud_deploy.CancelAutomationRunRequest.serialize,
                response_deserializer=cloud_deploy.CancelAutomationRunResponse.deserialize,
            )
        return self._stubs["cancel_automation_run"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_delivery_pipelines: self._wrap_method(
                self.list_delivery_pipelines,
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
            self.get_delivery_pipeline: self._wrap_method(
                self.get_delivery_pipeline,
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
            self.create_delivery_pipeline: self._wrap_method(
                self.create_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_delivery_pipeline: self._wrap_method(
                self.update_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_delivery_pipeline: self._wrap_method(
                self.delete_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_targets: self._wrap_method(
                self.list_targets,
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
            self.rollback_target: self._wrap_method(
                self.rollback_target,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_target: self._wrap_method(
                self.get_target,
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
            self.create_target: self._wrap_method(
                self.create_target,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_target: self._wrap_method(
                self.update_target,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_target: self._wrap_method(
                self.delete_target,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_custom_target_types: self._wrap_method(
                self.list_custom_target_types,
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
            self.get_custom_target_type: self._wrap_method(
                self.get_custom_target_type,
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
            self.create_custom_target_type: self._wrap_method(
                self.create_custom_target_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_custom_target_type: self._wrap_method(
                self.update_custom_target_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_custom_target_type: self._wrap_method(
                self.delete_custom_target_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_releases: self._wrap_method(
                self.list_releases,
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
            self.get_release: self._wrap_method(
                self.get_release,
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
            self.create_release: self._wrap_method(
                self.create_release,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.abandon_release: self._wrap_method(
                self.abandon_release,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_deploy_policy: self._wrap_method(
                self.create_deploy_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_deploy_policy: self._wrap_method(
                self.update_deploy_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_deploy_policy: self._wrap_method(
                self.delete_deploy_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_deploy_policies: self._wrap_method(
                self.list_deploy_policies,
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
            self.get_deploy_policy: self._wrap_method(
                self.get_deploy_policy,
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
            self.approve_rollout: self._wrap_method(
                self.approve_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.advance_rollout: self._wrap_method(
                self.advance_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.cancel_rollout: self._wrap_method(
                self.cancel_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_rollouts: self._wrap_method(
                self.list_rollouts,
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
            self.get_rollout: self._wrap_method(
                self.get_rollout,
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
            self.create_rollout: self._wrap_method(
                self.create_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.ignore_job: self._wrap_method(
                self.ignore_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.retry_job: self._wrap_method(
                self.retry_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_job_runs: self._wrap_method(
                self.list_job_runs,
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
            self.get_job_run: self._wrap_method(
                self.get_job_run,
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
            self.terminate_job_run: self._wrap_method(
                self.terminate_job_run,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_config: self._wrap_method(
                self.get_config,
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
            self.create_automation: self._wrap_method(
                self.create_automation,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_automation: self._wrap_method(
                self.update_automation,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_automation: self._wrap_method(
                self.delete_automation,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_automation: self._wrap_method(
                self.get_automation,
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
            self.list_automations: self._wrap_method(
                self.list_automations,
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
            self.get_automation_run: self._wrap_method(
                self.get_automation_run,
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
            self.list_automation_runs: self._wrap_method(
                self.list_automation_runs,
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
            self.cancel_automation_run: self._wrap_method(
                self.cancel_automation_run,
                default_timeout=60.0,
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


__all__ = ("CloudDeployGrpcAsyncIOTransport",)
