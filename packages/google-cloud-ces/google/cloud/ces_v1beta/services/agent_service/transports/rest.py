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

from google.cloud.ces_v1beta._compat import transcode_request
from google.cloud.ces_v1beta.types import (
    agent,
    agent_service,
    app,
    app_version,
    changelog,
    conversation,
    deployment,
    example,
    guardrail,
    security_settings,
    tool,
    toolset,
)
from google.cloud.ces_v1beta.types import agent as gcc_agent
from google.cloud.ces_v1beta.types import app as gcc_app
from google.cloud.ces_v1beta.types import app_version as gcc_app_version
from google.cloud.ces_v1beta.types import deployment as gcc_deployment
from google.cloud.ces_v1beta.types import example as gcc_example
from google.cloud.ces_v1beta.types import guardrail as gcc_guardrail
from google.cloud.ces_v1beta.types import security_settings as gcc_security_settings
from google.cloud.ces_v1beta.types import tool as gcc_tool
from google.cloud.ces_v1beta.types import toolset as gcc_toolset

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAgentServiceRestTransport

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


class AgentServiceRestInterceptor:
    """Interceptor for AgentService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AgentServiceRestTransport.

    .. code-block:: python
        class MyCustomAgentServiceInterceptor(AgentServiceRestInterceptor):
            def pre_batch_delete_conversations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_delete_conversations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_app(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_app(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_app_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_app_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_example(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_example(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_guardrail(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_guardrail(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_toolset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_toolset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_app(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_app(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_app_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_example(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_guardrail(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_tool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_toolset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_export_app(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_app(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_app_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_app_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_app(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_app(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_app_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_app_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_changelog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_changelog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_conversation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_example(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_example(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_guardrail(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_guardrail(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_security_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_security_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_toolset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_toolset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_app(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_app(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_agents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_agents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_apps(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_apps(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_app_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_app_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_changelogs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_changelogs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_conversations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_conversations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_examples(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_examples(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_guardrails(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_guardrails(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tools(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tools(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_toolsets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_toolsets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_app_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_app_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_app(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_app(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_example(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_example(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_guardrail(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_guardrail(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_security_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_security_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_toolset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_toolset(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AgentServiceRestTransport(interceptor=MyCustomAgentServiceInterceptor())
        client = AgentServiceClient(transport=transport)


    """

    def pre_batch_delete_conversations(
        self,
        request: agent_service.BatchDeleteConversationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.BatchDeleteConversationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_delete_conversations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_batch_delete_conversations(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_delete_conversations

        DEPRECATED. Please use the `post_batch_delete_conversations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_batch_delete_conversations` interceptor runs
        before the `post_batch_delete_conversations_with_metadata` interceptor.
        """
        return response

    def post_batch_delete_conversations_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_delete_conversations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_batch_delete_conversations_with_metadata`
        interceptor in new development instead of the `post_batch_delete_conversations` interceptor.
        When both interceptors are used, this `post_batch_delete_conversations_with_metadata` interceptor runs after the
        `post_batch_delete_conversations` interceptor. The (possibly modified) response returned by
        `post_batch_delete_conversations` will be passed to
        `post_batch_delete_conversations_with_metadata`.
        """
        return response, metadata

    def pre_create_agent(
        self,
        request: agent_service.CreateAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.CreateAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_create_agent(self, response: gcc_agent.Agent) -> gcc_agent.Agent:
        """Post-rpc interceptor for create_agent

        DEPRECATED. Please use the `post_create_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_create_agent` interceptor runs
        before the `post_create_agent_with_metadata` interceptor.
        """
        return response

    def post_create_agent_with_metadata(
        self,
        response: gcc_agent.Agent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_agent.Agent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_create_agent_with_metadata`
        interceptor in new development instead of the `post_create_agent` interceptor.
        When both interceptors are used, this `post_create_agent_with_metadata` interceptor runs after the
        `post_create_agent` interceptor. The (possibly modified) response returned by
        `post_create_agent` will be passed to
        `post_create_agent_with_metadata`.
        """
        return response, metadata

    def pre_create_app(
        self,
        request: agent_service.CreateAppRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.CreateAppRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_app

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_create_app(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_app

        DEPRECATED. Please use the `post_create_app_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_create_app` interceptor runs
        before the `post_create_app_with_metadata` interceptor.
        """
        return response

    def post_create_app_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_app

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_create_app_with_metadata`
        interceptor in new development instead of the `post_create_app` interceptor.
        When both interceptors are used, this `post_create_app_with_metadata` interceptor runs after the
        `post_create_app` interceptor. The (possibly modified) response returned by
        `post_create_app` will be passed to
        `post_create_app_with_metadata`.
        """
        return response, metadata

    def pre_create_app_version(
        self,
        request: agent_service.CreateAppVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.CreateAppVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_app_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_create_app_version(
        self, response: gcc_app_version.AppVersion
    ) -> gcc_app_version.AppVersion:
        """Post-rpc interceptor for create_app_version

        DEPRECATED. Please use the `post_create_app_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_create_app_version` interceptor runs
        before the `post_create_app_version_with_metadata` interceptor.
        """
        return response

    def post_create_app_version_with_metadata(
        self,
        response: gcc_app_version.AppVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_app_version.AppVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_app_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_create_app_version_with_metadata`
        interceptor in new development instead of the `post_create_app_version` interceptor.
        When both interceptors are used, this `post_create_app_version_with_metadata` interceptor runs after the
        `post_create_app_version` interceptor. The (possibly modified) response returned by
        `post_create_app_version` will be passed to
        `post_create_app_version_with_metadata`.
        """
        return response, metadata

    def pre_create_deployment(
        self,
        request: agent_service.CreateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.CreateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_create_deployment(
        self, response: gcc_deployment.Deployment
    ) -> gcc_deployment.Deployment:
        """Post-rpc interceptor for create_deployment

        DEPRECATED. Please use the `post_create_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_create_deployment` interceptor runs
        before the `post_create_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_deployment_with_metadata(
        self,
        response: gcc_deployment.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_deployment.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_create_deployment_with_metadata`
        interceptor in new development instead of the `post_create_deployment` interceptor.
        When both interceptors are used, this `post_create_deployment_with_metadata` interceptor runs after the
        `post_create_deployment` interceptor. The (possibly modified) response returned by
        `post_create_deployment` will be passed to
        `post_create_deployment_with_metadata`.
        """
        return response, metadata

    def pre_create_example(
        self,
        request: agent_service.CreateExampleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.CreateExampleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_example

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_create_example(self, response: gcc_example.Example) -> gcc_example.Example:
        """Post-rpc interceptor for create_example

        DEPRECATED. Please use the `post_create_example_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_create_example` interceptor runs
        before the `post_create_example_with_metadata` interceptor.
        """
        return response

    def post_create_example_with_metadata(
        self,
        response: gcc_example.Example,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_example.Example, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_example

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_create_example_with_metadata`
        interceptor in new development instead of the `post_create_example` interceptor.
        When both interceptors are used, this `post_create_example_with_metadata` interceptor runs after the
        `post_create_example` interceptor. The (possibly modified) response returned by
        `post_create_example` will be passed to
        `post_create_example_with_metadata`.
        """
        return response, metadata

    def pre_create_guardrail(
        self,
        request: agent_service.CreateGuardrailRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.CreateGuardrailRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_guardrail

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_create_guardrail(
        self, response: gcc_guardrail.Guardrail
    ) -> gcc_guardrail.Guardrail:
        """Post-rpc interceptor for create_guardrail

        DEPRECATED. Please use the `post_create_guardrail_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_create_guardrail` interceptor runs
        before the `post_create_guardrail_with_metadata` interceptor.
        """
        return response

    def post_create_guardrail_with_metadata(
        self,
        response: gcc_guardrail.Guardrail,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_guardrail.Guardrail, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_guardrail

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_create_guardrail_with_metadata`
        interceptor in new development instead of the `post_create_guardrail` interceptor.
        When both interceptors are used, this `post_create_guardrail_with_metadata` interceptor runs after the
        `post_create_guardrail` interceptor. The (possibly modified) response returned by
        `post_create_guardrail` will be passed to
        `post_create_guardrail_with_metadata`.
        """
        return response, metadata

    def pre_create_tool(
        self,
        request: agent_service.CreateToolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.CreateToolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_tool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_create_tool(self, response: gcc_tool.Tool) -> gcc_tool.Tool:
        """Post-rpc interceptor for create_tool

        DEPRECATED. Please use the `post_create_tool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_create_tool` interceptor runs
        before the `post_create_tool_with_metadata` interceptor.
        """
        return response

    def post_create_tool_with_metadata(
        self, response: gcc_tool.Tool, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcc_tool.Tool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_tool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_create_tool_with_metadata`
        interceptor in new development instead of the `post_create_tool` interceptor.
        When both interceptors are used, this `post_create_tool_with_metadata` interceptor runs after the
        `post_create_tool` interceptor. The (possibly modified) response returned by
        `post_create_tool` will be passed to
        `post_create_tool_with_metadata`.
        """
        return response, metadata

    def pre_create_toolset(
        self,
        request: agent_service.CreateToolsetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.CreateToolsetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_toolset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_create_toolset(self, response: gcc_toolset.Toolset) -> gcc_toolset.Toolset:
        """Post-rpc interceptor for create_toolset

        DEPRECATED. Please use the `post_create_toolset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_create_toolset` interceptor runs
        before the `post_create_toolset_with_metadata` interceptor.
        """
        return response

    def post_create_toolset_with_metadata(
        self,
        response: gcc_toolset.Toolset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_toolset.Toolset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_toolset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_create_toolset_with_metadata`
        interceptor in new development instead of the `post_create_toolset` interceptor.
        When both interceptors are used, this `post_create_toolset_with_metadata` interceptor runs after the
        `post_create_toolset` interceptor. The (possibly modified) response returned by
        `post_create_toolset` will be passed to
        `post_create_toolset_with_metadata`.
        """
        return response, metadata

    def pre_delete_agent(
        self,
        request: agent_service.DeleteAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.DeleteAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def pre_delete_app(
        self,
        request: agent_service.DeleteAppRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.DeleteAppRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_app

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_delete_app(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_app

        DEPRECATED. Please use the `post_delete_app_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_delete_app` interceptor runs
        before the `post_delete_app_with_metadata` interceptor.
        """
        return response

    def post_delete_app_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_app

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_delete_app_with_metadata`
        interceptor in new development instead of the `post_delete_app` interceptor.
        When both interceptors are used, this `post_delete_app_with_metadata` interceptor runs after the
        `post_delete_app` interceptor. The (possibly modified) response returned by
        `post_delete_app` will be passed to
        `post_delete_app_with_metadata`.
        """
        return response, metadata

    def pre_delete_app_version(
        self,
        request: agent_service.DeleteAppVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.DeleteAppVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_app_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def pre_delete_conversation(
        self,
        request: agent_service.DeleteConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.DeleteConversationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def pre_delete_deployment(
        self,
        request: agent_service.DeleteDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.DeleteDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def pre_delete_example(
        self,
        request: agent_service.DeleteExampleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.DeleteExampleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_example

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def pre_delete_guardrail(
        self,
        request: agent_service.DeleteGuardrailRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.DeleteGuardrailRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_guardrail

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def pre_delete_tool(
        self,
        request: agent_service.DeleteToolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.DeleteToolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_tool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def pre_delete_toolset(
        self,
        request: agent_service.DeleteToolsetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.DeleteToolsetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_toolset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def pre_export_app(
        self,
        request: agent_service.ExportAppRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.ExportAppRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for export_app

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_export_app(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_app

        DEPRECATED. Please use the `post_export_app_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_export_app` interceptor runs
        before the `post_export_app_with_metadata` interceptor.
        """
        return response

    def post_export_app_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_app

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_export_app_with_metadata`
        interceptor in new development instead of the `post_export_app` interceptor.
        When both interceptors are used, this `post_export_app_with_metadata` interceptor runs after the
        `post_export_app` interceptor. The (possibly modified) response returned by
        `post_export_app` will be passed to
        `post_export_app_with_metadata`.
        """
        return response, metadata

    def pre_generate_app_resource(
        self,
        request: agent_service.GenerateAppResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GenerateAppResourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_app_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_generate_app_resource(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for generate_app_resource

        DEPRECATED. Please use the `post_generate_app_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_generate_app_resource` interceptor runs
        before the `post_generate_app_resource_with_metadata` interceptor.
        """
        return response

    def post_generate_app_resource_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_app_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_generate_app_resource_with_metadata`
        interceptor in new development instead of the `post_generate_app_resource` interceptor.
        When both interceptors are used, this `post_generate_app_resource_with_metadata` interceptor runs after the
        `post_generate_app_resource` interceptor. The (possibly modified) response returned by
        `post_generate_app_resource` will be passed to
        `post_generate_app_resource_with_metadata`.
        """
        return response, metadata

    def pre_get_agent(
        self,
        request: agent_service.GetAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.GetAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_agent(self, response: agent.Agent) -> agent.Agent:
        """Post-rpc interceptor for get_agent

        DEPRECATED. Please use the `post_get_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_agent` interceptor runs
        before the `post_get_agent_with_metadata` interceptor.
        """
        return response

    def post_get_agent_with_metadata(
        self, response: agent.Agent, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[agent.Agent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_agent_with_metadata`
        interceptor in new development instead of the `post_get_agent` interceptor.
        When both interceptors are used, this `post_get_agent_with_metadata` interceptor runs after the
        `post_get_agent` interceptor. The (possibly modified) response returned by
        `post_get_agent` will be passed to
        `post_get_agent_with_metadata`.
        """
        return response, metadata

    def pre_get_app(
        self,
        request: agent_service.GetAppRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.GetAppRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_app

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_app(self, response: app.App) -> app.App:
        """Post-rpc interceptor for get_app

        DEPRECATED. Please use the `post_get_app_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_app` interceptor runs
        before the `post_get_app_with_metadata` interceptor.
        """
        return response

    def post_get_app_with_metadata(
        self, response: app.App, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[app.App, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_app

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_app_with_metadata`
        interceptor in new development instead of the `post_get_app` interceptor.
        When both interceptors are used, this `post_get_app_with_metadata` interceptor runs after the
        `post_get_app` interceptor. The (possibly modified) response returned by
        `post_get_app` will be passed to
        `post_get_app_with_metadata`.
        """
        return response, metadata

    def pre_get_app_version(
        self,
        request: agent_service.GetAppVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GetAppVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_app_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_app_version(
        self, response: app_version.AppVersion
    ) -> app_version.AppVersion:
        """Post-rpc interceptor for get_app_version

        DEPRECATED. Please use the `post_get_app_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_app_version` interceptor runs
        before the `post_get_app_version_with_metadata` interceptor.
        """
        return response

    def post_get_app_version_with_metadata(
        self,
        response: app_version.AppVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[app_version.AppVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_app_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_app_version_with_metadata`
        interceptor in new development instead of the `post_get_app_version` interceptor.
        When both interceptors are used, this `post_get_app_version_with_metadata` interceptor runs after the
        `post_get_app_version` interceptor. The (possibly modified) response returned by
        `post_get_app_version` will be passed to
        `post_get_app_version_with_metadata`.
        """
        return response, metadata

    def pre_get_changelog(
        self,
        request: agent_service.GetChangelogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GetChangelogRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_changelog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_changelog(self, response: changelog.Changelog) -> changelog.Changelog:
        """Post-rpc interceptor for get_changelog

        DEPRECATED. Please use the `post_get_changelog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_changelog` interceptor runs
        before the `post_get_changelog_with_metadata` interceptor.
        """
        return response

    def post_get_changelog_with_metadata(
        self,
        response: changelog.Changelog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[changelog.Changelog, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_changelog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_changelog_with_metadata`
        interceptor in new development instead of the `post_get_changelog` interceptor.
        When both interceptors are used, this `post_get_changelog_with_metadata` interceptor runs after the
        `post_get_changelog` interceptor. The (possibly modified) response returned by
        `post_get_changelog` will be passed to
        `post_get_changelog_with_metadata`.
        """
        return response, metadata

    def pre_get_conversation(
        self,
        request: agent_service.GetConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GetConversationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_conversation(
        self, response: conversation.Conversation
    ) -> conversation.Conversation:
        """Post-rpc interceptor for get_conversation

        DEPRECATED. Please use the `post_get_conversation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_conversation` interceptor runs
        before the `post_get_conversation_with_metadata` interceptor.
        """
        return response

    def post_get_conversation_with_metadata(
        self,
        response: conversation.Conversation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[conversation.Conversation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_conversation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_conversation_with_metadata`
        interceptor in new development instead of the `post_get_conversation` interceptor.
        When both interceptors are used, this `post_get_conversation_with_metadata` interceptor runs after the
        `post_get_conversation` interceptor. The (possibly modified) response returned by
        `post_get_conversation` will be passed to
        `post_get_conversation_with_metadata`.
        """
        return response, metadata

    def pre_get_deployment(
        self,
        request: agent_service.GetDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GetDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_deployment(
        self, response: deployment.Deployment
    ) -> deployment.Deployment:
        """Post-rpc interceptor for get_deployment

        DEPRECATED. Please use the `post_get_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_deployment` interceptor runs
        before the `post_get_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_deployment_with_metadata(
        self,
        response: deployment.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployment.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_deployment_with_metadata`
        interceptor in new development instead of the `post_get_deployment` interceptor.
        When both interceptors are used, this `post_get_deployment_with_metadata` interceptor runs after the
        `post_get_deployment` interceptor. The (possibly modified) response returned by
        `post_get_deployment` will be passed to
        `post_get_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_example(
        self,
        request: agent_service.GetExampleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GetExampleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_example

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_example(self, response: example.Example) -> example.Example:
        """Post-rpc interceptor for get_example

        DEPRECATED. Please use the `post_get_example_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_example` interceptor runs
        before the `post_get_example_with_metadata` interceptor.
        """
        return response

    def post_get_example_with_metadata(
        self,
        response: example.Example,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[example.Example, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_example

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_example_with_metadata`
        interceptor in new development instead of the `post_get_example` interceptor.
        When both interceptors are used, this `post_get_example_with_metadata` interceptor runs after the
        `post_get_example` interceptor. The (possibly modified) response returned by
        `post_get_example` will be passed to
        `post_get_example_with_metadata`.
        """
        return response, metadata

    def pre_get_guardrail(
        self,
        request: agent_service.GetGuardrailRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GetGuardrailRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_guardrail

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_guardrail(self, response: guardrail.Guardrail) -> guardrail.Guardrail:
        """Post-rpc interceptor for get_guardrail

        DEPRECATED. Please use the `post_get_guardrail_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_guardrail` interceptor runs
        before the `post_get_guardrail_with_metadata` interceptor.
        """
        return response

    def post_get_guardrail_with_metadata(
        self,
        response: guardrail.Guardrail,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[guardrail.Guardrail, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_guardrail

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_guardrail_with_metadata`
        interceptor in new development instead of the `post_get_guardrail` interceptor.
        When both interceptors are used, this `post_get_guardrail_with_metadata` interceptor runs after the
        `post_get_guardrail` interceptor. The (possibly modified) response returned by
        `post_get_guardrail` will be passed to
        `post_get_guardrail_with_metadata`.
        """
        return response, metadata

    def pre_get_security_settings(
        self,
        request: agent_service.GetSecuritySettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GetSecuritySettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_security_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_security_settings(
        self, response: security_settings.SecuritySettings
    ) -> security_settings.SecuritySettings:
        """Post-rpc interceptor for get_security_settings

        DEPRECATED. Please use the `post_get_security_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_security_settings` interceptor runs
        before the `post_get_security_settings_with_metadata` interceptor.
        """
        return response

    def post_get_security_settings_with_metadata(
        self,
        response: security_settings.SecuritySettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_settings.SecuritySettings, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_security_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_security_settings_with_metadata`
        interceptor in new development instead of the `post_get_security_settings` interceptor.
        When both interceptors are used, this `post_get_security_settings_with_metadata` interceptor runs after the
        `post_get_security_settings` interceptor. The (possibly modified) response returned by
        `post_get_security_settings` will be passed to
        `post_get_security_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_tool(
        self,
        request: agent_service.GetToolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.GetToolRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_tool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_tool(self, response: tool.Tool) -> tool.Tool:
        """Post-rpc interceptor for get_tool

        DEPRECATED. Please use the `post_get_tool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_tool` interceptor runs
        before the `post_get_tool_with_metadata` interceptor.
        """
        return response

    def post_get_tool_with_metadata(
        self, response: tool.Tool, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[tool.Tool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_tool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_tool_with_metadata`
        interceptor in new development instead of the `post_get_tool` interceptor.
        When both interceptors are used, this `post_get_tool_with_metadata` interceptor runs after the
        `post_get_tool` interceptor. The (possibly modified) response returned by
        `post_get_tool` will be passed to
        `post_get_tool_with_metadata`.
        """
        return response, metadata

    def pre_get_toolset(
        self,
        request: agent_service.GetToolsetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.GetToolsetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_toolset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_toolset(self, response: toolset.Toolset) -> toolset.Toolset:
        """Post-rpc interceptor for get_toolset

        DEPRECATED. Please use the `post_get_toolset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_get_toolset` interceptor runs
        before the `post_get_toolset_with_metadata` interceptor.
        """
        return response

    def post_get_toolset_with_metadata(
        self,
        response: toolset.Toolset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[toolset.Toolset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_toolset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_get_toolset_with_metadata`
        interceptor in new development instead of the `post_get_toolset` interceptor.
        When both interceptors are used, this `post_get_toolset_with_metadata` interceptor runs after the
        `post_get_toolset` interceptor. The (possibly modified) response returned by
        `post_get_toolset` will be passed to
        `post_get_toolset_with_metadata`.
        """
        return response, metadata

    def pre_import_app(
        self,
        request: agent_service.ImportAppRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.ImportAppRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for import_app

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_import_app(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_app

        DEPRECATED. Please use the `post_import_app_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_import_app` interceptor runs
        before the `post_import_app_with_metadata` interceptor.
        """
        return response

    def post_import_app_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_app

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_import_app_with_metadata`
        interceptor in new development instead of the `post_import_app` interceptor.
        When both interceptors are used, this `post_import_app_with_metadata` interceptor runs after the
        `post_import_app` interceptor. The (possibly modified) response returned by
        `post_import_app` will be passed to
        `post_import_app_with_metadata`.
        """
        return response, metadata

    def pre_list_agents(
        self,
        request: agent_service.ListAgentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListAgentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_agents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_agents(
        self, response: agent_service.ListAgentsResponse
    ) -> agent_service.ListAgentsResponse:
        """Post-rpc interceptor for list_agents

        DEPRECATED. Please use the `post_list_agents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_agents` interceptor runs
        before the `post_list_agents_with_metadata` interceptor.
        """
        return response

    def post_list_agents_with_metadata(
        self,
        response: agent_service.ListAgentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListAgentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_agents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_agents_with_metadata`
        interceptor in new development instead of the `post_list_agents` interceptor.
        When both interceptors are used, this `post_list_agents_with_metadata` interceptor runs after the
        `post_list_agents` interceptor. The (possibly modified) response returned by
        `post_list_agents` will be passed to
        `post_list_agents_with_metadata`.
        """
        return response, metadata

    def pre_list_apps(
        self,
        request: agent_service.ListAppsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.ListAppsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_apps

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_apps(
        self, response: agent_service.ListAppsResponse
    ) -> agent_service.ListAppsResponse:
        """Post-rpc interceptor for list_apps

        DEPRECATED. Please use the `post_list_apps_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_apps` interceptor runs
        before the `post_list_apps_with_metadata` interceptor.
        """
        return response

    def post_list_apps_with_metadata(
        self,
        response: agent_service.ListAppsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.ListAppsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_apps

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_apps_with_metadata`
        interceptor in new development instead of the `post_list_apps` interceptor.
        When both interceptors are used, this `post_list_apps_with_metadata` interceptor runs after the
        `post_list_apps` interceptor. The (possibly modified) response returned by
        `post_list_apps` will be passed to
        `post_list_apps_with_metadata`.
        """
        return response, metadata

    def pre_list_app_versions(
        self,
        request: agent_service.ListAppVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListAppVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_app_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_app_versions(
        self, response: agent_service.ListAppVersionsResponse
    ) -> agent_service.ListAppVersionsResponse:
        """Post-rpc interceptor for list_app_versions

        DEPRECATED. Please use the `post_list_app_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_app_versions` interceptor runs
        before the `post_list_app_versions_with_metadata` interceptor.
        """
        return response

    def post_list_app_versions_with_metadata(
        self,
        response: agent_service.ListAppVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListAppVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_app_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_app_versions_with_metadata`
        interceptor in new development instead of the `post_list_app_versions` interceptor.
        When both interceptors are used, this `post_list_app_versions_with_metadata` interceptor runs after the
        `post_list_app_versions` interceptor. The (possibly modified) response returned by
        `post_list_app_versions` will be passed to
        `post_list_app_versions_with_metadata`.
        """
        return response, metadata

    def pre_list_changelogs(
        self,
        request: agent_service.ListChangelogsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListChangelogsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_changelogs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_changelogs(
        self, response: agent_service.ListChangelogsResponse
    ) -> agent_service.ListChangelogsResponse:
        """Post-rpc interceptor for list_changelogs

        DEPRECATED. Please use the `post_list_changelogs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_changelogs` interceptor runs
        before the `post_list_changelogs_with_metadata` interceptor.
        """
        return response

    def post_list_changelogs_with_metadata(
        self,
        response: agent_service.ListChangelogsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListChangelogsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_changelogs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_changelogs_with_metadata`
        interceptor in new development instead of the `post_list_changelogs` interceptor.
        When both interceptors are used, this `post_list_changelogs_with_metadata` interceptor runs after the
        `post_list_changelogs` interceptor. The (possibly modified) response returned by
        `post_list_changelogs` will be passed to
        `post_list_changelogs_with_metadata`.
        """
        return response, metadata

    def pre_list_conversations(
        self,
        request: agent_service.ListConversationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListConversationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_conversations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_conversations(
        self, response: agent_service.ListConversationsResponse
    ) -> agent_service.ListConversationsResponse:
        """Post-rpc interceptor for list_conversations

        DEPRECATED. Please use the `post_list_conversations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_conversations` interceptor runs
        before the `post_list_conversations_with_metadata` interceptor.
        """
        return response

    def post_list_conversations_with_metadata(
        self,
        response: agent_service.ListConversationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListConversationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_conversations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_conversations_with_metadata`
        interceptor in new development instead of the `post_list_conversations` interceptor.
        When both interceptors are used, this `post_list_conversations_with_metadata` interceptor runs after the
        `post_list_conversations` interceptor. The (possibly modified) response returned by
        `post_list_conversations` will be passed to
        `post_list_conversations_with_metadata`.
        """
        return response, metadata

    def pre_list_deployments(
        self,
        request: agent_service.ListDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListDeploymentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_deployments(
        self, response: agent_service.ListDeploymentsResponse
    ) -> agent_service.ListDeploymentsResponse:
        """Post-rpc interceptor for list_deployments

        DEPRECATED. Please use the `post_list_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_deployments` interceptor runs
        before the `post_list_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_deployments_with_metadata(
        self,
        response: agent_service.ListDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListDeploymentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_deployments_with_metadata`
        interceptor in new development instead of the `post_list_deployments` interceptor.
        When both interceptors are used, this `post_list_deployments_with_metadata` interceptor runs after the
        `post_list_deployments` interceptor. The (possibly modified) response returned by
        `post_list_deployments` will be passed to
        `post_list_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_examples(
        self,
        request: agent_service.ListExamplesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListExamplesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_examples

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_examples(
        self, response: agent_service.ListExamplesResponse
    ) -> agent_service.ListExamplesResponse:
        """Post-rpc interceptor for list_examples

        DEPRECATED. Please use the `post_list_examples_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_examples` interceptor runs
        before the `post_list_examples_with_metadata` interceptor.
        """
        return response

    def post_list_examples_with_metadata(
        self,
        response: agent_service.ListExamplesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListExamplesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_examples

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_examples_with_metadata`
        interceptor in new development instead of the `post_list_examples` interceptor.
        When both interceptors are used, this `post_list_examples_with_metadata` interceptor runs after the
        `post_list_examples` interceptor. The (possibly modified) response returned by
        `post_list_examples` will be passed to
        `post_list_examples_with_metadata`.
        """
        return response, metadata

    def pre_list_guardrails(
        self,
        request: agent_service.ListGuardrailsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListGuardrailsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_guardrails

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_guardrails(
        self, response: agent_service.ListGuardrailsResponse
    ) -> agent_service.ListGuardrailsResponse:
        """Post-rpc interceptor for list_guardrails

        DEPRECATED. Please use the `post_list_guardrails_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_guardrails` interceptor runs
        before the `post_list_guardrails_with_metadata` interceptor.
        """
        return response

    def post_list_guardrails_with_metadata(
        self,
        response: agent_service.ListGuardrailsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListGuardrailsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_guardrails

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_guardrails_with_metadata`
        interceptor in new development instead of the `post_list_guardrails` interceptor.
        When both interceptors are used, this `post_list_guardrails_with_metadata` interceptor runs after the
        `post_list_guardrails` interceptor. The (possibly modified) response returned by
        `post_list_guardrails` will be passed to
        `post_list_guardrails_with_metadata`.
        """
        return response, metadata

    def pre_list_tools(
        self,
        request: agent_service.ListToolsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.ListToolsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_tools

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_tools(
        self, response: agent_service.ListToolsResponse
    ) -> agent_service.ListToolsResponse:
        """Post-rpc interceptor for list_tools

        DEPRECATED. Please use the `post_list_tools_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_tools` interceptor runs
        before the `post_list_tools_with_metadata` interceptor.
        """
        return response

    def post_list_tools_with_metadata(
        self,
        response: agent_service.ListToolsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListToolsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_tools

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_tools_with_metadata`
        interceptor in new development instead of the `post_list_tools` interceptor.
        When both interceptors are used, this `post_list_tools_with_metadata` interceptor runs after the
        `post_list_tools` interceptor. The (possibly modified) response returned by
        `post_list_tools` will be passed to
        `post_list_tools_with_metadata`.
        """
        return response, metadata

    def pre_list_toolsets(
        self,
        request: agent_service.ListToolsetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListToolsetsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_toolsets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_toolsets(
        self, response: agent_service.ListToolsetsResponse
    ) -> agent_service.ListToolsetsResponse:
        """Post-rpc interceptor for list_toolsets

        DEPRECATED. Please use the `post_list_toolsets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_list_toolsets` interceptor runs
        before the `post_list_toolsets_with_metadata` interceptor.
        """
        return response

    def post_list_toolsets_with_metadata(
        self,
        response: agent_service.ListToolsetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.ListToolsetsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_toolsets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_list_toolsets_with_metadata`
        interceptor in new development instead of the `post_list_toolsets` interceptor.
        When both interceptors are used, this `post_list_toolsets_with_metadata` interceptor runs after the
        `post_list_toolsets` interceptor. The (possibly modified) response returned by
        `post_list_toolsets` will be passed to
        `post_list_toolsets_with_metadata`.
        """
        return response, metadata

    def pre_restore_app_version(
        self,
        request: agent_service.RestoreAppVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.RestoreAppVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for restore_app_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_restore_app_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restore_app_version

        DEPRECATED. Please use the `post_restore_app_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_restore_app_version` interceptor runs
        before the `post_restore_app_version_with_metadata` interceptor.
        """
        return response

    def post_restore_app_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_app_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_restore_app_version_with_metadata`
        interceptor in new development instead of the `post_restore_app_version` interceptor.
        When both interceptors are used, this `post_restore_app_version_with_metadata` interceptor runs after the
        `post_restore_app_version` interceptor. The (possibly modified) response returned by
        `post_restore_app_version` will be passed to
        `post_restore_app_version_with_metadata`.
        """
        return response, metadata

    def pre_update_agent(
        self,
        request: agent_service.UpdateAgentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.UpdateAgentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_update_agent(self, response: gcc_agent.Agent) -> gcc_agent.Agent:
        """Post-rpc interceptor for update_agent

        DEPRECATED. Please use the `post_update_agent_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_update_agent` interceptor runs
        before the `post_update_agent_with_metadata` interceptor.
        """
        return response

    def post_update_agent_with_metadata(
        self,
        response: gcc_agent.Agent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_agent.Agent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_agent

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_update_agent_with_metadata`
        interceptor in new development instead of the `post_update_agent` interceptor.
        When both interceptors are used, this `post_update_agent_with_metadata` interceptor runs after the
        `post_update_agent` interceptor. The (possibly modified) response returned by
        `post_update_agent` will be passed to
        `post_update_agent_with_metadata`.
        """
        return response, metadata

    def pre_update_app(
        self,
        request: agent_service.UpdateAppRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_service.UpdateAppRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_app

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_update_app(self, response: gcc_app.App) -> gcc_app.App:
        """Post-rpc interceptor for update_app

        DEPRECATED. Please use the `post_update_app_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_update_app` interceptor runs
        before the `post_update_app_with_metadata` interceptor.
        """
        return response

    def post_update_app_with_metadata(
        self, response: gcc_app.App, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcc_app.App, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_app

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_update_app_with_metadata`
        interceptor in new development instead of the `post_update_app` interceptor.
        When both interceptors are used, this `post_update_app_with_metadata` interceptor runs after the
        `post_update_app` interceptor. The (possibly modified) response returned by
        `post_update_app` will be passed to
        `post_update_app_with_metadata`.
        """
        return response, metadata

    def pre_update_deployment(
        self,
        request: agent_service.UpdateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.UpdateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_update_deployment(
        self, response: gcc_deployment.Deployment
    ) -> gcc_deployment.Deployment:
        """Post-rpc interceptor for update_deployment

        DEPRECATED. Please use the `post_update_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_update_deployment` interceptor runs
        before the `post_update_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_deployment_with_metadata(
        self,
        response: gcc_deployment.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_deployment.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_update_deployment_with_metadata`
        interceptor in new development instead of the `post_update_deployment` interceptor.
        When both interceptors are used, this `post_update_deployment_with_metadata` interceptor runs after the
        `post_update_deployment` interceptor. The (possibly modified) response returned by
        `post_update_deployment` will be passed to
        `post_update_deployment_with_metadata`.
        """
        return response, metadata

    def pre_update_example(
        self,
        request: agent_service.UpdateExampleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.UpdateExampleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_example

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_update_example(self, response: gcc_example.Example) -> gcc_example.Example:
        """Post-rpc interceptor for update_example

        DEPRECATED. Please use the `post_update_example_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_update_example` interceptor runs
        before the `post_update_example_with_metadata` interceptor.
        """
        return response

    def post_update_example_with_metadata(
        self,
        response: gcc_example.Example,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_example.Example, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_example

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_update_example_with_metadata`
        interceptor in new development instead of the `post_update_example` interceptor.
        When both interceptors are used, this `post_update_example_with_metadata` interceptor runs after the
        `post_update_example` interceptor. The (possibly modified) response returned by
        `post_update_example` will be passed to
        `post_update_example_with_metadata`.
        """
        return response, metadata

    def pre_update_guardrail(
        self,
        request: agent_service.UpdateGuardrailRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.UpdateGuardrailRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_guardrail

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_update_guardrail(
        self, response: gcc_guardrail.Guardrail
    ) -> gcc_guardrail.Guardrail:
        """Post-rpc interceptor for update_guardrail

        DEPRECATED. Please use the `post_update_guardrail_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_update_guardrail` interceptor runs
        before the `post_update_guardrail_with_metadata` interceptor.
        """
        return response

    def post_update_guardrail_with_metadata(
        self,
        response: gcc_guardrail.Guardrail,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_guardrail.Guardrail, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_guardrail

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_update_guardrail_with_metadata`
        interceptor in new development instead of the `post_update_guardrail` interceptor.
        When both interceptors are used, this `post_update_guardrail_with_metadata` interceptor runs after the
        `post_update_guardrail` interceptor. The (possibly modified) response returned by
        `post_update_guardrail` will be passed to
        `post_update_guardrail_with_metadata`.
        """
        return response, metadata

    def pre_update_security_settings(
        self,
        request: agent_service.UpdateSecuritySettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.UpdateSecuritySettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_security_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_update_security_settings(
        self, response: gcc_security_settings.SecuritySettings
    ) -> gcc_security_settings.SecuritySettings:
        """Post-rpc interceptor for update_security_settings

        DEPRECATED. Please use the `post_update_security_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_update_security_settings` interceptor runs
        before the `post_update_security_settings_with_metadata` interceptor.
        """
        return response

    def post_update_security_settings_with_metadata(
        self,
        response: gcc_security_settings.SecuritySettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_security_settings.SecuritySettings, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_security_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_update_security_settings_with_metadata`
        interceptor in new development instead of the `post_update_security_settings` interceptor.
        When both interceptors are used, this `post_update_security_settings_with_metadata` interceptor runs after the
        `post_update_security_settings` interceptor. The (possibly modified) response returned by
        `post_update_security_settings` will be passed to
        `post_update_security_settings_with_metadata`.
        """
        return response, metadata

    def pre_update_tool(
        self,
        request: agent_service.UpdateToolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.UpdateToolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_tool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_update_tool(self, response: gcc_tool.Tool) -> gcc_tool.Tool:
        """Post-rpc interceptor for update_tool

        DEPRECATED. Please use the `post_update_tool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_update_tool` interceptor runs
        before the `post_update_tool_with_metadata` interceptor.
        """
        return response

    def post_update_tool_with_metadata(
        self, response: gcc_tool.Tool, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcc_tool.Tool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_tool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_update_tool_with_metadata`
        interceptor in new development instead of the `post_update_tool` interceptor.
        When both interceptors are used, this `post_update_tool_with_metadata` interceptor runs after the
        `post_update_tool` interceptor. The (possibly modified) response returned by
        `post_update_tool` will be passed to
        `post_update_tool_with_metadata`.
        """
        return response, metadata

    def pre_update_toolset(
        self,
        request: agent_service.UpdateToolsetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_service.UpdateToolsetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_toolset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_update_toolset(self, response: gcc_toolset.Toolset) -> gcc_toolset.Toolset:
        """Post-rpc interceptor for update_toolset

        DEPRECATED. Please use the `post_update_toolset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code. This `post_update_toolset` interceptor runs
        before the `post_update_toolset_with_metadata` interceptor.
        """
        return response

    def post_update_toolset_with_metadata(
        self,
        response: gcc_toolset.Toolset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_toolset.Toolset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_toolset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AgentService server but before it is returned to user code.

        We recommend only using this `post_update_toolset_with_metadata`
        interceptor in new development instead of the `post_update_toolset` interceptor.
        When both interceptors are used, this `post_update_toolset_with_metadata` interceptor runs after the
        `post_update_toolset` interceptor. The (possibly modified) response returned by
        `post_update_toolset` will be passed to
        `post_update_toolset_with_metadata`.
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
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the AgentService server but before
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
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the AgentService server but before
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
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AgentService server but before
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
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the AgentService server but before
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
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AgentService server but before
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
        before they are sent to the AgentService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the AgentService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AgentServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AgentServiceRestInterceptor


class AgentServiceRestTransport(_BaseAgentServiceRestTransport):
    """REST backend synchronous transport for AgentService.

    The service that manages agent-related resources in Gemini
    Enterprise for Customer Engagement (CES).

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "ces.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AgentServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'ces.googleapis.com').
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
            interceptor (Optional[AgentServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AgentServiceRestInterceptor()
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
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1beta/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchDeleteConversations(
        _BaseAgentServiceRestTransport._BaseBatchDeleteConversations,
        AgentServiceRestStub,
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.BatchDeleteConversations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.BatchDeleteConversationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch delete
            conversations method over HTTP.

                Args:
                    request (~.agent_service.BatchDeleteConversationsRequest):
                        The request object. Request message for
                    [AgentService.BatchDeleteConversations][google.cloud.ces.v1beta.AgentService.BatchDeleteConversations].
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

            http_options = _BaseAgentServiceRestTransport._BaseBatchDeleteConversations._get_http_options()
            request, metadata = self._interceptor.pre_batch_delete_conversations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseBatchDeleteConversations,
                    "_BaseBatchDeleteConversations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.BatchDeleteConversations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "BatchDeleteConversations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AgentServiceRestTransport._BatchDeleteConversations._get_response(
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

            resp = self._interceptor.post_batch_delete_conversations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_delete_conversations_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.batch_delete_conversations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "BatchDeleteConversations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAgent(
        _BaseAgentServiceRestTransport._BaseCreateAgent, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CreateAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.CreateAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_agent.Agent:
            r"""Call the create agent method over HTTP.

            Args:
                request (~.agent_service.CreateAgentRequest):
                    The request object. Request message for
                [AgentService.CreateAgent][google.cloud.ces.v1beta.AgentService.CreateAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_agent.Agent:
                    An agent acts as the fundamental
                building block that provides
                instructions to the Large Language Model
                (LLM) for executing specific tasks.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseCreateAgent._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCreateAgent,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CreateAgent",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CreateAgent._get_response(
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
            resp = gcc_agent.Agent()
            pb_resp = gcc_agent.Agent.pb(resp)

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
                    response_payload = gcc_agent.Agent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.create_agent",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateApp(
        _BaseAgentServiceRestTransport._BaseCreateApp, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CreateApp")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.CreateAppRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create app method over HTTP.

            Args:
                request (~.agent_service.CreateAppRequest):
                    The request object. Request message for
                [AgentService.CreateApp][google.cloud.ces.v1beta.AgentService.CreateApp].
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
                _BaseAgentServiceRestTransport._BaseCreateApp._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_app(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCreateApp,
                    "_BaseCreateApp__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CreateApp",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateApp",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CreateApp._get_response(
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

            resp = self._interceptor.post_create_app(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_app_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.create_app",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateApp",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAppVersion(
        _BaseAgentServiceRestTransport._BaseCreateAppVersion, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CreateAppVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.CreateAppVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_app_version.AppVersion:
            r"""Call the create app version method over HTTP.

            Args:
                request (~.agent_service.CreateAppVersionRequest):
                    The request object. Request message for
                [AgentService.CreateAppVersion][google.cloud.ces.v1beta.AgentService.CreateAppVersion]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_app_version.AppVersion:
                    In Customer Engagement Suite (CES),
                an app version is a snapshot of the app
                at a specific point in time. It is
                immutable and cannot be modified once
                created.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseCreateAppVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_app_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCreateAppVersion,
                    "_BaseCreateAppVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CreateAppVersion",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateAppVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CreateAppVersion._get_response(
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
            resp = gcc_app_version.AppVersion()
            pb_resp = gcc_app_version.AppVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_app_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_app_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_app_version.AppVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.create_app_version",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateAppVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDeployment(
        _BaseAgentServiceRestTransport._BaseCreateDeployment, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CreateDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.CreateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_deployment.Deployment:
            r"""Call the create deployment method over HTTP.

            Args:
                request (~.agent_service.CreateDeploymentRequest):
                    The request object. Request message for
                [AgentService.CreateDeployment][google.cloud.ces.v1beta.AgentService.CreateDeployment].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_deployment.Deployment:
                    A deployment represents an immutable,
                queryable version of the app. It is used
                to deploy an app version with a specific
                channel profile.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseCreateDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCreateDeployment,
                    "_BaseCreateDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CreateDeployment",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CreateDeployment._get_response(
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
            resp = gcc_deployment.Deployment()
            pb_resp = gcc_deployment.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_deployment.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.create_deployment",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateExample(
        _BaseAgentServiceRestTransport._BaseCreateExample, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CreateExample")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.CreateExampleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_example.Example:
            r"""Call the create example method over HTTP.

            Args:
                request (~.agent_service.CreateExampleRequest):
                    The request object. Request message for
                [AgentService.CreateExample][google.cloud.ces.v1beta.AgentService.CreateExample].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_example.Example:
                    An example represents a sample
                conversation between the user and the
                agent(s).

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseCreateExample._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_example(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCreateExample,
                    "_BaseCreateExample__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CreateExample",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateExample",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CreateExample._get_response(
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
            resp = gcc_example.Example()
            pb_resp = gcc_example.Example.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_example(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_example_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_example.Example.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.create_example",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateExample",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGuardrail(
        _BaseAgentServiceRestTransport._BaseCreateGuardrail, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CreateGuardrail")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.CreateGuardrailRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_guardrail.Guardrail:
            r"""Call the create guardrail method over HTTP.

            Args:
                request (~.agent_service.CreateGuardrailRequest):
                    The request object. Request message for
                [AgentService.CreateGuardrail][google.cloud.ces.v1beta.AgentService.CreateGuardrail].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_guardrail.Guardrail:
                    Guardrail contains a list of checks
                and balances to keep the agents safe and
                secure.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseCreateGuardrail._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_guardrail(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCreateGuardrail,
                    "_BaseCreateGuardrail__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CreateGuardrail",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateGuardrail",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CreateGuardrail._get_response(
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
            resp = gcc_guardrail.Guardrail()
            pb_resp = gcc_guardrail.Guardrail.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_guardrail(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_guardrail_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_guardrail.Guardrail.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.create_guardrail",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateGuardrail",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTool(
        _BaseAgentServiceRestTransport._BaseCreateTool, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CreateTool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.CreateToolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_tool.Tool:
            r"""Call the create tool method over HTTP.

            Args:
                request (~.agent_service.CreateToolRequest):
                    The request object. Request message for
                [AgentService.CreateTool][google.cloud.ces.v1beta.AgentService.CreateTool].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_tool.Tool:
                    A tool represents an action that the
                CES agent can take to achieve certain
                goals.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseCreateTool._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_tool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCreateTool,
                    "_BaseCreateTool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CreateTool",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateTool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CreateTool._get_response(
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
            resp = gcc_tool.Tool()
            pb_resp = gcc_tool.Tool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_tool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_tool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_tool.Tool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.create_tool",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateTool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateToolset(
        _BaseAgentServiceRestTransport._BaseCreateToolset, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CreateToolset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.CreateToolsetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_toolset.Toolset:
            r"""Call the create toolset method over HTTP.

            Args:
                request (~.agent_service.CreateToolsetRequest):
                    The request object. Request message for
                [AgentService.CreateToolset][google.cloud.ces.v1beta.AgentService.CreateToolset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_toolset.Toolset:
                    A toolset represents a group of
                dynamically managed tools that can be
                used by the agent.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseCreateToolset._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_toolset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCreateToolset,
                    "_BaseCreateToolset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CreateToolset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateToolset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CreateToolset._get_response(
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
            resp = gcc_toolset.Toolset()
            pb_resp = gcc_toolset.Toolset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_toolset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_toolset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_toolset.Toolset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.create_toolset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CreateToolset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAgent(
        _BaseAgentServiceRestTransport._BaseDeleteAgent, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete agent method over HTTP.

            Args:
                request (~.agent_service.DeleteAgentRequest):
                    The request object. Request message for
                [AgentService.DeleteAgent][google.cloud.ces.v1beta.AgentService.DeleteAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseDeleteAgent._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteAgent,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteAgent",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteAgent._get_response(
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

    class _DeleteApp(
        _BaseAgentServiceRestTransport._BaseDeleteApp, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteApp")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteAppRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete app method over HTTP.

            Args:
                request (~.agent_service.DeleteAppRequest):
                    The request object. Request message for
                [AgentService.DeleteApp][google.cloud.ces.v1beta.AgentService.DeleteApp].
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
                _BaseAgentServiceRestTransport._BaseDeleteApp._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_app(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteApp,
                    "_BaseDeleteApp__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteApp",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteApp",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteApp._get_response(
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

            resp = self._interceptor.post_delete_app(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_app_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.delete_app",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteApp",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAppVersion(
        _BaseAgentServiceRestTransport._BaseDeleteAppVersion, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteAppVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteAppVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete app version method over HTTP.

            Args:
                request (~.agent_service.DeleteAppVersionRequest):
                    The request object. Request message for
                [AgentService.DeleteAppVersion][google.cloud.ces.v1beta.AgentService.DeleteAppVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseDeleteAppVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_app_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteAppVersion,
                    "_BaseDeleteAppVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteAppVersion",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteAppVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteAppVersion._get_response(
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

    class _DeleteConversation(
        _BaseAgentServiceRestTransport._BaseDeleteConversation, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteConversation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete conversation method over HTTP.

            Args:
                request (~.agent_service.DeleteConversationRequest):
                    The request object. Request message for
                [AgentService.DeleteConversation][google.cloud.ces.v1beta.AgentService.DeleteConversation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAgentServiceRestTransport._BaseDeleteConversation._get_http_options()
            request, metadata = self._interceptor.pre_delete_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteConversation,
                    "_BaseDeleteConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteConversation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteConversation._get_response(
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

    class _DeleteDeployment(
        _BaseAgentServiceRestTransport._BaseDeleteDeployment, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete deployment method over HTTP.

            Args:
                request (~.agent_service.DeleteDeploymentRequest):
                    The request object. Request message for
                [AgentService.DeleteDeployment][google.cloud.ces.v1beta.AgentService.DeleteDeployment].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseDeleteDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteDeployment,
                    "_BaseDeleteDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteDeployment",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteDeployment._get_response(
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

    class _DeleteExample(
        _BaseAgentServiceRestTransport._BaseDeleteExample, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteExample")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteExampleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete example method over HTTP.

            Args:
                request (~.agent_service.DeleteExampleRequest):
                    The request object. Request message for
                [AgentService.DeleteExample][google.cloud.ces.v1beta.AgentService.DeleteExample].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseDeleteExample._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_example(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteExample,
                    "_BaseDeleteExample__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteExample",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteExample",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteExample._get_response(
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

    class _DeleteGuardrail(
        _BaseAgentServiceRestTransport._BaseDeleteGuardrail, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteGuardrail")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteGuardrailRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete guardrail method over HTTP.

            Args:
                request (~.agent_service.DeleteGuardrailRequest):
                    The request object. Request message for
                [AgentService.DeleteGuardrail][google.cloud.ces.v1beta.AgentService.DeleteGuardrail].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseDeleteGuardrail._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_guardrail(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteGuardrail,
                    "_BaseDeleteGuardrail__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteGuardrail",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteGuardrail",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteGuardrail._get_response(
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

    class _DeleteTool(
        _BaseAgentServiceRestTransport._BaseDeleteTool, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteTool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteToolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete tool method over HTTP.

            Args:
                request (~.agent_service.DeleteToolRequest):
                    The request object. Request message for
                [AgentService.DeleteTool][google.cloud.ces.v1beta.AgentService.DeleteTool].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseDeleteTool._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_tool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteTool,
                    "_BaseDeleteTool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteTool",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteTool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteTool._get_response(
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

    class _DeleteToolset(
        _BaseAgentServiceRestTransport._BaseDeleteToolset, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteToolset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.DeleteToolsetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete toolset method over HTTP.

            Args:
                request (~.agent_service.DeleteToolsetRequest):
                    The request object. Request message for
                [AgentService.DeleteToolset][google.cloud.ces.v1beta.AgentService.DeleteToolset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseDeleteToolset._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_toolset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteToolset,
                    "_BaseDeleteToolset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteToolset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteToolset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteToolset._get_response(
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

    class _ExportApp(
        _BaseAgentServiceRestTransport._BaseExportApp, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ExportApp")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ExportAppRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export app method over HTTP.

            Args:
                request (~.agent_service.ExportAppRequest):
                    The request object. Request message for
                [AgentService.ExportApp][google.cloud.ces.v1beta.AgentService.ExportApp].
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
                _BaseAgentServiceRestTransport._BaseExportApp._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_app(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseExportApp,
                    "_BaseExportApp__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ExportApp",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ExportApp",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ExportApp._get_response(
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

            resp = self._interceptor.post_export_app(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_app_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.export_app",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ExportApp",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateAppResource(
        _BaseAgentServiceRestTransport._BaseGenerateAppResource, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GenerateAppResource")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GenerateAppResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the generate app resource method over HTTP.

            Args:
                request (~.agent_service.GenerateAppResourceRequest):
                    The request object. Request message for
                [AgentService.GenerateAppResource][google.cloud.ces.v1beta.AgentService.GenerateAppResource].
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

            http_options = _BaseAgentServiceRestTransport._BaseGenerateAppResource._get_http_options()
            request, metadata = self._interceptor.pre_generate_app_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGenerateAppResource,
                    "_BaseGenerateAppResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GenerateAppResource",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GenerateAppResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GenerateAppResource._get_response(
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

            resp = self._interceptor.post_generate_app_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_app_resource_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.generate_app_resource",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GenerateAppResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAgent(_BaseAgentServiceRestTransport._BaseGetAgent, AgentServiceRestStub):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent.Agent:
            r"""Call the get agent method over HTTP.

            Args:
                request (~.agent_service.GetAgentRequest):
                    The request object. Request message for
                [AgentService.GetAgent][google.cloud.ces.v1beta.AgentService.GetAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent.Agent:
                    An agent acts as the fundamental
                building block that provides
                instructions to the Large Language Model
                (LLM) for executing specific tasks.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetAgent._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetAgent,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetAgent",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetAgent._get_response(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_agent",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApp(_BaseAgentServiceRestTransport._BaseGetApp, AgentServiceRestStub):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetApp")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetAppRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> app.App:
            r"""Call the get app method over HTTP.

            Args:
                request (~.agent_service.GetAppRequest):
                    The request object. Request message for
                [AgentService.GetApp][google.cloud.ces.v1beta.AgentService.GetApp].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.app.App:
                    An app serves as a top-level
                container for a group of agents,
                including the root agent and its
                sub-agents, along with their associated
                configurations. These agents work
                together to achieve specific goals
                within the app's context.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetApp._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_app(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetApp,
                    "_BaseGetApp__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetApp",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetApp",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetApp._get_response(
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
            resp = app.App()
            pb_resp = app.App.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_app(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_app_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = app.App.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_app",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetApp",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAppVersion(
        _BaseAgentServiceRestTransport._BaseGetAppVersion, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetAppVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetAppVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> app_version.AppVersion:
            r"""Call the get app version method over HTTP.

            Args:
                request (~.agent_service.GetAppVersionRequest):
                    The request object. Request message for
                [AgentService.GetAppVersion][google.cloud.ces.v1beta.AgentService.GetAppVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.app_version.AppVersion:
                    In Customer Engagement Suite (CES),
                an app version is a snapshot of the app
                at a specific point in time. It is
                immutable and cannot be modified once
                created.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetAppVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_app_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetAppVersion,
                    "_BaseGetAppVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetAppVersion",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetAppVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetAppVersion._get_response(
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
            resp = app_version.AppVersion()
            pb_resp = app_version.AppVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_app_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_app_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = app_version.AppVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_app_version",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetAppVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetChangelog(
        _BaseAgentServiceRestTransport._BaseGetChangelog, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetChangelog")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetChangelogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> changelog.Changelog:
            r"""Call the get changelog method over HTTP.

            Args:
                request (~.agent_service.GetChangelogRequest):
                    The request object. Request message for
                [AgentService.GetChangelog][google.cloud.ces.v1beta.AgentService.GetChangelog].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.changelog.Changelog:
                    Changelogs represent a change made to
                the app or to an resource within the
                app.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetChangelog._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_changelog(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetChangelog,
                    "_BaseGetChangelog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetChangelog",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetChangelog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetChangelog._get_response(
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
            resp = changelog.Changelog()
            pb_resp = changelog.Changelog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_changelog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_changelog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = changelog.Changelog.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_changelog",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetChangelog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConversation(
        _BaseAgentServiceRestTransport._BaseGetConversation, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetConversation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.Conversation:
            r"""Call the get conversation method over HTTP.

            Args:
                request (~.agent_service.GetConversationRequest):
                    The request object. Request message for
                [AgentService.GetConversation][google.cloud.ces.v1beta.AgentService.GetConversation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation.Conversation:
                    A conversation represents an
                interaction between an end user and the
                CES app.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetConversation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetConversation,
                    "_BaseGetConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetConversation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetConversation._get_response(
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
            resp = conversation.Conversation()
            pb_resp = conversation.Conversation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_conversation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_conversation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation.Conversation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_conversation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetConversation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeployment(
        _BaseAgentServiceRestTransport._BaseGetDeployment, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployment.Deployment:
            r"""Call the get deployment method over HTTP.

            Args:
                request (~.agent_service.GetDeploymentRequest):
                    The request object. Request message for
                [AgentService.GetDeployment][google.cloud.ces.v1beta.AgentService.GetDeployment].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployment.Deployment:
                    A deployment represents an immutable,
                queryable version of the app. It is used
                to deploy an app version with a specific
                channel profile.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_deployment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetDeployment,
                    "_BaseGetDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetDeployment",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetDeployment._get_response(
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
            resp = deployment.Deployment()
            pb_resp = deployment.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployment.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_deployment",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetExample(
        _BaseAgentServiceRestTransport._BaseGetExample, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetExample")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetExampleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> example.Example:
            r"""Call the get example method over HTTP.

            Args:
                request (~.agent_service.GetExampleRequest):
                    The request object. Request message for
                [AgentService.GetExample][google.cloud.ces.v1beta.AgentService.GetExample].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.example.Example:
                    An example represents a sample
                conversation between the user and the
                agent(s).

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetExample._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_example(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetExample,
                    "_BaseGetExample__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetExample",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetExample",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetExample._get_response(
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
            resp = example.Example()
            pb_resp = example.Example.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_example(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_example_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = example.Example.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_example",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetExample",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGuardrail(
        _BaseAgentServiceRestTransport._BaseGetGuardrail, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetGuardrail")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetGuardrailRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> guardrail.Guardrail:
            r"""Call the get guardrail method over HTTP.

            Args:
                request (~.agent_service.GetGuardrailRequest):
                    The request object. Request message for
                [AgentService.GetGuardrail][google.cloud.ces.v1beta.AgentService.GetGuardrail].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.guardrail.Guardrail:
                    Guardrail contains a list of checks
                and balances to keep the agents safe and
                secure.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetGuardrail._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_guardrail(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetGuardrail,
                    "_BaseGetGuardrail__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetGuardrail",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetGuardrail",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetGuardrail._get_response(
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
            resp = guardrail.Guardrail()
            pb_resp = guardrail.Guardrail.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_guardrail(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_guardrail_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = guardrail.Guardrail.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_guardrail",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetGuardrail",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSecuritySettings(
        _BaseAgentServiceRestTransport._BaseGetSecuritySettings, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetSecuritySettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetSecuritySettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_settings.SecuritySettings:
            r"""Call the get security settings method over HTTP.

            Args:
                request (~.agent_service.GetSecuritySettingsRequest):
                    The request object. Request message for
                [AgentService.GetSecuritySettings][google.cloud.ces.v1beta.AgentService.GetSecuritySettings].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.security_settings.SecuritySettings:
                    Project/Location level security
                settings for CES.

            """

            http_options = _BaseAgentServiceRestTransport._BaseGetSecuritySettings._get_http_options()
            request, metadata = self._interceptor.pre_get_security_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetSecuritySettings,
                    "_BaseGetSecuritySettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetSecuritySettings",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetSecuritySettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetSecuritySettings._get_response(
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
            resp = security_settings.SecuritySettings()
            pb_resp = security_settings.SecuritySettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_security_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_security_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = security_settings.SecuritySettings.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_security_settings",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetSecuritySettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTool(_BaseAgentServiceRestTransport._BaseGetTool, AgentServiceRestStub):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetTool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetToolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tool.Tool:
            r"""Call the get tool method over HTTP.

            Args:
                request (~.agent_service.GetToolRequest):
                    The request object. Request message for
                [AgentService.GetTool][google.cloud.ces.v1beta.AgentService.GetTool].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tool.Tool:
                    A tool represents an action that the
                CES agent can take to achieve certain
                goals.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetTool._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetTool,
                    "_BaseGetTool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetTool",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetTool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetTool._get_response(
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
            resp = tool.Tool()
            pb_resp = tool.Tool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_tool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_tool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tool.Tool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_tool",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetTool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetToolset(
        _BaseAgentServiceRestTransport._BaseGetToolset, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetToolset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.GetToolsetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> toolset.Toolset:
            r"""Call the get toolset method over HTTP.

            Args:
                request (~.agent_service.GetToolsetRequest):
                    The request object. Request message for
                [AgentService.GetToolset][google.cloud.ces.v1beta.AgentService.GetToolset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.toolset.Toolset:
                    A toolset represents a group of
                dynamically managed tools that can be
                used by the agent.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseGetToolset._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_toolset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetToolset,
                    "_BaseGetToolset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetToolset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetToolset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetToolset._get_response(
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
            resp = toolset.Toolset()
            pb_resp = toolset.Toolset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_toolset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_toolset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = toolset.Toolset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.get_toolset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetToolset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportApp(
        _BaseAgentServiceRestTransport._BaseImportApp, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ImportApp")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ImportAppRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import app method over HTTP.

            Args:
                request (~.agent_service.ImportAppRequest):
                    The request object. Request message for
                [AgentService.ImportApp][google.cloud.ces.v1beta.AgentService.ImportApp].
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
                _BaseAgentServiceRestTransport._BaseImportApp._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_app(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseImportApp,
                    "_BaseImportApp__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ImportApp",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ImportApp",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ImportApp._get_response(
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

            resp = self._interceptor.post_import_app(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_app_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.import_app",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ImportApp",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAgents(
        _BaseAgentServiceRestTransport._BaseListAgents, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListAgents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListAgentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListAgentsResponse:
            r"""Call the list agents method over HTTP.

            Args:
                request (~.agent_service.ListAgentsRequest):
                    The request object. Request message for
                [AgentService.ListAgents][google.cloud.ces.v1beta.AgentService.ListAgents].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListAgentsResponse:
                    Response message for
                [AgentService.ListAgents][google.cloud.ces.v1beta.AgentService.ListAgents].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListAgents._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_agents(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListAgents,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListAgents",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListAgents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListAgents._get_response(
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
            resp = agent_service.ListAgentsResponse()
            pb_resp = agent_service.ListAgentsResponse.pb(resp)

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
                    response_payload = agent_service.ListAgentsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_agents",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListAgents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApps(_BaseAgentServiceRestTransport._BaseListApps, AgentServiceRestStub):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListApps")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListAppsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListAppsResponse:
            r"""Call the list apps method over HTTP.

            Args:
                request (~.agent_service.ListAppsRequest):
                    The request object. Request message for
                [AgentService.ListApps][google.cloud.ces.v1beta.AgentService.ListApps].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListAppsResponse:
                    Response message for
                [AgentService.ListApps][google.cloud.ces.v1beta.AgentService.ListApps].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListApps._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_apps(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListApps,
                    "_BaseListApps__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListApps",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListApps",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListApps._get_response(
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
            resp = agent_service.ListAppsResponse()
            pb_resp = agent_service.ListAppsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_apps(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_apps_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListAppsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_apps",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListApps",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAppVersions(
        _BaseAgentServiceRestTransport._BaseListAppVersions, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListAppVersions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListAppVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListAppVersionsResponse:
            r"""Call the list app versions method over HTTP.

            Args:
                request (~.agent_service.ListAppVersionsRequest):
                    The request object. Request message for
                [AgentService.ListAppVersions][google.cloud.ces.v1beta.AgentService.ListAppVersions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListAppVersionsResponse:
                    Response message for
                [AgentService.ListAppVersions][google.cloud.ces.v1beta.AgentService.ListAppVersions].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListAppVersions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_app_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListAppVersions,
                    "_BaseListAppVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListAppVersions",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListAppVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListAppVersions._get_response(
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
            resp = agent_service.ListAppVersionsResponse()
            pb_resp = agent_service.ListAppVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_app_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_app_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListAppVersionsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_app_versions",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListAppVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListChangelogs(
        _BaseAgentServiceRestTransport._BaseListChangelogs, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListChangelogs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListChangelogsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListChangelogsResponse:
            r"""Call the list changelogs method over HTTP.

            Args:
                request (~.agent_service.ListChangelogsRequest):
                    The request object. Request message for
                [AgentService.ListChangelogs][google.cloud.ces.v1beta.AgentService.ListChangelogs].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListChangelogsResponse:
                    Response message for
                [AgentService.ListChangelogs][google.cloud.ces.v1beta.AgentService.ListChangelogs].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListChangelogs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_changelogs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListChangelogs,
                    "_BaseListChangelogs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListChangelogs",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListChangelogs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListChangelogs._get_response(
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
            resp = agent_service.ListChangelogsResponse()
            pb_resp = agent_service.ListChangelogsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_changelogs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_changelogs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListChangelogsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_changelogs",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListChangelogs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConversations(
        _BaseAgentServiceRestTransport._BaseListConversations, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListConversations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListConversationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListConversationsResponse:
            r"""Call the list conversations method over HTTP.

            Args:
                request (~.agent_service.ListConversationsRequest):
                    The request object. Request message for
                [AgentService.ListConversations][google.cloud.ces.v1beta.AgentService.ListConversations].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListConversationsResponse:
                    Response message for
                [AgentService.ListConversations][google.cloud.ces.v1beta.AgentService.ListConversations].

            """

            http_options = _BaseAgentServiceRestTransport._BaseListConversations._get_http_options()
            request, metadata = self._interceptor.pre_list_conversations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListConversations,
                    "_BaseListConversations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListConversations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListConversations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListConversations._get_response(
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
            resp = agent_service.ListConversationsResponse()
            pb_resp = agent_service.ListConversationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_conversations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_conversations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListConversationsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_conversations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListConversations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeployments(
        _BaseAgentServiceRestTransport._BaseListDeployments, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListDeployments")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListDeploymentsResponse:
            r"""Call the list deployments method over HTTP.

            Args:
                request (~.agent_service.ListDeploymentsRequest):
                    The request object. Request message for
                [AgentService.ListDeployments][google.cloud.ces.v1beta.AgentService.ListDeployments].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListDeploymentsResponse:
                    Response message for
                [AgentService.ListDeployments][google.cloud.ces.v1beta.AgentService.ListDeployments].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListDeployments._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListDeployments,
                    "_BaseListDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListDeployments",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListDeployments._get_response(
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
            resp = agent_service.ListDeploymentsResponse()
            pb_resp = agent_service.ListDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListDeploymentsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_deployments",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListExamples(
        _BaseAgentServiceRestTransport._BaseListExamples, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListExamples")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListExamplesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListExamplesResponse:
            r"""Call the list examples method over HTTP.

            Args:
                request (~.agent_service.ListExamplesRequest):
                    The request object. Request message for
                [AgentService.ListExamples][google.cloud.ces.v1beta.AgentService.ListExamples].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListExamplesResponse:
                    Response message for
                [AgentService.ListExamples][google.cloud.ces.v1beta.AgentService.ListExamples].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListExamples._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_examples(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListExamples,
                    "_BaseListExamples__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListExamples",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListExamples",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListExamples._get_response(
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
            resp = agent_service.ListExamplesResponse()
            pb_resp = agent_service.ListExamplesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_examples(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_examples_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListExamplesResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_examples",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListExamples",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGuardrails(
        _BaseAgentServiceRestTransport._BaseListGuardrails, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListGuardrails")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListGuardrailsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListGuardrailsResponse:
            r"""Call the list guardrails method over HTTP.

            Args:
                request (~.agent_service.ListGuardrailsRequest):
                    The request object. Request message for
                [AgentService.ListGuardrails][google.cloud.ces.v1beta.AgentService.ListGuardrails].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListGuardrailsResponse:
                    Response message for
                [AgentService.ListGuardrails][google.cloud.ces.v1beta.AgentService.ListGuardrails].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListGuardrails._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_guardrails(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListGuardrails,
                    "_BaseListGuardrails__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListGuardrails",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListGuardrails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListGuardrails._get_response(
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
            resp = agent_service.ListGuardrailsResponse()
            pb_resp = agent_service.ListGuardrailsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_guardrails(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_guardrails_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListGuardrailsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_guardrails",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListGuardrails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTools(
        _BaseAgentServiceRestTransport._BaseListTools, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListTools")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListToolsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListToolsResponse:
            r"""Call the list tools method over HTTP.

            Args:
                request (~.agent_service.ListToolsRequest):
                    The request object. Request message for
                [AgentService.ListTools][google.cloud.ces.v1beta.AgentService.ListTools].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListToolsResponse:
                    Response message for
                [AgentService.ListTools][google.cloud.ces.v1beta.AgentService.ListTools].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListTools._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tools(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListTools,
                    "_BaseListTools__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListTools",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListTools",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListTools._get_response(
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
            resp = agent_service.ListToolsResponse()
            pb_resp = agent_service.ListToolsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tools(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tools_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListToolsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_tools",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListTools",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListToolsets(
        _BaseAgentServiceRestTransport._BaseListToolsets, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListToolsets")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.ListToolsetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_service.ListToolsetsResponse:
            r"""Call the list toolsets method over HTTP.

            Args:
                request (~.agent_service.ListToolsetsRequest):
                    The request object. Request message for
                [AgentService.ListToolsets][google.cloud.ces.v1beta.AgentService.ListToolsets].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_service.ListToolsetsResponse:
                    Response message for
                [AgentService.ListToolsets][google.cloud.ces.v1beta.AgentService.ListToolsets].

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseListToolsets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_toolsets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListToolsets,
                    "_BaseListToolsets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListToolsets",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListToolsets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListToolsets._get_response(
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
            resp = agent_service.ListToolsetsResponse()
            pb_resp = agent_service.ListToolsetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_toolsets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_toolsets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_service.ListToolsetsResponse.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.list_toolsets",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListToolsets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreAppVersion(
        _BaseAgentServiceRestTransport._BaseRestoreAppVersion, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.RestoreAppVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.RestoreAppVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restore app version method over HTTP.

            Args:
                request (~.agent_service.RestoreAppVersionRequest):
                    The request object. Request message for
                [AgentService.RestoreAppVersion][google.cloud.ces.v1beta.AgentService.RestoreAppVersion]
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

            http_options = _BaseAgentServiceRestTransport._BaseRestoreAppVersion._get_http_options()
            request, metadata = self._interceptor.pre_restore_app_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseRestoreAppVersion,
                    "_BaseRestoreAppVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.RestoreAppVersion",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "RestoreAppVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._RestoreAppVersion._get_response(
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

            resp = self._interceptor.post_restore_app_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_app_version_with_metadata(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.restore_app_version",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "RestoreAppVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAgent(
        _BaseAgentServiceRestTransport._BaseUpdateAgent, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.UpdateAgent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.UpdateAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_agent.Agent:
            r"""Call the update agent method over HTTP.

            Args:
                request (~.agent_service.UpdateAgentRequest):
                    The request object. Request message for
                [AgentService.UpdateAgent][google.cloud.ces.v1beta.AgentService.UpdateAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_agent.Agent:
                    An agent acts as the fundamental
                building block that provides
                instructions to the Large Language Model
                (LLM) for executing specific tasks.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseUpdateAgent._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_agent(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseUpdateAgent,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.UpdateAgent",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateAgent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._UpdateAgent._get_response(
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
            resp = gcc_agent.Agent()
            pb_resp = gcc_agent.Agent.pb(resp)

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
                    response_payload = gcc_agent.Agent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.update_agent",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateAgent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApp(
        _BaseAgentServiceRestTransport._BaseUpdateApp, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.UpdateApp")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.UpdateAppRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_app.App:
            r"""Call the update app method over HTTP.

            Args:
                request (~.agent_service.UpdateAppRequest):
                    The request object. Request message for
                [AgentService.UpdateApp][google.cloud.ces.v1beta.AgentService.UpdateApp].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_app.App:
                    An app serves as a top-level
                container for a group of agents,
                including the root agent and its
                sub-agents, along with their associated
                configurations. These agents work
                together to achieve specific goals
                within the app's context.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseUpdateApp._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_app(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseUpdateApp,
                    "_BaseUpdateApp__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.UpdateApp",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateApp",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._UpdateApp._get_response(
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
            resp = gcc_app.App()
            pb_resp = gcc_app.App.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_app(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_app_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_app.App.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.update_app",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateApp",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeployment(
        _BaseAgentServiceRestTransport._BaseUpdateDeployment, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.UpdateDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.UpdateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_deployment.Deployment:
            r"""Call the update deployment method over HTTP.

            Args:
                request (~.agent_service.UpdateDeploymentRequest):
                    The request object. Request message for
                [AgentService.UpdateDeployment][google.cloud.ces.v1beta.AgentService.UpdateDeployment].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_deployment.Deployment:
                    A deployment represents an immutable,
                queryable version of the app. It is used
                to deploy an app version with a specific
                channel profile.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseUpdateDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseUpdateDeployment,
                    "_BaseUpdateDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.UpdateDeployment",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._UpdateDeployment._get_response(
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
            resp = gcc_deployment.Deployment()
            pb_resp = gcc_deployment.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_deployment.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.update_deployment",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateExample(
        _BaseAgentServiceRestTransport._BaseUpdateExample, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.UpdateExample")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.UpdateExampleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_example.Example:
            r"""Call the update example method over HTTP.

            Args:
                request (~.agent_service.UpdateExampleRequest):
                    The request object. Request message for
                [AgentService.UpdateExample][google.cloud.ces.v1beta.AgentService.UpdateExample].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_example.Example:
                    An example represents a sample
                conversation between the user and the
                agent(s).

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseUpdateExample._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_example(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseUpdateExample,
                    "_BaseUpdateExample__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.UpdateExample",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateExample",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._UpdateExample._get_response(
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
            resp = gcc_example.Example()
            pb_resp = gcc_example.Example.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_example(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_example_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_example.Example.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.update_example",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateExample",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGuardrail(
        _BaseAgentServiceRestTransport._BaseUpdateGuardrail, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.UpdateGuardrail")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.UpdateGuardrailRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_guardrail.Guardrail:
            r"""Call the update guardrail method over HTTP.

            Args:
                request (~.agent_service.UpdateGuardrailRequest):
                    The request object. Request message for
                [AgentService.UpdateGuardrail][google.cloud.ces.v1beta.AgentService.UpdateGuardrail].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_guardrail.Guardrail:
                    Guardrail contains a list of checks
                and balances to keep the agents safe and
                secure.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseUpdateGuardrail._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_guardrail(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseUpdateGuardrail,
                    "_BaseUpdateGuardrail__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.UpdateGuardrail",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateGuardrail",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._UpdateGuardrail._get_response(
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
            resp = gcc_guardrail.Guardrail()
            pb_resp = gcc_guardrail.Guardrail.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_guardrail(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_guardrail_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_guardrail.Guardrail.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.update_guardrail",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateGuardrail",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSecuritySettings(
        _BaseAgentServiceRestTransport._BaseUpdateSecuritySettings, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.UpdateSecuritySettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.UpdateSecuritySettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_security_settings.SecuritySettings:
            r"""Call the update security settings method over HTTP.

            Args:
                request (~.agent_service.UpdateSecuritySettingsRequest):
                    The request object. Request message for
                [AgentService.UpdateSecuritySettings][google.cloud.ces.v1beta.AgentService.UpdateSecuritySettings].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_security_settings.SecuritySettings:
                    Project/Location level security
                settings for CES.

            """

            http_options = _BaseAgentServiceRestTransport._BaseUpdateSecuritySettings._get_http_options()
            request, metadata = self._interceptor.pre_update_security_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseUpdateSecuritySettings,
                    "_BaseUpdateSecuritySettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.UpdateSecuritySettings",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateSecuritySettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._UpdateSecuritySettings._get_response(
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
            resp = gcc_security_settings.SecuritySettings()
            pb_resp = gcc_security_settings.SecuritySettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_security_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_security_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_security_settings.SecuritySettings.to_json(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.update_security_settings",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateSecuritySettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTool(
        _BaseAgentServiceRestTransport._BaseUpdateTool, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.UpdateTool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.UpdateToolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_tool.Tool:
            r"""Call the update tool method over HTTP.

            Args:
                request (~.agent_service.UpdateToolRequest):
                    The request object. Request message for
                [AgentService.UpdateTool][google.cloud.ces.v1beta.AgentService.UpdateTool].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_tool.Tool:
                    A tool represents an action that the
                CES agent can take to achieve certain
                goals.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseUpdateTool._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_tool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseUpdateTool,
                    "_BaseUpdateTool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.UpdateTool",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateTool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._UpdateTool._get_response(
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
            resp = gcc_tool.Tool()
            pb_resp = gcc_tool.Tool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_tool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_tool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_tool.Tool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.update_tool",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateTool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateToolset(
        _BaseAgentServiceRestTransport._BaseUpdateToolset, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.UpdateToolset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: agent_service.UpdateToolsetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_toolset.Toolset:
            r"""Call the update toolset method over HTTP.

            Args:
                request (~.agent_service.UpdateToolsetRequest):
                    The request object. Request message for
                [AgentService.UpdateToolset][google.cloud.ces.v1beta.AgentService.UpdateToolset].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_toolset.Toolset:
                    A toolset represents a group of
                dynamically managed tools that can be
                used by the agent.

            """

            http_options = (
                _BaseAgentServiceRestTransport._BaseUpdateToolset._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_toolset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseUpdateToolset,
                    "_BaseUpdateToolset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.UpdateToolset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateToolset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._UpdateToolset._get_response(
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
            resp = gcc_toolset.Toolset()
            pb_resp = gcc_toolset.Toolset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_toolset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_toolset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_toolset.Toolset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ces_v1beta.AgentServiceClient.update_toolset",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "UpdateToolset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_delete_conversations(
        self,
    ) -> Callable[
        [agent_service.BatchDeleteConversationsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeleteConversations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_agent(
        self,
    ) -> Callable[[agent_service.CreateAgentRequest], gcc_agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_app(
        self,
    ) -> Callable[[agent_service.CreateAppRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApp(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_app_version(
        self,
    ) -> Callable[[agent_service.CreateAppVersionRequest], gcc_app_version.AppVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAppVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_deployment(
        self,
    ) -> Callable[[agent_service.CreateDeploymentRequest], gcc_deployment.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_example(
        self,
    ) -> Callable[[agent_service.CreateExampleRequest], gcc_example.Example]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateExample(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_guardrail(
        self,
    ) -> Callable[[agent_service.CreateGuardrailRequest], gcc_guardrail.Guardrail]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGuardrail(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tool(self) -> Callable[[agent_service.CreateToolRequest], gcc_tool.Tool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_toolset(
        self,
    ) -> Callable[[agent_service.CreateToolsetRequest], gcc_toolset.Toolset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateToolset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_agent(
        self,
    ) -> Callable[[agent_service.DeleteAgentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_app(
        self,
    ) -> Callable[[agent_service.DeleteAppRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApp(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_app_version(
        self,
    ) -> Callable[[agent_service.DeleteAppVersionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAppVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_conversation(
        self,
    ) -> Callable[[agent_service.DeleteConversationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_deployment(
        self,
    ) -> Callable[[agent_service.DeleteDeploymentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_example(
        self,
    ) -> Callable[[agent_service.DeleteExampleRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteExample(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_guardrail(
        self,
    ) -> Callable[[agent_service.DeleteGuardrailRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGuardrail(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tool(
        self,
    ) -> Callable[[agent_service.DeleteToolRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_toolset(
        self,
    ) -> Callable[[agent_service.DeleteToolsetRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteToolset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_app(
        self,
    ) -> Callable[[agent_service.ExportAppRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportApp(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_app_resource(
        self,
    ) -> Callable[[agent_service.GenerateAppResourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateAppResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_agent(self) -> Callable[[agent_service.GetAgentRequest], agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_app(self) -> Callable[[agent_service.GetAppRequest], app.App]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApp(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_app_version(
        self,
    ) -> Callable[[agent_service.GetAppVersionRequest], app_version.AppVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAppVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_changelog(
        self,
    ) -> Callable[[agent_service.GetChangelogRequest], changelog.Changelog]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetChangelog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_conversation(
        self,
    ) -> Callable[[agent_service.GetConversationRequest], conversation.Conversation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_deployment(
        self,
    ) -> Callable[[agent_service.GetDeploymentRequest], deployment.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_example(
        self,
    ) -> Callable[[agent_service.GetExampleRequest], example.Example]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetExample(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_guardrail(
        self,
    ) -> Callable[[agent_service.GetGuardrailRequest], guardrail.Guardrail]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGuardrail(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_security_settings(
        self,
    ) -> Callable[
        [agent_service.GetSecuritySettingsRequest], security_settings.SecuritySettings
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSecuritySettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tool(self) -> Callable[[agent_service.GetToolRequest], tool.Tool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_toolset(
        self,
    ) -> Callable[[agent_service.GetToolsetRequest], toolset.Toolset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetToolset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_app(
        self,
    ) -> Callable[[agent_service.ImportAppRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportApp(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_agents(
        self,
    ) -> Callable[[agent_service.ListAgentsRequest], agent_service.ListAgentsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAgents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_apps(
        self,
    ) -> Callable[[agent_service.ListAppsRequest], agent_service.ListAppsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApps(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_app_versions(
        self,
    ) -> Callable[
        [agent_service.ListAppVersionsRequest], agent_service.ListAppVersionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAppVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_changelogs(
        self,
    ) -> Callable[
        [agent_service.ListChangelogsRequest], agent_service.ListChangelogsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListChangelogs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_conversations(
        self,
    ) -> Callable[
        [agent_service.ListConversationsRequest],
        agent_service.ListConversationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConversations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [agent_service.ListDeploymentsRequest], agent_service.ListDeploymentsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeployments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_examples(
        self,
    ) -> Callable[
        [agent_service.ListExamplesRequest], agent_service.ListExamplesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExamples(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_guardrails(
        self,
    ) -> Callable[
        [agent_service.ListGuardrailsRequest], agent_service.ListGuardrailsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGuardrails(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tools(
        self,
    ) -> Callable[[agent_service.ListToolsRequest], agent_service.ListToolsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTools(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_toolsets(
        self,
    ) -> Callable[
        [agent_service.ListToolsetsRequest], agent_service.ListToolsetsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListToolsets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_app_version(
        self,
    ) -> Callable[[agent_service.RestoreAppVersionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreAppVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_agent(
        self,
    ) -> Callable[[agent_service.UpdateAgentRequest], gcc_agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_app(self) -> Callable[[agent_service.UpdateAppRequest], gcc_app.App]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApp(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_deployment(
        self,
    ) -> Callable[[agent_service.UpdateDeploymentRequest], gcc_deployment.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_example(
        self,
    ) -> Callable[[agent_service.UpdateExampleRequest], gcc_example.Example]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateExample(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_guardrail(
        self,
    ) -> Callable[[agent_service.UpdateGuardrailRequest], gcc_guardrail.Guardrail]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGuardrail(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_security_settings(
        self,
    ) -> Callable[
        [agent_service.UpdateSecuritySettingsRequest],
        gcc_security_settings.SecuritySettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSecuritySettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_tool(self) -> Callable[[agent_service.UpdateToolRequest], gcc_tool.Tool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_toolset(
        self,
    ) -> Callable[[agent_service.UpdateToolsetRequest], gcc_toolset.Toolset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateToolset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseAgentServiceRestTransport._BaseGetLocation, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentServiceRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
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
        _BaseAgentServiceRestTransport._BaseListLocations, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentServiceRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
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
        _BaseAgentServiceRestTransport._BaseCancelOperation, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._CancelOperation._get_response(
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
        _BaseAgentServiceRestTransport._BaseDeleteOperation, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentServiceRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._DeleteOperation._get_response(
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
        _BaseAgentServiceRestTransport._BaseGetOperation, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
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
        _BaseAgentServiceRestTransport._BaseListOperations, AgentServiceRestStub
    ):
        def __hash__(self):
            return hash("AgentServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseAgentServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAgentServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.ces_v1beta.AgentServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AgentServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.ces_v1beta.AgentServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.ces.v1beta.AgentService",
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


__all__ = ("AgentServiceRestTransport",)
