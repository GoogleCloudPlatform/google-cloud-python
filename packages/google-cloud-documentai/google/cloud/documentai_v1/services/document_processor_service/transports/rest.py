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

from google.cloud.documentai_v1._compat import transcode_request
from google.cloud.documentai_v1.types import (
    document_processor_service,
    evaluation,
    processor,
    processor_type,
)
from google.cloud.documentai_v1.types import processor as gcd_processor

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDocumentProcessorServiceRestTransport

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


class DocumentProcessorServiceRestInterceptor:
    """Interceptor for DocumentProcessorService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DocumentProcessorServiceRestTransport.

    .. code-block:: python
        class MyCustomDocumentProcessorServiceInterceptor(DocumentProcessorServiceRestInterceptor):
            def pre_batch_process_documents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_process_documents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_processor_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_processor_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deploy_processor_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deploy_processor_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_disable_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_evaluate_processor_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_evaluate_processor_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_processor_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_processor_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_processor_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_processor_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_processor_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_processor_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_evaluations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_evaluations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_processors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_processors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_processor_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_processor_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_processor_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_processor_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_process_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_process_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_review_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_review_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_default_processor_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_default_processor_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_train_processor_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_train_processor_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undeploy_processor_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undeploy_processor_version(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DocumentProcessorServiceRestTransport(interceptor=MyCustomDocumentProcessorServiceInterceptor())
        client = DocumentProcessorServiceClient(transport=transport)


    """

    def pre_batch_process_documents(
        self,
        request: document_processor_service.BatchProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.BatchProcessRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_process_documents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_batch_process_documents(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_process_documents

        DEPRECATED. Please use the `post_batch_process_documents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_batch_process_documents` interceptor runs
        before the `post_batch_process_documents_with_metadata` interceptor.
        """
        return response

    def post_batch_process_documents_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_process_documents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_batch_process_documents_with_metadata`
        interceptor in new development instead of the `post_batch_process_documents` interceptor.
        When both interceptors are used, this `post_batch_process_documents_with_metadata` interceptor runs after the
        `post_batch_process_documents` interceptor. The (possibly modified) response returned by
        `post_batch_process_documents` will be passed to
        `post_batch_process_documents_with_metadata`.
        """
        return response, metadata

    def pre_create_processor(
        self,
        request: document_processor_service.CreateProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.CreateProcessorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_create_processor(
        self, response: gcd_processor.Processor
    ) -> gcd_processor.Processor:
        """Post-rpc interceptor for create_processor

        DEPRECATED. Please use the `post_create_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_create_processor` interceptor runs
        before the `post_create_processor_with_metadata` interceptor.
        """
        return response

    def post_create_processor_with_metadata(
        self,
        response: gcd_processor.Processor,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcd_processor.Processor, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_processor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_create_processor_with_metadata`
        interceptor in new development instead of the `post_create_processor` interceptor.
        When both interceptors are used, this `post_create_processor_with_metadata` interceptor runs after the
        `post_create_processor` interceptor. The (possibly modified) response returned by
        `post_create_processor` will be passed to
        `post_create_processor_with_metadata`.
        """
        return response, metadata

    def pre_delete_processor(
        self,
        request: document_processor_service.DeleteProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.DeleteProcessorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_delete_processor(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_processor

        DEPRECATED. Please use the `post_delete_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_delete_processor` interceptor runs
        before the `post_delete_processor_with_metadata` interceptor.
        """
        return response

    def post_delete_processor_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_processor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_delete_processor_with_metadata`
        interceptor in new development instead of the `post_delete_processor` interceptor.
        When both interceptors are used, this `post_delete_processor_with_metadata` interceptor runs after the
        `post_delete_processor` interceptor. The (possibly modified) response returned by
        `post_delete_processor` will be passed to
        `post_delete_processor_with_metadata`.
        """
        return response, metadata

    def pre_delete_processor_version(
        self,
        request: document_processor_service.DeleteProcessorVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.DeleteProcessorVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_processor_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_delete_processor_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_processor_version

        DEPRECATED. Please use the `post_delete_processor_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_delete_processor_version` interceptor runs
        before the `post_delete_processor_version_with_metadata` interceptor.
        """
        return response

    def post_delete_processor_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_processor_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_delete_processor_version_with_metadata`
        interceptor in new development instead of the `post_delete_processor_version` interceptor.
        When both interceptors are used, this `post_delete_processor_version_with_metadata` interceptor runs after the
        `post_delete_processor_version` interceptor. The (possibly modified) response returned by
        `post_delete_processor_version` will be passed to
        `post_delete_processor_version_with_metadata`.
        """
        return response, metadata

    def pre_deploy_processor_version(
        self,
        request: document_processor_service.DeployProcessorVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.DeployProcessorVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for deploy_processor_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_deploy_processor_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for deploy_processor_version

        DEPRECATED. Please use the `post_deploy_processor_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_deploy_processor_version` interceptor runs
        before the `post_deploy_processor_version_with_metadata` interceptor.
        """
        return response

    def post_deploy_processor_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deploy_processor_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_deploy_processor_version_with_metadata`
        interceptor in new development instead of the `post_deploy_processor_version` interceptor.
        When both interceptors are used, this `post_deploy_processor_version_with_metadata` interceptor runs after the
        `post_deploy_processor_version` interceptor. The (possibly modified) response returned by
        `post_deploy_processor_version` will be passed to
        `post_deploy_processor_version_with_metadata`.
        """
        return response, metadata

    def pre_disable_processor(
        self,
        request: document_processor_service.DisableProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.DisableProcessorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for disable_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_disable_processor(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for disable_processor

        DEPRECATED. Please use the `post_disable_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_disable_processor` interceptor runs
        before the `post_disable_processor_with_metadata` interceptor.
        """
        return response

    def post_disable_processor_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for disable_processor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_disable_processor_with_metadata`
        interceptor in new development instead of the `post_disable_processor` interceptor.
        When both interceptors are used, this `post_disable_processor_with_metadata` interceptor runs after the
        `post_disable_processor` interceptor. The (possibly modified) response returned by
        `post_disable_processor` will be passed to
        `post_disable_processor_with_metadata`.
        """
        return response, metadata

    def pre_enable_processor(
        self,
        request: document_processor_service.EnableProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.EnableProcessorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for enable_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_enable_processor(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for enable_processor

        DEPRECATED. Please use the `post_enable_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_enable_processor` interceptor runs
        before the `post_enable_processor_with_metadata` interceptor.
        """
        return response

    def post_enable_processor_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enable_processor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_enable_processor_with_metadata`
        interceptor in new development instead of the `post_enable_processor` interceptor.
        When both interceptors are used, this `post_enable_processor_with_metadata` interceptor runs after the
        `post_enable_processor` interceptor. The (possibly modified) response returned by
        `post_enable_processor` will be passed to
        `post_enable_processor_with_metadata`.
        """
        return response, metadata

    def pre_evaluate_processor_version(
        self,
        request: document_processor_service.EvaluateProcessorVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.EvaluateProcessorVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for evaluate_processor_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_evaluate_processor_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for evaluate_processor_version

        DEPRECATED. Please use the `post_evaluate_processor_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_evaluate_processor_version` interceptor runs
        before the `post_evaluate_processor_version_with_metadata` interceptor.
        """
        return response

    def post_evaluate_processor_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for evaluate_processor_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_evaluate_processor_version_with_metadata`
        interceptor in new development instead of the `post_evaluate_processor_version` interceptor.
        When both interceptors are used, this `post_evaluate_processor_version_with_metadata` interceptor runs after the
        `post_evaluate_processor_version` interceptor. The (possibly modified) response returned by
        `post_evaluate_processor_version` will be passed to
        `post_evaluate_processor_version_with_metadata`.
        """
        return response, metadata

    def pre_fetch_processor_types(
        self,
        request: document_processor_service.FetchProcessorTypesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.FetchProcessorTypesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_processor_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_fetch_processor_types(
        self, response: document_processor_service.FetchProcessorTypesResponse
    ) -> document_processor_service.FetchProcessorTypesResponse:
        """Post-rpc interceptor for fetch_processor_types

        DEPRECATED. Please use the `post_fetch_processor_types_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_fetch_processor_types` interceptor runs
        before the `post_fetch_processor_types_with_metadata` interceptor.
        """
        return response

    def post_fetch_processor_types_with_metadata(
        self,
        response: document_processor_service.FetchProcessorTypesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.FetchProcessorTypesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_processor_types

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_fetch_processor_types_with_metadata`
        interceptor in new development instead of the `post_fetch_processor_types` interceptor.
        When both interceptors are used, this `post_fetch_processor_types_with_metadata` interceptor runs after the
        `post_fetch_processor_types` interceptor. The (possibly modified) response returned by
        `post_fetch_processor_types` will be passed to
        `post_fetch_processor_types_with_metadata`.
        """
        return response, metadata

    def pre_get_evaluation(
        self,
        request: document_processor_service.GetEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.GetEvaluationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_get_evaluation(
        self, response: evaluation.Evaluation
    ) -> evaluation.Evaluation:
        """Post-rpc interceptor for get_evaluation

        DEPRECATED. Please use the `post_get_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_get_evaluation` interceptor runs
        before the `post_get_evaluation_with_metadata` interceptor.
        """
        return response

    def post_get_evaluation_with_metadata(
        self,
        response: evaluation.Evaluation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[evaluation.Evaluation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_get_evaluation_with_metadata`
        interceptor in new development instead of the `post_get_evaluation` interceptor.
        When both interceptors are used, this `post_get_evaluation_with_metadata` interceptor runs after the
        `post_get_evaluation` interceptor. The (possibly modified) response returned by
        `post_get_evaluation` will be passed to
        `post_get_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_get_processor(
        self,
        request: document_processor_service.GetProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.GetProcessorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_get_processor(self, response: processor.Processor) -> processor.Processor:
        """Post-rpc interceptor for get_processor

        DEPRECATED. Please use the `post_get_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_get_processor` interceptor runs
        before the `post_get_processor_with_metadata` interceptor.
        """
        return response

    def post_get_processor_with_metadata(
        self,
        response: processor.Processor,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[processor.Processor, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_processor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_get_processor_with_metadata`
        interceptor in new development instead of the `post_get_processor` interceptor.
        When both interceptors are used, this `post_get_processor_with_metadata` interceptor runs after the
        `post_get_processor` interceptor. The (possibly modified) response returned by
        `post_get_processor` will be passed to
        `post_get_processor_with_metadata`.
        """
        return response, metadata

    def pre_get_processor_type(
        self,
        request: document_processor_service.GetProcessorTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.GetProcessorTypeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_processor_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_get_processor_type(
        self, response: processor_type.ProcessorType
    ) -> processor_type.ProcessorType:
        """Post-rpc interceptor for get_processor_type

        DEPRECATED. Please use the `post_get_processor_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_get_processor_type` interceptor runs
        before the `post_get_processor_type_with_metadata` interceptor.
        """
        return response

    def post_get_processor_type_with_metadata(
        self,
        response: processor_type.ProcessorType,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[processor_type.ProcessorType, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_processor_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_get_processor_type_with_metadata`
        interceptor in new development instead of the `post_get_processor_type` interceptor.
        When both interceptors are used, this `post_get_processor_type_with_metadata` interceptor runs after the
        `post_get_processor_type` interceptor. The (possibly modified) response returned by
        `post_get_processor_type` will be passed to
        `post_get_processor_type_with_metadata`.
        """
        return response, metadata

    def pre_get_processor_version(
        self,
        request: document_processor_service.GetProcessorVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.GetProcessorVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_processor_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_get_processor_version(
        self, response: processor.ProcessorVersion
    ) -> processor.ProcessorVersion:
        """Post-rpc interceptor for get_processor_version

        DEPRECATED. Please use the `post_get_processor_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_get_processor_version` interceptor runs
        before the `post_get_processor_version_with_metadata` interceptor.
        """
        return response

    def post_get_processor_version_with_metadata(
        self,
        response: processor.ProcessorVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[processor.ProcessorVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_processor_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_get_processor_version_with_metadata`
        interceptor in new development instead of the `post_get_processor_version` interceptor.
        When both interceptors are used, this `post_get_processor_version_with_metadata` interceptor runs after the
        `post_get_processor_version` interceptor. The (possibly modified) response returned by
        `post_get_processor_version` will be passed to
        `post_get_processor_version_with_metadata`.
        """
        return response, metadata

    def pre_list_evaluations(
        self,
        request: document_processor_service.ListEvaluationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ListEvaluationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_evaluations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_list_evaluations(
        self, response: document_processor_service.ListEvaluationsResponse
    ) -> document_processor_service.ListEvaluationsResponse:
        """Post-rpc interceptor for list_evaluations

        DEPRECATED. Please use the `post_list_evaluations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_list_evaluations` interceptor runs
        before the `post_list_evaluations_with_metadata` interceptor.
        """
        return response

    def post_list_evaluations_with_metadata(
        self,
        response: document_processor_service.ListEvaluationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ListEvaluationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_evaluations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_list_evaluations_with_metadata`
        interceptor in new development instead of the `post_list_evaluations` interceptor.
        When both interceptors are used, this `post_list_evaluations_with_metadata` interceptor runs after the
        `post_list_evaluations` interceptor. The (possibly modified) response returned by
        `post_list_evaluations` will be passed to
        `post_list_evaluations_with_metadata`.
        """
        return response, metadata

    def pre_list_processors(
        self,
        request: document_processor_service.ListProcessorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ListProcessorsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_processors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_list_processors(
        self, response: document_processor_service.ListProcessorsResponse
    ) -> document_processor_service.ListProcessorsResponse:
        """Post-rpc interceptor for list_processors

        DEPRECATED. Please use the `post_list_processors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_list_processors` interceptor runs
        before the `post_list_processors_with_metadata` interceptor.
        """
        return response

    def post_list_processors_with_metadata(
        self,
        response: document_processor_service.ListProcessorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ListProcessorsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_processors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_list_processors_with_metadata`
        interceptor in new development instead of the `post_list_processors` interceptor.
        When both interceptors are used, this `post_list_processors_with_metadata` interceptor runs after the
        `post_list_processors` interceptor. The (possibly modified) response returned by
        `post_list_processors` will be passed to
        `post_list_processors_with_metadata`.
        """
        return response, metadata

    def pre_list_processor_types(
        self,
        request: document_processor_service.ListProcessorTypesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ListProcessorTypesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_processor_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_list_processor_types(
        self, response: document_processor_service.ListProcessorTypesResponse
    ) -> document_processor_service.ListProcessorTypesResponse:
        """Post-rpc interceptor for list_processor_types

        DEPRECATED. Please use the `post_list_processor_types_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_list_processor_types` interceptor runs
        before the `post_list_processor_types_with_metadata` interceptor.
        """
        return response

    def post_list_processor_types_with_metadata(
        self,
        response: document_processor_service.ListProcessorTypesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ListProcessorTypesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_processor_types

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_list_processor_types_with_metadata`
        interceptor in new development instead of the `post_list_processor_types` interceptor.
        When both interceptors are used, this `post_list_processor_types_with_metadata` interceptor runs after the
        `post_list_processor_types` interceptor. The (possibly modified) response returned by
        `post_list_processor_types` will be passed to
        `post_list_processor_types_with_metadata`.
        """
        return response, metadata

    def pre_list_processor_versions(
        self,
        request: document_processor_service.ListProcessorVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ListProcessorVersionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_processor_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_list_processor_versions(
        self, response: document_processor_service.ListProcessorVersionsResponse
    ) -> document_processor_service.ListProcessorVersionsResponse:
        """Post-rpc interceptor for list_processor_versions

        DEPRECATED. Please use the `post_list_processor_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_list_processor_versions` interceptor runs
        before the `post_list_processor_versions_with_metadata` interceptor.
        """
        return response

    def post_list_processor_versions_with_metadata(
        self,
        response: document_processor_service.ListProcessorVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ListProcessorVersionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_processor_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_list_processor_versions_with_metadata`
        interceptor in new development instead of the `post_list_processor_versions` interceptor.
        When both interceptors are used, this `post_list_processor_versions_with_metadata` interceptor runs after the
        `post_list_processor_versions` interceptor. The (possibly modified) response returned by
        `post_list_processor_versions` will be passed to
        `post_list_processor_versions_with_metadata`.
        """
        return response, metadata

    def pre_process_document(
        self,
        request: document_processor_service.ProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ProcessRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for process_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_process_document(
        self, response: document_processor_service.ProcessResponse
    ) -> document_processor_service.ProcessResponse:
        """Post-rpc interceptor for process_document

        DEPRECATED. Please use the `post_process_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_process_document` interceptor runs
        before the `post_process_document_with_metadata` interceptor.
        """
        return response

    def post_process_document_with_metadata(
        self,
        response: document_processor_service.ProcessResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ProcessResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for process_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_process_document_with_metadata`
        interceptor in new development instead of the `post_process_document` interceptor.
        When both interceptors are used, this `post_process_document_with_metadata` interceptor runs after the
        `post_process_document` interceptor. The (possibly modified) response returned by
        `post_process_document` will be passed to
        `post_process_document_with_metadata`.
        """
        return response, metadata

    def pre_review_document(
        self,
        request: document_processor_service.ReviewDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.ReviewDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for review_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_review_document(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for review_document

        DEPRECATED. Please use the `post_review_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_review_document` interceptor runs
        before the `post_review_document_with_metadata` interceptor.
        """
        return response

    def post_review_document_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for review_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_review_document_with_metadata`
        interceptor in new development instead of the `post_review_document` interceptor.
        When both interceptors are used, this `post_review_document_with_metadata` interceptor runs after the
        `post_review_document` interceptor. The (possibly modified) response returned by
        `post_review_document` will be passed to
        `post_review_document_with_metadata`.
        """
        return response, metadata

    def pre_set_default_processor_version(
        self,
        request: document_processor_service.SetDefaultProcessorVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.SetDefaultProcessorVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_default_processor_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_set_default_processor_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for set_default_processor_version

        DEPRECATED. Please use the `post_set_default_processor_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_set_default_processor_version` interceptor runs
        before the `post_set_default_processor_version_with_metadata` interceptor.
        """
        return response

    def post_set_default_processor_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_default_processor_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_set_default_processor_version_with_metadata`
        interceptor in new development instead of the `post_set_default_processor_version` interceptor.
        When both interceptors are used, this `post_set_default_processor_version_with_metadata` interceptor runs after the
        `post_set_default_processor_version` interceptor. The (possibly modified) response returned by
        `post_set_default_processor_version` will be passed to
        `post_set_default_processor_version_with_metadata`.
        """
        return response, metadata

    def pre_train_processor_version(
        self,
        request: document_processor_service.TrainProcessorVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.TrainProcessorVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for train_processor_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_train_processor_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for train_processor_version

        DEPRECATED. Please use the `post_train_processor_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_train_processor_version` interceptor runs
        before the `post_train_processor_version_with_metadata` interceptor.
        """
        return response

    def post_train_processor_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for train_processor_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_train_processor_version_with_metadata`
        interceptor in new development instead of the `post_train_processor_version` interceptor.
        When both interceptors are used, this `post_train_processor_version_with_metadata` interceptor runs after the
        `post_train_processor_version` interceptor. The (possibly modified) response returned by
        `post_train_processor_version` will be passed to
        `post_train_processor_version_with_metadata`.
        """
        return response, metadata

    def pre_undeploy_processor_version(
        self,
        request: document_processor_service.UndeployProcessorVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_processor_service.UndeployProcessorVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for undeploy_processor_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_undeploy_processor_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for undeploy_processor_version

        DEPRECATED. Please use the `post_undeploy_processor_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code. This `post_undeploy_processor_version` interceptor runs
        before the `post_undeploy_processor_version_with_metadata` interceptor.
        """
        return response

    def post_undeploy_processor_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for undeploy_processor_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentProcessorService server but before it is returned to user code.

        We recommend only using this `post_undeploy_processor_version_with_metadata`
        interceptor in new development instead of the `post_undeploy_processor_version` interceptor.
        When both interceptors are used, this `post_undeploy_processor_version_with_metadata` interceptor runs after the
        `post_undeploy_processor_version` interceptor. The (possibly modified) response returned by
        `post_undeploy_processor_version` will be passed to
        `post_undeploy_processor_version_with_metadata`.
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
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the DocumentProcessorService server but before
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
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the DocumentProcessorService server but before
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
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DocumentProcessorService server but before
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
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DocumentProcessorService server but before
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
        before they are sent to the DocumentProcessorService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DocumentProcessorService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DocumentProcessorServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DocumentProcessorServiceRestInterceptor


class DocumentProcessorServiceRestTransport(_BaseDocumentProcessorServiceRestTransport):
    """REST backend synchronous transport for DocumentProcessorService.

    Service to call Document AI to process documents according to
    the processor's definition. Processors are built using
    state-of-the-art Google AI such as natural language, computer
    vision, and translation to extract structured information from
    unstructured or semi-structured documents.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "documentai.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DocumentProcessorServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'documentai.googleapis.com').
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
            interceptor (Optional[DocumentProcessorServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DocumentProcessorServiceRestInterceptor()
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
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/uiv1beta3/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/uiv1beta3/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations}",
                    },
                    {
                        "method": "get",
                        "uri": "/uiv1beta3/{name=projects/*/locations/*/operations}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchProcessDocuments(
        _BaseDocumentProcessorServiceRestTransport._BaseBatchProcessDocuments,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.BatchProcessDocuments")

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
            request: document_processor_service.BatchProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch process documents method over HTTP.

            Args:
                request (~.document_processor_service.BatchProcessRequest):
                    The request object. Request message for
                [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments].
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseBatchProcessDocuments._get_http_options()
            request, metadata = self._interceptor.pre_batch_process_documents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseBatchProcessDocuments,
                    "_BaseBatchProcessDocuments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.BatchProcessDocuments",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "BatchProcessDocuments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._BatchProcessDocuments._get_response(
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

            resp = self._interceptor.post_batch_process_documents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_process_documents_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.batch_process_documents",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "BatchProcessDocuments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProcessor(
        _BaseDocumentProcessorServiceRestTransport._BaseCreateProcessor,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.CreateProcessor")

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
            request: document_processor_service.CreateProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_processor.Processor:
            r"""Call the create processor method over HTTP.

            Args:
                request (~.document_processor_service.CreateProcessorRequest):
                    The request object. Request message for the
                [CreateProcessor][google.cloud.documentai.v1.DocumentProcessorService.CreateProcessor]
                method. Notice this request is sent to a regionalized
                backend service. If the
                [ProcessorType][google.cloud.documentai.v1.ProcessorType]
                isn't available in that region, the creation fails.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_processor.Processor:
                    The first-class citizen for Document
                AI. Each processor defines how to
                extract structural information from a
                document.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseCreateProcessor._get_http_options()
            request, metadata = self._interceptor.pre_create_processor(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseCreateProcessor,
                    "_BaseCreateProcessor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.CreateProcessor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "CreateProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._CreateProcessor._get_response(
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
            resp = gcd_processor.Processor()
            pb_resp = gcd_processor.Processor.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_processor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_processor_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_processor.Processor.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.create_processor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "CreateProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteProcessor(
        _BaseDocumentProcessorServiceRestTransport._BaseDeleteProcessor,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.DeleteProcessor")

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
            request: document_processor_service.DeleteProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete processor method over HTTP.

            Args:
                request (~.document_processor_service.DeleteProcessorRequest):
                    The request object. Request message for the
                [DeleteProcessor][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessor]
                method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseDeleteProcessor._get_http_options()
            request, metadata = self._interceptor.pre_delete_processor(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseDeleteProcessor,
                    "_BaseDeleteProcessor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.DeleteProcessor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "DeleteProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._DeleteProcessor._get_response(
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

            resp = self._interceptor.post_delete_processor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_processor_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.delete_processor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "DeleteProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteProcessorVersion(
        _BaseDocumentProcessorServiceRestTransport._BaseDeleteProcessorVersion,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.DeleteProcessorVersion")

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
            request: document_processor_service.DeleteProcessorVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete processor version method over HTTP.

            Args:
                request (~.document_processor_service.DeleteProcessorVersionRequest):
                    The request object. Request message for the
                [DeleteProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersion]
                method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseDeleteProcessorVersion._get_http_options()
            request, metadata = self._interceptor.pre_delete_processor_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseDeleteProcessorVersion,
                    "_BaseDeleteProcessorVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.DeleteProcessorVersion",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "DeleteProcessorVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._DeleteProcessorVersion._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_processor_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_processor_version_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.delete_processor_version",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "DeleteProcessorVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeployProcessorVersion(
        _BaseDocumentProcessorServiceRestTransport._BaseDeployProcessorVersion,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.DeployProcessorVersion")

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
            request: document_processor_service.DeployProcessorVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the deploy processor version method over HTTP.

            Args:
                request (~.document_processor_service.DeployProcessorVersionRequest):
                    The request object. Request message for the
                [DeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion]
                method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseDeployProcessorVersion._get_http_options()
            request, metadata = self._interceptor.pre_deploy_processor_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseDeployProcessorVersion,
                    "_BaseDeployProcessorVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.DeployProcessorVersion",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "DeployProcessorVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._DeployProcessorVersion._get_response(
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

            resp = self._interceptor.post_deploy_processor_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deploy_processor_version_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.deploy_processor_version",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "DeployProcessorVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DisableProcessor(
        _BaseDocumentProcessorServiceRestTransport._BaseDisableProcessor,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.DisableProcessor")

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
            request: document_processor_service.DisableProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the disable processor method over HTTP.

            Args:
                request (~.document_processor_service.DisableProcessorRequest):
                    The request object. Request message for the
                [DisableProcessor][google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor]
                method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseDisableProcessor._get_http_options()
            request, metadata = self._interceptor.pre_disable_processor(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseDisableProcessor,
                    "_BaseDisableProcessor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.DisableProcessor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "DisableProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._DisableProcessor._get_response(
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

            resp = self._interceptor.post_disable_processor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_disable_processor_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.disable_processor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "DisableProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnableProcessor(
        _BaseDocumentProcessorServiceRestTransport._BaseEnableProcessor,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.EnableProcessor")

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
            request: document_processor_service.EnableProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the enable processor method over HTTP.

            Args:
                request (~.document_processor_service.EnableProcessorRequest):
                    The request object. Request message for the
                [EnableProcessor][google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor]
                method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseEnableProcessor._get_http_options()
            request, metadata = self._interceptor.pre_enable_processor(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseEnableProcessor,
                    "_BaseEnableProcessor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.EnableProcessor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "EnableProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._EnableProcessor._get_response(
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

            resp = self._interceptor.post_enable_processor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enable_processor_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.enable_processor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "EnableProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EvaluateProcessorVersion(
        _BaseDocumentProcessorServiceRestTransport._BaseEvaluateProcessorVersion,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DocumentProcessorServiceRestTransport.EvaluateProcessorVersion"
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
            request: document_processor_service.EvaluateProcessorVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the evaluate processor
            version method over HTTP.

                Args:
                    request (~.document_processor_service.EvaluateProcessorVersionRequest):
                        The request object. Evaluates the given
                    [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion]
                    against the supplied documents.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseEvaluateProcessorVersion._get_http_options()
            request, metadata = self._interceptor.pre_evaluate_processor_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseEvaluateProcessorVersion,
                    "_BaseEvaluateProcessorVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.EvaluateProcessorVersion",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "EvaluateProcessorVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._EvaluateProcessorVersion._get_response(
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

            resp = self._interceptor.post_evaluate_processor_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_evaluate_processor_version_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.evaluate_processor_version",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "EvaluateProcessorVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchProcessorTypes(
        _BaseDocumentProcessorServiceRestTransport._BaseFetchProcessorTypes,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.FetchProcessorTypes")

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
            request: document_processor_service.FetchProcessorTypesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_processor_service.FetchProcessorTypesResponse:
            r"""Call the fetch processor types method over HTTP.

            Args:
                request (~.document_processor_service.FetchProcessorTypesRequest):
                    The request object. Request message for the
                [FetchProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes]
                method. Some processor types may require the project be
                added to an allowlist.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_processor_service.FetchProcessorTypesResponse:
                    Response message for the
                [FetchProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes]
                method.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseFetchProcessorTypes._get_http_options()
            request, metadata = self._interceptor.pre_fetch_processor_types(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseFetchProcessorTypes,
                    "_BaseFetchProcessorTypes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.FetchProcessorTypes",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "FetchProcessorTypes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._FetchProcessorTypes._get_response(
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
            resp = document_processor_service.FetchProcessorTypesResponse()
            pb_resp = document_processor_service.FetchProcessorTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_processor_types(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_processor_types_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        document_processor_service.FetchProcessorTypesResponse.to_json(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.fetch_processor_types",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "FetchProcessorTypes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEvaluation(
        _BaseDocumentProcessorServiceRestTransport._BaseGetEvaluation,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.GetEvaluation")

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
            request: document_processor_service.GetEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> evaluation.Evaluation:
            r"""Call the get evaluation method over HTTP.

            Args:
                request (~.document_processor_service.GetEvaluationRequest):
                    The request object. Retrieves a specific Evaluation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.evaluation.Evaluation:
                    An evaluation of a ProcessorVersion's
                performance.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseGetEvaluation._get_http_options()
            request, metadata = self._interceptor.pre_get_evaluation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseGetEvaluation,
                    "_BaseGetEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.GetEvaluation",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._GetEvaluation._get_response(
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
            resp = evaluation.Evaluation()
            pb_resp = evaluation.Evaluation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_evaluation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = evaluation.Evaluation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.get_evaluation",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProcessor(
        _BaseDocumentProcessorServiceRestTransport._BaseGetProcessor,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.GetProcessor")

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
            request: document_processor_service.GetProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> processor.Processor:
            r"""Call the get processor method over HTTP.

            Args:
                request (~.document_processor_service.GetProcessorRequest):
                    The request object. Request message for the
                [GetProcessor][google.cloud.documentai.v1.DocumentProcessorService.GetProcessor]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.processor.Processor:
                    The first-class citizen for Document
                AI. Each processor defines how to
                extract structural information from a
                document.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseGetProcessor._get_http_options()
            request, metadata = self._interceptor.pre_get_processor(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseGetProcessor,
                    "_BaseGetProcessor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.GetProcessor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._GetProcessor._get_response(
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
            resp = processor.Processor()
            pb_resp = processor.Processor.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_processor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_processor_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = processor.Processor.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.get_processor",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProcessorType(
        _BaseDocumentProcessorServiceRestTransport._BaseGetProcessorType,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.GetProcessorType")

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
            request: document_processor_service.GetProcessorTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> processor_type.ProcessorType:
            r"""Call the get processor type method over HTTP.

            Args:
                request (~.document_processor_service.GetProcessorTypeRequest):
                    The request object. Request message for the
                [GetProcessorType][google.cloud.documentai.v1.DocumentProcessorService.GetProcessorType]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.processor_type.ProcessorType:
                    A processor type is responsible for
                performing a certain document
                understanding task on a certain type of
                document.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseGetProcessorType._get_http_options()
            request, metadata = self._interceptor.pre_get_processor_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseGetProcessorType,
                    "_BaseGetProcessorType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.GetProcessorType",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetProcessorType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._GetProcessorType._get_response(
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
            resp = processor_type.ProcessorType()
            pb_resp = processor_type.ProcessorType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_processor_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_processor_type_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = processor_type.ProcessorType.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.get_processor_type",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetProcessorType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProcessorVersion(
        _BaseDocumentProcessorServiceRestTransport._BaseGetProcessorVersion,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.GetProcessorVersion")

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
            request: document_processor_service.GetProcessorVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> processor.ProcessorVersion:
            r"""Call the get processor version method over HTTP.

            Args:
                request (~.document_processor_service.GetProcessorVersionRequest):
                    The request object. Request message for the
                [GetProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.GetProcessorVersion]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.processor.ProcessorVersion:
                    A processor version is an
                implementation of a processor. Each
                processor can have multiple versions,
                pretrained by Google internally or
                uptrained by the customer. A processor
                can only have one default version at a
                time. Its document-processing behavior
                is defined by that version.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseGetProcessorVersion._get_http_options()
            request, metadata = self._interceptor.pre_get_processor_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseGetProcessorVersion,
                    "_BaseGetProcessorVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.GetProcessorVersion",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetProcessorVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._GetProcessorVersion._get_response(
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
            resp = processor.ProcessorVersion()
            pb_resp = processor.ProcessorVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_processor_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_processor_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = processor.ProcessorVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.get_processor_version",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetProcessorVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvaluations(
        _BaseDocumentProcessorServiceRestTransport._BaseListEvaluations,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.ListEvaluations")

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
            request: document_processor_service.ListEvaluationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_processor_service.ListEvaluationsResponse:
            r"""Call the list evaluations method over HTTP.

            Args:
                request (~.document_processor_service.ListEvaluationsRequest):
                    The request object. Retrieves a list of evaluations for a given
                [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_processor_service.ListEvaluationsResponse:
                    The response from ``ListEvaluations``.
            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseListEvaluations._get_http_options()
            request, metadata = self._interceptor.pre_list_evaluations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseListEvaluations,
                    "_BaseListEvaluations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.ListEvaluations",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListEvaluations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._ListEvaluations._get_response(
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
            resp = document_processor_service.ListEvaluationsResponse()
            pb_resp = document_processor_service.ListEvaluationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_evaluations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_evaluations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        document_processor_service.ListEvaluationsResponse.to_json(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.list_evaluations",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListEvaluations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProcessors(
        _BaseDocumentProcessorServiceRestTransport._BaseListProcessors,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.ListProcessors")

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
            request: document_processor_service.ListProcessorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_processor_service.ListProcessorsResponse:
            r"""Call the list processors method over HTTP.

            Args:
                request (~.document_processor_service.ListProcessorsRequest):
                    The request object. Request message for list all
                processors belongs to a project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_processor_service.ListProcessorsResponse:
                    Response message for the
                [ListProcessors][google.cloud.documentai.v1.DocumentProcessorService.ListProcessors]
                method.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseListProcessors._get_http_options()
            request, metadata = self._interceptor.pre_list_processors(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseListProcessors,
                    "_BaseListProcessors__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.ListProcessors",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListProcessors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._ListProcessors._get_response(
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
            resp = document_processor_service.ListProcessorsResponse()
            pb_resp = document_processor_service.ListProcessorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_processors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_processors_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        document_processor_service.ListProcessorsResponse.to_json(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.list_processors",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListProcessors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProcessorTypes(
        _BaseDocumentProcessorServiceRestTransport._BaseListProcessorTypes,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.ListProcessorTypes")

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
            request: document_processor_service.ListProcessorTypesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_processor_service.ListProcessorTypesResponse:
            r"""Call the list processor types method over HTTP.

            Args:
                request (~.document_processor_service.ListProcessorTypesRequest):
                    The request object. Request message for the
                [ListProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes]
                method. Some processor types may require the project be
                added to an allowlist.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_processor_service.ListProcessorTypesResponse:
                    Response message for the
                [ListProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes]
                method.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseListProcessorTypes._get_http_options()
            request, metadata = self._interceptor.pre_list_processor_types(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseListProcessorTypes,
                    "_BaseListProcessorTypes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.ListProcessorTypes",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListProcessorTypes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._ListProcessorTypes._get_response(
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
            resp = document_processor_service.ListProcessorTypesResponse()
            pb_resp = document_processor_service.ListProcessorTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_processor_types(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_processor_types_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        document_processor_service.ListProcessorTypesResponse.to_json(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.list_processor_types",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListProcessorTypes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProcessorVersions(
        _BaseDocumentProcessorServiceRestTransport._BaseListProcessorVersions,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.ListProcessorVersions")

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
            request: document_processor_service.ListProcessorVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_processor_service.ListProcessorVersionsResponse:
            r"""Call the list processor versions method over HTTP.

            Args:
                request (~.document_processor_service.ListProcessorVersionsRequest):
                    The request object. Request message for list all
                processor versions belongs to a
                processor.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_processor_service.ListProcessorVersionsResponse:
                    Response message for the
                [ListProcessorVersions][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorVersions]
                method.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseListProcessorVersions._get_http_options()
            request, metadata = self._interceptor.pre_list_processor_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseListProcessorVersions,
                    "_BaseListProcessorVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.ListProcessorVersions",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListProcessorVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._ListProcessorVersions._get_response(
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
            resp = document_processor_service.ListProcessorVersionsResponse()
            pb_resp = document_processor_service.ListProcessorVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_processor_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_processor_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = document_processor_service.ListProcessorVersionsResponse.to_json(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.list_processor_versions",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListProcessorVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ProcessDocument(
        _BaseDocumentProcessorServiceRestTransport._BaseProcessDocument,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.ProcessDocument")

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
            request: document_processor_service.ProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_processor_service.ProcessResponse:
            r"""Call the process document method over HTTP.

            Args:
                request (~.document_processor_service.ProcessRequest):
                    The request object. Request message for the
                [ProcessDocument][google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_processor_service.ProcessResponse:
                    Response message for the
                [ProcessDocument][google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument]
                method.

            """

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseProcessDocument._get_http_options()
            request, metadata = self._interceptor.pre_process_document(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseProcessDocument,
                    "_BaseProcessDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.ProcessDocument",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ProcessDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._ProcessDocument._get_response(
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
            resp = document_processor_service.ProcessResponse()
            pb_resp = document_processor_service.ProcessResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_process_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_process_document_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        document_processor_service.ProcessResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.process_document",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ProcessDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReviewDocument(
        _BaseDocumentProcessorServiceRestTransport._BaseReviewDocument,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.ReviewDocument")

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
            request: document_processor_service.ReviewDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the review document method over HTTP.

            Args:
                request (~.document_processor_service.ReviewDocumentRequest):
                    The request object. Request message for the
                [ReviewDocument][google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument]
                method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseReviewDocument._get_http_options()
            request, metadata = self._interceptor.pre_review_document(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseReviewDocument,
                    "_BaseReviewDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.ReviewDocument",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ReviewDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._ReviewDocument._get_response(
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

            resp = self._interceptor.post_review_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_review_document_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.review_document",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ReviewDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetDefaultProcessorVersion(
        _BaseDocumentProcessorServiceRestTransport._BaseSetDefaultProcessorVersion,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DocumentProcessorServiceRestTransport.SetDefaultProcessorVersion"
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
            request: document_processor_service.SetDefaultProcessorVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the set default processor
            version method over HTTP.

                Args:
                    request (~.document_processor_service.SetDefaultProcessorVersionRequest):
                        The request object. Request message for the
                    [SetDefaultProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion]
                    method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseSetDefaultProcessorVersion._get_http_options()
            request, metadata = self._interceptor.pre_set_default_processor_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseSetDefaultProcessorVersion,
                    "_BaseSetDefaultProcessorVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.SetDefaultProcessorVersion",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "SetDefaultProcessorVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._SetDefaultProcessorVersion._get_response(
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

            resp = self._interceptor.post_set_default_processor_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_set_default_processor_version_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.set_default_processor_version",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "SetDefaultProcessorVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TrainProcessorVersion(
        _BaseDocumentProcessorServiceRestTransport._BaseTrainProcessorVersion,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.TrainProcessorVersion")

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
            request: document_processor_service.TrainProcessorVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the train processor version method over HTTP.

            Args:
                request (~.document_processor_service.TrainProcessorVersionRequest):
                    The request object. Request message for the
                [TrainProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersion]
                method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseTrainProcessorVersion._get_http_options()
            request, metadata = self._interceptor.pre_train_processor_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseTrainProcessorVersion,
                    "_BaseTrainProcessorVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.TrainProcessorVersion",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "TrainProcessorVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._TrainProcessorVersion._get_response(
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

            resp = self._interceptor.post_train_processor_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_train_processor_version_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.train_processor_version",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "TrainProcessorVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeployProcessorVersion(
        _BaseDocumentProcessorServiceRestTransport._BaseUndeployProcessorVersion,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DocumentProcessorServiceRestTransport.UndeployProcessorVersion"
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
            request: document_processor_service.UndeployProcessorVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the undeploy processor
            version method over HTTP.

                Args:
                    request (~.document_processor_service.UndeployProcessorVersionRequest):
                        The request object. Request message for the
                    [UndeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion]
                    method.
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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseUndeployProcessorVersion._get_http_options()
            request, metadata = self._interceptor.pre_undeploy_processor_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseUndeployProcessorVersion,
                    "_BaseUndeployProcessorVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.UndeployProcessorVersion",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "UndeployProcessorVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._UndeployProcessorVersion._get_response(
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

            resp = self._interceptor.post_undeploy_processor_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undeploy_processor_version_with_metadata(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceClient.undeploy_processor_version",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "UndeployProcessorVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_process_documents(
        self,
    ) -> Callable[
        [document_processor_service.BatchProcessRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchProcessDocuments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_processor(
        self,
    ) -> Callable[
        [document_processor_service.CreateProcessorRequest], gcd_processor.Processor
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_processor(
        self,
    ) -> Callable[
        [document_processor_service.DeleteProcessorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.DeleteProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProcessorVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def deploy_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.DeployProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeployProcessorVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def disable_processor(
        self,
    ) -> Callable[
        [document_processor_service.DisableProcessorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisableProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enable_processor(
        self,
    ) -> Callable[
        [document_processor_service.EnableProcessorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnableProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def evaluate_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.EvaluateProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EvaluateProcessorVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_processor_types(
        self,
    ) -> Callable[
        [document_processor_service.FetchProcessorTypesRequest],
        document_processor_service.FetchProcessorTypesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchProcessorTypes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_evaluation(
        self,
    ) -> Callable[
        [document_processor_service.GetEvaluationRequest], evaluation.Evaluation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_processor(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorRequest], processor.Processor
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_processor_type(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorTypeRequest],
        processor_type.ProcessorType,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProcessorType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorVersionRequest],
        processor.ProcessorVersion,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProcessorVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_evaluations(
        self,
    ) -> Callable[
        [document_processor_service.ListEvaluationsRequest],
        document_processor_service.ListEvaluationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvaluations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_processors(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorsRequest],
        document_processor_service.ListProcessorsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProcessors(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_processor_types(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorTypesRequest],
        document_processor_service.ListProcessorTypesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProcessorTypes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_processor_versions(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorVersionsRequest],
        document_processor_service.ListProcessorVersionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProcessorVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def process_document(
        self,
    ) -> Callable[
        [document_processor_service.ProcessRequest],
        document_processor_service.ProcessResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ProcessDocument(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def review_document(
        self,
    ) -> Callable[
        [document_processor_service.ReviewDocumentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReviewDocument(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_default_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.SetDefaultProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetDefaultProcessorVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def train_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.TrainProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TrainProcessorVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def undeploy_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.UndeployProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeployProcessorVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseDocumentProcessorServiceRestTransport._BaseGetLocation,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.GetLocation")

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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentProcessorServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
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
        _BaseDocumentProcessorServiceRestTransport._BaseListLocations,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.ListLocations")

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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
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
        _BaseDocumentProcessorServiceRestTransport._BaseCancelOperation,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.CancelOperation")

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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseDocumentProcessorServiceRestTransport._BaseGetOperation,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.GetOperation")

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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
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
        _BaseDocumentProcessorServiceRestTransport._BaseListOperations,
        DocumentProcessorServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentProcessorServiceRestTransport.ListOperations")

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

            http_options = _BaseDocumentProcessorServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentProcessorServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.documentai_v1.DocumentProcessorServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentProcessorServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.documentai_v1.DocumentProcessorServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
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


__all__ = ("DocumentProcessorServiceRestTransport",)
