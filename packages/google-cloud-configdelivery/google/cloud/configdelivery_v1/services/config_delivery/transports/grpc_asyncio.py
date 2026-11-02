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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.configdelivery_v1.types import config_delivery

from .base import DEFAULT_CLIENT_INFO, ConfigDeliveryTransport
from .grpc import ConfigDeliveryGrpcTransport

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
                    "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
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
                    "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ConfigDeliveryGrpcAsyncIOTransport(ConfigDeliveryTransport):
    """gRPC AsyncIO backend transport for ConfigDelivery.

    ConfigDelivery service manages the deployment of kubernetes
    configuration to a fleet of kubernetes clusters.

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
        host: str = "configdelivery.googleapis.com",
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
        host: str = "configdelivery.googleapis.com",
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
                 The hostname to connect to (default: 'configdelivery.googleapis.com').
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
    def list_resource_bundles(
        self,
    ) -> Callable[
        [config_delivery.ListResourceBundlesRequest],
        Awaitable[config_delivery.ListResourceBundlesResponse],
    ]:
        r"""Return a callable for the list resource bundles method over gRPC.

        Lists ResourceBundles in a given project and
        location.

        Returns:
            Callable[[~.ListResourceBundlesRequest],
                    Awaitable[~.ListResourceBundlesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_resource_bundles" not in self._stubs:
            self._stubs["list_resource_bundles"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/ListResourceBundles",
                request_serializer=config_delivery.ListResourceBundlesRequest.serialize,
                response_deserializer=config_delivery.ListResourceBundlesResponse.deserialize,
            )
        return self._stubs["list_resource_bundles"]

    @property
    def get_resource_bundle(
        self,
    ) -> Callable[
        [config_delivery.GetResourceBundleRequest],
        Awaitable[config_delivery.ResourceBundle],
    ]:
        r"""Return a callable for the get resource bundle method over gRPC.

        Gets details of a single ResourceBundle.

        Returns:
            Callable[[~.GetResourceBundleRequest],
                    Awaitable[~.ResourceBundle]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_resource_bundle" not in self._stubs:
            self._stubs["get_resource_bundle"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/GetResourceBundle",
                request_serializer=config_delivery.GetResourceBundleRequest.serialize,
                response_deserializer=config_delivery.ResourceBundle.deserialize,
            )
        return self._stubs["get_resource_bundle"]

    @property
    def create_resource_bundle(
        self,
    ) -> Callable[
        [config_delivery.CreateResourceBundleRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create resource bundle method over gRPC.

        Creates a new ResourceBundle in a given project and
        location.

        Returns:
            Callable[[~.CreateResourceBundleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_resource_bundle" not in self._stubs:
            self._stubs["create_resource_bundle"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/CreateResourceBundle",
                request_serializer=config_delivery.CreateResourceBundleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_resource_bundle"]

    @property
    def update_resource_bundle(
        self,
    ) -> Callable[
        [config_delivery.UpdateResourceBundleRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update resource bundle method over gRPC.

        Updates the parameters of a single ResourceBundle.

        Returns:
            Callable[[~.UpdateResourceBundleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_resource_bundle" not in self._stubs:
            self._stubs["update_resource_bundle"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/UpdateResourceBundle",
                request_serializer=config_delivery.UpdateResourceBundleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_resource_bundle"]

    @property
    def delete_resource_bundle(
        self,
    ) -> Callable[
        [config_delivery.DeleteResourceBundleRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete resource bundle method over gRPC.

        Deletes a single ResourceBundle.

        Returns:
            Callable[[~.DeleteResourceBundleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_resource_bundle" not in self._stubs:
            self._stubs["delete_resource_bundle"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/DeleteResourceBundle",
                request_serializer=config_delivery.DeleteResourceBundleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_resource_bundle"]

    @property
    def list_fleet_packages(
        self,
    ) -> Callable[
        [config_delivery.ListFleetPackagesRequest],
        Awaitable[config_delivery.ListFleetPackagesResponse],
    ]:
        r"""Return a callable for the list fleet packages method over gRPC.

        Lists FleetPackages in a given project and location.

        Returns:
            Callable[[~.ListFleetPackagesRequest],
                    Awaitable[~.ListFleetPackagesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_fleet_packages" not in self._stubs:
            self._stubs["list_fleet_packages"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/ListFleetPackages",
                request_serializer=config_delivery.ListFleetPackagesRequest.serialize,
                response_deserializer=config_delivery.ListFleetPackagesResponse.deserialize,
            )
        return self._stubs["list_fleet_packages"]

    @property
    def get_fleet_package(
        self,
    ) -> Callable[
        [config_delivery.GetFleetPackageRequest],
        Awaitable[config_delivery.FleetPackage],
    ]:
        r"""Return a callable for the get fleet package method over gRPC.

        Gets details of a single FleetPackage.

        Returns:
            Callable[[~.GetFleetPackageRequest],
                    Awaitable[~.FleetPackage]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_fleet_package" not in self._stubs:
            self._stubs["get_fleet_package"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/GetFleetPackage",
                request_serializer=config_delivery.GetFleetPackageRequest.serialize,
                response_deserializer=config_delivery.FleetPackage.deserialize,
            )
        return self._stubs["get_fleet_package"]

    @property
    def create_fleet_package(
        self,
    ) -> Callable[
        [config_delivery.CreateFleetPackageRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create fleet package method over gRPC.

        Creates a new FleetPackage in a given project and
        location.

        Returns:
            Callable[[~.CreateFleetPackageRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_fleet_package" not in self._stubs:
            self._stubs["create_fleet_package"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/CreateFleetPackage",
                request_serializer=config_delivery.CreateFleetPackageRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_fleet_package"]

    @property
    def update_fleet_package(
        self,
    ) -> Callable[
        [config_delivery.UpdateFleetPackageRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update fleet package method over gRPC.

        Updates the parameters of a single FleetPackage.

        Returns:
            Callable[[~.UpdateFleetPackageRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_fleet_package" not in self._stubs:
            self._stubs["update_fleet_package"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/UpdateFleetPackage",
                request_serializer=config_delivery.UpdateFleetPackageRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_fleet_package"]

    @property
    def delete_fleet_package(
        self,
    ) -> Callable[
        [config_delivery.DeleteFleetPackageRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete fleet package method over gRPC.

        Deletes a single FleetPackage.

        Returns:
            Callable[[~.DeleteFleetPackageRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_fleet_package" not in self._stubs:
            self._stubs["delete_fleet_package"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/DeleteFleetPackage",
                request_serializer=config_delivery.DeleteFleetPackageRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_fleet_package"]

    @property
    def list_releases(
        self,
    ) -> Callable[
        [config_delivery.ListReleasesRequest],
        Awaitable[config_delivery.ListReleasesResponse],
    ]:
        r"""Return a callable for the list releases method over gRPC.

        Lists Releases in a given project and location.

        Returns:
            Callable[[~.ListReleasesRequest],
                    Awaitable[~.ListReleasesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_releases" not in self._stubs:
            self._stubs["list_releases"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/ListReleases",
                request_serializer=config_delivery.ListReleasesRequest.serialize,
                response_deserializer=config_delivery.ListReleasesResponse.deserialize,
            )
        return self._stubs["list_releases"]

    @property
    def get_release(
        self,
    ) -> Callable[
        [config_delivery.GetReleaseRequest], Awaitable[config_delivery.Release]
    ]:
        r"""Return a callable for the get release method over gRPC.

        Gets details of a single Release.

        Returns:
            Callable[[~.GetReleaseRequest],
                    Awaitable[~.Release]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_release" not in self._stubs:
            self._stubs["get_release"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/GetRelease",
                request_serializer=config_delivery.GetReleaseRequest.serialize,
                response_deserializer=config_delivery.Release.deserialize,
            )
        return self._stubs["get_release"]

    @property
    def create_release(
        self,
    ) -> Callable[
        [config_delivery.CreateReleaseRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create release method over gRPC.

        Creates a new Release in a given project, location
        and resource bundle.

        Returns:
            Callable[[~.CreateReleaseRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_release" not in self._stubs:
            self._stubs["create_release"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/CreateRelease",
                request_serializer=config_delivery.CreateReleaseRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_release"]

    @property
    def update_release(
        self,
    ) -> Callable[
        [config_delivery.UpdateReleaseRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update release method over gRPC.

        Updates the parameters of a single Release.

        Returns:
            Callable[[~.UpdateReleaseRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_release" not in self._stubs:
            self._stubs["update_release"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/UpdateRelease",
                request_serializer=config_delivery.UpdateReleaseRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_release"]

    @property
    def delete_release(
        self,
    ) -> Callable[
        [config_delivery.DeleteReleaseRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete release method over gRPC.

        Deletes a single Release.

        Returns:
            Callable[[~.DeleteReleaseRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_release" not in self._stubs:
            self._stubs["delete_release"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/DeleteRelease",
                request_serializer=config_delivery.DeleteReleaseRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_release"]

    @property
    def list_variants(
        self,
    ) -> Callable[
        [config_delivery.ListVariantsRequest],
        Awaitable[config_delivery.ListVariantsResponse],
    ]:
        r"""Return a callable for the list variants method over gRPC.

        Lists Variants in a given project and location.

        Returns:
            Callable[[~.ListVariantsRequest],
                    Awaitable[~.ListVariantsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_variants" not in self._stubs:
            self._stubs["list_variants"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/ListVariants",
                request_serializer=config_delivery.ListVariantsRequest.serialize,
                response_deserializer=config_delivery.ListVariantsResponse.deserialize,
            )
        return self._stubs["list_variants"]

    @property
    def get_variant(
        self,
    ) -> Callable[
        [config_delivery.GetVariantRequest], Awaitable[config_delivery.Variant]
    ]:
        r"""Return a callable for the get variant method over gRPC.

        Gets details of a single Variant.

        Returns:
            Callable[[~.GetVariantRequest],
                    Awaitable[~.Variant]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_variant" not in self._stubs:
            self._stubs["get_variant"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/GetVariant",
                request_serializer=config_delivery.GetVariantRequest.serialize,
                response_deserializer=config_delivery.Variant.deserialize,
            )
        return self._stubs["get_variant"]

    @property
    def create_variant(
        self,
    ) -> Callable[
        [config_delivery.CreateVariantRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create variant method over gRPC.

        Creates a new Variant in a given project, location,
        resource bundle, and release.

        Returns:
            Callable[[~.CreateVariantRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_variant" not in self._stubs:
            self._stubs["create_variant"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/CreateVariant",
                request_serializer=config_delivery.CreateVariantRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_variant"]

    @property
    def update_variant(
        self,
    ) -> Callable[
        [config_delivery.UpdateVariantRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update variant method over gRPC.

        Updates the parameters of a single Variant.

        Returns:
            Callable[[~.UpdateVariantRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_variant" not in self._stubs:
            self._stubs["update_variant"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/UpdateVariant",
                request_serializer=config_delivery.UpdateVariantRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_variant"]

    @property
    def delete_variant(
        self,
    ) -> Callable[
        [config_delivery.DeleteVariantRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete variant method over gRPC.

        Deletes a single Variant.

        Returns:
            Callable[[~.DeleteVariantRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_variant" not in self._stubs:
            self._stubs["delete_variant"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/DeleteVariant",
                request_serializer=config_delivery.DeleteVariantRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_variant"]

    @property
    def list_rollouts(
        self,
    ) -> Callable[
        [config_delivery.ListRolloutsRequest],
        Awaitable[config_delivery.ListRolloutsResponse],
    ]:
        r"""Return a callable for the list rollouts method over gRPC.

        Lists Rollouts in a given project, location, and
        Fleet Package.

        Returns:
            Callable[[~.ListRolloutsRequest],
                    Awaitable[~.ListRolloutsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_rollouts" not in self._stubs:
            self._stubs["list_rollouts"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/ListRollouts",
                request_serializer=config_delivery.ListRolloutsRequest.serialize,
                response_deserializer=config_delivery.ListRolloutsResponse.deserialize,
            )
        return self._stubs["list_rollouts"]

    @property
    def get_rollout(
        self,
    ) -> Callable[
        [config_delivery.GetRolloutRequest], Awaitable[config_delivery.Rollout]
    ]:
        r"""Return a callable for the get rollout method over gRPC.

        Gets details of a single Rollout.

        Returns:
            Callable[[~.GetRolloutRequest],
                    Awaitable[~.Rollout]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_rollout" not in self._stubs:
            self._stubs["get_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/GetRollout",
                request_serializer=config_delivery.GetRolloutRequest.serialize,
                response_deserializer=config_delivery.Rollout.deserialize,
            )
        return self._stubs["get_rollout"]

    @property
    def suspend_rollout(
        self,
    ) -> Callable[
        [config_delivery.SuspendRolloutRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the suspend rollout method over gRPC.

        Suspend a Rollout.

        Returns:
            Callable[[~.SuspendRolloutRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "suspend_rollout" not in self._stubs:
            self._stubs["suspend_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/SuspendRollout",
                request_serializer=config_delivery.SuspendRolloutRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["suspend_rollout"]

    @property
    def resume_rollout(
        self,
    ) -> Callable[
        [config_delivery.ResumeRolloutRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the resume rollout method over gRPC.

        Resume a Rollout.

        Returns:
            Callable[[~.ResumeRolloutRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "resume_rollout" not in self._stubs:
            self._stubs["resume_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/ResumeRollout",
                request_serializer=config_delivery.ResumeRolloutRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["resume_rollout"]

    @property
    def abort_rollout(
        self,
    ) -> Callable[
        [config_delivery.AbortRolloutRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the abort rollout method over gRPC.

        Abort a Rollout.

        Returns:
            Callable[[~.AbortRolloutRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "abort_rollout" not in self._stubs:
            self._stubs["abort_rollout"] = self._logged_channel.unary_unary(
                "/google.cloud.configdelivery.v1.ConfigDelivery/AbortRollout",
                request_serializer=config_delivery.AbortRolloutRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["abort_rollout"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_resource_bundles: self._wrap_method(
                self.list_resource_bundles,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_resource_bundle: self._wrap_method(
                self.get_resource_bundle,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_resource_bundle: self._wrap_method(
                self.create_resource_bundle,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_resource_bundle: self._wrap_method(
                self.update_resource_bundle,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_resource_bundle: self._wrap_method(
                self.delete_resource_bundle,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_fleet_packages: self._wrap_method(
                self.list_fleet_packages,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_fleet_package: self._wrap_method(
                self.get_fleet_package,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_fleet_package: self._wrap_method(
                self.create_fleet_package,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_fleet_package: self._wrap_method(
                self.update_fleet_package,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_fleet_package: self._wrap_method(
                self.delete_fleet_package,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_releases: self._wrap_method(
                self.list_releases,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_release: self._wrap_method(
                self.get_release,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_release: self._wrap_method(
                self.create_release,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_release: self._wrap_method(
                self.update_release,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_release: self._wrap_method(
                self.delete_release,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_variants: self._wrap_method(
                self.list_variants,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_variant: self._wrap_method(
                self.get_variant,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_variant: self._wrap_method(
                self.create_variant,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_variant: self._wrap_method(
                self.update_variant,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_variant: self._wrap_method(
                self.delete_variant,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_rollouts: self._wrap_method(
                self.list_rollouts,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_rollout: self._wrap_method(
                self.get_rollout,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.suspend_rollout: self._wrap_method(
                self.suspend_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.resume_rollout: self._wrap_method(
                self.resume_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.abort_rollout: self._wrap_method(
                self.abort_rollout,
                default_timeout=60.0,
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


__all__ = ("ConfigDeliveryGrpcAsyncIOTransport",)
