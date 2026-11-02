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

from google.cloud.video.stitcher_v1.types import (
    ad_tag_details,
    cdn_keys,
    live_configs,
    sessions,
    slates,
    stitch_details,
    video_stitcher_service,
    vod_configs,
)

from .base import DEFAULT_CLIENT_INFO, VideoStitcherServiceTransport

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
                    "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
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
                    "serviceName": "google.cloud.video.stitcher.v1.VideoStitcherService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class VideoStitcherServiceGrpcTransport(VideoStitcherServiceTransport):
    """gRPC backend transport for VideoStitcherService.

    Video-On-Demand content stitching API allows you to insert
    ads into (VoD) video on demand files. You will be able to render
    custom scrubber bars with highlighted ads, enforce ad policies,
    allow seamless playback and tracking on native players and
    monetize content with any standard VMAP compliant ad server.

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
        host: str = "videostitcher.googleapis.com",
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
                 The hostname to connect to (default: 'videostitcher.googleapis.com').
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
        host: str = "videostitcher.googleapis.com",
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
    def create_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateCdnKeyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create cdn key method over gRPC.

        Creates a new CDN key.

        Returns:
            Callable[[~.CreateCdnKeyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_cdn_key" not in self._stubs:
            self._stubs["create_cdn_key"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/CreateCdnKey",
                request_serializer=video_stitcher_service.CreateCdnKeyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_cdn_key"]

    @property
    def list_cdn_keys(
        self,
    ) -> Callable[
        [video_stitcher_service.ListCdnKeysRequest],
        video_stitcher_service.ListCdnKeysResponse,
    ]:
        r"""Return a callable for the list cdn keys method over gRPC.

        Lists all CDN keys in the specified project and
        location.

        Returns:
            Callable[[~.ListCdnKeysRequest],
                    ~.ListCdnKeysResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_cdn_keys" not in self._stubs:
            self._stubs["list_cdn_keys"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/ListCdnKeys",
                request_serializer=video_stitcher_service.ListCdnKeysRequest.serialize,
                response_deserializer=video_stitcher_service.ListCdnKeysResponse.deserialize,
            )
        return self._stubs["list_cdn_keys"]

    @property
    def get_cdn_key(
        self,
    ) -> Callable[[video_stitcher_service.GetCdnKeyRequest], cdn_keys.CdnKey]:
        r"""Return a callable for the get cdn key method over gRPC.

        Returns the specified CDN key.

        Returns:
            Callable[[~.GetCdnKeyRequest],
                    ~.CdnKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cdn_key" not in self._stubs:
            self._stubs["get_cdn_key"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetCdnKey",
                request_serializer=video_stitcher_service.GetCdnKeyRequest.serialize,
                response_deserializer=cdn_keys.CdnKey.deserialize,
            )
        return self._stubs["get_cdn_key"]

    @property
    def delete_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteCdnKeyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete cdn key method over gRPC.

        Deletes the specified CDN key.

        Returns:
            Callable[[~.DeleteCdnKeyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_cdn_key" not in self._stubs:
            self._stubs["delete_cdn_key"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/DeleteCdnKey",
                request_serializer=video_stitcher_service.DeleteCdnKeyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_cdn_key"]

    @property
    def update_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateCdnKeyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update cdn key method over gRPC.

        Updates the specified CDN key. Only update fields
        specified in the call method body.

        Returns:
            Callable[[~.UpdateCdnKeyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_cdn_key" not in self._stubs:
            self._stubs["update_cdn_key"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/UpdateCdnKey",
                request_serializer=video_stitcher_service.UpdateCdnKeyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_cdn_key"]

    @property
    def create_vod_session(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateVodSessionRequest], sessions.VodSession
    ]:
        r"""Return a callable for the create vod session method over gRPC.

        Creates a client side playback VOD session and
        returns the full tracking and playback metadata of the
        session.

        Returns:
            Callable[[~.CreateVodSessionRequest],
                    ~.VodSession]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_vod_session" not in self._stubs:
            self._stubs["create_vod_session"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/CreateVodSession",
                request_serializer=video_stitcher_service.CreateVodSessionRequest.serialize,
                response_deserializer=sessions.VodSession.deserialize,
            )
        return self._stubs["create_vod_session"]

    @property
    def get_vod_session(
        self,
    ) -> Callable[[video_stitcher_service.GetVodSessionRequest], sessions.VodSession]:
        r"""Return a callable for the get vod session method over gRPC.

        Returns the full tracking, playback metadata, and
        relevant ad-ops logs for the specified VOD session.

        Returns:
            Callable[[~.GetVodSessionRequest],
                    ~.VodSession]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_vod_session" not in self._stubs:
            self._stubs["get_vod_session"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetVodSession",
                request_serializer=video_stitcher_service.GetVodSessionRequest.serialize,
                response_deserializer=sessions.VodSession.deserialize,
            )
        return self._stubs["get_vod_session"]

    @property
    def list_vod_stitch_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodStitchDetailsRequest],
        video_stitcher_service.ListVodStitchDetailsResponse,
    ]:
        r"""Return a callable for the list vod stitch details method over gRPC.

        Returns a list of detailed stitching information of
        the specified VOD session.

        Returns:
            Callable[[~.ListVodStitchDetailsRequest],
                    ~.ListVodStitchDetailsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_vod_stitch_details" not in self._stubs:
            self._stubs["list_vod_stitch_details"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/ListVodStitchDetails",
                request_serializer=video_stitcher_service.ListVodStitchDetailsRequest.serialize,
                response_deserializer=video_stitcher_service.ListVodStitchDetailsResponse.deserialize,
            )
        return self._stubs["list_vod_stitch_details"]

    @property
    def get_vod_stitch_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodStitchDetailRequest],
        stitch_details.VodStitchDetail,
    ]:
        r"""Return a callable for the get vod stitch detail method over gRPC.

        Returns the specified stitching information for the
        specified VOD session.

        Returns:
            Callable[[~.GetVodStitchDetailRequest],
                    ~.VodStitchDetail]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_vod_stitch_detail" not in self._stubs:
            self._stubs["get_vod_stitch_detail"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetVodStitchDetail",
                request_serializer=video_stitcher_service.GetVodStitchDetailRequest.serialize,
                response_deserializer=stitch_details.VodStitchDetail.deserialize,
            )
        return self._stubs["get_vod_stitch_detail"]

    @property
    def list_vod_ad_tag_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodAdTagDetailsRequest],
        video_stitcher_service.ListVodAdTagDetailsResponse,
    ]:
        r"""Return a callable for the list vod ad tag details method over gRPC.

        Return the list of ad tag details for the specified
        VOD session.

        Returns:
            Callable[[~.ListVodAdTagDetailsRequest],
                    ~.ListVodAdTagDetailsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_vod_ad_tag_details" not in self._stubs:
            self._stubs["list_vod_ad_tag_details"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/ListVodAdTagDetails",
                request_serializer=video_stitcher_service.ListVodAdTagDetailsRequest.serialize,
                response_deserializer=video_stitcher_service.ListVodAdTagDetailsResponse.deserialize,
            )
        return self._stubs["list_vod_ad_tag_details"]

    @property
    def get_vod_ad_tag_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodAdTagDetailRequest], ad_tag_details.VodAdTagDetail
    ]:
        r"""Return a callable for the get vod ad tag detail method over gRPC.

        Returns the specified ad tag detail for the specified
        VOD session.

        Returns:
            Callable[[~.GetVodAdTagDetailRequest],
                    ~.VodAdTagDetail]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_vod_ad_tag_detail" not in self._stubs:
            self._stubs["get_vod_ad_tag_detail"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetVodAdTagDetail",
                request_serializer=video_stitcher_service.GetVodAdTagDetailRequest.serialize,
                response_deserializer=ad_tag_details.VodAdTagDetail.deserialize,
            )
        return self._stubs["get_vod_ad_tag_detail"]

    @property
    def list_live_ad_tag_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListLiveAdTagDetailsRequest],
        video_stitcher_service.ListLiveAdTagDetailsResponse,
    ]:
        r"""Return a callable for the list live ad tag details method over gRPC.

        Return the list of ad tag details for the specified
        live session.

        Returns:
            Callable[[~.ListLiveAdTagDetailsRequest],
                    ~.ListLiveAdTagDetailsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_live_ad_tag_details" not in self._stubs:
            self._stubs["list_live_ad_tag_details"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/ListLiveAdTagDetails",
                request_serializer=video_stitcher_service.ListLiveAdTagDetailsRequest.serialize,
                response_deserializer=video_stitcher_service.ListLiveAdTagDetailsResponse.deserialize,
            )
        return self._stubs["list_live_ad_tag_details"]

    @property
    def get_live_ad_tag_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveAdTagDetailRequest],
        ad_tag_details.LiveAdTagDetail,
    ]:
        r"""Return a callable for the get live ad tag detail method over gRPC.

        Returns the specified ad tag detail for the specified
        live session.

        Returns:
            Callable[[~.GetLiveAdTagDetailRequest],
                    ~.LiveAdTagDetail]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_live_ad_tag_detail" not in self._stubs:
            self._stubs["get_live_ad_tag_detail"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetLiveAdTagDetail",
                request_serializer=video_stitcher_service.GetLiveAdTagDetailRequest.serialize,
                response_deserializer=ad_tag_details.LiveAdTagDetail.deserialize,
            )
        return self._stubs["get_live_ad_tag_detail"]

    @property
    def create_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateSlateRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create slate method over gRPC.

        Creates a slate.

        Returns:
            Callable[[~.CreateSlateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_slate" not in self._stubs:
            self._stubs["create_slate"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/CreateSlate",
                request_serializer=video_stitcher_service.CreateSlateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_slate"]

    @property
    def list_slates(
        self,
    ) -> Callable[
        [video_stitcher_service.ListSlatesRequest],
        video_stitcher_service.ListSlatesResponse,
    ]:
        r"""Return a callable for the list slates method over gRPC.

        Lists all slates in the specified project and
        location.

        Returns:
            Callable[[~.ListSlatesRequest],
                    ~.ListSlatesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_slates" not in self._stubs:
            self._stubs["list_slates"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/ListSlates",
                request_serializer=video_stitcher_service.ListSlatesRequest.serialize,
                response_deserializer=video_stitcher_service.ListSlatesResponse.deserialize,
            )
        return self._stubs["list_slates"]

    @property
    def get_slate(
        self,
    ) -> Callable[[video_stitcher_service.GetSlateRequest], slates.Slate]:
        r"""Return a callable for the get slate method over gRPC.

        Returns the specified slate.

        Returns:
            Callable[[~.GetSlateRequest],
                    ~.Slate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_slate" not in self._stubs:
            self._stubs["get_slate"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetSlate",
                request_serializer=video_stitcher_service.GetSlateRequest.serialize,
                response_deserializer=slates.Slate.deserialize,
            )
        return self._stubs["get_slate"]

    @property
    def update_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateSlateRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update slate method over gRPC.

        Updates the specified slate.

        Returns:
            Callable[[~.UpdateSlateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_slate" not in self._stubs:
            self._stubs["update_slate"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/UpdateSlate",
                request_serializer=video_stitcher_service.UpdateSlateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_slate"]

    @property
    def delete_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteSlateRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete slate method over gRPC.

        Deletes the specified slate.

        Returns:
            Callable[[~.DeleteSlateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_slate" not in self._stubs:
            self._stubs["delete_slate"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/DeleteSlate",
                request_serializer=video_stitcher_service.DeleteSlateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_slate"]

    @property
    def create_live_session(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateLiveSessionRequest], sessions.LiveSession
    ]:
        r"""Return a callable for the create live session method over gRPC.

        Creates a new live session.

        Returns:
            Callable[[~.CreateLiveSessionRequest],
                    ~.LiveSession]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_live_session" not in self._stubs:
            self._stubs["create_live_session"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/CreateLiveSession",
                request_serializer=video_stitcher_service.CreateLiveSessionRequest.serialize,
                response_deserializer=sessions.LiveSession.deserialize,
            )
        return self._stubs["create_live_session"]

    @property
    def get_live_session(
        self,
    ) -> Callable[[video_stitcher_service.GetLiveSessionRequest], sessions.LiveSession]:
        r"""Return a callable for the get live session method over gRPC.

        Returns the details for the specified live session.

        Returns:
            Callable[[~.GetLiveSessionRequest],
                    ~.LiveSession]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_live_session" not in self._stubs:
            self._stubs["get_live_session"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetLiveSession",
                request_serializer=video_stitcher_service.GetLiveSessionRequest.serialize,
                response_deserializer=sessions.LiveSession.deserialize,
            )
        return self._stubs["get_live_session"]

    @property
    def create_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateLiveConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create live config method over gRPC.

        Registers the live config with the provided unique ID
        in the specified region.

        Returns:
            Callable[[~.CreateLiveConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_live_config" not in self._stubs:
            self._stubs["create_live_config"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/CreateLiveConfig",
                request_serializer=video_stitcher_service.CreateLiveConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_live_config"]

    @property
    def list_live_configs(
        self,
    ) -> Callable[
        [video_stitcher_service.ListLiveConfigsRequest],
        video_stitcher_service.ListLiveConfigsResponse,
    ]:
        r"""Return a callable for the list live configs method over gRPC.

        Lists all live configs managed by the Video Stitcher
        that belong to the specified project and region.

        Returns:
            Callable[[~.ListLiveConfigsRequest],
                    ~.ListLiveConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_live_configs" not in self._stubs:
            self._stubs["list_live_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/ListLiveConfigs",
                request_serializer=video_stitcher_service.ListLiveConfigsRequest.serialize,
                response_deserializer=video_stitcher_service.ListLiveConfigsResponse.deserialize,
            )
        return self._stubs["list_live_configs"]

    @property
    def get_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveConfigRequest], live_configs.LiveConfig
    ]:
        r"""Return a callable for the get live config method over gRPC.

        Returns the specified live config managed by the
        Video Stitcher service.

        Returns:
            Callable[[~.GetLiveConfigRequest],
                    ~.LiveConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_live_config" not in self._stubs:
            self._stubs["get_live_config"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetLiveConfig",
                request_serializer=video_stitcher_service.GetLiveConfigRequest.serialize,
                response_deserializer=live_configs.LiveConfig.deserialize,
            )
        return self._stubs["get_live_config"]

    @property
    def delete_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteLiveConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete live config method over gRPC.

        Deletes the specified live config.

        Returns:
            Callable[[~.DeleteLiveConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_live_config" not in self._stubs:
            self._stubs["delete_live_config"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/DeleteLiveConfig",
                request_serializer=video_stitcher_service.DeleteLiveConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_live_config"]

    @property
    def update_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateLiveConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update live config method over gRPC.

        Updates the specified LiveConfig. Only update fields
        specified in the call method body.

        Returns:
            Callable[[~.UpdateLiveConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_live_config" not in self._stubs:
            self._stubs["update_live_config"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/UpdateLiveConfig",
                request_serializer=video_stitcher_service.UpdateLiveConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_live_config"]

    @property
    def create_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateVodConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create vod config method over gRPC.

        Registers the VOD config with the provided unique ID
        in the specified region.

        Returns:
            Callable[[~.CreateVodConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_vod_config" not in self._stubs:
            self._stubs["create_vod_config"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/CreateVodConfig",
                request_serializer=video_stitcher_service.CreateVodConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_vod_config"]

    @property
    def list_vod_configs(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodConfigsRequest],
        video_stitcher_service.ListVodConfigsResponse,
    ]:
        r"""Return a callable for the list vod configs method over gRPC.

        Lists all VOD configs managed by the Video Stitcher
        API that belong to the specified project and region.

        Returns:
            Callable[[~.ListVodConfigsRequest],
                    ~.ListVodConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_vod_configs" not in self._stubs:
            self._stubs["list_vod_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/ListVodConfigs",
                request_serializer=video_stitcher_service.ListVodConfigsRequest.serialize,
                response_deserializer=video_stitcher_service.ListVodConfigsResponse.deserialize,
            )
        return self._stubs["list_vod_configs"]

    @property
    def get_vod_config(
        self,
    ) -> Callable[[video_stitcher_service.GetVodConfigRequest], vod_configs.VodConfig]:
        r"""Return a callable for the get vod config method over gRPC.

        Returns the specified VOD config managed by the Video
        Stitcher API service.

        Returns:
            Callable[[~.GetVodConfigRequest],
                    ~.VodConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_vod_config" not in self._stubs:
            self._stubs["get_vod_config"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/GetVodConfig",
                request_serializer=video_stitcher_service.GetVodConfigRequest.serialize,
                response_deserializer=vod_configs.VodConfig.deserialize,
            )
        return self._stubs["get_vod_config"]

    @property
    def delete_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteVodConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete vod config method over gRPC.

        Deletes the specified VOD config.

        Returns:
            Callable[[~.DeleteVodConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_vod_config" not in self._stubs:
            self._stubs["delete_vod_config"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/DeleteVodConfig",
                request_serializer=video_stitcher_service.DeleteVodConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_vod_config"]

    @property
    def update_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateVodConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update vod config method over gRPC.

        Updates the specified VOD config. Only update fields
        specified in the call method body.

        Returns:
            Callable[[~.UpdateVodConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_vod_config" not in self._stubs:
            self._stubs["update_vod_config"] = self._logged_channel.unary_unary(
                "/google.cloud.video.stitcher.v1.VideoStitcherService/UpdateVodConfig",
                request_serializer=video_stitcher_service.UpdateVodConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_vod_config"]

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
    def kind(self) -> str:
        return "grpc"


__all__ = ("VideoStitcherServiceGrpcTransport",)
