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

from google.cloud.visionai_v1._compat import transcode_request
from google.cloud.visionai_v1.types import platform

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAppPlatformRestTransport

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


class AppPlatformRestInterceptor:
    """Interceptor for AppPlatform.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AppPlatformRestTransport.

    .. code-block:: python
        class MyCustomAppPlatformInterceptor(AppPlatformRestInterceptor):
            def pre_add_application_stream_input(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_application_stream_input(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_application_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_application_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_draft(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_draft(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_application_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_application_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_draft(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_draft(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deploy_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deploy_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_draft(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_draft(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_applications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_applications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_drafts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_drafts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_prebuilt_processors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_prebuilt_processors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_processors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_processors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_application_stream_input(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_application_stream_input(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undeploy_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undeploy_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_application_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_application_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_application_stream_input(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_application_stream_input(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_draft(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_draft(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_processor(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_processor(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AppPlatformRestTransport(interceptor=MyCustomAppPlatformInterceptor())
        client = AppPlatformClient(transport=transport)


    """

    def pre_add_application_stream_input(
        self,
        request: platform.AddApplicationStreamInputRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.AddApplicationStreamInputRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_application_stream_input

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_add_application_stream_input(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for add_application_stream_input

        DEPRECATED. Please use the `post_add_application_stream_input_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_add_application_stream_input` interceptor runs
        before the `post_add_application_stream_input_with_metadata` interceptor.
        """
        return response

    def post_add_application_stream_input_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_application_stream_input

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_add_application_stream_input_with_metadata`
        interceptor in new development instead of the `post_add_application_stream_input` interceptor.
        When both interceptors are used, this `post_add_application_stream_input_with_metadata` interceptor runs after the
        `post_add_application_stream_input` interceptor. The (possibly modified) response returned by
        `post_add_application_stream_input` will be passed to
        `post_add_application_stream_input_with_metadata`.
        """
        return response, metadata

    def pre_create_application(
        self,
        request: platform.CreateApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.CreateApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_create_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_application

        DEPRECATED. Please use the `post_create_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
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
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_create_application_with_metadata`
        interceptor in new development instead of the `post_create_application` interceptor.
        When both interceptors are used, this `post_create_application_with_metadata` interceptor runs after the
        `post_create_application` interceptor. The (possibly modified) response returned by
        `post_create_application` will be passed to
        `post_create_application_with_metadata`.
        """
        return response, metadata

    def pre_create_application_instances(
        self,
        request: platform.CreateApplicationInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.CreateApplicationInstancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_application_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_create_application_instances(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_application_instances

        DEPRECATED. Please use the `post_create_application_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_create_application_instances` interceptor runs
        before the `post_create_application_instances_with_metadata` interceptor.
        """
        return response

    def post_create_application_instances_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_application_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_create_application_instances_with_metadata`
        interceptor in new development instead of the `post_create_application_instances` interceptor.
        When both interceptors are used, this `post_create_application_instances_with_metadata` interceptor runs after the
        `post_create_application_instances` interceptor. The (possibly modified) response returned by
        `post_create_application_instances` will be passed to
        `post_create_application_instances_with_metadata`.
        """
        return response, metadata

    def pre_create_draft(
        self,
        request: platform.CreateDraftRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.CreateDraftRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_draft

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_create_draft(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_draft

        DEPRECATED. Please use the `post_create_draft_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_create_draft` interceptor runs
        before the `post_create_draft_with_metadata` interceptor.
        """
        return response

    def post_create_draft_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_draft

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_create_draft_with_metadata`
        interceptor in new development instead of the `post_create_draft` interceptor.
        When both interceptors are used, this `post_create_draft_with_metadata` interceptor runs after the
        `post_create_draft` interceptor. The (possibly modified) response returned by
        `post_create_draft` will be passed to
        `post_create_draft_with_metadata`.
        """
        return response, metadata

    def pre_create_processor(
        self,
        request: platform.CreateProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.CreateProcessorRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_create_processor(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_processor

        DEPRECATED. Please use the `post_create_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_create_processor` interceptor runs
        before the `post_create_processor_with_metadata` interceptor.
        """
        return response

    def post_create_processor_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_processor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_create_processor_with_metadata`
        interceptor in new development instead of the `post_create_processor` interceptor.
        When both interceptors are used, this `post_create_processor_with_metadata` interceptor runs after the
        `post_create_processor` interceptor. The (possibly modified) response returned by
        `post_create_processor` will be passed to
        `post_create_processor_with_metadata`.
        """
        return response, metadata

    def pre_delete_application(
        self,
        request: platform.DeleteApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.DeleteApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_delete_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_application

        DEPRECATED. Please use the `post_delete_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
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
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_delete_application_with_metadata`
        interceptor in new development instead of the `post_delete_application` interceptor.
        When both interceptors are used, this `post_delete_application_with_metadata` interceptor runs after the
        `post_delete_application` interceptor. The (possibly modified) response returned by
        `post_delete_application` will be passed to
        `post_delete_application_with_metadata`.
        """
        return response, metadata

    def pre_delete_application_instances(
        self,
        request: platform.DeleteApplicationInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.DeleteApplicationInstancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_application_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_delete_application_instances(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_application_instances

        DEPRECATED. Please use the `post_delete_application_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_delete_application_instances` interceptor runs
        before the `post_delete_application_instances_with_metadata` interceptor.
        """
        return response

    def post_delete_application_instances_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_application_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_delete_application_instances_with_metadata`
        interceptor in new development instead of the `post_delete_application_instances` interceptor.
        When both interceptors are used, this `post_delete_application_instances_with_metadata` interceptor runs after the
        `post_delete_application_instances` interceptor. The (possibly modified) response returned by
        `post_delete_application_instances` will be passed to
        `post_delete_application_instances_with_metadata`.
        """
        return response, metadata

    def pre_delete_draft(
        self,
        request: platform.DeleteDraftRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.DeleteDraftRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_draft

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_delete_draft(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_draft

        DEPRECATED. Please use the `post_delete_draft_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_delete_draft` interceptor runs
        before the `post_delete_draft_with_metadata` interceptor.
        """
        return response

    def post_delete_draft_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_draft

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_delete_draft_with_metadata`
        interceptor in new development instead of the `post_delete_draft` interceptor.
        When both interceptors are used, this `post_delete_draft_with_metadata` interceptor runs after the
        `post_delete_draft` interceptor. The (possibly modified) response returned by
        `post_delete_draft` will be passed to
        `post_delete_draft_with_metadata`.
        """
        return response, metadata

    def pre_delete_processor(
        self,
        request: platform.DeleteProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.DeleteProcessorRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_delete_processor(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_processor

        DEPRECATED. Please use the `post_delete_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
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
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_delete_processor_with_metadata`
        interceptor in new development instead of the `post_delete_processor` interceptor.
        When both interceptors are used, this `post_delete_processor_with_metadata` interceptor runs after the
        `post_delete_processor` interceptor. The (possibly modified) response returned by
        `post_delete_processor` will be passed to
        `post_delete_processor_with_metadata`.
        """
        return response, metadata

    def pre_deploy_application(
        self,
        request: platform.DeployApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.DeployApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for deploy_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_deploy_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for deploy_application

        DEPRECATED. Please use the `post_deploy_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_deploy_application` interceptor runs
        before the `post_deploy_application_with_metadata` interceptor.
        """
        return response

    def post_deploy_application_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deploy_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_deploy_application_with_metadata`
        interceptor in new development instead of the `post_deploy_application` interceptor.
        When both interceptors are used, this `post_deploy_application_with_metadata` interceptor runs after the
        `post_deploy_application` interceptor. The (possibly modified) response returned by
        `post_deploy_application` will be passed to
        `post_deploy_application_with_metadata`.
        """
        return response, metadata

    def pre_get_application(
        self,
        request: platform.GetApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.GetApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_get_application(
        self, response: platform.Application
    ) -> platform.Application:
        """Post-rpc interceptor for get_application

        DEPRECATED. Please use the `post_get_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_get_application` interceptor runs
        before the `post_get_application_with_metadata` interceptor.
        """
        return response

    def post_get_application_with_metadata(
        self,
        response: platform.Application,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.Application, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_get_application_with_metadata`
        interceptor in new development instead of the `post_get_application` interceptor.
        When both interceptors are used, this `post_get_application_with_metadata` interceptor runs after the
        `post_get_application` interceptor. The (possibly modified) response returned by
        `post_get_application` will be passed to
        `post_get_application_with_metadata`.
        """
        return response, metadata

    def pre_get_draft(
        self,
        request: platform.GetDraftRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.GetDraftRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_draft

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_get_draft(self, response: platform.Draft) -> platform.Draft:
        """Post-rpc interceptor for get_draft

        DEPRECATED. Please use the `post_get_draft_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_get_draft` interceptor runs
        before the `post_get_draft_with_metadata` interceptor.
        """
        return response

    def post_get_draft_with_metadata(
        self,
        response: platform.Draft,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.Draft, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_draft

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_get_draft_with_metadata`
        interceptor in new development instead of the `post_get_draft` interceptor.
        When both interceptors are used, this `post_get_draft_with_metadata` interceptor runs after the
        `post_get_draft` interceptor. The (possibly modified) response returned by
        `post_get_draft` will be passed to
        `post_get_draft_with_metadata`.
        """
        return response, metadata

    def pre_get_instance(
        self,
        request: platform.GetInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.GetInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_get_instance(self, response: platform.Instance) -> platform.Instance:
        """Post-rpc interceptor for get_instance

        DEPRECATED. Please use the `post_get_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_get_instance` interceptor runs
        before the `post_get_instance_with_metadata` interceptor.
        """
        return response

    def post_get_instance_with_metadata(
        self,
        response: platform.Instance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.Instance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_get_instance_with_metadata`
        interceptor in new development instead of the `post_get_instance` interceptor.
        When both interceptors are used, this `post_get_instance_with_metadata` interceptor runs after the
        `post_get_instance` interceptor. The (possibly modified) response returned by
        `post_get_instance` will be passed to
        `post_get_instance_with_metadata`.
        """
        return response, metadata

    def pre_get_processor(
        self,
        request: platform.GetProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.GetProcessorRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_get_processor(self, response: platform.Processor) -> platform.Processor:
        """Post-rpc interceptor for get_processor

        DEPRECATED. Please use the `post_get_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_get_processor` interceptor runs
        before the `post_get_processor_with_metadata` interceptor.
        """
        return response

    def post_get_processor_with_metadata(
        self,
        response: platform.Processor,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.Processor, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_processor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_get_processor_with_metadata`
        interceptor in new development instead of the `post_get_processor` interceptor.
        When both interceptors are used, this `post_get_processor_with_metadata` interceptor runs after the
        `post_get_processor` interceptor. The (possibly modified) response returned by
        `post_get_processor` will be passed to
        `post_get_processor_with_metadata`.
        """
        return response, metadata

    def pre_list_applications(
        self,
        request: platform.ListApplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.ListApplicationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_applications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_list_applications(
        self, response: platform.ListApplicationsResponse
    ) -> platform.ListApplicationsResponse:
        """Post-rpc interceptor for list_applications

        DEPRECATED. Please use the `post_list_applications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_list_applications` interceptor runs
        before the `post_list_applications_with_metadata` interceptor.
        """
        return response

    def post_list_applications_with_metadata(
        self,
        response: platform.ListApplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.ListApplicationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_applications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_list_applications_with_metadata`
        interceptor in new development instead of the `post_list_applications` interceptor.
        When both interceptors are used, this `post_list_applications_with_metadata` interceptor runs after the
        `post_list_applications` interceptor. The (possibly modified) response returned by
        `post_list_applications` will be passed to
        `post_list_applications_with_metadata`.
        """
        return response, metadata

    def pre_list_drafts(
        self,
        request: platform.ListDraftsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.ListDraftsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_drafts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_list_drafts(
        self, response: platform.ListDraftsResponse
    ) -> platform.ListDraftsResponse:
        """Post-rpc interceptor for list_drafts

        DEPRECATED. Please use the `post_list_drafts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_list_drafts` interceptor runs
        before the `post_list_drafts_with_metadata` interceptor.
        """
        return response

    def post_list_drafts_with_metadata(
        self,
        response: platform.ListDraftsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.ListDraftsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_drafts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_list_drafts_with_metadata`
        interceptor in new development instead of the `post_list_drafts` interceptor.
        When both interceptors are used, this `post_list_drafts_with_metadata` interceptor runs after the
        `post_list_drafts` interceptor. The (possibly modified) response returned by
        `post_list_drafts` will be passed to
        `post_list_drafts_with_metadata`.
        """
        return response, metadata

    def pre_list_instances(
        self,
        request: platform.ListInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.ListInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_list_instances(
        self, response: platform.ListInstancesResponse
    ) -> platform.ListInstancesResponse:
        """Post-rpc interceptor for list_instances

        DEPRECATED. Please use the `post_list_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_list_instances` interceptor runs
        before the `post_list_instances_with_metadata` interceptor.
        """
        return response

    def post_list_instances_with_metadata(
        self,
        response: platform.ListInstancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.ListInstancesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_list_instances_with_metadata`
        interceptor in new development instead of the `post_list_instances` interceptor.
        When both interceptors are used, this `post_list_instances_with_metadata` interceptor runs after the
        `post_list_instances` interceptor. The (possibly modified) response returned by
        `post_list_instances` will be passed to
        `post_list_instances_with_metadata`.
        """
        return response, metadata

    def pre_list_prebuilt_processors(
        self,
        request: platform.ListPrebuiltProcessorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.ListPrebuiltProcessorsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_prebuilt_processors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_list_prebuilt_processors(
        self, response: platform.ListPrebuiltProcessorsResponse
    ) -> platform.ListPrebuiltProcessorsResponse:
        """Post-rpc interceptor for list_prebuilt_processors

        DEPRECATED. Please use the `post_list_prebuilt_processors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_list_prebuilt_processors` interceptor runs
        before the `post_list_prebuilt_processors_with_metadata` interceptor.
        """
        return response

    def post_list_prebuilt_processors_with_metadata(
        self,
        response: platform.ListPrebuiltProcessorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.ListPrebuiltProcessorsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_prebuilt_processors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_list_prebuilt_processors_with_metadata`
        interceptor in new development instead of the `post_list_prebuilt_processors` interceptor.
        When both interceptors are used, this `post_list_prebuilt_processors_with_metadata` interceptor runs after the
        `post_list_prebuilt_processors` interceptor. The (possibly modified) response returned by
        `post_list_prebuilt_processors` will be passed to
        `post_list_prebuilt_processors_with_metadata`.
        """
        return response, metadata

    def pre_list_processors(
        self,
        request: platform.ListProcessorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.ListProcessorsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_processors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_list_processors(
        self, response: platform.ListProcessorsResponse
    ) -> platform.ListProcessorsResponse:
        """Post-rpc interceptor for list_processors

        DEPRECATED. Please use the `post_list_processors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_list_processors` interceptor runs
        before the `post_list_processors_with_metadata` interceptor.
        """
        return response

    def post_list_processors_with_metadata(
        self,
        response: platform.ListProcessorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.ListProcessorsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_processors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_list_processors_with_metadata`
        interceptor in new development instead of the `post_list_processors` interceptor.
        When both interceptors are used, this `post_list_processors_with_metadata` interceptor runs after the
        `post_list_processors` interceptor. The (possibly modified) response returned by
        `post_list_processors` will be passed to
        `post_list_processors_with_metadata`.
        """
        return response, metadata

    def pre_remove_application_stream_input(
        self,
        request: platform.RemoveApplicationStreamInputRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.RemoveApplicationStreamInputRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_application_stream_input

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_remove_application_stream_input(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for remove_application_stream_input

        DEPRECATED. Please use the `post_remove_application_stream_input_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_remove_application_stream_input` interceptor runs
        before the `post_remove_application_stream_input_with_metadata` interceptor.
        """
        return response

    def post_remove_application_stream_input_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_application_stream_input

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_remove_application_stream_input_with_metadata`
        interceptor in new development instead of the `post_remove_application_stream_input` interceptor.
        When both interceptors are used, this `post_remove_application_stream_input_with_metadata` interceptor runs after the
        `post_remove_application_stream_input` interceptor. The (possibly modified) response returned by
        `post_remove_application_stream_input` will be passed to
        `post_remove_application_stream_input_with_metadata`.
        """
        return response, metadata

    def pre_undeploy_application(
        self,
        request: platform.UndeployApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.UndeployApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for undeploy_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_undeploy_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for undeploy_application

        DEPRECATED. Please use the `post_undeploy_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_undeploy_application` interceptor runs
        before the `post_undeploy_application_with_metadata` interceptor.
        """
        return response

    def post_undeploy_application_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for undeploy_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_undeploy_application_with_metadata`
        interceptor in new development instead of the `post_undeploy_application` interceptor.
        When both interceptors are used, this `post_undeploy_application_with_metadata` interceptor runs after the
        `post_undeploy_application` interceptor. The (possibly modified) response returned by
        `post_undeploy_application` will be passed to
        `post_undeploy_application_with_metadata`.
        """
        return response, metadata

    def pre_update_application(
        self,
        request: platform.UpdateApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.UpdateApplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_update_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_application

        DEPRECATED. Please use the `post_update_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
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
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_update_application_with_metadata`
        interceptor in new development instead of the `post_update_application` interceptor.
        When both interceptors are used, this `post_update_application_with_metadata` interceptor runs after the
        `post_update_application` interceptor. The (possibly modified) response returned by
        `post_update_application` will be passed to
        `post_update_application_with_metadata`.
        """
        return response, metadata

    def pre_update_application_instances(
        self,
        request: platform.UpdateApplicationInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.UpdateApplicationInstancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_application_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_update_application_instances(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_application_instances

        DEPRECATED. Please use the `post_update_application_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_update_application_instances` interceptor runs
        before the `post_update_application_instances_with_metadata` interceptor.
        """
        return response

    def post_update_application_instances_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_application_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_update_application_instances_with_metadata`
        interceptor in new development instead of the `post_update_application_instances` interceptor.
        When both interceptors are used, this `post_update_application_instances_with_metadata` interceptor runs after the
        `post_update_application_instances` interceptor. The (possibly modified) response returned by
        `post_update_application_instances` will be passed to
        `post_update_application_instances_with_metadata`.
        """
        return response, metadata

    def pre_update_application_stream_input(
        self,
        request: platform.UpdateApplicationStreamInputRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.UpdateApplicationStreamInputRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_application_stream_input

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_update_application_stream_input(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_application_stream_input

        DEPRECATED. Please use the `post_update_application_stream_input_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_update_application_stream_input` interceptor runs
        before the `post_update_application_stream_input_with_metadata` interceptor.
        """
        return response

    def post_update_application_stream_input_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_application_stream_input

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_update_application_stream_input_with_metadata`
        interceptor in new development instead of the `post_update_application_stream_input` interceptor.
        When both interceptors are used, this `post_update_application_stream_input_with_metadata` interceptor runs after the
        `post_update_application_stream_input` interceptor. The (possibly modified) response returned by
        `post_update_application_stream_input` will be passed to
        `post_update_application_stream_input_with_metadata`.
        """
        return response, metadata

    def pre_update_draft(
        self,
        request: platform.UpdateDraftRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[platform.UpdateDraftRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_draft

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_update_draft(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_draft

        DEPRECATED. Please use the `post_update_draft_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_update_draft` interceptor runs
        before the `post_update_draft_with_metadata` interceptor.
        """
        return response

    def post_update_draft_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_draft

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_update_draft_with_metadata`
        interceptor in new development instead of the `post_update_draft` interceptor.
        When both interceptors are used, this `post_update_draft_with_metadata` interceptor runs after the
        `post_update_draft` interceptor. The (possibly modified) response returned by
        `post_update_draft` will be passed to
        `post_update_draft_with_metadata`.
        """
        return response, metadata

    def pre_update_processor(
        self,
        request: platform.UpdateProcessorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        platform.UpdateProcessorRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_processor

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_update_processor(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_processor

        DEPRECATED. Please use the `post_update_processor_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code. This `post_update_processor` interceptor runs
        before the `post_update_processor_with_metadata` interceptor.
        """
        return response

    def post_update_processor_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_processor

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AppPlatform server but before it is returned to user code.

        We recommend only using this `post_update_processor_with_metadata`
        interceptor in new development instead of the `post_update_processor` interceptor.
        When both interceptors are used, this `post_update_processor_with_metadata` interceptor runs after the
        `post_update_processor` interceptor. The (possibly modified) response returned by
        `post_update_processor` will be passed to
        `post_update_processor_with_metadata`.
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
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the AppPlatform server but before
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
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the AppPlatform server but before
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
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AppPlatform server but before
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
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the AppPlatform server but before
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
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AppPlatform server but before
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
        before they are sent to the AppPlatform server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the AppPlatform server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AppPlatformRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AppPlatformRestInterceptor


class AppPlatformRestTransport(_BaseAppPlatformRestTransport):
    """REST backend synchronous transport for AppPlatform.

    Service describing handlers for resources

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
        interceptor: Optional[AppPlatformRestInterceptor] = None,
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
            interceptor (Optional[AppPlatformRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AppPlatformRestInterceptor()
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
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/warehouseOperations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/assets/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/collections/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/imageIndexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/corpora/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
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

    class _AddApplicationStreamInput(
        _BaseAppPlatformRestTransport._BaseAddApplicationStreamInput,
        AppPlatformRestStub,
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.AddApplicationStreamInput")

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
            request: platform.AddApplicationStreamInputRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the add application stream
            input method over HTTP.

                Args:
                    request (~.platform.AddApplicationStreamInputRequest):
                        The request object. Message for adding stream input to an
                    Application.
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

            http_options = _BaseAppPlatformRestTransport._BaseAddApplicationStreamInput._get_http_options()
            request, metadata = self._interceptor.pre_add_application_stream_input(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseAddApplicationStreamInput,
                    "_BaseAddApplicationStreamInput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.AddApplicationStreamInput",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "AddApplicationStreamInput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppPlatformRestTransport._AddApplicationStreamInput._get_response(
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

            resp = self._interceptor.post_add_application_stream_input(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_application_stream_input_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.add_application_stream_input",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "AddApplicationStreamInput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateApplication(
        _BaseAppPlatformRestTransport._BaseCreateApplication, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.CreateApplication")

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
            request: platform.CreateApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create application method over HTTP.

            Args:
                request (~.platform.CreateApplicationRequest):
                    The request object. Message for creating a Application.
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
                _BaseAppPlatformRestTransport._BaseCreateApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseCreateApplication,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.CreateApplication",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CreateApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._CreateApplication._get_response(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.create_application",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CreateApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateApplicationInstances(
        _BaseAppPlatformRestTransport._BaseCreateApplicationInstances,
        AppPlatformRestStub,
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.CreateApplicationInstances")

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
            request: platform.CreateApplicationInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create application
            instances method over HTTP.

                Args:
                    request (~.platform.CreateApplicationInstancesRequest):
                        The request object. Message for adding stream input to an
                    Application.
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

            http_options = _BaseAppPlatformRestTransport._BaseCreateApplicationInstances._get_http_options()
            request, metadata = self._interceptor.pre_create_application_instances(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseCreateApplicationInstances,
                    "_BaseCreateApplicationInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.CreateApplicationInstances",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CreateApplicationInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppPlatformRestTransport._CreateApplicationInstances._get_response(
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

            resp = self._interceptor.post_create_application_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_application_instances_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.create_application_instances",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CreateApplicationInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDraft(
        _BaseAppPlatformRestTransport._BaseCreateDraft, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.CreateDraft")

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
            request: platform.CreateDraftRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create draft method over HTTP.

            Args:
                request (~.platform.CreateDraftRequest):
                    The request object. Message for creating a Draft.
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
                _BaseAppPlatformRestTransport._BaseCreateDraft._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_draft(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseCreateDraft,
                    "_BaseCreateDraft__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.CreateDraft",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CreateDraft",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._CreateDraft._get_response(
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

            resp = self._interceptor.post_create_draft(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_draft_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.create_draft",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CreateDraft",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProcessor(
        _BaseAppPlatformRestTransport._BaseCreateProcessor, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.CreateProcessor")

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
            request: platform.CreateProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create processor method over HTTP.

            Args:
                request (~.platform.CreateProcessorRequest):
                    The request object. Message for creating a Processor.
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
                _BaseAppPlatformRestTransport._BaseCreateProcessor._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_processor(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseCreateProcessor,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.CreateProcessor",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CreateProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._CreateProcessor._get_response(
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

            resp = self._interceptor.post_create_processor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_processor_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.create_processor",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CreateProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteApplication(
        _BaseAppPlatformRestTransport._BaseDeleteApplication, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.DeleteApplication")

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
            request: platform.DeleteApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete application method over HTTP.

            Args:
                request (~.platform.DeleteApplicationRequest):
                    The request object. Message for deleting an Application.
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
                _BaseAppPlatformRestTransport._BaseDeleteApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseDeleteApplication,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.DeleteApplication",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._DeleteApplication._get_response(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.delete_application",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteApplicationInstances(
        _BaseAppPlatformRestTransport._BaseDeleteApplicationInstances,
        AppPlatformRestStub,
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.DeleteApplicationInstances")

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
            request: platform.DeleteApplicationInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete application
            instances method over HTTP.

                Args:
                    request (~.platform.DeleteApplicationInstancesRequest):
                        The request object. Message for removing stream input
                    from an Application.
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

            http_options = _BaseAppPlatformRestTransport._BaseDeleteApplicationInstances._get_http_options()
            request, metadata = self._interceptor.pre_delete_application_instances(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseDeleteApplicationInstances,
                    "_BaseDeleteApplicationInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.DeleteApplicationInstances",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteApplicationInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppPlatformRestTransport._DeleteApplicationInstances._get_response(
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

            resp = self._interceptor.post_delete_application_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_application_instances_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.delete_application_instances",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteApplicationInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDraft(
        _BaseAppPlatformRestTransport._BaseDeleteDraft, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.DeleteDraft")

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
            request: platform.DeleteDraftRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete draft method over HTTP.

            Args:
                request (~.platform.DeleteDraftRequest):
                    The request object. Message for deleting a Draft.
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
                _BaseAppPlatformRestTransport._BaseDeleteDraft._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_draft(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseDeleteDraft,
                    "_BaseDeleteDraft__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.DeleteDraft",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteDraft",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._DeleteDraft._get_response(
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

            resp = self._interceptor.post_delete_draft(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_draft_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.delete_draft",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteDraft",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteProcessor(
        _BaseAppPlatformRestTransport._BaseDeleteProcessor, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.DeleteProcessor")

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
            request: platform.DeleteProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete processor method over HTTP.

            Args:
                request (~.platform.DeleteProcessorRequest):
                    The request object. Message for deleting a Processor.
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
                _BaseAppPlatformRestTransport._BaseDeleteProcessor._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_processor(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseDeleteProcessor,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.DeleteProcessor",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._DeleteProcessor._get_response(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.delete_processor",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeployApplication(
        _BaseAppPlatformRestTransport._BaseDeployApplication, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.DeployApplication")

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
            request: platform.DeployApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the deploy application method over HTTP.

            Args:
                request (~.platform.DeployApplicationRequest):
                    The request object. Message for deploying an Application.
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
                _BaseAppPlatformRestTransport._BaseDeployApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_deploy_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseDeployApplication,
                    "_BaseDeployApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.DeployApplication",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeployApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._DeployApplication._get_response(
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

            resp = self._interceptor.post_deploy_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deploy_application_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.deploy_application",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeployApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApplication(
        _BaseAppPlatformRestTransport._BaseGetApplication, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.GetApplication")

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
            request: platform.GetApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.Application:
            r"""Call the get application method over HTTP.

            Args:
                request (~.platform.GetApplicationRequest):
                    The request object. Message for getting a Application.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.Application:
                    Message describing Application object
            """

            http_options = (
                _BaseAppPlatformRestTransport._BaseGetApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_application(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseGetApplication,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.GetApplication",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._GetApplication._get_response(
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
            resp = platform.Application()
            pb_resp = platform.Application.pb(resp)

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
                    response_payload = platform.Application.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.get_application",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDraft(_BaseAppPlatformRestTransport._BaseGetDraft, AppPlatformRestStub):
        def __hash__(self):
            return hash("AppPlatformRestTransport.GetDraft")

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
            request: platform.GetDraftRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.Draft:
            r"""Call the get draft method over HTTP.

            Args:
                request (~.platform.GetDraftRequest):
                    The request object. Message for getting a Draft.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.Draft:
                    Message describing Draft object
            """

            http_options = (
                _BaseAppPlatformRestTransport._BaseGetDraft._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_draft(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseGetDraft,
                    "_BaseGetDraft__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.GetDraft",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetDraft",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._GetDraft._get_response(
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
            resp = platform.Draft()
            pb_resp = platform.Draft.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_draft(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_draft_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = platform.Draft.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.get_draft",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetDraft",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInstance(
        _BaseAppPlatformRestTransport._BaseGetInstance, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.GetInstance")

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
            request: platform.GetInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.Instance:
            r"""Call the get instance method over HTTP.

            Args:
                request (~.platform.GetInstanceRequest):
                    The request object. Message for getting a Instance.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.Instance:
                    Message describing Instance object
                Next ID: 12

            """

            http_options = (
                _BaseAppPlatformRestTransport._BaseGetInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseGetInstance,
                    "_BaseGetInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.GetInstance",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._GetInstance._get_response(
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
            resp = platform.Instance()
            pb_resp = platform.Instance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_instance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = platform.Instance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.get_instance",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProcessor(
        _BaseAppPlatformRestTransport._BaseGetProcessor, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.GetProcessor")

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
            request: platform.GetProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.Processor:
            r"""Call the get processor method over HTTP.

            Args:
                request (~.platform.GetProcessorRequest):
                    The request object. Message for getting a Processor.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.Processor:
                    Message describing Processor object.
                Next ID: 19

            """

            http_options = (
                _BaseAppPlatformRestTransport._BaseGetProcessor._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_processor(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseGetProcessor,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.GetProcessor",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._GetProcessor._get_response(
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
            resp = platform.Processor()
            pb_resp = platform.Processor.pb(resp)

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
                    response_payload = platform.Processor.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.get_processor",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApplications(
        _BaseAppPlatformRestTransport._BaseListApplications, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.ListApplications")

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
            request: platform.ListApplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.ListApplicationsResponse:
            r"""Call the list applications method over HTTP.

            Args:
                request (~.platform.ListApplicationsRequest):
                    The request object. Message for requesting list of
                Applications.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.ListApplicationsResponse:
                    Message for response to listing
                Applications.

            """

            http_options = (
                _BaseAppPlatformRestTransport._BaseListApplications._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_applications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseListApplications,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.ListApplications",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListApplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._ListApplications._get_response(
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
            resp = platform.ListApplicationsResponse()
            pb_resp = platform.ListApplicationsResponse.pb(resp)

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
                    response_payload = platform.ListApplicationsResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.list_applications",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListApplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDrafts(
        _BaseAppPlatformRestTransport._BaseListDrafts, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.ListDrafts")

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
            request: platform.ListDraftsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.ListDraftsResponse:
            r"""Call the list drafts method over HTTP.

            Args:
                request (~.platform.ListDraftsRequest):
                    The request object. Message for requesting list of
                Drafts.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.ListDraftsResponse:
                    Message for response to listing
                Drafts.

            """

            http_options = (
                _BaseAppPlatformRestTransport._BaseListDrafts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_drafts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseListDrafts,
                    "_BaseListDrafts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.ListDrafts",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListDrafts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._ListDrafts._get_response(
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
            resp = platform.ListDraftsResponse()
            pb_resp = platform.ListDraftsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_drafts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_drafts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = platform.ListDraftsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.list_drafts",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListDrafts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInstances(
        _BaseAppPlatformRestTransport._BaseListInstances, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.ListInstances")

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
            request: platform.ListInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.ListInstancesResponse:
            r"""Call the list instances method over HTTP.

            Args:
                request (~.platform.ListInstancesRequest):
                    The request object. Message for requesting list of
                Instances.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.ListInstancesResponse:
                    Message for response to listing
                Instances.

            """

            http_options = (
                _BaseAppPlatformRestTransport._BaseListInstances._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_instances(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseListInstances,
                    "_BaseListInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.ListInstances",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._ListInstances._get_response(
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
            resp = platform.ListInstancesResponse()
            pb_resp = platform.ListInstancesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_instances_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = platform.ListInstancesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.list_instances",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPrebuiltProcessors(
        _BaseAppPlatformRestTransport._BaseListPrebuiltProcessors, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.ListPrebuiltProcessors")

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
            request: platform.ListPrebuiltProcessorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.ListPrebuiltProcessorsResponse:
            r"""Call the list prebuilt processors method over HTTP.

            Args:
                request (~.platform.ListPrebuiltProcessorsRequest):
                    The request object. Request Message for listing Prebuilt
                Processors.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.ListPrebuiltProcessorsResponse:
                    Response Message for listing Prebuilt
                Processors.

            """

            http_options = _BaseAppPlatformRestTransport._BaseListPrebuiltProcessors._get_http_options()
            request, metadata = self._interceptor.pre_list_prebuilt_processors(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseListPrebuiltProcessors,
                    "_BaseListPrebuiltProcessors__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.ListPrebuiltProcessors",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListPrebuiltProcessors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._ListPrebuiltProcessors._get_response(
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
            resp = platform.ListPrebuiltProcessorsResponse()
            pb_resp = platform.ListPrebuiltProcessorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_prebuilt_processors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_prebuilt_processors_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = platform.ListPrebuiltProcessorsResponse.to_json(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.list_prebuilt_processors",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListPrebuiltProcessors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProcessors(
        _BaseAppPlatformRestTransport._BaseListProcessors, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.ListProcessors")

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
            request: platform.ListProcessorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> platform.ListProcessorsResponse:
            r"""Call the list processors method over HTTP.

            Args:
                request (~.platform.ListProcessorsRequest):
                    The request object. Message for requesting list of
                Processors.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.platform.ListProcessorsResponse:
                    Message for response to listing
                Processors.

            """

            http_options = (
                _BaseAppPlatformRestTransport._BaseListProcessors._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_processors(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseListProcessors,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.ListProcessors",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListProcessors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._ListProcessors._get_response(
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
            resp = platform.ListProcessorsResponse()
            pb_resp = platform.ListProcessorsResponse.pb(resp)

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
                    response_payload = platform.ListProcessorsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.list_processors",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListProcessors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveApplicationStreamInput(
        _BaseAppPlatformRestTransport._BaseRemoveApplicationStreamInput,
        AppPlatformRestStub,
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.RemoveApplicationStreamInput")

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
            request: platform.RemoveApplicationStreamInputRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the remove application stream
            input method over HTTP.

                Args:
                    request (~.platform.RemoveApplicationStreamInputRequest):
                        The request object. Message for removing stream input
                    from an Application.
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

            http_options = _BaseAppPlatformRestTransport._BaseRemoveApplicationStreamInput._get_http_options()
            request, metadata = self._interceptor.pre_remove_application_stream_input(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseRemoveApplicationStreamInput,
                    "_BaseRemoveApplicationStreamInput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.RemoveApplicationStreamInput",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "RemoveApplicationStreamInput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppPlatformRestTransport._RemoveApplicationStreamInput._get_response(
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

            resp = self._interceptor.post_remove_application_stream_input(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_remove_application_stream_input_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.remove_application_stream_input",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "RemoveApplicationStreamInput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeployApplication(
        _BaseAppPlatformRestTransport._BaseUndeployApplication, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.UndeployApplication")

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
            request: platform.UndeployApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the undeploy application method over HTTP.

            Args:
                request (~.platform.UndeployApplicationRequest):
                    The request object. Message for undeploying an
                Application.
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

            http_options = _BaseAppPlatformRestTransport._BaseUndeployApplication._get_http_options()
            request, metadata = self._interceptor.pre_undeploy_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseUndeployApplication,
                    "_BaseUndeployApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.UndeployApplication",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UndeployApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._UndeployApplication._get_response(
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

            resp = self._interceptor.post_undeploy_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undeploy_application_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.undeploy_application",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UndeployApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApplication(
        _BaseAppPlatformRestTransport._BaseUpdateApplication, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.UpdateApplication")

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
            request: platform.UpdateApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update application method over HTTP.

            Args:
                request (~.platform.UpdateApplicationRequest):
                    The request object. Message for updating an Application.
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
                _BaseAppPlatformRestTransport._BaseUpdateApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseUpdateApplication,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.UpdateApplication",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._UpdateApplication._get_response(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.update_application",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApplicationInstances(
        _BaseAppPlatformRestTransport._BaseUpdateApplicationInstances,
        AppPlatformRestStub,
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.UpdateApplicationInstances")

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
            request: platform.UpdateApplicationInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update application
            instances method over HTTP.

                Args:
                    request (~.platform.UpdateApplicationInstancesRequest):
                        The request object. Message for updating an
                    ApplicationInstance.
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

            http_options = _BaseAppPlatformRestTransport._BaseUpdateApplicationInstances._get_http_options()
            request, metadata = self._interceptor.pre_update_application_instances(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseUpdateApplicationInstances,
                    "_BaseUpdateApplicationInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.UpdateApplicationInstances",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateApplicationInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppPlatformRestTransport._UpdateApplicationInstances._get_response(
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

            resp = self._interceptor.post_update_application_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_application_instances_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.update_application_instances",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateApplicationInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApplicationStreamInput(
        _BaseAppPlatformRestTransport._BaseUpdateApplicationStreamInput,
        AppPlatformRestStub,
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.UpdateApplicationStreamInput")

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
            request: platform.UpdateApplicationStreamInputRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update application stream
            input method over HTTP.

                Args:
                    request (~.platform.UpdateApplicationStreamInputRequest):
                        The request object. Message for updating stream input to
                    an Application.
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

            http_options = _BaseAppPlatformRestTransport._BaseUpdateApplicationStreamInput._get_http_options()
            request, metadata = self._interceptor.pre_update_application_stream_input(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseUpdateApplicationStreamInput,
                    "_BaseUpdateApplicationStreamInput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.UpdateApplicationStreamInput",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateApplicationStreamInput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AppPlatformRestTransport._UpdateApplicationStreamInput._get_response(
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

            resp = self._interceptor.post_update_application_stream_input(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_application_stream_input_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.update_application_stream_input",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateApplicationStreamInput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDraft(
        _BaseAppPlatformRestTransport._BaseUpdateDraft, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.UpdateDraft")

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
            request: platform.UpdateDraftRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update draft method over HTTP.

            Args:
                request (~.platform.UpdateDraftRequest):
                    The request object. Message for updating a Draft.
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
                _BaseAppPlatformRestTransport._BaseUpdateDraft._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_draft(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseUpdateDraft,
                    "_BaseUpdateDraft__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.UpdateDraft",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateDraft",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._UpdateDraft._get_response(
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

            resp = self._interceptor.post_update_draft(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_draft_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.update_draft",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateDraft",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProcessor(
        _BaseAppPlatformRestTransport._BaseUpdateProcessor, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.UpdateProcessor")

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
            request: platform.UpdateProcessorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update processor method over HTTP.

            Args:
                request (~.platform.UpdateProcessorRequest):
                    The request object. Message for updating a Processor.
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
                _BaseAppPlatformRestTransport._BaseUpdateProcessor._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_processor(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseUpdateProcessor,
                    "_BaseUpdateProcessor__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.UpdateProcessor",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateProcessor",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._UpdateProcessor._get_response(
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

            resp = self._interceptor.post_update_processor(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_processor_with_metadata(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformClient.update_processor",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "UpdateProcessor",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def add_application_stream_input(
        self,
    ) -> Callable[
        [platform.AddApplicationStreamInputRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddApplicationStreamInput(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_application(
        self,
    ) -> Callable[[platform.CreateApplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_application_instances(
        self,
    ) -> Callable[
        [platform.CreateApplicationInstancesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApplicationInstances(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_draft(
        self,
    ) -> Callable[[platform.CreateDraftRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDraft(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_processor(
        self,
    ) -> Callable[[platform.CreateProcessorRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_application(
        self,
    ) -> Callable[[platform.DeleteApplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_application_instances(
        self,
    ) -> Callable[
        [platform.DeleteApplicationInstancesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApplicationInstances(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_draft(
        self,
    ) -> Callable[[platform.DeleteDraftRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDraft(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_processor(
        self,
    ) -> Callable[[platform.DeleteProcessorRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def deploy_application(
        self,
    ) -> Callable[[platform.DeployApplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeployApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_application(
        self,
    ) -> Callable[[platform.GetApplicationRequest], platform.Application]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_draft(self) -> Callable[[platform.GetDraftRequest], platform.Draft]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDraft(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_instance(
        self,
    ) -> Callable[[platform.GetInstanceRequest], platform.Instance]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_processor(
        self,
    ) -> Callable[[platform.GetProcessorRequest], platform.Processor]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_applications(
        self,
    ) -> Callable[
        [platform.ListApplicationsRequest], platform.ListApplicationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApplications(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_drafts(
        self,
    ) -> Callable[[platform.ListDraftsRequest], platform.ListDraftsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDrafts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_instances(
        self,
    ) -> Callable[[platform.ListInstancesRequest], platform.ListInstancesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInstances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_prebuilt_processors(
        self,
    ) -> Callable[
        [platform.ListPrebuiltProcessorsRequest],
        platform.ListPrebuiltProcessorsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrebuiltProcessors(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_processors(
        self,
    ) -> Callable[[platform.ListProcessorsRequest], platform.ListProcessorsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProcessors(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_application_stream_input(
        self,
    ) -> Callable[
        [platform.RemoveApplicationStreamInputRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveApplicationStreamInput(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def undeploy_application(
        self,
    ) -> Callable[[platform.UndeployApplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeployApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_application(
        self,
    ) -> Callable[[platform.UpdateApplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_application_instances(
        self,
    ) -> Callable[
        [platform.UpdateApplicationInstancesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApplicationInstances(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_application_stream_input(
        self,
    ) -> Callable[
        [platform.UpdateApplicationStreamInputRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApplicationStreamInput(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_draft(
        self,
    ) -> Callable[[platform.UpdateDraftRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDraft(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_processor(
        self,
    ) -> Callable[[platform.UpdateProcessorRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProcessor(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseAppPlatformRestTransport._BaseGetLocation, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.GetLocation")

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
                _BaseAppPlatformRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
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
        _BaseAppPlatformRestTransport._BaseListLocations, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.ListLocations")

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
                _BaseAppPlatformRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
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
        _BaseAppPlatformRestTransport._BaseCancelOperation, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.CancelOperation")

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
                _BaseAppPlatformRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._CancelOperation._get_response(
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
        _BaseAppPlatformRestTransport._BaseDeleteOperation, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.DeleteOperation")

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
                _BaseAppPlatformRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._DeleteOperation._get_response(
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
        _BaseAppPlatformRestTransport._BaseGetOperation, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.GetOperation")

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
                _BaseAppPlatformRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
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
        _BaseAppPlatformRestTransport._BaseListOperations, AppPlatformRestStub
    ):
        def __hash__(self):
            return hash("AppPlatformRestTransport.ListOperations")

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
                _BaseAppPlatformRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAppPlatformRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.visionai_v1.AppPlatformClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AppPlatformRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.visionai_v1.AppPlatformAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.visionai.v1.AppPlatform",
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


__all__ = ("AppPlatformRestTransport",)
