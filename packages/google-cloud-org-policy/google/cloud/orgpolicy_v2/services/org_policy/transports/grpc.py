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
from google.protobuf.json_format import MessageToJson

from google.cloud.orgpolicy_v2.types import constraint, orgpolicy

from .base import DEFAULT_CLIENT_INFO, OrgPolicyTransport

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
                    "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
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
                    "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class OrgPolicyGrpcTransport(OrgPolicyTransport):
    """gRPC backend transport for OrgPolicy.

    An interface for managing organization policies.

    The Organization Policy Service provides a simple mechanism for
    organizations to restrict the allowed configurations across
    their entire resource hierarchy.

    You can use a policy to configure restrictions on resources. For
    example, you can enforce a policy that restricts which Google
    Cloud APIs can be activated in a certain part of your resource
    hierarchy, or prevents serial port access to VM instances in a
    particular folder.

    Policies are inherited down through the resource hierarchy. A
    policy applied to a parent resource automatically applies to all
    its child resources unless overridden with a policy lower in the
    hierarchy.

    A constraint defines an aspect of a resource's configuration
    that can be controlled by an organization's policy
    administrator. Policies are a collection of constraints that
    defines their allowable configuration on a particular resource
    and its child resources.

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
        host: str = "orgpolicy.googleapis.com",
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
                 The hostname to connect to (default: 'orgpolicy.googleapis.com').
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
        host: str = "orgpolicy.googleapis.com",
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
    def list_constraints(
        self,
    ) -> Callable[
        [orgpolicy.ListConstraintsRequest], orgpolicy.ListConstraintsResponse
    ]:
        r"""Return a callable for the list constraints method over gRPC.

        Lists constraints that could be applied on the
        specified resource.

        Returns:
            Callable[[~.ListConstraintsRequest],
                    ~.ListConstraintsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_constraints" not in self._stubs:
            self._stubs["list_constraints"] = self._logged_channel.unary_unary(
                "/google.cloud.orgpolicy.v2.OrgPolicy/ListConstraints",
                request_serializer=orgpolicy.ListConstraintsRequest.serialize,
                response_deserializer=orgpolicy.ListConstraintsResponse.deserialize,
            )
        return self._stubs["list_constraints"]

    @property
    def list_policies(
        self,
    ) -> Callable[[orgpolicy.ListPoliciesRequest], orgpolicy.ListPoliciesResponse]:
        r"""Return a callable for the list policies method over gRPC.

        Retrieves all of the policies that exist on a
        particular resource.

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
                "/google.cloud.orgpolicy.v2.OrgPolicy/ListPolicies",
                request_serializer=orgpolicy.ListPoliciesRequest.serialize,
                response_deserializer=orgpolicy.ListPoliciesResponse.deserialize,
            )
        return self._stubs["list_policies"]

    @property
    def get_policy(self) -> Callable[[orgpolicy.GetPolicyRequest], orgpolicy.Policy]:
        r"""Return a callable for the get policy method over gRPC.

        Gets a policy on a resource.

        If no policy is set on the resource, ``NOT_FOUND`` is returned.
        The ``etag`` value can be used with ``UpdatePolicy()`` to update
        a policy during read-modify-write.

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
                "/google.cloud.orgpolicy.v2.OrgPolicy/GetPolicy",
                request_serializer=orgpolicy.GetPolicyRequest.serialize,
                response_deserializer=orgpolicy.Policy.deserialize,
            )
        return self._stubs["get_policy"]

    @property
    def get_effective_policy(
        self,
    ) -> Callable[[orgpolicy.GetEffectivePolicyRequest], orgpolicy.Policy]:
        r"""Return a callable for the get effective policy method over gRPC.

        Gets the effective policy on a resource. This is the result of
        merging policies in the resource hierarchy and evaluating
        conditions. The returned policy will not have an ``etag`` or
        ``condition`` set because it is an evaluated policy across
        multiple resources. Subtrees of Resource Manager resource
        hierarchy with 'under:' prefix will not be expanded.

        Returns:
            Callable[[~.GetEffectivePolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_effective_policy" not in self._stubs:
            self._stubs["get_effective_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.orgpolicy.v2.OrgPolicy/GetEffectivePolicy",
                request_serializer=orgpolicy.GetEffectivePolicyRequest.serialize,
                response_deserializer=orgpolicy.Policy.deserialize,
            )
        return self._stubs["get_effective_policy"]

    @property
    def create_policy(
        self,
    ) -> Callable[[orgpolicy.CreatePolicyRequest], orgpolicy.Policy]:
        r"""Return a callable for the create policy method over gRPC.

        Creates a policy.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint does not exist.
        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.ALREADY_EXISTS`` if the policy already exists
        on the given Google Cloud resource.

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
                "/google.cloud.orgpolicy.v2.OrgPolicy/CreatePolicy",
                request_serializer=orgpolicy.CreatePolicyRequest.serialize,
                response_deserializer=orgpolicy.Policy.deserialize,
            )
        return self._stubs["create_policy"]

    @property
    def update_policy(
        self,
    ) -> Callable[[orgpolicy.UpdatePolicyRequest], orgpolicy.Policy]:
        r"""Return a callable for the update policy method over gRPC.

        Updates a policy.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint or the policy do
        not exist. Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.ABORTED`` if the etag supplied in the request
        does not match the persisted etag of the policy

        Note: the supplied policy will perform a full overwrite of all
        fields.

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
                "/google.cloud.orgpolicy.v2.OrgPolicy/UpdatePolicy",
                request_serializer=orgpolicy.UpdatePolicyRequest.serialize,
                response_deserializer=orgpolicy.Policy.deserialize,
            )
        return self._stubs["update_policy"]

    @property
    def delete_policy(
        self,
    ) -> Callable[[orgpolicy.DeletePolicyRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete policy method over gRPC.

        Deletes a policy.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint or organization
        policy does not exist.

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
                "/google.cloud.orgpolicy.v2.OrgPolicy/DeletePolicy",
                request_serializer=orgpolicy.DeletePolicyRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_policy"]

    @property
    def create_custom_constraint(
        self,
    ) -> Callable[
        [orgpolicy.CreateCustomConstraintRequest], constraint.CustomConstraint
    ]:
        r"""Return a callable for the create custom constraint method over gRPC.

        Creates a custom constraint.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the organization does not
        exist. Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.ALREADY_EXISTS`` if the constraint already
        exists on the given organization.

        Returns:
            Callable[[~.CreateCustomConstraintRequest],
                    ~.CustomConstraint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_custom_constraint" not in self._stubs:
            self._stubs["create_custom_constraint"] = self._logged_channel.unary_unary(
                "/google.cloud.orgpolicy.v2.OrgPolicy/CreateCustomConstraint",
                request_serializer=orgpolicy.CreateCustomConstraintRequest.serialize,
                response_deserializer=constraint.CustomConstraint.deserialize,
            )
        return self._stubs["create_custom_constraint"]

    @property
    def update_custom_constraint(
        self,
    ) -> Callable[
        [orgpolicy.UpdateCustomConstraintRequest], constraint.CustomConstraint
    ]:
        r"""Return a callable for the update custom constraint method over gRPC.

        Updates a custom constraint.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint does not exist.

        Note: the supplied policy will perform a full overwrite of all
        fields.

        Returns:
            Callable[[~.UpdateCustomConstraintRequest],
                    ~.CustomConstraint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_custom_constraint" not in self._stubs:
            self._stubs["update_custom_constraint"] = self._logged_channel.unary_unary(
                "/google.cloud.orgpolicy.v2.OrgPolicy/UpdateCustomConstraint",
                request_serializer=orgpolicy.UpdateCustomConstraintRequest.serialize,
                response_deserializer=constraint.CustomConstraint.deserialize,
            )
        return self._stubs["update_custom_constraint"]

    @property
    def get_custom_constraint(
        self,
    ) -> Callable[[orgpolicy.GetCustomConstraintRequest], constraint.CustomConstraint]:
        r"""Return a callable for the get custom constraint method over gRPC.

        Gets a custom or managed constraint.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the custom or managed
        constraint does not exist.

        Returns:
            Callable[[~.GetCustomConstraintRequest],
                    ~.CustomConstraint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_custom_constraint" not in self._stubs:
            self._stubs["get_custom_constraint"] = self._logged_channel.unary_unary(
                "/google.cloud.orgpolicy.v2.OrgPolicy/GetCustomConstraint",
                request_serializer=orgpolicy.GetCustomConstraintRequest.serialize,
                response_deserializer=constraint.CustomConstraint.deserialize,
            )
        return self._stubs["get_custom_constraint"]

    @property
    def list_custom_constraints(
        self,
    ) -> Callable[
        [orgpolicy.ListCustomConstraintsRequest],
        orgpolicy.ListCustomConstraintsResponse,
    ]:
        r"""Return a callable for the list custom constraints method over gRPC.

        Retrieves all of the custom constraints that exist on
        a particular organization resource.

        Returns:
            Callable[[~.ListCustomConstraintsRequest],
                    ~.ListCustomConstraintsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_custom_constraints" not in self._stubs:
            self._stubs["list_custom_constraints"] = self._logged_channel.unary_unary(
                "/google.cloud.orgpolicy.v2.OrgPolicy/ListCustomConstraints",
                request_serializer=orgpolicy.ListCustomConstraintsRequest.serialize,
                response_deserializer=orgpolicy.ListCustomConstraintsResponse.deserialize,
            )
        return self._stubs["list_custom_constraints"]

    @property
    def delete_custom_constraint(
        self,
    ) -> Callable[[orgpolicy.DeleteCustomConstraintRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete custom constraint method over gRPC.

        Deletes a custom constraint.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint does not exist.

        Returns:
            Callable[[~.DeleteCustomConstraintRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_custom_constraint" not in self._stubs:
            self._stubs["delete_custom_constraint"] = self._logged_channel.unary_unary(
                "/google.cloud.orgpolicy.v2.OrgPolicy/DeleteCustomConstraint",
                request_serializer=orgpolicy.DeleteCustomConstraintRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_custom_constraint"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("OrgPolicyGrpcTransport",)
