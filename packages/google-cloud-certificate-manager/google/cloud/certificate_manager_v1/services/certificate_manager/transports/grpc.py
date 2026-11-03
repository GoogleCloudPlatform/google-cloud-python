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

from google.cloud.certificate_manager_v1.types import (
    certificate_issuance_config,
    certificate_manager,
    trust_config,
)
from google.cloud.certificate_manager_v1.types import (
    certificate_issuance_config as gcc_certificate_issuance_config,
)
from google.cloud.certificate_manager_v1.types import trust_config as gcc_trust_config

from .base import DEFAULT_CLIENT_INFO, CertificateManagerTransport

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
                    "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
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
                    "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class CertificateManagerGrpcTransport(CertificateManagerTransport):
    """gRPC backend transport for CertificateManager.

    API Overview

    Certificates Manager API allows customers to see and manage all
    their TLS certificates.

    Certificates Manager API service provides methods to manage
    certificates, group them into collections, and create serving
    configuration that can be easily applied to other Cloud resources
    e.g. Target Proxies.

    Data Model

    The Certificates Manager service exposes the following resources:

    - ``Certificate`` that describes a single TLS certificate.
    - ``CertificateMap`` that describes a collection of certificates
      that can be attached to a target resource.
    - ``CertificateMapEntry`` that describes a single configuration
      entry that consists of a SNI and a group of certificates. It's a
      subresource of CertificateMap.

    Certificate, CertificateMap and CertificateMapEntry IDs have to
    fully match the regexp ``[a-z0-9-]{1,63}``. In other words,

    - only lower case letters, digits, and hyphen are allowed
    - length of the resource ID has to be in [1,63] range.

    Provides methods to manage Cloud Certificate Manager entities.

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
        host: str = "certificatemanager.googleapis.com",
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
                 The hostname to connect to (default: 'certificatemanager.googleapis.com').
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
        host: str = "certificatemanager.googleapis.com",
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
    def list_certificates(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificatesRequest],
        certificate_manager.ListCertificatesResponse,
    ]:
        r"""Return a callable for the list certificates method over gRPC.

        Lists Certificates in a given project and location.

        Returns:
            Callable[[~.ListCertificatesRequest],
                    ~.ListCertificatesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_certificates" not in self._stubs:
            self._stubs["list_certificates"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/ListCertificates",
                request_serializer=certificate_manager.ListCertificatesRequest.serialize,
                response_deserializer=certificate_manager.ListCertificatesResponse.deserialize,
            )
        return self._stubs["list_certificates"]

    @property
    def get_certificate(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateRequest], certificate_manager.Certificate
    ]:
        r"""Return a callable for the get certificate method over gRPC.

        Gets details of a single Certificate.

        Returns:
            Callable[[~.GetCertificateRequest],
                    ~.Certificate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate" not in self._stubs:
            self._stubs["get_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/GetCertificate",
                request_serializer=certificate_manager.GetCertificateRequest.serialize,
                response_deserializer=certificate_manager.Certificate.deserialize,
            )
        return self._stubs["get_certificate"]

    @property
    def create_certificate(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create certificate method over gRPC.

        Creates a new Certificate in a given project and
        location.

        Returns:
            Callable[[~.CreateCertificateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_certificate" not in self._stubs:
            self._stubs["create_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/CreateCertificate",
                request_serializer=certificate_manager.CreateCertificateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_certificate"]

    @property
    def update_certificate(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update certificate method over gRPC.

        Updates a Certificate.

        Returns:
            Callable[[~.UpdateCertificateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_certificate" not in self._stubs:
            self._stubs["update_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/UpdateCertificate",
                request_serializer=certificate_manager.UpdateCertificateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_certificate"]

    @property
    def delete_certificate(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete certificate method over gRPC.

        Deletes a single Certificate.

        Returns:
            Callable[[~.DeleteCertificateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_certificate" not in self._stubs:
            self._stubs["delete_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/DeleteCertificate",
                request_serializer=certificate_manager.DeleteCertificateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_certificate"]

    @property
    def list_certificate_maps(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificateMapsRequest],
        certificate_manager.ListCertificateMapsResponse,
    ]:
        r"""Return a callable for the list certificate maps method over gRPC.

        Lists CertificateMaps in a given project and
        location.

        Returns:
            Callable[[~.ListCertificateMapsRequest],
                    ~.ListCertificateMapsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_certificate_maps" not in self._stubs:
            self._stubs["list_certificate_maps"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/ListCertificateMaps",
                request_serializer=certificate_manager.ListCertificateMapsRequest.serialize,
                response_deserializer=certificate_manager.ListCertificateMapsResponse.deserialize,
            )
        return self._stubs["list_certificate_maps"]

    @property
    def get_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateMapRequest],
        certificate_manager.CertificateMap,
    ]:
        r"""Return a callable for the get certificate map method over gRPC.

        Gets details of a single CertificateMap.

        Returns:
            Callable[[~.GetCertificateMapRequest],
                    ~.CertificateMap]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate_map" not in self._stubs:
            self._stubs["get_certificate_map"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/GetCertificateMap",
                request_serializer=certificate_manager.GetCertificateMapRequest.serialize,
                response_deserializer=certificate_manager.CertificateMap.deserialize,
            )
        return self._stubs["get_certificate_map"]

    @property
    def create_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateMapRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create certificate map method over gRPC.

        Creates a new CertificateMap in a given project and
        location.

        Returns:
            Callable[[~.CreateCertificateMapRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_certificate_map" not in self._stubs:
            self._stubs["create_certificate_map"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/CreateCertificateMap",
                request_serializer=certificate_manager.CreateCertificateMapRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_certificate_map"]

    @property
    def update_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateMapRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update certificate map method over gRPC.

        Updates a CertificateMap.

        Returns:
            Callable[[~.UpdateCertificateMapRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_certificate_map" not in self._stubs:
            self._stubs["update_certificate_map"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/UpdateCertificateMap",
                request_serializer=certificate_manager.UpdateCertificateMapRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_certificate_map"]

    @property
    def delete_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateMapRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete certificate map method over gRPC.

        Deletes a single CertificateMap. A Certificate Map
        can't be deleted if it contains Certificate Map Entries.
        Remove all the entries from the map before calling this
        method.

        Returns:
            Callable[[~.DeleteCertificateMapRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_certificate_map" not in self._stubs:
            self._stubs["delete_certificate_map"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/DeleteCertificateMap",
                request_serializer=certificate_manager.DeleteCertificateMapRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_certificate_map"]

    @property
    def list_certificate_map_entries(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificateMapEntriesRequest],
        certificate_manager.ListCertificateMapEntriesResponse,
    ]:
        r"""Return a callable for the list certificate map entries method over gRPC.

        Lists CertificateMapEntries in a given project and
        location.

        Returns:
            Callable[[~.ListCertificateMapEntriesRequest],
                    ~.ListCertificateMapEntriesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_certificate_map_entries" not in self._stubs:
            self._stubs["list_certificate_map_entries"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/ListCertificateMapEntries",
                    request_serializer=certificate_manager.ListCertificateMapEntriesRequest.serialize,
                    response_deserializer=certificate_manager.ListCertificateMapEntriesResponse.deserialize,
                )
            )
        return self._stubs["list_certificate_map_entries"]

    @property
    def get_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateMapEntryRequest],
        certificate_manager.CertificateMapEntry,
    ]:
        r"""Return a callable for the get certificate map entry method over gRPC.

        Gets details of a single CertificateMapEntry.

        Returns:
            Callable[[~.GetCertificateMapEntryRequest],
                    ~.CertificateMapEntry]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate_map_entry" not in self._stubs:
            self._stubs["get_certificate_map_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/GetCertificateMapEntry",
                request_serializer=certificate_manager.GetCertificateMapEntryRequest.serialize,
                response_deserializer=certificate_manager.CertificateMapEntry.deserialize,
            )
        return self._stubs["get_certificate_map_entry"]

    @property
    def create_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateMapEntryRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create certificate map entry method over gRPC.

        Creates a new CertificateMapEntry in a given project
        and location.

        Returns:
            Callable[[~.CreateCertificateMapEntryRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_certificate_map_entry" not in self._stubs:
            self._stubs["create_certificate_map_entry"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/CreateCertificateMapEntry",
                    request_serializer=certificate_manager.CreateCertificateMapEntryRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_certificate_map_entry"]

    @property
    def update_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateMapEntryRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update certificate map entry method over gRPC.

        Updates a CertificateMapEntry.

        Returns:
            Callable[[~.UpdateCertificateMapEntryRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_certificate_map_entry" not in self._stubs:
            self._stubs["update_certificate_map_entry"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/UpdateCertificateMapEntry",
                    request_serializer=certificate_manager.UpdateCertificateMapEntryRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_certificate_map_entry"]

    @property
    def delete_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateMapEntryRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete certificate map entry method over gRPC.

        Deletes a single CertificateMapEntry.

        Returns:
            Callable[[~.DeleteCertificateMapEntryRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_certificate_map_entry" not in self._stubs:
            self._stubs["delete_certificate_map_entry"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/DeleteCertificateMapEntry",
                    request_serializer=certificate_manager.DeleteCertificateMapEntryRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_certificate_map_entry"]

    @property
    def list_dns_authorizations(
        self,
    ) -> Callable[
        [certificate_manager.ListDnsAuthorizationsRequest],
        certificate_manager.ListDnsAuthorizationsResponse,
    ]:
        r"""Return a callable for the list dns authorizations method over gRPC.

        Lists DnsAuthorizations in a given project and
        location.

        Returns:
            Callable[[~.ListDnsAuthorizationsRequest],
                    ~.ListDnsAuthorizationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_dns_authorizations" not in self._stubs:
            self._stubs["list_dns_authorizations"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/ListDnsAuthorizations",
                request_serializer=certificate_manager.ListDnsAuthorizationsRequest.serialize,
                response_deserializer=certificate_manager.ListDnsAuthorizationsResponse.deserialize,
            )
        return self._stubs["list_dns_authorizations"]

    @property
    def get_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.GetDnsAuthorizationRequest],
        certificate_manager.DnsAuthorization,
    ]:
        r"""Return a callable for the get dns authorization method over gRPC.

        Gets details of a single DnsAuthorization.

        Returns:
            Callable[[~.GetDnsAuthorizationRequest],
                    ~.DnsAuthorization]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dns_authorization" not in self._stubs:
            self._stubs["get_dns_authorization"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/GetDnsAuthorization",
                request_serializer=certificate_manager.GetDnsAuthorizationRequest.serialize,
                response_deserializer=certificate_manager.DnsAuthorization.deserialize,
            )
        return self._stubs["get_dns_authorization"]

    @property
    def create_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.CreateDnsAuthorizationRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create dns authorization method over gRPC.

        Creates a new DnsAuthorization in a given project and
        location.

        Returns:
            Callable[[~.CreateDnsAuthorizationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_dns_authorization" not in self._stubs:
            self._stubs["create_dns_authorization"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/CreateDnsAuthorization",
                request_serializer=certificate_manager.CreateDnsAuthorizationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_dns_authorization"]

    @property
    def update_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.UpdateDnsAuthorizationRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update dns authorization method over gRPC.

        Updates a DnsAuthorization.

        Returns:
            Callable[[~.UpdateDnsAuthorizationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_dns_authorization" not in self._stubs:
            self._stubs["update_dns_authorization"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/UpdateDnsAuthorization",
                request_serializer=certificate_manager.UpdateDnsAuthorizationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_dns_authorization"]

    @property
    def delete_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.DeleteDnsAuthorizationRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete dns authorization method over gRPC.

        Deletes a single DnsAuthorization.

        Returns:
            Callable[[~.DeleteDnsAuthorizationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_dns_authorization" not in self._stubs:
            self._stubs["delete_dns_authorization"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/DeleteDnsAuthorization",
                request_serializer=certificate_manager.DeleteDnsAuthorizationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_dns_authorization"]

    @property
    def list_certificate_issuance_configs(
        self,
    ) -> Callable[
        [certificate_issuance_config.ListCertificateIssuanceConfigsRequest],
        certificate_issuance_config.ListCertificateIssuanceConfigsResponse,
    ]:
        r"""Return a callable for the list certificate issuance
        configs method over gRPC.

        Lists CertificateIssuanceConfigs in a given project
        and location.

        Returns:
            Callable[[~.ListCertificateIssuanceConfigsRequest],
                    ~.ListCertificateIssuanceConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_certificate_issuance_configs" not in self._stubs:
            self._stubs["list_certificate_issuance_configs"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/ListCertificateIssuanceConfigs",
                    request_serializer=certificate_issuance_config.ListCertificateIssuanceConfigsRequest.serialize,
                    response_deserializer=certificate_issuance_config.ListCertificateIssuanceConfigsResponse.deserialize,
                )
            )
        return self._stubs["list_certificate_issuance_configs"]

    @property
    def get_certificate_issuance_config(
        self,
    ) -> Callable[
        [certificate_issuance_config.GetCertificateIssuanceConfigRequest],
        certificate_issuance_config.CertificateIssuanceConfig,
    ]:
        r"""Return a callable for the get certificate issuance
        config method over gRPC.

        Gets details of a single CertificateIssuanceConfig.

        Returns:
            Callable[[~.GetCertificateIssuanceConfigRequest],
                    ~.CertificateIssuanceConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate_issuance_config" not in self._stubs:
            self._stubs["get_certificate_issuance_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/GetCertificateIssuanceConfig",
                    request_serializer=certificate_issuance_config.GetCertificateIssuanceConfigRequest.serialize,
                    response_deserializer=certificate_issuance_config.CertificateIssuanceConfig.deserialize,
                )
            )
        return self._stubs["get_certificate_issuance_config"]

    @property
    def create_certificate_issuance_config(
        self,
    ) -> Callable[
        [gcc_certificate_issuance_config.CreateCertificateIssuanceConfigRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create certificate issuance
        config method over gRPC.

        Creates a new CertificateIssuanceConfig in a given
        project and location.

        Returns:
            Callable[[~.CreateCertificateIssuanceConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_certificate_issuance_config" not in self._stubs:
            self._stubs["create_certificate_issuance_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/CreateCertificateIssuanceConfig",
                    request_serializer=gcc_certificate_issuance_config.CreateCertificateIssuanceConfigRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_certificate_issuance_config"]

    @property
    def update_certificate_issuance_config(
        self,
    ) -> Callable[
        [gcc_certificate_issuance_config.UpdateCertificateIssuanceConfigRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the update certificate issuance
        config method over gRPC.

        Updates a CertificateIssuanceConfig.

        Returns:
            Callable[[~.UpdateCertificateIssuanceConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_certificate_issuance_config" not in self._stubs:
            self._stubs["update_certificate_issuance_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/UpdateCertificateIssuanceConfig",
                    request_serializer=gcc_certificate_issuance_config.UpdateCertificateIssuanceConfigRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_certificate_issuance_config"]

    @property
    def delete_certificate_issuance_config(
        self,
    ) -> Callable[
        [certificate_issuance_config.DeleteCertificateIssuanceConfigRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete certificate issuance
        config method over gRPC.

        Deletes a single CertificateIssuanceConfig.

        Returns:
            Callable[[~.DeleteCertificateIssuanceConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_certificate_issuance_config" not in self._stubs:
            self._stubs["delete_certificate_issuance_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.certificatemanager.v1.CertificateManager/DeleteCertificateIssuanceConfig",
                    request_serializer=certificate_issuance_config.DeleteCertificateIssuanceConfigRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_certificate_issuance_config"]

    @property
    def list_trust_configs(
        self,
    ) -> Callable[
        [trust_config.ListTrustConfigsRequest], trust_config.ListTrustConfigsResponse
    ]:
        r"""Return a callable for the list trust configs method over gRPC.

        Lists TrustConfigs in a given project and location.

        Returns:
            Callable[[~.ListTrustConfigsRequest],
                    ~.ListTrustConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_trust_configs" not in self._stubs:
            self._stubs["list_trust_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/ListTrustConfigs",
                request_serializer=trust_config.ListTrustConfigsRequest.serialize,
                response_deserializer=trust_config.ListTrustConfigsResponse.deserialize,
            )
        return self._stubs["list_trust_configs"]

    @property
    def get_trust_config(
        self,
    ) -> Callable[[trust_config.GetTrustConfigRequest], trust_config.TrustConfig]:
        r"""Return a callable for the get trust config method over gRPC.

        Gets details of a single TrustConfig.

        Returns:
            Callable[[~.GetTrustConfigRequest],
                    ~.TrustConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_trust_config" not in self._stubs:
            self._stubs["get_trust_config"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/GetTrustConfig",
                request_serializer=trust_config.GetTrustConfigRequest.serialize,
                response_deserializer=trust_config.TrustConfig.deserialize,
            )
        return self._stubs["get_trust_config"]

    @property
    def create_trust_config(
        self,
    ) -> Callable[
        [gcc_trust_config.CreateTrustConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create trust config method over gRPC.

        Creates a new TrustConfig in a given project and
        location.

        Returns:
            Callable[[~.CreateTrustConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_trust_config" not in self._stubs:
            self._stubs["create_trust_config"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/CreateTrustConfig",
                request_serializer=gcc_trust_config.CreateTrustConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_trust_config"]

    @property
    def update_trust_config(
        self,
    ) -> Callable[
        [gcc_trust_config.UpdateTrustConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update trust config method over gRPC.

        Updates a TrustConfig.

        Returns:
            Callable[[~.UpdateTrustConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_trust_config" not in self._stubs:
            self._stubs["update_trust_config"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/UpdateTrustConfig",
                request_serializer=gcc_trust_config.UpdateTrustConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_trust_config"]

    @property
    def delete_trust_config(
        self,
    ) -> Callable[[trust_config.DeleteTrustConfigRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete trust config method over gRPC.

        Deletes a single TrustConfig.

        Returns:
            Callable[[~.DeleteTrustConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_trust_config" not in self._stubs:
            self._stubs["delete_trust_config"] = self._logged_channel.unary_unary(
                "/google.cloud.certificatemanager.v1.CertificateManager/DeleteTrustConfig",
                request_serializer=trust_config.DeleteTrustConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_trust_config"]

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


__all__ = ("CertificateManagerGrpcTransport",)
