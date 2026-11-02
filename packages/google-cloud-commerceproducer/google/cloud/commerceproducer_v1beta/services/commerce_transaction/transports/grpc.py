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
from google.api_core import gapic_v1, grpc_helpers
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.commerceproducer_v1beta.types import (
    commerce_transaction,
    private_offer,
    service,
    sku,
    sku_group,
    standard_offer,
)
from google.cloud.commerceproducer_v1beta.types import (
    private_offer as gcc_private_offer,
)

from .base import DEFAULT_CLIENT_INFO, CommerceTransactionTransport

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
                    "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
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
                    "serviceName": "google.cloud.commerceproducer.v1beta.CommerceTransaction",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class CommerceTransactionGrpcTransport(CommerceTransactionTransport):
    """gRPC backend transport for CommerceTransaction.

    APIs related to managing resources that model commercial
    transactions.

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
        host: str = "commerceproducer.googleapis.com",
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
                 The hostname to connect to (default: 'commerceproducer.googleapis.com').
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
        host: str = "commerceproducer.googleapis.com",
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
    def list_services(
        self,
    ) -> Callable[
        [commerce_transaction.ListServicesRequest],
        commerce_transaction.ListServicesResponse,
    ]:
        r"""Return a callable for the list services method over gRPC.

        Lists Services in a given project and location.

        Returns:
            Callable[[~.ListServicesRequest],
                    ~.ListServicesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_services" not in self._stubs:
            self._stubs["list_services"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/ListServices",
                request_serializer=commerce_transaction.ListServicesRequest.serialize,
                response_deserializer=commerce_transaction.ListServicesResponse.deserialize,
            )
        return self._stubs["list_services"]

    @property
    def get_service(
        self,
    ) -> Callable[[commerce_transaction.GetServiceRequest], service.Service]:
        r"""Return a callable for the get service method over gRPC.

        Gets details of a single Service.

        Returns:
            Callable[[~.GetServiceRequest],
                    ~.Service]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_service" not in self._stubs:
            self._stubs["get_service"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/GetService",
                request_serializer=commerce_transaction.GetServiceRequest.serialize,
                response_deserializer=service.Service.deserialize,
            )
        return self._stubs["get_service"]

    @property
    def list_private_offers(
        self,
    ) -> Callable[
        [commerce_transaction.ListPrivateOffersRequest],
        commerce_transaction.ListPrivateOffersResponse,
    ]:
        r"""Return a callable for the list private offers method over gRPC.

        Lists PrivateOffers for the given parent.

        Returns:
            Callable[[~.ListPrivateOffersRequest],
                    ~.ListPrivateOffersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_private_offers" not in self._stubs:
            self._stubs["list_private_offers"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/ListPrivateOffers",
                request_serializer=commerce_transaction.ListPrivateOffersRequest.serialize,
                response_deserializer=commerce_transaction.ListPrivateOffersResponse.deserialize,
            )
        return self._stubs["list_private_offers"]

    @property
    def get_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.GetPrivateOfferRequest], private_offer.PrivateOffer
    ]:
        r"""Return a callable for the get private offer method over gRPC.

        Gets details of a single PrivateOffer.

        Returns:
            Callable[[~.GetPrivateOfferRequest],
                    ~.PrivateOffer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_private_offer" not in self._stubs:
            self._stubs["get_private_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/GetPrivateOffer",
                request_serializer=commerce_transaction.GetPrivateOfferRequest.serialize,
                response_deserializer=private_offer.PrivateOffer.deserialize,
            )
        return self._stubs["get_private_offer"]

    @property
    def resolve_amendment_target(
        self,
    ) -> Callable[
        [commerce_transaction.ResolveAmendmentTargetRequest],
        commerce_transaction.ResolveAmendmentTargetResponse,
    ]:
        r"""Return a callable for the resolve amendment target method over gRPC.

        Resolves the existing offer that must be amended when
        creating a new PrivateOffer. Use this method to
        determine the correct amendment target before creating
        or publishing an offer.

        Returns:
            Callable[[~.ResolveAmendmentTargetRequest],
                    ~.ResolveAmendmentTargetResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "resolve_amendment_target" not in self._stubs:
            self._stubs["resolve_amendment_target"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/ResolveAmendmentTarget",
                request_serializer=commerce_transaction.ResolveAmendmentTargetRequest.serialize,
                response_deserializer=commerce_transaction.ResolveAmendmentTargetResponse.deserialize,
            )
        return self._stubs["resolve_amendment_target"]

    @property
    def create_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.CreatePrivateOfferRequest], private_offer.PrivateOffer
    ]:
        r"""Return a callable for the create private offer method over gRPC.

        Creates a new PrivateOffer in a given project and
        location.

        Returns:
            Callable[[~.CreatePrivateOfferRequest],
                    ~.PrivateOffer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_private_offer" not in self._stubs:
            self._stubs["create_private_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/CreatePrivateOffer",
                request_serializer=commerce_transaction.CreatePrivateOfferRequest.serialize,
                response_deserializer=private_offer.PrivateOffer.deserialize,
            )
        return self._stubs["create_private_offer"]

    @property
    def update_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.UpdatePrivateOfferRequest], gcc_private_offer.PrivateOffer
    ]:
        r"""Return a callable for the update private offer method over gRPC.

        Updates the target PrivateOffer.

        Returns:
            Callable[[~.UpdatePrivateOfferRequest],
                    ~.PrivateOffer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_private_offer" not in self._stubs:
            self._stubs["update_private_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/UpdatePrivateOffer",
                request_serializer=commerce_transaction.UpdatePrivateOfferRequest.serialize,
                response_deserializer=gcc_private_offer.PrivateOffer.deserialize,
            )
        return self._stubs["update_private_offer"]

    @property
    def publish_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.PublishPrivateOfferRequest], private_offer.PrivateOffer
    ]:
        r"""Return a callable for the publish private offer method over gRPC.

        Publishes the target PrivateOffer.

        Returns:
            Callable[[~.PublishPrivateOfferRequest],
                    ~.PrivateOffer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "publish_private_offer" not in self._stubs:
            self._stubs["publish_private_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/PublishPrivateOffer",
                request_serializer=commerce_transaction.PublishPrivateOfferRequest.serialize,
                response_deserializer=private_offer.PrivateOffer.deserialize,
            )
        return self._stubs["publish_private_offer"]

    @property
    def cancel_private_offer(
        self,
    ) -> Callable[
        [commerce_transaction.CancelPrivateOfferRequest], private_offer.PrivateOffer
    ]:
        r"""Return a callable for the cancel private offer method over gRPC.

        Cancels the target PrivateOffer.

        Returns:
            Callable[[~.CancelPrivateOfferRequest],
                    ~.PrivateOffer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_private_offer" not in self._stubs:
            self._stubs["cancel_private_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/CancelPrivateOffer",
                request_serializer=commerce_transaction.CancelPrivateOfferRequest.serialize,
                response_deserializer=private_offer.PrivateOffer.deserialize,
            )
        return self._stubs["cancel_private_offer"]

    @property
    def delete_private_offer(
        self,
    ) -> Callable[[commerce_transaction.DeletePrivateOfferRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete private offer method over gRPC.

        Deletes the target PrivateOffer.

        Returns:
            Callable[[~.DeletePrivateOfferRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_private_offer" not in self._stubs:
            self._stubs["delete_private_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/DeletePrivateOffer",
                request_serializer=commerce_transaction.DeletePrivateOfferRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_private_offer"]

    @property
    def list_private_offer_documents(
        self,
    ) -> Callable[
        [commerce_transaction.ListPrivateOfferDocumentsRequest],
        commerce_transaction.ListPrivateOfferDocumentsResponse,
    ]:
        r"""Return a callable for the list private offer documents method over gRPC.

        Lists PrivateOfferDocuments for the given parent.

        Returns:
            Callable[[~.ListPrivateOfferDocumentsRequest],
                    ~.ListPrivateOfferDocumentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_private_offer_documents" not in self._stubs:
            self._stubs["list_private_offer_documents"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.commerceproducer.v1beta.CommerceTransaction/ListPrivateOfferDocuments",
                    request_serializer=commerce_transaction.ListPrivateOfferDocumentsRequest.serialize,
                    response_deserializer=commerce_transaction.ListPrivateOfferDocumentsResponse.deserialize,
                )
            )
        return self._stubs["list_private_offer_documents"]

    @property
    def get_private_offer_document(
        self,
    ) -> Callable[
        [commerce_transaction.GetPrivateOfferDocumentRequest],
        private_offer.PrivateOfferDocument,
    ]:
        r"""Return a callable for the get private offer document method over gRPC.

        Gets details of a single PrivateOfferDocument.

        Returns:
            Callable[[~.GetPrivateOfferDocumentRequest],
                    ~.PrivateOfferDocument]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_private_offer_document" not in self._stubs:
            self._stubs["get_private_offer_document"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.commerceproducer.v1beta.CommerceTransaction/GetPrivateOfferDocument",
                    request_serializer=commerce_transaction.GetPrivateOfferDocumentRequest.serialize,
                    response_deserializer=private_offer.PrivateOfferDocument.deserialize,
                )
            )
        return self._stubs["get_private_offer_document"]

    @property
    def create_private_offer_document(
        self,
    ) -> Callable[
        [commerce_transaction.CreatePrivateOfferDocumentRequest],
        private_offer.PrivateOfferDocument,
    ]:
        r"""Return a callable for the create private offer document method over gRPC.

        Creates a new PrivateOfferDocument in a given project
        and location.

        Returns:
            Callable[[~.CreatePrivateOfferDocumentRequest],
                    ~.PrivateOfferDocument]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_private_offer_document" not in self._stubs:
            self._stubs["create_private_offer_document"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.commerceproducer.v1beta.CommerceTransaction/CreatePrivateOfferDocument",
                    request_serializer=commerce_transaction.CreatePrivateOfferDocumentRequest.serialize,
                    response_deserializer=private_offer.PrivateOfferDocument.deserialize,
                )
            )
        return self._stubs["create_private_offer_document"]

    @property
    def update_private_offer_document(
        self,
    ) -> Callable[
        [commerce_transaction.UpdatePrivateOfferDocumentRequest],
        private_offer.PrivateOfferDocument,
    ]:
        r"""Return a callable for the update private offer document method over gRPC.

        Updates the target PrivateOfferDocument.

        Returns:
            Callable[[~.UpdatePrivateOfferDocumentRequest],
                    ~.PrivateOfferDocument]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_private_offer_document" not in self._stubs:
            self._stubs["update_private_offer_document"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.commerceproducer.v1beta.CommerceTransaction/UpdatePrivateOfferDocument",
                    request_serializer=commerce_transaction.UpdatePrivateOfferDocumentRequest.serialize,
                    response_deserializer=private_offer.PrivateOfferDocument.deserialize,
                )
            )
        return self._stubs["update_private_offer_document"]

    @property
    def delete_private_offer_document(
        self,
    ) -> Callable[
        [commerce_transaction.DeletePrivateOfferDocumentRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete private offer document method over gRPC.

        Deletes the target PrivateOfferDocument.

        Returns:
            Callable[[~.DeletePrivateOfferDocumentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_private_offer_document" not in self._stubs:
            self._stubs["delete_private_offer_document"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.commerceproducer.v1beta.CommerceTransaction/DeletePrivateOfferDocument",
                    request_serializer=commerce_transaction.DeletePrivateOfferDocumentRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_private_offer_document"]

    @property
    def list_standard_offers(
        self,
    ) -> Callable[
        [commerce_transaction.ListStandardOffersRequest],
        commerce_transaction.ListStandardOffersResponse,
    ]:
        r"""Return a callable for the list standard offers method over gRPC.

        Lists StandardOffers for the given parent.

        Returns:
            Callable[[~.ListStandardOffersRequest],
                    ~.ListStandardOffersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_standard_offers" not in self._stubs:
            self._stubs["list_standard_offers"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/ListStandardOffers",
                request_serializer=commerce_transaction.ListStandardOffersRequest.serialize,
                response_deserializer=commerce_transaction.ListStandardOffersResponse.deserialize,
            )
        return self._stubs["list_standard_offers"]

    @property
    def get_standard_offer(
        self,
    ) -> Callable[
        [commerce_transaction.GetStandardOfferRequest], standard_offer.StandardOffer
    ]:
        r"""Return a callable for the get standard offer method over gRPC.

        Gets details of a single StandardOffer.

        Returns:
            Callable[[~.GetStandardOfferRequest],
                    ~.StandardOffer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_standard_offer" not in self._stubs:
            self._stubs["get_standard_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/GetStandardOffer",
                request_serializer=commerce_transaction.GetStandardOfferRequest.serialize,
                response_deserializer=standard_offer.StandardOffer.deserialize,
            )
        return self._stubs["get_standard_offer"]

    @property
    def get_sku(self) -> Callable[[commerce_transaction.GetSkuRequest], sku.Sku]:
        r"""Return a callable for the get sku method over gRPC.

        Gets details of a single Sku.

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
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/GetSku",
                request_serializer=commerce_transaction.GetSkuRequest.serialize,
                response_deserializer=sku.Sku.deserialize,
            )
        return self._stubs["get_sku"]

    @property
    def list_skus(
        self,
    ) -> Callable[
        [commerce_transaction.ListSkusRequest], commerce_transaction.ListSkusResponse
    ]:
        r"""Return a callable for the list skus method over gRPC.

        Lists Skus for the given parent.

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
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/ListSkus",
                request_serializer=commerce_transaction.ListSkusRequest.serialize,
                response_deserializer=commerce_transaction.ListSkusResponse.deserialize,
            )
        return self._stubs["list_skus"]

    @property
    def get_sku_group(
        self,
    ) -> Callable[[commerce_transaction.GetSkuGroupRequest], sku_group.SkuGroup]:
        r"""Return a callable for the get sku group method over gRPC.

        Gets details of a single SkuGroup.

        Returns:
            Callable[[~.GetSkuGroupRequest],
                    ~.SkuGroup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_sku_group" not in self._stubs:
            self._stubs["get_sku_group"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/GetSkuGroup",
                request_serializer=commerce_transaction.GetSkuGroupRequest.serialize,
                response_deserializer=sku_group.SkuGroup.deserialize,
            )
        return self._stubs["get_sku_group"]

    @property
    def list_sku_groups(
        self,
    ) -> Callable[
        [commerce_transaction.ListSkuGroupsRequest],
        commerce_transaction.ListSkuGroupsResponse,
    ]:
        r"""Return a callable for the list sku groups method over gRPC.

        Lists SkuGroups for the given parent.

        Returns:
            Callable[[~.ListSkuGroupsRequest],
                    ~.ListSkuGroupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sku_groups" not in self._stubs:
            self._stubs["list_sku_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.commerceproducer.v1beta.CommerceTransaction/ListSkuGroups",
                request_serializer=commerce_transaction.ListSkuGroupsRequest.serialize,
                response_deserializer=commerce_transaction.ListSkuGroupsResponse.deserialize,
            )
        return self._stubs["list_sku_groups"]

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


__all__ = ("CommerceTransactionGrpcTransport",)
