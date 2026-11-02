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
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.gsuiteaddons_v1.types import gsuiteaddons

from .base import DEFAULT_CLIENT_INFO, GSuiteAddOnsTransport
from .grpc import GSuiteAddOnsGrpcTransport

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
                    "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
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
                    "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class GSuiteAddOnsGrpcAsyncIOTransport(GSuiteAddOnsTransport):
    """gRPC AsyncIO backend transport for GSuiteAddOns.

    A service for managing Google Workspace add-ons deployments.

    A Google Workspace add-on is a third-party embedded component
    that can be installed in Google Workspace Applications like
    Gmail, Calendar, Drive, and the Google Docs, Sheets, and Slides
    editors. Google Workspace add-ons can display UI cards, receive
    contextual information from the host application, and perform
    actions in the host application (See:

    https://developers.google.com/gsuite/add-ons/overview for more
    information).

    A Google Workspace add-on deployment resource specifies metadata
    about the add-on, including a specification of the entry points
    in the host application that trigger add-on executions (see:

    https://developers.google.com/gsuite/add-ons/concepts/gsuite-manifests).
    Add-on deployments defined via the Google Workspace add-ons API
    define their entrypoints using HTTPS URLs (See:

    https://developers.google.com/gsuite/add-ons/guides/alternate-runtimes),

    A Google Workspace add-on deployment can be installed in
    developer mode, which allows an add-on developer to test the
    experience an end-user would see when installing and running the
    add-on in their G Suite applications.  When running in developer
    mode, more detailed error messages are exposed in the add-on UI
    to aid in debugging.

    A Google Workspace add-on deployment can be published to Google
    Workspace Marketplace, which allows other Google Workspace users
    to discover and install the add-on.  See:

    https://developers.google.com/gsuite/add-ons/how-tos/publish-add-on-overview
    for details.

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
        host: str = "gsuiteaddons.googleapis.com",
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
        host: str = "gsuiteaddons.googleapis.com",
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
                 The hostname to connect to (default: 'gsuiteaddons.googleapis.com').
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
    def get_authorization(
        self,
    ) -> Callable[
        [gsuiteaddons.GetAuthorizationRequest], Awaitable[gsuiteaddons.Authorization]
    ]:
        r"""Return a callable for the get authorization method over gRPC.

        Gets the authorization information for deployments in
        a given project.

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
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/GetAuthorization",
                request_serializer=gsuiteaddons.GetAuthorizationRequest.serialize,
                response_deserializer=gsuiteaddons.Authorization.deserialize,
            )
        return self._stubs["get_authorization"]

    @property
    def create_deployment(
        self,
    ) -> Callable[
        [gsuiteaddons.CreateDeploymentRequest], Awaitable[gsuiteaddons.Deployment]
    ]:
        r"""Return a callable for the create deployment method over gRPC.

        Creates a deployment with the specified name and
        configuration.

        Returns:
            Callable[[~.CreateDeploymentRequest],
                    Awaitable[~.Deployment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_deployment" not in self._stubs:
            self._stubs["create_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/CreateDeployment",
                request_serializer=gsuiteaddons.CreateDeploymentRequest.serialize,
                response_deserializer=gsuiteaddons.Deployment.deserialize,
            )
        return self._stubs["create_deployment"]

    @property
    def replace_deployment(
        self,
    ) -> Callable[
        [gsuiteaddons.ReplaceDeploymentRequest], Awaitable[gsuiteaddons.Deployment]
    ]:
        r"""Return a callable for the replace deployment method over gRPC.

        Creates or replaces a deployment with the specified
        name.

        Returns:
            Callable[[~.ReplaceDeploymentRequest],
                    Awaitable[~.Deployment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "replace_deployment" not in self._stubs:
            self._stubs["replace_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/ReplaceDeployment",
                request_serializer=gsuiteaddons.ReplaceDeploymentRequest.serialize,
                response_deserializer=gsuiteaddons.Deployment.deserialize,
            )
        return self._stubs["replace_deployment"]

    @property
    def get_deployment(
        self,
    ) -> Callable[
        [gsuiteaddons.GetDeploymentRequest], Awaitable[gsuiteaddons.Deployment]
    ]:
        r"""Return a callable for the get deployment method over gRPC.

        Gets the deployment with the specified name.

        Returns:
            Callable[[~.GetDeploymentRequest],
                    Awaitable[~.Deployment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deployment" not in self._stubs:
            self._stubs["get_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/GetDeployment",
                request_serializer=gsuiteaddons.GetDeploymentRequest.serialize,
                response_deserializer=gsuiteaddons.Deployment.deserialize,
            )
        return self._stubs["get_deployment"]

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [gsuiteaddons.ListDeploymentsRequest],
        Awaitable[gsuiteaddons.ListDeploymentsResponse],
    ]:
        r"""Return a callable for the list deployments method over gRPC.

        Lists all deployments in a particular project.

        Returns:
            Callable[[~.ListDeploymentsRequest],
                    Awaitable[~.ListDeploymentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deployments" not in self._stubs:
            self._stubs["list_deployments"] = self._logged_channel.unary_unary(
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/ListDeployments",
                request_serializer=gsuiteaddons.ListDeploymentsRequest.serialize,
                response_deserializer=gsuiteaddons.ListDeploymentsResponse.deserialize,
            )
        return self._stubs["list_deployments"]

    @property
    def delete_deployment(
        self,
    ) -> Callable[[gsuiteaddons.DeleteDeploymentRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete deployment method over gRPC.

        Deletes the deployment with the given name.

        Returns:
            Callable[[~.DeleteDeploymentRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_deployment" not in self._stubs:
            self._stubs["delete_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/DeleteDeployment",
                request_serializer=gsuiteaddons.DeleteDeploymentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_deployment"]

    @property
    def install_deployment(
        self,
    ) -> Callable[[gsuiteaddons.InstallDeploymentRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the install deployment method over gRPC.

        Installs a deployment in developer mode.
        See:

        https://developers.google.com/gsuite/add-ons/how-tos/testing-gsuite-addons.

        Returns:
            Callable[[~.InstallDeploymentRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "install_deployment" not in self._stubs:
            self._stubs["install_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/InstallDeployment",
                request_serializer=gsuiteaddons.InstallDeploymentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["install_deployment"]

    @property
    def uninstall_deployment(
        self,
    ) -> Callable[
        [gsuiteaddons.UninstallDeploymentRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the uninstall deployment method over gRPC.

        Uninstalls a developer mode deployment.
        See:

        https://developers.google.com/gsuite/add-ons/how-tos/testing-gsuite-addons.

        Returns:
            Callable[[~.UninstallDeploymentRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "uninstall_deployment" not in self._stubs:
            self._stubs["uninstall_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/UninstallDeployment",
                request_serializer=gsuiteaddons.UninstallDeploymentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["uninstall_deployment"]

    @property
    def get_install_status(
        self,
    ) -> Callable[
        [gsuiteaddons.GetInstallStatusRequest], Awaitable[gsuiteaddons.InstallStatus]
    ]:
        r"""Return a callable for the get install status method over gRPC.

        Fetches the install status of a developer mode
        deployment.

        Returns:
            Callable[[~.GetInstallStatusRequest],
                    Awaitable[~.InstallStatus]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_install_status" not in self._stubs:
            self._stubs["get_install_status"] = self._logged_channel.unary_unary(
                "/google.cloud.gsuiteaddons.v1.GSuiteAddOns/GetInstallStatus",
                request_serializer=gsuiteaddons.GetInstallStatusRequest.serialize,
                response_deserializer=gsuiteaddons.InstallStatus.deserialize,
            )
        return self._stubs["get_install_status"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.get_authorization: self._wrap_method(
                self.get_authorization,
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_deployment: self._wrap_method(
                self.create_deployment,
                default_timeout=10.0,
                client_info=client_info,
            ),
            self.replace_deployment: self._wrap_method(
                self.replace_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_deployment: self._wrap_method(
                self.get_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_deployments: self._wrap_method(
                self.list_deployments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_deployment: self._wrap_method(
                self.delete_deployment,
                default_timeout=10.0,
                client_info=client_info,
            ),
            self.install_deployment: self._wrap_method(
                self.install_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.uninstall_deployment: self._wrap_method(
                self.uninstall_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_install_status: self._wrap_method(
                self.get_install_status,
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


__all__ = ("GSuiteAddOnsGrpcAsyncIOTransport",)
