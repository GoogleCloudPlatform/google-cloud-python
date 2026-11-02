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

from google.cloud.apihub_v1.types import apihub_service, common_fields

from .base import DEFAULT_CLIENT_INFO, ApiHubTransport

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
                    "serviceName": "google.cloud.apihub.v1.ApiHub",
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
                    "serviceName": "google.cloud.apihub.v1.ApiHub",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ApiHubGrpcTransport(ApiHubTransport):
    """gRPC backend transport for ApiHub.

    This service provides all methods related to the API hub.

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
        host: str = "apihub.googleapis.com",
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
                 The hostname to connect to (default: 'apihub.googleapis.com').
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
        host: str = "apihub.googleapis.com",
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
    def create_api(
        self,
    ) -> Callable[[apihub_service.CreateApiRequest], common_fields.Api]:
        r"""Return a callable for the create api method over gRPC.

        Create an API resource in the API hub.
        Once an API resource is created, versions can be added
        to it.

        Returns:
            Callable[[~.CreateApiRequest],
                    ~.Api]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_api" not in self._stubs:
            self._stubs["create_api"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/CreateApi",
                request_serializer=apihub_service.CreateApiRequest.serialize,
                response_deserializer=common_fields.Api.deserialize,
            )
        return self._stubs["create_api"]

    @property
    def get_api(self) -> Callable[[apihub_service.GetApiRequest], common_fields.Api]:
        r"""Return a callable for the get api method over gRPC.

        Get API resource details including the API versions
        contained in it.

        Returns:
            Callable[[~.GetApiRequest],
                    ~.Api]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_api" not in self._stubs:
            self._stubs["get_api"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetApi",
                request_serializer=apihub_service.GetApiRequest.serialize,
                response_deserializer=common_fields.Api.deserialize,
            )
        return self._stubs["get_api"]

    @property
    def list_apis(
        self,
    ) -> Callable[[apihub_service.ListApisRequest], apihub_service.ListApisResponse]:
        r"""Return a callable for the list apis method over gRPC.

        List API resources in the API hub.

        Returns:
            Callable[[~.ListApisRequest],
                    ~.ListApisResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_apis" not in self._stubs:
            self._stubs["list_apis"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/ListApis",
                request_serializer=apihub_service.ListApisRequest.serialize,
                response_deserializer=apihub_service.ListApisResponse.deserialize,
            )
        return self._stubs["list_apis"]

    @property
    def update_api(
        self,
    ) -> Callable[[apihub_service.UpdateApiRequest], common_fields.Api]:
        r"""Return a callable for the update api method over gRPC.

        Update an API resource in the API hub. The following fields in
        the [API][google.cloud.apihub.v1.Api] can be updated:

        - [display_name][google.cloud.apihub.v1.Api.display_name]
        - [description][google.cloud.apihub.v1.Api.description]
        - [owner][google.cloud.apihub.v1.Api.owner]
        - [documentation][google.cloud.apihub.v1.Api.documentation]
        - [target_user][google.cloud.apihub.v1.Api.target_user]
        - [team][google.cloud.apihub.v1.Api.team]
        - [business_unit][google.cloud.apihub.v1.Api.business_unit]
        - [maturity_level][google.cloud.apihub.v1.Api.maturity_level]
        - [api_style][google.cloud.apihub.v1.Api.api_style]
        - [attributes][google.cloud.apihub.v1.Api.attributes]

        The
        [update_mask][google.cloud.apihub.v1.UpdateApiRequest.update_mask]
        should be used to specify the fields being updated.

        Updating the owner field requires complete owner message and
        updates both owner and email fields.

        Returns:
            Callable[[~.UpdateApiRequest],
                    ~.Api]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_api" not in self._stubs:
            self._stubs["update_api"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/UpdateApi",
                request_serializer=apihub_service.UpdateApiRequest.serialize,
                response_deserializer=common_fields.Api.deserialize,
            )
        return self._stubs["update_api"]

    @property
    def delete_api(
        self,
    ) -> Callable[[apihub_service.DeleteApiRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete api method over gRPC.

        Delete an API resource in the API hub. API can only
        be deleted if all underlying versions are deleted.

        Returns:
            Callable[[~.DeleteApiRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_api" not in self._stubs:
            self._stubs["delete_api"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/DeleteApi",
                request_serializer=apihub_service.DeleteApiRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_api"]

    @property
    def create_version(
        self,
    ) -> Callable[[apihub_service.CreateVersionRequest], common_fields.Version]:
        r"""Return a callable for the create version method over gRPC.

        Create an API version for an API resource in the API
        hub.

        Returns:
            Callable[[~.CreateVersionRequest],
                    ~.Version]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_version" not in self._stubs:
            self._stubs["create_version"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/CreateVersion",
                request_serializer=apihub_service.CreateVersionRequest.serialize,
                response_deserializer=common_fields.Version.deserialize,
            )
        return self._stubs["create_version"]

    @property
    def get_version(
        self,
    ) -> Callable[[apihub_service.GetVersionRequest], common_fields.Version]:
        r"""Return a callable for the get version method over gRPC.

        Get details about the API version of an API resource.
        This will include information about the specs and
        operations present in the API version as well as the
        deployments linked to it.

        Returns:
            Callable[[~.GetVersionRequest],
                    ~.Version]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_version" not in self._stubs:
            self._stubs["get_version"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetVersion",
                request_serializer=apihub_service.GetVersionRequest.serialize,
                response_deserializer=common_fields.Version.deserialize,
            )
        return self._stubs["get_version"]

    @property
    def list_versions(
        self,
    ) -> Callable[
        [apihub_service.ListVersionsRequest], apihub_service.ListVersionsResponse
    ]:
        r"""Return a callable for the list versions method over gRPC.

        List API versions of an API resource in the API hub.

        Returns:
            Callable[[~.ListVersionsRequest],
                    ~.ListVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_versions" not in self._stubs:
            self._stubs["list_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/ListVersions",
                request_serializer=apihub_service.ListVersionsRequest.serialize,
                response_deserializer=apihub_service.ListVersionsResponse.deserialize,
            )
        return self._stubs["list_versions"]

    @property
    def update_version(
        self,
    ) -> Callable[[apihub_service.UpdateVersionRequest], common_fields.Version]:
        r"""Return a callable for the update version method over gRPC.

        Update API version. The following fields in the
        [version][google.cloud.apihub.v1.Version] can be updated
        currently:

        - [display_name][google.cloud.apihub.v1.Version.display_name]
        - [description][google.cloud.apihub.v1.Version.description]
        - [documentation][google.cloud.apihub.v1.Version.documentation]
        - [deployments][google.cloud.apihub.v1.Version.deployments]
        - [lifecycle][google.cloud.apihub.v1.Version.lifecycle]
        - [compliance][google.cloud.apihub.v1.Version.compliance]
        - [accreditation][google.cloud.apihub.v1.Version.accreditation]
        - [attributes][google.cloud.apihub.v1.Version.attributes]

        The
        [update_mask][google.cloud.apihub.v1.UpdateVersionRequest.update_mask]
        should be used to specify the fields being updated.

        Returns:
            Callable[[~.UpdateVersionRequest],
                    ~.Version]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_version" not in self._stubs:
            self._stubs["update_version"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/UpdateVersion",
                request_serializer=apihub_service.UpdateVersionRequest.serialize,
                response_deserializer=common_fields.Version.deserialize,
            )
        return self._stubs["update_version"]

    @property
    def delete_version(
        self,
    ) -> Callable[[apihub_service.DeleteVersionRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete version method over gRPC.

        Delete an API version. Version can only be deleted if
        all underlying specs, operations, definitions and linked
        deployments are deleted.

        Returns:
            Callable[[~.DeleteVersionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_version" not in self._stubs:
            self._stubs["delete_version"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/DeleteVersion",
                request_serializer=apihub_service.DeleteVersionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_version"]

    @property
    def create_spec(
        self,
    ) -> Callable[[apihub_service.CreateSpecRequest], common_fields.Spec]:
        r"""Return a callable for the create spec method over gRPC.

        Add a spec to an API version in the API hub. Multiple specs can
        be added to an API version. Note, while adding a spec, at least
        one of ``contents`` or ``source_uri`` must be provided. If
        ``contents`` is provided, then ``spec_type`` must also be
        provided.

        On adding a spec with contents to the version, the operations
        present in it will be added to the version.Note that the file
        contents in the spec should be of the same type as defined in
        the
        ``projects/{project}/locations/{location}/attributes/system-spec-type``
        attribute associated with spec resource. Note that specs of
        various types can be uploaded, however parsing of details is
        supported for OpenAPI spec currently.

        In order to access the information parsed from the spec, use the
        [GetSpec][google.cloud.apihub.v1.ApiHub.GetSpec] method. In
        order to access the raw contents for a particular spec, use the
        [GetSpecContents][google.cloud.apihub.v1.ApiHub.GetSpecContents]
        method. In order to access the operations parsed from the spec,
        use the
        [ListAPIOperations][google.cloud.apihub.v1.ApiHub.ListApiOperations]
        method.

        Returns:
            Callable[[~.CreateSpecRequest],
                    ~.Spec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_spec" not in self._stubs:
            self._stubs["create_spec"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/CreateSpec",
                request_serializer=apihub_service.CreateSpecRequest.serialize,
                response_deserializer=common_fields.Spec.deserialize,
            )
        return self._stubs["create_spec"]

    @property
    def get_spec(self) -> Callable[[apihub_service.GetSpecRequest], common_fields.Spec]:
        r"""Return a callable for the get spec method over gRPC.

        Get details about the information parsed from a spec. Note that
        this method does not return the raw spec contents. Use
        [GetSpecContents][google.cloud.apihub.v1.ApiHub.GetSpecContents]
        method to retrieve the same.

        Returns:
            Callable[[~.GetSpecRequest],
                    ~.Spec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_spec" not in self._stubs:
            self._stubs["get_spec"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetSpec",
                request_serializer=apihub_service.GetSpecRequest.serialize,
                response_deserializer=common_fields.Spec.deserialize,
            )
        return self._stubs["get_spec"]

    @property
    def get_spec_contents(
        self,
    ) -> Callable[[apihub_service.GetSpecContentsRequest], common_fields.SpecContents]:
        r"""Return a callable for the get spec contents method over gRPC.

        Get spec contents.

        Returns:
            Callable[[~.GetSpecContentsRequest],
                    ~.SpecContents]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_spec_contents" not in self._stubs:
            self._stubs["get_spec_contents"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetSpecContents",
                request_serializer=apihub_service.GetSpecContentsRequest.serialize,
                response_deserializer=common_fields.SpecContents.deserialize,
            )
        return self._stubs["get_spec_contents"]

    @property
    def list_specs(
        self,
    ) -> Callable[[apihub_service.ListSpecsRequest], apihub_service.ListSpecsResponse]:
        r"""Return a callable for the list specs method over gRPC.

        List specs corresponding to a particular API
        resource.

        Returns:
            Callable[[~.ListSpecsRequest],
                    ~.ListSpecsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_specs" not in self._stubs:
            self._stubs["list_specs"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/ListSpecs",
                request_serializer=apihub_service.ListSpecsRequest.serialize,
                response_deserializer=apihub_service.ListSpecsResponse.deserialize,
            )
        return self._stubs["list_specs"]

    @property
    def update_spec(
        self,
    ) -> Callable[[apihub_service.UpdateSpecRequest], common_fields.Spec]:
        r"""Return a callable for the update spec method over gRPC.

        Update spec. The following fields in the
        [spec][google.cloud.apihub.v1.Spec] can be updated:

        - [display_name][google.cloud.apihub.v1.Spec.display_name]
        - [source_uri][google.cloud.apihub.v1.Spec.source_uri]
        - [lint_response][google.cloud.apihub.v1.Spec.lint_response]
        - [attributes][google.cloud.apihub.v1.Spec.attributes]
        - [contents][google.cloud.apihub.v1.Spec.contents]
        - [spec_type][google.cloud.apihub.v1.Spec.spec_type]

        In case of an OAS spec, updating spec contents can lead to:

        1. Creation, deletion and update of operations.
        2. Creation, deletion and update of definitions.
        3. Update of other info parsed out from the new spec.

        In case of contents or source_uri being present in update mask,
        spec_type must also be present. Also, spec_type can not be
        present in update mask if contents or source_uri is not present.

        The
        [update_mask][google.cloud.apihub.v1.UpdateSpecRequest.update_mask]
        should be used to specify the fields being updated.

        Returns:
            Callable[[~.UpdateSpecRequest],
                    ~.Spec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_spec" not in self._stubs:
            self._stubs["update_spec"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/UpdateSpec",
                request_serializer=apihub_service.UpdateSpecRequest.serialize,
                response_deserializer=common_fields.Spec.deserialize,
            )
        return self._stubs["update_spec"]

    @property
    def delete_spec(
        self,
    ) -> Callable[[apihub_service.DeleteSpecRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete spec method over gRPC.

        Delete a spec.
        Deleting a spec will also delete the associated
        operations from the version.

        Returns:
            Callable[[~.DeleteSpecRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_spec" not in self._stubs:
            self._stubs["delete_spec"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/DeleteSpec",
                request_serializer=apihub_service.DeleteSpecRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_spec"]

    @property
    def create_api_operation(
        self,
    ) -> Callable[
        [apihub_service.CreateApiOperationRequest], common_fields.ApiOperation
    ]:
        r"""Return a callable for the create api operation method over gRPC.

        Create an apiOperation in an API version.
        An apiOperation can be created only if the version has
        no apiOperations which were created by parsing a spec.

        Returns:
            Callable[[~.CreateApiOperationRequest],
                    ~.ApiOperation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_api_operation" not in self._stubs:
            self._stubs["create_api_operation"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/CreateApiOperation",
                request_serializer=apihub_service.CreateApiOperationRequest.serialize,
                response_deserializer=common_fields.ApiOperation.deserialize,
            )
        return self._stubs["create_api_operation"]

    @property
    def get_api_operation(
        self,
    ) -> Callable[[apihub_service.GetApiOperationRequest], common_fields.ApiOperation]:
        r"""Return a callable for the get api operation method over gRPC.

        Get details about a particular operation in API
        version.

        Returns:
            Callable[[~.GetApiOperationRequest],
                    ~.ApiOperation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_api_operation" not in self._stubs:
            self._stubs["get_api_operation"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetApiOperation",
                request_serializer=apihub_service.GetApiOperationRequest.serialize,
                response_deserializer=common_fields.ApiOperation.deserialize,
            )
        return self._stubs["get_api_operation"]

    @property
    def list_api_operations(
        self,
    ) -> Callable[
        [apihub_service.ListApiOperationsRequest],
        apihub_service.ListApiOperationsResponse,
    ]:
        r"""Return a callable for the list api operations method over gRPC.

        List operations in an API version.

        Returns:
            Callable[[~.ListApiOperationsRequest],
                    ~.ListApiOperationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_api_operations" not in self._stubs:
            self._stubs["list_api_operations"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/ListApiOperations",
                request_serializer=apihub_service.ListApiOperationsRequest.serialize,
                response_deserializer=apihub_service.ListApiOperationsResponse.deserialize,
            )
        return self._stubs["list_api_operations"]

    @property
    def update_api_operation(
        self,
    ) -> Callable[
        [apihub_service.UpdateApiOperationRequest], common_fields.ApiOperation
    ]:
        r"""Return a callable for the update api operation method over gRPC.

        Update an operation in an API version. The following fields in
        the [ApiOperation resource][google.cloud.apihub.v1.ApiOperation]
        can be updated:

        - [details.description][ApiOperation.details.description]
        - [details.documentation][ApiOperation.details.documentation]
        - [details.http_operation.path][ApiOperation.details.http_operation.path.path]
        - [details.http_operation.method][ApiOperation.details.http_operation.method]
        - [details.deprecated][ApiOperation.details.deprecated]
        - [attributes][google.cloud.apihub.v1.ApiOperation.attributes]

        The
        [update_mask][google.cloud.apihub.v1.UpdateApiOperationRequest.update_mask]
        should be used to specify the fields being updated.

        An operation can be updated only if the operation was created
        via
        [CreateApiOperation][google.cloud.apihub.v1.ApiHub.CreateApiOperation]
        API. If the operation was created by parsing the spec, then it
        can be edited by updating the spec.

        Returns:
            Callable[[~.UpdateApiOperationRequest],
                    ~.ApiOperation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_api_operation" not in self._stubs:
            self._stubs["update_api_operation"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/UpdateApiOperation",
                request_serializer=apihub_service.UpdateApiOperationRequest.serialize,
                response_deserializer=common_fields.ApiOperation.deserialize,
            )
        return self._stubs["update_api_operation"]

    @property
    def delete_api_operation(
        self,
    ) -> Callable[[apihub_service.DeleteApiOperationRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete api operation method over gRPC.

        Delete an operation in an API version and we can
        delete only the operations created via create API. If
        the operation was created by parsing the spec, then it
        can be deleted by editing or deleting the spec.

        Returns:
            Callable[[~.DeleteApiOperationRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_api_operation" not in self._stubs:
            self._stubs["delete_api_operation"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/DeleteApiOperation",
                request_serializer=apihub_service.DeleteApiOperationRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_api_operation"]

    @property
    def get_definition(
        self,
    ) -> Callable[[apihub_service.GetDefinitionRequest], common_fields.Definition]:
        r"""Return a callable for the get definition method over gRPC.

        Get details about a definition in an API version.

        Returns:
            Callable[[~.GetDefinitionRequest],
                    ~.Definition]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_definition" not in self._stubs:
            self._stubs["get_definition"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetDefinition",
                request_serializer=apihub_service.GetDefinitionRequest.serialize,
                response_deserializer=common_fields.Definition.deserialize,
            )
        return self._stubs["get_definition"]

    @property
    def create_deployment(
        self,
    ) -> Callable[[apihub_service.CreateDeploymentRequest], common_fields.Deployment]:
        r"""Return a callable for the create deployment method over gRPC.

        Create a deployment resource in the API hub.
        Once a deployment resource is created, it can be
        associated with API versions.

        Returns:
            Callable[[~.CreateDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_deployment" not in self._stubs:
            self._stubs["create_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/CreateDeployment",
                request_serializer=apihub_service.CreateDeploymentRequest.serialize,
                response_deserializer=common_fields.Deployment.deserialize,
            )
        return self._stubs["create_deployment"]

    @property
    def get_deployment(
        self,
    ) -> Callable[[apihub_service.GetDeploymentRequest], common_fields.Deployment]:
        r"""Return a callable for the get deployment method over gRPC.

        Get details about a deployment and the API versions
        linked to it.

        Returns:
            Callable[[~.GetDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deployment" not in self._stubs:
            self._stubs["get_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetDeployment",
                request_serializer=apihub_service.GetDeploymentRequest.serialize,
                response_deserializer=common_fields.Deployment.deserialize,
            )
        return self._stubs["get_deployment"]

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [apihub_service.ListDeploymentsRequest], apihub_service.ListDeploymentsResponse
    ]:
        r"""Return a callable for the list deployments method over gRPC.

        List deployment resources in the API hub.

        Returns:
            Callable[[~.ListDeploymentsRequest],
                    ~.ListDeploymentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deployments" not in self._stubs:
            self._stubs["list_deployments"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/ListDeployments",
                request_serializer=apihub_service.ListDeploymentsRequest.serialize,
                response_deserializer=apihub_service.ListDeploymentsResponse.deserialize,
            )
        return self._stubs["list_deployments"]

    @property
    def update_deployment(
        self,
    ) -> Callable[[apihub_service.UpdateDeploymentRequest], common_fields.Deployment]:
        r"""Return a callable for the update deployment method over gRPC.

        Update a deployment resource in the API hub. The following
        fields in the [deployment
        resource][google.cloud.apihub.v1.Deployment] can be updated:

        - [display_name][google.cloud.apihub.v1.Deployment.display_name]
        - [description][google.cloud.apihub.v1.Deployment.description]
        - [documentation][google.cloud.apihub.v1.Deployment.documentation]
        - [deployment_type][google.cloud.apihub.v1.Deployment.deployment_type]
        - [resource_uri][google.cloud.apihub.v1.Deployment.resource_uri]
        - [endpoints][google.cloud.apihub.v1.Deployment.endpoints]
        - [slo][google.cloud.apihub.v1.Deployment.slo]
        - [environment][google.cloud.apihub.v1.Deployment.environment]
        - [attributes][google.cloud.apihub.v1.Deployment.attributes]
        - [source_project]
          [google.cloud.apihub.v1.Deployment.source_project]
        - [source_environment]
          [google.cloud.apihub.v1.Deployment.source_environment]
        - [management_url][google.cloud.apihub.v1.Deployment.management_url]
        - [source_uri][google.cloud.apihub.v1.Deployment.source_uri] The
          [update_mask][google.cloud.apihub.v1.UpdateDeploymentRequest.update_mask]
          should be used to specify the fields being updated.

        Returns:
            Callable[[~.UpdateDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_deployment" not in self._stubs:
            self._stubs["update_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/UpdateDeployment",
                request_serializer=apihub_service.UpdateDeploymentRequest.serialize,
                response_deserializer=common_fields.Deployment.deserialize,
            )
        return self._stubs["update_deployment"]

    @property
    def delete_deployment(
        self,
    ) -> Callable[[apihub_service.DeleteDeploymentRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete deployment method over gRPC.

        Delete a deployment resource in the API hub.

        Returns:
            Callable[[~.DeleteDeploymentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_deployment" not in self._stubs:
            self._stubs["delete_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/DeleteDeployment",
                request_serializer=apihub_service.DeleteDeploymentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_deployment"]

    @property
    def create_attribute(
        self,
    ) -> Callable[[apihub_service.CreateAttributeRequest], common_fields.Attribute]:
        r"""Return a callable for the create attribute method over gRPC.

        Create a user defined attribute.

        Certain pre defined attributes are already created by the API
        hub. These attributes will have type as ``SYSTEM_DEFINED`` and
        can be listed via
        [ListAttributes][google.cloud.apihub.v1.ApiHub.ListAttributes]
        method. Allowed values for the same can be updated via
        [UpdateAttribute][google.cloud.apihub.v1.ApiHub.UpdateAttribute]
        method.

        Returns:
            Callable[[~.CreateAttributeRequest],
                    ~.Attribute]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_attribute" not in self._stubs:
            self._stubs["create_attribute"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/CreateAttribute",
                request_serializer=apihub_service.CreateAttributeRequest.serialize,
                response_deserializer=common_fields.Attribute.deserialize,
            )
        return self._stubs["create_attribute"]

    @property
    def get_attribute(
        self,
    ) -> Callable[[apihub_service.GetAttributeRequest], common_fields.Attribute]:
        r"""Return a callable for the get attribute method over gRPC.

        Get details about the attribute.

        Returns:
            Callable[[~.GetAttributeRequest],
                    ~.Attribute]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_attribute" not in self._stubs:
            self._stubs["get_attribute"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetAttribute",
                request_serializer=apihub_service.GetAttributeRequest.serialize,
                response_deserializer=common_fields.Attribute.deserialize,
            )
        return self._stubs["get_attribute"]

    @property
    def update_attribute(
        self,
    ) -> Callable[[apihub_service.UpdateAttributeRequest], common_fields.Attribute]:
        r"""Return a callable for the update attribute method over gRPC.

        Update the attribute. The following fields in the [Attribute
        resource][google.cloud.apihub.v1.Attribute] can be updated:

        - [display_name][google.cloud.apihub.v1.Attribute.display_name]
          The display name can be updated for user defined attributes
          only.
        - [description][google.cloud.apihub.v1.Attribute.description]
          The description can be updated for user defined attributes
          only.
        - [allowed_values][google.cloud.apihub.v1.Attribute.allowed_values]
          To update the list of allowed values, clients need to use the
          fetched list of allowed values and add or remove values to or
          from the same list. The mutable allowed values can be updated
          for both user defined and System defined attributes. The
          immutable allowed values cannot be updated or deleted. The
          updated list of allowed values cannot be empty. If an allowed
          value that is already used by some resource's attribute is
          deleted, then the association between the resource and the
          attribute value will also be deleted.
        - [cardinality][google.cloud.apihub.v1.Attribute.cardinality]
          The cardinality can be updated for user defined attributes
          only. Cardinality can only be increased during an update.

        The
        [update_mask][google.cloud.apihub.v1.UpdateAttributeRequest.update_mask]
        should be used to specify the fields being updated.

        Returns:
            Callable[[~.UpdateAttributeRequest],
                    ~.Attribute]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_attribute" not in self._stubs:
            self._stubs["update_attribute"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/UpdateAttribute",
                request_serializer=apihub_service.UpdateAttributeRequest.serialize,
                response_deserializer=common_fields.Attribute.deserialize,
            )
        return self._stubs["update_attribute"]

    @property
    def delete_attribute(
        self,
    ) -> Callable[[apihub_service.DeleteAttributeRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete attribute method over gRPC.

        Delete an attribute.

        Note: System defined attributes cannot be deleted. All
        associations of the attribute being deleted with any API
        hub resource will also get deleted.

        Returns:
            Callable[[~.DeleteAttributeRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_attribute" not in self._stubs:
            self._stubs["delete_attribute"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/DeleteAttribute",
                request_serializer=apihub_service.DeleteAttributeRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_attribute"]

    @property
    def list_attributes(
        self,
    ) -> Callable[
        [apihub_service.ListAttributesRequest], apihub_service.ListAttributesResponse
    ]:
        r"""Return a callable for the list attributes method over gRPC.

        List all attributes.

        Returns:
            Callable[[~.ListAttributesRequest],
                    ~.ListAttributesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_attributes" not in self._stubs:
            self._stubs["list_attributes"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/ListAttributes",
                request_serializer=apihub_service.ListAttributesRequest.serialize,
                response_deserializer=apihub_service.ListAttributesResponse.deserialize,
            )
        return self._stubs["list_attributes"]

    @property
    def search_resources(
        self,
    ) -> Callable[
        [apihub_service.SearchResourcesRequest], apihub_service.SearchResourcesResponse
    ]:
        r"""Return a callable for the search resources method over gRPC.

        Search across API-Hub resources.

        Returns:
            Callable[[~.SearchResourcesRequest],
                    ~.SearchResourcesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_resources" not in self._stubs:
            self._stubs["search_resources"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/SearchResources",
                request_serializer=apihub_service.SearchResourcesRequest.serialize,
                response_deserializer=apihub_service.SearchResourcesResponse.deserialize,
            )
        return self._stubs["search_resources"]

    @property
    def create_external_api(
        self,
    ) -> Callable[[apihub_service.CreateExternalApiRequest], common_fields.ExternalApi]:
        r"""Return a callable for the create external api method over gRPC.

        Create an External API resource in the API hub.

        Returns:
            Callable[[~.CreateExternalApiRequest],
                    ~.ExternalApi]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_external_api" not in self._stubs:
            self._stubs["create_external_api"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/CreateExternalApi",
                request_serializer=apihub_service.CreateExternalApiRequest.serialize,
                response_deserializer=common_fields.ExternalApi.deserialize,
            )
        return self._stubs["create_external_api"]

    @property
    def get_external_api(
        self,
    ) -> Callable[[apihub_service.GetExternalApiRequest], common_fields.ExternalApi]:
        r"""Return a callable for the get external api method over gRPC.

        Get details about an External API resource in the API
        hub.

        Returns:
            Callable[[~.GetExternalApiRequest],
                    ~.ExternalApi]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_external_api" not in self._stubs:
            self._stubs["get_external_api"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/GetExternalApi",
                request_serializer=apihub_service.GetExternalApiRequest.serialize,
                response_deserializer=common_fields.ExternalApi.deserialize,
            )
        return self._stubs["get_external_api"]

    @property
    def update_external_api(
        self,
    ) -> Callable[[apihub_service.UpdateExternalApiRequest], common_fields.ExternalApi]:
        r"""Return a callable for the update external api method over gRPC.

        Update an External API resource in the API hub. The following
        fields can be updated:

        - [display_name][google.cloud.apihub.v1.ExternalApi.display_name]
        - [description][google.cloud.apihub.v1.ExternalApi.description]
        - [documentation][google.cloud.apihub.v1.ExternalApi.documentation]
        - [endpoints][google.cloud.apihub.v1.ExternalApi.endpoints]
        - [paths][google.cloud.apihub.v1.ExternalApi.paths]

        The
        [update_mask][google.cloud.apihub.v1.UpdateExternalApiRequest.update_mask]
        should be used to specify the fields being updated.

        Returns:
            Callable[[~.UpdateExternalApiRequest],
                    ~.ExternalApi]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_external_api" not in self._stubs:
            self._stubs["update_external_api"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/UpdateExternalApi",
                request_serializer=apihub_service.UpdateExternalApiRequest.serialize,
                response_deserializer=common_fields.ExternalApi.deserialize,
            )
        return self._stubs["update_external_api"]

    @property
    def delete_external_api(
        self,
    ) -> Callable[[apihub_service.DeleteExternalApiRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete external api method over gRPC.

        Delete an External API resource in the API hub.

        Returns:
            Callable[[~.DeleteExternalApiRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_external_api" not in self._stubs:
            self._stubs["delete_external_api"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/DeleteExternalApi",
                request_serializer=apihub_service.DeleteExternalApiRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_external_api"]

    @property
    def list_external_apis(
        self,
    ) -> Callable[
        [apihub_service.ListExternalApisRequest],
        apihub_service.ListExternalApisResponse,
    ]:
        r"""Return a callable for the list external apis method over gRPC.

        List External API resources in the API hub.

        Returns:
            Callable[[~.ListExternalApisRequest],
                    ~.ListExternalApisResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_external_apis" not in self._stubs:
            self._stubs["list_external_apis"] = self._logged_channel.unary_unary(
                "/google.cloud.apihub.v1.ApiHub/ListExternalApis",
                request_serializer=apihub_service.ListExternalApisRequest.serialize,
                response_deserializer=apihub_service.ListExternalApisResponse.deserialize,
            )
        return self._stubs["list_external_apis"]

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


__all__ = ("ApiHubGrpcTransport",)
