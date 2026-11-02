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

from google.cloud.security.privateca_v1.types import resources, service

from .base import DEFAULT_CLIENT_INFO, CertificateAuthorityServiceTransport
from .grpc import CertificateAuthorityServiceGrpcTransport

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
                    "serviceName": "google.cloud.security.privateca.v1.CertificateAuthorityService",
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
                    "serviceName": "google.cloud.security.privateca.v1.CertificateAuthorityService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class CertificateAuthorityServiceGrpcAsyncIOTransport(
    CertificateAuthorityServiceTransport
):
    """gRPC AsyncIO backend transport for CertificateAuthorityService.

    [Certificate Authority
    Service][google.cloud.security.privateca.v1.CertificateAuthorityService]
    manages private certificate authorities and issued certificates.

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
        host: str = "privateca.googleapis.com",
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
        host: str = "privateca.googleapis.com",
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
                 The hostname to connect to (default: 'privateca.googleapis.com').
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
    def create_certificate(
        self,
    ) -> Callable[[service.CreateCertificateRequest], Awaitable[resources.Certificate]]:
        r"""Return a callable for the create certificate method over gRPC.

        Create a new
        [Certificate][google.cloud.security.privateca.v1.Certificate] in
        a given Project, Location from a particular
        [CaPool][google.cloud.security.privateca.v1.CaPool].

        Returns:
            Callable[[~.CreateCertificateRequest],
                    Awaitable[~.Certificate]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_certificate" not in self._stubs:
            self._stubs["create_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificate",
                request_serializer=service.CreateCertificateRequest.serialize,
                response_deserializer=resources.Certificate.deserialize,
            )
        return self._stubs["create_certificate"]

    @property
    def get_certificate(
        self,
    ) -> Callable[[service.GetCertificateRequest], Awaitable[resources.Certificate]]:
        r"""Return a callable for the get certificate method over gRPC.

        Returns a
        [Certificate][google.cloud.security.privateca.v1.Certificate].

        Returns:
            Callable[[~.GetCertificateRequest],
                    Awaitable[~.Certificate]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate" not in self._stubs:
            self._stubs["get_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificate",
                request_serializer=service.GetCertificateRequest.serialize,
                response_deserializer=resources.Certificate.deserialize,
            )
        return self._stubs["get_certificate"]

    @property
    def list_certificates(
        self,
    ) -> Callable[
        [service.ListCertificatesRequest], Awaitable[service.ListCertificatesResponse]
    ]:
        r"""Return a callable for the list certificates method over gRPC.

        Lists
        [Certificates][google.cloud.security.privateca.v1.Certificate].

        Returns:
            Callable[[~.ListCertificatesRequest],
                    Awaitable[~.ListCertificatesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_certificates" not in self._stubs:
            self._stubs["list_certificates"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificates",
                request_serializer=service.ListCertificatesRequest.serialize,
                response_deserializer=service.ListCertificatesResponse.deserialize,
            )
        return self._stubs["list_certificates"]

    @property
    def revoke_certificate(
        self,
    ) -> Callable[[service.RevokeCertificateRequest], Awaitable[resources.Certificate]]:
        r"""Return a callable for the revoke certificate method over gRPC.

        Revoke a
        [Certificate][google.cloud.security.privateca.v1.Certificate].

        Returns:
            Callable[[~.RevokeCertificateRequest],
                    Awaitable[~.Certificate]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "revoke_certificate" not in self._stubs:
            self._stubs["revoke_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/RevokeCertificate",
                request_serializer=service.RevokeCertificateRequest.serialize,
                response_deserializer=resources.Certificate.deserialize,
            )
        return self._stubs["revoke_certificate"]

    @property
    def update_certificate(
        self,
    ) -> Callable[[service.UpdateCertificateRequest], Awaitable[resources.Certificate]]:
        r"""Return a callable for the update certificate method over gRPC.

        Update a
        [Certificate][google.cloud.security.privateca.v1.Certificate].
        Currently, the only field you can update is the
        [labels][google.cloud.security.privateca.v1.Certificate.labels]
        field.

        Returns:
            Callable[[~.UpdateCertificateRequest],
                    Awaitable[~.Certificate]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_certificate" not in self._stubs:
            self._stubs["update_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificate",
                request_serializer=service.UpdateCertificateRequest.serialize,
                response_deserializer=resources.Certificate.deserialize,
            )
        return self._stubs["update_certificate"]

    @property
    def activate_certificate_authority(
        self,
    ) -> Callable[
        [service.ActivateCertificateAuthorityRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the activate certificate authority method over gRPC.

        Activate a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that is in state
        [AWAITING_USER_ACTIVATION][google.cloud.security.privateca.v1.CertificateAuthority.State.AWAITING_USER_ACTIVATION]
        and is of type
        [SUBORDINATE][google.cloud.security.privateca.v1.CertificateAuthority.Type.SUBORDINATE].
        After the parent Certificate Authority signs a certificate
        signing request from
        [FetchCertificateAuthorityCsr][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr],
        this method can complete the activation process.

        Returns:
            Callable[[~.ActivateCertificateAuthorityRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "activate_certificate_authority" not in self._stubs:
            self._stubs["activate_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/ActivateCertificateAuthority",
                    request_serializer=service.ActivateCertificateAuthorityRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["activate_certificate_authority"]

    @property
    def create_certificate_authority(
        self,
    ) -> Callable[
        [service.CreateCertificateAuthorityRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create certificate authority method over gRPC.

        Create a new
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        in a given Project and Location.

        Returns:
            Callable[[~.CreateCertificateAuthorityRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_certificate_authority" not in self._stubs:
            self._stubs["create_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateAuthority",
                    request_serializer=service.CreateCertificateAuthorityRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_certificate_authority"]

    @property
    def disable_certificate_authority(
        self,
    ) -> Callable[
        [service.DisableCertificateAuthorityRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the disable certificate authority method over gRPC.

        Disable a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        Returns:
            Callable[[~.DisableCertificateAuthorityRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "disable_certificate_authority" not in self._stubs:
            self._stubs["disable_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/DisableCertificateAuthority",
                    request_serializer=service.DisableCertificateAuthorityRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["disable_certificate_authority"]

    @property
    def enable_certificate_authority(
        self,
    ) -> Callable[
        [service.EnableCertificateAuthorityRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the enable certificate authority method over gRPC.

        Enable a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        Returns:
            Callable[[~.EnableCertificateAuthorityRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "enable_certificate_authority" not in self._stubs:
            self._stubs["enable_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/EnableCertificateAuthority",
                    request_serializer=service.EnableCertificateAuthorityRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["enable_certificate_authority"]

    @property
    def fetch_certificate_authority_csr(
        self,
    ) -> Callable[
        [service.FetchCertificateAuthorityCsrRequest],
        Awaitable[service.FetchCertificateAuthorityCsrResponse],
    ]:
        r"""Return a callable for the fetch certificate authority
        csr method over gRPC.

        Fetch a certificate signing request (CSR) from a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that is in state
        [AWAITING_USER_ACTIVATION][google.cloud.security.privateca.v1.CertificateAuthority.State.AWAITING_USER_ACTIVATION]
        and is of type
        [SUBORDINATE][google.cloud.security.privateca.v1.CertificateAuthority.Type.SUBORDINATE].
        The CSR must then be signed by the desired parent Certificate
        Authority, which could be another
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        resource, or could be an on-prem certificate authority. See also
        [ActivateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.ActivateCertificateAuthority].

        Returns:
            Callable[[~.FetchCertificateAuthorityCsrRequest],
                    Awaitable[~.FetchCertificateAuthorityCsrResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_certificate_authority_csr" not in self._stubs:
            self._stubs["fetch_certificate_authority_csr"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCertificateAuthorityCsr",
                    request_serializer=service.FetchCertificateAuthorityCsrRequest.serialize,
                    response_deserializer=service.FetchCertificateAuthorityCsrResponse.deserialize,
                )
            )
        return self._stubs["fetch_certificate_authority_csr"]

    @property
    def get_certificate_authority(
        self,
    ) -> Callable[
        [service.GetCertificateAuthorityRequest],
        Awaitable[resources.CertificateAuthority],
    ]:
        r"""Return a callable for the get certificate authority method over gRPC.

        Returns a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        Returns:
            Callable[[~.GetCertificateAuthorityRequest],
                    Awaitable[~.CertificateAuthority]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate_authority" not in self._stubs:
            self._stubs["get_certificate_authority"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateAuthority",
                request_serializer=service.GetCertificateAuthorityRequest.serialize,
                response_deserializer=resources.CertificateAuthority.deserialize,
            )
        return self._stubs["get_certificate_authority"]

    @property
    def list_certificate_authorities(
        self,
    ) -> Callable[
        [service.ListCertificateAuthoritiesRequest],
        Awaitable[service.ListCertificateAuthoritiesResponse],
    ]:
        r"""Return a callable for the list certificate authorities method over gRPC.

        Lists
        [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority].

        Returns:
            Callable[[~.ListCertificateAuthoritiesRequest],
                    Awaitable[~.ListCertificateAuthoritiesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_certificate_authorities" not in self._stubs:
            self._stubs["list_certificate_authorities"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateAuthorities",
                    request_serializer=service.ListCertificateAuthoritiesRequest.serialize,
                    response_deserializer=service.ListCertificateAuthoritiesResponse.deserialize,
                )
            )
        return self._stubs["list_certificate_authorities"]

    @property
    def undelete_certificate_authority(
        self,
    ) -> Callable[
        [service.UndeleteCertificateAuthorityRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the undelete certificate authority method over gRPC.

        Undelete a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that has been deleted.

        Returns:
            Callable[[~.UndeleteCertificateAuthorityRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undelete_certificate_authority" not in self._stubs:
            self._stubs["undelete_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/UndeleteCertificateAuthority",
                    request_serializer=service.UndeleteCertificateAuthorityRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["undelete_certificate_authority"]

    @property
    def delete_certificate_authority(
        self,
    ) -> Callable[
        [service.DeleteCertificateAuthorityRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete certificate authority method over gRPC.

        Delete a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        Returns:
            Callable[[~.DeleteCertificateAuthorityRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_certificate_authority" not in self._stubs:
            self._stubs["delete_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateAuthority",
                    request_serializer=service.DeleteCertificateAuthorityRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_certificate_authority"]

    @property
    def update_certificate_authority(
        self,
    ) -> Callable[
        [service.UpdateCertificateAuthorityRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update certificate authority method over gRPC.

        Update a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        Returns:
            Callable[[~.UpdateCertificateAuthorityRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_certificate_authority" not in self._stubs:
            self._stubs["update_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateAuthority",
                    request_serializer=service.UpdateCertificateAuthorityRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_certificate_authority"]

    @property
    def create_ca_pool(
        self,
    ) -> Callable[[service.CreateCaPoolRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create ca pool method over gRPC.

        Create a [CaPool][google.cloud.security.privateca.v1.CaPool].

        Returns:
            Callable[[~.CreateCaPoolRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_ca_pool" not in self._stubs:
            self._stubs["create_ca_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCaPool",
                request_serializer=service.CreateCaPoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_ca_pool"]

    @property
    def update_ca_pool(
        self,
    ) -> Callable[[service.UpdateCaPoolRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update ca pool method over gRPC.

        Update a [CaPool][google.cloud.security.privateca.v1.CaPool].

        Returns:
            Callable[[~.UpdateCaPoolRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_ca_pool" not in self._stubs:
            self._stubs["update_ca_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCaPool",
                request_serializer=service.UpdateCaPoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_ca_pool"]

    @property
    def get_ca_pool(
        self,
    ) -> Callable[[service.GetCaPoolRequest], Awaitable[resources.CaPool]]:
        r"""Return a callable for the get ca pool method over gRPC.

        Returns a [CaPool][google.cloud.security.privateca.v1.CaPool].

        Returns:
            Callable[[~.GetCaPoolRequest],
                    Awaitable[~.CaPool]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_ca_pool" not in self._stubs:
            self._stubs["get_ca_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCaPool",
                request_serializer=service.GetCaPoolRequest.serialize,
                response_deserializer=resources.CaPool.deserialize,
            )
        return self._stubs["get_ca_pool"]

    @property
    def list_ca_pools(
        self,
    ) -> Callable[[service.ListCaPoolsRequest], Awaitable[service.ListCaPoolsResponse]]:
        r"""Return a callable for the list ca pools method over gRPC.

        Lists [CaPools][google.cloud.security.privateca.v1.CaPool].

        Returns:
            Callable[[~.ListCaPoolsRequest],
                    Awaitable[~.ListCaPoolsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_ca_pools" not in self._stubs:
            self._stubs["list_ca_pools"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCaPools",
                request_serializer=service.ListCaPoolsRequest.serialize,
                response_deserializer=service.ListCaPoolsResponse.deserialize,
            )
        return self._stubs["list_ca_pools"]

    @property
    def delete_ca_pool(
        self,
    ) -> Callable[[service.DeleteCaPoolRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete ca pool method over gRPC.

        Delete a [CaPool][google.cloud.security.privateca.v1.CaPool].

        Returns:
            Callable[[~.DeleteCaPoolRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_ca_pool" not in self._stubs:
            self._stubs["delete_ca_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCaPool",
                request_serializer=service.DeleteCaPoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_ca_pool"]

    @property
    def fetch_ca_certs(
        self,
    ) -> Callable[
        [service.FetchCaCertsRequest], Awaitable[service.FetchCaCertsResponse]
    ]:
        r"""Return a callable for the fetch ca certs method over gRPC.

        FetchCaCerts returns the current trust anchor for the
        [CaPool][google.cloud.security.privateca.v1.CaPool]. This will
        include CA certificate chains for all certificate authorities in
        the ENABLED, DISABLED, or STAGED states.

        Returns:
            Callable[[~.FetchCaCertsRequest],
                    Awaitable[~.FetchCaCertsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_ca_certs" not in self._stubs:
            self._stubs["fetch_ca_certs"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCaCerts",
                request_serializer=service.FetchCaCertsRequest.serialize,
                response_deserializer=service.FetchCaCertsResponse.deserialize,
            )
        return self._stubs["fetch_ca_certs"]

    @property
    def get_certificate_revocation_list(
        self,
    ) -> Callable[
        [service.GetCertificateRevocationListRequest],
        Awaitable[resources.CertificateRevocationList],
    ]:
        r"""Return a callable for the get certificate revocation
        list method over gRPC.

        Returns a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].

        Returns:
            Callable[[~.GetCertificateRevocationListRequest],
                    Awaitable[~.CertificateRevocationList]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate_revocation_list" not in self._stubs:
            self._stubs["get_certificate_revocation_list"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateRevocationList",
                    request_serializer=service.GetCertificateRevocationListRequest.serialize,
                    response_deserializer=resources.CertificateRevocationList.deserialize,
                )
            )
        return self._stubs["get_certificate_revocation_list"]

    @property
    def list_certificate_revocation_lists(
        self,
    ) -> Callable[
        [service.ListCertificateRevocationListsRequest],
        Awaitable[service.ListCertificateRevocationListsResponse],
    ]:
        r"""Return a callable for the list certificate revocation
        lists method over gRPC.

        Lists
        [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList].

        Returns:
            Callable[[~.ListCertificateRevocationListsRequest],
                    Awaitable[~.ListCertificateRevocationListsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_certificate_revocation_lists" not in self._stubs:
            self._stubs["list_certificate_revocation_lists"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateRevocationLists",
                    request_serializer=service.ListCertificateRevocationListsRequest.serialize,
                    response_deserializer=service.ListCertificateRevocationListsResponse.deserialize,
                )
            )
        return self._stubs["list_certificate_revocation_lists"]

    @property
    def update_certificate_revocation_list(
        self,
    ) -> Callable[
        [service.UpdateCertificateRevocationListRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update certificate revocation
        list method over gRPC.

        Update a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].

        Returns:
            Callable[[~.UpdateCertificateRevocationListRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_certificate_revocation_list" not in self._stubs:
            self._stubs["update_certificate_revocation_list"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateRevocationList",
                    request_serializer=service.UpdateCertificateRevocationListRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_certificate_revocation_list"]

    @property
    def create_certificate_template(
        self,
    ) -> Callable[
        [service.CreateCertificateTemplateRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create certificate template method over gRPC.

        Create a new
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
        in a given Project and Location.

        Returns:
            Callable[[~.CreateCertificateTemplateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_certificate_template" not in self._stubs:
            self._stubs["create_certificate_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateTemplate",
                    request_serializer=service.CreateCertificateTemplateRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_certificate_template"]

    @property
    def delete_certificate_template(
        self,
    ) -> Callable[
        [service.DeleteCertificateTemplateRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete certificate template method over gRPC.

        DeleteCertificateTemplate deletes a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].

        Returns:
            Callable[[~.DeleteCertificateTemplateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_certificate_template" not in self._stubs:
            self._stubs["delete_certificate_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateTemplate",
                    request_serializer=service.DeleteCertificateTemplateRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_certificate_template"]

    @property
    def get_certificate_template(
        self,
    ) -> Callable[
        [service.GetCertificateTemplateRequest],
        Awaitable[resources.CertificateTemplate],
    ]:
        r"""Return a callable for the get certificate template method over gRPC.

        Returns a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].

        Returns:
            Callable[[~.GetCertificateTemplateRequest],
                    Awaitable[~.CertificateTemplate]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate_template" not in self._stubs:
            self._stubs["get_certificate_template"] = self._logged_channel.unary_unary(
                "/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateTemplate",
                request_serializer=service.GetCertificateTemplateRequest.serialize,
                response_deserializer=resources.CertificateTemplate.deserialize,
            )
        return self._stubs["get_certificate_template"]

    @property
    def list_certificate_templates(
        self,
    ) -> Callable[
        [service.ListCertificateTemplatesRequest],
        Awaitable[service.ListCertificateTemplatesResponse],
    ]:
        r"""Return a callable for the list certificate templates method over gRPC.

        Lists
        [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate].

        Returns:
            Callable[[~.ListCertificateTemplatesRequest],
                    Awaitable[~.ListCertificateTemplatesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_certificate_templates" not in self._stubs:
            self._stubs["list_certificate_templates"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateTemplates",
                    request_serializer=service.ListCertificateTemplatesRequest.serialize,
                    response_deserializer=service.ListCertificateTemplatesResponse.deserialize,
                )
            )
        return self._stubs["list_certificate_templates"]

    @property
    def update_certificate_template(
        self,
    ) -> Callable[
        [service.UpdateCertificateTemplateRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update certificate template method over gRPC.

        Update a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].

        Returns:
            Callable[[~.UpdateCertificateTemplateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_certificate_template" not in self._stubs:
            self._stubs["update_certificate_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateTemplate",
                    request_serializer=service.UpdateCertificateTemplateRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_certificate_template"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_certificate: self._wrap_method(
                self.create_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_certificate: self._wrap_method(
                self.get_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_certificates: self._wrap_method(
                self.list_certificates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.revoke_certificate: self._wrap_method(
                self.revoke_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_certificate: self._wrap_method(
                self.update_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.activate_certificate_authority: self._wrap_method(
                self.activate_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_certificate_authority: self._wrap_method(
                self.create_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.disable_certificate_authority: self._wrap_method(
                self.disable_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enable_certificate_authority: self._wrap_method(
                self.enable_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_certificate_authority_csr: self._wrap_method(
                self.fetch_certificate_authority_csr,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_certificate_authority: self._wrap_method(
                self.get_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_certificate_authorities: self._wrap_method(
                self.list_certificate_authorities,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undelete_certificate_authority: self._wrap_method(
                self.undelete_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_certificate_authority: self._wrap_method(
                self.delete_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_certificate_authority: self._wrap_method(
                self.update_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_ca_pool: self._wrap_method(
                self.create_ca_pool,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_ca_pool: self._wrap_method(
                self.update_ca_pool,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_ca_pool: self._wrap_method(
                self.get_ca_pool,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_ca_pools: self._wrap_method(
                self.list_ca_pools,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_ca_pool: self._wrap_method(
                self.delete_ca_pool,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_ca_certs: self._wrap_method(
                self.fetch_ca_certs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_certificate_revocation_list: self._wrap_method(
                self.get_certificate_revocation_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_certificate_revocation_lists: self._wrap_method(
                self.list_certificate_revocation_lists,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_certificate_revocation_list: self._wrap_method(
                self.update_certificate_revocation_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_certificate_template: self._wrap_method(
                self.create_certificate_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_certificate_template: self._wrap_method(
                self.delete_certificate_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_certificate_template: self._wrap_method(
                self.get_certificate_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_certificate_templates: self._wrap_method(
                self.list_certificate_templates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_certificate_template: self._wrap_method(
                self.update_certificate_template,
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


__all__ = ("CertificateAuthorityServiceGrpcAsyncIOTransport",)
