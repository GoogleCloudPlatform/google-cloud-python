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

from google.cloud.rapidmigrationassessment_v1._compat import transcode_request
from google.cloud.rapidmigrationassessment_v1.types import (
    api_entities,
    rapidmigrationassessment,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseRapidMigrationAssessmentRestTransport

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


class RapidMigrationAssessmentRestInterceptor:
    """Interceptor for RapidMigrationAssessment.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the RapidMigrationAssessmentRestTransport.

    .. code-block:: python
        class MyCustomRapidMigrationAssessmentInterceptor(RapidMigrationAssessmentRestInterceptor):
            def pre_create_annotation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_annotation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_collector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_collector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_collector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_collector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_annotation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_annotation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_collector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_collector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_collectors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_collectors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_pause_collector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_pause_collector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_register_collector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_register_collector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resume_collector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resume_collector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_collector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_collector(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = RapidMigrationAssessmentRestTransport(interceptor=MyCustomRapidMigrationAssessmentInterceptor())
        client = RapidMigrationAssessmentClient(transport=transport)


    """

    def pre_create_annotation(
        self,
        request: rapidmigrationassessment.CreateAnnotationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.CreateAnnotationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_annotation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_create_annotation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_annotation

        DEPRECATED. Please use the `post_create_annotation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_create_annotation` interceptor runs
        before the `post_create_annotation_with_metadata` interceptor.
        """
        return response

    def post_create_annotation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_annotation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_create_annotation_with_metadata`
        interceptor in new development instead of the `post_create_annotation` interceptor.
        When both interceptors are used, this `post_create_annotation_with_metadata` interceptor runs after the
        `post_create_annotation` interceptor. The (possibly modified) response returned by
        `post_create_annotation` will be passed to
        `post_create_annotation_with_metadata`.
        """
        return response, metadata

    def pre_create_collector(
        self,
        request: rapidmigrationassessment.CreateCollectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.CreateCollectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_collector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_create_collector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_collector

        DEPRECATED. Please use the `post_create_collector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_create_collector` interceptor runs
        before the `post_create_collector_with_metadata` interceptor.
        """
        return response

    def post_create_collector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_collector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_create_collector_with_metadata`
        interceptor in new development instead of the `post_create_collector` interceptor.
        When both interceptors are used, this `post_create_collector_with_metadata` interceptor runs after the
        `post_create_collector` interceptor. The (possibly modified) response returned by
        `post_create_collector` will be passed to
        `post_create_collector_with_metadata`.
        """
        return response, metadata

    def pre_delete_collector(
        self,
        request: rapidmigrationassessment.DeleteCollectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.DeleteCollectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_collector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_delete_collector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_collector

        DEPRECATED. Please use the `post_delete_collector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_delete_collector` interceptor runs
        before the `post_delete_collector_with_metadata` interceptor.
        """
        return response

    def post_delete_collector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_collector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_delete_collector_with_metadata`
        interceptor in new development instead of the `post_delete_collector` interceptor.
        When both interceptors are used, this `post_delete_collector_with_metadata` interceptor runs after the
        `post_delete_collector` interceptor. The (possibly modified) response returned by
        `post_delete_collector` will be passed to
        `post_delete_collector_with_metadata`.
        """
        return response, metadata

    def pre_get_annotation(
        self,
        request: rapidmigrationassessment.GetAnnotationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.GetAnnotationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_annotation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_get_annotation(
        self, response: api_entities.Annotation
    ) -> api_entities.Annotation:
        """Post-rpc interceptor for get_annotation

        DEPRECATED. Please use the `post_get_annotation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_get_annotation` interceptor runs
        before the `post_get_annotation_with_metadata` interceptor.
        """
        return response

    def post_get_annotation_with_metadata(
        self,
        response: api_entities.Annotation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[api_entities.Annotation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_annotation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_get_annotation_with_metadata`
        interceptor in new development instead of the `post_get_annotation` interceptor.
        When both interceptors are used, this `post_get_annotation_with_metadata` interceptor runs after the
        `post_get_annotation` interceptor. The (possibly modified) response returned by
        `post_get_annotation` will be passed to
        `post_get_annotation_with_metadata`.
        """
        return response, metadata

    def pre_get_collector(
        self,
        request: rapidmigrationassessment.GetCollectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.GetCollectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_collector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_get_collector(
        self, response: api_entities.Collector
    ) -> api_entities.Collector:
        """Post-rpc interceptor for get_collector

        DEPRECATED. Please use the `post_get_collector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_get_collector` interceptor runs
        before the `post_get_collector_with_metadata` interceptor.
        """
        return response

    def post_get_collector_with_metadata(
        self,
        response: api_entities.Collector,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[api_entities.Collector, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_collector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_get_collector_with_metadata`
        interceptor in new development instead of the `post_get_collector` interceptor.
        When both interceptors are used, this `post_get_collector_with_metadata` interceptor runs after the
        `post_get_collector` interceptor. The (possibly modified) response returned by
        `post_get_collector` will be passed to
        `post_get_collector_with_metadata`.
        """
        return response, metadata

    def pre_list_collectors(
        self,
        request: rapidmigrationassessment.ListCollectorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.ListCollectorsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_collectors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_list_collectors(
        self, response: rapidmigrationassessment.ListCollectorsResponse
    ) -> rapidmigrationassessment.ListCollectorsResponse:
        """Post-rpc interceptor for list_collectors

        DEPRECATED. Please use the `post_list_collectors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_list_collectors` interceptor runs
        before the `post_list_collectors_with_metadata` interceptor.
        """
        return response

    def post_list_collectors_with_metadata(
        self,
        response: rapidmigrationassessment.ListCollectorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.ListCollectorsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_collectors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_list_collectors_with_metadata`
        interceptor in new development instead of the `post_list_collectors` interceptor.
        When both interceptors are used, this `post_list_collectors_with_metadata` interceptor runs after the
        `post_list_collectors` interceptor. The (possibly modified) response returned by
        `post_list_collectors` will be passed to
        `post_list_collectors_with_metadata`.
        """
        return response, metadata

    def pre_pause_collector(
        self,
        request: rapidmigrationassessment.PauseCollectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.PauseCollectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for pause_collector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_pause_collector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for pause_collector

        DEPRECATED. Please use the `post_pause_collector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_pause_collector` interceptor runs
        before the `post_pause_collector_with_metadata` interceptor.
        """
        return response

    def post_pause_collector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for pause_collector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_pause_collector_with_metadata`
        interceptor in new development instead of the `post_pause_collector` interceptor.
        When both interceptors are used, this `post_pause_collector_with_metadata` interceptor runs after the
        `post_pause_collector` interceptor. The (possibly modified) response returned by
        `post_pause_collector` will be passed to
        `post_pause_collector_with_metadata`.
        """
        return response, metadata

    def pre_register_collector(
        self,
        request: rapidmigrationassessment.RegisterCollectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.RegisterCollectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for register_collector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_register_collector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for register_collector

        DEPRECATED. Please use the `post_register_collector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_register_collector` interceptor runs
        before the `post_register_collector_with_metadata` interceptor.
        """
        return response

    def post_register_collector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for register_collector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_register_collector_with_metadata`
        interceptor in new development instead of the `post_register_collector` interceptor.
        When both interceptors are used, this `post_register_collector_with_metadata` interceptor runs after the
        `post_register_collector` interceptor. The (possibly modified) response returned by
        `post_register_collector` will be passed to
        `post_register_collector_with_metadata`.
        """
        return response, metadata

    def pre_resume_collector(
        self,
        request: rapidmigrationassessment.ResumeCollectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.ResumeCollectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for resume_collector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_resume_collector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for resume_collector

        DEPRECATED. Please use the `post_resume_collector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_resume_collector` interceptor runs
        before the `post_resume_collector_with_metadata` interceptor.
        """
        return response

    def post_resume_collector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for resume_collector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_resume_collector_with_metadata`
        interceptor in new development instead of the `post_resume_collector` interceptor.
        When both interceptors are used, this `post_resume_collector_with_metadata` interceptor runs after the
        `post_resume_collector` interceptor. The (possibly modified) response returned by
        `post_resume_collector` will be passed to
        `post_resume_collector_with_metadata`.
        """
        return response, metadata

    def pre_update_collector(
        self,
        request: rapidmigrationassessment.UpdateCollectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rapidmigrationassessment.UpdateCollectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_collector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_update_collector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_collector

        DEPRECATED. Please use the `post_update_collector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code. This `post_update_collector` interceptor runs
        before the `post_update_collector_with_metadata` interceptor.
        """
        return response

    def post_update_collector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_collector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RapidMigrationAssessment server but before it is returned to user code.

        We recommend only using this `post_update_collector_with_metadata`
        interceptor in new development instead of the `post_update_collector` interceptor.
        When both interceptors are used, this `post_update_collector_with_metadata` interceptor runs after the
        `post_update_collector` interceptor. The (possibly modified) response returned by
        `post_update_collector` will be passed to
        `post_update_collector_with_metadata`.
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
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
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
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
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
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
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
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
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
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
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
        before they are sent to the RapidMigrationAssessment server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the RapidMigrationAssessment server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class RapidMigrationAssessmentRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: RapidMigrationAssessmentRestInterceptor


class RapidMigrationAssessmentRestTransport(_BaseRapidMigrationAssessmentRestTransport):
    """REST backend synchronous transport for RapidMigrationAssessment.

    Service describing handlers for resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "rapidmigrationassessment.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[RapidMigrationAssessmentRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'rapidmigrationassessment.googleapis.com').
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
            interceptor (Optional[RapidMigrationAssessmentRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or RapidMigrationAssessmentRestInterceptor()
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
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
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

    class _CreateAnnotation(
        _BaseRapidMigrationAssessmentRestTransport._BaseCreateAnnotation,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.CreateAnnotation")

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
            request: rapidmigrationassessment.CreateAnnotationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create annotation method over HTTP.

            Args:
                request (~.rapidmigrationassessment.CreateAnnotationRequest):
                    The request object. Message for creating an AnnotationS.
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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseCreateAnnotation._get_http_options()
            request, metadata = self._interceptor.pre_create_annotation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseCreateAnnotation,
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.CreateAnnotation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "CreateAnnotation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._CreateAnnotation._get_response(
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

            resp = self._interceptor.post_create_annotation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_annotation_with_metadata(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.create_annotation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "CreateAnnotation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCollector(
        _BaseRapidMigrationAssessmentRestTransport._BaseCreateCollector,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.CreateCollector")

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
            request: rapidmigrationassessment.CreateCollectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create collector method over HTTP.

            Args:
                request (~.rapidmigrationassessment.CreateCollectorRequest):
                    The request object. Message for creating a Collector.
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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseCreateCollector._get_http_options()
            request, metadata = self._interceptor.pre_create_collector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseCreateCollector,
                    "_BaseCreateCollector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.CreateCollector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "CreateCollector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._CreateCollector._get_response(
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

            resp = self._interceptor.post_create_collector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_collector_with_metadata(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.create_collector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "CreateCollector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCollector(
        _BaseRapidMigrationAssessmentRestTransport._BaseDeleteCollector,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.DeleteCollector")

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
            request: rapidmigrationassessment.DeleteCollectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete collector method over HTTP.

            Args:
                request (~.rapidmigrationassessment.DeleteCollectorRequest):
                    The request object. Message for deleting a Collector.
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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseDeleteCollector._get_http_options()
            request, metadata = self._interceptor.pre_delete_collector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseDeleteCollector,
                    "_BaseDeleteCollector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.DeleteCollector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "DeleteCollector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._DeleteCollector._get_response(
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

            resp = self._interceptor.post_delete_collector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_collector_with_metadata(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.delete_collector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "DeleteCollector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAnnotation(
        _BaseRapidMigrationAssessmentRestTransport._BaseGetAnnotation,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.GetAnnotation")

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
            request: rapidmigrationassessment.GetAnnotationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> api_entities.Annotation:
            r"""Call the get annotation method over HTTP.

            Args:
                request (~.rapidmigrationassessment.GetAnnotationRequest):
                    The request object. Message for getting a specific
                Annotation
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.api_entities.Annotation:
                    Message describing an Annotation
            """

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseGetAnnotation._get_http_options()
            request, metadata = self._interceptor.pre_get_annotation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseGetAnnotation,
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.GetAnnotation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "GetAnnotation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._GetAnnotation._get_response(
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
            resp = api_entities.Annotation()
            pb_resp = api_entities.Annotation.pb(resp)

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
                    response_payload = api_entities.Annotation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.get_annotation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "GetAnnotation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCollector(
        _BaseRapidMigrationAssessmentRestTransport._BaseGetCollector,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.GetCollector")

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
            request: rapidmigrationassessment.GetCollectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> api_entities.Collector:
            r"""Call the get collector method over HTTP.

            Args:
                request (~.rapidmigrationassessment.GetCollectorRequest):
                    The request object. Message for getting a specific
                Collector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.api_entities.Collector:
                    Message describing Collector object.
            """

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseGetCollector._get_http_options()
            request, metadata = self._interceptor.pre_get_collector(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseGetCollector,
                    "_BaseGetCollector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.GetCollector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "GetCollector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._GetCollector._get_response(
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
            resp = api_entities.Collector()
            pb_resp = api_entities.Collector.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_collector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_collector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = api_entities.Collector.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.get_collector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "GetCollector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCollectors(
        _BaseRapidMigrationAssessmentRestTransport._BaseListCollectors,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.ListCollectors")

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
            request: rapidmigrationassessment.ListCollectorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rapidmigrationassessment.ListCollectorsResponse:
            r"""Call the list collectors method over HTTP.

            Args:
                request (~.rapidmigrationassessment.ListCollectorsRequest):
                    The request object. Message for requesting list of
                Collectors.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rapidmigrationassessment.ListCollectorsResponse:
                    Message for response to listing
                Collectors.

            """

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseListCollectors._get_http_options()
            request, metadata = self._interceptor.pre_list_collectors(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseListCollectors,
                    "_BaseListCollectors__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.ListCollectors",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "ListCollectors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._ListCollectors._get_response(
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
            resp = rapidmigrationassessment.ListCollectorsResponse()
            pb_resp = rapidmigrationassessment.ListCollectorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_collectors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_collectors_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        rapidmigrationassessment.ListCollectorsResponse.to_json(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.list_collectors",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "ListCollectors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PauseCollector(
        _BaseRapidMigrationAssessmentRestTransport._BasePauseCollector,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.PauseCollector")

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
            request: rapidmigrationassessment.PauseCollectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the pause collector method over HTTP.

            Args:
                request (~.rapidmigrationassessment.PauseCollectorRequest):
                    The request object. Message for pausing a Collector.
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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BasePauseCollector._get_http_options()
            request, metadata = self._interceptor.pre_pause_collector(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BasePauseCollector,
                    "_BasePauseCollector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.PauseCollector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "PauseCollector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._PauseCollector._get_response(
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

            resp = self._interceptor.post_pause_collector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_pause_collector_with_metadata(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.pause_collector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "PauseCollector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RegisterCollector(
        _BaseRapidMigrationAssessmentRestTransport._BaseRegisterCollector,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.RegisterCollector")

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
            request: rapidmigrationassessment.RegisterCollectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the register collector method over HTTP.

            Args:
                request (~.rapidmigrationassessment.RegisterCollectorRequest):
                    The request object. Message for registering a Collector.
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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseRegisterCollector._get_http_options()
            request, metadata = self._interceptor.pre_register_collector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseRegisterCollector,
                    "_BaseRegisterCollector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.RegisterCollector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "RegisterCollector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._RegisterCollector._get_response(
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

            resp = self._interceptor.post_register_collector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_register_collector_with_metadata(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.register_collector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "RegisterCollector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResumeCollector(
        _BaseRapidMigrationAssessmentRestTransport._BaseResumeCollector,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.ResumeCollector")

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
            request: rapidmigrationassessment.ResumeCollectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the resume collector method over HTTP.

            Args:
                request (~.rapidmigrationassessment.ResumeCollectorRequest):
                    The request object. Message for resuming a Collector.
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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseResumeCollector._get_http_options()
            request, metadata = self._interceptor.pre_resume_collector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseResumeCollector,
                    "_BaseResumeCollector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.ResumeCollector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "ResumeCollector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._ResumeCollector._get_response(
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

            resp = self._interceptor.post_resume_collector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resume_collector_with_metadata(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.resume_collector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "ResumeCollector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCollector(
        _BaseRapidMigrationAssessmentRestTransport._BaseUpdateCollector,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.UpdateCollector")

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
            request: rapidmigrationassessment.UpdateCollectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update collector method over HTTP.

            Args:
                request (~.rapidmigrationassessment.UpdateCollectorRequest):
                    The request object. Message for updating a Collector.
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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseUpdateCollector._get_http_options()
            request, metadata = self._interceptor.pre_update_collector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseUpdateCollector,
                    "_BaseUpdateCollector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.UpdateCollector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "UpdateCollector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._UpdateCollector._get_response(
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

            resp = self._interceptor.post_update_collector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_collector_with_metadata(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.update_collector",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "UpdateCollector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_annotation(
        self,
    ) -> Callable[
        [rapidmigrationassessment.CreateAnnotationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAnnotation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_collector(
        self,
    ) -> Callable[
        [rapidmigrationassessment.CreateCollectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCollector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_collector(
        self,
    ) -> Callable[
        [rapidmigrationassessment.DeleteCollectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCollector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_annotation(
        self,
    ) -> Callable[
        [rapidmigrationassessment.GetAnnotationRequest], api_entities.Annotation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAnnotation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_collector(
        self,
    ) -> Callable[
        [rapidmigrationassessment.GetCollectorRequest], api_entities.Collector
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCollector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_collectors(
        self,
    ) -> Callable[
        [rapidmigrationassessment.ListCollectorsRequest],
        rapidmigrationassessment.ListCollectorsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCollectors(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def pause_collector(
        self,
    ) -> Callable[
        [rapidmigrationassessment.PauseCollectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PauseCollector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def register_collector(
        self,
    ) -> Callable[
        [rapidmigrationassessment.RegisterCollectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RegisterCollector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resume_collector(
        self,
    ) -> Callable[
        [rapidmigrationassessment.ResumeCollectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResumeCollector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_collector(
        self,
    ) -> Callable[
        [rapidmigrationassessment.UpdateCollectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCollector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseRapidMigrationAssessmentRestTransport._BaseGetLocation,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.GetLocation")

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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RapidMigrationAssessmentRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
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
        _BaseRapidMigrationAssessmentRestTransport._BaseListLocations,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.ListLocations")

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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
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
        _BaseRapidMigrationAssessmentRestTransport._BaseCancelOperation,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.CancelOperation")

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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseRapidMigrationAssessmentRestTransport._BaseDeleteOperation,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.DeleteOperation")

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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseRapidMigrationAssessmentRestTransport._BaseGetOperation,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.GetOperation")

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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
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
        _BaseRapidMigrationAssessmentRestTransport._BaseListOperations,
        RapidMigrationAssessmentRestStub,
    ):
        def __hash__(self):
            return hash("RapidMigrationAssessmentRestTransport.ListOperations")

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

            http_options = _BaseRapidMigrationAssessmentRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRapidMigrationAssessmentRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RapidMigrationAssessmentRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.rapidmigrationassessment_v1.RapidMigrationAssessmentAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment",
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


__all__ = ("RapidMigrationAssessmentRestTransport",)
