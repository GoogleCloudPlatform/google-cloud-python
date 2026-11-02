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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.channel_v1.types import (
    channel_partner_links,
    customers,
    entitlements,
    offers,
    repricing,
    service,
)

from .base import DEFAULT_CLIENT_INFO, CloudChannelServiceTransport
from .grpc import CloudChannelServiceGrpcTransport

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
                    "serviceName": "google.cloud.channel.v1.CloudChannelService",
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
                    "serviceName": "google.cloud.channel.v1.CloudChannelService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class CloudChannelServiceGrpcAsyncIOTransport(CloudChannelServiceTransport):
    """gRPC AsyncIO backend transport for CloudChannelService.

    CloudChannelService lets Google cloud resellers and distributors
    manage their customers, channel partners, entitlements, and reports.

    Using this service:

    1. Resellers and distributors can manage a customer entity.
    2. Distributors can register an authorized reseller in their channel
       and provide them with delegated admin access.
    3. Resellers and distributors can manage customer entitlements.

    CloudChannelService exposes the following resources:

    - [Customer][google.cloud.channel.v1.Customer]s: An entity-usually
      an enterprise-managed by a reseller or distributor.

    - [Entitlement][google.cloud.channel.v1.Entitlement]s: An entity
      that provides a customer with the means to use a service.
      Entitlements are created or updated as a result of a successful
      fulfillment.

    - [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]s:
      An entity that identifies links between distributors and their
      indirect resellers in a channel.

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
        host: str = "cloudchannel.googleapis.com",
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
        host: str = "cloudchannel.googleapis.com",
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
                 The hostname to connect to (default: 'cloudchannel.googleapis.com').
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
    def list_customers(
        self,
    ) -> Callable[
        [service.ListCustomersRequest], Awaitable[service.ListCustomersResponse]
    ]:
        r"""Return a callable for the list customers method over gRPC.

        List [Customer][google.cloud.channel.v1.Customer]s.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Return value: List of
        [Customer][google.cloud.channel.v1.Customer]s, or an empty list
        if there are no customers.

        Returns:
            Callable[[~.ListCustomersRequest],
                    Awaitable[~.ListCustomersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_customers" not in self._stubs:
            self._stubs["list_customers"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListCustomers",
                request_serializer=service.ListCustomersRequest.serialize,
                response_deserializer=service.ListCustomersResponse.deserialize,
            )
        return self._stubs["list_customers"]

    @property
    def get_customer(
        self,
    ) -> Callable[[service.GetCustomerRequest], Awaitable[customers.Customer]]:
        r"""Return a callable for the get customer method over gRPC.

        Returns the requested
        [Customer][google.cloud.channel.v1.Customer] resource.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: The customer resource doesn't exist. Usually the
          result of an invalid name parameter.

        Return value: The [Customer][google.cloud.channel.v1.Customer]
        resource.

        Returns:
            Callable[[~.GetCustomerRequest],
                    Awaitable[~.Customer]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_customer" not in self._stubs:
            self._stubs["get_customer"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/GetCustomer",
                request_serializer=service.GetCustomerRequest.serialize,
                response_deserializer=customers.Customer.deserialize,
            )
        return self._stubs["get_customer"]

    @property
    def check_cloud_identity_accounts_exist(
        self,
    ) -> Callable[
        [service.CheckCloudIdentityAccountsExistRequest],
        Awaitable[service.CheckCloudIdentityAccountsExistResponse],
    ]:
        r"""Return a callable for the check cloud identity accounts
        exist method over gRPC.

        Confirms the existence of Cloud Identity accounts based on the
        domain and if the Cloud Identity accounts are owned by the
        reseller.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - INVALID_VALUE: Invalid domain value in the request.

        Return value: A list of
        [CloudIdentityCustomerAccount][google.cloud.channel.v1.CloudIdentityCustomerAccount]
        resources for the domain (may be empty)

        Note: in the v1alpha1 version of the API, a NOT_FOUND error
        returns if no
        [CloudIdentityCustomerAccount][google.cloud.channel.v1.CloudIdentityCustomerAccount]
        resources match the domain.

        Returns:
            Callable[[~.CheckCloudIdentityAccountsExistRequest],
                    Awaitable[~.CheckCloudIdentityAccountsExistResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "check_cloud_identity_accounts_exist" not in self._stubs:
            self._stubs["check_cloud_identity_accounts_exist"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/CheckCloudIdentityAccountsExist",
                    request_serializer=service.CheckCloudIdentityAccountsExistRequest.serialize,
                    response_deserializer=service.CheckCloudIdentityAccountsExistResponse.deserialize,
                )
            )
        return self._stubs["check_cloud_identity_accounts_exist"]

    @property
    def create_customer(
        self,
    ) -> Callable[[service.CreateCustomerRequest], Awaitable[customers.Customer]]:
        r"""Return a callable for the create customer method over gRPC.

        Creates a new [Customer][google.cloud.channel.v1.Customer]
        resource under the reseller or distributor account.

        Possible error codes:

        - PERMISSION_DENIED:

          - The reseller account making the request is different from
            the reseller account in the API request.
          - You are not authorized to create a customer. See
            https://support.google.com/channelservices/answer/9759265

        - INVALID_ARGUMENT:

          - Required request parameters are missing or invalid.
          - Domain field value doesn't match the primary email domain.

        Return value: The newly created
        [Customer][google.cloud.channel.v1.Customer] resource.

        Returns:
            Callable[[~.CreateCustomerRequest],
                    Awaitable[~.Customer]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_customer" not in self._stubs:
            self._stubs["create_customer"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/CreateCustomer",
                request_serializer=service.CreateCustomerRequest.serialize,
                response_deserializer=customers.Customer.deserialize,
            )
        return self._stubs["create_customer"]

    @property
    def update_customer(
        self,
    ) -> Callable[[service.UpdateCustomerRequest], Awaitable[customers.Customer]]:
        r"""Return a callable for the update customer method over gRPC.

        Updates an existing [Customer][google.cloud.channel.v1.Customer]
        resource for the reseller or distributor.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: No [Customer][google.cloud.channel.v1.Customer]
          resource found for the name in the request.

        Return value: The updated
        [Customer][google.cloud.channel.v1.Customer] resource.

        Returns:
            Callable[[~.UpdateCustomerRequest],
                    Awaitable[~.Customer]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_customer" not in self._stubs:
            self._stubs["update_customer"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/UpdateCustomer",
                request_serializer=service.UpdateCustomerRequest.serialize,
                response_deserializer=customers.Customer.deserialize,
            )
        return self._stubs["update_customer"]

    @property
    def delete_customer(
        self,
    ) -> Callable[[service.DeleteCustomerRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete customer method over gRPC.

        Deletes the given [Customer][google.cloud.channel.v1.Customer]
        permanently.

        Possible error codes:

        - PERMISSION_DENIED: The account making the request does not own
          this customer.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - FAILED_PRECONDITION: The customer has existing entitlements.
        - NOT_FOUND: No [Customer][google.cloud.channel.v1.Customer]
          resource found for the name in the request.

        Returns:
            Callable[[~.DeleteCustomerRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_customer" not in self._stubs:
            self._stubs["delete_customer"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/DeleteCustomer",
                request_serializer=service.DeleteCustomerRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_customer"]

    @property
    def import_customer(
        self,
    ) -> Callable[[service.ImportCustomerRequest], Awaitable[customers.Customer]]:
        r"""Return a callable for the import customer method over gRPC.

        Imports a [Customer][google.cloud.channel.v1.Customer] from the
        Cloud Identity associated with the provided Cloud Identity ID or
        domain before a TransferEntitlements call. If a linked Customer
        already exists and overwrite_if_exists is true, it will update
        that Customer's data.

        Possible error codes:

        - PERMISSION_DENIED:

          - The reseller account making the request is different from
            the reseller account in the API request.
          - You are not authorized to import the customer. See
            https://support.google.com/channelservices/answer/9759265

        - NOT_FOUND: Cloud Identity doesn't exist or was deleted.
        - INVALID_ARGUMENT: Required parameters are missing, or the
          auth_token is expired or invalid.
        - ALREADY_EXISTS: A customer already exists and has conflicting
          critical fields. Requires an overwrite.

        Return value: The [Customer][google.cloud.channel.v1.Customer].

        Returns:
            Callable[[~.ImportCustomerRequest],
                    Awaitable[~.Customer]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_customer" not in self._stubs:
            self._stubs["import_customer"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ImportCustomer",
                request_serializer=service.ImportCustomerRequest.serialize,
                response_deserializer=customers.Customer.deserialize,
            )
        return self._stubs["import_customer"]

    @property
    def provision_cloud_identity(
        self,
    ) -> Callable[
        [service.ProvisionCloudIdentityRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the provision cloud identity method over gRPC.

        Creates a Cloud Identity for the given customer using the
        customer's information, or the information provided here.

        Possible error codes:

        - PERMISSION_DENIED:

          - The customer doesn't belong to the reseller.
          - You are not authorized to provision cloud identity id. See
            https://support.google.com/channelservices/answer/9759265

        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: The customer was not found.
        - ALREADY_EXISTS: The customer's primary email already exists.
          Retry after changing the customer's primary contact email.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        contains an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.ProvisionCloudIdentityRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "provision_cloud_identity" not in self._stubs:
            self._stubs["provision_cloud_identity"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ProvisionCloudIdentity",
                request_serializer=service.ProvisionCloudIdentityRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["provision_cloud_identity"]

    @property
    def list_entitlements(
        self,
    ) -> Callable[
        [service.ListEntitlementsRequest], Awaitable[service.ListEntitlementsResponse]
    ]:
        r"""Return a callable for the list entitlements method over gRPC.

        Lists [Entitlement][google.cloud.channel.v1.Entitlement]s
        belonging to a customer.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Return value: A list of the customer's
        [Entitlement][google.cloud.channel.v1.Entitlement]s.

        Returns:
            Callable[[~.ListEntitlementsRequest],
                    Awaitable[~.ListEntitlementsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entitlements" not in self._stubs:
            self._stubs["list_entitlements"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListEntitlements",
                request_serializer=service.ListEntitlementsRequest.serialize,
                response_deserializer=service.ListEntitlementsResponse.deserialize,
            )
        return self._stubs["list_entitlements"]

    @property
    def list_transferable_skus(
        self,
    ) -> Callable[
        [service.ListTransferableSkusRequest],
        Awaitable[service.ListTransferableSkusResponse],
    ]:
        r"""Return a callable for the list transferable skus method over gRPC.

        List [TransferableSku][google.cloud.channel.v1.TransferableSku]s
        of a customer based on the Cloud Identity ID or Customer Name in
        the request.

        Use this method to list the entitlements information of an
        unowned customer. You should provide the customer's Cloud
        Identity ID or Customer Name.

        Possible error codes:

        - PERMISSION_DENIED:

          - The customer doesn't belong to the reseller and has no auth
            token.
          - The supplied auth token is invalid.
          - The reseller account making the request is different from
            the reseller account in the query.

        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Return value: A list of the customer's
        [TransferableSku][google.cloud.channel.v1.TransferableSku].

        Returns:
            Callable[[~.ListTransferableSkusRequest],
                    Awaitable[~.ListTransferableSkusResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_transferable_skus" not in self._stubs:
            self._stubs["list_transferable_skus"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListTransferableSkus",
                request_serializer=service.ListTransferableSkusRequest.serialize,
                response_deserializer=service.ListTransferableSkusResponse.deserialize,
            )
        return self._stubs["list_transferable_skus"]

    @property
    def list_transferable_offers(
        self,
    ) -> Callable[
        [service.ListTransferableOffersRequest],
        Awaitable[service.ListTransferableOffersResponse],
    ]:
        r"""Return a callable for the list transferable offers method over gRPC.

        List
        [TransferableOffer][google.cloud.channel.v1.TransferableOffer]s
        of a customer based on Cloud Identity ID or Customer Name in the
        request.

        Use this method when a reseller gets the entitlement information
        of an unowned customer. The reseller should provide the
        customer's Cloud Identity ID or Customer Name.

        Possible error codes:

        - PERMISSION_DENIED:

          - The customer doesn't belong to the reseller and has no auth
            token.
          - The customer provided incorrect reseller information when
            generating auth token.
          - The reseller account making the request is different from
            the reseller account in the query.
          - The reseller is not authorized to transact on this Product.
            See
            https://support.google.com/channelservices/answer/9759265

        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Return value: List of
        [TransferableOffer][google.cloud.channel.v1.TransferableOffer]
        for the given customer and SKU.

        Returns:
            Callable[[~.ListTransferableOffersRequest],
                    Awaitable[~.ListTransferableOffersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_transferable_offers" not in self._stubs:
            self._stubs["list_transferable_offers"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListTransferableOffers",
                request_serializer=service.ListTransferableOffersRequest.serialize,
                response_deserializer=service.ListTransferableOffersResponse.deserialize,
            )
        return self._stubs["list_transferable_offers"]

    @property
    def get_entitlement(
        self,
    ) -> Callable[[service.GetEntitlementRequest], Awaitable[entitlements.Entitlement]]:
        r"""Return a callable for the get entitlement method over gRPC.

        Returns the requested
        [Entitlement][google.cloud.channel.v1.Entitlement] resource.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: The customer entitlement was not found.

        Return value: The requested
        [Entitlement][google.cloud.channel.v1.Entitlement] resource.

        Returns:
            Callable[[~.GetEntitlementRequest],
                    Awaitable[~.Entitlement]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entitlement" not in self._stubs:
            self._stubs["get_entitlement"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/GetEntitlement",
                request_serializer=service.GetEntitlementRequest.serialize,
                response_deserializer=entitlements.Entitlement.deserialize,
            )
        return self._stubs["get_entitlement"]

    @property
    def create_entitlement(
        self,
    ) -> Callable[
        [service.CreateEntitlementRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create entitlement method over gRPC.

        Creates an entitlement for a customer.

        Possible error codes:

        - PERMISSION_DENIED:

          - The customer doesn't belong to the reseller.
          - The reseller is not authorized to transact on this Product.
            See
            https://support.google.com/channelservices/answer/9759265

        - INVALID_ARGUMENT:

          - Required request parameters are missing or invalid.
          - There is already a customer entitlement for a SKU from the
            same product family.

        - INVALID_VALUE: Make sure the OfferId is valid. If it is,
          contact Google Channel support for further troubleshooting.
        - NOT_FOUND: The customer or offer resource was not found.
        - ALREADY_EXISTS:

          - The SKU was already purchased for the customer.
          - The customer's primary email already exists. Retry after
            changing the customer's primary contact email.

        - CONDITION_NOT_MET or FAILED_PRECONDITION:

          - The domain required for purchasing a SKU has not been
            verified.
          - A pre-requisite SKU required to purchase an Add-On SKU is
            missing. For example, Google Workspace Business Starter is
            required to purchase Vault or Drive.
          - (Developer accounts only) Reseller and resold domain must
            meet the following naming requirements:

            - Domain names must start with goog-test.
            - Domain names must include the reseller domain.

        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.CreateEntitlementRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entitlement" not in self._stubs:
            self._stubs["create_entitlement"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/CreateEntitlement",
                request_serializer=service.CreateEntitlementRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_entitlement"]

    @property
    def change_parameters(
        self,
    ) -> Callable[
        [service.ChangeParametersRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the change parameters method over gRPC.

        Change parameters of the entitlement.

        An entitlement update is a long-running operation and it updates
        the entitlement as a result of fulfillment.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid. For example, the number of seats being changed is
          greater than the allowed number of max seats, or decreasing
          seats for a commitment based plan.
        - NOT_FOUND: Entitlement resource not found.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.ChangeParametersRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "change_parameters" not in self._stubs:
            self._stubs["change_parameters"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ChangeParameters",
                request_serializer=service.ChangeParametersRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["change_parameters"]

    @property
    def change_renewal_settings(
        self,
    ) -> Callable[
        [service.ChangeRenewalSettingsRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the change renewal settings method over gRPC.

        Updates the renewal settings for an existing customer
        entitlement.

        An entitlement update is a long-running operation and it updates
        the entitlement as a result of fulfillment.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: Entitlement resource not found.
        - NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for
          a commitment plan. Can't enable or disable renewals for
          non-commitment plans.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.ChangeRenewalSettingsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "change_renewal_settings" not in self._stubs:
            self._stubs["change_renewal_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ChangeRenewalSettings",
                request_serializer=service.ChangeRenewalSettingsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["change_renewal_settings"]

    @property
    def change_offer(
        self,
    ) -> Callable[[service.ChangeOfferRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the change offer method over gRPC.

        Updates the Offer for an existing customer entitlement.

        An entitlement update is a long-running operation and it updates
        the entitlement as a result of fulfillment.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: Offer or Entitlement resource not found.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.ChangeOfferRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "change_offer" not in self._stubs:
            self._stubs["change_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ChangeOffer",
                request_serializer=service.ChangeOfferRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["change_offer"]

    @property
    def start_paid_service(
        self,
    ) -> Callable[
        [service.StartPaidServiceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the start paid service method over gRPC.

        Starts paid service for a trial entitlement.

        Starts paid service for a trial entitlement immediately. This
        method is only applicable if a plan is set up for a trial
        entitlement but has some trial days remaining.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: Entitlement resource not found.
        - FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for
          entitlement on trial plans.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.StartPaidServiceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_paid_service" not in self._stubs:
            self._stubs["start_paid_service"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/StartPaidService",
                request_serializer=service.StartPaidServiceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_paid_service"]

    @property
    def suspend_entitlement(
        self,
    ) -> Callable[
        [service.SuspendEntitlementRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the suspend entitlement method over gRPC.

        Suspends a previously fulfilled entitlement.

        An entitlement suspension is a long-running operation.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: Entitlement resource not found.
        - NOT_ACTIVE: Entitlement is not active.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.SuspendEntitlementRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "suspend_entitlement" not in self._stubs:
            self._stubs["suspend_entitlement"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/SuspendEntitlement",
                request_serializer=service.SuspendEntitlementRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["suspend_entitlement"]

    @property
    def cancel_entitlement(
        self,
    ) -> Callable[
        [service.CancelEntitlementRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the cancel entitlement method over gRPC.

        Cancels a previously fulfilled entitlement.

        An entitlement cancellation is a long-running operation.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - FAILED_PRECONDITION: There are Google Cloud projects linked to
          the Google Cloud entitlement's Cloud Billing subaccount.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: Entitlement resource not found.
        - DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google
          Workspace add-ons, or entitlements for Google Cloud's
          development platform.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The response will
        contain google.protobuf.Empty on success. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.CancelEntitlementRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_entitlement" not in self._stubs:
            self._stubs["cancel_entitlement"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/CancelEntitlement",
                request_serializer=service.CancelEntitlementRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["cancel_entitlement"]

    @property
    def activate_entitlement(
        self,
    ) -> Callable[
        [service.ActivateEntitlementRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the activate entitlement method over gRPC.

        Activates a previously suspended entitlement. Entitlements
        suspended for pending ToS acceptance can't be activated using
        this method.

        An entitlement activation is a long-running operation and it
        updates the state of the customer entitlement.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: Entitlement resource not found.
        - SUSPENSION_NOT_RESELLER_INITIATED: Can only activate
          reseller-initiated suspensions and entitlements that have
          accepted the TOS.
        - NOT_SUSPENDED: Can only activate suspended entitlements not in
          an ACTIVE state.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.ActivateEntitlementRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "activate_entitlement" not in self._stubs:
            self._stubs["activate_entitlement"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ActivateEntitlement",
                request_serializer=service.ActivateEntitlementRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["activate_entitlement"]

    @property
    def transfer_entitlements(
        self,
    ) -> Callable[
        [service.TransferEntitlementsRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the transfer entitlements method over gRPC.

        Transfers customer entitlements to new reseller.

        Possible error codes:

        - PERMISSION_DENIED:

          - The customer doesn't belong to the reseller.
          - The reseller is not authorized to transact on this Product.
            See
            https://support.google.com/channelservices/answer/9759265

        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: The customer or offer resource was not found.
        - ALREADY_EXISTS: The SKU was already transferred for the
          customer.
        - CONDITION_NOT_MET or FAILED_PRECONDITION:

          - The SKU requires domain verification to transfer, but the
            domain is not verified.
          - An Add-On SKU (example, Vault or Drive) is missing the
            pre-requisite SKU (example, G Suite Basic).
          - (Developer accounts only) Reseller and resold domain must
            meet the following naming requirements:

            - Domain names must start with goog-test.
            - Domain names must include the reseller domain.

          - Specify all transferring entitlements.

        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.TransferEntitlementsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "transfer_entitlements" not in self._stubs:
            self._stubs["transfer_entitlements"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/TransferEntitlements",
                request_serializer=service.TransferEntitlementsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["transfer_entitlements"]

    @property
    def transfer_entitlements_to_google(
        self,
    ) -> Callable[
        [service.TransferEntitlementsToGoogleRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the transfer entitlements to
        google method over gRPC.

        Transfers customer entitlements from their current reseller to
        Google.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: The customer or offer resource was not found.
        - ALREADY_EXISTS: The SKU was already transferred for the
          customer.
        - CONDITION_NOT_MET or FAILED_PRECONDITION:

          - The SKU requires domain verification to transfer, but the
            domain is not verified.
          - An Add-On SKU (example, Vault or Drive) is missing the
            pre-requisite SKU (example, G Suite Basic).
          - (Developer accounts only) Reseller and resold domain must
            meet the following naming requirements:

            - Domain names must start with goog-test.
            - Domain names must include the reseller domain.

        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The response will
        contain google.protobuf.Empty on success. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        Returns:
            Callable[[~.TransferEntitlementsToGoogleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "transfer_entitlements_to_google" not in self._stubs:
            self._stubs["transfer_entitlements_to_google"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/TransferEntitlementsToGoogle",
                    request_serializer=service.TransferEntitlementsToGoogleRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["transfer_entitlements_to_google"]

    @property
    def list_channel_partner_links(
        self,
    ) -> Callable[
        [service.ListChannelPartnerLinksRequest],
        Awaitable[service.ListChannelPartnerLinksResponse],
    ]:
        r"""Return a callable for the list channel partner links method over gRPC.

        List
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]s
        belonging to a distributor. You must be a distributor to call
        this method.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Return value: The list of the distributor account's
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resources.

        Returns:
            Callable[[~.ListChannelPartnerLinksRequest],
                    Awaitable[~.ListChannelPartnerLinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_channel_partner_links" not in self._stubs:
            self._stubs["list_channel_partner_links"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/ListChannelPartnerLinks",
                    request_serializer=service.ListChannelPartnerLinksRequest.serialize,
                    response_deserializer=service.ListChannelPartnerLinksResponse.deserialize,
                )
            )
        return self._stubs["list_channel_partner_links"]

    @property
    def get_channel_partner_link(
        self,
    ) -> Callable[
        [service.GetChannelPartnerLinkRequest],
        Awaitable[channel_partner_links.ChannelPartnerLink],
    ]:
        r"""Return a callable for the get channel partner link method over gRPC.

        Returns the requested
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource. You must be a distributor to call this method.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: ChannelPartnerLink resource not found because of an
          invalid channel partner link name.

        Return value: The
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource.

        Returns:
            Callable[[~.GetChannelPartnerLinkRequest],
                    Awaitable[~.ChannelPartnerLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_channel_partner_link" not in self._stubs:
            self._stubs["get_channel_partner_link"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/GetChannelPartnerLink",
                request_serializer=service.GetChannelPartnerLinkRequest.serialize,
                response_deserializer=channel_partner_links.ChannelPartnerLink.deserialize,
            )
        return self._stubs["get_channel_partner_link"]

    @property
    def create_channel_partner_link(
        self,
    ) -> Callable[
        [service.CreateChannelPartnerLinkRequest],
        Awaitable[channel_partner_links.ChannelPartnerLink],
    ]:
        r"""Return a callable for the create channel partner link method over gRPC.

        Initiates a channel partner link between a distributor and a
        reseller, or between resellers in an n-tier reseller channel.
        Invited partners need to follow the invite_link_uri provided in
        the response to accept. After accepting the invitation, a link
        is set up between the two parties. You must be a distributor to
        call this method.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - ALREADY_EXISTS: The ChannelPartnerLink sent in the request
          already exists.
        - NOT_FOUND: No Cloud Identity customer exists for provided
          domain.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The new
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource.

        Returns:
            Callable[[~.CreateChannelPartnerLinkRequest],
                    Awaitable[~.ChannelPartnerLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_channel_partner_link" not in self._stubs:
            self._stubs["create_channel_partner_link"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/CreateChannelPartnerLink",
                    request_serializer=service.CreateChannelPartnerLinkRequest.serialize,
                    response_deserializer=channel_partner_links.ChannelPartnerLink.deserialize,
                )
            )
        return self._stubs["create_channel_partner_link"]

    @property
    def update_channel_partner_link(
        self,
    ) -> Callable[
        [service.UpdateChannelPartnerLinkRequest],
        Awaitable[channel_partner_links.ChannelPartnerLink],
    ]:
        r"""Return a callable for the update channel partner link method over gRPC.

        Updates a channel partner link. Distributors call this method to
        change a link's status. For example, to suspend a partner link.
        You must be a distributor to call this method.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request is
          different from the reseller account in the API request.
        - INVALID_ARGUMENT:

          - Required request parameters are missing or invalid.
          - Link state cannot change from invited to active or
            suspended.
          - Cannot send reseller_cloud_identity_id, invite_url, or name
            in update mask.

        - NOT_FOUND: ChannelPartnerLink resource not found.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The updated
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource.

        Returns:
            Callable[[~.UpdateChannelPartnerLinkRequest],
                    Awaitable[~.ChannelPartnerLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_channel_partner_link" not in self._stubs:
            self._stubs["update_channel_partner_link"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/UpdateChannelPartnerLink",
                    request_serializer=service.UpdateChannelPartnerLinkRequest.serialize,
                    response_deserializer=channel_partner_links.ChannelPartnerLink.deserialize,
                )
            )
        return self._stubs["update_channel_partner_link"]

    @property
    def get_customer_repricing_config(
        self,
    ) -> Callable[
        [service.GetCustomerRepricingConfigRequest],
        Awaitable[repricing.CustomerRepricingConfig],
    ]:
        r"""Return a callable for the get customer repricing config method over gRPC.

        Gets information about how a Reseller modifies their bill before
        sending it to a Customer.

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different.
        - NOT_FOUND: The
          [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
          was not found.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.

        Returns:
            Callable[[~.GetCustomerRepricingConfigRequest],
                    Awaitable[~.CustomerRepricingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_customer_repricing_config" not in self._stubs:
            self._stubs["get_customer_repricing_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/GetCustomerRepricingConfig",
                    request_serializer=service.GetCustomerRepricingConfigRequest.serialize,
                    response_deserializer=repricing.CustomerRepricingConfig.deserialize,
                )
            )
        return self._stubs["get_customer_repricing_config"]

    @property
    def list_customer_repricing_configs(
        self,
    ) -> Callable[
        [service.ListCustomerRepricingConfigsRequest],
        Awaitable[service.ListCustomerRepricingConfigsResponse],
    ]:
        r"""Return a callable for the list customer repricing
        configs method over gRPC.

        Lists information about how a Reseller modifies their bill
        before sending it to a Customer.

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different.
        - NOT_FOUND: The
          [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
          specified does not exist or is not associated with the given
          account.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resources. The data for each resource is displayed in the
        ascending order of:

        - Customer ID
        - [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement]
        - [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        - [CustomerRepricingConfig.update_time][google.cloud.channel.v1.CustomerRepricingConfig.update_time]

        If unsuccessful, returns an error.

        Returns:
            Callable[[~.ListCustomerRepricingConfigsRequest],
                    Awaitable[~.ListCustomerRepricingConfigsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_customer_repricing_configs" not in self._stubs:
            self._stubs["list_customer_repricing_configs"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/ListCustomerRepricingConfigs",
                    request_serializer=service.ListCustomerRepricingConfigsRequest.serialize,
                    response_deserializer=service.ListCustomerRepricingConfigsResponse.deserialize,
                )
            )
        return self._stubs["list_customer_repricing_configs"]

    @property
    def create_customer_repricing_config(
        self,
    ) -> Callable[
        [service.CreateCustomerRepricingConfigRequest],
        Awaitable[repricing.CustomerRepricingConfig],
    ]:
        r"""Return a callable for the create customer repricing
        config method over gRPC.

        Creates a CustomerRepricingConfig. Call this method to set
        modifications for a specific customer's bill. You can only
        create configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. If needed, you can create a config for the
        current month, with some restrictions.

        When creating a config for a future month, make sure there are
        no existing configs for that
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        The following restrictions are for creating configs in the
        current month.

        - This functionality is reserved for recovering from an
          erroneous config, and should not be used for regular business
          cases.
        - The new config will not modify exports used with other
          configs. Changes to the config may be immediate, but may take
          up to 24 hours.
        - There is a limit of ten configs for any
          [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement],
          for any
          [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].
        - The contained
          [CustomerRepricingConfig.repricing_config][google.cloud.channel.v1.CustomerRepricingConfig.repricing_config]
          value must be different from the value used in the current
          config for a
          [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement].

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different.
        - INVALID_ARGUMENT: Missing or invalid required parameters in
          the request. Also displays if the updated config is for the
          current month or past months.
        - NOT_FOUND: The
          [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
          specified does not exist or is not associated with the given
          account.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the updated
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.

        Returns:
            Callable[[~.CreateCustomerRepricingConfigRequest],
                    Awaitable[~.CustomerRepricingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_customer_repricing_config" not in self._stubs:
            self._stubs["create_customer_repricing_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/CreateCustomerRepricingConfig",
                    request_serializer=service.CreateCustomerRepricingConfigRequest.serialize,
                    response_deserializer=repricing.CustomerRepricingConfig.deserialize,
                )
            )
        return self._stubs["create_customer_repricing_config"]

    @property
    def update_customer_repricing_config(
        self,
    ) -> Callable[
        [service.UpdateCustomerRepricingConfigRequest],
        Awaitable[repricing.CustomerRepricingConfig],
    ]:
        r"""Return a callable for the update customer repricing
        config method over gRPC.

        Updates a CustomerRepricingConfig. Call this method to set
        modifications for a specific customer's bill. This method
        overwrites the existing CustomerRepricingConfig.

        You can only update configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. To make changes to configs for the current
        month, use
        [CreateCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateCustomerRepricingConfig],
        taking note of its restrictions. You cannot update the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        When updating a config in the future:

        - This config must already exist.

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different.
        - INVALID_ARGUMENT: Missing or invalid required parameters in
          the request. Also displays if the updated config is for the
          current month or past months.
        - NOT_FOUND: The
          [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
          specified does not exist or is not associated with the given
          account.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the updated
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.

        Returns:
            Callable[[~.UpdateCustomerRepricingConfigRequest],
                    Awaitable[~.CustomerRepricingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_customer_repricing_config" not in self._stubs:
            self._stubs["update_customer_repricing_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/UpdateCustomerRepricingConfig",
                    request_serializer=service.UpdateCustomerRepricingConfigRequest.serialize,
                    response_deserializer=repricing.CustomerRepricingConfig.deserialize,
                )
            )
        return self._stubs["update_customer_repricing_config"]

    @property
    def delete_customer_repricing_config(
        self,
    ) -> Callable[
        [service.DeleteCustomerRepricingConfigRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete customer repricing
        config method over gRPC.

        Deletes the given
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        permanently. You can only delete configs if their
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is set to a date after the current month.

        Possible error codes:

        - PERMISSION_DENIED: The account making the request does not own
          this customer.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - FAILED_PRECONDITION: The
          [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
          is active or in the past.
        - NOT_FOUND: No
          [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
          found for the name in the request.

        Returns:
            Callable[[~.DeleteCustomerRepricingConfigRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_customer_repricing_config" not in self._stubs:
            self._stubs["delete_customer_repricing_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/DeleteCustomerRepricingConfig",
                    request_serializer=service.DeleteCustomerRepricingConfigRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_customer_repricing_config"]

    @property
    def get_channel_partner_repricing_config(
        self,
    ) -> Callable[
        [service.GetChannelPartnerRepricingConfigRequest],
        Awaitable[repricing.ChannelPartnerRepricingConfig],
    ]:
        r"""Return a callable for the get channel partner repricing
        config method over gRPC.

        Gets information about how a Distributor modifies their bill
        before sending it to a ChannelPartner.

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different.
        - NOT_FOUND: The
          [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
          was not found.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.

        Returns:
            Callable[[~.GetChannelPartnerRepricingConfigRequest],
                    Awaitable[~.ChannelPartnerRepricingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_channel_partner_repricing_config" not in self._stubs:
            self._stubs["get_channel_partner_repricing_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/GetChannelPartnerRepricingConfig",
                    request_serializer=service.GetChannelPartnerRepricingConfigRequest.serialize,
                    response_deserializer=repricing.ChannelPartnerRepricingConfig.deserialize,
                )
            )
        return self._stubs["get_channel_partner_repricing_config"]

    @property
    def list_channel_partner_repricing_configs(
        self,
    ) -> Callable[
        [service.ListChannelPartnerRepricingConfigsRequest],
        Awaitable[service.ListChannelPartnerRepricingConfigsResponse],
    ]:
        r"""Return a callable for the list channel partner repricing
        configs method over gRPC.

        Lists information about how a Reseller modifies their bill
        before sending it to a ChannelPartner.

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different.
        - NOT_FOUND: The
          [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
          specified does not exist or is not associated with the given
          account.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resources. The data for each resource is displayed in the
        ascending order of:

        - Channel Partner ID
        - [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        - [ChannelPartnerRepricingConfig.update_time][google.cloud.channel.v1.ChannelPartnerRepricingConfig.update_time]

        If unsuccessful, returns an error.

        Returns:
            Callable[[~.ListChannelPartnerRepricingConfigsRequest],
                    Awaitable[~.ListChannelPartnerRepricingConfigsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_channel_partner_repricing_configs" not in self._stubs:
            self._stubs["list_channel_partner_repricing_configs"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/ListChannelPartnerRepricingConfigs",
                    request_serializer=service.ListChannelPartnerRepricingConfigsRequest.serialize,
                    response_deserializer=service.ListChannelPartnerRepricingConfigsResponse.deserialize,
                )
            )
        return self._stubs["list_channel_partner_repricing_configs"]

    @property
    def create_channel_partner_repricing_config(
        self,
    ) -> Callable[
        [service.CreateChannelPartnerRepricingConfigRequest],
        Awaitable[repricing.ChannelPartnerRepricingConfig],
    ]:
        r"""Return a callable for the create channel partner
        repricing config method over gRPC.

        Creates a ChannelPartnerRepricingConfig. Call this method to set
        modifications for a specific ChannelPartner's bill. You can only
        create configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. If needed, you can create a config for the
        current month, with some restrictions.

        When creating a config for a future month, make sure there are
        no existing configs for that
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        The following restrictions are for creating configs in the
        current month.

        - This functionality is reserved for recovering from an
          erroneous config, and should not be used for regular business
          cases.
        - The new config will not modify exports used with other
          configs. Changes to the config may be immediate, but may take
          up to 24 hours.
        - There is a limit of ten configs for any ChannelPartner or
          [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement],
          for any
          [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].
        - The contained
          [ChannelPartnerRepricingConfig.repricing_config][google.cloud.channel.v1.ChannelPartnerRepricingConfig.repricing_config]
          value must be different from the value used in the current
          config for a ChannelPartner.

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different.
        - INVALID_ARGUMENT: Missing or invalid required parameters in
          the request. Also displays if the updated config is for the
          current month or past months.
        - NOT_FOUND: The
          [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
          specified does not exist or is not associated with the given
          account.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the updated
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.

        Returns:
            Callable[[~.CreateChannelPartnerRepricingConfigRequest],
                    Awaitable[~.ChannelPartnerRepricingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_channel_partner_repricing_config" not in self._stubs:
            self._stubs["create_channel_partner_repricing_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/CreateChannelPartnerRepricingConfig",
                    request_serializer=service.CreateChannelPartnerRepricingConfigRequest.serialize,
                    response_deserializer=repricing.ChannelPartnerRepricingConfig.deserialize,
                )
            )
        return self._stubs["create_channel_partner_repricing_config"]

    @property
    def update_channel_partner_repricing_config(
        self,
    ) -> Callable[
        [service.UpdateChannelPartnerRepricingConfigRequest],
        Awaitable[repricing.ChannelPartnerRepricingConfig],
    ]:
        r"""Return a callable for the update channel partner
        repricing config method over gRPC.

        Updates a ChannelPartnerRepricingConfig. Call this method to set
        modifications for a specific ChannelPartner's bill. This method
        overwrites the existing CustomerRepricingConfig.

        You can only update configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. To make changes to configs for the current
        month, use
        [CreateChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerRepricingConfig],
        taking note of its restrictions. You cannot update the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        When updating a config in the future:

        - This config must already exist.

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different.
        - INVALID_ARGUMENT: Missing or invalid required parameters in
          the request. Also displays if the updated config is for the
          current month or past months.
        - NOT_FOUND: The
          [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
          specified does not exist or is not associated with the given
          account.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the updated
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.

        Returns:
            Callable[[~.UpdateChannelPartnerRepricingConfigRequest],
                    Awaitable[~.ChannelPartnerRepricingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_channel_partner_repricing_config" not in self._stubs:
            self._stubs["update_channel_partner_repricing_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/UpdateChannelPartnerRepricingConfig",
                    request_serializer=service.UpdateChannelPartnerRepricingConfigRequest.serialize,
                    response_deserializer=repricing.ChannelPartnerRepricingConfig.deserialize,
                )
            )
        return self._stubs["update_channel_partner_repricing_config"]

    @property
    def delete_channel_partner_repricing_config(
        self,
    ) -> Callable[
        [service.DeleteChannelPartnerRepricingConfigRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete channel partner
        repricing config method over gRPC.

        Deletes the given
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        permanently. You can only delete configs if their
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is set to a date after the current month.

        Possible error codes:

        - PERMISSION_DENIED: The account making the request does not own
          this customer.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - FAILED_PRECONDITION: The
          [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
          is active or in the past.
        - NOT_FOUND: No
          [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
          found for the name in the request.

        Returns:
            Callable[[~.DeleteChannelPartnerRepricingConfigRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_channel_partner_repricing_config" not in self._stubs:
            self._stubs["delete_channel_partner_repricing_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/DeleteChannelPartnerRepricingConfig",
                    request_serializer=service.DeleteChannelPartnerRepricingConfigRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_channel_partner_repricing_config"]

    @property
    def list_sku_groups(
        self,
    ) -> Callable[
        [service.ListSkuGroupsRequest], Awaitable[service.ListSkuGroupsResponse]
    ]:
        r"""Return a callable for the list sku groups method over gRPC.

        Lists the Rebilling supported SKU groups the account is
        authorized to sell. Reference:
        https://cloud.google.com/skus/sku-groups

        Possible Error Codes:

        - PERMISSION_DENIED: If the account making the request and the
          account being queried are different, or the account doesn't
          exist.
        - INTERNAL: Any non-user error related to technical issues in
          the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [SkuGroup][google.cloud.channel.v1.SkuGroup] resources. The data
        for each resource is displayed in the alphabetical order of SKU
        group display name. The data for each resource is displayed in
        the ascending order of
        [SkuGroup.display_name][google.cloud.channel.v1.SkuGroup.display_name]

        If unsuccessful, returns an error.

        Returns:
            Callable[[~.ListSkuGroupsRequest],
                    Awaitable[~.ListSkuGroupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sku_groups" not in self._stubs:
            self._stubs["list_sku_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListSkuGroups",
                request_serializer=service.ListSkuGroupsRequest.serialize,
                response_deserializer=service.ListSkuGroupsResponse.deserialize,
            )
        return self._stubs["list_sku_groups"]

    @property
    def list_sku_group_billable_skus(
        self,
    ) -> Callable[
        [service.ListSkuGroupBillableSkusRequest],
        Awaitable[service.ListSkuGroupBillableSkusResponse],
    ]:
        r"""Return a callable for the list sku group billable skus method over gRPC.

        Lists the Billable SKUs in a given SKU group.

        Possible error codes: PERMISSION_DENIED: If the account making
        the request and the account being queried for are different, or
        the account doesn't exist. INVALID_ARGUMENT: Missing or invalid
        required parameters in the request. INTERNAL: Any non-user error
        related to technical issue in the backend. In this case, contact
        cloud channel support.

        Return Value: If successful, the
        [BillableSku][google.cloud.channel.v1.BillableSku] resources.
        The data for each resource is displayed in the ascending order
        of:

        - [BillableSku.service_display_name][google.cloud.channel.v1.BillableSku.service_display_name]
        - [BillableSku.sku_display_name][google.cloud.channel.v1.BillableSku.sku_display_name]

        If unsuccessful, returns an error.

        Returns:
            Callable[[~.ListSkuGroupBillableSkusRequest],
                    Awaitable[~.ListSkuGroupBillableSkusResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sku_group_billable_skus" not in self._stubs:
            self._stubs["list_sku_group_billable_skus"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/ListSkuGroupBillableSkus",
                    request_serializer=service.ListSkuGroupBillableSkusRequest.serialize,
                    response_deserializer=service.ListSkuGroupBillableSkusResponse.deserialize,
                )
            )
        return self._stubs["list_sku_group_billable_skus"]

    @property
    def lookup_offer(
        self,
    ) -> Callable[[service.LookupOfferRequest], Awaitable[offers.Offer]]:
        r"""Return a callable for the lookup offer method over gRPC.

        Returns the requested [Offer][google.cloud.channel.v1.Offer]
        resource.

        Possible error codes:

        - PERMISSION_DENIED: The entitlement doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: Entitlement or offer was not found.

        Return value: The [Offer][google.cloud.channel.v1.Offer]
        resource.

        Returns:
            Callable[[~.LookupOfferRequest],
                    Awaitable[~.Offer]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_offer" not in self._stubs:
            self._stubs["lookup_offer"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/LookupOffer",
                request_serializer=service.LookupOfferRequest.serialize,
                response_deserializer=offers.Offer.deserialize,
            )
        return self._stubs["lookup_offer"]

    @property
    def list_products(
        self,
    ) -> Callable[
        [service.ListProductsRequest], Awaitable[service.ListProductsResponse]
    ]:
        r"""Return a callable for the list products method over gRPC.

        Lists the Products the reseller is authorized to sell.

        Possible error codes:

        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Returns:
            Callable[[~.ListProductsRequest],
                    Awaitable[~.ListProductsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_products" not in self._stubs:
            self._stubs["list_products"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListProducts",
                request_serializer=service.ListProductsRequest.serialize,
                response_deserializer=service.ListProductsResponse.deserialize,
            )
        return self._stubs["list_products"]

    @property
    def list_skus(
        self,
    ) -> Callable[[service.ListSkusRequest], Awaitable[service.ListSkusResponse]]:
        r"""Return a callable for the list skus method over gRPC.

        Lists the SKUs for a product the reseller is authorized to sell.

        Possible error codes:

        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Returns:
            Callable[[~.ListSkusRequest],
                    Awaitable[~.ListSkusResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_skus" not in self._stubs:
            self._stubs["list_skus"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListSkus",
                request_serializer=service.ListSkusRequest.serialize,
                response_deserializer=service.ListSkusResponse.deserialize,
            )
        return self._stubs["list_skus"]

    @property
    def list_offers(
        self,
    ) -> Callable[[service.ListOffersRequest], Awaitable[service.ListOffersResponse]]:
        r"""Return a callable for the list offers method over gRPC.

        Lists the Offers the reseller can sell.

        Possible error codes:

        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Returns:
            Callable[[~.ListOffersRequest],
                    Awaitable[~.ListOffersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_offers" not in self._stubs:
            self._stubs["list_offers"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListOffers",
                request_serializer=service.ListOffersRequest.serialize,
                response_deserializer=service.ListOffersResponse.deserialize,
            )
        return self._stubs["list_offers"]

    @property
    def list_purchasable_skus(
        self,
    ) -> Callable[
        [service.ListPurchasableSkusRequest],
        Awaitable[service.ListPurchasableSkusResponse],
    ]:
        r"""Return a callable for the list purchasable skus method over gRPC.

        Lists the following:

        - SKUs that you can purchase for a customer
        - SKUs that you can upgrade or downgrade for an entitlement.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Returns:
            Callable[[~.ListPurchasableSkusRequest],
                    Awaitable[~.ListPurchasableSkusResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_purchasable_skus" not in self._stubs:
            self._stubs["list_purchasable_skus"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListPurchasableSkus",
                request_serializer=service.ListPurchasableSkusRequest.serialize,
                response_deserializer=service.ListPurchasableSkusResponse.deserialize,
            )
        return self._stubs["list_purchasable_skus"]

    @property
    def list_purchasable_offers(
        self,
    ) -> Callable[
        [service.ListPurchasableOffersRequest],
        Awaitable[service.ListPurchasableOffersResponse],
    ]:
        r"""Return a callable for the list purchasable offers method over gRPC.

        Lists the following:

        - Offers that you can purchase for a customer.
        - Offers that you can change for an entitlement.

        Possible error codes:

        - PERMISSION_DENIED:

          - The customer doesn't belong to the reseller
          - The reseller is not authorized to transact on this Product.
            See
            https://support.google.com/channelservices/answer/9759265

        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Returns:
            Callable[[~.ListPurchasableOffersRequest],
                    Awaitable[~.ListPurchasableOffersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_purchasable_offers" not in self._stubs:
            self._stubs["list_purchasable_offers"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListPurchasableOffers",
                request_serializer=service.ListPurchasableOffersRequest.serialize,
                response_deserializer=service.ListPurchasableOffersResponse.deserialize,
            )
        return self._stubs["list_purchasable_offers"]

    @property
    def query_eligible_billing_accounts(
        self,
    ) -> Callable[
        [service.QueryEligibleBillingAccountsRequest],
        Awaitable[service.QueryEligibleBillingAccountsResponse],
    ]:
        r"""Return a callable for the query eligible billing
        accounts method over gRPC.

        Lists the billing accounts that are eligible to purchase
        particular SKUs for a given customer.

        Possible error codes:

        - PERMISSION_DENIED: The customer doesn't belong to the
          reseller.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.

        Return value: Based on the provided list of SKUs, returns a list
        of SKU groups that must be purchased using the same billing
        account and the billing accounts eligible to purchase each SKU
        group.

        Returns:
            Callable[[~.QueryEligibleBillingAccountsRequest],
                    Awaitable[~.QueryEligibleBillingAccountsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_eligible_billing_accounts" not in self._stubs:
            self._stubs["query_eligible_billing_accounts"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.channel.v1.CloudChannelService/QueryEligibleBillingAccounts",
                    request_serializer=service.QueryEligibleBillingAccountsRequest.serialize,
                    response_deserializer=service.QueryEligibleBillingAccountsResponse.deserialize,
                )
            )
        return self._stubs["query_eligible_billing_accounts"]

    @property
    def register_subscriber(
        self,
    ) -> Callable[
        [service.RegisterSubscriberRequest],
        Awaitable[service.RegisterSubscriberResponse],
    ]:
        r"""Return a callable for the register subscriber method over gRPC.

        Registers a service account with subscriber privileges on the
        Pub/Sub topic for this Channel Services account or integrator.
        After you create a subscriber, you get the events through
        [SubscriberEvent][google.cloud.channel.v1.SubscriberEvent]

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request and
          the provided reseller account are different, or the
          impersonated user is not a super admin.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The topic name with the registered service email
        address.

        Returns:
            Callable[[~.RegisterSubscriberRequest],
                    Awaitable[~.RegisterSubscriberResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "register_subscriber" not in self._stubs:
            self._stubs["register_subscriber"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/RegisterSubscriber",
                request_serializer=service.RegisterSubscriberRequest.serialize,
                response_deserializer=service.RegisterSubscriberResponse.deserialize,
            )
        return self._stubs["register_subscriber"]

    @property
    def unregister_subscriber(
        self,
    ) -> Callable[
        [service.UnregisterSubscriberRequest],
        Awaitable[service.UnregisterSubscriberResponse],
    ]:
        r"""Return a callable for the unregister subscriber method over gRPC.

        Unregisters a service account with subscriber privileges on the
        Pub/Sub topic created for this Channel Services account or
        integrator. If there are no service accounts left with
        subscriber privileges, this deletes the topic. You can call
        ListSubscribers to check for these accounts.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request and
          the provided reseller account are different, or the
          impersonated user is not a super admin.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: The topic resource doesn't exist.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: The topic name that unregistered the service email
        address. Returns a success response if the service email address
        wasn't registered with the topic.

        Returns:
            Callable[[~.UnregisterSubscriberRequest],
                    Awaitable[~.UnregisterSubscriberResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "unregister_subscriber" not in self._stubs:
            self._stubs["unregister_subscriber"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/UnregisterSubscriber",
                request_serializer=service.UnregisterSubscriberRequest.serialize,
                response_deserializer=service.UnregisterSubscriberResponse.deserialize,
            )
        return self._stubs["unregister_subscriber"]

    @property
    def list_subscribers(
        self,
    ) -> Callable[
        [service.ListSubscribersRequest], Awaitable[service.ListSubscribersResponse]
    ]:
        r"""Return a callable for the list subscribers method over gRPC.

        Lists service accounts with subscriber privileges on the Pub/Sub
        topic created for this Channel Services account or integrator.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request and
          the provided reseller account are different, or the
          impersonated user is not a super admin.
        - INVALID_ARGUMENT: Required request parameters are missing or
          invalid.
        - NOT_FOUND: The topic resource doesn't exist.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. Contact Cloud Channel support.

        Return value: A list of service email addresses.

        Returns:
            Callable[[~.ListSubscribersRequest],
                    Awaitable[~.ListSubscribersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_subscribers" not in self._stubs:
            self._stubs["list_subscribers"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListSubscribers",
                request_serializer=service.ListSubscribersRequest.serialize,
                response_deserializer=service.ListSubscribersResponse.deserialize,
            )
        return self._stubs["list_subscribers"]

    @property
    def list_entitlement_changes(
        self,
    ) -> Callable[
        [service.ListEntitlementChangesRequest],
        Awaitable[service.ListEntitlementChangesResponse],
    ]:
        r"""Return a callable for the list entitlement changes method over gRPC.

        List entitlement history.

        Possible error codes:

        - PERMISSION_DENIED: The reseller account making the request and
          the provided reseller account are different.
        - INVALID_ARGUMENT: Missing or invalid required fields in the
          request.
        - NOT_FOUND: The parent resource doesn't exist. Usually the
          result of an invalid name parameter.
        - INTERNAL: Any non-user error related to a technical issue in
          the backend. In this case, contact CloudChannel support.
        - UNKNOWN: Any non-user error related to a technical issue in
          the backend. In this case, contact Cloud Channel support.

        Return value: List of
        [EntitlementChange][google.cloud.channel.v1.EntitlementChange]s.

        Returns:
            Callable[[~.ListEntitlementChangesRequest],
                    Awaitable[~.ListEntitlementChangesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entitlement_changes" not in self._stubs:
            self._stubs["list_entitlement_changes"] = self._logged_channel.unary_unary(
                "/google.cloud.channel.v1.CloudChannelService/ListEntitlementChanges",
                request_serializer=service.ListEntitlementChangesRequest.serialize,
                response_deserializer=service.ListEntitlementChangesResponse.deserialize,
            )
        return self._stubs["list_entitlement_changes"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_customers: self._wrap_method(
                self.list_customers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_customer: self._wrap_method(
                self.get_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.check_cloud_identity_accounts_exist: self._wrap_method(
                self.check_cloud_identity_accounts_exist,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_customer: self._wrap_method(
                self.create_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_customer: self._wrap_method(
                self.update_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_customer: self._wrap_method(
                self.delete_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_customer: self._wrap_method(
                self.import_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.provision_cloud_identity: self._wrap_method(
                self.provision_cloud_identity,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_entitlements: self._wrap_method(
                self.list_entitlements,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_transferable_skus: self._wrap_method(
                self.list_transferable_skus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_transferable_offers: self._wrap_method(
                self.list_transferable_offers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entitlement: self._wrap_method(
                self.get_entitlement,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entitlement: self._wrap_method(
                self.create_entitlement,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.change_parameters: self._wrap_method(
                self.change_parameters,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.change_renewal_settings: self._wrap_method(
                self.change_renewal_settings,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.change_offer: self._wrap_method(
                self.change_offer,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.start_paid_service: self._wrap_method(
                self.start_paid_service,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.suspend_entitlement: self._wrap_method(
                self.suspend_entitlement,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.cancel_entitlement: self._wrap_method(
                self.cancel_entitlement,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.activate_entitlement: self._wrap_method(
                self.activate_entitlement,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.transfer_entitlements: self._wrap_method(
                self.transfer_entitlements,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.transfer_entitlements_to_google: self._wrap_method(
                self.transfer_entitlements_to_google,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_channel_partner_links: self._wrap_method(
                self.list_channel_partner_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_channel_partner_link: self._wrap_method(
                self.get_channel_partner_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_channel_partner_link: self._wrap_method(
                self.create_channel_partner_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_channel_partner_link: self._wrap_method(
                self.update_channel_partner_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_customer_repricing_config: self._wrap_method(
                self.get_customer_repricing_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_customer_repricing_configs: self._wrap_method(
                self.list_customer_repricing_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_customer_repricing_config: self._wrap_method(
                self.create_customer_repricing_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_customer_repricing_config: self._wrap_method(
                self.update_customer_repricing_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_customer_repricing_config: self._wrap_method(
                self.delete_customer_repricing_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_channel_partner_repricing_config: self._wrap_method(
                self.get_channel_partner_repricing_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_channel_partner_repricing_configs: self._wrap_method(
                self.list_channel_partner_repricing_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_channel_partner_repricing_config: self._wrap_method(
                self.create_channel_partner_repricing_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_channel_partner_repricing_config: self._wrap_method(
                self.update_channel_partner_repricing_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_channel_partner_repricing_config: self._wrap_method(
                self.delete_channel_partner_repricing_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_sku_groups: self._wrap_method(
                self.list_sku_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_sku_group_billable_skus: self._wrap_method(
                self.list_sku_group_billable_skus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.lookup_offer: self._wrap_method(
                self.lookup_offer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_products: self._wrap_method(
                self.list_products,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_skus: self._wrap_method(
                self.list_skus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_offers: self._wrap_method(
                self.list_offers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_purchasable_skus: self._wrap_method(
                self.list_purchasable_skus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_purchasable_offers: self._wrap_method(
                self.list_purchasable_offers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_eligible_billing_accounts: self._wrap_method(
                self.query_eligible_billing_accounts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.register_subscriber: self._wrap_method(
                self.register_subscriber,
                default_timeout=None,
                client_info=client_info,
            ),
            self.unregister_subscriber: self._wrap_method(
                self.unregister_subscriber,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subscribers: self._wrap_method(
                self.list_subscribers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entitlement_changes: self._wrap_method(
                self.list_entitlement_changes,
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


__all__ = ("CloudChannelServiceGrpcAsyncIOTransport",)
