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
from typing import TYPE_CHECKING, Callable, Dict, Optional, Sequence, Tuple, Union

import google.auth  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.designcenter_v1._compat import (
    _observability,
    apply_channel_interceptors,
)
from google.cloud.designcenter_v1.types import (
    apphub_integration_messages,
    authoring,
    authoring_messages,
    best_practices,
    best_practices_messages,
    catalog_management,
    catalog_management_messages,
    deployment_messages,
    deployment_resources,
    sharing,
    sharing_messages,
)

from .base import DEFAULT_CLIENT_INFO, DesignCenterTransport

if TYPE_CHECKING:  # pragma: NO COVER
    # ClientInterceptor was added in google-api-core 2.36.0+; ignore attribute-defined for older api-core versions during type checking
    from google.api_core.grpc_helpers import (
        ClientInterceptor,  # type: ignore[attr-defined]
    )

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
                    "serviceName": "google.cloud.designcenter.v1.DesignCenter",
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
                    "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DesignCenterGrpcTransport(DesignCenterTransport):
    """gRPC backend transport for DesignCenter.

    Service describing handlers for resources

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
        host: str = "designcenter.googleapis.com",
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
        interceptors: Optional[
            Sequence[Union["ClientInterceptor", Callable[[grpc.Channel], grpc.Channel]]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'designcenter.googleapis.com').
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
            interceptors (Optional[Sequence[Union[ClientInterceptor, Callable[[grpc.Channel], grpc.Channel]]]]):
                Additional interceptors (or callables that apply interceptors) to apply to the
                gRPC channel.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.

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
            client_options=client_options,
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

        channel_interceptors = list(interceptors) if interceptors else []
        if (
            _observability is not None
            and (
                otel_interceptor := _observability.get_otel_interceptor(
                    self._client_options
                )
            )
            is not None
            and otel_interceptor not in channel_interceptors
            and not any(
                getattr(i, "_is_otel_interceptor", None) is True
                for i in channel_interceptors
            )
        ):
            channel_interceptors.append(otel_interceptor)

        self._grpc_channel = apply_channel_interceptors(
            self._grpc_channel, channel_interceptors
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
        host: str = "designcenter.googleapis.com",
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
    def get_space(
        self,
    ) -> Callable[
        [catalog_management_messages.GetSpaceRequest], catalog_management.Space
    ]:
        r"""Return a callable for the get space method over gRPC.

        Gets details about a space.

        Returns:
            Callable[[~.GetSpaceRequest],
                    ~.Space]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_space" not in self._stubs:
            self._stubs["get_space"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetSpace",
                request_serializer=catalog_management_messages.GetSpaceRequest.serialize,
                response_deserializer=catalog_management.Space.deserialize,
            )
        return self._stubs["get_space"]

    @property
    def list_spaces(
        self,
    ) -> Callable[
        [catalog_management_messages.ListSpacesRequest],
        catalog_management_messages.ListSpacesResponse,
    ]:
        r"""Return a callable for the list spaces method over gRPC.

        Lists spaces in a given project and location.

        Returns:
            Callable[[~.ListSpacesRequest],
                    ~.ListSpacesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_spaces" not in self._stubs:
            self._stubs["list_spaces"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ListSpaces",
                request_serializer=catalog_management_messages.ListSpacesRequest.serialize,
                response_deserializer=catalog_management_messages.ListSpacesResponse.deserialize,
            )
        return self._stubs["list_spaces"]

    @property
    def create_space(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateSpaceRequest], catalog_management.Space
    ]:
        r"""Return a callable for the create space method over gRPC.

        Creates a space.

        Returns:
            Callable[[~.CreateSpaceRequest],
                    ~.Space]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_space" not in self._stubs:
            self._stubs["create_space"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/CreateSpace",
                request_serializer=catalog_management_messages.CreateSpaceRequest.serialize,
                response_deserializer=catalog_management.Space.deserialize,
            )
        return self._stubs["create_space"]

    @property
    def update_space(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateSpaceRequest], catalog_management.Space
    ]:
        r"""Return a callable for the update space method over gRPC.

        Updates a space.

        Returns:
            Callable[[~.UpdateSpaceRequest],
                    ~.Space]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_space" not in self._stubs:
            self._stubs["update_space"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/UpdateSpace",
                request_serializer=catalog_management_messages.UpdateSpaceRequest.serialize,
                response_deserializer=catalog_management.Space.deserialize,
            )
        return self._stubs["update_space"]

    @property
    def delete_space(
        self,
    ) -> Callable[[catalog_management_messages.DeleteSpaceRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete space method over gRPC.

        Deletes a space.

        Returns:
            Callable[[~.DeleteSpaceRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_space" not in self._stubs:
            self._stubs["delete_space"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/DeleteSpace",
                request_serializer=catalog_management_messages.DeleteSpaceRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_space"]

    @property
    def get_application_template(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateRequest],
        authoring.ApplicationTemplate,
    ]:
        r"""Return a callable for the get application template method over gRPC.

        Gets details about an application template.

        Returns:
            Callable[[~.GetApplicationTemplateRequest],
                    ~.ApplicationTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_application_template" not in self._stubs:
            self._stubs["get_application_template"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetApplicationTemplate",
                request_serializer=authoring_messages.GetApplicationTemplateRequest.serialize,
                response_deserializer=authoring.ApplicationTemplate.deserialize,
            )
        return self._stubs["get_application_template"]

    @property
    def list_application_templates(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplatesRequest],
        authoring_messages.ListApplicationTemplatesResponse,
    ]:
        r"""Return a callable for the list application templates method over gRPC.

        Lists application templates in a given space.

        Returns:
            Callable[[~.ListApplicationTemplatesRequest],
                    ~.ListApplicationTemplatesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_application_templates" not in self._stubs:
            self._stubs["list_application_templates"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ListApplicationTemplates",
                    request_serializer=authoring_messages.ListApplicationTemplatesRequest.serialize,
                    response_deserializer=authoring_messages.ListApplicationTemplatesResponse.deserialize,
                )
            )
        return self._stubs["list_application_templates"]

    @property
    def create_application_template(
        self,
    ) -> Callable[
        [authoring_messages.CreateApplicationTemplateRequest],
        authoring.ApplicationTemplate,
    ]:
        r"""Return a callable for the create application template method over gRPC.

        Creates an application template.

        Returns:
            Callable[[~.CreateApplicationTemplateRequest],
                    ~.ApplicationTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_application_template" not in self._stubs:
            self._stubs["create_application_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/CreateApplicationTemplate",
                    request_serializer=authoring_messages.CreateApplicationTemplateRequest.serialize,
                    response_deserializer=authoring.ApplicationTemplate.deserialize,
                )
            )
        return self._stubs["create_application_template"]

    @property
    def update_application_template(
        self,
    ) -> Callable[
        [authoring_messages.UpdateApplicationTemplateRequest],
        authoring.ApplicationTemplate,
    ]:
        r"""Return a callable for the update application template method over gRPC.

        Updates an application template.

        Returns:
            Callable[[~.UpdateApplicationTemplateRequest],
                    ~.ApplicationTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_application_template" not in self._stubs:
            self._stubs["update_application_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/UpdateApplicationTemplate",
                    request_serializer=authoring_messages.UpdateApplicationTemplateRequest.serialize,
                    response_deserializer=authoring.ApplicationTemplate.deserialize,
                )
            )
        return self._stubs["update_application_template"]

    @property
    def import_application_template(
        self,
    ) -> Callable[
        [authoring_messages.ImportApplicationTemplateRequest],
        authoring.ApplicationTemplate,
    ]:
        r"""Return a callable for the import application template method over gRPC.

        Imports to an existing application template from a
        given shared template.

        Returns:
            Callable[[~.ImportApplicationTemplateRequest],
                    ~.ApplicationTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_application_template" not in self._stubs:
            self._stubs["import_application_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ImportApplicationTemplate",
                    request_serializer=authoring_messages.ImportApplicationTemplateRequest.serialize,
                    response_deserializer=authoring.ApplicationTemplate.deserialize,
                )
            )
        return self._stubs["import_application_template"]

    @property
    def delete_application_template(
        self,
    ) -> Callable[
        [authoring_messages.DeleteApplicationTemplateRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete application template method over gRPC.

        Deletes an application template.

        Returns:
            Callable[[~.DeleteApplicationTemplateRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_application_template" not in self._stubs:
            self._stubs["delete_application_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/DeleteApplicationTemplate",
                    request_serializer=authoring_messages.DeleteApplicationTemplateRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_application_template"]

    @property
    def commit_application_template(
        self,
    ) -> Callable[
        [authoring_messages.CommitApplicationTemplateRequest],
        authoring.ApplicationTemplateRevision,
    ]:
        r"""Return a callable for the commit application template method over gRPC.

        Commits an application template to create a new
        revision.

        Returns:
            Callable[[~.CommitApplicationTemplateRequest],
                    ~.ApplicationTemplateRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "commit_application_template" not in self._stubs:
            self._stubs["commit_application_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/CommitApplicationTemplate",
                    request_serializer=authoring_messages.CommitApplicationTemplateRequest.serialize,
                    response_deserializer=authoring.ApplicationTemplateRevision.deserialize,
                )
            )
        return self._stubs["commit_application_template"]

    @property
    def snapshot_application_template(
        self,
    ) -> Callable[
        [authoring_messages.SnapshotApplicationTemplateRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the snapshot application template method over gRPC.

        Snapshots an application template to create a new
        revision asynchronously.

        Returns:
            Callable[[~.SnapshotApplicationTemplateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "snapshot_application_template" not in self._stubs:
            self._stubs["snapshot_application_template"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/SnapshotApplicationTemplate",
                    request_serializer=authoring_messages.SnapshotApplicationTemplateRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["snapshot_application_template"]

    @property
    def generate_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.GenerateApplicationTemplateIaCRequest],
        authoring_messages.GenerateApplicationTemplateIaCResponse,
    ]:
        r"""Return a callable for the generate application template
        ia c method over gRPC.

        Generates Terraform files for an application
        template. This is a SYNCHRONOUS operation and returns
        the generated IaC directly in the response. It
        does NOT download external module sources; it only uses
        remote sources.

        Returns:
            Callable[[~.GenerateApplicationTemplateIaCRequest],
                    ~.GenerateApplicationTemplateIaCResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_application_template_ia_c" not in self._stubs:
            self._stubs["generate_application_template_ia_c"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GenerateApplicationTemplateIaC",
                    request_serializer=authoring_messages.GenerateApplicationTemplateIaCRequest.serialize,
                    response_deserializer=authoring_messages.GenerateApplicationTemplateIaCResponse.deserialize,
                )
            )
        return self._stubs["generate_application_template_ia_c"]

    @property
    def export_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ExportApplicationTemplateIaCRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the export application template ia
        c method over gRPC.

        Exports Terraform files for an application template.
        The generated modules can have remote sources or local
        sources downloaded from remote. This is an ASYNCHRONOUS
        operation that returns a Long Running Operation.

        Returns:
            Callable[[~.ExportApplicationTemplateIaCRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_application_template_ia_c" not in self._stubs:
            self._stubs["export_application_template_ia_c"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ExportApplicationTemplateIaC",
                    request_serializer=authoring_messages.ExportApplicationTemplateIaCRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["export_application_template_ia_c"]

    @property
    def generate_application_template_revision_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.GenerateApplicationTemplateRevisionIaCRequest],
        authoring_messages.GenerateApplicationTemplateRevisionIaCResponse,
    ]:
        r"""Return a callable for the generate application template
        revision ia c method over gRPC.

        Generates Terraform files for an application template
        revision. This is a SYNCHRONOUS operation and returns
        the generated IaC directly in the response. It
        does NOT download external module sources; it only uses
        remote sources.

        Returns:
            Callable[[~.GenerateApplicationTemplateRevisionIaCRequest],
                    ~.GenerateApplicationTemplateRevisionIaCResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_application_template_revision_ia_c" not in self._stubs:
            self._stubs["generate_application_template_revision_ia_c"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GenerateApplicationTemplateRevisionIaC",
                    request_serializer=authoring_messages.GenerateApplicationTemplateRevisionIaCRequest.serialize,
                    response_deserializer=authoring_messages.GenerateApplicationTemplateRevisionIaCResponse.deserialize,
                )
            )
        return self._stubs["generate_application_template_revision_ia_c"]

    @property
    def export_application_template_revision_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ExportApplicationTemplateRevisionIaCRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the export application template
        revision ia c method over gRPC.

        Exports Terraform files for an application template
        revision. The generated modules can have remote sources
        or local sources downloaded from remote. This is an
        ASYNCHRONOUS operation that returns a Long Running
        Operation.

        Returns:
            Callable[[~.ExportApplicationTemplateRevisionIaCRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_application_template_revision_ia_c" not in self._stubs:
            self._stubs["export_application_template_revision_ia_c"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ExportApplicationTemplateRevisionIaC",
                    request_serializer=authoring_messages.ExportApplicationTemplateRevisionIaCRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["export_application_template_revision_ia_c"]

    @property
    def get_component(
        self,
    ) -> Callable[[authoring_messages.GetComponentRequest], authoring.Component]:
        r"""Return a callable for the get component method over gRPC.

        Gets details about a Component.

        Returns:
            Callable[[~.GetComponentRequest],
                    ~.Component]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_component" not in self._stubs:
            self._stubs["get_component"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetComponent",
                request_serializer=authoring_messages.GetComponentRequest.serialize,
                response_deserializer=authoring.Component.deserialize,
            )
        return self._stubs["get_component"]

    @property
    def list_components(
        self,
    ) -> Callable[
        [authoring_messages.ListComponentsRequest],
        authoring_messages.ListComponentsResponse,
    ]:
        r"""Return a callable for the list components method over gRPC.

        Lists components in an application template.

        Returns:
            Callable[[~.ListComponentsRequest],
                    ~.ListComponentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_components" not in self._stubs:
            self._stubs["list_components"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ListComponents",
                request_serializer=authoring_messages.ListComponentsRequest.serialize,
                response_deserializer=authoring_messages.ListComponentsResponse.deserialize,
            )
        return self._stubs["list_components"]

    @property
    def create_component(
        self,
    ) -> Callable[[authoring_messages.CreateComponentRequest], authoring.Component]:
        r"""Return a callable for the create component method over gRPC.

        Creates a component.

        Returns:
            Callable[[~.CreateComponentRequest],
                    ~.Component]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_component" not in self._stubs:
            self._stubs["create_component"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/CreateComponent",
                request_serializer=authoring_messages.CreateComponentRequest.serialize,
                response_deserializer=authoring.Component.deserialize,
            )
        return self._stubs["create_component"]

    @property
    def update_component(
        self,
    ) -> Callable[[authoring_messages.UpdateComponentRequest], authoring.Component]:
        r"""Return a callable for the update component method over gRPC.

        Updates a component.

        Returns:
            Callable[[~.UpdateComponentRequest],
                    ~.Component]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_component" not in self._stubs:
            self._stubs["update_component"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/UpdateComponent",
                request_serializer=authoring_messages.UpdateComponentRequest.serialize,
                response_deserializer=authoring.Component.deserialize,
            )
        return self._stubs["update_component"]

    @property
    def delete_component(
        self,
    ) -> Callable[[authoring_messages.DeleteComponentRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete component method over gRPC.

        Deletes a component.

        Returns:
            Callable[[~.DeleteComponentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_component" not in self._stubs:
            self._stubs["delete_component"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/DeleteComponent",
                request_serializer=authoring_messages.DeleteComponentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_component"]

    @property
    def get_connection(
        self,
    ) -> Callable[[authoring_messages.GetConnectionRequest], authoring.Connection]:
        r"""Return a callable for the get connection method over gRPC.

        Gets details about a connection.

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
                "/google.cloud.designcenter.v1.DesignCenter/GetConnection",
                request_serializer=authoring_messages.GetConnectionRequest.serialize,
                response_deserializer=authoring.Connection.deserialize,
            )
        return self._stubs["get_connection"]

    @property
    def list_connections(
        self,
    ) -> Callable[
        [authoring_messages.ListConnectionsRequest],
        authoring_messages.ListConnectionsResponse,
    ]:
        r"""Return a callable for the list connections method over gRPC.

        Lists connections in an application template.

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
                "/google.cloud.designcenter.v1.DesignCenter/ListConnections",
                request_serializer=authoring_messages.ListConnectionsRequest.serialize,
                response_deserializer=authoring_messages.ListConnectionsResponse.deserialize,
            )
        return self._stubs["list_connections"]

    @property
    def create_connection(
        self,
    ) -> Callable[[authoring_messages.CreateConnectionRequest], authoring.Connection]:
        r"""Return a callable for the create connection method over gRPC.

        Creates a connection.

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
                "/google.cloud.designcenter.v1.DesignCenter/CreateConnection",
                request_serializer=authoring_messages.CreateConnectionRequest.serialize,
                response_deserializer=authoring.Connection.deserialize,
            )
        return self._stubs["create_connection"]

    @property
    def update_connection(
        self,
    ) -> Callable[[authoring_messages.UpdateConnectionRequest], authoring.Connection]:
        r"""Return a callable for the update connection method over gRPC.

        Updates a connection.

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
                "/google.cloud.designcenter.v1.DesignCenter/UpdateConnection",
                request_serializer=authoring_messages.UpdateConnectionRequest.serialize,
                response_deserializer=authoring.Connection.deserialize,
            )
        return self._stubs["update_connection"]

    @property
    def delete_connection(
        self,
    ) -> Callable[[authoring_messages.DeleteConnectionRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete connection method over gRPC.

        Deletes a connection.

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
                "/google.cloud.designcenter.v1.DesignCenter/DeleteConnection",
                request_serializer=authoring_messages.DeleteConnectionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_connection"]

    @property
    def get_application_template_revision(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateRevisionRequest],
        authoring.ApplicationTemplateRevision,
    ]:
        r"""Return a callable for the get application template
        revision method over gRPC.

        Gets details about an application template revision.

        Returns:
            Callable[[~.GetApplicationTemplateRevisionRequest],
                    ~.ApplicationTemplateRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_application_template_revision" not in self._stubs:
            self._stubs["get_application_template_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GetApplicationTemplateRevision",
                    request_serializer=authoring_messages.GetApplicationTemplateRevisionRequest.serialize,
                    response_deserializer=authoring.ApplicationTemplateRevision.deserialize,
                )
            )
        return self._stubs["get_application_template_revision"]

    @property
    def list_application_template_revisions(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplateRevisionsRequest],
        authoring_messages.ListApplicationTemplateRevisionsResponse,
    ]:
        r"""Return a callable for the list application template
        revisions method over gRPC.

        Lists application template revisions in a given
        application template.

        Returns:
            Callable[[~.ListApplicationTemplateRevisionsRequest],
                    ~.ListApplicationTemplateRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_application_template_revisions" not in self._stubs:
            self._stubs["list_application_template_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ListApplicationTemplateRevisions",
                    request_serializer=authoring_messages.ListApplicationTemplateRevisionsRequest.serialize,
                    response_deserializer=authoring_messages.ListApplicationTemplateRevisionsResponse.deserialize,
                )
            )
        return self._stubs["list_application_template_revisions"]

    @property
    def delete_application_template_revision(
        self,
    ) -> Callable[
        [authoring_messages.DeleteApplicationTemplateRevisionRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete application template
        revision method over gRPC.

        Deletes an application template revision.

        Returns:
            Callable[[~.DeleteApplicationTemplateRevisionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_application_template_revision" not in self._stubs:
            self._stubs["delete_application_template_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/DeleteApplicationTemplateRevision",
                    request_serializer=authoring_messages.DeleteApplicationTemplateRevisionRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_application_template_revision"]

    @property
    def get_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogRequest], catalog_management.Catalog
    ]:
        r"""Return a callable for the get catalog method over gRPC.

        Gets details about a catalog.

        Returns:
            Callable[[~.GetCatalogRequest],
                    ~.Catalog]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_catalog" not in self._stubs:
            self._stubs["get_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetCatalog",
                request_serializer=catalog_management_messages.GetCatalogRequest.serialize,
                response_deserializer=catalog_management.Catalog.deserialize,
            )
        return self._stubs["get_catalog"]

    @property
    def list_catalogs(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogsRequest],
        catalog_management_messages.ListCatalogsResponse,
    ]:
        r"""Return a callable for the list catalogs method over gRPC.

        Lists catalogs in a given space.

        Returns:
            Callable[[~.ListCatalogsRequest],
                    ~.ListCatalogsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_catalogs" not in self._stubs:
            self._stubs["list_catalogs"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ListCatalogs",
                request_serializer=catalog_management_messages.ListCatalogsRequest.serialize,
                response_deserializer=catalog_management_messages.ListCatalogsResponse.deserialize,
            )
        return self._stubs["list_catalogs"]

    @property
    def create_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogRequest], catalog_management.Catalog
    ]:
        r"""Return a callable for the create catalog method over gRPC.

        Creates a catalog.

        Returns:
            Callable[[~.CreateCatalogRequest],
                    ~.Catalog]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_catalog" not in self._stubs:
            self._stubs["create_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/CreateCatalog",
                request_serializer=catalog_management_messages.CreateCatalogRequest.serialize,
                response_deserializer=catalog_management.Catalog.deserialize,
            )
        return self._stubs["create_catalog"]

    @property
    def update_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateCatalogRequest], catalog_management.Catalog
    ]:
        r"""Return a callable for the update catalog method over gRPC.

        Updates a catalog.

        Returns:
            Callable[[~.UpdateCatalogRequest],
                    ~.Catalog]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_catalog" not in self._stubs:
            self._stubs["update_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/UpdateCatalog",
                request_serializer=catalog_management_messages.UpdateCatalogRequest.serialize,
                response_deserializer=catalog_management.Catalog.deserialize,
            )
        return self._stubs["update_catalog"]

    @property
    def delete_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete catalog method over gRPC.

        Deletes a catalog.

        Returns:
            Callable[[~.DeleteCatalogRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_catalog" not in self._stubs:
            self._stubs["delete_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/DeleteCatalog",
                request_serializer=catalog_management_messages.DeleteCatalogRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_catalog"]

    @property
    def create_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogTemplateRequest],
        catalog_management.CatalogTemplate,
    ]:
        r"""Return a callable for the create catalog template method over gRPC.

        Adds a template to a catalog.

        Returns:
            Callable[[~.CreateCatalogTemplateRequest],
                    ~.CatalogTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_catalog_template" not in self._stubs:
            self._stubs["create_catalog_template"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/CreateCatalogTemplate",
                request_serializer=catalog_management_messages.CreateCatalogTemplateRequest.serialize,
                response_deserializer=catalog_management.CatalogTemplate.deserialize,
            )
        return self._stubs["create_catalog_template"]

    @property
    def get_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogTemplateRequest],
        catalog_management.CatalogTemplate,
    ]:
        r"""Return a callable for the get catalog template method over gRPC.

        Gets a catalog template.

        Returns:
            Callable[[~.GetCatalogTemplateRequest],
                    ~.CatalogTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_catalog_template" not in self._stubs:
            self._stubs["get_catalog_template"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetCatalogTemplate",
                request_serializer=catalog_management_messages.GetCatalogTemplateRequest.serialize,
                response_deserializer=catalog_management.CatalogTemplate.deserialize,
            )
        return self._stubs["get_catalog_template"]

    @property
    def list_catalog_templates(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogTemplatesRequest],
        catalog_management_messages.ListCatalogTemplatesResponse,
    ]:
        r"""Return a callable for the list catalog templates method over gRPC.

        Lists catalog templates.

        Returns:
            Callable[[~.ListCatalogTemplatesRequest],
                    ~.ListCatalogTemplatesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_catalog_templates" not in self._stubs:
            self._stubs["list_catalog_templates"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ListCatalogTemplates",
                request_serializer=catalog_management_messages.ListCatalogTemplatesRequest.serialize,
                response_deserializer=catalog_management_messages.ListCatalogTemplatesResponse.deserialize,
            )
        return self._stubs["list_catalog_templates"]

    @property
    def update_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateCatalogTemplateRequest],
        catalog_management.CatalogTemplate,
    ]:
        r"""Return a callable for the update catalog template method over gRPC.

        Updates a catalog template resource.

        Returns:
            Callable[[~.UpdateCatalogTemplateRequest],
                    ~.CatalogTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_catalog_template" not in self._stubs:
            self._stubs["update_catalog_template"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/UpdateCatalogTemplate",
                request_serializer=catalog_management_messages.UpdateCatalogTemplateRequest.serialize,
                response_deserializer=catalog_management.CatalogTemplate.deserialize,
            )
        return self._stubs["update_catalog_template"]

    @property
    def delete_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogTemplateRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete catalog template method over gRPC.

        Deletes a catalog template.

        Returns:
            Callable[[~.DeleteCatalogTemplateRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_catalog_template" not in self._stubs:
            self._stubs["delete_catalog_template"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/DeleteCatalogTemplate",
                request_serializer=catalog_management_messages.DeleteCatalogTemplateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_catalog_template"]

    @property
    def create_share(
        self,
    ) -> Callable[[sharing_messages.CreateShareRequest], operations_pb2.Operation]:
        r"""Return a callable for the create share method over gRPC.

        Shares a catalog from one space to another space.

        Returns:
            Callable[[~.CreateShareRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_share" not in self._stubs:
            self._stubs["create_share"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/CreateShare",
                request_serializer=sharing_messages.CreateShareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_share"]

    @property
    def list_shares(
        self,
    ) -> Callable[
        [sharing_messages.ListSharesRequest], sharing_messages.ListSharesResponse
    ]:
        r"""Return a callable for the list shares method over gRPC.

        Lists catalog share objects for the space.

        Returns:
            Callable[[~.ListSharesRequest],
                    ~.ListSharesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_shares" not in self._stubs:
            self._stubs["list_shares"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ListShares",
                request_serializer=sharing_messages.ListSharesRequest.serialize,
                response_deserializer=sharing_messages.ListSharesResponse.deserialize,
            )
        return self._stubs["list_shares"]

    @property
    def get_share(self) -> Callable[[sharing_messages.GetShareRequest], sharing.Share]:
        r"""Return a callable for the get share method over gRPC.

        Get catalog share object for the space.

        Returns:
            Callable[[~.GetShareRequest],
                    ~.Share]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_share" not in self._stubs:
            self._stubs["get_share"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetShare",
                request_serializer=sharing_messages.GetShareRequest.serialize,
                response_deserializer=sharing.Share.deserialize,
            )
        return self._stubs["get_share"]

    @property
    def delete_share(
        self,
    ) -> Callable[[sharing_messages.DeleteShareRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete share method over gRPC.

        Deletes a catalog share.

        Returns:
            Callable[[~.DeleteShareRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_share" not in self._stubs:
            self._stubs["delete_share"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/DeleteShare",
                request_serializer=sharing_messages.DeleteShareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_share"]

    @property
    def sync_share(
        self,
    ) -> Callable[[sharing_messages.SyncShareRequest], operations_pb2.Operation]:
        r"""Return a callable for the sync share method over gRPC.

        Synchronizes a share and updates the destination
        workspace to reflect. reflect the most recent changes to
        the catalog.

        Returns:
            Callable[[~.SyncShareRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "sync_share" not in self._stubs:
            self._stubs["sync_share"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/SyncShare",
                request_serializer=sharing_messages.SyncShareRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["sync_share"]

    @property
    def get_shared_template(
        self,
    ) -> Callable[[sharing_messages.GetSharedTemplateRequest], sharing.SharedTemplate]:
        r"""Return a callable for the get shared template method over gRPC.

        Gets details about a shared template.

        Returns:
            Callable[[~.GetSharedTemplateRequest],
                    ~.SharedTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_shared_template" not in self._stubs:
            self._stubs["get_shared_template"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetSharedTemplate",
                request_serializer=sharing_messages.GetSharedTemplateRequest.serialize,
                response_deserializer=sharing.SharedTemplate.deserialize,
            )
        return self._stubs["get_shared_template"]

    @property
    def list_shared_templates(
        self,
    ) -> Callable[
        [sharing_messages.ListSharedTemplatesRequest],
        sharing_messages.ListSharedTemplatesResponse,
    ]:
        r"""Return a callable for the list shared templates method over gRPC.

        Lists shared templates in a given space.

        Returns:
            Callable[[~.ListSharedTemplatesRequest],
                    ~.ListSharedTemplatesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_shared_templates" not in self._stubs:
            self._stubs["list_shared_templates"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ListSharedTemplates",
                request_serializer=sharing_messages.ListSharedTemplatesRequest.serialize,
                response_deserializer=sharing_messages.ListSharedTemplatesResponse.deserialize,
            )
        return self._stubs["list_shared_templates"]

    @property
    def get_shared_template_revision(
        self,
    ) -> Callable[
        [sharing_messages.GetSharedTemplateRevisionRequest],
        sharing.SharedTemplateRevision,
    ]:
        r"""Return a callable for the get shared template revision method over gRPC.

        Gets details about a shared template revision.

        Returns:
            Callable[[~.GetSharedTemplateRevisionRequest],
                    ~.SharedTemplateRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_shared_template_revision" not in self._stubs:
            self._stubs["get_shared_template_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GetSharedTemplateRevision",
                    request_serializer=sharing_messages.GetSharedTemplateRevisionRequest.serialize,
                    response_deserializer=sharing.SharedTemplateRevision.deserialize,
                )
            )
        return self._stubs["get_shared_template_revision"]

    @property
    def list_shared_template_revisions(
        self,
    ) -> Callable[
        [sharing_messages.ListSharedTemplateRevisionsRequest],
        sharing_messages.ListSharedTemplateRevisionsResponse,
    ]:
        r"""Return a callable for the list shared template revisions method over gRPC.

        Lists shared template revisions in a given space.

        Returns:
            Callable[[~.ListSharedTemplateRevisionsRequest],
                    ~.ListSharedTemplateRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_shared_template_revisions" not in self._stubs:
            self._stubs["list_shared_template_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ListSharedTemplateRevisions",
                    request_serializer=sharing_messages.ListSharedTemplateRevisionsRequest.serialize,
                    response_deserializer=sharing_messages.ListSharedTemplateRevisionsResponse.deserialize,
                )
            )
        return self._stubs["list_shared_template_revisions"]

    @property
    def create_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogTemplateRevisionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create catalog template
        revision method over gRPC.

        Creates a template revision.

        Returns:
            Callable[[~.CreateCatalogTemplateRevisionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_catalog_template_revision" not in self._stubs:
            self._stubs["create_catalog_template_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/CreateCatalogTemplateRevision",
                    request_serializer=catalog_management_messages.CreateCatalogTemplateRevisionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_catalog_template_revision"]

    @property
    def get_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogTemplateRevisionRequest],
        catalog_management.CatalogTemplateRevision,
    ]:
        r"""Return a callable for the get catalog template revision method over gRPC.

        Gets details about a template revision.

        Returns:
            Callable[[~.GetCatalogTemplateRevisionRequest],
                    ~.CatalogTemplateRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_catalog_template_revision" not in self._stubs:
            self._stubs["get_catalog_template_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GetCatalogTemplateRevision",
                    request_serializer=catalog_management_messages.GetCatalogTemplateRevisionRequest.serialize,
                    response_deserializer=catalog_management.CatalogTemplateRevision.deserialize,
                )
            )
        return self._stubs["get_catalog_template_revision"]

    @property
    def list_catalog_template_revisions(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogTemplateRevisionsRequest],
        catalog_management_messages.ListCatalogTemplateRevisionsResponse,
    ]:
        r"""Return a callable for the list catalog template
        revisions method over gRPC.

        Lists template revisions.

        Returns:
            Callable[[~.ListCatalogTemplateRevisionsRequest],
                    ~.ListCatalogTemplateRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_catalog_template_revisions" not in self._stubs:
            self._stubs["list_catalog_template_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ListCatalogTemplateRevisions",
                    request_serializer=catalog_management_messages.ListCatalogTemplateRevisionsRequest.serialize,
                    response_deserializer=catalog_management_messages.ListCatalogTemplateRevisionsResponse.deserialize,
                )
            )
        return self._stubs["list_catalog_template_revisions"]

    @property
    def delete_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogTemplateRevisionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete catalog template
        revision method over gRPC.

        Deletes a template revision.

        Returns:
            Callable[[~.DeleteCatalogTemplateRevisionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_catalog_template_revision" not in self._stubs:
            self._stubs["delete_catalog_template_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/DeleteCatalogTemplateRevision",
                    request_serializer=catalog_management_messages.DeleteCatalogTemplateRevisionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_catalog_template_revision"]

    @property
    def create_application(
        self,
    ) -> Callable[
        [deployment_messages.CreateApplicationRequest], deployment_resources.Application
    ]:
        r"""Return a callable for the create application method over gRPC.

        Creates an application.

        Returns:
            Callable[[~.CreateApplicationRequest],
                    ~.Application]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_application" not in self._stubs:
            self._stubs["create_application"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/CreateApplication",
                request_serializer=deployment_messages.CreateApplicationRequest.serialize,
                response_deserializer=deployment_resources.Application.deserialize,
            )
        return self._stubs["create_application"]

    @property
    def get_application(
        self,
    ) -> Callable[
        [deployment_messages.GetApplicationRequest], deployment_resources.Application
    ]:
        r"""Return a callable for the get application method over gRPC.

        Gets details about an application.

        Returns:
            Callable[[~.GetApplicationRequest],
                    ~.Application]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_application" not in self._stubs:
            self._stubs["get_application"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetApplication",
                request_serializer=deployment_messages.GetApplicationRequest.serialize,
                response_deserializer=deployment_resources.Application.deserialize,
            )
        return self._stubs["get_application"]

    @property
    def list_applications(
        self,
    ) -> Callable[
        [deployment_messages.ListApplicationsRequest],
        deployment_messages.ListApplicationsResponse,
    ]:
        r"""Return a callable for the list applications method over gRPC.

        Lists applications in a given space.

        Returns:
            Callable[[~.ListApplicationsRequest],
                    ~.ListApplicationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_applications" not in self._stubs:
            self._stubs["list_applications"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ListApplications",
                request_serializer=deployment_messages.ListApplicationsRequest.serialize,
                response_deserializer=deployment_messages.ListApplicationsResponse.deserialize,
            )
        return self._stubs["list_applications"]

    @property
    def update_application(
        self,
    ) -> Callable[
        [deployment_messages.UpdateApplicationRequest], deployment_resources.Application
    ]:
        r"""Return a callable for the update application method over gRPC.

        Updates an application.

        Returns:
            Callable[[~.UpdateApplicationRequest],
                    ~.Application]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_application" not in self._stubs:
            self._stubs["update_application"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/UpdateApplication",
                request_serializer=deployment_messages.UpdateApplicationRequest.serialize,
                response_deserializer=deployment_resources.Application.deserialize,
            )
        return self._stubs["update_application"]

    @property
    def delete_application(
        self,
    ) -> Callable[
        [deployment_messages.DeleteApplicationRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete application method over gRPC.

        Deletes an application.

        Returns:
            Callable[[~.DeleteApplicationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_application" not in self._stubs:
            self._stubs["delete_application"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/DeleteApplication",
                request_serializer=deployment_messages.DeleteApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_application"]

    @property
    def deploy_application(
        self,
    ) -> Callable[
        [deployment_messages.DeployApplicationRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the deploy application method over gRPC.

        Deploys an application.

        Returns:
            Callable[[~.DeployApplicationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_application" not in self._stubs:
            self._stubs["deploy_application"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/DeployApplication",
                request_serializer=deployment_messages.DeployApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["deploy_application"]

    @property
    def preview_application(
        self,
    ) -> Callable[
        [deployment_messages.PreviewApplicationRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the preview application method over gRPC.

        Previews deployment of an application.

        Returns:
            Callable[[~.PreviewApplicationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "preview_application" not in self._stubs:
            self._stubs["preview_application"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/PreviewApplication",
                request_serializer=deployment_messages.PreviewApplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["preview_application"]

    @property
    def fetch_application_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.FetchApplicationAssessmentReportRequest],
        best_practices_messages.FetchApplicationAssessmentReportResponse,
    ]:
        r"""Return a callable for the fetch application assessment
        report method over gRPC.

        Fetches the assessment report of a deployed
        application if present.

        Returns:
            Callable[[~.FetchApplicationAssessmentReportRequest],
                    ~.FetchApplicationAssessmentReportResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_application_assessment_report" not in self._stubs:
            self._stubs["fetch_application_assessment_report"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/FetchApplicationAssessmentReport",
                    request_serializer=best_practices_messages.FetchApplicationAssessmentReportRequest.serialize,
                    response_deserializer=best_practices_messages.FetchApplicationAssessmentReportResponse.deserialize,
                )
            )
        return self._stubs["fetch_application_assessment_report"]

    @property
    def generate_application_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateApplicationAssessmentReportRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the generate application
        assessment report method over gRPC.

        Generate Assessment Reports of an application.

        Returns:
            Callable[[~.GenerateApplicationAssessmentReportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_application_assessment_report" not in self._stubs:
            self._stubs["generate_application_assessment_report"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GenerateApplicationAssessmentReport",
                    request_serializer=best_practices_messages.GenerateApplicationAssessmentReportRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["generate_application_assessment_report"]

    @property
    def generate_application_template_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the generate application template
        assessment report method over gRPC.

        Generate Assessment Reports of an application
        template.

        Returns:
            Callable[[~.GenerateApplicationTemplateAssessmentReportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_application_template_assessment_report" not in self._stubs:
            self._stubs["generate_application_template_assessment_report"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GenerateApplicationTemplateAssessmentReport",
                    request_serializer=best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["generate_application_template_assessment_report"]

    @property
    def generate_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateAssessmentReportRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the generate assessment report method over gRPC.

        Deprecated: Use GenerateTerraformPlanAssessmentReport
        instead.
        Generate a best practice report for a given Terraform
        plan.

        Returns:
            Callable[[~.GenerateAssessmentReportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_assessment_report" not in self._stubs:
            self._stubs["generate_assessment_report"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GenerateAssessmentReport",
                    request_serializer=best_practices_messages.GenerateAssessmentReportRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["generate_assessment_report"]

    @property
    def generate_terraform_plan_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateTerraformPlanAssessmentReportRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the generate terraform plan
        assessment report method over gRPC.

        Generate a Terraform plan assessment report for a
        given Terraform plan.

        Returns:
            Callable[[~.GenerateTerraformPlanAssessmentReportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_terraform_plan_assessment_report" not in self._stubs:
            self._stubs["generate_terraform_plan_assessment_report"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GenerateTerraformPlanAssessmentReport",
                    request_serializer=best_practices_messages.GenerateTerraformPlanAssessmentReportRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["generate_terraform_plan_assessment_report"]

    @property
    def get_policy(
        self,
    ) -> Callable[[best_practices_messages.GetPolicyRequest], best_practices.Policy]:
        r"""Return a callable for the get policy method over gRPC.

        Policy related APIs.
        Get a policy for an application template.

        Returns:
            Callable[[~.GetPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_policy" not in self._stubs:
            self._stubs["get_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GetPolicy",
                request_serializer=best_practices_messages.GetPolicyRequest.serialize,
                response_deserializer=best_practices.Policy.deserialize,
            )
        return self._stubs["get_policy"]

    @property
    def list_policies(
        self,
    ) -> Callable[
        [best_practices_messages.ListPoliciesRequest],
        best_practices_messages.ListPoliciesResponse,
    ]:
        r"""Return a callable for the list policies method over gRPC.

        Lists policies for an application template.

        Returns:
            Callable[[~.ListPoliciesRequest],
                    ~.ListPoliciesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_policies" not in self._stubs:
            self._stubs["list_policies"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ListPolicies",
                request_serializer=best_practices_messages.ListPoliciesRequest.serialize,
                response_deserializer=best_practices_messages.ListPoliciesResponse.deserialize,
            )
        return self._stubs["list_policies"]

    @property
    def create_policy(
        self,
    ) -> Callable[[best_practices_messages.CreatePolicyRequest], best_practices.Policy]:
        r"""Return a callable for the create policy method over gRPC.

        Creates a policy for an application template.

        Returns:
            Callable[[~.CreatePolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_policy" not in self._stubs:
            self._stubs["create_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/CreatePolicy",
                request_serializer=best_practices_messages.CreatePolicyRequest.serialize,
                response_deserializer=best_practices.Policy.deserialize,
            )
        return self._stubs["create_policy"]

    @property
    def update_policy(
        self,
    ) -> Callable[[best_practices_messages.UpdatePolicyRequest], best_practices.Policy]:
        r"""Return a callable for the update policy method over gRPC.

        Updates a policy.

        Returns:
            Callable[[~.UpdatePolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_policy" not in self._stubs:
            self._stubs["update_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/UpdatePolicy",
                request_serializer=best_practices_messages.UpdatePolicyRequest.serialize,
                response_deserializer=best_practices.Policy.deserialize,
            )
        return self._stubs["update_policy"]

    @property
    def delete_policy(
        self,
    ) -> Callable[[best_practices_messages.DeletePolicyRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete policy method over gRPC.

        Deletes a policy.

        Returns:
            Callable[[~.DeletePolicyRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_policy" not in self._stubs:
            self._stubs["delete_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/DeletePolicy",
                request_serializer=best_practices_messages.DeletePolicyRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_policy"]

    @property
    def fetch_frameworks(
        self,
    ) -> Callable[
        [best_practices_messages.FetchFrameworksRequest],
        best_practices_messages.FetchFrameworksResponse,
    ]:
        r"""Return a callable for the fetch frameworks method over gRPC.

        Fetches all frameworks for assessment report.

        Returns:
            Callable[[~.FetchFrameworksRequest],
                    ~.FetchFrameworksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_frameworks" not in self._stubs:
            self._stubs["fetch_frameworks"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/FetchFrameworks",
                request_serializer=best_practices_messages.FetchFrameworksRequest.serialize,
                response_deserializer=best_practices_messages.FetchFrameworksResponse.deserialize,
            )
        return self._stubs["fetch_frameworks"]

    @property
    def generate_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.GenerateApplicationIaCRequest],
        deployment_messages.GenerateApplicationIaCResponse,
    ]:
        r"""Return a callable for the generate application ia c method over gRPC.

        Generates Terraform files for an application.

        Returns:
            Callable[[~.GenerateApplicationIaCRequest],
                    ~.GenerateApplicationIaCResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_application_ia_c" not in self._stubs:
            self._stubs["generate_application_ia_c"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/GenerateApplicationIaC",
                request_serializer=deployment_messages.GenerateApplicationIaCRequest.serialize,
                response_deserializer=deployment_messages.GenerateApplicationIaCResponse.deserialize,
            )
        return self._stubs["generate_application_ia_c"]

    @property
    def export_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.ExportApplicationIaCRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the export application ia c method over gRPC.

        Exports Terraform files for an application
        asynchronously.

        Returns:
            Callable[[~.ExportApplicationIaCRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_application_ia_c" not in self._stubs:
            self._stubs["export_application_ia_c"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ExportApplicationIaC",
                request_serializer=deployment_messages.ExportApplicationIaCRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_application_ia_c"]

    @property
    def import_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ImportApplicationTemplateIaCRequest],
        authoring_messages.ImportApplicationTemplateIaCResponse,
    ]:
        r"""Return a callable for the import application template ia
        c method over gRPC.

        Imports IaC for an application template.

        Returns:
            Callable[[~.ImportApplicationTemplateIaCRequest],
                    ~.ImportApplicationTemplateIaCResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_application_template_ia_c" not in self._stubs:
            self._stubs["import_application_template_ia_c"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ImportApplicationTemplateIaC",
                    request_serializer=authoring_messages.ImportApplicationTemplateIaCRequest.serialize,
                    response_deserializer=authoring_messages.ImportApplicationTemplateIaCResponse.deserialize,
                )
            )
        return self._stubs["import_application_template_ia_c"]

    @property
    def ingest_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.IngestApplicationTemplateIaCRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the ingest application template ia
        c method over gRPC.

        Ingests IaC for an application template
        asynchronously.

        Returns:
            Callable[[~.IngestApplicationTemplateIaCRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "ingest_application_template_ia_c" not in self._stubs:
            self._stubs["ingest_application_template_ia_c"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/IngestApplicationTemplateIaC",
                    request_serializer=authoring_messages.IngestApplicationTemplateIaCRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["ingest_application_template_ia_c"]

    @property
    def import_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.ImportApplicationIaCRequest],
        deployment_messages.ImportApplicationIaCResponse,
    ]:
        r"""Return a callable for the import application ia c method over gRPC.

        Imports IaC for an application resource.

        Returns:
            Callable[[~.ImportApplicationIaCRequest],
                    ~.ImportApplicationIaCResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_application_ia_c" not in self._stubs:
            self._stubs["import_application_ia_c"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/ImportApplicationIaC",
                request_serializer=deployment_messages.ImportApplicationIaCRequest.serialize,
                response_deserializer=deployment_messages.ImportApplicationIaCResponse.deserialize,
            )
        return self._stubs["import_application_ia_c"]

    @property
    def register_app_hub_application_resources(
        self,
    ) -> Callable[
        [apphub_integration_messages.RegisterAppHubApplicationResourcesRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the register app hub application
        resources method over gRPC.

        Register deployed resources from terraform state file
        with App Hub without needing a space.

        Returns:
            Callable[[~.RegisterAppHubApplicationResourcesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "register_app_hub_application_resources" not in self._stubs:
            self._stubs["register_app_hub_application_resources"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/RegisterAppHubApplicationResources",
                    request_serializer=apphub_integration_messages.RegisterAppHubApplicationResourcesRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["register_app_hub_application_resources"]

    @property
    def list_application_template_system_revisions(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplateSystemRevisionsRequest],
        authoring_messages.ListApplicationTemplateSystemRevisionsResponse,
    ]:
        r"""Return a callable for the list application template
        system revisions method over gRPC.

        Lists application template system revisions in a
        given application template.

        Returns:
            Callable[[~.ListApplicationTemplateSystemRevisionsRequest],
                    ~.ListApplicationTemplateSystemRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_application_template_system_revisions" not in self._stubs:
            self._stubs["list_application_template_system_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/ListApplicationTemplateSystemRevisions",
                    request_serializer=authoring_messages.ListApplicationTemplateSystemRevisionsRequest.serialize,
                    response_deserializer=authoring_messages.ListApplicationTemplateSystemRevisionsResponse.deserialize,
                )
            )
        return self._stubs["list_application_template_system_revisions"]

    @property
    def get_application_template_system_revision(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateSystemRevisionRequest],
        authoring.ApplicationTemplateSystemRevision,
    ]:
        r"""Return a callable for the get application template
        system revision method over gRPC.

        Gets the given application template system revision.

        Returns:
            Callable[[~.GetApplicationTemplateSystemRevisionRequest],
                    ~.ApplicationTemplateSystemRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_application_template_system_revision" not in self._stubs:
            self._stubs["get_application_template_system_revision"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.designcenter.v1.DesignCenter/GetApplicationTemplateSystemRevision",
                    request_serializer=authoring_messages.GetApplicationTemplateSystemRevisionRequest.serialize,
                    response_deserializer=authoring.ApplicationTemplateSystemRevision.deserialize,
                )
            )
        return self._stubs["get_application_template_system_revision"]

    @property
    def recommend_iam_roles(
        self,
    ) -> Callable[
        [deployment_messages.RecommendIAMRolesRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the recommend iam roles method over gRPC.

        Gets recommended IAM roles for an application.

        Evaluates the infrastructure resources defined by an application
        (including its template configuration and parameters) to
        determine the set of IAM roles and Google Cloud APIs that you
        must configure before you deploy across target projects.

        The operation is asynchronous and returns a
        ``google.longrunning.Operation``. Upon completion, the operation
        result contains a ``RecommendIAMRolesResponse`` with
        project-level IAM role and API recommendations.

        Returns:
            Callable[[~.RecommendIAMRolesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "recommend_iam_roles" not in self._stubs:
            self._stubs["recommend_iam_roles"] = self._logged_channel.unary_unary(
                "/google.cloud.designcenter.v1.DesignCenter/RecommendIAMRoles",
                request_serializer=deployment_messages.RecommendIAMRolesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["recommend_iam_roles"]

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

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("DesignCenterGrpcTransport",)
