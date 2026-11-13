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

import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
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

from google.cloud.bigquery_reservation_v1.types import reservation
from google.cloud.bigquery_reservation_v1.types import reservation as gcbr_reservation

from .base import DEFAULT_CLIENT_INFO, ReservationServiceTransport
from .grpc import ReservationServiceGrpcTransport

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
                    "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
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
                    "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ReservationServiceGrpcAsyncIOTransport(ReservationServiceTransport):
    """gRPC AsyncIO backend transport for ReservationService.

    This API allows users to manage their BigQuery reservations.

    A reservation provides computational resource guarantees, in the
    form of `slots <https://cloud.google.com/bigquery/docs/slots>`__, to
    users. A slot is a unit of computational power in BigQuery, and
    serves as the basic unit of parallelism. In a scan of a
    multi-partitioned table, a single slot operates on a single
    partition of the table. A reservation resource exists as a child
    resource of the admin project and location, e.g.:
    ``projects/myproject/locations/US/reservations/reservationName``.

    A capacity commitment is a way to purchase compute capacity for
    BigQuery jobs (in the form of slots) with some committed period of
    usage. A capacity commitment resource exists as a child resource of
    the admin project and location, e.g.:
    ``projects/myproject/locations/US/capacityCommitments/id``.

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
        host: str = "bigqueryreservation.googleapis.com",
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
        host: str = "bigqueryreservation.googleapis.com",
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
                 The hostname to connect to (default: 'bigqueryreservation.googleapis.com').
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
    def create_reservation(
        self,
    ) -> Callable[
        [gcbr_reservation.CreateReservationRequest],
        Awaitable[gcbr_reservation.Reservation],
    ]:
        r"""Return a callable for the create reservation method over gRPC.

        Creates a new reservation resource.

        Returns:
            Callable[[~.CreateReservationRequest],
                    Awaitable[~.Reservation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_reservation" not in self._stubs:
            self._stubs["create_reservation"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateReservation",
                request_serializer=gcbr_reservation.CreateReservationRequest.serialize,
                response_deserializer=gcbr_reservation.Reservation.deserialize,
            )
        return self._stubs["create_reservation"]

    @property
    def list_reservations(
        self,
    ) -> Callable[
        [reservation.ListReservationsRequest],
        Awaitable[reservation.ListReservationsResponse],
    ]:
        r"""Return a callable for the list reservations method over gRPC.

        Lists all the reservations for the project in the
        specified location.

        Returns:
            Callable[[~.ListReservationsRequest],
                    Awaitable[~.ListReservationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_reservations" not in self._stubs:
            self._stubs["list_reservations"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListReservations",
                request_serializer=reservation.ListReservationsRequest.serialize,
                response_deserializer=reservation.ListReservationsResponse.deserialize,
            )
        return self._stubs["list_reservations"]

    @property
    def get_reservation(
        self,
    ) -> Callable[
        [reservation.GetReservationRequest], Awaitable[reservation.Reservation]
    ]:
        r"""Return a callable for the get reservation method over gRPC.

        Returns information about the reservation.

        Returns:
            Callable[[~.GetReservationRequest],
                    Awaitable[~.Reservation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_reservation" not in self._stubs:
            self._stubs["get_reservation"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetReservation",
                request_serializer=reservation.GetReservationRequest.serialize,
                response_deserializer=reservation.Reservation.deserialize,
            )
        return self._stubs["get_reservation"]

    @property
    def delete_reservation(
        self,
    ) -> Callable[[reservation.DeleteReservationRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete reservation method over gRPC.

        Deletes a reservation. Returns
        ``google.rpc.Code.FAILED_PRECONDITION`` when reservation has
        assignments.

        Returns:
            Callable[[~.DeleteReservationRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_reservation" not in self._stubs:
            self._stubs["delete_reservation"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteReservation",
                request_serializer=reservation.DeleteReservationRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_reservation"]

    @property
    def update_reservation(
        self,
    ) -> Callable[
        [gcbr_reservation.UpdateReservationRequest],
        Awaitable[gcbr_reservation.Reservation],
    ]:
        r"""Return a callable for the update reservation method over gRPC.

        Updates an existing reservation resource.

        Returns:
            Callable[[~.UpdateReservationRequest],
                    Awaitable[~.Reservation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_reservation" not in self._stubs:
            self._stubs["update_reservation"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateReservation",
                request_serializer=gcbr_reservation.UpdateReservationRequest.serialize,
                response_deserializer=gcbr_reservation.Reservation.deserialize,
            )
        return self._stubs["update_reservation"]

    @property
    def failover_reservation(
        self,
    ) -> Callable[
        [reservation.FailoverReservationRequest], Awaitable[reservation.Reservation]
    ]:
        r"""Return a callable for the failover reservation method over gRPC.

        Fail over a reservation to the secondary location. The operation
        should be done in the current secondary location, which will be
        promoted to the new primary location for the reservation.
        Attempting to failover a reservation in the current primary
        location will fail with the error code
        ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.FailoverReservationRequest],
                    Awaitable[~.Reservation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "failover_reservation" not in self._stubs:
            self._stubs["failover_reservation"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/FailoverReservation",
                request_serializer=reservation.FailoverReservationRequest.serialize,
                response_deserializer=reservation.Reservation.deserialize,
            )
        return self._stubs["failover_reservation"]

    @property
    def create_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.CreateCapacityCommitmentRequest],
        Awaitable[reservation.CapacityCommitment],
    ]:
        r"""Return a callable for the create capacity commitment method over gRPC.

        Creates a new capacity commitment resource.

        Returns:
            Callable[[~.CreateCapacityCommitmentRequest],
                    Awaitable[~.CapacityCommitment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_capacity_commitment" not in self._stubs:
            self._stubs["create_capacity_commitment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.bigquery.reservation.v1.ReservationService/CreateCapacityCommitment",
                    request_serializer=reservation.CreateCapacityCommitmentRequest.serialize,
                    response_deserializer=reservation.CapacityCommitment.deserialize,
                )
            )
        return self._stubs["create_capacity_commitment"]

    @property
    def list_capacity_commitments(
        self,
    ) -> Callable[
        [reservation.ListCapacityCommitmentsRequest],
        Awaitable[reservation.ListCapacityCommitmentsResponse],
    ]:
        r"""Return a callable for the list capacity commitments method over gRPC.

        Lists all the capacity commitments for the admin
        project.

        Returns:
            Callable[[~.ListCapacityCommitmentsRequest],
                    Awaitable[~.ListCapacityCommitmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_capacity_commitments" not in self._stubs:
            self._stubs["list_capacity_commitments"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListCapacityCommitments",
                request_serializer=reservation.ListCapacityCommitmentsRequest.serialize,
                response_deserializer=reservation.ListCapacityCommitmentsResponse.deserialize,
            )
        return self._stubs["list_capacity_commitments"]

    @property
    def get_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.GetCapacityCommitmentRequest],
        Awaitable[reservation.CapacityCommitment],
    ]:
        r"""Return a callable for the get capacity commitment method over gRPC.

        Returns information about the capacity commitment.

        Returns:
            Callable[[~.GetCapacityCommitmentRequest],
                    Awaitable[~.CapacityCommitment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_capacity_commitment" not in self._stubs:
            self._stubs["get_capacity_commitment"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetCapacityCommitment",
                request_serializer=reservation.GetCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["get_capacity_commitment"]

    @property
    def delete_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.DeleteCapacityCommitmentRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete capacity commitment method over gRPC.

        Deletes a capacity commitment. Attempting to delete capacity
        commitment before its commitment_end_time will fail with the
        error code ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.DeleteCapacityCommitmentRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_capacity_commitment" not in self._stubs:
            self._stubs["delete_capacity_commitment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteCapacityCommitment",
                    request_serializer=reservation.DeleteCapacityCommitmentRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_capacity_commitment"]

    @property
    def update_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.UpdateCapacityCommitmentRequest],
        Awaitable[reservation.CapacityCommitment],
    ]:
        r"""Return a callable for the update capacity commitment method over gRPC.

        Updates an existing capacity commitment.

        Only ``plan`` and ``renewal_plan`` fields can be updated.

        Plan can only be changed to a plan of a longer commitment
        period. Attempting to change to a plan with shorter commitment
        period will fail with the error code
        ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.UpdateCapacityCommitmentRequest],
                    Awaitable[~.CapacityCommitment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_capacity_commitment" not in self._stubs:
            self._stubs["update_capacity_commitment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateCapacityCommitment",
                    request_serializer=reservation.UpdateCapacityCommitmentRequest.serialize,
                    response_deserializer=reservation.CapacityCommitment.deserialize,
                )
            )
        return self._stubs["update_capacity_commitment"]

    @property
    def split_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.SplitCapacityCommitmentRequest],
        Awaitable[reservation.SplitCapacityCommitmentResponse],
    ]:
        r"""Return a callable for the split capacity commitment method over gRPC.

        Splits capacity commitment to two commitments of the same plan
        and ``commitment_end_time``.

        A common use case is to enable downgrading commitments.

        For example, in order to downgrade from 10000 slots to 8000, you
        might split a 10000 capacity commitment into commitments of 2000
        and 8000. Then, you delete the first one after the commitment
        end time passes.

        Returns:
            Callable[[~.SplitCapacityCommitmentRequest],
                    Awaitable[~.SplitCapacityCommitmentResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "split_capacity_commitment" not in self._stubs:
            self._stubs["split_capacity_commitment"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SplitCapacityCommitment",
                request_serializer=reservation.SplitCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.SplitCapacityCommitmentResponse.deserialize,
            )
        return self._stubs["split_capacity_commitment"]

    @property
    def merge_capacity_commitments(
        self,
    ) -> Callable[
        [reservation.MergeCapacityCommitmentsRequest],
        Awaitable[reservation.CapacityCommitment],
    ]:
        r"""Return a callable for the merge capacity commitments method over gRPC.

        Merges capacity commitments of the same plan into a single
        commitment.

        The resulting capacity commitment has the greater
        commitment_end_time out of the to-be-merged capacity
        commitments.

        Attempting to merge capacity commitments of different plan will
        fail with the error code
        ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.MergeCapacityCommitmentsRequest],
                    Awaitable[~.CapacityCommitment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "merge_capacity_commitments" not in self._stubs:
            self._stubs["merge_capacity_commitments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.bigquery.reservation.v1.ReservationService/MergeCapacityCommitments",
                    request_serializer=reservation.MergeCapacityCommitmentsRequest.serialize,
                    response_deserializer=reservation.CapacityCommitment.deserialize,
                )
            )
        return self._stubs["merge_capacity_commitments"]

    @property
    def create_assignment(
        self,
    ) -> Callable[
        [reservation.CreateAssignmentRequest], Awaitable[reservation.Assignment]
    ]:
        r"""Return a callable for the create assignment method over gRPC.

        Creates an assignment object which allows the given project to
        submit jobs of a certain type using slots from the specified
        reservation.

        Currently a resource (project, folder, organization) can only
        have one assignment per each (job_type, location) combination,
        and that reservation will be used for all jobs of the matching
        type.

        Different assignments can be created on different levels of the
        projects, folders or organization hierarchy. During query
        execution, the assignment is looked up at the project, folder
        and organization levels in that order. The first assignment
        found is applied to the query.

        When creating assignments, it does not matter if other
        assignments exist at higher levels.

        Example:

        - The organization ``organizationA`` contains two projects,
          ``project1`` and ``project2``.
        - Assignments for all three entities (``organizationA``,
          ``project1``, and ``project2``) could all be created and
          mapped to the same or different reservations.

        "None" assignments represent an absence of the assignment.
        Projects assigned to None use on-demand pricing. To create a
        "None" assignment, use "none" as a reservation_id in the parent.
        Example parent:
        ``projects/myproject/locations/US/reservations/none``.

        Returns ``google.rpc.Code.PERMISSION_DENIED`` if user does not
        have 'bigquery.admin' permissions on the project using the
        reservation and the project that owns this reservation.

        Returns ``google.rpc.Code.INVALID_ARGUMENT`` when location of
        the assignment does not match location of the reservation.

        Returns:
            Callable[[~.CreateAssignmentRequest],
                    Awaitable[~.Assignment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_assignment" not in self._stubs:
            self._stubs["create_assignment"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateAssignment",
                request_serializer=reservation.CreateAssignmentRequest.serialize,
                response_deserializer=reservation.Assignment.deserialize,
            )
        return self._stubs["create_assignment"]

    @property
    def list_assignments(
        self,
    ) -> Callable[
        [reservation.ListAssignmentsRequest],
        Awaitable[reservation.ListAssignmentsResponse],
    ]:
        r"""Return a callable for the list assignments method over gRPC.

        Lists assignments.

        Only explicitly created assignments will be returned.

        Example:

        - Organization ``organizationA`` contains two projects,
          ``project1`` and ``project2``.
        - Reservation ``res1`` exists and was created previously.
        - CreateAssignment was used previously to define the following
          associations between entities and reservations:
          ``<organizationA, res1>`` and ``<project1, res1>``

        In this example, ListAssignments will just return the above two
        assignments for reservation ``res1``, and no expansion/merge
        will happen.

        The wildcard "-" can be used for reservations in the request. In
        that case all assignments belongs to the specified project and
        location will be listed.

        **Note** "-" cannot be used for projects nor locations.

        Returns:
            Callable[[~.ListAssignmentsRequest],
                    Awaitable[~.ListAssignmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_assignments" not in self._stubs:
            self._stubs["list_assignments"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListAssignments",
                request_serializer=reservation.ListAssignmentsRequest.serialize,
                response_deserializer=reservation.ListAssignmentsResponse.deserialize,
            )
        return self._stubs["list_assignments"]

    @property
    def delete_assignment(
        self,
    ) -> Callable[[reservation.DeleteAssignmentRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete assignment method over gRPC.

        Deletes a assignment. No expansion will happen.

        Example:

        - Organization ``organizationA`` contains two projects,
          ``project1`` and ``project2``.
        - Reservation ``res1`` exists and was created previously.
        - CreateAssignment was used previously to define the following
          associations between entities and reservations:
          ``<organizationA, res1>`` and ``<project1, res1>``

        In this example, deletion of the ``<organizationA, res1>``
        assignment won't affect the other assignment
        ``<project1, res1>``. After said deletion, queries from
        ``project1`` will still use ``res1`` while queries from
        ``project2`` will switch to use on-demand mode.

        Returns:
            Callable[[~.DeleteAssignmentRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_assignment" not in self._stubs:
            self._stubs["delete_assignment"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteAssignment",
                request_serializer=reservation.DeleteAssignmentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_assignment"]

    @property
    def search_assignments(
        self,
    ) -> Callable[
        [reservation.SearchAssignmentsRequest],
        Awaitable[reservation.SearchAssignmentsResponse],
    ]:
        r"""Return a callable for the search assignments method over gRPC.

        Deprecated: Looks up assignments for a specified resource for a
        particular region. If the request is about a project:

        1. Assignments created on the project will be returned if they
           exist.
        2. Otherwise assignments created on the closest ancestor will be
           returned.
        3. Assignments for different JobTypes will all be returned.

        The same logic applies if the request is about a folder.

        If the request is about an organization, then assignments
        created on the organization will be returned (organization
        doesn't have ancestors).

        Comparing to ListAssignments, there are some behavior
        differences:

        1. permission on the assignee will be verified in this API.
        2. Hierarchy lookup (project->folder->organization) happens in
           this API.
        3. Parent here is ``projects/*/locations/*``, instead of
           ``projects/*/locations/*reservations/*``.

        **Note** "-" cannot be used for projects nor locations.

        Returns:
            Callable[[~.SearchAssignmentsRequest],
                    Awaitable[~.SearchAssignmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_assignments" not in self._stubs:
            self._stubs["search_assignments"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SearchAssignments",
                request_serializer=reservation.SearchAssignmentsRequest.serialize,
                response_deserializer=reservation.SearchAssignmentsResponse.deserialize,
            )
        return self._stubs["search_assignments"]

    @property
    def search_all_assignments(
        self,
    ) -> Callable[
        [reservation.SearchAllAssignmentsRequest],
        Awaitable[reservation.SearchAllAssignmentsResponse],
    ]:
        r"""Return a callable for the search all assignments method over gRPC.

        Looks up assignments for a specified resource for a particular
        region. If the request is about a project:

        1. Assignments created on the project will be returned if they
           exist.
        2. Otherwise assignments created on the closest ancestor will be
           returned.
        3. Assignments for different JobTypes will all be returned.

        The same logic applies if the request is about a folder.

        If the request is about an organization, then assignments
        created on the organization will be returned (organization
        doesn't have ancestors).

        Comparing to ListAssignments, there are some behavior
        differences:

        1. permission on the assignee will be verified in this API.
        2. Hierarchy lookup (project->folder->organization) happens in
           this API.
        3. Parent here is ``projects/*/locations/*``, instead of
           ``projects/*/locations/*reservations/*``.

        Returns:
            Callable[[~.SearchAllAssignmentsRequest],
                    Awaitable[~.SearchAllAssignmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_all_assignments" not in self._stubs:
            self._stubs["search_all_assignments"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SearchAllAssignments",
                request_serializer=reservation.SearchAllAssignmentsRequest.serialize,
                response_deserializer=reservation.SearchAllAssignmentsResponse.deserialize,
            )
        return self._stubs["search_all_assignments"]

    @property
    def move_assignment(
        self,
    ) -> Callable[
        [reservation.MoveAssignmentRequest], Awaitable[reservation.Assignment]
    ]:
        r"""Return a callable for the move assignment method over gRPC.

        Moves an assignment under a new reservation.

        This differs from removing an existing assignment and
        recreating a new one by providing a transactional change
        that ensures an assignee always has an associated
        reservation.

        Returns:
            Callable[[~.MoveAssignmentRequest],
                    Awaitable[~.Assignment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_assignment" not in self._stubs:
            self._stubs["move_assignment"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/MoveAssignment",
                request_serializer=reservation.MoveAssignmentRequest.serialize,
                response_deserializer=reservation.Assignment.deserialize,
            )
        return self._stubs["move_assignment"]

    @property
    def update_assignment(
        self,
    ) -> Callable[
        [reservation.UpdateAssignmentRequest], Awaitable[reservation.Assignment]
    ]:
        r"""Return a callable for the update assignment method over gRPC.

        Updates an existing assignment.

        Only the ``priority`` field can be updated.

        Returns:
            Callable[[~.UpdateAssignmentRequest],
                    Awaitable[~.Assignment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_assignment" not in self._stubs:
            self._stubs["update_assignment"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateAssignment",
                request_serializer=reservation.UpdateAssignmentRequest.serialize,
                response_deserializer=reservation.Assignment.deserialize,
            )
        return self._stubs["update_assignment"]

    @property
    def get_bi_reservation(
        self,
    ) -> Callable[
        [reservation.GetBiReservationRequest], Awaitable[reservation.BiReservation]
    ]:
        r"""Return a callable for the get bi reservation method over gRPC.

        Retrieves a BI reservation.

        Returns:
            Callable[[~.GetBiReservationRequest],
                    Awaitable[~.BiReservation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_bi_reservation" not in self._stubs:
            self._stubs["get_bi_reservation"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetBiReservation",
                request_serializer=reservation.GetBiReservationRequest.serialize,
                response_deserializer=reservation.BiReservation.deserialize,
            )
        return self._stubs["get_bi_reservation"]

    @property
    def update_bi_reservation(
        self,
    ) -> Callable[
        [reservation.UpdateBiReservationRequest], Awaitable[reservation.BiReservation]
    ]:
        r"""Return a callable for the update bi reservation method over gRPC.

        Updates a BI reservation.

        Only fields specified in the ``field_mask`` are updated.

        A singleton BI reservation always exists with default size 0. In
        order to reserve BI capacity it needs to be updated to an amount
        greater than 0. In order to release BI capacity reservation size
        must be set to 0.

        Returns:
            Callable[[~.UpdateBiReservationRequest],
                    Awaitable[~.BiReservation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_bi_reservation" not in self._stubs:
            self._stubs["update_bi_reservation"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateBiReservation",
                request_serializer=reservation.UpdateBiReservationRequest.serialize,
                response_deserializer=reservation.BiReservation.deserialize,
            )
        return self._stubs["update_bi_reservation"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the access control policy for a resource. May return:

        - A\ ``NOT_FOUND`` error if the resource doesn't exist or you
          don't have the permission to view it.
        - An empty policy if the resource exists but doesn't have a set
          policy.

        Supported resources are:

        - Reservations
        - ReservationAssignments

        To call this method, you must have the following Google IAM
        permissions:

        - ``bigqueryreservation.reservations.getIamPolicy`` to get
          policies on reservations.

        Returns:
            Callable[[~.GetIamPolicyRequest],
                    Awaitable[~.Policy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets an access control policy for a resource. Replaces any
        existing policy.

        Supported resources are:

        - Reservations

        To call this method, you must have the following Google IAM
        permissions:

        - ``bigqueryreservation.reservations.setIamPolicy`` to set
          policies on reservations.

        Returns:
            Callable[[~.SetIamPolicyRequest],
                    Awaitable[~.Policy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.

        Gets your permissions on a resource. Returns an empty
        set of permissions if the resource doesn't exist.

        Supported resources are:

        - Reservations

        No Google IAM permissions are required to call this
        method.

        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    Awaitable[~.TestIamPermissionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def create_reservation_group(
        self,
    ) -> Callable[
        [reservation.CreateReservationGroupRequest],
        Awaitable[reservation.ReservationGroup],
    ]:
        r"""Return a callable for the create reservation group method over gRPC.

        Creates a new reservation group.

        Returns:
            Callable[[~.CreateReservationGroupRequest],
                    Awaitable[~.ReservationGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_reservation_group" not in self._stubs:
            self._stubs["create_reservation_group"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateReservationGroup",
                request_serializer=reservation.CreateReservationGroupRequest.serialize,
                response_deserializer=reservation.ReservationGroup.deserialize,
            )
        return self._stubs["create_reservation_group"]

    @property
    def get_reservation_group(
        self,
    ) -> Callable[
        [reservation.GetReservationGroupRequest],
        Awaitable[reservation.ReservationGroup],
    ]:
        r"""Return a callable for the get reservation group method over gRPC.

        Returns information about the reservation group.

        Returns:
            Callable[[~.GetReservationGroupRequest],
                    Awaitable[~.ReservationGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_reservation_group" not in self._stubs:
            self._stubs["get_reservation_group"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetReservationGroup",
                request_serializer=reservation.GetReservationGroupRequest.serialize,
                response_deserializer=reservation.ReservationGroup.deserialize,
            )
        return self._stubs["get_reservation_group"]

    @property
    def delete_reservation_group(
        self,
    ) -> Callable[
        [reservation.DeleteReservationGroupRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete reservation group method over gRPC.

        Deletes a reservation. Returns
        ``google.rpc.Code.FAILED_PRECONDITION`` when reservation has
        assignments.

        Returns:
            Callable[[~.DeleteReservationGroupRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_reservation_group" not in self._stubs:
            self._stubs["delete_reservation_group"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteReservationGroup",
                request_serializer=reservation.DeleteReservationGroupRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_reservation_group"]

    @property
    def list_reservation_groups(
        self,
    ) -> Callable[
        [reservation.ListReservationGroupsRequest],
        Awaitable[reservation.ListReservationGroupsResponse],
    ]:
        r"""Return a callable for the list reservation groups method over gRPC.

        Lists all the reservation groups for the project in
        the specified location.

        Returns:
            Callable[[~.ListReservationGroupsRequest],
                    Awaitable[~.ListReservationGroupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_reservation_groups" not in self._stubs:
            self._stubs["list_reservation_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListReservationGroups",
                request_serializer=reservation.ListReservationGroupsRequest.serialize,
                response_deserializer=reservation.ListReservationGroupsResponse.deserialize,
            )
        return self._stubs["list_reservation_groups"]

    @property
    def update_reservation_group(
        self,
    ) -> Callable[
        [reservation.UpdateReservationGroupRequest],
        Awaitable[reservation.ReservationGroup],
    ]:
        r"""Return a callable for the update reservation group method over gRPC.

        Updates an existing reservation group resource.

        Returns:
            Callable[[~.UpdateReservationGroupRequest],
                    Awaitable[~.ReservationGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_reservation_group" not in self._stubs:
            self._stubs["update_reservation_group"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateReservationGroup",
                request_serializer=reservation.UpdateReservationGroupRequest.serialize,
                response_deserializer=reservation.ReservationGroup.deserialize,
            )
        return self._stubs["update_reservation_group"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_reservation: self._wrap_method(
                self.create_reservation,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_reservations: self._wrap_method(
                self.list_reservations,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_reservation: self._wrap_method(
                self.get_reservation,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_reservation: self._wrap_method(
                self.delete_reservation,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_reservation: self._wrap_method(
                self.update_reservation,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.failover_reservation: self._wrap_method(
                self.failover_reservation,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_capacity_commitment: self._wrap_method(
                self.create_capacity_commitment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_capacity_commitments: self._wrap_method(
                self.list_capacity_commitments,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_capacity_commitment: self._wrap_method(
                self.get_capacity_commitment,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_capacity_commitment: self._wrap_method(
                self.delete_capacity_commitment,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_capacity_commitment: self._wrap_method(
                self.update_capacity_commitment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.split_capacity_commitment: self._wrap_method(
                self.split_capacity_commitment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.merge_capacity_commitments: self._wrap_method(
                self.merge_capacity_commitments,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_assignment: self._wrap_method(
                self.create_assignment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_assignments: self._wrap_method(
                self.list_assignments,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_assignment: self._wrap_method(
                self.delete_assignment,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.search_assignments: self._wrap_method(
                self.search_assignments,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.search_all_assignments: self._wrap_method(
                self.search_all_assignments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_assignment: self._wrap_method(
                self.move_assignment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_assignment: self._wrap_method(
                self.update_assignment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_bi_reservation: self._wrap_method(
                self.get_bi_reservation,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_bi_reservation: self._wrap_method(
                self.update_bi_reservation,
                default_timeout=300.0,
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
            self.create_reservation_group: self._wrap_method(
                self.create_reservation_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_reservation_group: self._wrap_method(
                self.get_reservation_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_reservation_group: self._wrap_method(
                self.delete_reservation_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_reservation_groups: self._wrap_method(
                self.list_reservation_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_reservation_group: self._wrap_method(
                self.update_reservation_group,
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


__all__ = ("ReservationServiceGrpcAsyncIOTransport",)
