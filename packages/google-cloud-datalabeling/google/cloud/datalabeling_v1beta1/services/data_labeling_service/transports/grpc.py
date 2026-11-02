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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.datalabeling_v1beta1.types import (
    annotation_spec_set,
    data_labeling_service,
    dataset,
    evaluation,
    evaluation_job,
    instruction,
)
from google.cloud.datalabeling_v1beta1.types import (
    annotation_spec_set as gcd_annotation_spec_set,
)
from google.cloud.datalabeling_v1beta1.types import dataset as gcd_dataset
from google.cloud.datalabeling_v1beta1.types import evaluation_job as gcd_evaluation_job

from .base import DEFAULT_CLIENT_INFO, DataLabelingServiceTransport

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
                    "serviceName": "google.cloud.datalabeling.v1beta1.DataLabelingService",
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
                    "serviceName": "google.cloud.datalabeling.v1beta1.DataLabelingService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DataLabelingServiceGrpcTransport(DataLabelingServiceTransport):
    """gRPC backend transport for DataLabelingService.

    Service for the AI Platform Data Labeling API.

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
        host: str = "datalabeling.googleapis.com",
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
                 The hostname to connect to (default: 'datalabeling.googleapis.com').
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
        host: str = "datalabeling.googleapis.com",
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
    def create_dataset(
        self,
    ) -> Callable[[data_labeling_service.CreateDatasetRequest], gcd_dataset.Dataset]:
        r"""Return a callable for the create dataset method over gRPC.

        Creates dataset. If success return a Dataset
        resource.

        Returns:
            Callable[[~.CreateDatasetRequest],
                    ~.Dataset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_dataset" not in self._stubs:
            self._stubs["create_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/CreateDataset",
                request_serializer=data_labeling_service.CreateDatasetRequest.serialize,
                response_deserializer=gcd_dataset.Dataset.deserialize,
            )
        return self._stubs["create_dataset"]

    @property
    def get_dataset(
        self,
    ) -> Callable[[data_labeling_service.GetDatasetRequest], dataset.Dataset]:
        r"""Return a callable for the get dataset method over gRPC.

        Gets dataset by resource name.

        Returns:
            Callable[[~.GetDatasetRequest],
                    ~.Dataset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dataset" not in self._stubs:
            self._stubs["get_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetDataset",
                request_serializer=data_labeling_service.GetDatasetRequest.serialize,
                response_deserializer=dataset.Dataset.deserialize,
            )
        return self._stubs["get_dataset"]

    @property
    def list_datasets(
        self,
    ) -> Callable[
        [data_labeling_service.ListDatasetsRequest],
        data_labeling_service.ListDatasetsResponse,
    ]:
        r"""Return a callable for the list datasets method over gRPC.

        Lists datasets under a project. Pagination is
        supported.

        Returns:
            Callable[[~.ListDatasetsRequest],
                    ~.ListDatasetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_datasets" not in self._stubs:
            self._stubs["list_datasets"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListDatasets",
                request_serializer=data_labeling_service.ListDatasetsRequest.serialize,
                response_deserializer=data_labeling_service.ListDatasetsResponse.deserialize,
            )
        return self._stubs["list_datasets"]

    @property
    def delete_dataset(
        self,
    ) -> Callable[[data_labeling_service.DeleteDatasetRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete dataset method over gRPC.

        Deletes a dataset by resource name.

        Returns:
            Callable[[~.DeleteDatasetRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_dataset" not in self._stubs:
            self._stubs["delete_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteDataset",
                request_serializer=data_labeling_service.DeleteDatasetRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_dataset"]

    @property
    def import_data(
        self,
    ) -> Callable[[data_labeling_service.ImportDataRequest], operations_pb2.Operation]:
        r"""Return a callable for the import data method over gRPC.

        Imports data into dataset based on source locations
        defined in request. It can be called multiple times for
        the same dataset. Each dataset can only have one long
        running operation running on it. For example, no
        labeling task (also long running operation) can be
        started while importing is still ongoing. Vice versa.

        Returns:
            Callable[[~.ImportDataRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_data" not in self._stubs:
            self._stubs["import_data"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ImportData",
                request_serializer=data_labeling_service.ImportDataRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_data"]

    @property
    def export_data(
        self,
    ) -> Callable[[data_labeling_service.ExportDataRequest], operations_pb2.Operation]:
        r"""Return a callable for the export data method over gRPC.

        Exports data and annotations from dataset.

        Returns:
            Callable[[~.ExportDataRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_data" not in self._stubs:
            self._stubs["export_data"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ExportData",
                request_serializer=data_labeling_service.ExportDataRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_data"]

    @property
    def get_data_item(
        self,
    ) -> Callable[[data_labeling_service.GetDataItemRequest], dataset.DataItem]:
        r"""Return a callable for the get data item method over gRPC.

        Gets a data item in a dataset by resource name. This
        API can be called after data are imported into dataset.

        Returns:
            Callable[[~.GetDataItemRequest],
                    ~.DataItem]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_data_item" not in self._stubs:
            self._stubs["get_data_item"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetDataItem",
                request_serializer=data_labeling_service.GetDataItemRequest.serialize,
                response_deserializer=dataset.DataItem.deserialize,
            )
        return self._stubs["get_data_item"]

    @property
    def list_data_items(
        self,
    ) -> Callable[
        [data_labeling_service.ListDataItemsRequest],
        data_labeling_service.ListDataItemsResponse,
    ]:
        r"""Return a callable for the list data items method over gRPC.

        Lists data items in a dataset. This API can be called
        after data are imported into dataset. Pagination is
        supported.

        Returns:
            Callable[[~.ListDataItemsRequest],
                    ~.ListDataItemsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_data_items" not in self._stubs:
            self._stubs["list_data_items"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListDataItems",
                request_serializer=data_labeling_service.ListDataItemsRequest.serialize,
                response_deserializer=data_labeling_service.ListDataItemsResponse.deserialize,
            )
        return self._stubs["list_data_items"]

    @property
    def get_annotated_dataset(
        self,
    ) -> Callable[
        [data_labeling_service.GetAnnotatedDatasetRequest], dataset.AnnotatedDataset
    ]:
        r"""Return a callable for the get annotated dataset method over gRPC.

        Gets an annotated dataset by resource name.

        Returns:
            Callable[[~.GetAnnotatedDatasetRequest],
                    ~.AnnotatedDataset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_annotated_dataset" not in self._stubs:
            self._stubs["get_annotated_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetAnnotatedDataset",
                request_serializer=data_labeling_service.GetAnnotatedDatasetRequest.serialize,
                response_deserializer=dataset.AnnotatedDataset.deserialize,
            )
        return self._stubs["get_annotated_dataset"]

    @property
    def list_annotated_datasets(
        self,
    ) -> Callable[
        [data_labeling_service.ListAnnotatedDatasetsRequest],
        data_labeling_service.ListAnnotatedDatasetsResponse,
    ]:
        r"""Return a callable for the list annotated datasets method over gRPC.

        Lists annotated datasets for a dataset. Pagination is
        supported.

        Returns:
            Callable[[~.ListAnnotatedDatasetsRequest],
                    ~.ListAnnotatedDatasetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_annotated_datasets" not in self._stubs:
            self._stubs["list_annotated_datasets"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListAnnotatedDatasets",
                request_serializer=data_labeling_service.ListAnnotatedDatasetsRequest.serialize,
                response_deserializer=data_labeling_service.ListAnnotatedDatasetsResponse.deserialize,
            )
        return self._stubs["list_annotated_datasets"]

    @property
    def delete_annotated_dataset(
        self,
    ) -> Callable[
        [data_labeling_service.DeleteAnnotatedDatasetRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete annotated dataset method over gRPC.

        Deletes an annotated dataset by resource name.

        Returns:
            Callable[[~.DeleteAnnotatedDatasetRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_annotated_dataset" not in self._stubs:
            self._stubs["delete_annotated_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteAnnotatedDataset",
                request_serializer=data_labeling_service.DeleteAnnotatedDatasetRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_annotated_dataset"]

    @property
    def label_image(
        self,
    ) -> Callable[[data_labeling_service.LabelImageRequest], operations_pb2.Operation]:
        r"""Return a callable for the label image method over gRPC.

        Starts a labeling task for image. The type of image
        labeling task is configured by feature in the request.

        Returns:
            Callable[[~.LabelImageRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "label_image" not in self._stubs:
            self._stubs["label_image"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/LabelImage",
                request_serializer=data_labeling_service.LabelImageRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["label_image"]

    @property
    def label_video(
        self,
    ) -> Callable[[data_labeling_service.LabelVideoRequest], operations_pb2.Operation]:
        r"""Return a callable for the label video method over gRPC.

        Starts a labeling task for video. The type of video
        labeling task is configured by feature in the request.

        Returns:
            Callable[[~.LabelVideoRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "label_video" not in self._stubs:
            self._stubs["label_video"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/LabelVideo",
                request_serializer=data_labeling_service.LabelVideoRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["label_video"]

    @property
    def label_text(
        self,
    ) -> Callable[[data_labeling_service.LabelTextRequest], operations_pb2.Operation]:
        r"""Return a callable for the label text method over gRPC.

        Starts a labeling task for text. The type of text
        labeling task is configured by feature in the request.

        Returns:
            Callable[[~.LabelTextRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "label_text" not in self._stubs:
            self._stubs["label_text"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/LabelText",
                request_serializer=data_labeling_service.LabelTextRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["label_text"]

    @property
    def get_example(
        self,
    ) -> Callable[[data_labeling_service.GetExampleRequest], dataset.Example]:
        r"""Return a callable for the get example method over gRPC.

        Gets an example by resource name, including both data
        and annotation.

        Returns:
            Callable[[~.GetExampleRequest],
                    ~.Example]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_example" not in self._stubs:
            self._stubs["get_example"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetExample",
                request_serializer=data_labeling_service.GetExampleRequest.serialize,
                response_deserializer=dataset.Example.deserialize,
            )
        return self._stubs["get_example"]

    @property
    def list_examples(
        self,
    ) -> Callable[
        [data_labeling_service.ListExamplesRequest],
        data_labeling_service.ListExamplesResponse,
    ]:
        r"""Return a callable for the list examples method over gRPC.

        Lists examples in an annotated dataset. Pagination is
        supported.

        Returns:
            Callable[[~.ListExamplesRequest],
                    ~.ListExamplesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_examples" not in self._stubs:
            self._stubs["list_examples"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListExamples",
                request_serializer=data_labeling_service.ListExamplesRequest.serialize,
                response_deserializer=data_labeling_service.ListExamplesResponse.deserialize,
            )
        return self._stubs["list_examples"]

    @property
    def create_annotation_spec_set(
        self,
    ) -> Callable[
        [data_labeling_service.CreateAnnotationSpecSetRequest],
        gcd_annotation_spec_set.AnnotationSpecSet,
    ]:
        r"""Return a callable for the create annotation spec set method over gRPC.

        Creates an annotation spec set by providing a set of
        labels.

        Returns:
            Callable[[~.CreateAnnotationSpecSetRequest],
                    ~.AnnotationSpecSet]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_annotation_spec_set" not in self._stubs:
            self._stubs["create_annotation_spec_set"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.datalabeling.v1beta1.DataLabelingService/CreateAnnotationSpecSet",
                    request_serializer=data_labeling_service.CreateAnnotationSpecSetRequest.serialize,
                    response_deserializer=gcd_annotation_spec_set.AnnotationSpecSet.deserialize,
                )
            )
        return self._stubs["create_annotation_spec_set"]

    @property
    def get_annotation_spec_set(
        self,
    ) -> Callable[
        [data_labeling_service.GetAnnotationSpecSetRequest],
        annotation_spec_set.AnnotationSpecSet,
    ]:
        r"""Return a callable for the get annotation spec set method over gRPC.

        Gets an annotation spec set by resource name.

        Returns:
            Callable[[~.GetAnnotationSpecSetRequest],
                    ~.AnnotationSpecSet]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_annotation_spec_set" not in self._stubs:
            self._stubs["get_annotation_spec_set"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetAnnotationSpecSet",
                request_serializer=data_labeling_service.GetAnnotationSpecSetRequest.serialize,
                response_deserializer=annotation_spec_set.AnnotationSpecSet.deserialize,
            )
        return self._stubs["get_annotation_spec_set"]

    @property
    def list_annotation_spec_sets(
        self,
    ) -> Callable[
        [data_labeling_service.ListAnnotationSpecSetsRequest],
        data_labeling_service.ListAnnotationSpecSetsResponse,
    ]:
        r"""Return a callable for the list annotation spec sets method over gRPC.

        Lists annotation spec sets for a project. Pagination
        is supported.

        Returns:
            Callable[[~.ListAnnotationSpecSetsRequest],
                    ~.ListAnnotationSpecSetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_annotation_spec_sets" not in self._stubs:
            self._stubs["list_annotation_spec_sets"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListAnnotationSpecSets",
                request_serializer=data_labeling_service.ListAnnotationSpecSetsRequest.serialize,
                response_deserializer=data_labeling_service.ListAnnotationSpecSetsResponse.deserialize,
            )
        return self._stubs["list_annotation_spec_sets"]

    @property
    def delete_annotation_spec_set(
        self,
    ) -> Callable[
        [data_labeling_service.DeleteAnnotationSpecSetRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete annotation spec set method over gRPC.

        Deletes an annotation spec set by resource name.

        Returns:
            Callable[[~.DeleteAnnotationSpecSetRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_annotation_spec_set" not in self._stubs:
            self._stubs["delete_annotation_spec_set"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteAnnotationSpecSet",
                    request_serializer=data_labeling_service.DeleteAnnotationSpecSetRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_annotation_spec_set"]

    @property
    def create_instruction(
        self,
    ) -> Callable[
        [data_labeling_service.CreateInstructionRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create instruction method over gRPC.

        Creates an instruction for how data should be
        labeled.

        Returns:
            Callable[[~.CreateInstructionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_instruction" not in self._stubs:
            self._stubs["create_instruction"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/CreateInstruction",
                request_serializer=data_labeling_service.CreateInstructionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_instruction"]

    @property
    def get_instruction(
        self,
    ) -> Callable[
        [data_labeling_service.GetInstructionRequest], instruction.Instruction
    ]:
        r"""Return a callable for the get instruction method over gRPC.

        Gets an instruction by resource name.

        Returns:
            Callable[[~.GetInstructionRequest],
                    ~.Instruction]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_instruction" not in self._stubs:
            self._stubs["get_instruction"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetInstruction",
                request_serializer=data_labeling_service.GetInstructionRequest.serialize,
                response_deserializer=instruction.Instruction.deserialize,
            )
        return self._stubs["get_instruction"]

    @property
    def list_instructions(
        self,
    ) -> Callable[
        [data_labeling_service.ListInstructionsRequest],
        data_labeling_service.ListInstructionsResponse,
    ]:
        r"""Return a callable for the list instructions method over gRPC.

        Lists instructions for a project. Pagination is
        supported.

        Returns:
            Callable[[~.ListInstructionsRequest],
                    ~.ListInstructionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_instructions" not in self._stubs:
            self._stubs["list_instructions"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListInstructions",
                request_serializer=data_labeling_service.ListInstructionsRequest.serialize,
                response_deserializer=data_labeling_service.ListInstructionsResponse.deserialize,
            )
        return self._stubs["list_instructions"]

    @property
    def delete_instruction(
        self,
    ) -> Callable[[data_labeling_service.DeleteInstructionRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete instruction method over gRPC.

        Deletes an instruction object by resource name.

        Returns:
            Callable[[~.DeleteInstructionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_instruction" not in self._stubs:
            self._stubs["delete_instruction"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteInstruction",
                request_serializer=data_labeling_service.DeleteInstructionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_instruction"]

    @property
    def get_evaluation(
        self,
    ) -> Callable[[data_labeling_service.GetEvaluationRequest], evaluation.Evaluation]:
        r"""Return a callable for the get evaluation method over gRPC.

        Gets an evaluation by resource name (to search, use
        [projects.evaluations.search][google.cloud.datalabeling.v1beta1.DataLabelingService.SearchEvaluations]).

        Returns:
            Callable[[~.GetEvaluationRequest],
                    ~.Evaluation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_evaluation" not in self._stubs:
            self._stubs["get_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetEvaluation",
                request_serializer=data_labeling_service.GetEvaluationRequest.serialize,
                response_deserializer=evaluation.Evaluation.deserialize,
            )
        return self._stubs["get_evaluation"]

    @property
    def search_evaluations(
        self,
    ) -> Callable[
        [data_labeling_service.SearchEvaluationsRequest],
        data_labeling_service.SearchEvaluationsResponse,
    ]:
        r"""Return a callable for the search evaluations method over gRPC.

        Searches
        [evaluations][google.cloud.datalabeling.v1beta1.Evaluation]
        within a project.

        Returns:
            Callable[[~.SearchEvaluationsRequest],
                    ~.SearchEvaluationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_evaluations" not in self._stubs:
            self._stubs["search_evaluations"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/SearchEvaluations",
                request_serializer=data_labeling_service.SearchEvaluationsRequest.serialize,
                response_deserializer=data_labeling_service.SearchEvaluationsResponse.deserialize,
            )
        return self._stubs["search_evaluations"]

    @property
    def search_example_comparisons(
        self,
    ) -> Callable[
        [data_labeling_service.SearchExampleComparisonsRequest],
        data_labeling_service.SearchExampleComparisonsResponse,
    ]:
        r"""Return a callable for the search example comparisons method over gRPC.

        Searches example comparisons from an evaluation. The
        return format is a list of example comparisons that show
        ground truth and prediction(s) for a single input.
        Search by providing an evaluation ID.

        Returns:
            Callable[[~.SearchExampleComparisonsRequest],
                    ~.SearchExampleComparisonsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_example_comparisons" not in self._stubs:
            self._stubs["search_example_comparisons"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.datalabeling.v1beta1.DataLabelingService/SearchExampleComparisons",
                    request_serializer=data_labeling_service.SearchExampleComparisonsRequest.serialize,
                    response_deserializer=data_labeling_service.SearchExampleComparisonsResponse.deserialize,
                )
            )
        return self._stubs["search_example_comparisons"]

    @property
    def create_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.CreateEvaluationJobRequest], evaluation_job.EvaluationJob
    ]:
        r"""Return a callable for the create evaluation job method over gRPC.

        Creates an evaluation job.

        Returns:
            Callable[[~.CreateEvaluationJobRequest],
                    ~.EvaluationJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_evaluation_job" not in self._stubs:
            self._stubs["create_evaluation_job"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/CreateEvaluationJob",
                request_serializer=data_labeling_service.CreateEvaluationJobRequest.serialize,
                response_deserializer=evaluation_job.EvaluationJob.deserialize,
            )
        return self._stubs["create_evaluation_job"]

    @property
    def update_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.UpdateEvaluationJobRequest],
        gcd_evaluation_job.EvaluationJob,
    ]:
        r"""Return a callable for the update evaluation job method over gRPC.

        Updates an evaluation job. You can only update certain fields of
        the job's
        [EvaluationJobConfig][google.cloud.datalabeling.v1beta1.EvaluationJobConfig]:
        ``humanAnnotationConfig.instruction``, ``exampleCount``, and
        ``exampleSamplePercentage``.

        If you want to change any other aspect of the evaluation job,
        you must delete the job and create a new one.

        Returns:
            Callable[[~.UpdateEvaluationJobRequest],
                    ~.EvaluationJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_evaluation_job" not in self._stubs:
            self._stubs["update_evaluation_job"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/UpdateEvaluationJob",
                request_serializer=data_labeling_service.UpdateEvaluationJobRequest.serialize,
                response_deserializer=gcd_evaluation_job.EvaluationJob.deserialize,
            )
        return self._stubs["update_evaluation_job"]

    @property
    def get_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.GetEvaluationJobRequest], evaluation_job.EvaluationJob
    ]:
        r"""Return a callable for the get evaluation job method over gRPC.

        Gets an evaluation job by resource name.

        Returns:
            Callable[[~.GetEvaluationJobRequest],
                    ~.EvaluationJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_evaluation_job" not in self._stubs:
            self._stubs["get_evaluation_job"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/GetEvaluationJob",
                request_serializer=data_labeling_service.GetEvaluationJobRequest.serialize,
                response_deserializer=evaluation_job.EvaluationJob.deserialize,
            )
        return self._stubs["get_evaluation_job"]

    @property
    def pause_evaluation_job(
        self,
    ) -> Callable[[data_labeling_service.PauseEvaluationJobRequest], empty_pb2.Empty]:
        r"""Return a callable for the pause evaluation job method over gRPC.

        Pauses an evaluation job. Pausing an evaluation job that is
        already in a ``PAUSED`` state is a no-op.

        Returns:
            Callable[[~.PauseEvaluationJobRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "pause_evaluation_job" not in self._stubs:
            self._stubs["pause_evaluation_job"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/PauseEvaluationJob",
                request_serializer=data_labeling_service.PauseEvaluationJobRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["pause_evaluation_job"]

    @property
    def resume_evaluation_job(
        self,
    ) -> Callable[[data_labeling_service.ResumeEvaluationJobRequest], empty_pb2.Empty]:
        r"""Return a callable for the resume evaluation job method over gRPC.

        Resumes a paused evaluation job. A deleted evaluation
        job can't be resumed. Resuming a running or scheduled
        evaluation job is a no-op.

        Returns:
            Callable[[~.ResumeEvaluationJobRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "resume_evaluation_job" not in self._stubs:
            self._stubs["resume_evaluation_job"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ResumeEvaluationJob",
                request_serializer=data_labeling_service.ResumeEvaluationJobRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["resume_evaluation_job"]

    @property
    def delete_evaluation_job(
        self,
    ) -> Callable[[data_labeling_service.DeleteEvaluationJobRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete evaluation job method over gRPC.

        Stops and deletes an evaluation job.

        Returns:
            Callable[[~.DeleteEvaluationJobRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_evaluation_job" not in self._stubs:
            self._stubs["delete_evaluation_job"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/DeleteEvaluationJob",
                request_serializer=data_labeling_service.DeleteEvaluationJobRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_evaluation_job"]

    @property
    def list_evaluation_jobs(
        self,
    ) -> Callable[
        [data_labeling_service.ListEvaluationJobsRequest],
        data_labeling_service.ListEvaluationJobsResponse,
    ]:
        r"""Return a callable for the list evaluation jobs method over gRPC.

        Lists all evaluation jobs within a project with
        possible filters. Pagination is supported.

        Returns:
            Callable[[~.ListEvaluationJobsRequest],
                    ~.ListEvaluationJobsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_evaluation_jobs" not in self._stubs:
            self._stubs["list_evaluation_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.datalabeling.v1beta1.DataLabelingService/ListEvaluationJobs",
                request_serializer=data_labeling_service.ListEvaluationJobsRequest.serialize,
                response_deserializer=data_labeling_service.ListEvaluationJobsResponse.deserialize,
            )
        return self._stubs["list_evaluation_jobs"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("DataLabelingServiceGrpcTransport",)
