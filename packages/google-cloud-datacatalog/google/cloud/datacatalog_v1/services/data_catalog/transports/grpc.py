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
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.datacatalog_v1.types import datacatalog, tags

from .base import DEFAULT_CLIENT_INFO, DataCatalogTransport

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
                    "serviceName": "google.cloud.datacatalog.v1.DataCatalog",
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
                    "serviceName": "google.cloud.datacatalog.v1.DataCatalog",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DataCatalogGrpcTransport(DataCatalogTransport):
    """gRPC backend transport for DataCatalog.

    Deprecated: Please use Dataplex Catalog instead.

    Data Catalog API service allows you to discover, understand, and
    manage your data.

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
        host: str = "datacatalog.googleapis.com",
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
        host: str = "datacatalog.googleapis.com",
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
    def search_catalog(
        self,
    ) -> Callable[
        [datacatalog.SearchCatalogRequest], datacatalog.SearchCatalogResponse
    ]:
        r"""Return a callable for the search catalog method over gRPC.

        Searches Data Catalog for multiple resources like entries and
        tags that match a query.

        This is a [Custom Method]
        (https://cloud.google.com/apis/design/custom_methods) that
        doesn't return all information on a resource, only its ID and
        high level fields. To get more information, you can subsequently
        call specific get methods.

        Note: Data Catalog search queries don't guarantee full recall.
        Results that match your query might not be returned, even in
        subsequent result pages. Additionally, returned (and not
        returned) results can vary if you repeat search queries.

        For more information, see [Data Catalog search syntax]
        (https://cloud.google.com/data-catalog/docs/how-to/search-reference).

        Returns:
            Callable[[~.SearchCatalogRequest],
                    ~.SearchCatalogResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_catalog" not in self._stubs:
            self._stubs["search_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/SearchCatalog",
                request_serializer=datacatalog.SearchCatalogRequest.serialize,
                response_deserializer=datacatalog.SearchCatalogResponse.deserialize,
            )
        return self._stubs["search_catalog"]

    @property
    def create_entry_group(
        self,
    ) -> Callable[[datacatalog.CreateEntryGroupRequest], datacatalog.EntryGroup]:
        r"""Return a callable for the create entry group method over gRPC.

        Creates an entry group.

        An entry group contains logically related entries together with
        `Cloud Identity and Access
        Management </data-catalog/docs/concepts/iam>`__ policies. These
        policies specify users who can create, edit, and view entries
        within entry groups.

        Data Catalog automatically creates entry groups with names that
        start with the ``@`` symbol for the following resources:

        - BigQuery entries (``@bigquery``)
        - Pub/Sub topics (``@pubsub``)
        - Dataproc Metastore services
          (``@dataproc_metastore_{SERVICE_NAME_HASH}``)

        You can create your own entry groups for Cloud Storage fileset
        entries and custom entries together with the corresponding IAM
        policies. User-created entry groups can't contain the ``@``
        symbol, it is reserved for automatically created groups.

        Entry groups, like entries, can be searched.

        A maximum of 10,000 entry groups may be created per organization
        across all locations.

        You must enable the Data Catalog API in the project identified
        by the ``parent`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.CreateEntryGroupRequest],
                    ~.EntryGroup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entry_group" not in self._stubs:
            self._stubs["create_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/CreateEntryGroup",
                request_serializer=datacatalog.CreateEntryGroupRequest.serialize,
                response_deserializer=datacatalog.EntryGroup.deserialize,
            )
        return self._stubs["create_entry_group"]

    @property
    def get_entry_group(
        self,
    ) -> Callable[[datacatalog.GetEntryGroupRequest], datacatalog.EntryGroup]:
        r"""Return a callable for the get entry group method over gRPC.

        Gets an entry group.

        Returns:
            Callable[[~.GetEntryGroupRequest],
                    ~.EntryGroup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entry_group" not in self._stubs:
            self._stubs["get_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/GetEntryGroup",
                request_serializer=datacatalog.GetEntryGroupRequest.serialize,
                response_deserializer=datacatalog.EntryGroup.deserialize,
            )
        return self._stubs["get_entry_group"]

    @property
    def update_entry_group(
        self,
    ) -> Callable[[datacatalog.UpdateEntryGroupRequest], datacatalog.EntryGroup]:
        r"""Return a callable for the update entry group method over gRPC.

        Updates an entry group.

        You must enable the Data Catalog API in the project identified
        by the ``entry_group.name`` parameter. For more information, see
        `Data Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.UpdateEntryGroupRequest],
                    ~.EntryGroup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entry_group" not in self._stubs:
            self._stubs["update_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/UpdateEntryGroup",
                request_serializer=datacatalog.UpdateEntryGroupRequest.serialize,
                response_deserializer=datacatalog.EntryGroup.deserialize,
            )
        return self._stubs["update_entry_group"]

    @property
    def delete_entry_group(
        self,
    ) -> Callable[[datacatalog.DeleteEntryGroupRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete entry group method over gRPC.

        Deletes an entry group.

        You must enable the Data Catalog API in the project identified
        by the ``name`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.DeleteEntryGroupRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entry_group" not in self._stubs:
            self._stubs["delete_entry_group"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/DeleteEntryGroup",
                request_serializer=datacatalog.DeleteEntryGroupRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_entry_group"]

    @property
    def list_entry_groups(
        self,
    ) -> Callable[
        [datacatalog.ListEntryGroupsRequest], datacatalog.ListEntryGroupsResponse
    ]:
        r"""Return a callable for the list entry groups method over gRPC.

        Lists entry groups.

        Returns:
            Callable[[~.ListEntryGroupsRequest],
                    ~.ListEntryGroupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entry_groups" not in self._stubs:
            self._stubs["list_entry_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/ListEntryGroups",
                request_serializer=datacatalog.ListEntryGroupsRequest.serialize,
                response_deserializer=datacatalog.ListEntryGroupsResponse.deserialize,
            )
        return self._stubs["list_entry_groups"]

    @property
    def create_entry(
        self,
    ) -> Callable[[datacatalog.CreateEntryRequest], datacatalog.Entry]:
        r"""Return a callable for the create entry method over gRPC.

        Creates an entry.

        You can create entries only with 'FILESET', 'CLUSTER',
        'DATA_STREAM', or custom types. Data Catalog automatically
        creates entries with other types during metadata ingestion from
        integrated systems.

        You must enable the Data Catalog API in the project identified
        by the ``parent`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        An entry group can have a maximum of 100,000 entries.

        Returns:
            Callable[[~.CreateEntryRequest],
                    ~.Entry]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entry" not in self._stubs:
            self._stubs["create_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/CreateEntry",
                request_serializer=datacatalog.CreateEntryRequest.serialize,
                response_deserializer=datacatalog.Entry.deserialize,
            )
        return self._stubs["create_entry"]

    @property
    def update_entry(
        self,
    ) -> Callable[[datacatalog.UpdateEntryRequest], datacatalog.Entry]:
        r"""Return a callable for the update entry method over gRPC.

        Updates an existing entry.

        You must enable the Data Catalog API in the project identified
        by the ``entry.name`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.UpdateEntryRequest],
                    ~.Entry]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entry" not in self._stubs:
            self._stubs["update_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/UpdateEntry",
                request_serializer=datacatalog.UpdateEntryRequest.serialize,
                response_deserializer=datacatalog.Entry.deserialize,
            )
        return self._stubs["update_entry"]

    @property
    def delete_entry(
        self,
    ) -> Callable[[datacatalog.DeleteEntryRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete entry method over gRPC.

        Deletes an existing entry.

        You can delete only the entries created by the
        [CreateEntry][google.cloud.datacatalog.v1.DataCatalog.CreateEntry]
        method.

        You must enable the Data Catalog API in the project identified
        by the ``name`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.DeleteEntryRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entry" not in self._stubs:
            self._stubs["delete_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/DeleteEntry",
                request_serializer=datacatalog.DeleteEntryRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_entry"]

    @property
    def get_entry(self) -> Callable[[datacatalog.GetEntryRequest], datacatalog.Entry]:
        r"""Return a callable for the get entry method over gRPC.

        Gets an entry.

        Returns:
            Callable[[~.GetEntryRequest],
                    ~.Entry]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entry" not in self._stubs:
            self._stubs["get_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/GetEntry",
                request_serializer=datacatalog.GetEntryRequest.serialize,
                response_deserializer=datacatalog.Entry.deserialize,
            )
        return self._stubs["get_entry"]

    @property
    def lookup_entry(
        self,
    ) -> Callable[[datacatalog.LookupEntryRequest], datacatalog.Entry]:
        r"""Return a callable for the lookup entry method over gRPC.

        Gets an entry by its target resource name.

        The resource name comes from the source Google Cloud
        Platform service.

        Returns:
            Callable[[~.LookupEntryRequest],
                    ~.Entry]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_entry" not in self._stubs:
            self._stubs["lookup_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/LookupEntry",
                request_serializer=datacatalog.LookupEntryRequest.serialize,
                response_deserializer=datacatalog.Entry.deserialize,
            )
        return self._stubs["lookup_entry"]

    @property
    def list_entries(
        self,
    ) -> Callable[[datacatalog.ListEntriesRequest], datacatalog.ListEntriesResponse]:
        r"""Return a callable for the list entries method over gRPC.

        Lists entries.

        Note: Currently, this method can list only custom entries. To
        get a list of both custom and automatically created entries, use
        [SearchCatalog][google.cloud.datacatalog.v1.DataCatalog.SearchCatalog].

        Returns:
            Callable[[~.ListEntriesRequest],
                    ~.ListEntriesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entries" not in self._stubs:
            self._stubs["list_entries"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/ListEntries",
                request_serializer=datacatalog.ListEntriesRequest.serialize,
                response_deserializer=datacatalog.ListEntriesResponse.deserialize,
            )
        return self._stubs["list_entries"]

    @property
    def modify_entry_overview(
        self,
    ) -> Callable[[datacatalog.ModifyEntryOverviewRequest], datacatalog.EntryOverview]:
        r"""Return a callable for the modify entry overview method over gRPC.

        Modifies entry overview, part of the business context of an
        [Entry][google.cloud.datacatalog.v1.Entry].

        To call this method, you must have the
        ``datacatalog.entries.updateOverview`` IAM permission on the
        corresponding project.

        Returns:
            Callable[[~.ModifyEntryOverviewRequest],
                    ~.EntryOverview]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "modify_entry_overview" not in self._stubs:
            self._stubs["modify_entry_overview"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/ModifyEntryOverview",
                request_serializer=datacatalog.ModifyEntryOverviewRequest.serialize,
                response_deserializer=datacatalog.EntryOverview.deserialize,
            )
        return self._stubs["modify_entry_overview"]

    @property
    def modify_entry_contacts(
        self,
    ) -> Callable[[datacatalog.ModifyEntryContactsRequest], datacatalog.Contacts]:
        r"""Return a callable for the modify entry contacts method over gRPC.

        Modifies contacts, part of the business context of an
        [Entry][google.cloud.datacatalog.v1.Entry].

        To call this method, you must have the
        ``datacatalog.entries.updateContacts`` IAM permission on the
        corresponding project.

        Returns:
            Callable[[~.ModifyEntryContactsRequest],
                    ~.Contacts]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "modify_entry_contacts" not in self._stubs:
            self._stubs["modify_entry_contacts"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/ModifyEntryContacts",
                request_serializer=datacatalog.ModifyEntryContactsRequest.serialize,
                response_deserializer=datacatalog.Contacts.deserialize,
            )
        return self._stubs["modify_entry_contacts"]

    @property
    def create_tag_template(
        self,
    ) -> Callable[[datacatalog.CreateTagTemplateRequest], tags.TagTemplate]:
        r"""Return a callable for the create tag template method over gRPC.

        Creates a tag template.

        You must enable the Data Catalog API in the project identified
        by the ``parent`` parameter. For more information, see [Data
        Catalog resource project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project).

        Returns:
            Callable[[~.CreateTagTemplateRequest],
                    ~.TagTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tag_template" not in self._stubs:
            self._stubs["create_tag_template"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/CreateTagTemplate",
                request_serializer=datacatalog.CreateTagTemplateRequest.serialize,
                response_deserializer=tags.TagTemplate.deserialize,
            )
        return self._stubs["create_tag_template"]

    @property
    def get_tag_template(
        self,
    ) -> Callable[[datacatalog.GetTagTemplateRequest], tags.TagTemplate]:
        r"""Return a callable for the get tag template method over gRPC.

        Gets a tag template.

        Returns:
            Callable[[~.GetTagTemplateRequest],
                    ~.TagTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_tag_template" not in self._stubs:
            self._stubs["get_tag_template"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/GetTagTemplate",
                request_serializer=datacatalog.GetTagTemplateRequest.serialize,
                response_deserializer=tags.TagTemplate.deserialize,
            )
        return self._stubs["get_tag_template"]

    @property
    def update_tag_template(
        self,
    ) -> Callable[[datacatalog.UpdateTagTemplateRequest], tags.TagTemplate]:
        r"""Return a callable for the update tag template method over gRPC.

        Updates a tag template.

        You can't update template fields with this method. These fields
        are separate resources with their own create, update, and delete
        methods.

        You must enable the Data Catalog API in the project identified
        by the ``tag_template.name`` parameter. For more information,
        see `Data Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.UpdateTagTemplateRequest],
                    ~.TagTemplate]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tag_template" not in self._stubs:
            self._stubs["update_tag_template"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/UpdateTagTemplate",
                request_serializer=datacatalog.UpdateTagTemplateRequest.serialize,
                response_deserializer=tags.TagTemplate.deserialize,
            )
        return self._stubs["update_tag_template"]

    @property
    def delete_tag_template(
        self,
    ) -> Callable[[datacatalog.DeleteTagTemplateRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete tag template method over gRPC.

        Deletes a tag template and all tags that use it.

        You must enable the Data Catalog API in the project identified
        by the ``name`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.DeleteTagTemplateRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tag_template" not in self._stubs:
            self._stubs["delete_tag_template"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/DeleteTagTemplate",
                request_serializer=datacatalog.DeleteTagTemplateRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_tag_template"]

    @property
    def create_tag_template_field(
        self,
    ) -> Callable[[datacatalog.CreateTagTemplateFieldRequest], tags.TagTemplateField]:
        r"""Return a callable for the create tag template field method over gRPC.

        Creates a field in a tag template.

        You must enable the Data Catalog API in the project identified
        by the ``parent`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.CreateTagTemplateFieldRequest],
                    ~.TagTemplateField]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tag_template_field" not in self._stubs:
            self._stubs["create_tag_template_field"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/CreateTagTemplateField",
                request_serializer=datacatalog.CreateTagTemplateFieldRequest.serialize,
                response_deserializer=tags.TagTemplateField.deserialize,
            )
        return self._stubs["create_tag_template_field"]

    @property
    def update_tag_template_field(
        self,
    ) -> Callable[[datacatalog.UpdateTagTemplateFieldRequest], tags.TagTemplateField]:
        r"""Return a callable for the update tag template field method over gRPC.

        Updates a field in a tag template.

        You can't update the field type with this method.

        You must enable the Data Catalog API in the project identified
        by the ``name`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.UpdateTagTemplateFieldRequest],
                    ~.TagTemplateField]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tag_template_field" not in self._stubs:
            self._stubs["update_tag_template_field"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/UpdateTagTemplateField",
                request_serializer=datacatalog.UpdateTagTemplateFieldRequest.serialize,
                response_deserializer=tags.TagTemplateField.deserialize,
            )
        return self._stubs["update_tag_template_field"]

    @property
    def rename_tag_template_field(
        self,
    ) -> Callable[[datacatalog.RenameTagTemplateFieldRequest], tags.TagTemplateField]:
        r"""Return a callable for the rename tag template field method over gRPC.

        Renames a field in a tag template.

        You must enable the Data Catalog API in the project identified
        by the ``name`` parameter. For more information, see [Data
        Catalog resource project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project).

        Returns:
            Callable[[~.RenameTagTemplateFieldRequest],
                    ~.TagTemplateField]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rename_tag_template_field" not in self._stubs:
            self._stubs["rename_tag_template_field"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/RenameTagTemplateField",
                request_serializer=datacatalog.RenameTagTemplateFieldRequest.serialize,
                response_deserializer=tags.TagTemplateField.deserialize,
            )
        return self._stubs["rename_tag_template_field"]

    @property
    def rename_tag_template_field_enum_value(
        self,
    ) -> Callable[
        [datacatalog.RenameTagTemplateFieldEnumValueRequest], tags.TagTemplateField
    ]:
        r"""Return a callable for the rename tag template field enum
        value method over gRPC.

        Renames an enum value in a tag template.

        Within a single enum field, enum values must be unique.

        Returns:
            Callable[[~.RenameTagTemplateFieldEnumValueRequest],
                    ~.TagTemplateField]:
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
                    "/google.cloud.datacatalog.v1.DataCatalog/RenameTagTemplateFieldEnumValue",
                    request_serializer=datacatalog.RenameTagTemplateFieldEnumValueRequest.serialize,
                    response_deserializer=tags.TagTemplateField.deserialize,
                )
            )
        return self._stubs["rename_tag_template_field_enum_value"]

    @property
    def delete_tag_template_field(
        self,
    ) -> Callable[[datacatalog.DeleteTagTemplateFieldRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete tag template field method over gRPC.

        Deletes a field in a tag template and all uses of this field
        from the tags based on this template.

        You must enable the Data Catalog API in the project identified
        by the ``name`` parameter. For more information, see `Data
        Catalog resource
        project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__.

        Returns:
            Callable[[~.DeleteTagTemplateFieldRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tag_template_field" not in self._stubs:
            self._stubs["delete_tag_template_field"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/DeleteTagTemplateField",
                request_serializer=datacatalog.DeleteTagTemplateFieldRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_tag_template_field"]

    @property
    def create_tag(self) -> Callable[[datacatalog.CreateTagRequest], tags.Tag]:
        r"""Return a callable for the create tag method over gRPC.

        Creates a tag and assigns it to:

        - An [Entry][google.cloud.datacatalog.v1.Entry] if the method
          name is
          ``projects.locations.entryGroups.entries.tags.create``.
        - Or [EntryGroup][google.cloud.datacatalog.v1.EntryGroup]if the
          method name is ``projects.locations.entryGroups.tags.create``.

        Note: The project identified by the ``parent`` parameter for the
        [tag]
        (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create#path-parameters)
        and the [tag template]
        (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create#path-parameters)
        used to create the tag must be in the same organization.

        Returns:
            Callable[[~.CreateTagRequest],
                    ~.Tag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tag" not in self._stubs:
            self._stubs["create_tag"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/CreateTag",
                request_serializer=datacatalog.CreateTagRequest.serialize,
                response_deserializer=tags.Tag.deserialize,
            )
        return self._stubs["create_tag"]

    @property
    def update_tag(self) -> Callable[[datacatalog.UpdateTagRequest], tags.Tag]:
        r"""Return a callable for the update tag method over gRPC.

        Updates an existing tag.

        Returns:
            Callable[[~.UpdateTagRequest],
                    ~.Tag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tag" not in self._stubs:
            self._stubs["update_tag"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/UpdateTag",
                request_serializer=datacatalog.UpdateTagRequest.serialize,
                response_deserializer=tags.Tag.deserialize,
            )
        return self._stubs["update_tag"]

    @property
    def delete_tag(self) -> Callable[[datacatalog.DeleteTagRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete tag method over gRPC.

        Deletes a tag.

        Returns:
            Callable[[~.DeleteTagRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tag" not in self._stubs:
            self._stubs["delete_tag"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/DeleteTag",
                request_serializer=datacatalog.DeleteTagRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_tag"]

    @property
    def list_tags(
        self,
    ) -> Callable[[datacatalog.ListTagsRequest], datacatalog.ListTagsResponse]:
        r"""Return a callable for the list tags method over gRPC.

        Lists tags assigned to an
        [Entry][google.cloud.datacatalog.v1.Entry]. The
        [columns][google.cloud.datacatalog.v1.Tag.column] in the
        response are lowercased.

        Returns:
            Callable[[~.ListTagsRequest],
                    ~.ListTagsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_tags" not in self._stubs:
            self._stubs["list_tags"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/ListTags",
                request_serializer=datacatalog.ListTagsRequest.serialize,
                response_deserializer=datacatalog.ListTagsResponse.deserialize,
            )
        return self._stubs["list_tags"]

    @property
    def reconcile_tags(
        self,
    ) -> Callable[[datacatalog.ReconcileTagsRequest], operations_pb2.Operation]:
        r"""Return a callable for the reconcile tags method over gRPC.

        ``ReconcileTags`` creates or updates a list of tags on the
        entry. If the
        [ReconcileTagsRequest.force_delete_missing][google.cloud.datacatalog.v1.ReconcileTagsRequest.force_delete_missing]
        parameter is set, the operation deletes tags not included in the
        input tag list.

        ``ReconcileTags`` returns a [long-running operation]
        [google.longrunning.Operation] resource that can be queried with
        [Operations.GetOperation][google.longrunning.Operations.GetOperation]
        to return [ReconcileTagsMetadata]
        [google.cloud.datacatalog.v1.ReconcileTagsMetadata] and a
        [ReconcileTagsResponse]
        [google.cloud.datacatalog.v1.ReconcileTagsResponse] message.

        Returns:
            Callable[[~.ReconcileTagsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reconcile_tags" not in self._stubs:
            self._stubs["reconcile_tags"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/ReconcileTags",
                request_serializer=datacatalog.ReconcileTagsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reconcile_tags"]

    @property
    def star_entry(
        self,
    ) -> Callable[[datacatalog.StarEntryRequest], datacatalog.StarEntryResponse]:
        r"""Return a callable for the star entry method over gRPC.

        Marks an [Entry][google.cloud.datacatalog.v1.Entry] as starred
        by the current user. Starring information is private to each
        user.

        Returns:
            Callable[[~.StarEntryRequest],
                    ~.StarEntryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "star_entry" not in self._stubs:
            self._stubs["star_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/StarEntry",
                request_serializer=datacatalog.StarEntryRequest.serialize,
                response_deserializer=datacatalog.StarEntryResponse.deserialize,
            )
        return self._stubs["star_entry"]

    @property
    def unstar_entry(
        self,
    ) -> Callable[[datacatalog.UnstarEntryRequest], datacatalog.UnstarEntryResponse]:
        r"""Return a callable for the unstar entry method over gRPC.

        Marks an [Entry][google.cloud.datacatalog.v1.Entry] as NOT
        starred by the current user. Starring information is private to
        each user.

        Returns:
            Callable[[~.UnstarEntryRequest],
                    ~.UnstarEntryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "unstar_entry" not in self._stubs:
            self._stubs["unstar_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/UnstarEntry",
                request_serializer=datacatalog.UnstarEntryRequest.serialize,
                response_deserializer=datacatalog.UnstarEntryResponse.deserialize,
            )
        return self._stubs["unstar_entry"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets an access control policy for a resource. Replaces any
        existing policy.

        Supported resources are:

        - Tag templates
        - Entry groups

        Note: This method sets policies only within Data Catalog and
        can't be used to manage policies in BigQuery, Pub/Sub, Dataproc
        Metastore, and any external Google Cloud Platform resources
        synced with the Data Catalog.

        To call this method, you must have the following Google IAM
        permissions:

        - ``datacatalog.tagTemplates.setIamPolicy`` to set policies on
          tag templates.
        - ``datacatalog.entryGroups.setIamPolicy`` to set policies on
          entry groups.

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
                "/google.cloud.datacatalog.v1.DataCatalog/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the access control policy for a resource.

        May return:

        - A\ ``NOT_FOUND`` error if the resource doesn't exist or you
          don't have the permission to view it.
        - An empty policy if the resource exists but doesn't have a set
          policy.

        Supported resources are:

        - Tag templates
        - Entry groups

        Note: This method doesn't get policies from Google Cloud
        Platform resources ingested into Data Catalog.

        To call this method, you must have the following Google IAM
        permissions:

        - ``datacatalog.tagTemplates.getIamPolicy`` to get policies on
          tag templates.
        - ``datacatalog.entryGroups.getIamPolicy`` to get policies on
          entry groups.

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
                "/google.cloud.datacatalog.v1.DataCatalog/GetIamPolicy",
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

        Gets your permissions on a resource.

        Returns an empty set of permissions if the resource
        doesn't exist.

        Supported resources are:

        - Tag templates
        - Entry groups

        Note: This method gets policies only within Data Catalog
        and can't be used to get policies from BigQuery,
        Pub/Sub, Dataproc Metastore, and any external Google
        Cloud Platform resources ingested into Data Catalog.

        No Google IAM permissions are required to call this
        method.

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
                "/google.cloud.datacatalog.v1.DataCatalog/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def import_entries(
        self,
    ) -> Callable[[datacatalog.ImportEntriesRequest], operations_pb2.Operation]:
        r"""Return a callable for the import entries method over gRPC.

        Imports entries from a source, such as data previously dumped
        into a Cloud Storage bucket, into Data Catalog. Import of
        entries is a sync operation that reconciles the state of the
        third-party system with the Data Catalog.

        ``ImportEntries`` accepts source data snapshots of a third-party
        system. Snapshot should be delivered as a .wire or
        base65-encoded .txt file containing a sequence of Protocol
        Buffer messages of
        [DumpItem][google.cloud.datacatalog.v1.DumpItem] type.

        ``ImportEntries`` returns a [long-running operation]
        [google.longrunning.Operation] resource that can be queried with
        [Operations.GetOperation][google.longrunning.Operations.GetOperation]
        to return
        [ImportEntriesMetadata][google.cloud.datacatalog.v1.ImportEntriesMetadata]
        and an
        [ImportEntriesResponse][google.cloud.datacatalog.v1.ImportEntriesResponse]
        message.

        Returns:
            Callable[[~.ImportEntriesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_entries" not in self._stubs:
            self._stubs["import_entries"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/ImportEntries",
                request_serializer=datacatalog.ImportEntriesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_entries"]

    @property
    def set_config(
        self,
    ) -> Callable[[datacatalog.SetConfigRequest], datacatalog.MigrationConfig]:
        r"""Return a callable for the set config method over gRPC.

        Sets the configuration related to the migration to
        Dataplex for an organization or project.

        Returns:
            Callable[[~.SetConfigRequest],
                    ~.MigrationConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_config" not in self._stubs:
            self._stubs["set_config"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/SetConfig",
                request_serializer=datacatalog.SetConfigRequest.serialize,
                response_deserializer=datacatalog.MigrationConfig.deserialize,
            )
        return self._stubs["set_config"]

    @property
    def retrieve_config(
        self,
    ) -> Callable[[datacatalog.RetrieveConfigRequest], datacatalog.OrganizationConfig]:
        r"""Return a callable for the retrieve config method over gRPC.

        Retrieves the configuration related to the migration
        from Data Catalog to Dataplex for a specific
        organization, including all the projects under it which
        have a separate configuration set.

        Returns:
            Callable[[~.RetrieveConfigRequest],
                    ~.OrganizationConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retrieve_config" not in self._stubs:
            self._stubs["retrieve_config"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/RetrieveConfig",
                request_serializer=datacatalog.RetrieveConfigRequest.serialize,
                response_deserializer=datacatalog.OrganizationConfig.deserialize,
            )
        return self._stubs["retrieve_config"]

    @property
    def retrieve_effective_config(
        self,
    ) -> Callable[
        [datacatalog.RetrieveEffectiveConfigRequest], datacatalog.MigrationConfig
    ]:
        r"""Return a callable for the retrieve effective config method over gRPC.

        Retrieves the effective configuration related to the
        migration from Data Catalog to Dataplex for a specific
        organization or project. If there is no specific
        configuration set for the resource, the setting is
        checked hierarchicahlly through the ancestors of the
        resource, starting from the resource itself.

        Returns:
            Callable[[~.RetrieveEffectiveConfigRequest],
                    ~.MigrationConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retrieve_effective_config" not in self._stubs:
            self._stubs["retrieve_effective_config"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.v1.DataCatalog/RetrieveEffectiveConfig",
                request_serializer=datacatalog.RetrieveEffectiveConfigRequest.serialize,
                response_deserializer=datacatalog.MigrationConfig.deserialize,
            )
        return self._stubs["retrieve_effective_config"]

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
    def kind(self) -> str:
        return "grpc"


__all__ = ("DataCatalogGrpcTransport",)
