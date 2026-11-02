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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
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

from google.cloud.dataform_v1.types import dataform

from .base import DEFAULT_CLIENT_INFO, DataformTransport

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
                    "serviceName": "google.cloud.dataform.v1.Dataform",
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
                    "serviceName": "google.cloud.dataform.v1.Dataform",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DataformGrpcTransport(DataformTransport):
    """gRPC backend transport for Dataform.

    Dataform is a service to develop, create, document, test, and
    update curated tables in BigQuery.

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
        host: str = "dataform.googleapis.com",
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
                 The hostname to connect to (default: 'dataform.googleapis.com').
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
        host: str = "dataform.googleapis.com",
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
    def get_team_folder(
        self,
    ) -> Callable[[dataform.GetTeamFolderRequest], dataform.TeamFolder]:
        r"""Return a callable for the get team folder method over gRPC.

        Fetches a single TeamFolder.

        Returns:
            Callable[[~.GetTeamFolderRequest],
                    ~.TeamFolder]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_team_folder" not in self._stubs:
            self._stubs["get_team_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/GetTeamFolder",
                request_serializer=dataform.GetTeamFolderRequest.serialize,
                response_deserializer=dataform.TeamFolder.deserialize,
            )
        return self._stubs["get_team_folder"]

    @property
    def create_team_folder(
        self,
    ) -> Callable[[dataform.CreateTeamFolderRequest], dataform.TeamFolder]:
        r"""Return a callable for the create team folder method over gRPC.

        Creates a new TeamFolder in a given project and
        location.

        Returns:
            Callable[[~.CreateTeamFolderRequest],
                    ~.TeamFolder]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_team_folder" not in self._stubs:
            self._stubs["create_team_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CreateTeamFolder",
                request_serializer=dataform.CreateTeamFolderRequest.serialize,
                response_deserializer=dataform.TeamFolder.deserialize,
            )
        return self._stubs["create_team_folder"]

    @property
    def update_team_folder(
        self,
    ) -> Callable[[dataform.UpdateTeamFolderRequest], dataform.TeamFolder]:
        r"""Return a callable for the update team folder method over gRPC.

        Updates a single TeamFolder.

        Returns:
            Callable[[~.UpdateTeamFolderRequest],
                    ~.TeamFolder]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_team_folder" not in self._stubs:
            self._stubs["update_team_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/UpdateTeamFolder",
                request_serializer=dataform.UpdateTeamFolderRequest.serialize,
                response_deserializer=dataform.TeamFolder.deserialize,
            )
        return self._stubs["update_team_folder"]

    @property
    def delete_team_folder(
        self,
    ) -> Callable[[dataform.DeleteTeamFolderRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete team folder method over gRPC.

        Deletes a single TeamFolder.

        Returns:
            Callable[[~.DeleteTeamFolderRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_team_folder" not in self._stubs:
            self._stubs["delete_team_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/DeleteTeamFolder",
                request_serializer=dataform.DeleteTeamFolderRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_team_folder"]

    @property
    def delete_team_folder_tree(
        self,
    ) -> Callable[[dataform.DeleteTeamFolderTreeRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete team folder tree method over gRPC.

        Deletes a TeamFolder with its contents (Folders,
        Repositories, Workspaces, ReleaseConfigs, and
        WorkflowConfigs).

        Returns:
            Callable[[~.DeleteTeamFolderTreeRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_team_folder_tree" not in self._stubs:
            self._stubs["delete_team_folder_tree"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/DeleteTeamFolderTree",
                request_serializer=dataform.DeleteTeamFolderTreeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_team_folder_tree"]

    @property
    def query_team_folder_contents(
        self,
    ) -> Callable[
        [dataform.QueryTeamFolderContentsRequest],
        dataform.QueryTeamFolderContentsResponse,
    ]:
        r"""Return a callable for the query team folder contents method over gRPC.

        Returns the contents of a given TeamFolder.

        Returns:
            Callable[[~.QueryTeamFolderContentsRequest],
                    ~.QueryTeamFolderContentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_team_folder_contents" not in self._stubs:
            self._stubs["query_team_folder_contents"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.dataform.v1.Dataform/QueryTeamFolderContents",
                    request_serializer=dataform.QueryTeamFolderContentsRequest.serialize,
                    response_deserializer=dataform.QueryTeamFolderContentsResponse.deserialize,
                )
            )
        return self._stubs["query_team_folder_contents"]

    @property
    def search_team_folders(
        self,
    ) -> Callable[
        [dataform.SearchTeamFoldersRequest], dataform.SearchTeamFoldersResponse
    ]:
        r"""Return a callable for the search team folders method over gRPC.

        Returns all TeamFolders in a given location that the
        caller has access to and match the provided filter.

        Returns:
            Callable[[~.SearchTeamFoldersRequest],
                    ~.SearchTeamFoldersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_team_folders" not in self._stubs:
            self._stubs["search_team_folders"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/SearchTeamFolders",
                request_serializer=dataform.SearchTeamFoldersRequest.serialize,
                response_deserializer=dataform.SearchTeamFoldersResponse.deserialize,
            )
        return self._stubs["search_team_folders"]

    @property
    def get_folder(self) -> Callable[[dataform.GetFolderRequest], dataform.Folder]:
        r"""Return a callable for the get folder method over gRPC.

        Fetches a single Folder.

        Returns:
            Callable[[~.GetFolderRequest],
                    ~.Folder]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_folder" not in self._stubs:
            self._stubs["get_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/GetFolder",
                request_serializer=dataform.GetFolderRequest.serialize,
                response_deserializer=dataform.Folder.deserialize,
            )
        return self._stubs["get_folder"]

    @property
    def create_folder(
        self,
    ) -> Callable[[dataform.CreateFolderRequest], dataform.Folder]:
        r"""Return a callable for the create folder method over gRPC.

        Creates a new Folder in a given project and location.

        Returns:
            Callable[[~.CreateFolderRequest],
                    ~.Folder]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_folder" not in self._stubs:
            self._stubs["create_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CreateFolder",
                request_serializer=dataform.CreateFolderRequest.serialize,
                response_deserializer=dataform.Folder.deserialize,
            )
        return self._stubs["create_folder"]

    @property
    def update_folder(
        self,
    ) -> Callable[[dataform.UpdateFolderRequest], dataform.Folder]:
        r"""Return a callable for the update folder method over gRPC.

        Updates a single Folder.

        Returns:
            Callable[[~.UpdateFolderRequest],
                    ~.Folder]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_folder" not in self._stubs:
            self._stubs["update_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/UpdateFolder",
                request_serializer=dataform.UpdateFolderRequest.serialize,
                response_deserializer=dataform.Folder.deserialize,
            )
        return self._stubs["update_folder"]

    @property
    def delete_folder(
        self,
    ) -> Callable[[dataform.DeleteFolderRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete folder method over gRPC.

        Deletes a single Folder.

        Returns:
            Callable[[~.DeleteFolderRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_folder" not in self._stubs:
            self._stubs["delete_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/DeleteFolder",
                request_serializer=dataform.DeleteFolderRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_folder"]

    @property
    def delete_folder_tree(
        self,
    ) -> Callable[[dataform.DeleteFolderTreeRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete folder tree method over gRPC.

        Deletes a Folder with its contents (Folders,
        Repositories, Workspaces, ReleaseConfigs, and
        WorkflowConfigs).

        Returns:
            Callable[[~.DeleteFolderTreeRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_folder_tree" not in self._stubs:
            self._stubs["delete_folder_tree"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/DeleteFolderTree",
                request_serializer=dataform.DeleteFolderTreeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_folder_tree"]

    @property
    def query_folder_contents(
        self,
    ) -> Callable[
        [dataform.QueryFolderContentsRequest], dataform.QueryFolderContentsResponse
    ]:
        r"""Return a callable for the query folder contents method over gRPC.

        Returns the contents of a given Folder.

        Returns:
            Callable[[~.QueryFolderContentsRequest],
                    ~.QueryFolderContentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_folder_contents" not in self._stubs:
            self._stubs["query_folder_contents"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/QueryFolderContents",
                request_serializer=dataform.QueryFolderContentsRequest.serialize,
                response_deserializer=dataform.QueryFolderContentsResponse.deserialize,
            )
        return self._stubs["query_folder_contents"]

    @property
    def query_user_root_contents(
        self,
    ) -> Callable[
        [dataform.QueryUserRootContentsRequest], dataform.QueryUserRootContentsResponse
    ]:
        r"""Return a callable for the query user root contents method over gRPC.

        Returns the contents of a caller's root folder in a
        given location. The root folder contains all resources
        that are created by the user and not contained in any
        other folder.

        Returns:
            Callable[[~.QueryUserRootContentsRequest],
                    ~.QueryUserRootContentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_user_root_contents" not in self._stubs:
            self._stubs["query_user_root_contents"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/QueryUserRootContents",
                request_serializer=dataform.QueryUserRootContentsRequest.serialize,
                response_deserializer=dataform.QueryUserRootContentsResponse.deserialize,
            )
        return self._stubs["query_user_root_contents"]

    @property
    def move_folder(
        self,
    ) -> Callable[[dataform.MoveFolderRequest], operations_pb2.Operation]:
        r"""Return a callable for the move folder method over gRPC.

        Moves a Folder to a new Folder, TeamFolder, or the
        root location.

        Returns:
            Callable[[~.MoveFolderRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_folder" not in self._stubs:
            self._stubs["move_folder"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/MoveFolder",
                request_serializer=dataform.MoveFolderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["move_folder"]

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [dataform.ListRepositoriesRequest], dataform.ListRepositoriesResponse
    ]:
        r"""Return a callable for the list repositories method over gRPC.

        Lists Repositories in a given project and location.

        **Note:** *This method can return repositories not shown in the*
        `Dataform
        UI <https://console.cloud.google.com/bigquery/dataform>`__.

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
                "/google.cloud.dataform.v1.Dataform/ListRepositories",
                request_serializer=dataform.ListRepositoriesRequest.serialize,
                response_deserializer=dataform.ListRepositoriesResponse.deserialize,
            )
        return self._stubs["list_repositories"]

    @property
    def get_repository(
        self,
    ) -> Callable[[dataform.GetRepositoryRequest], dataform.Repository]:
        r"""Return a callable for the get repository method over gRPC.

        Fetches a single Repository.

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
                "/google.cloud.dataform.v1.Dataform/GetRepository",
                request_serializer=dataform.GetRepositoryRequest.serialize,
                response_deserializer=dataform.Repository.deserialize,
            )
        return self._stubs["get_repository"]

    @property
    def create_repository(
        self,
    ) -> Callable[[dataform.CreateRepositoryRequest], dataform.Repository]:
        r"""Return a callable for the create repository method over gRPC.

        Creates a new Repository in a given project and
        location.

        Returns:
            Callable[[~.CreateRepositoryRequest],
                    ~.Repository]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_repository" not in self._stubs:
            self._stubs["create_repository"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CreateRepository",
                request_serializer=dataform.CreateRepositoryRequest.serialize,
                response_deserializer=dataform.Repository.deserialize,
            )
        return self._stubs["create_repository"]

    @property
    def update_repository(
        self,
    ) -> Callable[[dataform.UpdateRepositoryRequest], dataform.Repository]:
        r"""Return a callable for the update repository method over gRPC.

        Updates a single Repository.

        **Note:** *This method does not fully
        implement*\ `AIP/134 <https://google.aip.dev/134>`__\ *. The
        wildcard entry (\*) is treated as a bad request, and when the
        ``field_mask`` is omitted, the request is treated as a full
        update on all modifiable fields.*

        Returns:
            Callable[[~.UpdateRepositoryRequest],
                    ~.Repository]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_repository" not in self._stubs:
            self._stubs["update_repository"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/UpdateRepository",
                request_serializer=dataform.UpdateRepositoryRequest.serialize,
                response_deserializer=dataform.Repository.deserialize,
            )
        return self._stubs["update_repository"]

    @property
    def delete_repository(
        self,
    ) -> Callable[[dataform.DeleteRepositoryRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete repository method over gRPC.

        Deletes a single Repository.

        Returns:
            Callable[[~.DeleteRepositoryRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_repository" not in self._stubs:
            self._stubs["delete_repository"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/DeleteRepository",
                request_serializer=dataform.DeleteRepositoryRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_repository"]

    @property
    def move_repository(
        self,
    ) -> Callable[[dataform.MoveRepositoryRequest], operations_pb2.Operation]:
        r"""Return a callable for the move repository method over gRPC.

        Moves a Repository to a new location.

        Returns:
            Callable[[~.MoveRepositoryRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_repository" not in self._stubs:
            self._stubs["move_repository"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/MoveRepository",
                request_serializer=dataform.MoveRepositoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["move_repository"]

    @property
    def commit_repository_changes(
        self,
    ) -> Callable[
        [dataform.CommitRepositoryChangesRequest],
        dataform.CommitRepositoryChangesResponse,
    ]:
        r"""Return a callable for the commit repository changes method over gRPC.

        Applies a Git commit to a Repository. The Repository must not
        have a value for ``git_remote_settings.url``.

        Returns:
            Callable[[~.CommitRepositoryChangesRequest],
                    ~.CommitRepositoryChangesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "commit_repository_changes" not in self._stubs:
            self._stubs["commit_repository_changes"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CommitRepositoryChanges",
                request_serializer=dataform.CommitRepositoryChangesRequest.serialize,
                response_deserializer=dataform.CommitRepositoryChangesResponse.deserialize,
            )
        return self._stubs["commit_repository_changes"]

    @property
    def read_repository_file(
        self,
    ) -> Callable[
        [dataform.ReadRepositoryFileRequest], dataform.ReadRepositoryFileResponse
    ]:
        r"""Return a callable for the read repository file method over gRPC.

        Returns the contents of a file (inside a Repository). The
        Repository must not have a value for
        ``git_remote_settings.url``.

        Returns:
            Callable[[~.ReadRepositoryFileRequest],
                    ~.ReadRepositoryFileResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "read_repository_file" not in self._stubs:
            self._stubs["read_repository_file"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/ReadRepositoryFile",
                request_serializer=dataform.ReadRepositoryFileRequest.serialize,
                response_deserializer=dataform.ReadRepositoryFileResponse.deserialize,
            )
        return self._stubs["read_repository_file"]

    @property
    def query_repository_directory_contents(
        self,
    ) -> Callable[
        [dataform.QueryRepositoryDirectoryContentsRequest],
        dataform.QueryRepositoryDirectoryContentsResponse,
    ]:
        r"""Return a callable for the query repository directory
        contents method over gRPC.

        Returns the contents of a given Repository directory. The
        Repository must not have a value for
        ``git_remote_settings.url``.

        Returns:
            Callable[[~.QueryRepositoryDirectoryContentsRequest],
                    ~.QueryRepositoryDirectoryContentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_repository_directory_contents" not in self._stubs:
            self._stubs["query_repository_directory_contents"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.dataform.v1.Dataform/QueryRepositoryDirectoryContents",
                    request_serializer=dataform.QueryRepositoryDirectoryContentsRequest.serialize,
                    response_deserializer=dataform.QueryRepositoryDirectoryContentsResponse.deserialize,
                )
            )
        return self._stubs["query_repository_directory_contents"]

    @property
    def fetch_repository_history(
        self,
    ) -> Callable[
        [dataform.FetchRepositoryHistoryRequest],
        dataform.FetchRepositoryHistoryResponse,
    ]:
        r"""Return a callable for the fetch repository history method over gRPC.

        Fetches a Repository's history of commits. The Repository must
        not have a value for ``git_remote_settings.url``.

        Returns:
            Callable[[~.FetchRepositoryHistoryRequest],
                    ~.FetchRepositoryHistoryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_repository_history" not in self._stubs:
            self._stubs["fetch_repository_history"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/FetchRepositoryHistory",
                request_serializer=dataform.FetchRepositoryHistoryRequest.serialize,
                response_deserializer=dataform.FetchRepositoryHistoryResponse.deserialize,
            )
        return self._stubs["fetch_repository_history"]

    @property
    def compute_repository_access_token_status(
        self,
    ) -> Callable[
        [dataform.ComputeRepositoryAccessTokenStatusRequest],
        dataform.ComputeRepositoryAccessTokenStatusResponse,
    ]:
        r"""Return a callable for the compute repository access
        token status method over gRPC.

        Computes a Repository's Git access token status.

        Returns:
            Callable[[~.ComputeRepositoryAccessTokenStatusRequest],
                    ~.ComputeRepositoryAccessTokenStatusResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "compute_repository_access_token_status" not in self._stubs:
            self._stubs["compute_repository_access_token_status"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.dataform.v1.Dataform/ComputeRepositoryAccessTokenStatus",
                    request_serializer=dataform.ComputeRepositoryAccessTokenStatusRequest.serialize,
                    response_deserializer=dataform.ComputeRepositoryAccessTokenStatusResponse.deserialize,
                )
            )
        return self._stubs["compute_repository_access_token_status"]

    @property
    def fetch_remote_branches(
        self,
    ) -> Callable[
        [dataform.FetchRemoteBranchesRequest], dataform.FetchRemoteBranchesResponse
    ]:
        r"""Return a callable for the fetch remote branches method over gRPC.

        Fetches a Repository's remote branches.

        Returns:
            Callable[[~.FetchRemoteBranchesRequest],
                    ~.FetchRemoteBranchesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_remote_branches" not in self._stubs:
            self._stubs["fetch_remote_branches"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/FetchRemoteBranches",
                request_serializer=dataform.FetchRemoteBranchesRequest.serialize,
                response_deserializer=dataform.FetchRemoteBranchesResponse.deserialize,
            )
        return self._stubs["fetch_remote_branches"]

    @property
    def list_workspaces(
        self,
    ) -> Callable[[dataform.ListWorkspacesRequest], dataform.ListWorkspacesResponse]:
        r"""Return a callable for the list workspaces method over gRPC.

        Lists Workspaces in a given Repository.

        Returns:
            Callable[[~.ListWorkspacesRequest],
                    ~.ListWorkspacesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_workspaces" not in self._stubs:
            self._stubs["list_workspaces"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/ListWorkspaces",
                request_serializer=dataform.ListWorkspacesRequest.serialize,
                response_deserializer=dataform.ListWorkspacesResponse.deserialize,
            )
        return self._stubs["list_workspaces"]

    @property
    def get_workspace(
        self,
    ) -> Callable[[dataform.GetWorkspaceRequest], dataform.Workspace]:
        r"""Return a callable for the get workspace method over gRPC.

        Fetches a single Workspace.

        Returns:
            Callable[[~.GetWorkspaceRequest],
                    ~.Workspace]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_workspace" not in self._stubs:
            self._stubs["get_workspace"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/GetWorkspace",
                request_serializer=dataform.GetWorkspaceRequest.serialize,
                response_deserializer=dataform.Workspace.deserialize,
            )
        return self._stubs["get_workspace"]

    @property
    def create_workspace(
        self,
    ) -> Callable[[dataform.CreateWorkspaceRequest], dataform.Workspace]:
        r"""Return a callable for the create workspace method over gRPC.

        Creates a new Workspace in a given Repository.

        Returns:
            Callable[[~.CreateWorkspaceRequest],
                    ~.Workspace]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_workspace" not in self._stubs:
            self._stubs["create_workspace"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CreateWorkspace",
                request_serializer=dataform.CreateWorkspaceRequest.serialize,
                response_deserializer=dataform.Workspace.deserialize,
            )
        return self._stubs["create_workspace"]

    @property
    def delete_workspace(
        self,
    ) -> Callable[[dataform.DeleteWorkspaceRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete workspace method over gRPC.

        Deletes a single Workspace.

        Returns:
            Callable[[~.DeleteWorkspaceRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_workspace" not in self._stubs:
            self._stubs["delete_workspace"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/DeleteWorkspace",
                request_serializer=dataform.DeleteWorkspaceRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_workspace"]

    @property
    def install_npm_packages(
        self,
    ) -> Callable[
        [dataform.InstallNpmPackagesRequest], dataform.InstallNpmPackagesResponse
    ]:
        r"""Return a callable for the install npm packages method over gRPC.

        Installs dependency NPM packages (inside a
        Workspace).

        Returns:
            Callable[[~.InstallNpmPackagesRequest],
                    ~.InstallNpmPackagesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "install_npm_packages" not in self._stubs:
            self._stubs["install_npm_packages"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/InstallNpmPackages",
                request_serializer=dataform.InstallNpmPackagesRequest.serialize,
                response_deserializer=dataform.InstallNpmPackagesResponse.deserialize,
            )
        return self._stubs["install_npm_packages"]

    @property
    def pull_git_commits(
        self,
    ) -> Callable[[dataform.PullGitCommitsRequest], dataform.PullGitCommitsResponse]:
        r"""Return a callable for the pull git commits method over gRPC.

        Pulls Git commits from the Repository's remote into a
        Workspace.

        Returns:
            Callable[[~.PullGitCommitsRequest],
                    ~.PullGitCommitsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "pull_git_commits" not in self._stubs:
            self._stubs["pull_git_commits"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/PullGitCommits",
                request_serializer=dataform.PullGitCommitsRequest.serialize,
                response_deserializer=dataform.PullGitCommitsResponse.deserialize,
            )
        return self._stubs["pull_git_commits"]

    @property
    def push_git_commits(
        self,
    ) -> Callable[[dataform.PushGitCommitsRequest], dataform.PushGitCommitsResponse]:
        r"""Return a callable for the push git commits method over gRPC.

        Pushes Git commits from a Workspace to the
        Repository's remote.

        Returns:
            Callable[[~.PushGitCommitsRequest],
                    ~.PushGitCommitsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "push_git_commits" not in self._stubs:
            self._stubs["push_git_commits"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/PushGitCommits",
                request_serializer=dataform.PushGitCommitsRequest.serialize,
                response_deserializer=dataform.PushGitCommitsResponse.deserialize,
            )
        return self._stubs["push_git_commits"]

    @property
    def fetch_file_git_statuses(
        self,
    ) -> Callable[
        [dataform.FetchFileGitStatusesRequest], dataform.FetchFileGitStatusesResponse
    ]:
        r"""Return a callable for the fetch file git statuses method over gRPC.

        Fetches Git statuses for the files in a Workspace.

        Returns:
            Callable[[~.FetchFileGitStatusesRequest],
                    ~.FetchFileGitStatusesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_file_git_statuses" not in self._stubs:
            self._stubs["fetch_file_git_statuses"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/FetchFileGitStatuses",
                request_serializer=dataform.FetchFileGitStatusesRequest.serialize,
                response_deserializer=dataform.FetchFileGitStatusesResponse.deserialize,
            )
        return self._stubs["fetch_file_git_statuses"]

    @property
    def fetch_git_ahead_behind(
        self,
    ) -> Callable[
        [dataform.FetchGitAheadBehindRequest], dataform.FetchGitAheadBehindResponse
    ]:
        r"""Return a callable for the fetch git ahead behind method over gRPC.

        Fetches Git ahead/behind against a remote branch.

        Returns:
            Callable[[~.FetchGitAheadBehindRequest],
                    ~.FetchGitAheadBehindResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_git_ahead_behind" not in self._stubs:
            self._stubs["fetch_git_ahead_behind"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/FetchGitAheadBehind",
                request_serializer=dataform.FetchGitAheadBehindRequest.serialize,
                response_deserializer=dataform.FetchGitAheadBehindResponse.deserialize,
            )
        return self._stubs["fetch_git_ahead_behind"]

    @property
    def commit_workspace_changes(
        self,
    ) -> Callable[
        [dataform.CommitWorkspaceChangesRequest],
        dataform.CommitWorkspaceChangesResponse,
    ]:
        r"""Return a callable for the commit workspace changes method over gRPC.

        Applies a Git commit for uncommitted files in a
        Workspace.

        Returns:
            Callable[[~.CommitWorkspaceChangesRequest],
                    ~.CommitWorkspaceChangesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "commit_workspace_changes" not in self._stubs:
            self._stubs["commit_workspace_changes"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CommitWorkspaceChanges",
                request_serializer=dataform.CommitWorkspaceChangesRequest.serialize,
                response_deserializer=dataform.CommitWorkspaceChangesResponse.deserialize,
            )
        return self._stubs["commit_workspace_changes"]

    @property
    def reset_workspace_changes(
        self,
    ) -> Callable[
        [dataform.ResetWorkspaceChangesRequest], dataform.ResetWorkspaceChangesResponse
    ]:
        r"""Return a callable for the reset workspace changes method over gRPC.

        Performs a Git reset for uncommitted files in a
        Workspace.

        Returns:
            Callable[[~.ResetWorkspaceChangesRequest],
                    ~.ResetWorkspaceChangesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_workspace_changes" not in self._stubs:
            self._stubs["reset_workspace_changes"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/ResetWorkspaceChanges",
                request_serializer=dataform.ResetWorkspaceChangesRequest.serialize,
                response_deserializer=dataform.ResetWorkspaceChangesResponse.deserialize,
            )
        return self._stubs["reset_workspace_changes"]

    @property
    def fetch_file_diff(
        self,
    ) -> Callable[[dataform.FetchFileDiffRequest], dataform.FetchFileDiffResponse]:
        r"""Return a callable for the fetch file diff method over gRPC.

        Fetches Git diff for an uncommitted file in a
        Workspace.

        Returns:
            Callable[[~.FetchFileDiffRequest],
                    ~.FetchFileDiffResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_file_diff" not in self._stubs:
            self._stubs["fetch_file_diff"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/FetchFileDiff",
                request_serializer=dataform.FetchFileDiffRequest.serialize,
                response_deserializer=dataform.FetchFileDiffResponse.deserialize,
            )
        return self._stubs["fetch_file_diff"]

    @property
    def query_directory_contents(
        self,
    ) -> Callable[
        [dataform.QueryDirectoryContentsRequest],
        dataform.QueryDirectoryContentsResponse,
    ]:
        r"""Return a callable for the query directory contents method over gRPC.

        Returns the contents of a given Workspace directory.

        Returns:
            Callable[[~.QueryDirectoryContentsRequest],
                    ~.QueryDirectoryContentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_directory_contents" not in self._stubs:
            self._stubs["query_directory_contents"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/QueryDirectoryContents",
                request_serializer=dataform.QueryDirectoryContentsRequest.serialize,
                response_deserializer=dataform.QueryDirectoryContentsResponse.deserialize,
            )
        return self._stubs["query_directory_contents"]

    @property
    def search_files(
        self,
    ) -> Callable[[dataform.SearchFilesRequest], dataform.SearchFilesResponse]:
        r"""Return a callable for the search files method over gRPC.

        Finds the contents of a given Workspace directory by
        filter.

        Returns:
            Callable[[~.SearchFilesRequest],
                    ~.SearchFilesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_files" not in self._stubs:
            self._stubs["search_files"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/SearchFiles",
                request_serializer=dataform.SearchFilesRequest.serialize,
                response_deserializer=dataform.SearchFilesResponse.deserialize,
            )
        return self._stubs["search_files"]

    @property
    def make_directory(
        self,
    ) -> Callable[[dataform.MakeDirectoryRequest], dataform.MakeDirectoryResponse]:
        r"""Return a callable for the make directory method over gRPC.

        Creates a directory inside a Workspace.

        Returns:
            Callable[[~.MakeDirectoryRequest],
                    ~.MakeDirectoryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "make_directory" not in self._stubs:
            self._stubs["make_directory"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/MakeDirectory",
                request_serializer=dataform.MakeDirectoryRequest.serialize,
                response_deserializer=dataform.MakeDirectoryResponse.deserialize,
            )
        return self._stubs["make_directory"]

    @property
    def remove_directory(
        self,
    ) -> Callable[[dataform.RemoveDirectoryRequest], dataform.RemoveDirectoryResponse]:
        r"""Return a callable for the remove directory method over gRPC.

        Deletes a directory (inside a Workspace) and all of
        its contents.

        Returns:
            Callable[[~.RemoveDirectoryRequest],
                    ~.RemoveDirectoryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_directory" not in self._stubs:
            self._stubs["remove_directory"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/RemoveDirectory",
                request_serializer=dataform.RemoveDirectoryRequest.serialize,
                response_deserializer=dataform.RemoveDirectoryResponse.deserialize,
            )
        return self._stubs["remove_directory"]

    @property
    def move_directory(
        self,
    ) -> Callable[[dataform.MoveDirectoryRequest], dataform.MoveDirectoryResponse]:
        r"""Return a callable for the move directory method over gRPC.

        Moves a directory (inside a Workspace), and all of
        its contents, to a new location.

        Returns:
            Callable[[~.MoveDirectoryRequest],
                    ~.MoveDirectoryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_directory" not in self._stubs:
            self._stubs["move_directory"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/MoveDirectory",
                request_serializer=dataform.MoveDirectoryRequest.serialize,
                response_deserializer=dataform.MoveDirectoryResponse.deserialize,
            )
        return self._stubs["move_directory"]

    @property
    def read_file(
        self,
    ) -> Callable[[dataform.ReadFileRequest], dataform.ReadFileResponse]:
        r"""Return a callable for the read file method over gRPC.

        Returns the contents of a file (inside a Workspace).

        Returns:
            Callable[[~.ReadFileRequest],
                    ~.ReadFileResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "read_file" not in self._stubs:
            self._stubs["read_file"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/ReadFile",
                request_serializer=dataform.ReadFileRequest.serialize,
                response_deserializer=dataform.ReadFileResponse.deserialize,
            )
        return self._stubs["read_file"]

    @property
    def remove_file(
        self,
    ) -> Callable[[dataform.RemoveFileRequest], dataform.RemoveFileResponse]:
        r"""Return a callable for the remove file method over gRPC.

        Deletes a file (inside a Workspace).

        Returns:
            Callable[[~.RemoveFileRequest],
                    ~.RemoveFileResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_file" not in self._stubs:
            self._stubs["remove_file"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/RemoveFile",
                request_serializer=dataform.RemoveFileRequest.serialize,
                response_deserializer=dataform.RemoveFileResponse.deserialize,
            )
        return self._stubs["remove_file"]

    @property
    def move_file(
        self,
    ) -> Callable[[dataform.MoveFileRequest], dataform.MoveFileResponse]:
        r"""Return a callable for the move file method over gRPC.

        Moves a file (inside a Workspace) to a new location.

        Returns:
            Callable[[~.MoveFileRequest],
                    ~.MoveFileResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_file" not in self._stubs:
            self._stubs["move_file"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/MoveFile",
                request_serializer=dataform.MoveFileRequest.serialize,
                response_deserializer=dataform.MoveFileResponse.deserialize,
            )
        return self._stubs["move_file"]

    @property
    def write_file(
        self,
    ) -> Callable[[dataform.WriteFileRequest], dataform.WriteFileResponse]:
        r"""Return a callable for the write file method over gRPC.

        Writes to a file (inside a Workspace).

        Returns:
            Callable[[~.WriteFileRequest],
                    ~.WriteFileResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "write_file" not in self._stubs:
            self._stubs["write_file"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/WriteFile",
                request_serializer=dataform.WriteFileRequest.serialize,
                response_deserializer=dataform.WriteFileResponse.deserialize,
            )
        return self._stubs["write_file"]

    @property
    def list_release_configs(
        self,
    ) -> Callable[
        [dataform.ListReleaseConfigsRequest], dataform.ListReleaseConfigsResponse
    ]:
        r"""Return a callable for the list release configs method over gRPC.

        Lists ReleaseConfigs in a given Repository.

        Returns:
            Callable[[~.ListReleaseConfigsRequest],
                    ~.ListReleaseConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_release_configs" not in self._stubs:
            self._stubs["list_release_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/ListReleaseConfigs",
                request_serializer=dataform.ListReleaseConfigsRequest.serialize,
                response_deserializer=dataform.ListReleaseConfigsResponse.deserialize,
            )
        return self._stubs["list_release_configs"]

    @property
    def get_release_config(
        self,
    ) -> Callable[[dataform.GetReleaseConfigRequest], dataform.ReleaseConfig]:
        r"""Return a callable for the get release config method over gRPC.

        Fetches a single ReleaseConfig.

        Returns:
            Callable[[~.GetReleaseConfigRequest],
                    ~.ReleaseConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_release_config" not in self._stubs:
            self._stubs["get_release_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/GetReleaseConfig",
                request_serializer=dataform.GetReleaseConfigRequest.serialize,
                response_deserializer=dataform.ReleaseConfig.deserialize,
            )
        return self._stubs["get_release_config"]

    @property
    def create_release_config(
        self,
    ) -> Callable[[dataform.CreateReleaseConfigRequest], dataform.ReleaseConfig]:
        r"""Return a callable for the create release config method over gRPC.

        Creates a new ReleaseConfig in a given Repository.

        Returns:
            Callable[[~.CreateReleaseConfigRequest],
                    ~.ReleaseConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_release_config" not in self._stubs:
            self._stubs["create_release_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CreateReleaseConfig",
                request_serializer=dataform.CreateReleaseConfigRequest.serialize,
                response_deserializer=dataform.ReleaseConfig.deserialize,
            )
        return self._stubs["create_release_config"]

    @property
    def update_release_config(
        self,
    ) -> Callable[[dataform.UpdateReleaseConfigRequest], dataform.ReleaseConfig]:
        r"""Return a callable for the update release config method over gRPC.

        Updates a single ReleaseConfig.

        **Note:** *This method does not fully
        implement*\ `AIP/134 <https://google.aip.dev/134>`__\ *. The
        wildcard entry (\*) is treated as a bad request, and when the
        ``field_mask`` is omitted, the request is treated as a full
        update on all modifiable fields.*

        Returns:
            Callable[[~.UpdateReleaseConfigRequest],
                    ~.ReleaseConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_release_config" not in self._stubs:
            self._stubs["update_release_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/UpdateReleaseConfig",
                request_serializer=dataform.UpdateReleaseConfigRequest.serialize,
                response_deserializer=dataform.ReleaseConfig.deserialize,
            )
        return self._stubs["update_release_config"]

    @property
    def delete_release_config(
        self,
    ) -> Callable[[dataform.DeleteReleaseConfigRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete release config method over gRPC.

        Deletes a single ReleaseConfig.

        Returns:
            Callable[[~.DeleteReleaseConfigRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_release_config" not in self._stubs:
            self._stubs["delete_release_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/DeleteReleaseConfig",
                request_serializer=dataform.DeleteReleaseConfigRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_release_config"]

    @property
    def list_compilation_results(
        self,
    ) -> Callable[
        [dataform.ListCompilationResultsRequest],
        dataform.ListCompilationResultsResponse,
    ]:
        r"""Return a callable for the list compilation results method over gRPC.

        Lists CompilationResults in a given Repository.

        Returns:
            Callable[[~.ListCompilationResultsRequest],
                    ~.ListCompilationResultsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_compilation_results" not in self._stubs:
            self._stubs["list_compilation_results"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/ListCompilationResults",
                request_serializer=dataform.ListCompilationResultsRequest.serialize,
                response_deserializer=dataform.ListCompilationResultsResponse.deserialize,
            )
        return self._stubs["list_compilation_results"]

    @property
    def get_compilation_result(
        self,
    ) -> Callable[[dataform.GetCompilationResultRequest], dataform.CompilationResult]:
        r"""Return a callable for the get compilation result method over gRPC.

        Fetches a single CompilationResult.

        Returns:
            Callable[[~.GetCompilationResultRequest],
                    ~.CompilationResult]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_compilation_result" not in self._stubs:
            self._stubs["get_compilation_result"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/GetCompilationResult",
                request_serializer=dataform.GetCompilationResultRequest.serialize,
                response_deserializer=dataform.CompilationResult.deserialize,
            )
        return self._stubs["get_compilation_result"]

    @property
    def create_compilation_result(
        self,
    ) -> Callable[
        [dataform.CreateCompilationResultRequest], dataform.CompilationResult
    ]:
        r"""Return a callable for the create compilation result method over gRPC.

        Creates a new CompilationResult in a given project
        and location.

        Returns:
            Callable[[~.CreateCompilationResultRequest],
                    ~.CompilationResult]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_compilation_result" not in self._stubs:
            self._stubs["create_compilation_result"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CreateCompilationResult",
                request_serializer=dataform.CreateCompilationResultRequest.serialize,
                response_deserializer=dataform.CompilationResult.deserialize,
            )
        return self._stubs["create_compilation_result"]

    @property
    def query_compilation_result_actions(
        self,
    ) -> Callable[
        [dataform.QueryCompilationResultActionsRequest],
        dataform.QueryCompilationResultActionsResponse,
    ]:
        r"""Return a callable for the query compilation result
        actions method over gRPC.

        Returns CompilationResultActions in a given
        CompilationResult.

        Returns:
            Callable[[~.QueryCompilationResultActionsRequest],
                    ~.QueryCompilationResultActionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_compilation_result_actions" not in self._stubs:
            self._stubs["query_compilation_result_actions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.dataform.v1.Dataform/QueryCompilationResultActions",
                    request_serializer=dataform.QueryCompilationResultActionsRequest.serialize,
                    response_deserializer=dataform.QueryCompilationResultActionsResponse.deserialize,
                )
            )
        return self._stubs["query_compilation_result_actions"]

    @property
    def list_workflow_configs(
        self,
    ) -> Callable[
        [dataform.ListWorkflowConfigsRequest], dataform.ListWorkflowConfigsResponse
    ]:
        r"""Return a callable for the list workflow configs method over gRPC.

        Lists WorkflowConfigs in a given Repository.

        Returns:
            Callable[[~.ListWorkflowConfigsRequest],
                    ~.ListWorkflowConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_workflow_configs" not in self._stubs:
            self._stubs["list_workflow_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/ListWorkflowConfigs",
                request_serializer=dataform.ListWorkflowConfigsRequest.serialize,
                response_deserializer=dataform.ListWorkflowConfigsResponse.deserialize,
            )
        return self._stubs["list_workflow_configs"]

    @property
    def get_workflow_config(
        self,
    ) -> Callable[[dataform.GetWorkflowConfigRequest], dataform.WorkflowConfig]:
        r"""Return a callable for the get workflow config method over gRPC.

        Fetches a single WorkflowConfig.

        Returns:
            Callable[[~.GetWorkflowConfigRequest],
                    ~.WorkflowConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_workflow_config" not in self._stubs:
            self._stubs["get_workflow_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/GetWorkflowConfig",
                request_serializer=dataform.GetWorkflowConfigRequest.serialize,
                response_deserializer=dataform.WorkflowConfig.deserialize,
            )
        return self._stubs["get_workflow_config"]

    @property
    def create_workflow_config(
        self,
    ) -> Callable[[dataform.CreateWorkflowConfigRequest], dataform.WorkflowConfig]:
        r"""Return a callable for the create workflow config method over gRPC.

        Creates a new WorkflowConfig in a given Repository.

        Returns:
            Callable[[~.CreateWorkflowConfigRequest],
                    ~.WorkflowConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_workflow_config" not in self._stubs:
            self._stubs["create_workflow_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/CreateWorkflowConfig",
                request_serializer=dataform.CreateWorkflowConfigRequest.serialize,
                response_deserializer=dataform.WorkflowConfig.deserialize,
            )
        return self._stubs["create_workflow_config"]

    @property
    def update_workflow_config(
        self,
    ) -> Callable[[dataform.UpdateWorkflowConfigRequest], dataform.WorkflowConfig]:
        r"""Return a callable for the update workflow config method over gRPC.

        Updates a single WorkflowConfig.

        **Note:** *This method does not fully
        implement*\ `AIP/134 <https://google.aip.dev/134>`__\ *. The
        wildcard entry (\*) is treated as a bad request, and when the
        ``field_mask`` is omitted, the request is treated as a full
        update on all modifiable fields.*

        Returns:
            Callable[[~.UpdateWorkflowConfigRequest],
                    ~.WorkflowConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_workflow_config" not in self._stubs:
            self._stubs["update_workflow_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/UpdateWorkflowConfig",
                request_serializer=dataform.UpdateWorkflowConfigRequest.serialize,
                response_deserializer=dataform.WorkflowConfig.deserialize,
            )
        return self._stubs["update_workflow_config"]

    @property
    def delete_workflow_config(
        self,
    ) -> Callable[[dataform.DeleteWorkflowConfigRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete workflow config method over gRPC.

        Deletes a single WorkflowConfig.

        Returns:
            Callable[[~.DeleteWorkflowConfigRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_workflow_config" not in self._stubs:
            self._stubs["delete_workflow_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/DeleteWorkflowConfig",
                request_serializer=dataform.DeleteWorkflowConfigRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_workflow_config"]

    @property
    def list_workflow_invocations(
        self,
    ) -> Callable[
        [dataform.ListWorkflowInvocationsRequest],
        dataform.ListWorkflowInvocationsResponse,
    ]:
        r"""Return a callable for the list workflow invocations method over gRPC.

        Lists WorkflowInvocations in a given Repository.

        Returns:
            Callable[[~.ListWorkflowInvocationsRequest],
                    ~.ListWorkflowInvocationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_workflow_invocations" not in self._stubs:
            self._stubs["list_workflow_invocations"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/ListWorkflowInvocations",
                request_serializer=dataform.ListWorkflowInvocationsRequest.serialize,
                response_deserializer=dataform.ListWorkflowInvocationsResponse.deserialize,
            )
        return self._stubs["list_workflow_invocations"]

    @property
    def get_workflow_invocation(
        self,
    ) -> Callable[[dataform.GetWorkflowInvocationRequest], dataform.WorkflowInvocation]:
        r"""Return a callable for the get workflow invocation method over gRPC.

        Fetches a single WorkflowInvocation.

        Returns:
            Callable[[~.GetWorkflowInvocationRequest],
                    ~.WorkflowInvocation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_workflow_invocation" not in self._stubs:
            self._stubs["get_workflow_invocation"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/GetWorkflowInvocation",
                request_serializer=dataform.GetWorkflowInvocationRequest.serialize,
                response_deserializer=dataform.WorkflowInvocation.deserialize,
            )
        return self._stubs["get_workflow_invocation"]

    @property
    def create_workflow_invocation(
        self,
    ) -> Callable[
        [dataform.CreateWorkflowInvocationRequest], dataform.WorkflowInvocation
    ]:
        r"""Return a callable for the create workflow invocation method over gRPC.

        Creates a new WorkflowInvocation in a given
        Repository.

        Returns:
            Callable[[~.CreateWorkflowInvocationRequest],
                    ~.WorkflowInvocation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_workflow_invocation" not in self._stubs:
            self._stubs["create_workflow_invocation"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.dataform.v1.Dataform/CreateWorkflowInvocation",
                    request_serializer=dataform.CreateWorkflowInvocationRequest.serialize,
                    response_deserializer=dataform.WorkflowInvocation.deserialize,
                )
            )
        return self._stubs["create_workflow_invocation"]

    @property
    def delete_workflow_invocation(
        self,
    ) -> Callable[[dataform.DeleteWorkflowInvocationRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete workflow invocation method over gRPC.

        Deletes a single WorkflowInvocation.

        Returns:
            Callable[[~.DeleteWorkflowInvocationRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_workflow_invocation" not in self._stubs:
            self._stubs["delete_workflow_invocation"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.dataform.v1.Dataform/DeleteWorkflowInvocation",
                    request_serializer=dataform.DeleteWorkflowInvocationRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_workflow_invocation"]

    @property
    def cancel_workflow_invocation(
        self,
    ) -> Callable[
        [dataform.CancelWorkflowInvocationRequest],
        dataform.CancelWorkflowInvocationResponse,
    ]:
        r"""Return a callable for the cancel workflow invocation method over gRPC.

        Requests cancellation of a running
        WorkflowInvocation.

        Returns:
            Callable[[~.CancelWorkflowInvocationRequest],
                    ~.CancelWorkflowInvocationResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_workflow_invocation" not in self._stubs:
            self._stubs["cancel_workflow_invocation"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.dataform.v1.Dataform/CancelWorkflowInvocation",
                    request_serializer=dataform.CancelWorkflowInvocationRequest.serialize,
                    response_deserializer=dataform.CancelWorkflowInvocationResponse.deserialize,
                )
            )
        return self._stubs["cancel_workflow_invocation"]

    @property
    def query_workflow_invocation_actions(
        self,
    ) -> Callable[
        [dataform.QueryWorkflowInvocationActionsRequest],
        dataform.QueryWorkflowInvocationActionsResponse,
    ]:
        r"""Return a callable for the query workflow invocation
        actions method over gRPC.

        Returns WorkflowInvocationActions in a given
        WorkflowInvocation.

        Returns:
            Callable[[~.QueryWorkflowInvocationActionsRequest],
                    ~.QueryWorkflowInvocationActionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_workflow_invocation_actions" not in self._stubs:
            self._stubs["query_workflow_invocation_actions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.dataform.v1.Dataform/QueryWorkflowInvocationActions",
                    request_serializer=dataform.QueryWorkflowInvocationActionsRequest.serialize,
                    response_deserializer=dataform.QueryWorkflowInvocationActionsResponse.deserialize,
                )
            )
        return self._stubs["query_workflow_invocation_actions"]

    @property
    def get_config(self) -> Callable[[dataform.GetConfigRequest], dataform.Config]:
        r"""Return a callable for the get config method over gRPC.

        Get default config for a given project and location.

        Returns:
            Callable[[~.GetConfigRequest],
                    ~.Config]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_config" not in self._stubs:
            self._stubs["get_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/GetConfig",
                request_serializer=dataform.GetConfigRequest.serialize,
                response_deserializer=dataform.Config.deserialize,
            )
        return self._stubs["get_config"]

    @property
    def update_config(
        self,
    ) -> Callable[[dataform.UpdateConfigRequest], dataform.Config]:
        r"""Return a callable for the update config method over gRPC.

        Update default config for a given project and location.

        **Note:** *This method does not fully
        implement*\ `AIP/134 <https://google.aip.dev/134>`__\ *. The
        wildcard entry (\*) is treated as a bad request, and when the
        ``field_mask`` is omitted, the request is treated as a full
        update on all modifiable fields.*

        Returns:
            Callable[[~.UpdateConfigRequest],
                    ~.Config]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_config" not in self._stubs:
            self._stubs["update_config"] = self._logged_channel.unary_unary(
                "/google.cloud.dataform.v1.Dataform/UpdateConfig",
                request_serializer=dataform.UpdateConfigRequest.serialize,
                response_deserializer=dataform.Config.deserialize,
            )
        return self._stubs["update_config"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the access control policy for a resource.
        Returns an empty policy if the resource exists and does
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
                "/google.cloud.dataform.v1.Dataform/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the access control policy on the specified resource.
        Replaces any existing policy.

        Can return ``NOT_FOUND``, ``INVALID_ARGUMENT``, and
        ``PERMISSION_DENIED`` errors.

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
                "/google.cloud.dataform.v1.Dataform/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.

        Returns permissions that a caller has on the specified resource.
        If the resource does not exist, this will return an empty set of
        permissions, not a ``NOT_FOUND`` error.

        Note: This operation is designed to be used for building
        permission-aware UIs and command-line tools, not for
        authorization checking. This operation may "fail open" without
        warning.

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
                "/google.cloud.dataform.v1.Dataform/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

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
    def kind(self) -> str:
        return "grpc"


__all__ = ("DataformGrpcTransport",)
