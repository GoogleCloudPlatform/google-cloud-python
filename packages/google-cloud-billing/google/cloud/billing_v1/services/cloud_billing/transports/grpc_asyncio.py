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

import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.billing_v1.types import cloud_billing

from .base import DEFAULT_CLIENT_INFO, CloudBillingTransport
from .grpc import CloudBillingGrpcTransport

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
                    "serviceName": "google.cloud.billing.v1.CloudBilling",
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
                    "serviceName": "google.cloud.billing.v1.CloudBilling",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class CloudBillingGrpcAsyncIOTransport(CloudBillingTransport):
    """gRPC AsyncIO backend transport for CloudBilling.

    Retrieves the Google Cloud Console billing accounts and
    associates them with projects.

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
        host: str = "cloudbilling.googleapis.com",
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
        host: str = "cloudbilling.googleapis.com",
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
                 The hostname to connect to (default: 'cloudbilling.googleapis.com').
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
    def get_billing_account(
        self,
    ) -> Callable[
        [cloud_billing.GetBillingAccountRequest],
        Awaitable[cloud_billing.BillingAccount],
    ]:
        r"""Return a callable for the get billing account method over gRPC.

        Gets information about a billing account. The current
        authenticated user must be a `viewer of the billing
        account <https://cloud.google.com/billing/docs/how-to/billing-access>`__.

        Returns:
            Callable[[~.GetBillingAccountRequest],
                    Awaitable[~.BillingAccount]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_billing_account" not in self._stubs:
            self._stubs["get_billing_account"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/GetBillingAccount",
                request_serializer=cloud_billing.GetBillingAccountRequest.serialize,
                response_deserializer=cloud_billing.BillingAccount.deserialize,
            )
        return self._stubs["get_billing_account"]

    @property
    def list_billing_accounts(
        self,
    ) -> Callable[
        [cloud_billing.ListBillingAccountsRequest],
        Awaitable[cloud_billing.ListBillingAccountsResponse],
    ]:
        r"""Return a callable for the list billing accounts method over gRPC.

        Lists the billing accounts that the current authenticated user
        has permission to
        `view <https://cloud.google.com/billing/docs/how-to/billing-access>`__.

        Returns:
            Callable[[~.ListBillingAccountsRequest],
                    Awaitable[~.ListBillingAccountsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_billing_accounts" not in self._stubs:
            self._stubs["list_billing_accounts"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/ListBillingAccounts",
                request_serializer=cloud_billing.ListBillingAccountsRequest.serialize,
                response_deserializer=cloud_billing.ListBillingAccountsResponse.deserialize,
            )
        return self._stubs["list_billing_accounts"]

    @property
    def update_billing_account(
        self,
    ) -> Callable[
        [cloud_billing.UpdateBillingAccountRequest],
        Awaitable[cloud_billing.BillingAccount],
    ]:
        r"""Return a callable for the update billing account method over gRPC.

        Updates a billing account's fields. Currently the only field
        that can be edited is ``display_name``. The current
        authenticated user must have the ``billing.accounts.update`` IAM
        permission, which is typically given to the
        `administrator <https://cloud.google.com/billing/docs/how-to/billing-access>`__
        of the billing account.

        Returns:
            Callable[[~.UpdateBillingAccountRequest],
                    Awaitable[~.BillingAccount]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_billing_account" not in self._stubs:
            self._stubs["update_billing_account"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/UpdateBillingAccount",
                request_serializer=cloud_billing.UpdateBillingAccountRequest.serialize,
                response_deserializer=cloud_billing.BillingAccount.deserialize,
            )
        return self._stubs["update_billing_account"]

    @property
    def create_billing_account(
        self,
    ) -> Callable[
        [cloud_billing.CreateBillingAccountRequest],
        Awaitable[cloud_billing.BillingAccount],
    ]:
        r"""Return a callable for the create billing account method over gRPC.

        This method creates `billing
        subaccounts <https://cloud.google.com/billing/docs/concepts#subaccounts>`__.

        Google Cloud resellers should use the Channel Services APIs,
        `accounts.customers.create <https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/create>`__
        and
        `accounts.customers.entitlements.create <https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create>`__.

        When creating a subaccount, the current authenticated user must
        have the ``billing.accounts.update`` IAM permission on the
        parent account, which is typically given to billing account
        `administrators <https://cloud.google.com/billing/docs/how-to/billing-access>`__.
        This method will return an error if the parent account has not
        been provisioned for subaccounts.

        Returns:
            Callable[[~.CreateBillingAccountRequest],
                    Awaitable[~.BillingAccount]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_billing_account" not in self._stubs:
            self._stubs["create_billing_account"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/CreateBillingAccount",
                request_serializer=cloud_billing.CreateBillingAccountRequest.serialize,
                response_deserializer=cloud_billing.BillingAccount.deserialize,
            )
        return self._stubs["create_billing_account"]

    @property
    def list_project_billing_info(
        self,
    ) -> Callable[
        [cloud_billing.ListProjectBillingInfoRequest],
        Awaitable[cloud_billing.ListProjectBillingInfoResponse],
    ]:
        r"""Return a callable for the list project billing info method over gRPC.

        Lists the projects associated with a billing account. The
        current authenticated user must have the
        ``billing.resourceAssociations.list`` IAM permission, which is
        often given to billing account
        `viewers <https://cloud.google.com/billing/docs/how-to/billing-access>`__.

        Returns:
            Callable[[~.ListProjectBillingInfoRequest],
                    Awaitable[~.ListProjectBillingInfoResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_project_billing_info" not in self._stubs:
            self._stubs["list_project_billing_info"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/ListProjectBillingInfo",
                request_serializer=cloud_billing.ListProjectBillingInfoRequest.serialize,
                response_deserializer=cloud_billing.ListProjectBillingInfoResponse.deserialize,
            )
        return self._stubs["list_project_billing_info"]

    @property
    def get_project_billing_info(
        self,
    ) -> Callable[
        [cloud_billing.GetProjectBillingInfoRequest],
        Awaitable[cloud_billing.ProjectBillingInfo],
    ]:
        r"""Return a callable for the get project billing info method over gRPC.

        Gets the billing information for a project. The current
        authenticated user must have the
        ``resourcemanager.projects.get`` permission for the project,
        which can be granted by assigning the `Project
        Viewer <https://cloud.google.com/iam/docs/understanding-roles#predefined_roles>`__
        role.

        Returns:
            Callable[[~.GetProjectBillingInfoRequest],
                    Awaitable[~.ProjectBillingInfo]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_project_billing_info" not in self._stubs:
            self._stubs["get_project_billing_info"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/GetProjectBillingInfo",
                request_serializer=cloud_billing.GetProjectBillingInfoRequest.serialize,
                response_deserializer=cloud_billing.ProjectBillingInfo.deserialize,
            )
        return self._stubs["get_project_billing_info"]

    @property
    def update_project_billing_info(
        self,
    ) -> Callable[
        [cloud_billing.UpdateProjectBillingInfoRequest],
        Awaitable[cloud_billing.ProjectBillingInfo],
    ]:
        r"""Return a callable for the update project billing info method over gRPC.

        Sets or updates the billing account associated with a project.
        You specify the new billing account by setting the
        ``billing_account_name`` in the ``ProjectBillingInfo`` resource
        to the resource name of a billing account. Associating a project
        with an open billing account enables billing on the project and
        allows charges for resource usage. If the project already had a
        billing account, this method changes the billing account used
        for resource usage charges.

        *Note:* Incurred charges that have not yet been reported in the
        transaction history of the Google Cloud Console might be billed
        to the new billing account, even if the charge occurred before
        the new billing account was assigned to the project.

        The current authenticated user must have ownership privileges
        for both the
        `project <https://cloud.google.com/docs/permissions-overview#h.bgs0oxofvnoo>`__
        and the `billing
        account <https://cloud.google.com/billing/docs/how-to/billing-access>`__.

        You can disable billing on the project by setting the
        ``billing_account_name`` field to empty. This action
        disassociates the current billing account from the project. Any
        billable activity of your in-use services will stop, and your
        application could stop functioning as expected. Any unbilled
        charges to date will be billed to the previously associated
        account. The current authenticated user must be either an owner
        of the project or an owner of the billing account for the
        project.

        Note that associating a project with a *closed* billing account
        will have much the same effect as disabling billing on the
        project: any paid resources used by the project will be shut
        down. Thus, unless you wish to disable billing, you should
        always call this method with the name of an *open* billing
        account.

        Returns:
            Callable[[~.UpdateProjectBillingInfoRequest],
                    Awaitable[~.ProjectBillingInfo]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_project_billing_info" not in self._stubs:
            self._stubs["update_project_billing_info"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.billing.v1.CloudBilling/UpdateProjectBillingInfo",
                    request_serializer=cloud_billing.UpdateProjectBillingInfoRequest.serialize,
                    response_deserializer=cloud_billing.ProjectBillingInfo.deserialize,
                )
            )
        return self._stubs["update_project_billing_info"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the access control policy for a billing account. The caller
        must have the ``billing.accounts.getIamPolicy`` permission on
        the account, which is often given to billing account
        `viewers <https://cloud.google.com/billing/docs/how-to/billing-access>`__.

        Returns:
            Callable[[~.GetIamPolicyRequest],
                    Awaitable[~.Policy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the access control policy for a billing account. Replaces
        any existing policy. The caller must have the
        ``billing.accounts.setIamPolicy`` permission on the account,
        which is often given to billing account
        `administrators <https://cloud.google.com/billing/docs/how-to/billing-access>`__.

        Returns:
            Callable[[~.SetIamPolicyRequest],
                    Awaitable[~.Policy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.

        Tests the access control policy for a billing
        account. This method takes the resource and a set of
        permissions as input and returns the subset of the input
        permissions that the caller is allowed for that
        resource.

        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    Awaitable[~.TestIamPermissionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def move_billing_account(
        self,
    ) -> Callable[
        [cloud_billing.MoveBillingAccountRequest],
        Awaitable[cloud_billing.BillingAccount],
    ]:
        r"""Return a callable for the move billing account method over gRPC.

        Changes which parent organization a billing account
        belongs to.

        Returns:
            Callable[[~.MoveBillingAccountRequest],
                    Awaitable[~.BillingAccount]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_billing_account" not in self._stubs:
            self._stubs["move_billing_account"] = self._logged_channel.unary_unary(
                "/google.cloud.billing.v1.CloudBilling/MoveBillingAccount",
                request_serializer=cloud_billing.MoveBillingAccountRequest.serialize,
                response_deserializer=cloud_billing.BillingAccount.deserialize,
            )
        return self._stubs["move_billing_account"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.get_billing_account: self._wrap_method(
                self.get_billing_account,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_billing_accounts: self._wrap_method(
                self.list_billing_accounts,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_billing_account: self._wrap_method(
                self.update_billing_account,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_billing_account: self._wrap_method(
                self.create_billing_account,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_project_billing_info: self._wrap_method(
                self.list_project_billing_info,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_project_billing_info: self._wrap_method(
                self.get_project_billing_info,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_project_billing_info: self._wrap_method(
                self.update_project_billing_info,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.move_billing_account: self._wrap_method(
                self.move_billing_account,
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


__all__ = ("CloudBillingGrpcAsyncIOTransport",)
