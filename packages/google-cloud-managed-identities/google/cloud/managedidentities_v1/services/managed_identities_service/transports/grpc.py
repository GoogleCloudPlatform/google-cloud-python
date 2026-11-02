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

from google.cloud.managedidentities_v1.types import managed_identities_service, resource

from .base import DEFAULT_CLIENT_INFO, ManagedIdentitiesServiceTransport

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
                    "serviceName": "google.cloud.managedidentities.v1.ManagedIdentitiesService",
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
                    "serviceName": "google.cloud.managedidentities.v1.ManagedIdentitiesService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ManagedIdentitiesServiceGrpcTransport(ManagedIdentitiesServiceTransport):
    """gRPC backend transport for ManagedIdentitiesService.

    API Overview

    The ``managedidentites.googleapis.com`` service implements the
    Google Cloud Managed Identites API for identity services (e.g.
    Microsoft Active Directory).

    The Managed Identities service provides methods to manage
    (create/read/update/delete) domains, reset managed identities admin
    password, add/remove domain controllers in GCP regions and
    add/remove VPC peering.

    Data Model

    The Managed Identities service exposes the following resources:

    - Locations as global, named as follows:
      ``projects/{project_id}/locations/global``.

    - Domains, named as follows:
      ``/projects/{project_id}/locations/global/domain/{domain_name}``.

    The ``{domain_name}`` refers to fully qualified domain name in the
    customer project e.g. mydomain.myorganization.com, with the
    following restrictions:

    - Must contain only lowercase letters, numbers, periods and hyphens.
    - Must start with a letter.
    - Must contain between 2-64 characters.
    - Must end with a number or a letter.
    - Must not start with period.
    - First segement length (mydomain form example above) shouldn't
      exceed 15 chars.
    - The last segment cannot be fully numeric.
    - Must be unique within the customer project.

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
        host: str = "managedidentities.googleapis.com",
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
                 The hostname to connect to (default: 'managedidentities.googleapis.com').
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
        host: str = "managedidentities.googleapis.com",
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
    def create_microsoft_ad_domain(
        self,
    ) -> Callable[
        [managed_identities_service.CreateMicrosoftAdDomainRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create microsoft ad domain method over gRPC.

        Creates a Microsoft AD domain.

        Returns:
            Callable[[~.CreateMicrosoftAdDomainRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_microsoft_ad_domain" not in self._stubs:
            self._stubs["create_microsoft_ad_domain"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.managedidentities.v1.ManagedIdentitiesService/CreateMicrosoftAdDomain",
                    request_serializer=managed_identities_service.CreateMicrosoftAdDomainRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_microsoft_ad_domain"]

    @property
    def reset_admin_password(
        self,
    ) -> Callable[
        [managed_identities_service.ResetAdminPasswordRequest],
        managed_identities_service.ResetAdminPasswordResponse,
    ]:
        r"""Return a callable for the reset admin password method over gRPC.

        Resets a domain's administrator password.

        Returns:
            Callable[[~.ResetAdminPasswordRequest],
                    ~.ResetAdminPasswordResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_admin_password" not in self._stubs:
            self._stubs["reset_admin_password"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/ResetAdminPassword",
                request_serializer=managed_identities_service.ResetAdminPasswordRequest.serialize,
                response_deserializer=managed_identities_service.ResetAdminPasswordResponse.deserialize,
            )
        return self._stubs["reset_admin_password"]

    @property
    def list_domains(
        self,
    ) -> Callable[
        [managed_identities_service.ListDomainsRequest],
        managed_identities_service.ListDomainsResponse,
    ]:
        r"""Return a callable for the list domains method over gRPC.

        Lists domains in a project.

        Returns:
            Callable[[~.ListDomainsRequest],
                    ~.ListDomainsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_domains" not in self._stubs:
            self._stubs["list_domains"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/ListDomains",
                request_serializer=managed_identities_service.ListDomainsRequest.serialize,
                response_deserializer=managed_identities_service.ListDomainsResponse.deserialize,
            )
        return self._stubs["list_domains"]

    @property
    def get_domain(
        self,
    ) -> Callable[[managed_identities_service.GetDomainRequest], resource.Domain]:
        r"""Return a callable for the get domain method over gRPC.

        Gets information about a domain.

        Returns:
            Callable[[~.GetDomainRequest],
                    ~.Domain]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_domain" not in self._stubs:
            self._stubs["get_domain"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/GetDomain",
                request_serializer=managed_identities_service.GetDomainRequest.serialize,
                response_deserializer=resource.Domain.deserialize,
            )
        return self._stubs["get_domain"]

    @property
    def update_domain(
        self,
    ) -> Callable[
        [managed_identities_service.UpdateDomainRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update domain method over gRPC.

        Updates the metadata and configuration of a domain.

        Returns:
            Callable[[~.UpdateDomainRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_domain" not in self._stubs:
            self._stubs["update_domain"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/UpdateDomain",
                request_serializer=managed_identities_service.UpdateDomainRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_domain"]

    @property
    def delete_domain(
        self,
    ) -> Callable[
        [managed_identities_service.DeleteDomainRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete domain method over gRPC.

        Deletes a domain.

        Returns:
            Callable[[~.DeleteDomainRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_domain" not in self._stubs:
            self._stubs["delete_domain"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/DeleteDomain",
                request_serializer=managed_identities_service.DeleteDomainRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_domain"]

    @property
    def attach_trust(
        self,
    ) -> Callable[
        [managed_identities_service.AttachTrustRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the attach trust method over gRPC.

        Adds an AD trust to a domain.

        Returns:
            Callable[[~.AttachTrustRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "attach_trust" not in self._stubs:
            self._stubs["attach_trust"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/AttachTrust",
                request_serializer=managed_identities_service.AttachTrustRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["attach_trust"]

    @property
    def reconfigure_trust(
        self,
    ) -> Callable[
        [managed_identities_service.ReconfigureTrustRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the reconfigure trust method over gRPC.

        Updates the DNS conditional forwarder.

        Returns:
            Callable[[~.ReconfigureTrustRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reconfigure_trust" not in self._stubs:
            self._stubs["reconfigure_trust"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/ReconfigureTrust",
                request_serializer=managed_identities_service.ReconfigureTrustRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reconfigure_trust"]

    @property
    def detach_trust(
        self,
    ) -> Callable[
        [managed_identities_service.DetachTrustRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the detach trust method over gRPC.

        Removes an AD trust.

        Returns:
            Callable[[~.DetachTrustRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "detach_trust" not in self._stubs:
            self._stubs["detach_trust"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/DetachTrust",
                request_serializer=managed_identities_service.DetachTrustRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["detach_trust"]

    @property
    def validate_trust(
        self,
    ) -> Callable[
        [managed_identities_service.ValidateTrustRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the validate trust method over gRPC.

        Validates a trust state, that the target domain is
        reachable, and that the target domain is able to accept
        incoming trust requests.

        Returns:
            Callable[[~.ValidateTrustRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "validate_trust" not in self._stubs:
            self._stubs["validate_trust"] = self._logged_channel.unary_unary(
                "/google.cloud.managedidentities.v1.ManagedIdentitiesService/ValidateTrust",
                request_serializer=managed_identities_service.ValidateTrustRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["validate_trust"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("ManagedIdentitiesServiceGrpcTransport",)
