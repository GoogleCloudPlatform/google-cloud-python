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

from google.cloud.chronicle_v1._compat import transcode_request
from google.cloud.chronicle_v1.types import rule
from google.cloud.chronicle_v1.types import rule as gcc_rule

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseRuleServiceRestTransport

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


class RuleServiceRestInterceptor:
    """Interceptor for RuleService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the RuleServiceRestTransport.

    .. code-block:: python
        class MyCustomRuleServiceInterceptor(RuleServiceRestInterceptor):
            def pre_create_retrohunt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_retrohunt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_retrohunt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_retrohunt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_rule_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_rule_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_retrohunts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_retrohunts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rule_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rule_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rule_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rule_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_rule_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_rule_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_rule_text(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_rule_text(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = RuleServiceRestTransport(interceptor=MyCustomRuleServiceInterceptor())
        client = RuleServiceClient(transport=transport)


    """

    def pre_create_retrohunt(
        self,
        request: rule.CreateRetrohuntRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.CreateRetrohuntRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_retrohunt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_create_retrohunt(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_retrohunt

        DEPRECATED. Please use the `post_create_retrohunt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_create_retrohunt` interceptor runs
        before the `post_create_retrohunt_with_metadata` interceptor.
        """
        return response

    def post_create_retrohunt_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_retrohunt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_create_retrohunt_with_metadata`
        interceptor in new development instead of the `post_create_retrohunt` interceptor.
        When both interceptors are used, this `post_create_retrohunt_with_metadata` interceptor runs after the
        `post_create_retrohunt` interceptor. The (possibly modified) response returned by
        `post_create_retrohunt` will be passed to
        `post_create_retrohunt_with_metadata`.
        """
        return response, metadata

    def pre_create_rule(
        self,
        request: gcc_rule.CreateRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_rule.CreateRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_create_rule(self, response: gcc_rule.Rule) -> gcc_rule.Rule:
        """Post-rpc interceptor for create_rule

        DEPRECATED. Please use the `post_create_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_create_rule` interceptor runs
        before the `post_create_rule_with_metadata` interceptor.
        """
        return response

    def post_create_rule_with_metadata(
        self, response: gcc_rule.Rule, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcc_rule.Rule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_create_rule_with_metadata`
        interceptor in new development instead of the `post_create_rule` interceptor.
        When both interceptors are used, this `post_create_rule_with_metadata` interceptor runs after the
        `post_create_rule` interceptor. The (possibly modified) response returned by
        `post_create_rule` will be passed to
        `post_create_rule_with_metadata`.
        """
        return response, metadata

    def pre_delete_rule(
        self,
        request: rule.DeleteRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.DeleteRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def pre_get_retrohunt(
        self,
        request: rule.GetRetrohuntRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.GetRetrohuntRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_retrohunt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_get_retrohunt(self, response: rule.Retrohunt) -> rule.Retrohunt:
        """Post-rpc interceptor for get_retrohunt

        DEPRECATED. Please use the `post_get_retrohunt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_get_retrohunt` interceptor runs
        before the `post_get_retrohunt_with_metadata` interceptor.
        """
        return response

    def post_get_retrohunt_with_metadata(
        self,
        response: rule.Retrohunt,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.Retrohunt, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_retrohunt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_get_retrohunt_with_metadata`
        interceptor in new development instead of the `post_get_retrohunt` interceptor.
        When both interceptors are used, this `post_get_retrohunt_with_metadata` interceptor runs after the
        `post_get_retrohunt` interceptor. The (possibly modified) response returned by
        `post_get_retrohunt` will be passed to
        `post_get_retrohunt_with_metadata`.
        """
        return response, metadata

    def pre_get_rule(
        self,
        request: rule.GetRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.GetRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_get_rule(self, response: rule.Rule) -> rule.Rule:
        """Post-rpc interceptor for get_rule

        DEPRECATED. Please use the `post_get_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_get_rule` interceptor runs
        before the `post_get_rule_with_metadata` interceptor.
        """
        return response

    def post_get_rule_with_metadata(
        self, response: rule.Rule, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[rule.Rule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_get_rule_with_metadata`
        interceptor in new development instead of the `post_get_rule` interceptor.
        When both interceptors are used, this `post_get_rule_with_metadata` interceptor runs after the
        `post_get_rule` interceptor. The (possibly modified) response returned by
        `post_get_rule` will be passed to
        `post_get_rule_with_metadata`.
        """
        return response, metadata

    def pre_get_rule_deployment(
        self,
        request: rule.GetRuleDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.GetRuleDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_rule_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_get_rule_deployment(
        self, response: rule.RuleDeployment
    ) -> rule.RuleDeployment:
        """Post-rpc interceptor for get_rule_deployment

        DEPRECATED. Please use the `post_get_rule_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_get_rule_deployment` interceptor runs
        before the `post_get_rule_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_rule_deployment_with_metadata(
        self,
        response: rule.RuleDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.RuleDeployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_rule_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_get_rule_deployment_with_metadata`
        interceptor in new development instead of the `post_get_rule_deployment` interceptor.
        When both interceptors are used, this `post_get_rule_deployment_with_metadata` interceptor runs after the
        `post_get_rule_deployment` interceptor. The (possibly modified) response returned by
        `post_get_rule_deployment` will be passed to
        `post_get_rule_deployment_with_metadata`.
        """
        return response, metadata

    def pre_list_retrohunts(
        self,
        request: rule.ListRetrohuntsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.ListRetrohuntsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_retrohunts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_list_retrohunts(
        self, response: rule.ListRetrohuntsResponse
    ) -> rule.ListRetrohuntsResponse:
        """Post-rpc interceptor for list_retrohunts

        DEPRECATED. Please use the `post_list_retrohunts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_list_retrohunts` interceptor runs
        before the `post_list_retrohunts_with_metadata` interceptor.
        """
        return response

    def post_list_retrohunts_with_metadata(
        self,
        response: rule.ListRetrohuntsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.ListRetrohuntsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_retrohunts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_list_retrohunts_with_metadata`
        interceptor in new development instead of the `post_list_retrohunts` interceptor.
        When both interceptors are used, this `post_list_retrohunts_with_metadata` interceptor runs after the
        `post_list_retrohunts` interceptor. The (possibly modified) response returned by
        `post_list_retrohunts` will be passed to
        `post_list_retrohunts_with_metadata`.
        """
        return response, metadata

    def pre_list_rule_deployments(
        self,
        request: rule.ListRuleDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rule.ListRuleDeploymentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_rule_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_list_rule_deployments(
        self, response: rule.ListRuleDeploymentsResponse
    ) -> rule.ListRuleDeploymentsResponse:
        """Post-rpc interceptor for list_rule_deployments

        DEPRECATED. Please use the `post_list_rule_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_list_rule_deployments` interceptor runs
        before the `post_list_rule_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_rule_deployments_with_metadata(
        self,
        response: rule.ListRuleDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rule.ListRuleDeploymentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_rule_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_list_rule_deployments_with_metadata`
        interceptor in new development instead of the `post_list_rule_deployments` interceptor.
        When both interceptors are used, this `post_list_rule_deployments_with_metadata` interceptor runs after the
        `post_list_rule_deployments` interceptor. The (possibly modified) response returned by
        `post_list_rule_deployments` will be passed to
        `post_list_rule_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_rule_revisions(
        self,
        request: rule.ListRuleRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.ListRuleRevisionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_rule_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_list_rule_revisions(
        self, response: rule.ListRuleRevisionsResponse
    ) -> rule.ListRuleRevisionsResponse:
        """Post-rpc interceptor for list_rule_revisions

        DEPRECATED. Please use the `post_list_rule_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_list_rule_revisions` interceptor runs
        before the `post_list_rule_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_rule_revisions_with_metadata(
        self,
        response: rule.ListRuleRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.ListRuleRevisionsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_rule_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_list_rule_revisions_with_metadata`
        interceptor in new development instead of the `post_list_rule_revisions` interceptor.
        When both interceptors are used, this `post_list_rule_revisions_with_metadata` interceptor runs after the
        `post_list_rule_revisions` interceptor. The (possibly modified) response returned by
        `post_list_rule_revisions` will be passed to
        `post_list_rule_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_rules(
        self,
        request: rule.ListRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.ListRulesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_list_rules(
        self, response: rule.ListRulesResponse
    ) -> rule.ListRulesResponse:
        """Post-rpc interceptor for list_rules

        DEPRECATED. Please use the `post_list_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_list_rules` interceptor runs
        before the `post_list_rules_with_metadata` interceptor.
        """
        return response

    def post_list_rules_with_metadata(
        self,
        response: rule.ListRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.ListRulesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_list_rules_with_metadata`
        interceptor in new development instead of the `post_list_rules` interceptor.
        When both interceptors are used, this `post_list_rules_with_metadata` interceptor runs after the
        `post_list_rules` interceptor. The (possibly modified) response returned by
        `post_list_rules` will be passed to
        `post_list_rules_with_metadata`.
        """
        return response, metadata

    def pre_update_rule(
        self,
        request: gcc_rule.UpdateRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_rule.UpdateRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_update_rule(self, response: gcc_rule.Rule) -> gcc_rule.Rule:
        """Post-rpc interceptor for update_rule

        DEPRECATED. Please use the `post_update_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_update_rule` interceptor runs
        before the `post_update_rule_with_metadata` interceptor.
        """
        return response

    def post_update_rule_with_metadata(
        self, response: gcc_rule.Rule, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcc_rule.Rule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_update_rule_with_metadata`
        interceptor in new development instead of the `post_update_rule` interceptor.
        When both interceptors are used, this `post_update_rule_with_metadata` interceptor runs after the
        `post_update_rule` interceptor. The (possibly modified) response returned by
        `post_update_rule` will be passed to
        `post_update_rule_with_metadata`.
        """
        return response, metadata

    def pre_update_rule_deployment(
        self,
        request: rule.UpdateRuleDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rule.UpdateRuleDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_rule_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_update_rule_deployment(
        self, response: rule.RuleDeployment
    ) -> rule.RuleDeployment:
        """Post-rpc interceptor for update_rule_deployment

        DEPRECATED. Please use the `post_update_rule_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_update_rule_deployment` interceptor runs
        before the `post_update_rule_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_rule_deployment_with_metadata(
        self,
        response: rule.RuleDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.RuleDeployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_rule_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_update_rule_deployment_with_metadata`
        interceptor in new development instead of the `post_update_rule_deployment` interceptor.
        When both interceptors are used, this `post_update_rule_deployment_with_metadata` interceptor runs after the
        `post_update_rule_deployment` interceptor. The (possibly modified) response returned by
        `post_update_rule_deployment` will be passed to
        `post_update_rule_deployment_with_metadata`.
        """
        return response, metadata

    def pre_verify_rule_text(
        self,
        request: rule.VerifyRuleTextRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.VerifyRuleTextRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for verify_rule_text

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_verify_rule_text(
        self, response: rule.VerifyRuleTextResponse
    ) -> rule.VerifyRuleTextResponse:
        """Post-rpc interceptor for verify_rule_text

        DEPRECATED. Please use the `post_verify_rule_text_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code. This `post_verify_rule_text` interceptor runs
        before the `post_verify_rule_text_with_metadata` interceptor.
        """
        return response

    def post_verify_rule_text_with_metadata(
        self,
        response: rule.VerifyRuleTextResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rule.VerifyRuleTextResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for verify_rule_text

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuleService server but before it is returned to user code.

        We recommend only using this `post_verify_rule_text_with_metadata`
        interceptor in new development instead of the `post_verify_rule_text` interceptor.
        When both interceptors are used, this `post_verify_rule_text_with_metadata` interceptor runs after the
        `post_verify_rule_text` interceptor. The (possibly modified) response returned by
        `post_verify_rule_text` will be passed to
        `post_verify_rule_text_with_metadata`.
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
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the RuleService server but before
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
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the RuleService server but before
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
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the RuleService server but before
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
        before they are sent to the RuleService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the RuleService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class RuleServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: RuleServiceRestInterceptor


class RuleServiceRestTransport(_BaseRuleServiceRestTransport):
    """REST backend synchronous transport for RuleService.

    RuleService provides interface for user-created rules.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "chronicle.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[RuleServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'chronicle.googleapis.com').
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
            interceptor (Optional[RuleServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or RuleServiceRestInterceptor()
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
                        "uri": "/v1/{name=projects/*/locations/*/instances/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/instances/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/instances/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/instances/*}/operations",
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

    class _CreateRetrohunt(
        _BaseRuleServiceRestTransport._BaseCreateRetrohunt, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.CreateRetrohunt")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.CreateRetrohuntRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create retrohunt method over HTTP.

            Args:
                request (~.rule.CreateRetrohuntRequest):
                    The request object. Request message for CreateRetrohunt
                method.
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
                _BaseRuleServiceRestTransport._BaseCreateRetrohunt._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_retrohunt(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseCreateRetrohunt,
                    "_BaseCreateRetrohunt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.CreateRetrohunt",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "CreateRetrohunt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._CreateRetrohunt._get_response(
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

            resp = self._interceptor.post_create_retrohunt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_retrohunt_with_metadata(
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
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.create_retrohunt",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "CreateRetrohunt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRule(
        _BaseRuleServiceRestTransport._BaseCreateRule, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.CreateRule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcc_rule.CreateRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_rule.Rule:
            r"""Call the create rule method over HTTP.

            Args:
                request (~.gcc_rule.CreateRuleRequest):
                    The request object. Request message for CreateRule
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_rule.Rule:
                    The Rule resource represents a
                user-created rule. NEXT TAG: 21

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseCreateRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseCreateRule,
                    "_BaseCreateRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.CreateRule",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "CreateRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._CreateRule._get_response(
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
            resp = gcc_rule.Rule()
            pb_resp = gcc_rule.Rule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_rule.Rule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.create_rule",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "CreateRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRule(
        _BaseRuleServiceRestTransport._BaseDeleteRule, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.DeleteRule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.DeleteRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete rule method over HTTP.

            Args:
                request (~.rule.DeleteRuleRequest):
                    The request object. Request message for the DeleteRule
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseDeleteRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseDeleteRule,
                    "_BaseDeleteRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.DeleteRule",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "DeleteRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._DeleteRule._get_response(
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

    class _GetRetrohunt(
        _BaseRuleServiceRestTransport._BaseGetRetrohunt, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.GetRetrohunt")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.GetRetrohuntRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.Retrohunt:
            r"""Call the get retrohunt method over HTTP.

            Args:
                request (~.rule.GetRetrohuntRequest):
                    The request object. Request message for GetRetrohunt
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.Retrohunt:
                    Retrohunt is an execution of a Rule
                over a time range in the past.

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseGetRetrohunt._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_retrohunt(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseGetRetrohunt,
                    "_BaseGetRetrohunt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.GetRetrohunt",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "GetRetrohunt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._GetRetrohunt._get_response(
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
            resp = rule.Retrohunt()
            pb_resp = rule.Retrohunt.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_retrohunt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_retrohunt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.Retrohunt.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.get_retrohunt",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "GetRetrohunt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRule(_BaseRuleServiceRestTransport._BaseGetRule, RuleServiceRestStub):
        def __hash__(self):
            return hash("RuleServiceRestTransport.GetRule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.GetRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.Rule:
            r"""Call the get rule method over HTTP.

            Args:
                request (~.rule.GetRuleRequest):
                    The request object. Request message for GetRule method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.Rule:
                    The Rule resource represents a
                user-created rule. NEXT TAG: 21

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseGetRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseGetRule,
                    "_BaseGetRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.GetRule",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "GetRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._GetRule._get_response(
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
            resp = rule.Rule()
            pb_resp = rule.Rule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.Rule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.get_rule",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "GetRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRuleDeployment(
        _BaseRuleServiceRestTransport._BaseGetRuleDeployment, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.GetRuleDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.GetRuleDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.RuleDeployment:
            r"""Call the get rule deployment method over HTTP.

            Args:
                request (~.rule.GetRuleDeploymentRequest):
                    The request object. Request message for
                GetRuleDeployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.RuleDeployment:
                    The RuleDeployment resource
                represents the deployment state of a
                Rule.

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseGetRuleDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_rule_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseGetRuleDeployment,
                    "_BaseGetRuleDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.GetRuleDeployment",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "GetRuleDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._GetRuleDeployment._get_response(
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
            resp = rule.RuleDeployment()
            pb_resp = rule.RuleDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_rule_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_rule_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.RuleDeployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.get_rule_deployment",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "GetRuleDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRetrohunts(
        _BaseRuleServiceRestTransport._BaseListRetrohunts, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.ListRetrohunts")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.ListRetrohuntsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.ListRetrohuntsResponse:
            r"""Call the list retrohunts method over HTTP.

            Args:
                request (~.rule.ListRetrohuntsRequest):
                    The request object. Request message for ListRetrohunts
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.ListRetrohuntsResponse:
                    Response message for ListRetrohunts
                method.

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseListRetrohunts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_retrohunts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseListRetrohunts,
                    "_BaseListRetrohunts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.ListRetrohunts",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListRetrohunts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._ListRetrohunts._get_response(
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
            resp = rule.ListRetrohuntsResponse()
            pb_resp = rule.ListRetrohuntsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_retrohunts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_retrohunts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.ListRetrohuntsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.list_retrohunts",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListRetrohunts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRuleDeployments(
        _BaseRuleServiceRestTransport._BaseListRuleDeployments, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.ListRuleDeployments")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.ListRuleDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.ListRuleDeploymentsResponse:
            r"""Call the list rule deployments method over HTTP.

            Args:
                request (~.rule.ListRuleDeploymentsRequest):
                    The request object. Request message for
                ListRuleDeployments.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.ListRuleDeploymentsResponse:
                    Response message for
                ListRuleDeployments.

            """

            http_options = _BaseRuleServiceRestTransport._BaseListRuleDeployments._get_http_options()
            request, metadata = self._interceptor.pre_list_rule_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseListRuleDeployments,
                    "_BaseListRuleDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.ListRuleDeployments",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListRuleDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._ListRuleDeployments._get_response(
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
            resp = rule.ListRuleDeploymentsResponse()
            pb_resp = rule.ListRuleDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_rule_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rule_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.ListRuleDeploymentsResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.list_rule_deployments",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListRuleDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRuleRevisions(
        _BaseRuleServiceRestTransport._BaseListRuleRevisions, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.ListRuleRevisions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.ListRuleRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.ListRuleRevisionsResponse:
            r"""Call the list rule revisions method over HTTP.

            Args:
                request (~.rule.ListRuleRevisionsRequest):
                    The request object. Request message for ListRuleRevisions
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.ListRuleRevisionsResponse:
                    Response message for
                ListRuleRevisions method.

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseListRuleRevisions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_rule_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseListRuleRevisions,
                    "_BaseListRuleRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.ListRuleRevisions",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListRuleRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._ListRuleRevisions._get_response(
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
            resp = rule.ListRuleRevisionsResponse()
            pb_resp = rule.ListRuleRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_rule_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rule_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.ListRuleRevisionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.list_rule_revisions",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListRuleRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRules(_BaseRuleServiceRestTransport._BaseListRules, RuleServiceRestStub):
        def __hash__(self):
            return hash("RuleServiceRestTransport.ListRules")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.ListRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.ListRulesResponse:
            r"""Call the list rules method over HTTP.

            Args:
                request (~.rule.ListRulesRequest):
                    The request object. Request message for ListRules method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.ListRulesResponse:
                    Response message for ListRules
                method.

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseListRules._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_rules(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseListRules,
                    "_BaseListRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.ListRules",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._ListRules._get_response(
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
            resp = rule.ListRulesResponse()
            pb_resp = rule.ListRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.ListRulesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.list_rules",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRule(
        _BaseRuleServiceRestTransport._BaseUpdateRule, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.UpdateRule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcc_rule.UpdateRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_rule.Rule:
            r"""Call the update rule method over HTTP.

            Args:
                request (~.gcc_rule.UpdateRuleRequest):
                    The request object. Request message for UpdateRule
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_rule.Rule:
                    The Rule resource represents a
                user-created rule. NEXT TAG: 21

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseUpdateRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseUpdateRule,
                    "_BaseUpdateRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.UpdateRule",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "UpdateRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._UpdateRule._get_response(
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
            resp = gcc_rule.Rule()
            pb_resp = gcc_rule.Rule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_rule.Rule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.update_rule",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "UpdateRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRuleDeployment(
        _BaseRuleServiceRestTransport._BaseUpdateRuleDeployment, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.UpdateRuleDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.UpdateRuleDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.RuleDeployment:
            r"""Call the update rule deployment method over HTTP.

            Args:
                request (~.rule.UpdateRuleDeploymentRequest):
                    The request object. Request message for
                UpdateRuleDeployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.RuleDeployment:
                    The RuleDeployment resource
                represents the deployment state of a
                Rule.

            """

            http_options = _BaseRuleServiceRestTransport._BaseUpdateRuleDeployment._get_http_options()
            request, metadata = self._interceptor.pre_update_rule_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseUpdateRuleDeployment,
                    "_BaseUpdateRuleDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.UpdateRuleDeployment",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "UpdateRuleDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._UpdateRuleDeployment._get_response(
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
            resp = rule.RuleDeployment()
            pb_resp = rule.RuleDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_rule_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_rule_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.RuleDeployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.update_rule_deployment",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "UpdateRuleDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _VerifyRuleText(
        _BaseRuleServiceRestTransport._BaseVerifyRuleText, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.VerifyRuleText")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: rule.VerifyRuleTextRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rule.VerifyRuleTextResponse:
            r"""Call the verify rule text method over HTTP.

            Args:
                request (~.rule.VerifyRuleTextRequest):
                    The request object. Request message for VerifyRuleText
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rule.VerifyRuleTextResponse:
                    Response message for VerifyRuleText
                method.

            """

            http_options = (
                _BaseRuleServiceRestTransport._BaseVerifyRuleText._get_http_options()
            )
            request, metadata = self._interceptor.pre_verify_rule_text(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseVerifyRuleText,
                    "_BaseVerifyRuleText__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.VerifyRuleText",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "VerifyRuleText",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._VerifyRuleText._get_response(
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
            resp = rule.VerifyRuleTextResponse()
            pb_resp = rule.VerifyRuleTextResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_verify_rule_text(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_verify_rule_text_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rule.VerifyRuleTextResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.RuleServiceClient.verify_rule_text",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "VerifyRuleText",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_retrohunt(
        self,
    ) -> Callable[[rule.CreateRetrohuntRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRetrohunt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_rule(self) -> Callable[[gcc_rule.CreateRuleRequest], gcc_rule.Rule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_rule(self) -> Callable[[rule.DeleteRuleRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_retrohunt(self) -> Callable[[rule.GetRetrohuntRequest], rule.Retrohunt]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRetrohunt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_rule(self) -> Callable[[rule.GetRuleRequest], rule.Rule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_rule_deployment(
        self,
    ) -> Callable[[rule.GetRuleDeploymentRequest], rule.RuleDeployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRuleDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_retrohunts(
        self,
    ) -> Callable[[rule.ListRetrohuntsRequest], rule.ListRetrohuntsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRetrohunts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rule_deployments(
        self,
    ) -> Callable[[rule.ListRuleDeploymentsRequest], rule.ListRuleDeploymentsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRuleDeployments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rule_revisions(
        self,
    ) -> Callable[[rule.ListRuleRevisionsRequest], rule.ListRuleRevisionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRuleRevisions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rules(self) -> Callable[[rule.ListRulesRequest], rule.ListRulesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_rule(self) -> Callable[[gcc_rule.UpdateRuleRequest], gcc_rule.Rule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_rule_deployment(
        self,
    ) -> Callable[[rule.UpdateRuleDeploymentRequest], rule.RuleDeployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRuleDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def verify_rule_text(
        self,
    ) -> Callable[[rule.VerifyRuleTextRequest], rule.VerifyRuleTextResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyRuleText(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseRuleServiceRestTransport._BaseCancelOperation, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseRuleServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._CancelOperation._get_response(
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
        _BaseRuleServiceRestTransport._BaseDeleteOperation, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseRuleServiceRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._DeleteOperation._get_response(
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
        _BaseRuleServiceRestTransport._BaseGetOperation, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseRuleServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.chronicle_v1.RuleServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
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
        _BaseRuleServiceRestTransport._BaseListOperations, RuleServiceRestStub
    ):
        def __hash__(self):
            return hash("RuleServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseRuleServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuleServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.chronicle_v1.RuleServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuleServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.chronicle_v1.RuleServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.RuleService",
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


__all__ = ("RuleServiceRestTransport",)
