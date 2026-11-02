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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.ces_v1beta.types import evaluation, evaluation_service
from google.cloud.ces_v1beta.types import evaluation as gcc_evaluation

from .base import DEFAULT_CLIENT_INFO, EvaluationServiceTransport
from .grpc import EvaluationServiceGrpcTransport

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
                    "serviceName": "google.cloud.ces.v1beta.EvaluationService",
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
                    "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class EvaluationServiceGrpcAsyncIOTransport(EvaluationServiceTransport):
    """gRPC AsyncIO backend transport for EvaluationService.

    EvaluationService exposes methods to perform evaluation for
    the CES app.

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
        host: str = "ces.googleapis.com",
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
        host: str = "ces.googleapis.com",
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
                 The hostname to connect to (default: 'ces.googleapis.com').
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
    def run_evaluation(
        self,
    ) -> Callable[
        [evaluation.RunEvaluationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the run evaluation method over gRPC.

        Runs an evaluation of the app.

        Returns:
            Callable[[~.RunEvaluationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "run_evaluation" not in self._stubs:
            self._stubs["run_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/RunEvaluation",
                request_serializer=evaluation.RunEvaluationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["run_evaluation"]

    @property
    def upload_evaluation_audio(
        self,
    ) -> Callable[
        [evaluation_service.UploadEvaluationAudioRequest],
        Awaitable[evaluation_service.UploadEvaluationAudioResponse],
    ]:
        r"""Return a callable for the upload evaluation audio method over gRPC.

        Uploads audio for use in Golden Evaluations. Stores the audio in
        the Cloud Storage bucket defined in
        'App.logging_settings.evaluation_audio_recording_config.gcs_bucket'
        and returns a transcript.

        Returns:
            Callable[[~.UploadEvaluationAudioRequest],
                    Awaitable[~.UploadEvaluationAudioResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "upload_evaluation_audio" not in self._stubs:
            self._stubs["upload_evaluation_audio"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/UploadEvaluationAudio",
                request_serializer=evaluation_service.UploadEvaluationAudioRequest.serialize,
                response_deserializer=evaluation_service.UploadEvaluationAudioResponse.deserialize,
            )
        return self._stubs["upload_evaluation_audio"]

    @property
    def create_evaluation(
        self,
    ) -> Callable[
        [evaluation_service.CreateEvaluationRequest],
        Awaitable[gcc_evaluation.Evaluation],
    ]:
        r"""Return a callable for the create evaluation method over gRPC.

        Creates an evaluation.

        Returns:
            Callable[[~.CreateEvaluationRequest],
                    Awaitable[~.Evaluation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_evaluation" not in self._stubs:
            self._stubs["create_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/CreateEvaluation",
                request_serializer=evaluation_service.CreateEvaluationRequest.serialize,
                response_deserializer=gcc_evaluation.Evaluation.deserialize,
            )
        return self._stubs["create_evaluation"]

    @property
    def generate_evaluation(
        self,
    ) -> Callable[
        [evaluation_service.GenerateEvaluationRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the generate evaluation method over gRPC.

        Creates a golden evaluation from a conversation.

        Returns:
            Callable[[~.GenerateEvaluationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_evaluation" not in self._stubs:
            self._stubs["generate_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/GenerateEvaluation",
                request_serializer=evaluation_service.GenerateEvaluationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["generate_evaluation"]

    @property
    def import_evaluations(
        self,
    ) -> Callable[
        [evaluation_service.ImportEvaluationsRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the import evaluations method over gRPC.

        Imports evaluations into the app.

        Returns:
            Callable[[~.ImportEvaluationsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_evaluations" not in self._stubs:
            self._stubs["import_evaluations"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/ImportEvaluations",
                request_serializer=evaluation_service.ImportEvaluationsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_evaluations"]

    @property
    def create_evaluation_dataset(
        self,
    ) -> Callable[
        [evaluation_service.CreateEvaluationDatasetRequest],
        Awaitable[evaluation.EvaluationDataset],
    ]:
        r"""Return a callable for the create evaluation dataset method over gRPC.

        Creates an evaluation dataset.

        Returns:
            Callable[[~.CreateEvaluationDatasetRequest],
                    Awaitable[~.EvaluationDataset]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_evaluation_dataset" not in self._stubs:
            self._stubs["create_evaluation_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/CreateEvaluationDataset",
                request_serializer=evaluation_service.CreateEvaluationDatasetRequest.serialize,
                response_deserializer=evaluation.EvaluationDataset.deserialize,
            )
        return self._stubs["create_evaluation_dataset"]

    @property
    def update_evaluation(
        self,
    ) -> Callable[
        [evaluation_service.UpdateEvaluationRequest],
        Awaitable[gcc_evaluation.Evaluation],
    ]:
        r"""Return a callable for the update evaluation method over gRPC.

        Updates an evaluation.

        Returns:
            Callable[[~.UpdateEvaluationRequest],
                    Awaitable[~.Evaluation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_evaluation" not in self._stubs:
            self._stubs["update_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/UpdateEvaluation",
                request_serializer=evaluation_service.UpdateEvaluationRequest.serialize,
                response_deserializer=gcc_evaluation.Evaluation.deserialize,
            )
        return self._stubs["update_evaluation"]

    @property
    def update_evaluation_dataset(
        self,
    ) -> Callable[
        [evaluation_service.UpdateEvaluationDatasetRequest],
        Awaitable[evaluation.EvaluationDataset],
    ]:
        r"""Return a callable for the update evaluation dataset method over gRPC.

        Updates an evaluation dataset.

        Returns:
            Callable[[~.UpdateEvaluationDatasetRequest],
                    Awaitable[~.EvaluationDataset]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_evaluation_dataset" not in self._stubs:
            self._stubs["update_evaluation_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/UpdateEvaluationDataset",
                request_serializer=evaluation_service.UpdateEvaluationDatasetRequest.serialize,
                response_deserializer=evaluation.EvaluationDataset.deserialize,
            )
        return self._stubs["update_evaluation_dataset"]

    @property
    def delete_evaluation(
        self,
    ) -> Callable[
        [evaluation_service.DeleteEvaluationRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete evaluation method over gRPC.

        Deletes an evaluation.

        Returns:
            Callable[[~.DeleteEvaluationRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_evaluation" not in self._stubs:
            self._stubs["delete_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/DeleteEvaluation",
                request_serializer=evaluation_service.DeleteEvaluationRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_evaluation"]

    @property
    def delete_evaluation_result(
        self,
    ) -> Callable[
        [evaluation_service.DeleteEvaluationResultRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete evaluation result method over gRPC.

        Deletes an evaluation result.

        Returns:
            Callable[[~.DeleteEvaluationResultRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_evaluation_result" not in self._stubs:
            self._stubs["delete_evaluation_result"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/DeleteEvaluationResult",
                request_serializer=evaluation_service.DeleteEvaluationResultRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_evaluation_result"]

    @property
    def delete_evaluation_dataset(
        self,
    ) -> Callable[
        [evaluation_service.DeleteEvaluationDatasetRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete evaluation dataset method over gRPC.

        Deletes an evaluation dataset.

        Returns:
            Callable[[~.DeleteEvaluationDatasetRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_evaluation_dataset" not in self._stubs:
            self._stubs["delete_evaluation_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/DeleteEvaluationDataset",
                request_serializer=evaluation_service.DeleteEvaluationDatasetRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_evaluation_dataset"]

    @property
    def delete_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.DeleteEvaluationRunRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete evaluation run method over gRPC.

        Deletes an evaluation run.

        Returns:
            Callable[[~.DeleteEvaluationRunRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_evaluation_run" not in self._stubs:
            self._stubs["delete_evaluation_run"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/DeleteEvaluationRun",
                request_serializer=evaluation_service.DeleteEvaluationRunRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_evaluation_run"]

    @property
    def get_evaluation(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationRequest], Awaitable[evaluation.Evaluation]
    ]:
        r"""Return a callable for the get evaluation method over gRPC.

        Gets details of the specified evaluation.

        Returns:
            Callable[[~.GetEvaluationRequest],
                    Awaitable[~.Evaluation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_evaluation" not in self._stubs:
            self._stubs["get_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/GetEvaluation",
                request_serializer=evaluation_service.GetEvaluationRequest.serialize,
                response_deserializer=evaluation.Evaluation.deserialize,
            )
        return self._stubs["get_evaluation"]

    @property
    def get_evaluation_result(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationResultRequest],
        Awaitable[evaluation.EvaluationResult],
    ]:
        r"""Return a callable for the get evaluation result method over gRPC.

        Gets details of the specified evaluation result.

        Returns:
            Callable[[~.GetEvaluationResultRequest],
                    Awaitable[~.EvaluationResult]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_evaluation_result" not in self._stubs:
            self._stubs["get_evaluation_result"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/GetEvaluationResult",
                request_serializer=evaluation_service.GetEvaluationResultRequest.serialize,
                response_deserializer=evaluation.EvaluationResult.deserialize,
            )
        return self._stubs["get_evaluation_result"]

    @property
    def get_evaluation_dataset(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationDatasetRequest],
        Awaitable[evaluation.EvaluationDataset],
    ]:
        r"""Return a callable for the get evaluation dataset method over gRPC.

        Gets details of the specified evaluation dataset.

        Returns:
            Callable[[~.GetEvaluationDatasetRequest],
                    Awaitable[~.EvaluationDataset]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_evaluation_dataset" not in self._stubs:
            self._stubs["get_evaluation_dataset"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/GetEvaluationDataset",
                request_serializer=evaluation_service.GetEvaluationDatasetRequest.serialize,
                response_deserializer=evaluation.EvaluationDataset.deserialize,
            )
        return self._stubs["get_evaluation_dataset"]

    @property
    def get_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationRunRequest],
        Awaitable[evaluation.EvaluationRun],
    ]:
        r"""Return a callable for the get evaluation run method over gRPC.

        Gets details of the specified evaluation run.

        Returns:
            Callable[[~.GetEvaluationRunRequest],
                    Awaitable[~.EvaluationRun]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_evaluation_run" not in self._stubs:
            self._stubs["get_evaluation_run"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/GetEvaluationRun",
                request_serializer=evaluation_service.GetEvaluationRunRequest.serialize,
                response_deserializer=evaluation.EvaluationRun.deserialize,
            )
        return self._stubs["get_evaluation_run"]

    @property
    def list_evaluations(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationsRequest],
        Awaitable[evaluation_service.ListEvaluationsResponse],
    ]:
        r"""Return a callable for the list evaluations method over gRPC.

        Lists all evaluations in the given app.

        Returns:
            Callable[[~.ListEvaluationsRequest],
                    Awaitable[~.ListEvaluationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_evaluations" not in self._stubs:
            self._stubs["list_evaluations"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/ListEvaluations",
                request_serializer=evaluation_service.ListEvaluationsRequest.serialize,
                response_deserializer=evaluation_service.ListEvaluationsResponse.deserialize,
            )
        return self._stubs["list_evaluations"]

    @property
    def list_evaluation_results(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationResultsRequest],
        Awaitable[evaluation_service.ListEvaluationResultsResponse],
    ]:
        r"""Return a callable for the list evaluation results method over gRPC.

        Lists all evaluation results for a given evaluation.

        Returns:
            Callable[[~.ListEvaluationResultsRequest],
                    Awaitable[~.ListEvaluationResultsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_evaluation_results" not in self._stubs:
            self._stubs["list_evaluation_results"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/ListEvaluationResults",
                request_serializer=evaluation_service.ListEvaluationResultsRequest.serialize,
                response_deserializer=evaluation_service.ListEvaluationResultsResponse.deserialize,
            )
        return self._stubs["list_evaluation_results"]

    @property
    def list_evaluation_datasets(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationDatasetsRequest],
        Awaitable[evaluation_service.ListEvaluationDatasetsResponse],
    ]:
        r"""Return a callable for the list evaluation datasets method over gRPC.

        Lists all evaluation datasets in the given app.

        Returns:
            Callable[[~.ListEvaluationDatasetsRequest],
                    Awaitable[~.ListEvaluationDatasetsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_evaluation_datasets" not in self._stubs:
            self._stubs["list_evaluation_datasets"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/ListEvaluationDatasets",
                request_serializer=evaluation_service.ListEvaluationDatasetsRequest.serialize,
                response_deserializer=evaluation_service.ListEvaluationDatasetsResponse.deserialize,
            )
        return self._stubs["list_evaluation_datasets"]

    @property
    def list_evaluation_runs(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationRunsRequest],
        Awaitable[evaluation_service.ListEvaluationRunsResponse],
    ]:
        r"""Return a callable for the list evaluation runs method over gRPC.

        Lists all evaluation runs in the given app.

        Returns:
            Callable[[~.ListEvaluationRunsRequest],
                    Awaitable[~.ListEvaluationRunsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_evaluation_runs" not in self._stubs:
            self._stubs["list_evaluation_runs"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/ListEvaluationRuns",
                request_serializer=evaluation_service.ListEvaluationRunsRequest.serialize,
                response_deserializer=evaluation_service.ListEvaluationRunsResponse.deserialize,
            )
        return self._stubs["list_evaluation_runs"]

    @property
    def list_evaluation_expectations(
        self,
    ) -> Callable[
        [evaluation_service.ListEvaluationExpectationsRequest],
        Awaitable[evaluation_service.ListEvaluationExpectationsResponse],
    ]:
        r"""Return a callable for the list evaluation expectations method over gRPC.

        Lists all evaluation expectations in the given app.

        Returns:
            Callable[[~.ListEvaluationExpectationsRequest],
                    Awaitable[~.ListEvaluationExpectationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_evaluation_expectations" not in self._stubs:
            self._stubs["list_evaluation_expectations"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/ListEvaluationExpectations",
                    request_serializer=evaluation_service.ListEvaluationExpectationsRequest.serialize,
                    response_deserializer=evaluation_service.ListEvaluationExpectationsResponse.deserialize,
                )
            )
        return self._stubs["list_evaluation_expectations"]

    @property
    def get_evaluation_expectation(
        self,
    ) -> Callable[
        [evaluation_service.GetEvaluationExpectationRequest],
        Awaitable[evaluation.EvaluationExpectation],
    ]:
        r"""Return a callable for the get evaluation expectation method over gRPC.

        Gets details of the specified evaluation expectation.

        Returns:
            Callable[[~.GetEvaluationExpectationRequest],
                    Awaitable[~.EvaluationExpectation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_evaluation_expectation" not in self._stubs:
            self._stubs["get_evaluation_expectation"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/GetEvaluationExpectation",
                    request_serializer=evaluation_service.GetEvaluationExpectationRequest.serialize,
                    response_deserializer=evaluation.EvaluationExpectation.deserialize,
                )
            )
        return self._stubs["get_evaluation_expectation"]

    @property
    def create_evaluation_expectation(
        self,
    ) -> Callable[
        [evaluation_service.CreateEvaluationExpectationRequest],
        Awaitable[evaluation.EvaluationExpectation],
    ]:
        r"""Return a callable for the create evaluation expectation method over gRPC.

        Creates an evaluation expectation.

        Returns:
            Callable[[~.CreateEvaluationExpectationRequest],
                    Awaitable[~.EvaluationExpectation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_evaluation_expectation" not in self._stubs:
            self._stubs["create_evaluation_expectation"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/CreateEvaluationExpectation",
                    request_serializer=evaluation_service.CreateEvaluationExpectationRequest.serialize,
                    response_deserializer=evaluation.EvaluationExpectation.deserialize,
                )
            )
        return self._stubs["create_evaluation_expectation"]

    @property
    def update_evaluation_expectation(
        self,
    ) -> Callable[
        [evaluation_service.UpdateEvaluationExpectationRequest],
        Awaitable[evaluation.EvaluationExpectation],
    ]:
        r"""Return a callable for the update evaluation expectation method over gRPC.

        Updates an evaluation expectation.

        Returns:
            Callable[[~.UpdateEvaluationExpectationRequest],
                    Awaitable[~.EvaluationExpectation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_evaluation_expectation" not in self._stubs:
            self._stubs["update_evaluation_expectation"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/UpdateEvaluationExpectation",
                    request_serializer=evaluation_service.UpdateEvaluationExpectationRequest.serialize,
                    response_deserializer=evaluation.EvaluationExpectation.deserialize,
                )
            )
        return self._stubs["update_evaluation_expectation"]

    @property
    def delete_evaluation_expectation(
        self,
    ) -> Callable[
        [evaluation_service.DeleteEvaluationExpectationRequest],
        Awaitable[empty_pb2.Empty],
    ]:
        r"""Return a callable for the delete evaluation expectation method over gRPC.

        Deletes an evaluation expectation.

        Returns:
            Callable[[~.DeleteEvaluationExpectationRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_evaluation_expectation" not in self._stubs:
            self._stubs["delete_evaluation_expectation"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/DeleteEvaluationExpectation",
                    request_serializer=evaluation_service.DeleteEvaluationExpectationRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_evaluation_expectation"]

    @property
    def create_scheduled_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.CreateScheduledEvaluationRunRequest],
        Awaitable[evaluation.ScheduledEvaluationRun],
    ]:
        r"""Return a callable for the create scheduled evaluation
        run method over gRPC.

        Creates a scheduled evaluation run.

        Returns:
            Callable[[~.CreateScheduledEvaluationRunRequest],
                    Awaitable[~.ScheduledEvaluationRun]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_scheduled_evaluation_run" not in self._stubs:
            self._stubs["create_scheduled_evaluation_run"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/CreateScheduledEvaluationRun",
                    request_serializer=evaluation_service.CreateScheduledEvaluationRunRequest.serialize,
                    response_deserializer=evaluation.ScheduledEvaluationRun.deserialize,
                )
            )
        return self._stubs["create_scheduled_evaluation_run"]

    @property
    def get_scheduled_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.GetScheduledEvaluationRunRequest],
        Awaitable[evaluation.ScheduledEvaluationRun],
    ]:
        r"""Return a callable for the get scheduled evaluation run method over gRPC.

        Gets details of the specified scheduled evaluation
        run.

        Returns:
            Callable[[~.GetScheduledEvaluationRunRequest],
                    Awaitable[~.ScheduledEvaluationRun]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_scheduled_evaluation_run" not in self._stubs:
            self._stubs["get_scheduled_evaluation_run"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/GetScheduledEvaluationRun",
                    request_serializer=evaluation_service.GetScheduledEvaluationRunRequest.serialize,
                    response_deserializer=evaluation.ScheduledEvaluationRun.deserialize,
                )
            )
        return self._stubs["get_scheduled_evaluation_run"]

    @property
    def list_scheduled_evaluation_runs(
        self,
    ) -> Callable[
        [evaluation_service.ListScheduledEvaluationRunsRequest],
        Awaitable[evaluation_service.ListScheduledEvaluationRunsResponse],
    ]:
        r"""Return a callable for the list scheduled evaluation runs method over gRPC.

        Lists all scheduled evaluation runs in the given app.

        Returns:
            Callable[[~.ListScheduledEvaluationRunsRequest],
                    Awaitable[~.ListScheduledEvaluationRunsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_scheduled_evaluation_runs" not in self._stubs:
            self._stubs["list_scheduled_evaluation_runs"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/ListScheduledEvaluationRuns",
                    request_serializer=evaluation_service.ListScheduledEvaluationRunsRequest.serialize,
                    response_deserializer=evaluation_service.ListScheduledEvaluationRunsResponse.deserialize,
                )
            )
        return self._stubs["list_scheduled_evaluation_runs"]

    @property
    def update_scheduled_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.UpdateScheduledEvaluationRunRequest],
        Awaitable[evaluation.ScheduledEvaluationRun],
    ]:
        r"""Return a callable for the update scheduled evaluation
        run method over gRPC.

        Updates a scheduled evaluation run.

        Returns:
            Callable[[~.UpdateScheduledEvaluationRunRequest],
                    Awaitable[~.ScheduledEvaluationRun]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_scheduled_evaluation_run" not in self._stubs:
            self._stubs["update_scheduled_evaluation_run"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/UpdateScheduledEvaluationRun",
                    request_serializer=evaluation_service.UpdateScheduledEvaluationRunRequest.serialize,
                    response_deserializer=evaluation.ScheduledEvaluationRun.deserialize,
                )
            )
        return self._stubs["update_scheduled_evaluation_run"]

    @property
    def delete_scheduled_evaluation_run(
        self,
    ) -> Callable[
        [evaluation_service.DeleteScheduledEvaluationRunRequest],
        Awaitable[empty_pb2.Empty],
    ]:
        r"""Return a callable for the delete scheduled evaluation
        run method over gRPC.

        Deletes a scheduled evaluation run.

        Returns:
            Callable[[~.DeleteScheduledEvaluationRunRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_scheduled_evaluation_run" not in self._stubs:
            self._stubs["delete_scheduled_evaluation_run"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/DeleteScheduledEvaluationRun",
                    request_serializer=evaluation_service.DeleteScheduledEvaluationRunRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_scheduled_evaluation_run"]

    @property
    def test_persona_voice(
        self,
    ) -> Callable[
        [evaluation_service.TestPersonaVoiceRequest],
        Awaitable[evaluation_service.TestPersonaVoiceResponse],
    ]:
        r"""Return a callable for the test persona voice method over gRPC.

        Tests the voice of a persona. Also accepts a default
        persona.

        Returns:
            Callable[[~.TestPersonaVoiceRequest],
                    Awaitable[~.TestPersonaVoiceResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_persona_voice" not in self._stubs:
            self._stubs["test_persona_voice"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/TestPersonaVoice",
                request_serializer=evaluation_service.TestPersonaVoiceRequest.serialize,
                response_deserializer=evaluation_service.TestPersonaVoiceResponse.deserialize,
            )
        return self._stubs["test_persona_voice"]

    @property
    def export_evaluations(
        self,
    ) -> Callable[
        [evaluation_service.ExportEvaluationsRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the export evaluations method over gRPC.

        Exports evaluations.

        Returns:
            Callable[[~.ExportEvaluationsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_evaluations" not in self._stubs:
            self._stubs["export_evaluations"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/ExportEvaluations",
                request_serializer=evaluation_service.ExportEvaluationsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_evaluations"]

    @property
    def export_evaluation_runs(
        self,
    ) -> Callable[
        [evaluation_service.ExportEvaluationRunsRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the export evaluation runs method over gRPC.

        Exports evaluations runs.

        Returns:
            Callable[[~.ExportEvaluationRunsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_evaluation_runs" not in self._stubs:
            self._stubs["export_evaluation_runs"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/ExportEvaluationRuns",
                request_serializer=evaluation_service.ExportEvaluationRunsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_evaluation_runs"]

    @property
    def export_evaluation_results(
        self,
    ) -> Callable[
        [evaluation_service.ExportEvaluationResultsRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the export evaluation results method over gRPC.

        Exports evaluations results.

        Returns:
            Callable[[~.ExportEvaluationResultsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_evaluation_results" not in self._stubs:
            self._stubs["export_evaluation_results"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.EvaluationService/ExportEvaluationResults",
                request_serializer=evaluation_service.ExportEvaluationResultsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_evaluation_results"]

    @property
    def run_evaluation_result_metrics(
        self,
    ) -> Callable[
        [evaluation_service.RunEvaluationResultMetricsRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the run evaluation result metrics method over gRPC.

        Runs metrics on an existing evaluation result.

        Returns:
            Callable[[~.RunEvaluationResultMetricsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "run_evaluation_result_metrics" not in self._stubs:
            self._stubs["run_evaluation_result_metrics"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.EvaluationService/RunEvaluationResultMetrics",
                    request_serializer=evaluation_service.RunEvaluationResultMetricsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["run_evaluation_result_metrics"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.run_evaluation: self._wrap_method(
                self.run_evaluation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.upload_evaluation_audio: self._wrap_method(
                self.upload_evaluation_audio,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_evaluation: self._wrap_method(
                self.create_evaluation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.generate_evaluation: self._wrap_method(
                self.generate_evaluation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_evaluations: self._wrap_method(
                self.import_evaluations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_evaluation_dataset: self._wrap_method(
                self.create_evaluation_dataset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_evaluation: self._wrap_method(
                self.update_evaluation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_evaluation_dataset: self._wrap_method(
                self.update_evaluation_dataset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_evaluation: self._wrap_method(
                self.delete_evaluation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_evaluation_result: self._wrap_method(
                self.delete_evaluation_result,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_evaluation_dataset: self._wrap_method(
                self.delete_evaluation_dataset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_evaluation_run: self._wrap_method(
                self.delete_evaluation_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_evaluation: self._wrap_method(
                self.get_evaluation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_evaluation_result: self._wrap_method(
                self.get_evaluation_result,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_evaluation_dataset: self._wrap_method(
                self.get_evaluation_dataset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_evaluation_run: self._wrap_method(
                self.get_evaluation_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_evaluations: self._wrap_method(
                self.list_evaluations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_evaluation_results: self._wrap_method(
                self.list_evaluation_results,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_evaluation_datasets: self._wrap_method(
                self.list_evaluation_datasets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_evaluation_runs: self._wrap_method(
                self.list_evaluation_runs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_evaluation_expectations: self._wrap_method(
                self.list_evaluation_expectations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_evaluation_expectation: self._wrap_method(
                self.get_evaluation_expectation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_evaluation_expectation: self._wrap_method(
                self.create_evaluation_expectation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_evaluation_expectation: self._wrap_method(
                self.update_evaluation_expectation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_evaluation_expectation: self._wrap_method(
                self.delete_evaluation_expectation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_scheduled_evaluation_run: self._wrap_method(
                self.create_scheduled_evaluation_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_scheduled_evaluation_run: self._wrap_method(
                self.get_scheduled_evaluation_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_scheduled_evaluation_runs: self._wrap_method(
                self.list_scheduled_evaluation_runs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_scheduled_evaluation_run: self._wrap_method(
                self.update_scheduled_evaluation_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_scheduled_evaluation_run: self._wrap_method(
                self.delete_scheduled_evaluation_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_persona_voice: self._wrap_method(
                self.test_persona_voice,
                default_timeout=None,
                client_info=client_info,
            ),
            self.export_evaluations: self._wrap_method(
                self.export_evaluations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.export_evaluation_runs: self._wrap_method(
                self.export_evaluation_runs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.export_evaluation_results: self._wrap_method(
                self.export_evaluation_results,
                default_timeout=None,
                client_info=client_info,
            ),
            self.run_evaluation_result_metrics: self._wrap_method(
                self.run_evaluation_result_metrics,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
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


__all__ = ("EvaluationServiceGrpcAsyncIOTransport",)
