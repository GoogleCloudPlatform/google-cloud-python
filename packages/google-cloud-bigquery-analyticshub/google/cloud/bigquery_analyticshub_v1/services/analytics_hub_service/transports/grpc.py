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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.bigquery_analyticshub_v1.types import analyticshub

from .base import DEFAULT_CLIENT_INFO, AnalyticsHubServiceTransport

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
                    "serviceName": "google.cloud.bigquery.analyticshub.v1.AnalyticsHubService",
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
                    "serviceName": "google.cloud.bigquery.analyticshub.v1.AnalyticsHubService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AnalyticsHubServiceGrpcTransport(AnalyticsHubServiceTransport):
    """gRPC backend transport for AnalyticsHubService.

    The ``AnalyticsHubService`` API facilitates data sharing within and
    across organizations. It allows data providers to publish listings
    that reference shared datasets. With Analytics Hub, users can
    discover and search for listings that they have access to.
    Subscribers can view and subscribe to listings. When you subscribe
    to a listing, Analytics Hub creates a linked dataset in your
    project.

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
        host: str = "analyticshub.googleapis.com",
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
                 The hostname to connect to (default: 'analyticshub.googleapis.com').
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
        host: str = "analyticshub.googleapis.com",
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
    def list_data_exchanges(
        self,
    ) -> Callable[
        [analyticshub.ListDataExchangesRequest], analyticshub.ListDataExchangesResponse
    ]:
        r"""Return a callable for the list data exchanges method over gRPC.

        Lists all data exchanges in a given project and
        location.

        Returns:
            Callable[[~.ListDataExchangesRequest],
                    ~.ListDataExchangesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_data_exchanges" not in self._stubs:
            self._stubs["list_data_exchanges"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/ListDataExchanges",
                request_serializer=analyticshub.ListDataExchangesRequest.serialize,
                response_deserializer=analyticshub.ListDataExchangesResponse.deserialize,
            )
        return self._stubs["list_data_exchanges"]

    @property
    def list_org_data_exchanges(
        self,
    ) -> Callable[
        [analyticshub.ListOrgDataExchangesRequest],
        analyticshub.ListOrgDataExchangesResponse,
    ]:
        r"""Return a callable for the list org data exchanges method over gRPC.

        Lists all data exchanges from projects in a given
        organization and location.

        Returns:
            Callable[[~.ListOrgDataExchangesRequest],
                    ~.ListOrgDataExchangesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_org_data_exchanges" not in self._stubs:
            self._stubs["list_org_data_exchanges"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/ListOrgDataExchanges",
                request_serializer=analyticshub.ListOrgDataExchangesRequest.serialize,
                response_deserializer=analyticshub.ListOrgDataExchangesResponse.deserialize,
            )
        return self._stubs["list_org_data_exchanges"]

    @property
    def get_data_exchange(
        self,
    ) -> Callable[[analyticshub.GetDataExchangeRequest], analyticshub.DataExchange]:
        r"""Return a callable for the get data exchange method over gRPC.

        Gets the details of a data exchange.

        Returns:
            Callable[[~.GetDataExchangeRequest],
                    ~.DataExchange]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_data_exchange" not in self._stubs:
            self._stubs["get_data_exchange"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/GetDataExchange",
                request_serializer=analyticshub.GetDataExchangeRequest.serialize,
                response_deserializer=analyticshub.DataExchange.deserialize,
            )
        return self._stubs["get_data_exchange"]

    @property
    def create_data_exchange(
        self,
    ) -> Callable[[analyticshub.CreateDataExchangeRequest], analyticshub.DataExchange]:
        r"""Return a callable for the create data exchange method over gRPC.

        Creates a new data exchange.

        Returns:
            Callable[[~.CreateDataExchangeRequest],
                    ~.DataExchange]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_data_exchange" not in self._stubs:
            self._stubs["create_data_exchange"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/CreateDataExchange",
                request_serializer=analyticshub.CreateDataExchangeRequest.serialize,
                response_deserializer=analyticshub.DataExchange.deserialize,
            )
        return self._stubs["create_data_exchange"]

    @property
    def update_data_exchange(
        self,
    ) -> Callable[[analyticshub.UpdateDataExchangeRequest], analyticshub.DataExchange]:
        r"""Return a callable for the update data exchange method over gRPC.

        Updates an existing data exchange.

        Returns:
            Callable[[~.UpdateDataExchangeRequest],
                    ~.DataExchange]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_data_exchange" not in self._stubs:
            self._stubs["update_data_exchange"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/UpdateDataExchange",
                request_serializer=analyticshub.UpdateDataExchangeRequest.serialize,
                response_deserializer=analyticshub.DataExchange.deserialize,
            )
        return self._stubs["update_data_exchange"]

    @property
    def delete_data_exchange(
        self,
    ) -> Callable[[analyticshub.DeleteDataExchangeRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete data exchange method over gRPC.

        Deletes an existing data exchange.

        Returns:
            Callable[[~.DeleteDataExchangeRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_data_exchange" not in self._stubs:
            self._stubs["delete_data_exchange"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/DeleteDataExchange",
                request_serializer=analyticshub.DeleteDataExchangeRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_data_exchange"]

    @property
    def list_listings(
        self,
    ) -> Callable[
        [analyticshub.ListListingsRequest], analyticshub.ListListingsResponse
    ]:
        r"""Return a callable for the list listings method over gRPC.

        Lists all listings in a given project and location.

        Returns:
            Callable[[~.ListListingsRequest],
                    ~.ListListingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_listings" not in self._stubs:
            self._stubs["list_listings"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/ListListings",
                request_serializer=analyticshub.ListListingsRequest.serialize,
                response_deserializer=analyticshub.ListListingsResponse.deserialize,
            )
        return self._stubs["list_listings"]

    @property
    def get_listing(
        self,
    ) -> Callable[[analyticshub.GetListingRequest], analyticshub.Listing]:
        r"""Return a callable for the get listing method over gRPC.

        Gets the details of a listing.

        Returns:
            Callable[[~.GetListingRequest],
                    ~.Listing]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_listing" not in self._stubs:
            self._stubs["get_listing"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/GetListing",
                request_serializer=analyticshub.GetListingRequest.serialize,
                response_deserializer=analyticshub.Listing.deserialize,
            )
        return self._stubs["get_listing"]

    @property
    def create_listing(
        self,
    ) -> Callable[[analyticshub.CreateListingRequest], analyticshub.Listing]:
        r"""Return a callable for the create listing method over gRPC.

        Creates a new listing.

        Returns:
            Callable[[~.CreateListingRequest],
                    ~.Listing]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_listing" not in self._stubs:
            self._stubs["create_listing"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/CreateListing",
                request_serializer=analyticshub.CreateListingRequest.serialize,
                response_deserializer=analyticshub.Listing.deserialize,
            )
        return self._stubs["create_listing"]

    @property
    def update_listing(
        self,
    ) -> Callable[[analyticshub.UpdateListingRequest], analyticshub.Listing]:
        r"""Return a callable for the update listing method over gRPC.

        Updates an existing listing.

        Returns:
            Callable[[~.UpdateListingRequest],
                    ~.Listing]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_listing" not in self._stubs:
            self._stubs["update_listing"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/UpdateListing",
                request_serializer=analyticshub.UpdateListingRequest.serialize,
                response_deserializer=analyticshub.Listing.deserialize,
            )
        return self._stubs["update_listing"]

    @property
    def delete_listing(
        self,
    ) -> Callable[[analyticshub.DeleteListingRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete listing method over gRPC.

        Deletes a listing.

        Returns:
            Callable[[~.DeleteListingRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_listing" not in self._stubs:
            self._stubs["delete_listing"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/DeleteListing",
                request_serializer=analyticshub.DeleteListingRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_listing"]

    @property
    def subscribe_listing(
        self,
    ) -> Callable[
        [analyticshub.SubscribeListingRequest], analyticshub.SubscribeListingResponse
    ]:
        r"""Return a callable for the subscribe listing method over gRPC.

        Subscribes to a listing.

        Currently, with Analytics Hub, you can create listings
        that reference only BigQuery datasets.
        Upon subscription to a listing for a BigQuery dataset,
        Analytics Hub creates a linked dataset in the
        subscriber's project.

        Returns:
            Callable[[~.SubscribeListingRequest],
                    ~.SubscribeListingResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "subscribe_listing" not in self._stubs:
            self._stubs["subscribe_listing"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/SubscribeListing",
                request_serializer=analyticshub.SubscribeListingRequest.serialize,
                response_deserializer=analyticshub.SubscribeListingResponse.deserialize,
            )
        return self._stubs["subscribe_listing"]

    @property
    def subscribe_data_exchange(
        self,
    ) -> Callable[
        [analyticshub.SubscribeDataExchangeRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the subscribe data exchange method over gRPC.

        Creates a Subscription to a Data Clean Room. This is
        a long-running operation as it will create one or more
        linked datasets. Throws a Bad Request error if the Data
        Exchange does not contain any listings.

        Returns:
            Callable[[~.SubscribeDataExchangeRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "subscribe_data_exchange" not in self._stubs:
            self._stubs["subscribe_data_exchange"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/SubscribeDataExchange",
                request_serializer=analyticshub.SubscribeDataExchangeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["subscribe_data_exchange"]

    @property
    def refresh_subscription(
        self,
    ) -> Callable[[analyticshub.RefreshSubscriptionRequest], operations_pb2.Operation]:
        r"""Return a callable for the refresh subscription method over gRPC.

        Refreshes a Subscription to a Data Exchange. A Data
        Exchange can become stale when a publisher adds or
        removes data. This is a long-running operation as it may
        create many linked datasets.

        Returns:
            Callable[[~.RefreshSubscriptionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "refresh_subscription" not in self._stubs:
            self._stubs["refresh_subscription"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/RefreshSubscription",
                request_serializer=analyticshub.RefreshSubscriptionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["refresh_subscription"]

    @property
    def get_subscription(
        self,
    ) -> Callable[[analyticshub.GetSubscriptionRequest], analyticshub.Subscription]:
        r"""Return a callable for the get subscription method over gRPC.

        Gets the details of a Subscription.

        Returns:
            Callable[[~.GetSubscriptionRequest],
                    ~.Subscription]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_subscription" not in self._stubs:
            self._stubs["get_subscription"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/GetSubscription",
                request_serializer=analyticshub.GetSubscriptionRequest.serialize,
                response_deserializer=analyticshub.Subscription.deserialize,
            )
        return self._stubs["get_subscription"]

    @property
    def list_subscriptions(
        self,
    ) -> Callable[
        [analyticshub.ListSubscriptionsRequest], analyticshub.ListSubscriptionsResponse
    ]:
        r"""Return a callable for the list subscriptions method over gRPC.

        Lists all subscriptions in a given project and
        location.

        Returns:
            Callable[[~.ListSubscriptionsRequest],
                    ~.ListSubscriptionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_subscriptions" not in self._stubs:
            self._stubs["list_subscriptions"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/ListSubscriptions",
                request_serializer=analyticshub.ListSubscriptionsRequest.serialize,
                response_deserializer=analyticshub.ListSubscriptionsResponse.deserialize,
            )
        return self._stubs["list_subscriptions"]

    @property
    def list_shared_resource_subscriptions(
        self,
    ) -> Callable[
        [analyticshub.ListSharedResourceSubscriptionsRequest],
        analyticshub.ListSharedResourceSubscriptionsResponse,
    ]:
        r"""Return a callable for the list shared resource
        subscriptions method over gRPC.

        Lists all subscriptions on a given Data Exchange or
        Listing.

        Returns:
            Callable[[~.ListSharedResourceSubscriptionsRequest],
                    ~.ListSharedResourceSubscriptionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_shared_resource_subscriptions" not in self._stubs:
            self._stubs["list_shared_resource_subscriptions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/ListSharedResourceSubscriptions",
                    request_serializer=analyticshub.ListSharedResourceSubscriptionsRequest.serialize,
                    response_deserializer=analyticshub.ListSharedResourceSubscriptionsResponse.deserialize,
                )
            )
        return self._stubs["list_shared_resource_subscriptions"]

    @property
    def revoke_subscription(
        self,
    ) -> Callable[
        [analyticshub.RevokeSubscriptionRequest],
        analyticshub.RevokeSubscriptionResponse,
    ]:
        r"""Return a callable for the revoke subscription method over gRPC.

        Revokes a given subscription.

        Returns:
            Callable[[~.RevokeSubscriptionRequest],
                    ~.RevokeSubscriptionResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "revoke_subscription" not in self._stubs:
            self._stubs["revoke_subscription"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/RevokeSubscription",
                request_serializer=analyticshub.RevokeSubscriptionRequest.serialize,
                response_deserializer=analyticshub.RevokeSubscriptionResponse.deserialize,
            )
        return self._stubs["revoke_subscription"]

    @property
    def delete_subscription(
        self,
    ) -> Callable[[analyticshub.DeleteSubscriptionRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete subscription method over gRPC.

        Deletes a subscription.

        Returns:
            Callable[[~.DeleteSubscriptionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_subscription" not in self._stubs:
            self._stubs["delete_subscription"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/DeleteSubscription",
                request_serializer=analyticshub.DeleteSubscriptionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_subscription"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the IAM policy.

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
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the IAM policy.

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
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/SetIamPolicy",
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

        Returns the permissions that a caller has.

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
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def create_query_template(
        self,
    ) -> Callable[
        [analyticshub.CreateQueryTemplateRequest], analyticshub.QueryTemplate
    ]:
        r"""Return a callable for the create query template method over gRPC.

        Creates a new QueryTemplate

        Returns:
            Callable[[~.CreateQueryTemplateRequest],
                    ~.QueryTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_query_template" not in self._stubs:
            self._stubs["create_query_template"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/CreateQueryTemplate",
                request_serializer=analyticshub.CreateQueryTemplateRequest.serialize,
                response_deserializer=analyticshub.QueryTemplate.deserialize,
            )
        return self._stubs["create_query_template"]

    @property
    def get_query_template(
        self,
    ) -> Callable[[analyticshub.GetQueryTemplateRequest], analyticshub.QueryTemplate]:
        r"""Return a callable for the get query template method over gRPC.

        Gets a QueryTemplate

        Returns:
            Callable[[~.GetQueryTemplateRequest],
                    ~.QueryTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_query_template" not in self._stubs:
            self._stubs["get_query_template"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/GetQueryTemplate",
                request_serializer=analyticshub.GetQueryTemplateRequest.serialize,
                response_deserializer=analyticshub.QueryTemplate.deserialize,
            )
        return self._stubs["get_query_template"]

    @property
    def list_query_templates(
        self,
    ) -> Callable[
        [analyticshub.ListQueryTemplatesRequest],
        analyticshub.ListQueryTemplatesResponse,
    ]:
        r"""Return a callable for the list query templates method over gRPC.

        Lists all QueryTemplates in a given project and
        location.

        Returns:
            Callable[[~.ListQueryTemplatesRequest],
                    ~.ListQueryTemplatesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_query_templates" not in self._stubs:
            self._stubs["list_query_templates"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/ListQueryTemplates",
                request_serializer=analyticshub.ListQueryTemplatesRequest.serialize,
                response_deserializer=analyticshub.ListQueryTemplatesResponse.deserialize,
            )
        return self._stubs["list_query_templates"]

    @property
    def update_query_template(
        self,
    ) -> Callable[
        [analyticshub.UpdateQueryTemplateRequest], analyticshub.QueryTemplate
    ]:
        r"""Return a callable for the update query template method over gRPC.

        Updates an existing QueryTemplate

        Returns:
            Callable[[~.UpdateQueryTemplateRequest],
                    ~.QueryTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_query_template" not in self._stubs:
            self._stubs["update_query_template"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/UpdateQueryTemplate",
                request_serializer=analyticshub.UpdateQueryTemplateRequest.serialize,
                response_deserializer=analyticshub.QueryTemplate.deserialize,
            )
        return self._stubs["update_query_template"]

    @property
    def delete_query_template(
        self,
    ) -> Callable[[analyticshub.DeleteQueryTemplateRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete query template method over gRPC.

        Deletes a query template.

        Returns:
            Callable[[~.DeleteQueryTemplateRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_query_template" not in self._stubs:
            self._stubs["delete_query_template"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/DeleteQueryTemplate",
                request_serializer=analyticshub.DeleteQueryTemplateRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_query_template"]

    @property
    def submit_query_template(
        self,
    ) -> Callable[
        [analyticshub.SubmitQueryTemplateRequest], analyticshub.QueryTemplate
    ]:
        r"""Return a callable for the submit query template method over gRPC.

        Submits a query template for approval.

        Returns:
            Callable[[~.SubmitQueryTemplateRequest],
                    ~.QueryTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "submit_query_template" not in self._stubs:
            self._stubs["submit_query_template"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/SubmitQueryTemplate",
                request_serializer=analyticshub.SubmitQueryTemplateRequest.serialize,
                response_deserializer=analyticshub.QueryTemplate.deserialize,
            )
        return self._stubs["submit_query_template"]

    @property
    def approve_query_template(
        self,
    ) -> Callable[
        [analyticshub.ApproveQueryTemplateRequest], analyticshub.QueryTemplate
    ]:
        r"""Return a callable for the approve query template method over gRPC.

        Approves a query template.

        Returns:
            Callable[[~.ApproveQueryTemplateRequest],
                    ~.QueryTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "approve_query_template" not in self._stubs:
            self._stubs["approve_query_template"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.analyticshub.v1.AnalyticsHubService/ApproveQueryTemplate",
                request_serializer=analyticshub.ApproveQueryTemplateRequest.serialize,
                response_deserializer=analyticshub.QueryTemplate.deserialize,
            )
        return self._stubs["approve_query_template"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("AnalyticsHubServiceGrpcTransport",)
