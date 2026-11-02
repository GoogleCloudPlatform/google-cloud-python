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

from google.cloud.storage_transfer_v1._compat import transcode_request
from google.cloud.storage_transfer_v1.types import transfer, transfer_types

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseStorageTransferServiceRestTransport

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


class StorageTransferServiceRestInterceptor:
    """Interceptor for StorageTransferService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the StorageTransferServiceRestTransport.

    .. code-block:: python
        class MyCustomStorageTransferServiceInterceptor(StorageTransferServiceRestInterceptor):
            def pre_create_agent_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_agent_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_transfer_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_transfer_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_agent_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_transfer_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_agent_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_agent_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_google_service_account(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_google_service_account(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_transfer_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_transfer_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_agent_pools(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_agent_pools(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_transfer_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_transfer_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_pause_transfer_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_resume_transfer_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_run_transfer_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_transfer_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_agent_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_agent_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_transfer_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_transfer_job(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = StorageTransferServiceRestTransport(interceptor=MyCustomStorageTransferServiceInterceptor())
        client = StorageTransferServiceClient(transport=transport)


    """

    def pre_create_agent_pool(
        self,
        request: transfer.CreateAgentPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.CreateAgentPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_agent_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_create_agent_pool(
        self, response: transfer_types.AgentPool
    ) -> transfer_types.AgentPool:
        """Post-rpc interceptor for create_agent_pool

        DEPRECATED. Please use the `post_create_agent_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_create_agent_pool` interceptor runs
        before the `post_create_agent_pool_with_metadata` interceptor.
        """
        return response

    def post_create_agent_pool_with_metadata(
        self,
        response: transfer_types.AgentPool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer_types.AgentPool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_agent_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_create_agent_pool_with_metadata`
        interceptor in new development instead of the `post_create_agent_pool` interceptor.
        When both interceptors are used, this `post_create_agent_pool_with_metadata` interceptor runs after the
        `post_create_agent_pool` interceptor. The (possibly modified) response returned by
        `post_create_agent_pool` will be passed to
        `post_create_agent_pool_with_metadata`.
        """
        return response, metadata

    def pre_create_transfer_job(
        self,
        request: transfer.CreateTransferJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.CreateTransferJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_transfer_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_create_transfer_job(
        self, response: transfer_types.TransferJob
    ) -> transfer_types.TransferJob:
        """Post-rpc interceptor for create_transfer_job

        DEPRECATED. Please use the `post_create_transfer_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_create_transfer_job` interceptor runs
        before the `post_create_transfer_job_with_metadata` interceptor.
        """
        return response

    def post_create_transfer_job_with_metadata(
        self,
        response: transfer_types.TransferJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer_types.TransferJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_transfer_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_create_transfer_job_with_metadata`
        interceptor in new development instead of the `post_create_transfer_job` interceptor.
        When both interceptors are used, this `post_create_transfer_job_with_metadata` interceptor runs after the
        `post_create_transfer_job` interceptor. The (possibly modified) response returned by
        `post_create_transfer_job` will be passed to
        `post_create_transfer_job_with_metadata`.
        """
        return response, metadata

    def pre_delete_agent_pool(
        self,
        request: transfer.DeleteAgentPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.DeleteAgentPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_agent_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def pre_delete_transfer_job(
        self,
        request: transfer.DeleteTransferJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.DeleteTransferJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_transfer_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def pre_get_agent_pool(
        self,
        request: transfer.GetAgentPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer.GetAgentPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_agent_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_get_agent_pool(
        self, response: transfer_types.AgentPool
    ) -> transfer_types.AgentPool:
        """Post-rpc interceptor for get_agent_pool

        DEPRECATED. Please use the `post_get_agent_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_get_agent_pool` interceptor runs
        before the `post_get_agent_pool_with_metadata` interceptor.
        """
        return response

    def post_get_agent_pool_with_metadata(
        self,
        response: transfer_types.AgentPool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer_types.AgentPool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_agent_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_get_agent_pool_with_metadata`
        interceptor in new development instead of the `post_get_agent_pool` interceptor.
        When both interceptors are used, this `post_get_agent_pool_with_metadata` interceptor runs after the
        `post_get_agent_pool` interceptor. The (possibly modified) response returned by
        `post_get_agent_pool` will be passed to
        `post_get_agent_pool_with_metadata`.
        """
        return response, metadata

    def pre_get_google_service_account(
        self,
        request: transfer.GetGoogleServiceAccountRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.GetGoogleServiceAccountRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_google_service_account

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_get_google_service_account(
        self, response: transfer_types.GoogleServiceAccount
    ) -> transfer_types.GoogleServiceAccount:
        """Post-rpc interceptor for get_google_service_account

        DEPRECATED. Please use the `post_get_google_service_account_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_get_google_service_account` interceptor runs
        before the `post_get_google_service_account_with_metadata` interceptor.
        """
        return response

    def post_get_google_service_account_with_metadata(
        self,
        response: transfer_types.GoogleServiceAccount,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer_types.GoogleServiceAccount, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_google_service_account

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_get_google_service_account_with_metadata`
        interceptor in new development instead of the `post_get_google_service_account` interceptor.
        When both interceptors are used, this `post_get_google_service_account_with_metadata` interceptor runs after the
        `post_get_google_service_account` interceptor. The (possibly modified) response returned by
        `post_get_google_service_account` will be passed to
        `post_get_google_service_account_with_metadata`.
        """
        return response, metadata

    def pre_get_transfer_job(
        self,
        request: transfer.GetTransferJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer.GetTransferJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_transfer_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_get_transfer_job(
        self, response: transfer_types.TransferJob
    ) -> transfer_types.TransferJob:
        """Post-rpc interceptor for get_transfer_job

        DEPRECATED. Please use the `post_get_transfer_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_get_transfer_job` interceptor runs
        before the `post_get_transfer_job_with_metadata` interceptor.
        """
        return response

    def post_get_transfer_job_with_metadata(
        self,
        response: transfer_types.TransferJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer_types.TransferJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_transfer_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_get_transfer_job_with_metadata`
        interceptor in new development instead of the `post_get_transfer_job` interceptor.
        When both interceptors are used, this `post_get_transfer_job_with_metadata` interceptor runs after the
        `post_get_transfer_job` interceptor. The (possibly modified) response returned by
        `post_get_transfer_job` will be passed to
        `post_get_transfer_job_with_metadata`.
        """
        return response, metadata

    def pre_list_agent_pools(
        self,
        request: transfer.ListAgentPoolsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer.ListAgentPoolsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_agent_pools

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_list_agent_pools(
        self, response: transfer.ListAgentPoolsResponse
    ) -> transfer.ListAgentPoolsResponse:
        """Post-rpc interceptor for list_agent_pools

        DEPRECATED. Please use the `post_list_agent_pools_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_list_agent_pools` interceptor runs
        before the `post_list_agent_pools_with_metadata` interceptor.
        """
        return response

    def post_list_agent_pools_with_metadata(
        self,
        response: transfer.ListAgentPoolsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.ListAgentPoolsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_agent_pools

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_list_agent_pools_with_metadata`
        interceptor in new development instead of the `post_list_agent_pools` interceptor.
        When both interceptors are used, this `post_list_agent_pools_with_metadata` interceptor runs after the
        `post_list_agent_pools` interceptor. The (possibly modified) response returned by
        `post_list_agent_pools` will be passed to
        `post_list_agent_pools_with_metadata`.
        """
        return response, metadata

    def pre_list_transfer_jobs(
        self,
        request: transfer.ListTransferJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.ListTransferJobsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_transfer_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_list_transfer_jobs(
        self, response: transfer.ListTransferJobsResponse
    ) -> transfer.ListTransferJobsResponse:
        """Post-rpc interceptor for list_transfer_jobs

        DEPRECATED. Please use the `post_list_transfer_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_list_transfer_jobs` interceptor runs
        before the `post_list_transfer_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_transfer_jobs_with_metadata(
        self,
        response: transfer.ListTransferJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.ListTransferJobsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_transfer_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_list_transfer_jobs_with_metadata`
        interceptor in new development instead of the `post_list_transfer_jobs` interceptor.
        When both interceptors are used, this `post_list_transfer_jobs_with_metadata` interceptor runs after the
        `post_list_transfer_jobs` interceptor. The (possibly modified) response returned by
        `post_list_transfer_jobs` will be passed to
        `post_list_transfer_jobs_with_metadata`.
        """
        return response, metadata

    def pre_pause_transfer_operation(
        self,
        request: transfer.PauseTransferOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.PauseTransferOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for pause_transfer_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def pre_resume_transfer_operation(
        self,
        request: transfer.ResumeTransferOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.ResumeTransferOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for resume_transfer_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def pre_run_transfer_job(
        self,
        request: transfer.RunTransferJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer.RunTransferJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for run_transfer_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_run_transfer_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_transfer_job

        DEPRECATED. Please use the `post_run_transfer_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_run_transfer_job` interceptor runs
        before the `post_run_transfer_job_with_metadata` interceptor.
        """
        return response

    def post_run_transfer_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_transfer_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_run_transfer_job_with_metadata`
        interceptor in new development instead of the `post_run_transfer_job` interceptor.
        When both interceptors are used, this `post_run_transfer_job_with_metadata` interceptor runs after the
        `post_run_transfer_job` interceptor. The (possibly modified) response returned by
        `post_run_transfer_job` will be passed to
        `post_run_transfer_job_with_metadata`.
        """
        return response, metadata

    def pre_update_agent_pool(
        self,
        request: transfer.UpdateAgentPoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.UpdateAgentPoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_agent_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_update_agent_pool(
        self, response: transfer_types.AgentPool
    ) -> transfer_types.AgentPool:
        """Post-rpc interceptor for update_agent_pool

        DEPRECATED. Please use the `post_update_agent_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_update_agent_pool` interceptor runs
        before the `post_update_agent_pool_with_metadata` interceptor.
        """
        return response

    def post_update_agent_pool_with_metadata(
        self,
        response: transfer_types.AgentPool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer_types.AgentPool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_agent_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_update_agent_pool_with_metadata`
        interceptor in new development instead of the `post_update_agent_pool` interceptor.
        When both interceptors are used, this `post_update_agent_pool_with_metadata` interceptor runs after the
        `post_update_agent_pool` interceptor. The (possibly modified) response returned by
        `post_update_agent_pool` will be passed to
        `post_update_agent_pool_with_metadata`.
        """
        return response, metadata

    def pre_update_transfer_job(
        self,
        request: transfer.UpdateTransferJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        transfer.UpdateTransferJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_transfer_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_update_transfer_job(
        self, response: transfer_types.TransferJob
    ) -> transfer_types.TransferJob:
        """Post-rpc interceptor for update_transfer_job

        DEPRECATED. Please use the `post_update_transfer_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code. This `post_update_transfer_job` interceptor runs
        before the `post_update_transfer_job_with_metadata` interceptor.
        """
        return response

    def post_update_transfer_job_with_metadata(
        self,
        response: transfer_types.TransferJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[transfer_types.TransferJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_transfer_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the StorageTransferService server but before it is returned to user code.

        We recommend only using this `post_update_transfer_job_with_metadata`
        interceptor in new development instead of the `post_update_transfer_job` interceptor.
        When both interceptors are used, this `post_update_transfer_job_with_metadata` interceptor runs after the
        `post_update_transfer_job` interceptor. The (possibly modified) response returned by
        `post_update_transfer_job` will be passed to
        `post_update_transfer_job_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the StorageTransferService server but before
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
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the StorageTransferService server but before
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
        before they are sent to the StorageTransferService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the StorageTransferService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class StorageTransferServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: StorageTransferServiceRestInterceptor


class StorageTransferServiceRestTransport(_BaseStorageTransferServiceRestTransport):
    """REST backend synchronous transport for StorageTransferService.

    Storage Transfer Service and its protos.
    Transfers data between between Google Cloud Storage buckets or
    from a data source external to Google to a Cloud Storage bucket.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "storagetransfer.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[StorageTransferServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'storagetransfer.googleapis.com').
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
            interceptor (Optional[StorageTransferServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or StorageTransferServiceRestInterceptor()
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
                        "uri": "/v1/{name=transferOperations/**}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=transferOperations/**}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=transferOperations}",
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

    class _CreateAgentPool(
        _BaseStorageTransferServiceRestTransport._BaseCreateAgentPool,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.CreateAgentPool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.CreateAgentPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer_types.AgentPool:
            r"""Call the create agent pool method over HTTP.

            Args:
                request (~.transfer.CreateAgentPoolRequest):
                    The request object. Specifies the request passed to
                CreateAgentPool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer_types.AgentPool:
                    Represents an agent pool.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseCreateAgentPool._get_http_options()
            request, metadata = self._interceptor.pre_create_agent_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseCreateAgentPool,
                    "_BaseCreateAgentPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.CreateAgentPool",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "CreateAgentPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._CreateAgentPool._get_response(
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
            resp = transfer_types.AgentPool()
            pb_resp = transfer_types.AgentPool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_agent_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_agent_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer_types.AgentPool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.create_agent_pool",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "CreateAgentPool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTransferJob(
        _BaseStorageTransferServiceRestTransport._BaseCreateTransferJob,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.CreateTransferJob")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.CreateTransferJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer_types.TransferJob:
            r"""Call the create transfer job method over HTTP.

            Args:
                request (~.transfer.CreateTransferJobRequest):
                    The request object. Request passed to CreateTransferJob.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer_types.TransferJob:
                    This resource represents the
                configuration of a transfer job that
                runs periodically.

            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseCreateTransferJob._get_http_options()
            request, metadata = self._interceptor.pre_create_transfer_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseCreateTransferJob,
                    "_BaseCreateTransferJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.CreateTransferJob",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "CreateTransferJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._CreateTransferJob._get_response(
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
            resp = transfer_types.TransferJob()
            pb_resp = transfer_types.TransferJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_transfer_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_transfer_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer_types.TransferJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.create_transfer_job",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "CreateTransferJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAgentPool(
        _BaseStorageTransferServiceRestTransport._BaseDeleteAgentPool,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.DeleteAgentPool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.DeleteAgentPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete agent pool method over HTTP.

            Args:
                request (~.transfer.DeleteAgentPoolRequest):
                    The request object. Specifies the request passed to
                DeleteAgentPool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseDeleteAgentPool._get_http_options()
            request, metadata = self._interceptor.pre_delete_agent_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseDeleteAgentPool,
                    "_BaseDeleteAgentPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.DeleteAgentPool",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "DeleteAgentPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._DeleteAgentPool._get_response(
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

    class _DeleteTransferJob(
        _BaseStorageTransferServiceRestTransport._BaseDeleteTransferJob,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.DeleteTransferJob")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.DeleteTransferJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete transfer job method over HTTP.

            Args:
                request (~.transfer.DeleteTransferJobRequest):
                    The request object. Request passed to DeleteTransferJob.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseDeleteTransferJob._get_http_options()
            request, metadata = self._interceptor.pre_delete_transfer_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseDeleteTransferJob,
                    "_BaseDeleteTransferJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.DeleteTransferJob",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "DeleteTransferJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._DeleteTransferJob._get_response(
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

    class _GetAgentPool(
        _BaseStorageTransferServiceRestTransport._BaseGetAgentPool,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.GetAgentPool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.GetAgentPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer_types.AgentPool:
            r"""Call the get agent pool method over HTTP.

            Args:
                request (~.transfer.GetAgentPoolRequest):
                    The request object. Specifies the request passed to
                GetAgentPool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer_types.AgentPool:
                    Represents an agent pool.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseGetAgentPool._get_http_options()
            request, metadata = self._interceptor.pre_get_agent_pool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseGetAgentPool,
                    "_BaseGetAgentPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.GetAgentPool",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "GetAgentPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageTransferServiceRestTransport._GetAgentPool._get_response(
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
            resp = transfer_types.AgentPool()
            pb_resp = transfer_types.AgentPool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_agent_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_agent_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer_types.AgentPool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.get_agent_pool",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "GetAgentPool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGoogleServiceAccount(
        _BaseStorageTransferServiceRestTransport._BaseGetGoogleServiceAccount,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.GetGoogleServiceAccount")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.GetGoogleServiceAccountRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer_types.GoogleServiceAccount:
            r"""Call the get google service
            account method over HTTP.

                Args:
                    request (~.transfer.GetGoogleServiceAccountRequest):
                        The request object. Request passed to
                    GetGoogleServiceAccount.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.transfer_types.GoogleServiceAccount:
                        Google service account
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseGetGoogleServiceAccount._get_http_options()
            request, metadata = self._interceptor.pre_get_google_service_account(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseGetGoogleServiceAccount,
                    "_BaseGetGoogleServiceAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.GetGoogleServiceAccount",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "GetGoogleServiceAccount",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageTransferServiceRestTransport._GetGoogleServiceAccount._get_response(
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
            resp = transfer_types.GoogleServiceAccount()
            pb_resp = transfer_types.GoogleServiceAccount.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_google_service_account(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_google_service_account_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer_types.GoogleServiceAccount.to_json(
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
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.get_google_service_account",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "GetGoogleServiceAccount",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTransferJob(
        _BaseStorageTransferServiceRestTransport._BaseGetTransferJob,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.GetTransferJob")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.GetTransferJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer_types.TransferJob:
            r"""Call the get transfer job method over HTTP.

            Args:
                request (~.transfer.GetTransferJobRequest):
                    The request object. Request passed to GetTransferJob.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer_types.TransferJob:
                    This resource represents the
                configuration of a transfer job that
                runs periodically.

            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseGetTransferJob._get_http_options()
            request, metadata = self._interceptor.pre_get_transfer_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseGetTransferJob,
                    "_BaseGetTransferJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.GetTransferJob",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "GetTransferJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._GetTransferJob._get_response(
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
            resp = transfer_types.TransferJob()
            pb_resp = transfer_types.TransferJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_transfer_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_transfer_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer_types.TransferJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.get_transfer_job",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "GetTransferJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAgentPools(
        _BaseStorageTransferServiceRestTransport._BaseListAgentPools,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.ListAgentPools")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.ListAgentPoolsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer.ListAgentPoolsResponse:
            r"""Call the list agent pools method over HTTP.

            Args:
                request (~.transfer.ListAgentPoolsRequest):
                    The request object. The request passed to ListAgentPools.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer.ListAgentPoolsResponse:
                    Response from ListAgentPools.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseListAgentPools._get_http_options()
            request, metadata = self._interceptor.pre_list_agent_pools(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseListAgentPools,
                    "_BaseListAgentPools__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.ListAgentPools",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "ListAgentPools",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._ListAgentPools._get_response(
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
            resp = transfer.ListAgentPoolsResponse()
            pb_resp = transfer.ListAgentPoolsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_agent_pools(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_agent_pools_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer.ListAgentPoolsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.list_agent_pools",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "ListAgentPools",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTransferJobs(
        _BaseStorageTransferServiceRestTransport._BaseListTransferJobs,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.ListTransferJobs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.ListTransferJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer.ListTransferJobsResponse:
            r"""Call the list transfer jobs method over HTTP.

            Args:
                request (~.transfer.ListTransferJobsRequest):
                    The request object. ``projectId``, ``jobNames``, and ``jobStatuses`` are
                query parameters that can be specified when listing
                transfer jobs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer.ListTransferJobsResponse:
                    Response from ListTransferJobs.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseListTransferJobs._get_http_options()
            request, metadata = self._interceptor.pre_list_transfer_jobs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseListTransferJobs,
                    "_BaseListTransferJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.ListTransferJobs",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "ListTransferJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._ListTransferJobs._get_response(
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
            resp = transfer.ListTransferJobsResponse()
            pb_resp = transfer.ListTransferJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_transfer_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_transfer_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer.ListTransferJobsResponse.to_json(
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
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.list_transfer_jobs",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "ListTransferJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PauseTransferOperation(
        _BaseStorageTransferServiceRestTransport._BasePauseTransferOperation,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.PauseTransferOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.PauseTransferOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the pause transfer operation method over HTTP.

            Args:
                request (~.transfer.PauseTransferOperationRequest):
                    The request object. Request passed to
                PauseTransferOperation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BasePauseTransferOperation._get_http_options()
            request, metadata = self._interceptor.pre_pause_transfer_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BasePauseTransferOperation,
                    "_BasePauseTransferOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.PauseTransferOperation",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "PauseTransferOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageTransferServiceRestTransport._PauseTransferOperation._get_response(
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

    class _ResumeTransferOperation(
        _BaseStorageTransferServiceRestTransport._BaseResumeTransferOperation,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.ResumeTransferOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.ResumeTransferOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the resume transfer operation method over HTTP.

            Args:
                request (~.transfer.ResumeTransferOperationRequest):
                    The request object. Request passed to
                ResumeTransferOperation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseResumeTransferOperation._get_http_options()
            request, metadata = self._interceptor.pre_resume_transfer_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseResumeTransferOperation,
                    "_BaseResumeTransferOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.ResumeTransferOperation",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "ResumeTransferOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageTransferServiceRestTransport._ResumeTransferOperation._get_response(
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

    class _RunTransferJob(
        _BaseStorageTransferServiceRestTransport._BaseRunTransferJob,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.RunTransferJob")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.RunTransferJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run transfer job method over HTTP.

            Args:
                request (~.transfer.RunTransferJobRequest):
                    The request object. Request passed to RunTransferJob.
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

            http_options = _BaseStorageTransferServiceRestTransport._BaseRunTransferJob._get_http_options()
            request, metadata = self._interceptor.pre_run_transfer_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseRunTransferJob,
                    "_BaseRunTransferJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.RunTransferJob",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "RunTransferJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._RunTransferJob._get_response(
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

            resp = self._interceptor.post_run_transfer_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_transfer_job_with_metadata(
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
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.run_transfer_job",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "RunTransferJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAgentPool(
        _BaseStorageTransferServiceRestTransport._BaseUpdateAgentPool,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.UpdateAgentPool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.UpdateAgentPoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer_types.AgentPool:
            r"""Call the update agent pool method over HTTP.

            Args:
                request (~.transfer.UpdateAgentPoolRequest):
                    The request object. Specifies the request passed to
                UpdateAgentPool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer_types.AgentPool:
                    Represents an agent pool.
            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseUpdateAgentPool._get_http_options()
            request, metadata = self._interceptor.pre_update_agent_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseUpdateAgentPool,
                    "_BaseUpdateAgentPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.UpdateAgentPool",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "UpdateAgentPool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._UpdateAgentPool._get_response(
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
            resp = transfer_types.AgentPool()
            pb_resp = transfer_types.AgentPool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_agent_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_agent_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer_types.AgentPool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.update_agent_pool",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "UpdateAgentPool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTransferJob(
        _BaseStorageTransferServiceRestTransport._BaseUpdateTransferJob,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.UpdateTransferJob")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: transfer.UpdateTransferJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> transfer_types.TransferJob:
            r"""Call the update transfer job method over HTTP.

            Args:
                request (~.transfer.UpdateTransferJobRequest):
                    The request object. Request passed to UpdateTransferJob.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.transfer_types.TransferJob:
                    This resource represents the
                configuration of a transfer job that
                runs periodically.

            """

            http_options = _BaseStorageTransferServiceRestTransport._BaseUpdateTransferJob._get_http_options()
            request, metadata = self._interceptor.pre_update_transfer_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseUpdateTransferJob,
                    "_BaseUpdateTransferJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.UpdateTransferJob",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "UpdateTransferJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._UpdateTransferJob._get_response(
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
            resp = transfer_types.TransferJob()
            pb_resp = transfer_types.TransferJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_transfer_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_transfer_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = transfer_types.TransferJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.storagetransfer_v1.StorageTransferServiceClient.update_transfer_job",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "UpdateTransferJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_agent_pool(
        self,
    ) -> Callable[[transfer.CreateAgentPoolRequest], transfer_types.AgentPool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAgentPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_transfer_job(
        self,
    ) -> Callable[[transfer.CreateTransferJobRequest], transfer_types.TransferJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTransferJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_agent_pool(
        self,
    ) -> Callable[[transfer.DeleteAgentPoolRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAgentPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_transfer_job(
        self,
    ) -> Callable[[transfer.DeleteTransferJobRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTransferJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_agent_pool(
        self,
    ) -> Callable[[transfer.GetAgentPoolRequest], transfer_types.AgentPool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAgentPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_google_service_account(
        self,
    ) -> Callable[
        [transfer.GetGoogleServiceAccountRequest], transfer_types.GoogleServiceAccount
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGoogleServiceAccount(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_transfer_job(
        self,
    ) -> Callable[[transfer.GetTransferJobRequest], transfer_types.TransferJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTransferJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_agent_pools(
        self,
    ) -> Callable[[transfer.ListAgentPoolsRequest], transfer.ListAgentPoolsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAgentPools(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_transfer_jobs(
        self,
    ) -> Callable[
        [transfer.ListTransferJobsRequest], transfer.ListTransferJobsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTransferJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def pause_transfer_operation(
        self,
    ) -> Callable[[transfer.PauseTransferOperationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PauseTransferOperation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def resume_transfer_operation(
        self,
    ) -> Callable[[transfer.ResumeTransferOperationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResumeTransferOperation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def run_transfer_job(
        self,
    ) -> Callable[[transfer.RunTransferJobRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunTransferJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_agent_pool(
        self,
    ) -> Callable[[transfer.UpdateAgentPoolRequest], transfer_types.AgentPool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAgentPool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_transfer_job(
        self,
    ) -> Callable[[transfer.UpdateTransferJobRequest], transfer_types.TransferJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTransferJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseStorageTransferServiceRestTransport._BaseCancelOperation,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseStorageTransferServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._CancelOperation._get_response(
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
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseStorageTransferServiceRestTransport._BaseGetOperation,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseStorageTransferServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = StorageTransferServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.storagetransfer_v1.StorageTransferServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
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
        _BaseStorageTransferServiceRestTransport._BaseListOperations,
        StorageTransferServiceRestStub,
    ):
        def __hash__(self):
            return hash("StorageTransferServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseStorageTransferServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseStorageTransferServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.storagetransfer_v1.StorageTransferServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                StorageTransferServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.storagetransfer_v1.StorageTransferServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.storagetransfer.v1.StorageTransferService",
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


__all__ = ("StorageTransferServiceRestTransport",)
