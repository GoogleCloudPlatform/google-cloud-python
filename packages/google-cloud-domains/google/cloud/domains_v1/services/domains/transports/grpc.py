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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.domains_v1.types import domains

from .base import DEFAULT_CLIENT_INFO, DomainsTransport

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
                    "serviceName": "google.cloud.domains.v1.Domains",
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
                    "serviceName": "google.cloud.domains.v1.Domains",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DomainsGrpcTransport(DomainsTransport):
    """gRPC backend transport for Domains.

    The Cloud Domains API enables management and configuration of
    domain names.

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
        host: str = "domains.googleapis.com",
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
                 The hostname to connect to (default: 'domains.googleapis.com').
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
        host: str = "domains.googleapis.com",
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
    def search_domains(
        self,
    ) -> Callable[[domains.SearchDomainsRequest], domains.SearchDomainsResponse]:
        r"""Return a callable for the search domains method over gRPC.

        Searches for available domain names similar to the provided
        query.

        Availability results from this method are approximate; call
        ``RetrieveRegisterParameters`` on a domain before registering to
        confirm availability.

        Returns:
            Callable[[~.SearchDomainsRequest],
                    ~.SearchDomainsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_domains" not in self._stubs:
            self._stubs["search_domains"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/SearchDomains",
                request_serializer=domains.SearchDomainsRequest.serialize,
                response_deserializer=domains.SearchDomainsResponse.deserialize,
            )
        return self._stubs["search_domains"]

    @property
    def retrieve_register_parameters(
        self,
    ) -> Callable[
        [domains.RetrieveRegisterParametersRequest],
        domains.RetrieveRegisterParametersResponse,
    ]:
        r"""Return a callable for the retrieve register parameters method over gRPC.

        Gets parameters needed to register a new domain name, including
        price and up-to-date availability. Use the returned values to
        call ``RegisterDomain``.

        Returns:
            Callable[[~.RetrieveRegisterParametersRequest],
                    ~.RetrieveRegisterParametersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retrieve_register_parameters" not in self._stubs:
            self._stubs["retrieve_register_parameters"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.domains.v1.Domains/RetrieveRegisterParameters",
                    request_serializer=domains.RetrieveRegisterParametersRequest.serialize,
                    response_deserializer=domains.RetrieveRegisterParametersResponse.deserialize,
                )
            )
        return self._stubs["retrieve_register_parameters"]

    @property
    def register_domain(
        self,
    ) -> Callable[[domains.RegisterDomainRequest], operations_pb2.Operation]:
        r"""Return a callable for the register domain method over gRPC.

        Registers a new domain name and creates a corresponding
        ``Registration`` resource.

        Call ``RetrieveRegisterParameters`` first to check availability
        of the domain name and determine parameters like price that are
        needed to build a call to this method.

        A successful call creates a ``Registration`` resource in state
        ``REGISTRATION_PENDING``, which resolves to ``ACTIVE`` within
        1-2 minutes, indicating that the domain was successfully
        registered. If the resource ends up in state
        ``REGISTRATION_FAILED``, it indicates that the domain was not
        registered successfully, and you can safely delete the resource
        and retry registration.

        Returns:
            Callable[[~.RegisterDomainRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "register_domain" not in self._stubs:
            self._stubs["register_domain"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/RegisterDomain",
                request_serializer=domains.RegisterDomainRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["register_domain"]

    @property
    def retrieve_transfer_parameters(
        self,
    ) -> Callable[
        [domains.RetrieveTransferParametersRequest],
        domains.RetrieveTransferParametersResponse,
    ]:
        r"""Return a callable for the retrieve transfer parameters method over gRPC.

        Gets parameters needed to transfer a domain name from another
        registrar to Cloud Domains. For domains managed by Google
        Domains, transferring to Cloud Domains is not supported.

        Use the returned values to call ``TransferDomain``.

        Returns:
            Callable[[~.RetrieveTransferParametersRequest],
                    ~.RetrieveTransferParametersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retrieve_transfer_parameters" not in self._stubs:
            self._stubs["retrieve_transfer_parameters"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.domains.v1.Domains/RetrieveTransferParameters",
                    request_serializer=domains.RetrieveTransferParametersRequest.serialize,
                    response_deserializer=domains.RetrieveTransferParametersResponse.deserialize,
                )
            )
        return self._stubs["retrieve_transfer_parameters"]

    @property
    def transfer_domain(
        self,
    ) -> Callable[[domains.TransferDomainRequest], operations_pb2.Operation]:
        r"""Return a callable for the transfer domain method over gRPC.

        Transfers a domain name from another registrar to Cloud Domains.
        For domains managed by Google Domains, transferring to Cloud
        Domains is not supported.

        Before calling this method, go to the domain's current registrar
        to unlock the domain for transfer and retrieve the domain's
        transfer authorization code. Then call
        ``RetrieveTransferParameters`` to confirm that the domain is
        unlocked and to get values needed to build a call to this
        method.

        A successful call creates a ``Registration`` resource in state
        ``TRANSFER_PENDING``. It can take several days to complete the
        transfer process. The registrant can often speed up this process
        by approving the transfer through the current registrar, either
        by clicking a link in an email from the registrar or by visiting
        the registrar's website.

        A few minutes after transfer approval, the resource transitions
        to state ``ACTIVE``, indicating that the transfer was
        successful. If the transfer is rejected or the request expires
        without being approved, the resource can end up in state
        ``TRANSFER_FAILED``. If transfer fails, you can safely delete
        the resource and retry the transfer.

        Returns:
            Callable[[~.TransferDomainRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "transfer_domain" not in self._stubs:
            self._stubs["transfer_domain"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/TransferDomain",
                request_serializer=domains.TransferDomainRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["transfer_domain"]

    @property
    def list_registrations(
        self,
    ) -> Callable[
        [domains.ListRegistrationsRequest], domains.ListRegistrationsResponse
    ]:
        r"""Return a callable for the list registrations method over gRPC.

        Lists the ``Registration`` resources in a project.

        Returns:
            Callable[[~.ListRegistrationsRequest],
                    ~.ListRegistrationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_registrations" not in self._stubs:
            self._stubs["list_registrations"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/ListRegistrations",
                request_serializer=domains.ListRegistrationsRequest.serialize,
                response_deserializer=domains.ListRegistrationsResponse.deserialize,
            )
        return self._stubs["list_registrations"]

    @property
    def get_registration(
        self,
    ) -> Callable[[domains.GetRegistrationRequest], domains.Registration]:
        r"""Return a callable for the get registration method over gRPC.

        Gets the details of a ``Registration`` resource.

        Returns:
            Callable[[~.GetRegistrationRequest],
                    ~.Registration]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_registration" not in self._stubs:
            self._stubs["get_registration"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/GetRegistration",
                request_serializer=domains.GetRegistrationRequest.serialize,
                response_deserializer=domains.Registration.deserialize,
            )
        return self._stubs["get_registration"]

    @property
    def update_registration(
        self,
    ) -> Callable[[domains.UpdateRegistrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the update registration method over gRPC.

        Updates select fields of a ``Registration`` resource, notably
        ``labels``. To update other fields, use the appropriate custom
        update method:

        - To update management settings, see
          ``ConfigureManagementSettings``
        - To update DNS configuration, see ``ConfigureDnsSettings``
        - To update contact information, see
          ``ConfigureContactSettings``

        Returns:
            Callable[[~.UpdateRegistrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_registration" not in self._stubs:
            self._stubs["update_registration"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/UpdateRegistration",
                request_serializer=domains.UpdateRegistrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_registration"]

    @property
    def configure_management_settings(
        self,
    ) -> Callable[
        [domains.ConfigureManagementSettingsRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the configure management settings method over gRPC.

        Updates a ``Registration``'s management settings.

        Returns:
            Callable[[~.ConfigureManagementSettingsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "configure_management_settings" not in self._stubs:
            self._stubs["configure_management_settings"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.domains.v1.Domains/ConfigureManagementSettings",
                    request_serializer=domains.ConfigureManagementSettingsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["configure_management_settings"]

    @property
    def configure_dns_settings(
        self,
    ) -> Callable[[domains.ConfigureDnsSettingsRequest], operations_pb2.Operation]:
        r"""Return a callable for the configure dns settings method over gRPC.

        Updates a ``Registration``'s DNS settings.

        Returns:
            Callable[[~.ConfigureDnsSettingsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "configure_dns_settings" not in self._stubs:
            self._stubs["configure_dns_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/ConfigureDnsSettings",
                request_serializer=domains.ConfigureDnsSettingsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["configure_dns_settings"]

    @property
    def configure_contact_settings(
        self,
    ) -> Callable[[domains.ConfigureContactSettingsRequest], operations_pb2.Operation]:
        r"""Return a callable for the configure contact settings method over gRPC.

        Updates a ``Registration``'s contact settings. Some changes
        require confirmation by the domain's registrant contact .

        Returns:
            Callable[[~.ConfigureContactSettingsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "configure_contact_settings" not in self._stubs:
            self._stubs["configure_contact_settings"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.domains.v1.Domains/ConfigureContactSettings",
                    request_serializer=domains.ConfigureContactSettingsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["configure_contact_settings"]

    @property
    def export_registration(
        self,
    ) -> Callable[[domains.ExportRegistrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the export registration method over gRPC.

        Exports a ``Registration`` resource, such that it is no longer
        managed by Cloud Domains.

        When an active domain is successfully exported, you can continue
        to use the domain in `Google
        Domains <https://domains.google/>`__ until it expires. The
        calling user becomes the domain's sole owner in Google Domains,
        and permissions for the domain are subsequently managed there.
        The domain does not renew automatically unless the new owner
        sets up billing in Google Domains.

        Returns:
            Callable[[~.ExportRegistrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_registration" not in self._stubs:
            self._stubs["export_registration"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/ExportRegistration",
                request_serializer=domains.ExportRegistrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_registration"]

    @property
    def delete_registration(
        self,
    ) -> Callable[[domains.DeleteRegistrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete registration method over gRPC.

        Deletes a ``Registration`` resource.

        This method works on any ``Registration`` resource using
        `Subscription or Commitment
        billing </domains/pricing#billing-models>`__, provided that the
        resource was created at least 1 day in the past.

        For ``Registration`` resources using `Monthly
        billing </domains/pricing#billing-models>`__, this method works
        if:

        - ``state`` is ``EXPORTED`` with ``expire_time`` in the past
        - ``state`` is ``REGISTRATION_FAILED``
        - ``state`` is ``TRANSFER_FAILED``

        When an active registration is successfully deleted, you can
        continue to use the domain in `Google
        Domains <https://domains.google/>`__ until it expires. The
        calling user becomes the domain's sole owner in Google Domains,
        and permissions for the domain are subsequently managed there.
        The domain does not renew automatically unless the new owner
        sets up billing in Google Domains.

        Returns:
            Callable[[~.DeleteRegistrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_registration" not in self._stubs:
            self._stubs["delete_registration"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/DeleteRegistration",
                request_serializer=domains.DeleteRegistrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_registration"]

    @property
    def retrieve_authorization_code(
        self,
    ) -> Callable[
        [domains.RetrieveAuthorizationCodeRequest], domains.AuthorizationCode
    ]:
        r"""Return a callable for the retrieve authorization code method over gRPC.

        Gets the authorization code of the ``Registration`` for the
        purpose of transferring the domain to another registrar.

        You can call this method only after 60 days have elapsed since
        the initial domain registration.

        Returns:
            Callable[[~.RetrieveAuthorizationCodeRequest],
                    ~.AuthorizationCode]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retrieve_authorization_code" not in self._stubs:
            self._stubs["retrieve_authorization_code"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.domains.v1.Domains/RetrieveAuthorizationCode",
                    request_serializer=domains.RetrieveAuthorizationCodeRequest.serialize,
                    response_deserializer=domains.AuthorizationCode.deserialize,
                )
            )
        return self._stubs["retrieve_authorization_code"]

    @property
    def reset_authorization_code(
        self,
    ) -> Callable[[domains.ResetAuthorizationCodeRequest], domains.AuthorizationCode]:
        r"""Return a callable for the reset authorization code method over gRPC.

        Resets the authorization code of the ``Registration`` to a new
        random string.

        You can call this method only after 60 days have elapsed since
        the initial domain registration.

        Returns:
            Callable[[~.ResetAuthorizationCodeRequest],
                    ~.AuthorizationCode]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_authorization_code" not in self._stubs:
            self._stubs["reset_authorization_code"] = self._logged_channel.unary_unary(
                "/google.cloud.domains.v1.Domains/ResetAuthorizationCode",
                request_serializer=domains.ResetAuthorizationCodeRequest.serialize,
                response_deserializer=domains.AuthorizationCode.deserialize,
            )
        return self._stubs["reset_authorization_code"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("DomainsGrpcTransport",)
