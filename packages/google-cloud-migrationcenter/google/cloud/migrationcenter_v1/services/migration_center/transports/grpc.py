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
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.migrationcenter_v1.types import migrationcenter

from .base import DEFAULT_CLIENT_INFO, MigrationCenterTransport

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
                    "serviceName": "google.cloud.migrationcenter.v1.MigrationCenter",
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
                    "serviceName": "google.cloud.migrationcenter.v1.MigrationCenter",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class MigrationCenterGrpcTransport(MigrationCenterTransport):
    """gRPC backend transport for MigrationCenter.

    Service describing handlers for resources.

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
        host: str = "migrationcenter.googleapis.com",
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
                 The hostname to connect to (default: 'migrationcenter.googleapis.com').
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
        host: str = "migrationcenter.googleapis.com",
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
    def list_assets(
        self,
    ) -> Callable[
        [migrationcenter.ListAssetsRequest], migrationcenter.ListAssetsResponse
    ]:
        r"""Return a callable for the list assets method over gRPC.

        Lists all the assets in a given project and location.

        Returns:
            Callable[[~.ListAssetsRequest],
                    ~.ListAssetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_assets" not in self._stubs:
            self._stubs["list_assets"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListAssets",
                request_serializer=migrationcenter.ListAssetsRequest.serialize,
                response_deserializer=migrationcenter.ListAssetsResponse.deserialize,
            )
        return self._stubs["list_assets"]

    @property
    def get_asset(
        self,
    ) -> Callable[[migrationcenter.GetAssetRequest], migrationcenter.Asset]:
        r"""Return a callable for the get asset method over gRPC.

        Gets the details of an asset.

        Returns:
            Callable[[~.GetAssetRequest],
                    ~.Asset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_asset" not in self._stubs:
            self._stubs["get_asset"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetAsset",
                request_serializer=migrationcenter.GetAssetRequest.serialize,
                response_deserializer=migrationcenter.Asset.deserialize,
            )
        return self._stubs["get_asset"]

    @property
    def update_asset(
        self,
    ) -> Callable[[migrationcenter.UpdateAssetRequest], migrationcenter.Asset]:
        r"""Return a callable for the update asset method over gRPC.

        Updates the parameters of an asset.

        Returns:
            Callable[[~.UpdateAssetRequest],
                    ~.Asset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_asset" not in self._stubs:
            self._stubs["update_asset"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateAsset",
                request_serializer=migrationcenter.UpdateAssetRequest.serialize,
                response_deserializer=migrationcenter.Asset.deserialize,
            )
        return self._stubs["update_asset"]

    @property
    def batch_update_assets(
        self,
    ) -> Callable[
        [migrationcenter.BatchUpdateAssetsRequest],
        migrationcenter.BatchUpdateAssetsResponse,
    ]:
        r"""Return a callable for the batch update assets method over gRPC.

        Updates the parameters of a list of assets.

        Returns:
            Callable[[~.BatchUpdateAssetsRequest],
                    ~.BatchUpdateAssetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_update_assets" not in self._stubs:
            self._stubs["batch_update_assets"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/BatchUpdateAssets",
                request_serializer=migrationcenter.BatchUpdateAssetsRequest.serialize,
                response_deserializer=migrationcenter.BatchUpdateAssetsResponse.deserialize,
            )
        return self._stubs["batch_update_assets"]

    @property
    def delete_asset(
        self,
    ) -> Callable[[migrationcenter.DeleteAssetRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete asset method over gRPC.

        Deletes an asset.

        Returns:
            Callable[[~.DeleteAssetRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_asset" not in self._stubs:
            self._stubs["delete_asset"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteAsset",
                request_serializer=migrationcenter.DeleteAssetRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_asset"]

    @property
    def batch_delete_assets(
        self,
    ) -> Callable[[migrationcenter.BatchDeleteAssetsRequest], empty_pb2.Empty]:
        r"""Return a callable for the batch delete assets method over gRPC.

        Deletes list of Assets.

        Returns:
            Callable[[~.BatchDeleteAssetsRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_assets" not in self._stubs:
            self._stubs["batch_delete_assets"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/BatchDeleteAssets",
                request_serializer=migrationcenter.BatchDeleteAssetsRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["batch_delete_assets"]

    @property
    def report_asset_frames(
        self,
    ) -> Callable[
        [migrationcenter.ReportAssetFramesRequest],
        migrationcenter.ReportAssetFramesResponse,
    ]:
        r"""Return a callable for the report asset frames method over gRPC.

        Reports a set of frames.

        Returns:
            Callable[[~.ReportAssetFramesRequest],
                    ~.ReportAssetFramesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "report_asset_frames" not in self._stubs:
            self._stubs["report_asset_frames"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ReportAssetFrames",
                request_serializer=migrationcenter.ReportAssetFramesRequest.serialize,
                response_deserializer=migrationcenter.ReportAssetFramesResponse.deserialize,
            )
        return self._stubs["report_asset_frames"]

    @property
    def aggregate_assets_values(
        self,
    ) -> Callable[
        [migrationcenter.AggregateAssetsValuesRequest],
        migrationcenter.AggregateAssetsValuesResponse,
    ]:
        r"""Return a callable for the aggregate assets values method over gRPC.

        Aggregates the requested fields based on provided
        function.

        Returns:
            Callable[[~.AggregateAssetsValuesRequest],
                    ~.AggregateAssetsValuesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "aggregate_assets_values" not in self._stubs:
            self._stubs["aggregate_assets_values"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/AggregateAssetsValues",
                request_serializer=migrationcenter.AggregateAssetsValuesRequest.serialize,
                response_deserializer=migrationcenter.AggregateAssetsValuesResponse.deserialize,
            )
        return self._stubs["aggregate_assets_values"]

    @property
    def create_import_job(
        self,
    ) -> Callable[[migrationcenter.CreateImportJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the create import job method over gRPC.

        Creates an import job.

        Returns:
            Callable[[~.CreateImportJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_import_job" not in self._stubs:
            self._stubs["create_import_job"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/CreateImportJob",
                request_serializer=migrationcenter.CreateImportJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_import_job"]

    @property
    def list_import_jobs(
        self,
    ) -> Callable[
        [migrationcenter.ListImportJobsRequest], migrationcenter.ListImportJobsResponse
    ]:
        r"""Return a callable for the list import jobs method over gRPC.

        Lists all import jobs.

        Returns:
            Callable[[~.ListImportJobsRequest],
                    ~.ListImportJobsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_import_jobs" not in self._stubs:
            self._stubs["list_import_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListImportJobs",
                request_serializer=migrationcenter.ListImportJobsRequest.serialize,
                response_deserializer=migrationcenter.ListImportJobsResponse.deserialize,
            )
        return self._stubs["list_import_jobs"]

    @property
    def get_import_job(
        self,
    ) -> Callable[[migrationcenter.GetImportJobRequest], migrationcenter.ImportJob]:
        r"""Return a callable for the get import job method over gRPC.

        Gets the details of an import job.

        Returns:
            Callable[[~.GetImportJobRequest],
                    ~.ImportJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_import_job" not in self._stubs:
            self._stubs["get_import_job"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetImportJob",
                request_serializer=migrationcenter.GetImportJobRequest.serialize,
                response_deserializer=migrationcenter.ImportJob.deserialize,
            )
        return self._stubs["get_import_job"]

    @property
    def delete_import_job(
        self,
    ) -> Callable[[migrationcenter.DeleteImportJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete import job method over gRPC.

        Deletes an import job.

        Returns:
            Callable[[~.DeleteImportJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_import_job" not in self._stubs:
            self._stubs["delete_import_job"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteImportJob",
                request_serializer=migrationcenter.DeleteImportJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_import_job"]

    @property
    def update_import_job(
        self,
    ) -> Callable[[migrationcenter.UpdateImportJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the update import job method over gRPC.

        Updates an import job.

        Returns:
            Callable[[~.UpdateImportJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_import_job" not in self._stubs:
            self._stubs["update_import_job"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateImportJob",
                request_serializer=migrationcenter.UpdateImportJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_import_job"]

    @property
    def validate_import_job(
        self,
    ) -> Callable[[migrationcenter.ValidateImportJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the validate import job method over gRPC.

        Validates an import job.

        Returns:
            Callable[[~.ValidateImportJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "validate_import_job" not in self._stubs:
            self._stubs["validate_import_job"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ValidateImportJob",
                request_serializer=migrationcenter.ValidateImportJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["validate_import_job"]

    @property
    def run_import_job(
        self,
    ) -> Callable[[migrationcenter.RunImportJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the run import job method over gRPC.

        Runs an import job.

        Returns:
            Callable[[~.RunImportJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "run_import_job" not in self._stubs:
            self._stubs["run_import_job"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/RunImportJob",
                request_serializer=migrationcenter.RunImportJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["run_import_job"]

    @property
    def get_import_data_file(
        self,
    ) -> Callable[
        [migrationcenter.GetImportDataFileRequest], migrationcenter.ImportDataFile
    ]:
        r"""Return a callable for the get import data file method over gRPC.

        Gets an import data file.

        Returns:
            Callable[[~.GetImportDataFileRequest],
                    ~.ImportDataFile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_import_data_file" not in self._stubs:
            self._stubs["get_import_data_file"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetImportDataFile",
                request_serializer=migrationcenter.GetImportDataFileRequest.serialize,
                response_deserializer=migrationcenter.ImportDataFile.deserialize,
            )
        return self._stubs["get_import_data_file"]

    @property
    def list_import_data_files(
        self,
    ) -> Callable[
        [migrationcenter.ListImportDataFilesRequest],
        migrationcenter.ListImportDataFilesResponse,
    ]:
        r"""Return a callable for the list import data files method over gRPC.

        List import data files.

        Returns:
            Callable[[~.ListImportDataFilesRequest],
                    ~.ListImportDataFilesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_import_data_files" not in self._stubs:
            self._stubs["list_import_data_files"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListImportDataFiles",
                request_serializer=migrationcenter.ListImportDataFilesRequest.serialize,
                response_deserializer=migrationcenter.ListImportDataFilesResponse.deserialize,
            )
        return self._stubs["list_import_data_files"]

    @property
    def create_import_data_file(
        self,
    ) -> Callable[
        [migrationcenter.CreateImportDataFileRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create import data file method over gRPC.

        Creates an import data file.

        Returns:
            Callable[[~.CreateImportDataFileRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_import_data_file" not in self._stubs:
            self._stubs["create_import_data_file"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/CreateImportDataFile",
                request_serializer=migrationcenter.CreateImportDataFileRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_import_data_file"]

    @property
    def delete_import_data_file(
        self,
    ) -> Callable[
        [migrationcenter.DeleteImportDataFileRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete import data file method over gRPC.

        Delete an import data file.

        Returns:
            Callable[[~.DeleteImportDataFileRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_import_data_file" not in self._stubs:
            self._stubs["delete_import_data_file"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteImportDataFile",
                request_serializer=migrationcenter.DeleteImportDataFileRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_import_data_file"]

    @property
    def list_groups(
        self,
    ) -> Callable[
        [migrationcenter.ListGroupsRequest], migrationcenter.ListGroupsResponse
    ]:
        r"""Return a callable for the list groups method over gRPC.

        Lists all groups in a given project and location.

        Returns:
            Callable[[~.ListGroupsRequest],
                    ~.ListGroupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_groups" not in self._stubs:
            self._stubs["list_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListGroups",
                request_serializer=migrationcenter.ListGroupsRequest.serialize,
                response_deserializer=migrationcenter.ListGroupsResponse.deserialize,
            )
        return self._stubs["list_groups"]

    @property
    def get_group(
        self,
    ) -> Callable[[migrationcenter.GetGroupRequest], migrationcenter.Group]:
        r"""Return a callable for the get group method over gRPC.

        Gets the details of a group.

        Returns:
            Callable[[~.GetGroupRequest],
                    ~.Group]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_group" not in self._stubs:
            self._stubs["get_group"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetGroup",
                request_serializer=migrationcenter.GetGroupRequest.serialize,
                response_deserializer=migrationcenter.Group.deserialize,
            )
        return self._stubs["get_group"]

    @property
    def create_group(
        self,
    ) -> Callable[[migrationcenter.CreateGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the create group method over gRPC.

        Creates a new group in a given project and location.

        Returns:
            Callable[[~.CreateGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_group" not in self._stubs:
            self._stubs["create_group"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/CreateGroup",
                request_serializer=migrationcenter.CreateGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_group"]

    @property
    def update_group(
        self,
    ) -> Callable[[migrationcenter.UpdateGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the update group method over gRPC.

        Updates the parameters of a group.

        Returns:
            Callable[[~.UpdateGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_group" not in self._stubs:
            self._stubs["update_group"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateGroup",
                request_serializer=migrationcenter.UpdateGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_group"]

    @property
    def delete_group(
        self,
    ) -> Callable[[migrationcenter.DeleteGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete group method over gRPC.

        Deletes a group.

        Returns:
            Callable[[~.DeleteGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_group" not in self._stubs:
            self._stubs["delete_group"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteGroup",
                request_serializer=migrationcenter.DeleteGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_group"]

    @property
    def add_assets_to_group(
        self,
    ) -> Callable[[migrationcenter.AddAssetsToGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the add assets to group method over gRPC.

        Adds assets to a group.

        Returns:
            Callable[[~.AddAssetsToGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_assets_to_group" not in self._stubs:
            self._stubs["add_assets_to_group"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/AddAssetsToGroup",
                request_serializer=migrationcenter.AddAssetsToGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["add_assets_to_group"]

    @property
    def remove_assets_from_group(
        self,
    ) -> Callable[
        [migrationcenter.RemoveAssetsFromGroupRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the remove assets from group method over gRPC.

        Removes assets from a group.

        Returns:
            Callable[[~.RemoveAssetsFromGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_assets_from_group" not in self._stubs:
            self._stubs["remove_assets_from_group"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/RemoveAssetsFromGroup",
                request_serializer=migrationcenter.RemoveAssetsFromGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["remove_assets_from_group"]

    @property
    def list_error_frames(
        self,
    ) -> Callable[
        [migrationcenter.ListErrorFramesRequest],
        migrationcenter.ListErrorFramesResponse,
    ]:
        r"""Return a callable for the list error frames method over gRPC.

        Lists all error frames in a given source and
        location.

        Returns:
            Callable[[~.ListErrorFramesRequest],
                    ~.ListErrorFramesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_error_frames" not in self._stubs:
            self._stubs["list_error_frames"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListErrorFrames",
                request_serializer=migrationcenter.ListErrorFramesRequest.serialize,
                response_deserializer=migrationcenter.ListErrorFramesResponse.deserialize,
            )
        return self._stubs["list_error_frames"]

    @property
    def get_error_frame(
        self,
    ) -> Callable[[migrationcenter.GetErrorFrameRequest], migrationcenter.ErrorFrame]:
        r"""Return a callable for the get error frame method over gRPC.

        Gets the details of an error frame.

        Returns:
            Callable[[~.GetErrorFrameRequest],
                    ~.ErrorFrame]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_error_frame" not in self._stubs:
            self._stubs["get_error_frame"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetErrorFrame",
                request_serializer=migrationcenter.GetErrorFrameRequest.serialize,
                response_deserializer=migrationcenter.ErrorFrame.deserialize,
            )
        return self._stubs["get_error_frame"]

    @property
    def list_sources(
        self,
    ) -> Callable[
        [migrationcenter.ListSourcesRequest], migrationcenter.ListSourcesResponse
    ]:
        r"""Return a callable for the list sources method over gRPC.

        Lists all the sources in a given project and
        location.

        Returns:
            Callable[[~.ListSourcesRequest],
                    ~.ListSourcesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sources" not in self._stubs:
            self._stubs["list_sources"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListSources",
                request_serializer=migrationcenter.ListSourcesRequest.serialize,
                response_deserializer=migrationcenter.ListSourcesResponse.deserialize,
            )
        return self._stubs["list_sources"]

    @property
    def get_source(
        self,
    ) -> Callable[[migrationcenter.GetSourceRequest], migrationcenter.Source]:
        r"""Return a callable for the get source method over gRPC.

        Gets the details of a source.

        Returns:
            Callable[[~.GetSourceRequest],
                    ~.Source]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_source" not in self._stubs:
            self._stubs["get_source"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetSource",
                request_serializer=migrationcenter.GetSourceRequest.serialize,
                response_deserializer=migrationcenter.Source.deserialize,
            )
        return self._stubs["get_source"]

    @property
    def create_source(
        self,
    ) -> Callable[[migrationcenter.CreateSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the create source method over gRPC.

        Creates a new source in a given project and location.

        Returns:
            Callable[[~.CreateSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_source" not in self._stubs:
            self._stubs["create_source"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/CreateSource",
                request_serializer=migrationcenter.CreateSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_source"]

    @property
    def update_source(
        self,
    ) -> Callable[[migrationcenter.UpdateSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the update source method over gRPC.

        Updates the parameters of a source.

        Returns:
            Callable[[~.UpdateSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_source" not in self._stubs:
            self._stubs["update_source"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateSource",
                request_serializer=migrationcenter.UpdateSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_source"]

    @property
    def delete_source(
        self,
    ) -> Callable[[migrationcenter.DeleteSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete source method over gRPC.

        Deletes a source.

        Returns:
            Callable[[~.DeleteSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_source" not in self._stubs:
            self._stubs["delete_source"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteSource",
                request_serializer=migrationcenter.DeleteSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_source"]

    @property
    def list_preference_sets(
        self,
    ) -> Callable[
        [migrationcenter.ListPreferenceSetsRequest],
        migrationcenter.ListPreferenceSetsResponse,
    ]:
        r"""Return a callable for the list preference sets method over gRPC.

        Lists all the preference sets in a given project and
        location.

        Returns:
            Callable[[~.ListPreferenceSetsRequest],
                    ~.ListPreferenceSetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_preference_sets" not in self._stubs:
            self._stubs["list_preference_sets"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListPreferenceSets",
                request_serializer=migrationcenter.ListPreferenceSetsRequest.serialize,
                response_deserializer=migrationcenter.ListPreferenceSetsResponse.deserialize,
            )
        return self._stubs["list_preference_sets"]

    @property
    def get_preference_set(
        self,
    ) -> Callable[
        [migrationcenter.GetPreferenceSetRequest], migrationcenter.PreferenceSet
    ]:
        r"""Return a callable for the get preference set method over gRPC.

        Gets the details of a preference set.

        Returns:
            Callable[[~.GetPreferenceSetRequest],
                    ~.PreferenceSet]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_preference_set" not in self._stubs:
            self._stubs["get_preference_set"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetPreferenceSet",
                request_serializer=migrationcenter.GetPreferenceSetRequest.serialize,
                response_deserializer=migrationcenter.PreferenceSet.deserialize,
            )
        return self._stubs["get_preference_set"]

    @property
    def create_preference_set(
        self,
    ) -> Callable[
        [migrationcenter.CreatePreferenceSetRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create preference set method over gRPC.

        Creates a new preference set in a given project and
        location.

        Returns:
            Callable[[~.CreatePreferenceSetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_preference_set" not in self._stubs:
            self._stubs["create_preference_set"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/CreatePreferenceSet",
                request_serializer=migrationcenter.CreatePreferenceSetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_preference_set"]

    @property
    def update_preference_set(
        self,
    ) -> Callable[
        [migrationcenter.UpdatePreferenceSetRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update preference set method over gRPC.

        Updates the parameters of a preference set.

        Returns:
            Callable[[~.UpdatePreferenceSetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_preference_set" not in self._stubs:
            self._stubs["update_preference_set"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/UpdatePreferenceSet",
                request_serializer=migrationcenter.UpdatePreferenceSetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_preference_set"]

    @property
    def delete_preference_set(
        self,
    ) -> Callable[
        [migrationcenter.DeletePreferenceSetRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete preference set method over gRPC.

        Deletes a preference set.

        Returns:
            Callable[[~.DeletePreferenceSetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_preference_set" not in self._stubs:
            self._stubs["delete_preference_set"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/DeletePreferenceSet",
                request_serializer=migrationcenter.DeletePreferenceSetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_preference_set"]

    @property
    def get_settings(
        self,
    ) -> Callable[[migrationcenter.GetSettingsRequest], migrationcenter.Settings]:
        r"""Return a callable for the get settings method over gRPC.

        Gets the details of regional settings.

        Returns:
            Callable[[~.GetSettingsRequest],
                    ~.Settings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_settings" not in self._stubs:
            self._stubs["get_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetSettings",
                request_serializer=migrationcenter.GetSettingsRequest.serialize,
                response_deserializer=migrationcenter.Settings.deserialize,
            )
        return self._stubs["get_settings"]

    @property
    def update_settings(
        self,
    ) -> Callable[[migrationcenter.UpdateSettingsRequest], operations_pb2.Operation]:
        r"""Return a callable for the update settings method over gRPC.

        Updates the regional-level project settings.

        Returns:
            Callable[[~.UpdateSettingsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_settings" not in self._stubs:
            self._stubs["update_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateSettings",
                request_serializer=migrationcenter.UpdateSettingsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_settings"]

    @property
    def create_report_config(
        self,
    ) -> Callable[
        [migrationcenter.CreateReportConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create report config method over gRPC.

        Creates a report configuration.

        Returns:
            Callable[[~.CreateReportConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_report_config" not in self._stubs:
            self._stubs["create_report_config"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/CreateReportConfig",
                request_serializer=migrationcenter.CreateReportConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_report_config"]

    @property
    def get_report_config(
        self,
    ) -> Callable[
        [migrationcenter.GetReportConfigRequest], migrationcenter.ReportConfig
    ]:
        r"""Return a callable for the get report config method over gRPC.

        Gets details of a single ReportConfig.

        Returns:
            Callable[[~.GetReportConfigRequest],
                    ~.ReportConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_report_config" not in self._stubs:
            self._stubs["get_report_config"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetReportConfig",
                request_serializer=migrationcenter.GetReportConfigRequest.serialize,
                response_deserializer=migrationcenter.ReportConfig.deserialize,
            )
        return self._stubs["get_report_config"]

    @property
    def list_report_configs(
        self,
    ) -> Callable[
        [migrationcenter.ListReportConfigsRequest],
        migrationcenter.ListReportConfigsResponse,
    ]:
        r"""Return a callable for the list report configs method over gRPC.

        Lists ReportConfigs in a given project and location.

        Returns:
            Callable[[~.ListReportConfigsRequest],
                    ~.ListReportConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_report_configs" not in self._stubs:
            self._stubs["list_report_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListReportConfigs",
                request_serializer=migrationcenter.ListReportConfigsRequest.serialize,
                response_deserializer=migrationcenter.ListReportConfigsResponse.deserialize,
            )
        return self._stubs["list_report_configs"]

    @property
    def delete_report_config(
        self,
    ) -> Callable[
        [migrationcenter.DeleteReportConfigRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete report config method over gRPC.

        Deletes a ReportConfig.

        Returns:
            Callable[[~.DeleteReportConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_report_config" not in self._stubs:
            self._stubs["delete_report_config"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteReportConfig",
                request_serializer=migrationcenter.DeleteReportConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_report_config"]

    @property
    def create_report(
        self,
    ) -> Callable[[migrationcenter.CreateReportRequest], operations_pb2.Operation]:
        r"""Return a callable for the create report method over gRPC.

        Creates a report.

        Returns:
            Callable[[~.CreateReportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_report" not in self._stubs:
            self._stubs["create_report"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/CreateReport",
                request_serializer=migrationcenter.CreateReportRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_report"]

    @property
    def get_report(
        self,
    ) -> Callable[[migrationcenter.GetReportRequest], migrationcenter.Report]:
        r"""Return a callable for the get report method over gRPC.

        Gets details of a single Report.

        Returns:
            Callable[[~.GetReportRequest],
                    ~.Report]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_report" not in self._stubs:
            self._stubs["get_report"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/GetReport",
                request_serializer=migrationcenter.GetReportRequest.serialize,
                response_deserializer=migrationcenter.Report.deserialize,
            )
        return self._stubs["get_report"]

    @property
    def list_reports(
        self,
    ) -> Callable[
        [migrationcenter.ListReportsRequest], migrationcenter.ListReportsResponse
    ]:
        r"""Return a callable for the list reports method over gRPC.

        Lists Reports in a given ReportConfig.

        Returns:
            Callable[[~.ListReportsRequest],
                    ~.ListReportsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_reports" not in self._stubs:
            self._stubs["list_reports"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/ListReports",
                request_serializer=migrationcenter.ListReportsRequest.serialize,
                response_deserializer=migrationcenter.ListReportsResponse.deserialize,
            )
        return self._stubs["list_reports"]

    @property
    def delete_report(
        self,
    ) -> Callable[[migrationcenter.DeleteReportRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete report method over gRPC.

        Deletes a Report.

        Returns:
            Callable[[~.DeleteReportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_report" not in self._stubs:
            self._stubs["delete_report"] = self._logged_channel.unary_unary(
                "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteReport",
                request_serializer=migrationcenter.DeleteReportRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_report"]

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


__all__ = ("MigrationCenterGrpcTransport",)
