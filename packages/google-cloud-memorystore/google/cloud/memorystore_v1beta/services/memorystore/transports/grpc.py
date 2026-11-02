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
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.memorystore_v1beta._compat import (
    _observability,
    apply_channel_interceptors,
)
from google.cloud.memorystore_v1beta.types import memorystore

from .base import DEFAULT_CLIENT_INFO, MemorystoreTransport

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
                    "serviceName": "google.cloud.memorystore.v1beta.Memorystore",
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
                    "serviceName": "google.cloud.memorystore.v1beta.Memorystore",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class MemorystoreGrpcTransport(MemorystoreTransport):
    """gRPC backend transport for Memorystore.

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
        host: str = "memorystore.googleapis.com",
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
                 The hostname to connect to (default: 'memorystore.googleapis.com').
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
        host: str = "memorystore.googleapis.com",
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
    def list_acl_policies(
        self,
    ) -> Callable[
        [memorystore.ListAclPoliciesRequest], memorystore.ListAclPoliciesResponse
    ]:
        r"""Return a callable for the list acl policies method over gRPC.

        Lists all ACL policies owned by a project in either the
        specified location (region) or all locations.

        The location should have the following format:

        - ``projects/{project_id}/locations/{location_id}``

        If ``location_id`` is specified as ``-`` (wildcard), then all
        regions available to the project are queried, and the results
        are aggregated.

        Returns:
            Callable[[~.ListAclPoliciesRequest],
                    ~.ListAclPoliciesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_acl_policies" not in self._stubs:
            self._stubs["list_acl_policies"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/ListAclPolicies",
                request_serializer=memorystore.ListAclPoliciesRequest.serialize,
                response_deserializer=memorystore.ListAclPoliciesResponse.deserialize,
            )
        return self._stubs["list_acl_policies"]

    @property
    def list_instances(
        self,
    ) -> Callable[
        [memorystore.ListInstancesRequest], memorystore.ListInstancesResponse
    ]:
        r"""Return a callable for the list instances method over gRPC.

        Lists Instances in a given project and location.

        Returns:
            Callable[[~.ListInstancesRequest],
                    ~.ListInstancesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_instances" not in self._stubs:
            self._stubs["list_instances"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/ListInstances",
                request_serializer=memorystore.ListInstancesRequest.serialize,
                response_deserializer=memorystore.ListInstancesResponse.deserialize,
            )
        return self._stubs["list_instances"]

    @property
    def get_acl_policy(
        self,
    ) -> Callable[[memorystore.GetAclPolicyRequest], memorystore.AclPolicy]:
        r"""Return a callable for the get acl policy method over gRPC.

        Gets the details of a specific Memorystore ACL
        policy.

        Returns:
            Callable[[~.GetAclPolicyRequest],
                    ~.AclPolicy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_acl_policy" not in self._stubs:
            self._stubs["get_acl_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/GetAclPolicy",
                request_serializer=memorystore.GetAclPolicyRequest.serialize,
                response_deserializer=memorystore.AclPolicy.deserialize,
            )
        return self._stubs["get_acl_policy"]

    @property
    def get_instance(
        self,
    ) -> Callable[[memorystore.GetInstanceRequest], memorystore.Instance]:
        r"""Return a callable for the get instance method over gRPC.

        Gets details of a single Instance.

        Returns:
            Callable[[~.GetInstanceRequest],
                    ~.Instance]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_instance" not in self._stubs:
            self._stubs["get_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/GetInstance",
                request_serializer=memorystore.GetInstanceRequest.serialize,
                response_deserializer=memorystore.Instance.deserialize,
            )
        return self._stubs["get_instance"]

    @property
    def create_acl_policy(
        self,
    ) -> Callable[[memorystore.CreateAclPolicyRequest], memorystore.AclPolicy]:
        r"""Return a callable for the create acl policy method over gRPC.

        Creates an ACL policy.
        The creation is executed synchronously and the policy is
        available for use immediately after the RPC returns.

        Returns:
            Callable[[~.CreateAclPolicyRequest],
                    ~.AclPolicy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_acl_policy" not in self._stubs:
            self._stubs["create_acl_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/CreateAclPolicy",
                request_serializer=memorystore.CreateAclPolicyRequest.serialize,
                response_deserializer=memorystore.AclPolicy.deserialize,
            )
        return self._stubs["create_acl_policy"]

    @property
    def create_instance(
        self,
    ) -> Callable[[memorystore.CreateInstanceRequest], operations_pb2.Operation]:
        r"""Return a callable for the create instance method over gRPC.

        Creates a new Instance in a given project and
        location.

        Returns:
            Callable[[~.CreateInstanceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_instance" not in self._stubs:
            self._stubs["create_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/CreateInstance",
                request_serializer=memorystore.CreateInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_instance"]

    @property
    def update_acl_policy(
        self,
    ) -> Callable[[memorystore.UpdateAclPolicyRequest], operations_pb2.Operation]:
        r"""Return a callable for the update acl policy method over gRPC.

        Updates the ACL policy.

        The operation will apply the updated ACL policy to all
        the linked instances. The operation will return success
        if it successfully applied the policy to all the
        instances. If the operation completed with a failure,
        the service will continue to apply the policy via
        reconciliation for the failed instances even after
        operation completion to ensure eventual consistency.

        Completed longrunning.Operation will contain the new ACL
        policy object in the response field.

        Returns:
            Callable[[~.UpdateAclPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_acl_policy" not in self._stubs:
            self._stubs["update_acl_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/UpdateAclPolicy",
                request_serializer=memorystore.UpdateAclPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_acl_policy"]

    @property
    def update_instance(
        self,
    ) -> Callable[[memorystore.UpdateInstanceRequest], operations_pb2.Operation]:
        r"""Return a callable for the update instance method over gRPC.

        Updates the parameters of a single Instance.

        Returns:
            Callable[[~.UpdateInstanceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_instance" not in self._stubs:
            self._stubs["update_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/UpdateInstance",
                request_serializer=memorystore.UpdateInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_instance"]

    @property
    def delete_acl_policy(
        self,
    ) -> Callable[[memorystore.DeleteAclPolicyRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete acl policy method over gRPC.

        Deletes a specific ACL policy. This action will
        delete the ACL policy and all the rules associated with
        it. An ACL policy cannot be deleted if it is attached to
        an instance.

        Returns:
            Callable[[~.DeleteAclPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_acl_policy" not in self._stubs:
            self._stubs["delete_acl_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/DeleteAclPolicy",
                request_serializer=memorystore.DeleteAclPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_acl_policy"]

    @property
    def get_acl_policy_revision(
        self,
    ) -> Callable[
        [memorystore.GetAclPolicyRevisionRequest], memorystore.AclPolicyRevision
    ]:
        r"""Return a callable for the get acl policy revision method over gRPC.

        Gets details of a specific ACL policy revision.

        Returns:
            Callable[[~.GetAclPolicyRevisionRequest],
                    ~.AclPolicyRevision]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_acl_policy_revision" not in self._stubs:
            self._stubs["get_acl_policy_revision"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/GetAclPolicyRevision",
                request_serializer=memorystore.GetAclPolicyRevisionRequest.serialize,
                response_deserializer=memorystore.AclPolicyRevision.deserialize,
            )
        return self._stubs["get_acl_policy_revision"]

    @property
    def list_acl_policy_revisions(
        self,
    ) -> Callable[
        [memorystore.ListAclPolicyRevisionsRequest],
        memorystore.ListAclPolicyRevisionsResponse,
    ]:
        r"""Return a callable for the list acl policy revisions method over gRPC.

        Lists all ACL policy revisions in a given ACL policy.

        Returns:
            Callable[[~.ListAclPolicyRevisionsRequest],
                    ~.ListAclPolicyRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_acl_policy_revisions" not in self._stubs:
            self._stubs["list_acl_policy_revisions"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/ListAclPolicyRevisions",
                request_serializer=memorystore.ListAclPolicyRevisionsRequest.serialize,
                response_deserializer=memorystore.ListAclPolicyRevisionsResponse.deserialize,
            )
        return self._stubs["list_acl_policy_revisions"]

    @property
    def delete_instance(
        self,
    ) -> Callable[[memorystore.DeleteInstanceRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete instance method over gRPC.

        Deletes a single Instance.

        Returns:
            Callable[[~.DeleteInstanceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_instance" not in self._stubs:
            self._stubs["delete_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/DeleteInstance",
                request_serializer=memorystore.DeleteInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_instance"]

    @property
    def get_certificate_authority(
        self,
    ) -> Callable[
        [memorystore.GetCertificateAuthorityRequest], memorystore.CertificateAuthority
    ]:
        r"""Return a callable for the get certificate authority method over gRPC.

        Gets details about the certificate authority for an
        Instance.

        Returns:
            Callable[[~.GetCertificateAuthorityRequest],
                    ~.CertificateAuthority]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_certificate_authority" not in self._stubs:
            self._stubs["get_certificate_authority"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/GetCertificateAuthority",
                request_serializer=memorystore.GetCertificateAuthorityRequest.serialize,
                response_deserializer=memorystore.CertificateAuthority.deserialize,
            )
        return self._stubs["get_certificate_authority"]

    @property
    def get_shared_regional_certificate_authority(
        self,
    ) -> Callable[
        [memorystore.GetSharedRegionalCertificateAuthorityRequest],
        memorystore.SharedRegionalCertificateAuthority,
    ]:
        r"""Return a callable for the get shared regional
        certificate authority method over gRPC.

        Gets the details of shared regional certificate
        authority information for Memorystore instance.

        Returns:
            Callable[[~.GetSharedRegionalCertificateAuthorityRequest],
                    ~.SharedRegionalCertificateAuthority]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_shared_regional_certificate_authority" not in self._stubs:
            self._stubs["get_shared_regional_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.memorystore.v1beta.Memorystore/GetSharedRegionalCertificateAuthority",
                    request_serializer=memorystore.GetSharedRegionalCertificateAuthorityRequest.serialize,
                    response_deserializer=memorystore.SharedRegionalCertificateAuthority.deserialize,
                )
            )
        return self._stubs["get_shared_regional_certificate_authority"]

    @property
    def reschedule_maintenance(
        self,
    ) -> Callable[[memorystore.RescheduleMaintenanceRequest], operations_pb2.Operation]:
        r"""Return a callable for the reschedule maintenance method over gRPC.

        Reschedules upcoming maintenance event.

        Returns:
            Callable[[~.RescheduleMaintenanceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reschedule_maintenance" not in self._stubs:
            self._stubs["reschedule_maintenance"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/RescheduleMaintenance",
                request_serializer=memorystore.RescheduleMaintenanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reschedule_maintenance"]

    @property
    def list_backup_collections(
        self,
    ) -> Callable[
        [memorystore.ListBackupCollectionsRequest],
        memorystore.ListBackupCollectionsResponse,
    ]:
        r"""Return a callable for the list backup collections method over gRPC.

        Lists all backup collections owned by a consumer project in
        either the specified location (region) or all locations.

        If ``location_id`` is specified as ``-`` (wildcard), then all
        regions available to the project are queried, and the results
        are aggregated.

        Returns:
            Callable[[~.ListBackupCollectionsRequest],
                    ~.ListBackupCollectionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_backup_collections" not in self._stubs:
            self._stubs["list_backup_collections"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/ListBackupCollections",
                request_serializer=memorystore.ListBackupCollectionsRequest.serialize,
                response_deserializer=memorystore.ListBackupCollectionsResponse.deserialize,
            )
        return self._stubs["list_backup_collections"]

    @property
    def get_backup_collection(
        self,
    ) -> Callable[
        [memorystore.GetBackupCollectionRequest], memorystore.BackupCollection
    ]:
        r"""Return a callable for the get backup collection method over gRPC.

        Get a backup collection.

        Returns:
            Callable[[~.GetBackupCollectionRequest],
                    ~.BackupCollection]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_backup_collection" not in self._stubs:
            self._stubs["get_backup_collection"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/GetBackupCollection",
                request_serializer=memorystore.GetBackupCollectionRequest.serialize,
                response_deserializer=memorystore.BackupCollection.deserialize,
            )
        return self._stubs["get_backup_collection"]

    @property
    def list_backups(
        self,
    ) -> Callable[[memorystore.ListBackupsRequest], memorystore.ListBackupsResponse]:
        r"""Return a callable for the list backups method over gRPC.

        Lists all backups owned by a backup collection.

        Returns:
            Callable[[~.ListBackupsRequest],
                    ~.ListBackupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_backups" not in self._stubs:
            self._stubs["list_backups"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/ListBackups",
                request_serializer=memorystore.ListBackupsRequest.serialize,
                response_deserializer=memorystore.ListBackupsResponse.deserialize,
            )
        return self._stubs["list_backups"]

    @property
    def get_backup(
        self,
    ) -> Callable[[memorystore.GetBackupRequest], memorystore.Backup]:
        r"""Return a callable for the get backup method over gRPC.

        Gets the details of a specific backup.

        Returns:
            Callable[[~.GetBackupRequest],
                    ~.Backup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_backup" not in self._stubs:
            self._stubs["get_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/GetBackup",
                request_serializer=memorystore.GetBackupRequest.serialize,
                response_deserializer=memorystore.Backup.deserialize,
            )
        return self._stubs["get_backup"]

    @property
    def delete_backup(
        self,
    ) -> Callable[[memorystore.DeleteBackupRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete backup method over gRPC.

        Deletes a specific backup.

        Returns:
            Callable[[~.DeleteBackupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_backup" not in self._stubs:
            self._stubs["delete_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/DeleteBackup",
                request_serializer=memorystore.DeleteBackupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_backup"]

    @property
    def export_backup(
        self,
    ) -> Callable[[memorystore.ExportBackupRequest], operations_pb2.Operation]:
        r"""Return a callable for the export backup method over gRPC.

        Exports a specific backup to a customer target Cloud
        Storage URI.

        Returns:
            Callable[[~.ExportBackupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_backup" not in self._stubs:
            self._stubs["export_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/ExportBackup",
                request_serializer=memorystore.ExportBackupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_backup"]

    @property
    def backup_instance(
        self,
    ) -> Callable[[memorystore.BackupInstanceRequest], operations_pb2.Operation]:
        r"""Return a callable for the backup instance method over gRPC.

        Backup Instance.
        If this is the first time a backup is being created, a
        backup collection will be created at the backend, and
        this backup belongs to this collection. Both collection
        and backup will have a resource name. Backup will be
        executed for each shard. A replica (primary if nonHA)
        will be selected to perform the execution. Backup call
        will be rejected if there is an ongoing backup or update
        operation. Be aware that during preview, if the
        instance's internal software version is too old,
        critical update will be performed before actual backup.
        Once the internal software version is updated to the
        minimum version required by the backup feature,
        subsequent backups will not require critical update.
        After preview, there will be no critical update needed
        for backup.

        Returns:
            Callable[[~.BackupInstanceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "backup_instance" not in self._stubs:
            self._stubs["backup_instance"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/BackupInstance",
                request_serializer=memorystore.BackupInstanceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["backup_instance"]

    @property
    def start_migration(
        self,
    ) -> Callable[[memorystore.StartMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the start migration method over gRPC.

        Initiates the migration of a source instance to the
        target Memorystore instance.

        After the successful completion of this operation, the
        target instance will:

        1. Set up replication with the source instance and
            replicate any writes to the source instance.
        2. Only allow reads.

        Returns:
            Callable[[~.StartMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_migration" not in self._stubs:
            self._stubs["start_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/StartMigration",
                request_serializer=memorystore.StartMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_migration"]

    @property
    def finish_migration(
        self,
    ) -> Callable[[memorystore.FinishMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the finish migration method over gRPC.

        Finalizes the migration process.

        After the successful completion of this operation, the
        target instance will:

        1. Stop replicating from the source instance.
        2. Allow both reads and writes.

        Returns:
            Callable[[~.FinishMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "finish_migration" not in self._stubs:
            self._stubs["finish_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/FinishMigration",
                request_serializer=memorystore.FinishMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["finish_migration"]

    @property
    def list_token_auth_users(
        self,
    ) -> Callable[
        [memorystore.ListTokenAuthUsersRequest], memorystore.ListTokenAuthUsersResponse
    ]:
        r"""Return a callable for the list token auth users method over gRPC.

        Lists all the token auth users for a token based auth
        enabled instance.

        Returns:
            Callable[[~.ListTokenAuthUsersRequest],
                    ~.ListTokenAuthUsersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_token_auth_users" not in self._stubs:
            self._stubs["list_token_auth_users"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/ListTokenAuthUsers",
                request_serializer=memorystore.ListTokenAuthUsersRequest.serialize,
                response_deserializer=memorystore.ListTokenAuthUsersResponse.deserialize,
            )
        return self._stubs["list_token_auth_users"]

    @property
    def get_token_auth_user(
        self,
    ) -> Callable[[memorystore.GetTokenAuthUserRequest], memorystore.TokenAuthUser]:
        r"""Return a callable for the get token auth user method over gRPC.

        Gets a specific token auth user for a token based
        auth enabled instance.

        Returns:
            Callable[[~.GetTokenAuthUserRequest],
                    ~.TokenAuthUser]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_token_auth_user" not in self._stubs:
            self._stubs["get_token_auth_user"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/GetTokenAuthUser",
                request_serializer=memorystore.GetTokenAuthUserRequest.serialize,
                response_deserializer=memorystore.TokenAuthUser.deserialize,
            )
        return self._stubs["get_token_auth_user"]

    @property
    def list_auth_tokens(
        self,
    ) -> Callable[
        [memorystore.ListAuthTokensRequest], memorystore.ListAuthTokensResponse
    ]:
        r"""Return a callable for the list auth tokens method over gRPC.

        Lists all the auth tokens for a specific token auth
        user.

        Returns:
            Callable[[~.ListAuthTokensRequest],
                    ~.ListAuthTokensResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_auth_tokens" not in self._stubs:
            self._stubs["list_auth_tokens"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/ListAuthTokens",
                request_serializer=memorystore.ListAuthTokensRequest.serialize,
                response_deserializer=memorystore.ListAuthTokensResponse.deserialize,
            )
        return self._stubs["list_auth_tokens"]

    @property
    def get_auth_token(
        self,
    ) -> Callable[[memorystore.GetAuthTokenRequest], memorystore.AuthToken]:
        r"""Return a callable for the get auth token method over gRPC.

        Gets a token based auth enabled instance's auth token
        for a given user.

        Returns:
            Callable[[~.GetAuthTokenRequest],
                    ~.AuthToken]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_auth_token" not in self._stubs:
            self._stubs["get_auth_token"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/GetAuthToken",
                request_serializer=memorystore.GetAuthTokenRequest.serialize,
                response_deserializer=memorystore.AuthToken.deserialize,
            )
        return self._stubs["get_auth_token"]

    @property
    def add_token_auth_user(
        self,
    ) -> Callable[[memorystore.AddTokenAuthUserRequest], operations_pb2.Operation]:
        r"""Return a callable for the add token auth user method over gRPC.

        Adds a token auth user for a token based auth enabled
        instance.

        Returns:
            Callable[[~.AddTokenAuthUserRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_token_auth_user" not in self._stubs:
            self._stubs["add_token_auth_user"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/AddTokenAuthUser",
                request_serializer=memorystore.AddTokenAuthUserRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["add_token_auth_user"]

    @property
    def delete_token_auth_user(
        self,
    ) -> Callable[[memorystore.DeleteTokenAuthUserRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete token auth user method over gRPC.

        Deletes a token auth user for a token based auth
        enabled instance.

        Returns:
            Callable[[~.DeleteTokenAuthUserRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_token_auth_user" not in self._stubs:
            self._stubs["delete_token_auth_user"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/DeleteTokenAuthUser",
                request_serializer=memorystore.DeleteTokenAuthUserRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_token_auth_user"]

    @property
    def add_auth_token(
        self,
    ) -> Callable[[memorystore.AddAuthTokenRequest], operations_pb2.Operation]:
        r"""Return a callable for the add auth token method over gRPC.

        Adds a token for a user of a token based auth enabled
        instance.

        Returns:
            Callable[[~.AddAuthTokenRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_auth_token" not in self._stubs:
            self._stubs["add_auth_token"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/AddAuthToken",
                request_serializer=memorystore.AddAuthTokenRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["add_auth_token"]

    @property
    def delete_auth_token(
        self,
    ) -> Callable[[memorystore.DeleteAuthTokenRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete auth token method over gRPC.

        Deletes a token for a user of a token based auth
        enabled instance.

        Returns:
            Callable[[~.DeleteAuthTokenRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_auth_token" not in self._stubs:
            self._stubs["delete_auth_token"] = self._logged_channel.unary_unary(
                "/google.cloud.memorystore.v1beta.Memorystore/DeleteAuthToken",
                request_serializer=memorystore.DeleteAuthTokenRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_auth_token"]

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


__all__ = ("MemorystoreGrpcTransport",)
