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
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.gdchardwaremanagement_v1alpha.types import resources, service

from .base import DEFAULT_CLIENT_INFO, GDCHardwareManagementTransport

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
                    "serviceName": "google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement",
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
                    "serviceName": "google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class GDCHardwareManagementGrpcTransport(GDCHardwareManagementTransport):
    """gRPC backend transport for GDCHardwareManagement.

    The GDC Hardware Management service.

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
        host: str = "gdchardwaremanagement.googleapis.com",
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
                 The hostname to connect to (default: 'gdchardwaremanagement.googleapis.com').
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
        host: str = "gdchardwaremanagement.googleapis.com",
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
    def list_orders(
        self,
    ) -> Callable[[service.ListOrdersRequest], service.ListOrdersResponse]:
        r"""Return a callable for the list orders method over gRPC.

        Lists orders in a given project and location.

        Returns:
            Callable[[~.ListOrdersRequest],
                    ~.ListOrdersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_orders" not in self._stubs:
            self._stubs["list_orders"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListOrders",
                request_serializer=service.ListOrdersRequest.serialize,
                response_deserializer=service.ListOrdersResponse.deserialize,
            )
        return self._stubs["list_orders"]

    @property
    def get_order(self) -> Callable[[service.GetOrderRequest], resources.Order]:
        r"""Return a callable for the get order method over gRPC.

        Gets details of an order.

        Returns:
            Callable[[~.GetOrderRequest],
                    ~.Order]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_order" not in self._stubs:
            self._stubs["get_order"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetOrder",
                request_serializer=service.GetOrderRequest.serialize,
                response_deserializer=resources.Order.deserialize,
            )
        return self._stubs["get_order"]

    @property
    def create_order(
        self,
    ) -> Callable[[service.CreateOrderRequest], operations_pb2.Operation]:
        r"""Return a callable for the create order method over gRPC.

        Creates a new order in a given project and location.

        Returns:
            Callable[[~.CreateOrderRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_order" not in self._stubs:
            self._stubs["create_order"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateOrder",
                request_serializer=service.CreateOrderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_order"]

    @property
    def update_order(
        self,
    ) -> Callable[[service.UpdateOrderRequest], operations_pb2.Operation]:
        r"""Return a callable for the update order method over gRPC.

        Updates the parameters of an order.

        Returns:
            Callable[[~.UpdateOrderRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_order" not in self._stubs:
            self._stubs["update_order"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateOrder",
                request_serializer=service.UpdateOrderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_order"]

    @property
    def delete_order(
        self,
    ) -> Callable[[service.DeleteOrderRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete order method over gRPC.

        Deletes an order.

        Returns:
            Callable[[~.DeleteOrderRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_order" not in self._stubs:
            self._stubs["delete_order"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteOrder",
                request_serializer=service.DeleteOrderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_order"]

    @property
    def submit_order(
        self,
    ) -> Callable[[service.SubmitOrderRequest], operations_pb2.Operation]:
        r"""Return a callable for the submit order method over gRPC.

        Submits an order.

        Returns:
            Callable[[~.SubmitOrderRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "submit_order" not in self._stubs:
            self._stubs["submit_order"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/SubmitOrder",
                request_serializer=service.SubmitOrderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["submit_order"]

    @property
    def cancel_order(
        self,
    ) -> Callable[[service.CancelOrderRequest], operations_pb2.Operation]:
        r"""Return a callable for the cancel order method over gRPC.

        Cancels an order.

        Returns:
            Callable[[~.CancelOrderRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_order" not in self._stubs:
            self._stubs["cancel_order"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CancelOrder",
                request_serializer=service.CancelOrderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["cancel_order"]

    @property
    def list_sites(
        self,
    ) -> Callable[[service.ListSitesRequest], service.ListSitesResponse]:
        r"""Return a callable for the list sites method over gRPC.

        Lists sites in a given project and location.

        Returns:
            Callable[[~.ListSitesRequest],
                    ~.ListSitesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sites" not in self._stubs:
            self._stubs["list_sites"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListSites",
                request_serializer=service.ListSitesRequest.serialize,
                response_deserializer=service.ListSitesResponse.deserialize,
            )
        return self._stubs["list_sites"]

    @property
    def get_site(self) -> Callable[[service.GetSiteRequest], resources.Site]:
        r"""Return a callable for the get site method over gRPC.

        Gets details of a site.

        Returns:
            Callable[[~.GetSiteRequest],
                    ~.Site]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_site" not in self._stubs:
            self._stubs["get_site"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetSite",
                request_serializer=service.GetSiteRequest.serialize,
                response_deserializer=resources.Site.deserialize,
            )
        return self._stubs["get_site"]

    @property
    def create_site(
        self,
    ) -> Callable[[service.CreateSiteRequest], operations_pb2.Operation]:
        r"""Return a callable for the create site method over gRPC.

        Creates a new site in a given project and location.

        Returns:
            Callable[[~.CreateSiteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_site" not in self._stubs:
            self._stubs["create_site"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateSite",
                request_serializer=service.CreateSiteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_site"]

    @property
    def update_site(
        self,
    ) -> Callable[[service.UpdateSiteRequest], operations_pb2.Operation]:
        r"""Return a callable for the update site method over gRPC.

        Updates the parameters of a site.

        Returns:
            Callable[[~.UpdateSiteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_site" not in self._stubs:
            self._stubs["update_site"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateSite",
                request_serializer=service.UpdateSiteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_site"]

    @property
    def delete_site(
        self,
    ) -> Callable[[service.DeleteSiteRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete site method over gRPC.

        Deletes a site.

        Returns:
            Callable[[~.DeleteSiteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_site" not in self._stubs:
            self._stubs["delete_site"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteSite",
                request_serializer=service.DeleteSiteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_site"]

    @property
    def list_hardware_groups(
        self,
    ) -> Callable[
        [service.ListHardwareGroupsRequest], service.ListHardwareGroupsResponse
    ]:
        r"""Return a callable for the list hardware groups method over gRPC.

        Lists hardware groups in a given order.

        Returns:
            Callable[[~.ListHardwareGroupsRequest],
                    ~.ListHardwareGroupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hardware_groups" not in self._stubs:
            self._stubs["list_hardware_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListHardwareGroups",
                request_serializer=service.ListHardwareGroupsRequest.serialize,
                response_deserializer=service.ListHardwareGroupsResponse.deserialize,
            )
        return self._stubs["list_hardware_groups"]

    @property
    def get_hardware_group(
        self,
    ) -> Callable[[service.GetHardwareGroupRequest], resources.HardwareGroup]:
        r"""Return a callable for the get hardware group method over gRPC.

        Gets details of a hardware group.

        Returns:
            Callable[[~.GetHardwareGroupRequest],
                    ~.HardwareGroup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hardware_group" not in self._stubs:
            self._stubs["get_hardware_group"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetHardwareGroup",
                request_serializer=service.GetHardwareGroupRequest.serialize,
                response_deserializer=resources.HardwareGroup.deserialize,
            )
        return self._stubs["get_hardware_group"]

    @property
    def create_hardware_group(
        self,
    ) -> Callable[[service.CreateHardwareGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the create hardware group method over gRPC.

        Creates a new hardware group in a given order.

        Returns:
            Callable[[~.CreateHardwareGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hardware_group" not in self._stubs:
            self._stubs["create_hardware_group"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateHardwareGroup",
                request_serializer=service.CreateHardwareGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_hardware_group"]

    @property
    def update_hardware_group(
        self,
    ) -> Callable[[service.UpdateHardwareGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the update hardware group method over gRPC.

        Updates the parameters of a hardware group.

        Returns:
            Callable[[~.UpdateHardwareGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_hardware_group" not in self._stubs:
            self._stubs["update_hardware_group"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateHardwareGroup",
                request_serializer=service.UpdateHardwareGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_hardware_group"]

    @property
    def delete_hardware_group(
        self,
    ) -> Callable[[service.DeleteHardwareGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete hardware group method over gRPC.

        Deletes a hardware group.

        Returns:
            Callable[[~.DeleteHardwareGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_hardware_group" not in self._stubs:
            self._stubs["delete_hardware_group"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteHardwareGroup",
                request_serializer=service.DeleteHardwareGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_hardware_group"]

    @property
    def list_hardware(
        self,
    ) -> Callable[[service.ListHardwareRequest], service.ListHardwareResponse]:
        r"""Return a callable for the list hardware method over gRPC.

        Lists hardware in a given project and location.

        Returns:
            Callable[[~.ListHardwareRequest],
                    ~.ListHardwareResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hardware" not in self._stubs:
            self._stubs["list_hardware"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListHardware",
                request_serializer=service.ListHardwareRequest.serialize,
                response_deserializer=service.ListHardwareResponse.deserialize,
            )
        return self._stubs["list_hardware"]

    @property
    def get_hardware(
        self,
    ) -> Callable[[service.GetHardwareRequest], resources.Hardware]:
        r"""Return a callable for the get hardware method over gRPC.

        Gets hardware details.

        Returns:
            Callable[[~.GetHardwareRequest],
                    ~.Hardware]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hardware" not in self._stubs:
            self._stubs["get_hardware"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetHardware",
                request_serializer=service.GetHardwareRequest.serialize,
                response_deserializer=resources.Hardware.deserialize,
            )
        return self._stubs["get_hardware"]

    @property
    def create_hardware(
        self,
    ) -> Callable[[service.CreateHardwareRequest], operations_pb2.Operation]:
        r"""Return a callable for the create hardware method over gRPC.

        Creates new hardware in a given project and location.

        Returns:
            Callable[[~.CreateHardwareRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hardware" not in self._stubs:
            self._stubs["create_hardware"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateHardware",
                request_serializer=service.CreateHardwareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_hardware"]

    @property
    def update_hardware(
        self,
    ) -> Callable[[service.UpdateHardwareRequest], operations_pb2.Operation]:
        r"""Return a callable for the update hardware method over gRPC.

        Updates hardware parameters.

        Returns:
            Callable[[~.UpdateHardwareRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_hardware" not in self._stubs:
            self._stubs["update_hardware"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateHardware",
                request_serializer=service.UpdateHardwareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_hardware"]

    @property
    def delete_hardware(
        self,
    ) -> Callable[[service.DeleteHardwareRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete hardware method over gRPC.

        Deletes hardware.

        Returns:
            Callable[[~.DeleteHardwareRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_hardware" not in self._stubs:
            self._stubs["delete_hardware"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteHardware",
                request_serializer=service.DeleteHardwareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_hardware"]

    @property
    def list_comments(
        self,
    ) -> Callable[[service.ListCommentsRequest], service.ListCommentsResponse]:
        r"""Return a callable for the list comments method over gRPC.

        Lists the comments on an order.

        Returns:
            Callable[[~.ListCommentsRequest],
                    ~.ListCommentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_comments" not in self._stubs:
            self._stubs["list_comments"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListComments",
                request_serializer=service.ListCommentsRequest.serialize,
                response_deserializer=service.ListCommentsResponse.deserialize,
            )
        return self._stubs["list_comments"]

    @property
    def get_comment(self) -> Callable[[service.GetCommentRequest], resources.Comment]:
        r"""Return a callable for the get comment method over gRPC.

        Gets the content of a comment.

        Returns:
            Callable[[~.GetCommentRequest],
                    ~.Comment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_comment" not in self._stubs:
            self._stubs["get_comment"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetComment",
                request_serializer=service.GetCommentRequest.serialize,
                response_deserializer=resources.Comment.deserialize,
            )
        return self._stubs["get_comment"]

    @property
    def create_comment(
        self,
    ) -> Callable[[service.CreateCommentRequest], operations_pb2.Operation]:
        r"""Return a callable for the create comment method over gRPC.

        Creates a new comment on an order.

        Returns:
            Callable[[~.CreateCommentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_comment" not in self._stubs:
            self._stubs["create_comment"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateComment",
                request_serializer=service.CreateCommentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_comment"]

    @property
    def record_action_on_comment(
        self,
    ) -> Callable[[service.RecordActionOnCommentRequest], resources.Comment]:
        r"""Return a callable for the record action on comment method over gRPC.

        Record Action on a Comment. If the Action specified
        in the request is READ, the viewed time in the comment
        is set to the time the request was received. If the
        comment is already marked as read, subsequent calls will
        be ignored. If the Action is UNREAD, the viewed time is
        cleared from the comment.

        Returns:
            Callable[[~.RecordActionOnCommentRequest],
                    ~.Comment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "record_action_on_comment" not in self._stubs:
            self._stubs["record_action_on_comment"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/RecordActionOnComment",
                request_serializer=service.RecordActionOnCommentRequest.serialize,
                response_deserializer=resources.Comment.deserialize,
            )
        return self._stubs["record_action_on_comment"]

    @property
    def list_change_log_entries(
        self,
    ) -> Callable[
        [service.ListChangeLogEntriesRequest], service.ListChangeLogEntriesResponse
    ]:
        r"""Return a callable for the list change log entries method over gRPC.

        Lists the changes made to an order.

        Returns:
            Callable[[~.ListChangeLogEntriesRequest],
                    ~.ListChangeLogEntriesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_change_log_entries" not in self._stubs:
            self._stubs["list_change_log_entries"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListChangeLogEntries",
                request_serializer=service.ListChangeLogEntriesRequest.serialize,
                response_deserializer=service.ListChangeLogEntriesResponse.deserialize,
            )
        return self._stubs["list_change_log_entries"]

    @property
    def get_change_log_entry(
        self,
    ) -> Callable[[service.GetChangeLogEntryRequest], resources.ChangeLogEntry]:
        r"""Return a callable for the get change log entry method over gRPC.

        Gets details of a change to an order.

        Returns:
            Callable[[~.GetChangeLogEntryRequest],
                    ~.ChangeLogEntry]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_change_log_entry" not in self._stubs:
            self._stubs["get_change_log_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetChangeLogEntry",
                request_serializer=service.GetChangeLogEntryRequest.serialize,
                response_deserializer=resources.ChangeLogEntry.deserialize,
            )
        return self._stubs["get_change_log_entry"]

    @property
    def list_skus(
        self,
    ) -> Callable[[service.ListSkusRequest], service.ListSkusResponse]:
        r"""Return a callable for the list skus method over gRPC.

        Lists SKUs for a given project and location.

        Returns:
            Callable[[~.ListSkusRequest],
                    ~.ListSkusResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_skus" not in self._stubs:
            self._stubs["list_skus"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListSkus",
                request_serializer=service.ListSkusRequest.serialize,
                response_deserializer=service.ListSkusResponse.deserialize,
            )
        return self._stubs["list_skus"]

    @property
    def get_sku(self) -> Callable[[service.GetSkuRequest], resources.Sku]:
        r"""Return a callable for the get sku method over gRPC.

        Gets details of an SKU.

        Returns:
            Callable[[~.GetSkuRequest],
                    ~.Sku]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_sku" not in self._stubs:
            self._stubs["get_sku"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetSku",
                request_serializer=service.GetSkuRequest.serialize,
                response_deserializer=resources.Sku.deserialize,
            )
        return self._stubs["get_sku"]

    @property
    def list_zones(
        self,
    ) -> Callable[[service.ListZonesRequest], service.ListZonesResponse]:
        r"""Return a callable for the list zones method over gRPC.

        Lists zones in a given project and location.

        Returns:
            Callable[[~.ListZonesRequest],
                    ~.ListZonesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_zones" not in self._stubs:
            self._stubs["list_zones"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListZones",
                request_serializer=service.ListZonesRequest.serialize,
                response_deserializer=service.ListZonesResponse.deserialize,
            )
        return self._stubs["list_zones"]

    @property
    def get_zone(self) -> Callable[[service.GetZoneRequest], resources.Zone]:
        r"""Return a callable for the get zone method over gRPC.

        Gets details of a zone.

        Returns:
            Callable[[~.GetZoneRequest],
                    ~.Zone]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_zone" not in self._stubs:
            self._stubs["get_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetZone",
                request_serializer=service.GetZoneRequest.serialize,
                response_deserializer=resources.Zone.deserialize,
            )
        return self._stubs["get_zone"]

    @property
    def create_zone(
        self,
    ) -> Callable[[service.CreateZoneRequest], operations_pb2.Operation]:
        r"""Return a callable for the create zone method over gRPC.

        Creates a new zone in a given project and location.

        Returns:
            Callable[[~.CreateZoneRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_zone" not in self._stubs:
            self._stubs["create_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateZone",
                request_serializer=service.CreateZoneRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_zone"]

    @property
    def update_zone(
        self,
    ) -> Callable[[service.UpdateZoneRequest], operations_pb2.Operation]:
        r"""Return a callable for the update zone method over gRPC.

        Updates the parameters of a zone.

        Returns:
            Callable[[~.UpdateZoneRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_zone" not in self._stubs:
            self._stubs["update_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateZone",
                request_serializer=service.UpdateZoneRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_zone"]

    @property
    def delete_zone(
        self,
    ) -> Callable[[service.DeleteZoneRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete zone method over gRPC.

        Deletes a zone.

        Returns:
            Callable[[~.DeleteZoneRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_zone" not in self._stubs:
            self._stubs["delete_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteZone",
                request_serializer=service.DeleteZoneRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_zone"]

    @property
    def signal_zone_state(
        self,
    ) -> Callable[[service.SignalZoneStateRequest], operations_pb2.Operation]:
        r"""Return a callable for the signal zone state method over gRPC.

        Signals the state of a zone.

        Returns:
            Callable[[~.SignalZoneStateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "signal_zone_state" not in self._stubs:
            self._stubs["signal_zone_state"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/SignalZoneState",
                request_serializer=service.SignalZoneStateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["signal_zone_state"]

    @property
    def request_order_date_change(
        self,
    ) -> Callable[[service.RequestOrderDateChangeRequest], operations_pb2.Operation]:
        r"""Return a callable for the request order date change method over gRPC.

        Updates the requested date change of a single Order.

        Returns:
            Callable[[~.RequestOrderDateChangeRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "request_order_date_change" not in self._stubs:
            self._stubs["request_order_date_change"] = self._logged_channel.unary_unary(
                "/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/RequestOrderDateChange",
                request_serializer=service.RequestOrderDateChangeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["request_order_date_change"]

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


__all__ = ("GDCHardwareManagementGrpcTransport",)
