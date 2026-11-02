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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.apphub_v1._compat import transcode_request
from google.cloud.apphub_v1.types import (
    apphub_service,
    application,
    boundary,
    extended_metadata_schema,
    service,
    service_project_attachment,
    workload,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAppHubRestTransport

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


class AppHubRestInterceptor:
    """Interceptor for AppHub.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AppHubRestTransport.

    .. code-block:: python
        class MyCustomAppHubInterceptor(AppHubRestInterceptor):
            def pre_create_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_service_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_service_project_attachment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_workload(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_workload(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_service_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_service_project_attachment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_workload(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_workload(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_detach_service_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_detach_service_project_attachment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_boundary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_boundary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_discovered_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_discovered_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_discovered_workload(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_discovered_workload(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_extended_metadata_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_extended_metadata_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_service_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_service_project_attachment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_workload(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_workload(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_applications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_applications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_discovered_services(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_discovered_services(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_discovered_workloads(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_discovered_workloads(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_extended_metadata_schemas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_extended_metadata_schemas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_service_project_attachments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_service_project_attachments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_services(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_services(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workloads(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workloads(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_discovered_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_discovered_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_discovered_workload(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_discovered_workload(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_service_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_service_project_attachment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_boundary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_boundary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_workload(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_workload(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AppHubRestTransport(interceptor=MyCustomAppHubInterceptor())
        client = AppHubClient(transport=transport)


    """

    def pre_create_application(
        self,
        request: apphub_service.CreateApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.CreateApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_create_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_application

        DEPRECATED. Please use the `post_create_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_create_application` interceptor runs
        before the `post_create_application_with_metadata` interceptor.
        """
        return response

    def post_create_application_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_create_application_with_metadata`
        interceptor in new development instead of the `post_create_application` interceptor.
        When both interceptors are used, this `post_create_application_with_metadata` interceptor runs after the
        `post_create_application` interceptor. The (possibly modified) response returned by
        `post_create_application` will be passed to
        `post_create_application_with_metadata`.
        """
        return response, metadata

    def pre_create_service(
        self,
        request: apphub_service.CreateServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.CreateServiceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_create_service(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_service

        DEPRECATED. Please use the `post_create_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_create_service` interceptor runs
        before the `post_create_service_with_metadata` interceptor.
        """
        return response

    def post_create_service_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_create_service_with_metadata`
        interceptor in new development instead of the `post_create_service` interceptor.
        When both interceptors are used, this `post_create_service_with_metadata` interceptor runs after the
        `post_create_service` interceptor. The (possibly modified) response returned by
        `post_create_service` will be passed to
        `post_create_service_with_metadata`.
        """
        return response, metadata

    def pre_create_service_project_attachment(
        self,
        request: apphub_service.CreateServiceProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.CreateServiceProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_service_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_create_service_project_attachment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_service_project_attachment

        DEPRECATED. Please use the `post_create_service_project_attachment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_create_service_project_attachment` interceptor runs
        before the `post_create_service_project_attachment_with_metadata` interceptor.
        """
        return response

    def post_create_service_project_attachment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_service_project_attachment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_create_service_project_attachment_with_metadata`
        interceptor in new development instead of the `post_create_service_project_attachment` interceptor.
        When both interceptors are used, this `post_create_service_project_attachment_with_metadata` interceptor runs after the
        `post_create_service_project_attachment` interceptor. The (possibly modified) response returned by
        `post_create_service_project_attachment` will be passed to
        `post_create_service_project_attachment_with_metadata`.
        """
        return response, metadata

    def pre_create_workload(
        self,
        request: apphub_service.CreateWorkloadRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.CreateWorkloadRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_workload

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_create_workload(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_workload

        DEPRECATED. Please use the `post_create_workload_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_create_workload` interceptor runs
        before the `post_create_workload_with_metadata` interceptor.
        """
        return response

    def post_create_workload_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_workload

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_create_workload_with_metadata`
        interceptor in new development instead of the `post_create_workload` interceptor.
        When both interceptors are used, this `post_create_workload_with_metadata` interceptor runs after the
        `post_create_workload` interceptor. The (possibly modified) response returned by
        `post_create_workload` will be passed to
        `post_create_workload_with_metadata`.
        """
        return response, metadata

    def pre_delete_application(
        self,
        request: apphub_service.DeleteApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.DeleteApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_delete_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_application

        DEPRECATED. Please use the `post_delete_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_delete_application` interceptor runs
        before the `post_delete_application_with_metadata` interceptor.
        """
        return response

    def post_delete_application_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_delete_application_with_metadata`
        interceptor in new development instead of the `post_delete_application` interceptor.
        When both interceptors are used, this `post_delete_application_with_metadata` interceptor runs after the
        `post_delete_application` interceptor. The (possibly modified) response returned by
        `post_delete_application` will be passed to
        `post_delete_application_with_metadata`.
        """
        return response, metadata

    def pre_delete_service(
        self,
        request: apphub_service.DeleteServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.DeleteServiceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_delete_service(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_service

        DEPRECATED. Please use the `post_delete_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_delete_service` interceptor runs
        before the `post_delete_service_with_metadata` interceptor.
        """
        return response

    def post_delete_service_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_delete_service_with_metadata`
        interceptor in new development instead of the `post_delete_service` interceptor.
        When both interceptors are used, this `post_delete_service_with_metadata` interceptor runs after the
        `post_delete_service` interceptor. The (possibly modified) response returned by
        `post_delete_service` will be passed to
        `post_delete_service_with_metadata`.
        """
        return response, metadata

    def pre_delete_service_project_attachment(
        self,
        request: apphub_service.DeleteServiceProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.DeleteServiceProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_service_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_delete_service_project_attachment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_service_project_attachment

        DEPRECATED. Please use the `post_delete_service_project_attachment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_delete_service_project_attachment` interceptor runs
        before the `post_delete_service_project_attachment_with_metadata` interceptor.
        """
        return response

    def post_delete_service_project_attachment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_service_project_attachment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_delete_service_project_attachment_with_metadata`
        interceptor in new development instead of the `post_delete_service_project_attachment` interceptor.
        When both interceptors are used, this `post_delete_service_project_attachment_with_metadata` interceptor runs after the
        `post_delete_service_project_attachment` interceptor. The (possibly modified) response returned by
        `post_delete_service_project_attachment` will be passed to
        `post_delete_service_project_attachment_with_metadata`.
        """
        return response, metadata

    def pre_delete_workload(
        self,
        request: apphub_service.DeleteWorkloadRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.DeleteWorkloadRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_workload

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_delete_workload(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_workload

        DEPRECATED. Please use the `post_delete_workload_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_delete_workload` interceptor runs
        before the `post_delete_workload_with_metadata` interceptor.
        """
        return response

    def post_delete_workload_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_workload

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_delete_workload_with_metadata`
        interceptor in new development instead of the `post_delete_workload` interceptor.
        When both interceptors are used, this `post_delete_workload_with_metadata` interceptor runs after the
        `post_delete_workload` interceptor. The (possibly modified) response returned by
        `post_delete_workload` will be passed to
        `post_delete_workload_with_metadata`.
        """
        return response, metadata

    def pre_detach_service_project_attachment(
        self,
        request: apphub_service.DetachServiceProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.DetachServiceProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for detach_service_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_detach_service_project_attachment(
        self, response: apphub_service.DetachServiceProjectAttachmentResponse
    ) -> apphub_service.DetachServiceProjectAttachmentResponse:
        """Post-rpc interceptor for detach_service_project_attachment

        DEPRECATED. Please use the `post_detach_service_project_attachment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_detach_service_project_attachment` interceptor runs
        before the `post_detach_service_project_attachment_with_metadata` interceptor.
        """
        return response

    def post_detach_service_project_attachment_with_metadata(
        self,
        response: apphub_service.DetachServiceProjectAttachmentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.DetachServiceProjectAttachmentResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for detach_service_project_attachment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_detach_service_project_attachment_with_metadata`
        interceptor in new development instead of the `post_detach_service_project_attachment` interceptor.
        When both interceptors are used, this `post_detach_service_project_attachment_with_metadata` interceptor runs after the
        `post_detach_service_project_attachment` interceptor. The (possibly modified) response returned by
        `post_detach_service_project_attachment` will be passed to
        `post_detach_service_project_attachment_with_metadata`.
        """
        return response, metadata

    def pre_get_application(
        self,
        request: apphub_service.GetApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.GetApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_application(
        self, response: application.Application
    ) -> application.Application:
        """Post-rpc interceptor for get_application

        DEPRECATED. Please use the `post_get_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_get_application` interceptor runs
        before the `post_get_application_with_metadata` interceptor.
        """
        return response

    def post_get_application_with_metadata(
        self,
        response: application.Application,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[application.Application, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_get_application_with_metadata`
        interceptor in new development instead of the `post_get_application` interceptor.
        When both interceptors are used, this `post_get_application_with_metadata` interceptor runs after the
        `post_get_application` interceptor. The (possibly modified) response returned by
        `post_get_application` will be passed to
        `post_get_application_with_metadata`.
        """
        return response, metadata

    def pre_get_boundary(
        self,
        request: apphub_service.GetBoundaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.GetBoundaryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_boundary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_boundary(self, response: boundary.Boundary) -> boundary.Boundary:
        """Post-rpc interceptor for get_boundary

        DEPRECATED. Please use the `post_get_boundary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_get_boundary` interceptor runs
        before the `post_get_boundary_with_metadata` interceptor.
        """
        return response

    def post_get_boundary_with_metadata(
        self,
        response: boundary.Boundary,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[boundary.Boundary, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_boundary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_get_boundary_with_metadata`
        interceptor in new development instead of the `post_get_boundary` interceptor.
        When both interceptors are used, this `post_get_boundary_with_metadata` interceptor runs after the
        `post_get_boundary` interceptor. The (possibly modified) response returned by
        `post_get_boundary` will be passed to
        `post_get_boundary_with_metadata`.
        """
        return response, metadata

    def pre_get_discovered_service(
        self,
        request: apphub_service.GetDiscoveredServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.GetDiscoveredServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_discovered_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_discovered_service(
        self, response: service.DiscoveredService
    ) -> service.DiscoveredService:
        """Post-rpc interceptor for get_discovered_service

        DEPRECATED. Please use the `post_get_discovered_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_get_discovered_service` interceptor runs
        before the `post_get_discovered_service_with_metadata` interceptor.
        """
        return response

    def post_get_discovered_service_with_metadata(
        self,
        response: service.DiscoveredService,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DiscoveredService, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_discovered_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_get_discovered_service_with_metadata`
        interceptor in new development instead of the `post_get_discovered_service` interceptor.
        When both interceptors are used, this `post_get_discovered_service_with_metadata` interceptor runs after the
        `post_get_discovered_service` interceptor. The (possibly modified) response returned by
        `post_get_discovered_service` will be passed to
        `post_get_discovered_service_with_metadata`.
        """
        return response, metadata

    def pre_get_discovered_workload(
        self,
        request: apphub_service.GetDiscoveredWorkloadRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.GetDiscoveredWorkloadRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_discovered_workload

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_discovered_workload(
        self, response: workload.DiscoveredWorkload
    ) -> workload.DiscoveredWorkload:
        """Post-rpc interceptor for get_discovered_workload

        DEPRECATED. Please use the `post_get_discovered_workload_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_get_discovered_workload` interceptor runs
        before the `post_get_discovered_workload_with_metadata` interceptor.
        """
        return response

    def post_get_discovered_workload_with_metadata(
        self,
        response: workload.DiscoveredWorkload,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[workload.DiscoveredWorkload, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_discovered_workload

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_get_discovered_workload_with_metadata`
        interceptor in new development instead of the `post_get_discovered_workload` interceptor.
        When both interceptors are used, this `post_get_discovered_workload_with_metadata` interceptor runs after the
        `post_get_discovered_workload` interceptor. The (possibly modified) response returned by
        `post_get_discovered_workload` will be passed to
        `post_get_discovered_workload_with_metadata`.
        """
        return response, metadata

    def pre_get_extended_metadata_schema(
        self,
        request: apphub_service.GetExtendedMetadataSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.GetExtendedMetadataSchemaRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_extended_metadata_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_extended_metadata_schema(
        self, response: extended_metadata_schema.ExtendedMetadataSchema
    ) -> extended_metadata_schema.ExtendedMetadataSchema:
        """Post-rpc interceptor for get_extended_metadata_schema

        DEPRECATED. Please use the `post_get_extended_metadata_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_get_extended_metadata_schema` interceptor runs
        before the `post_get_extended_metadata_schema_with_metadata` interceptor.
        """
        return response

    def post_get_extended_metadata_schema_with_metadata(
        self,
        response: extended_metadata_schema.ExtendedMetadataSchema,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extended_metadata_schema.ExtendedMetadataSchema,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_extended_metadata_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_get_extended_metadata_schema_with_metadata`
        interceptor in new development instead of the `post_get_extended_metadata_schema` interceptor.
        When both interceptors are used, this `post_get_extended_metadata_schema_with_metadata` interceptor runs after the
        `post_get_extended_metadata_schema` interceptor. The (possibly modified) response returned by
        `post_get_extended_metadata_schema` will be passed to
        `post_get_extended_metadata_schema_with_metadata`.
        """
        return response, metadata

    def pre_get_service(
        self,
        request: apphub_service.GetServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.GetServiceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_service(self, response: service.Service) -> service.Service:
        """Post-rpc interceptor for get_service

        DEPRECATED. Please use the `post_get_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_get_service` interceptor runs
        before the `post_get_service_with_metadata` interceptor.
        """
        return response

    def post_get_service_with_metadata(
        self,
        response: service.Service,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Service, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_get_service_with_metadata`
        interceptor in new development instead of the `post_get_service` interceptor.
        When both interceptors are used, this `post_get_service_with_metadata` interceptor runs after the
        `post_get_service` interceptor. The (possibly modified) response returned by
        `post_get_service` will be passed to
        `post_get_service_with_metadata`.
        """
        return response, metadata

    def pre_get_service_project_attachment(
        self,
        request: apphub_service.GetServiceProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.GetServiceProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_service_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_service_project_attachment(
        self, response: service_project_attachment.ServiceProjectAttachment
    ) -> service_project_attachment.ServiceProjectAttachment:
        """Post-rpc interceptor for get_service_project_attachment

        DEPRECATED. Please use the `post_get_service_project_attachment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_get_service_project_attachment` interceptor runs
        before the `post_get_service_project_attachment_with_metadata` interceptor.
        """
        return response

    def post_get_service_project_attachment_with_metadata(
        self,
        response: service_project_attachment.ServiceProjectAttachment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_project_attachment.ServiceProjectAttachment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_service_project_attachment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_get_service_project_attachment_with_metadata`
        interceptor in new development instead of the `post_get_service_project_attachment` interceptor.
        When both interceptors are used, this `post_get_service_project_attachment_with_metadata` interceptor runs after the
        `post_get_service_project_attachment` interceptor. The (possibly modified) response returned by
        `post_get_service_project_attachment` will be passed to
        `post_get_service_project_attachment_with_metadata`.
        """
        return response, metadata

    def pre_get_workload(
        self,
        request: apphub_service.GetWorkloadRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.GetWorkloadRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_workload

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_workload(self, response: workload.Workload) -> workload.Workload:
        """Post-rpc interceptor for get_workload

        DEPRECATED. Please use the `post_get_workload_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_get_workload` interceptor runs
        before the `post_get_workload_with_metadata` interceptor.
        """
        return response

    def post_get_workload_with_metadata(
        self,
        response: workload.Workload,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[workload.Workload, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_workload

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_get_workload_with_metadata`
        interceptor in new development instead of the `post_get_workload` interceptor.
        When both interceptors are used, this `post_get_workload_with_metadata` interceptor runs after the
        `post_get_workload` interceptor. The (possibly modified) response returned by
        `post_get_workload` will be passed to
        `post_get_workload_with_metadata`.
        """
        return response, metadata

    def pre_list_applications(
        self,
        request: apphub_service.ListApplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListApplicationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_applications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_applications(
        self, response: apphub_service.ListApplicationsResponse
    ) -> apphub_service.ListApplicationsResponse:
        """Post-rpc interceptor for list_applications

        DEPRECATED. Please use the `post_list_applications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_list_applications` interceptor runs
        before the `post_list_applications_with_metadata` interceptor.
        """
        return response

    def post_list_applications_with_metadata(
        self,
        response: apphub_service.ListApplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListApplicationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_applications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_list_applications_with_metadata`
        interceptor in new development instead of the `post_list_applications` interceptor.
        When both interceptors are used, this `post_list_applications_with_metadata` interceptor runs after the
        `post_list_applications` interceptor. The (possibly modified) response returned by
        `post_list_applications` will be passed to
        `post_list_applications_with_metadata`.
        """
        return response, metadata

    def pre_list_discovered_services(
        self,
        request: apphub_service.ListDiscoveredServicesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListDiscoveredServicesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_discovered_services

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_discovered_services(
        self, response: apphub_service.ListDiscoveredServicesResponse
    ) -> apphub_service.ListDiscoveredServicesResponse:
        """Post-rpc interceptor for list_discovered_services

        DEPRECATED. Please use the `post_list_discovered_services_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_list_discovered_services` interceptor runs
        before the `post_list_discovered_services_with_metadata` interceptor.
        """
        return response

    def post_list_discovered_services_with_metadata(
        self,
        response: apphub_service.ListDiscoveredServicesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListDiscoveredServicesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_discovered_services

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_list_discovered_services_with_metadata`
        interceptor in new development instead of the `post_list_discovered_services` interceptor.
        When both interceptors are used, this `post_list_discovered_services_with_metadata` interceptor runs after the
        `post_list_discovered_services` interceptor. The (possibly modified) response returned by
        `post_list_discovered_services` will be passed to
        `post_list_discovered_services_with_metadata`.
        """
        return response, metadata

    def pre_list_discovered_workloads(
        self,
        request: apphub_service.ListDiscoveredWorkloadsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListDiscoveredWorkloadsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_discovered_workloads

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_discovered_workloads(
        self, response: apphub_service.ListDiscoveredWorkloadsResponse
    ) -> apphub_service.ListDiscoveredWorkloadsResponse:
        """Post-rpc interceptor for list_discovered_workloads

        DEPRECATED. Please use the `post_list_discovered_workloads_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_list_discovered_workloads` interceptor runs
        before the `post_list_discovered_workloads_with_metadata` interceptor.
        """
        return response

    def post_list_discovered_workloads_with_metadata(
        self,
        response: apphub_service.ListDiscoveredWorkloadsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListDiscoveredWorkloadsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_discovered_workloads

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_list_discovered_workloads_with_metadata`
        interceptor in new development instead of the `post_list_discovered_workloads` interceptor.
        When both interceptors are used, this `post_list_discovered_workloads_with_metadata` interceptor runs after the
        `post_list_discovered_workloads` interceptor. The (possibly modified) response returned by
        `post_list_discovered_workloads` will be passed to
        `post_list_discovered_workloads_with_metadata`.
        """
        return response, metadata

    def pre_list_extended_metadata_schemas(
        self,
        request: apphub_service.ListExtendedMetadataSchemasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListExtendedMetadataSchemasRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_extended_metadata_schemas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_extended_metadata_schemas(
        self, response: apphub_service.ListExtendedMetadataSchemasResponse
    ) -> apphub_service.ListExtendedMetadataSchemasResponse:
        """Post-rpc interceptor for list_extended_metadata_schemas

        DEPRECATED. Please use the `post_list_extended_metadata_schemas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_list_extended_metadata_schemas` interceptor runs
        before the `post_list_extended_metadata_schemas_with_metadata` interceptor.
        """
        return response

    def post_list_extended_metadata_schemas_with_metadata(
        self,
        response: apphub_service.ListExtendedMetadataSchemasResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListExtendedMetadataSchemasResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_extended_metadata_schemas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_list_extended_metadata_schemas_with_metadata`
        interceptor in new development instead of the `post_list_extended_metadata_schemas` interceptor.
        When both interceptors are used, this `post_list_extended_metadata_schemas_with_metadata` interceptor runs after the
        `post_list_extended_metadata_schemas` interceptor. The (possibly modified) response returned by
        `post_list_extended_metadata_schemas` will be passed to
        `post_list_extended_metadata_schemas_with_metadata`.
        """
        return response, metadata

    def pre_list_service_project_attachments(
        self,
        request: apphub_service.ListServiceProjectAttachmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListServiceProjectAttachmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_service_project_attachments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_service_project_attachments(
        self, response: apphub_service.ListServiceProjectAttachmentsResponse
    ) -> apphub_service.ListServiceProjectAttachmentsResponse:
        """Post-rpc interceptor for list_service_project_attachments

        DEPRECATED. Please use the `post_list_service_project_attachments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_list_service_project_attachments` interceptor runs
        before the `post_list_service_project_attachments_with_metadata` interceptor.
        """
        return response

    def post_list_service_project_attachments_with_metadata(
        self,
        response: apphub_service.ListServiceProjectAttachmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListServiceProjectAttachmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_service_project_attachments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_list_service_project_attachments_with_metadata`
        interceptor in new development instead of the `post_list_service_project_attachments` interceptor.
        When both interceptors are used, this `post_list_service_project_attachments_with_metadata` interceptor runs after the
        `post_list_service_project_attachments` interceptor. The (possibly modified) response returned by
        `post_list_service_project_attachments` will be passed to
        `post_list_service_project_attachments_with_metadata`.
        """
        return response, metadata

    def pre_list_services(
        self,
        request: apphub_service.ListServicesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListServicesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_services

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_services(
        self, response: apphub_service.ListServicesResponse
    ) -> apphub_service.ListServicesResponse:
        """Post-rpc interceptor for list_services

        DEPRECATED. Please use the `post_list_services_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_list_services` interceptor runs
        before the `post_list_services_with_metadata` interceptor.
        """
        return response

    def post_list_services_with_metadata(
        self,
        response: apphub_service.ListServicesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListServicesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_services

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_list_services_with_metadata`
        interceptor in new development instead of the `post_list_services` interceptor.
        When both interceptors are used, this `post_list_services_with_metadata` interceptor runs after the
        `post_list_services` interceptor. The (possibly modified) response returned by
        `post_list_services` will be passed to
        `post_list_services_with_metadata`.
        """
        return response, metadata

    def pre_list_workloads(
        self,
        request: apphub_service.ListWorkloadsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListWorkloadsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_workloads

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_workloads(
        self, response: apphub_service.ListWorkloadsResponse
    ) -> apphub_service.ListWorkloadsResponse:
        """Post-rpc interceptor for list_workloads

        DEPRECATED. Please use the `post_list_workloads_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_list_workloads` interceptor runs
        before the `post_list_workloads_with_metadata` interceptor.
        """
        return response

    def post_list_workloads_with_metadata(
        self,
        response: apphub_service.ListWorkloadsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.ListWorkloadsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_workloads

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_list_workloads_with_metadata`
        interceptor in new development instead of the `post_list_workloads` interceptor.
        When both interceptors are used, this `post_list_workloads_with_metadata` interceptor runs after the
        `post_list_workloads` interceptor. The (possibly modified) response returned by
        `post_list_workloads` will be passed to
        `post_list_workloads_with_metadata`.
        """
        return response, metadata

    def pre_lookup_discovered_service(
        self,
        request: apphub_service.LookupDiscoveredServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.LookupDiscoveredServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for lookup_discovered_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_lookup_discovered_service(
        self, response: apphub_service.LookupDiscoveredServiceResponse
    ) -> apphub_service.LookupDiscoveredServiceResponse:
        """Post-rpc interceptor for lookup_discovered_service

        DEPRECATED. Please use the `post_lookup_discovered_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_lookup_discovered_service` interceptor runs
        before the `post_lookup_discovered_service_with_metadata` interceptor.
        """
        return response

    def post_lookup_discovered_service_with_metadata(
        self,
        response: apphub_service.LookupDiscoveredServiceResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.LookupDiscoveredServiceResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for lookup_discovered_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_lookup_discovered_service_with_metadata`
        interceptor in new development instead of the `post_lookup_discovered_service` interceptor.
        When both interceptors are used, this `post_lookup_discovered_service_with_metadata` interceptor runs after the
        `post_lookup_discovered_service` interceptor. The (possibly modified) response returned by
        `post_lookup_discovered_service` will be passed to
        `post_lookup_discovered_service_with_metadata`.
        """
        return response, metadata

    def pre_lookup_discovered_workload(
        self,
        request: apphub_service.LookupDiscoveredWorkloadRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.LookupDiscoveredWorkloadRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for lookup_discovered_workload

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_lookup_discovered_workload(
        self, response: apphub_service.LookupDiscoveredWorkloadResponse
    ) -> apphub_service.LookupDiscoveredWorkloadResponse:
        """Post-rpc interceptor for lookup_discovered_workload

        DEPRECATED. Please use the `post_lookup_discovered_workload_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_lookup_discovered_workload` interceptor runs
        before the `post_lookup_discovered_workload_with_metadata` interceptor.
        """
        return response

    def post_lookup_discovered_workload_with_metadata(
        self,
        response: apphub_service.LookupDiscoveredWorkloadResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.LookupDiscoveredWorkloadResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for lookup_discovered_workload

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_lookup_discovered_workload_with_metadata`
        interceptor in new development instead of the `post_lookup_discovered_workload` interceptor.
        When both interceptors are used, this `post_lookup_discovered_workload_with_metadata` interceptor runs after the
        `post_lookup_discovered_workload` interceptor. The (possibly modified) response returned by
        `post_lookup_discovered_workload` will be passed to
        `post_lookup_discovered_workload_with_metadata`.
        """
        return response, metadata

    def pre_lookup_service_project_attachment(
        self,
        request: apphub_service.LookupServiceProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.LookupServiceProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for lookup_service_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_lookup_service_project_attachment(
        self, response: apphub_service.LookupServiceProjectAttachmentResponse
    ) -> apphub_service.LookupServiceProjectAttachmentResponse:
        """Post-rpc interceptor for lookup_service_project_attachment

        DEPRECATED. Please use the `post_lookup_service_project_attachment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_lookup_service_project_attachment` interceptor runs
        before the `post_lookup_service_project_attachment_with_metadata` interceptor.
        """
        return response

    def post_lookup_service_project_attachment_with_metadata(
        self,
        response: apphub_service.LookupServiceProjectAttachmentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.LookupServiceProjectAttachmentResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for lookup_service_project_attachment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_lookup_service_project_attachment_with_metadata`
        interceptor in new development instead of the `post_lookup_service_project_attachment` interceptor.
        When both interceptors are used, this `post_lookup_service_project_attachment_with_metadata` interceptor runs after the
        `post_lookup_service_project_attachment` interceptor. The (possibly modified) response returned by
        `post_lookup_service_project_attachment` will be passed to
        `post_lookup_service_project_attachment_with_metadata`.
        """
        return response, metadata

    def pre_update_application(
        self,
        request: apphub_service.UpdateApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.UpdateApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_update_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_application

        DEPRECATED. Please use the `post_update_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_update_application` interceptor runs
        before the `post_update_application_with_metadata` interceptor.
        """
        return response

    def post_update_application_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_update_application_with_metadata`
        interceptor in new development instead of the `post_update_application` interceptor.
        When both interceptors are used, this `post_update_application_with_metadata` interceptor runs after the
        `post_update_application` interceptor. The (possibly modified) response returned by
        `post_update_application` will be passed to
        `post_update_application_with_metadata`.
        """
        return response, metadata

    def pre_update_boundary(
        self,
        request: apphub_service.UpdateBoundaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.UpdateBoundaryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_boundary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_update_boundary(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_boundary

        DEPRECATED. Please use the `post_update_boundary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_update_boundary` interceptor runs
        before the `post_update_boundary_with_metadata` interceptor.
        """
        return response

    def post_update_boundary_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_boundary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_update_boundary_with_metadata`
        interceptor in new development instead of the `post_update_boundary` interceptor.
        When both interceptors are used, this `post_update_boundary_with_metadata` interceptor runs after the
        `post_update_boundary` interceptor. The (possibly modified) response returned by
        `post_update_boundary` will be passed to
        `post_update_boundary_with_metadata`.
        """
        return response, metadata

    def pre_update_service(
        self,
        request: apphub_service.UpdateServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.UpdateServiceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_update_service(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_service

        DEPRECATED. Please use the `post_update_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_update_service` interceptor runs
        before the `post_update_service_with_metadata` interceptor.
        """
        return response

    def post_update_service_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_update_service_with_metadata`
        interceptor in new development instead of the `post_update_service` interceptor.
        When both interceptors are used, this `post_update_service_with_metadata` interceptor runs after the
        `post_update_service` interceptor. The (possibly modified) response returned by
        `post_update_service` will be passed to
        `post_update_service_with_metadata`.
        """
        return response, metadata

    def pre_update_workload(
        self,
        request: apphub_service.UpdateWorkloadRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_service.UpdateWorkloadRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_workload

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_update_workload(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_workload

        DEPRECATED. Please use the `post_update_workload_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code. This `post_update_workload` interceptor runs
        before the `post_update_workload_with_metadata` interceptor.
        """
        return response

    def post_update_workload_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_workload

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppHub server but before it is returned to user code.

        We recommend only using this `post_update_workload_with_metadata`
        interceptor in new development instead of the `post_update_workload` interceptor.
        When both interceptors are used, this `post_update_workload_with_metadata` interceptor runs after the
        `post_update_workload` interceptor. The (possibly modified) response returned by
        `post_update_workload` will be passed to
        `post_update_workload_with_metadata`.
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
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
        before they are sent to the AppHub server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the AppHub server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AppHubRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AppHubRestInterceptor


class AppHubRestTransport(_BaseAppHubRestTransport):
    """REST backend synchronous transport for AppHub.

    The App Hub API allows you to manage App Hub resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "apphub.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AppHubRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'apphub.googleapis.com').
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
            interceptor (Optional[AppHubRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AppHubRestInterceptor()
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

    class _CreateApplication(
        _BaseAppHubRestTransport._BaseCreateApplication, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.CreateApplication")

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
            request: apphub_service.CreateApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create application method over HTTP.

            Args:
                request (~.apphub_service.CreateApplicationRequest):
                    The request object. Request for CreateApplication.
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
                _BaseAppHubRestTransport._BaseCreateApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseCreateApplication,
                    "_BaseCreateApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.CreateApplication",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CreateApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._CreateApplication._get_response(
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

            resp = self._interceptor.post_create_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_application_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.create_application",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CreateApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateService(_BaseAppHubRestTransport._BaseCreateService, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.CreateService")

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
            request: apphub_service.CreateServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create service method over HTTP.

            Args:
                request (~.apphub_service.CreateServiceRequest):
                    The request object. Request for CreateService.
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
                _BaseAppHubRestTransport._BaseCreateService._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_service(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseCreateService,
                    "_BaseCreateService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.CreateService",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CreateService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._CreateService._get_response(
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

            resp = self._interceptor.post_create_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_service_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.create_service",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CreateService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateServiceProjectAttachment(
        _BaseAppHubRestTransport._BaseCreateServiceProjectAttachment, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.CreateServiceProjectAttachment")

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
            request: apphub_service.CreateServiceProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create service project
            attachment method over HTTP.

                Args:
                    request (~.apphub_service.CreateServiceProjectAttachmentRequest):
                        The request object. Request for
                    CreateServiceProjectAttachment.
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

            http_options = _BaseAppHubRestTransport._BaseCreateServiceProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_create_service_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseCreateServiceProjectAttachment,
                    "_BaseCreateServiceProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.CreateServiceProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CreateServiceProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppHubRestTransport._CreateServiceProjectAttachment._get_response(
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

            resp = self._interceptor.post_create_service_project_attachment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_service_project_attachment_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.create_service_project_attachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CreateServiceProjectAttachment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWorkload(_BaseAppHubRestTransport._BaseCreateWorkload, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.CreateWorkload")

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
            request: apphub_service.CreateWorkloadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create workload method over HTTP.

            Args:
                request (~.apphub_service.CreateWorkloadRequest):
                    The request object. Request for CreateWorkload.
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
                _BaseAppHubRestTransport._BaseCreateWorkload._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_workload(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseCreateWorkload,
                    "_BaseCreateWorkload__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.CreateWorkload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CreateWorkload",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._CreateWorkload._get_response(
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

            resp = self._interceptor.post_create_workload(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_workload_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.create_workload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CreateWorkload",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteApplication(
        _BaseAppHubRestTransport._BaseDeleteApplication, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.DeleteApplication")

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
            request: apphub_service.DeleteApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete application method over HTTP.

            Args:
                request (~.apphub_service.DeleteApplicationRequest):
                    The request object. Request for DeleteApplication.
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
                _BaseAppHubRestTransport._BaseDeleteApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseDeleteApplication,
                    "_BaseDeleteApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.DeleteApplication",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._DeleteApplication._get_response(
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

            resp = self._interceptor.post_delete_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_application_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.delete_application",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteService(_BaseAppHubRestTransport._BaseDeleteService, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.DeleteService")

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
            request: apphub_service.DeleteServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete service method over HTTP.

            Args:
                request (~.apphub_service.DeleteServiceRequest):
                    The request object. Request for DeleteService.
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
                _BaseAppHubRestTransport._BaseDeleteService._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_service(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseDeleteService,
                    "_BaseDeleteService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.DeleteService",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._DeleteService._get_response(
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

            resp = self._interceptor.post_delete_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_service_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.delete_service",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteServiceProjectAttachment(
        _BaseAppHubRestTransport._BaseDeleteServiceProjectAttachment, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.DeleteServiceProjectAttachment")

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
            request: apphub_service.DeleteServiceProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete service project
            attachment method over HTTP.

                Args:
                    request (~.apphub_service.DeleteServiceProjectAttachmentRequest):
                        The request object. Request for
                    DeleteServiceProjectAttachment.
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

            http_options = _BaseAppHubRestTransport._BaseDeleteServiceProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_delete_service_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseDeleteServiceProjectAttachment,
                    "_BaseDeleteServiceProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.DeleteServiceProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteServiceProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppHubRestTransport._DeleteServiceProjectAttachment._get_response(
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

            resp = self._interceptor.post_delete_service_project_attachment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_service_project_attachment_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.delete_service_project_attachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteServiceProjectAttachment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteWorkload(_BaseAppHubRestTransport._BaseDeleteWorkload, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.DeleteWorkload")

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
            request: apphub_service.DeleteWorkloadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete workload method over HTTP.

            Args:
                request (~.apphub_service.DeleteWorkloadRequest):
                    The request object. Request for DeleteWorkload.
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
                _BaseAppHubRestTransport._BaseDeleteWorkload._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_workload(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseDeleteWorkload,
                    "_BaseDeleteWorkload__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.DeleteWorkload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteWorkload",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._DeleteWorkload._get_response(
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

            resp = self._interceptor.post_delete_workload(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_workload_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.delete_workload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteWorkload",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DetachServiceProjectAttachment(
        _BaseAppHubRestTransport._BaseDetachServiceProjectAttachment, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.DetachServiceProjectAttachment")

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
            request: apphub_service.DetachServiceProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.DetachServiceProjectAttachmentResponse:
            r"""Call the detach service project
            attachment method over HTTP.

                Args:
                    request (~.apphub_service.DetachServiceProjectAttachmentRequest):
                        The request object. Request for
                    DetachServiceProjectAttachment.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.apphub_service.DetachServiceProjectAttachmentResponse:
                        Response for
                    DetachServiceProjectAttachment.

            """

            http_options = _BaseAppHubRestTransport._BaseDetachServiceProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_detach_service_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseDetachServiceProjectAttachment,
                    "_BaseDetachServiceProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.DetachServiceProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DetachServiceProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppHubRestTransport._DetachServiceProjectAttachment._get_response(
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
            resp = apphub_service.DetachServiceProjectAttachmentResponse()
            pb_resp = apphub_service.DetachServiceProjectAttachmentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_detach_service_project_attachment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_detach_service_project_attachment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        apphub_service.DetachServiceProjectAttachmentResponse.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.detach_service_project_attachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DetachServiceProjectAttachment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApplication(_BaseAppHubRestTransport._BaseGetApplication, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.GetApplication")

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
            request: apphub_service.GetApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application.Application:
            r"""Call the get application method over HTTP.

            Args:
                request (~.apphub_service.GetApplicationRequest):
                    The request object. Request for GetApplication.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.application.Application:
                    Application defines the governance
                boundary for App Hub entities that
                perform a logical end-to-end business
                function. App Hub supports application
                level IAM permission to align with
                governance requirements.

            """

            http_options = (
                _BaseAppHubRestTransport._BaseGetApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_application(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetApplication,
                    "_BaseGetApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetApplication",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetApplication._get_response(
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
            resp = application.Application()
            pb_resp = application.Application.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_application_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = application.Application.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.get_application",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBoundary(_BaseAppHubRestTransport._BaseGetBoundary, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.GetBoundary")

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
            request: apphub_service.GetBoundaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> boundary.Boundary:
            r"""Call the get boundary method over HTTP.

            Args:
                request (~.apphub_service.GetBoundaryRequest):
                    The request object. Request message for
                AppHub.GetBoundary.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.boundary.Boundary:
                    Application management boundary.
            """

            http_options = _BaseAppHubRestTransport._BaseGetBoundary._get_http_options()
            request, metadata = self._interceptor.pre_get_boundary(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetBoundary,
                    "_BaseGetBoundary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetBoundary",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetBoundary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetBoundary._get_response(
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
            resp = boundary.Boundary()
            pb_resp = boundary.Boundary.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_boundary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_boundary_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = boundary.Boundary.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.get_boundary",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetBoundary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDiscoveredService(
        _BaseAppHubRestTransport._BaseGetDiscoveredService, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.GetDiscoveredService")

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
            request: apphub_service.GetDiscoveredServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.DiscoveredService:
            r"""Call the get discovered service method over HTTP.

            Args:
                request (~.apphub_service.GetDiscoveredServiceRequest):
                    The request object. Request for GetDiscoveredService.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.DiscoveredService:
                    DiscoveredService is a network or API
                interface that exposes some
                functionality to clients for consumption
                over the network. A discovered service
                can be registered to a App Hub service.

            """

            http_options = (
                _BaseAppHubRestTransport._BaseGetDiscoveredService._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_discovered_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetDiscoveredService,
                    "_BaseGetDiscoveredService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetDiscoveredService",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetDiscoveredService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetDiscoveredService._get_response(
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
            resp = service.DiscoveredService()
            pb_resp = service.DiscoveredService.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_discovered_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_discovered_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.DiscoveredService.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.get_discovered_service",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetDiscoveredService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDiscoveredWorkload(
        _BaseAppHubRestTransport._BaseGetDiscoveredWorkload, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.GetDiscoveredWorkload")

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
            request: apphub_service.GetDiscoveredWorkloadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workload.DiscoveredWorkload:
            r"""Call the get discovered workload method over HTTP.

            Args:
                request (~.apphub_service.GetDiscoveredWorkloadRequest):
                    The request object. Request for GetDiscoveredWorkload.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workload.DiscoveredWorkload:
                    DiscoveredWorkload is a binary
                deployment (such as managed instance
                groups (MIGs) and GKE deployments) that
                performs the smallest logical subset of
                business functionality. A discovered
                workload can be registered to an App Hub
                Workload.

            """

            http_options = (
                _BaseAppHubRestTransport._BaseGetDiscoveredWorkload._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_discovered_workload(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetDiscoveredWorkload,
                    "_BaseGetDiscoveredWorkload__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetDiscoveredWorkload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetDiscoveredWorkload",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetDiscoveredWorkload._get_response(
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
            resp = workload.DiscoveredWorkload()
            pb_resp = workload.DiscoveredWorkload.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_discovered_workload(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_discovered_workload_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = workload.DiscoveredWorkload.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.get_discovered_workload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetDiscoveredWorkload",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetExtendedMetadataSchema(
        _BaseAppHubRestTransport._BaseGetExtendedMetadataSchema, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.GetExtendedMetadataSchema")

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
            request: apphub_service.GetExtendedMetadataSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> extended_metadata_schema.ExtendedMetadataSchema:
            r"""Call the get extended metadata
            schema method over HTTP.

                Args:
                    request (~.apphub_service.GetExtendedMetadataSchemaRequest):
                        The request object. Request for
                    GetExtendedMetadataSchema.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.extended_metadata_schema.ExtendedMetadataSchema:
                        ExtendedMetadataSchema represents a
                    schema for extended metadata of a
                    service or workload.

            """

            http_options = _BaseAppHubRestTransport._BaseGetExtendedMetadataSchema._get_http_options()
            request, metadata = self._interceptor.pre_get_extended_metadata_schema(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetExtendedMetadataSchema,
                    "_BaseGetExtendedMetadataSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetExtendedMetadataSchema",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetExtendedMetadataSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetExtendedMetadataSchema._get_response(
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
            resp = extended_metadata_schema.ExtendedMetadataSchema()
            pb_resp = extended_metadata_schema.ExtendedMetadataSchema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_extended_metadata_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_extended_metadata_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        extended_metadata_schema.ExtendedMetadataSchema.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.get_extended_metadata_schema",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetExtendedMetadataSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetService(_BaseAppHubRestTransport._BaseGetService, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.GetService")

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
            request: apphub_service.GetServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Service:
            r"""Call the get service method over HTTP.

            Args:
                request (~.apphub_service.GetServiceRequest):
                    The request object. Request for GetService.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Service:
                    Service is an App Hub data model that
                contains a discovered service, which
                represents a network or API interface
                that exposes some functionality to
                clients for consumption over the
                network.

            """

            http_options = _BaseAppHubRestTransport._BaseGetService._get_http_options()
            request, metadata = self._interceptor.pre_get_service(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetService,
                    "_BaseGetService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetService",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetService._get_response(
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
            resp = service.Service()
            pb_resp = service.Service.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Service.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.get_service",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetServiceProjectAttachment(
        _BaseAppHubRestTransport._BaseGetServiceProjectAttachment, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.GetServiceProjectAttachment")

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
            request: apphub_service.GetServiceProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service_project_attachment.ServiceProjectAttachment:
            r"""Call the get service project
            attachment method over HTTP.

                Args:
                    request (~.apphub_service.GetServiceProjectAttachmentRequest):
                        The request object. Request for
                    GetServiceProjectAttachment.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service_project_attachment.ServiceProjectAttachment:
                        ServiceProjectAttachment represents
                    an attachment from a service project to
                    a host project. Service projects contain
                    the underlying cloud infrastructure
                    resources, and expose these resources to
                    the host project through a
                    ServiceProjectAttachment. With the
                    attachments, the host project can
                    provide an aggregated view of resources
                    across all service projects.

            """

            http_options = _BaseAppHubRestTransport._BaseGetServiceProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_get_service_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetServiceProjectAttachment,
                    "_BaseGetServiceProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetServiceProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetServiceProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetServiceProjectAttachment._get_response(
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
            resp = service_project_attachment.ServiceProjectAttachment()
            pb_resp = service_project_attachment.ServiceProjectAttachment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_service_project_attachment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_service_project_attachment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service_project_attachment.ServiceProjectAttachment.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.get_service_project_attachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetServiceProjectAttachment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkload(_BaseAppHubRestTransport._BaseGetWorkload, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.GetWorkload")

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
            request: apphub_service.GetWorkloadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> workload.Workload:
            r"""Call the get workload method over HTTP.

            Args:
                request (~.apphub_service.GetWorkloadRequest):
                    The request object. Request for GetWorkload.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.workload.Workload:
                    Workload is an App Hub data model
                that contains a discovered workload,
                which represents a binary deployment
                (such as managed instance groups (MIGs)
                and GKE deployments) that performs the
                smallest logical subset of business
                functionality.

            """

            http_options = _BaseAppHubRestTransport._BaseGetWorkload._get_http_options()
            request, metadata = self._interceptor.pre_get_workload(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetWorkload,
                    "_BaseGetWorkload__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetWorkload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetWorkload",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetWorkload._get_response(
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
            resp = workload.Workload()
            pb_resp = workload.Workload.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_workload(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_workload_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = workload.Workload.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.get_workload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetWorkload",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApplications(
        _BaseAppHubRestTransport._BaseListApplications, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.ListApplications")

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
            request: apphub_service.ListApplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.ListApplicationsResponse:
            r"""Call the list applications method over HTTP.

            Args:
                request (~.apphub_service.ListApplicationsRequest):
                    The request object. Request for ListApplications.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apphub_service.ListApplicationsResponse:
                    Response for ListApplications.
            """

            http_options = (
                _BaseAppHubRestTransport._BaseListApplications._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_applications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListApplications,
                    "_BaseListApplications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListApplications",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListApplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListApplications._get_response(
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
            resp = apphub_service.ListApplicationsResponse()
            pb_resp = apphub_service.ListApplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_applications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_applications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apphub_service.ListApplicationsResponse.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.list_applications",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListApplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDiscoveredServices(
        _BaseAppHubRestTransport._BaseListDiscoveredServices, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.ListDiscoveredServices")

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
            request: apphub_service.ListDiscoveredServicesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.ListDiscoveredServicesResponse:
            r"""Call the list discovered services method over HTTP.

            Args:
                request (~.apphub_service.ListDiscoveredServicesRequest):
                    The request object. Request for ListDiscoveredServices.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apphub_service.ListDiscoveredServicesResponse:
                    Response for ListDiscoveredServices.
            """

            http_options = (
                _BaseAppHubRestTransport._BaseListDiscoveredServices._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_discovered_services(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListDiscoveredServices,
                    "_BaseListDiscoveredServices__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListDiscoveredServices",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListDiscoveredServices",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListDiscoveredServices._get_response(
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
            resp = apphub_service.ListDiscoveredServicesResponse()
            pb_resp = apphub_service.ListDiscoveredServicesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_discovered_services(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_discovered_services_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        apphub_service.ListDiscoveredServicesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.list_discovered_services",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListDiscoveredServices",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDiscoveredWorkloads(
        _BaseAppHubRestTransport._BaseListDiscoveredWorkloads, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.ListDiscoveredWorkloads")

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
            request: apphub_service.ListDiscoveredWorkloadsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.ListDiscoveredWorkloadsResponse:
            r"""Call the list discovered workloads method over HTTP.

            Args:
                request (~.apphub_service.ListDiscoveredWorkloadsRequest):
                    The request object. Request for ListDiscoveredWorkloads.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apphub_service.ListDiscoveredWorkloadsResponse:
                    Response for ListDiscoveredWorkloads.
            """

            http_options = _BaseAppHubRestTransport._BaseListDiscoveredWorkloads._get_http_options()
            request, metadata = self._interceptor.pre_list_discovered_workloads(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListDiscoveredWorkloads,
                    "_BaseListDiscoveredWorkloads__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListDiscoveredWorkloads",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListDiscoveredWorkloads",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListDiscoveredWorkloads._get_response(
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
            resp = apphub_service.ListDiscoveredWorkloadsResponse()
            pb_resp = apphub_service.ListDiscoveredWorkloadsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_discovered_workloads(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_discovered_workloads_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        apphub_service.ListDiscoveredWorkloadsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.list_discovered_workloads",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListDiscoveredWorkloads",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListExtendedMetadataSchemas(
        _BaseAppHubRestTransport._BaseListExtendedMetadataSchemas, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.ListExtendedMetadataSchemas")

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
            request: apphub_service.ListExtendedMetadataSchemasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.ListExtendedMetadataSchemasResponse:
            r"""Call the list extended metadata
            schemas method over HTTP.

                Args:
                    request (~.apphub_service.ListExtendedMetadataSchemasRequest):
                        The request object. Request for
                    ListExtendedMetadataSchemas.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.apphub_service.ListExtendedMetadataSchemasResponse:
                        Response for
                    ListExtendedMetadataSchemas.

            """

            http_options = _BaseAppHubRestTransport._BaseListExtendedMetadataSchemas._get_http_options()
            request, metadata = self._interceptor.pre_list_extended_metadata_schemas(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListExtendedMetadataSchemas,
                    "_BaseListExtendedMetadataSchemas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListExtendedMetadataSchemas",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListExtendedMetadataSchemas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListExtendedMetadataSchemas._get_response(
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
            resp = apphub_service.ListExtendedMetadataSchemasResponse()
            pb_resp = apphub_service.ListExtendedMetadataSchemasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_extended_metadata_schemas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_extended_metadata_schemas_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        apphub_service.ListExtendedMetadataSchemasResponse.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.list_extended_metadata_schemas",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListExtendedMetadataSchemas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServiceProjectAttachments(
        _BaseAppHubRestTransport._BaseListServiceProjectAttachments, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.ListServiceProjectAttachments")

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
            request: apphub_service.ListServiceProjectAttachmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.ListServiceProjectAttachmentsResponse:
            r"""Call the list service project
            attachments method over HTTP.

                Args:
                    request (~.apphub_service.ListServiceProjectAttachmentsRequest):
                        The request object. Request for
                    ListServiceProjectAttachments.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.apphub_service.ListServiceProjectAttachmentsResponse:
                        Response for
                    ListServiceProjectAttachments.

            """

            http_options = _BaseAppHubRestTransport._BaseListServiceProjectAttachments._get_http_options()
            request, metadata = self._interceptor.pre_list_service_project_attachments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListServiceProjectAttachments,
                    "_BaseListServiceProjectAttachments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListServiceProjectAttachments",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListServiceProjectAttachments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListServiceProjectAttachments._get_response(
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
            resp = apphub_service.ListServiceProjectAttachmentsResponse()
            pb_resp = apphub_service.ListServiceProjectAttachmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_service_project_attachments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_service_project_attachments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        apphub_service.ListServiceProjectAttachmentsResponse.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.list_service_project_attachments",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListServiceProjectAttachments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServices(_BaseAppHubRestTransport._BaseListServices, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.ListServices")

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
            request: apphub_service.ListServicesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.ListServicesResponse:
            r"""Call the list services method over HTTP.

            Args:
                request (~.apphub_service.ListServicesRequest):
                    The request object. Request for ListServices.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apphub_service.ListServicesResponse:
                    Response for ListServices.
            """

            http_options = (
                _BaseAppHubRestTransport._BaseListServices._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_services(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListServices,
                    "_BaseListServices__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListServices",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListServices",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListServices._get_response(
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
            resp = apphub_service.ListServicesResponse()
            pb_resp = apphub_service.ListServicesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_services(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_services_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apphub_service.ListServicesResponse.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.list_services",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListServices",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkloads(_BaseAppHubRestTransport._BaseListWorkloads, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.ListWorkloads")

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
            request: apphub_service.ListWorkloadsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.ListWorkloadsResponse:
            r"""Call the list workloads method over HTTP.

            Args:
                request (~.apphub_service.ListWorkloadsRequest):
                    The request object. Request for ListWorkloads.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apphub_service.ListWorkloadsResponse:
                    Response for ListWorkloads.
            """

            http_options = (
                _BaseAppHubRestTransport._BaseListWorkloads._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_workloads(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListWorkloads,
                    "_BaseListWorkloads__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListWorkloads",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListWorkloads",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListWorkloads._get_response(
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
            resp = apphub_service.ListWorkloadsResponse()
            pb_resp = apphub_service.ListWorkloadsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_workloads(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_workloads_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apphub_service.ListWorkloadsResponse.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.list_workloads",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListWorkloads",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupDiscoveredService(
        _BaseAppHubRestTransport._BaseLookupDiscoveredService, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.LookupDiscoveredService")

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
            request: apphub_service.LookupDiscoveredServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.LookupDiscoveredServiceResponse:
            r"""Call the lookup discovered service method over HTTP.

            Args:
                request (~.apphub_service.LookupDiscoveredServiceRequest):
                    The request object. Request for LookupDiscoveredService.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apphub_service.LookupDiscoveredServiceResponse:
                    Response for LookupDiscoveredService.
            """

            http_options = _BaseAppHubRestTransport._BaseLookupDiscoveredService._get_http_options()
            request, metadata = self._interceptor.pre_lookup_discovered_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseLookupDiscoveredService,
                    "_BaseLookupDiscoveredService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.LookupDiscoveredService",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "LookupDiscoveredService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._LookupDiscoveredService._get_response(
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
            resp = apphub_service.LookupDiscoveredServiceResponse()
            pb_resp = apphub_service.LookupDiscoveredServiceResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_discovered_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lookup_discovered_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        apphub_service.LookupDiscoveredServiceResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apphub_v1.AppHubClient.lookup_discovered_service",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "LookupDiscoveredService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupDiscoveredWorkload(
        _BaseAppHubRestTransport._BaseLookupDiscoveredWorkload, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.LookupDiscoveredWorkload")

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
            request: apphub_service.LookupDiscoveredWorkloadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.LookupDiscoveredWorkloadResponse:
            r"""Call the lookup discovered
            workload method over HTTP.

                Args:
                    request (~.apphub_service.LookupDiscoveredWorkloadRequest):
                        The request object. Request for LookupDiscoveredWorkload.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.apphub_service.LookupDiscoveredWorkloadResponse:
                        Response for
                    LookupDiscoveredWorkload.

            """

            http_options = _BaseAppHubRestTransport._BaseLookupDiscoveredWorkload._get_http_options()
            request, metadata = self._interceptor.pre_lookup_discovered_workload(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseLookupDiscoveredWorkload,
                    "_BaseLookupDiscoveredWorkload__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.LookupDiscoveredWorkload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "LookupDiscoveredWorkload",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._LookupDiscoveredWorkload._get_response(
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
            resp = apphub_service.LookupDiscoveredWorkloadResponse()
            pb_resp = apphub_service.LookupDiscoveredWorkloadResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_discovered_workload(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lookup_discovered_workload_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        apphub_service.LookupDiscoveredWorkloadResponse.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.lookup_discovered_workload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "LookupDiscoveredWorkload",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupServiceProjectAttachment(
        _BaseAppHubRestTransport._BaseLookupServiceProjectAttachment, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.LookupServiceProjectAttachment")

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
            request: apphub_service.LookupServiceProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apphub_service.LookupServiceProjectAttachmentResponse:
            r"""Call the lookup service project
            attachment method over HTTP.

                Args:
                    request (~.apphub_service.LookupServiceProjectAttachmentRequest):
                        The request object. Request for
                    LookupServiceProjectAttachment.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.apphub_service.LookupServiceProjectAttachmentResponse:
                        Response for
                    LookupServiceProjectAttachment.

            """

            http_options = _BaseAppHubRestTransport._BaseLookupServiceProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_lookup_service_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseLookupServiceProjectAttachment,
                    "_BaseLookupServiceProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.LookupServiceProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "LookupServiceProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppHubRestTransport._LookupServiceProjectAttachment._get_response(
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
            resp = apphub_service.LookupServiceProjectAttachmentResponse()
            pb_resp = apphub_service.LookupServiceProjectAttachmentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_service_project_attachment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_lookup_service_project_attachment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        apphub_service.LookupServiceProjectAttachmentResponse.to_json(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.lookup_service_project_attachment",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "LookupServiceProjectAttachment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApplication(
        _BaseAppHubRestTransport._BaseUpdateApplication, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.UpdateApplication")

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
            request: apphub_service.UpdateApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update application method over HTTP.

            Args:
                request (~.apphub_service.UpdateApplicationRequest):
                    The request object. Request for UpdateApplication.
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
                _BaseAppHubRestTransport._BaseUpdateApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseUpdateApplication,
                    "_BaseUpdateApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.UpdateApplication",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "UpdateApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._UpdateApplication._get_response(
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

            resp = self._interceptor.post_update_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_application_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.update_application",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "UpdateApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBoundary(_BaseAppHubRestTransport._BaseUpdateBoundary, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.UpdateBoundary")

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
            request: apphub_service.UpdateBoundaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update boundary method over HTTP.

            Args:
                request (~.apphub_service.UpdateBoundaryRequest):
                    The request object. Request message for
                AppHub.UpdateBoundary.
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
                _BaseAppHubRestTransport._BaseUpdateBoundary._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_boundary(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseUpdateBoundary,
                    "_BaseUpdateBoundary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.UpdateBoundary",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "UpdateBoundary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._UpdateBoundary._get_response(
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

            resp = self._interceptor.post_update_boundary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_boundary_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.update_boundary",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "UpdateBoundary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateService(_BaseAppHubRestTransport._BaseUpdateService, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.UpdateService")

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
            request: apphub_service.UpdateServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update service method over HTTP.

            Args:
                request (~.apphub_service.UpdateServiceRequest):
                    The request object. Request for UpdateService.
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
                _BaseAppHubRestTransport._BaseUpdateService._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_service(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseUpdateService,
                    "_BaseUpdateService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.UpdateService",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "UpdateService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._UpdateService._get_response(
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

            resp = self._interceptor.post_update_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_service_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.update_service",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "UpdateService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateWorkload(_BaseAppHubRestTransport._BaseUpdateWorkload, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.UpdateWorkload")

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
            request: apphub_service.UpdateWorkloadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update workload method over HTTP.

            Args:
                request (~.apphub_service.UpdateWorkloadRequest):
                    The request object. Request for UpdateWorkload.
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
                _BaseAppHubRestTransport._BaseUpdateWorkload._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_workload(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseUpdateWorkload,
                    "_BaseUpdateWorkload__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.UpdateWorkload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "UpdateWorkload",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._UpdateWorkload._get_response(
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

            resp = self._interceptor.post_update_workload(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_workload_with_metadata(
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
                    "Received response for google.cloud.apphub_v1.AppHubClient.update_workload",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "UpdateWorkload",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_application(
        self,
    ) -> Callable[[apphub_service.CreateApplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_service(
        self,
    ) -> Callable[[apphub_service.CreateServiceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.CreateServiceProjectAttachmentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateServiceProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_workload(
        self,
    ) -> Callable[[apphub_service.CreateWorkloadRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWorkload(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_application(
        self,
    ) -> Callable[[apphub_service.DeleteApplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_service(
        self,
    ) -> Callable[[apphub_service.DeleteServiceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.DeleteServiceProjectAttachmentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteServiceProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_workload(
        self,
    ) -> Callable[[apphub_service.DeleteWorkloadRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWorkload(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def detach_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.DetachServiceProjectAttachmentRequest],
        apphub_service.DetachServiceProjectAttachmentResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DetachServiceProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_application(
        self,
    ) -> Callable[[apphub_service.GetApplicationRequest], application.Application]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_boundary(
        self,
    ) -> Callable[[apphub_service.GetBoundaryRequest], boundary.Boundary]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBoundary(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_discovered_service(
        self,
    ) -> Callable[
        [apphub_service.GetDiscoveredServiceRequest], service.DiscoveredService
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDiscoveredService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_discovered_workload(
        self,
    ) -> Callable[
        [apphub_service.GetDiscoveredWorkloadRequest], workload.DiscoveredWorkload
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDiscoveredWorkload(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_extended_metadata_schema(
        self,
    ) -> Callable[
        [apphub_service.GetExtendedMetadataSchemaRequest],
        extended_metadata_schema.ExtendedMetadataSchema,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetExtendedMetadataSchema(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_service(
        self,
    ) -> Callable[[apphub_service.GetServiceRequest], service.Service]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.GetServiceProjectAttachmentRequest],
        service_project_attachment.ServiceProjectAttachment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetServiceProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_workload(
        self,
    ) -> Callable[[apphub_service.GetWorkloadRequest], workload.Workload]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkload(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_applications(
        self,
    ) -> Callable[
        [apphub_service.ListApplicationsRequest],
        apphub_service.ListApplicationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApplications(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_discovered_services(
        self,
    ) -> Callable[
        [apphub_service.ListDiscoveredServicesRequest],
        apphub_service.ListDiscoveredServicesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDiscoveredServices(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_discovered_workloads(
        self,
    ) -> Callable[
        [apphub_service.ListDiscoveredWorkloadsRequest],
        apphub_service.ListDiscoveredWorkloadsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDiscoveredWorkloads(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_extended_metadata_schemas(
        self,
    ) -> Callable[
        [apphub_service.ListExtendedMetadataSchemasRequest],
        apphub_service.ListExtendedMetadataSchemasResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExtendedMetadataSchemas(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_service_project_attachments(
        self,
    ) -> Callable[
        [apphub_service.ListServiceProjectAttachmentsRequest],
        apphub_service.ListServiceProjectAttachmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServiceProjectAttachments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_services(
        self,
    ) -> Callable[
        [apphub_service.ListServicesRequest], apphub_service.ListServicesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServices(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_workloads(
        self,
    ) -> Callable[
        [apphub_service.ListWorkloadsRequest], apphub_service.ListWorkloadsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkloads(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lookup_discovered_service(
        self,
    ) -> Callable[
        [apphub_service.LookupDiscoveredServiceRequest],
        apphub_service.LookupDiscoveredServiceResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupDiscoveredService(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def lookup_discovered_workload(
        self,
    ) -> Callable[
        [apphub_service.LookupDiscoveredWorkloadRequest],
        apphub_service.LookupDiscoveredWorkloadResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupDiscoveredWorkload(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def lookup_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.LookupServiceProjectAttachmentRequest],
        apphub_service.LookupServiceProjectAttachmentResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupServiceProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_application(
        self,
    ) -> Callable[[apphub_service.UpdateApplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_boundary(
        self,
    ) -> Callable[[apphub_service.UpdateBoundaryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBoundary(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_service(
        self,
    ) -> Callable[[apphub_service.UpdateServiceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_workload(
        self,
    ) -> Callable[[apphub_service.UpdateWorkloadRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateWorkload(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseAppHubRestTransport._BaseGetLocation, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.GetLocation")

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

            http_options = _BaseAppHubRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.apphub_v1.AppHubAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(_BaseAppHubRestTransport._BaseListLocations, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.ListLocations")

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
                _BaseAppHubRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.apphub_v1.AppHubAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(_BaseAppHubRestTransport._BaseGetIamPolicy, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.GetIamPolicy")

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
                _BaseAppHubRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.apphub_v1.AppHubAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(_BaseAppHubRestTransport._BaseSetIamPolicy, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.SetIamPolicy")

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
                _BaseAppHubRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.apphub_v1.AppHubAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
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
        _BaseAppHubRestTransport._BaseTestIamPermissions, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.TestIamPermissions")

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
                _BaseAppHubRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.apphub_v1.AppHubAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
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
        _BaseAppHubRestTransport._BaseCancelOperation, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.CancelOperation")

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
                _BaseAppHubRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._CancelOperation._get_response(
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
        _BaseAppHubRestTransport._BaseDeleteOperation, AppHubRestStub
    ):
        def __hash__(self):
            return hash("AppHubRestTransport.DeleteOperation")

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
                _BaseAppHubRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(_BaseAppHubRestTransport._BaseGetOperation, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.GetOperation")

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
                _BaseAppHubRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.apphub_v1.AppHubAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(_BaseAppHubRestTransport._BaseListOperations, AppHubRestStub):
        def __hash__(self):
            return hash("AppHubRestTransport.ListOperations")

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
                _BaseAppHubRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppHubRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.apphub_v1.AppHubClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppHubRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.apphub_v1.AppHubAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.apphub.v1.AppHub",
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


__all__ = ("AppHubRestTransport",)
