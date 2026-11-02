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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.dialogflowcx_v3._compat import transcode_request
from google.cloud.dialogflowcx_v3.types import agent, generative_settings
from google.cloud.dialogflowcx_v3.types import agent as gcdc_agent
from google.cloud.dialogflowcx_v3.types import (
    generative_settings as gcdc_generative_settings,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAgentsRestTransport

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


class AgentsRestInterceptor:
    """Interceptor for Agents.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AgentsRestTransport.

    .. code-block:: python
        class MyCustomAgentsInterceptor(AgentsRestInterceptor):
            def pre_create_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_export_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_agent_validation_result(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_agent_validation_result(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_generative_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_generative_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_agents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_agents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_generative_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_generative_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_validate_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AgentsRestTransport(interceptor=MyCustomAgentsInterceptor())
        client = AgentsClient(transport=transport)


    """

    def pre_create_agent(
        self,
        request: gcdc_agent.CreateAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcdc_agent.CreateAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_create_agent(self, response: gcdc_agent.Agent) -> gcdc_agent.Agent:
        """Post-rpc interceptor for create_agent

        DEPRECATED. Please use the `post_create_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_create_agent` interceptor runs
        before the `post_create_agent_with_metadata` interceptor.
        """
        return response

    def post_create_agent_with_metadata(
        self,
        response: gcdc_agent.Agent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcdc_agent.Agent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_create_agent_with_metadata`
        interceptor in new development instead of the `post_create_agent` interceptor.
        When both interceptors are used, this `post_create_agent_with_metadata` interceptor runs after the
        `post_create_agent` interceptor. The (possibly modified) response returned by
        `post_create_agent` will be passed to
        `post_create_agent_with_metadata`.
        """
        return response, metadata

    def pre_delete_agent(
        self,
        request: agent.DeleteAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.DeleteAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def pre_export_agent(
        self,
        request: agent.ExportAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.ExportAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for export_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_export_agent(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_agent

        DEPRECATED. Please use the `post_export_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_export_agent` interceptor runs
        before the `post_export_agent_with_metadata` interceptor.
        """
        return response

    def post_export_agent_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_export_agent_with_metadata`
        interceptor in new development instead of the `post_export_agent` interceptor.
        When both interceptors are used, this `post_export_agent_with_metadata` interceptor runs after the
        `post_export_agent` interceptor. The (possibly modified) response returned by
        `post_export_agent` will be passed to
        `post_export_agent_with_metadata`.
        """
        return response, metadata

    def pre_get_agent(
        self,
        request: agent.GetAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.GetAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_agent(self, response: agent.Agent) -> agent.Agent:
        """Post-rpc interceptor for get_agent

        DEPRECATED. Please use the `post_get_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_get_agent` interceptor runs
        before the `post_get_agent_with_metadata` interceptor.
        """
        return response

    def post_get_agent_with_metadata(
        self, response: agent.Agent, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[agent.Agent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_get_agent_with_metadata`
        interceptor in new development instead of the `post_get_agent` interceptor.
        When both interceptors are used, this `post_get_agent_with_metadata` interceptor runs after the
        `post_get_agent` interceptor. The (possibly modified) response returned by
        `post_get_agent` will be passed to
        `post_get_agent_with_metadata`.
        """
        return response, metadata

    def pre_get_agent_validation_result(
        self,
        request: agent.GetAgentValidationResultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent.GetAgentValidationResultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_agent_validation_result

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_agent_validation_result(
        self, response: agent.AgentValidationResult
    ) -> agent.AgentValidationResult:
        """Post-rpc interceptor for get_agent_validation_result

        DEPRECATED. Please use the `post_get_agent_validation_result_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_get_agent_validation_result` interceptor runs
        before the `post_get_agent_validation_result_with_metadata` interceptor.
        """
        return response

    def post_get_agent_validation_result_with_metadata(
        self,
        response: agent.AgentValidationResult,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.AgentValidationResult, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_agent_validation_result

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_get_agent_validation_result_with_metadata`
        interceptor in new development instead of the `post_get_agent_validation_result` interceptor.
        When both interceptors are used, this `post_get_agent_validation_result_with_metadata` interceptor runs after the
        `post_get_agent_validation_result` interceptor. The (possibly modified) response returned by
        `post_get_agent_validation_result` will be passed to
        `post_get_agent_validation_result_with_metadata`.
        """
        return response, metadata

    def pre_get_generative_settings(
        self,
        request: agent.GetGenerativeSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent.GetGenerativeSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_generative_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_generative_settings(
        self, response: generative_settings.GenerativeSettings
    ) -> generative_settings.GenerativeSettings:
        """Post-rpc interceptor for get_generative_settings

        DEPRECATED. Please use the `post_get_generative_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_get_generative_settings` interceptor runs
        before the `post_get_generative_settings_with_metadata` interceptor.
        """
        return response

    def post_get_generative_settings_with_metadata(
        self,
        response: generative_settings.GenerativeSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        generative_settings.GenerativeSettings, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_generative_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_get_generative_settings_with_metadata`
        interceptor in new development instead of the `post_get_generative_settings` interceptor.
        When both interceptors are used, this `post_get_generative_settings_with_metadata` interceptor runs after the
        `post_get_generative_settings` interceptor. The (possibly modified) response returned by
        `post_get_generative_settings` will be passed to
        `post_get_generative_settings_with_metadata`.
        """
        return response, metadata

    def pre_list_agents(
        self,
        request: agent.ListAgentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.ListAgentsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_agents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_list_agents(
        self, response: agent.ListAgentsResponse
    ) -> agent.ListAgentsResponse:
        """Post-rpc interceptor for list_agents

        DEPRECATED. Please use the `post_list_agents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_list_agents` interceptor runs
        before the `post_list_agents_with_metadata` interceptor.
        """
        return response

    def post_list_agents_with_metadata(
        self,
        response: agent.ListAgentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.ListAgentsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_agents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_list_agents_with_metadata`
        interceptor in new development instead of the `post_list_agents` interceptor.
        When both interceptors are used, this `post_list_agents_with_metadata` interceptor runs after the
        `post_list_agents` interceptor. The (possibly modified) response returned by
        `post_list_agents` will be passed to
        `post_list_agents_with_metadata`.
        """
        return response, metadata

    def pre_restore_agent(
        self,
        request: agent.RestoreAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.RestoreAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for restore_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_restore_agent(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restore_agent

        DEPRECATED. Please use the `post_restore_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_restore_agent` interceptor runs
        before the `post_restore_agent_with_metadata` interceptor.
        """
        return response

    def post_restore_agent_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_restore_agent_with_metadata`
        interceptor in new development instead of the `post_restore_agent` interceptor.
        When both interceptors are used, this `post_restore_agent_with_metadata` interceptor runs after the
        `post_restore_agent` interceptor. The (possibly modified) response returned by
        `post_restore_agent` will be passed to
        `post_restore_agent_with_metadata`.
        """
        return response, metadata

    def pre_update_agent(
        self,
        request: gcdc_agent.UpdateAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcdc_agent.UpdateAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_update_agent(self, response: gcdc_agent.Agent) -> gcdc_agent.Agent:
        """Post-rpc interceptor for update_agent

        DEPRECATED. Please use the `post_update_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_update_agent` interceptor runs
        before the `post_update_agent_with_metadata` interceptor.
        """
        return response

    def post_update_agent_with_metadata(
        self,
        response: gcdc_agent.Agent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcdc_agent.Agent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_update_agent_with_metadata`
        interceptor in new development instead of the `post_update_agent` interceptor.
        When both interceptors are used, this `post_update_agent_with_metadata` interceptor runs after the
        `post_update_agent` interceptor. The (possibly modified) response returned by
        `post_update_agent` will be passed to
        `post_update_agent_with_metadata`.
        """
        return response, metadata

    def pre_update_generative_settings(
        self,
        request: agent.UpdateGenerativeSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent.UpdateGenerativeSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_generative_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_update_generative_settings(
        self, response: gcdc_generative_settings.GenerativeSettings
    ) -> gcdc_generative_settings.GenerativeSettings:
        """Post-rpc interceptor for update_generative_settings

        DEPRECATED. Please use the `post_update_generative_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_update_generative_settings` interceptor runs
        before the `post_update_generative_settings_with_metadata` interceptor.
        """
        return response

    def post_update_generative_settings_with_metadata(
        self,
        response: gcdc_generative_settings.GenerativeSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcdc_generative_settings.GenerativeSettings,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_generative_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_update_generative_settings_with_metadata`
        interceptor in new development instead of the `post_update_generative_settings` interceptor.
        When both interceptors are used, this `post_update_generative_settings_with_metadata` interceptor runs after the
        `post_update_generative_settings` interceptor. The (possibly modified) response returned by
        `post_update_generative_settings` will be passed to
        `post_update_generative_settings_with_metadata`.
        """
        return response, metadata

    def pre_validate_agent(
        self,
        request: agent.ValidateAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.ValidateAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for validate_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_validate_agent(
        self, response: agent.AgentValidationResult
    ) -> agent.AgentValidationResult:
        """Post-rpc interceptor for validate_agent

        DEPRECATED. Please use the `post_validate_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code. This `post_validate_agent` interceptor runs
        before the `post_validate_agent_with_metadata` interceptor.
        """
        return response

    def post_validate_agent_with_metadata(
        self,
        response: agent.AgentValidationResult,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent.AgentValidationResult, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for validate_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Agents server but before it is returned to user code.

        We recommend only using this `post_validate_agent_with_metadata`
        interceptor in new development instead of the `post_validate_agent` interceptor.
        When both interceptors are used, this `post_validate_agent_with_metadata` interceptor runs after the
        `post_validate_agent` interceptor. The (possibly modified) response returned by
        `post_validate_agent` will be passed to
        `post_validate_agent_with_metadata`.
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
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
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
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
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
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
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
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
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
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AgentsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AgentsRestInterceptor


class AgentsRestTransport(_BaseAgentsRestTransport):
    """REST backend synchronous transport for Agents.

    Service for managing [Agents][google.cloud.dialogflow.cx.v3.Agent].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AgentsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dialogflow.googleapis.com').
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
            interceptor (Optional[AgentsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AgentsRestInterceptor()
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
                        "uri": "/v3/{name=projects/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v3/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v3/{name=projects/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v3/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v3/{name=projects/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v3/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v3",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateAgent(_BaseAgentsRestTransport._BaseCreateAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.CreateAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcdc_agent.CreateAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcdc_agent.Agent:
            r"""Call the create agent method over HTTP.

            Args:
                request (~.gcdc_agent.CreateAgentRequest):
                    The request object. The request message for
                [Agents.CreateAgent][google.cloud.dialogflow.cx.v3.Agents.CreateAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcdc_agent.Agent:
                    Agents are best described as Natural Language
                Understanding (NLU) modules that transform user requests
                into actionable data. You can include agents in your
                app, product, or service to determine user intent and
                respond to the user in a natural way.

                After you create an agent, you can add
                [Intents][google.cloud.dialogflow.cx.v3.Intent], [Entity
                Types][google.cloud.dialogflow.cx.v3.EntityType],
                [Flows][google.cloud.dialogflow.cx.v3.Flow],
                [Fulfillments][google.cloud.dialogflow.cx.v3.Fulfillment],
                [Webhooks][google.cloud.dialogflow.cx.v3.Webhook],
                [TransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroup]
                and so on to manage the conversation flows.

            """

            http_options = _BaseAgentsRestTransport._BaseCreateAgent._get_http_options()
            request, metadata = self._interceptor.pre_create_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseCreateAgent,
                    "_BaseCreateAgent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.CreateAgent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "CreateAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._CreateAgent._get_response(
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
            resp = gcdc_agent.Agent()
            pb_resp = gcdc_agent.Agent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_agent(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_agent_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcdc_agent.Agent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.create_agent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "CreateAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAgent(_BaseAgentsRestTransport._BaseDeleteAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.DeleteAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.DeleteAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete agent method over HTTP.

            Args:
                request (~.agent.DeleteAgentRequest):
                    The request object. The request message for
                [Agents.DeleteAgent][google.cloud.dialogflow.cx.v3.Agents.DeleteAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAgentsRestTransport._BaseDeleteAgent._get_http_options()
            request, metadata = self._interceptor.pre_delete_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseDeleteAgent,
                    "_BaseDeleteAgent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.DeleteAgent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "DeleteAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._DeleteAgent._get_response(
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

    class _ExportAgent(_BaseAgentsRestTransport._BaseExportAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ExportAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.ExportAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export agent method over HTTP.

            Args:
                request (~.agent.ExportAgentRequest):
                    The request object. The request message for
                [Agents.ExportAgent][google.cloud.dialogflow.cx.v3.Agents.ExportAgent].
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

            http_options = _BaseAgentsRestTransport._BaseExportAgent._get_http_options()
            request, metadata = self._interceptor.pre_export_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseExportAgent,
                    "_BaseExportAgent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.ExportAgent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "ExportAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._ExportAgent._get_response(
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

            resp = self._interceptor.post_export_agent(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_agent_with_metadata(
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
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.export_agent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "ExportAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAgent(_BaseAgentsRestTransport._BaseGetAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.GetAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.GetAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent.Agent:
            r"""Call the get agent method over HTTP.

            Args:
                request (~.agent.GetAgentRequest):
                    The request object. The request message for
                [Agents.GetAgent][google.cloud.dialogflow.cx.v3.Agents.GetAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent.Agent:
                    Agents are best described as Natural Language
                Understanding (NLU) modules that transform user requests
                into actionable data. You can include agents in your
                app, product, or service to determine user intent and
                respond to the user in a natural way.

                After you create an agent, you can add
                [Intents][google.cloud.dialogflow.cx.v3.Intent], [Entity
                Types][google.cloud.dialogflow.cx.v3.EntityType],
                [Flows][google.cloud.dialogflow.cx.v3.Flow],
                [Fulfillments][google.cloud.dialogflow.cx.v3.Fulfillment],
                [Webhooks][google.cloud.dialogflow.cx.v3.Webhook],
                [TransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroup]
                and so on to manage the conversation flows.

            """

            http_options = _BaseAgentsRestTransport._BaseGetAgent._get_http_options()
            request, metadata = self._interceptor.pre_get_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseGetAgent,
                    "_BaseGetAgent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.GetAgent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._GetAgent._get_response(
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
            resp = agent.Agent()
            pb_resp = agent.Agent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_agent(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_agent_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent.Agent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.get_agent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAgentValidationResult(
        _BaseAgentsRestTransport._BaseGetAgentValidationResult, AgentsRestStub
    ):
        def __hash__(self):
            return hash("AgentsRestTransport.GetAgentValidationResult")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.GetAgentValidationResultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent.AgentValidationResult:
            r"""Call the get agent validation
            result method over HTTP.

                Args:
                    request (~.agent.GetAgentValidationResultRequest):
                        The request object. The request message for
                    [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.agent.AgentValidationResult:
                        The response message for
                    [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult].

            """

            http_options = _BaseAgentsRestTransport._BaseGetAgentValidationResult._get_http_options()
            request, metadata = self._interceptor.pre_get_agent_validation_result(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseGetAgentValidationResult,
                    "_BaseGetAgentValidationResult__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.GetAgentValidationResult",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetAgentValidationResult",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._GetAgentValidationResult._get_response(
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
            resp = agent.AgentValidationResult()
            pb_resp = agent.AgentValidationResult.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_agent_validation_result(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_agent_validation_result_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent.AgentValidationResult.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.get_agent_validation_result",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetAgentValidationResult",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGenerativeSettings(
        _BaseAgentsRestTransport._BaseGetGenerativeSettings, AgentsRestStub
    ):
        def __hash__(self):
            return hash("AgentsRestTransport.GetGenerativeSettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.GetGenerativeSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> generative_settings.GenerativeSettings:
            r"""Call the get generative settings method over HTTP.

            Args:
                request (~.agent.GetGenerativeSettingsRequest):
                    The request object. Request for
                [GetGenerativeSettings][google.cloud.dialogflow.cx.v3.Agents.GetGenerativeSettings]
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.generative_settings.GenerativeSettings:
                    Settings for Generative AI.
            """

            http_options = (
                _BaseAgentsRestTransport._BaseGetGenerativeSettings._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_generative_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseGetGenerativeSettings,
                    "_BaseGetGenerativeSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.GetGenerativeSettings",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetGenerativeSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._GetGenerativeSettings._get_response(
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
            resp = generative_settings.GenerativeSettings()
            pb_resp = generative_settings.GenerativeSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_generative_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_generative_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = generative_settings.GenerativeSettings.to_json(
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
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.get_generative_settings",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetGenerativeSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAgents(_BaseAgentsRestTransport._BaseListAgents, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ListAgents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.ListAgentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent.ListAgentsResponse:
            r"""Call the list agents method over HTTP.

            Args:
                request (~.agent.ListAgentsRequest):
                    The request object. The request message for
                [Agents.ListAgents][google.cloud.dialogflow.cx.v3.Agents.ListAgents].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent.ListAgentsResponse:
                    The response message for
                [Agents.ListAgents][google.cloud.dialogflow.cx.v3.Agents.ListAgents].

            """

            http_options = _BaseAgentsRestTransport._BaseListAgents._get_http_options()
            request, metadata = self._interceptor.pre_list_agents(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseListAgents,
                    "_BaseListAgents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.ListAgents",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "ListAgents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._ListAgents._get_response(
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
            resp = agent.ListAgentsResponse()
            pb_resp = agent.ListAgentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_agents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_agents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent.ListAgentsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.list_agents",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "ListAgents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreAgent(_BaseAgentsRestTransport._BaseRestoreAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.RestoreAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.RestoreAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restore agent method over HTTP.

            Args:
                request (~.agent.RestoreAgentRequest):
                    The request object. The request message for
                [Agents.RestoreAgent][google.cloud.dialogflow.cx.v3.Agents.RestoreAgent].
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
                _BaseAgentsRestTransport._BaseRestoreAgent._get_http_options()
            )
            request, metadata = self._interceptor.pre_restore_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseRestoreAgent,
                    "_BaseRestoreAgent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.RestoreAgent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "RestoreAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._RestoreAgent._get_response(
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

            resp = self._interceptor.post_restore_agent(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_agent_with_metadata(
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
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.restore_agent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "RestoreAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAgent(_BaseAgentsRestTransport._BaseUpdateAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.UpdateAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcdc_agent.UpdateAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcdc_agent.Agent:
            r"""Call the update agent method over HTTP.

            Args:
                request (~.gcdc_agent.UpdateAgentRequest):
                    The request object. The request message for
                [Agents.UpdateAgent][google.cloud.dialogflow.cx.v3.Agents.UpdateAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcdc_agent.Agent:
                    Agents are best described as Natural Language
                Understanding (NLU) modules that transform user requests
                into actionable data. You can include agents in your
                app, product, or service to determine user intent and
                respond to the user in a natural way.

                After you create an agent, you can add
                [Intents][google.cloud.dialogflow.cx.v3.Intent], [Entity
                Types][google.cloud.dialogflow.cx.v3.EntityType],
                [Flows][google.cloud.dialogflow.cx.v3.Flow],
                [Fulfillments][google.cloud.dialogflow.cx.v3.Fulfillment],
                [Webhooks][google.cloud.dialogflow.cx.v3.Webhook],
                [TransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroup]
                and so on to manage the conversation flows.

            """

            http_options = _BaseAgentsRestTransport._BaseUpdateAgent._get_http_options()
            request, metadata = self._interceptor.pre_update_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseUpdateAgent,
                    "_BaseUpdateAgent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.UpdateAgent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "UpdateAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._UpdateAgent._get_response(
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
            resp = gcdc_agent.Agent()
            pb_resp = gcdc_agent.Agent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_agent(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_agent_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcdc_agent.Agent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.update_agent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "UpdateAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGenerativeSettings(
        _BaseAgentsRestTransport._BaseUpdateGenerativeSettings, AgentsRestStub
    ):
        def __hash__(self):
            return hash("AgentsRestTransport.UpdateGenerativeSettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.UpdateGenerativeSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcdc_generative_settings.GenerativeSettings:
            r"""Call the update generative
            settings method over HTTP.

                Args:
                    request (~.agent.UpdateGenerativeSettingsRequest):
                        The request object. Request for
                    [UpdateGenerativeSettings][google.cloud.dialogflow.cx.v3.Agents.UpdateGenerativeSettings]
                    RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcdc_generative_settings.GenerativeSettings:
                        Settings for Generative AI.
            """

            http_options = _BaseAgentsRestTransport._BaseUpdateGenerativeSettings._get_http_options()
            request, metadata = self._interceptor.pre_update_generative_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseUpdateGenerativeSettings,
                    "_BaseUpdateGenerativeSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.UpdateGenerativeSettings",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "UpdateGenerativeSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._UpdateGenerativeSettings._get_response(
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
            resp = gcdc_generative_settings.GenerativeSettings()
            pb_resp = gcdc_generative_settings.GenerativeSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_generative_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_generative_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcdc_generative_settings.GenerativeSettings.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.update_generative_settings",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "UpdateGenerativeSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ValidateAgent(_BaseAgentsRestTransport._BaseValidateAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ValidateAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent.ValidateAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent.AgentValidationResult:
            r"""Call the validate agent method over HTTP.

            Args:
                request (~.agent.ValidateAgentRequest):
                    The request object. The request message for
                [Agents.ValidateAgent][google.cloud.dialogflow.cx.v3.Agents.ValidateAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent.AgentValidationResult:
                    The response message for
                [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult].

            """

            http_options = (
                _BaseAgentsRestTransport._BaseValidateAgent._get_http_options()
            )
            request, metadata = self._interceptor.pre_validate_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseValidateAgent,
                    "_BaseValidateAgent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.ValidateAgent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "ValidateAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._ValidateAgent._get_response(
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
            resp = agent.AgentValidationResult()
            pb_resp = agent.AgentValidationResult.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_validate_agent(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_validate_agent_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent.AgentValidationResult.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsClient.validate_agent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "ValidateAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_agent(
        self,
    ) -> Callable[[gcdc_agent.CreateAgentRequest], gcdc_agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_agent(self) -> Callable[[agent.DeleteAgentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_agent(
        self,
    ) -> Callable[[agent.ExportAgentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_agent(self) -> Callable[[agent.GetAgentRequest], agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_agent_validation_result(
        self,
    ) -> Callable[[agent.GetAgentValidationResultRequest], agent.AgentValidationResult]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAgentValidationResult(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_generative_settings(
        self,
    ) -> Callable[
        [agent.GetGenerativeSettingsRequest], generative_settings.GenerativeSettings
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGenerativeSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_agents(
        self,
    ) -> Callable[[agent.ListAgentsRequest], agent.ListAgentsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAgents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_agent(
        self,
    ) -> Callable[[agent.RestoreAgentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_agent(
        self,
    ) -> Callable[[gcdc_agent.UpdateAgentRequest], gcdc_agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_generative_settings(
        self,
    ) -> Callable[
        [agent.UpdateGenerativeSettingsRequest],
        gcdc_generative_settings.GenerativeSettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGenerativeSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def validate_agent(
        self,
    ) -> Callable[[agent.ValidateAgentRequest], agent.AgentValidationResult]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseAgentsRestTransport._BaseGetLocation, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseAgentsRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(_BaseAgentsRestTransport._BaseListLocations, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentsRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
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
        _BaseAgentsRestTransport._BaseCancelOperation, AgentsRestStub
    ):
        def __hash__(self):
            return hash("AgentsRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = (
                _BaseAgentsRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(_BaseAgentsRestTransport._BaseGetOperation, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentsRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(_BaseAgentsRestTransport._BaseListOperations, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentsRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentsRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.AgentsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentsRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3.AgentsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Agents",
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


__all__ = ("AgentsRestTransport",)
