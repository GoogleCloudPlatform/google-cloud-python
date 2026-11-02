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
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.ads.marketingplatform_admin_v1alpha.types import (
    marketingplatform_admin,
    resources,
)

from .base import DEFAULT_CLIENT_INFO, MarketingplatformAdminServiceTransport
from .grpc import MarketingplatformAdminServiceGrpcTransport

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
                    "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
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
                    "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class MarketingplatformAdminServiceGrpcAsyncIOTransport(
    MarketingplatformAdminServiceTransport
):
    """gRPC AsyncIO backend transport for MarketingplatformAdminService.

    Service Interface for the Google Marketing Platform Admin
    API.

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
        host: str = "marketingplatformadmin.googleapis.com",
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
        host: str = "marketingplatformadmin.googleapis.com",
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
                 The hostname to connect to (default: 'marketingplatformadmin.googleapis.com').
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
    def get_organization(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetOrganizationRequest],
        Awaitable[resources.Organization],
    ]:
        r"""Return a callable for the get organization method over gRPC.

        Looks up a single organization.

        Returns:
            Callable[[~.GetOrganizationRequest],
                    Awaitable[~.Organization]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_organization" not in self._stubs:
            self._stubs["get_organization"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/GetOrganization",
                request_serializer=marketingplatform_admin.GetOrganizationRequest.serialize,
                response_deserializer=resources.Organization.deserialize,
            )
        return self._stubs["get_organization"]

    @property
    def list_organizations(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListOrganizationsRequest],
        Awaitable[marketingplatform_admin.ListOrganizationsResponse],
    ]:
        r"""Return a callable for the list organizations method over gRPC.

        Returns a list of organizations that the user has
        access to.

        Returns:
            Callable[[~.ListOrganizationsRequest],
                    Awaitable[~.ListOrganizationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_organizations" not in self._stubs:
            self._stubs["list_organizations"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/ListOrganizations",
                request_serializer=marketingplatform_admin.ListOrganizationsRequest.serialize,
                response_deserializer=marketingplatform_admin.ListOrganizationsResponse.deserialize,
            )
        return self._stubs["list_organizations"]

    @property
    def find_sales_partner_managed_clients(
        self,
    ) -> Callable[
        [marketingplatform_admin.FindSalesPartnerManagedClientsRequest],
        Awaitable[marketingplatform_admin.FindSalesPartnerManagedClientsResponse],
    ]:
        r"""Return a callable for the find sales partner managed
        clients method over gRPC.

        Returns a list of clients managed by the sales
        partner organization.
        User needs to be an OrgAdmin/BillingAdmin on the sales
        partner organization in order to view the end clients.

        Returns:
            Callable[[~.FindSalesPartnerManagedClientsRequest],
                    Awaitable[~.FindSalesPartnerManagedClientsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "find_sales_partner_managed_clients" not in self._stubs:
            self._stubs["find_sales_partner_managed_clients"] = (
                self._logged_channel.unary_unary(
                    "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/FindSalesPartnerManagedClients",
                    request_serializer=marketingplatform_admin.FindSalesPartnerManagedClientsRequest.serialize,
                    response_deserializer=marketingplatform_admin.FindSalesPartnerManagedClientsResponse.deserialize,
                )
            )
        return self._stubs["find_sales_partner_managed_clients"]

    @property
    def list_analytics_account_links(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListAnalyticsAccountLinksRequest],
        Awaitable[marketingplatform_admin.ListAnalyticsAccountLinksResponse],
    ]:
        r"""Return a callable for the list analytics account links method over gRPC.

        Lists the Google Analytics accounts link to the
        specified Google Marketing Platform organization.

        Returns:
            Callable[[~.ListAnalyticsAccountLinksRequest],
                    Awaitable[~.ListAnalyticsAccountLinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_analytics_account_links" not in self._stubs:
            self._stubs["list_analytics_account_links"] = (
                self._logged_channel.unary_unary(
                    "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/ListAnalyticsAccountLinks",
                    request_serializer=marketingplatform_admin.ListAnalyticsAccountLinksRequest.serialize,
                    response_deserializer=marketingplatform_admin.ListAnalyticsAccountLinksResponse.deserialize,
                )
            )
        return self._stubs["list_analytics_account_links"]

    @property
    def create_analytics_account_link(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateAnalyticsAccountLinkRequest],
        Awaitable[resources.AnalyticsAccountLink],
    ]:
        r"""Return a callable for the create analytics account link method over gRPC.

        Creates the link between the Analytics account and
        the Google Marketing Platform organization.

        User needs to be an org user, and admin on the Analytics
        account to create the link. If the account is already
        linked to an organization, user needs to unlink the
        account from the current organization, then try link
        again.

        Returns:
            Callable[[~.CreateAnalyticsAccountLinkRequest],
                    Awaitable[~.AnalyticsAccountLink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_analytics_account_link" not in self._stubs:
            self._stubs["create_analytics_account_link"] = (
                self._logged_channel.unary_unary(
                    "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/CreateAnalyticsAccountLink",
                    request_serializer=marketingplatform_admin.CreateAnalyticsAccountLinkRequest.serialize,
                    response_deserializer=resources.AnalyticsAccountLink.deserialize,
                )
            )
        return self._stubs["create_analytics_account_link"]

    @property
    def delete_analytics_account_link(
        self,
    ) -> Callable[
        [marketingplatform_admin.DeleteAnalyticsAccountLinkRequest],
        Awaitable[empty_pb2.Empty],
    ]:
        r"""Return a callable for the delete analytics account link method over gRPC.

        Deletes the AnalyticsAccountLink, which detaches the
        Analytics account from the Google Marketing Platform
        organization.

        User needs to be an org user, and admin on the Analytics
        account in order to delete the link.

        Returns:
            Callable[[~.DeleteAnalyticsAccountLinkRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_analytics_account_link" not in self._stubs:
            self._stubs["delete_analytics_account_link"] = (
                self._logged_channel.unary_unary(
                    "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/DeleteAnalyticsAccountLink",
                    request_serializer=marketingplatform_admin.DeleteAnalyticsAccountLinkRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_analytics_account_link"]

    @property
    def set_property_service_level(
        self,
    ) -> Callable[
        [marketingplatform_admin.SetPropertyServiceLevelRequest],
        Awaitable[marketingplatform_admin.SetPropertyServiceLevelResponse],
    ]:
        r"""Return a callable for the set property service level method over gRPC.

        Updates the service level for an Analytics property.

        Returns:
            Callable[[~.SetPropertyServiceLevelRequest],
                    Awaitable[~.SetPropertyServiceLevelResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_property_service_level" not in self._stubs:
            self._stubs["set_property_service_level"] = (
                self._logged_channel.unary_unary(
                    "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/SetPropertyServiceLevel",
                    request_serializer=marketingplatform_admin.SetPropertyServiceLevelRequest.serialize,
                    response_deserializer=marketingplatform_admin.SetPropertyServiceLevelResponse.deserialize,
                )
            )
        return self._stubs["set_property_service_level"]

    @property
    def report_property_usage(
        self,
    ) -> Callable[
        [marketingplatform_admin.ReportPropertyUsageRequest],
        Awaitable[marketingplatform_admin.ReportPropertyUsageResponse],
    ]:
        r"""Return a callable for the report property usage method over gRPC.

        Gets the usage and billing data for properties within
        the organization for the specified month.

        Per direct client org, user needs to be
        OrgAdmin/BillingAdmin on the organization in order to
        view the billing and usage data.

        Per sales partner client org, user needs to be
        OrgAdmin/BillingAdmin on the sales partner org in order
        to view the billing and usage data, or
        OrgAdmin/BillingAdmin on the sales partner client org in
        order to view the usage data only.

        Returns:
            Callable[[~.ReportPropertyUsageRequest],
                    Awaitable[~.ReportPropertyUsageResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "report_property_usage" not in self._stubs:
            self._stubs["report_property_usage"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/ReportPropertyUsage",
                request_serializer=marketingplatform_admin.ReportPropertyUsageRequest.serialize,
                response_deserializer=marketingplatform_admin.ReportPropertyUsageResponse.deserialize,
            )
        return self._stubs["report_property_usage"]

    @property
    def get_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetUserGroupRequest], Awaitable[resources.UserGroup]
    ]:
        r"""Return a callable for the get user group method over gRPC.

        Looks up a single user group.

        Returns:
            Callable[[~.GetUserGroupRequest],
                    Awaitable[~.UserGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_user_group" not in self._stubs:
            self._stubs["get_user_group"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/GetUserGroup",
                request_serializer=marketingplatform_admin.GetUserGroupRequest.serialize,
                response_deserializer=resources.UserGroup.deserialize,
            )
        return self._stubs["get_user_group"]

    @property
    def list_user_groups(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListUserGroupsRequest],
        Awaitable[marketingplatform_admin.ListUserGroupsResponse],
    ]:
        r"""Return a callable for the list user groups method over gRPC.

        Returns a list of user groups in the specified GMP
        organization.

        Returns:
            Callable[[~.ListUserGroupsRequest],
                    Awaitable[~.ListUserGroupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_user_groups" not in self._stubs:
            self._stubs["list_user_groups"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/ListUserGroups",
                request_serializer=marketingplatform_admin.ListUserGroupsRequest.serialize,
                response_deserializer=marketingplatform_admin.ListUserGroupsResponse.deserialize,
            )
        return self._stubs["list_user_groups"]

    @property
    def create_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateUserGroupRequest], Awaitable[resources.UserGroup]
    ]:
        r"""Return a callable for the create user group method over gRPC.

        Creates a user group in the specified GMP
        organization.

        Returns:
            Callable[[~.CreateUserGroupRequest],
                    Awaitable[~.UserGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_user_group" not in self._stubs:
            self._stubs["create_user_group"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/CreateUserGroup",
                request_serializer=marketingplatform_admin.CreateUserGroupRequest.serialize,
                response_deserializer=resources.UserGroup.deserialize,
            )
        return self._stubs["create_user_group"]

    @property
    def update_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateUserGroupRequest], Awaitable[resources.UserGroup]
    ]:
        r"""Return a callable for the update user group method over gRPC.

        Updates a user group in the specified GMP
        organization.

        Returns:
            Callable[[~.UpdateUserGroupRequest],
                    Awaitable[~.UserGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_user_group" not in self._stubs:
            self._stubs["update_user_group"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/UpdateUserGroup",
                request_serializer=marketingplatform_admin.UpdateUserGroupRequest.serialize,
                response_deserializer=resources.UserGroup.deserialize,
            )
        return self._stubs["update_user_group"]

    @property
    def delete_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.DeleteUserGroupRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete user group method over gRPC.

        Deletes a user group in the specified GMP
        organization.

        Returns:
            Callable[[~.DeleteUserGroupRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_user_group" not in self._stubs:
            self._stubs["delete_user_group"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/DeleteUserGroup",
                request_serializer=marketingplatform_admin.DeleteUserGroupRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_user_group"]

    @property
    def get_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetUserGroupMemberRequest],
        Awaitable[resources.UserGroupMember],
    ]:
        r"""Return a callable for the get user group member method over gRPC.

        Looks up a single user group member.

        Returns:
            Callable[[~.GetUserGroupMemberRequest],
                    Awaitable[~.UserGroupMember]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_user_group_member" not in self._stubs:
            self._stubs["get_user_group_member"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/GetUserGroupMember",
                request_serializer=marketingplatform_admin.GetUserGroupMemberRequest.serialize,
                response_deserializer=resources.UserGroupMember.deserialize,
            )
        return self._stubs["get_user_group_member"]

    @property
    def list_user_group_members(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListUserGroupMembersRequest],
        Awaitable[marketingplatform_admin.ListUserGroupMembersResponse],
    ]:
        r"""Return a callable for the list user group members method over gRPC.

        Returns a list of members in the specified user
        group.

        Returns:
            Callable[[~.ListUserGroupMembersRequest],
                    Awaitable[~.ListUserGroupMembersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_user_group_members" not in self._stubs:
            self._stubs["list_user_group_members"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/ListUserGroupMembers",
                request_serializer=marketingplatform_admin.ListUserGroupMembersRequest.serialize,
                response_deserializer=marketingplatform_admin.ListUserGroupMembersResponse.deserialize,
            )
        return self._stubs["list_user_group_members"]

    @property
    def create_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateUserGroupMemberRequest],
        Awaitable[resources.UserGroupMember],
    ]:
        r"""Return a callable for the create user group member method over gRPC.

        Adds a member to the specified GMP user group.

        Returns:
            Callable[[~.CreateUserGroupMemberRequest],
                    Awaitable[~.UserGroupMember]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_user_group_member" not in self._stubs:
            self._stubs["create_user_group_member"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/CreateUserGroupMember",
                request_serializer=marketingplatform_admin.CreateUserGroupMemberRequest.serialize,
                response_deserializer=resources.UserGroupMember.deserialize,
            )
        return self._stubs["create_user_group_member"]

    @property
    def update_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateUserGroupMemberRequest],
        Awaitable[resources.UserGroupMember],
    ]:
        r"""Return a callable for the update user group member method over gRPC.

        Updates a member in the specified GMP user group.

        Returns:
            Callable[[~.UpdateUserGroupMemberRequest],
                    Awaitable[~.UserGroupMember]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_user_group_member" not in self._stubs:
            self._stubs["update_user_group_member"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/UpdateUserGroupMember",
                request_serializer=marketingplatform_admin.UpdateUserGroupMemberRequest.serialize,
                response_deserializer=resources.UserGroupMember.deserialize,
            )
        return self._stubs["update_user_group_member"]

    @property
    def delete_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.DeleteUserGroupMemberRequest],
        Awaitable[empty_pb2.Empty],
    ]:
        r"""Return a callable for the delete user group member method over gRPC.

        Deletes a member in the specified GMP user group.

        Returns:
            Callable[[~.DeleteUserGroupMemberRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_user_group_member" not in self._stubs:
            self._stubs["delete_user_group_member"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/DeleteUserGroupMember",
                request_serializer=marketingplatform_admin.DeleteUserGroupMemberRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_user_group_member"]

    @property
    def get_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetAdminAccessBindingRequest],
        Awaitable[resources.AdminAccessBinding],
    ]:
        r"""Return a callable for the get admin access binding method over gRPC.

        Looks up a single admin access binding.

        Returns:
            Callable[[~.GetAdminAccessBindingRequest],
                    Awaitable[~.AdminAccessBinding]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_admin_access_binding" not in self._stubs:
            self._stubs["get_admin_access_binding"] = self._logged_channel.unary_unary(
                "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/GetAdminAccessBinding",
                request_serializer=marketingplatform_admin.GetAdminAccessBindingRequest.serialize,
                response_deserializer=resources.AdminAccessBinding.deserialize,
            )
        return self._stubs["get_admin_access_binding"]

    @property
    def list_admin_access_bindings(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListAdminAccessBindingsRequest],
        Awaitable[marketingplatform_admin.ListAdminAccessBindingsResponse],
    ]:
        r"""Return a callable for the list admin access bindings method over gRPC.

        Returns a list of admin access bindings in the
        specified GMP organization.

        Returns:
            Callable[[~.ListAdminAccessBindingsRequest],
                    Awaitable[~.ListAdminAccessBindingsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_admin_access_bindings" not in self._stubs:
            self._stubs["list_admin_access_bindings"] = (
                self._logged_channel.unary_unary(
                    "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/ListAdminAccessBindings",
                    request_serializer=marketingplatform_admin.ListAdminAccessBindingsRequest.serialize,
                    response_deserializer=marketingplatform_admin.ListAdminAccessBindingsResponse.deserialize,
                )
            )
        return self._stubs["list_admin_access_bindings"]

    @property
    def create_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateAdminAccessBindingRequest],
        Awaitable[resources.AdminAccessBinding],
    ]:
        r"""Return a callable for the create admin access binding method over gRPC.

        Creates an admin access binding in the specified GMP
        organization.

        Returns:
            Callable[[~.CreateAdminAccessBindingRequest],
                    Awaitable[~.AdminAccessBinding]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_admin_access_binding" not in self._stubs:
            self._stubs["create_admin_access_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/CreateAdminAccessBinding",
                    request_serializer=marketingplatform_admin.CreateAdminAccessBindingRequest.serialize,
                    response_deserializer=resources.AdminAccessBinding.deserialize,
                )
            )
        return self._stubs["create_admin_access_binding"]

    @property
    def update_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateAdminAccessBindingRequest],
        Awaitable[resources.AdminAccessBinding],
    ]:
        r"""Return a callable for the update admin access binding method over gRPC.

        Updates an admin access binding in the specified GMP
        organization.

        Returns:
            Callable[[~.UpdateAdminAccessBindingRequest],
                    Awaitable[~.AdminAccessBinding]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_admin_access_binding" not in self._stubs:
            self._stubs["update_admin_access_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.marketingplatform.admin.v1alpha.MarketingplatformAdminService/UpdateAdminAccessBinding",
                    request_serializer=marketingplatform_admin.UpdateAdminAccessBindingRequest.serialize,
                    response_deserializer=resources.AdminAccessBinding.deserialize,
                )
            )
        return self._stubs["update_admin_access_binding"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.get_organization: self._wrap_method(
                self.get_organization,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_organizations: self._wrap_method(
                self.list_organizations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.find_sales_partner_managed_clients: self._wrap_method(
                self.find_sales_partner_managed_clients,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_analytics_account_links: self._wrap_method(
                self.list_analytics_account_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_analytics_account_link: self._wrap_method(
                self.create_analytics_account_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_analytics_account_link: self._wrap_method(
                self.delete_analytics_account_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_property_service_level: self._wrap_method(
                self.set_property_service_level,
                default_timeout=None,
                client_info=client_info,
            ),
            self.report_property_usage: self._wrap_method(
                self.report_property_usage,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_user_group: self._wrap_method(
                self.get_user_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_user_groups: self._wrap_method(
                self.list_user_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_user_group: self._wrap_method(
                self.create_user_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_user_group: self._wrap_method(
                self.update_user_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_user_group: self._wrap_method(
                self.delete_user_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_user_group_member: self._wrap_method(
                self.get_user_group_member,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_user_group_members: self._wrap_method(
                self.list_user_group_members,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_user_group_member: self._wrap_method(
                self.create_user_group_member,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_user_group_member: self._wrap_method(
                self.update_user_group_member,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_user_group_member: self._wrap_method(
                self.delete_user_group_member,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_admin_access_binding: self._wrap_method(
                self.get_admin_access_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_admin_access_bindings: self._wrap_method(
                self.list_admin_access_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_admin_access_binding: self._wrap_method(
                self.create_admin_access_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_admin_access_binding: self._wrap_method(
                self.update_admin_access_binding,
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


__all__ = ("MarketingplatformAdminServiceGrpcAsyncIOTransport",)
