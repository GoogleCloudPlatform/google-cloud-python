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

from google.cloud.automl_v1.types import (
    annotation_spec,
    dataset,
    model,
    model_evaluation,
    service,
)
from google.cloud.automl_v1.types import dataset as gca_dataset
from google.cloud.automl_v1.types import model as gca_model

from .base import DEFAULT_CLIENT_INFO, AutoMlTransport
from .grpc import AutoMlGrpcTransport

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
                    "serviceName": "google.cloud.automl.v1.AutoMl",
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
                    "serviceName": "google.cloud.automl.v1.AutoMl",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AutoMlGrpcAsyncIOTransport(AutoMlTransport):
    """gRPC AsyncIO backend transport for AutoMl.

    AutoML Server API.

    The resource names are assigned by the server. The server never
    reuses names that it has created after the resources with those
    names are deleted.

    An ID of a resource is the last element of the item's resource name.
    For
    ``projects/{project_id}/locations/{location_id}/datasets/{dataset_id}``,
    then the id for the item is ``{dataset_id}``.

    Currently the only supported ``location_id`` is "us-central1".

    On any input that is documented to expect a string parameter in
    snake_case or dash-case, either of those cases is accepted.

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
        host: str = "automl.googleapis.com",
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
        host: str = "automl.googleapis.com",
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
                 The hostname to connect to (default: 'automl.googleapis.com').
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
    def create_dataset(
        self,
    ) -> Callable[[service.CreateDatasetRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create dataset method over gRPC.

        Creates a dataset.

        Returns:
            Callable[[~.CreateDatasetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_dataset" not in self._stubs:
            self._stubs["create_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/CreateDataset",
                request_serializer=service.CreateDatasetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_dataset"]

    @property
    def get_dataset(
        self,
    ) -> Callable[[service.GetDatasetRequest], Awaitable[dataset.Dataset]]:
        r"""Return a callable for the get dataset method over gRPC.

        Gets a dataset.

        Returns:
            Callable[[~.GetDatasetRequest],
                    Awaitable[~.Dataset]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dataset" not in self._stubs:
            self._stubs["get_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/GetDataset",
                request_serializer=service.GetDatasetRequest.serialize,
                response_deserializer=dataset.Dataset.deserialize,
            )
        return self._stubs["get_dataset"]

    @property
    def list_datasets(
        self,
    ) -> Callable[
        [service.ListDatasetsRequest], Awaitable[service.ListDatasetsResponse]
    ]:
        r"""Return a callable for the list datasets method over gRPC.

        Lists datasets in a project.

        Returns:
            Callable[[~.ListDatasetsRequest],
                    Awaitable[~.ListDatasetsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_datasets" not in self._stubs:
            self._stubs["list_datasets"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/ListDatasets",
                request_serializer=service.ListDatasetsRequest.serialize,
                response_deserializer=service.ListDatasetsResponse.deserialize,
            )
        return self._stubs["list_datasets"]

    @property
    def update_dataset(
        self,
    ) -> Callable[[service.UpdateDatasetRequest], Awaitable[gca_dataset.Dataset]]:
        r"""Return a callable for the update dataset method over gRPC.

        Updates a dataset.

        Returns:
            Callable[[~.UpdateDatasetRequest],
                    Awaitable[~.Dataset]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_dataset" not in self._stubs:
            self._stubs["update_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/UpdateDataset",
                request_serializer=service.UpdateDatasetRequest.serialize,
                response_deserializer=gca_dataset.Dataset.deserialize,
            )
        return self._stubs["update_dataset"]

    @property
    def delete_dataset(
        self,
    ) -> Callable[[service.DeleteDatasetRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete dataset method over gRPC.

        Deletes a dataset and all of its contents. Returns empty
        response in the
        [response][google.longrunning.Operation.response] field when it
        completes, and ``delete_details`` in the
        [metadata][google.longrunning.Operation.metadata] field.

        Returns:
            Callable[[~.DeleteDatasetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_dataset" not in self._stubs:
            self._stubs["delete_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/DeleteDataset",
                request_serializer=service.DeleteDatasetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_dataset"]

    @property
    def import_data(
        self,
    ) -> Callable[[service.ImportDataRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the import data method over gRPC.

        Imports data into a dataset. For Tables this method can only be
        called on an empty Dataset.

        For Tables:

        - A
          [schema_inference_version][google.cloud.automl.v1.InputConfig.params]
          parameter must be explicitly set. Returns an empty response in
          the [response][google.longrunning.Operation.response] field
          when it completes.

        Returns:
            Callable[[~.ImportDataRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_data" not in self._stubs:
            self._stubs["import_data"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/ImportData",
                request_serializer=service.ImportDataRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_data"]

    @property
    def export_data(
        self,
    ) -> Callable[[service.ExportDataRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the export data method over gRPC.

        Exports dataset's data to the provided output location. Returns
        an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.ExportDataRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_data" not in self._stubs:
            self._stubs["export_data"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/ExportData",
                request_serializer=service.ExportDataRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_data"]

    @property
    def get_annotation_spec(
        self,
    ) -> Callable[
        [service.GetAnnotationSpecRequest], Awaitable[annotation_spec.AnnotationSpec]
    ]:
        r"""Return a callable for the get annotation spec method over gRPC.

        Gets an annotation spec.

        Returns:
            Callable[[~.GetAnnotationSpecRequest],
                    Awaitable[~.AnnotationSpec]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_annotation_spec" not in self._stubs:
            self._stubs["get_annotation_spec"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/GetAnnotationSpec",
                request_serializer=service.GetAnnotationSpecRequest.serialize,
                response_deserializer=annotation_spec.AnnotationSpec.deserialize,
            )
        return self._stubs["get_annotation_spec"]

    @property
    def create_model(
        self,
    ) -> Callable[[service.CreateModelRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create model method over gRPC.

        Creates a model. Returns a Model in the
        [response][google.longrunning.Operation.response] field when it
        completes. When you create a model, several model evaluations
        are created for it: a global evaluation, and one evaluation for
        each annotation spec.

        Returns:
            Callable[[~.CreateModelRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_model" not in self._stubs:
            self._stubs["create_model"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/CreateModel",
                request_serializer=service.CreateModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_model"]

    @property
    def get_model(self) -> Callable[[service.GetModelRequest], Awaitable[model.Model]]:
        r"""Return a callable for the get model method over gRPC.

        Gets a model.

        Returns:
            Callable[[~.GetModelRequest],
                    Awaitable[~.Model]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_model" not in self._stubs:
            self._stubs["get_model"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/GetModel",
                request_serializer=service.GetModelRequest.serialize,
                response_deserializer=model.Model.deserialize,
            )
        return self._stubs["get_model"]

    @property
    def list_models(
        self,
    ) -> Callable[[service.ListModelsRequest], Awaitable[service.ListModelsResponse]]:
        r"""Return a callable for the list models method over gRPC.

        Lists models.

        Returns:
            Callable[[~.ListModelsRequest],
                    Awaitable[~.ListModelsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_models" not in self._stubs:
            self._stubs["list_models"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/ListModels",
                request_serializer=service.ListModelsRequest.serialize,
                response_deserializer=service.ListModelsResponse.deserialize,
            )
        return self._stubs["list_models"]

    @property
    def delete_model(
        self,
    ) -> Callable[[service.DeleteModelRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete model method over gRPC.

        Deletes a model. Returns ``google.protobuf.Empty`` in the
        [response][google.longrunning.Operation.response] field when it
        completes, and ``delete_details`` in the
        [metadata][google.longrunning.Operation.metadata] field.

        Returns:
            Callable[[~.DeleteModelRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_model" not in self._stubs:
            self._stubs["delete_model"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/DeleteModel",
                request_serializer=service.DeleteModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_model"]

    @property
    def update_model(
        self,
    ) -> Callable[[service.UpdateModelRequest], Awaitable[gca_model.Model]]:
        r"""Return a callable for the update model method over gRPC.

        Updates a model.

        Returns:
            Callable[[~.UpdateModelRequest],
                    Awaitable[~.Model]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_model" not in self._stubs:
            self._stubs["update_model"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/UpdateModel",
                request_serializer=service.UpdateModelRequest.serialize,
                response_deserializer=gca_model.Model.deserialize,
            )
        return self._stubs["update_model"]

    @property
    def deploy_model(
        self,
    ) -> Callable[[service.DeployModelRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the deploy model method over gRPC.

        Deploys a model. If a model is already deployed, deploying it
        with the same parameters has no effect. Deploying with different
        parametrs (as e.g. changing
        [node_number][google.cloud.automl.v1p1beta.ImageObjectDetectionModelDeploymentMetadata.node_number])
        will reset the deployment state without pausing the model's
        availability.

        Only applicable for Text Classification, Image Object Detection
        , Tables, and Image Segmentation; all other domains manage
        deployment automatically.

        Returns an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.DeployModelRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_model" not in self._stubs:
            self._stubs["deploy_model"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/DeployModel",
                request_serializer=service.DeployModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["deploy_model"]

    @property
    def undeploy_model(
        self,
    ) -> Callable[[service.UndeployModelRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the undeploy model method over gRPC.

        Undeploys a model. If the model is not deployed this method has
        no effect.

        Only applicable for Text Classification, Image Object Detection
        and Tables; all other domains manage deployment automatically.

        Returns an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.UndeployModelRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undeploy_model" not in self._stubs:
            self._stubs["undeploy_model"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/UndeployModel",
                request_serializer=service.UndeployModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undeploy_model"]

    @property
    def export_model(
        self,
    ) -> Callable[[service.ExportModelRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the export model method over gRPC.

        Exports a trained, "export-able", model to a user specified
        Google Cloud Storage location. A model is considered export-able
        if and only if it has an export format defined for it in
        [ModelExportOutputConfig][google.cloud.automl.v1.ModelExportOutputConfig].

        Returns an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.ExportModelRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_model" not in self._stubs:
            self._stubs["export_model"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/ExportModel",
                request_serializer=service.ExportModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_model"]

    @property
    def get_model_evaluation(
        self,
    ) -> Callable[
        [service.GetModelEvaluationRequest], Awaitable[model_evaluation.ModelEvaluation]
    ]:
        r"""Return a callable for the get model evaluation method over gRPC.

        Gets a model evaluation.

        Returns:
            Callable[[~.GetModelEvaluationRequest],
                    Awaitable[~.ModelEvaluation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_model_evaluation" not in self._stubs:
            self._stubs["get_model_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/GetModelEvaluation",
                request_serializer=service.GetModelEvaluationRequest.serialize,
                response_deserializer=model_evaluation.ModelEvaluation.deserialize,
            )
        return self._stubs["get_model_evaluation"]

    @property
    def list_model_evaluations(
        self,
    ) -> Callable[
        [service.ListModelEvaluationsRequest],
        Awaitable[service.ListModelEvaluationsResponse],
    ]:
        r"""Return a callable for the list model evaluations method over gRPC.

        Lists model evaluations.

        Returns:
            Callable[[~.ListModelEvaluationsRequest],
                    Awaitable[~.ListModelEvaluationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_model_evaluations" not in self._stubs:
            self._stubs["list_model_evaluations"] = self._logged_channel.unary_unary(
                "/google.cloud.automl.v1.AutoMl/ListModelEvaluations",
                request_serializer=service.ListModelEvaluationsRequest.serialize,
                response_deserializer=service.ListModelEvaluationsResponse.deserialize,
            )
        return self._stubs["list_model_evaluations"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_dataset: self._wrap_method(
                self.create_dataset,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.get_dataset: self._wrap_method(
                self.get_dataset,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.list_datasets: self._wrap_method(
                self.list_datasets,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.update_dataset: self._wrap_method(
                self.update_dataset,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.delete_dataset: self._wrap_method(
                self.delete_dataset,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.import_data: self._wrap_method(
                self.import_data,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.export_data: self._wrap_method(
                self.export_data,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.get_annotation_spec: self._wrap_method(
                self.get_annotation_spec,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.create_model: self._wrap_method(
                self.create_model,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.get_model: self._wrap_method(
                self.get_model,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.list_models: self._wrap_method(
                self.list_models,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.delete_model: self._wrap_method(
                self.delete_model,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.update_model: self._wrap_method(
                self.update_model,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.deploy_model: self._wrap_method(
                self.deploy_model,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.undeploy_model: self._wrap_method(
                self.undeploy_model,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.export_model: self._wrap_method(
                self.export_model,
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.get_model_evaluation: self._wrap_method(
                self.get_model_evaluation,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
                client_info=client_info,
            ),
            self.list_model_evaluations: self._wrap_method(
                self.list_model_evaluations,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=5.0,
                ),
                default_timeout=5.0,
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


__all__ = ("AutoMlGrpcAsyncIOTransport",)
