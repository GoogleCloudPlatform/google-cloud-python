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
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.securesourcemanager_v1.types import secure_source_manager

from .base import DEFAULT_CLIENT_INFO, SecureSourceManagerTransport

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
                    "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
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
                    "serviceName": "google.cloud.securesourcemanager.v1.SecureSourceManager",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class SecureSourceManagerGrpcTransport(SecureSourceManagerTransport):
    """gRPC backend transport for SecureSourceManager.

    Secure Source Manager API

    Access Secure Source Manager instances, resources, and
    repositories.

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
        host: str = "securesourcemanager.googleapis.com",
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
                 The hostname to connect to (default: 'securesourcemanager.googleapis.com').
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
        host: str = "securesourcemanager.googleapis.com",
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
    def list_instances(
        self,
    ) -> Callable[
        [secure_source_manager.ListInstancesRequest],
        secure_source_manager.ListInstancesResponse,
    ]:
        r"""Return a callable for the list instances method over gRPC.

        Lists Instances in a given project and location.

        Returns:
            Callable[[~.ListInstancesRequest],
                    ~.ListInstancesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_instances" not in self._stubs:
            self._stubs["list_instances"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListInstances",
                request_serializer=secure_source_manager.ListInstancesRequest.serialize,
                response_deserializer=secure_source_manager.ListInstancesResponse.deserialize,
            )
        return self._stubs["list_instances"]

    @property
    def get_instance(
        self,
    ) -> Callable[
        [secure_source_manager.GetInstanceRequest], secure_source_manager.Instance
    ]:
        r"""Return a callable for the get instance method over gRPC.

        Gets details of a single instance.

        Returns:
            Callable[[~.GetInstanceRequest],
                    ~.Instance]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_instance" not in self._stubs:
            self._stubs["get_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetInstance",
                request_serializer=secure_source_manager.GetInstanceRequest.serialize,
                response_deserializer=secure_source_manager.Instance.deserialize,
            )
        return self._stubs["get_instance"]

    @property
    def create_instance(
        self,
    ) -> Callable[
        [secure_source_manager.CreateInstanceRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create instance method over gRPC.

        Creates a new instance in a given project and
        location.

        Returns:
            Callable[[~.CreateInstanceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_instance" not in self._stubs:
            self._stubs["create_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/CreateInstance",
                request_serializer=secure_source_manager.CreateInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_instance"]

    @property
    def delete_instance(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteInstanceRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete instance method over gRPC.

        Deletes a single instance.

        Returns:
            Callable[[~.DeleteInstanceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_instance" not in self._stubs:
            self._stubs["delete_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/DeleteInstance",
                request_serializer=secure_source_manager.DeleteInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_instance"]

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [secure_source_manager.ListRepositoriesRequest],
        secure_source_manager.ListRepositoriesResponse,
    ]:
        r"""Return a callable for the list repositories method over gRPC.

        Lists Repositories in a given project and location.

        The instance field is required in the query parameter
        for requests using the
        securesourcemanager.googleapis.com endpoint.

        Returns:
            Callable[[~.ListRepositoriesRequest],
                    ~.ListRepositoriesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_repositories" not in self._stubs:
            self._stubs["list_repositories"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListRepositories",
                request_serializer=secure_source_manager.ListRepositoriesRequest.serialize,
                response_deserializer=secure_source_manager.ListRepositoriesResponse.deserialize,
            )
        return self._stubs["list_repositories"]

    @property
    def get_repository(
        self,
    ) -> Callable[
        [secure_source_manager.GetRepositoryRequest], secure_source_manager.Repository
    ]:
        r"""Return a callable for the get repository method over gRPC.

        Gets metadata of a repository.

        Returns:
            Callable[[~.GetRepositoryRequest],
                    ~.Repository]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_repository" not in self._stubs:
            self._stubs["get_repository"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetRepository",
                request_serializer=secure_source_manager.GetRepositoryRequest.serialize,
                response_deserializer=secure_source_manager.Repository.deserialize,
            )
        return self._stubs["get_repository"]

    @property
    def create_repository(
        self,
    ) -> Callable[
        [secure_source_manager.CreateRepositoryRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create repository method over gRPC.

        Creates a new repository in a given project and
        location.
        The Repository.Instance field is required in the request
        body for requests using the
        securesourcemanager.googleapis.com endpoint.

        Returns:
            Callable[[~.CreateRepositoryRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_repository" not in self._stubs:
            self._stubs["create_repository"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/CreateRepository",
                request_serializer=secure_source_manager.CreateRepositoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_repository"]

    @property
    def update_repository(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateRepositoryRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update repository method over gRPC.

        Updates the metadata of a repository.

        Returns:
            Callable[[~.UpdateRepositoryRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_repository" not in self._stubs:
            self._stubs["update_repository"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/UpdateRepository",
                request_serializer=secure_source_manager.UpdateRepositoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_repository"]

    @property
    def delete_repository(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteRepositoryRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete repository method over gRPC.

        Deletes a Repository.

        Returns:
            Callable[[~.DeleteRepositoryRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_repository" not in self._stubs:
            self._stubs["delete_repository"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/DeleteRepository",
                request_serializer=secure_source_manager.DeleteRepositoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_repository"]

    @property
    def list_hooks(
        self,
    ) -> Callable[
        [secure_source_manager.ListHooksRequest],
        secure_source_manager.ListHooksResponse,
    ]:
        r"""Return a callable for the list hooks method over gRPC.

        Lists hooks in a given repository.

        Returns:
            Callable[[~.ListHooksRequest],
                    ~.ListHooksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hooks" not in self._stubs:
            self._stubs["list_hooks"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListHooks",
                request_serializer=secure_source_manager.ListHooksRequest.serialize,
                response_deserializer=secure_source_manager.ListHooksResponse.deserialize,
            )
        return self._stubs["list_hooks"]

    @property
    def get_hook(
        self,
    ) -> Callable[[secure_source_manager.GetHookRequest], secure_source_manager.Hook]:
        r"""Return a callable for the get hook method over gRPC.

        Gets metadata of a hook.

        Returns:
            Callable[[~.GetHookRequest],
                    ~.Hook]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hook" not in self._stubs:
            self._stubs["get_hook"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetHook",
                request_serializer=secure_source_manager.GetHookRequest.serialize,
                response_deserializer=secure_source_manager.Hook.deserialize,
            )
        return self._stubs["get_hook"]

    @property
    def create_hook(
        self,
    ) -> Callable[[secure_source_manager.CreateHookRequest], operations_pb2.Operation]:
        r"""Return a callable for the create hook method over gRPC.

        Creates a new hook in a given repository.

        Returns:
            Callable[[~.CreateHookRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hook" not in self._stubs:
            self._stubs["create_hook"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/CreateHook",
                request_serializer=secure_source_manager.CreateHookRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_hook"]

    @property
    def update_hook(
        self,
    ) -> Callable[[secure_source_manager.UpdateHookRequest], operations_pb2.Operation]:
        r"""Return a callable for the update hook method over gRPC.

        Updates the metadata of a hook.

        Returns:
            Callable[[~.UpdateHookRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_hook" not in self._stubs:
            self._stubs["update_hook"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/UpdateHook",
                request_serializer=secure_source_manager.UpdateHookRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_hook"]

    @property
    def delete_hook(
        self,
    ) -> Callable[[secure_source_manager.DeleteHookRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete hook method over gRPC.

        Deletes a Hook.

        Returns:
            Callable[[~.DeleteHookRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_hook" not in self._stubs:
            self._stubs["delete_hook"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/DeleteHook",
                request_serializer=secure_source_manager.DeleteHookRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_hook"]

    @property
    def get_iam_policy_repo(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy repo method over gRPC.

        Get IAM policy for a repository.

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
        if "get_iam_policy_repo" not in self._stubs:
            self._stubs["get_iam_policy_repo"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetIamPolicyRepo",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy_repo"]

    @property
    def set_iam_policy_repo(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy repo method over gRPC.

        Set IAM policy on a repository.

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
        if "set_iam_policy_repo" not in self._stubs:
            self._stubs["set_iam_policy_repo"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/SetIamPolicyRepo",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy_repo"]

    @property
    def test_iam_permissions_repo(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        r"""Return a callable for the test iam permissions repo method over gRPC.

        Test IAM permissions on a repository.
        IAM permission checks are not required on this method.

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
        if "test_iam_permissions_repo" not in self._stubs:
            self._stubs["test_iam_permissions_repo"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/TestIamPermissionsRepo",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions_repo"]

    @property
    def create_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.CreateBranchRuleRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create branch rule method over gRPC.

        CreateBranchRule creates a branch rule in a given
        repository.

        Returns:
            Callable[[~.CreateBranchRuleRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_branch_rule" not in self._stubs:
            self._stubs["create_branch_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/CreateBranchRule",
                request_serializer=secure_source_manager.CreateBranchRuleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_branch_rule"]

    @property
    def list_branch_rules(
        self,
    ) -> Callable[
        [secure_source_manager.ListBranchRulesRequest],
        secure_source_manager.ListBranchRulesResponse,
    ]:
        r"""Return a callable for the list branch rules method over gRPC.

        ListBranchRules lists branch rules in a given
        repository.

        Returns:
            Callable[[~.ListBranchRulesRequest],
                    ~.ListBranchRulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_branch_rules" not in self._stubs:
            self._stubs["list_branch_rules"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListBranchRules",
                request_serializer=secure_source_manager.ListBranchRulesRequest.serialize,
                response_deserializer=secure_source_manager.ListBranchRulesResponse.deserialize,
            )
        return self._stubs["list_branch_rules"]

    @property
    def get_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.GetBranchRuleRequest], secure_source_manager.BranchRule
    ]:
        r"""Return a callable for the get branch rule method over gRPC.

        GetBranchRule gets a branch rule.

        Returns:
            Callable[[~.GetBranchRuleRequest],
                    ~.BranchRule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_branch_rule" not in self._stubs:
            self._stubs["get_branch_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetBranchRule",
                request_serializer=secure_source_manager.GetBranchRuleRequest.serialize,
                response_deserializer=secure_source_manager.BranchRule.deserialize,
            )
        return self._stubs["get_branch_rule"]

    @property
    def update_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateBranchRuleRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update branch rule method over gRPC.

        UpdateBranchRule updates a branch rule.

        Returns:
            Callable[[~.UpdateBranchRuleRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_branch_rule" not in self._stubs:
            self._stubs["update_branch_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/UpdateBranchRule",
                request_serializer=secure_source_manager.UpdateBranchRuleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_branch_rule"]

    @property
    def delete_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteBranchRuleRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete branch rule method over gRPC.

        DeleteBranchRule deletes a branch rule.

        Returns:
            Callable[[~.DeleteBranchRuleRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_branch_rule" not in self._stubs:
            self._stubs["delete_branch_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/DeleteBranchRule",
                request_serializer=secure_source_manager.DeleteBranchRuleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_branch_rule"]

    @property
    def create_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.CreatePullRequestRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create pull request method over gRPC.

        Creates a pull request.

        Returns:
            Callable[[~.CreatePullRequestRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_pull_request" not in self._stubs:
            self._stubs["create_pull_request"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/CreatePullRequest",
                request_serializer=secure_source_manager.CreatePullRequestRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_pull_request"]

    @property
    def get_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.GetPullRequestRequest], secure_source_manager.PullRequest
    ]:
        r"""Return a callable for the get pull request method over gRPC.

        Gets a pull request.

        Returns:
            Callable[[~.GetPullRequestRequest],
                    ~.PullRequest]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_pull_request" not in self._stubs:
            self._stubs["get_pull_request"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetPullRequest",
                request_serializer=secure_source_manager.GetPullRequestRequest.serialize,
                response_deserializer=secure_source_manager.PullRequest.deserialize,
            )
        return self._stubs["get_pull_request"]

    @property
    def list_pull_requests(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestsRequest],
        secure_source_manager.ListPullRequestsResponse,
    ]:
        r"""Return a callable for the list pull requests method over gRPC.

        Lists pull requests in a repository.

        Returns:
            Callable[[~.ListPullRequestsRequest],
                    ~.ListPullRequestsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_pull_requests" not in self._stubs:
            self._stubs["list_pull_requests"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListPullRequests",
                request_serializer=secure_source_manager.ListPullRequestsRequest.serialize,
                response_deserializer=secure_source_manager.ListPullRequestsResponse.deserialize,
            )
        return self._stubs["list_pull_requests"]

    @property
    def update_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.UpdatePullRequestRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update pull request method over gRPC.

        Updates a pull request.

        Returns:
            Callable[[~.UpdatePullRequestRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_pull_request" not in self._stubs:
            self._stubs["update_pull_request"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/UpdatePullRequest",
                request_serializer=secure_source_manager.UpdatePullRequestRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_pull_request"]

    @property
    def merge_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.MergePullRequestRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the merge pull request method over gRPC.

        Merges a pull request.

        Returns:
            Callable[[~.MergePullRequestRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "merge_pull_request" not in self._stubs:
            self._stubs["merge_pull_request"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/MergePullRequest",
                request_serializer=secure_source_manager.MergePullRequestRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["merge_pull_request"]

    @property
    def open_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.OpenPullRequestRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the open pull request method over gRPC.

        Opens a pull request.

        Returns:
            Callable[[~.OpenPullRequestRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "open_pull_request" not in self._stubs:
            self._stubs["open_pull_request"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/OpenPullRequest",
                request_serializer=secure_source_manager.OpenPullRequestRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["open_pull_request"]

    @property
    def close_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.ClosePullRequestRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the close pull request method over gRPC.

        Closes a pull request without merging.

        Returns:
            Callable[[~.ClosePullRequestRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "close_pull_request" not in self._stubs:
            self._stubs["close_pull_request"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/ClosePullRequest",
                request_serializer=secure_source_manager.ClosePullRequestRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["close_pull_request"]

    @property
    def list_pull_request_file_diffs(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestFileDiffsRequest],
        secure_source_manager.ListPullRequestFileDiffsResponse,
    ]:
        r"""Return a callable for the list pull request file diffs method over gRPC.

        Lists a pull request's file diffs.

        Returns:
            Callable[[~.ListPullRequestFileDiffsRequest],
                    ~.ListPullRequestFileDiffsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_pull_request_file_diffs" not in self._stubs:
            self._stubs["list_pull_request_file_diffs"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListPullRequestFileDiffs",
                    request_serializer=secure_source_manager.ListPullRequestFileDiffsRequest.serialize,
                    response_deserializer=secure_source_manager.ListPullRequestFileDiffsResponse.deserialize,
                )
            )
        return self._stubs["list_pull_request_file_diffs"]

    @property
    def fetch_tree(
        self,
    ) -> Callable[
        [secure_source_manager.FetchTreeRequest],
        secure_source_manager.FetchTreeResponse,
    ]:
        r"""Return a callable for the fetch tree method over gRPC.

        Fetches a tree from a repository.

        Returns:
            Callable[[~.FetchTreeRequest],
                    ~.FetchTreeResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_tree" not in self._stubs:
            self._stubs["fetch_tree"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/FetchTree",
                request_serializer=secure_source_manager.FetchTreeRequest.serialize,
                response_deserializer=secure_source_manager.FetchTreeResponse.deserialize,
            )
        return self._stubs["fetch_tree"]

    @property
    def fetch_blob(
        self,
    ) -> Callable[
        [secure_source_manager.FetchBlobRequest],
        secure_source_manager.FetchBlobResponse,
    ]:
        r"""Return a callable for the fetch blob method over gRPC.

        Fetches a blob from a repository.

        Returns:
            Callable[[~.FetchBlobRequest],
                    ~.FetchBlobResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_blob" not in self._stubs:
            self._stubs["fetch_blob"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/FetchBlob",
                request_serializer=secure_source_manager.FetchBlobRequest.serialize,
                response_deserializer=secure_source_manager.FetchBlobResponse.deserialize,
            )
        return self._stubs["fetch_blob"]

    @property
    def fetch_refs(
        self,
    ) -> Callable[
        [secure_source_manager.FetchRefsRequest],
        secure_source_manager.FetchRefsResponse,
    ]:
        r"""Return a callable for the fetch refs method over gRPC.

        Fetches git references from a repository.

        Returns:
            Callable[[~.FetchRefsRequest],
                    ~.FetchRefsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_refs" not in self._stubs:
            self._stubs["fetch_refs"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/FetchRefs",
                request_serializer=secure_source_manager.FetchRefsRequest.serialize,
                response_deserializer=secure_source_manager.FetchRefsResponse.deserialize,
            )
        return self._stubs["fetch_refs"]

    @property
    def create_issue(
        self,
    ) -> Callable[[secure_source_manager.CreateIssueRequest], operations_pb2.Operation]:
        r"""Return a callable for the create issue method over gRPC.

        Creates an issue.

        Returns:
            Callable[[~.CreateIssueRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_issue" not in self._stubs:
            self._stubs["create_issue"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/CreateIssue",
                request_serializer=secure_source_manager.CreateIssueRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_issue"]

    @property
    def get_issue(
        self,
    ) -> Callable[[secure_source_manager.GetIssueRequest], secure_source_manager.Issue]:
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
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetIssue",
                request_serializer=secure_source_manager.GetIssueRequest.serialize,
                response_deserializer=secure_source_manager.Issue.deserialize,
            )
        return self._stubs["get_issue"]

    @property
    def list_issues(
        self,
    ) -> Callable[
        [secure_source_manager.ListIssuesRequest],
        secure_source_manager.ListIssuesResponse,
    ]:
        r"""Return a callable for the list issues method over gRPC.

        Lists issues in a repository.

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
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListIssues",
                request_serializer=secure_source_manager.ListIssuesRequest.serialize,
                response_deserializer=secure_source_manager.ListIssuesResponse.deserialize,
            )
        return self._stubs["list_issues"]

    @property
    def update_issue(
        self,
    ) -> Callable[[secure_source_manager.UpdateIssueRequest], operations_pb2.Operation]:
        r"""Return a callable for the update issue method over gRPC.

        Updates a issue.

        Returns:
            Callable[[~.UpdateIssueRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_issue" not in self._stubs:
            self._stubs["update_issue"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/UpdateIssue",
                request_serializer=secure_source_manager.UpdateIssueRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_issue"]

    @property
    def delete_issue(
        self,
    ) -> Callable[[secure_source_manager.DeleteIssueRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete issue method over gRPC.

        Deletes an issue.

        Returns:
            Callable[[~.DeleteIssueRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_issue" not in self._stubs:
            self._stubs["delete_issue"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/DeleteIssue",
                request_serializer=secure_source_manager.DeleteIssueRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_issue"]

    @property
    def open_issue(
        self,
    ) -> Callable[[secure_source_manager.OpenIssueRequest], operations_pb2.Operation]:
        r"""Return a callable for the open issue method over gRPC.

        Opens an issue.

        Returns:
            Callable[[~.OpenIssueRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "open_issue" not in self._stubs:
            self._stubs["open_issue"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/OpenIssue",
                request_serializer=secure_source_manager.OpenIssueRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["open_issue"]

    @property
    def close_issue(
        self,
    ) -> Callable[[secure_source_manager.CloseIssueRequest], operations_pb2.Operation]:
        r"""Return a callable for the close issue method over gRPC.

        Closes an issue.

        Returns:
            Callable[[~.CloseIssueRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "close_issue" not in self._stubs:
            self._stubs["close_issue"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/CloseIssue",
                request_serializer=secure_source_manager.CloseIssueRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["close_issue"]

    @property
    def get_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.GetPullRequestCommentRequest],
        secure_source_manager.PullRequestComment,
    ]:
        r"""Return a callable for the get pull request comment method over gRPC.

        Gets a pull request comment.

        Returns:
            Callable[[~.GetPullRequestCommentRequest],
                    ~.PullRequestComment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_pull_request_comment" not in self._stubs:
            self._stubs["get_pull_request_comment"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetPullRequestComment",
                request_serializer=secure_source_manager.GetPullRequestCommentRequest.serialize,
                response_deserializer=secure_source_manager.PullRequestComment.deserialize,
            )
        return self._stubs["get_pull_request_comment"]

    @property
    def list_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestCommentsRequest],
        secure_source_manager.ListPullRequestCommentsResponse,
    ]:
        r"""Return a callable for the list pull request comments method over gRPC.

        Lists pull request comments.

        Returns:
            Callable[[~.ListPullRequestCommentsRequest],
                    ~.ListPullRequestCommentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_pull_request_comments" not in self._stubs:
            self._stubs["list_pull_request_comments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListPullRequestComments",
                    request_serializer=secure_source_manager.ListPullRequestCommentsRequest.serialize,
                    response_deserializer=secure_source_manager.ListPullRequestCommentsResponse.deserialize,
                )
            )
        return self._stubs["list_pull_request_comments"]

    @property
    def create_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.CreatePullRequestCommentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create pull request comment method over gRPC.

        Creates a pull request comment. This function is used
        to create a single PullRequestComment of type Comment,
        or a single PullRequestComment of type Code that's
        replying to another PullRequestComment of type Code. Use
        BatchCreatePullRequestComments to create multiple
        PullRequestComments for code reviews.

        Returns:
            Callable[[~.CreatePullRequestCommentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_pull_request_comment" not in self._stubs:
            self._stubs["create_pull_request_comment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securesourcemanager.v1.SecureSourceManager/CreatePullRequestComment",
                    request_serializer=secure_source_manager.CreatePullRequestCommentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_pull_request_comment"]

    @property
    def update_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.UpdatePullRequestCommentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the update pull request comment method over gRPC.

        Updates a pull request comment.

        Returns:
            Callable[[~.UpdatePullRequestCommentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_pull_request_comment" not in self._stubs:
            self._stubs["update_pull_request_comment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securesourcemanager.v1.SecureSourceManager/UpdatePullRequestComment",
                    request_serializer=secure_source_manager.UpdatePullRequestCommentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_pull_request_comment"]

    @property
    def delete_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.DeletePullRequestCommentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete pull request comment method over gRPC.

        Deletes a pull request comment.

        Returns:
            Callable[[~.DeletePullRequestCommentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_pull_request_comment" not in self._stubs:
            self._stubs["delete_pull_request_comment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securesourcemanager.v1.SecureSourceManager/DeletePullRequestComment",
                    request_serializer=secure_source_manager.DeletePullRequestCommentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_pull_request_comment"]

    @property
    def batch_create_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.BatchCreatePullRequestCommentsRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the batch create pull request
        comments method over gRPC.

        Batch creates pull request comments. This function is
        used to create multiple PullRequestComments for code
        review. There needs to be exactly one PullRequestComment
        of type Review, and at most 100 PullRequestComments of
        type Code per request. The Position of the code comments
        must be unique within the request.

        Returns:
            Callable[[~.BatchCreatePullRequestCommentsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_pull_request_comments" not in self._stubs:
            self._stubs["batch_create_pull_request_comments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securesourcemanager.v1.SecureSourceManager/BatchCreatePullRequestComments",
                    request_serializer=secure_source_manager.BatchCreatePullRequestCommentsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["batch_create_pull_request_comments"]

    @property
    def resolve_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ResolvePullRequestCommentsRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the resolve pull request comments method over gRPC.

        Resolves pull request comments. A list of PullRequestComment
        names must be provided. The PullRequestComment names must be in
        the same conversation thread. If auto_fill is set, all comments
        in the conversation thread will be resolved.

        Returns:
            Callable[[~.ResolvePullRequestCommentsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "resolve_pull_request_comments" not in self._stubs:
            self._stubs["resolve_pull_request_comments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securesourcemanager.v1.SecureSourceManager/ResolvePullRequestComments",
                    request_serializer=secure_source_manager.ResolvePullRequestCommentsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["resolve_pull_request_comments"]

    @property
    def unresolve_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.UnresolvePullRequestCommentsRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the unresolve pull request
        comments method over gRPC.

        Unresolves pull request comments. A list of PullRequestComment
        names must be provided. The PullRequestComment names must be in
        the same conversation thread. If auto_fill is set, all comments
        in the conversation thread will be unresolved.

        Returns:
            Callable[[~.UnresolvePullRequestCommentsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "unresolve_pull_request_comments" not in self._stubs:
            self._stubs["unresolve_pull_request_comments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securesourcemanager.v1.SecureSourceManager/UnresolvePullRequestComments",
                    request_serializer=secure_source_manager.UnresolvePullRequestCommentsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["unresolve_pull_request_comments"]

    @property
    def create_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.CreateIssueCommentRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create issue comment method over gRPC.

        Creates an issue comment.

        Returns:
            Callable[[~.CreateIssueCommentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_issue_comment" not in self._stubs:
            self._stubs["create_issue_comment"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/CreateIssueComment",
                request_serializer=secure_source_manager.CreateIssueCommentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_issue_comment"]

    @property
    def get_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.GetIssueCommentRequest],
        secure_source_manager.IssueComment,
    ]:
        r"""Return a callable for the get issue comment method over gRPC.

        Gets an issue comment.

        Returns:
            Callable[[~.GetIssueCommentRequest],
                    ~.IssueComment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_issue_comment" not in self._stubs:
            self._stubs["get_issue_comment"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/GetIssueComment",
                request_serializer=secure_source_manager.GetIssueCommentRequest.serialize,
                response_deserializer=secure_source_manager.IssueComment.deserialize,
            )
        return self._stubs["get_issue_comment"]

    @property
    def list_issue_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ListIssueCommentsRequest],
        secure_source_manager.ListIssueCommentsResponse,
    ]:
        r"""Return a callable for the list issue comments method over gRPC.

        Lists comments in an issue.

        Returns:
            Callable[[~.ListIssueCommentsRequest],
                    ~.ListIssueCommentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_issue_comments" not in self._stubs:
            self._stubs["list_issue_comments"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/ListIssueComments",
                request_serializer=secure_source_manager.ListIssueCommentsRequest.serialize,
                response_deserializer=secure_source_manager.ListIssueCommentsResponse.deserialize,
            )
        return self._stubs["list_issue_comments"]

    @property
    def update_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateIssueCommentRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update issue comment method over gRPC.

        Updates an issue comment.

        Returns:
            Callable[[~.UpdateIssueCommentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_issue_comment" not in self._stubs:
            self._stubs["update_issue_comment"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/UpdateIssueComment",
                request_serializer=secure_source_manager.UpdateIssueCommentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_issue_comment"]

    @property
    def delete_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteIssueCommentRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete issue comment method over gRPC.

        Deletes an issue comment.

        Returns:
            Callable[[~.DeleteIssueCommentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_issue_comment" not in self._stubs:
            self._stubs["delete_issue_comment"] = self._logged_channel.unary_unary(
                "/google.cloud.securesourcemanager.v1.SecureSourceManager/DeleteIssueComment",
                request_serializer=secure_source_manager.DeleteIssueCommentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_issue_comment"]

    def close(self):
        self._logged_channel.close()

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

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("SecureSourceManagerGrpcTransport",)
