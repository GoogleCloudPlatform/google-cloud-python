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

from google.cloud.dataplex_v1.types import catalog

from .base import DEFAULT_CLIENT_INFO, CatalogServiceTransport
from .grpc import CatalogServiceGrpcTransport

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
                    "serviceName": "google.cloud.dataplex.v1.CatalogService",
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
                    "serviceName": "google.cloud.dataplex.v1.CatalogService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class CatalogServiceGrpcAsyncIOTransport(CatalogServiceTransport):
    """gRPC AsyncIO backend transport for CatalogService.

    The primary resources offered by this service are
    EntryGroups, EntryTypes, AspectTypes, Entries and EntryLinks.
    They collectively let data administrators organize, manage,
    secure, and catalog data located across cloud projects in their
    organization in a variety of storage systems, including Cloud
    Storage and BigQuery.

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
        host: str = "dataplex.googleapis.com",
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
        host: str = "dataplex.googleapis.com",
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
                 The hostname to connect to (default: 'dataplex.googleapis.com').
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
    def create_entry_type(
        self,
    ) -> Callable[
        [catalog.CreateEntryTypeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create entry type method over gRPC.

        Creates an EntryType.

        Returns:
            Callable[[~.CreateEntryTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entry_type" not in self._stubs:
            self._stubs["create_entry_type"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/CreateEntryType",
                request_serializer=catalog.CreateEntryTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_entry_type"]

    @property
    def update_entry_type(
        self,
    ) -> Callable[
        [catalog.UpdateEntryTypeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update entry type method over gRPC.

        Updates an EntryType.

        Returns:
            Callable[[~.UpdateEntryTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entry_type" not in self._stubs:
            self._stubs["update_entry_type"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/UpdateEntryType",
                request_serializer=catalog.UpdateEntryTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_entry_type"]

    @property
    def delete_entry_type(
        self,
    ) -> Callable[
        [catalog.DeleteEntryTypeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete entry type method over gRPC.

        Deletes an EntryType.

        Returns:
            Callable[[~.DeleteEntryTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entry_type" not in self._stubs:
            self._stubs["delete_entry_type"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/DeleteEntryType",
                request_serializer=catalog.DeleteEntryTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_entry_type"]

    @property
    def list_entry_types(
        self,
    ) -> Callable[
        [catalog.ListEntryTypesRequest], Awaitable[catalog.ListEntryTypesResponse]
    ]:
        r"""Return a callable for the list entry types method over gRPC.

        Lists EntryType resources in a project and location.

        Returns:
            Callable[[~.ListEntryTypesRequest],
                    Awaitable[~.ListEntryTypesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entry_types" not in self._stubs:
            self._stubs["list_entry_types"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/ListEntryTypes",
                request_serializer=catalog.ListEntryTypesRequest.serialize,
                response_deserializer=catalog.ListEntryTypesResponse.deserialize,
            )
        return self._stubs["list_entry_types"]

    @property
    def get_entry_type(
        self,
    ) -> Callable[[catalog.GetEntryTypeRequest], Awaitable[catalog.EntryType]]:
        r"""Return a callable for the get entry type method over gRPC.

        Gets an EntryType.

        Returns:
            Callable[[~.GetEntryTypeRequest],
                    Awaitable[~.EntryType]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entry_type" not in self._stubs:
            self._stubs["get_entry_type"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/GetEntryType",
                request_serializer=catalog.GetEntryTypeRequest.serialize,
                response_deserializer=catalog.EntryType.deserialize,
            )
        return self._stubs["get_entry_type"]

    @property
    def create_aspect_type(
        self,
    ) -> Callable[
        [catalog.CreateAspectTypeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create aspect type method over gRPC.

        Creates an AspectType.

        Returns:
            Callable[[~.CreateAspectTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_aspect_type" not in self._stubs:
            self._stubs["create_aspect_type"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/CreateAspectType",
                request_serializer=catalog.CreateAspectTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_aspect_type"]

    @property
    def update_aspect_type(
        self,
    ) -> Callable[
        [catalog.UpdateAspectTypeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update aspect type method over gRPC.

        Updates an AspectType.

        Returns:
            Callable[[~.UpdateAspectTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_aspect_type" not in self._stubs:
            self._stubs["update_aspect_type"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/UpdateAspectType",
                request_serializer=catalog.UpdateAspectTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_aspect_type"]

    @property
    def delete_aspect_type(
        self,
    ) -> Callable[
        [catalog.DeleteAspectTypeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete aspect type method over gRPC.

        Deletes an AspectType.

        Returns:
            Callable[[~.DeleteAspectTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_aspect_type" not in self._stubs:
            self._stubs["delete_aspect_type"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/DeleteAspectType",
                request_serializer=catalog.DeleteAspectTypeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_aspect_type"]

    @property
    def list_aspect_types(
        self,
    ) -> Callable[
        [catalog.ListAspectTypesRequest], Awaitable[catalog.ListAspectTypesResponse]
    ]:
        r"""Return a callable for the list aspect types method over gRPC.

        Lists AspectType resources in a project and location.

        Returns:
            Callable[[~.ListAspectTypesRequest],
                    Awaitable[~.ListAspectTypesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_aspect_types" not in self._stubs:
            self._stubs["list_aspect_types"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/ListAspectTypes",
                request_serializer=catalog.ListAspectTypesRequest.serialize,
                response_deserializer=catalog.ListAspectTypesResponse.deserialize,
            )
        return self._stubs["list_aspect_types"]

    @property
    def get_aspect_type(
        self,
    ) -> Callable[[catalog.GetAspectTypeRequest], Awaitable[catalog.AspectType]]:
        r"""Return a callable for the get aspect type method over gRPC.

        Gets an AspectType.

        Returns:
            Callable[[~.GetAspectTypeRequest],
                    Awaitable[~.AspectType]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_aspect_type" not in self._stubs:
            self._stubs["get_aspect_type"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/GetAspectType",
                request_serializer=catalog.GetAspectTypeRequest.serialize,
                response_deserializer=catalog.AspectType.deserialize,
            )
        return self._stubs["get_aspect_type"]

    @property
    def create_entry_group(
        self,
    ) -> Callable[
        [catalog.CreateEntryGroupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create entry group method over gRPC.

        Creates an EntryGroup.

        Returns:
            Callable[[~.CreateEntryGroupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entry_group" not in self._stubs:
            self._stubs["create_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/CreateEntryGroup",
                request_serializer=catalog.CreateEntryGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_entry_group"]

    @property
    def update_entry_group(
        self,
    ) -> Callable[
        [catalog.UpdateEntryGroupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update entry group method over gRPC.

        Updates an EntryGroup.

        Returns:
            Callable[[~.UpdateEntryGroupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entry_group" not in self._stubs:
            self._stubs["update_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/UpdateEntryGroup",
                request_serializer=catalog.UpdateEntryGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_entry_group"]

    @property
    def delete_entry_group(
        self,
    ) -> Callable[
        [catalog.DeleteEntryGroupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete entry group method over gRPC.

        Deletes an EntryGroup.

        Returns:
            Callable[[~.DeleteEntryGroupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entry_group" not in self._stubs:
            self._stubs["delete_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/DeleteEntryGroup",
                request_serializer=catalog.DeleteEntryGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_entry_group"]

    @property
    def list_entry_groups(
        self,
    ) -> Callable[
        [catalog.ListEntryGroupsRequest], Awaitable[catalog.ListEntryGroupsResponse]
    ]:
        r"""Return a callable for the list entry groups method over gRPC.

        Lists EntryGroup resources in a project and location.

        Returns:
            Callable[[~.ListEntryGroupsRequest],
                    Awaitable[~.ListEntryGroupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entry_groups" not in self._stubs:
            self._stubs["list_entry_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/ListEntryGroups",
                request_serializer=catalog.ListEntryGroupsRequest.serialize,
                response_deserializer=catalog.ListEntryGroupsResponse.deserialize,
            )
        return self._stubs["list_entry_groups"]

    @property
    def get_entry_group(
        self,
    ) -> Callable[[catalog.GetEntryGroupRequest], Awaitable[catalog.EntryGroup]]:
        r"""Return a callable for the get entry group method over gRPC.

        Gets an EntryGroup.

        Returns:
            Callable[[~.GetEntryGroupRequest],
                    Awaitable[~.EntryGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entry_group" not in self._stubs:
            self._stubs["get_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/GetEntryGroup",
                request_serializer=catalog.GetEntryGroupRequest.serialize,
                response_deserializer=catalog.EntryGroup.deserialize,
            )
        return self._stubs["get_entry_group"]

    @property
    def create_entry(
        self,
    ) -> Callable[[catalog.CreateEntryRequest], Awaitable[catalog.Entry]]:
        r"""Return a callable for the create entry method over gRPC.

        Creates an Entry.

        Returns:
            Callable[[~.CreateEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entry" not in self._stubs:
            self._stubs["create_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/CreateEntry",
                request_serializer=catalog.CreateEntryRequest.serialize,
                response_deserializer=catalog.Entry.deserialize,
            )
        return self._stubs["create_entry"]

    @property
    def update_entry(
        self,
    ) -> Callable[[catalog.UpdateEntryRequest], Awaitable[catalog.Entry]]:
        r"""Return a callable for the update entry method over gRPC.

        Updates an Entry.

        Returns:
            Callable[[~.UpdateEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entry" not in self._stubs:
            self._stubs["update_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/UpdateEntry",
                request_serializer=catalog.UpdateEntryRequest.serialize,
                response_deserializer=catalog.Entry.deserialize,
            )
        return self._stubs["update_entry"]

    @property
    def delete_entry(
        self,
    ) -> Callable[[catalog.DeleteEntryRequest], Awaitable[catalog.Entry]]:
        r"""Return a callable for the delete entry method over gRPC.

        Deletes an Entry.

        Returns:
            Callable[[~.DeleteEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entry" not in self._stubs:
            self._stubs["delete_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/DeleteEntry",
                request_serializer=catalog.DeleteEntryRequest.serialize,
                response_deserializer=catalog.Entry.deserialize,
            )
        return self._stubs["delete_entry"]

    @property
    def list_entries(
        self,
    ) -> Callable[[catalog.ListEntriesRequest], Awaitable[catalog.ListEntriesResponse]]:
        r"""Return a callable for the list entries method over gRPC.

        Lists Entries within an EntryGroup.

        Returns:
            Callable[[~.ListEntriesRequest],
                    Awaitable[~.ListEntriesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entries" not in self._stubs:
            self._stubs["list_entries"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/ListEntries",
                request_serializer=catalog.ListEntriesRequest.serialize,
                response_deserializer=catalog.ListEntriesResponse.deserialize,
            )
        return self._stubs["list_entries"]

    @property
    def get_entry(
        self,
    ) -> Callable[[catalog.GetEntryRequest], Awaitable[catalog.Entry]]:
        r"""Return a callable for the get entry method over gRPC.

        Gets an Entry.

        Returns:
            Callable[[~.GetEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entry" not in self._stubs:
            self._stubs["get_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/GetEntry",
                request_serializer=catalog.GetEntryRequest.serialize,
                response_deserializer=catalog.Entry.deserialize,
            )
        return self._stubs["get_entry"]

    @property
    def lookup_entry(
        self,
    ) -> Callable[[catalog.LookupEntryRequest], Awaitable[catalog.Entry]]:
        r"""Return a callable for the lookup entry method over gRPC.

        Looks up an entry by name using the permission on the
        source system.

        Returns:
            Callable[[~.LookupEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_entry" not in self._stubs:
            self._stubs["lookup_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/LookupEntry",
                request_serializer=catalog.LookupEntryRequest.serialize,
                response_deserializer=catalog.Entry.deserialize,
            )
        return self._stubs["lookup_entry"]

    @property
    def modify_entry(
        self,
    ) -> Callable[[catalog.ModifyEntryRequest], Awaitable[catalog.Entry]]:
        r"""Return a callable for the modify entry method over gRPC.

        Modifies an entry using the permission on the source
        system.

        Returns:
            Callable[[~.ModifyEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "modify_entry" not in self._stubs:
            self._stubs["modify_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/ModifyEntry",
                request_serializer=catalog.ModifyEntryRequest.serialize,
                response_deserializer=catalog.Entry.deserialize,
            )
        return self._stubs["modify_entry"]

    @property
    def search_entries(
        self,
    ) -> Callable[
        [catalog.SearchEntriesRequest], Awaitable[catalog.SearchEntriesResponse]
    ]:
        r"""Return a callable for the search entries method over gRPC.

        Searches for Entries matching the given query and
        scope.

        Returns:
            Callable[[~.SearchEntriesRequest],
                    Awaitable[~.SearchEntriesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_entries" not in self._stubs:
            self._stubs["search_entries"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/SearchEntries",
                request_serializer=catalog.SearchEntriesRequest.serialize,
                response_deserializer=catalog.SearchEntriesResponse.deserialize,
            )
        return self._stubs["search_entries"]

    @property
    def create_metadata_job(
        self,
    ) -> Callable[
        [catalog.CreateMetadataJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create metadata job method over gRPC.

        Creates a metadata job. For example, use a metadata
        job to import metadata from a third-party system into
        Dataplex Universal Catalog.

        Returns:
            Callable[[~.CreateMetadataJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_metadata_job" not in self._stubs:
            self._stubs["create_metadata_job"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/CreateMetadataJob",
                request_serializer=catalog.CreateMetadataJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_metadata_job"]

    @property
    def get_metadata_job(
        self,
    ) -> Callable[[catalog.GetMetadataJobRequest], Awaitable[catalog.MetadataJob]]:
        r"""Return a callable for the get metadata job method over gRPC.

        Gets a metadata job.

        Returns:
            Callable[[~.GetMetadataJobRequest],
                    Awaitable[~.MetadataJob]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_metadata_job" not in self._stubs:
            self._stubs["get_metadata_job"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/GetMetadataJob",
                request_serializer=catalog.GetMetadataJobRequest.serialize,
                response_deserializer=catalog.MetadataJob.deserialize,
            )
        return self._stubs["get_metadata_job"]

    @property
    def list_metadata_jobs(
        self,
    ) -> Callable[
        [catalog.ListMetadataJobsRequest], Awaitable[catalog.ListMetadataJobsResponse]
    ]:
        r"""Return a callable for the list metadata jobs method over gRPC.

        Lists metadata jobs.

        Returns:
            Callable[[~.ListMetadataJobsRequest],
                    Awaitable[~.ListMetadataJobsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_metadata_jobs" not in self._stubs:
            self._stubs["list_metadata_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/ListMetadataJobs",
                request_serializer=catalog.ListMetadataJobsRequest.serialize,
                response_deserializer=catalog.ListMetadataJobsResponse.deserialize,
            )
        return self._stubs["list_metadata_jobs"]

    @property
    def cancel_metadata_job(
        self,
    ) -> Callable[[catalog.CancelMetadataJobRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the cancel metadata job method over gRPC.

        Cancels a metadata job.

        If you cancel a metadata import job that is in progress,
        the changes in the job might be partially applied. We
        recommend that you reset the state of the entry groups
        in your project by running another metadata job that
        reverts the changes from the canceled job.

        Returns:
            Callable[[~.CancelMetadataJobRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_metadata_job" not in self._stubs:
            self._stubs["cancel_metadata_job"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/CancelMetadataJob",
                request_serializer=catalog.CancelMetadataJobRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["cancel_metadata_job"]

    @property
    def create_entry_link(
        self,
    ) -> Callable[[catalog.CreateEntryLinkRequest], Awaitable[catalog.EntryLink]]:
        r"""Return a callable for the create entry link method over gRPC.

        Creates an Entry Link.

        Returns:
            Callable[[~.CreateEntryLinkRequest],
                    Awaitable[~.EntryLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entry_link" not in self._stubs:
            self._stubs["create_entry_link"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/CreateEntryLink",
                request_serializer=catalog.CreateEntryLinkRequest.serialize,
                response_deserializer=catalog.EntryLink.deserialize,
            )
        return self._stubs["create_entry_link"]

    @property
    def update_entry_link(
        self,
    ) -> Callable[[catalog.UpdateEntryLinkRequest], Awaitable[catalog.EntryLink]]:
        r"""Return a callable for the update entry link method over gRPC.

        Updates an Entry Link.

        Returns:
            Callable[[~.UpdateEntryLinkRequest],
                    Awaitable[~.EntryLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entry_link" not in self._stubs:
            self._stubs["update_entry_link"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/UpdateEntryLink",
                request_serializer=catalog.UpdateEntryLinkRequest.serialize,
                response_deserializer=catalog.EntryLink.deserialize,
            )
        return self._stubs["update_entry_link"]

    @property
    def delete_entry_link(
        self,
    ) -> Callable[[catalog.DeleteEntryLinkRequest], Awaitable[catalog.EntryLink]]:
        r"""Return a callable for the delete entry link method over gRPC.

        Deletes an Entry Link.

        Returns:
            Callable[[~.DeleteEntryLinkRequest],
                    Awaitable[~.EntryLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entry_link" not in self._stubs:
            self._stubs["delete_entry_link"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/DeleteEntryLink",
                request_serializer=catalog.DeleteEntryLinkRequest.serialize,
                response_deserializer=catalog.EntryLink.deserialize,
            )
        return self._stubs["delete_entry_link"]

    @property
    def lookup_entry_links(
        self,
    ) -> Callable[
        [catalog.LookupEntryLinksRequest], Awaitable[catalog.LookupEntryLinksResponse]
    ]:
        r"""Return a callable for the lookup entry links method over gRPC.

        Looks up Entry Links referencing the specified Entry.

        Returns:
            Callable[[~.LookupEntryLinksRequest],
                    Awaitable[~.LookupEntryLinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_entry_links" not in self._stubs:
            self._stubs["lookup_entry_links"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/LookupEntryLinks",
                request_serializer=catalog.LookupEntryLinksRequest.serialize,
                response_deserializer=catalog.LookupEntryLinksResponse.deserialize,
            )
        return self._stubs["lookup_entry_links"]

    @property
    def lookup_context(
        self,
    ) -> Callable[
        [catalog.LookupContextRequest], Awaitable[catalog.LookupContextResponse]
    ]:
        r"""Return a callable for the lookup context method over gRPC.

        Looks up LLM Context for the specified resources.

        Returns:
            Callable[[~.LookupContextRequest],
                    Awaitable[~.LookupContextResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_context" not in self._stubs:
            self._stubs["lookup_context"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/LookupContext",
                request_serializer=catalog.LookupContextRequest.serialize,
                response_deserializer=catalog.LookupContextResponse.deserialize,
            )
        return self._stubs["lookup_context"]

    @property
    def get_entry_link(
        self,
    ) -> Callable[[catalog.GetEntryLinkRequest], Awaitable[catalog.EntryLink]]:
        r"""Return a callable for the get entry link method over gRPC.

        Gets an Entry Link.

        Returns:
            Callable[[~.GetEntryLinkRequest],
                    Awaitable[~.EntryLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entry_link" not in self._stubs:
            self._stubs["get_entry_link"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/GetEntryLink",
                request_serializer=catalog.GetEntryLinkRequest.serialize,
                response_deserializer=catalog.EntryLink.deserialize,
            )
        return self._stubs["get_entry_link"]

    @property
    def create_metadata_feed(
        self,
    ) -> Callable[
        [catalog.CreateMetadataFeedRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create metadata feed method over gRPC.

        Creates a MetadataFeed.

        Returns:
            Callable[[~.CreateMetadataFeedRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_metadata_feed" not in self._stubs:
            self._stubs["create_metadata_feed"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/CreateMetadataFeed",
                request_serializer=catalog.CreateMetadataFeedRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_metadata_feed"]

    @property
    def get_metadata_feed(
        self,
    ) -> Callable[[catalog.GetMetadataFeedRequest], Awaitable[catalog.MetadataFeed]]:
        r"""Return a callable for the get metadata feed method over gRPC.

        Gets a MetadataFeed.

        Returns:
            Callable[[~.GetMetadataFeedRequest],
                    Awaitable[~.MetadataFeed]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_metadata_feed" not in self._stubs:
            self._stubs["get_metadata_feed"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/GetMetadataFeed",
                request_serializer=catalog.GetMetadataFeedRequest.serialize,
                response_deserializer=catalog.MetadataFeed.deserialize,
            )
        return self._stubs["get_metadata_feed"]

    @property
    def list_metadata_feeds(
        self,
    ) -> Callable[
        [catalog.ListMetadataFeedsRequest], Awaitable[catalog.ListMetadataFeedsResponse]
    ]:
        r"""Return a callable for the list metadata feeds method over gRPC.

        Retrieve a list of MetadataFeeds.

        Returns:
            Callable[[~.ListMetadataFeedsRequest],
                    Awaitable[~.ListMetadataFeedsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_metadata_feeds" not in self._stubs:
            self._stubs["list_metadata_feeds"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/ListMetadataFeeds",
                request_serializer=catalog.ListMetadataFeedsRequest.serialize,
                response_deserializer=catalog.ListMetadataFeedsResponse.deserialize,
            )
        return self._stubs["list_metadata_feeds"]

    @property
    def delete_metadata_feed(
        self,
    ) -> Callable[
        [catalog.DeleteMetadataFeedRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete metadata feed method over gRPC.

        Deletes a MetadataFeed.

        Returns:
            Callable[[~.DeleteMetadataFeedRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_metadata_feed" not in self._stubs:
            self._stubs["delete_metadata_feed"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/DeleteMetadataFeed",
                request_serializer=catalog.DeleteMetadataFeedRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_metadata_feed"]

    @property
    def update_metadata_feed(
        self,
    ) -> Callable[
        [catalog.UpdateMetadataFeedRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update metadata feed method over gRPC.

        Updates a MetadataFeed.

        Returns:
            Callable[[~.UpdateMetadataFeedRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_metadata_feed" not in self._stubs:
            self._stubs["update_metadata_feed"] = self._logged_channel.unary_unary(
                "/google.cloud.dataplex.v1.CatalogService/UpdateMetadataFeed",
                request_serializer=catalog.UpdateMetadataFeedRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_metadata_feed"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_entry_type: self._wrap_method(
                self.create_entry_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_entry_type: self._wrap_method(
                self.update_entry_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_entry_type: self._wrap_method(
                self.delete_entry_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_entry_types: self._wrap_method(
                self.list_entry_types,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_entry_type: self._wrap_method(
                self.get_entry_type,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_aspect_type: self._wrap_method(
                self.create_aspect_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_aspect_type: self._wrap_method(
                self.update_aspect_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_aspect_type: self._wrap_method(
                self.delete_aspect_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_aspect_types: self._wrap_method(
                self.list_aspect_types,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_aspect_type: self._wrap_method(
                self.get_aspect_type,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_entry_group: self._wrap_method(
                self.create_entry_group,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_entry_group: self._wrap_method(
                self.update_entry_group,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_entry_group: self._wrap_method(
                self.delete_entry_group,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_entry_groups: self._wrap_method(
                self.list_entry_groups,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_entry_group: self._wrap_method(
                self.get_entry_group,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_entry: self._wrap_method(
                self.create_entry,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_entry: self._wrap_method(
                self.update_entry,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_entry: self._wrap_method(
                self.delete_entry,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_entries: self._wrap_method(
                self.list_entries,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.get_entry: self._wrap_method(
                self.get_entry,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.lookup_entry: self._wrap_method(
                self.lookup_entry,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.modify_entry: self._wrap_method(
                self.modify_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_entries: self._wrap_method(
                self.search_entries,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_metadata_job: self._wrap_method(
                self.create_metadata_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_metadata_job: self._wrap_method(
                self.get_metadata_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_metadata_jobs: self._wrap_method(
                self.list_metadata_jobs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_metadata_job: self._wrap_method(
                self.cancel_metadata_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entry_link: self._wrap_method(
                self.create_entry_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_entry_link: self._wrap_method(
                self.update_entry_link,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_entry_link: self._wrap_method(
                self.delete_entry_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.lookup_entry_links: self._wrap_method(
                self.lookup_entry_links,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.lookup_context: self._wrap_method(
                self.lookup_context,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entry_link: self._wrap_method(
                self.get_entry_link,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.create_metadata_feed: self._wrap_method(
                self.create_metadata_feed,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_metadata_feed: self._wrap_method(
                self.get_metadata_feed,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_metadata_feeds: self._wrap_method(
                self.list_metadata_feeds,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_metadata_feed: self._wrap_method(
                self.delete_metadata_feed,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_metadata_feed: self._wrap_method(
                self.update_metadata_feed,
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


__all__ = ("CatalogServiceGrpcAsyncIOTransport",)
