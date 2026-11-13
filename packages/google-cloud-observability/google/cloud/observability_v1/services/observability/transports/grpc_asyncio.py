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
from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.observability_v1.types import observability

from .base import DEFAULT_CLIENT_INFO, ObservabilityTransport
from .grpc import ObservabilityGrpcTransport

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
                    "serviceName": "google.cloud.observability.v1.Observability",
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
                    "serviceName": "google.cloud.observability.v1.Observability",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ObservabilityGrpcAsyncIOTransport(ObservabilityTransport):
    """gRPC AsyncIO backend transport for Observability.

    Service describing handlers for resources

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
        host: str = "observability.googleapis.com",
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
        host: str = "observability.googleapis.com",
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
                 The hostname to connect to (default: 'observability.googleapis.com').
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
    def get_scope(
        self,
    ) -> Callable[[observability.GetScopeRequest], Awaitable[observability.Scope]]:
        r"""Return a callable for the get scope method over gRPC.

        Gets details of a single Scope.

        Returns:
            Callable[[~.GetScopeRequest],
                    Awaitable[~.Scope]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_scope" not in self._stubs:
            self._stubs["get_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/GetScope",
                request_serializer=observability.GetScopeRequest.serialize,
                response_deserializer=observability.Scope.deserialize,
            )
        return self._stubs["get_scope"]

    @property
    def update_scope(
        self,
    ) -> Callable[[observability.UpdateScopeRequest], Awaitable[observability.Scope]]:
        r"""Return a callable for the update scope method over gRPC.

        Updates the parameters of a single Scope.

        Returns:
            Callable[[~.UpdateScopeRequest],
                    Awaitable[~.Scope]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_scope" not in self._stubs:
            self._stubs["update_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/UpdateScope",
                request_serializer=observability.UpdateScopeRequest.serialize,
                response_deserializer=observability.Scope.deserialize,
            )
        return self._stubs["update_scope"]

    @property
    def get_bucket(
        self,
    ) -> Callable[[observability.GetBucketRequest], Awaitable[observability.Bucket]]:
        r"""Return a callable for the get bucket method over gRPC.

        Get bucket resource.

        Returns:
            Callable[[~.GetBucketRequest],
                    Awaitable[~.Bucket]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_bucket" not in self._stubs:
            self._stubs["get_bucket"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/GetBucket",
                request_serializer=observability.GetBucketRequest.serialize,
                response_deserializer=observability.Bucket.deserialize,
            )
        return self._stubs["get_bucket"]

    @property
    def list_buckets(
        self,
    ) -> Callable[
        [observability.ListBucketsRequest], Awaitable[observability.ListBucketsResponse]
    ]:
        r"""Return a callable for the list buckets method over gRPC.

        List buckets of a project in a particular location.

        Returns:
            Callable[[~.ListBucketsRequest],
                    Awaitable[~.ListBucketsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_buckets" not in self._stubs:
            self._stubs["list_buckets"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/ListBuckets",
                request_serializer=observability.ListBucketsRequest.serialize,
                response_deserializer=observability.ListBucketsResponse.deserialize,
            )
        return self._stubs["list_buckets"]

    @property
    def create_bucket(
        self,
    ) -> Callable[
        [observability.CreateBucketRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create bucket method over gRPC.

        Create a new bucket.

        Returns:
            Callable[[~.CreateBucketRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_bucket" not in self._stubs:
            self._stubs["create_bucket"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/CreateBucket",
                request_serializer=observability.CreateBucketRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_bucket"]

    @property
    def update_bucket(
        self,
    ) -> Callable[
        [observability.UpdateBucketRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update bucket method over gRPC.

        Update a bucket.

        Returns:
            Callable[[~.UpdateBucketRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_bucket" not in self._stubs:
            self._stubs["update_bucket"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/UpdateBucket",
                request_serializer=observability.UpdateBucketRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_bucket"]

    @property
    def get_dataset(
        self,
    ) -> Callable[[observability.GetDatasetRequest], Awaitable[observability.Dataset]]:
        r"""Return a callable for the get dataset method over gRPC.

        Get a dataset.

        Returns:
            Callable[[~.GetDatasetRequest],
                    Awaitable[~.Dataset]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dataset" not in self._stubs:
            self._stubs["get_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/GetDataset",
                request_serializer=observability.GetDatasetRequest.serialize,
                response_deserializer=observability.Dataset.deserialize,
            )
        return self._stubs["get_dataset"]

    @property
    def list_datasets(
        self,
    ) -> Callable[
        [observability.ListDatasetsRequest],
        Awaitable[observability.ListDatasetsResponse],
    ]:
        r"""Return a callable for the list datasets method over gRPC.

        List datasets of a bucket.

        Returns:
            Callable[[~.ListDatasetsRequest],
                    Awaitable[~.ListDatasetsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_datasets" not in self._stubs:
            self._stubs["list_datasets"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/ListDatasets",
                request_serializer=observability.ListDatasetsRequest.serialize,
                response_deserializer=observability.ListDatasetsResponse.deserialize,
            )
        return self._stubs["list_datasets"]

    @property
    def get_view(
        self,
    ) -> Callable[[observability.GetViewRequest], Awaitable[observability.View]]:
        r"""Return a callable for the get view method over gRPC.

        Get a view.

        Returns:
            Callable[[~.GetViewRequest],
                    Awaitable[~.View]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_view" not in self._stubs:
            self._stubs["get_view"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/GetView",
                request_serializer=observability.GetViewRequest.serialize,
                response_deserializer=observability.View.deserialize,
            )
        return self._stubs["get_view"]

    @property
    def list_views(
        self,
    ) -> Callable[
        [observability.ListViewsRequest], Awaitable[observability.ListViewsResponse]
    ]:
        r"""Return a callable for the list views method over gRPC.

        List views of a dataset.

        Returns:
            Callable[[~.ListViewsRequest],
                    Awaitable[~.ListViewsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_views" not in self._stubs:
            self._stubs["list_views"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/ListViews",
                request_serializer=observability.ListViewsRequest.serialize,
                response_deserializer=observability.ListViewsResponse.deserialize,
            )
        return self._stubs["list_views"]

    @property
    def get_link(
        self,
    ) -> Callable[[observability.GetLinkRequest], Awaitable[observability.Link]]:
        r"""Return a callable for the get link method over gRPC.

        Get a link.

        Returns:
            Callable[[~.GetLinkRequest],
                    Awaitable[~.Link]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_link" not in self._stubs:
            self._stubs["get_link"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/GetLink",
                request_serializer=observability.GetLinkRequest.serialize,
                response_deserializer=observability.Link.deserialize,
            )
        return self._stubs["get_link"]

    @property
    def list_links(
        self,
    ) -> Callable[
        [observability.ListLinksRequest], Awaitable[observability.ListLinksResponse]
    ]:
        r"""Return a callable for the list links method over gRPC.

        List links of a dataset.

        Returns:
            Callable[[~.ListLinksRequest],
                    Awaitable[~.ListLinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_links" not in self._stubs:
            self._stubs["list_links"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/ListLinks",
                request_serializer=observability.ListLinksRequest.serialize,
                response_deserializer=observability.ListLinksResponse.deserialize,
            )
        return self._stubs["list_links"]

    @property
    def create_link(
        self,
    ) -> Callable[
        [observability.CreateLinkRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create link method over gRPC.

        Create a new link.

        Returns:
            Callable[[~.CreateLinkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_link" not in self._stubs:
            self._stubs["create_link"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/CreateLink",
                request_serializer=observability.CreateLinkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_link"]

    @property
    def update_link(
        self,
    ) -> Callable[
        [observability.UpdateLinkRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update link method over gRPC.

        Update a link.

        Returns:
            Callable[[~.UpdateLinkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_link" not in self._stubs:
            self._stubs["update_link"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/UpdateLink",
                request_serializer=observability.UpdateLinkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_link"]

    @property
    def delete_link(
        self,
    ) -> Callable[
        [observability.DeleteLinkRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete link method over gRPC.

        Delete a link.

        Returns:
            Callable[[~.DeleteLinkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_link" not in self._stubs:
            self._stubs["delete_link"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/DeleteLink",
                request_serializer=observability.DeleteLinkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_link"]

    @property
    def get_trace_scope(
        self,
    ) -> Callable[
        [observability.GetTraceScopeRequest], Awaitable[observability.TraceScope]
    ]:
        r"""Return a callable for the get trace scope method over gRPC.

        Get TraceScope resource.

        Returns:
            Callable[[~.GetTraceScopeRequest],
                    Awaitable[~.TraceScope]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_trace_scope" not in self._stubs:
            self._stubs["get_trace_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/GetTraceScope",
                request_serializer=observability.GetTraceScopeRequest.serialize,
                response_deserializer=observability.TraceScope.deserialize,
            )
        return self._stubs["get_trace_scope"]

    @property
    def list_trace_scopes(
        self,
    ) -> Callable[
        [observability.ListTraceScopesRequest],
        Awaitable[observability.ListTraceScopesResponse],
    ]:
        r"""Return a callable for the list trace scopes method over gRPC.

        List TraceScopes of a project in a particular
        location.

        Returns:
            Callable[[~.ListTraceScopesRequest],
                    Awaitable[~.ListTraceScopesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_trace_scopes" not in self._stubs:
            self._stubs["list_trace_scopes"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/ListTraceScopes",
                request_serializer=observability.ListTraceScopesRequest.serialize,
                response_deserializer=observability.ListTraceScopesResponse.deserialize,
            )
        return self._stubs["list_trace_scopes"]

    @property
    def create_trace_scope(
        self,
    ) -> Callable[
        [observability.CreateTraceScopeRequest], Awaitable[observability.TraceScope]
    ]:
        r"""Return a callable for the create trace scope method over gRPC.

        Create a new TraceScope.

        Returns:
            Callable[[~.CreateTraceScopeRequest],
                    Awaitable[~.TraceScope]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_trace_scope" not in self._stubs:
            self._stubs["create_trace_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/CreateTraceScope",
                request_serializer=observability.CreateTraceScopeRequest.serialize,
                response_deserializer=observability.TraceScope.deserialize,
            )
        return self._stubs["create_trace_scope"]

    @property
    def update_trace_scope(
        self,
    ) -> Callable[
        [observability.UpdateTraceScopeRequest], Awaitable[observability.TraceScope]
    ]:
        r"""Return a callable for the update trace scope method over gRPC.

        Update a TraceScope.

        Returns:
            Callable[[~.UpdateTraceScopeRequest],
                    Awaitable[~.TraceScope]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_trace_scope" not in self._stubs:
            self._stubs["update_trace_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/UpdateTraceScope",
                request_serializer=observability.UpdateTraceScopeRequest.serialize,
                response_deserializer=observability.TraceScope.deserialize,
            )
        return self._stubs["update_trace_scope"]

    @property
    def delete_trace_scope(
        self,
    ) -> Callable[[observability.DeleteTraceScopeRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete trace scope method over gRPC.

        Delete a TraceScope.

        Returns:
            Callable[[~.DeleteTraceScopeRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_trace_scope" not in self._stubs:
            self._stubs["delete_trace_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/DeleteTraceScope",
                request_serializer=observability.DeleteTraceScopeRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_trace_scope"]

    @property
    def get_settings(
        self,
    ) -> Callable[
        [observability.GetSettingsRequest], Awaitable[observability.Settings]
    ]:
        r"""Return a callable for the get settings method over gRPC.

        Get Settings

        Returns:
            Callable[[~.GetSettingsRequest],
                    Awaitable[~.Settings]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_settings" not in self._stubs:
            self._stubs["get_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/GetSettings",
                request_serializer=observability.GetSettingsRequest.serialize,
                response_deserializer=observability.Settings.deserialize,
            )
        return self._stubs["get_settings"]

    @property
    def update_settings(
        self,
    ) -> Callable[
        [observability.UpdateSettingsRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update settings method over gRPC.

        Update Settings

        Returns:
            Callable[[~.UpdateSettingsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_settings" not in self._stubs:
            self._stubs["update_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.observability.v1.Observability/UpdateSettings",
                request_serializer=observability.UpdateSettingsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_settings"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.get_scope: self._wrap_method(
                self.get_scope,
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
            self.update_scope: self._wrap_method(
                self.update_scope,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_bucket: self._wrap_method(
                self.get_bucket,
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
            self.list_buckets: self._wrap_method(
                self.list_buckets,
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
            self.create_bucket: self._wrap_method(
                self.create_bucket,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_bucket: self._wrap_method(
                self.update_bucket,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_dataset: self._wrap_method(
                self.get_dataset,
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
            self.list_datasets: self._wrap_method(
                self.list_datasets,
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
            self.get_view: self._wrap_method(
                self.get_view,
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
            self.list_views: self._wrap_method(
                self.list_views,
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
            self.get_link: self._wrap_method(
                self.get_link,
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
            self.list_links: self._wrap_method(
                self.list_links,
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
            self.create_link: self._wrap_method(
                self.create_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_link: self._wrap_method(
                self.update_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_link: self._wrap_method(
                self.delete_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_trace_scope: self._wrap_method(
                self.get_trace_scope,
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
            self.list_trace_scopes: self._wrap_method(
                self.list_trace_scopes,
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
            self.create_trace_scope: self._wrap_method(
                self.create_trace_scope,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_trace_scope: self._wrap_method(
                self.update_trace_scope,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_trace_scope: self._wrap_method(
                self.delete_trace_scope,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_settings: self._wrap_method(
                self.get_settings,
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
            self.update_settings: self._wrap_method(
                self.update_settings,
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


__all__ = ("ObservabilityGrpcAsyncIOTransport",)
