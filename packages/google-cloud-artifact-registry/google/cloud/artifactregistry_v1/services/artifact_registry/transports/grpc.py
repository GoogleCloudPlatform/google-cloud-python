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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.artifactregistry_v1.types import (
    apt_artifact,
    artifact,
    attachment,
    export,
    file,
    package,
    repository,
    rule,
    settings,
    tag,
    version,
    vpcsc_config,
    yum_artifact,
)
from google.cloud.artifactregistry_v1.types import attachment as gda_attachment
from google.cloud.artifactregistry_v1.types import file as gda_file
from google.cloud.artifactregistry_v1.types import package as gda_package
from google.cloud.artifactregistry_v1.types import repository as gda_repository
from google.cloud.artifactregistry_v1.types import rule as gda_rule
from google.cloud.artifactregistry_v1.types import tag as gda_tag
from google.cloud.artifactregistry_v1.types import version as gda_version
from google.cloud.artifactregistry_v1.types import vpcsc_config as gda_vpcsc_config

from .base import DEFAULT_CLIENT_INFO, ArtifactRegistryTransport

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
                    "serviceName": "google.devtools.artifactregistry.v1.ArtifactRegistry",
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
                    "serviceName": "google.devtools.artifactregistry.v1.ArtifactRegistry",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ArtifactRegistryGrpcTransport(ArtifactRegistryTransport):
    """gRPC backend transport for ArtifactRegistry.

    The Artifact Registry API service.

    Artifact Registry is an artifact management system for storing
    artifacts from different package management systems.

    The resources managed by this API are:

    - Repositories, which group packages and their data.
    - Packages, which group versions and their tags.
    - Versions, which are specific forms of a package.
    - Tags, which represent alternative names for versions.
    - Files, which contain content and are optionally associated with a
      Package or Version.

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
        host: str = "artifactregistry.googleapis.com",
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
                 The hostname to connect to (default: 'artifactregistry.googleapis.com').
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
        host: str = "artifactregistry.googleapis.com",
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
    def list_docker_images(
        self,
    ) -> Callable[
        [artifact.ListDockerImagesRequest], artifact.ListDockerImagesResponse
    ]:
        r"""Return a callable for the list docker images method over gRPC.

        Lists docker images.

        Returns:
            Callable[[~.ListDockerImagesRequest],
                    ~.ListDockerImagesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_docker_images" not in self._stubs:
            self._stubs["list_docker_images"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListDockerImages",
                request_serializer=artifact.ListDockerImagesRequest.serialize,
                response_deserializer=artifact.ListDockerImagesResponse.deserialize,
            )
        return self._stubs["list_docker_images"]

    @property
    def get_docker_image(
        self,
    ) -> Callable[[artifact.GetDockerImageRequest], artifact.DockerImage]:
        r"""Return a callable for the get docker image method over gRPC.

        Gets a docker image.

        Returns:
            Callable[[~.GetDockerImageRequest],
                    ~.DockerImage]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_docker_image" not in self._stubs:
            self._stubs["get_docker_image"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetDockerImage",
                request_serializer=artifact.GetDockerImageRequest.serialize,
                response_deserializer=artifact.DockerImage.deserialize,
            )
        return self._stubs["get_docker_image"]

    @property
    def list_maven_artifacts(
        self,
    ) -> Callable[
        [artifact.ListMavenArtifactsRequest], artifact.ListMavenArtifactsResponse
    ]:
        r"""Return a callable for the list maven artifacts method over gRPC.

        Lists maven artifacts.

        Returns:
            Callable[[~.ListMavenArtifactsRequest],
                    ~.ListMavenArtifactsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_maven_artifacts" not in self._stubs:
            self._stubs["list_maven_artifacts"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListMavenArtifacts",
                request_serializer=artifact.ListMavenArtifactsRequest.serialize,
                response_deserializer=artifact.ListMavenArtifactsResponse.deserialize,
            )
        return self._stubs["list_maven_artifacts"]

    @property
    def get_maven_artifact(
        self,
    ) -> Callable[[artifact.GetMavenArtifactRequest], artifact.MavenArtifact]:
        r"""Return a callable for the get maven artifact method over gRPC.

        Gets a maven artifact.

        Returns:
            Callable[[~.GetMavenArtifactRequest],
                    ~.MavenArtifact]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_maven_artifact" not in self._stubs:
            self._stubs["get_maven_artifact"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetMavenArtifact",
                request_serializer=artifact.GetMavenArtifactRequest.serialize,
                response_deserializer=artifact.MavenArtifact.deserialize,
            )
        return self._stubs["get_maven_artifact"]

    @property
    def list_npm_packages(
        self,
    ) -> Callable[[artifact.ListNpmPackagesRequest], artifact.ListNpmPackagesResponse]:
        r"""Return a callable for the list npm packages method over gRPC.

        Lists npm packages.

        Returns:
            Callable[[~.ListNpmPackagesRequest],
                    ~.ListNpmPackagesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_npm_packages" not in self._stubs:
            self._stubs["list_npm_packages"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListNpmPackages",
                request_serializer=artifact.ListNpmPackagesRequest.serialize,
                response_deserializer=artifact.ListNpmPackagesResponse.deserialize,
            )
        return self._stubs["list_npm_packages"]

    @property
    def get_npm_package(
        self,
    ) -> Callable[[artifact.GetNpmPackageRequest], artifact.NpmPackage]:
        r"""Return a callable for the get npm package method over gRPC.

        Gets a npm package.

        Returns:
            Callable[[~.GetNpmPackageRequest],
                    ~.NpmPackage]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_npm_package" not in self._stubs:
            self._stubs["get_npm_package"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetNpmPackage",
                request_serializer=artifact.GetNpmPackageRequest.serialize,
                response_deserializer=artifact.NpmPackage.deserialize,
            )
        return self._stubs["get_npm_package"]

    @property
    def list_python_packages(
        self,
    ) -> Callable[
        [artifact.ListPythonPackagesRequest], artifact.ListPythonPackagesResponse
    ]:
        r"""Return a callable for the list python packages method over gRPC.

        Lists python packages.

        Returns:
            Callable[[~.ListPythonPackagesRequest],
                    ~.ListPythonPackagesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_python_packages" not in self._stubs:
            self._stubs["list_python_packages"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListPythonPackages",
                request_serializer=artifact.ListPythonPackagesRequest.serialize,
                response_deserializer=artifact.ListPythonPackagesResponse.deserialize,
            )
        return self._stubs["list_python_packages"]

    @property
    def get_python_package(
        self,
    ) -> Callable[[artifact.GetPythonPackageRequest], artifact.PythonPackage]:
        r"""Return a callable for the get python package method over gRPC.

        Gets a python package.

        Returns:
            Callable[[~.GetPythonPackageRequest],
                    ~.PythonPackage]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_python_package" not in self._stubs:
            self._stubs["get_python_package"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetPythonPackage",
                request_serializer=artifact.GetPythonPackageRequest.serialize,
                response_deserializer=artifact.PythonPackage.deserialize,
            )
        return self._stubs["get_python_package"]

    @property
    def import_apt_artifacts(
        self,
    ) -> Callable[[apt_artifact.ImportAptArtifactsRequest], operations_pb2.Operation]:
        r"""Return a callable for the import apt artifacts method over gRPC.

        Imports Apt artifacts. The returned Operation will
        complete once the resources are imported. Package,
        Version, and File resources are created based on the
        imported artifacts. Imported artifacts that conflict
        with existing resources are ignored.

        Returns:
            Callable[[~.ImportAptArtifactsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_apt_artifacts" not in self._stubs:
            self._stubs["import_apt_artifacts"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ImportAptArtifacts",
                request_serializer=apt_artifact.ImportAptArtifactsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_apt_artifacts"]

    @property
    def import_yum_artifacts(
        self,
    ) -> Callable[[yum_artifact.ImportYumArtifactsRequest], operations_pb2.Operation]:
        r"""Return a callable for the import yum artifacts method over gRPC.

        Imports Yum (RPM) artifacts. The returned Operation
        will complete once the resources are imported. Package,
        Version, and File resources are created based on the
        imported artifacts. Imported artifacts that conflict
        with existing resources are ignored.

        Returns:
            Callable[[~.ImportYumArtifactsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_yum_artifacts" not in self._stubs:
            self._stubs["import_yum_artifacts"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ImportYumArtifacts",
                request_serializer=yum_artifact.ImportYumArtifactsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_yum_artifacts"]

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [repository.ListRepositoriesRequest], repository.ListRepositoriesResponse
    ]:
        r"""Return a callable for the list repositories method over gRPC.

        Lists repositories.

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
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListRepositories",
                request_serializer=repository.ListRepositoriesRequest.serialize,
                response_deserializer=repository.ListRepositoriesResponse.deserialize,
            )
        return self._stubs["list_repositories"]

    @property
    def get_repository(
        self,
    ) -> Callable[[repository.GetRepositoryRequest], repository.Repository]:
        r"""Return a callable for the get repository method over gRPC.

        Gets a repository.

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
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetRepository",
                request_serializer=repository.GetRepositoryRequest.serialize,
                response_deserializer=repository.Repository.deserialize,
            )
        return self._stubs["get_repository"]

    @property
    def create_repository(
        self,
    ) -> Callable[[gda_repository.CreateRepositoryRequest], operations_pb2.Operation]:
        r"""Return a callable for the create repository method over gRPC.

        Creates a repository. The returned Operation will
        finish once the repository has been created. Its
        response will be the created Repository.

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
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateRepository",
                request_serializer=gda_repository.CreateRepositoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_repository"]

    @property
    def update_repository(
        self,
    ) -> Callable[[gda_repository.UpdateRepositoryRequest], gda_repository.Repository]:
        r"""Return a callable for the update repository method over gRPC.

        Updates a repository.

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
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateRepository",
                request_serializer=gda_repository.UpdateRepositoryRequest.serialize,
                response_deserializer=gda_repository.Repository.deserialize,
            )
        return self._stubs["update_repository"]

    @property
    def delete_repository(
        self,
    ) -> Callable[[repository.DeleteRepositoryRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete repository method over gRPC.

        Deletes a repository and all of its contents. The
        returned Operation will finish once the repository has
        been deleted. It will not have any Operation metadata
        and will return a google.protobuf.Empty response.

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
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteRepository",
                request_serializer=repository.DeleteRepositoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_repository"]

    @property
    def list_packages(
        self,
    ) -> Callable[[package.ListPackagesRequest], package.ListPackagesResponse]:
        r"""Return a callable for the list packages method over gRPC.

        Lists packages.

        Returns:
            Callable[[~.ListPackagesRequest],
                    ~.ListPackagesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_packages" not in self._stubs:
            self._stubs["list_packages"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListPackages",
                request_serializer=package.ListPackagesRequest.serialize,
                response_deserializer=package.ListPackagesResponse.deserialize,
            )
        return self._stubs["list_packages"]

    @property
    def get_package(self) -> Callable[[package.GetPackageRequest], package.Package]:
        r"""Return a callable for the get package method over gRPC.

        Gets a package.

        Returns:
            Callable[[~.GetPackageRequest],
                    ~.Package]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_package" not in self._stubs:
            self._stubs["get_package"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetPackage",
                request_serializer=package.GetPackageRequest.serialize,
                response_deserializer=package.Package.deserialize,
            )
        return self._stubs["get_package"]

    @property
    def delete_package(
        self,
    ) -> Callable[[package.DeletePackageRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete package method over gRPC.

        Deletes a package and all of its versions and tags.
        The returned operation will complete once the package
        has been deleted.

        Returns:
            Callable[[~.DeletePackageRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_package" not in self._stubs:
            self._stubs["delete_package"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/DeletePackage",
                request_serializer=package.DeletePackageRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_package"]

    @property
    def list_versions(
        self,
    ) -> Callable[[version.ListVersionsRequest], version.ListVersionsResponse]:
        r"""Return a callable for the list versions method over gRPC.

        Lists versions.

        Returns:
            Callable[[~.ListVersionsRequest],
                    ~.ListVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_versions" not in self._stubs:
            self._stubs["list_versions"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListVersions",
                request_serializer=version.ListVersionsRequest.serialize,
                response_deserializer=version.ListVersionsResponse.deserialize,
            )
        return self._stubs["list_versions"]

    @property
    def get_version(self) -> Callable[[version.GetVersionRequest], version.Version]:
        r"""Return a callable for the get version method over gRPC.

        Gets a version

        Returns:
            Callable[[~.GetVersionRequest],
                    ~.Version]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_version" not in self._stubs:
            self._stubs["get_version"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetVersion",
                request_serializer=version.GetVersionRequest.serialize,
                response_deserializer=version.Version.deserialize,
            )
        return self._stubs["get_version"]

    @property
    def delete_version(
        self,
    ) -> Callable[[version.DeleteVersionRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete version method over gRPC.

        Deletes a version and all of its content. The
        returned operation will complete once the version has
        been deleted.

        Returns:
            Callable[[~.DeleteVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_version" not in self._stubs:
            self._stubs["delete_version"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteVersion",
                request_serializer=version.DeleteVersionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_version"]

    @property
    def batch_delete_versions(
        self,
    ) -> Callable[[version.BatchDeleteVersionsRequest], operations_pb2.Operation]:
        r"""Return a callable for the batch delete versions method over gRPC.

        Deletes multiple versions across a repository. The
        returned operation will complete once the versions have
        been deleted.

        Returns:
            Callable[[~.BatchDeleteVersionsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_versions" not in self._stubs:
            self._stubs["batch_delete_versions"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/BatchDeleteVersions",
                request_serializer=version.BatchDeleteVersionsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_delete_versions"]

    @property
    def update_version(
        self,
    ) -> Callable[[gda_version.UpdateVersionRequest], gda_version.Version]:
        r"""Return a callable for the update version method over gRPC.

        Updates a version.

        Returns:
            Callable[[~.UpdateVersionRequest],
                    ~.Version]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_version" not in self._stubs:
            self._stubs["update_version"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateVersion",
                request_serializer=gda_version.UpdateVersionRequest.serialize,
                response_deserializer=gda_version.Version.deserialize,
            )
        return self._stubs["update_version"]

    @property
    def list_files(self) -> Callable[[file.ListFilesRequest], file.ListFilesResponse]:
        r"""Return a callable for the list files method over gRPC.

        Lists files.

        Returns:
            Callable[[~.ListFilesRequest],
                    ~.ListFilesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_files" not in self._stubs:
            self._stubs["list_files"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListFiles",
                request_serializer=file.ListFilesRequest.serialize,
                response_deserializer=file.ListFilesResponse.deserialize,
            )
        return self._stubs["list_files"]

    @property
    def get_file(self) -> Callable[[file.GetFileRequest], file.File]:
        r"""Return a callable for the get file method over gRPC.

        Gets a file.

        Returns:
            Callable[[~.GetFileRequest],
                    ~.File]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_file" not in self._stubs:
            self._stubs["get_file"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetFile",
                request_serializer=file.GetFileRequest.serialize,
                response_deserializer=file.File.deserialize,
            )
        return self._stubs["get_file"]

    @property
    def delete_file(
        self,
    ) -> Callable[[file.DeleteFileRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete file method over gRPC.

        Deletes a file and all of its content. It is only
        allowed on generic repositories. The returned operation
        will complete once the file has been deleted.

        Returns:
            Callable[[~.DeleteFileRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_file" not in self._stubs:
            self._stubs["delete_file"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteFile",
                request_serializer=file.DeleteFileRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_file"]

    @property
    def update_file(self) -> Callable[[gda_file.UpdateFileRequest], gda_file.File]:
        r"""Return a callable for the update file method over gRPC.

        Updates a file.

        Returns:
            Callable[[~.UpdateFileRequest],
                    ~.File]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_file" not in self._stubs:
            self._stubs["update_file"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateFile",
                request_serializer=gda_file.UpdateFileRequest.serialize,
                response_deserializer=gda_file.File.deserialize,
            )
        return self._stubs["update_file"]

    @property
    def list_tags(self) -> Callable[[tag.ListTagsRequest], tag.ListTagsResponse]:
        r"""Return a callable for the list tags method over gRPC.

        Lists tags.

        Returns:
            Callable[[~.ListTagsRequest],
                    ~.ListTagsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_tags" not in self._stubs:
            self._stubs["list_tags"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListTags",
                request_serializer=tag.ListTagsRequest.serialize,
                response_deserializer=tag.ListTagsResponse.deserialize,
            )
        return self._stubs["list_tags"]

    @property
    def get_tag(self) -> Callable[[tag.GetTagRequest], tag.Tag]:
        r"""Return a callable for the get tag method over gRPC.

        Gets a tag.

        Returns:
            Callable[[~.GetTagRequest],
                    ~.Tag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_tag" not in self._stubs:
            self._stubs["get_tag"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetTag",
                request_serializer=tag.GetTagRequest.serialize,
                response_deserializer=tag.Tag.deserialize,
            )
        return self._stubs["get_tag"]

    @property
    def create_tag(self) -> Callable[[gda_tag.CreateTagRequest], gda_tag.Tag]:
        r"""Return a callable for the create tag method over gRPC.

        Creates a tag.

        Returns:
            Callable[[~.CreateTagRequest],
                    ~.Tag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tag" not in self._stubs:
            self._stubs["create_tag"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateTag",
                request_serializer=gda_tag.CreateTagRequest.serialize,
                response_deserializer=gda_tag.Tag.deserialize,
            )
        return self._stubs["create_tag"]

    @property
    def update_tag(self) -> Callable[[gda_tag.UpdateTagRequest], gda_tag.Tag]:
        r"""Return a callable for the update tag method over gRPC.

        Updates a tag.

        Returns:
            Callable[[~.UpdateTagRequest],
                    ~.Tag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tag" not in self._stubs:
            self._stubs["update_tag"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateTag",
                request_serializer=gda_tag.UpdateTagRequest.serialize,
                response_deserializer=gda_tag.Tag.deserialize,
            )
        return self._stubs["update_tag"]

    @property
    def delete_tag(self) -> Callable[[tag.DeleteTagRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete tag method over gRPC.

        Deletes a tag.

        Returns:
            Callable[[~.DeleteTagRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tag" not in self._stubs:
            self._stubs["delete_tag"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteTag",
                request_serializer=tag.DeleteTagRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_tag"]

    @property
    def create_rule(self) -> Callable[[gda_rule.CreateRuleRequest], gda_rule.Rule]:
        r"""Return a callable for the create rule method over gRPC.

        Creates a rule.

        Returns:
            Callable[[~.CreateRuleRequest],
                    ~.Rule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_rule" not in self._stubs:
            self._stubs["create_rule"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateRule",
                request_serializer=gda_rule.CreateRuleRequest.serialize,
                response_deserializer=gda_rule.Rule.deserialize,
            )
        return self._stubs["create_rule"]

    @property
    def list_rules(self) -> Callable[[rule.ListRulesRequest], rule.ListRulesResponse]:
        r"""Return a callable for the list rules method over gRPC.

        Lists rules.

        Returns:
            Callable[[~.ListRulesRequest],
                    ~.ListRulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_rules" not in self._stubs:
            self._stubs["list_rules"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListRules",
                request_serializer=rule.ListRulesRequest.serialize,
                response_deserializer=rule.ListRulesResponse.deserialize,
            )
        return self._stubs["list_rules"]

    @property
    def get_rule(self) -> Callable[[rule.GetRuleRequest], rule.Rule]:
        r"""Return a callable for the get rule method over gRPC.

        Gets a rule.

        Returns:
            Callable[[~.GetRuleRequest],
                    ~.Rule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_rule" not in self._stubs:
            self._stubs["get_rule"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetRule",
                request_serializer=rule.GetRuleRequest.serialize,
                response_deserializer=rule.Rule.deserialize,
            )
        return self._stubs["get_rule"]

    @property
    def update_rule(self) -> Callable[[gda_rule.UpdateRuleRequest], gda_rule.Rule]:
        r"""Return a callable for the update rule method over gRPC.

        Updates a rule.

        Returns:
            Callable[[~.UpdateRuleRequest],
                    ~.Rule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_rule" not in self._stubs:
            self._stubs["update_rule"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateRule",
                request_serializer=gda_rule.UpdateRuleRequest.serialize,
                response_deserializer=gda_rule.Rule.deserialize,
            )
        return self._stubs["update_rule"]

    @property
    def delete_rule(self) -> Callable[[rule.DeleteRuleRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete rule method over gRPC.

        Deletes a rule.

        Returns:
            Callable[[~.DeleteRuleRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_rule" not in self._stubs:
            self._stubs["delete_rule"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteRule",
                request_serializer=rule.DeleteRuleRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_rule"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.

        Updates the IAM policy for a given resource.

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
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the IAM policy for a given resource.

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
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetIamPolicy",
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

        Tests if the caller has a list of permissions on a
        resource.

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
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def get_project_settings(
        self,
    ) -> Callable[[settings.GetProjectSettingsRequest], settings.ProjectSettings]:
        r"""Return a callable for the get project settings method over gRPC.

        Retrieves the Settings for the Project.

        Returns:
            Callable[[~.GetProjectSettingsRequest],
                    ~.ProjectSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_project_settings" not in self._stubs:
            self._stubs["get_project_settings"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetProjectSettings",
                request_serializer=settings.GetProjectSettingsRequest.serialize,
                response_deserializer=settings.ProjectSettings.deserialize,
            )
        return self._stubs["get_project_settings"]

    @property
    def update_project_settings(
        self,
    ) -> Callable[[settings.UpdateProjectSettingsRequest], settings.ProjectSettings]:
        r"""Return a callable for the update project settings method over gRPC.

        Updates the Settings for the Project.

        Returns:
            Callable[[~.UpdateProjectSettingsRequest],
                    ~.ProjectSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_project_settings" not in self._stubs:
            self._stubs["update_project_settings"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateProjectSettings",
                request_serializer=settings.UpdateProjectSettingsRequest.serialize,
                response_deserializer=settings.ProjectSettings.deserialize,
            )
        return self._stubs["update_project_settings"]

    @property
    def get_vpcsc_config(
        self,
    ) -> Callable[[vpcsc_config.GetVPCSCConfigRequest], vpcsc_config.VPCSCConfig]:
        r"""Return a callable for the get vpcsc config method over gRPC.

        Retrieves the VPCSC Config for the Project.

        Returns:
            Callable[[~.GetVPCSCConfigRequest],
                    ~.VPCSCConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_vpcsc_config" not in self._stubs:
            self._stubs["get_vpcsc_config"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetVPCSCConfig",
                request_serializer=vpcsc_config.GetVPCSCConfigRequest.serialize,
                response_deserializer=vpcsc_config.VPCSCConfig.deserialize,
            )
        return self._stubs["get_vpcsc_config"]

    @property
    def update_vpcsc_config(
        self,
    ) -> Callable[
        [gda_vpcsc_config.UpdateVPCSCConfigRequest], gda_vpcsc_config.VPCSCConfig
    ]:
        r"""Return a callable for the update vpcsc config method over gRPC.

        Updates the VPCSC Config for the Project.

        Returns:
            Callable[[~.UpdateVPCSCConfigRequest],
                    ~.VPCSCConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_vpcsc_config" not in self._stubs:
            self._stubs["update_vpcsc_config"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateVPCSCConfig",
                request_serializer=gda_vpcsc_config.UpdateVPCSCConfigRequest.serialize,
                response_deserializer=gda_vpcsc_config.VPCSCConfig.deserialize,
            )
        return self._stubs["update_vpcsc_config"]

    @property
    def update_package(
        self,
    ) -> Callable[[gda_package.UpdatePackageRequest], gda_package.Package]:
        r"""Return a callable for the update package method over gRPC.

        Updates a package.

        Returns:
            Callable[[~.UpdatePackageRequest],
                    ~.Package]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_package" not in self._stubs:
            self._stubs["update_package"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdatePackage",
                request_serializer=gda_package.UpdatePackageRequest.serialize,
                response_deserializer=gda_package.Package.deserialize,
            )
        return self._stubs["update_package"]

    @property
    def list_attachments(
        self,
    ) -> Callable[
        [attachment.ListAttachmentsRequest], attachment.ListAttachmentsResponse
    ]:
        r"""Return a callable for the list attachments method over gRPC.

        Lists attachments.

        Returns:
            Callable[[~.ListAttachmentsRequest],
                    ~.ListAttachmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_attachments" not in self._stubs:
            self._stubs["list_attachments"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ListAttachments",
                request_serializer=attachment.ListAttachmentsRequest.serialize,
                response_deserializer=attachment.ListAttachmentsResponse.deserialize,
            )
        return self._stubs["list_attachments"]

    @property
    def get_attachment(
        self,
    ) -> Callable[[attachment.GetAttachmentRequest], attachment.Attachment]:
        r"""Return a callable for the get attachment method over gRPC.

        Gets an attachment.

        Returns:
            Callable[[~.GetAttachmentRequest],
                    ~.Attachment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_attachment" not in self._stubs:
            self._stubs["get_attachment"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/GetAttachment",
                request_serializer=attachment.GetAttachmentRequest.serialize,
                response_deserializer=attachment.Attachment.deserialize,
            )
        return self._stubs["get_attachment"]

    @property
    def create_attachment(
        self,
    ) -> Callable[[gda_attachment.CreateAttachmentRequest], operations_pb2.Operation]:
        r"""Return a callable for the create attachment method over gRPC.

        Creates an attachment. The returned Operation will
        finish once the attachment has been created. Its
        response will be the created attachment.

        Returns:
            Callable[[~.CreateAttachmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_attachment" not in self._stubs:
            self._stubs["create_attachment"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateAttachment",
                request_serializer=gda_attachment.CreateAttachmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_attachment"]

    @property
    def delete_attachment(
        self,
    ) -> Callable[[attachment.DeleteAttachmentRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete attachment method over gRPC.

        Deletes an attachment. The returned Operation will finish once
        the attachments has been deleted. It will not have any Operation
        metadata and will return a ``google.protobuf.Empty`` response.

        Returns:
            Callable[[~.DeleteAttachmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_attachment" not in self._stubs:
            self._stubs["delete_attachment"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteAttachment",
                request_serializer=attachment.DeleteAttachmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_attachment"]

    @property
    def export_artifact(
        self,
    ) -> Callable[[export.ExportArtifactRequest], operations_pb2.Operation]:
        r"""Return a callable for the export artifact method over gRPC.

        Exports an artifact to a Cloud Storage bucket.

        Returns:
            Callable[[~.ExportArtifactRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_artifact" not in self._stubs:
            self._stubs["export_artifact"] = self._logged_channel.unary_unary(
                "/google.devtools.artifactregistry.v1.ArtifactRegistry/ExportArtifact",
                request_serializer=export.ExportArtifactRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_artifact"]

    def close(self):
        self._logged_channel.close()

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


__all__ = ("ArtifactRegistryGrpcTransport",)
