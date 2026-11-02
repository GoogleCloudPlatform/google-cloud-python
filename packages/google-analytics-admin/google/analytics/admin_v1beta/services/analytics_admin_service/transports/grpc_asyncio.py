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

from google.analytics.admin_v1beta.types import analytics_admin, resources

from .base import DEFAULT_CLIENT_INFO, AnalyticsAdminServiceTransport
from .grpc import AnalyticsAdminServiceGrpcTransport

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
                    "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
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
                    "serviceName": "google.analytics.admin.v1beta.AnalyticsAdminService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AnalyticsAdminServiceGrpcAsyncIOTransport(AnalyticsAdminServiceTransport):
    """gRPC AsyncIO backend transport for AnalyticsAdminService.

    Service Interface for the Google Analytics Admin API.

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
        host: str = "analyticsadmin.googleapis.com",
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
        host: str = "analyticsadmin.googleapis.com",
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
                 The hostname to connect to (default: 'analyticsadmin.googleapis.com').
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
    def get_account(
        self,
    ) -> Callable[[analytics_admin.GetAccountRequest], Awaitable[resources.Account]]:
        r"""Return a callable for the get account method over gRPC.

        Lookup for a single Account.

        Returns:
            Callable[[~.GetAccountRequest],
                    Awaitable[~.Account]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_account" not in self._stubs:
            self._stubs["get_account"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/GetAccount",
                request_serializer=analytics_admin.GetAccountRequest.serialize,
                response_deserializer=resources.Account.deserialize,
            )
        return self._stubs["get_account"]

    @property
    def list_accounts(
        self,
    ) -> Callable[
        [analytics_admin.ListAccountsRequest],
        Awaitable[analytics_admin.ListAccountsResponse],
    ]:
        r"""Return a callable for the list accounts method over gRPC.

        Returns all accounts accessible by the caller.

        Note that these accounts might not currently have GA
        properties. Soft-deleted (ie: "trashed") accounts are
        excluded by default. Returns an empty list if no
        relevant accounts are found.

        Returns:
            Callable[[~.ListAccountsRequest],
                    Awaitable[~.ListAccountsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_accounts" not in self._stubs:
            self._stubs["list_accounts"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListAccounts",
                request_serializer=analytics_admin.ListAccountsRequest.serialize,
                response_deserializer=analytics_admin.ListAccountsResponse.deserialize,
            )
        return self._stubs["list_accounts"]

    @property
    def delete_account(
        self,
    ) -> Callable[[analytics_admin.DeleteAccountRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete account method over gRPC.

        Marks target Account as soft-deleted (ie: "trashed")
        and returns it.
        This API does not have a method to restore soft-deleted
        accounts. However, they can be restored using the Trash
        Can UI.

        If the accounts are not restored before the expiration
        time, the account and all child resources (eg:
        Properties, GoogleAdsLinks, Streams, AccessBindings)
        will be permanently purged.
        https://support.google.com/analytics/answer/6154772

        Returns an error if the target is not found.

        Returns:
            Callable[[~.DeleteAccountRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_account" not in self._stubs:
            self._stubs["delete_account"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/DeleteAccount",
                request_serializer=analytics_admin.DeleteAccountRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_account"]

    @property
    def update_account(
        self,
    ) -> Callable[[analytics_admin.UpdateAccountRequest], Awaitable[resources.Account]]:
        r"""Return a callable for the update account method over gRPC.

        Updates an account.

        Returns:
            Callable[[~.UpdateAccountRequest],
                    Awaitable[~.Account]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_account" not in self._stubs:
            self._stubs["update_account"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateAccount",
                request_serializer=analytics_admin.UpdateAccountRequest.serialize,
                response_deserializer=resources.Account.deserialize,
            )
        return self._stubs["update_account"]

    @property
    def provision_account_ticket(
        self,
    ) -> Callable[
        [analytics_admin.ProvisionAccountTicketRequest],
        Awaitable[analytics_admin.ProvisionAccountTicketResponse],
    ]:
        r"""Return a callable for the provision account ticket method over gRPC.

        Requests a ticket for creating an account.

        Returns:
            Callable[[~.ProvisionAccountTicketRequest],
                    Awaitable[~.ProvisionAccountTicketResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "provision_account_ticket" not in self._stubs:
            self._stubs["provision_account_ticket"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ProvisionAccountTicket",
                request_serializer=analytics_admin.ProvisionAccountTicketRequest.serialize,
                response_deserializer=analytics_admin.ProvisionAccountTicketResponse.deserialize,
            )
        return self._stubs["provision_account_ticket"]

    @property
    def list_account_summaries(
        self,
    ) -> Callable[
        [analytics_admin.ListAccountSummariesRequest],
        Awaitable[analytics_admin.ListAccountSummariesResponse],
    ]:
        r"""Return a callable for the list account summaries method over gRPC.

        Returns summaries of all accounts accessible by the
        caller.

        Returns:
            Callable[[~.ListAccountSummariesRequest],
                    Awaitable[~.ListAccountSummariesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_account_summaries" not in self._stubs:
            self._stubs["list_account_summaries"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListAccountSummaries",
                request_serializer=analytics_admin.ListAccountSummariesRequest.serialize,
                response_deserializer=analytics_admin.ListAccountSummariesResponse.deserialize,
            )
        return self._stubs["list_account_summaries"]

    @property
    def get_property(
        self,
    ) -> Callable[[analytics_admin.GetPropertyRequest], Awaitable[resources.Property]]:
        r"""Return a callable for the get property method over gRPC.

        Lookup for a single GA Property.

        Returns:
            Callable[[~.GetPropertyRequest],
                    Awaitable[~.Property]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_property" not in self._stubs:
            self._stubs["get_property"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/GetProperty",
                request_serializer=analytics_admin.GetPropertyRequest.serialize,
                response_deserializer=resources.Property.deserialize,
            )
        return self._stubs["get_property"]

    @property
    def list_properties(
        self,
    ) -> Callable[
        [analytics_admin.ListPropertiesRequest],
        Awaitable[analytics_admin.ListPropertiesResponse],
    ]:
        r"""Return a callable for the list properties method over gRPC.

        Returns child Properties under the specified parent
        Account.
        Properties will be excluded if the caller does not have
        access. Soft-deleted (ie: "trashed") properties are
        excluded by default. Returns an empty list if no
        relevant properties are found.

        Returns:
            Callable[[~.ListPropertiesRequest],
                    Awaitable[~.ListPropertiesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_properties" not in self._stubs:
            self._stubs["list_properties"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListProperties",
                request_serializer=analytics_admin.ListPropertiesRequest.serialize,
                response_deserializer=analytics_admin.ListPropertiesResponse.deserialize,
            )
        return self._stubs["list_properties"]

    @property
    def create_property(
        self,
    ) -> Callable[
        [analytics_admin.CreatePropertyRequest], Awaitable[resources.Property]
    ]:
        r"""Return a callable for the create property method over gRPC.

        Creates a Google Analytics property with the
        specified location and attributes.

        Returns:
            Callable[[~.CreatePropertyRequest],
                    Awaitable[~.Property]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_property" not in self._stubs:
            self._stubs["create_property"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateProperty",
                request_serializer=analytics_admin.CreatePropertyRequest.serialize,
                response_deserializer=resources.Property.deserialize,
            )
        return self._stubs["create_property"]

    @property
    def delete_property(
        self,
    ) -> Callable[
        [analytics_admin.DeletePropertyRequest], Awaitable[resources.Property]
    ]:
        r"""Return a callable for the delete property method over gRPC.

        Marks target Property as soft-deleted (ie: "trashed")
        and returns it.
        This API does not have a method to restore soft-deleted
        properties. However, they can be restored using the
        Trash Can UI.

        If the properties are not restored before the expiration
        time, the Property and all child resources (eg:
        GoogleAdsLinks, Streams, AccessBindings) will be
        permanently purged.
        https://support.google.com/analytics/answer/6154772

        Returns an error if the target is not found.

        Returns:
            Callable[[~.DeletePropertyRequest],
                    Awaitable[~.Property]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_property" not in self._stubs:
            self._stubs["delete_property"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/DeleteProperty",
                request_serializer=analytics_admin.DeletePropertyRequest.serialize,
                response_deserializer=resources.Property.deserialize,
            )
        return self._stubs["delete_property"]

    @property
    def update_property(
        self,
    ) -> Callable[
        [analytics_admin.UpdatePropertyRequest], Awaitable[resources.Property]
    ]:
        r"""Return a callable for the update property method over gRPC.

        Updates a property.

        Returns:
            Callable[[~.UpdatePropertyRequest],
                    Awaitable[~.Property]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_property" not in self._stubs:
            self._stubs["update_property"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateProperty",
                request_serializer=analytics_admin.UpdatePropertyRequest.serialize,
                response_deserializer=resources.Property.deserialize,
            )
        return self._stubs["update_property"]

    @property
    def create_firebase_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateFirebaseLinkRequest], Awaitable[resources.FirebaseLink]
    ]:
        r"""Return a callable for the create firebase link method over gRPC.

        Creates a FirebaseLink.

        Properties can have at most one FirebaseLink.

        Returns:
            Callable[[~.CreateFirebaseLinkRequest],
                    Awaitable[~.FirebaseLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_firebase_link" not in self._stubs:
            self._stubs["create_firebase_link"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateFirebaseLink",
                request_serializer=analytics_admin.CreateFirebaseLinkRequest.serialize,
                response_deserializer=resources.FirebaseLink.deserialize,
            )
        return self._stubs["create_firebase_link"]

    @property
    def delete_firebase_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteFirebaseLinkRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete firebase link method over gRPC.

        Deletes a FirebaseLink on a property

        Returns:
            Callable[[~.DeleteFirebaseLinkRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_firebase_link" not in self._stubs:
            self._stubs["delete_firebase_link"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/DeleteFirebaseLink",
                request_serializer=analytics_admin.DeleteFirebaseLinkRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_firebase_link"]

    @property
    def list_firebase_links(
        self,
    ) -> Callable[
        [analytics_admin.ListFirebaseLinksRequest],
        Awaitable[analytics_admin.ListFirebaseLinksResponse],
    ]:
        r"""Return a callable for the list firebase links method over gRPC.

        Lists FirebaseLinks on a property.
        Properties can have at most one FirebaseLink.

        Returns:
            Callable[[~.ListFirebaseLinksRequest],
                    Awaitable[~.ListFirebaseLinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_firebase_links" not in self._stubs:
            self._stubs["list_firebase_links"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListFirebaseLinks",
                request_serializer=analytics_admin.ListFirebaseLinksRequest.serialize,
                response_deserializer=analytics_admin.ListFirebaseLinksResponse.deserialize,
            )
        return self._stubs["list_firebase_links"]

    @property
    def create_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateGoogleAdsLinkRequest], Awaitable[resources.GoogleAdsLink]
    ]:
        r"""Return a callable for the create google ads link method over gRPC.

        Creates a GoogleAdsLink.

        Returns:
            Callable[[~.CreateGoogleAdsLinkRequest],
                    Awaitable[~.GoogleAdsLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_google_ads_link" not in self._stubs:
            self._stubs["create_google_ads_link"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateGoogleAdsLink",
                request_serializer=analytics_admin.CreateGoogleAdsLinkRequest.serialize,
                response_deserializer=resources.GoogleAdsLink.deserialize,
            )
        return self._stubs["create_google_ads_link"]

    @property
    def update_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.UpdateGoogleAdsLinkRequest], Awaitable[resources.GoogleAdsLink]
    ]:
        r"""Return a callable for the update google ads link method over gRPC.

        Updates a GoogleAdsLink on a property

        Returns:
            Callable[[~.UpdateGoogleAdsLinkRequest],
                    Awaitable[~.GoogleAdsLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_google_ads_link" not in self._stubs:
            self._stubs["update_google_ads_link"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateGoogleAdsLink",
                request_serializer=analytics_admin.UpdateGoogleAdsLinkRequest.serialize,
                response_deserializer=resources.GoogleAdsLink.deserialize,
            )
        return self._stubs["update_google_ads_link"]

    @property
    def delete_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteGoogleAdsLinkRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete google ads link method over gRPC.

        Deletes a GoogleAdsLink on a property

        Returns:
            Callable[[~.DeleteGoogleAdsLinkRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_google_ads_link" not in self._stubs:
            self._stubs["delete_google_ads_link"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/DeleteGoogleAdsLink",
                request_serializer=analytics_admin.DeleteGoogleAdsLinkRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_google_ads_link"]

    @property
    def list_google_ads_links(
        self,
    ) -> Callable[
        [analytics_admin.ListGoogleAdsLinksRequest],
        Awaitable[analytics_admin.ListGoogleAdsLinksResponse],
    ]:
        r"""Return a callable for the list google ads links method over gRPC.

        Lists GoogleAdsLinks on a property.

        Returns:
            Callable[[~.ListGoogleAdsLinksRequest],
                    Awaitable[~.ListGoogleAdsLinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_google_ads_links" not in self._stubs:
            self._stubs["list_google_ads_links"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListGoogleAdsLinks",
                request_serializer=analytics_admin.ListGoogleAdsLinksRequest.serialize,
                response_deserializer=analytics_admin.ListGoogleAdsLinksResponse.deserialize,
            )
        return self._stubs["list_google_ads_links"]

    @property
    def get_data_sharing_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetDataSharingSettingsRequest],
        Awaitable[resources.DataSharingSettings],
    ]:
        r"""Return a callable for the get data sharing settings method over gRPC.

        Get data sharing settings on an account.
        Data sharing settings are singletons.

        Returns:
            Callable[[~.GetDataSharingSettingsRequest],
                    Awaitable[~.DataSharingSettings]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_data_sharing_settings" not in self._stubs:
            self._stubs["get_data_sharing_settings"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/GetDataSharingSettings",
                request_serializer=analytics_admin.GetDataSharingSettingsRequest.serialize,
                response_deserializer=resources.DataSharingSettings.deserialize,
            )
        return self._stubs["get_data_sharing_settings"]

    @property
    def get_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.GetMeasurementProtocolSecretRequest],
        Awaitable[resources.MeasurementProtocolSecret],
    ]:
        r"""Return a callable for the get measurement protocol
        secret method over gRPC.

        Lookup for a single MeasurementProtocolSecret.

        Returns:
            Callable[[~.GetMeasurementProtocolSecretRequest],
                    Awaitable[~.MeasurementProtocolSecret]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_measurement_protocol_secret" not in self._stubs:
            self._stubs["get_measurement_protocol_secret"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/GetMeasurementProtocolSecret",
                    request_serializer=analytics_admin.GetMeasurementProtocolSecretRequest.serialize,
                    response_deserializer=resources.MeasurementProtocolSecret.deserialize,
                )
            )
        return self._stubs["get_measurement_protocol_secret"]

    @property
    def list_measurement_protocol_secrets(
        self,
    ) -> Callable[
        [analytics_admin.ListMeasurementProtocolSecretsRequest],
        Awaitable[analytics_admin.ListMeasurementProtocolSecretsResponse],
    ]:
        r"""Return a callable for the list measurement protocol
        secrets method over gRPC.

        Returns child MeasurementProtocolSecrets under the
        specified parent Property.

        Returns:
            Callable[[~.ListMeasurementProtocolSecretsRequest],
                    Awaitable[~.ListMeasurementProtocolSecretsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_measurement_protocol_secrets" not in self._stubs:
            self._stubs["list_measurement_protocol_secrets"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/ListMeasurementProtocolSecrets",
                    request_serializer=analytics_admin.ListMeasurementProtocolSecretsRequest.serialize,
                    response_deserializer=analytics_admin.ListMeasurementProtocolSecretsResponse.deserialize,
                )
            )
        return self._stubs["list_measurement_protocol_secrets"]

    @property
    def create_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.CreateMeasurementProtocolSecretRequest],
        Awaitable[resources.MeasurementProtocolSecret],
    ]:
        r"""Return a callable for the create measurement protocol
        secret method over gRPC.

        Creates a measurement protocol secret.

        Returns:
            Callable[[~.CreateMeasurementProtocolSecretRequest],
                    Awaitable[~.MeasurementProtocolSecret]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_measurement_protocol_secret" not in self._stubs:
            self._stubs["create_measurement_protocol_secret"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateMeasurementProtocolSecret",
                    request_serializer=analytics_admin.CreateMeasurementProtocolSecretRequest.serialize,
                    response_deserializer=resources.MeasurementProtocolSecret.deserialize,
                )
            )
        return self._stubs["create_measurement_protocol_secret"]

    @property
    def delete_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.DeleteMeasurementProtocolSecretRequest],
        Awaitable[empty_pb2.Empty],
    ]:
        r"""Return a callable for the delete measurement protocol
        secret method over gRPC.

        Deletes target MeasurementProtocolSecret.

        Returns:
            Callable[[~.DeleteMeasurementProtocolSecretRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_measurement_protocol_secret" not in self._stubs:
            self._stubs["delete_measurement_protocol_secret"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/DeleteMeasurementProtocolSecret",
                    request_serializer=analytics_admin.DeleteMeasurementProtocolSecretRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_measurement_protocol_secret"]

    @property
    def update_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.UpdateMeasurementProtocolSecretRequest],
        Awaitable[resources.MeasurementProtocolSecret],
    ]:
        r"""Return a callable for the update measurement protocol
        secret method over gRPC.

        Updates a measurement protocol secret.

        Returns:
            Callable[[~.UpdateMeasurementProtocolSecretRequest],
                    Awaitable[~.MeasurementProtocolSecret]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_measurement_protocol_secret" not in self._stubs:
            self._stubs["update_measurement_protocol_secret"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateMeasurementProtocolSecret",
                    request_serializer=analytics_admin.UpdateMeasurementProtocolSecretRequest.serialize,
                    response_deserializer=resources.MeasurementProtocolSecret.deserialize,
                )
            )
        return self._stubs["update_measurement_protocol_secret"]

    @property
    def acknowledge_user_data_collection(
        self,
    ) -> Callable[
        [analytics_admin.AcknowledgeUserDataCollectionRequest],
        Awaitable[analytics_admin.AcknowledgeUserDataCollectionResponse],
    ]:
        r"""Return a callable for the acknowledge user data
        collection method over gRPC.

        Acknowledges the terms of user data collection for
        the specified property.
        This acknowledgement must be completed (either in the
        Google Analytics UI or through this API) before
        MeasurementProtocolSecret resources may be created.

        Returns:
            Callable[[~.AcknowledgeUserDataCollectionRequest],
                    Awaitable[~.AcknowledgeUserDataCollectionResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "acknowledge_user_data_collection" not in self._stubs:
            self._stubs["acknowledge_user_data_collection"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/AcknowledgeUserDataCollection",
                    request_serializer=analytics_admin.AcknowledgeUserDataCollectionRequest.serialize,
                    response_deserializer=analytics_admin.AcknowledgeUserDataCollectionResponse.deserialize,
                )
            )
        return self._stubs["acknowledge_user_data_collection"]

    @property
    def search_change_history_events(
        self,
    ) -> Callable[
        [analytics_admin.SearchChangeHistoryEventsRequest],
        Awaitable[analytics_admin.SearchChangeHistoryEventsResponse],
    ]:
        r"""Return a callable for the search change history events method over gRPC.

        Searches through all changes to an account or its
        children given the specified set of filters.

        Only returns the subset of changes supported by the API.
        The UI may return additional changes.

        Returns:
            Callable[[~.SearchChangeHistoryEventsRequest],
                    Awaitable[~.SearchChangeHistoryEventsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_change_history_events" not in self._stubs:
            self._stubs["search_change_history_events"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/SearchChangeHistoryEvents",
                    request_serializer=analytics_admin.SearchChangeHistoryEventsRequest.serialize,
                    response_deserializer=analytics_admin.SearchChangeHistoryEventsResponse.deserialize,
                )
            )
        return self._stubs["search_change_history_events"]

    @property
    def create_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.CreateConversionEventRequest],
        Awaitable[resources.ConversionEvent],
    ]:
        r"""Return a callable for the create conversion event method over gRPC.

        Deprecated: Use ``CreateKeyEvent`` instead. Creates a conversion
        event with the specified attributes.

        Returns:
            Callable[[~.CreateConversionEventRequest],
                    Awaitable[~.ConversionEvent]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_conversion_event" not in self._stubs:
            self._stubs["create_conversion_event"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateConversionEvent",
                request_serializer=analytics_admin.CreateConversionEventRequest.serialize,
                response_deserializer=resources.ConversionEvent.deserialize,
            )
        return self._stubs["create_conversion_event"]

    @property
    def update_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.UpdateConversionEventRequest],
        Awaitable[resources.ConversionEvent],
    ]:
        r"""Return a callable for the update conversion event method over gRPC.

        Deprecated: Use ``UpdateKeyEvent`` instead. Updates a conversion
        event with the specified attributes.

        Returns:
            Callable[[~.UpdateConversionEventRequest],
                    Awaitable[~.ConversionEvent]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_conversion_event" not in self._stubs:
            self._stubs["update_conversion_event"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateConversionEvent",
                request_serializer=analytics_admin.UpdateConversionEventRequest.serialize,
                response_deserializer=resources.ConversionEvent.deserialize,
            )
        return self._stubs["update_conversion_event"]

    @property
    def get_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.GetConversionEventRequest],
        Awaitable[resources.ConversionEvent],
    ]:
        r"""Return a callable for the get conversion event method over gRPC.

        Deprecated: Use ``GetKeyEvent`` instead. Retrieve a single
        conversion event.

        Returns:
            Callable[[~.GetConversionEventRequest],
                    Awaitable[~.ConversionEvent]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_conversion_event" not in self._stubs:
            self._stubs["get_conversion_event"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/GetConversionEvent",
                request_serializer=analytics_admin.GetConversionEventRequest.serialize,
                response_deserializer=resources.ConversionEvent.deserialize,
            )
        return self._stubs["get_conversion_event"]

    @property
    def delete_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.DeleteConversionEventRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete conversion event method over gRPC.

        Deprecated: Use ``DeleteKeyEvent`` instead. Deletes a conversion
        event in a property.

        Returns:
            Callable[[~.DeleteConversionEventRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_conversion_event" not in self._stubs:
            self._stubs["delete_conversion_event"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/DeleteConversionEvent",
                request_serializer=analytics_admin.DeleteConversionEventRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_conversion_event"]

    @property
    def list_conversion_events(
        self,
    ) -> Callable[
        [analytics_admin.ListConversionEventsRequest],
        Awaitable[analytics_admin.ListConversionEventsResponse],
    ]:
        r"""Return a callable for the list conversion events method over gRPC.

        Deprecated: Use ``ListKeyEvents`` instead. Returns a list of
        conversion events in the specified parent property.

        Returns an empty list if no conversion events are found.

        Returns:
            Callable[[~.ListConversionEventsRequest],
                    Awaitable[~.ListConversionEventsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_conversion_events" not in self._stubs:
            self._stubs["list_conversion_events"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListConversionEvents",
                request_serializer=analytics_admin.ListConversionEventsRequest.serialize,
                response_deserializer=analytics_admin.ListConversionEventsResponse.deserialize,
            )
        return self._stubs["list_conversion_events"]

    @property
    def create_key_event(
        self,
    ) -> Callable[
        [analytics_admin.CreateKeyEventRequest], Awaitable[resources.KeyEvent]
    ]:
        r"""Return a callable for the create key event method over gRPC.

        Creates a Key Event.

        Returns:
            Callable[[~.CreateKeyEventRequest],
                    Awaitable[~.KeyEvent]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_key_event" not in self._stubs:
            self._stubs["create_key_event"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateKeyEvent",
                request_serializer=analytics_admin.CreateKeyEventRequest.serialize,
                response_deserializer=resources.KeyEvent.deserialize,
            )
        return self._stubs["create_key_event"]

    @property
    def update_key_event(
        self,
    ) -> Callable[
        [analytics_admin.UpdateKeyEventRequest], Awaitable[resources.KeyEvent]
    ]:
        r"""Return a callable for the update key event method over gRPC.

        Updates a Key Event.

        Returns:
            Callable[[~.UpdateKeyEventRequest],
                    Awaitable[~.KeyEvent]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_key_event" not in self._stubs:
            self._stubs["update_key_event"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateKeyEvent",
                request_serializer=analytics_admin.UpdateKeyEventRequest.serialize,
                response_deserializer=resources.KeyEvent.deserialize,
            )
        return self._stubs["update_key_event"]

    @property
    def get_key_event(
        self,
    ) -> Callable[[analytics_admin.GetKeyEventRequest], Awaitable[resources.KeyEvent]]:
        r"""Return a callable for the get key event method over gRPC.

        Retrieve a single Key Event.

        Returns:
            Callable[[~.GetKeyEventRequest],
                    Awaitable[~.KeyEvent]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_key_event" not in self._stubs:
            self._stubs["get_key_event"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/GetKeyEvent",
                request_serializer=analytics_admin.GetKeyEventRequest.serialize,
                response_deserializer=resources.KeyEvent.deserialize,
            )
        return self._stubs["get_key_event"]

    @property
    def delete_key_event(
        self,
    ) -> Callable[[analytics_admin.DeleteKeyEventRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete key event method over gRPC.

        Deletes a Key Event.

        Returns:
            Callable[[~.DeleteKeyEventRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_key_event" not in self._stubs:
            self._stubs["delete_key_event"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/DeleteKeyEvent",
                request_serializer=analytics_admin.DeleteKeyEventRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_key_event"]

    @property
    def list_key_events(
        self,
    ) -> Callable[
        [analytics_admin.ListKeyEventsRequest],
        Awaitable[analytics_admin.ListKeyEventsResponse],
    ]:
        r"""Return a callable for the list key events method over gRPC.

        Returns a list of Key Events in the specified parent
        property. Returns an empty list if no Key Events are
        found.

        Returns:
            Callable[[~.ListKeyEventsRequest],
                    Awaitable[~.ListKeyEventsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_key_events" not in self._stubs:
            self._stubs["list_key_events"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListKeyEvents",
                request_serializer=analytics_admin.ListKeyEventsRequest.serialize,
                response_deserializer=analytics_admin.ListKeyEventsResponse.deserialize,
            )
        return self._stubs["list_key_events"]

    @property
    def create_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.CreateCustomDimensionRequest],
        Awaitable[resources.CustomDimension],
    ]:
        r"""Return a callable for the create custom dimension method over gRPC.

        Creates a CustomDimension.

        Returns:
            Callable[[~.CreateCustomDimensionRequest],
                    Awaitable[~.CustomDimension]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_custom_dimension" not in self._stubs:
            self._stubs["create_custom_dimension"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateCustomDimension",
                request_serializer=analytics_admin.CreateCustomDimensionRequest.serialize,
                response_deserializer=resources.CustomDimension.deserialize,
            )
        return self._stubs["create_custom_dimension"]

    @property
    def update_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.UpdateCustomDimensionRequest],
        Awaitable[resources.CustomDimension],
    ]:
        r"""Return a callable for the update custom dimension method over gRPC.

        Updates a CustomDimension on a property.

        Returns:
            Callable[[~.UpdateCustomDimensionRequest],
                    Awaitable[~.CustomDimension]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_custom_dimension" not in self._stubs:
            self._stubs["update_custom_dimension"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateCustomDimension",
                request_serializer=analytics_admin.UpdateCustomDimensionRequest.serialize,
                response_deserializer=resources.CustomDimension.deserialize,
            )
        return self._stubs["update_custom_dimension"]

    @property
    def list_custom_dimensions(
        self,
    ) -> Callable[
        [analytics_admin.ListCustomDimensionsRequest],
        Awaitable[analytics_admin.ListCustomDimensionsResponse],
    ]:
        r"""Return a callable for the list custom dimensions method over gRPC.

        Lists CustomDimensions on a property.

        Returns:
            Callable[[~.ListCustomDimensionsRequest],
                    Awaitable[~.ListCustomDimensionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_custom_dimensions" not in self._stubs:
            self._stubs["list_custom_dimensions"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListCustomDimensions",
                request_serializer=analytics_admin.ListCustomDimensionsRequest.serialize,
                response_deserializer=analytics_admin.ListCustomDimensionsResponse.deserialize,
            )
        return self._stubs["list_custom_dimensions"]

    @property
    def archive_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.ArchiveCustomDimensionRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the archive custom dimension method over gRPC.

        Archives a CustomDimension on a property.

        Returns:
            Callable[[~.ArchiveCustomDimensionRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "archive_custom_dimension" not in self._stubs:
            self._stubs["archive_custom_dimension"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ArchiveCustomDimension",
                request_serializer=analytics_admin.ArchiveCustomDimensionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["archive_custom_dimension"]

    @property
    def get_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.GetCustomDimensionRequest],
        Awaitable[resources.CustomDimension],
    ]:
        r"""Return a callable for the get custom dimension method over gRPC.

        Lookup for a single CustomDimension.

        Returns:
            Callable[[~.GetCustomDimensionRequest],
                    Awaitable[~.CustomDimension]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_custom_dimension" not in self._stubs:
            self._stubs["get_custom_dimension"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/GetCustomDimension",
                request_serializer=analytics_admin.GetCustomDimensionRequest.serialize,
                response_deserializer=resources.CustomDimension.deserialize,
            )
        return self._stubs["get_custom_dimension"]

    @property
    def create_custom_metric(
        self,
    ) -> Callable[
        [analytics_admin.CreateCustomMetricRequest], Awaitable[resources.CustomMetric]
    ]:
        r"""Return a callable for the create custom metric method over gRPC.

        Creates a CustomMetric.

        Returns:
            Callable[[~.CreateCustomMetricRequest],
                    Awaitable[~.CustomMetric]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_custom_metric" not in self._stubs:
            self._stubs["create_custom_metric"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateCustomMetric",
                request_serializer=analytics_admin.CreateCustomMetricRequest.serialize,
                response_deserializer=resources.CustomMetric.deserialize,
            )
        return self._stubs["create_custom_metric"]

    @property
    def update_custom_metric(
        self,
    ) -> Callable[
        [analytics_admin.UpdateCustomMetricRequest], Awaitable[resources.CustomMetric]
    ]:
        r"""Return a callable for the update custom metric method over gRPC.

        Updates a CustomMetric on a property.

        Returns:
            Callable[[~.UpdateCustomMetricRequest],
                    Awaitable[~.CustomMetric]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_custom_metric" not in self._stubs:
            self._stubs["update_custom_metric"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateCustomMetric",
                request_serializer=analytics_admin.UpdateCustomMetricRequest.serialize,
                response_deserializer=resources.CustomMetric.deserialize,
            )
        return self._stubs["update_custom_metric"]

    @property
    def list_custom_metrics(
        self,
    ) -> Callable[
        [analytics_admin.ListCustomMetricsRequest],
        Awaitable[analytics_admin.ListCustomMetricsResponse],
    ]:
        r"""Return a callable for the list custom metrics method over gRPC.

        Lists CustomMetrics on a property.

        Returns:
            Callable[[~.ListCustomMetricsRequest],
                    Awaitable[~.ListCustomMetricsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_custom_metrics" not in self._stubs:
            self._stubs["list_custom_metrics"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListCustomMetrics",
                request_serializer=analytics_admin.ListCustomMetricsRequest.serialize,
                response_deserializer=analytics_admin.ListCustomMetricsResponse.deserialize,
            )
        return self._stubs["list_custom_metrics"]

    @property
    def archive_custom_metric(
        self,
    ) -> Callable[
        [analytics_admin.ArchiveCustomMetricRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the archive custom metric method over gRPC.

        Archives a CustomMetric on a property.

        Returns:
            Callable[[~.ArchiveCustomMetricRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "archive_custom_metric" not in self._stubs:
            self._stubs["archive_custom_metric"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ArchiveCustomMetric",
                request_serializer=analytics_admin.ArchiveCustomMetricRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["archive_custom_metric"]

    @property
    def get_custom_metric(
        self,
    ) -> Callable[
        [analytics_admin.GetCustomMetricRequest], Awaitable[resources.CustomMetric]
    ]:
        r"""Return a callable for the get custom metric method over gRPC.

        Lookup for a single CustomMetric.

        Returns:
            Callable[[~.GetCustomMetricRequest],
                    Awaitable[~.CustomMetric]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_custom_metric" not in self._stubs:
            self._stubs["get_custom_metric"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/GetCustomMetric",
                request_serializer=analytics_admin.GetCustomMetricRequest.serialize,
                response_deserializer=resources.CustomMetric.deserialize,
            )
        return self._stubs["get_custom_metric"]

    @property
    def get_data_retention_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetDataRetentionSettingsRequest],
        Awaitable[resources.DataRetentionSettings],
    ]:
        r"""Return a callable for the get data retention settings method over gRPC.

        Returns the singleton data retention settings for
        this property.

        Returns:
            Callable[[~.GetDataRetentionSettingsRequest],
                    Awaitable[~.DataRetentionSettings]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_data_retention_settings" not in self._stubs:
            self._stubs["get_data_retention_settings"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/GetDataRetentionSettings",
                    request_serializer=analytics_admin.GetDataRetentionSettingsRequest.serialize,
                    response_deserializer=resources.DataRetentionSettings.deserialize,
                )
            )
        return self._stubs["get_data_retention_settings"]

    @property
    def update_data_retention_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateDataRetentionSettingsRequest],
        Awaitable[resources.DataRetentionSettings],
    ]:
        r"""Return a callable for the update data retention settings method over gRPC.

        Updates the singleton data retention settings for
        this property.

        Returns:
            Callable[[~.UpdateDataRetentionSettingsRequest],
                    Awaitable[~.DataRetentionSettings]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_data_retention_settings" not in self._stubs:
            self._stubs["update_data_retention_settings"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateDataRetentionSettings",
                    request_serializer=analytics_admin.UpdateDataRetentionSettingsRequest.serialize,
                    response_deserializer=resources.DataRetentionSettings.deserialize,
                )
            )
        return self._stubs["update_data_retention_settings"]

    @property
    def create_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.CreateDataStreamRequest], Awaitable[resources.DataStream]
    ]:
        r"""Return a callable for the create data stream method over gRPC.

        Creates a DataStream.

        Returns:
            Callable[[~.CreateDataStreamRequest],
                    Awaitable[~.DataStream]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_data_stream" not in self._stubs:
            self._stubs["create_data_stream"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/CreateDataStream",
                request_serializer=analytics_admin.CreateDataStreamRequest.serialize,
                response_deserializer=resources.DataStream.deserialize,
            )
        return self._stubs["create_data_stream"]

    @property
    def delete_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.DeleteDataStreamRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete data stream method over gRPC.

        Deletes a DataStream on a property.

        Returns:
            Callable[[~.DeleteDataStreamRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_data_stream" not in self._stubs:
            self._stubs["delete_data_stream"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/DeleteDataStream",
                request_serializer=analytics_admin.DeleteDataStreamRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_data_stream"]

    @property
    def update_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.UpdateDataStreamRequest], Awaitable[resources.DataStream]
    ]:
        r"""Return a callable for the update data stream method over gRPC.

        Updates a DataStream on a property.

        Returns:
            Callable[[~.UpdateDataStreamRequest],
                    Awaitable[~.DataStream]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_data_stream" not in self._stubs:
            self._stubs["update_data_stream"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/UpdateDataStream",
                request_serializer=analytics_admin.UpdateDataStreamRequest.serialize,
                response_deserializer=resources.DataStream.deserialize,
            )
        return self._stubs["update_data_stream"]

    @property
    def list_data_streams(
        self,
    ) -> Callable[
        [analytics_admin.ListDataStreamsRequest],
        Awaitable[analytics_admin.ListDataStreamsResponse],
    ]:
        r"""Return a callable for the list data streams method over gRPC.

        Lists DataStreams on a property.

        Returns:
            Callable[[~.ListDataStreamsRequest],
                    Awaitable[~.ListDataStreamsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_data_streams" not in self._stubs:
            self._stubs["list_data_streams"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/ListDataStreams",
                request_serializer=analytics_admin.ListDataStreamsRequest.serialize,
                response_deserializer=analytics_admin.ListDataStreamsResponse.deserialize,
            )
        return self._stubs["list_data_streams"]

    @property
    def get_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.GetDataStreamRequest], Awaitable[resources.DataStream]
    ]:
        r"""Return a callable for the get data stream method over gRPC.

        Lookup for a single DataStream.

        Returns:
            Callable[[~.GetDataStreamRequest],
                    Awaitable[~.DataStream]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_data_stream" not in self._stubs:
            self._stubs["get_data_stream"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/GetDataStream",
                request_serializer=analytics_admin.GetDataStreamRequest.serialize,
                response_deserializer=resources.DataStream.deserialize,
            )
        return self._stubs["get_data_stream"]

    @property
    def run_access_report(
        self,
    ) -> Callable[
        [analytics_admin.RunAccessReportRequest],
        Awaitable[analytics_admin.RunAccessReportResponse],
    ]:
        r"""Return a callable for the run access report method over gRPC.

        Returns a customized report of data access records. The report
        provides records of each time a user reads Google Analytics
        reporting data. Access records are retained for up to 2 years.

        Data Access Reports can be requested for a property. Reports may
        be requested for any property, but dimensions that aren't
        related to quota can only be requested on Google Analytics 360
        properties. This method is only available to Administrators.

        These data access records include GA UI Reporting, GA UI
        Explorations, GA Data API, and other products like Firebase &
        Admob that can retrieve data from Google Analytics through a
        linkage. These records don't include property configuration
        changes like adding a stream or changing a property's time zone.
        For configuration change history, see
        `searchChangeHistoryEvents <https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts/searchChangeHistoryEvents>`__.

        To give your feedback on this API, complete the `Google
        Analytics Access Reports
        feedback <https://docs.google.com/forms/d/e/1FAIpQLSdmEBUrMzAEdiEKk5TV5dEHvDUZDRlgWYdQdAeSdtR4hVjEhw/viewform>`__
        form.

        Returns:
            Callable[[~.RunAccessReportRequest],
                    Awaitable[~.RunAccessReportResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "run_access_report" not in self._stubs:
            self._stubs["run_access_report"] = self._logged_channel.unary_unary(
                "/google.analytics.admin.v1beta.AnalyticsAdminService/RunAccessReport",
                request_serializer=analytics_admin.RunAccessReportRequest.serialize,
                response_deserializer=analytics_admin.RunAccessReportResponse.deserialize,
            )
        return self._stubs["run_access_report"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.get_account: self._wrap_method(
                self.get_account,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_accounts: self._wrap_method(
                self.list_accounts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_account: self._wrap_method(
                self.delete_account,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_account: self._wrap_method(
                self.update_account,
                default_timeout=None,
                client_info=client_info,
            ),
            self.provision_account_ticket: self._wrap_method(
                self.provision_account_ticket,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_account_summaries: self._wrap_method(
                self.list_account_summaries,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_property: self._wrap_method(
                self.get_property,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_properties: self._wrap_method(
                self.list_properties,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_property: self._wrap_method(
                self.create_property,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_property: self._wrap_method(
                self.delete_property,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_property: self._wrap_method(
                self.update_property,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_firebase_link: self._wrap_method(
                self.create_firebase_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_firebase_link: self._wrap_method(
                self.delete_firebase_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_firebase_links: self._wrap_method(
                self.list_firebase_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_google_ads_link: self._wrap_method(
                self.create_google_ads_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_google_ads_link: self._wrap_method(
                self.update_google_ads_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_google_ads_link: self._wrap_method(
                self.delete_google_ads_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_google_ads_links: self._wrap_method(
                self.list_google_ads_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_data_sharing_settings: self._wrap_method(
                self.get_data_sharing_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_measurement_protocol_secret: self._wrap_method(
                self.get_measurement_protocol_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_measurement_protocol_secrets: self._wrap_method(
                self.list_measurement_protocol_secrets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_measurement_protocol_secret: self._wrap_method(
                self.create_measurement_protocol_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_measurement_protocol_secret: self._wrap_method(
                self.delete_measurement_protocol_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_measurement_protocol_secret: self._wrap_method(
                self.update_measurement_protocol_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.acknowledge_user_data_collection: self._wrap_method(
                self.acknowledge_user_data_collection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_change_history_events: self._wrap_method(
                self.search_change_history_events,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_conversion_event: self._wrap_method(
                self.create_conversion_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_conversion_event: self._wrap_method(
                self.update_conversion_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_conversion_event: self._wrap_method(
                self.get_conversion_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_conversion_event: self._wrap_method(
                self.delete_conversion_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_conversion_events: self._wrap_method(
                self.list_conversion_events,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_key_event: self._wrap_method(
                self.create_key_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_key_event: self._wrap_method(
                self.update_key_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_key_event: self._wrap_method(
                self.get_key_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_key_event: self._wrap_method(
                self.delete_key_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_key_events: self._wrap_method(
                self.list_key_events,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_custom_dimension: self._wrap_method(
                self.create_custom_dimension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_custom_dimension: self._wrap_method(
                self.update_custom_dimension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_custom_dimensions: self._wrap_method(
                self.list_custom_dimensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.archive_custom_dimension: self._wrap_method(
                self.archive_custom_dimension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_custom_dimension: self._wrap_method(
                self.get_custom_dimension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_custom_metric: self._wrap_method(
                self.create_custom_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_custom_metric: self._wrap_method(
                self.update_custom_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_custom_metrics: self._wrap_method(
                self.list_custom_metrics,
                default_timeout=None,
                client_info=client_info,
            ),
            self.archive_custom_metric: self._wrap_method(
                self.archive_custom_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_custom_metric: self._wrap_method(
                self.get_custom_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_data_retention_settings: self._wrap_method(
                self.get_data_retention_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_data_retention_settings: self._wrap_method(
                self.update_data_retention_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_data_stream: self._wrap_method(
                self.create_data_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_data_stream: self._wrap_method(
                self.delete_data_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_data_stream: self._wrap_method(
                self.update_data_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_data_streams: self._wrap_method(
                self.list_data_streams,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_data_stream: self._wrap_method(
                self.get_data_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.run_access_report: self._wrap_method(
                self.run_access_report,
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


__all__ = ("AnalyticsAdminServiceGrpcAsyncIOTransport",)
