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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.config_v1.types import config

from .base import DEFAULT_CLIENT_INFO, ConfigTransport

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
                    "serviceName": "google.cloud.config.v1.Config",
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
                    "serviceName": "google.cloud.config.v1.Config",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ConfigGrpcTransport(ConfigTransport):
    """gRPC backend transport for Config.

    Infrastructure Manager is a managed service that automates
    the deployment and management of Google Cloud infrastructure
    resources.

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
        host: str = "config.googleapis.com",
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
                 The hostname to connect to (default: 'config.googleapis.com').
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
        host: str = "config.googleapis.com",
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
    def list_deployments(
        self,
    ) -> Callable[[config.ListDeploymentsRequest], config.ListDeploymentsResponse]:
        r"""Return a callable for the list deployments method over gRPC.

        Lists [Deployment][google.cloud.config.v1.Deployment]s in a
        given project and location.

        Returns:
            Callable[[~.ListDeploymentsRequest],
                    ~.ListDeploymentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deployments" not in self._stubs:
            self._stubs["list_deployments"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ListDeployments",
                request_serializer=config.ListDeploymentsRequest.serialize,
                response_deserializer=config.ListDeploymentsResponse.deserialize,
            )
        return self._stubs["list_deployments"]

    @property
    def get_deployment(
        self,
    ) -> Callable[[config.GetDeploymentRequest], config.Deployment]:
        r"""Return a callable for the get deployment method over gRPC.

        Gets details about a
        [Deployment][google.cloud.config.v1.Deployment].

        Returns:
            Callable[[~.GetDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deployment" not in self._stubs:
            self._stubs["get_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetDeployment",
                request_serializer=config.GetDeploymentRequest.serialize,
                response_deserializer=config.Deployment.deserialize,
            )
        return self._stubs["get_deployment"]

    @property
    def create_deployment(
        self,
    ) -> Callable[[config.CreateDeploymentRequest], operations_pb2.Operation]:
        r"""Return a callable for the create deployment method over gRPC.

        Creates a [Deployment][google.cloud.config.v1.Deployment].

        Returns:
            Callable[[~.CreateDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_deployment" not in self._stubs:
            self._stubs["create_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/CreateDeployment",
                request_serializer=config.CreateDeploymentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_deployment"]

    @property
    def update_deployment(
        self,
    ) -> Callable[[config.UpdateDeploymentRequest], operations_pb2.Operation]:
        r"""Return a callable for the update deployment method over gRPC.

        Updates a [Deployment][google.cloud.config.v1.Deployment].

        Returns:
            Callable[[~.UpdateDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_deployment" not in self._stubs:
            self._stubs["update_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/UpdateDeployment",
                request_serializer=config.UpdateDeploymentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_deployment"]

    @property
    def delete_deployment(
        self,
    ) -> Callable[[config.DeleteDeploymentRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete deployment method over gRPC.

        Deletes a [Deployment][google.cloud.config.v1.Deployment].

        Returns:
            Callable[[~.DeleteDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_deployment" not in self._stubs:
            self._stubs["delete_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/DeleteDeployment",
                request_serializer=config.DeleteDeploymentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_deployment"]

    @property
    def list_revisions(
        self,
    ) -> Callable[[config.ListRevisionsRequest], config.ListRevisionsResponse]:
        r"""Return a callable for the list revisions method over gRPC.

        Lists [Revision][google.cloud.config.v1.Revision]s of a
        deployment.

        Returns:
            Callable[[~.ListRevisionsRequest],
                    ~.ListRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_revisions" not in self._stubs:
            self._stubs["list_revisions"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ListRevisions",
                request_serializer=config.ListRevisionsRequest.serialize,
                response_deserializer=config.ListRevisionsResponse.deserialize,
            )
        return self._stubs["list_revisions"]

    @property
    def get_revision(self) -> Callable[[config.GetRevisionRequest], config.Revision]:
        r"""Return a callable for the get revision method over gRPC.

        Gets details about a
        [Revision][google.cloud.config.v1.Revision].

        Returns:
            Callable[[~.GetRevisionRequest],
                    ~.Revision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_revision" not in self._stubs:
            self._stubs["get_revision"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetRevision",
                request_serializer=config.GetRevisionRequest.serialize,
                response_deserializer=config.Revision.deserialize,
            )
        return self._stubs["get_revision"]

    @property
    def get_resource(self) -> Callable[[config.GetResourceRequest], config.Resource]:
        r"""Return a callable for the get resource method over gRPC.

        Gets details about a [Resource][google.cloud.config.v1.Resource]
        deployed by Infra Manager.

        Returns:
            Callable[[~.GetResourceRequest],
                    ~.Resource]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_resource" not in self._stubs:
            self._stubs["get_resource"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetResource",
                request_serializer=config.GetResourceRequest.serialize,
                response_deserializer=config.Resource.deserialize,
            )
        return self._stubs["get_resource"]

    @property
    def list_resources(
        self,
    ) -> Callable[[config.ListResourcesRequest], config.ListResourcesResponse]:
        r"""Return a callable for the list resources method over gRPC.

        Lists [Resources][google.cloud.config.v1.Resource] in a given
        revision.

        Returns:
            Callable[[~.ListResourcesRequest],
                    ~.ListResourcesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_resources" not in self._stubs:
            self._stubs["list_resources"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ListResources",
                request_serializer=config.ListResourcesRequest.serialize,
                response_deserializer=config.ListResourcesResponse.deserialize,
            )
        return self._stubs["list_resources"]

    @property
    def export_deployment_statefile(
        self,
    ) -> Callable[[config.ExportDeploymentStatefileRequest], config.Statefile]:
        r"""Return a callable for the export deployment statefile method over gRPC.

        Exports Terraform state file from a given deployment.

        Returns:
            Callable[[~.ExportDeploymentStatefileRequest],
                    ~.Statefile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_deployment_statefile" not in self._stubs:
            self._stubs["export_deployment_statefile"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.config.v1.Config/ExportDeploymentStatefile",
                    request_serializer=config.ExportDeploymentStatefileRequest.serialize,
                    response_deserializer=config.Statefile.deserialize,
                )
            )
        return self._stubs["export_deployment_statefile"]

    @property
    def export_revision_statefile(
        self,
    ) -> Callable[[config.ExportRevisionStatefileRequest], config.Statefile]:
        r"""Return a callable for the export revision statefile method over gRPC.

        Exports Terraform state file from a given revision.

        Returns:
            Callable[[~.ExportRevisionStatefileRequest],
                    ~.Statefile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_revision_statefile" not in self._stubs:
            self._stubs["export_revision_statefile"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ExportRevisionStatefile",
                request_serializer=config.ExportRevisionStatefileRequest.serialize,
                response_deserializer=config.Statefile.deserialize,
            )
        return self._stubs["export_revision_statefile"]

    @property
    def import_statefile(
        self,
    ) -> Callable[[config.ImportStatefileRequest], config.Statefile]:
        r"""Return a callable for the import statefile method over gRPC.

        Imports Terraform state file in a given deployment.
        The state file does not take effect until the Deployment
        has been unlocked.

        Returns:
            Callable[[~.ImportStatefileRequest],
                    ~.Statefile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_statefile" not in self._stubs:
            self._stubs["import_statefile"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ImportStatefile",
                request_serializer=config.ImportStatefileRequest.serialize,
                response_deserializer=config.Statefile.deserialize,
            )
        return self._stubs["import_statefile"]

    @property
    def delete_statefile(
        self,
    ) -> Callable[[config.DeleteStatefileRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete statefile method over gRPC.

        Deletes Terraform state file in a given deployment.

        Returns:
            Callable[[~.DeleteStatefileRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_statefile" not in self._stubs:
            self._stubs["delete_statefile"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/DeleteStatefile",
                request_serializer=config.DeleteStatefileRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_statefile"]

    @property
    def lock_deployment(
        self,
    ) -> Callable[[config.LockDeploymentRequest], operations_pb2.Operation]:
        r"""Return a callable for the lock deployment method over gRPC.

        Locks a deployment.

        Returns:
            Callable[[~.LockDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lock_deployment" not in self._stubs:
            self._stubs["lock_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/LockDeployment",
                request_serializer=config.LockDeploymentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["lock_deployment"]

    @property
    def unlock_deployment(
        self,
    ) -> Callable[[config.UnlockDeploymentRequest], operations_pb2.Operation]:
        r"""Return a callable for the unlock deployment method over gRPC.

        Unlocks a locked deployment.

        Returns:
            Callable[[~.UnlockDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "unlock_deployment" not in self._stubs:
            self._stubs["unlock_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/UnlockDeployment",
                request_serializer=config.UnlockDeploymentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["unlock_deployment"]

    @property
    def export_lock_info(
        self,
    ) -> Callable[[config.ExportLockInfoRequest], config.LockInfo]:
        r"""Return a callable for the export lock info method over gRPC.

        Exports the lock info on a locked deployment.

        Returns:
            Callable[[~.ExportLockInfoRequest],
                    ~.LockInfo]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_lock_info" not in self._stubs:
            self._stubs["export_lock_info"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ExportLockInfo",
                request_serializer=config.ExportLockInfoRequest.serialize,
                response_deserializer=config.LockInfo.deserialize,
            )
        return self._stubs["export_lock_info"]

    @property
    def create_preview(
        self,
    ) -> Callable[[config.CreatePreviewRequest], operations_pb2.Operation]:
        r"""Return a callable for the create preview method over gRPC.

        Creates a [Preview][google.cloud.config.v1.Preview].

        Returns:
            Callable[[~.CreatePreviewRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_preview" not in self._stubs:
            self._stubs["create_preview"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/CreatePreview",
                request_serializer=config.CreatePreviewRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_preview"]

    @property
    def get_preview(self) -> Callable[[config.GetPreviewRequest], config.Preview]:
        r"""Return a callable for the get preview method over gRPC.

        Gets details about a [Preview][google.cloud.config.v1.Preview].

        Returns:
            Callable[[~.GetPreviewRequest],
                    ~.Preview]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_preview" not in self._stubs:
            self._stubs["get_preview"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetPreview",
                request_serializer=config.GetPreviewRequest.serialize,
                response_deserializer=config.Preview.deserialize,
            )
        return self._stubs["get_preview"]

    @property
    def list_previews(
        self,
    ) -> Callable[[config.ListPreviewsRequest], config.ListPreviewsResponse]:
        r"""Return a callable for the list previews method over gRPC.

        Lists [Preview][google.cloud.config.v1.Preview]s in a given
        project and location.

        Returns:
            Callable[[~.ListPreviewsRequest],
                    ~.ListPreviewsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_previews" not in self._stubs:
            self._stubs["list_previews"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ListPreviews",
                request_serializer=config.ListPreviewsRequest.serialize,
                response_deserializer=config.ListPreviewsResponse.deserialize,
            )
        return self._stubs["list_previews"]

    @property
    def delete_preview(
        self,
    ) -> Callable[[config.DeletePreviewRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete preview method over gRPC.

        Deletes a [Preview][google.cloud.config.v1.Preview].

        Returns:
            Callable[[~.DeletePreviewRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_preview" not in self._stubs:
            self._stubs["delete_preview"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/DeletePreview",
                request_serializer=config.DeletePreviewRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_preview"]

    @property
    def export_preview_result(
        self,
    ) -> Callable[
        [config.ExportPreviewResultRequest], config.ExportPreviewResultResponse
    ]:
        r"""Return a callable for the export preview result method over gRPC.

        Export [Preview][google.cloud.config.v1.Preview] results.

        Returns:
            Callable[[~.ExportPreviewResultRequest],
                    ~.ExportPreviewResultResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_preview_result" not in self._stubs:
            self._stubs["export_preview_result"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ExportPreviewResult",
                request_serializer=config.ExportPreviewResultRequest.serialize,
                response_deserializer=config.ExportPreviewResultResponse.deserialize,
            )
        return self._stubs["export_preview_result"]

    @property
    def list_terraform_versions(
        self,
    ) -> Callable[
        [config.ListTerraformVersionsRequest], config.ListTerraformVersionsResponse
    ]:
        r"""Return a callable for the list terraform versions method over gRPC.

        Lists
        [TerraformVersion][google.cloud.config.v1.TerraformVersion]s in
        a given project and location.

        Returns:
            Callable[[~.ListTerraformVersionsRequest],
                    ~.ListTerraformVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_terraform_versions" not in self._stubs:
            self._stubs["list_terraform_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ListTerraformVersions",
                request_serializer=config.ListTerraformVersionsRequest.serialize,
                response_deserializer=config.ListTerraformVersionsResponse.deserialize,
            )
        return self._stubs["list_terraform_versions"]

    @property
    def get_terraform_version(
        self,
    ) -> Callable[[config.GetTerraformVersionRequest], config.TerraformVersion]:
        r"""Return a callable for the get terraform version method over gRPC.

        Gets details about a
        [TerraformVersion][google.cloud.config.v1.TerraformVersion].

        Returns:
            Callable[[~.GetTerraformVersionRequest],
                    ~.TerraformVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_terraform_version" not in self._stubs:
            self._stubs["get_terraform_version"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetTerraformVersion",
                request_serializer=config.GetTerraformVersionRequest.serialize,
                response_deserializer=config.TerraformVersion.deserialize,
            )
        return self._stubs["get_terraform_version"]

    @property
    def list_resource_changes(
        self,
    ) -> Callable[
        [config.ListResourceChangesRequest], config.ListResourceChangesResponse
    ]:
        r"""Return a callable for the list resource changes method over gRPC.

        Lists ResourceChanges for a given preview.

        Returns:
            Callable[[~.ListResourceChangesRequest],
                    ~.ListResourceChangesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_resource_changes" not in self._stubs:
            self._stubs["list_resource_changes"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ListResourceChanges",
                request_serializer=config.ListResourceChangesRequest.serialize,
                response_deserializer=config.ListResourceChangesResponse.deserialize,
            )
        return self._stubs["list_resource_changes"]

    @property
    def get_resource_change(
        self,
    ) -> Callable[[config.GetResourceChangeRequest], config.ResourceChange]:
        r"""Return a callable for the get resource change method over gRPC.

        Get a ResourceChange for a given preview.

        Returns:
            Callable[[~.GetResourceChangeRequest],
                    ~.ResourceChange]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_resource_change" not in self._stubs:
            self._stubs["get_resource_change"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetResourceChange",
                request_serializer=config.GetResourceChangeRequest.serialize,
                response_deserializer=config.ResourceChange.deserialize,
            )
        return self._stubs["get_resource_change"]

    @property
    def list_resource_drifts(
        self,
    ) -> Callable[
        [config.ListResourceDriftsRequest], config.ListResourceDriftsResponse
    ]:
        r"""Return a callable for the list resource drifts method over gRPC.

        List ResourceDrifts for a given preview.

        Returns:
            Callable[[~.ListResourceDriftsRequest],
                    ~.ListResourceDriftsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_resource_drifts" not in self._stubs:
            self._stubs["list_resource_drifts"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ListResourceDrifts",
                request_serializer=config.ListResourceDriftsRequest.serialize,
                response_deserializer=config.ListResourceDriftsResponse.deserialize,
            )
        return self._stubs["list_resource_drifts"]

    @property
    def get_resource_drift(
        self,
    ) -> Callable[[config.GetResourceDriftRequest], config.ResourceDrift]:
        r"""Return a callable for the get resource drift method over gRPC.

        Get a ResourceDrift for a given preview.

        Returns:
            Callable[[~.GetResourceDriftRequest],
                    ~.ResourceDrift]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_resource_drift" not in self._stubs:
            self._stubs["get_resource_drift"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetResourceDrift",
                request_serializer=config.GetResourceDriftRequest.serialize,
                response_deserializer=config.ResourceDrift.deserialize,
            )
        return self._stubs["get_resource_drift"]

    @property
    def get_auto_migration_config(
        self,
    ) -> Callable[[config.GetAutoMigrationConfigRequest], config.AutoMigrationConfig]:
        r"""Return a callable for the get auto migration config method over gRPC.

        Get the AutoMigrationConfig for a given project and
        location.

        Returns:
            Callable[[~.GetAutoMigrationConfigRequest],
                    ~.AutoMigrationConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_auto_migration_config" not in self._stubs:
            self._stubs["get_auto_migration_config"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetAutoMigrationConfig",
                request_serializer=config.GetAutoMigrationConfigRequest.serialize,
                response_deserializer=config.AutoMigrationConfig.deserialize,
            )
        return self._stubs["get_auto_migration_config"]

    @property
    def update_auto_migration_config(
        self,
    ) -> Callable[[config.UpdateAutoMigrationConfigRequest], operations_pb2.Operation]:
        r"""Return a callable for the update auto migration config method over gRPC.

        Updates the AutoMigrationConfig for a given project
        and location.

        Returns:
            Callable[[~.UpdateAutoMigrationConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_auto_migration_config" not in self._stubs:
            self._stubs["update_auto_migration_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.config.v1.Config/UpdateAutoMigrationConfig",
                    request_serializer=config.UpdateAutoMigrationConfigRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_auto_migration_config"]

    @property
    def get_deployment_group(
        self,
    ) -> Callable[[config.GetDeploymentGroupRequest], config.DeploymentGroup]:
        r"""Return a callable for the get deployment group method over gRPC.

        Get a DeploymentGroup for a given project and
        location.

        Returns:
            Callable[[~.GetDeploymentGroupRequest],
                    ~.DeploymentGroup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deployment_group" not in self._stubs:
            self._stubs["get_deployment_group"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/GetDeploymentGroup",
                request_serializer=config.GetDeploymentGroupRequest.serialize,
                response_deserializer=config.DeploymentGroup.deserialize,
            )
        return self._stubs["get_deployment_group"]

    @property
    def create_deployment_group(
        self,
    ) -> Callable[[config.CreateDeploymentGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the create deployment group method over gRPC.

        Creates a
        [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] The
        newly created DeploymentGroup will be in the ``CREATING`` state
        and can be retrieved via Get and List calls.

        Returns:
            Callable[[~.CreateDeploymentGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_deployment_group" not in self._stubs:
            self._stubs["create_deployment_group"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/CreateDeploymentGroup",
                request_serializer=config.CreateDeploymentGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_deployment_group"]

    @property
    def update_deployment_group(
        self,
    ) -> Callable[[config.UpdateDeploymentGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the update deployment group method over gRPC.

        Updates a
        [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

        Returns:
            Callable[[~.UpdateDeploymentGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_deployment_group" not in self._stubs:
            self._stubs["update_deployment_group"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/UpdateDeploymentGroup",
                request_serializer=config.UpdateDeploymentGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_deployment_group"]

    @property
    def delete_deployment_group(
        self,
    ) -> Callable[[config.DeleteDeploymentGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete deployment group method over gRPC.

        Deletes a
        [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

        Returns:
            Callable[[~.DeleteDeploymentGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_deployment_group" not in self._stubs:
            self._stubs["delete_deployment_group"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/DeleteDeploymentGroup",
                request_serializer=config.DeleteDeploymentGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_deployment_group"]

    @property
    def list_deployment_groups(
        self,
    ) -> Callable[
        [config.ListDeploymentGroupsRequest], config.ListDeploymentGroupsResponse
    ]:
        r"""Return a callable for the list deployment groups method over gRPC.

        List DeploymentGroups for a given project and
        location.

        Returns:
            Callable[[~.ListDeploymentGroupsRequest],
                    ~.ListDeploymentGroupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deployment_groups" not in self._stubs:
            self._stubs["list_deployment_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.config.v1.Config/ListDeploymentGroups",
                request_serializer=config.ListDeploymentGroupsRequest.serialize,
                response_deserializer=config.ListDeploymentGroupsResponse.deserialize,
            )
        return self._stubs["list_deployment_groups"]

    @property
    def provision_deployment_group(
        self,
    ) -> Callable[[config.ProvisionDeploymentGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the provision deployment group method over gRPC.

        Provisions a deployment group.

        NOTE: As a first step of this operation, Infra Manager will
        automatically delete any Deployments that were part of the *last
        successful*
        [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision]
        but are *no longer* included in the *current*
        [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]
        definition (e.g., following an ``UpdateDeploymentGroup`` call),
        along with their actuated resources.

        Returns:
            Callable[[~.ProvisionDeploymentGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "provision_deployment_group" not in self._stubs:
            self._stubs["provision_deployment_group"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.config.v1.Config/ProvisionDeploymentGroup",
                    request_serializer=config.ProvisionDeploymentGroupRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["provision_deployment_group"]

    @property
    def deprovision_deployment_group(
        self,
    ) -> Callable[[config.DeprovisionDeploymentGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the deprovision deployment group method over gRPC.

        Deprovisions a deployment group.

        NOTE: As a first step of this operation, Infra Manager will
        automatically delete any Deployments that were part of the *last
        successful*
        [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision]
        but are *no longer* included in the *current*
        [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]
        definition (e.g., following an ``UpdateDeploymentGroup`` call),
        along with their actuated resources.

        Returns:
            Callable[[~.DeprovisionDeploymentGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deprovision_deployment_group" not in self._stubs:
            self._stubs["deprovision_deployment_group"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.config.v1.Config/DeprovisionDeploymentGroup",
                    request_serializer=config.DeprovisionDeploymentGroupRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["deprovision_deployment_group"]

    @property
    def get_deployment_group_revision(
        self,
    ) -> Callable[
        [config.GetDeploymentGroupRevisionRequest], config.DeploymentGroupRevision
    ]:
        r"""Return a callable for the get deployment group revision method over gRPC.

        Gets details about a
        [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision].

        Returns:
            Callable[[~.GetDeploymentGroupRevisionRequest],
                    ~.DeploymentGroupRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deployment_group_revision" not in self._stubs:
            self._stubs["get_deployment_group_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.config.v1.Config/GetDeploymentGroupRevision",
                    request_serializer=config.GetDeploymentGroupRevisionRequest.serialize,
                    response_deserializer=config.DeploymentGroupRevision.deserialize,
                )
            )
        return self._stubs["get_deployment_group_revision"]

    @property
    def list_deployment_group_revisions(
        self,
    ) -> Callable[
        [config.ListDeploymentGroupRevisionsRequest],
        config.ListDeploymentGroupRevisionsResponse,
    ]:
        r"""Return a callable for the list deployment group
        revisions method over gRPC.

        Lists
        [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision]s
        in a given
        [DeploymentGroup][google.cloud.config.v1.DeploymentGroup].

        Returns:
            Callable[[~.ListDeploymentGroupRevisionsRequest],
                    ~.ListDeploymentGroupRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deployment_group_revisions" not in self._stubs:
            self._stubs["list_deployment_group_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.config.v1.Config/ListDeploymentGroupRevisions",
                    request_serializer=config.ListDeploymentGroupRevisionsRequest.serialize,
                    response_deserializer=config.ListDeploymentGroupRevisionsResponse.deserialize,
                )
            )
        return self._stubs["list_deployment_group_revisions"]

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


__all__ = ("ConfigGrpcTransport",)
