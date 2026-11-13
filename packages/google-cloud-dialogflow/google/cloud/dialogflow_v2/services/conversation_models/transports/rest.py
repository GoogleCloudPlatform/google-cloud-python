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
import dataclasses
import json  # type: ignore
import logging
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.dialogflow_v2._compat import transcode_request
from google.cloud.dialogflow_v2.types import conversation_model
from google.cloud.dialogflow_v2.types import (
    conversation_model as gcd_conversation_model,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseConversationModelsRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ConversationModelsRestInterceptor:
    """Interceptor for ConversationModels.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ConversationModelsRestTransport.

    .. code-block:: python
        class MyCustomConversationModelsInterceptor(ConversationModelsRestInterceptor):
            def pre_create_conversation_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_conversation_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_conversation_model_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_conversation_model_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_conversation_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_conversation_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deploy_conversation_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deploy_conversation_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_conversation_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_conversation_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_conversation_model_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_conversation_model_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_conversation_model_evaluations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_conversation_model_evaluations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_conversation_models(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_conversation_models(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undeploy_conversation_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undeploy_conversation_model(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ConversationModelsRestTransport(interceptor=MyCustomConversationModelsInterceptor())
        client = ConversationModelsClient(transport=transport)


    """

    def pre_create_conversation_model(
        self,
        request: gcd_conversation_model.CreateConversationModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_conversation_model.CreateConversationModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_conversation_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_create_conversation_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_conversation_model

        DEPRECATED. Please use the `post_create_conversation_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_create_conversation_model` interceptor runs
        before the `post_create_conversation_model_with_metadata` interceptor.
        """
        return response

    def post_create_conversation_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_conversation_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_create_conversation_model_with_metadata`
        interceptor in new development instead of the `post_create_conversation_model` interceptor.
        When both interceptors are used, this `post_create_conversation_model_with_metadata` interceptor runs after the
        `post_create_conversation_model` interceptor. The (possibly modified) response returned by
        `post_create_conversation_model` will be passed to
        `post_create_conversation_model_with_metadata`.
        """
        return response, metadata

    def pre_create_conversation_model_evaluation(
        self,
        request: conversation_model.CreateConversationModelEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.CreateConversationModelEvaluationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_conversation_model_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_create_conversation_model_evaluation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_conversation_model_evaluation

        DEPRECATED. Please use the `post_create_conversation_model_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_create_conversation_model_evaluation` interceptor runs
        before the `post_create_conversation_model_evaluation_with_metadata` interceptor.
        """
        return response

    def post_create_conversation_model_evaluation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_conversation_model_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_create_conversation_model_evaluation_with_metadata`
        interceptor in new development instead of the `post_create_conversation_model_evaluation` interceptor.
        When both interceptors are used, this `post_create_conversation_model_evaluation_with_metadata` interceptor runs after the
        `post_create_conversation_model_evaluation` interceptor. The (possibly modified) response returned by
        `post_create_conversation_model_evaluation` will be passed to
        `post_create_conversation_model_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_delete_conversation_model(
        self,
        request: conversation_model.DeleteConversationModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.DeleteConversationModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_conversation_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_delete_conversation_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_conversation_model

        DEPRECATED. Please use the `post_delete_conversation_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_delete_conversation_model` interceptor runs
        before the `post_delete_conversation_model_with_metadata` interceptor.
        """
        return response

    def post_delete_conversation_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_conversation_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_delete_conversation_model_with_metadata`
        interceptor in new development instead of the `post_delete_conversation_model` interceptor.
        When both interceptors are used, this `post_delete_conversation_model_with_metadata` interceptor runs after the
        `post_delete_conversation_model` interceptor. The (possibly modified) response returned by
        `post_delete_conversation_model` will be passed to
        `post_delete_conversation_model_with_metadata`.
        """
        return response, metadata

    def pre_deploy_conversation_model(
        self,
        request: conversation_model.DeployConversationModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.DeployConversationModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for deploy_conversation_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_deploy_conversation_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for deploy_conversation_model

        DEPRECATED. Please use the `post_deploy_conversation_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_deploy_conversation_model` interceptor runs
        before the `post_deploy_conversation_model_with_metadata` interceptor.
        """
        return response

    def post_deploy_conversation_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deploy_conversation_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_deploy_conversation_model_with_metadata`
        interceptor in new development instead of the `post_deploy_conversation_model` interceptor.
        When both interceptors are used, this `post_deploy_conversation_model_with_metadata` interceptor runs after the
        `post_deploy_conversation_model` interceptor. The (possibly modified) response returned by
        `post_deploy_conversation_model` will be passed to
        `post_deploy_conversation_model_with_metadata`.
        """
        return response, metadata

    def pre_get_conversation_model(
        self,
        request: conversation_model.GetConversationModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.GetConversationModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_conversation_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_get_conversation_model(
        self, response: conversation_model.ConversationModel
    ) -> conversation_model.ConversationModel:
        """Post-rpc interceptor for get_conversation_model

        DEPRECATED. Please use the `post_get_conversation_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_get_conversation_model` interceptor runs
        before the `post_get_conversation_model_with_metadata` interceptor.
        """
        return response

    def post_get_conversation_model_with_metadata(
        self,
        response: conversation_model.ConversationModel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.ConversationModel, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_conversation_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_get_conversation_model_with_metadata`
        interceptor in new development instead of the `post_get_conversation_model` interceptor.
        When both interceptors are used, this `post_get_conversation_model_with_metadata` interceptor runs after the
        `post_get_conversation_model` interceptor. The (possibly modified) response returned by
        `post_get_conversation_model` will be passed to
        `post_get_conversation_model_with_metadata`.
        """
        return response, metadata

    def pre_get_conversation_model_evaluation(
        self,
        request: conversation_model.GetConversationModelEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.GetConversationModelEvaluationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_conversation_model_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_get_conversation_model_evaluation(
        self, response: conversation_model.ConversationModelEvaluation
    ) -> conversation_model.ConversationModelEvaluation:
        """Post-rpc interceptor for get_conversation_model_evaluation

        DEPRECATED. Please use the `post_get_conversation_model_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_get_conversation_model_evaluation` interceptor runs
        before the `post_get_conversation_model_evaluation_with_metadata` interceptor.
        """
        return response

    def post_get_conversation_model_evaluation_with_metadata(
        self,
        response: conversation_model.ConversationModelEvaluation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.ConversationModelEvaluation,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_conversation_model_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_get_conversation_model_evaluation_with_metadata`
        interceptor in new development instead of the `post_get_conversation_model_evaluation` interceptor.
        When both interceptors are used, this `post_get_conversation_model_evaluation_with_metadata` interceptor runs after the
        `post_get_conversation_model_evaluation` interceptor. The (possibly modified) response returned by
        `post_get_conversation_model_evaluation` will be passed to
        `post_get_conversation_model_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_list_conversation_model_evaluations(
        self,
        request: conversation_model.ListConversationModelEvaluationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.ListConversationModelEvaluationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_conversation_model_evaluations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_list_conversation_model_evaluations(
        self, response: conversation_model.ListConversationModelEvaluationsResponse
    ) -> conversation_model.ListConversationModelEvaluationsResponse:
        """Post-rpc interceptor for list_conversation_model_evaluations

        DEPRECATED. Please use the `post_list_conversation_model_evaluations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_list_conversation_model_evaluations` interceptor runs
        before the `post_list_conversation_model_evaluations_with_metadata` interceptor.
        """
        return response

    def post_list_conversation_model_evaluations_with_metadata(
        self,
        response: conversation_model.ListConversationModelEvaluationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.ListConversationModelEvaluationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_conversation_model_evaluations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_list_conversation_model_evaluations_with_metadata`
        interceptor in new development instead of the `post_list_conversation_model_evaluations` interceptor.
        When both interceptors are used, this `post_list_conversation_model_evaluations_with_metadata` interceptor runs after the
        `post_list_conversation_model_evaluations` interceptor. The (possibly modified) response returned by
        `post_list_conversation_model_evaluations` will be passed to
        `post_list_conversation_model_evaluations_with_metadata`.
        """
        return response, metadata

    def pre_list_conversation_models(
        self,
        request: conversation_model.ListConversationModelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.ListConversationModelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_conversation_models

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_list_conversation_models(
        self, response: conversation_model.ListConversationModelsResponse
    ) -> conversation_model.ListConversationModelsResponse:
        """Post-rpc interceptor for list_conversation_models

        DEPRECATED. Please use the `post_list_conversation_models_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_list_conversation_models` interceptor runs
        before the `post_list_conversation_models_with_metadata` interceptor.
        """
        return response

    def post_list_conversation_models_with_metadata(
        self,
        response: conversation_model.ListConversationModelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.ListConversationModelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_conversation_models

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_list_conversation_models_with_metadata`
        interceptor in new development instead of the `post_list_conversation_models` interceptor.
        When both interceptors are used, this `post_list_conversation_models_with_metadata` interceptor runs after the
        `post_list_conversation_models` interceptor. The (possibly modified) response returned by
        `post_list_conversation_models` will be passed to
        `post_list_conversation_models_with_metadata`.
        """
        return response, metadata

    def pre_undeploy_conversation_model(
        self,
        request: conversation_model.UndeployConversationModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation_model.UndeployConversationModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for undeploy_conversation_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_undeploy_conversation_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for undeploy_conversation_model

        DEPRECATED. Please use the `post_undeploy_conversation_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code. This `post_undeploy_conversation_model` interceptor runs
        before the `post_undeploy_conversation_model_with_metadata` interceptor.
        """
        return response

    def post_undeploy_conversation_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for undeploy_conversation_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversationModels server but before it is returned to user code.

        We recommend only using this `post_undeploy_conversation_model_with_metadata`
        interceptor in new development instead of the `post_undeploy_conversation_model` interceptor.
        When both interceptors are used, this `post_undeploy_conversation_model_with_metadata` interceptor runs after the
        `post_undeploy_conversation_model` interceptor. The (possibly modified) response returned by
        `post_undeploy_conversation_model` will be passed to
        `post_undeploy_conversation_model_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversationModels server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ConversationModels server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ConversationModelsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ConversationModelsRestInterceptor


class ConversationModelsRestTransport(_BaseConversationModelsRestTransport):
    """REST backend synchronous transport for ConversationModels.

    Manages a collection of models for human agent assistant.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ConversationModelsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dialogflow.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided. This argument will be
                removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[ConversationModelsRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or ConversationModelsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v2/{name=projects/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v2/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v2",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateConversationModel(
        _BaseConversationModelsRestTransport._BaseCreateConversationModel,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.CreateConversationModel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: gcd_conversation_model.CreateConversationModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create conversation model method over HTTP.

            Args:
                request (~.gcd_conversation_model.CreateConversationModelRequest):
                    The request object. The request message for
                [ConversationModels.CreateConversationModel][google.cloud.dialogflow.v2.ConversationModels.CreateConversationModel]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseConversationModelsRestTransport._BaseCreateConversationModel._get_http_options()
            request, metadata = self._interceptor.pre_create_conversation_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseCreateConversationModel,
                    "_BaseCreateConversationModel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.CreateConversationModel",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "CreateConversationModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationModelsRestTransport._CreateConversationModel._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_conversation_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_conversation_model_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.create_conversation_model",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "CreateConversationModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateConversationModelEvaluation(
        _BaseConversationModelsRestTransport._BaseCreateConversationModelEvaluation,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash(
                "ConversationModelsRestTransport.CreateConversationModelEvaluation"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: conversation_model.CreateConversationModelEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create conversation model
            evaluation method over HTTP.

                Args:
                    request (~.conversation_model.CreateConversationModelEvaluationRequest):
                        The request object. The request message for
                    [ConversationModels.CreateConversationModelEvaluation][google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelEvaluation]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = _BaseConversationModelsRestTransport._BaseCreateConversationModelEvaluation._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_conversation_model_evaluation(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseCreateConversationModelEvaluation,
                    "_BaseCreateConversationModelEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.CreateConversationModelEvaluation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "CreateConversationModelEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._CreateConversationModelEvaluation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_conversation_model_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_conversation_model_evaluation_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.create_conversation_model_evaluation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "CreateConversationModelEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConversationModel(
        _BaseConversationModelsRestTransport._BaseDeleteConversationModel,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.DeleteConversationModel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: conversation_model.DeleteConversationModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete conversation model method over HTTP.

            Args:
                request (~.conversation_model.DeleteConversationModelRequest):
                    The request object. The request message for
                [ConversationModels.DeleteConversationModel][google.cloud.dialogflow.v2.ConversationModels.DeleteConversationModel]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseConversationModelsRestTransport._BaseDeleteConversationModel._get_http_options()
            request, metadata = self._interceptor.pre_delete_conversation_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseDeleteConversationModel,
                    "_BaseDeleteConversationModel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.DeleteConversationModel",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "DeleteConversationModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationModelsRestTransport._DeleteConversationModel._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_conversation_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_conversation_model_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.delete_conversation_model",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "DeleteConversationModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeployConversationModel(
        _BaseConversationModelsRestTransport._BaseDeployConversationModel,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.DeployConversationModel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: conversation_model.DeployConversationModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the deploy conversation model method over HTTP.

            Args:
                request (~.conversation_model.DeployConversationModelRequest):
                    The request object. The request message for
                [ConversationModels.DeployConversationModel][google.cloud.dialogflow.v2.ConversationModels.DeployConversationModel]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseConversationModelsRestTransport._BaseDeployConversationModel._get_http_options()
            request, metadata = self._interceptor.pre_deploy_conversation_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseDeployConversationModel,
                    "_BaseDeployConversationModel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.DeployConversationModel",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "DeployConversationModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationModelsRestTransport._DeployConversationModel._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_deploy_conversation_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deploy_conversation_model_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.deploy_conversation_model",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "DeployConversationModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConversationModel(
        _BaseConversationModelsRestTransport._BaseGetConversationModel,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.GetConversationModel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: conversation_model.GetConversationModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation_model.ConversationModel:
            r"""Call the get conversation model method over HTTP.

            Args:
                request (~.conversation_model.GetConversationModelRequest):
                    The request object. The request message for
                [ConversationModels.GetConversationModel][google.cloud.dialogflow.v2.ConversationModels.GetConversationModel]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation_model.ConversationModel:
                    Represents a conversation model.
            """

            http_options = _BaseConversationModelsRestTransport._BaseGetConversationModel._get_http_options()
            request, metadata = self._interceptor.pre_get_conversation_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseGetConversationModel,
                    "_BaseGetConversationModel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.GetConversationModel",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "GetConversationModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationModelsRestTransport._GetConversationModel._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = conversation_model.ConversationModel()
            pb_resp = conversation_model.ConversationModel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_conversation_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_conversation_model_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation_model.ConversationModel.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.get_conversation_model",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "GetConversationModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConversationModelEvaluation(
        _BaseConversationModelsRestTransport._BaseGetConversationModelEvaluation,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash(
                "ConversationModelsRestTransport.GetConversationModelEvaluation"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: conversation_model.GetConversationModelEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation_model.ConversationModelEvaluation:
            r"""Call the get conversation model
            evaluation method over HTTP.

                Args:
                    request (~.conversation_model.GetConversationModelEvaluationRequest):
                        The request object. The request message for
                    [ConversationModels.GetConversationModelEvaluation][google.cloud.dialogflow.v2.ConversationModels.GetConversationModelEvaluation]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.conversation_model.ConversationModelEvaluation:
                        Represents evaluation result of a
                    conversation model.

            """

            http_options = _BaseConversationModelsRestTransport._BaseGetConversationModelEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_get_conversation_model_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseGetConversationModelEvaluation,
                    "_BaseGetConversationModelEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.GetConversationModelEvaluation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "GetConversationModelEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._GetConversationModelEvaluation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = conversation_model.ConversationModelEvaluation()
            pb_resp = conversation_model.ConversationModelEvaluation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_conversation_model_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_conversation_model_evaluation_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        conversation_model.ConversationModelEvaluation.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.get_conversation_model_evaluation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "GetConversationModelEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConversationModelEvaluations(
        _BaseConversationModelsRestTransport._BaseListConversationModelEvaluations,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash(
                "ConversationModelsRestTransport.ListConversationModelEvaluations"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: conversation_model.ListConversationModelEvaluationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation_model.ListConversationModelEvaluationsResponse:
            r"""Call the list conversation model
            evaluations method over HTTP.

                Args:
                    request (~.conversation_model.ListConversationModelEvaluationsRequest):
                        The request object. The request message for
                    [ConversationModels.ListConversationModelEvaluations][google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.conversation_model.ListConversationModelEvaluationsResponse:
                        The response message for
                    [ConversationModels.ListConversationModelEvaluations][google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations]

            """

            http_options = _BaseConversationModelsRestTransport._BaseListConversationModelEvaluations._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_conversation_model_evaluations(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseListConversationModelEvaluations,
                    "_BaseListConversationModelEvaluations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.ListConversationModelEvaluations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "ListConversationModelEvaluations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._ListConversationModelEvaluations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = conversation_model.ListConversationModelEvaluationsResponse()
            pb_resp = conversation_model.ListConversationModelEvaluationsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_conversation_model_evaluations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_conversation_model_evaluations_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation_model.ListConversationModelEvaluationsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.list_conversation_model_evaluations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "ListConversationModelEvaluations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConversationModels(
        _BaseConversationModelsRestTransport._BaseListConversationModels,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.ListConversationModels")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: conversation_model.ListConversationModelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation_model.ListConversationModelsResponse:
            r"""Call the list conversation models method over HTTP.

            Args:
                request (~.conversation_model.ListConversationModelsRequest):
                    The request object. The request message for
                [ConversationModels.ListConversationModels][google.cloud.dialogflow.v2.ConversationModels.ListConversationModels]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation_model.ListConversationModelsResponse:
                    The response message for
                [ConversationModels.ListConversationModels][google.cloud.dialogflow.v2.ConversationModels.ListConversationModels]

            """

            http_options = _BaseConversationModelsRestTransport._BaseListConversationModels._get_http_options()
            request, metadata = self._interceptor.pre_list_conversation_models(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseListConversationModels,
                    "_BaseListConversationModels__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.ListConversationModels",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "ListConversationModels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationModelsRestTransport._ListConversationModels._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = conversation_model.ListConversationModelsResponse()
            pb_resp = conversation_model.ListConversationModelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_conversation_models(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_conversation_models_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        conversation_model.ListConversationModelsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.list_conversation_models",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "ListConversationModels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeployConversationModel(
        _BaseConversationModelsRestTransport._BaseUndeployConversationModel,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.UndeployConversationModel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: conversation_model.UndeployConversationModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the undeploy conversation
            model method over HTTP.

                Args:
                    request (~.conversation_model.UndeployConversationModelRequest):
                        The request object. The request message for
                    [ConversationModels.UndeployConversationModel][google.cloud.dialogflow.v2.ConversationModels.UndeployConversationModel]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = _BaseConversationModelsRestTransport._BaseUndeployConversationModel._get_http_options()
            request, metadata = self._interceptor.pre_undeploy_conversation_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseUndeployConversationModel,
                    "_BaseUndeployConversationModel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.UndeployConversationModel",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "UndeployConversationModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._UndeployConversationModel._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_undeploy_conversation_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undeploy_conversation_model_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsClient.undeploy_conversation_model",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "UndeployConversationModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_conversation_model(
        self,
    ) -> Callable[
        [gcd_conversation_model.CreateConversationModelRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConversationModel(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_conversation_model_evaluation(
        self,
    ) -> Callable[
        [conversation_model.CreateConversationModelEvaluationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConversationModelEvaluation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_conversation_model(
        self,
    ) -> Callable[
        [conversation_model.DeleteConversationModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConversationModel(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def deploy_conversation_model(
        self,
    ) -> Callable[
        [conversation_model.DeployConversationModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeployConversationModel(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_conversation_model(
        self,
    ) -> Callable[
        [conversation_model.GetConversationModelRequest],
        conversation_model.ConversationModel,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConversationModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_conversation_model_evaluation(
        self,
    ) -> Callable[
        [conversation_model.GetConversationModelEvaluationRequest],
        conversation_model.ConversationModelEvaluation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConversationModelEvaluation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_conversation_model_evaluations(
        self,
    ) -> Callable[
        [conversation_model.ListConversationModelEvaluationsRequest],
        conversation_model.ListConversationModelEvaluationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConversationModelEvaluations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_conversation_models(
        self,
    ) -> Callable[
        [conversation_model.ListConversationModelsRequest],
        conversation_model.ListConversationModelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConversationModels(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def undeploy_conversation_model(
        self,
    ) -> Callable[
        [conversation_model.UndeployConversationModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeployConversationModel(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseConversationModelsRestTransport._BaseGetLocation,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseConversationModelsRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseConversationModelsRestTransport._BaseListLocations,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseConversationModelsRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseConversationModelsRestTransport._BaseCancelOperation,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseConversationModelsRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseConversationModelsRestTransport._BaseGetOperation,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = _BaseConversationModelsRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseConversationModelsRestTransport._BaseListOperations,
        ConversationModelsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationModelsRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseConversationModelsRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationModelsRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dialogflow_v2.ConversationModelsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationModelsRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2.ConversationModelsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2.ConversationModels",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("ConversationModelsRestTransport",)
