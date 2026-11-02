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

from google.cloud.deploy_v1._compat import transcode_request
from google.cloud.deploy_v1.types import cloud_deploy

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCloudDeployRestTransport

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


class CloudDeployRestInterceptor:
    """Interceptor for CloudDeploy.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CloudDeployRestTransport.

    .. code-block:: python
        class MyCustomCloudDeployInterceptor(CloudDeployRestInterceptor):
            def pre_abandon_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_abandon_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_advance_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_advance_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_approve_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_approve_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_automation_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_automation_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_automation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_automation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_custom_target_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_custom_target_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_delivery_pipeline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_delivery_pipeline(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_deploy_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deploy_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_target(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_target(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_automation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_automation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_custom_target_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_custom_target_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_delivery_pipeline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_delivery_pipeline(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_deploy_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_deploy_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_target(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_target(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_automation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_automation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_automation_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_automation_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_custom_target_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_custom_target_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_delivery_pipeline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_delivery_pipeline(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deploy_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deploy_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_job_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_job_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_target(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_target(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_ignore_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_ignore_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_automation_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_automation_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_automations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_automations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_custom_target_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_custom_target_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_delivery_pipelines(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_delivery_pipelines(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deploy_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deploy_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_job_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_job_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_releases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_releases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rollouts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rollouts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_targets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_targets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_retry_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retry_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rollback_target(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rollback_target(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_terminate_job_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_terminate_job_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_automation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_automation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_custom_target_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_custom_target_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_delivery_pipeline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_delivery_pipeline(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_deploy_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_deploy_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_target(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_target(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CloudDeployRestTransport(interceptor=MyCustomCloudDeployInterceptor())
        client = CloudDeployClient(transport=transport)


    """

    def pre_abandon_release(
        self,
        request: cloud_deploy.AbandonReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.AbandonReleaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for abandon_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_abandon_release(
        self, response: cloud_deploy.AbandonReleaseResponse
    ) -> cloud_deploy.AbandonReleaseResponse:
        """Post-rpc interceptor for abandon_release

        DEPRECATED. Please use the `post_abandon_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_abandon_release` interceptor runs
        before the `post_abandon_release_with_metadata` interceptor.
        """
        return response

    def post_abandon_release_with_metadata(
        self,
        response: cloud_deploy.AbandonReleaseResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.AbandonReleaseResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for abandon_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_abandon_release_with_metadata`
        interceptor in new development instead of the `post_abandon_release` interceptor.
        When both interceptors are used, this `post_abandon_release_with_metadata` interceptor runs after the
        `post_abandon_release` interceptor. The (possibly modified) response returned by
        `post_abandon_release` will be passed to
        `post_abandon_release_with_metadata`.
        """
        return response, metadata

    def pre_advance_rollout(
        self,
        request: cloud_deploy.AdvanceRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.AdvanceRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for advance_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_advance_rollout(
        self, response: cloud_deploy.AdvanceRolloutResponse
    ) -> cloud_deploy.AdvanceRolloutResponse:
        """Post-rpc interceptor for advance_rollout

        DEPRECATED. Please use the `post_advance_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_advance_rollout` interceptor runs
        before the `post_advance_rollout_with_metadata` interceptor.
        """
        return response

    def post_advance_rollout_with_metadata(
        self,
        response: cloud_deploy.AdvanceRolloutResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.AdvanceRolloutResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for advance_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_advance_rollout_with_metadata`
        interceptor in new development instead of the `post_advance_rollout` interceptor.
        When both interceptors are used, this `post_advance_rollout_with_metadata` interceptor runs after the
        `post_advance_rollout` interceptor. The (possibly modified) response returned by
        `post_advance_rollout` will be passed to
        `post_advance_rollout_with_metadata`.
        """
        return response, metadata

    def pre_approve_rollout(
        self,
        request: cloud_deploy.ApproveRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ApproveRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for approve_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_approve_rollout(
        self, response: cloud_deploy.ApproveRolloutResponse
    ) -> cloud_deploy.ApproveRolloutResponse:
        """Post-rpc interceptor for approve_rollout

        DEPRECATED. Please use the `post_approve_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_approve_rollout` interceptor runs
        before the `post_approve_rollout_with_metadata` interceptor.
        """
        return response

    def post_approve_rollout_with_metadata(
        self,
        response: cloud_deploy.ApproveRolloutResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ApproveRolloutResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for approve_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_approve_rollout_with_metadata`
        interceptor in new development instead of the `post_approve_rollout` interceptor.
        When both interceptors are used, this `post_approve_rollout_with_metadata` interceptor runs after the
        `post_approve_rollout` interceptor. The (possibly modified) response returned by
        `post_approve_rollout` will be passed to
        `post_approve_rollout_with_metadata`.
        """
        return response, metadata

    def pre_cancel_automation_run(
        self,
        request: cloud_deploy.CancelAutomationRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CancelAutomationRunRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_automation_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_cancel_automation_run(
        self, response: cloud_deploy.CancelAutomationRunResponse
    ) -> cloud_deploy.CancelAutomationRunResponse:
        """Post-rpc interceptor for cancel_automation_run

        DEPRECATED. Please use the `post_cancel_automation_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_cancel_automation_run` interceptor runs
        before the `post_cancel_automation_run_with_metadata` interceptor.
        """
        return response

    def post_cancel_automation_run_with_metadata(
        self,
        response: cloud_deploy.CancelAutomationRunResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CancelAutomationRunResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for cancel_automation_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_cancel_automation_run_with_metadata`
        interceptor in new development instead of the `post_cancel_automation_run` interceptor.
        When both interceptors are used, this `post_cancel_automation_run_with_metadata` interceptor runs after the
        `post_cancel_automation_run` interceptor. The (possibly modified) response returned by
        `post_cancel_automation_run` will be passed to
        `post_cancel_automation_run_with_metadata`.
        """
        return response, metadata

    def pre_cancel_rollout(
        self,
        request: cloud_deploy.CancelRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CancelRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_cancel_rollout(
        self, response: cloud_deploy.CancelRolloutResponse
    ) -> cloud_deploy.CancelRolloutResponse:
        """Post-rpc interceptor for cancel_rollout

        DEPRECATED. Please use the `post_cancel_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_cancel_rollout` interceptor runs
        before the `post_cancel_rollout_with_metadata` interceptor.
        """
        return response

    def post_cancel_rollout_with_metadata(
        self,
        response: cloud_deploy.CancelRolloutResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CancelRolloutResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for cancel_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_cancel_rollout_with_metadata`
        interceptor in new development instead of the `post_cancel_rollout` interceptor.
        When both interceptors are used, this `post_cancel_rollout_with_metadata` interceptor runs after the
        `post_cancel_rollout` interceptor. The (possibly modified) response returned by
        `post_cancel_rollout` will be passed to
        `post_cancel_rollout_with_metadata`.
        """
        return response, metadata

    def pre_create_automation(
        self,
        request: cloud_deploy.CreateAutomationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CreateAutomationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_automation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_create_automation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_automation

        DEPRECATED. Please use the `post_create_automation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_create_automation` interceptor runs
        before the `post_create_automation_with_metadata` interceptor.
        """
        return response

    def post_create_automation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_automation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_create_automation_with_metadata`
        interceptor in new development instead of the `post_create_automation` interceptor.
        When both interceptors are used, this `post_create_automation_with_metadata` interceptor runs after the
        `post_create_automation` interceptor. The (possibly modified) response returned by
        `post_create_automation` will be passed to
        `post_create_automation_with_metadata`.
        """
        return response, metadata

    def pre_create_custom_target_type(
        self,
        request: cloud_deploy.CreateCustomTargetTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CreateCustomTargetTypeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_custom_target_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_create_custom_target_type(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_custom_target_type

        DEPRECATED. Please use the `post_create_custom_target_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_create_custom_target_type` interceptor runs
        before the `post_create_custom_target_type_with_metadata` interceptor.
        """
        return response

    def post_create_custom_target_type_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_custom_target_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_create_custom_target_type_with_metadata`
        interceptor in new development instead of the `post_create_custom_target_type` interceptor.
        When both interceptors are used, this `post_create_custom_target_type_with_metadata` interceptor runs after the
        `post_create_custom_target_type` interceptor. The (possibly modified) response returned by
        `post_create_custom_target_type` will be passed to
        `post_create_custom_target_type_with_metadata`.
        """
        return response, metadata

    def pre_create_delivery_pipeline(
        self,
        request: cloud_deploy.CreateDeliveryPipelineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CreateDeliveryPipelineRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_delivery_pipeline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_create_delivery_pipeline(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_delivery_pipeline

        DEPRECATED. Please use the `post_create_delivery_pipeline_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_create_delivery_pipeline` interceptor runs
        before the `post_create_delivery_pipeline_with_metadata` interceptor.
        """
        return response

    def post_create_delivery_pipeline_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_delivery_pipeline

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_create_delivery_pipeline_with_metadata`
        interceptor in new development instead of the `post_create_delivery_pipeline` interceptor.
        When both interceptors are used, this `post_create_delivery_pipeline_with_metadata` interceptor runs after the
        `post_create_delivery_pipeline` interceptor. The (possibly modified) response returned by
        `post_create_delivery_pipeline` will be passed to
        `post_create_delivery_pipeline_with_metadata`.
        """
        return response, metadata

    def pre_create_deploy_policy(
        self,
        request: cloud_deploy.CreateDeployPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CreateDeployPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_deploy_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_create_deploy_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_deploy_policy

        DEPRECATED. Please use the `post_create_deploy_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_create_deploy_policy` interceptor runs
        before the `post_create_deploy_policy_with_metadata` interceptor.
        """
        return response

    def post_create_deploy_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_deploy_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_create_deploy_policy_with_metadata`
        interceptor in new development instead of the `post_create_deploy_policy` interceptor.
        When both interceptors are used, this `post_create_deploy_policy_with_metadata` interceptor runs after the
        `post_create_deploy_policy` interceptor. The (possibly modified) response returned by
        `post_create_deploy_policy` will be passed to
        `post_create_deploy_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_release(
        self,
        request: cloud_deploy.CreateReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CreateReleaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_create_release(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_release

        DEPRECATED. Please use the `post_create_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_create_release` interceptor runs
        before the `post_create_release_with_metadata` interceptor.
        """
        return response

    def post_create_release_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_create_release_with_metadata`
        interceptor in new development instead of the `post_create_release` interceptor.
        When both interceptors are used, this `post_create_release_with_metadata` interceptor runs after the
        `post_create_release` interceptor. The (possibly modified) response returned by
        `post_create_release` will be passed to
        `post_create_release_with_metadata`.
        """
        return response, metadata

    def pre_create_rollout(
        self,
        request: cloud_deploy.CreateRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CreateRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_create_rollout(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_rollout

        DEPRECATED. Please use the `post_create_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_create_rollout` interceptor runs
        before the `post_create_rollout_with_metadata` interceptor.
        """
        return response

    def post_create_rollout_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_create_rollout_with_metadata`
        interceptor in new development instead of the `post_create_rollout` interceptor.
        When both interceptors are used, this `post_create_rollout_with_metadata` interceptor runs after the
        `post_create_rollout` interceptor. The (possibly modified) response returned by
        `post_create_rollout` will be passed to
        `post_create_rollout_with_metadata`.
        """
        return response, metadata

    def pre_create_target(
        self,
        request: cloud_deploy.CreateTargetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.CreateTargetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_target

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_create_target(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_target

        DEPRECATED. Please use the `post_create_target_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_create_target` interceptor runs
        before the `post_create_target_with_metadata` interceptor.
        """
        return response

    def post_create_target_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_target

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_create_target_with_metadata`
        interceptor in new development instead of the `post_create_target` interceptor.
        When both interceptors are used, this `post_create_target_with_metadata` interceptor runs after the
        `post_create_target` interceptor. The (possibly modified) response returned by
        `post_create_target` will be passed to
        `post_create_target_with_metadata`.
        """
        return response, metadata

    def pre_delete_automation(
        self,
        request: cloud_deploy.DeleteAutomationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.DeleteAutomationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_automation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_delete_automation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_automation

        DEPRECATED. Please use the `post_delete_automation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_delete_automation` interceptor runs
        before the `post_delete_automation_with_metadata` interceptor.
        """
        return response

    def post_delete_automation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_automation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_delete_automation_with_metadata`
        interceptor in new development instead of the `post_delete_automation` interceptor.
        When both interceptors are used, this `post_delete_automation_with_metadata` interceptor runs after the
        `post_delete_automation` interceptor. The (possibly modified) response returned by
        `post_delete_automation` will be passed to
        `post_delete_automation_with_metadata`.
        """
        return response, metadata

    def pre_delete_custom_target_type(
        self,
        request: cloud_deploy.DeleteCustomTargetTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.DeleteCustomTargetTypeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_custom_target_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_delete_custom_target_type(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_custom_target_type

        DEPRECATED. Please use the `post_delete_custom_target_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_delete_custom_target_type` interceptor runs
        before the `post_delete_custom_target_type_with_metadata` interceptor.
        """
        return response

    def post_delete_custom_target_type_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_custom_target_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_delete_custom_target_type_with_metadata`
        interceptor in new development instead of the `post_delete_custom_target_type` interceptor.
        When both interceptors are used, this `post_delete_custom_target_type_with_metadata` interceptor runs after the
        `post_delete_custom_target_type` interceptor. The (possibly modified) response returned by
        `post_delete_custom_target_type` will be passed to
        `post_delete_custom_target_type_with_metadata`.
        """
        return response, metadata

    def pre_delete_delivery_pipeline(
        self,
        request: cloud_deploy.DeleteDeliveryPipelineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.DeleteDeliveryPipelineRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_delivery_pipeline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_delete_delivery_pipeline(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_delivery_pipeline

        DEPRECATED. Please use the `post_delete_delivery_pipeline_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_delete_delivery_pipeline` interceptor runs
        before the `post_delete_delivery_pipeline_with_metadata` interceptor.
        """
        return response

    def post_delete_delivery_pipeline_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_delivery_pipeline

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_delete_delivery_pipeline_with_metadata`
        interceptor in new development instead of the `post_delete_delivery_pipeline` interceptor.
        When both interceptors are used, this `post_delete_delivery_pipeline_with_metadata` interceptor runs after the
        `post_delete_delivery_pipeline` interceptor. The (possibly modified) response returned by
        `post_delete_delivery_pipeline` will be passed to
        `post_delete_delivery_pipeline_with_metadata`.
        """
        return response, metadata

    def pre_delete_deploy_policy(
        self,
        request: cloud_deploy.DeleteDeployPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.DeleteDeployPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_deploy_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_delete_deploy_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_deploy_policy

        DEPRECATED. Please use the `post_delete_deploy_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_delete_deploy_policy` interceptor runs
        before the `post_delete_deploy_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_deploy_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_deploy_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_delete_deploy_policy_with_metadata`
        interceptor in new development instead of the `post_delete_deploy_policy` interceptor.
        When both interceptors are used, this `post_delete_deploy_policy_with_metadata` interceptor runs after the
        `post_delete_deploy_policy` interceptor. The (possibly modified) response returned by
        `post_delete_deploy_policy` will be passed to
        `post_delete_deploy_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_target(
        self,
        request: cloud_deploy.DeleteTargetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.DeleteTargetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_target

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_delete_target(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_target

        DEPRECATED. Please use the `post_delete_target_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_delete_target` interceptor runs
        before the `post_delete_target_with_metadata` interceptor.
        """
        return response

    def post_delete_target_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_target

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_delete_target_with_metadata`
        interceptor in new development instead of the `post_delete_target` interceptor.
        When both interceptors are used, this `post_delete_target_with_metadata` interceptor runs after the
        `post_delete_target` interceptor. The (possibly modified) response returned by
        `post_delete_target` will be passed to
        `post_delete_target_with_metadata`.
        """
        return response, metadata

    def pre_get_automation(
        self,
        request: cloud_deploy.GetAutomationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.GetAutomationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_automation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_automation(
        self, response: cloud_deploy.Automation
    ) -> cloud_deploy.Automation:
        """Post-rpc interceptor for get_automation

        DEPRECATED. Please use the `post_get_automation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_automation` interceptor runs
        before the `post_get_automation_with_metadata` interceptor.
        """
        return response

    def post_get_automation_with_metadata(
        self,
        response: cloud_deploy.Automation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.Automation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_automation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_automation_with_metadata`
        interceptor in new development instead of the `post_get_automation` interceptor.
        When both interceptors are used, this `post_get_automation_with_metadata` interceptor runs after the
        `post_get_automation` interceptor. The (possibly modified) response returned by
        `post_get_automation` will be passed to
        `post_get_automation_with_metadata`.
        """
        return response, metadata

    def pre_get_automation_run(
        self,
        request: cloud_deploy.GetAutomationRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.GetAutomationRunRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_automation_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_automation_run(
        self, response: cloud_deploy.AutomationRun
    ) -> cloud_deploy.AutomationRun:
        """Post-rpc interceptor for get_automation_run

        DEPRECATED. Please use the `post_get_automation_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_automation_run` interceptor runs
        before the `post_get_automation_run_with_metadata` interceptor.
        """
        return response

    def post_get_automation_run_with_metadata(
        self,
        response: cloud_deploy.AutomationRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.AutomationRun, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_automation_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_automation_run_with_metadata`
        interceptor in new development instead of the `post_get_automation_run` interceptor.
        When both interceptors are used, this `post_get_automation_run_with_metadata` interceptor runs after the
        `post_get_automation_run` interceptor. The (possibly modified) response returned by
        `post_get_automation_run` will be passed to
        `post_get_automation_run_with_metadata`.
        """
        return response, metadata

    def pre_get_config(
        self,
        request: cloud_deploy.GetConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.GetConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_config(self, response: cloud_deploy.Config) -> cloud_deploy.Config:
        """Post-rpc interceptor for get_config

        DEPRECATED. Please use the `post_get_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_config` interceptor runs
        before the `post_get_config_with_metadata` interceptor.
        """
        return response

    def post_get_config_with_metadata(
        self,
        response: cloud_deploy.Config,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.Config, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_config_with_metadata`
        interceptor in new development instead of the `post_get_config` interceptor.
        When both interceptors are used, this `post_get_config_with_metadata` interceptor runs after the
        `post_get_config` interceptor. The (possibly modified) response returned by
        `post_get_config` will be passed to
        `post_get_config_with_metadata`.
        """
        return response, metadata

    def pre_get_custom_target_type(
        self,
        request: cloud_deploy.GetCustomTargetTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.GetCustomTargetTypeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_custom_target_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_custom_target_type(
        self, response: cloud_deploy.CustomTargetType
    ) -> cloud_deploy.CustomTargetType:
        """Post-rpc interceptor for get_custom_target_type

        DEPRECATED. Please use the `post_get_custom_target_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_custom_target_type` interceptor runs
        before the `post_get_custom_target_type_with_metadata` interceptor.
        """
        return response

    def post_get_custom_target_type_with_metadata(
        self,
        response: cloud_deploy.CustomTargetType,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.CustomTargetType, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_custom_target_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_custom_target_type_with_metadata`
        interceptor in new development instead of the `post_get_custom_target_type` interceptor.
        When both interceptors are used, this `post_get_custom_target_type_with_metadata` interceptor runs after the
        `post_get_custom_target_type` interceptor. The (possibly modified) response returned by
        `post_get_custom_target_type` will be passed to
        `post_get_custom_target_type_with_metadata`.
        """
        return response, metadata

    def pre_get_delivery_pipeline(
        self,
        request: cloud_deploy.GetDeliveryPipelineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.GetDeliveryPipelineRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_delivery_pipeline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_delivery_pipeline(
        self, response: cloud_deploy.DeliveryPipeline
    ) -> cloud_deploy.DeliveryPipeline:
        """Post-rpc interceptor for get_delivery_pipeline

        DEPRECATED. Please use the `post_get_delivery_pipeline_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_delivery_pipeline` interceptor runs
        before the `post_get_delivery_pipeline_with_metadata` interceptor.
        """
        return response

    def post_get_delivery_pipeline_with_metadata(
        self,
        response: cloud_deploy.DeliveryPipeline,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.DeliveryPipeline, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_delivery_pipeline

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_delivery_pipeline_with_metadata`
        interceptor in new development instead of the `post_get_delivery_pipeline` interceptor.
        When both interceptors are used, this `post_get_delivery_pipeline_with_metadata` interceptor runs after the
        `post_get_delivery_pipeline` interceptor. The (possibly modified) response returned by
        `post_get_delivery_pipeline` will be passed to
        `post_get_delivery_pipeline_with_metadata`.
        """
        return response, metadata

    def pre_get_deploy_policy(
        self,
        request: cloud_deploy.GetDeployPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.GetDeployPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_deploy_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_deploy_policy(
        self, response: cloud_deploy.DeployPolicy
    ) -> cloud_deploy.DeployPolicy:
        """Post-rpc interceptor for get_deploy_policy

        DEPRECATED. Please use the `post_get_deploy_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_deploy_policy` interceptor runs
        before the `post_get_deploy_policy_with_metadata` interceptor.
        """
        return response

    def post_get_deploy_policy_with_metadata(
        self,
        response: cloud_deploy.DeployPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.DeployPolicy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deploy_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_deploy_policy_with_metadata`
        interceptor in new development instead of the `post_get_deploy_policy` interceptor.
        When both interceptors are used, this `post_get_deploy_policy_with_metadata` interceptor runs after the
        `post_get_deploy_policy` interceptor. The (possibly modified) response returned by
        `post_get_deploy_policy` will be passed to
        `post_get_deploy_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_job_run(
        self,
        request: cloud_deploy.GetJobRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.GetJobRunRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_job_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_job_run(self, response: cloud_deploy.JobRun) -> cloud_deploy.JobRun:
        """Post-rpc interceptor for get_job_run

        DEPRECATED. Please use the `post_get_job_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_job_run` interceptor runs
        before the `post_get_job_run_with_metadata` interceptor.
        """
        return response

    def post_get_job_run_with_metadata(
        self,
        response: cloud_deploy.JobRun,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.JobRun, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_job_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_job_run_with_metadata`
        interceptor in new development instead of the `post_get_job_run` interceptor.
        When both interceptors are used, this `post_get_job_run_with_metadata` interceptor runs after the
        `post_get_job_run` interceptor. The (possibly modified) response returned by
        `post_get_job_run` will be passed to
        `post_get_job_run_with_metadata`.
        """
        return response, metadata

    def pre_get_release(
        self,
        request: cloud_deploy.GetReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.GetReleaseRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_release(self, response: cloud_deploy.Release) -> cloud_deploy.Release:
        """Post-rpc interceptor for get_release

        DEPRECATED. Please use the `post_get_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_release` interceptor runs
        before the `post_get_release_with_metadata` interceptor.
        """
        return response

    def post_get_release_with_metadata(
        self,
        response: cloud_deploy.Release,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.Release, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_release_with_metadata`
        interceptor in new development instead of the `post_get_release` interceptor.
        When both interceptors are used, this `post_get_release_with_metadata` interceptor runs after the
        `post_get_release` interceptor. The (possibly modified) response returned by
        `post_get_release` will be passed to
        `post_get_release_with_metadata`.
        """
        return response, metadata

    def pre_get_rollout(
        self,
        request: cloud_deploy.GetRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.GetRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_rollout(self, response: cloud_deploy.Rollout) -> cloud_deploy.Rollout:
        """Post-rpc interceptor for get_rollout

        DEPRECATED. Please use the `post_get_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_rollout` interceptor runs
        before the `post_get_rollout_with_metadata` interceptor.
        """
        return response

    def post_get_rollout_with_metadata(
        self,
        response: cloud_deploy.Rollout,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.Rollout, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_rollout_with_metadata`
        interceptor in new development instead of the `post_get_rollout` interceptor.
        When both interceptors are used, this `post_get_rollout_with_metadata` interceptor runs after the
        `post_get_rollout` interceptor. The (possibly modified) response returned by
        `post_get_rollout` will be passed to
        `post_get_rollout_with_metadata`.
        """
        return response, metadata

    def pre_get_target(
        self,
        request: cloud_deploy.GetTargetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.GetTargetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_target

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_target(self, response: cloud_deploy.Target) -> cloud_deploy.Target:
        """Post-rpc interceptor for get_target

        DEPRECATED. Please use the `post_get_target_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_get_target` interceptor runs
        before the `post_get_target_with_metadata` interceptor.
        """
        return response

    def post_get_target_with_metadata(
        self,
        response: cloud_deploy.Target,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.Target, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_target

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_get_target_with_metadata`
        interceptor in new development instead of the `post_get_target` interceptor.
        When both interceptors are used, this `post_get_target_with_metadata` interceptor runs after the
        `post_get_target` interceptor. The (possibly modified) response returned by
        `post_get_target` will be passed to
        `post_get_target_with_metadata`.
        """
        return response, metadata

    def pre_ignore_job(
        self,
        request: cloud_deploy.IgnoreJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.IgnoreJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for ignore_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_ignore_job(
        self, response: cloud_deploy.IgnoreJobResponse
    ) -> cloud_deploy.IgnoreJobResponse:
        """Post-rpc interceptor for ignore_job

        DEPRECATED. Please use the `post_ignore_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_ignore_job` interceptor runs
        before the `post_ignore_job_with_metadata` interceptor.
        """
        return response

    def post_ignore_job_with_metadata(
        self,
        response: cloud_deploy.IgnoreJobResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.IgnoreJobResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for ignore_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_ignore_job_with_metadata`
        interceptor in new development instead of the `post_ignore_job` interceptor.
        When both interceptors are used, this `post_ignore_job_with_metadata` interceptor runs after the
        `post_ignore_job` interceptor. The (possibly modified) response returned by
        `post_ignore_job` will be passed to
        `post_ignore_job_with_metadata`.
        """
        return response, metadata

    def pre_list_automation_runs(
        self,
        request: cloud_deploy.ListAutomationRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListAutomationRunsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_automation_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_automation_runs(
        self, response: cloud_deploy.ListAutomationRunsResponse
    ) -> cloud_deploy.ListAutomationRunsResponse:
        """Post-rpc interceptor for list_automation_runs

        DEPRECATED. Please use the `post_list_automation_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_automation_runs` interceptor runs
        before the `post_list_automation_runs_with_metadata` interceptor.
        """
        return response

    def post_list_automation_runs_with_metadata(
        self,
        response: cloud_deploy.ListAutomationRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListAutomationRunsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_automation_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_automation_runs_with_metadata`
        interceptor in new development instead of the `post_list_automation_runs` interceptor.
        When both interceptors are used, this `post_list_automation_runs_with_metadata` interceptor runs after the
        `post_list_automation_runs` interceptor. The (possibly modified) response returned by
        `post_list_automation_runs` will be passed to
        `post_list_automation_runs_with_metadata`.
        """
        return response, metadata

    def pre_list_automations(
        self,
        request: cloud_deploy.ListAutomationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListAutomationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_automations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_automations(
        self, response: cloud_deploy.ListAutomationsResponse
    ) -> cloud_deploy.ListAutomationsResponse:
        """Post-rpc interceptor for list_automations

        DEPRECATED. Please use the `post_list_automations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_automations` interceptor runs
        before the `post_list_automations_with_metadata` interceptor.
        """
        return response

    def post_list_automations_with_metadata(
        self,
        response: cloud_deploy.ListAutomationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListAutomationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_automations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_automations_with_metadata`
        interceptor in new development instead of the `post_list_automations` interceptor.
        When both interceptors are used, this `post_list_automations_with_metadata` interceptor runs after the
        `post_list_automations` interceptor. The (possibly modified) response returned by
        `post_list_automations` will be passed to
        `post_list_automations_with_metadata`.
        """
        return response, metadata

    def pre_list_custom_target_types(
        self,
        request: cloud_deploy.ListCustomTargetTypesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListCustomTargetTypesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_custom_target_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_custom_target_types(
        self, response: cloud_deploy.ListCustomTargetTypesResponse
    ) -> cloud_deploy.ListCustomTargetTypesResponse:
        """Post-rpc interceptor for list_custom_target_types

        DEPRECATED. Please use the `post_list_custom_target_types_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_custom_target_types` interceptor runs
        before the `post_list_custom_target_types_with_metadata` interceptor.
        """
        return response

    def post_list_custom_target_types_with_metadata(
        self,
        response: cloud_deploy.ListCustomTargetTypesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListCustomTargetTypesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_custom_target_types

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_custom_target_types_with_metadata`
        interceptor in new development instead of the `post_list_custom_target_types` interceptor.
        When both interceptors are used, this `post_list_custom_target_types_with_metadata` interceptor runs after the
        `post_list_custom_target_types` interceptor. The (possibly modified) response returned by
        `post_list_custom_target_types` will be passed to
        `post_list_custom_target_types_with_metadata`.
        """
        return response, metadata

    def pre_list_delivery_pipelines(
        self,
        request: cloud_deploy.ListDeliveryPipelinesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListDeliveryPipelinesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_delivery_pipelines

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_delivery_pipelines(
        self, response: cloud_deploy.ListDeliveryPipelinesResponse
    ) -> cloud_deploy.ListDeliveryPipelinesResponse:
        """Post-rpc interceptor for list_delivery_pipelines

        DEPRECATED. Please use the `post_list_delivery_pipelines_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_delivery_pipelines` interceptor runs
        before the `post_list_delivery_pipelines_with_metadata` interceptor.
        """
        return response

    def post_list_delivery_pipelines_with_metadata(
        self,
        response: cloud_deploy.ListDeliveryPipelinesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListDeliveryPipelinesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_delivery_pipelines

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_delivery_pipelines_with_metadata`
        interceptor in new development instead of the `post_list_delivery_pipelines` interceptor.
        When both interceptors are used, this `post_list_delivery_pipelines_with_metadata` interceptor runs after the
        `post_list_delivery_pipelines` interceptor. The (possibly modified) response returned by
        `post_list_delivery_pipelines` will be passed to
        `post_list_delivery_pipelines_with_metadata`.
        """
        return response, metadata

    def pre_list_deploy_policies(
        self,
        request: cloud_deploy.ListDeployPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListDeployPoliciesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_deploy_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_deploy_policies(
        self, response: cloud_deploy.ListDeployPoliciesResponse
    ) -> cloud_deploy.ListDeployPoliciesResponse:
        """Post-rpc interceptor for list_deploy_policies

        DEPRECATED. Please use the `post_list_deploy_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_deploy_policies` interceptor runs
        before the `post_list_deploy_policies_with_metadata` interceptor.
        """
        return response

    def post_list_deploy_policies_with_metadata(
        self,
        response: cloud_deploy.ListDeployPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListDeployPoliciesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_deploy_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_deploy_policies_with_metadata`
        interceptor in new development instead of the `post_list_deploy_policies` interceptor.
        When both interceptors are used, this `post_list_deploy_policies_with_metadata` interceptor runs after the
        `post_list_deploy_policies` interceptor. The (possibly modified) response returned by
        `post_list_deploy_policies` will be passed to
        `post_list_deploy_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_job_runs(
        self,
        request: cloud_deploy.ListJobRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListJobRunsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_job_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_job_runs(
        self, response: cloud_deploy.ListJobRunsResponse
    ) -> cloud_deploy.ListJobRunsResponse:
        """Post-rpc interceptor for list_job_runs

        DEPRECATED. Please use the `post_list_job_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_job_runs` interceptor runs
        before the `post_list_job_runs_with_metadata` interceptor.
        """
        return response

    def post_list_job_runs_with_metadata(
        self,
        response: cloud_deploy.ListJobRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListJobRunsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_job_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_job_runs_with_metadata`
        interceptor in new development instead of the `post_list_job_runs` interceptor.
        When both interceptors are used, this `post_list_job_runs_with_metadata` interceptor runs after the
        `post_list_job_runs` interceptor. The (possibly modified) response returned by
        `post_list_job_runs` will be passed to
        `post_list_job_runs_with_metadata`.
        """
        return response, metadata

    def pre_list_releases(
        self,
        request: cloud_deploy.ListReleasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListReleasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_releases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_releases(
        self, response: cloud_deploy.ListReleasesResponse
    ) -> cloud_deploy.ListReleasesResponse:
        """Post-rpc interceptor for list_releases

        DEPRECATED. Please use the `post_list_releases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_releases` interceptor runs
        before the `post_list_releases_with_metadata` interceptor.
        """
        return response

    def post_list_releases_with_metadata(
        self,
        response: cloud_deploy.ListReleasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListReleasesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_releases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_releases_with_metadata`
        interceptor in new development instead of the `post_list_releases` interceptor.
        When both interceptors are used, this `post_list_releases_with_metadata` interceptor runs after the
        `post_list_releases` interceptor. The (possibly modified) response returned by
        `post_list_releases` will be passed to
        `post_list_releases_with_metadata`.
        """
        return response, metadata

    def pre_list_rollouts(
        self,
        request: cloud_deploy.ListRolloutsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListRolloutsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_rollouts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_rollouts(
        self, response: cloud_deploy.ListRolloutsResponse
    ) -> cloud_deploy.ListRolloutsResponse:
        """Post-rpc interceptor for list_rollouts

        DEPRECATED. Please use the `post_list_rollouts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_rollouts` interceptor runs
        before the `post_list_rollouts_with_metadata` interceptor.
        """
        return response

    def post_list_rollouts_with_metadata(
        self,
        response: cloud_deploy.ListRolloutsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListRolloutsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_rollouts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_rollouts_with_metadata`
        interceptor in new development instead of the `post_list_rollouts` interceptor.
        When both interceptors are used, this `post_list_rollouts_with_metadata` interceptor runs after the
        `post_list_rollouts` interceptor. The (possibly modified) response returned by
        `post_list_rollouts` will be passed to
        `post_list_rollouts_with_metadata`.
        """
        return response, metadata

    def pre_list_targets(
        self,
        request: cloud_deploy.ListTargetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListTargetsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_targets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_targets(
        self, response: cloud_deploy.ListTargetsResponse
    ) -> cloud_deploy.ListTargetsResponse:
        """Post-rpc interceptor for list_targets

        DEPRECATED. Please use the `post_list_targets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_list_targets` interceptor runs
        before the `post_list_targets_with_metadata` interceptor.
        """
        return response

    def post_list_targets_with_metadata(
        self,
        response: cloud_deploy.ListTargetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.ListTargetsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_targets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_list_targets_with_metadata`
        interceptor in new development instead of the `post_list_targets` interceptor.
        When both interceptors are used, this `post_list_targets_with_metadata` interceptor runs after the
        `post_list_targets` interceptor. The (possibly modified) response returned by
        `post_list_targets` will be passed to
        `post_list_targets_with_metadata`.
        """
        return response, metadata

    def pre_retry_job(
        self,
        request: cloud_deploy.RetryJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.RetryJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for retry_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_retry_job(
        self, response: cloud_deploy.RetryJobResponse
    ) -> cloud_deploy.RetryJobResponse:
        """Post-rpc interceptor for retry_job

        DEPRECATED. Please use the `post_retry_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_retry_job` interceptor runs
        before the `post_retry_job_with_metadata` interceptor.
        """
        return response

    def post_retry_job_with_metadata(
        self,
        response: cloud_deploy.RetryJobResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_deploy.RetryJobResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for retry_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_retry_job_with_metadata`
        interceptor in new development instead of the `post_retry_job` interceptor.
        When both interceptors are used, this `post_retry_job_with_metadata` interceptor runs after the
        `post_retry_job` interceptor. The (possibly modified) response returned by
        `post_retry_job` will be passed to
        `post_retry_job_with_metadata`.
        """
        return response, metadata

    def pre_rollback_target(
        self,
        request: cloud_deploy.RollbackTargetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.RollbackTargetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for rollback_target

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_rollback_target(
        self, response: cloud_deploy.RollbackTargetResponse
    ) -> cloud_deploy.RollbackTargetResponse:
        """Post-rpc interceptor for rollback_target

        DEPRECATED. Please use the `post_rollback_target_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_rollback_target` interceptor runs
        before the `post_rollback_target_with_metadata` interceptor.
        """
        return response

    def post_rollback_target_with_metadata(
        self,
        response: cloud_deploy.RollbackTargetResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.RollbackTargetResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for rollback_target

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_rollback_target_with_metadata`
        interceptor in new development instead of the `post_rollback_target` interceptor.
        When both interceptors are used, this `post_rollback_target_with_metadata` interceptor runs after the
        `post_rollback_target` interceptor. The (possibly modified) response returned by
        `post_rollback_target` will be passed to
        `post_rollback_target_with_metadata`.
        """
        return response, metadata

    def pre_terminate_job_run(
        self,
        request: cloud_deploy.TerminateJobRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.TerminateJobRunRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for terminate_job_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_terminate_job_run(
        self, response: cloud_deploy.TerminateJobRunResponse
    ) -> cloud_deploy.TerminateJobRunResponse:
        """Post-rpc interceptor for terminate_job_run

        DEPRECATED. Please use the `post_terminate_job_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_terminate_job_run` interceptor runs
        before the `post_terminate_job_run_with_metadata` interceptor.
        """
        return response

    def post_terminate_job_run_with_metadata(
        self,
        response: cloud_deploy.TerminateJobRunResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.TerminateJobRunResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for terminate_job_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_terminate_job_run_with_metadata`
        interceptor in new development instead of the `post_terminate_job_run` interceptor.
        When both interceptors are used, this `post_terminate_job_run_with_metadata` interceptor runs after the
        `post_terminate_job_run` interceptor. The (possibly modified) response returned by
        `post_terminate_job_run` will be passed to
        `post_terminate_job_run_with_metadata`.
        """
        return response, metadata

    def pre_update_automation(
        self,
        request: cloud_deploy.UpdateAutomationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.UpdateAutomationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_automation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_update_automation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_automation

        DEPRECATED. Please use the `post_update_automation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_update_automation` interceptor runs
        before the `post_update_automation_with_metadata` interceptor.
        """
        return response

    def post_update_automation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_automation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_update_automation_with_metadata`
        interceptor in new development instead of the `post_update_automation` interceptor.
        When both interceptors are used, this `post_update_automation_with_metadata` interceptor runs after the
        `post_update_automation` interceptor. The (possibly modified) response returned by
        `post_update_automation` will be passed to
        `post_update_automation_with_metadata`.
        """
        return response, metadata

    def pre_update_custom_target_type(
        self,
        request: cloud_deploy.UpdateCustomTargetTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.UpdateCustomTargetTypeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_custom_target_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_update_custom_target_type(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_custom_target_type

        DEPRECATED. Please use the `post_update_custom_target_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_update_custom_target_type` interceptor runs
        before the `post_update_custom_target_type_with_metadata` interceptor.
        """
        return response

    def post_update_custom_target_type_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_custom_target_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_update_custom_target_type_with_metadata`
        interceptor in new development instead of the `post_update_custom_target_type` interceptor.
        When both interceptors are used, this `post_update_custom_target_type_with_metadata` interceptor runs after the
        `post_update_custom_target_type` interceptor. The (possibly modified) response returned by
        `post_update_custom_target_type` will be passed to
        `post_update_custom_target_type_with_metadata`.
        """
        return response, metadata

    def pre_update_delivery_pipeline(
        self,
        request: cloud_deploy.UpdateDeliveryPipelineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.UpdateDeliveryPipelineRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_delivery_pipeline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_update_delivery_pipeline(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_delivery_pipeline

        DEPRECATED. Please use the `post_update_delivery_pipeline_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_update_delivery_pipeline` interceptor runs
        before the `post_update_delivery_pipeline_with_metadata` interceptor.
        """
        return response

    def post_update_delivery_pipeline_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_delivery_pipeline

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_update_delivery_pipeline_with_metadata`
        interceptor in new development instead of the `post_update_delivery_pipeline` interceptor.
        When both interceptors are used, this `post_update_delivery_pipeline_with_metadata` interceptor runs after the
        `post_update_delivery_pipeline` interceptor. The (possibly modified) response returned by
        `post_update_delivery_pipeline` will be passed to
        `post_update_delivery_pipeline_with_metadata`.
        """
        return response, metadata

    def pre_update_deploy_policy(
        self,
        request: cloud_deploy.UpdateDeployPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.UpdateDeployPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_deploy_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_update_deploy_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_deploy_policy

        DEPRECATED. Please use the `post_update_deploy_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_update_deploy_policy` interceptor runs
        before the `post_update_deploy_policy_with_metadata` interceptor.
        """
        return response

    def post_update_deploy_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_deploy_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_update_deploy_policy_with_metadata`
        interceptor in new development instead of the `post_update_deploy_policy` interceptor.
        When both interceptors are used, this `post_update_deploy_policy_with_metadata` interceptor runs after the
        `post_update_deploy_policy` interceptor. The (possibly modified) response returned by
        `post_update_deploy_policy` will be passed to
        `post_update_deploy_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_target(
        self,
        request: cloud_deploy.UpdateTargetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_deploy.UpdateTargetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_target

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_update_target(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_target

        DEPRECATED. Please use the `post_update_target_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code. This `post_update_target` interceptor runs
        before the `post_update_target_with_metadata` interceptor.
        """
        return response

    def post_update_target_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_target

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudDeploy server but before it is returned to user code.

        We recommend only using this `post_update_target_with_metadata`
        interceptor in new development instead of the `post_update_target` interceptor.
        When both interceptors are used, this `post_update_target_with_metadata` interceptor runs after the
        `post_update_target` interceptor. The (possibly modified) response returned by
        `post_update_target` will be passed to
        `post_update_target_with_metadata`.
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
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
        before they are sent to the CloudDeploy server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the CloudDeploy server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CloudDeployRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CloudDeployRestInterceptor


class CloudDeployRestTransport(_BaseCloudDeployRestTransport):
    """REST backend synchronous transport for CloudDeploy.

    CloudDeploy service creates and manages Continuous Delivery
    operations on Google Cloud Platform via Skaffold
    (https://skaffold.dev).

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "clouddeploy.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CloudDeployRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'clouddeploy.googleapis.com').
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
            interceptor (Optional[CloudDeployRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CloudDeployRestInterceptor()
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

    class _AbandonRelease(
        _BaseCloudDeployRestTransport._BaseAbandonRelease, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.AbandonRelease")

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
            request: cloud_deploy.AbandonReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.AbandonReleaseResponse:
            r"""Call the abandon release method over HTTP.

            Args:
                request (~.cloud_deploy.AbandonReleaseRequest):
                    The request object. The request object used by ``AbandonRelease``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.AbandonReleaseResponse:
                    The response object for ``AbandonRelease``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseAbandonRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_abandon_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseAbandonRelease,
                    "_BaseAbandonRelease__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.AbandonRelease",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "AbandonRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._AbandonRelease._get_response(
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
            resp = cloud_deploy.AbandonReleaseResponse()
            pb_resp = cloud_deploy.AbandonReleaseResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_abandon_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_abandon_release_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.AbandonReleaseResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.abandon_release",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "AbandonRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AdvanceRollout(
        _BaseCloudDeployRestTransport._BaseAdvanceRollout, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.AdvanceRollout")

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
            request: cloud_deploy.AdvanceRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.AdvanceRolloutResponse:
            r"""Call the advance rollout method over HTTP.

            Args:
                request (~.cloud_deploy.AdvanceRolloutRequest):
                    The request object. The request object used by ``AdvanceRollout``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.AdvanceRolloutResponse:
                    The response object from ``AdvanceRollout``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseAdvanceRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_advance_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseAdvanceRollout,
                    "_BaseAdvanceRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.AdvanceRollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "AdvanceRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._AdvanceRollout._get_response(
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
            resp = cloud_deploy.AdvanceRolloutResponse()
            pb_resp = cloud_deploy.AdvanceRolloutResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_advance_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_advance_rollout_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.AdvanceRolloutResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.advance_rollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "AdvanceRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ApproveRollout(
        _BaseCloudDeployRestTransport._BaseApproveRollout, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ApproveRollout")

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
            request: cloud_deploy.ApproveRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ApproveRolloutResponse:
            r"""Call the approve rollout method over HTTP.

            Args:
                request (~.cloud_deploy.ApproveRolloutRequest):
                    The request object. The request object used by ``ApproveRollout``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ApproveRolloutResponse:
                    The response object from ``ApproveRollout``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseApproveRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_approve_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseApproveRollout,
                    "_BaseApproveRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ApproveRollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ApproveRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ApproveRollout._get_response(
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
            resp = cloud_deploy.ApproveRolloutResponse()
            pb_resp = cloud_deploy.ApproveRolloutResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_approve_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_approve_rollout_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.ApproveRolloutResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.approve_rollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ApproveRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CancelAutomationRun(
        _BaseCloudDeployRestTransport._BaseCancelAutomationRun, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CancelAutomationRun")

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
            request: cloud_deploy.CancelAutomationRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.CancelAutomationRunResponse:
            r"""Call the cancel automation run method over HTTP.

            Args:
                request (~.cloud_deploy.CancelAutomationRunRequest):
                    The request object. The request object used by ``CancelAutomationRun``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.CancelAutomationRunResponse:
                    The response object from ``CancelAutomationRun``.
            """

            http_options = _BaseCloudDeployRestTransport._BaseCancelAutomationRun._get_http_options()
            request, metadata = self._interceptor.pre_cancel_automation_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCancelAutomationRun,
                    "_BaseCancelAutomationRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CancelAutomationRun",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CancelAutomationRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CancelAutomationRun._get_response(
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
            resp = cloud_deploy.CancelAutomationRunResponse()
            pb_resp = cloud_deploy.CancelAutomationRunResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_cancel_automation_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_automation_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.CancelAutomationRunResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.cancel_automation_run",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CancelAutomationRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CancelRollout(
        _BaseCloudDeployRestTransport._BaseCancelRollout, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CancelRollout")

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
            request: cloud_deploy.CancelRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.CancelRolloutResponse:
            r"""Call the cancel rollout method over HTTP.

            Args:
                request (~.cloud_deploy.CancelRolloutRequest):
                    The request object. The request object used by ``CancelRollout``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.CancelRolloutResponse:
                    The response object from ``CancelRollout``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseCancelRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCancelRollout,
                    "_BaseCancelRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CancelRollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CancelRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CancelRollout._get_response(
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
            resp = cloud_deploy.CancelRolloutResponse()
            pb_resp = cloud_deploy.CancelRolloutResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_cancel_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_rollout_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.CancelRolloutResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.cancel_rollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CancelRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAutomation(
        _BaseCloudDeployRestTransport._BaseCreateAutomation, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CreateAutomation")

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
            request: cloud_deploy.CreateAutomationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create automation method over HTTP.

            Args:
                request (~.cloud_deploy.CreateAutomationRequest):
                    The request object. The request object for ``CreateAutomation``.
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
                _BaseCloudDeployRestTransport._BaseCreateAutomation._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_automation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCreateAutomation,
                    "_BaseCreateAutomation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CreateAutomation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateAutomation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CreateAutomation._get_response(
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

            resp = self._interceptor.post_create_automation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_automation_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.create_automation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateAutomation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCustomTargetType(
        _BaseCloudDeployRestTransport._BaseCreateCustomTargetType, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CreateCustomTargetType")

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
            request: cloud_deploy.CreateCustomTargetTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create custom target type method over HTTP.

            Args:
                request (~.cloud_deploy.CreateCustomTargetTypeRequest):
                    The request object. The request object for ``CreateCustomTargetType``.
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

            http_options = _BaseCloudDeployRestTransport._BaseCreateCustomTargetType._get_http_options()
            request, metadata = self._interceptor.pre_create_custom_target_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCreateCustomTargetType,
                    "_BaseCreateCustomTargetType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CreateCustomTargetType",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateCustomTargetType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CreateCustomTargetType._get_response(
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

            resp = self._interceptor.post_create_custom_target_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_custom_target_type_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.create_custom_target_type",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateCustomTargetType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDeliveryPipeline(
        _BaseCloudDeployRestTransport._BaseCreateDeliveryPipeline, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CreateDeliveryPipeline")

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
            request: cloud_deploy.CreateDeliveryPipelineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create delivery pipeline method over HTTP.

            Args:
                request (~.cloud_deploy.CreateDeliveryPipelineRequest):
                    The request object. The request object for ``CreateDeliveryPipeline``.
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

            http_options = _BaseCloudDeployRestTransport._BaseCreateDeliveryPipeline._get_http_options()
            request, metadata = self._interceptor.pre_create_delivery_pipeline(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCreateDeliveryPipeline,
                    "_BaseCreateDeliveryPipeline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CreateDeliveryPipeline",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateDeliveryPipeline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CreateDeliveryPipeline._get_response(
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

            resp = self._interceptor.post_create_delivery_pipeline(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_delivery_pipeline_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.create_delivery_pipeline",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateDeliveryPipeline",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDeployPolicy(
        _BaseCloudDeployRestTransport._BaseCreateDeployPolicy, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CreateDeployPolicy")

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
            request: cloud_deploy.CreateDeployPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create deploy policy method over HTTP.

            Args:
                request (~.cloud_deploy.CreateDeployPolicyRequest):
                    The request object. The request object for ``CreateDeployPolicy``.
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

            http_options = _BaseCloudDeployRestTransport._BaseCreateDeployPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_deploy_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCreateDeployPolicy,
                    "_BaseCreateDeployPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CreateDeployPolicy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateDeployPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CreateDeployPolicy._get_response(
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

            resp = self._interceptor.post_create_deploy_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_deploy_policy_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.create_deploy_policy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateDeployPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRelease(
        _BaseCloudDeployRestTransport._BaseCreateRelease, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CreateRelease")

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
            request: cloud_deploy.CreateReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create release method over HTTP.

            Args:
                request (~.cloud_deploy.CreateReleaseRequest):
                    The request object. The request object for ``CreateRelease``,
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
                _BaseCloudDeployRestTransport._BaseCreateRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCreateRelease,
                    "_BaseCreateRelease__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CreateRelease",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CreateRelease._get_response(
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

            resp = self._interceptor.post_create_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_release_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.create_release",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRollout(
        _BaseCloudDeployRestTransport._BaseCreateRollout, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CreateRollout")

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
            request: cloud_deploy.CreateRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create rollout method over HTTP.

            Args:
                request (~.cloud_deploy.CreateRolloutRequest):
                    The request object. CreateRolloutRequest is the request object used by
                ``CreateRollout``.
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
                _BaseCloudDeployRestTransport._BaseCreateRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCreateRollout,
                    "_BaseCreateRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CreateRollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CreateRollout._get_response(
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

            resp = self._interceptor.post_create_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_rollout_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.create_rollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTarget(
        _BaseCloudDeployRestTransport._BaseCreateTarget, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CreateTarget")

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
            request: cloud_deploy.CreateTargetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create target method over HTTP.

            Args:
                request (~.cloud_deploy.CreateTargetRequest):
                    The request object. The request object for ``CreateTarget``.
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
                _BaseCloudDeployRestTransport._BaseCreateTarget._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_target(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCreateTarget,
                    "_BaseCreateTarget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CreateTarget",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateTarget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CreateTarget._get_response(
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

            resp = self._interceptor.post_create_target(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_target_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.create_target",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CreateTarget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAutomation(
        _BaseCloudDeployRestTransport._BaseDeleteAutomation, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.DeleteAutomation")

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
            request: cloud_deploy.DeleteAutomationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete automation method over HTTP.

            Args:
                request (~.cloud_deploy.DeleteAutomationRequest):
                    The request object. The request object for ``DeleteAutomation``.
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
                _BaseCloudDeployRestTransport._BaseDeleteAutomation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_automation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseDeleteAutomation,
                    "_BaseDeleteAutomation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.DeleteAutomation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteAutomation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._DeleteAutomation._get_response(
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

            resp = self._interceptor.post_delete_automation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_automation_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.delete_automation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteAutomation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCustomTargetType(
        _BaseCloudDeployRestTransport._BaseDeleteCustomTargetType, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.DeleteCustomTargetType")

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
            request: cloud_deploy.DeleteCustomTargetTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete custom target type method over HTTP.

            Args:
                request (~.cloud_deploy.DeleteCustomTargetTypeRequest):
                    The request object. The request object for ``DeleteCustomTargetType``.
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

            http_options = _BaseCloudDeployRestTransport._BaseDeleteCustomTargetType._get_http_options()
            request, metadata = self._interceptor.pre_delete_custom_target_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseDeleteCustomTargetType,
                    "_BaseDeleteCustomTargetType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.DeleteCustomTargetType",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteCustomTargetType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._DeleteCustomTargetType._get_response(
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

            resp = self._interceptor.post_delete_custom_target_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_custom_target_type_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.delete_custom_target_type",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteCustomTargetType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDeliveryPipeline(
        _BaseCloudDeployRestTransport._BaseDeleteDeliveryPipeline, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.DeleteDeliveryPipeline")

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
            request: cloud_deploy.DeleteDeliveryPipelineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete delivery pipeline method over HTTP.

            Args:
                request (~.cloud_deploy.DeleteDeliveryPipelineRequest):
                    The request object. The request object for ``DeleteDeliveryPipeline``.
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

            http_options = _BaseCloudDeployRestTransport._BaseDeleteDeliveryPipeline._get_http_options()
            request, metadata = self._interceptor.pre_delete_delivery_pipeline(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseDeleteDeliveryPipeline,
                    "_BaseDeleteDeliveryPipeline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.DeleteDeliveryPipeline",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteDeliveryPipeline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._DeleteDeliveryPipeline._get_response(
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

            resp = self._interceptor.post_delete_delivery_pipeline(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_delivery_pipeline_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.delete_delivery_pipeline",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteDeliveryPipeline",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDeployPolicy(
        _BaseCloudDeployRestTransport._BaseDeleteDeployPolicy, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.DeleteDeployPolicy")

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
            request: cloud_deploy.DeleteDeployPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete deploy policy method over HTTP.

            Args:
                request (~.cloud_deploy.DeleteDeployPolicyRequest):
                    The request object. The request object for ``DeleteDeployPolicy``.
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

            http_options = _BaseCloudDeployRestTransport._BaseDeleteDeployPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_deploy_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseDeleteDeployPolicy,
                    "_BaseDeleteDeployPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.DeleteDeployPolicy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteDeployPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._DeleteDeployPolicy._get_response(
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

            resp = self._interceptor.post_delete_deploy_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_deploy_policy_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.delete_deploy_policy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteDeployPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTarget(
        _BaseCloudDeployRestTransport._BaseDeleteTarget, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.DeleteTarget")

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
            request: cloud_deploy.DeleteTargetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete target method over HTTP.

            Args:
                request (~.cloud_deploy.DeleteTargetRequest):
                    The request object. The request object for ``DeleteTarget``.
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
                _BaseCloudDeployRestTransport._BaseDeleteTarget._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_target(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseDeleteTarget,
                    "_BaseDeleteTarget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.DeleteTarget",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteTarget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._DeleteTarget._get_response(
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

            resp = self._interceptor.post_delete_target(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_target_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.delete_target",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteTarget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAutomation(
        _BaseCloudDeployRestTransport._BaseGetAutomation, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetAutomation")

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
            request: cloud_deploy.GetAutomationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.Automation:
            r"""Call the get automation method over HTTP.

            Args:
                request (~.cloud_deploy.GetAutomationRequest):
                    The request object. The request object for ``GetAutomation``
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.Automation:
                    An ``Automation`` resource in the Cloud Deploy API.

                An ``Automation`` enables the automation of manually
                driven actions for a Delivery Pipeline, which includes
                Release promotion among Targets, Rollout repair and
                Rollout deployment strategy advancement. The intention
                of Automation is to reduce manual intervention in the
                continuous delivery process.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseGetAutomation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_automation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetAutomation,
                    "_BaseGetAutomation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetAutomation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetAutomation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetAutomation._get_response(
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
            resp = cloud_deploy.Automation()
            pb_resp = cloud_deploy.Automation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_automation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_automation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.Automation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_automation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetAutomation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAutomationRun(
        _BaseCloudDeployRestTransport._BaseGetAutomationRun, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetAutomationRun")

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
            request: cloud_deploy.GetAutomationRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.AutomationRun:
            r"""Call the get automation run method over HTTP.

            Args:
                request (~.cloud_deploy.GetAutomationRunRequest):
                    The request object. The request object for ``GetAutomationRun``
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.AutomationRun:
                    An ``AutomationRun`` resource in the Cloud Deploy API.

                An ``AutomationRun`` represents an execution instance of
                an automation rule.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseGetAutomationRun._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_automation_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetAutomationRun,
                    "_BaseGetAutomationRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetAutomationRun",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetAutomationRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetAutomationRun._get_response(
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
            resp = cloud_deploy.AutomationRun()
            pb_resp = cloud_deploy.AutomationRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_automation_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_automation_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.AutomationRun.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_automation_run",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetAutomationRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConfig(_BaseCloudDeployRestTransport._BaseGetConfig, CloudDeployRestStub):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetConfig")

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
            request: cloud_deploy.GetConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.Config:
            r"""Call the get config method over HTTP.

            Args:
                request (~.cloud_deploy.GetConfigRequest):
                    The request object. Request to get a configuration.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.Config:
                    Service-wide configuration.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseGetConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetConfig,
                    "_BaseGetConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetConfig",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetConfig._get_response(
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
            resp = cloud_deploy.Config()
            pb_resp = cloud_deploy.Config.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.Config.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_config",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCustomTargetType(
        _BaseCloudDeployRestTransport._BaseGetCustomTargetType, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetCustomTargetType")

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
            request: cloud_deploy.GetCustomTargetTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.CustomTargetType:
            r"""Call the get custom target type method over HTTP.

            Args:
                request (~.cloud_deploy.GetCustomTargetTypeRequest):
                    The request object. The request object for ``GetCustomTargetType``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.CustomTargetType:
                    A ``CustomTargetType`` resource in the Cloud Deploy API.

                A ``CustomTargetType`` defines a type of custom target
                that can be referenced in a ``Target`` in order to
                facilitate deploying to other systems besides the
                supported runtimes.

            """

            http_options = _BaseCloudDeployRestTransport._BaseGetCustomTargetType._get_http_options()
            request, metadata = self._interceptor.pre_get_custom_target_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetCustomTargetType,
                    "_BaseGetCustomTargetType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetCustomTargetType",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetCustomTargetType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetCustomTargetType._get_response(
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
            resp = cloud_deploy.CustomTargetType()
            pb_resp = cloud_deploy.CustomTargetType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_custom_target_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_custom_target_type_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.CustomTargetType.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_custom_target_type",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetCustomTargetType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeliveryPipeline(
        _BaseCloudDeployRestTransport._BaseGetDeliveryPipeline, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetDeliveryPipeline")

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
            request: cloud_deploy.GetDeliveryPipelineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.DeliveryPipeline:
            r"""Call the get delivery pipeline method over HTTP.

            Args:
                request (~.cloud_deploy.GetDeliveryPipelineRequest):
                    The request object. The request object for ``GetDeliveryPipeline``
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.DeliveryPipeline:
                    A ``DeliveryPipeline`` resource in the Cloud Deploy API.

                A ``DeliveryPipeline`` defines a pipeline through which
                a Skaffold configuration can progress.

            """

            http_options = _BaseCloudDeployRestTransport._BaseGetDeliveryPipeline._get_http_options()
            request, metadata = self._interceptor.pre_get_delivery_pipeline(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetDeliveryPipeline,
                    "_BaseGetDeliveryPipeline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetDeliveryPipeline",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetDeliveryPipeline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetDeliveryPipeline._get_response(
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
            resp = cloud_deploy.DeliveryPipeline()
            pb_resp = cloud_deploy.DeliveryPipeline.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_delivery_pipeline(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_delivery_pipeline_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.DeliveryPipeline.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_delivery_pipeline",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetDeliveryPipeline",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeployPolicy(
        _BaseCloudDeployRestTransport._BaseGetDeployPolicy, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetDeployPolicy")

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
            request: cloud_deploy.GetDeployPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.DeployPolicy:
            r"""Call the get deploy policy method over HTTP.

            Args:
                request (~.cloud_deploy.GetDeployPolicyRequest):
                    The request object. The request object for ``GetDeployPolicy``
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.DeployPolicy:
                    A ``DeployPolicy`` resource in the Cloud Deploy API.

                A ``DeployPolicy`` inhibits manual or automation-driven
                actions within a Delivery Pipeline or Target.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseGetDeployPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_deploy_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetDeployPolicy,
                    "_BaseGetDeployPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetDeployPolicy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetDeployPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetDeployPolicy._get_response(
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
            resp = cloud_deploy.DeployPolicy()
            pb_resp = cloud_deploy.DeployPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_deploy_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_deploy_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.DeployPolicy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_deploy_policy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetDeployPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetJobRun(_BaseCloudDeployRestTransport._BaseGetJobRun, CloudDeployRestStub):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetJobRun")

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
            request: cloud_deploy.GetJobRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.JobRun:
            r"""Call the get job run method over HTTP.

            Args:
                request (~.cloud_deploy.GetJobRunRequest):
                    The request object. GetJobRunRequest is the request object used by
                ``GetJobRun``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.JobRun:
                    A ``JobRun`` resource in the Cloud Deploy API.

                A ``JobRun`` contains information of a single
                ``Rollout`` job evaluation.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseGetJobRun._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_job_run(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetJobRun,
                    "_BaseGetJobRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetJobRun",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetJobRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetJobRun._get_response(
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
            resp = cloud_deploy.JobRun()
            pb_resp = cloud_deploy.JobRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_job_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_job_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.JobRun.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_job_run",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetJobRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRelease(
        _BaseCloudDeployRestTransport._BaseGetRelease, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetRelease")

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
            request: cloud_deploy.GetReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.Release:
            r"""Call the get release method over HTTP.

            Args:
                request (~.cloud_deploy.GetReleaseRequest):
                    The request object. The request object for ``GetRelease``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.Release:
                    A ``Release`` resource in the Cloud Deploy API.

                A ``Release`` defines a specific Skaffold configuration
                instance that can be deployed.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseGetRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetRelease,
                    "_BaseGetRelease__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetRelease",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetRelease._get_response(
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
            resp = cloud_deploy.Release()
            pb_resp = cloud_deploy.Release.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_release_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.Release.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_release",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRollout(
        _BaseCloudDeployRestTransport._BaseGetRollout, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetRollout")

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
            request: cloud_deploy.GetRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.Rollout:
            r"""Call the get rollout method over HTTP.

            Args:
                request (~.cloud_deploy.GetRolloutRequest):
                    The request object. GetRolloutRequest is the request object used by
                ``GetRollout``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.Rollout:
                    A ``Rollout`` resource in the Cloud Deploy API.

                A ``Rollout`` contains information around a specific
                deployment to a ``Target``.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseGetRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetRollout,
                    "_BaseGetRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetRollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetRollout._get_response(
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
            resp = cloud_deploy.Rollout()
            pb_resp = cloud_deploy.Rollout.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_rollout_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.Rollout.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_rollout",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTarget(_BaseCloudDeployRestTransport._BaseGetTarget, CloudDeployRestStub):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetTarget")

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
            request: cloud_deploy.GetTargetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.Target:
            r"""Call the get target method over HTTP.

            Args:
                request (~.cloud_deploy.GetTargetRequest):
                    The request object. The request object for ``GetTarget``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.Target:
                    A ``Target`` resource in the Cloud Deploy API.

                A ``Target`` defines a location to which a Skaffold
                configuration can be deployed.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseGetTarget._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_target(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetTarget,
                    "_BaseGetTarget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetTarget",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetTarget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetTarget._get_response(
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
            resp = cloud_deploy.Target()
            pb_resp = cloud_deploy.Target.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_target(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_target_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.Target.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.get_target",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetTarget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _IgnoreJob(_BaseCloudDeployRestTransport._BaseIgnoreJob, CloudDeployRestStub):
        def __hash__(self):
            return hash("CloudDeployRestTransport.IgnoreJob")

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
            request: cloud_deploy.IgnoreJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.IgnoreJobResponse:
            r"""Call the ignore job method over HTTP.

            Args:
                request (~.cloud_deploy.IgnoreJobRequest):
                    The request object. The request object used by ``IgnoreJob``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.IgnoreJobResponse:
                    The response object from ``IgnoreJob``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseIgnoreJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_ignore_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseIgnoreJob,
                    "_BaseIgnoreJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.IgnoreJob",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "IgnoreJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._IgnoreJob._get_response(
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
            resp = cloud_deploy.IgnoreJobResponse()
            pb_resp = cloud_deploy.IgnoreJobResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_ignore_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_ignore_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.IgnoreJobResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.ignore_job",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "IgnoreJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAutomationRuns(
        _BaseCloudDeployRestTransport._BaseListAutomationRuns, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListAutomationRuns")

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
            request: cloud_deploy.ListAutomationRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListAutomationRunsResponse:
            r"""Call the list automation runs method over HTTP.

            Args:
                request (~.cloud_deploy.ListAutomationRunsRequest):
                    The request object. The request object for ``ListAutomationRuns``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListAutomationRunsResponse:
                    The response object from ``ListAutomationRuns``.
            """

            http_options = _BaseCloudDeployRestTransport._BaseListAutomationRuns._get_http_options()
            request, metadata = self._interceptor.pre_list_automation_runs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListAutomationRuns,
                    "_BaseListAutomationRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListAutomationRuns",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListAutomationRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListAutomationRuns._get_response(
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
            resp = cloud_deploy.ListAutomationRunsResponse()
            pb_resp = cloud_deploy.ListAutomationRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_automation_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_automation_runs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.ListAutomationRunsResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_automation_runs",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListAutomationRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAutomations(
        _BaseCloudDeployRestTransport._BaseListAutomations, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListAutomations")

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
            request: cloud_deploy.ListAutomationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListAutomationsResponse:
            r"""Call the list automations method over HTTP.

            Args:
                request (~.cloud_deploy.ListAutomationsRequest):
                    The request object. The request object for ``ListAutomations``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListAutomationsResponse:
                    The response object from ``ListAutomations``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseListAutomations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_automations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListAutomations,
                    "_BaseListAutomations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListAutomations",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListAutomations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListAutomations._get_response(
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
            resp = cloud_deploy.ListAutomationsResponse()
            pb_resp = cloud_deploy.ListAutomationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_automations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_automations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.ListAutomationsResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_automations",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListAutomations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCustomTargetTypes(
        _BaseCloudDeployRestTransport._BaseListCustomTargetTypes, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListCustomTargetTypes")

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
            request: cloud_deploy.ListCustomTargetTypesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListCustomTargetTypesResponse:
            r"""Call the list custom target types method over HTTP.

            Args:
                request (~.cloud_deploy.ListCustomTargetTypesRequest):
                    The request object. The request object for ``ListCustomTargetTypes``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListCustomTargetTypesResponse:
                    The response object from ``ListCustomTargetTypes.``
            """

            http_options = _BaseCloudDeployRestTransport._BaseListCustomTargetTypes._get_http_options()
            request, metadata = self._interceptor.pre_list_custom_target_types(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListCustomTargetTypes,
                    "_BaseListCustomTargetTypes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListCustomTargetTypes",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListCustomTargetTypes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListCustomTargetTypes._get_response(
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
            resp = cloud_deploy.ListCustomTargetTypesResponse()
            pb_resp = cloud_deploy.ListCustomTargetTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_custom_target_types(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_custom_target_types_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_deploy.ListCustomTargetTypesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_custom_target_types",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListCustomTargetTypes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeliveryPipelines(
        _BaseCloudDeployRestTransport._BaseListDeliveryPipelines, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListDeliveryPipelines")

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
            request: cloud_deploy.ListDeliveryPipelinesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListDeliveryPipelinesResponse:
            r"""Call the list delivery pipelines method over HTTP.

            Args:
                request (~.cloud_deploy.ListDeliveryPipelinesRequest):
                    The request object. The request object for ``ListDeliveryPipelines``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListDeliveryPipelinesResponse:
                    The response object from ``ListDeliveryPipelines``.
            """

            http_options = _BaseCloudDeployRestTransport._BaseListDeliveryPipelines._get_http_options()
            request, metadata = self._interceptor.pre_list_delivery_pipelines(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListDeliveryPipelines,
                    "_BaseListDeliveryPipelines__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListDeliveryPipelines",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListDeliveryPipelines",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListDeliveryPipelines._get_response(
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
            resp = cloud_deploy.ListDeliveryPipelinesResponse()
            pb_resp = cloud_deploy.ListDeliveryPipelinesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_delivery_pipelines(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_delivery_pipelines_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_deploy.ListDeliveryPipelinesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_delivery_pipelines",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListDeliveryPipelines",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeployPolicies(
        _BaseCloudDeployRestTransport._BaseListDeployPolicies, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListDeployPolicies")

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
            request: cloud_deploy.ListDeployPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListDeployPoliciesResponse:
            r"""Call the list deploy policies method over HTTP.

            Args:
                request (~.cloud_deploy.ListDeployPoliciesRequest):
                    The request object. The request object for ``ListDeployPolicies``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListDeployPoliciesResponse:
                    The response object from ``ListDeployPolicies``.
            """

            http_options = _BaseCloudDeployRestTransport._BaseListDeployPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_deploy_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListDeployPolicies,
                    "_BaseListDeployPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListDeployPolicies",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListDeployPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListDeployPolicies._get_response(
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
            resp = cloud_deploy.ListDeployPoliciesResponse()
            pb_resp = cloud_deploy.ListDeployPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deploy_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_deploy_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.ListDeployPoliciesResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_deploy_policies",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListDeployPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListJobRuns(
        _BaseCloudDeployRestTransport._BaseListJobRuns, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListJobRuns")

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
            request: cloud_deploy.ListJobRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListJobRunsResponse:
            r"""Call the list job runs method over HTTP.

            Args:
                request (~.cloud_deploy.ListJobRunsRequest):
                    The request object. ListJobRunsRequest is the request object used by
                ``ListJobRuns``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListJobRunsResponse:
                    ListJobRunsResponse is the response object returned by
                ``ListJobRuns``.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseListJobRuns._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_job_runs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListJobRuns,
                    "_BaseListJobRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListJobRuns",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListJobRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListJobRuns._get_response(
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
            resp = cloud_deploy.ListJobRunsResponse()
            pb_resp = cloud_deploy.ListJobRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_job_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_job_runs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.ListJobRunsResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_job_runs",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListJobRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReleases(
        _BaseCloudDeployRestTransport._BaseListReleases, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListReleases")

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
            request: cloud_deploy.ListReleasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListReleasesResponse:
            r"""Call the list releases method over HTTP.

            Args:
                request (~.cloud_deploy.ListReleasesRequest):
                    The request object. The request object for ``ListReleases``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListReleasesResponse:
                    The response object from ``ListReleases``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseListReleases._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_releases(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListReleases,
                    "_BaseListReleases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListReleases",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListReleases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListReleases._get_response(
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
            resp = cloud_deploy.ListReleasesResponse()
            pb_resp = cloud_deploy.ListReleasesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_releases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_releases_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.ListReleasesResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_releases",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListReleases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRollouts(
        _BaseCloudDeployRestTransport._BaseListRollouts, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListRollouts")

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
            request: cloud_deploy.ListRolloutsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListRolloutsResponse:
            r"""Call the list rollouts method over HTTP.

            Args:
                request (~.cloud_deploy.ListRolloutsRequest):
                    The request object. ListRolloutsRequest is the request object used by
                ``ListRollouts``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListRolloutsResponse:
                    ListRolloutsResponse is the response object returned by
                ``ListRollouts``.

            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseListRollouts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_rollouts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListRollouts,
                    "_BaseListRollouts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListRollouts",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListRollouts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListRollouts._get_response(
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
            resp = cloud_deploy.ListRolloutsResponse()
            pb_resp = cloud_deploy.ListRolloutsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_rollouts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rollouts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.ListRolloutsResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_rollouts",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListRollouts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTargets(
        _BaseCloudDeployRestTransport._BaseListTargets, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListTargets")

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
            request: cloud_deploy.ListTargetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.ListTargetsResponse:
            r"""Call the list targets method over HTTP.

            Args:
                request (~.cloud_deploy.ListTargetsRequest):
                    The request object. The request object for ``ListTargets``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.ListTargetsResponse:
                    The response object from ``ListTargets``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseListTargets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_targets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListTargets,
                    "_BaseListTargets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListTargets",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListTargets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListTargets._get_response(
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
            resp = cloud_deploy.ListTargetsResponse()
            pb_resp = cloud_deploy.ListTargetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_targets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_targets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.ListTargetsResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.list_targets",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListTargets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RetryJob(_BaseCloudDeployRestTransport._BaseRetryJob, CloudDeployRestStub):
        def __hash__(self):
            return hash("CloudDeployRestTransport.RetryJob")

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
            request: cloud_deploy.RetryJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.RetryJobResponse:
            r"""Call the retry job method over HTTP.

            Args:
                request (~.cloud_deploy.RetryJobRequest):
                    The request object. RetryJobRequest is the request object used by
                ``RetryJob``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.RetryJobResponse:
                    The response object from 'RetryJob'.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseRetryJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_retry_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseRetryJob,
                    "_BaseRetryJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.RetryJob",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "RetryJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._RetryJob._get_response(
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
            resp = cloud_deploy.RetryJobResponse()
            pb_resp = cloud_deploy.RetryJobResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_retry_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_retry_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.RetryJobResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.retry_job",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "RetryJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RollbackTarget(
        _BaseCloudDeployRestTransport._BaseRollbackTarget, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.RollbackTarget")

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
            request: cloud_deploy.RollbackTargetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.RollbackTargetResponse:
            r"""Call the rollback target method over HTTP.

            Args:
                request (~.cloud_deploy.RollbackTargetRequest):
                    The request object. The request object for ``RollbackTarget``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.RollbackTargetResponse:
                    The response object from ``RollbackTarget``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseRollbackTarget._get_http_options()
            )
            request, metadata = self._interceptor.pre_rollback_target(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseRollbackTarget,
                    "_BaseRollbackTarget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.RollbackTarget",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "RollbackTarget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._RollbackTarget._get_response(
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
            resp = cloud_deploy.RollbackTargetResponse()
            pb_resp = cloud_deploy.RollbackTargetResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rollback_target(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rollback_target_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.RollbackTargetResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.rollback_target",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "RollbackTarget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TerminateJobRun(
        _BaseCloudDeployRestTransport._BaseTerminateJobRun, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.TerminateJobRun")

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
            request: cloud_deploy.TerminateJobRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_deploy.TerminateJobRunResponse:
            r"""Call the terminate job run method over HTTP.

            Args:
                request (~.cloud_deploy.TerminateJobRunRequest):
                    The request object. The request object used by ``TerminateJobRun``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_deploy.TerminateJobRunResponse:
                    The response object from ``TerminateJobRun``.
            """

            http_options = (
                _BaseCloudDeployRestTransport._BaseTerminateJobRun._get_http_options()
            )
            request, metadata = self._interceptor.pre_terminate_job_run(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseTerminateJobRun,
                    "_BaseTerminateJobRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.TerminateJobRun",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "TerminateJobRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._TerminateJobRun._get_response(
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
            resp = cloud_deploy.TerminateJobRunResponse()
            pb_resp = cloud_deploy.TerminateJobRunResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_terminate_job_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_terminate_job_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_deploy.TerminateJobRunResponse.to_json(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.terminate_job_run",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "TerminateJobRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAutomation(
        _BaseCloudDeployRestTransport._BaseUpdateAutomation, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.UpdateAutomation")

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
            request: cloud_deploy.UpdateAutomationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update automation method over HTTP.

            Args:
                request (~.cloud_deploy.UpdateAutomationRequest):
                    The request object. The request object for ``UpdateAutomation``.
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
                _BaseCloudDeployRestTransport._BaseUpdateAutomation._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_automation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseUpdateAutomation,
                    "_BaseUpdateAutomation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.UpdateAutomation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateAutomation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._UpdateAutomation._get_response(
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

            resp = self._interceptor.post_update_automation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_automation_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.update_automation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateAutomation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCustomTargetType(
        _BaseCloudDeployRestTransport._BaseUpdateCustomTargetType, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.UpdateCustomTargetType")

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
            request: cloud_deploy.UpdateCustomTargetTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update custom target type method over HTTP.

            Args:
                request (~.cloud_deploy.UpdateCustomTargetTypeRequest):
                    The request object. The request object for ``UpdateCustomTargetType``.
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

            http_options = _BaseCloudDeployRestTransport._BaseUpdateCustomTargetType._get_http_options()
            request, metadata = self._interceptor.pre_update_custom_target_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseUpdateCustomTargetType,
                    "_BaseUpdateCustomTargetType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.UpdateCustomTargetType",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateCustomTargetType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._UpdateCustomTargetType._get_response(
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

            resp = self._interceptor.post_update_custom_target_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_custom_target_type_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.update_custom_target_type",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateCustomTargetType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeliveryPipeline(
        _BaseCloudDeployRestTransport._BaseUpdateDeliveryPipeline, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.UpdateDeliveryPipeline")

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
            request: cloud_deploy.UpdateDeliveryPipelineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update delivery pipeline method over HTTP.

            Args:
                request (~.cloud_deploy.UpdateDeliveryPipelineRequest):
                    The request object. The request object for ``UpdateDeliveryPipeline``.
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

            http_options = _BaseCloudDeployRestTransport._BaseUpdateDeliveryPipeline._get_http_options()
            request, metadata = self._interceptor.pre_update_delivery_pipeline(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseUpdateDeliveryPipeline,
                    "_BaseUpdateDeliveryPipeline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.UpdateDeliveryPipeline",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateDeliveryPipeline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._UpdateDeliveryPipeline._get_response(
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

            resp = self._interceptor.post_update_delivery_pipeline(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_delivery_pipeline_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.update_delivery_pipeline",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateDeliveryPipeline",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeployPolicy(
        _BaseCloudDeployRestTransport._BaseUpdateDeployPolicy, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.UpdateDeployPolicy")

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
            request: cloud_deploy.UpdateDeployPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update deploy policy method over HTTP.

            Args:
                request (~.cloud_deploy.UpdateDeployPolicyRequest):
                    The request object. The request object for ``UpdateDeployPolicy``.
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

            http_options = _BaseCloudDeployRestTransport._BaseUpdateDeployPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_deploy_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseUpdateDeployPolicy,
                    "_BaseUpdateDeployPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.UpdateDeployPolicy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateDeployPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._UpdateDeployPolicy._get_response(
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

            resp = self._interceptor.post_update_deploy_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_deploy_policy_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.update_deploy_policy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateDeployPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTarget(
        _BaseCloudDeployRestTransport._BaseUpdateTarget, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.UpdateTarget")

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
            request: cloud_deploy.UpdateTargetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update target method over HTTP.

            Args:
                request (~.cloud_deploy.UpdateTargetRequest):
                    The request object. The request object for ``UpdateTarget``.
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
                _BaseCloudDeployRestTransport._BaseUpdateTarget._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_target(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseUpdateTarget,
                    "_BaseUpdateTarget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.UpdateTarget",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateTarget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._UpdateTarget._get_response(
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

            resp = self._interceptor.post_update_target(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_target_with_metadata(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployClient.update_target",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "UpdateTarget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def abandon_release(
        self,
    ) -> Callable[
        [cloud_deploy.AbandonReleaseRequest], cloud_deploy.AbandonReleaseResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AbandonRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def advance_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.AdvanceRolloutRequest], cloud_deploy.AdvanceRolloutResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AdvanceRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def approve_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.ApproveRolloutRequest], cloud_deploy.ApproveRolloutResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApproveRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_automation_run(
        self,
    ) -> Callable[
        [cloud_deploy.CancelAutomationRunRequest],
        cloud_deploy.CancelAutomationRunResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelAutomationRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.CancelRolloutRequest], cloud_deploy.CancelRolloutResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_automation(
        self,
    ) -> Callable[[cloud_deploy.CreateAutomationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAutomation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.CreateCustomTargetTypeRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCustomTargetType(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.CreateDeliveryPipelineRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeliveryPipeline(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_deploy_policy(
        self,
    ) -> Callable[[cloud_deploy.CreateDeployPolicyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeployPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_release(
        self,
    ) -> Callable[[cloud_deploy.CreateReleaseRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_rollout(
        self,
    ) -> Callable[[cloud_deploy.CreateRolloutRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_target(
        self,
    ) -> Callable[[cloud_deploy.CreateTargetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTarget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_automation(
        self,
    ) -> Callable[[cloud_deploy.DeleteAutomationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAutomation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteCustomTargetTypeRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCustomTargetType(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteDeliveryPipelineRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeliveryPipeline(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_deploy_policy(
        self,
    ) -> Callable[[cloud_deploy.DeleteDeployPolicyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeployPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_target(
        self,
    ) -> Callable[[cloud_deploy.DeleteTargetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTarget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_automation(
        self,
    ) -> Callable[[cloud_deploy.GetAutomationRequest], cloud_deploy.Automation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAutomation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_automation_run(
        self,
    ) -> Callable[[cloud_deploy.GetAutomationRunRequest], cloud_deploy.AutomationRun]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAutomationRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_config(
        self,
    ) -> Callable[[cloud_deploy.GetConfigRequest], cloud_deploy.Config]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.GetCustomTargetTypeRequest], cloud_deploy.CustomTargetType
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCustomTargetType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.GetDeliveryPipelineRequest], cloud_deploy.DeliveryPipeline
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeliveryPipeline(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_deploy_policy(
        self,
    ) -> Callable[[cloud_deploy.GetDeployPolicyRequest], cloud_deploy.DeployPolicy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeployPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_job_run(
        self,
    ) -> Callable[[cloud_deploy.GetJobRunRequest], cloud_deploy.JobRun]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetJobRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_release(
        self,
    ) -> Callable[[cloud_deploy.GetReleaseRequest], cloud_deploy.Release]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_rollout(
        self,
    ) -> Callable[[cloud_deploy.GetRolloutRequest], cloud_deploy.Rollout]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_target(
        self,
    ) -> Callable[[cloud_deploy.GetTargetRequest], cloud_deploy.Target]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTarget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def ignore_job(
        self,
    ) -> Callable[[cloud_deploy.IgnoreJobRequest], cloud_deploy.IgnoreJobResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IgnoreJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_automation_runs(
        self,
    ) -> Callable[
        [cloud_deploy.ListAutomationRunsRequest],
        cloud_deploy.ListAutomationRunsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAutomationRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_automations(
        self,
    ) -> Callable[
        [cloud_deploy.ListAutomationsRequest], cloud_deploy.ListAutomationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAutomations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_custom_target_types(
        self,
    ) -> Callable[
        [cloud_deploy.ListCustomTargetTypesRequest],
        cloud_deploy.ListCustomTargetTypesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCustomTargetTypes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_delivery_pipelines(
        self,
    ) -> Callable[
        [cloud_deploy.ListDeliveryPipelinesRequest],
        cloud_deploy.ListDeliveryPipelinesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeliveryPipelines(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_deploy_policies(
        self,
    ) -> Callable[
        [cloud_deploy.ListDeployPoliciesRequest],
        cloud_deploy.ListDeployPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeployPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_job_runs(
        self,
    ) -> Callable[[cloud_deploy.ListJobRunsRequest], cloud_deploy.ListJobRunsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListJobRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_releases(
        self,
    ) -> Callable[
        [cloud_deploy.ListReleasesRequest], cloud_deploy.ListReleasesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReleases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rollouts(
        self,
    ) -> Callable[
        [cloud_deploy.ListRolloutsRequest], cloud_deploy.ListRolloutsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRollouts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_targets(
        self,
    ) -> Callable[[cloud_deploy.ListTargetsRequest], cloud_deploy.ListTargetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTargets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def retry_job(
        self,
    ) -> Callable[[cloud_deploy.RetryJobRequest], cloud_deploy.RetryJobResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetryJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rollback_target(
        self,
    ) -> Callable[
        [cloud_deploy.RollbackTargetRequest], cloud_deploy.RollbackTargetResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RollbackTarget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def terminate_job_run(
        self,
    ) -> Callable[
        [cloud_deploy.TerminateJobRunRequest], cloud_deploy.TerminateJobRunResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TerminateJobRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_automation(
        self,
    ) -> Callable[[cloud_deploy.UpdateAutomationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAutomation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateCustomTargetTypeRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCustomTargetType(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateDeliveryPipelineRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeliveryPipeline(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_deploy_policy(
        self,
    ) -> Callable[[cloud_deploy.UpdateDeployPolicyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeployPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_target(
        self,
    ) -> Callable[[cloud_deploy.UpdateTargetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTarget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseCloudDeployRestTransport._BaseGetLocation, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetLocation")

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
                _BaseCloudDeployRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
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
        _BaseCloudDeployRestTransport._BaseListLocations, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListLocations")

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
                _BaseCloudDeployRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
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
        _BaseCloudDeployRestTransport._BaseGetIamPolicy, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetIamPolicy")

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
                _BaseCloudDeployRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
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
        _BaseCloudDeployRestTransport._BaseSetIamPolicy, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.SetIamPolicy")

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
                _BaseCloudDeployRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
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
        _BaseCloudDeployRestTransport._BaseTestIamPermissions, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.TestIamPermissions")

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

            http_options = _BaseCloudDeployRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
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
        _BaseCloudDeployRestTransport._BaseCancelOperation, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.CancelOperation")

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
                _BaseCloudDeployRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._CancelOperation._get_response(
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
        _BaseCloudDeployRestTransport._BaseDeleteOperation, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.DeleteOperation")

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
                _BaseCloudDeployRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._DeleteOperation._get_response(
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
        _BaseCloudDeployRestTransport._BaseGetOperation, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.GetOperation")

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
                _BaseCloudDeployRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
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
        _BaseCloudDeployRestTransport._BaseListOperations, CloudDeployRestStub
    ):
        def __hash__(self):
            return hash("CloudDeployRestTransport.ListOperations")

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
                _BaseCloudDeployRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudDeployRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.deploy_v1.CloudDeployClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudDeployRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.deploy_v1.CloudDeployAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.deploy.v1.CloudDeploy",
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


__all__ = ("CloudDeployRestTransport",)
