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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.automl_v1beta1._compat import transcode_request
from google.cloud.automl_v1beta1.types import (
    annotation_spec,
    column_spec,
    dataset,
    model,
    model_evaluation,
    service,
    table_spec,
)
from google.cloud.automl_v1beta1.types import column_spec as gca_column_spec
from google.cloud.automl_v1beta1.types import dataset as gca_dataset
from google.cloud.automl_v1beta1.types import table_spec as gca_table_spec

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAutoMlRestTransport

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


class AutoMlRestInterceptor:
    """Interceptor for AutoMl.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AutoMlRestTransport.

    .. code-block:: python
        class MyCustomAutoMlInterceptor(AutoMlRestInterceptor):
            def pre_create_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deploy_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deploy_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_evaluated_examples(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_evaluated_examples(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_annotation_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_annotation_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_column_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_column_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_model_evaluation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_model_evaluation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_table_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_table_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_column_specs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_column_specs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_datasets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_datasets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_model_evaluations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_model_evaluations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_models(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_models(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_table_specs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_table_specs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undeploy_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undeploy_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_column_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_column_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_table_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_table_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AutoMlRestTransport(interceptor=MyCustomAutoMlInterceptor())
        client = AutoMlClient(transport=transport)


    """

    def pre_create_dataset(
        self,
        request: service.CreateDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateDatasetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_create_dataset(self, response: gca_dataset.Dataset) -> gca_dataset.Dataset:
        """Post-rpc interceptor for create_dataset

        DEPRECATED. Please use the `post_create_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_create_dataset` interceptor runs
        before the `post_create_dataset_with_metadata` interceptor.
        """
        return response

    def post_create_dataset_with_metadata(
        self,
        response: gca_dataset.Dataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gca_dataset.Dataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_create_dataset_with_metadata`
        interceptor in new development instead of the `post_create_dataset` interceptor.
        When both interceptors are used, this `post_create_dataset_with_metadata` interceptor runs after the
        `post_create_dataset` interceptor. The (possibly modified) response returned by
        `post_create_dataset` will be passed to
        `post_create_dataset_with_metadata`.
        """
        return response, metadata

    def pre_create_model(
        self,
        request: service.CreateModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateModelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_create_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_model

        DEPRECATED. Please use the `post_create_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_create_model` interceptor runs
        before the `post_create_model_with_metadata` interceptor.
        """
        return response

    def post_create_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_create_model_with_metadata`
        interceptor in new development instead of the `post_create_model` interceptor.
        When both interceptors are used, this `post_create_model_with_metadata` interceptor runs after the
        `post_create_model` interceptor. The (possibly modified) response returned by
        `post_create_model` will be passed to
        `post_create_model_with_metadata`.
        """
        return response, metadata

    def pre_delete_dataset(
        self,
        request: service.DeleteDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteDatasetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_delete_dataset(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_dataset

        DEPRECATED. Please use the `post_delete_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_delete_dataset` interceptor runs
        before the `post_delete_dataset_with_metadata` interceptor.
        """
        return response

    def post_delete_dataset_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_delete_dataset_with_metadata`
        interceptor in new development instead of the `post_delete_dataset` interceptor.
        When both interceptors are used, this `post_delete_dataset_with_metadata` interceptor runs after the
        `post_delete_dataset` interceptor. The (possibly modified) response returned by
        `post_delete_dataset` will be passed to
        `post_delete_dataset_with_metadata`.
        """
        return response, metadata

    def pre_delete_model(
        self,
        request: service.DeleteModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteModelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_delete_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_model

        DEPRECATED. Please use the `post_delete_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_delete_model` interceptor runs
        before the `post_delete_model_with_metadata` interceptor.
        """
        return response

    def post_delete_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_delete_model_with_metadata`
        interceptor in new development instead of the `post_delete_model` interceptor.
        When both interceptors are used, this `post_delete_model_with_metadata` interceptor runs after the
        `post_delete_model` interceptor. The (possibly modified) response returned by
        `post_delete_model` will be passed to
        `post_delete_model_with_metadata`.
        """
        return response, metadata

    def pre_deploy_model(
        self,
        request: service.DeployModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeployModelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for deploy_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_deploy_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for deploy_model

        DEPRECATED. Please use the `post_deploy_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_deploy_model` interceptor runs
        before the `post_deploy_model_with_metadata` interceptor.
        """
        return response

    def post_deploy_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deploy_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_deploy_model_with_metadata`
        interceptor in new development instead of the `post_deploy_model` interceptor.
        When both interceptors are used, this `post_deploy_model_with_metadata` interceptor runs after the
        `post_deploy_model` interceptor. The (possibly modified) response returned by
        `post_deploy_model` will be passed to
        `post_deploy_model_with_metadata`.
        """
        return response, metadata

    def pre_export_data(
        self,
        request: service.ExportDataRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ExportDataRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for export_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_export_data(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_data

        DEPRECATED. Please use the `post_export_data_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_export_data` interceptor runs
        before the `post_export_data_with_metadata` interceptor.
        """
        return response

    def post_export_data_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_data

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_export_data_with_metadata`
        interceptor in new development instead of the `post_export_data` interceptor.
        When both interceptors are used, this `post_export_data_with_metadata` interceptor runs after the
        `post_export_data` interceptor. The (possibly modified) response returned by
        `post_export_data` will be passed to
        `post_export_data_with_metadata`.
        """
        return response, metadata

    def pre_export_evaluated_examples(
        self,
        request: service.ExportEvaluatedExamplesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ExportEvaluatedExamplesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_evaluated_examples

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_export_evaluated_examples(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_evaluated_examples

        DEPRECATED. Please use the `post_export_evaluated_examples_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_export_evaluated_examples` interceptor runs
        before the `post_export_evaluated_examples_with_metadata` interceptor.
        """
        return response

    def post_export_evaluated_examples_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_evaluated_examples

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_export_evaluated_examples_with_metadata`
        interceptor in new development instead of the `post_export_evaluated_examples` interceptor.
        When both interceptors are used, this `post_export_evaluated_examples_with_metadata` interceptor runs after the
        `post_export_evaluated_examples` interceptor. The (possibly modified) response returned by
        `post_export_evaluated_examples` will be passed to
        `post_export_evaluated_examples_with_metadata`.
        """
        return response, metadata

    def pre_export_model(
        self,
        request: service.ExportModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ExportModelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for export_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_export_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_model

        DEPRECATED. Please use the `post_export_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_export_model` interceptor runs
        before the `post_export_model_with_metadata` interceptor.
        """
        return response

    def post_export_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_export_model_with_metadata`
        interceptor in new development instead of the `post_export_model` interceptor.
        When both interceptors are used, this `post_export_model_with_metadata` interceptor runs after the
        `post_export_model` interceptor. The (possibly modified) response returned by
        `post_export_model` will be passed to
        `post_export_model_with_metadata`.
        """
        return response, metadata

    def pre_get_annotation_spec(
        self,
        request: service.GetAnnotationSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetAnnotationSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_annotation_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_get_annotation_spec(
        self, response: annotation_spec.AnnotationSpec
    ) -> annotation_spec.AnnotationSpec:
        """Post-rpc interceptor for get_annotation_spec

        DEPRECATED. Please use the `post_get_annotation_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_get_annotation_spec` interceptor runs
        before the `post_get_annotation_spec_with_metadata` interceptor.
        """
        return response

    def post_get_annotation_spec_with_metadata(
        self,
        response: annotation_spec.AnnotationSpec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[annotation_spec.AnnotationSpec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_annotation_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_get_annotation_spec_with_metadata`
        interceptor in new development instead of the `post_get_annotation_spec` interceptor.
        When both interceptors are used, this `post_get_annotation_spec_with_metadata` interceptor runs after the
        `post_get_annotation_spec` interceptor. The (possibly modified) response returned by
        `post_get_annotation_spec` will be passed to
        `post_get_annotation_spec_with_metadata`.
        """
        return response, metadata

    def pre_get_column_spec(
        self,
        request: service.GetColumnSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetColumnSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_column_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_get_column_spec(
        self, response: column_spec.ColumnSpec
    ) -> column_spec.ColumnSpec:
        """Post-rpc interceptor for get_column_spec

        DEPRECATED. Please use the `post_get_column_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_get_column_spec` interceptor runs
        before the `post_get_column_spec_with_metadata` interceptor.
        """
        return response

    def post_get_column_spec_with_metadata(
        self,
        response: column_spec.ColumnSpec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[column_spec.ColumnSpec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_column_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_get_column_spec_with_metadata`
        interceptor in new development instead of the `post_get_column_spec` interceptor.
        When both interceptors are used, this `post_get_column_spec_with_metadata` interceptor runs after the
        `post_get_column_spec` interceptor. The (possibly modified) response returned by
        `post_get_column_spec` will be passed to
        `post_get_column_spec_with_metadata`.
        """
        return response, metadata

    def pre_get_dataset(
        self,
        request: service.GetDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetDatasetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_get_dataset(self, response: dataset.Dataset) -> dataset.Dataset:
        """Post-rpc interceptor for get_dataset

        DEPRECATED. Please use the `post_get_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_get_dataset` interceptor runs
        before the `post_get_dataset_with_metadata` interceptor.
        """
        return response

    def post_get_dataset_with_metadata(
        self,
        response: dataset.Dataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataset.Dataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_get_dataset_with_metadata`
        interceptor in new development instead of the `post_get_dataset` interceptor.
        When both interceptors are used, this `post_get_dataset_with_metadata` interceptor runs after the
        `post_get_dataset` interceptor. The (possibly modified) response returned by
        `post_get_dataset` will be passed to
        `post_get_dataset_with_metadata`.
        """
        return response, metadata

    def pre_get_model(
        self,
        request: service.GetModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetModelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_get_model(self, response: model.Model) -> model.Model:
        """Post-rpc interceptor for get_model

        DEPRECATED. Please use the `post_get_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_get_model` interceptor runs
        before the `post_get_model_with_metadata` interceptor.
        """
        return response

    def post_get_model_with_metadata(
        self, response: model.Model, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[model.Model, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_get_model_with_metadata`
        interceptor in new development instead of the `post_get_model` interceptor.
        When both interceptors are used, this `post_get_model_with_metadata` interceptor runs after the
        `post_get_model` interceptor. The (possibly modified) response returned by
        `post_get_model` will be passed to
        `post_get_model_with_metadata`.
        """
        return response, metadata

    def pre_get_model_evaluation(
        self,
        request: service.GetModelEvaluationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetModelEvaluationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_model_evaluation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_get_model_evaluation(
        self, response: model_evaluation.ModelEvaluation
    ) -> model_evaluation.ModelEvaluation:
        """Post-rpc interceptor for get_model_evaluation

        DEPRECATED. Please use the `post_get_model_evaluation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_get_model_evaluation` interceptor runs
        before the `post_get_model_evaluation_with_metadata` interceptor.
        """
        return response

    def post_get_model_evaluation_with_metadata(
        self,
        response: model_evaluation.ModelEvaluation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        model_evaluation.ModelEvaluation, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_model_evaluation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_get_model_evaluation_with_metadata`
        interceptor in new development instead of the `post_get_model_evaluation` interceptor.
        When both interceptors are used, this `post_get_model_evaluation_with_metadata` interceptor runs after the
        `post_get_model_evaluation` interceptor. The (possibly modified) response returned by
        `post_get_model_evaluation` will be passed to
        `post_get_model_evaluation_with_metadata`.
        """
        return response, metadata

    def pre_get_table_spec(
        self,
        request: service.GetTableSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetTableSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_table_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_get_table_spec(
        self, response: table_spec.TableSpec
    ) -> table_spec.TableSpec:
        """Post-rpc interceptor for get_table_spec

        DEPRECATED. Please use the `post_get_table_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_get_table_spec` interceptor runs
        before the `post_get_table_spec_with_metadata` interceptor.
        """
        return response

    def post_get_table_spec_with_metadata(
        self,
        response: table_spec.TableSpec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[table_spec.TableSpec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_table_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_get_table_spec_with_metadata`
        interceptor in new development instead of the `post_get_table_spec` interceptor.
        When both interceptors are used, this `post_get_table_spec_with_metadata` interceptor runs after the
        `post_get_table_spec` interceptor. The (possibly modified) response returned by
        `post_get_table_spec` will be passed to
        `post_get_table_spec_with_metadata`.
        """
        return response, metadata

    def pre_import_data(
        self,
        request: service.ImportDataRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ImportDataRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for import_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_import_data(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_data

        DEPRECATED. Please use the `post_import_data_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_import_data` interceptor runs
        before the `post_import_data_with_metadata` interceptor.
        """
        return response

    def post_import_data_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_data

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_import_data_with_metadata`
        interceptor in new development instead of the `post_import_data` interceptor.
        When both interceptors are used, this `post_import_data_with_metadata` interceptor runs after the
        `post_import_data` interceptor. The (possibly modified) response returned by
        `post_import_data` will be passed to
        `post_import_data_with_metadata`.
        """
        return response, metadata

    def pre_list_column_specs(
        self,
        request: service.ListColumnSpecsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListColumnSpecsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_column_specs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_list_column_specs(
        self, response: service.ListColumnSpecsResponse
    ) -> service.ListColumnSpecsResponse:
        """Post-rpc interceptor for list_column_specs

        DEPRECATED. Please use the `post_list_column_specs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_list_column_specs` interceptor runs
        before the `post_list_column_specs_with_metadata` interceptor.
        """
        return response

    def post_list_column_specs_with_metadata(
        self,
        response: service.ListColumnSpecsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListColumnSpecsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_column_specs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_list_column_specs_with_metadata`
        interceptor in new development instead of the `post_list_column_specs` interceptor.
        When both interceptors are used, this `post_list_column_specs_with_metadata` interceptor runs after the
        `post_list_column_specs` interceptor. The (possibly modified) response returned by
        `post_list_column_specs` will be passed to
        `post_list_column_specs_with_metadata`.
        """
        return response, metadata

    def pre_list_datasets(
        self,
        request: service.ListDatasetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListDatasetsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_datasets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_list_datasets(
        self, response: service.ListDatasetsResponse
    ) -> service.ListDatasetsResponse:
        """Post-rpc interceptor for list_datasets

        DEPRECATED. Please use the `post_list_datasets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_list_datasets` interceptor runs
        before the `post_list_datasets_with_metadata` interceptor.
        """
        return response

    def post_list_datasets_with_metadata(
        self,
        response: service.ListDatasetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListDatasetsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_datasets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_list_datasets_with_metadata`
        interceptor in new development instead of the `post_list_datasets` interceptor.
        When both interceptors are used, this `post_list_datasets_with_metadata` interceptor runs after the
        `post_list_datasets` interceptor. The (possibly modified) response returned by
        `post_list_datasets` will be passed to
        `post_list_datasets_with_metadata`.
        """
        return response, metadata

    def pre_list_model_evaluations(
        self,
        request: service.ListModelEvaluationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListModelEvaluationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_model_evaluations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_list_model_evaluations(
        self, response: service.ListModelEvaluationsResponse
    ) -> service.ListModelEvaluationsResponse:
        """Post-rpc interceptor for list_model_evaluations

        DEPRECATED. Please use the `post_list_model_evaluations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_list_model_evaluations` interceptor runs
        before the `post_list_model_evaluations_with_metadata` interceptor.
        """
        return response

    def post_list_model_evaluations_with_metadata(
        self,
        response: service.ListModelEvaluationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListModelEvaluationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_model_evaluations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_list_model_evaluations_with_metadata`
        interceptor in new development instead of the `post_list_model_evaluations` interceptor.
        When both interceptors are used, this `post_list_model_evaluations_with_metadata` interceptor runs after the
        `post_list_model_evaluations` interceptor. The (possibly modified) response returned by
        `post_list_model_evaluations` will be passed to
        `post_list_model_evaluations_with_metadata`.
        """
        return response, metadata

    def pre_list_models(
        self,
        request: service.ListModelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListModelsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_models

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_list_models(
        self, response: service.ListModelsResponse
    ) -> service.ListModelsResponse:
        """Post-rpc interceptor for list_models

        DEPRECATED. Please use the `post_list_models_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_list_models` interceptor runs
        before the `post_list_models_with_metadata` interceptor.
        """
        return response

    def post_list_models_with_metadata(
        self,
        response: service.ListModelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListModelsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_models

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_list_models_with_metadata`
        interceptor in new development instead of the `post_list_models` interceptor.
        When both interceptors are used, this `post_list_models_with_metadata` interceptor runs after the
        `post_list_models` interceptor. The (possibly modified) response returned by
        `post_list_models` will be passed to
        `post_list_models_with_metadata`.
        """
        return response, metadata

    def pre_list_table_specs(
        self,
        request: service.ListTableSpecsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListTableSpecsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_table_specs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_list_table_specs(
        self, response: service.ListTableSpecsResponse
    ) -> service.ListTableSpecsResponse:
        """Post-rpc interceptor for list_table_specs

        DEPRECATED. Please use the `post_list_table_specs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_list_table_specs` interceptor runs
        before the `post_list_table_specs_with_metadata` interceptor.
        """
        return response

    def post_list_table_specs_with_metadata(
        self,
        response: service.ListTableSpecsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListTableSpecsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_table_specs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_list_table_specs_with_metadata`
        interceptor in new development instead of the `post_list_table_specs` interceptor.
        When both interceptors are used, this `post_list_table_specs_with_metadata` interceptor runs after the
        `post_list_table_specs` interceptor. The (possibly modified) response returned by
        `post_list_table_specs` will be passed to
        `post_list_table_specs_with_metadata`.
        """
        return response, metadata

    def pre_undeploy_model(
        self,
        request: service.UndeployModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UndeployModelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for undeploy_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_undeploy_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for undeploy_model

        DEPRECATED. Please use the `post_undeploy_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_undeploy_model` interceptor runs
        before the `post_undeploy_model_with_metadata` interceptor.
        """
        return response

    def post_undeploy_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for undeploy_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_undeploy_model_with_metadata`
        interceptor in new development instead of the `post_undeploy_model` interceptor.
        When both interceptors are used, this `post_undeploy_model_with_metadata` interceptor runs after the
        `post_undeploy_model` interceptor. The (possibly modified) response returned by
        `post_undeploy_model` will be passed to
        `post_undeploy_model_with_metadata`.
        """
        return response, metadata

    def pre_update_column_spec(
        self,
        request: service.UpdateColumnSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateColumnSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_column_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_update_column_spec(
        self, response: gca_column_spec.ColumnSpec
    ) -> gca_column_spec.ColumnSpec:
        """Post-rpc interceptor for update_column_spec

        DEPRECATED. Please use the `post_update_column_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_update_column_spec` interceptor runs
        before the `post_update_column_spec_with_metadata` interceptor.
        """
        return response

    def post_update_column_spec_with_metadata(
        self,
        response: gca_column_spec.ColumnSpec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gca_column_spec.ColumnSpec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_column_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_update_column_spec_with_metadata`
        interceptor in new development instead of the `post_update_column_spec` interceptor.
        When both interceptors are used, this `post_update_column_spec_with_metadata` interceptor runs after the
        `post_update_column_spec` interceptor. The (possibly modified) response returned by
        `post_update_column_spec` will be passed to
        `post_update_column_spec_with_metadata`.
        """
        return response, metadata

    def pre_update_dataset(
        self,
        request: service.UpdateDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateDatasetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_update_dataset(self, response: gca_dataset.Dataset) -> gca_dataset.Dataset:
        """Post-rpc interceptor for update_dataset

        DEPRECATED. Please use the `post_update_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_update_dataset` interceptor runs
        before the `post_update_dataset_with_metadata` interceptor.
        """
        return response

    def post_update_dataset_with_metadata(
        self,
        response: gca_dataset.Dataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gca_dataset.Dataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_update_dataset_with_metadata`
        interceptor in new development instead of the `post_update_dataset` interceptor.
        When both interceptors are used, this `post_update_dataset_with_metadata` interceptor runs after the
        `post_update_dataset` interceptor. The (possibly modified) response returned by
        `post_update_dataset` will be passed to
        `post_update_dataset_with_metadata`.
        """
        return response, metadata

    def pre_update_table_spec(
        self,
        request: service.UpdateTableSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateTableSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_table_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AutoMl server.
        """
        return request, metadata

    def post_update_table_spec(
        self, response: gca_table_spec.TableSpec
    ) -> gca_table_spec.TableSpec:
        """Post-rpc interceptor for update_table_spec

        DEPRECATED. Please use the `post_update_table_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AutoMl server but before
        it is returned to user code. This `post_update_table_spec` interceptor runs
        before the `post_update_table_spec_with_metadata` interceptor.
        """
        return response

    def post_update_table_spec_with_metadata(
        self,
        response: gca_table_spec.TableSpec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gca_table_spec.TableSpec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_table_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AutoMl server but before it is returned to user code.

        We recommend only using this `post_update_table_spec_with_metadata`
        interceptor in new development instead of the `post_update_table_spec` interceptor.
        When both interceptors are used, this `post_update_table_spec_with_metadata` interceptor runs after the
        `post_update_table_spec` interceptor. The (possibly modified) response returned by
        `post_update_table_spec` will be passed to
        `post_update_table_spec_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class AutoMlRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AutoMlRestInterceptor


class AutoMlRestTransport(_BaseAutoMlRestTransport):
    """REST backend synchronous transport for AutoMl.

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
    snake_case or kebab-case, either of those cases is accepted.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "automl.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AutoMlRestInterceptor] = None,
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
            interceptor (Optional[AutoMlRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AutoMlRestInterceptor()
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
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*}/operations",
                    },
                ],
                "google.longrunning.Operations.WaitOperation": [
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:wait",
                        "body": "*",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateDataset(_BaseAutoMlRestTransport._BaseCreateDataset, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.CreateDataset")

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
            request: service.CreateDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gca_dataset.Dataset:
            r"""Call the create dataset method over HTTP.

            Args:
                request (~.service.CreateDatasetRequest):
                    The request object. Request message for
                [AutoMl.CreateDataset][google.cloud.automl.v1beta1.AutoMl.CreateDataset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gca_dataset.Dataset:
                    A workspace for solving a single,
                particular machine learning (ML)
                problem. A workspace contains examples
                that may be annotated.

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseCreateDataset._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseCreateDataset,
                    "_BaseCreateDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.CreateDataset",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "CreateDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._CreateDataset._get_response(
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
            resp = gca_dataset.Dataset()
            pb_resp = gca_dataset.Dataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gca_dataset.Dataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.create_dataset",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "CreateDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateModel(_BaseAutoMlRestTransport._BaseCreateModel, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.CreateModel")

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
            request: service.CreateModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create model method over HTTP.

            Args:
                request (~.service.CreateModelRequest):
                    The request object. Request message for
                [AutoMl.CreateModel][google.cloud.automl.v1beta1.AutoMl.CreateModel].
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

            http_options = _BaseAutoMlRestTransport._BaseCreateModel._get_http_options()
            request, metadata = self._interceptor.pre_create_model(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseCreateModel,
                    "_BaseCreateModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.CreateModel",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "CreateModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._CreateModel._get_response(
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

            resp = self._interceptor.post_create_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_model_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.create_model",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "CreateModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDataset(_BaseAutoMlRestTransport._BaseDeleteDataset, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.DeleteDataset")

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
            request: service.DeleteDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete dataset method over HTTP.

            Args:
                request (~.service.DeleteDatasetRequest):
                    The request object. Request message for
                [AutoMl.DeleteDataset][google.cloud.automl.v1beta1.AutoMl.DeleteDataset].
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

            http_options = (
                _BaseAutoMlRestTransport._BaseDeleteDataset._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseDeleteDataset,
                    "_BaseDeleteDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.DeleteDataset",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "DeleteDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._DeleteDataset._get_response(
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

            resp = self._interceptor.post_delete_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_dataset_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.delete_dataset",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "DeleteDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteModel(_BaseAutoMlRestTransport._BaseDeleteModel, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.DeleteModel")

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
            request: service.DeleteModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete model method over HTTP.

            Args:
                request (~.service.DeleteModelRequest):
                    The request object. Request message for
                [AutoMl.DeleteModel][google.cloud.automl.v1beta1.AutoMl.DeleteModel].
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

            http_options = _BaseAutoMlRestTransport._BaseDeleteModel._get_http_options()
            request, metadata = self._interceptor.pre_delete_model(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseDeleteModel,
                    "_BaseDeleteModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.DeleteModel",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "DeleteModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._DeleteModel._get_response(
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

            resp = self._interceptor.post_delete_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_model_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.delete_model",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "DeleteModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeployModel(_BaseAutoMlRestTransport._BaseDeployModel, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.DeployModel")

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
            request: service.DeployModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the deploy model method over HTTP.

            Args:
                request (~.service.DeployModelRequest):
                    The request object. Request message for
                [AutoMl.DeployModel][google.cloud.automl.v1beta1.AutoMl.DeployModel].
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

            http_options = _BaseAutoMlRestTransport._BaseDeployModel._get_http_options()
            request, metadata = self._interceptor.pre_deploy_model(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseDeployModel,
                    "_BaseDeployModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.DeployModel",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "DeployModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._DeployModel._get_response(
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

            resp = self._interceptor.post_deploy_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deploy_model_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.deploy_model",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "DeployModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportData(_BaseAutoMlRestTransport._BaseExportData, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.ExportData")

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
            request: service.ExportDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export data method over HTTP.

            Args:
                request (~.service.ExportDataRequest):
                    The request object. Request message for
                [AutoMl.ExportData][google.cloud.automl.v1beta1.AutoMl.ExportData].
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

            http_options = _BaseAutoMlRestTransport._BaseExportData._get_http_options()
            request, metadata = self._interceptor.pre_export_data(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseExportData,
                    "_BaseExportData__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ExportData",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ExportData",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ExportData._get_response(
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

            resp = self._interceptor.post_export_data(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_data_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.export_data",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ExportData",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportEvaluatedExamples(
        _BaseAutoMlRestTransport._BaseExportEvaluatedExamples, AutoMlRestStub
    ):
        def __hash__(self):
            return hash("AutoMlRestTransport.ExportEvaluatedExamples")

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
            request: service.ExportEvaluatedExamplesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export evaluated examples method over HTTP.

            Args:
                request (~.service.ExportEvaluatedExamplesRequest):
                    The request object. Request message for
                [AutoMl.ExportEvaluatedExamples][google.cloud.automl.v1beta1.AutoMl.ExportEvaluatedExamples].
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

            http_options = _BaseAutoMlRestTransport._BaseExportEvaluatedExamples._get_http_options()
            request, metadata = self._interceptor.pre_export_evaluated_examples(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseExportEvaluatedExamples,
                    "_BaseExportEvaluatedExamples__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ExportEvaluatedExamples",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ExportEvaluatedExamples",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ExportEvaluatedExamples._get_response(
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

            resp = self._interceptor.post_export_evaluated_examples(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_evaluated_examples_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.export_evaluated_examples",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ExportEvaluatedExamples",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportModel(_BaseAutoMlRestTransport._BaseExportModel, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.ExportModel")

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
            request: service.ExportModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export model method over HTTP.

            Args:
                request (~.service.ExportModelRequest):
                    The request object. Request message for
                [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel].
                Models need to be enabled for exporting, otherwise an
                error code will be returned.
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

            http_options = _BaseAutoMlRestTransport._BaseExportModel._get_http_options()
            request, metadata = self._interceptor.pre_export_model(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseExportModel,
                    "_BaseExportModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ExportModel",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ExportModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ExportModel._get_response(
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

            resp = self._interceptor.post_export_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_model_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.export_model",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ExportModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAnnotationSpec(
        _BaseAutoMlRestTransport._BaseGetAnnotationSpec, AutoMlRestStub
    ):
        def __hash__(self):
            return hash("AutoMlRestTransport.GetAnnotationSpec")

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
            request: service.GetAnnotationSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> annotation_spec.AnnotationSpec:
            r"""Call the get annotation spec method over HTTP.

            Args:
                request (~.service.GetAnnotationSpecRequest):
                    The request object. Request message for
                [AutoMl.GetAnnotationSpec][google.cloud.automl.v1beta1.AutoMl.GetAnnotationSpec].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.annotation_spec.AnnotationSpec:
                    A definition of an annotation spec.
            """

            http_options = (
                _BaseAutoMlRestTransport._BaseGetAnnotationSpec._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_annotation_spec(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseGetAnnotationSpec,
                    "_BaseGetAnnotationSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.GetAnnotationSpec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetAnnotationSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._GetAnnotationSpec._get_response(
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
            resp = annotation_spec.AnnotationSpec()
            pb_resp = annotation_spec.AnnotationSpec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_annotation_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_annotation_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = annotation_spec.AnnotationSpec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.get_annotation_spec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetAnnotationSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetColumnSpec(_BaseAutoMlRestTransport._BaseGetColumnSpec, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.GetColumnSpec")

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
            request: service.GetColumnSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> column_spec.ColumnSpec:
            r"""Call the get column spec method over HTTP.

            Args:
                request (~.service.GetColumnSpecRequest):
                    The request object. Request message for
                [AutoMl.GetColumnSpec][google.cloud.automl.v1beta1.AutoMl.GetColumnSpec].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.column_spec.ColumnSpec:
                    A representation of a column in a relational table. When
                listing them, column specs are returned in the same
                order in which they were given on import . Used by:

                - Tables

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseGetColumnSpec._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_column_spec(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseGetColumnSpec,
                    "_BaseGetColumnSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.GetColumnSpec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetColumnSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._GetColumnSpec._get_response(
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
            resp = column_spec.ColumnSpec()
            pb_resp = column_spec.ColumnSpec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_column_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_column_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = column_spec.ColumnSpec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.get_column_spec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetColumnSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataset(_BaseAutoMlRestTransport._BaseGetDataset, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.GetDataset")

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
            request: service.GetDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataset.Dataset:
            r"""Call the get dataset method over HTTP.

            Args:
                request (~.service.GetDatasetRequest):
                    The request object. Request message for
                [AutoMl.GetDataset][google.cloud.automl.v1beta1.AutoMl.GetDataset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataset.Dataset:
                    A workspace for solving a single,
                particular machine learning (ML)
                problem. A workspace contains examples
                that may be annotated.

            """

            http_options = _BaseAutoMlRestTransport._BaseGetDataset._get_http_options()
            request, metadata = self._interceptor.pre_get_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseGetDataset,
                    "_BaseGetDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.GetDataset",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._GetDataset._get_response(
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
            resp = dataset.Dataset()
            pb_resp = dataset.Dataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataset.Dataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.get_dataset",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetModel(_BaseAutoMlRestTransport._BaseGetModel, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.GetModel")

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
            request: service.GetModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> model.Model:
            r"""Call the get model method over HTTP.

            Args:
                request (~.service.GetModelRequest):
                    The request object. Request message for
                [AutoMl.GetModel][google.cloud.automl.v1beta1.AutoMl.GetModel].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.model.Model:
                    API proto representing a trained
                machine learning model.

            """

            http_options = _BaseAutoMlRestTransport._BaseGetModel._get_http_options()
            request, metadata = self._interceptor.pre_get_model(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseGetModel,
                    "_BaseGetModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.GetModel",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._GetModel._get_response(
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
            resp = model.Model()
            pb_resp = model.Model.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_model_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = model.Model.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.get_model",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetModelEvaluation(
        _BaseAutoMlRestTransport._BaseGetModelEvaluation, AutoMlRestStub
    ):
        def __hash__(self):
            return hash("AutoMlRestTransport.GetModelEvaluation")

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
            request: service.GetModelEvaluationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> model_evaluation.ModelEvaluation:
            r"""Call the get model evaluation method over HTTP.

            Args:
                request (~.service.GetModelEvaluationRequest):
                    The request object. Request message for
                [AutoMl.GetModelEvaluation][google.cloud.automl.v1beta1.AutoMl.GetModelEvaluation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.model_evaluation.ModelEvaluation:
                    Evaluation results of a model.
            """

            http_options = (
                _BaseAutoMlRestTransport._BaseGetModelEvaluation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_model_evaluation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseGetModelEvaluation,
                    "_BaseGetModelEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.GetModelEvaluation",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetModelEvaluation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._GetModelEvaluation._get_response(
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
            resp = model_evaluation.ModelEvaluation()
            pb_resp = model_evaluation.ModelEvaluation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_model_evaluation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_model_evaluation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = model_evaluation.ModelEvaluation.to_json(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.get_model_evaluation",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetModelEvaluation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTableSpec(_BaseAutoMlRestTransport._BaseGetTableSpec, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.GetTableSpec")

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
            request: service.GetTableSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> table_spec.TableSpec:
            r"""Call the get table spec method over HTTP.

            Args:
                request (~.service.GetTableSpecRequest):
                    The request object. Request message for
                [AutoMl.GetTableSpec][google.cloud.automl.v1beta1.AutoMl.GetTableSpec].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.table_spec.TableSpec:
                    A specification of a relational table. The table's
                schema is represented via its child column specs. It is
                pre-populated as part of ImportData by schema inference
                algorithm, the version of which is a required parameter
                of ImportData InputConfig. Note: While working with a
                table, at times the schema may be inconsistent with the
                data in the table (e.g. string in a FLOAT64 column). The
                consistency validation is done upon creation of a model.
                Used by:

                - Tables

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseGetTableSpec._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_table_spec(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseGetTableSpec,
                    "_BaseGetTableSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.GetTableSpec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetTableSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._GetTableSpec._get_response(
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
            resp = table_spec.TableSpec()
            pb_resp = table_spec.TableSpec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_table_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_table_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = table_spec.TableSpec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.get_table_spec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "GetTableSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportData(_BaseAutoMlRestTransport._BaseImportData, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.ImportData")

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
            request: service.ImportDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import data method over HTTP.

            Args:
                request (~.service.ImportDataRequest):
                    The request object. Request message for
                [AutoMl.ImportData][google.cloud.automl.v1beta1.AutoMl.ImportData].
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

            http_options = _BaseAutoMlRestTransport._BaseImportData._get_http_options()
            request, metadata = self._interceptor.pre_import_data(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseImportData,
                    "_BaseImportData__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ImportData",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ImportData",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ImportData._get_response(
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

            resp = self._interceptor.post_import_data(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_data_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.import_data",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ImportData",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListColumnSpecs(
        _BaseAutoMlRestTransport._BaseListColumnSpecs, AutoMlRestStub
    ):
        def __hash__(self):
            return hash("AutoMlRestTransport.ListColumnSpecs")

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
            request: service.ListColumnSpecsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListColumnSpecsResponse:
            r"""Call the list column specs method over HTTP.

            Args:
                request (~.service.ListColumnSpecsRequest):
                    The request object. Request message for
                [AutoMl.ListColumnSpecs][google.cloud.automl.v1beta1.AutoMl.ListColumnSpecs].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListColumnSpecsResponse:
                    Response message for
                [AutoMl.ListColumnSpecs][google.cloud.automl.v1beta1.AutoMl.ListColumnSpecs].

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseListColumnSpecs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_column_specs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseListColumnSpecs,
                    "_BaseListColumnSpecs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ListColumnSpecs",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListColumnSpecs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ListColumnSpecs._get_response(
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
            resp = service.ListColumnSpecsResponse()
            pb_resp = service.ListColumnSpecsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_column_specs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_column_specs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListColumnSpecsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.list_column_specs",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListColumnSpecs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDatasets(_BaseAutoMlRestTransport._BaseListDatasets, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.ListDatasets")

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
            request: service.ListDatasetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListDatasetsResponse:
            r"""Call the list datasets method over HTTP.

            Args:
                request (~.service.ListDatasetsRequest):
                    The request object. Request message for
                [AutoMl.ListDatasets][google.cloud.automl.v1beta1.AutoMl.ListDatasets].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListDatasetsResponse:
                    Response message for
                [AutoMl.ListDatasets][google.cloud.automl.v1beta1.AutoMl.ListDatasets].

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseListDatasets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_datasets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseListDatasets,
                    "_BaseListDatasets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ListDatasets",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListDatasets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ListDatasets._get_response(
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
            resp = service.ListDatasetsResponse()
            pb_resp = service.ListDatasetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_datasets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_datasets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListDatasetsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.list_datasets",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListDatasets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListModelEvaluations(
        _BaseAutoMlRestTransport._BaseListModelEvaluations, AutoMlRestStub
    ):
        def __hash__(self):
            return hash("AutoMlRestTransport.ListModelEvaluations")

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
            request: service.ListModelEvaluationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListModelEvaluationsResponse:
            r"""Call the list model evaluations method over HTTP.

            Args:
                request (~.service.ListModelEvaluationsRequest):
                    The request object. Request message for
                [AutoMl.ListModelEvaluations][google.cloud.automl.v1beta1.AutoMl.ListModelEvaluations].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListModelEvaluationsResponse:
                    Response message for
                [AutoMl.ListModelEvaluations][google.cloud.automl.v1beta1.AutoMl.ListModelEvaluations].

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseListModelEvaluations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_model_evaluations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseListModelEvaluations,
                    "_BaseListModelEvaluations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ListModelEvaluations",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListModelEvaluations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ListModelEvaluations._get_response(
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
            resp = service.ListModelEvaluationsResponse()
            pb_resp = service.ListModelEvaluationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_model_evaluations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_model_evaluations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListModelEvaluationsResponse.to_json(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.list_model_evaluations",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListModelEvaluations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListModels(_BaseAutoMlRestTransport._BaseListModels, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.ListModels")

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
            request: service.ListModelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListModelsResponse:
            r"""Call the list models method over HTTP.

            Args:
                request (~.service.ListModelsRequest):
                    The request object. Request message for
                [AutoMl.ListModels][google.cloud.automl.v1beta1.AutoMl.ListModels].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListModelsResponse:
                    Response message for
                [AutoMl.ListModels][google.cloud.automl.v1beta1.AutoMl.ListModels].

            """

            http_options = _BaseAutoMlRestTransport._BaseListModels._get_http_options()
            request, metadata = self._interceptor.pre_list_models(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseListModels,
                    "_BaseListModels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ListModels",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListModels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ListModels._get_response(
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
            resp = service.ListModelsResponse()
            pb_resp = service.ListModelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_models(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_models_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListModelsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.list_models",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListModels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTableSpecs(_BaseAutoMlRestTransport._BaseListTableSpecs, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.ListTableSpecs")

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
            request: service.ListTableSpecsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListTableSpecsResponse:
            r"""Call the list table specs method over HTTP.

            Args:
                request (~.service.ListTableSpecsRequest):
                    The request object. Request message for
                [AutoMl.ListTableSpecs][google.cloud.automl.v1beta1.AutoMl.ListTableSpecs].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListTableSpecsResponse:
                    Response message for
                [AutoMl.ListTableSpecs][google.cloud.automl.v1beta1.AutoMl.ListTableSpecs].

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseListTableSpecs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_table_specs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseListTableSpecs,
                    "_BaseListTableSpecs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.ListTableSpecs",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListTableSpecs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._ListTableSpecs._get_response(
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
            resp = service.ListTableSpecsResponse()
            pb_resp = service.ListTableSpecsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_table_specs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_table_specs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListTableSpecsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.list_table_specs",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "ListTableSpecs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeployModel(_BaseAutoMlRestTransport._BaseUndeployModel, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.UndeployModel")

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
            request: service.UndeployModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the undeploy model method over HTTP.

            Args:
                request (~.service.UndeployModelRequest):
                    The request object. Request message for
                [AutoMl.UndeployModel][google.cloud.automl.v1beta1.AutoMl.UndeployModel].
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

            http_options = (
                _BaseAutoMlRestTransport._BaseUndeployModel._get_http_options()
            )
            request, metadata = self._interceptor.pre_undeploy_model(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseUndeployModel,
                    "_BaseUndeployModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.UndeployModel",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "UndeployModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._UndeployModel._get_response(
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

            resp = self._interceptor.post_undeploy_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undeploy_model_with_metadata(
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
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.undeploy_model",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "UndeployModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateColumnSpec(
        _BaseAutoMlRestTransport._BaseUpdateColumnSpec, AutoMlRestStub
    ):
        def __hash__(self):
            return hash("AutoMlRestTransport.UpdateColumnSpec")

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
            request: service.UpdateColumnSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gca_column_spec.ColumnSpec:
            r"""Call the update column spec method over HTTP.

            Args:
                request (~.service.UpdateColumnSpecRequest):
                    The request object. Request message for
                [AutoMl.UpdateColumnSpec][google.cloud.automl.v1beta1.AutoMl.UpdateColumnSpec]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gca_column_spec.ColumnSpec:
                    A representation of a column in a relational table. When
                listing them, column specs are returned in the same
                order in which they were given on import . Used by:

                - Tables

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseUpdateColumnSpec._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_column_spec(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseUpdateColumnSpec,
                    "_BaseUpdateColumnSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.UpdateColumnSpec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "UpdateColumnSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._UpdateColumnSpec._get_response(
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
            resp = gca_column_spec.ColumnSpec()
            pb_resp = gca_column_spec.ColumnSpec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_column_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_column_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gca_column_spec.ColumnSpec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.update_column_spec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "UpdateColumnSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataset(_BaseAutoMlRestTransport._BaseUpdateDataset, AutoMlRestStub):
        def __hash__(self):
            return hash("AutoMlRestTransport.UpdateDataset")

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
            request: service.UpdateDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gca_dataset.Dataset:
            r"""Call the update dataset method over HTTP.

            Args:
                request (~.service.UpdateDatasetRequest):
                    The request object. Request message for
                [AutoMl.UpdateDataset][google.cloud.automl.v1beta1.AutoMl.UpdateDataset]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gca_dataset.Dataset:
                    A workspace for solving a single,
                particular machine learning (ML)
                problem. A workspace contains examples
                that may be annotated.

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseUpdateDataset._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseUpdateDataset,
                    "_BaseUpdateDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.UpdateDataset",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "UpdateDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._UpdateDataset._get_response(
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
            resp = gca_dataset.Dataset()
            pb_resp = gca_dataset.Dataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gca_dataset.Dataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.update_dataset",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "UpdateDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTableSpec(
        _BaseAutoMlRestTransport._BaseUpdateTableSpec, AutoMlRestStub
    ):
        def __hash__(self):
            return hash("AutoMlRestTransport.UpdateTableSpec")

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
            request: service.UpdateTableSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gca_table_spec.TableSpec:
            r"""Call the update table spec method over HTTP.

            Args:
                request (~.service.UpdateTableSpecRequest):
                    The request object. Request message for
                [AutoMl.UpdateTableSpec][google.cloud.automl.v1beta1.AutoMl.UpdateTableSpec]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gca_table_spec.TableSpec:
                    A specification of a relational table. The table's
                schema is represented via its child column specs. It is
                pre-populated as part of ImportData by schema inference
                algorithm, the version of which is a required parameter
                of ImportData InputConfig. Note: While working with a
                table, at times the schema may be inconsistent with the
                data in the table (e.g. string in a FLOAT64 column). The
                consistency validation is done upon creation of a model.
                Used by:

                - Tables

            """

            http_options = (
                _BaseAutoMlRestTransport._BaseUpdateTableSpec._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_table_spec(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAutoMlRestTransport._BaseUpdateTableSpec,
                    "_BaseUpdateTableSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.automl_v1beta1.AutoMlClient.UpdateTableSpec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "UpdateTableSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AutoMlRestTransport._UpdateTableSpec._get_response(
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
            resp = gca_table_spec.TableSpec()
            pb_resp = gca_table_spec.TableSpec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_table_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_table_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gca_table_spec.TableSpec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.automl_v1beta1.AutoMlClient.update_table_spec",
                    extra={
                        "serviceName": "google.cloud.automl.v1beta1.AutoMl",
                        "rpcName": "UpdateTableSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_dataset(
        self,
    ) -> Callable[[service.CreateDatasetRequest], gca_dataset.Dataset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_model(
        self,
    ) -> Callable[[service.CreateModelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_dataset(
        self,
    ) -> Callable[[service.DeleteDatasetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_model(
        self,
    ) -> Callable[[service.DeleteModelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def deploy_model(
        self,
    ) -> Callable[[service.DeployModelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeployModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_data(
        self,
    ) -> Callable[[service.ExportDataRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_evaluated_examples(
        self,
    ) -> Callable[[service.ExportEvaluatedExamplesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportEvaluatedExamples(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def export_model(
        self,
    ) -> Callable[[service.ExportModelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_annotation_spec(
        self,
    ) -> Callable[[service.GetAnnotationSpecRequest], annotation_spec.AnnotationSpec]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAnnotationSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_column_spec(
        self,
    ) -> Callable[[service.GetColumnSpecRequest], column_spec.ColumnSpec]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetColumnSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dataset(self) -> Callable[[service.GetDatasetRequest], dataset.Dataset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_model(self) -> Callable[[service.GetModelRequest], model.Model]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_model_evaluation(
        self,
    ) -> Callable[
        [service.GetModelEvaluationRequest], model_evaluation.ModelEvaluation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetModelEvaluation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_table_spec(
        self,
    ) -> Callable[[service.GetTableSpecRequest], table_spec.TableSpec]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTableSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_data(
        self,
    ) -> Callable[[service.ImportDataRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_column_specs(
        self,
    ) -> Callable[[service.ListColumnSpecsRequest], service.ListColumnSpecsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListColumnSpecs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_datasets(
        self,
    ) -> Callable[[service.ListDatasetsRequest], service.ListDatasetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDatasets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_model_evaluations(
        self,
    ) -> Callable[
        [service.ListModelEvaluationsRequest], service.ListModelEvaluationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListModelEvaluations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_models(
        self,
    ) -> Callable[[service.ListModelsRequest], service.ListModelsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListModels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_table_specs(
        self,
    ) -> Callable[[service.ListTableSpecsRequest], service.ListTableSpecsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTableSpecs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def undeploy_model(
        self,
    ) -> Callable[[service.UndeployModelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeployModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_column_spec(
        self,
    ) -> Callable[[service.UpdateColumnSpecRequest], gca_column_spec.ColumnSpec]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateColumnSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_dataset(
        self,
    ) -> Callable[[service.UpdateDatasetRequest], gca_dataset.Dataset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_table_spec(
        self,
    ) -> Callable[[service.UpdateTableSpecRequest], gca_table_spec.TableSpec]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTableSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("AutoMlRestTransport",)
