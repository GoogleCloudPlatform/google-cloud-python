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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.visionai_v1alpha1._compat import transcode_request
from google.cloud.visionai_v1alpha1.types import warehouse

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseWarehouseRestTransport

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


class WarehouseRestInterceptor:
    """Interceptor for Warehouse.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the WarehouseRestTransport.

    .. code-block:: python
        class MyCustomWarehouseInterceptor(WarehouseRestInterceptor):
            def pre_clip_asset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_clip_asset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_annotation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_annotation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_asset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_asset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_corpus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_search_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_search_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_annotation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_asset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_asset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_data_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_search_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_generate_hls_uri(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_hls_uri(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_annotation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_annotation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_asset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_asset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_corpus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_search_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_search_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_annotations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_annotations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_corpora(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_corpora(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_schemas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_schemas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_search_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_search_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_annotation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_annotation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_asset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_asset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_corpus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_search_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_search_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = WarehouseRestTransport(interceptor=MyCustomWarehouseInterceptor())
        client = WarehouseClient(transport=transport)


    """

    def pre_clip_asset(
        self,
        request: warehouse.ClipAssetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.ClipAssetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for clip_asset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_clip_asset(
        self, response: warehouse.ClipAssetResponse
    ) -> warehouse.ClipAssetResponse:
        """Post-rpc interceptor for clip_asset

        DEPRECATED. Please use the `post_clip_asset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_clip_asset` interceptor runs
        before the `post_clip_asset_with_metadata` interceptor.
        """
        return response

    def post_clip_asset_with_metadata(
        self,
        response: warehouse.ClipAssetResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.ClipAssetResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for clip_asset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_clip_asset_with_metadata`
        interceptor in new development instead of the `post_clip_asset` interceptor.
        When both interceptors are used, this `post_clip_asset_with_metadata` interceptor runs after the
        `post_clip_asset` interceptor. The (possibly modified) response returned by
        `post_clip_asset` will be passed to
        `post_clip_asset_with_metadata`.
        """
        return response, metadata

    def pre_create_annotation(
        self,
        request: warehouse.CreateAnnotationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.CreateAnnotationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_annotation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_create_annotation(
        self, response: warehouse.Annotation
    ) -> warehouse.Annotation:
        """Post-rpc interceptor for create_annotation

        DEPRECATED. Please use the `post_create_annotation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_create_annotation` interceptor runs
        before the `post_create_annotation_with_metadata` interceptor.
        """
        return response

    def post_create_annotation_with_metadata(
        self,
        response: warehouse.Annotation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.Annotation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_annotation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_create_annotation_with_metadata`
        interceptor in new development instead of the `post_create_annotation` interceptor.
        When both interceptors are used, this `post_create_annotation_with_metadata` interceptor runs after the
        `post_create_annotation` interceptor. The (possibly modified) response returned by
        `post_create_annotation` will be passed to
        `post_create_annotation_with_metadata`.
        """
        return response, metadata

    def pre_create_asset(
        self,
        request: warehouse.CreateAssetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.CreateAssetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_asset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_create_asset(self, response: warehouse.Asset) -> warehouse.Asset:
        """Post-rpc interceptor for create_asset

        DEPRECATED. Please use the `post_create_asset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_create_asset` interceptor runs
        before the `post_create_asset_with_metadata` interceptor.
        """
        return response

    def post_create_asset_with_metadata(
        self,
        response: warehouse.Asset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.Asset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_asset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_create_asset_with_metadata`
        interceptor in new development instead of the `post_create_asset` interceptor.
        When both interceptors are used, this `post_create_asset_with_metadata` interceptor runs after the
        `post_create_asset` interceptor. The (possibly modified) response returned by
        `post_create_asset` will be passed to
        `post_create_asset_with_metadata`.
        """
        return response, metadata

    def pre_create_corpus(
        self,
        request: warehouse.CreateCorpusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.CreateCorpusRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_create_corpus(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_corpus

        DEPRECATED. Please use the `post_create_corpus_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_create_corpus` interceptor runs
        before the `post_create_corpus_with_metadata` interceptor.
        """
        return response

    def post_create_corpus_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_corpus

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_create_corpus_with_metadata`
        interceptor in new development instead of the `post_create_corpus` interceptor.
        When both interceptors are used, this `post_create_corpus_with_metadata` interceptor runs after the
        `post_create_corpus` interceptor. The (possibly modified) response returned by
        `post_create_corpus` will be passed to
        `post_create_corpus_with_metadata`.
        """
        return response, metadata

    def pre_create_data_schema(
        self,
        request: warehouse.CreateDataSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.CreateDataSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_data_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_create_data_schema(
        self, response: warehouse.DataSchema
    ) -> warehouse.DataSchema:
        """Post-rpc interceptor for create_data_schema

        DEPRECATED. Please use the `post_create_data_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_create_data_schema` interceptor runs
        before the `post_create_data_schema_with_metadata` interceptor.
        """
        return response

    def post_create_data_schema_with_metadata(
        self,
        response: warehouse.DataSchema,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.DataSchema, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_create_data_schema_with_metadata`
        interceptor in new development instead of the `post_create_data_schema` interceptor.
        When both interceptors are used, this `post_create_data_schema_with_metadata` interceptor runs after the
        `post_create_data_schema` interceptor. The (possibly modified) response returned by
        `post_create_data_schema` will be passed to
        `post_create_data_schema_with_metadata`.
        """
        return response, metadata

    def pre_create_search_config(
        self,
        request: warehouse.CreateSearchConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.CreateSearchConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_search_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_create_search_config(
        self, response: warehouse.SearchConfig
    ) -> warehouse.SearchConfig:
        """Post-rpc interceptor for create_search_config

        DEPRECATED. Please use the `post_create_search_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_create_search_config` interceptor runs
        before the `post_create_search_config_with_metadata` interceptor.
        """
        return response

    def post_create_search_config_with_metadata(
        self,
        response: warehouse.SearchConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.SearchConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_search_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_create_search_config_with_metadata`
        interceptor in new development instead of the `post_create_search_config` interceptor.
        When both interceptors are used, this `post_create_search_config_with_metadata` interceptor runs after the
        `post_create_search_config` interceptor. The (possibly modified) response returned by
        `post_create_search_config` will be passed to
        `post_create_search_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_annotation(
        self,
        request: warehouse.DeleteAnnotationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.DeleteAnnotationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_annotation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def pre_delete_asset(
        self,
        request: warehouse.DeleteAssetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.DeleteAssetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_asset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_delete_asset(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_asset

        DEPRECATED. Please use the `post_delete_asset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_delete_asset` interceptor runs
        before the `post_delete_asset_with_metadata` interceptor.
        """
        return response

    def post_delete_asset_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_asset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_delete_asset_with_metadata`
        interceptor in new development instead of the `post_delete_asset` interceptor.
        When both interceptors are used, this `post_delete_asset_with_metadata` interceptor runs after the
        `post_delete_asset` interceptor. The (possibly modified) response returned by
        `post_delete_asset` will be passed to
        `post_delete_asset_with_metadata`.
        """
        return response, metadata

    def pre_delete_corpus(
        self,
        request: warehouse.DeleteCorpusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.DeleteCorpusRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def pre_delete_data_schema(
        self,
        request: warehouse.DeleteDataSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.DeleteDataSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_data_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def pre_delete_search_config(
        self,
        request: warehouse.DeleteSearchConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.DeleteSearchConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_search_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def pre_generate_hls_uri(
        self,
        request: warehouse.GenerateHlsUriRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.GenerateHlsUriRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for generate_hls_uri

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_generate_hls_uri(
        self, response: warehouse.GenerateHlsUriResponse
    ) -> warehouse.GenerateHlsUriResponse:
        """Post-rpc interceptor for generate_hls_uri

        DEPRECATED. Please use the `post_generate_hls_uri_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_generate_hls_uri` interceptor runs
        before the `post_generate_hls_uri_with_metadata` interceptor.
        """
        return response

    def post_generate_hls_uri_with_metadata(
        self,
        response: warehouse.GenerateHlsUriResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.GenerateHlsUriResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for generate_hls_uri

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_generate_hls_uri_with_metadata`
        interceptor in new development instead of the `post_generate_hls_uri` interceptor.
        When both interceptors are used, this `post_generate_hls_uri_with_metadata` interceptor runs after the
        `post_generate_hls_uri` interceptor. The (possibly modified) response returned by
        `post_generate_hls_uri` will be passed to
        `post_generate_hls_uri_with_metadata`.
        """
        return response, metadata

    def pre_get_annotation(
        self,
        request: warehouse.GetAnnotationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.GetAnnotationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_annotation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_get_annotation(
        self, response: warehouse.Annotation
    ) -> warehouse.Annotation:
        """Post-rpc interceptor for get_annotation

        DEPRECATED. Please use the `post_get_annotation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_get_annotation` interceptor runs
        before the `post_get_annotation_with_metadata` interceptor.
        """
        return response

    def post_get_annotation_with_metadata(
        self,
        response: warehouse.Annotation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.Annotation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_annotation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_get_annotation_with_metadata`
        interceptor in new development instead of the `post_get_annotation` interceptor.
        When both interceptors are used, this `post_get_annotation_with_metadata` interceptor runs after the
        `post_get_annotation` interceptor. The (possibly modified) response returned by
        `post_get_annotation` will be passed to
        `post_get_annotation_with_metadata`.
        """
        return response, metadata

    def pre_get_asset(
        self,
        request: warehouse.GetAssetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.GetAssetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_asset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_get_asset(self, response: warehouse.Asset) -> warehouse.Asset:
        """Post-rpc interceptor for get_asset

        DEPRECATED. Please use the `post_get_asset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_get_asset` interceptor runs
        before the `post_get_asset_with_metadata` interceptor.
        """
        return response

    def post_get_asset_with_metadata(
        self,
        response: warehouse.Asset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.Asset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_asset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_get_asset_with_metadata`
        interceptor in new development instead of the `post_get_asset` interceptor.
        When both interceptors are used, this `post_get_asset_with_metadata` interceptor runs after the
        `post_get_asset` interceptor. The (possibly modified) response returned by
        `post_get_asset` will be passed to
        `post_get_asset_with_metadata`.
        """
        return response, metadata

    def pre_get_corpus(
        self,
        request: warehouse.GetCorpusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.GetCorpusRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_get_corpus(self, response: warehouse.Corpus) -> warehouse.Corpus:
        """Post-rpc interceptor for get_corpus

        DEPRECATED. Please use the `post_get_corpus_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_get_corpus` interceptor runs
        before the `post_get_corpus_with_metadata` interceptor.
        """
        return response

    def post_get_corpus_with_metadata(
        self,
        response: warehouse.Corpus,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.Corpus, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_corpus

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_get_corpus_with_metadata`
        interceptor in new development instead of the `post_get_corpus` interceptor.
        When both interceptors are used, this `post_get_corpus_with_metadata` interceptor runs after the
        `post_get_corpus` interceptor. The (possibly modified) response returned by
        `post_get_corpus` will be passed to
        `post_get_corpus_with_metadata`.
        """
        return response, metadata

    def pre_get_data_schema(
        self,
        request: warehouse.GetDataSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.GetDataSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_data_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_get_data_schema(
        self, response: warehouse.DataSchema
    ) -> warehouse.DataSchema:
        """Post-rpc interceptor for get_data_schema

        DEPRECATED. Please use the `post_get_data_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_get_data_schema` interceptor runs
        before the `post_get_data_schema_with_metadata` interceptor.
        """
        return response

    def post_get_data_schema_with_metadata(
        self,
        response: warehouse.DataSchema,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.DataSchema, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_get_data_schema_with_metadata`
        interceptor in new development instead of the `post_get_data_schema` interceptor.
        When both interceptors are used, this `post_get_data_schema_with_metadata` interceptor runs after the
        `post_get_data_schema` interceptor. The (possibly modified) response returned by
        `post_get_data_schema` will be passed to
        `post_get_data_schema_with_metadata`.
        """
        return response, metadata

    def pre_get_search_config(
        self,
        request: warehouse.GetSearchConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.GetSearchConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_search_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_get_search_config(
        self, response: warehouse.SearchConfig
    ) -> warehouse.SearchConfig:
        """Post-rpc interceptor for get_search_config

        DEPRECATED. Please use the `post_get_search_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_get_search_config` interceptor runs
        before the `post_get_search_config_with_metadata` interceptor.
        """
        return response

    def post_get_search_config_with_metadata(
        self,
        response: warehouse.SearchConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.SearchConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_search_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_get_search_config_with_metadata`
        interceptor in new development instead of the `post_get_search_config` interceptor.
        When both interceptors are used, this `post_get_search_config_with_metadata` interceptor runs after the
        `post_get_search_config` interceptor. The (possibly modified) response returned by
        `post_get_search_config` will be passed to
        `post_get_search_config_with_metadata`.
        """
        return response, metadata

    def pre_list_annotations(
        self,
        request: warehouse.ListAnnotationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.ListAnnotationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_annotations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_list_annotations(
        self, response: warehouse.ListAnnotationsResponse
    ) -> warehouse.ListAnnotationsResponse:
        """Post-rpc interceptor for list_annotations

        DEPRECATED. Please use the `post_list_annotations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_list_annotations` interceptor runs
        before the `post_list_annotations_with_metadata` interceptor.
        """
        return response

    def post_list_annotations_with_metadata(
        self,
        response: warehouse.ListAnnotationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.ListAnnotationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_annotations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_list_annotations_with_metadata`
        interceptor in new development instead of the `post_list_annotations` interceptor.
        When both interceptors are used, this `post_list_annotations_with_metadata` interceptor runs after the
        `post_list_annotations` interceptor. The (possibly modified) response returned by
        `post_list_annotations` will be passed to
        `post_list_annotations_with_metadata`.
        """
        return response, metadata

    def pre_list_assets(
        self,
        request: warehouse.ListAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.ListAssetsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_list_assets(
        self, response: warehouse.ListAssetsResponse
    ) -> warehouse.ListAssetsResponse:
        """Post-rpc interceptor for list_assets

        DEPRECATED. Please use the `post_list_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_list_assets` interceptor runs
        before the `post_list_assets_with_metadata` interceptor.
        """
        return response

    def post_list_assets_with_metadata(
        self,
        response: warehouse.ListAssetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.ListAssetsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_list_assets_with_metadata`
        interceptor in new development instead of the `post_list_assets` interceptor.
        When both interceptors are used, this `post_list_assets_with_metadata` interceptor runs after the
        `post_list_assets` interceptor. The (possibly modified) response returned by
        `post_list_assets` will be passed to
        `post_list_assets_with_metadata`.
        """
        return response, metadata

    def pre_list_corpora(
        self,
        request: warehouse.ListCorporaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.ListCorporaRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_corpora

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_list_corpora(
        self, response: warehouse.ListCorporaResponse
    ) -> warehouse.ListCorporaResponse:
        """Post-rpc interceptor for list_corpora

        DEPRECATED. Please use the `post_list_corpora_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_list_corpora` interceptor runs
        before the `post_list_corpora_with_metadata` interceptor.
        """
        return response

    def post_list_corpora_with_metadata(
        self,
        response: warehouse.ListCorporaResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.ListCorporaResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_corpora

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_list_corpora_with_metadata`
        interceptor in new development instead of the `post_list_corpora` interceptor.
        When both interceptors are used, this `post_list_corpora_with_metadata` interceptor runs after the
        `post_list_corpora` interceptor. The (possibly modified) response returned by
        `post_list_corpora` will be passed to
        `post_list_corpora_with_metadata`.
        """
        return response, metadata

    def pre_list_data_schemas(
        self,
        request: warehouse.ListDataSchemasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.ListDataSchemasRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_schemas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_list_data_schemas(
        self, response: warehouse.ListDataSchemasResponse
    ) -> warehouse.ListDataSchemasResponse:
        """Post-rpc interceptor for list_data_schemas

        DEPRECATED. Please use the `post_list_data_schemas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_list_data_schemas` interceptor runs
        before the `post_list_data_schemas_with_metadata` interceptor.
        """
        return response

    def post_list_data_schemas_with_metadata(
        self,
        response: warehouse.ListDataSchemasResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.ListDataSchemasResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_data_schemas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_list_data_schemas_with_metadata`
        interceptor in new development instead of the `post_list_data_schemas` interceptor.
        When both interceptors are used, this `post_list_data_schemas_with_metadata` interceptor runs after the
        `post_list_data_schemas` interceptor. The (possibly modified) response returned by
        `post_list_data_schemas` will be passed to
        `post_list_data_schemas_with_metadata`.
        """
        return response, metadata

    def pre_list_search_configs(
        self,
        request: warehouse.ListSearchConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.ListSearchConfigsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_search_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_list_search_configs(
        self, response: warehouse.ListSearchConfigsResponse
    ) -> warehouse.ListSearchConfigsResponse:
        """Post-rpc interceptor for list_search_configs

        DEPRECATED. Please use the `post_list_search_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_list_search_configs` interceptor runs
        before the `post_list_search_configs_with_metadata` interceptor.
        """
        return response

    def post_list_search_configs_with_metadata(
        self,
        response: warehouse.ListSearchConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.ListSearchConfigsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_search_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_list_search_configs_with_metadata`
        interceptor in new development instead of the `post_list_search_configs` interceptor.
        When both interceptors are used, this `post_list_search_configs_with_metadata` interceptor runs after the
        `post_list_search_configs` interceptor. The (possibly modified) response returned by
        `post_list_search_configs` will be passed to
        `post_list_search_configs_with_metadata`.
        """
        return response, metadata

    def pre_search_assets(
        self,
        request: warehouse.SearchAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.SearchAssetsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for search_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_search_assets(
        self, response: warehouse.SearchAssetsResponse
    ) -> warehouse.SearchAssetsResponse:
        """Post-rpc interceptor for search_assets

        DEPRECATED. Please use the `post_search_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_search_assets` interceptor runs
        before the `post_search_assets_with_metadata` interceptor.
        """
        return response

    def post_search_assets_with_metadata(
        self,
        response: warehouse.SearchAssetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.SearchAssetsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for search_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_search_assets_with_metadata`
        interceptor in new development instead of the `post_search_assets` interceptor.
        When both interceptors are used, this `post_search_assets_with_metadata` interceptor runs after the
        `post_search_assets` interceptor. The (possibly modified) response returned by
        `post_search_assets` will be passed to
        `post_search_assets_with_metadata`.
        """
        return response, metadata

    def pre_update_annotation(
        self,
        request: warehouse.UpdateAnnotationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.UpdateAnnotationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_annotation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_update_annotation(
        self, response: warehouse.Annotation
    ) -> warehouse.Annotation:
        """Post-rpc interceptor for update_annotation

        DEPRECATED. Please use the `post_update_annotation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_update_annotation` interceptor runs
        before the `post_update_annotation_with_metadata` interceptor.
        """
        return response

    def post_update_annotation_with_metadata(
        self,
        response: warehouse.Annotation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.Annotation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_annotation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_update_annotation_with_metadata`
        interceptor in new development instead of the `post_update_annotation` interceptor.
        When both interceptors are used, this `post_update_annotation_with_metadata` interceptor runs after the
        `post_update_annotation` interceptor. The (possibly modified) response returned by
        `post_update_annotation` will be passed to
        `post_update_annotation_with_metadata`.
        """
        return response, metadata

    def pre_update_asset(
        self,
        request: warehouse.UpdateAssetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.UpdateAssetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_asset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_update_asset(self, response: warehouse.Asset) -> warehouse.Asset:
        """Post-rpc interceptor for update_asset

        DEPRECATED. Please use the `post_update_asset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_update_asset` interceptor runs
        before the `post_update_asset_with_metadata` interceptor.
        """
        return response

    def post_update_asset_with_metadata(
        self,
        response: warehouse.Asset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.Asset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_asset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_update_asset_with_metadata`
        interceptor in new development instead of the `post_update_asset` interceptor.
        When both interceptors are used, this `post_update_asset_with_metadata` interceptor runs after the
        `post_update_asset` interceptor. The (possibly modified) response returned by
        `post_update_asset` will be passed to
        `post_update_asset_with_metadata`.
        """
        return response, metadata

    def pre_update_corpus(
        self,
        request: warehouse.UpdateCorpusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.UpdateCorpusRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_update_corpus(self, response: warehouse.Corpus) -> warehouse.Corpus:
        """Post-rpc interceptor for update_corpus

        DEPRECATED. Please use the `post_update_corpus_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_update_corpus` interceptor runs
        before the `post_update_corpus_with_metadata` interceptor.
        """
        return response

    def post_update_corpus_with_metadata(
        self,
        response: warehouse.Corpus,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.Corpus, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_corpus

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_update_corpus_with_metadata`
        interceptor in new development instead of the `post_update_corpus` interceptor.
        When both interceptors are used, this `post_update_corpus_with_metadata` interceptor runs after the
        `post_update_corpus` interceptor. The (possibly modified) response returned by
        `post_update_corpus` will be passed to
        `post_update_corpus_with_metadata`.
        """
        return response, metadata

    def pre_update_data_schema(
        self,
        request: warehouse.UpdateDataSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.UpdateDataSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_data_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_update_data_schema(
        self, response: warehouse.DataSchema
    ) -> warehouse.DataSchema:
        """Post-rpc interceptor for update_data_schema

        DEPRECATED. Please use the `post_update_data_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_update_data_schema` interceptor runs
        before the `post_update_data_schema_with_metadata` interceptor.
        """
        return response

    def post_update_data_schema_with_metadata(
        self,
        response: warehouse.DataSchema,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.DataSchema, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_update_data_schema_with_metadata`
        interceptor in new development instead of the `post_update_data_schema` interceptor.
        When both interceptors are used, this `post_update_data_schema_with_metadata` interceptor runs after the
        `post_update_data_schema` interceptor. The (possibly modified) response returned by
        `post_update_data_schema` will be passed to
        `post_update_data_schema_with_metadata`.
        """
        return response, metadata

    def pre_update_search_config(
        self,
        request: warehouse.UpdateSearchConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        warehouse.UpdateSearchConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_search_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_update_search_config(
        self, response: warehouse.SearchConfig
    ) -> warehouse.SearchConfig:
        """Post-rpc interceptor for update_search_config

        DEPRECATED. Please use the `post_update_search_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code. This `post_update_search_config` interceptor runs
        before the `post_update_search_config_with_metadata` interceptor.
        """
        return response

    def post_update_search_config_with_metadata(
        self,
        response: warehouse.SearchConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[warehouse.SearchConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_search_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Warehouse server but before it is returned to user code.

        We recommend only using this `post_update_search_config_with_metadata`
        interceptor in new development instead of the `post_update_search_config` interceptor.
        When both interceptors are used, this `post_update_search_config_with_metadata` interceptor runs after the
        `post_update_search_config` interceptor. The (possibly modified) response returned by
        `post_update_search_config` will be passed to
        `post_update_search_config_with_metadata`.
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
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
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
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
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
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
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
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
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
        before they are sent to the Warehouse server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Warehouse server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class WarehouseRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: WarehouseRestInterceptor


class WarehouseRestTransport(_BaseWarehouseRestTransport):
    """REST backend synchronous transport for Warehouse.

    Service that manages media content + metadata for streaming.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "visionai.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[WarehouseRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'visionai.googleapis.com').
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
            interceptor (Optional[WarehouseRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or WarehouseRestInterceptor()
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
                        "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1alpha1/{name=projects/*/locations/*/warehouseOperations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/assets/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1alpha1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1alpha1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _ClipAsset(_BaseWarehouseRestTransport._BaseClipAsset, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.ClipAsset")

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
            request: warehouse.ClipAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.ClipAssetResponse:
            r"""Call the clip asset method over HTTP.

            Args:
                request (~.warehouse.ClipAssetRequest):
                    The request object. Request message for ClipAsset API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.ClipAssetResponse:
                    Response message for ClipAsset API.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseClipAsset._get_http_options()
            )
            request, metadata = self._interceptor.pre_clip_asset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseClipAsset,
                    "_BaseClipAsset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.ClipAsset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ClipAsset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._ClipAsset._get_response(
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
            resp = warehouse.ClipAssetResponse()
            pb_resp = warehouse.ClipAssetResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_clip_asset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_clip_asset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.ClipAssetResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.clip_asset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ClipAsset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAnnotation(
        _BaseWarehouseRestTransport._BaseCreateAnnotation, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.CreateAnnotation")

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
            request: warehouse.CreateAnnotationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.Annotation:
            r"""Call the create annotation method over HTTP.

            Args:
                request (~.warehouse.CreateAnnotationRequest):
                    The request object. Request message for CreateAnnotation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.Annotation:
                    An annotation is a resource in asset.
                It represents a key-value mapping of
                content in asset.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseCreateAnnotation._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_annotation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseCreateAnnotation,
                    "_BaseCreateAnnotation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.CreateAnnotation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateAnnotation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._CreateAnnotation._get_response(
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
            resp = warehouse.Annotation()
            pb_resp = warehouse.Annotation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_annotation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_annotation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.Annotation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.create_annotation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateAnnotation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAsset(_BaseWarehouseRestTransport._BaseCreateAsset, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.CreateAsset")

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
            request: warehouse.CreateAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.Asset:
            r"""Call the create asset method over HTTP.

            Args:
                request (~.warehouse.CreateAssetRequest):
                    The request object. Request message for
                CreateAssetRequest.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.Asset:
                    An asset is a resource in corpus. It
                represents a media object inside corpus,
                contains metadata and another resource
                annotation. Different feature could be
                applied to the asset to generate
                annotations. User could specified
                annotation related to the target asset.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseCreateAsset._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_asset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseCreateAsset,
                    "_BaseCreateAsset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.CreateAsset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateAsset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._CreateAsset._get_response(
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
            resp = warehouse.Asset()
            pb_resp = warehouse.Asset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_asset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_asset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.Asset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.create_asset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateAsset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCorpus(
        _BaseWarehouseRestTransport._BaseCreateCorpus, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.CreateCorpus")

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
            request: warehouse.CreateCorpusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create corpus method over HTTP.

            Args:
                request (~.warehouse.CreateCorpusRequest):
                    The request object. Request message of CreateCorpus API.
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
                _BaseWarehouseRestTransport._BaseCreateCorpus._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_corpus(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseCreateCorpus,
                    "_BaseCreateCorpus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.CreateCorpus",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateCorpus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._CreateCorpus._get_response(
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

            resp = self._interceptor.post_create_corpus(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_corpus_with_metadata(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.create_corpus",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateCorpus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataSchema(
        _BaseWarehouseRestTransport._BaseCreateDataSchema, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.CreateDataSchema")

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
            request: warehouse.CreateDataSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.DataSchema:
            r"""Call the create data schema method over HTTP.

            Args:
                request (~.warehouse.CreateDataSchemaRequest):
                    The request object. Request message for CreateDataSchema.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.DataSchema:
                    Data schema indicates how the user
                specified annotation is interpreted in
                the system.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseCreateDataSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_data_schema(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseCreateDataSchema,
                    "_BaseCreateDataSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.CreateDataSchema",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateDataSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._CreateDataSchema._get_response(
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
            resp = warehouse.DataSchema()
            pb_resp = warehouse.DataSchema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_data_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.DataSchema.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.create_data_schema",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateDataSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSearchConfig(
        _BaseWarehouseRestTransport._BaseCreateSearchConfig, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.CreateSearchConfig")

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
            request: warehouse.CreateSearchConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.SearchConfig:
            r"""Call the create search config method over HTTP.

            Args:
                request (~.warehouse.CreateSearchConfigRequest):
                    The request object. Request message for
                CreateSearchConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.SearchConfig:
                    SearchConfig stores different
                properties that will affect search
                behaviors and search results.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseCreateSearchConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_search_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseCreateSearchConfig,
                    "_BaseCreateSearchConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.CreateSearchConfig",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateSearchConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._CreateSearchConfig._get_response(
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
            resp = warehouse.SearchConfig()
            pb_resp = warehouse.SearchConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_search_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_search_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.SearchConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.create_search_config",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CreateSearchConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAnnotation(
        _BaseWarehouseRestTransport._BaseDeleteAnnotation, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.DeleteAnnotation")

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
            request: warehouse.DeleteAnnotationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete annotation method over HTTP.

            Args:
                request (~.warehouse.DeleteAnnotationRequest):
                    The request object. Request message for DeleteAnnotation
                API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseDeleteAnnotation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_annotation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseDeleteAnnotation,
                    "_BaseDeleteAnnotation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.DeleteAnnotation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "DeleteAnnotation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._DeleteAnnotation._get_response(
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

    class _DeleteAsset(_BaseWarehouseRestTransport._BaseDeleteAsset, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.DeleteAsset")

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
            request: warehouse.DeleteAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete asset method over HTTP.

            Args:
                request (~.warehouse.DeleteAssetRequest):
                    The request object. Request message for DeleteAsset.
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
                _BaseWarehouseRestTransport._BaseDeleteAsset._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_asset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseDeleteAsset,
                    "_BaseDeleteAsset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.DeleteAsset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "DeleteAsset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._DeleteAsset._get_response(
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

            resp = self._interceptor.post_delete_asset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_asset_with_metadata(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.delete_asset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "DeleteAsset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCorpus(
        _BaseWarehouseRestTransport._BaseDeleteCorpus, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.DeleteCorpus")

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
            request: warehouse.DeleteCorpusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete corpus method over HTTP.

            Args:
                request (~.warehouse.DeleteCorpusRequest):
                    The request object. Request message for DeleteCorpus.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseDeleteCorpus._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_corpus(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseDeleteCorpus,
                    "_BaseDeleteCorpus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.DeleteCorpus",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "DeleteCorpus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._DeleteCorpus._get_response(
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

    class _DeleteDataSchema(
        _BaseWarehouseRestTransport._BaseDeleteDataSchema, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.DeleteDataSchema")

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
            request: warehouse.DeleteDataSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete data schema method over HTTP.

            Args:
                request (~.warehouse.DeleteDataSchemaRequest):
                    The request object. Request message for DeleteDataSchema.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseDeleteDataSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_data_schema(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseDeleteDataSchema,
                    "_BaseDeleteDataSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.DeleteDataSchema",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "DeleteDataSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._DeleteDataSchema._get_response(
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

    class _DeleteSearchConfig(
        _BaseWarehouseRestTransport._BaseDeleteSearchConfig, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.DeleteSearchConfig")

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
            request: warehouse.DeleteSearchConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete search config method over HTTP.

            Args:
                request (~.warehouse.DeleteSearchConfigRequest):
                    The request object. Request message for
                DeleteSearchConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseDeleteSearchConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_search_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseDeleteSearchConfig,
                    "_BaseDeleteSearchConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.DeleteSearchConfig",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "DeleteSearchConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._DeleteSearchConfig._get_response(
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

    class _GenerateHlsUri(
        _BaseWarehouseRestTransport._BaseGenerateHlsUri, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.GenerateHlsUri")

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
            request: warehouse.GenerateHlsUriRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.GenerateHlsUriResponse:
            r"""Call the generate hls uri method over HTTP.

            Args:
                request (~.warehouse.GenerateHlsUriRequest):
                    The request object. Request message for GenerateHlsUri
                API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.GenerateHlsUriResponse:
                    Response message for GenerateHlsUri
                API.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseGenerateHlsUri._get_http_options()
            )
            request, metadata = self._interceptor.pre_generate_hls_uri(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGenerateHlsUri,
                    "_BaseGenerateHlsUri__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GenerateHlsUri",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GenerateHlsUri",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GenerateHlsUri._get_response(
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
            resp = warehouse.GenerateHlsUriResponse()
            pb_resp = warehouse.GenerateHlsUriResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_hls_uri(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_hls_uri_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.GenerateHlsUriResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.generate_hls_uri",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GenerateHlsUri",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAnnotation(
        _BaseWarehouseRestTransport._BaseGetAnnotation, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.GetAnnotation")

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
            request: warehouse.GetAnnotationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.Annotation:
            r"""Call the get annotation method over HTTP.

            Args:
                request (~.warehouse.GetAnnotationRequest):
                    The request object. Request message for GetAnnotation
                API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.Annotation:
                    An annotation is a resource in asset.
                It represents a key-value mapping of
                content in asset.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseGetAnnotation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_annotation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGetAnnotation,
                    "_BaseGetAnnotation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GetAnnotation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetAnnotation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GetAnnotation._get_response(
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
            resp = warehouse.Annotation()
            pb_resp = warehouse.Annotation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_annotation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_annotation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.Annotation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.get_annotation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetAnnotation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAsset(_BaseWarehouseRestTransport._BaseGetAsset, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.GetAsset")

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
            request: warehouse.GetAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.Asset:
            r"""Call the get asset method over HTTP.

            Args:
                request (~.warehouse.GetAssetRequest):
                    The request object. Request message for GetAsset.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.Asset:
                    An asset is a resource in corpus. It
                represents a media object inside corpus,
                contains metadata and another resource
                annotation. Different feature could be
                applied to the asset to generate
                annotations. User could specified
                annotation related to the target asset.

            """

            http_options = _BaseWarehouseRestTransport._BaseGetAsset._get_http_options()
            request, metadata = self._interceptor.pre_get_asset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGetAsset,
                    "_BaseGetAsset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GetAsset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetAsset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GetAsset._get_response(
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
            resp = warehouse.Asset()
            pb_resp = warehouse.Asset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_asset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_asset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.Asset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.get_asset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetAsset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCorpus(_BaseWarehouseRestTransport._BaseGetCorpus, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.GetCorpus")

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
            request: warehouse.GetCorpusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.Corpus:
            r"""Call the get corpus method over HTTP.

            Args:
                request (~.warehouse.GetCorpusRequest):
                    The request object. Request message for GetCorpus.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.Corpus:
                    Corpus is a set of video contents for
                management. Within a corpus, videos
                share the same data schema. Search is
                also restricted within a single corpus.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseGetCorpus._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_corpus(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGetCorpus,
                    "_BaseGetCorpus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GetCorpus",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetCorpus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GetCorpus._get_response(
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
            resp = warehouse.Corpus()
            pb_resp = warehouse.Corpus.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_corpus(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_corpus_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.Corpus.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.get_corpus",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetCorpus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataSchema(
        _BaseWarehouseRestTransport._BaseGetDataSchema, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.GetDataSchema")

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
            request: warehouse.GetDataSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.DataSchema:
            r"""Call the get data schema method over HTTP.

            Args:
                request (~.warehouse.GetDataSchemaRequest):
                    The request object. Request message for GetDataSchema.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.DataSchema:
                    Data schema indicates how the user
                specified annotation is interpreted in
                the system.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseGetDataSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_data_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGetDataSchema,
                    "_BaseGetDataSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GetDataSchema",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetDataSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GetDataSchema._get_response(
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
            resp = warehouse.DataSchema()
            pb_resp = warehouse.DataSchema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.DataSchema.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.get_data_schema",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetDataSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSearchConfig(
        _BaseWarehouseRestTransport._BaseGetSearchConfig, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.GetSearchConfig")

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
            request: warehouse.GetSearchConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.SearchConfig:
            r"""Call the get search config method over HTTP.

            Args:
                request (~.warehouse.GetSearchConfigRequest):
                    The request object. Request message for GetSearchConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.SearchConfig:
                    SearchConfig stores different
                properties that will affect search
                behaviors and search results.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseGetSearchConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_search_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGetSearchConfig,
                    "_BaseGetSearchConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GetSearchConfig",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetSearchConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GetSearchConfig._get_response(
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
            resp = warehouse.SearchConfig()
            pb_resp = warehouse.SearchConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_search_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_search_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.SearchConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.get_search_config",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetSearchConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _IngestAsset(_BaseWarehouseRestTransport._BaseIngestAsset, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.IngestAsset")

        def __call__(
            self,
            request: warehouse.IngestAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method IngestAsset is not available over REST transport"
            )

    class _ListAnnotations(
        _BaseWarehouseRestTransport._BaseListAnnotations, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.ListAnnotations")

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
            request: warehouse.ListAnnotationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.ListAnnotationsResponse:
            r"""Call the list annotations method over HTTP.

            Args:
                request (~.warehouse.ListAnnotationsRequest):
                    The request object. Request message for GetAnnotation
                API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.ListAnnotationsResponse:
                    Request message for ListAnnotations
                API.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseListAnnotations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_annotations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseListAnnotations,
                    "_BaseListAnnotations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.ListAnnotations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListAnnotations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._ListAnnotations._get_response(
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
            resp = warehouse.ListAnnotationsResponse()
            pb_resp = warehouse.ListAnnotationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_annotations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_annotations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.ListAnnotationsResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.list_annotations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListAnnotations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAssets(_BaseWarehouseRestTransport._BaseListAssets, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.ListAssets")

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
            request: warehouse.ListAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.ListAssetsResponse:
            r"""Call the list assets method over HTTP.

            Args:
                request (~.warehouse.ListAssetsRequest):
                    The request object. Request message for ListAssets.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.ListAssetsResponse:
                    Response message for ListAssets.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseListAssets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_assets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseListAssets,
                    "_BaseListAssets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.ListAssets",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._ListAssets._get_response(
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
            resp = warehouse.ListAssetsResponse()
            pb_resp = warehouse.ListAssetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_assets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_assets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.ListAssetsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.list_assets",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCorpora(_BaseWarehouseRestTransport._BaseListCorpora, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.ListCorpora")

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
            request: warehouse.ListCorporaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.ListCorporaResponse:
            r"""Call the list corpora method over HTTP.

            Args:
                request (~.warehouse.ListCorporaRequest):
                    The request object. Request message for ListCorpora.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.ListCorporaResponse:
                    Response message for ListCorpora.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseListCorpora._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_corpora(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseListCorpora,
                    "_BaseListCorpora__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.ListCorpora",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListCorpora",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._ListCorpora._get_response(
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
            resp = warehouse.ListCorporaResponse()
            pb_resp = warehouse.ListCorporaResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_corpora(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_corpora_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.ListCorporaResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.list_corpora",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListCorpora",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataSchemas(
        _BaseWarehouseRestTransport._BaseListDataSchemas, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.ListDataSchemas")

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
            request: warehouse.ListDataSchemasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.ListDataSchemasResponse:
            r"""Call the list data schemas method over HTTP.

            Args:
                request (~.warehouse.ListDataSchemasRequest):
                    The request object. Request message for ListDataSchemas.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.ListDataSchemasResponse:
                    Response message for ListDataSchemas.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseListDataSchemas._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_data_schemas(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseListDataSchemas,
                    "_BaseListDataSchemas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.ListDataSchemas",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListDataSchemas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._ListDataSchemas._get_response(
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
            resp = warehouse.ListDataSchemasResponse()
            pb_resp = warehouse.ListDataSchemasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_schemas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_schemas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.ListDataSchemasResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.list_data_schemas",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListDataSchemas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSearchConfigs(
        _BaseWarehouseRestTransport._BaseListSearchConfigs, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.ListSearchConfigs")

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
            request: warehouse.ListSearchConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.ListSearchConfigsResponse:
            r"""Call the list search configs method over HTTP.

            Args:
                request (~.warehouse.ListSearchConfigsRequest):
                    The request object. Request message for
                ListSearchConfigs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.ListSearchConfigsResponse:
                    Response message for
                ListSearchConfigs.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseListSearchConfigs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_search_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseListSearchConfigs,
                    "_BaseListSearchConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.ListSearchConfigs",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListSearchConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._ListSearchConfigs._get_response(
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
            resp = warehouse.ListSearchConfigsResponse()
            pb_resp = warehouse.ListSearchConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_search_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_search_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.ListSearchConfigsResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.list_search_configs",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListSearchConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchAssets(
        _BaseWarehouseRestTransport._BaseSearchAssets, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.SearchAssets")

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
            request: warehouse.SearchAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.SearchAssetsResponse:
            r"""Call the search assets method over HTTP.

            Args:
                request (~.warehouse.SearchAssetsRequest):
                    The request object. Request message for SearchAssets.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.SearchAssetsResponse:
                    Response message for SearchAssets.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseSearchAssets._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_assets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseSearchAssets,
                    "_BaseSearchAssets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.SearchAssets",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "SearchAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._SearchAssets._get_response(
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
            resp = warehouse.SearchAssetsResponse()
            pb_resp = warehouse.SearchAssetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_assets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_assets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.SearchAssetsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.search_assets",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "SearchAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAnnotation(
        _BaseWarehouseRestTransport._BaseUpdateAnnotation, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.UpdateAnnotation")

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
            request: warehouse.UpdateAnnotationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.Annotation:
            r"""Call the update annotation method over HTTP.

            Args:
                request (~.warehouse.UpdateAnnotationRequest):
                    The request object. Request message for UpdateAnnotation
                API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.Annotation:
                    An annotation is a resource in asset.
                It represents a key-value mapping of
                content in asset.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseUpdateAnnotation._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_annotation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseUpdateAnnotation,
                    "_BaseUpdateAnnotation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.UpdateAnnotation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateAnnotation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._UpdateAnnotation._get_response(
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
            resp = warehouse.Annotation()
            pb_resp = warehouse.Annotation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_annotation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_annotation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.Annotation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.update_annotation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateAnnotation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAsset(_BaseWarehouseRestTransport._BaseUpdateAsset, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.UpdateAsset")

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
            request: warehouse.UpdateAssetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.Asset:
            r"""Call the update asset method over HTTP.

            Args:
                request (~.warehouse.UpdateAssetRequest):
                    The request object. Response message for UpdateAsset.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.Asset:
                    An asset is a resource in corpus. It
                represents a media object inside corpus,
                contains metadata and another resource
                annotation. Different feature could be
                applied to the asset to generate
                annotations. User could specified
                annotation related to the target asset.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseUpdateAsset._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_asset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseUpdateAsset,
                    "_BaseUpdateAsset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.UpdateAsset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateAsset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._UpdateAsset._get_response(
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
            resp = warehouse.Asset()
            pb_resp = warehouse.Asset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_asset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_asset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.Asset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.update_asset",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateAsset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCorpus(
        _BaseWarehouseRestTransport._BaseUpdateCorpus, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.UpdateCorpus")

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
            request: warehouse.UpdateCorpusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.Corpus:
            r"""Call the update corpus method over HTTP.

            Args:
                request (~.warehouse.UpdateCorpusRequest):
                    The request object. Request message for UpdateCorpus.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.Corpus:
                    Corpus is a set of video contents for
                management. Within a corpus, videos
                share the same data schema. Search is
                also restricted within a single corpus.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseUpdateCorpus._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_corpus(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseUpdateCorpus,
                    "_BaseUpdateCorpus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.UpdateCorpus",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateCorpus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._UpdateCorpus._get_response(
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
            resp = warehouse.Corpus()
            pb_resp = warehouse.Corpus.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_corpus(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_corpus_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.Corpus.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.update_corpus",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateCorpus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataSchema(
        _BaseWarehouseRestTransport._BaseUpdateDataSchema, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.UpdateDataSchema")

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
            request: warehouse.UpdateDataSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.DataSchema:
            r"""Call the update data schema method over HTTP.

            Args:
                request (~.warehouse.UpdateDataSchemaRequest):
                    The request object. Request message for UpdateDataSchema.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.DataSchema:
                    Data schema indicates how the user
                specified annotation is interpreted in
                the system.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseUpdateDataSchema._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_data_schema(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseUpdateDataSchema,
                    "_BaseUpdateDataSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.UpdateDataSchema",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateDataSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._UpdateDataSchema._get_response(
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
            resp = warehouse.DataSchema()
            pb_resp = warehouse.DataSchema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_data_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.DataSchema.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.update_data_schema",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateDataSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSearchConfig(
        _BaseWarehouseRestTransport._BaseUpdateSearchConfig, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.UpdateSearchConfig")

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
            request: warehouse.UpdateSearchConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> warehouse.SearchConfig:
            r"""Call the update search config method over HTTP.

            Args:
                request (~.warehouse.UpdateSearchConfigRequest):
                    The request object. Request message for
                UpdateSearchConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.warehouse.SearchConfig:
                    SearchConfig stores different
                properties that will affect search
                behaviors and search results.

            """

            http_options = (
                _BaseWarehouseRestTransport._BaseUpdateSearchConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_search_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseUpdateSearchConfig,
                    "_BaseUpdateSearchConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.UpdateSearchConfig",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateSearchConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._UpdateSearchConfig._get_response(
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
            resp = warehouse.SearchConfig()
            pb_resp = warehouse.SearchConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_search_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_search_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = warehouse.SearchConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseClient.update_search_config",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "UpdateSearchConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def clip_asset(
        self,
    ) -> Callable[[warehouse.ClipAssetRequest], warehouse.ClipAssetResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ClipAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_annotation(
        self,
    ) -> Callable[[warehouse.CreateAnnotationRequest], warehouse.Annotation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAnnotation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_asset(self) -> Callable[[warehouse.CreateAssetRequest], warehouse.Asset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_corpus(
        self,
    ) -> Callable[[warehouse.CreateCorpusRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCorpus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_data_schema(
        self,
    ) -> Callable[[warehouse.CreateDataSchemaRequest], warehouse.DataSchema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_search_config(
        self,
    ) -> Callable[[warehouse.CreateSearchConfigRequest], warehouse.SearchConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSearchConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_annotation(
        self,
    ) -> Callable[[warehouse.DeleteAnnotationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAnnotation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_asset(
        self,
    ) -> Callable[[warehouse.DeleteAssetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_corpus(
        self,
    ) -> Callable[[warehouse.DeleteCorpusRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCorpus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_schema(
        self,
    ) -> Callable[[warehouse.DeleteDataSchemaRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_search_config(
        self,
    ) -> Callable[[warehouse.DeleteSearchConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSearchConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_hls_uri(
        self,
    ) -> Callable[[warehouse.GenerateHlsUriRequest], warehouse.GenerateHlsUriResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateHlsUri(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_annotation(
        self,
    ) -> Callable[[warehouse.GetAnnotationRequest], warehouse.Annotation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAnnotation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_asset(self) -> Callable[[warehouse.GetAssetRequest], warehouse.Asset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_corpus(self) -> Callable[[warehouse.GetCorpusRequest], warehouse.Corpus]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCorpus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_schema(
        self,
    ) -> Callable[[warehouse.GetDataSchemaRequest], warehouse.DataSchema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_search_config(
        self,
    ) -> Callable[[warehouse.GetSearchConfigRequest], warehouse.SearchConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSearchConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def ingest_asset(
        self,
    ) -> Callable[[warehouse.IngestAssetRequest], warehouse.IngestAssetResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IngestAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_annotations(
        self,
    ) -> Callable[
        [warehouse.ListAnnotationsRequest], warehouse.ListAnnotationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAnnotations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_assets(
        self,
    ) -> Callable[[warehouse.ListAssetsRequest], warehouse.ListAssetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAssets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_corpora(
        self,
    ) -> Callable[[warehouse.ListCorporaRequest], warehouse.ListCorporaResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCorpora(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_schemas(
        self,
    ) -> Callable[
        [warehouse.ListDataSchemasRequest], warehouse.ListDataSchemasResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataSchemas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_search_configs(
        self,
    ) -> Callable[
        [warehouse.ListSearchConfigsRequest], warehouse.ListSearchConfigsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSearchConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_assets(
        self,
    ) -> Callable[[warehouse.SearchAssetsRequest], warehouse.SearchAssetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchAssets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_annotation(
        self,
    ) -> Callable[[warehouse.UpdateAnnotationRequest], warehouse.Annotation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAnnotation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_asset(self) -> Callable[[warehouse.UpdateAssetRequest], warehouse.Asset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAsset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_corpus(
        self,
    ) -> Callable[[warehouse.UpdateCorpusRequest], warehouse.Corpus]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCorpus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_schema(
        self,
    ) -> Callable[[warehouse.UpdateDataSchemaRequest], warehouse.DataSchema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_search_config(
        self,
    ) -> Callable[[warehouse.UpdateSearchConfigRequest], warehouse.SearchConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSearchConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseWarehouseRestTransport._BaseGetLocation, WarehouseRestStub):
        def __hash__(self):
            return hash("WarehouseRestTransport.GetLocation")

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

            http_options = (
                _BaseWarehouseRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
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
        _BaseWarehouseRestTransport._BaseListLocations, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.ListLocations")

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

            http_options = (
                _BaseWarehouseRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseWarehouseRestTransport._BaseGetIamPolicy, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseWarehouseRestTransport._BaseSetIamPolicy, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseWarehouseRestTransport._BaseTestIamPermissions, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._TestIamPermissions._get_response(
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

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseWarehouseRestTransport._BaseCancelOperation, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.CancelOperation")

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

            http_options = (
                _BaseWarehouseRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseWarehouseRestTransport._BaseDeleteOperation, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.DeleteOperation")

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
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseWarehouseRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseWarehouseRestTransport._BaseGetOperation, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.GetOperation")

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

            http_options = (
                _BaseWarehouseRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
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
        _BaseWarehouseRestTransport._BaseListOperations, WarehouseRestStub
    ):
        def __hash__(self):
            return hash("WarehouseRestTransport.ListOperations")

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

            http_options = (
                _BaseWarehouseRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseWarehouseRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.visionai_v1alpha1.WarehouseClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = WarehouseRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.visionai_v1alpha1.WarehouseAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1alpha1.Warehouse",
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


__all__ = ("WarehouseRestTransport",)
