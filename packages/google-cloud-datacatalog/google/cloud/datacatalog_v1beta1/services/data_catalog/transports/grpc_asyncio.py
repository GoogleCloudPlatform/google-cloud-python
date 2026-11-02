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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.datacatalog_v1beta1.types import datacatalog, tags

from .base import DEFAULT_CLIENT_INFO, DataCatalogTransport
from .grpc import DataCatalogGrpcTransport

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
                    "serviceName": "google.cloud.datacatalog.v1beta1.DataCatalog",
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
                    "serviceName": "google.cloud.datacatalog.v1beta1.DataCatalog",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DataCatalogGrpcAsyncIOTransport(DataCatalogTransport):
    """gRPC AsyncIO backend transport for DataCatalog.

    Deprecated: Please use Dataplex Catalog instead.

    Data Catalog API service allows clients to discover, understand,
    and manage their data.

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
        host: str = "datacatalog.googleapis.com",
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
        host: str = "datacatalog.googleapis.com",
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
                 The hostname to connect to (default: 'datacatalog.googleapis.com').
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
    def search_catalog(
        self,
    ) -> Callable[
        [datacatalog.SearchCatalogRequest], Awaitable[datacatalog.SearchCatalogResponse]
    ]:
        r"""Return a callable for the search catalog method over gRPC.

        Searches Data Catalog for multiple resources like entries, tags
        that match a query.

        This is a custom method
        (https://cloud.google.com/apis/design/custom_methods) and does
        not return the complete resource, only the resource identifier
        and high level fields. Clients can subsequently call ``Get``
        methods.

        Note that Data Catalog search queries do not guarantee full
        recall. Query results that match your query may not be returned,
        even in subsequent result pages. Also note that results returned
        (and not returned) can vary across repeated search queries.

        See `Data Catalog Search
        Syntax <https://cloud.google.com/data-catalog/docs/how-to/search-reference>`__
        for more information.

        Returns:
            Callable[[~.SearchCatalogRequest],
                    Awaitable[~.SearchCatalogResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_catalog" not in self._stubs:
            self._stubs["search_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/SearchCatalog",
                request_serializer=datacatalog.SearchCatalogRequest.serialize,
                response_deserializer=datacatalog.SearchCatalogResponse.deserialize,
            )
        return self._stubs["search_catalog"]

    @property
    def create_entry_group(
        self,
    ) -> Callable[
        [datacatalog.CreateEntryGroupRequest], Awaitable[datacatalog.EntryGroup]
    ]:
        r"""Return a callable for the create entry group method over gRPC.

        A maximum of 10,000 entry groups may be created per organization
        across all locations.

        Users should enable the Data Catalog API in the project
        identified by the ``parent`` parameter (see [Data Catalog
        Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.CreateEntryGroupRequest],
                    Awaitable[~.EntryGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entry_group" not in self._stubs:
            self._stubs["create_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/CreateEntryGroup",
                request_serializer=datacatalog.CreateEntryGroupRequest.serialize,
                response_deserializer=datacatalog.EntryGroup.deserialize,
            )
        return self._stubs["create_entry_group"]

    @property
    def update_entry_group(
        self,
    ) -> Callable[
        [datacatalog.UpdateEntryGroupRequest], Awaitable[datacatalog.EntryGroup]
    ]:
        r"""Return a callable for the update entry group method over gRPC.

        Updates an EntryGroup. The user should enable the Data Catalog
        API in the project identified by the ``entry_group.name``
        parameter (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.UpdateEntryGroupRequest],
                    Awaitable[~.EntryGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entry_group" not in self._stubs:
            self._stubs["update_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateEntryGroup",
                request_serializer=datacatalog.UpdateEntryGroupRequest.serialize,
                response_deserializer=datacatalog.EntryGroup.deserialize,
            )
        return self._stubs["update_entry_group"]

    @property
    def get_entry_group(
        self,
    ) -> Callable[
        [datacatalog.GetEntryGroupRequest], Awaitable[datacatalog.EntryGroup]
    ]:
        r"""Return a callable for the get entry group method over gRPC.

        Gets an EntryGroup.

        Returns:
            Callable[[~.GetEntryGroupRequest],
                    Awaitable[~.EntryGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entry_group" not in self._stubs:
            self._stubs["get_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/GetEntryGroup",
                request_serializer=datacatalog.GetEntryGroupRequest.serialize,
                response_deserializer=datacatalog.EntryGroup.deserialize,
            )
        return self._stubs["get_entry_group"]

    @property
    def delete_entry_group(
        self,
    ) -> Callable[[datacatalog.DeleteEntryGroupRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete entry group method over gRPC.

        Deletes an EntryGroup. Only entry groups that do not contain
        entries can be deleted. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.DeleteEntryGroupRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entry_group" not in self._stubs:
            self._stubs["delete_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteEntryGroup",
                request_serializer=datacatalog.DeleteEntryGroupRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_entry_group"]

    @property
    def list_entry_groups(
        self,
    ) -> Callable[
        [datacatalog.ListEntryGroupsRequest],
        Awaitable[datacatalog.ListEntryGroupsResponse],
    ]:
        r"""Return a callable for the list entry groups method over gRPC.

        Lists entry groups.

        Returns:
            Callable[[~.ListEntryGroupsRequest],
                    Awaitable[~.ListEntryGroupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entry_groups" not in self._stubs:
            self._stubs["list_entry_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/ListEntryGroups",
                request_serializer=datacatalog.ListEntryGroupsRequest.serialize,
                response_deserializer=datacatalog.ListEntryGroupsResponse.deserialize,
            )
        return self._stubs["list_entry_groups"]

    @property
    def create_entry(
        self,
    ) -> Callable[[datacatalog.CreateEntryRequest], Awaitable[datacatalog.Entry]]:
        r"""Return a callable for the create entry method over gRPC.

        Creates an entry. Only entries of 'FILESET' type or
        user-specified type can be created.

        Users should enable the Data Catalog API in the project
        identified by the ``parent`` parameter (see [Data Catalog
        Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        A maximum of 100,000 entries may be created per entry group.

        Returns:
            Callable[[~.CreateEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entry" not in self._stubs:
            self._stubs["create_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/CreateEntry",
                request_serializer=datacatalog.CreateEntryRequest.serialize,
                response_deserializer=datacatalog.Entry.deserialize,
            )
        return self._stubs["create_entry"]

    @property
    def update_entry(
        self,
    ) -> Callable[[datacatalog.UpdateEntryRequest], Awaitable[datacatalog.Entry]]:
        r"""Return a callable for the update entry method over gRPC.

        Updates an existing entry. Users should enable the Data Catalog
        API in the project identified by the ``entry.name`` parameter
        (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.UpdateEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entry" not in self._stubs:
            self._stubs["update_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateEntry",
                request_serializer=datacatalog.UpdateEntryRequest.serialize,
                response_deserializer=datacatalog.Entry.deserialize,
            )
        return self._stubs["update_entry"]

    @property
    def delete_entry(
        self,
    ) -> Callable[[datacatalog.DeleteEntryRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete entry method over gRPC.

        Deletes an existing entry. Only entries created through
        [CreateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntry]
        method can be deleted. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.DeleteEntryRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entry" not in self._stubs:
            self._stubs["delete_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteEntry",
                request_serializer=datacatalog.DeleteEntryRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_entry"]

    @property
    def get_entry(
        self,
    ) -> Callable[[datacatalog.GetEntryRequest], Awaitable[datacatalog.Entry]]:
        r"""Return a callable for the get entry method over gRPC.

        Gets an entry.

        Returns:
            Callable[[~.GetEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entry" not in self._stubs:
            self._stubs["get_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/GetEntry",
                request_serializer=datacatalog.GetEntryRequest.serialize,
                response_deserializer=datacatalog.Entry.deserialize,
            )
        return self._stubs["get_entry"]

    @property
    def lookup_entry(
        self,
    ) -> Callable[[datacatalog.LookupEntryRequest], Awaitable[datacatalog.Entry]]:
        r"""Return a callable for the lookup entry method over gRPC.

        Get an entry by target resource name. This method
        allows clients to use the resource name from the source
        Google Cloud Platform service to get the Data Catalog
        Entry.

        Returns:
            Callable[[~.LookupEntryRequest],
                    Awaitable[~.Entry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_entry" not in self._stubs:
            self._stubs["lookup_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/LookupEntry",
                request_serializer=datacatalog.LookupEntryRequest.serialize,
                response_deserializer=datacatalog.Entry.deserialize,
            )
        return self._stubs["lookup_entry"]

    @property
    def list_entries(
        self,
    ) -> Callable[
        [datacatalog.ListEntriesRequest], Awaitable[datacatalog.ListEntriesResponse]
    ]:
        r"""Return a callable for the list entries method over gRPC.

        Lists entries.

        Returns:
            Callable[[~.ListEntriesRequest],
                    Awaitable[~.ListEntriesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entries" not in self._stubs:
            self._stubs["list_entries"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/ListEntries",
                request_serializer=datacatalog.ListEntriesRequest.serialize,
                response_deserializer=datacatalog.ListEntriesResponse.deserialize,
            )
        return self._stubs["list_entries"]

    @property
    def create_tag_template(
        self,
    ) -> Callable[[datacatalog.CreateTagTemplateRequest], Awaitable[tags.TagTemplate]]:
        r"""Return a callable for the create tag template method over gRPC.

        Creates a tag template. The user should enable the Data Catalog
        API in the project identified by the ``parent`` parameter (see
        `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        Returns:
            Callable[[~.CreateTagTemplateRequest],
                    Awaitable[~.TagTemplate]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tag_template" not in self._stubs:
            self._stubs["create_tag_template"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTagTemplate",
                request_serializer=datacatalog.CreateTagTemplateRequest.serialize,
                response_deserializer=tags.TagTemplate.deserialize,
            )
        return self._stubs["create_tag_template"]

    @property
    def get_tag_template(
        self,
    ) -> Callable[[datacatalog.GetTagTemplateRequest], Awaitable[tags.TagTemplate]]:
        r"""Return a callable for the get tag template method over gRPC.

        Gets a tag template.

        Returns:
            Callable[[~.GetTagTemplateRequest],
                    Awaitable[~.TagTemplate]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_tag_template" not in self._stubs:
            self._stubs["get_tag_template"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/GetTagTemplate",
                request_serializer=datacatalog.GetTagTemplateRequest.serialize,
                response_deserializer=tags.TagTemplate.deserialize,
            )
        return self._stubs["get_tag_template"]

    @property
    def update_tag_template(
        self,
    ) -> Callable[[datacatalog.UpdateTagTemplateRequest], Awaitable[tags.TagTemplate]]:
        r"""Return a callable for the update tag template method over gRPC.

        Updates a tag template. This method cannot be used to update the
        fields of a template. The tag template fields are represented as
        separate resources and should be updated using their own
        create/update/delete methods. Users should enable the Data
        Catalog API in the project identified by the
        ``tag_template.name`` parameter (see [Data Catalog Resource
        Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.UpdateTagTemplateRequest],
                    Awaitable[~.TagTemplate]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tag_template" not in self._stubs:
            self._stubs["update_tag_template"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTagTemplate",
                request_serializer=datacatalog.UpdateTagTemplateRequest.serialize,
                response_deserializer=tags.TagTemplate.deserialize,
            )
        return self._stubs["update_tag_template"]

    @property
    def delete_tag_template(
        self,
    ) -> Callable[[datacatalog.DeleteTagTemplateRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete tag template method over gRPC.

        Deletes a tag template and all tags using the template. Users
        should enable the Data Catalog API in the project identified by
        the ``name`` parameter (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.DeleteTagTemplateRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tag_template" not in self._stubs:
            self._stubs["delete_tag_template"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTagTemplate",
                request_serializer=datacatalog.DeleteTagTemplateRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_tag_template"]

    @property
    def create_tag_template_field(
        self,
    ) -> Callable[
        [datacatalog.CreateTagTemplateFieldRequest], Awaitable[tags.TagTemplateField]
    ]:
        r"""Return a callable for the create tag template field method over gRPC.

        Creates a field in a tag template. The user should enable the
        Data Catalog API in the project identified by the ``parent``
        parameter (see `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        Returns:
            Callable[[~.CreateTagTemplateFieldRequest],
                    Awaitable[~.TagTemplateField]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tag_template_field" not in self._stubs:
            self._stubs["create_tag_template_field"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTagTemplateField",
                request_serializer=datacatalog.CreateTagTemplateFieldRequest.serialize,
                response_deserializer=tags.TagTemplateField.deserialize,
            )
        return self._stubs["create_tag_template_field"]

    @property
    def update_tag_template_field(
        self,
    ) -> Callable[
        [datacatalog.UpdateTagTemplateFieldRequest], Awaitable[tags.TagTemplateField]
    ]:
        r"""Return a callable for the update tag template field method over gRPC.

        Updates a field in a tag template. This method cannot be used to
        update the field type. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.UpdateTagTemplateFieldRequest],
                    Awaitable[~.TagTemplateField]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tag_template_field" not in self._stubs:
            self._stubs["update_tag_template_field"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTagTemplateField",
                request_serializer=datacatalog.UpdateTagTemplateFieldRequest.serialize,
                response_deserializer=tags.TagTemplateField.deserialize,
            )
        return self._stubs["update_tag_template_field"]

    @property
    def rename_tag_template_field(
        self,
    ) -> Callable[
        [datacatalog.RenameTagTemplateFieldRequest], Awaitable[tags.TagTemplateField]
    ]:
        r"""Return a callable for the rename tag template field method over gRPC.

        Renames a field in a tag template. The user should enable the
        Data Catalog API in the project identified by the ``name``
        parameter (see `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        Returns:
            Callable[[~.RenameTagTemplateFieldRequest],
                    Awaitable[~.TagTemplateField]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rename_tag_template_field" not in self._stubs:
            self._stubs["rename_tag_template_field"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/RenameTagTemplateField",
                request_serializer=datacatalog.RenameTagTemplateFieldRequest.serialize,
                response_deserializer=tags.TagTemplateField.deserialize,
            )
        return self._stubs["rename_tag_template_field"]

    @property
    def rename_tag_template_field_enum_value(
        self,
    ) -> Callable[
        [datacatalog.RenameTagTemplateFieldEnumValueRequest],
        Awaitable[tags.TagTemplateField],
    ]:
        r"""Return a callable for the rename tag template field enum
        value method over gRPC.

        Renames an enum value in a tag template. The enum
        values have to be unique within one enum field. Thus, an
        enum value cannot be renamed with a name used in any
        other enum value within the same enum field.

        Returns:
            Callable[[~.RenameTagTemplateFieldEnumValueRequest],
                    Awaitable[~.TagTemplateField]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rename_tag_template_field_enum_value" not in self._stubs:
            self._stubs["rename_tag_template_field_enum_value"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.datacatalog.v1beta1.DataCatalog/RenameTagTemplateFieldEnumValue",
                    request_serializer=datacatalog.RenameTagTemplateFieldEnumValueRequest.serialize,
                    response_deserializer=tags.TagTemplateField.deserialize,
                )
            )
        return self._stubs["rename_tag_template_field_enum_value"]

    @property
    def delete_tag_template_field(
        self,
    ) -> Callable[
        [datacatalog.DeleteTagTemplateFieldRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete tag template field method over gRPC.

        Deletes a field in a tag template and all uses of that field.
        Users should enable the Data Catalog API in the project
        identified by the ``name`` parameter (see [Data Catalog Resource
        Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        Returns:
            Callable[[~.DeleteTagTemplateFieldRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tag_template_field" not in self._stubs:
            self._stubs["delete_tag_template_field"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTagTemplateField",
                request_serializer=datacatalog.DeleteTagTemplateFieldRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_tag_template_field"]

    @property
    def create_tag(
        self,
    ) -> Callable[[datacatalog.CreateTagRequest], Awaitable[tags.Tag]]:
        r"""Return a callable for the create tag method over gRPC.

        Creates a tag on an
        [Entry][google.cloud.datacatalog.v1beta1.Entry]. Note: The
        project identified by the ``parent`` parameter for the
        `tag <https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups.entries.tags/create#path-parameters>`__
        and the `tag
        template <https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.tagTemplates/create#path-parameters>`__
        used to create the tag must be from the same organization.

        Returns:
            Callable[[~.CreateTagRequest],
                    Awaitable[~.Tag]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tag" not in self._stubs:
            self._stubs["create_tag"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTag",
                request_serializer=datacatalog.CreateTagRequest.serialize,
                response_deserializer=tags.Tag.deserialize,
            )
        return self._stubs["create_tag"]

    @property
    def update_tag(
        self,
    ) -> Callable[[datacatalog.UpdateTagRequest], Awaitable[tags.Tag]]:
        r"""Return a callable for the update tag method over gRPC.

        Updates an existing tag.

        Returns:
            Callable[[~.UpdateTagRequest],
                    Awaitable[~.Tag]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tag" not in self._stubs:
            self._stubs["update_tag"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTag",
                request_serializer=datacatalog.UpdateTagRequest.serialize,
                response_deserializer=tags.Tag.deserialize,
            )
        return self._stubs["update_tag"]

    @property
    def delete_tag(
        self,
    ) -> Callable[[datacatalog.DeleteTagRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete tag method over gRPC.

        Deletes a tag.

        Returns:
            Callable[[~.DeleteTagRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tag" not in self._stubs:
            self._stubs["delete_tag"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTag",
                request_serializer=datacatalog.DeleteTagRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_tag"]

    @property
    def list_tags(
        self,
    ) -> Callable[
        [datacatalog.ListTagsRequest], Awaitable[datacatalog.ListTagsResponse]
    ]:
        r"""Return a callable for the list tags method over gRPC.

        Lists tags assigned to an
        [Entry][google.cloud.datacatalog.v1beta1.Entry]. The
        [columns][google.cloud.datacatalog.v1beta1.Tag.column] in the
        response are lowercased.

        Returns:
            Callable[[~.ListTagsRequest],
                    Awaitable[~.ListTagsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_tags" not in self._stubs:
            self._stubs["list_tags"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1beta1.DataCatalog/ListTags",
                request_serializer=datacatalog.ListTagsRequest.serialize,
                response_deserializer=datacatalog.ListTagsResponse.deserialize,
            )
        return self._stubs["list_tags"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the access control policy for a resource. Replaces any
        existing policy. Supported resources are:

        - Tag templates.
        - Entries.
        - Entry groups. Note, this method cannot be used to manage
          policies for BigQuery, Pub/Sub and any external Google Cloud
          Platform resources synced to Data Catalog.

        Callers must have following Google IAM permission

        - ``datacatalog.tagTemplates.setIamPolicy`` to set policies on
          tag templates.
        - ``datacatalog.entries.setIamPolicy`` to set policies on
          entries.
        - ``datacatalog.entryGroups.setIamPolicy`` to set policies on
          entry groups.

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
                "/google.cloud.datacatalog.v1beta1.DataCatalog/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the access control policy for a resource. A ``NOT_FOUND``
        error is returned if the resource does not exist. An empty
        policy is returned if the resource exists but does not have a
        policy set on it.

        Supported resources are:

        - Tag templates.
        - Entries.
        - Entry groups. Note, this method cannot be used to manage
          policies for BigQuery, Pub/Sub and any external Google Cloud
          Platform resources synced to Data Catalog.

        Callers must have following Google IAM permission

        - ``datacatalog.tagTemplates.getIamPolicy`` to get policies on
          tag templates.
        - ``datacatalog.entries.getIamPolicy`` to get policies on
          entries.
        - ``datacatalog.entryGroups.getIamPolicy`` to get policies on
          entry groups.

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
                "/google.cloud.datacatalog.v1beta1.DataCatalog/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.

        Returns the caller's permissions on a resource. If the resource
        does not exist, an empty set of permissions is returned (We
        don't return a ``NOT_FOUND`` error).

        Supported resources are:

        - Tag templates.
        - Entries.
        - Entry groups. Note, this method cannot be used to manage
          policies for BigQuery, Pub/Sub and any external Google Cloud
          Platform resources synced to Data Catalog.

        A caller is not required to have Google IAM permission to make
        this request.

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
                "/google.cloud.datacatalog.v1beta1.DataCatalog/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.search_catalog: self._wrap_method(
                self.search_catalog,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entry_group: self._wrap_method(
                self.create_entry_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_entry_group: self._wrap_method(
                self.update_entry_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entry_group: self._wrap_method(
                self.get_entry_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_entry_group: self._wrap_method(
                self.delete_entry_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entry_groups: self._wrap_method(
                self.list_entry_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entry: self._wrap_method(
                self.create_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_entry: self._wrap_method(
                self.update_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_entry: self._wrap_method(
                self.delete_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entry: self._wrap_method(
                self.get_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.lookup_entry: self._wrap_method(
                self.lookup_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entries: self._wrap_method(
                self.list_entries,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_tag_template: self._wrap_method(
                self.create_tag_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_tag_template: self._wrap_method(
                self.get_tag_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_tag_template: self._wrap_method(
                self.update_tag_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_tag_template: self._wrap_method(
                self.delete_tag_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_tag_template_field: self._wrap_method(
                self.create_tag_template_field,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_tag_template_field: self._wrap_method(
                self.update_tag_template_field,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_tag_template_field: self._wrap_method(
                self.rename_tag_template_field,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_tag_template_field_enum_value: self._wrap_method(
                self.rename_tag_template_field_enum_value,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_tag_template_field: self._wrap_method(
                self.delete_tag_template_field,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_tag: self._wrap_method(
                self.create_tag,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_tag: self._wrap_method(
                self.update_tag,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_tag: self._wrap_method(
                self.delete_tag,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_tags: self._wrap_method(
                self.list_tags,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
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


__all__ = ("DataCatalogGrpcAsyncIOTransport",)
