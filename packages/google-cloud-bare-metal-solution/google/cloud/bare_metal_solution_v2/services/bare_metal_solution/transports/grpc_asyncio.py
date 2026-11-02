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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.bare_metal_solution_v2.types import (
    instance,
    lun,
    network,
    nfs_share,
    osimage,
    provisioning,
    ssh_key,
    volume,
    volume_snapshot,
)
from google.cloud.bare_metal_solution_v2.types import instance as gcb_instance
from google.cloud.bare_metal_solution_v2.types import network as gcb_network
from google.cloud.bare_metal_solution_v2.types import nfs_share as gcb_nfs_share
from google.cloud.bare_metal_solution_v2.types import ssh_key as gcb_ssh_key
from google.cloud.bare_metal_solution_v2.types import volume as gcb_volume
from google.cloud.bare_metal_solution_v2.types import (
    volume_snapshot as gcb_volume_snapshot,
)

from .base import DEFAULT_CLIENT_INFO, BareMetalSolutionTransport
from .grpc import BareMetalSolutionGrpcTransport

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
                    "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
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
                    "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class BareMetalSolutionGrpcAsyncIOTransport(BareMetalSolutionTransport):
    """gRPC AsyncIO backend transport for BareMetalSolution.

    Performs management operations on Bare Metal Solution servers.

    The ``baremetalsolution.googleapis.com`` service provides management
    capabilities for Bare Metal Solution servers. To access the API
    methods, you must assign Bare Metal Solution IAM roles containing
    the desired permissions to your staff in your Google Cloud project.
    You must also enable the Bare Metal Solution API. Once enabled, the
    methods act upon specific servers in your Bare Metal Solution
    environment.

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
        host: str = "baremetalsolution.googleapis.com",
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
        host: str = "baremetalsolution.googleapis.com",
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
                 The hostname to connect to (default: 'baremetalsolution.googleapis.com').
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
    def list_instances(
        self,
    ) -> Callable[
        [instance.ListInstancesRequest], Awaitable[instance.ListInstancesResponse]
    ]:
        r"""Return a callable for the list instances method over gRPC.

        List servers in a given project and location.

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
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListInstances",
                request_serializer=instance.ListInstancesRequest.serialize,
                response_deserializer=instance.ListInstancesResponse.deserialize,
            )
        return self._stubs["list_instances"]

    @property
    def get_instance(
        self,
    ) -> Callable[[instance.GetInstanceRequest], Awaitable[instance.Instance]]:
        r"""Return a callable for the get instance method over gRPC.

        Get details about a single server.

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
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/GetInstance",
                request_serializer=instance.GetInstanceRequest.serialize,
                response_deserializer=instance.Instance.deserialize,
            )
        return self._stubs["get_instance"]

    @property
    def update_instance(
        self,
    ) -> Callable[
        [gcb_instance.UpdateInstanceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update instance method over gRPC.

        Update details of a single server.

        Returns:
            Callable[[~.UpdateInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_instance" not in self._stubs:
            self._stubs["update_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateInstance",
                request_serializer=gcb_instance.UpdateInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_instance"]

    @property
    def rename_instance(
        self,
    ) -> Callable[[instance.RenameInstanceRequest], Awaitable[instance.Instance]]:
        r"""Return a callable for the rename instance method over gRPC.

        RenameInstance sets a new name for an instance.
        Use with caution, previous names become immediately
        invalidated.

        Returns:
            Callable[[~.RenameInstanceRequest],
                    Awaitable[~.Instance]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rename_instance" not in self._stubs:
            self._stubs["rename_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/RenameInstance",
                request_serializer=instance.RenameInstanceRequest.serialize,
                response_deserializer=instance.Instance.deserialize,
            )
        return self._stubs["rename_instance"]

    @property
    def reset_instance(
        self,
    ) -> Callable[[instance.ResetInstanceRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the reset instance method over gRPC.

        Perform an ungraceful, hard reset on a server.
        Equivalent to shutting the power off and then turning it
        back on.

        Returns:
            Callable[[~.ResetInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_instance" not in self._stubs:
            self._stubs["reset_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ResetInstance",
                request_serializer=instance.ResetInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reset_instance"]

    @property
    def start_instance(
        self,
    ) -> Callable[[instance.StartInstanceRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the start instance method over gRPC.

        Starts a server that was shutdown.

        Returns:
            Callable[[~.StartInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_instance" not in self._stubs:
            self._stubs["start_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/StartInstance",
                request_serializer=instance.StartInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_instance"]

    @property
    def stop_instance(
        self,
    ) -> Callable[[instance.StopInstanceRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the stop instance method over gRPC.

        Stop a running server.

        Returns:
            Callable[[~.StopInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_instance" not in self._stubs:
            self._stubs["stop_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/StopInstance",
                request_serializer=instance.StopInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["stop_instance"]

    @property
    def enable_interactive_serial_console(
        self,
    ) -> Callable[
        [instance.EnableInteractiveSerialConsoleRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the enable interactive serial
        console method over gRPC.

        Enable the interactive serial console feature on an
        instance.

        Returns:
            Callable[[~.EnableInteractiveSerialConsoleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "enable_interactive_serial_console" not in self._stubs:
            self._stubs["enable_interactive_serial_console"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.baremetalsolution.v2.BareMetalSolution/EnableInteractiveSerialConsole",
                    request_serializer=instance.EnableInteractiveSerialConsoleRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["enable_interactive_serial_console"]

    @property
    def disable_interactive_serial_console(
        self,
    ) -> Callable[
        [instance.DisableInteractiveSerialConsoleRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the disable interactive serial
        console method over gRPC.

        Disable the interactive serial console feature on an
        instance.

        Returns:
            Callable[[~.DisableInteractiveSerialConsoleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "disable_interactive_serial_console" not in self._stubs:
            self._stubs["disable_interactive_serial_console"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.baremetalsolution.v2.BareMetalSolution/DisableInteractiveSerialConsole",
                    request_serializer=instance.DisableInteractiveSerialConsoleRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["disable_interactive_serial_console"]

    @property
    def detach_lun(
        self,
    ) -> Callable[[gcb_instance.DetachLunRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the detach lun method over gRPC.

        Detach LUN from Instance.

        Returns:
            Callable[[~.DetachLunRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "detach_lun" not in self._stubs:
            self._stubs["detach_lun"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/DetachLun",
                request_serializer=gcb_instance.DetachLunRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["detach_lun"]

    @property
    def list_ssh_keys(
        self,
    ) -> Callable[[ssh_key.ListSSHKeysRequest], Awaitable[ssh_key.ListSSHKeysResponse]]:
        r"""Return a callable for the list ssh keys method over gRPC.

        Lists the public SSH keys registered for the
        specified project. These SSH keys are used only for the
        interactive serial console feature.

        Returns:
            Callable[[~.ListSSHKeysRequest],
                    Awaitable[~.ListSSHKeysResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_ssh_keys" not in self._stubs:
            self._stubs["list_ssh_keys"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListSSHKeys",
                request_serializer=ssh_key.ListSSHKeysRequest.serialize,
                response_deserializer=ssh_key.ListSSHKeysResponse.deserialize,
            )
        return self._stubs["list_ssh_keys"]

    @property
    def create_ssh_key(
        self,
    ) -> Callable[[gcb_ssh_key.CreateSSHKeyRequest], Awaitable[gcb_ssh_key.SSHKey]]:
        r"""Return a callable for the create ssh key method over gRPC.

        Register a public SSH key in the specified project
        for use with the interactive serial console feature.

        Returns:
            Callable[[~.CreateSSHKeyRequest],
                    Awaitable[~.SSHKey]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_ssh_key" not in self._stubs:
            self._stubs["create_ssh_key"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/CreateSSHKey",
                request_serializer=gcb_ssh_key.CreateSSHKeyRequest.serialize,
                response_deserializer=gcb_ssh_key.SSHKey.deserialize,
            )
        return self._stubs["create_ssh_key"]

    @property
    def delete_ssh_key(
        self,
    ) -> Callable[[ssh_key.DeleteSSHKeyRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete ssh key method over gRPC.

        Deletes a public SSH key registered in the specified
        project.

        Returns:
            Callable[[~.DeleteSSHKeyRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_ssh_key" not in self._stubs:
            self._stubs["delete_ssh_key"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/DeleteSSHKey",
                request_serializer=ssh_key.DeleteSSHKeyRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_ssh_key"]

    @property
    def list_volumes(
        self,
    ) -> Callable[[volume.ListVolumesRequest], Awaitable[volume.ListVolumesResponse]]:
        r"""Return a callable for the list volumes method over gRPC.

        List storage volumes in a given project and location.

        Returns:
            Callable[[~.ListVolumesRequest],
                    Awaitable[~.ListVolumesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_volumes" not in self._stubs:
            self._stubs["list_volumes"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListVolumes",
                request_serializer=volume.ListVolumesRequest.serialize,
                response_deserializer=volume.ListVolumesResponse.deserialize,
            )
        return self._stubs["list_volumes"]

    @property
    def get_volume(
        self,
    ) -> Callable[[volume.GetVolumeRequest], Awaitable[volume.Volume]]:
        r"""Return a callable for the get volume method over gRPC.

        Get details of a single storage volume.

        Returns:
            Callable[[~.GetVolumeRequest],
                    Awaitable[~.Volume]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_volume" not in self._stubs:
            self._stubs["get_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/GetVolume",
                request_serializer=volume.GetVolumeRequest.serialize,
                response_deserializer=volume.Volume.deserialize,
            )
        return self._stubs["get_volume"]

    @property
    def update_volume(
        self,
    ) -> Callable[
        [gcb_volume.UpdateVolumeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update volume method over gRPC.

        Update details of a single storage volume.

        Returns:
            Callable[[~.UpdateVolumeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_volume" not in self._stubs:
            self._stubs["update_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateVolume",
                request_serializer=gcb_volume.UpdateVolumeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_volume"]

    @property
    def rename_volume(
        self,
    ) -> Callable[[volume.RenameVolumeRequest], Awaitable[volume.Volume]]:
        r"""Return a callable for the rename volume method over gRPC.

        RenameVolume sets a new name for a volume.
        Use with caution, previous names become immediately
        invalidated.

        Returns:
            Callable[[~.RenameVolumeRequest],
                    Awaitable[~.Volume]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rename_volume" not in self._stubs:
            self._stubs["rename_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/RenameVolume",
                request_serializer=volume.RenameVolumeRequest.serialize,
                response_deserializer=volume.Volume.deserialize,
            )
        return self._stubs["rename_volume"]

    @property
    def evict_volume(
        self,
    ) -> Callable[[volume.EvictVolumeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the evict volume method over gRPC.

        Skips volume's cooloff and deletes it now.
        Volume must be in cooloff state.

        Returns:
            Callable[[~.EvictVolumeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "evict_volume" not in self._stubs:
            self._stubs["evict_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/EvictVolume",
                request_serializer=volume.EvictVolumeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["evict_volume"]

    @property
    def resize_volume(
        self,
    ) -> Callable[
        [gcb_volume.ResizeVolumeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the resize volume method over gRPC.

        Emergency Volume resize.

        Returns:
            Callable[[~.ResizeVolumeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "resize_volume" not in self._stubs:
            self._stubs["resize_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ResizeVolume",
                request_serializer=gcb_volume.ResizeVolumeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["resize_volume"]

    @property
    def list_networks(
        self,
    ) -> Callable[
        [network.ListNetworksRequest], Awaitable[network.ListNetworksResponse]
    ]:
        r"""Return a callable for the list networks method over gRPC.

        List network in a given project and location.

        Returns:
            Callable[[~.ListNetworksRequest],
                    Awaitable[~.ListNetworksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_networks" not in self._stubs:
            self._stubs["list_networks"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListNetworks",
                request_serializer=network.ListNetworksRequest.serialize,
                response_deserializer=network.ListNetworksResponse.deserialize,
            )
        return self._stubs["list_networks"]

    @property
    def list_network_usage(
        self,
    ) -> Callable[
        [network.ListNetworkUsageRequest], Awaitable[network.ListNetworkUsageResponse]
    ]:
        r"""Return a callable for the list network usage method over gRPC.

        List all Networks (and used IPs for each Network) in
        the vendor account associated with the specified
        project.

        Returns:
            Callable[[~.ListNetworkUsageRequest],
                    Awaitable[~.ListNetworkUsageResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_network_usage" not in self._stubs:
            self._stubs["list_network_usage"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListNetworkUsage",
                request_serializer=network.ListNetworkUsageRequest.serialize,
                response_deserializer=network.ListNetworkUsageResponse.deserialize,
            )
        return self._stubs["list_network_usage"]

    @property
    def get_network(
        self,
    ) -> Callable[[network.GetNetworkRequest], Awaitable[network.Network]]:
        r"""Return a callable for the get network method over gRPC.

        Get details of a single network.

        Returns:
            Callable[[~.GetNetworkRequest],
                    Awaitable[~.Network]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_network" not in self._stubs:
            self._stubs["get_network"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/GetNetwork",
                request_serializer=network.GetNetworkRequest.serialize,
                response_deserializer=network.Network.deserialize,
            )
        return self._stubs["get_network"]

    @property
    def update_network(
        self,
    ) -> Callable[
        [gcb_network.UpdateNetworkRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update network method over gRPC.

        Update details of a single network.

        Returns:
            Callable[[~.UpdateNetworkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_network" not in self._stubs:
            self._stubs["update_network"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateNetwork",
                request_serializer=gcb_network.UpdateNetworkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_network"]

    @property
    def create_volume_snapshot(
        self,
    ) -> Callable[
        [gcb_volume_snapshot.CreateVolumeSnapshotRequest],
        Awaitable[gcb_volume_snapshot.VolumeSnapshot],
    ]:
        r"""Return a callable for the create volume snapshot method over gRPC.

        Takes a snapshot of a boot volume. Returns INVALID_ARGUMENT if
        called for a non-boot volume.

        Returns:
            Callable[[~.CreateVolumeSnapshotRequest],
                    Awaitable[~.VolumeSnapshot]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_volume_snapshot" not in self._stubs:
            self._stubs["create_volume_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/CreateVolumeSnapshot",
                request_serializer=gcb_volume_snapshot.CreateVolumeSnapshotRequest.serialize,
                response_deserializer=gcb_volume_snapshot.VolumeSnapshot.deserialize,
            )
        return self._stubs["create_volume_snapshot"]

    @property
    def restore_volume_snapshot(
        self,
    ) -> Callable[
        [gcb_volume_snapshot.RestoreVolumeSnapshotRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the restore volume snapshot method over gRPC.

        Uses the specified snapshot to restore its parent volume.
        Returns INVALID_ARGUMENT if called for a non-boot volume.

        Returns:
            Callable[[~.RestoreVolumeSnapshotRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restore_volume_snapshot" not in self._stubs:
            self._stubs["restore_volume_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/RestoreVolumeSnapshot",
                request_serializer=gcb_volume_snapshot.RestoreVolumeSnapshotRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["restore_volume_snapshot"]

    @property
    def delete_volume_snapshot(
        self,
    ) -> Callable[
        [volume_snapshot.DeleteVolumeSnapshotRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete volume snapshot method over gRPC.

        Deletes a volume snapshot. Returns INVALID_ARGUMENT if called
        for a non-boot volume.

        Returns:
            Callable[[~.DeleteVolumeSnapshotRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_volume_snapshot" not in self._stubs:
            self._stubs["delete_volume_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/DeleteVolumeSnapshot",
                request_serializer=volume_snapshot.DeleteVolumeSnapshotRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_volume_snapshot"]

    @property
    def get_volume_snapshot(
        self,
    ) -> Callable[
        [volume_snapshot.GetVolumeSnapshotRequest],
        Awaitable[volume_snapshot.VolumeSnapshot],
    ]:
        r"""Return a callable for the get volume snapshot method over gRPC.

        Returns the specified snapshot resource. Returns
        INVALID_ARGUMENT if called for a non-boot volume.

        Returns:
            Callable[[~.GetVolumeSnapshotRequest],
                    Awaitable[~.VolumeSnapshot]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_volume_snapshot" not in self._stubs:
            self._stubs["get_volume_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/GetVolumeSnapshot",
                request_serializer=volume_snapshot.GetVolumeSnapshotRequest.serialize,
                response_deserializer=volume_snapshot.VolumeSnapshot.deserialize,
            )
        return self._stubs["get_volume_snapshot"]

    @property
    def list_volume_snapshots(
        self,
    ) -> Callable[
        [volume_snapshot.ListVolumeSnapshotsRequest],
        Awaitable[volume_snapshot.ListVolumeSnapshotsResponse],
    ]:
        r"""Return a callable for the list volume snapshots method over gRPC.

        Retrieves the list of snapshots for the specified
        volume. Returns a response with an empty list of
        snapshots if called for a non-boot volume.

        Returns:
            Callable[[~.ListVolumeSnapshotsRequest],
                    Awaitable[~.ListVolumeSnapshotsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_volume_snapshots" not in self._stubs:
            self._stubs["list_volume_snapshots"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListVolumeSnapshots",
                request_serializer=volume_snapshot.ListVolumeSnapshotsRequest.serialize,
                response_deserializer=volume_snapshot.ListVolumeSnapshotsResponse.deserialize,
            )
        return self._stubs["list_volume_snapshots"]

    @property
    def get_lun(self) -> Callable[[lun.GetLunRequest], Awaitable[lun.Lun]]:
        r"""Return a callable for the get lun method over gRPC.

        Get details of a single storage logical unit
        number(LUN).

        Returns:
            Callable[[~.GetLunRequest],
                    Awaitable[~.Lun]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_lun" not in self._stubs:
            self._stubs["get_lun"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/GetLun",
                request_serializer=lun.GetLunRequest.serialize,
                response_deserializer=lun.Lun.deserialize,
            )
        return self._stubs["get_lun"]

    @property
    def list_luns(
        self,
    ) -> Callable[[lun.ListLunsRequest], Awaitable[lun.ListLunsResponse]]:
        r"""Return a callable for the list luns method over gRPC.

        List storage volume luns for given storage volume.

        Returns:
            Callable[[~.ListLunsRequest],
                    Awaitable[~.ListLunsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_luns" not in self._stubs:
            self._stubs["list_luns"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListLuns",
                request_serializer=lun.ListLunsRequest.serialize,
                response_deserializer=lun.ListLunsResponse.deserialize,
            )
        return self._stubs["list_luns"]

    @property
    def evict_lun(
        self,
    ) -> Callable[[lun.EvictLunRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the evict lun method over gRPC.

        Skips lun's cooloff and deletes it now.
        Lun must be in cooloff state.

        Returns:
            Callable[[~.EvictLunRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "evict_lun" not in self._stubs:
            self._stubs["evict_lun"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/EvictLun",
                request_serializer=lun.EvictLunRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["evict_lun"]

    @property
    def get_nfs_share(
        self,
    ) -> Callable[[nfs_share.GetNfsShareRequest], Awaitable[nfs_share.NfsShare]]:
        r"""Return a callable for the get nfs share method over gRPC.

        Get details of a single NFS share.

        Returns:
            Callable[[~.GetNfsShareRequest],
                    Awaitable[~.NfsShare]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_nfs_share" not in self._stubs:
            self._stubs["get_nfs_share"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/GetNfsShare",
                request_serializer=nfs_share.GetNfsShareRequest.serialize,
                response_deserializer=nfs_share.NfsShare.deserialize,
            )
        return self._stubs["get_nfs_share"]

    @property
    def list_nfs_shares(
        self,
    ) -> Callable[
        [nfs_share.ListNfsSharesRequest], Awaitable[nfs_share.ListNfsSharesResponse]
    ]:
        r"""Return a callable for the list nfs shares method over gRPC.

        List NFS shares.

        Returns:
            Callable[[~.ListNfsSharesRequest],
                    Awaitable[~.ListNfsSharesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_nfs_shares" not in self._stubs:
            self._stubs["list_nfs_shares"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListNfsShares",
                request_serializer=nfs_share.ListNfsSharesRequest.serialize,
                response_deserializer=nfs_share.ListNfsSharesResponse.deserialize,
            )
        return self._stubs["list_nfs_shares"]

    @property
    def update_nfs_share(
        self,
    ) -> Callable[
        [gcb_nfs_share.UpdateNfsShareRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update nfs share method over gRPC.

        Update details of a single NFS share.

        Returns:
            Callable[[~.UpdateNfsShareRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_nfs_share" not in self._stubs:
            self._stubs["update_nfs_share"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateNfsShare",
                request_serializer=gcb_nfs_share.UpdateNfsShareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_nfs_share"]

    @property
    def create_nfs_share(
        self,
    ) -> Callable[
        [gcb_nfs_share.CreateNfsShareRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create nfs share method over gRPC.

        Create an NFS share.

        Returns:
            Callable[[~.CreateNfsShareRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_nfs_share" not in self._stubs:
            self._stubs["create_nfs_share"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/CreateNfsShare",
                request_serializer=gcb_nfs_share.CreateNfsShareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_nfs_share"]

    @property
    def rename_nfs_share(
        self,
    ) -> Callable[[nfs_share.RenameNfsShareRequest], Awaitable[nfs_share.NfsShare]]:
        r"""Return a callable for the rename nfs share method over gRPC.

        RenameNfsShare sets a new name for an nfsshare.
        Use with caution, previous names become immediately
        invalidated.

        Returns:
            Callable[[~.RenameNfsShareRequest],
                    Awaitable[~.NfsShare]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rename_nfs_share" not in self._stubs:
            self._stubs["rename_nfs_share"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/RenameNfsShare",
                request_serializer=nfs_share.RenameNfsShareRequest.serialize,
                response_deserializer=nfs_share.NfsShare.deserialize,
            )
        return self._stubs["rename_nfs_share"]

    @property
    def delete_nfs_share(
        self,
    ) -> Callable[
        [nfs_share.DeleteNfsShareRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete nfs share method over gRPC.

        Delete an NFS share. The underlying volume is
        automatically deleted.

        Returns:
            Callable[[~.DeleteNfsShareRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_nfs_share" not in self._stubs:
            self._stubs["delete_nfs_share"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/DeleteNfsShare",
                request_serializer=nfs_share.DeleteNfsShareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_nfs_share"]

    @property
    def list_provisioning_quotas(
        self,
    ) -> Callable[
        [provisioning.ListProvisioningQuotasRequest],
        Awaitable[provisioning.ListProvisioningQuotasResponse],
    ]:
        r"""Return a callable for the list provisioning quotas method over gRPC.

        List the budget details to provision resources on a
        given project.

        Returns:
            Callable[[~.ListProvisioningQuotasRequest],
                    Awaitable[~.ListProvisioningQuotasResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_provisioning_quotas" not in self._stubs:
            self._stubs["list_provisioning_quotas"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListProvisioningQuotas",
                request_serializer=provisioning.ListProvisioningQuotasRequest.serialize,
                response_deserializer=provisioning.ListProvisioningQuotasResponse.deserialize,
            )
        return self._stubs["list_provisioning_quotas"]

    @property
    def submit_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.SubmitProvisioningConfigRequest],
        Awaitable[provisioning.SubmitProvisioningConfigResponse],
    ]:
        r"""Return a callable for the submit provisioning config method over gRPC.

        Submit a provisiong configuration for a given
        project.

        Returns:
            Callable[[~.SubmitProvisioningConfigRequest],
                    Awaitable[~.SubmitProvisioningConfigResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "submit_provisioning_config" not in self._stubs:
            self._stubs["submit_provisioning_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.baremetalsolution.v2.BareMetalSolution/SubmitProvisioningConfig",
                    request_serializer=provisioning.SubmitProvisioningConfigRequest.serialize,
                    response_deserializer=provisioning.SubmitProvisioningConfigResponse.deserialize,
                )
            )
        return self._stubs["submit_provisioning_config"]

    @property
    def get_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.GetProvisioningConfigRequest],
        Awaitable[provisioning.ProvisioningConfig],
    ]:
        r"""Return a callable for the get provisioning config method over gRPC.

        Get ProvisioningConfig by name.

        Returns:
            Callable[[~.GetProvisioningConfigRequest],
                    Awaitable[~.ProvisioningConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_provisioning_config" not in self._stubs:
            self._stubs["get_provisioning_config"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/GetProvisioningConfig",
                request_serializer=provisioning.GetProvisioningConfigRequest.serialize,
                response_deserializer=provisioning.ProvisioningConfig.deserialize,
            )
        return self._stubs["get_provisioning_config"]

    @property
    def create_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.CreateProvisioningConfigRequest],
        Awaitable[provisioning.ProvisioningConfig],
    ]:
        r"""Return a callable for the create provisioning config method over gRPC.

        Create new ProvisioningConfig.

        Returns:
            Callable[[~.CreateProvisioningConfigRequest],
                    Awaitable[~.ProvisioningConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_provisioning_config" not in self._stubs:
            self._stubs["create_provisioning_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.baremetalsolution.v2.BareMetalSolution/CreateProvisioningConfig",
                    request_serializer=provisioning.CreateProvisioningConfigRequest.serialize,
                    response_deserializer=provisioning.ProvisioningConfig.deserialize,
                )
            )
        return self._stubs["create_provisioning_config"]

    @property
    def update_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.UpdateProvisioningConfigRequest],
        Awaitable[provisioning.ProvisioningConfig],
    ]:
        r"""Return a callable for the update provisioning config method over gRPC.

        Update existing ProvisioningConfig.

        Returns:
            Callable[[~.UpdateProvisioningConfigRequest],
                    Awaitable[~.ProvisioningConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_provisioning_config" not in self._stubs:
            self._stubs["update_provisioning_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateProvisioningConfig",
                    request_serializer=provisioning.UpdateProvisioningConfigRequest.serialize,
                    response_deserializer=provisioning.ProvisioningConfig.deserialize,
                )
            )
        return self._stubs["update_provisioning_config"]

    @property
    def rename_network(
        self,
    ) -> Callable[[network.RenameNetworkRequest], Awaitable[network.Network]]:
        r"""Return a callable for the rename network method over gRPC.

        RenameNetwork sets a new name for a network.
        Use with caution, previous names become immediately
        invalidated.

        Returns:
            Callable[[~.RenameNetworkRequest],
                    Awaitable[~.Network]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rename_network" not in self._stubs:
            self._stubs["rename_network"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/RenameNetwork",
                request_serializer=network.RenameNetworkRequest.serialize,
                response_deserializer=network.Network.deserialize,
            )
        return self._stubs["rename_network"]

    @property
    def list_os_images(
        self,
    ) -> Callable[
        [osimage.ListOSImagesRequest], Awaitable[osimage.ListOSImagesResponse]
    ]:
        r"""Return a callable for the list os images method over gRPC.

        Retrieves the list of OS images which are currently
        approved.

        Returns:
            Callable[[~.ListOSImagesRequest],
                    Awaitable[~.ListOSImagesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_os_images" not in self._stubs:
            self._stubs["list_os_images"] = self._logged_channel.unary_unary(
                "/google.cloud.baremetalsolution.v2.BareMetalSolution/ListOSImages",
                request_serializer=osimage.ListOSImagesRequest.serialize,
                response_deserializer=osimage.ListOSImagesResponse.deserialize,
            )
        return self._stubs["list_os_images"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
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
            self.update_instance: self._wrap_method(
                self.update_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_instance: self._wrap_method(
                self.rename_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_instance: self._wrap_method(
                self.reset_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_instance: self._wrap_method(
                self.start_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.stop_instance: self._wrap_method(
                self.stop_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enable_interactive_serial_console: self._wrap_method(
                self.enable_interactive_serial_console,
                default_timeout=None,
                client_info=client_info,
            ),
            self.disable_interactive_serial_console: self._wrap_method(
                self.disable_interactive_serial_console,
                default_timeout=None,
                client_info=client_info,
            ),
            self.detach_lun: self._wrap_method(
                self.detach_lun,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_ssh_keys: self._wrap_method(
                self.list_ssh_keys,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_ssh_key: self._wrap_method(
                self.create_ssh_key,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_ssh_key: self._wrap_method(
                self.delete_ssh_key,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_volumes: self._wrap_method(
                self.list_volumes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_volume: self._wrap_method(
                self.get_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_volume: self._wrap_method(
                self.update_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_volume: self._wrap_method(
                self.rename_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.evict_volume: self._wrap_method(
                self.evict_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.resize_volume: self._wrap_method(
                self.resize_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_networks: self._wrap_method(
                self.list_networks,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_network_usage: self._wrap_method(
                self.list_network_usage,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_network: self._wrap_method(
                self.get_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_network: self._wrap_method(
                self.update_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_volume_snapshot: self._wrap_method(
                self.create_volume_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_volume_snapshot: self._wrap_method(
                self.restore_volume_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_volume_snapshot: self._wrap_method(
                self.delete_volume_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_volume_snapshot: self._wrap_method(
                self.get_volume_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_volume_snapshots: self._wrap_method(
                self.list_volume_snapshots,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_lun: self._wrap_method(
                self.get_lun,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_luns: self._wrap_method(
                self.list_luns,
                default_timeout=None,
                client_info=client_info,
            ),
            self.evict_lun: self._wrap_method(
                self.evict_lun,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_nfs_share: self._wrap_method(
                self.get_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_nfs_shares: self._wrap_method(
                self.list_nfs_shares,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_nfs_share: self._wrap_method(
                self.update_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_nfs_share: self._wrap_method(
                self.create_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_nfs_share: self._wrap_method(
                self.rename_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_nfs_share: self._wrap_method(
                self.delete_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_provisioning_quotas: self._wrap_method(
                self.list_provisioning_quotas,
                default_timeout=None,
                client_info=client_info,
            ),
            self.submit_provisioning_config: self._wrap_method(
                self.submit_provisioning_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_provisioning_config: self._wrap_method(
                self.get_provisioning_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_provisioning_config: self._wrap_method(
                self.create_provisioning_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_provisioning_config: self._wrap_method(
                self.update_provisioning_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_network: self._wrap_method(
                self.rename_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_os_images: self._wrap_method(
                self.list_os_images,
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


__all__ = ("BareMetalSolutionGrpcAsyncIOTransport",)
