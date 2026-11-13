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
from google.protobuf.json_format import MessageToJson

from google.cloud.dlp_v2.types import dlp

from .base import DEFAULT_CLIENT_INFO, DlpServiceTransport

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
                    "serviceName": "google.privacy.dlp.v2.DlpService",
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
                    "serviceName": "google.privacy.dlp.v2.DlpService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DlpServiceGrpcTransport(DlpServiceTransport):
    """gRPC backend transport for DlpService.

    Sensitive Data Protection provides access to a powerful
    sensitive data inspection, classification, and de-identification
    platform that works on text, images, and Google Cloud storage
    repositories. To learn more about concepts and find how-to
    guides see
    https://docs.cloud.google.com/sensitive-data-protection/docs/.

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
        host: str = "dlp.googleapis.com",
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
                 The hostname to connect to (default: 'dlp.googleapis.com').
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
        host: str = "dlp.googleapis.com",
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
    def inspect_content(
        self,
    ) -> Callable[[dlp.InspectContentRequest], dlp.InspectContentResponse]:
        r"""Return a callable for the inspect content method over gRPC.

        Finds potentially sensitive info in content.
        This method has limits on input size, processing time,
        and output size.

        When no InfoTypes or CustomInfoTypes are specified in
        this request, the system will automatically choose what
        detectors to run. By default this may be all types, but
        may change over time as detectors are updated.

        For how to guides, see
        https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images
        and
        https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text,

        Returns:
            Callable[[~.InspectContentRequest],
                    ~.InspectContentResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "inspect_content" not in self._stubs:
            self._stubs["inspect_content"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/InspectContent",
                request_serializer=dlp.InspectContentRequest.serialize,
                response_deserializer=dlp.InspectContentResponse.deserialize,
            )
        return self._stubs["inspect_content"]

    @property
    def redact_image(
        self,
    ) -> Callable[[dlp.RedactImageRequest], dlp.RedactImageResponse]:
        r"""Return a callable for the redact image method over gRPC.

        Redacts potentially sensitive info from an image.
        This method has limits on input size, processing time,
        and output size. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images
        to learn more.

        When no InfoTypes or CustomInfoTypes are specified in
        this request, the system will automatically choose what
        detectors to run. By default this may be all types, but
        may change over time as detectors are updated.

        Only the first frame of each multiframe image is
        redacted. Metadata and other frames are omitted in the
        response.

        Returns:
            Callable[[~.RedactImageRequest],
                    ~.RedactImageResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "redact_image" not in self._stubs:
            self._stubs["redact_image"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/RedactImage",
                request_serializer=dlp.RedactImageRequest.serialize,
                response_deserializer=dlp.RedactImageResponse.deserialize,
            )
        return self._stubs["redact_image"]

    @property
    def deidentify_content(
        self,
    ) -> Callable[[dlp.DeidentifyContentRequest], dlp.DeidentifyContentResponse]:
        r"""Return a callable for the deidentify content method over gRPC.

        De-identifies potentially sensitive info from a
        ContentItem. This method has limits on input size and
        output size. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data
        to learn more.

        When no InfoTypes or CustomInfoTypes are specified in
        this request, the system will automatically choose what
        detectors to run. By default this may be all types, but
        may change over time as detectors are updated.

        Returns:
            Callable[[~.DeidentifyContentRequest],
                    ~.DeidentifyContentResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deidentify_content" not in self._stubs:
            self._stubs["deidentify_content"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeidentifyContent",
                request_serializer=dlp.DeidentifyContentRequest.serialize,
                response_deserializer=dlp.DeidentifyContentResponse.deserialize,
            )
        return self._stubs["deidentify_content"]

    @property
    def reidentify_content(
        self,
    ) -> Callable[[dlp.ReidentifyContentRequest], dlp.ReidentifyContentResponse]:
        r"""Return a callable for the reidentify content method over gRPC.

        Re-identifies content that has been de-identified. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#re-identification_in_free_text_code_example
        to learn more.

        Returns:
            Callable[[~.ReidentifyContentRequest],
                    ~.ReidentifyContentResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reidentify_content" not in self._stubs:
            self._stubs["reidentify_content"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ReidentifyContent",
                request_serializer=dlp.ReidentifyContentRequest.serialize,
                response_deserializer=dlp.ReidentifyContentResponse.deserialize,
            )
        return self._stubs["reidentify_content"]

    @property
    def list_info_types(
        self,
    ) -> Callable[[dlp.ListInfoTypesRequest], dlp.ListInfoTypesResponse]:
        r"""Return a callable for the list info types method over gRPC.

        Returns a list of the sensitive information types
        that the DLP API supports. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference
        to learn more.

        Returns:
            Callable[[~.ListInfoTypesRequest],
                    ~.ListInfoTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_info_types" not in self._stubs:
            self._stubs["list_info_types"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListInfoTypes",
                request_serializer=dlp.ListInfoTypesRequest.serialize,
                response_deserializer=dlp.ListInfoTypesResponse.deserialize,
            )
        return self._stubs["list_info_types"]

    @property
    def create_inspect_template(
        self,
    ) -> Callable[[dlp.CreateInspectTemplateRequest], dlp.InspectTemplate]:
        r"""Return a callable for the create inspect template method over gRPC.

        Creates an InspectTemplate for reusing frequently
        used configuration for inspecting content, images, and
        storage. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates
        to learn more.

        Returns:
            Callable[[~.CreateInspectTemplateRequest],
                    ~.InspectTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_inspect_template" not in self._stubs:
            self._stubs["create_inspect_template"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/CreateInspectTemplate",
                request_serializer=dlp.CreateInspectTemplateRequest.serialize,
                response_deserializer=dlp.InspectTemplate.deserialize,
            )
        return self._stubs["create_inspect_template"]

    @property
    def update_inspect_template(
        self,
    ) -> Callable[[dlp.UpdateInspectTemplateRequest], dlp.InspectTemplate]:
        r"""Return a callable for the update inspect template method over gRPC.

        Updates the InspectTemplate.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates
        to learn more.

        Returns:
            Callable[[~.UpdateInspectTemplateRequest],
                    ~.InspectTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_inspect_template" not in self._stubs:
            self._stubs["update_inspect_template"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/UpdateInspectTemplate",
                request_serializer=dlp.UpdateInspectTemplateRequest.serialize,
                response_deserializer=dlp.InspectTemplate.deserialize,
            )
        return self._stubs["update_inspect_template"]

    @property
    def get_inspect_template(
        self,
    ) -> Callable[[dlp.GetInspectTemplateRequest], dlp.InspectTemplate]:
        r"""Return a callable for the get inspect template method over gRPC.

        Gets an InspectTemplate.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates
        to learn more.

        Returns:
            Callable[[~.GetInspectTemplateRequest],
                    ~.InspectTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_inspect_template" not in self._stubs:
            self._stubs["get_inspect_template"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetInspectTemplate",
                request_serializer=dlp.GetInspectTemplateRequest.serialize,
                response_deserializer=dlp.InspectTemplate.deserialize,
            )
        return self._stubs["get_inspect_template"]

    @property
    def list_inspect_templates(
        self,
    ) -> Callable[[dlp.ListInspectTemplatesRequest], dlp.ListInspectTemplatesResponse]:
        r"""Return a callable for the list inspect templates method over gRPC.

        Lists InspectTemplates.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates
        to learn more.

        Returns:
            Callable[[~.ListInspectTemplatesRequest],
                    ~.ListInspectTemplatesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_inspect_templates" not in self._stubs:
            self._stubs["list_inspect_templates"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListInspectTemplates",
                request_serializer=dlp.ListInspectTemplatesRequest.serialize,
                response_deserializer=dlp.ListInspectTemplatesResponse.deserialize,
            )
        return self._stubs["list_inspect_templates"]

    @property
    def delete_inspect_template(
        self,
    ) -> Callable[[dlp.DeleteInspectTemplateRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete inspect template method over gRPC.

        Deletes an InspectTemplate.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates
        to learn more.

        Returns:
            Callable[[~.DeleteInspectTemplateRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_inspect_template" not in self._stubs:
            self._stubs["delete_inspect_template"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeleteInspectTemplate",
                request_serializer=dlp.DeleteInspectTemplateRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_inspect_template"]

    @property
    def create_deidentify_template(
        self,
    ) -> Callable[[dlp.CreateDeidentifyTemplateRequest], dlp.DeidentifyTemplate]:
        r"""Return a callable for the create deidentify template method over gRPC.

        Creates a DeidentifyTemplate for reusing frequently
        used configuration for de-identifying content, images,
        and storage. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid
        to learn more.

        Returns:
            Callable[[~.CreateDeidentifyTemplateRequest],
                    ~.DeidentifyTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_deidentify_template" not in self._stubs:
            self._stubs["create_deidentify_template"] = (
                self._logged_channel.unary_unary(
                    "/google.privacy.dlp.v2.DlpService/CreateDeidentifyTemplate",
                    request_serializer=dlp.CreateDeidentifyTemplateRequest.serialize,
                    response_deserializer=dlp.DeidentifyTemplate.deserialize,
                )
            )
        return self._stubs["create_deidentify_template"]

    @property
    def update_deidentify_template(
        self,
    ) -> Callable[[dlp.UpdateDeidentifyTemplateRequest], dlp.DeidentifyTemplate]:
        r"""Return a callable for the update deidentify template method over gRPC.

        Updates the DeidentifyTemplate.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid
        to learn more.

        Returns:
            Callable[[~.UpdateDeidentifyTemplateRequest],
                    ~.DeidentifyTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_deidentify_template" not in self._stubs:
            self._stubs["update_deidentify_template"] = (
                self._logged_channel.unary_unary(
                    "/google.privacy.dlp.v2.DlpService/UpdateDeidentifyTemplate",
                    request_serializer=dlp.UpdateDeidentifyTemplateRequest.serialize,
                    response_deserializer=dlp.DeidentifyTemplate.deserialize,
                )
            )
        return self._stubs["update_deidentify_template"]

    @property
    def get_deidentify_template(
        self,
    ) -> Callable[[dlp.GetDeidentifyTemplateRequest], dlp.DeidentifyTemplate]:
        r"""Return a callable for the get deidentify template method over gRPC.

        Gets a DeidentifyTemplate.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid
        to learn more.

        Returns:
            Callable[[~.GetDeidentifyTemplateRequest],
                    ~.DeidentifyTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deidentify_template" not in self._stubs:
            self._stubs["get_deidentify_template"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetDeidentifyTemplate",
                request_serializer=dlp.GetDeidentifyTemplateRequest.serialize,
                response_deserializer=dlp.DeidentifyTemplate.deserialize,
            )
        return self._stubs["get_deidentify_template"]

    @property
    def list_deidentify_templates(
        self,
    ) -> Callable[
        [dlp.ListDeidentifyTemplatesRequest], dlp.ListDeidentifyTemplatesResponse
    ]:
        r"""Return a callable for the list deidentify templates method over gRPC.

        Lists DeidentifyTemplates.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid
        to learn more.

        Returns:
            Callable[[~.ListDeidentifyTemplatesRequest],
                    ~.ListDeidentifyTemplatesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deidentify_templates" not in self._stubs:
            self._stubs["list_deidentify_templates"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListDeidentifyTemplates",
                request_serializer=dlp.ListDeidentifyTemplatesRequest.serialize,
                response_deserializer=dlp.ListDeidentifyTemplatesResponse.deserialize,
            )
        return self._stubs["list_deidentify_templates"]

    @property
    def delete_deidentify_template(
        self,
    ) -> Callable[[dlp.DeleteDeidentifyTemplateRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete deidentify template method over gRPC.

        Deletes a DeidentifyTemplate.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid
        to learn more.

        Returns:
            Callable[[~.DeleteDeidentifyTemplateRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_deidentify_template" not in self._stubs:
            self._stubs["delete_deidentify_template"] = (
                self._logged_channel.unary_unary(
                    "/google.privacy.dlp.v2.DlpService/DeleteDeidentifyTemplate",
                    request_serializer=dlp.DeleteDeidentifyTemplateRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_deidentify_template"]

    @property
    def create_job_trigger(
        self,
    ) -> Callable[[dlp.CreateJobTriggerRequest], dlp.JobTrigger]:
        r"""Return a callable for the create job trigger method over gRPC.

        Creates a job trigger to run DLP actions such as
        scanning storage for sensitive information on a set
        schedule. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers
        to learn more.

        Returns:
            Callable[[~.CreateJobTriggerRequest],
                    ~.JobTrigger]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_job_trigger" not in self._stubs:
            self._stubs["create_job_trigger"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/CreateJobTrigger",
                request_serializer=dlp.CreateJobTriggerRequest.serialize,
                response_deserializer=dlp.JobTrigger.deserialize,
            )
        return self._stubs["create_job_trigger"]

    @property
    def update_job_trigger(
        self,
    ) -> Callable[[dlp.UpdateJobTriggerRequest], dlp.JobTrigger]:
        r"""Return a callable for the update job trigger method over gRPC.

        Updates a job trigger.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers
        to learn more.

        Returns:
            Callable[[~.UpdateJobTriggerRequest],
                    ~.JobTrigger]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_job_trigger" not in self._stubs:
            self._stubs["update_job_trigger"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/UpdateJobTrigger",
                request_serializer=dlp.UpdateJobTriggerRequest.serialize,
                response_deserializer=dlp.JobTrigger.deserialize,
            )
        return self._stubs["update_job_trigger"]

    @property
    def hybrid_inspect_job_trigger(
        self,
    ) -> Callable[[dlp.HybridInspectJobTriggerRequest], dlp.HybridInspectResponse]:
        r"""Return a callable for the hybrid inspect job trigger method over gRPC.

        Inspect hybrid content and store findings to a
        trigger. The inspection will be processed
        asynchronously. To review the findings monitor the jobs
        within the trigger.

        Returns:
            Callable[[~.HybridInspectJobTriggerRequest],
                    ~.HybridInspectResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "hybrid_inspect_job_trigger" not in self._stubs:
            self._stubs["hybrid_inspect_job_trigger"] = (
                self._logged_channel.unary_unary(
                    "/google.privacy.dlp.v2.DlpService/HybridInspectJobTrigger",
                    request_serializer=dlp.HybridInspectJobTriggerRequest.serialize,
                    response_deserializer=dlp.HybridInspectResponse.deserialize,
                )
            )
        return self._stubs["hybrid_inspect_job_trigger"]

    @property
    def get_job_trigger(self) -> Callable[[dlp.GetJobTriggerRequest], dlp.JobTrigger]:
        r"""Return a callable for the get job trigger method over gRPC.

        Gets a job trigger.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers
        to learn more.

        Returns:
            Callable[[~.GetJobTriggerRequest],
                    ~.JobTrigger]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_job_trigger" not in self._stubs:
            self._stubs["get_job_trigger"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetJobTrigger",
                request_serializer=dlp.GetJobTriggerRequest.serialize,
                response_deserializer=dlp.JobTrigger.deserialize,
            )
        return self._stubs["get_job_trigger"]

    @property
    def list_job_triggers(
        self,
    ) -> Callable[[dlp.ListJobTriggersRequest], dlp.ListJobTriggersResponse]:
        r"""Return a callable for the list job triggers method over gRPC.

        Lists job triggers.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers
        to learn more.

        Returns:
            Callable[[~.ListJobTriggersRequest],
                    ~.ListJobTriggersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_job_triggers" not in self._stubs:
            self._stubs["list_job_triggers"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListJobTriggers",
                request_serializer=dlp.ListJobTriggersRequest.serialize,
                response_deserializer=dlp.ListJobTriggersResponse.deserialize,
            )
        return self._stubs["list_job_triggers"]

    @property
    def delete_job_trigger(
        self,
    ) -> Callable[[dlp.DeleteJobTriggerRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete job trigger method over gRPC.

        Deletes a job trigger.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers
        to learn more.

        Returns:
            Callable[[~.DeleteJobTriggerRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_job_trigger" not in self._stubs:
            self._stubs["delete_job_trigger"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeleteJobTrigger",
                request_serializer=dlp.DeleteJobTriggerRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_job_trigger"]

    @property
    def activate_job_trigger(
        self,
    ) -> Callable[[dlp.ActivateJobTriggerRequest], dlp.DlpJob]:
        r"""Return a callable for the activate job trigger method over gRPC.

        Activate a job trigger. Causes the immediate execute
        of a trigger instead of waiting on the trigger event to
        occur.

        Returns:
            Callable[[~.ActivateJobTriggerRequest],
                    ~.DlpJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "activate_job_trigger" not in self._stubs:
            self._stubs["activate_job_trigger"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ActivateJobTrigger",
                request_serializer=dlp.ActivateJobTriggerRequest.serialize,
                response_deserializer=dlp.DlpJob.deserialize,
            )
        return self._stubs["activate_job_trigger"]

    @property
    def create_discovery_config(
        self,
    ) -> Callable[[dlp.CreateDiscoveryConfigRequest], dlp.DiscoveryConfig]:
        r"""Return a callable for the create discovery config method over gRPC.

        Creates a config for discovery to scan and profile
        storage.

        Returns:
            Callable[[~.CreateDiscoveryConfigRequest],
                    ~.DiscoveryConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_discovery_config" not in self._stubs:
            self._stubs["create_discovery_config"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/CreateDiscoveryConfig",
                request_serializer=dlp.CreateDiscoveryConfigRequest.serialize,
                response_deserializer=dlp.DiscoveryConfig.deserialize,
            )
        return self._stubs["create_discovery_config"]

    @property
    def update_discovery_config(
        self,
    ) -> Callable[[dlp.UpdateDiscoveryConfigRequest], dlp.DiscoveryConfig]:
        r"""Return a callable for the update discovery config method over gRPC.

        Updates a discovery configuration.

        Returns:
            Callable[[~.UpdateDiscoveryConfigRequest],
                    ~.DiscoveryConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_discovery_config" not in self._stubs:
            self._stubs["update_discovery_config"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/UpdateDiscoveryConfig",
                request_serializer=dlp.UpdateDiscoveryConfigRequest.serialize,
                response_deserializer=dlp.DiscoveryConfig.deserialize,
            )
        return self._stubs["update_discovery_config"]

    @property
    def get_discovery_config(
        self,
    ) -> Callable[[dlp.GetDiscoveryConfigRequest], dlp.DiscoveryConfig]:
        r"""Return a callable for the get discovery config method over gRPC.

        Gets a discovery configuration.

        Returns:
            Callable[[~.GetDiscoveryConfigRequest],
                    ~.DiscoveryConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_discovery_config" not in self._stubs:
            self._stubs["get_discovery_config"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetDiscoveryConfig",
                request_serializer=dlp.GetDiscoveryConfigRequest.serialize,
                response_deserializer=dlp.DiscoveryConfig.deserialize,
            )
        return self._stubs["get_discovery_config"]

    @property
    def list_discovery_configs(
        self,
    ) -> Callable[[dlp.ListDiscoveryConfigsRequest], dlp.ListDiscoveryConfigsResponse]:
        r"""Return a callable for the list discovery configs method over gRPC.

        Lists discovery configurations.

        Returns:
            Callable[[~.ListDiscoveryConfigsRequest],
                    ~.ListDiscoveryConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_discovery_configs" not in self._stubs:
            self._stubs["list_discovery_configs"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListDiscoveryConfigs",
                request_serializer=dlp.ListDiscoveryConfigsRequest.serialize,
                response_deserializer=dlp.ListDiscoveryConfigsResponse.deserialize,
            )
        return self._stubs["list_discovery_configs"]

    @property
    def delete_discovery_config(
        self,
    ) -> Callable[[dlp.DeleteDiscoveryConfigRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete discovery config method over gRPC.

        Deletes a discovery configuration.

        Returns:
            Callable[[~.DeleteDiscoveryConfigRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_discovery_config" not in self._stubs:
            self._stubs["delete_discovery_config"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeleteDiscoveryConfig",
                request_serializer=dlp.DeleteDiscoveryConfigRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_discovery_config"]

    @property
    def create_dlp_job(self) -> Callable[[dlp.CreateDlpJobRequest], dlp.DlpJob]:
        r"""Return a callable for the create dlp job method over gRPC.

        Creates a new job to inspect storage or calculate
        risk metrics. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage
        and
        https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis
        to learn more.

        When no InfoTypes or CustomInfoTypes are specified in
        inspect jobs, the system will automatically choose what
        detectors to run. By default this may be all types, but
        may change over time as detectors are updated.

        Returns:
            Callable[[~.CreateDlpJobRequest],
                    ~.DlpJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_dlp_job" not in self._stubs:
            self._stubs["create_dlp_job"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/CreateDlpJob",
                request_serializer=dlp.CreateDlpJobRequest.serialize,
                response_deserializer=dlp.DlpJob.deserialize,
            )
        return self._stubs["create_dlp_job"]

    @property
    def list_dlp_jobs(
        self,
    ) -> Callable[[dlp.ListDlpJobsRequest], dlp.ListDlpJobsResponse]:
        r"""Return a callable for the list dlp jobs method over gRPC.

        Lists DlpJobs that match the specified filter in the
        request. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage
        and
        https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis
        to learn more.

        Returns:
            Callable[[~.ListDlpJobsRequest],
                    ~.ListDlpJobsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_dlp_jobs" not in self._stubs:
            self._stubs["list_dlp_jobs"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListDlpJobs",
                request_serializer=dlp.ListDlpJobsRequest.serialize,
                response_deserializer=dlp.ListDlpJobsResponse.deserialize,
            )
        return self._stubs["list_dlp_jobs"]

    @property
    def get_dlp_job(self) -> Callable[[dlp.GetDlpJobRequest], dlp.DlpJob]:
        r"""Return a callable for the get dlp job method over gRPC.

        Gets the latest state of a long-running DlpJob.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage
        and
        https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis
        to learn more.

        Returns:
            Callable[[~.GetDlpJobRequest],
                    ~.DlpJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dlp_job" not in self._stubs:
            self._stubs["get_dlp_job"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetDlpJob",
                request_serializer=dlp.GetDlpJobRequest.serialize,
                response_deserializer=dlp.DlpJob.deserialize,
            )
        return self._stubs["get_dlp_job"]

    @property
    def delete_dlp_job(self) -> Callable[[dlp.DeleteDlpJobRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete dlp job method over gRPC.

        Deletes a long-running DlpJob. This method indicates
        that the client is no longer interested in the DlpJob
        result. The job will be canceled if possible.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage
        and
        https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis
        to learn more.

        Returns:
            Callable[[~.DeleteDlpJobRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_dlp_job" not in self._stubs:
            self._stubs["delete_dlp_job"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeleteDlpJob",
                request_serializer=dlp.DeleteDlpJobRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_dlp_job"]

    @property
    def cancel_dlp_job(self) -> Callable[[dlp.CancelDlpJobRequest], empty_pb2.Empty]:
        r"""Return a callable for the cancel dlp job method over gRPC.

        Starts asynchronous cancellation on a long-running
        DlpJob. The server makes a best effort to cancel the
        DlpJob, but success is not guaranteed.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage
        and
        https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis
        to learn more.

        Returns:
            Callable[[~.CancelDlpJobRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_dlp_job" not in self._stubs:
            self._stubs["cancel_dlp_job"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/CancelDlpJob",
                request_serializer=dlp.CancelDlpJobRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["cancel_dlp_job"]

    @property
    def create_stored_info_type(
        self,
    ) -> Callable[[dlp.CreateStoredInfoTypeRequest], dlp.StoredInfoType]:
        r"""Return a callable for the create stored info type method over gRPC.

        Creates a pre-built stored infoType to be used for
        inspection. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes
        to learn more.

        Returns:
            Callable[[~.CreateStoredInfoTypeRequest],
                    ~.StoredInfoType]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_stored_info_type" not in self._stubs:
            self._stubs["create_stored_info_type"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/CreateStoredInfoType",
                request_serializer=dlp.CreateStoredInfoTypeRequest.serialize,
                response_deserializer=dlp.StoredInfoType.deserialize,
            )
        return self._stubs["create_stored_info_type"]

    @property
    def update_stored_info_type(
        self,
    ) -> Callable[[dlp.UpdateStoredInfoTypeRequest], dlp.StoredInfoType]:
        r"""Return a callable for the update stored info type method over gRPC.

        Updates the stored infoType by creating a new
        version. The existing version will continue to be used
        until the new version is ready. See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes
        to learn more.

        Returns:
            Callable[[~.UpdateStoredInfoTypeRequest],
                    ~.StoredInfoType]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_stored_info_type" not in self._stubs:
            self._stubs["update_stored_info_type"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/UpdateStoredInfoType",
                request_serializer=dlp.UpdateStoredInfoTypeRequest.serialize,
                response_deserializer=dlp.StoredInfoType.deserialize,
            )
        return self._stubs["update_stored_info_type"]

    @property
    def get_stored_info_type(
        self,
    ) -> Callable[[dlp.GetStoredInfoTypeRequest], dlp.StoredInfoType]:
        r"""Return a callable for the get stored info type method over gRPC.

        Gets a stored infoType.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes
        to learn more.

        Returns:
            Callable[[~.GetStoredInfoTypeRequest],
                    ~.StoredInfoType]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_stored_info_type" not in self._stubs:
            self._stubs["get_stored_info_type"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetStoredInfoType",
                request_serializer=dlp.GetStoredInfoTypeRequest.serialize,
                response_deserializer=dlp.StoredInfoType.deserialize,
            )
        return self._stubs["get_stored_info_type"]

    @property
    def list_stored_info_types(
        self,
    ) -> Callable[[dlp.ListStoredInfoTypesRequest], dlp.ListStoredInfoTypesResponse]:
        r"""Return a callable for the list stored info types method over gRPC.

        Lists stored infoTypes.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes
        to learn more.

        Returns:
            Callable[[~.ListStoredInfoTypesRequest],
                    ~.ListStoredInfoTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_stored_info_types" not in self._stubs:
            self._stubs["list_stored_info_types"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListStoredInfoTypes",
                request_serializer=dlp.ListStoredInfoTypesRequest.serialize,
                response_deserializer=dlp.ListStoredInfoTypesResponse.deserialize,
            )
        return self._stubs["list_stored_info_types"]

    @property
    def delete_stored_info_type(
        self,
    ) -> Callable[[dlp.DeleteStoredInfoTypeRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete stored info type method over gRPC.

        Deletes a stored infoType.
        See
        https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes
        to learn more.

        Returns:
            Callable[[~.DeleteStoredInfoTypeRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_stored_info_type" not in self._stubs:
            self._stubs["delete_stored_info_type"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeleteStoredInfoType",
                request_serializer=dlp.DeleteStoredInfoTypeRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_stored_info_type"]

    @property
    def list_project_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListProjectDataProfilesRequest], dlp.ListProjectDataProfilesResponse
    ]:
        r"""Return a callable for the list project data profiles method over gRPC.

        Lists project data profiles for an organization.

        Returns:
            Callable[[~.ListProjectDataProfilesRequest],
                    ~.ListProjectDataProfilesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_project_data_profiles" not in self._stubs:
            self._stubs["list_project_data_profiles"] = (
                self._logged_channel.unary_unary(
                    "/google.privacy.dlp.v2.DlpService/ListProjectDataProfiles",
                    request_serializer=dlp.ListProjectDataProfilesRequest.serialize,
                    response_deserializer=dlp.ListProjectDataProfilesResponse.deserialize,
                )
            )
        return self._stubs["list_project_data_profiles"]

    @property
    def list_table_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListTableDataProfilesRequest], dlp.ListTableDataProfilesResponse
    ]:
        r"""Return a callable for the list table data profiles method over gRPC.

        Lists table data profiles for an organization.

        Returns:
            Callable[[~.ListTableDataProfilesRequest],
                    ~.ListTableDataProfilesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_table_data_profiles" not in self._stubs:
            self._stubs["list_table_data_profiles"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListTableDataProfiles",
                request_serializer=dlp.ListTableDataProfilesRequest.serialize,
                response_deserializer=dlp.ListTableDataProfilesResponse.deserialize,
            )
        return self._stubs["list_table_data_profiles"]

    @property
    def list_column_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListColumnDataProfilesRequest], dlp.ListColumnDataProfilesResponse
    ]:
        r"""Return a callable for the list column data profiles method over gRPC.

        Lists column data profiles for an organization.

        Returns:
            Callable[[~.ListColumnDataProfilesRequest],
                    ~.ListColumnDataProfilesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_column_data_profiles" not in self._stubs:
            self._stubs["list_column_data_profiles"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListColumnDataProfiles",
                request_serializer=dlp.ListColumnDataProfilesRequest.serialize,
                response_deserializer=dlp.ListColumnDataProfilesResponse.deserialize,
            )
        return self._stubs["list_column_data_profiles"]

    @property
    def get_project_data_profile(
        self,
    ) -> Callable[[dlp.GetProjectDataProfileRequest], dlp.ProjectDataProfile]:
        r"""Return a callable for the get project data profile method over gRPC.

        Gets a project data profile.

        Returns:
            Callable[[~.GetProjectDataProfileRequest],
                    ~.ProjectDataProfile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_project_data_profile" not in self._stubs:
            self._stubs["get_project_data_profile"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetProjectDataProfile",
                request_serializer=dlp.GetProjectDataProfileRequest.serialize,
                response_deserializer=dlp.ProjectDataProfile.deserialize,
            )
        return self._stubs["get_project_data_profile"]

    @property
    def list_file_store_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListFileStoreDataProfilesRequest], dlp.ListFileStoreDataProfilesResponse
    ]:
        r"""Return a callable for the list file store data profiles method over gRPC.

        Lists file store data profiles for an organization.

        Returns:
            Callable[[~.ListFileStoreDataProfilesRequest],
                    ~.ListFileStoreDataProfilesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_file_store_data_profiles" not in self._stubs:
            self._stubs["list_file_store_data_profiles"] = (
                self._logged_channel.unary_unary(
                    "/google.privacy.dlp.v2.DlpService/ListFileStoreDataProfiles",
                    request_serializer=dlp.ListFileStoreDataProfilesRequest.serialize,
                    response_deserializer=dlp.ListFileStoreDataProfilesResponse.deserialize,
                )
            )
        return self._stubs["list_file_store_data_profiles"]

    @property
    def get_file_store_data_profile(
        self,
    ) -> Callable[[dlp.GetFileStoreDataProfileRequest], dlp.FileStoreDataProfile]:
        r"""Return a callable for the get file store data profile method over gRPC.

        Gets a file store data profile.

        Returns:
            Callable[[~.GetFileStoreDataProfileRequest],
                    ~.FileStoreDataProfile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_file_store_data_profile" not in self._stubs:
            self._stubs["get_file_store_data_profile"] = (
                self._logged_channel.unary_unary(
                    "/google.privacy.dlp.v2.DlpService/GetFileStoreDataProfile",
                    request_serializer=dlp.GetFileStoreDataProfileRequest.serialize,
                    response_deserializer=dlp.FileStoreDataProfile.deserialize,
                )
            )
        return self._stubs["get_file_store_data_profile"]

    @property
    def delete_file_store_data_profile(
        self,
    ) -> Callable[[dlp.DeleteFileStoreDataProfileRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete file store data profile method over gRPC.

        Delete a FileStoreDataProfile. Will not prevent the
        profile from being regenerated if the resource is still
        included in a discovery configuration.

        Returns:
            Callable[[~.DeleteFileStoreDataProfileRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_file_store_data_profile" not in self._stubs:
            self._stubs["delete_file_store_data_profile"] = (
                self._logged_channel.unary_unary(
                    "/google.privacy.dlp.v2.DlpService/DeleteFileStoreDataProfile",
                    request_serializer=dlp.DeleteFileStoreDataProfileRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_file_store_data_profile"]

    @property
    def get_table_data_profile(
        self,
    ) -> Callable[[dlp.GetTableDataProfileRequest], dlp.TableDataProfile]:
        r"""Return a callable for the get table data profile method over gRPC.

        Gets a table data profile.

        Returns:
            Callable[[~.GetTableDataProfileRequest],
                    ~.TableDataProfile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_table_data_profile" not in self._stubs:
            self._stubs["get_table_data_profile"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetTableDataProfile",
                request_serializer=dlp.GetTableDataProfileRequest.serialize,
                response_deserializer=dlp.TableDataProfile.deserialize,
            )
        return self._stubs["get_table_data_profile"]

    @property
    def get_column_data_profile(
        self,
    ) -> Callable[[dlp.GetColumnDataProfileRequest], dlp.ColumnDataProfile]:
        r"""Return a callable for the get column data profile method over gRPC.

        Gets a column data profile.

        Returns:
            Callable[[~.GetColumnDataProfileRequest],
                    ~.ColumnDataProfile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_column_data_profile" not in self._stubs:
            self._stubs["get_column_data_profile"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetColumnDataProfile",
                request_serializer=dlp.GetColumnDataProfileRequest.serialize,
                response_deserializer=dlp.ColumnDataProfile.deserialize,
            )
        return self._stubs["get_column_data_profile"]

    @property
    def delete_table_data_profile(
        self,
    ) -> Callable[[dlp.DeleteTableDataProfileRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete table data profile method over gRPC.

        Delete a TableDataProfile. Will not prevent the
        profile from being regenerated if the table is still
        included in a discovery configuration.

        Returns:
            Callable[[~.DeleteTableDataProfileRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_table_data_profile" not in self._stubs:
            self._stubs["delete_table_data_profile"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeleteTableDataProfile",
                request_serializer=dlp.DeleteTableDataProfileRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_table_data_profile"]

    @property
    def hybrid_inspect_dlp_job(
        self,
    ) -> Callable[[dlp.HybridInspectDlpJobRequest], dlp.HybridInspectResponse]:
        r"""Return a callable for the hybrid inspect dlp job method over gRPC.

        Inspect hybrid content and store findings to a job.
        To review the findings, inspect the job. Inspection will
        occur asynchronously.

        Returns:
            Callable[[~.HybridInspectDlpJobRequest],
                    ~.HybridInspectResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "hybrid_inspect_dlp_job" not in self._stubs:
            self._stubs["hybrid_inspect_dlp_job"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/HybridInspectDlpJob",
                request_serializer=dlp.HybridInspectDlpJobRequest.serialize,
                response_deserializer=dlp.HybridInspectResponse.deserialize,
            )
        return self._stubs["hybrid_inspect_dlp_job"]

    @property
    def finish_dlp_job(self) -> Callable[[dlp.FinishDlpJobRequest], empty_pb2.Empty]:
        r"""Return a callable for the finish dlp job method over gRPC.

        Finish a running hybrid DlpJob. Triggers the
        finalization steps and running of any enabled actions
        that have not yet run.

        Returns:
            Callable[[~.FinishDlpJobRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "finish_dlp_job" not in self._stubs:
            self._stubs["finish_dlp_job"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/FinishDlpJob",
                request_serializer=dlp.FinishDlpJobRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["finish_dlp_job"]

    @property
    def create_connection(
        self,
    ) -> Callable[[dlp.CreateConnectionRequest], dlp.Connection]:
        r"""Return a callable for the create connection method over gRPC.

        Create a Connection to an external data source.

        Returns:
            Callable[[~.CreateConnectionRequest],
                    ~.Connection]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_connection" not in self._stubs:
            self._stubs["create_connection"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/CreateConnection",
                request_serializer=dlp.CreateConnectionRequest.serialize,
                response_deserializer=dlp.Connection.deserialize,
            )
        return self._stubs["create_connection"]

    @property
    def get_connection(self) -> Callable[[dlp.GetConnectionRequest], dlp.Connection]:
        r"""Return a callable for the get connection method over gRPC.

        Get a Connection by name.

        Returns:
            Callable[[~.GetConnectionRequest],
                    ~.Connection]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_connection" not in self._stubs:
            self._stubs["get_connection"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetConnection",
                request_serializer=dlp.GetConnectionRequest.serialize,
                response_deserializer=dlp.Connection.deserialize,
            )
        return self._stubs["get_connection"]

    @property
    def list_connections(
        self,
    ) -> Callable[[dlp.ListConnectionsRequest], dlp.ListConnectionsResponse]:
        r"""Return a callable for the list connections method over gRPC.

        Lists Connections in a parent. Use SearchConnections
        to see all connections within an organization.

        Returns:
            Callable[[~.ListConnectionsRequest],
                    ~.ListConnectionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_connections" not in self._stubs:
            self._stubs["list_connections"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListConnections",
                request_serializer=dlp.ListConnectionsRequest.serialize,
                response_deserializer=dlp.ListConnectionsResponse.deserialize,
            )
        return self._stubs["list_connections"]

    @property
    def search_connections(
        self,
    ) -> Callable[[dlp.SearchConnectionsRequest], dlp.SearchConnectionsResponse]:
        r"""Return a callable for the search connections method over gRPC.

        Searches for Connections in a parent.

        Returns:
            Callable[[~.SearchConnectionsRequest],
                    ~.SearchConnectionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_connections" not in self._stubs:
            self._stubs["search_connections"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/SearchConnections",
                request_serializer=dlp.SearchConnectionsRequest.serialize,
                response_deserializer=dlp.SearchConnectionsResponse.deserialize,
            )
        return self._stubs["search_connections"]

    @property
    def delete_connection(
        self,
    ) -> Callable[[dlp.DeleteConnectionRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete connection method over gRPC.

        Delete a Connection.

        Returns:
            Callable[[~.DeleteConnectionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_connection" not in self._stubs:
            self._stubs["delete_connection"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeleteConnection",
                request_serializer=dlp.DeleteConnectionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_connection"]

    @property
    def update_connection(
        self,
    ) -> Callable[[dlp.UpdateConnectionRequest], dlp.Connection]:
        r"""Return a callable for the update connection method over gRPC.

        Update a Connection.

        Returns:
            Callable[[~.UpdateConnectionRequest],
                    ~.Connection]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_connection" not in self._stubs:
            self._stubs["update_connection"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/UpdateConnection",
                request_serializer=dlp.UpdateConnectionRequest.serialize,
                response_deserializer=dlp.Connection.deserialize,
            )
        return self._stubs["update_connection"]

    @property
    def create_content_policy(
        self,
    ) -> Callable[[dlp.CreateContentPolicyRequest], dlp.ContentPolicy]:
        r"""Return a callable for the create content policy method over gRPC.

        Create a ContentPolicy.

        Returns:
            Callable[[~.CreateContentPolicyRequest],
                    ~.ContentPolicy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_content_policy" not in self._stubs:
            self._stubs["create_content_policy"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/CreateContentPolicy",
                request_serializer=dlp.CreateContentPolicyRequest.serialize,
                response_deserializer=dlp.ContentPolicy.deserialize,
            )
        return self._stubs["create_content_policy"]

    @property
    def update_content_policy(
        self,
    ) -> Callable[[dlp.UpdateContentPolicyRequest], dlp.ContentPolicy]:
        r"""Return a callable for the update content policy method over gRPC.

        Update a ContentPolicy.

        Returns:
            Callable[[~.UpdateContentPolicyRequest],
                    ~.ContentPolicy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_content_policy" not in self._stubs:
            self._stubs["update_content_policy"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/UpdateContentPolicy",
                request_serializer=dlp.UpdateContentPolicyRequest.serialize,
                response_deserializer=dlp.ContentPolicy.deserialize,
            )
        return self._stubs["update_content_policy"]

    @property
    def get_content_policy(
        self,
    ) -> Callable[[dlp.GetContentPolicyRequest], dlp.ContentPolicy]:
        r"""Return a callable for the get content policy method over gRPC.

        Get a ContentPolicy.

        Returns:
            Callable[[~.GetContentPolicyRequest],
                    ~.ContentPolicy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_content_policy" not in self._stubs:
            self._stubs["get_content_policy"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/GetContentPolicy",
                request_serializer=dlp.GetContentPolicyRequest.serialize,
                response_deserializer=dlp.ContentPolicy.deserialize,
            )
        return self._stubs["get_content_policy"]

    @property
    def list_content_policies(
        self,
    ) -> Callable[[dlp.ListContentPoliciesRequest], dlp.ListContentPoliciesResponse]:
        r"""Return a callable for the list content policies method over gRPC.

        Lists ContentPolicies in a parent.

        Returns:
            Callable[[~.ListContentPoliciesRequest],
                    ~.ListContentPoliciesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_content_policies" not in self._stubs:
            self._stubs["list_content_policies"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/ListContentPolicies",
                request_serializer=dlp.ListContentPoliciesRequest.serialize,
                response_deserializer=dlp.ListContentPoliciesResponse.deserialize,
            )
        return self._stubs["list_content_policies"]

    @property
    def delete_content_policy(
        self,
    ) -> Callable[[dlp.DeleteContentPolicyRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete content policy method over gRPC.

        Delete a ContentPolicy.

        Returns:
            Callable[[~.DeleteContentPolicyRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_content_policy" not in self._stubs:
            self._stubs["delete_content_policy"] = self._logged_channel.unary_unary(
                "/google.privacy.dlp.v2.DlpService/DeleteContentPolicy",
                request_serializer=dlp.DeleteContentPolicyRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_content_policy"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("DlpServiceGrpcTransport",)
