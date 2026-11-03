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

from google.cloud.apphub_v1.types import (
    apphub_service,
    application,
    boundary,
    extended_metadata_schema,
    service,
    service_project_attachment,
    workload,
)

from .base import DEFAULT_CLIENT_INFO, AppHubTransport
from .grpc import AppHubGrpcTransport

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
                    "serviceName": "google.cloud.apphub.v1.AppHub",
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
                    "serviceName": "google.cloud.apphub.v1.AppHub",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AppHubGrpcAsyncIOTransport(AppHubTransport):
    """gRPC AsyncIO backend transport for AppHub.

    The App Hub API allows you to manage App Hub resources.

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
        host: str = "apphub.googleapis.com",
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
        host: str = "apphub.googleapis.com",
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
                 The hostname to connect to (default: 'apphub.googleapis.com').
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
    def lookup_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.LookupServiceProjectAttachmentRequest],
        Awaitable[apphub_service.LookupServiceProjectAttachmentResponse],
    ]:
        r"""Return a callable for the lookup service project
        attachment method over gRPC.

        Lists a service project attachment for a given
        service project. You can call this API from any project
        to find if it is attached to a host project.

        Returns:
            Callable[[~.LookupServiceProjectAttachmentRequest],
                    Awaitable[~.LookupServiceProjectAttachmentResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_service_project_attachment" not in self._stubs:
            self._stubs["lookup_service_project_attachment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/LookupServiceProjectAttachment",
                    request_serializer=apphub_service.LookupServiceProjectAttachmentRequest.serialize,
                    response_deserializer=apphub_service.LookupServiceProjectAttachmentResponse.deserialize,
                )
            )
        return self._stubs["lookup_service_project_attachment"]

    @property
    def list_service_project_attachments(
        self,
    ) -> Callable[
        [apphub_service.ListServiceProjectAttachmentsRequest],
        Awaitable[apphub_service.ListServiceProjectAttachmentsResponse],
    ]:
        r"""Return a callable for the list service project
        attachments method over gRPC.

        Lists service projects attached to the host project.

        Returns:
            Callable[[~.ListServiceProjectAttachmentsRequest],
                    Awaitable[~.ListServiceProjectAttachmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_service_project_attachments" not in self._stubs:
            self._stubs["list_service_project_attachments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/ListServiceProjectAttachments",
                    request_serializer=apphub_service.ListServiceProjectAttachmentsRequest.serialize,
                    response_deserializer=apphub_service.ListServiceProjectAttachmentsResponse.deserialize,
                )
            )
        return self._stubs["list_service_project_attachments"]

    @property
    def create_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.CreateServiceProjectAttachmentRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create service project
        attachment method over gRPC.

        Attaches a service project to the host project.

        Returns:
            Callable[[~.CreateServiceProjectAttachmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_service_project_attachment" not in self._stubs:
            self._stubs["create_service_project_attachment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/CreateServiceProjectAttachment",
                    request_serializer=apphub_service.CreateServiceProjectAttachmentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_service_project_attachment"]

    @property
    def get_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.GetServiceProjectAttachmentRequest],
        Awaitable[service_project_attachment.ServiceProjectAttachment],
    ]:
        r"""Return a callable for the get service project attachment method over gRPC.

        Gets a service project attachment.

        Returns:
            Callable[[~.GetServiceProjectAttachmentRequest],
                    Awaitable[~.ServiceProjectAttachment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_service_project_attachment" not in self._stubs:
            self._stubs["get_service_project_attachment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/GetServiceProjectAttachment",
                    request_serializer=apphub_service.GetServiceProjectAttachmentRequest.serialize,
                    response_deserializer=service_project_attachment.ServiceProjectAttachment.deserialize,
                )
            )
        return self._stubs["get_service_project_attachment"]

    @property
    def delete_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.DeleteServiceProjectAttachmentRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete service project
        attachment method over gRPC.

        Deletes a service project attachment.

        Returns:
            Callable[[~.DeleteServiceProjectAttachmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_service_project_attachment" not in self._stubs:
            self._stubs["delete_service_project_attachment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/DeleteServiceProjectAttachment",
                    request_serializer=apphub_service.DeleteServiceProjectAttachmentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_service_project_attachment"]

    @property
    def detach_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.DetachServiceProjectAttachmentRequest],
        Awaitable[apphub_service.DetachServiceProjectAttachmentResponse],
    ]:
        r"""Return a callable for the detach service project
        attachment method over gRPC.

        Detaches a service project from a host project.
        You can call this API from any service project without
        needing access to the host project that it is attached
        to.

        Returns:
            Callable[[~.DetachServiceProjectAttachmentRequest],
                    Awaitable[~.DetachServiceProjectAttachmentResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "detach_service_project_attachment" not in self._stubs:
            self._stubs["detach_service_project_attachment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/DetachServiceProjectAttachment",
                    request_serializer=apphub_service.DetachServiceProjectAttachmentRequest.serialize,
                    response_deserializer=apphub_service.DetachServiceProjectAttachmentResponse.deserialize,
                )
            )
        return self._stubs["detach_service_project_attachment"]

    @property
    def list_discovered_services(
        self,
    ) -> Callable[
        [apphub_service.ListDiscoveredServicesRequest],
        Awaitable[apphub_service.ListDiscoveredServicesResponse],
    ]:
        r"""Return a callable for the list discovered services method over gRPC.

        Lists Discovered Services that can be added to an
        Application in a host project and location.

        Returns:
            Callable[[~.ListDiscoveredServicesRequest],
                    Awaitable[~.ListDiscoveredServicesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_discovered_services" not in self._stubs:
            self._stubs["list_discovered_services"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/ListDiscoveredServices",
                request_serializer=apphub_service.ListDiscoveredServicesRequest.serialize,
                response_deserializer=apphub_service.ListDiscoveredServicesResponse.deserialize,
            )
        return self._stubs["list_discovered_services"]

    @property
    def get_discovered_service(
        self,
    ) -> Callable[
        [apphub_service.GetDiscoveredServiceRequest],
        Awaitable[service.DiscoveredService],
    ]:
        r"""Return a callable for the get discovered service method over gRPC.

        Gets a Discovered Service in a host project and
        location.

        Returns:
            Callable[[~.GetDiscoveredServiceRequest],
                    Awaitable[~.DiscoveredService]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_discovered_service" not in self._stubs:
            self._stubs["get_discovered_service"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/GetDiscoveredService",
                request_serializer=apphub_service.GetDiscoveredServiceRequest.serialize,
                response_deserializer=service.DiscoveredService.deserialize,
            )
        return self._stubs["get_discovered_service"]

    @property
    def lookup_discovered_service(
        self,
    ) -> Callable[
        [apphub_service.LookupDiscoveredServiceRequest],
        Awaitable[apphub_service.LookupDiscoveredServiceResponse],
    ]:
        r"""Return a callable for the lookup discovered service method over gRPC.

        Lists a Discovered Service in a host project and
        location, with a given resource URI.

        Returns:
            Callable[[~.LookupDiscoveredServiceRequest],
                    Awaitable[~.LookupDiscoveredServiceResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_discovered_service" not in self._stubs:
            self._stubs["lookup_discovered_service"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/LookupDiscoveredService",
                request_serializer=apphub_service.LookupDiscoveredServiceRequest.serialize,
                response_deserializer=apphub_service.LookupDiscoveredServiceResponse.deserialize,
            )
        return self._stubs["lookup_discovered_service"]

    @property
    def list_services(
        self,
    ) -> Callable[
        [apphub_service.ListServicesRequest],
        Awaitable[apphub_service.ListServicesResponse],
    ]:
        r"""Return a callable for the list services method over gRPC.

        Lists Services in an Application.

        Returns:
            Callable[[~.ListServicesRequest],
                    Awaitable[~.ListServicesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_services" not in self._stubs:
            self._stubs["list_services"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/ListServices",
                request_serializer=apphub_service.ListServicesRequest.serialize,
                response_deserializer=apphub_service.ListServicesResponse.deserialize,
            )
        return self._stubs["list_services"]

    @property
    def create_service(
        self,
    ) -> Callable[
        [apphub_service.CreateServiceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create service method over gRPC.

        Creates a Service in an Application.

        Returns:
            Callable[[~.CreateServiceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_service" not in self._stubs:
            self._stubs["create_service"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/CreateService",
                request_serializer=apphub_service.CreateServiceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_service"]

    @property
    def get_service(
        self,
    ) -> Callable[[apphub_service.GetServiceRequest], Awaitable[service.Service]]:
        r"""Return a callable for the get service method over gRPC.

        Gets a Service in an Application.

        Returns:
            Callable[[~.GetServiceRequest],
                    Awaitable[~.Service]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_service" not in self._stubs:
            self._stubs["get_service"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/GetService",
                request_serializer=apphub_service.GetServiceRequest.serialize,
                response_deserializer=service.Service.deserialize,
            )
        return self._stubs["get_service"]

    @property
    def update_service(
        self,
    ) -> Callable[
        [apphub_service.UpdateServiceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update service method over gRPC.

        Updates a Service in an Application.

        Returns:
            Callable[[~.UpdateServiceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_service" not in self._stubs:
            self._stubs["update_service"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/UpdateService",
                request_serializer=apphub_service.UpdateServiceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_service"]

    @property
    def delete_service(
        self,
    ) -> Callable[
        [apphub_service.DeleteServiceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete service method over gRPC.

        Deletes a Service from an Application.

        Returns:
            Callable[[~.DeleteServiceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_service" not in self._stubs:
            self._stubs["delete_service"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/DeleteService",
                request_serializer=apphub_service.DeleteServiceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_service"]

    @property
    def list_discovered_workloads(
        self,
    ) -> Callable[
        [apphub_service.ListDiscoveredWorkloadsRequest],
        Awaitable[apphub_service.ListDiscoveredWorkloadsResponse],
    ]:
        r"""Return a callable for the list discovered workloads method over gRPC.

        Lists Discovered Workloads that can be added to an
        Application in a host project and location.

        Returns:
            Callable[[~.ListDiscoveredWorkloadsRequest],
                    Awaitable[~.ListDiscoveredWorkloadsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_discovered_workloads" not in self._stubs:
            self._stubs["list_discovered_workloads"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/ListDiscoveredWorkloads",
                request_serializer=apphub_service.ListDiscoveredWorkloadsRequest.serialize,
                response_deserializer=apphub_service.ListDiscoveredWorkloadsResponse.deserialize,
            )
        return self._stubs["list_discovered_workloads"]

    @property
    def get_discovered_workload(
        self,
    ) -> Callable[
        [apphub_service.GetDiscoveredWorkloadRequest],
        Awaitable[workload.DiscoveredWorkload],
    ]:
        r"""Return a callable for the get discovered workload method over gRPC.

        Gets a Discovered Workload in a host project and
        location.

        Returns:
            Callable[[~.GetDiscoveredWorkloadRequest],
                    Awaitable[~.DiscoveredWorkload]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_discovered_workload" not in self._stubs:
            self._stubs["get_discovered_workload"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/GetDiscoveredWorkload",
                request_serializer=apphub_service.GetDiscoveredWorkloadRequest.serialize,
                response_deserializer=workload.DiscoveredWorkload.deserialize,
            )
        return self._stubs["get_discovered_workload"]

    @property
    def lookup_discovered_workload(
        self,
    ) -> Callable[
        [apphub_service.LookupDiscoveredWorkloadRequest],
        Awaitable[apphub_service.LookupDiscoveredWorkloadResponse],
    ]:
        r"""Return a callable for the lookup discovered workload method over gRPC.

        Lists a Discovered Workload in a host project and
        location, with a given resource URI.

        Returns:
            Callable[[~.LookupDiscoveredWorkloadRequest],
                    Awaitable[~.LookupDiscoveredWorkloadResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_discovered_workload" not in self._stubs:
            self._stubs["lookup_discovered_workload"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/LookupDiscoveredWorkload",
                    request_serializer=apphub_service.LookupDiscoveredWorkloadRequest.serialize,
                    response_deserializer=apphub_service.LookupDiscoveredWorkloadResponse.deserialize,
                )
            )
        return self._stubs["lookup_discovered_workload"]

    @property
    def list_workloads(
        self,
    ) -> Callable[
        [apphub_service.ListWorkloadsRequest],
        Awaitable[apphub_service.ListWorkloadsResponse],
    ]:
        r"""Return a callable for the list workloads method over gRPC.

        Lists Workloads in an Application.

        Returns:
            Callable[[~.ListWorkloadsRequest],
                    Awaitable[~.ListWorkloadsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_workloads" not in self._stubs:
            self._stubs["list_workloads"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/ListWorkloads",
                request_serializer=apphub_service.ListWorkloadsRequest.serialize,
                response_deserializer=apphub_service.ListWorkloadsResponse.deserialize,
            )
        return self._stubs["list_workloads"]

    @property
    def create_workload(
        self,
    ) -> Callable[
        [apphub_service.CreateWorkloadRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create workload method over gRPC.

        Creates a Workload in an Application.

        Returns:
            Callable[[~.CreateWorkloadRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_workload" not in self._stubs:
            self._stubs["create_workload"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/CreateWorkload",
                request_serializer=apphub_service.CreateWorkloadRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_workload"]

    @property
    def get_workload(
        self,
    ) -> Callable[[apphub_service.GetWorkloadRequest], Awaitable[workload.Workload]]:
        r"""Return a callable for the get workload method over gRPC.

        Gets a Workload in an Application.

        Returns:
            Callable[[~.GetWorkloadRequest],
                    Awaitable[~.Workload]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_workload" not in self._stubs:
            self._stubs["get_workload"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/GetWorkload",
                request_serializer=apphub_service.GetWorkloadRequest.serialize,
                response_deserializer=workload.Workload.deserialize,
            )
        return self._stubs["get_workload"]

    @property
    def update_workload(
        self,
    ) -> Callable[
        [apphub_service.UpdateWorkloadRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update workload method over gRPC.

        Updates a Workload in an Application.

        Returns:
            Callable[[~.UpdateWorkloadRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_workload" not in self._stubs:
            self._stubs["update_workload"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/UpdateWorkload",
                request_serializer=apphub_service.UpdateWorkloadRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_workload"]

    @property
    def delete_workload(
        self,
    ) -> Callable[
        [apphub_service.DeleteWorkloadRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete workload method over gRPC.

        Deletes a Workload from an Application.

        Returns:
            Callable[[~.DeleteWorkloadRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_workload" not in self._stubs:
            self._stubs["delete_workload"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/DeleteWorkload",
                request_serializer=apphub_service.DeleteWorkloadRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_workload"]

    @property
    def list_applications(
        self,
    ) -> Callable[
        [apphub_service.ListApplicationsRequest],
        Awaitable[apphub_service.ListApplicationsResponse],
    ]:
        r"""Return a callable for the list applications method over gRPC.

        Lists Applications in a host project and location.

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
                "/google.cloud.apphub.v1.AppHub/ListApplications",
                request_serializer=apphub_service.ListApplicationsRequest.serialize,
                response_deserializer=apphub_service.ListApplicationsResponse.deserialize,
            )
        return self._stubs["list_applications"]

    @property
    def create_application(
        self,
    ) -> Callable[
        [apphub_service.CreateApplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create application method over gRPC.

        Creates an Application in a host project and
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
                "/google.cloud.apphub.v1.AppHub/CreateApplication",
                request_serializer=apphub_service.CreateApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_application"]

    @property
    def get_application(
        self,
    ) -> Callable[
        [apphub_service.GetApplicationRequest], Awaitable[application.Application]
    ]:
        r"""Return a callable for the get application method over gRPC.

        Gets an Application in a host project and location.

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
                "/google.cloud.apphub.v1.AppHub/GetApplication",
                request_serializer=apphub_service.GetApplicationRequest.serialize,
                response_deserializer=application.Application.deserialize,
            )
        return self._stubs["get_application"]

    @property
    def update_application(
        self,
    ) -> Callable[
        [apphub_service.UpdateApplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update application method over gRPC.

        Updates an Application in a host project and
        location.

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
                "/google.cloud.apphub.v1.AppHub/UpdateApplication",
                request_serializer=apphub_service.UpdateApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_application"]

    @property
    def delete_application(
        self,
    ) -> Callable[
        [apphub_service.DeleteApplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete application method over gRPC.

        Deletes an Application in a host project and
        location.

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
                "/google.cloud.apphub.v1.AppHub/DeleteApplication",
                request_serializer=apphub_service.DeleteApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_application"]

    @property
    def get_boundary(
        self,
    ) -> Callable[[apphub_service.GetBoundaryRequest], Awaitable[boundary.Boundary]]:
        r"""Return a callable for the get boundary method over gRPC.

        Gets a Boundary.

        Returns:
            Callable[[~.GetBoundaryRequest],
                    Awaitable[~.Boundary]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_boundary" not in self._stubs:
            self._stubs["get_boundary"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/GetBoundary",
                request_serializer=apphub_service.GetBoundaryRequest.serialize,
                response_deserializer=boundary.Boundary.deserialize,
            )
        return self._stubs["get_boundary"]

    @property
    def update_boundary(
        self,
    ) -> Callable[
        [apphub_service.UpdateBoundaryRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update boundary method over gRPC.

        Updates a Boundary.

        Returns:
            Callable[[~.UpdateBoundaryRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_boundary" not in self._stubs:
            self._stubs["update_boundary"] = self._logged_channel.unary_unary(
                "/google.cloud.apphub.v1.AppHub/UpdateBoundary",
                request_serializer=apphub_service.UpdateBoundaryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_boundary"]

    @property
    def get_extended_metadata_schema(
        self,
    ) -> Callable[
        [apphub_service.GetExtendedMetadataSchemaRequest],
        Awaitable[extended_metadata_schema.ExtendedMetadataSchema],
    ]:
        r"""Return a callable for the get extended metadata schema method over gRPC.

        Gets an Extended Metadata Schema.

        Returns:
            Callable[[~.GetExtendedMetadataSchemaRequest],
                    Awaitable[~.ExtendedMetadataSchema]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_extended_metadata_schema" not in self._stubs:
            self._stubs["get_extended_metadata_schema"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/GetExtendedMetadataSchema",
                    request_serializer=apphub_service.GetExtendedMetadataSchemaRequest.serialize,
                    response_deserializer=extended_metadata_schema.ExtendedMetadataSchema.deserialize,
                )
            )
        return self._stubs["get_extended_metadata_schema"]

    @property
    def list_extended_metadata_schemas(
        self,
    ) -> Callable[
        [apphub_service.ListExtendedMetadataSchemasRequest],
        Awaitable[apphub_service.ListExtendedMetadataSchemasResponse],
    ]:
        r"""Return a callable for the list extended metadata schemas method over gRPC.

        Lists Extended Metadata Schemas available in a host
        project and location.

        Returns:
            Callable[[~.ListExtendedMetadataSchemasRequest],
                    Awaitable[~.ListExtendedMetadataSchemasResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_extended_metadata_schemas" not in self._stubs:
            self._stubs["list_extended_metadata_schemas"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.apphub.v1.AppHub/ListExtendedMetadataSchemas",
                    request_serializer=apphub_service.ListExtendedMetadataSchemasRequest.serialize,
                    response_deserializer=apphub_service.ListExtendedMetadataSchemasResponse.deserialize,
                )
            )
        return self._stubs["list_extended_metadata_schemas"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.lookup_service_project_attachment: self._wrap_method(
                self.lookup_service_project_attachment,
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
            self.list_service_project_attachments: self._wrap_method(
                self.list_service_project_attachments,
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
            self.create_service_project_attachment: self._wrap_method(
                self.create_service_project_attachment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_service_project_attachment: self._wrap_method(
                self.get_service_project_attachment,
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
            self.delete_service_project_attachment: self._wrap_method(
                self.delete_service_project_attachment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.detach_service_project_attachment: self._wrap_method(
                self.detach_service_project_attachment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_discovered_services: self._wrap_method(
                self.list_discovered_services,
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
            self.get_discovered_service: self._wrap_method(
                self.get_discovered_service,
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
            self.lookup_discovered_service: self._wrap_method(
                self.lookup_discovered_service,
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
            self.list_services: self._wrap_method(
                self.list_services,
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
            self.create_service: self._wrap_method(
                self.create_service,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_service: self._wrap_method(
                self.get_service,
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
            self.update_service: self._wrap_method(
                self.update_service,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_service: self._wrap_method(
                self.delete_service,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_discovered_workloads: self._wrap_method(
                self.list_discovered_workloads,
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
            self.get_discovered_workload: self._wrap_method(
                self.get_discovered_workload,
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
            self.lookup_discovered_workload: self._wrap_method(
                self.lookup_discovered_workload,
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
            self.list_workloads: self._wrap_method(
                self.list_workloads,
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
            self.create_workload: self._wrap_method(
                self.create_workload,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_workload: self._wrap_method(
                self.get_workload,
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
            self.update_workload: self._wrap_method(
                self.update_workload,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_workload: self._wrap_method(
                self.delete_workload,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_applications: self._wrap_method(
                self.list_applications,
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
            self.create_application: self._wrap_method(
                self.create_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_application: self._wrap_method(
                self.get_application,
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
            self.update_application: self._wrap_method(
                self.update_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_application: self._wrap_method(
                self.delete_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_boundary: self._wrap_method(
                self.get_boundary,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_boundary: self._wrap_method(
                self.update_boundary,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_extended_metadata_schema: self._wrap_method(
                self.get_extended_metadata_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_extended_metadata_schemas: self._wrap_method(
                self.list_extended_metadata_schemas,
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


__all__ = ("AppHubGrpcAsyncIOTransport",)
