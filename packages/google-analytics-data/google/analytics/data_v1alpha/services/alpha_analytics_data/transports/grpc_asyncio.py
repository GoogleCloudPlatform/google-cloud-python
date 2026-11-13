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

from google.analytics.data_v1alpha.types import analytics_data_api

from .base import DEFAULT_CLIENT_INFO, AlphaAnalyticsDataTransport
from .grpc import AlphaAnalyticsDataGrpcTransport

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
                    "serviceName": "google.analytics.data.v1alpha.AlphaAnalyticsData",
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
                    "serviceName": "google.analytics.data.v1alpha.AlphaAnalyticsData",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AlphaAnalyticsDataGrpcAsyncIOTransport(AlphaAnalyticsDataTransport):
    """gRPC AsyncIO backend transport for AlphaAnalyticsData.

    Google Analytics reporting data service.

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
        host: str = "analyticsdata.googleapis.com",
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
        host: str = "analyticsdata.googleapis.com",
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
                 The hostname to connect to (default: 'analyticsdata.googleapis.com').
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
    def run_funnel_report(
        self,
    ) -> Callable[
        [analytics_data_api.RunFunnelReportRequest],
        Awaitable[analytics_data_api.RunFunnelReportResponse],
    ]:
        r"""Return a callable for the run funnel report method over gRPC.

        Returns a customized funnel report of your Google Analytics
        event data. The data returned from the API is as a table with
        columns for the requested dimensions and metrics.

        Funnel exploration lets you visualize the steps your users take
        to complete a task and quickly see how well they are succeeding
        or failing at each step. For example, how do prospects become
        shoppers and then become buyers? How do one time buyers become
        repeat buyers? With this information, you can improve
        inefficient or abandoned customer journeys. To learn more, see
        `GA4 Funnel
        Explorations <https://support.google.com/analytics/answer/9327974>`__.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Data API Funnel Reporting
        Feedback <https://docs.google.com/forms/d/e/1FAIpQLSdwOlQDJAUoBiIgUZZ3S_Lwi8gr7Bb0k1jhvc-DEg7Rol3UjA/viewform>`__.

        Returns:
            Callable[[~.RunFunnelReportRequest],
                    Awaitable[~.RunFunnelReportResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "run_funnel_report" not in self._stubs:
            self._stubs["run_funnel_report"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/RunFunnelReport",
                request_serializer=analytics_data_api.RunFunnelReportRequest.serialize,
                response_deserializer=analytics_data_api.RunFunnelReportResponse.deserialize,
            )
        return self._stubs["run_funnel_report"]

    @property
    def create_audience_list(
        self,
    ) -> Callable[
        [analytics_data_api.CreateAudienceListRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create audience list method over gRPC.

        Creates an audience list for later retrieval. This method
        quickly returns the audience list's resource name and initiates
        a long running asynchronous request to form an audience list. To
        list the users in an audience list, first create the audience
        list through this method and then send the audience resource
        name to the ``QueryAudienceList`` method.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        An audience list is a snapshot of the users currently in the
        audience at the time of audience list creation. Creating
        audience lists for one audience on different days will return
        different results as users enter and exit the audience.

        Audiences in Google Analytics 4 allow you to segment your users
        in the ways that are important to your business. To learn more,
        see https://support.google.com/analytics/answer/9267572.
        Audience lists contain the users in each audience.

        This method is available at beta stability at
        `audienceExports.create <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/create>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        Returns:
            Callable[[~.CreateAudienceListRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_audience_list" not in self._stubs:
            self._stubs["create_audience_list"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/CreateAudienceList",
                request_serializer=analytics_data_api.CreateAudienceListRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_audience_list"]

    @property
    def query_audience_list(
        self,
    ) -> Callable[
        [analytics_data_api.QueryAudienceListRequest],
        Awaitable[analytics_data_api.QueryAudienceListResponse],
    ]:
        r"""Return a callable for the query audience list method over gRPC.

        Retrieves an audience list of users. After creating an audience,
        the users are not immediately available for listing. First, a
        request to ``CreateAudienceList`` is necessary to create an
        audience list of users, and then second, this method is used to
        retrieve the users in the audience list.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        Audiences in Google Analytics 4 allow you to segment your users
        in the ways that are important to your business. To learn more,
        see https://support.google.com/analytics/answer/9267572.

        This method is available at beta stability at
        `audienceExports.query <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/query>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        Returns:
            Callable[[~.QueryAudienceListRequest],
                    Awaitable[~.QueryAudienceListResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_audience_list" not in self._stubs:
            self._stubs["query_audience_list"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/QueryAudienceList",
                request_serializer=analytics_data_api.QueryAudienceListRequest.serialize,
                response_deserializer=analytics_data_api.QueryAudienceListResponse.deserialize,
            )
        return self._stubs["query_audience_list"]

    @property
    def get_audience_list(
        self,
    ) -> Callable[
        [analytics_data_api.GetAudienceListRequest],
        Awaitable[analytics_data_api.AudienceList],
    ]:
        r"""Return a callable for the get audience list method over gRPC.

        Gets configuration metadata about a specific audience list. This
        method can be used to understand an audience list after it has
        been created.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        This method is available at beta stability at
        `audienceExports.get <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/get>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        Returns:
            Callable[[~.GetAudienceListRequest],
                    Awaitable[~.AudienceList]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_audience_list" not in self._stubs:
            self._stubs["get_audience_list"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/GetAudienceList",
                request_serializer=analytics_data_api.GetAudienceListRequest.serialize,
                response_deserializer=analytics_data_api.AudienceList.deserialize,
            )
        return self._stubs["get_audience_list"]

    @property
    def list_audience_lists(
        self,
    ) -> Callable[
        [analytics_data_api.ListAudienceListsRequest],
        Awaitable[analytics_data_api.ListAudienceListsResponse],
    ]:
        r"""Return a callable for the list audience lists method over gRPC.

        Lists all audience lists for a property. This method can be used
        for you to find and reuse existing audience lists rather than
        creating unnecessary new audience lists. The same audience can
        have multiple audience lists that represent the list of users
        that were in an audience on different days.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        This method is available at beta stability at
        `audienceExports.list <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/list>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        Returns:
            Callable[[~.ListAudienceListsRequest],
                    Awaitable[~.ListAudienceListsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_audience_lists" not in self._stubs:
            self._stubs["list_audience_lists"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/ListAudienceLists",
                request_serializer=analytics_data_api.ListAudienceListsRequest.serialize,
                response_deserializer=analytics_data_api.ListAudienceListsResponse.deserialize,
            )
        return self._stubs["list_audience_lists"]

    @property
    def create_recurring_audience_list(
        self,
    ) -> Callable[
        [analytics_data_api.CreateRecurringAudienceListRequest],
        Awaitable[analytics_data_api.RecurringAudienceList],
    ]:
        r"""Return a callable for the create recurring audience list method over gRPC.

        Creates a recurring audience list. Recurring audience lists
        produces new audience lists each day. Audience lists are users
        in an audience at the time of the list's creation.

        A recurring audience list ensures that you have audience list
        based on the most recent data available for use each day. If you
        manually create audience list, you don't know when an audience
        list based on an additional day's data is available. This
        recurring audience list automates the creation of an audience
        list when an additional day's data is available. You will
        consume fewer quota tokens by using recurring audience list
        versus manually creating audience list at various times of day
        trying to guess when an additional day's data is ready.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        Returns:
            Callable[[~.CreateRecurringAudienceListRequest],
                    Awaitable[~.RecurringAudienceList]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_recurring_audience_list" not in self._stubs:
            self._stubs["create_recurring_audience_list"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.data.v1alpha.AlphaAnalyticsData/CreateRecurringAudienceList",
                    request_serializer=analytics_data_api.CreateRecurringAudienceListRequest.serialize,
                    response_deserializer=analytics_data_api.RecurringAudienceList.deserialize,
                )
            )
        return self._stubs["create_recurring_audience_list"]

    @property
    def get_recurring_audience_list(
        self,
    ) -> Callable[
        [analytics_data_api.GetRecurringAudienceListRequest],
        Awaitable[analytics_data_api.RecurringAudienceList],
    ]:
        r"""Return a callable for the get recurring audience list method over gRPC.

        Gets configuration metadata about a specific recurring audience
        list. This method can be used to understand a recurring audience
        list's state after it has been created. For example, a recurring
        audience list resource will generate audience list instances for
        each day, and this method can be used to get the resource name
        of the most recent audience list instance.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        Returns:
            Callable[[~.GetRecurringAudienceListRequest],
                    Awaitable[~.RecurringAudienceList]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_recurring_audience_list" not in self._stubs:
            self._stubs["get_recurring_audience_list"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.data.v1alpha.AlphaAnalyticsData/GetRecurringAudienceList",
                    request_serializer=analytics_data_api.GetRecurringAudienceListRequest.serialize,
                    response_deserializer=analytics_data_api.RecurringAudienceList.deserialize,
                )
            )
        return self._stubs["get_recurring_audience_list"]

    @property
    def list_recurring_audience_lists(
        self,
    ) -> Callable[
        [analytics_data_api.ListRecurringAudienceListsRequest],
        Awaitable[analytics_data_api.ListRecurringAudienceListsResponse],
    ]:
        r"""Return a callable for the list recurring audience lists method over gRPC.

        Lists all recurring audience lists for a property. This method
        can be used for you to find and reuse existing recurring
        audience lists rather than creating unnecessary new recurring
        audience lists. The same audience can have multiple recurring
        audience lists that represent different dimension combinations;
        for example, just the dimension ``deviceId`` or both the
        dimensions ``deviceId`` and ``userId``.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        Returns:
            Callable[[~.ListRecurringAudienceListsRequest],
                    Awaitable[~.ListRecurringAudienceListsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_recurring_audience_lists" not in self._stubs:
            self._stubs["list_recurring_audience_lists"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.data.v1alpha.AlphaAnalyticsData/ListRecurringAudienceLists",
                    request_serializer=analytics_data_api.ListRecurringAudienceListsRequest.serialize,
                    response_deserializer=analytics_data_api.ListRecurringAudienceListsResponse.deserialize,
                )
            )
        return self._stubs["list_recurring_audience_lists"]

    @property
    def get_property_quotas_snapshot(
        self,
    ) -> Callable[
        [analytics_data_api.GetPropertyQuotasSnapshotRequest],
        Awaitable[analytics_data_api.PropertyQuotasSnapshot],
    ]:
        r"""Return a callable for the get property quotas snapshot method over gRPC.

        Get all property quotas organized by quota category
        for a given property. This will charge 1 property quota
        from the category with the most quota.

        Returns:
            Callable[[~.GetPropertyQuotasSnapshotRequest],
                    Awaitable[~.PropertyQuotasSnapshot]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_property_quotas_snapshot" not in self._stubs:
            self._stubs["get_property_quotas_snapshot"] = (
                self._logged_channel.unary_unary(
                    "/google.analytics.data.v1alpha.AlphaAnalyticsData/GetPropertyQuotasSnapshot",
                    request_serializer=analytics_data_api.GetPropertyQuotasSnapshotRequest.serialize,
                    response_deserializer=analytics_data_api.PropertyQuotasSnapshot.deserialize,
                )
            )
        return self._stubs["get_property_quotas_snapshot"]

    @property
    def create_report_task(
        self,
    ) -> Callable[
        [analytics_data_api.CreateReportTaskRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create report task method over gRPC.

        Initiates the creation of a report task. This method
        quickly returns a report task and initiates a long
        running asynchronous request to form a customized report
        of your Google Analytics event data.

        A report task will be retained and available for
        querying for 72 hours after it has been created.

        A report task created by one user can be listed and
        queried by all users who have access to the property.

        Returns:
            Callable[[~.CreateReportTaskRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_report_task" not in self._stubs:
            self._stubs["create_report_task"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/CreateReportTask",
                request_serializer=analytics_data_api.CreateReportTaskRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_report_task"]

    @property
    def query_report_task(
        self,
    ) -> Callable[
        [analytics_data_api.QueryReportTaskRequest],
        Awaitable[analytics_data_api.QueryReportTaskResponse],
    ]:
        r"""Return a callable for the query report task method over gRPC.

        Retrieves a report task's content. After requesting the
        ``CreateReportTask``, you are able to retrieve the report
        content once the report is ACTIVE. This method will return an
        error if the report task's state is not ``ACTIVE``. A query
        response will return the tabular row & column values of the
        report.

        Returns:
            Callable[[~.QueryReportTaskRequest],
                    Awaitable[~.QueryReportTaskResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_report_task" not in self._stubs:
            self._stubs["query_report_task"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/QueryReportTask",
                request_serializer=analytics_data_api.QueryReportTaskRequest.serialize,
                response_deserializer=analytics_data_api.QueryReportTaskResponse.deserialize,
            )
        return self._stubs["query_report_task"]

    @property
    def get_report_task(
        self,
    ) -> Callable[
        [analytics_data_api.GetReportTaskRequest],
        Awaitable[analytics_data_api.ReportTask],
    ]:
        r"""Return a callable for the get report task method over gRPC.

        Gets report metadata about a specific report task.
        After creating a report task, use this method to check
        its processing state or inspect its report definition.

        Returns:
            Callable[[~.GetReportTaskRequest],
                    Awaitable[~.ReportTask]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_report_task" not in self._stubs:
            self._stubs["get_report_task"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/GetReportTask",
                request_serializer=analytics_data_api.GetReportTaskRequest.serialize,
                response_deserializer=analytics_data_api.ReportTask.deserialize,
            )
        return self._stubs["get_report_task"]

    @property
    def list_report_tasks(
        self,
    ) -> Callable[
        [analytics_data_api.ListReportTasksRequest],
        Awaitable[analytics_data_api.ListReportTasksResponse],
    ]:
        r"""Return a callable for the list report tasks method over gRPC.

        Lists all report tasks for a property.

        Returns:
            Callable[[~.ListReportTasksRequest],
                    Awaitable[~.ListReportTasksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_report_tasks" not in self._stubs:
            self._stubs["list_report_tasks"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/ListReportTasks",
                request_serializer=analytics_data_api.ListReportTasksRequest.serialize,
                response_deserializer=analytics_data_api.ListReportTasksResponse.deserialize,
            )
        return self._stubs["list_report_tasks"]

    @property
    def chat(
        self,
    ) -> Callable[
        [analytics_data_api.ChatRequest], Awaitable[analytics_data_api.ChatResponse]
    ]:
        r"""Return a callable for the chat method over gRPC.

        Provides a chat interface for interacting with Google Analytics
        data through the API.

        This product uses AI and may display inaccurate info. Your chat
        activity may be used to improve the product and your use is
        subject to Google's
        `Terms <https://policies.google.com/terms>`__, `AI Use
        Policy <https://policies.google.com/terms/generative-ai/use-policy>`__,
        and `Privacy Policy <https://policies.google.com/privacy>`__.
        `Learn more about Chat AI
        Privacy <https://support.google.com/helpguide/answer/14185196>`__.

        Returns:
            Callable[[~.ChatRequest],
                    Awaitable[~.ChatResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "chat" not in self._stubs:
            self._stubs["chat"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/Chat",
                request_serializer=analytics_data_api.ChatRequest.serialize,
                response_deserializer=analytics_data_api.ChatResponse.deserialize,
            )
        return self._stubs["chat"]

    @property
    def run_report(
        self,
    ) -> Callable[
        [analytics_data_api.RunReportRequest],
        Awaitable[analytics_data_api.RunReportResponse],
    ]:
        r"""Return a callable for the run report method over gRPC.

        Returns a customized report of your Google Analytics
        event data. Reports contain statistics derived from data
        collected by the Google Analytics tracking code. The
        data returned from the API is as a table with columns
        for the requested dimensions and metrics. Metrics are
        individual measurements of user activity on your
        property, such as active users or event count.
        Dimensions break down metrics across some common
        criteria, such as country or event name.

        Returns:
            Callable[[~.RunReportRequest],
                    Awaitable[~.RunReportResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "run_report" not in self._stubs:
            self._stubs["run_report"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/RunReport",
                request_serializer=analytics_data_api.RunReportRequest.serialize,
                response_deserializer=analytics_data_api.RunReportResponse.deserialize,
            )
        return self._stubs["run_report"]

    @property
    def get_metadata(
        self,
    ) -> Callable[
        [analytics_data_api.GetMetadataRequest], Awaitable[analytics_data_api.Metadata]
    ]:
        r"""Return a callable for the get metadata method over gRPC.

        Returns metadata for dimensions and metrics available in
        reporting methods. Used to explore the dimensions and metrics.
        In this method, a Google Analytics property identifier is
        specified in the request, and the metadata response includes
        Custom dimensions and metrics as well as Universal metadata.

        For example if a custom metric with parameter name
        ``levels_unlocked`` is registered to a property, the Metadata
        response will contain ``customEvent:levels_unlocked``. Universal
        metadata are dimensions and metrics applicable to any property
        such as ``country`` and ``totalUsers``.

        Returns:
            Callable[[~.GetMetadataRequest],
                    Awaitable[~.Metadata]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_metadata" not in self._stubs:
            self._stubs["get_metadata"] = self._logged_channel.unary_unary(
                "/google.analytics.data.v1alpha.AlphaAnalyticsData/GetMetadata",
                request_serializer=analytics_data_api.GetMetadataRequest.serialize,
                response_deserializer=analytics_data_api.Metadata.deserialize,
            )
        return self._stubs["get_metadata"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.run_funnel_report: self._wrap_method(
                self.run_funnel_report,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_audience_list: self._wrap_method(
                self.create_audience_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_audience_list: self._wrap_method(
                self.query_audience_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_audience_list: self._wrap_method(
                self.get_audience_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_audience_lists: self._wrap_method(
                self.list_audience_lists,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_recurring_audience_list: self._wrap_method(
                self.create_recurring_audience_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_recurring_audience_list: self._wrap_method(
                self.get_recurring_audience_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_recurring_audience_lists: self._wrap_method(
                self.list_recurring_audience_lists,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_property_quotas_snapshot: self._wrap_method(
                self.get_property_quotas_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_report_task: self._wrap_method(
                self.create_report_task,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_report_task: self._wrap_method(
                self.query_report_task,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_report_task: self._wrap_method(
                self.get_report_task,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_report_tasks: self._wrap_method(
                self.list_report_tasks,
                default_timeout=None,
                client_info=client_info,
            ),
            self.chat: self._wrap_method(
                self.chat,
                default_timeout=None,
                client_info=client_info,
            ),
            self.run_report: self._wrap_method(
                self.run_report,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_metadata: self._wrap_method(
                self.get_metadata,
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


__all__ = ("AlphaAnalyticsDataGrpcAsyncIOTransport",)
