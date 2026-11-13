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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.osconfig_v1._compat import transcode_request
from google.cloud.osconfig_v1.types import patch_deployments, patch_jobs

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOsConfigServiceRestTransport

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


class OsConfigServiceRestInterceptor:
    """Interceptor for OsConfigService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OsConfigServiceRestTransport.

    .. code-block:: python
        class MyCustomOsConfigServiceInterceptor(OsConfigServiceRestInterceptor):
            def pre_cancel_patch_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_patch_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_patch_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_patch_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_patch_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_execute_patch_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_patch_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_patch_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_patch_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_patch_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_patch_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_patch_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_patch_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_patch_job_instance_details(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_patch_job_instance_details(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_patch_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_patch_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_pause_patch_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_pause_patch_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resume_patch_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resume_patch_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_patch_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_patch_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OsConfigServiceRestTransport(interceptor=MyCustomOsConfigServiceInterceptor())
        client = OsConfigServiceClient(transport=transport)


    """

    def pre_cancel_patch_job(
        self,
        request: patch_jobs.CancelPatchJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_jobs.CancelPatchJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_patch_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_cancel_patch_job(
        self, response: patch_jobs.PatchJob
    ) -> patch_jobs.PatchJob:
        """Post-rpc interceptor for cancel_patch_job

        DEPRECATED. Please use the `post_cancel_patch_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_cancel_patch_job` interceptor runs
        before the `post_cancel_patch_job_with_metadata` interceptor.
        """
        return response

    def post_cancel_patch_job_with_metadata(
        self,
        response: patch_jobs.PatchJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[patch_jobs.PatchJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for cancel_patch_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_cancel_patch_job_with_metadata`
        interceptor in new development instead of the `post_cancel_patch_job` interceptor.
        When both interceptors are used, this `post_cancel_patch_job_with_metadata` interceptor runs after the
        `post_cancel_patch_job` interceptor. The (possibly modified) response returned by
        `post_cancel_patch_job` will be passed to
        `post_cancel_patch_job_with_metadata`.
        """
        return response, metadata

    def pre_create_patch_deployment(
        self,
        request: patch_deployments.CreatePatchDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.CreatePatchDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_patch_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_create_patch_deployment(
        self, response: patch_deployments.PatchDeployment
    ) -> patch_deployments.PatchDeployment:
        """Post-rpc interceptor for create_patch_deployment

        DEPRECATED. Please use the `post_create_patch_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_create_patch_deployment` interceptor runs
        before the `post_create_patch_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_patch_deployment_with_metadata(
        self,
        response: patch_deployments.PatchDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.PatchDeployment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_patch_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_create_patch_deployment_with_metadata`
        interceptor in new development instead of the `post_create_patch_deployment` interceptor.
        When both interceptors are used, this `post_create_patch_deployment_with_metadata` interceptor runs after the
        `post_create_patch_deployment` interceptor. The (possibly modified) response returned by
        `post_create_patch_deployment` will be passed to
        `post_create_patch_deployment_with_metadata`.
        """
        return response, metadata

    def pre_delete_patch_deployment(
        self,
        request: patch_deployments.DeletePatchDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.DeletePatchDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_patch_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def pre_execute_patch_job(
        self,
        request: patch_jobs.ExecutePatchJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_jobs.ExecutePatchJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for execute_patch_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_execute_patch_job(
        self, response: patch_jobs.PatchJob
    ) -> patch_jobs.PatchJob:
        """Post-rpc interceptor for execute_patch_job

        DEPRECATED. Please use the `post_execute_patch_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_execute_patch_job` interceptor runs
        before the `post_execute_patch_job_with_metadata` interceptor.
        """
        return response

    def post_execute_patch_job_with_metadata(
        self,
        response: patch_jobs.PatchJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[patch_jobs.PatchJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for execute_patch_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_execute_patch_job_with_metadata`
        interceptor in new development instead of the `post_execute_patch_job` interceptor.
        When both interceptors are used, this `post_execute_patch_job_with_metadata` interceptor runs after the
        `post_execute_patch_job` interceptor. The (possibly modified) response returned by
        `post_execute_patch_job` will be passed to
        `post_execute_patch_job_with_metadata`.
        """
        return response, metadata

    def pre_get_patch_deployment(
        self,
        request: patch_deployments.GetPatchDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.GetPatchDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_patch_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_get_patch_deployment(
        self, response: patch_deployments.PatchDeployment
    ) -> patch_deployments.PatchDeployment:
        """Post-rpc interceptor for get_patch_deployment

        DEPRECATED. Please use the `post_get_patch_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_get_patch_deployment` interceptor runs
        before the `post_get_patch_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_patch_deployment_with_metadata(
        self,
        response: patch_deployments.PatchDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.PatchDeployment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_patch_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_get_patch_deployment_with_metadata`
        interceptor in new development instead of the `post_get_patch_deployment` interceptor.
        When both interceptors are used, this `post_get_patch_deployment_with_metadata` interceptor runs after the
        `post_get_patch_deployment` interceptor. The (possibly modified) response returned by
        `post_get_patch_deployment` will be passed to
        `post_get_patch_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_patch_job(
        self,
        request: patch_jobs.GetPatchJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[patch_jobs.GetPatchJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_patch_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_get_patch_job(self, response: patch_jobs.PatchJob) -> patch_jobs.PatchJob:
        """Post-rpc interceptor for get_patch_job

        DEPRECATED. Please use the `post_get_patch_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_get_patch_job` interceptor runs
        before the `post_get_patch_job_with_metadata` interceptor.
        """
        return response

    def post_get_patch_job_with_metadata(
        self,
        response: patch_jobs.PatchJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[patch_jobs.PatchJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_patch_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_get_patch_job_with_metadata`
        interceptor in new development instead of the `post_get_patch_job` interceptor.
        When both interceptors are used, this `post_get_patch_job_with_metadata` interceptor runs after the
        `post_get_patch_job` interceptor. The (possibly modified) response returned by
        `post_get_patch_job` will be passed to
        `post_get_patch_job_with_metadata`.
        """
        return response, metadata

    def pre_list_patch_deployments(
        self,
        request: patch_deployments.ListPatchDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.ListPatchDeploymentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_patch_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_list_patch_deployments(
        self, response: patch_deployments.ListPatchDeploymentsResponse
    ) -> patch_deployments.ListPatchDeploymentsResponse:
        """Post-rpc interceptor for list_patch_deployments

        DEPRECATED. Please use the `post_list_patch_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_list_patch_deployments` interceptor runs
        before the `post_list_patch_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_patch_deployments_with_metadata(
        self,
        response: patch_deployments.ListPatchDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.ListPatchDeploymentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_patch_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_list_patch_deployments_with_metadata`
        interceptor in new development instead of the `post_list_patch_deployments` interceptor.
        When both interceptors are used, this `post_list_patch_deployments_with_metadata` interceptor runs after the
        `post_list_patch_deployments` interceptor. The (possibly modified) response returned by
        `post_list_patch_deployments` will be passed to
        `post_list_patch_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_patch_job_instance_details(
        self,
        request: patch_jobs.ListPatchJobInstanceDetailsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_jobs.ListPatchJobInstanceDetailsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_patch_job_instance_details

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_list_patch_job_instance_details(
        self, response: patch_jobs.ListPatchJobInstanceDetailsResponse
    ) -> patch_jobs.ListPatchJobInstanceDetailsResponse:
        """Post-rpc interceptor for list_patch_job_instance_details

        DEPRECATED. Please use the `post_list_patch_job_instance_details_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_list_patch_job_instance_details` interceptor runs
        before the `post_list_patch_job_instance_details_with_metadata` interceptor.
        """
        return response

    def post_list_patch_job_instance_details_with_metadata(
        self,
        response: patch_jobs.ListPatchJobInstanceDetailsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_jobs.ListPatchJobInstanceDetailsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_patch_job_instance_details

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_list_patch_job_instance_details_with_metadata`
        interceptor in new development instead of the `post_list_patch_job_instance_details` interceptor.
        When both interceptors are used, this `post_list_patch_job_instance_details_with_metadata` interceptor runs after the
        `post_list_patch_job_instance_details` interceptor. The (possibly modified) response returned by
        `post_list_patch_job_instance_details` will be passed to
        `post_list_patch_job_instance_details_with_metadata`.
        """
        return response, metadata

    def pre_list_patch_jobs(
        self,
        request: patch_jobs.ListPatchJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_jobs.ListPatchJobsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_patch_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_list_patch_jobs(
        self, response: patch_jobs.ListPatchJobsResponse
    ) -> patch_jobs.ListPatchJobsResponse:
        """Post-rpc interceptor for list_patch_jobs

        DEPRECATED. Please use the `post_list_patch_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_list_patch_jobs` interceptor runs
        before the `post_list_patch_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_patch_jobs_with_metadata(
        self,
        response: patch_jobs.ListPatchJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_jobs.ListPatchJobsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_patch_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_list_patch_jobs_with_metadata`
        interceptor in new development instead of the `post_list_patch_jobs` interceptor.
        When both interceptors are used, this `post_list_patch_jobs_with_metadata` interceptor runs after the
        `post_list_patch_jobs` interceptor. The (possibly modified) response returned by
        `post_list_patch_jobs` will be passed to
        `post_list_patch_jobs_with_metadata`.
        """
        return response, metadata

    def pre_pause_patch_deployment(
        self,
        request: patch_deployments.PausePatchDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.PausePatchDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for pause_patch_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_pause_patch_deployment(
        self, response: patch_deployments.PatchDeployment
    ) -> patch_deployments.PatchDeployment:
        """Post-rpc interceptor for pause_patch_deployment

        DEPRECATED. Please use the `post_pause_patch_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_pause_patch_deployment` interceptor runs
        before the `post_pause_patch_deployment_with_metadata` interceptor.
        """
        return response

    def post_pause_patch_deployment_with_metadata(
        self,
        response: patch_deployments.PatchDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.PatchDeployment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for pause_patch_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_pause_patch_deployment_with_metadata`
        interceptor in new development instead of the `post_pause_patch_deployment` interceptor.
        When both interceptors are used, this `post_pause_patch_deployment_with_metadata` interceptor runs after the
        `post_pause_patch_deployment` interceptor. The (possibly modified) response returned by
        `post_pause_patch_deployment` will be passed to
        `post_pause_patch_deployment_with_metadata`.
        """
        return response, metadata

    def pre_resume_patch_deployment(
        self,
        request: patch_deployments.ResumePatchDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.ResumePatchDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for resume_patch_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_resume_patch_deployment(
        self, response: patch_deployments.PatchDeployment
    ) -> patch_deployments.PatchDeployment:
        """Post-rpc interceptor for resume_patch_deployment

        DEPRECATED. Please use the `post_resume_patch_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_resume_patch_deployment` interceptor runs
        before the `post_resume_patch_deployment_with_metadata` interceptor.
        """
        return response

    def post_resume_patch_deployment_with_metadata(
        self,
        response: patch_deployments.PatchDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.PatchDeployment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for resume_patch_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_resume_patch_deployment_with_metadata`
        interceptor in new development instead of the `post_resume_patch_deployment` interceptor.
        When both interceptors are used, this `post_resume_patch_deployment_with_metadata` interceptor runs after the
        `post_resume_patch_deployment` interceptor. The (possibly modified) response returned by
        `post_resume_patch_deployment` will be passed to
        `post_resume_patch_deployment_with_metadata`.
        """
        return response, metadata

    def pre_update_patch_deployment(
        self,
        request: patch_deployments.UpdatePatchDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.UpdatePatchDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_patch_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigService server.
        """
        return request, metadata

    def post_update_patch_deployment(
        self, response: patch_deployments.PatchDeployment
    ) -> patch_deployments.PatchDeployment:
        """Post-rpc interceptor for update_patch_deployment

        DEPRECATED. Please use the `post_update_patch_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigService server but before
        it is returned to user code. This `post_update_patch_deployment` interceptor runs
        before the `post_update_patch_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_patch_deployment_with_metadata(
        self,
        response: patch_deployments.PatchDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        patch_deployments.PatchDeployment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_patch_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigService server but before it is returned to user code.

        We recommend only using this `post_update_patch_deployment_with_metadata`
        interceptor in new development instead of the `post_update_patch_deployment` interceptor.
        When both interceptors are used, this `post_update_patch_deployment_with_metadata` interceptor runs after the
        `post_update_patch_deployment` interceptor. The (possibly modified) response returned by
        `post_update_patch_deployment` will be passed to
        `post_update_patch_deployment_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class OsConfigServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OsConfigServiceRestInterceptor


class OsConfigServiceRestTransport(_BaseOsConfigServiceRestTransport):
    """REST backend synchronous transport for OsConfigService.

    OS Config API

    The OS Config service is a server-side component that you can
    use to manage package installations and patch jobs for virtual
    machine instances.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "osconfig.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[OsConfigServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'osconfig.googleapis.com').
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
            interceptor (Optional[OsConfigServiceRestInterceptor]): Interceptor used
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
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or OsConfigServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CancelPatchJob(
        _BaseOsConfigServiceRestTransport._BaseCancelPatchJob, OsConfigServiceRestStub
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.CancelPatchJob")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_jobs.CancelPatchJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_jobs.PatchJob:
            r"""Call the cancel patch job method over HTTP.

            Args:
                request (~.patch_jobs.CancelPatchJobRequest):
                    The request object. Message for canceling a patch job.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_jobs.PatchJob:
                    A high level representation of a patch job that is
                either in progress or has completed.

                Instance details are not included in the job. To
                paginate through instance details, use
                ListPatchJobInstanceDetails.

                For more information about patch jobs, see `Creating
                patch
                jobs <https://cloud.google.com/compute/docs/os-patch-management/create-patch-job>`__.

            """

            http_options = _BaseOsConfigServiceRestTransport._BaseCancelPatchJob._get_http_options()
            request, metadata = self._interceptor.pre_cancel_patch_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseCancelPatchJob,
                    "_BaseCancelPatchJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.CancelPatchJob",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "CancelPatchJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigServiceRestTransport._CancelPatchJob._get_response(
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
            resp = patch_jobs.PatchJob()
            pb_resp = patch_jobs.PatchJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_cancel_patch_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_patch_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_jobs.PatchJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.cancel_patch_job",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "CancelPatchJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePatchDeployment(
        _BaseOsConfigServiceRestTransport._BaseCreatePatchDeployment,
        OsConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.CreatePatchDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_deployments.CreatePatchDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_deployments.PatchDeployment:
            r"""Call the create patch deployment method over HTTP.

            Args:
                request (~.patch_deployments.CreatePatchDeploymentRequest):
                    The request object. A request message for creating a
                patch deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_deployments.PatchDeployment:
                    Patch deployments are configurations that individual
                patch jobs use to complete a patch. These configurations
                include instance filter, package repository settings,
                and a schedule. For more information about creating and
                managing patch deployments, see `Scheduling patch
                jobs <https://cloud.google.com/compute/docs/os-patch-management/schedule-patch-jobs>`__.

            """

            http_options = _BaseOsConfigServiceRestTransport._BaseCreatePatchDeployment._get_http_options()
            request, metadata = self._interceptor.pre_create_patch_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseCreatePatchDeployment,
                    "_BaseCreatePatchDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.CreatePatchDeployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "CreatePatchDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OsConfigServiceRestTransport._CreatePatchDeployment._get_response(
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
            resp = patch_deployments.PatchDeployment()
            pb_resp = patch_deployments.PatchDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_patch_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_patch_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_deployments.PatchDeployment.to_json(
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
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.create_patch_deployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "CreatePatchDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePatchDeployment(
        _BaseOsConfigServiceRestTransport._BaseDeletePatchDeployment,
        OsConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.DeletePatchDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_deployments.DeletePatchDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete patch deployment method over HTTP.

            Args:
                request (~.patch_deployments.DeletePatchDeploymentRequest):
                    The request object. A request message for deleting a
                patch deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseOsConfigServiceRestTransport._BaseDeletePatchDeployment._get_http_options()
            request, metadata = self._interceptor.pre_delete_patch_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseDeletePatchDeployment,
                    "_BaseDeletePatchDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.DeletePatchDeployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "DeletePatchDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OsConfigServiceRestTransport._DeletePatchDeployment._get_response(
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

    class _ExecutePatchJob(
        _BaseOsConfigServiceRestTransport._BaseExecutePatchJob, OsConfigServiceRestStub
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.ExecutePatchJob")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_jobs.ExecutePatchJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_jobs.PatchJob:
            r"""Call the execute patch job method over HTTP.

            Args:
                request (~.patch_jobs.ExecutePatchJobRequest):
                    The request object. A request message to initiate
                patching across Compute Engine
                instances.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_jobs.PatchJob:
                    A high level representation of a patch job that is
                either in progress or has completed.

                Instance details are not included in the job. To
                paginate through instance details, use
                ListPatchJobInstanceDetails.

                For more information about patch jobs, see `Creating
                patch
                jobs <https://cloud.google.com/compute/docs/os-patch-management/create-patch-job>`__.

            """

            http_options = _BaseOsConfigServiceRestTransport._BaseExecutePatchJob._get_http_options()
            request, metadata = self._interceptor.pre_execute_patch_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseExecutePatchJob,
                    "_BaseExecutePatchJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.ExecutePatchJob",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ExecutePatchJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigServiceRestTransport._ExecutePatchJob._get_response(
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
            resp = patch_jobs.PatchJob()
            pb_resp = patch_jobs.PatchJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_execute_patch_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_execute_patch_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_jobs.PatchJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.execute_patch_job",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ExecutePatchJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPatchDeployment(
        _BaseOsConfigServiceRestTransport._BaseGetPatchDeployment,
        OsConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.GetPatchDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_deployments.GetPatchDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_deployments.PatchDeployment:
            r"""Call the get patch deployment method over HTTP.

            Args:
                request (~.patch_deployments.GetPatchDeploymentRequest):
                    The request object. A request message for retrieving a
                patch deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_deployments.PatchDeployment:
                    Patch deployments are configurations that individual
                patch jobs use to complete a patch. These configurations
                include instance filter, package repository settings,
                and a schedule. For more information about creating and
                managing patch deployments, see `Scheduling patch
                jobs <https://cloud.google.com/compute/docs/os-patch-management/schedule-patch-jobs>`__.

            """

            http_options = _BaseOsConfigServiceRestTransport._BaseGetPatchDeployment._get_http_options()
            request, metadata = self._interceptor.pre_get_patch_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseGetPatchDeployment,
                    "_BaseGetPatchDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.GetPatchDeployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "GetPatchDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigServiceRestTransport._GetPatchDeployment._get_response(
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
            resp = patch_deployments.PatchDeployment()
            pb_resp = patch_deployments.PatchDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_patch_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_patch_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_deployments.PatchDeployment.to_json(
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
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.get_patch_deployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "GetPatchDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPatchJob(
        _BaseOsConfigServiceRestTransport._BaseGetPatchJob, OsConfigServiceRestStub
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.GetPatchJob")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_jobs.GetPatchJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_jobs.PatchJob:
            r"""Call the get patch job method over HTTP.

            Args:
                request (~.patch_jobs.GetPatchJobRequest):
                    The request object. Request to get an active or completed
                patch job.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_jobs.PatchJob:
                    A high level representation of a patch job that is
                either in progress or has completed.

                Instance details are not included in the job. To
                paginate through instance details, use
                ListPatchJobInstanceDetails.

                For more information about patch jobs, see `Creating
                patch
                jobs <https://cloud.google.com/compute/docs/os-patch-management/create-patch-job>`__.

            """

            http_options = (
                _BaseOsConfigServiceRestTransport._BaseGetPatchJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_patch_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseGetPatchJob,
                    "_BaseGetPatchJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.GetPatchJob",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "GetPatchJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigServiceRestTransport._GetPatchJob._get_response(
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
            resp = patch_jobs.PatchJob()
            pb_resp = patch_jobs.PatchJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_patch_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_patch_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_jobs.PatchJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.get_patch_job",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "GetPatchJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPatchDeployments(
        _BaseOsConfigServiceRestTransport._BaseListPatchDeployments,
        OsConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.ListPatchDeployments")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_deployments.ListPatchDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_deployments.ListPatchDeploymentsResponse:
            r"""Call the list patch deployments method over HTTP.

            Args:
                request (~.patch_deployments.ListPatchDeploymentsRequest):
                    The request object. A request message for listing patch
                deployments.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_deployments.ListPatchDeploymentsResponse:
                    A response message for listing patch
                deployments.

            """

            http_options = _BaseOsConfigServiceRestTransport._BaseListPatchDeployments._get_http_options()
            request, metadata = self._interceptor.pre_list_patch_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseListPatchDeployments,
                    "_BaseListPatchDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.ListPatchDeployments",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ListPatchDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigServiceRestTransport._ListPatchDeployments._get_response(
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
            resp = patch_deployments.ListPatchDeploymentsResponse()
            pb_resp = patch_deployments.ListPatchDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_patch_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_patch_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        patch_deployments.ListPatchDeploymentsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.list_patch_deployments",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ListPatchDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPatchJobInstanceDetails(
        _BaseOsConfigServiceRestTransport._BaseListPatchJobInstanceDetails,
        OsConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.ListPatchJobInstanceDetails")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_jobs.ListPatchJobInstanceDetailsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_jobs.ListPatchJobInstanceDetailsResponse:
            r"""Call the list patch job instance
            details method over HTTP.

                Args:
                    request (~.patch_jobs.ListPatchJobInstanceDetailsRequest):
                        The request object. Request to list details for all
                    instances that are part of a patch job.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.patch_jobs.ListPatchJobInstanceDetailsResponse:
                        A response message for listing the
                    instances details for a patch job.

            """

            http_options = _BaseOsConfigServiceRestTransport._BaseListPatchJobInstanceDetails._get_http_options()
            request, metadata = self._interceptor.pre_list_patch_job_instance_details(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseListPatchJobInstanceDetails,
                    "_BaseListPatchJobInstanceDetails__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.ListPatchJobInstanceDetails",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ListPatchJobInstanceDetails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OsConfigServiceRestTransport._ListPatchJobInstanceDetails._get_response(
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
            resp = patch_jobs.ListPatchJobInstanceDetailsResponse()
            pb_resp = patch_jobs.ListPatchJobInstanceDetailsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_patch_job_instance_details(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_patch_job_instance_details_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        patch_jobs.ListPatchJobInstanceDetailsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.list_patch_job_instance_details",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ListPatchJobInstanceDetails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPatchJobs(
        _BaseOsConfigServiceRestTransport._BaseListPatchJobs, OsConfigServiceRestStub
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.ListPatchJobs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_jobs.ListPatchJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_jobs.ListPatchJobsResponse:
            r"""Call the list patch jobs method over HTTP.

            Args:
                request (~.patch_jobs.ListPatchJobsRequest):
                    The request object. A request message for listing patch
                jobs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_jobs.ListPatchJobsResponse:
                    A response message for listing patch
                jobs.

            """

            http_options = (
                _BaseOsConfigServiceRestTransport._BaseListPatchJobs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_patch_jobs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseListPatchJobs,
                    "_BaseListPatchJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.ListPatchJobs",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ListPatchJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigServiceRestTransport._ListPatchJobs._get_response(
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
            resp = patch_jobs.ListPatchJobsResponse()
            pb_resp = patch_jobs.ListPatchJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_patch_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_patch_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_jobs.ListPatchJobsResponse.to_json(
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
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.list_patch_jobs",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ListPatchJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PausePatchDeployment(
        _BaseOsConfigServiceRestTransport._BasePausePatchDeployment,
        OsConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.PausePatchDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_deployments.PausePatchDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_deployments.PatchDeployment:
            r"""Call the pause patch deployment method over HTTP.

            Args:
                request (~.patch_deployments.PausePatchDeploymentRequest):
                    The request object. A request message for pausing a patch
                deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_deployments.PatchDeployment:
                    Patch deployments are configurations that individual
                patch jobs use to complete a patch. These configurations
                include instance filter, package repository settings,
                and a schedule. For more information about creating and
                managing patch deployments, see `Scheduling patch
                jobs <https://cloud.google.com/compute/docs/os-patch-management/schedule-patch-jobs>`__.

            """

            http_options = _BaseOsConfigServiceRestTransport._BasePausePatchDeployment._get_http_options()
            request, metadata = self._interceptor.pre_pause_patch_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BasePausePatchDeployment,
                    "_BasePausePatchDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.PausePatchDeployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "PausePatchDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigServiceRestTransport._PausePatchDeployment._get_response(
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
            resp = patch_deployments.PatchDeployment()
            pb_resp = patch_deployments.PatchDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_pause_patch_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_pause_patch_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_deployments.PatchDeployment.to_json(
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
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.pause_patch_deployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "PausePatchDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResumePatchDeployment(
        _BaseOsConfigServiceRestTransport._BaseResumePatchDeployment,
        OsConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.ResumePatchDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_deployments.ResumePatchDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_deployments.PatchDeployment:
            r"""Call the resume patch deployment method over HTTP.

            Args:
                request (~.patch_deployments.ResumePatchDeploymentRequest):
                    The request object. A request message for resuming a
                patch deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_deployments.PatchDeployment:
                    Patch deployments are configurations that individual
                patch jobs use to complete a patch. These configurations
                include instance filter, package repository settings,
                and a schedule. For more information about creating and
                managing patch deployments, see `Scheduling patch
                jobs <https://cloud.google.com/compute/docs/os-patch-management/schedule-patch-jobs>`__.

            """

            http_options = _BaseOsConfigServiceRestTransport._BaseResumePatchDeployment._get_http_options()
            request, metadata = self._interceptor.pre_resume_patch_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseResumePatchDeployment,
                    "_BaseResumePatchDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.ResumePatchDeployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ResumePatchDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OsConfigServiceRestTransport._ResumePatchDeployment._get_response(
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
            resp = patch_deployments.PatchDeployment()
            pb_resp = patch_deployments.PatchDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_resume_patch_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resume_patch_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_deployments.PatchDeployment.to_json(
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
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.resume_patch_deployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "ResumePatchDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePatchDeployment(
        _BaseOsConfigServiceRestTransport._BaseUpdatePatchDeployment,
        OsConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigServiceRestTransport.UpdatePatchDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: patch_deployments.UpdatePatchDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> patch_deployments.PatchDeployment:
            r"""Call the update patch deployment method over HTTP.

            Args:
                request (~.patch_deployments.UpdatePatchDeploymentRequest):
                    The request object. A request message for updating a
                patch deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.patch_deployments.PatchDeployment:
                    Patch deployments are configurations that individual
                patch jobs use to complete a patch. These configurations
                include instance filter, package repository settings,
                and a schedule. For more information about creating and
                managing patch deployments, see `Scheduling patch
                jobs <https://cloud.google.com/compute/docs/os-patch-management/schedule-patch-jobs>`__.

            """

            http_options = _BaseOsConfigServiceRestTransport._BaseUpdatePatchDeployment._get_http_options()
            request, metadata = self._interceptor.pre_update_patch_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigServiceRestTransport._BaseUpdatePatchDeployment,
                    "_BaseUpdatePatchDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1.OsConfigServiceClient.UpdatePatchDeployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "UpdatePatchDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OsConfigServiceRestTransport._UpdatePatchDeployment._get_response(
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
            resp = patch_deployments.PatchDeployment()
            pb_resp = patch_deployments.PatchDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_patch_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_patch_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = patch_deployments.PatchDeployment.to_json(
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
                    "Received response for google.cloud.osconfig_v1.OsConfigServiceClient.update_patch_deployment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigService",
                        "rpcName": "UpdatePatchDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def cancel_patch_job(
        self,
    ) -> Callable[[patch_jobs.CancelPatchJobRequest], patch_jobs.PatchJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelPatchJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.CreatePatchDeploymentRequest],
        patch_deployments.PatchDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePatchDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_patch_deployment(
        self,
    ) -> Callable[[patch_deployments.DeletePatchDeploymentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePatchDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_patch_job(
        self,
    ) -> Callable[[patch_jobs.ExecutePatchJobRequest], patch_jobs.PatchJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecutePatchJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.GetPatchDeploymentRequest], patch_deployments.PatchDeployment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPatchDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_patch_job(
        self,
    ) -> Callable[[patch_jobs.GetPatchJobRequest], patch_jobs.PatchJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPatchJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_patch_deployments(
        self,
    ) -> Callable[
        [patch_deployments.ListPatchDeploymentsRequest],
        patch_deployments.ListPatchDeploymentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPatchDeployments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_patch_job_instance_details(
        self,
    ) -> Callable[
        [patch_jobs.ListPatchJobInstanceDetailsRequest],
        patch_jobs.ListPatchJobInstanceDetailsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPatchJobInstanceDetails(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_patch_jobs(
        self,
    ) -> Callable[[patch_jobs.ListPatchJobsRequest], patch_jobs.ListPatchJobsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPatchJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def pause_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.PausePatchDeploymentRequest],
        patch_deployments.PatchDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PausePatchDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resume_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.ResumePatchDeploymentRequest],
        patch_deployments.PatchDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResumePatchDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.UpdatePatchDeploymentRequest],
        patch_deployments.PatchDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePatchDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("OsConfigServiceRestTransport",)
