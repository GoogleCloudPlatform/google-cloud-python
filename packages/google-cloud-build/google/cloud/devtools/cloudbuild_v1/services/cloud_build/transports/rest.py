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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.devtools.cloudbuild_v1._compat import transcode_request
from google.cloud.devtools.cloudbuild_v1.types import cloudbuild

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCloudBuildRestTransport

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


class CloudBuildRestInterceptor:
    """Interceptor for CloudBuild.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CloudBuildRestTransport.

    .. code-block:: python
        class MyCustomCloudBuildInterceptor(CloudBuildRestInterceptor):
            def pre_approve_build(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_approve_build(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_build(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_build(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_build(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_build(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_build_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_build_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_worker_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_worker_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_build_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_worker_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_worker_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_build(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_build(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_build_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_build_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_default_service_account(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_default_service_account(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_worker_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_worker_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_builds(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_builds(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_build_triggers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_build_triggers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_worker_pools(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_worker_pools(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_receive_trigger_webhook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_receive_trigger_webhook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_retry_build(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retry_build(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_build_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_build_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_build_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_build_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_worker_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_worker_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CloudBuildRestTransport(interceptor=MyCustomCloudBuildInterceptor())
        client = CloudBuildClient(transport=transport)


    """

    def pre_approve_build(
        self,
        request: cloudbuild.ApproveBuildRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.ApproveBuildRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for approve_build

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_approve_build(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for approve_build

        DEPRECATED. Please use the `post_approve_build_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_approve_build` interceptor runs
        before the `post_approve_build_with_metadata` interceptor.
        """
        return response

    def post_approve_build_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for approve_build

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_approve_build_with_metadata`
        interceptor in new development instead of the `post_approve_build` interceptor.
        When both interceptors are used, this `post_approve_build_with_metadata` interceptor runs after the
        `post_approve_build` interceptor. The (possibly modified) response returned by
        `post_approve_build` will be passed to
        `post_approve_build_with_metadata`.
        """
        return response, metadata

    def pre_cancel_build(
        self,
        request: cloudbuild.CancelBuildRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.CancelBuildRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for cancel_build

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_cancel_build(self, response: cloudbuild.Build) -> cloudbuild.Build:
        """Post-rpc interceptor for cancel_build

        DEPRECATED. Please use the `post_cancel_build_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_cancel_build` interceptor runs
        before the `post_cancel_build_with_metadata` interceptor.
        """
        return response

    def post_cancel_build_with_metadata(
        self,
        response: cloudbuild.Build,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.Build, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for cancel_build

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_cancel_build_with_metadata`
        interceptor in new development instead of the `post_cancel_build` interceptor.
        When both interceptors are used, this `post_cancel_build_with_metadata` interceptor runs after the
        `post_cancel_build` interceptor. The (possibly modified) response returned by
        `post_cancel_build` will be passed to
        `post_cancel_build_with_metadata`.
        """
        return response, metadata

    def pre_create_build(
        self,
        request: cloudbuild.CreateBuildRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.CreateBuildRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_build

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_create_build(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_build

        DEPRECATED. Please use the `post_create_build_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_create_build` interceptor runs
        before the `post_create_build_with_metadata` interceptor.
        """
        return response

    def post_create_build_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_build

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_create_build_with_metadata`
        interceptor in new development instead of the `post_create_build` interceptor.
        When both interceptors are used, this `post_create_build_with_metadata` interceptor runs after the
        `post_create_build` interceptor. The (possibly modified) response returned by
        `post_create_build` will be passed to
        `post_create_build_with_metadata`.
        """
        return response, metadata

    def pre_create_build_trigger(
        self,
        request: cloudbuild.CreateBuildTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.CreateBuildTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_build_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_create_build_trigger(
        self, response: cloudbuild.BuildTrigger
    ) -> cloudbuild.BuildTrigger:
        """Post-rpc interceptor for create_build_trigger

        DEPRECATED. Please use the `post_create_build_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_create_build_trigger` interceptor runs
        before the `post_create_build_trigger_with_metadata` interceptor.
        """
        return response

    def post_create_build_trigger_with_metadata(
        self,
        response: cloudbuild.BuildTrigger,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.BuildTrigger, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_build_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_create_build_trigger_with_metadata`
        interceptor in new development instead of the `post_create_build_trigger` interceptor.
        When both interceptors are used, this `post_create_build_trigger_with_metadata` interceptor runs after the
        `post_create_build_trigger` interceptor. The (possibly modified) response returned by
        `post_create_build_trigger` will be passed to
        `post_create_build_trigger_with_metadata`.
        """
        return response, metadata

    def pre_create_worker_pool(
        self,
        request: cloudbuild.CreateWorkerPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.CreateWorkerPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_worker_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_create_worker_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_worker_pool

        DEPRECATED. Please use the `post_create_worker_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_create_worker_pool` interceptor runs
        before the `post_create_worker_pool_with_metadata` interceptor.
        """
        return response

    def post_create_worker_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_worker_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_create_worker_pool_with_metadata`
        interceptor in new development instead of the `post_create_worker_pool` interceptor.
        When both interceptors are used, this `post_create_worker_pool_with_metadata` interceptor runs after the
        `post_create_worker_pool` interceptor. The (possibly modified) response returned by
        `post_create_worker_pool` will be passed to
        `post_create_worker_pool_with_metadata`.
        """
        return response, metadata

    def pre_delete_build_trigger(
        self,
        request: cloudbuild.DeleteBuildTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.DeleteBuildTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_build_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def pre_delete_worker_pool(
        self,
        request: cloudbuild.DeleteWorkerPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.DeleteWorkerPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_worker_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_delete_worker_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_worker_pool

        DEPRECATED. Please use the `post_delete_worker_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_delete_worker_pool` interceptor runs
        before the `post_delete_worker_pool_with_metadata` interceptor.
        """
        return response

    def post_delete_worker_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_worker_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_delete_worker_pool_with_metadata`
        interceptor in new development instead of the `post_delete_worker_pool` interceptor.
        When both interceptors are used, this `post_delete_worker_pool_with_metadata` interceptor runs after the
        `post_delete_worker_pool` interceptor. The (possibly modified) response returned by
        `post_delete_worker_pool` will be passed to
        `post_delete_worker_pool_with_metadata`.
        """
        return response, metadata

    def pre_get_build(
        self,
        request: cloudbuild.GetBuildRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.GetBuildRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_build

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_get_build(self, response: cloudbuild.Build) -> cloudbuild.Build:
        """Post-rpc interceptor for get_build

        DEPRECATED. Please use the `post_get_build_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_get_build` interceptor runs
        before the `post_get_build_with_metadata` interceptor.
        """
        return response

    def post_get_build_with_metadata(
        self,
        response: cloudbuild.Build,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.Build, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_build

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_get_build_with_metadata`
        interceptor in new development instead of the `post_get_build` interceptor.
        When both interceptors are used, this `post_get_build_with_metadata` interceptor runs after the
        `post_get_build` interceptor. The (possibly modified) response returned by
        `post_get_build` will be passed to
        `post_get_build_with_metadata`.
        """
        return response, metadata

    def pre_get_build_trigger(
        self,
        request: cloudbuild.GetBuildTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.GetBuildTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_build_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_get_build_trigger(
        self, response: cloudbuild.BuildTrigger
    ) -> cloudbuild.BuildTrigger:
        """Post-rpc interceptor for get_build_trigger

        DEPRECATED. Please use the `post_get_build_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_get_build_trigger` interceptor runs
        before the `post_get_build_trigger_with_metadata` interceptor.
        """
        return response

    def post_get_build_trigger_with_metadata(
        self,
        response: cloudbuild.BuildTrigger,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.BuildTrigger, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_build_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_get_build_trigger_with_metadata`
        interceptor in new development instead of the `post_get_build_trigger` interceptor.
        When both interceptors are used, this `post_get_build_trigger_with_metadata` interceptor runs after the
        `post_get_build_trigger` interceptor. The (possibly modified) response returned by
        `post_get_build_trigger` will be passed to
        `post_get_build_trigger_with_metadata`.
        """
        return response, metadata

    def pre_get_default_service_account(
        self,
        request: cloudbuild.GetDefaultServiceAccountRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.GetDefaultServiceAccountRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_default_service_account

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_get_default_service_account(
        self, response: cloudbuild.DefaultServiceAccount
    ) -> cloudbuild.DefaultServiceAccount:
        """Post-rpc interceptor for get_default_service_account

        DEPRECATED. Please use the `post_get_default_service_account_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_get_default_service_account` interceptor runs
        before the `post_get_default_service_account_with_metadata` interceptor.
        """
        return response

    def post_get_default_service_account_with_metadata(
        self,
        response: cloudbuild.DefaultServiceAccount,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.DefaultServiceAccount, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_default_service_account

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_get_default_service_account_with_metadata`
        interceptor in new development instead of the `post_get_default_service_account` interceptor.
        When both interceptors are used, this `post_get_default_service_account_with_metadata` interceptor runs after the
        `post_get_default_service_account` interceptor. The (possibly modified) response returned by
        `post_get_default_service_account` will be passed to
        `post_get_default_service_account_with_metadata`.
        """
        return response, metadata

    def pre_get_worker_pool(
        self,
        request: cloudbuild.GetWorkerPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.GetWorkerPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_worker_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_get_worker_pool(
        self, response: cloudbuild.WorkerPool
    ) -> cloudbuild.WorkerPool:
        """Post-rpc interceptor for get_worker_pool

        DEPRECATED. Please use the `post_get_worker_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_get_worker_pool` interceptor runs
        before the `post_get_worker_pool_with_metadata` interceptor.
        """
        return response

    def post_get_worker_pool_with_metadata(
        self,
        response: cloudbuild.WorkerPool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.WorkerPool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_worker_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_get_worker_pool_with_metadata`
        interceptor in new development instead of the `post_get_worker_pool` interceptor.
        When both interceptors are used, this `post_get_worker_pool_with_metadata` interceptor runs after the
        `post_get_worker_pool` interceptor. The (possibly modified) response returned by
        `post_get_worker_pool` will be passed to
        `post_get_worker_pool_with_metadata`.
        """
        return response, metadata

    def pre_list_builds(
        self,
        request: cloudbuild.ListBuildsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.ListBuildsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_builds

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_list_builds(
        self, response: cloudbuild.ListBuildsResponse
    ) -> cloudbuild.ListBuildsResponse:
        """Post-rpc interceptor for list_builds

        DEPRECATED. Please use the `post_list_builds_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_list_builds` interceptor runs
        before the `post_list_builds_with_metadata` interceptor.
        """
        return response

    def post_list_builds_with_metadata(
        self,
        response: cloudbuild.ListBuildsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.ListBuildsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_builds

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_list_builds_with_metadata`
        interceptor in new development instead of the `post_list_builds` interceptor.
        When both interceptors are used, this `post_list_builds_with_metadata` interceptor runs after the
        `post_list_builds` interceptor. The (possibly modified) response returned by
        `post_list_builds` will be passed to
        `post_list_builds_with_metadata`.
        """
        return response, metadata

    def pre_list_build_triggers(
        self,
        request: cloudbuild.ListBuildTriggersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.ListBuildTriggersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_build_triggers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_list_build_triggers(
        self, response: cloudbuild.ListBuildTriggersResponse
    ) -> cloudbuild.ListBuildTriggersResponse:
        """Post-rpc interceptor for list_build_triggers

        DEPRECATED. Please use the `post_list_build_triggers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_list_build_triggers` interceptor runs
        before the `post_list_build_triggers_with_metadata` interceptor.
        """
        return response

    def post_list_build_triggers_with_metadata(
        self,
        response: cloudbuild.ListBuildTriggersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.ListBuildTriggersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_build_triggers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_list_build_triggers_with_metadata`
        interceptor in new development instead of the `post_list_build_triggers` interceptor.
        When both interceptors are used, this `post_list_build_triggers_with_metadata` interceptor runs after the
        `post_list_build_triggers` interceptor. The (possibly modified) response returned by
        `post_list_build_triggers` will be passed to
        `post_list_build_triggers_with_metadata`.
        """
        return response, metadata

    def pre_list_worker_pools(
        self,
        request: cloudbuild.ListWorkerPoolsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.ListWorkerPoolsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_worker_pools

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_list_worker_pools(
        self, response: cloudbuild.ListWorkerPoolsResponse
    ) -> cloudbuild.ListWorkerPoolsResponse:
        """Post-rpc interceptor for list_worker_pools

        DEPRECATED. Please use the `post_list_worker_pools_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_list_worker_pools` interceptor runs
        before the `post_list_worker_pools_with_metadata` interceptor.
        """
        return response

    def post_list_worker_pools_with_metadata(
        self,
        response: cloudbuild.ListWorkerPoolsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.ListWorkerPoolsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_worker_pools

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_list_worker_pools_with_metadata`
        interceptor in new development instead of the `post_list_worker_pools` interceptor.
        When both interceptors are used, this `post_list_worker_pools_with_metadata` interceptor runs after the
        `post_list_worker_pools` interceptor. The (possibly modified) response returned by
        `post_list_worker_pools` will be passed to
        `post_list_worker_pools_with_metadata`.
        """
        return response, metadata

    def pre_receive_trigger_webhook(
        self,
        request: cloudbuild.ReceiveTriggerWebhookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.ReceiveTriggerWebhookRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for receive_trigger_webhook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_receive_trigger_webhook(
        self, response: cloudbuild.ReceiveTriggerWebhookResponse
    ) -> cloudbuild.ReceiveTriggerWebhookResponse:
        """Post-rpc interceptor for receive_trigger_webhook

        DEPRECATED. Please use the `post_receive_trigger_webhook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_receive_trigger_webhook` interceptor runs
        before the `post_receive_trigger_webhook_with_metadata` interceptor.
        """
        return response

    def post_receive_trigger_webhook_with_metadata(
        self,
        response: cloudbuild.ReceiveTriggerWebhookResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.ReceiveTriggerWebhookResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for receive_trigger_webhook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_receive_trigger_webhook_with_metadata`
        interceptor in new development instead of the `post_receive_trigger_webhook` interceptor.
        When both interceptors are used, this `post_receive_trigger_webhook_with_metadata` interceptor runs after the
        `post_receive_trigger_webhook` interceptor. The (possibly modified) response returned by
        `post_receive_trigger_webhook` will be passed to
        `post_receive_trigger_webhook_with_metadata`.
        """
        return response, metadata

    def pre_retry_build(
        self,
        request: cloudbuild.RetryBuildRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.RetryBuildRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for retry_build

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_retry_build(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for retry_build

        DEPRECATED. Please use the `post_retry_build_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_retry_build` interceptor runs
        before the `post_retry_build_with_metadata` interceptor.
        """
        return response

    def post_retry_build_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for retry_build

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_retry_build_with_metadata`
        interceptor in new development instead of the `post_retry_build` interceptor.
        When both interceptors are used, this `post_retry_build_with_metadata` interceptor runs after the
        `post_retry_build` interceptor. The (possibly modified) response returned by
        `post_retry_build` will be passed to
        `post_retry_build_with_metadata`.
        """
        return response, metadata

    def pre_run_build_trigger(
        self,
        request: cloudbuild.RunBuildTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.RunBuildTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for run_build_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_run_build_trigger(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_build_trigger

        DEPRECATED. Please use the `post_run_build_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_run_build_trigger` interceptor runs
        before the `post_run_build_trigger_with_metadata` interceptor.
        """
        return response

    def post_run_build_trigger_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_build_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_run_build_trigger_with_metadata`
        interceptor in new development instead of the `post_run_build_trigger` interceptor.
        When both interceptors are used, this `post_run_build_trigger_with_metadata` interceptor runs after the
        `post_run_build_trigger` interceptor. The (possibly modified) response returned by
        `post_run_build_trigger` will be passed to
        `post_run_build_trigger_with_metadata`.
        """
        return response, metadata

    def pre_update_build_trigger(
        self,
        request: cloudbuild.UpdateBuildTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.UpdateBuildTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_build_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_update_build_trigger(
        self, response: cloudbuild.BuildTrigger
    ) -> cloudbuild.BuildTrigger:
        """Post-rpc interceptor for update_build_trigger

        DEPRECATED. Please use the `post_update_build_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_update_build_trigger` interceptor runs
        before the `post_update_build_trigger_with_metadata` interceptor.
        """
        return response

    def post_update_build_trigger_with_metadata(
        self,
        response: cloudbuild.BuildTrigger,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloudbuild.BuildTrigger, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_build_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_update_build_trigger_with_metadata`
        interceptor in new development instead of the `post_update_build_trigger` interceptor.
        When both interceptors are used, this `post_update_build_trigger_with_metadata` interceptor runs after the
        `post_update_build_trigger` interceptor. The (possibly modified) response returned by
        `post_update_build_trigger` will be passed to
        `post_update_build_trigger_with_metadata`.
        """
        return response, metadata

    def pre_update_worker_pool(
        self,
        request: cloudbuild.UpdateWorkerPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloudbuild.UpdateWorkerPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_worker_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudBuild server.
        """
        return request, metadata

    def post_update_worker_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_worker_pool

        DEPRECATED. Please use the `post_update_worker_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudBuild server but before
        it is returned to user code. This `post_update_worker_pool` interceptor runs
        before the `post_update_worker_pool_with_metadata` interceptor.
        """
        return response

    def post_update_worker_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_worker_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudBuild server but before it is returned to user code.

        We recommend only using this `post_update_worker_pool_with_metadata`
        interceptor in new development instead of the `post_update_worker_pool` interceptor.
        When both interceptors are used, this `post_update_worker_pool_with_metadata` interceptor runs after the
        `post_update_worker_pool` interceptor. The (possibly modified) response returned by
        `post_update_worker_pool` will be passed to
        `post_update_worker_pool_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class CloudBuildRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CloudBuildRestInterceptor


class CloudBuildRestTransport(_BaseCloudBuildRestTransport):
    """REST backend synchronous transport for CloudBuild.

    Creates and manages builds on Google Cloud Platform.

    The main concept used by this API is a ``Build``, which describes
    the location of the source to build, how to build the source, and
    where to store the built artifacts, if any.

    A user can list previously-requested builds or get builds by their
    ID to determine the status of the build.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudbuild.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CloudBuildRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudbuild.googleapis.com').
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
            interceptor (Optional[CloudBuildRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CloudBuildRestInterceptor()
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
                        "uri": "/v1/{name=operations/**}:cancel",
                        "body": "*",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=operations/**}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
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

    class _ApproveBuild(
        _BaseCloudBuildRestTransport._BaseApproveBuild, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.ApproveBuild")

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
            request: cloudbuild.ApproveBuildRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the approve build method over HTTP.

            Args:
                request (~.cloudbuild.ApproveBuildRequest):
                    The request object. Request to approve or reject a
                pending build.
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
                _BaseCloudBuildRestTransport._BaseApproveBuild._get_http_options()
            )
            request, metadata = self._interceptor.pre_approve_build(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseApproveBuild,
                    "_BaseApproveBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.ApproveBuild",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ApproveBuild",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._ApproveBuild._get_response(
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

            resp = self._interceptor.post_approve_build(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_approve_build_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.approve_build",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ApproveBuild",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CancelBuild(
        _BaseCloudBuildRestTransport._BaseCancelBuild, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.CancelBuild")

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
            request: cloudbuild.CancelBuildRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.Build:
            r"""Call the cancel build method over HTTP.

            Args:
                request (~.cloudbuild.CancelBuildRequest):
                    The request object. Request to cancel an ongoing build.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.Build:
                    A build resource in the Cloud Build API.

                At a high level, a ``Build`` describes where to find
                source code, how to build it (for example, the builder
                image to run on the source), and where to store the
                built artifacts.

                Fields can include the following variables, which will
                be expanded when the build is created:

                - $PROJECT_ID: the project ID of the build.
                - $PROJECT_NUMBER: the project number of the build.
                - $LOCATION: the location/region of the build.
                - $BUILD_ID: the autogenerated ID of the build.
                - $REPO_NAME: the source repository name specified by
                  RepoSource.
                - $BRANCH_NAME: the branch name specified by RepoSource.
                - $TAG_NAME: the tag name specified by RepoSource.
                - $REVISION_ID or $COMMIT_SHA: the commit SHA specified
                  by RepoSource or resolved from the specified branch or
                  tag.
                - $SHORT_SHA: first 7 characters of $REVISION_ID or
                  $COMMIT_SHA.

            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseCancelBuild._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_build(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseCancelBuild,
                    "_BaseCancelBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.CancelBuild",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "CancelBuild",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._CancelBuild._get_response(
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
            resp = cloudbuild.Build()
            pb_resp = cloudbuild.Build.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_cancel_build(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_build_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.Build.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.cancel_build",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "CancelBuild",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBuild(
        _BaseCloudBuildRestTransport._BaseCreateBuild, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.CreateBuild")

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
            request: cloudbuild.CreateBuildRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create build method over HTTP.

            Args:
                request (~.cloudbuild.CreateBuildRequest):
                    The request object. Request to create a new build.
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
                _BaseCloudBuildRestTransport._BaseCreateBuild._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_build(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseCreateBuild,
                    "_BaseCreateBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.CreateBuild",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "CreateBuild",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._CreateBuild._get_response(
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

            resp = self._interceptor.post_create_build(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_build_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.create_build",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "CreateBuild",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBuildTrigger(
        _BaseCloudBuildRestTransport._BaseCreateBuildTrigger, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.CreateBuildTrigger")

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
            request: cloudbuild.CreateBuildTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.BuildTrigger:
            r"""Call the create build trigger method over HTTP.

            Args:
                request (~.cloudbuild.CreateBuildTriggerRequest):
                    The request object. Request to create a new ``BuildTrigger``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.BuildTrigger:
                    Configuration for an automated build
                in response to source repository
                changes.

            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseCreateBuildTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_build_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseCreateBuildTrigger,
                    "_BaseCreateBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.CreateBuildTrigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "CreateBuildTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._CreateBuildTrigger._get_response(
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
            resp = cloudbuild.BuildTrigger()
            pb_resp = cloudbuild.BuildTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_build_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_build_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.BuildTrigger.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.create_build_trigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "CreateBuildTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWorkerPool(
        _BaseCloudBuildRestTransport._BaseCreateWorkerPool, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.CreateWorkerPool")

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
            request: cloudbuild.CreateWorkerPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create worker pool method over HTTP.

            Args:
                request (~.cloudbuild.CreateWorkerPoolRequest):
                    The request object. Request to create a new ``WorkerPool``.
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
                _BaseCloudBuildRestTransport._BaseCreateWorkerPool._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_worker_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseCreateWorkerPool,
                    "_BaseCreateWorkerPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.CreateWorkerPool",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "CreateWorkerPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._CreateWorkerPool._get_response(
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

            resp = self._interceptor.post_create_worker_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_worker_pool_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.create_worker_pool",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "CreateWorkerPool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBuildTrigger(
        _BaseCloudBuildRestTransport._BaseDeleteBuildTrigger, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.DeleteBuildTrigger")

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
            request: cloudbuild.DeleteBuildTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete build trigger method over HTTP.

            Args:
                request (~.cloudbuild.DeleteBuildTriggerRequest):
                    The request object. Request to delete a ``BuildTrigger``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseDeleteBuildTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_build_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseDeleteBuildTrigger,
                    "_BaseDeleteBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.DeleteBuildTrigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "DeleteBuildTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._DeleteBuildTrigger._get_response(
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

    class _DeleteWorkerPool(
        _BaseCloudBuildRestTransport._BaseDeleteWorkerPool, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.DeleteWorkerPool")

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
            request: cloudbuild.DeleteWorkerPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete worker pool method over HTTP.

            Args:
                request (~.cloudbuild.DeleteWorkerPoolRequest):
                    The request object. Request to delete a ``WorkerPool``.
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
                _BaseCloudBuildRestTransport._BaseDeleteWorkerPool._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_worker_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseDeleteWorkerPool,
                    "_BaseDeleteWorkerPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.DeleteWorkerPool",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "DeleteWorkerPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._DeleteWorkerPool._get_response(
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

            resp = self._interceptor.post_delete_worker_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_worker_pool_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.delete_worker_pool",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "DeleteWorkerPool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBuild(_BaseCloudBuildRestTransport._BaseGetBuild, CloudBuildRestStub):
        def __hash__(self):
            return hash("CloudBuildRestTransport.GetBuild")

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
            request: cloudbuild.GetBuildRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.Build:
            r"""Call the get build method over HTTP.

            Args:
                request (~.cloudbuild.GetBuildRequest):
                    The request object. Request to get a build.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.Build:
                    A build resource in the Cloud Build API.

                At a high level, a ``Build`` describes where to find
                source code, how to build it (for example, the builder
                image to run on the source), and where to store the
                built artifacts.

                Fields can include the following variables, which will
                be expanded when the build is created:

                - $PROJECT_ID: the project ID of the build.
                - $PROJECT_NUMBER: the project number of the build.
                - $LOCATION: the location/region of the build.
                - $BUILD_ID: the autogenerated ID of the build.
                - $REPO_NAME: the source repository name specified by
                  RepoSource.
                - $BRANCH_NAME: the branch name specified by RepoSource.
                - $TAG_NAME: the tag name specified by RepoSource.
                - $REVISION_ID or $COMMIT_SHA: the commit SHA specified
                  by RepoSource or resolved from the specified branch or
                  tag.
                - $SHORT_SHA: first 7 characters of $REVISION_ID or
                  $COMMIT_SHA.

            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseGetBuild._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_build(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseGetBuild,
                    "_BaseGetBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.GetBuild",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "GetBuild",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._GetBuild._get_response(
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
            resp = cloudbuild.Build()
            pb_resp = cloudbuild.Build.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_build(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_build_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.Build.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.get_build",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "GetBuild",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBuildTrigger(
        _BaseCloudBuildRestTransport._BaseGetBuildTrigger, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.GetBuildTrigger")

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
            request: cloudbuild.GetBuildTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.BuildTrigger:
            r"""Call the get build trigger method over HTTP.

            Args:
                request (~.cloudbuild.GetBuildTriggerRequest):
                    The request object. Returns the ``BuildTrigger`` with the specified ID.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.BuildTrigger:
                    Configuration for an automated build
                in response to source repository
                changes.

            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseGetBuildTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_build_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseGetBuildTrigger,
                    "_BaseGetBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.GetBuildTrigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "GetBuildTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._GetBuildTrigger._get_response(
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
            resp = cloudbuild.BuildTrigger()
            pb_resp = cloudbuild.BuildTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_build_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_build_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.BuildTrigger.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.get_build_trigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "GetBuildTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDefaultServiceAccount(
        _BaseCloudBuildRestTransport._BaseGetDefaultServiceAccount, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.GetDefaultServiceAccount")

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
            request: cloudbuild.GetDefaultServiceAccountRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.DefaultServiceAccount:
            r"""Call the get default service
            account method over HTTP.

                Args:
                    request (~.cloudbuild.GetDefaultServiceAccountRequest):
                        The request object. Returns the default service account that will be used
                    for ``Builds``.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloudbuild.DefaultServiceAccount:
                        The default service account used for ``Builds``.
            """

            http_options = _BaseCloudBuildRestTransport._BaseGetDefaultServiceAccount._get_http_options()
            request, metadata = self._interceptor.pre_get_default_service_account(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseGetDefaultServiceAccount,
                    "_BaseGetDefaultServiceAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.GetDefaultServiceAccount",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "GetDefaultServiceAccount",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._GetDefaultServiceAccount._get_response(
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
            resp = cloudbuild.DefaultServiceAccount()
            pb_resp = cloudbuild.DefaultServiceAccount.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_default_service_account(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_default_service_account_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.DefaultServiceAccount.to_json(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.get_default_service_account",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "GetDefaultServiceAccount",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkerPool(
        _BaseCloudBuildRestTransport._BaseGetWorkerPool, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.GetWorkerPool")

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
            request: cloudbuild.GetWorkerPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.WorkerPool:
            r"""Call the get worker pool method over HTTP.

            Args:
                request (~.cloudbuild.GetWorkerPoolRequest):
                    The request object. Request to get a ``WorkerPool`` with the specified name.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.WorkerPool:
                    Configuration for a ``WorkerPool``.

                Cloud Build owns and maintains a pool of workers for
                general use and have no access to a project's private
                network. By default, builds submitted to Cloud Build
                will use a worker from this pool.

                If your build needs access to resources on a private
                network, create and use a ``WorkerPool`` to run your
                builds. Private ``WorkerPool``\ s give your builds
                access to any single VPC network that you administer,
                including any on-prem resources connected to that VPC
                network. For an overview of private pools, see `Private
                pools
                overview <https://cloud.google.com/build/docs/private-pools/private-pools-overview>`__.

            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseGetWorkerPool._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_worker_pool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseGetWorkerPool,
                    "_BaseGetWorkerPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.GetWorkerPool",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "GetWorkerPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._GetWorkerPool._get_response(
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
            resp = cloudbuild.WorkerPool()
            pb_resp = cloudbuild.WorkerPool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_worker_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_worker_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.WorkerPool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.get_worker_pool",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "GetWorkerPool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBuilds(_BaseCloudBuildRestTransport._BaseListBuilds, CloudBuildRestStub):
        def __hash__(self):
            return hash("CloudBuildRestTransport.ListBuilds")

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
            request: cloudbuild.ListBuildsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.ListBuildsResponse:
            r"""Call the list builds method over HTTP.

            Args:
                request (~.cloudbuild.ListBuildsRequest):
                    The request object. Request to list builds.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.ListBuildsResponse:
                    Response including listed builds.
            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseListBuilds._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_builds(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseListBuilds,
                    "_BaseListBuilds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.ListBuilds",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ListBuilds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._ListBuilds._get_response(
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
            resp = cloudbuild.ListBuildsResponse()
            pb_resp = cloudbuild.ListBuildsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_builds(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_builds_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.ListBuildsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.list_builds",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ListBuilds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBuildTriggers(
        _BaseCloudBuildRestTransport._BaseListBuildTriggers, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.ListBuildTriggers")

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
            request: cloudbuild.ListBuildTriggersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.ListBuildTriggersResponse:
            r"""Call the list build triggers method over HTTP.

            Args:
                request (~.cloudbuild.ListBuildTriggersRequest):
                    The request object. Request to list existing ``BuildTriggers``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.ListBuildTriggersResponse:
                    Response containing existing ``BuildTriggers``.
            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseListBuildTriggers._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_build_triggers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseListBuildTriggers,
                    "_BaseListBuildTriggers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.ListBuildTriggers",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ListBuildTriggers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._ListBuildTriggers._get_response(
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
            resp = cloudbuild.ListBuildTriggersResponse()
            pb_resp = cloudbuild.ListBuildTriggersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_build_triggers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_build_triggers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.ListBuildTriggersResponse.to_json(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.list_build_triggers",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ListBuildTriggers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkerPools(
        _BaseCloudBuildRestTransport._BaseListWorkerPools, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.ListWorkerPools")

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
            request: cloudbuild.ListWorkerPoolsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.ListWorkerPoolsResponse:
            r"""Call the list worker pools method over HTTP.

            Args:
                request (~.cloudbuild.ListWorkerPoolsRequest):
                    The request object. Request to list ``WorkerPool``\ s.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.ListWorkerPoolsResponse:
                    Response containing existing ``WorkerPools``.
            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseListWorkerPools._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_worker_pools(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseListWorkerPools,
                    "_BaseListWorkerPools__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.ListWorkerPools",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ListWorkerPools",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._ListWorkerPools._get_response(
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
            resp = cloudbuild.ListWorkerPoolsResponse()
            pb_resp = cloudbuild.ListWorkerPoolsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_worker_pools(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_worker_pools_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.ListWorkerPoolsResponse.to_json(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.list_worker_pools",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ListWorkerPools",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReceiveTriggerWebhook(
        _BaseCloudBuildRestTransport._BaseReceiveTriggerWebhook, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.ReceiveTriggerWebhook")

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
            request: cloudbuild.ReceiveTriggerWebhookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.ReceiveTriggerWebhookResponse:
            r"""Call the receive trigger webhook method over HTTP.

            Args:
                request (~.cloudbuild.ReceiveTriggerWebhookRequest):
                    The request object. ReceiveTriggerWebhookRequest [Experimental] is the
                request object accepted by the ReceiveTriggerWebhook
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.ReceiveTriggerWebhookResponse:
                    ReceiveTriggerWebhookResponse [Experimental] is the
                response object for the ReceiveTriggerWebhook method.

            """

            http_options = _BaseCloudBuildRestTransport._BaseReceiveTriggerWebhook._get_http_options()
            request, metadata = self._interceptor.pre_receive_trigger_webhook(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseReceiveTriggerWebhook,
                    "_BaseReceiveTriggerWebhook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.ReceiveTriggerWebhook",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ReceiveTriggerWebhook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._ReceiveTriggerWebhook._get_response(
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
            resp = cloudbuild.ReceiveTriggerWebhookResponse()
            pb_resp = cloudbuild.ReceiveTriggerWebhookResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_receive_trigger_webhook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_receive_trigger_webhook_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.ReceiveTriggerWebhookResponse.to_json(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.receive_trigger_webhook",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "ReceiveTriggerWebhook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RetryBuild(_BaseCloudBuildRestTransport._BaseRetryBuild, CloudBuildRestStub):
        def __hash__(self):
            return hash("CloudBuildRestTransport.RetryBuild")

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
            request: cloudbuild.RetryBuildRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the retry build method over HTTP.

            Args:
                request (~.cloudbuild.RetryBuildRequest):
                    The request object. Specifies a build to retry.
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
                _BaseCloudBuildRestTransport._BaseRetryBuild._get_http_options()
            )
            request, metadata = self._interceptor.pre_retry_build(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseRetryBuild,
                    "_BaseRetryBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.RetryBuild",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "RetryBuild",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._RetryBuild._get_response(
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

            resp = self._interceptor.post_retry_build(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_retry_build_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.retry_build",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "RetryBuild",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunBuildTrigger(
        _BaseCloudBuildRestTransport._BaseRunBuildTrigger, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.RunBuildTrigger")

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
            request: cloudbuild.RunBuildTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run build trigger method over HTTP.

            Args:
                request (~.cloudbuild.RunBuildTriggerRequest):
                    The request object. Specifies a build trigger to run and
                the source to use.
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
                _BaseCloudBuildRestTransport._BaseRunBuildTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_run_build_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseRunBuildTrigger,
                    "_BaseRunBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.RunBuildTrigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "RunBuildTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._RunBuildTrigger._get_response(
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

            resp = self._interceptor.post_run_build_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_build_trigger_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.run_build_trigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "RunBuildTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBuildTrigger(
        _BaseCloudBuildRestTransport._BaseUpdateBuildTrigger, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.UpdateBuildTrigger")

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
            request: cloudbuild.UpdateBuildTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloudbuild.BuildTrigger:
            r"""Call the update build trigger method over HTTP.

            Args:
                request (~.cloudbuild.UpdateBuildTriggerRequest):
                    The request object. Request to update an existing ``BuildTrigger``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloudbuild.BuildTrigger:
                    Configuration for an automated build
                in response to source repository
                changes.

            """

            http_options = (
                _BaseCloudBuildRestTransport._BaseUpdateBuildTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_build_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseUpdateBuildTrigger,
                    "_BaseUpdateBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.UpdateBuildTrigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "UpdateBuildTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._UpdateBuildTrigger._get_response(
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
            resp = cloudbuild.BuildTrigger()
            pb_resp = cloudbuild.BuildTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_build_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_build_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloudbuild.BuildTrigger.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.update_build_trigger",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "UpdateBuildTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateWorkerPool(
        _BaseCloudBuildRestTransport._BaseUpdateWorkerPool, CloudBuildRestStub
    ):
        def __hash__(self):
            return hash("CloudBuildRestTransport.UpdateWorkerPool")

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
            request: cloudbuild.UpdateWorkerPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update worker pool method over HTTP.

            Args:
                request (~.cloudbuild.UpdateWorkerPoolRequest):
                    The request object. Request to update a ``WorkerPool``.
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
                _BaseCloudBuildRestTransport._BaseUpdateWorkerPool._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_worker_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudBuildRestTransport._BaseUpdateWorkerPool,
                    "_BaseUpdateWorkerPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v1.CloudBuildClient.UpdateWorkerPool",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "UpdateWorkerPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudBuildRestTransport._UpdateWorkerPool._get_response(
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

            resp = self._interceptor.post_update_worker_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_worker_pool_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v1.CloudBuildClient.update_worker_pool",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "rpcName": "UpdateWorkerPool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def approve_build(
        self,
    ) -> Callable[[cloudbuild.ApproveBuildRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApproveBuild(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_build(
        self,
    ) -> Callable[[cloudbuild.CancelBuildRequest], cloudbuild.Build]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelBuild(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_build(
        self,
    ) -> Callable[[cloudbuild.CreateBuildRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBuild(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_build_trigger(
        self,
    ) -> Callable[[cloudbuild.CreateBuildTriggerRequest], cloudbuild.BuildTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBuildTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_worker_pool(
        self,
    ) -> Callable[[cloudbuild.CreateWorkerPoolRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWorkerPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_build_trigger(
        self,
    ) -> Callable[[cloudbuild.DeleteBuildTriggerRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBuildTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_worker_pool(
        self,
    ) -> Callable[[cloudbuild.DeleteWorkerPoolRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWorkerPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_build(self) -> Callable[[cloudbuild.GetBuildRequest], cloudbuild.Build]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBuild(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_build_trigger(
        self,
    ) -> Callable[[cloudbuild.GetBuildTriggerRequest], cloudbuild.BuildTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBuildTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_default_service_account(
        self,
    ) -> Callable[
        [cloudbuild.GetDefaultServiceAccountRequest], cloudbuild.DefaultServiceAccount
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDefaultServiceAccount(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_worker_pool(
        self,
    ) -> Callable[[cloudbuild.GetWorkerPoolRequest], cloudbuild.WorkerPool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkerPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_builds(
        self,
    ) -> Callable[[cloudbuild.ListBuildsRequest], cloudbuild.ListBuildsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBuilds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_build_triggers(
        self,
    ) -> Callable[
        [cloudbuild.ListBuildTriggersRequest], cloudbuild.ListBuildTriggersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBuildTriggers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_worker_pools(
        self,
    ) -> Callable[
        [cloudbuild.ListWorkerPoolsRequest], cloudbuild.ListWorkerPoolsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkerPools(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def receive_trigger_webhook(
        self,
    ) -> Callable[
        [cloudbuild.ReceiveTriggerWebhookRequest],
        cloudbuild.ReceiveTriggerWebhookResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReceiveTriggerWebhook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def retry_build(
        self,
    ) -> Callable[[cloudbuild.RetryBuildRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetryBuild(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_build_trigger(
        self,
    ) -> Callable[[cloudbuild.RunBuildTriggerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunBuildTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_build_trigger(
        self,
    ) -> Callable[[cloudbuild.UpdateBuildTriggerRequest], cloudbuild.BuildTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBuildTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_worker_pool(
        self,
    ) -> Callable[[cloudbuild.UpdateWorkerPoolRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateWorkerPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("CloudBuildRestTransport",)
