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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.compute_v1._compat import transcode_request
from google.cloud.compute_v1.types import compute

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOrganizationSecurityPoliciesRestTransport

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


class OrganizationSecurityPoliciesRestInterceptor:
    """Interceptor for OrganizationSecurityPolicies.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OrganizationSecurityPoliciesRestTransport.

    .. code-block:: python
        class MyCustomOrganizationSecurityPoliciesInterceptor(OrganizationSecurityPoliciesRestInterceptor):
            def pre_add_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_copy_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_copy_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_associations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_associations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_preconfigured_expression_sets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_preconfigured_expression_sets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_move(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_move(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_patch(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_patch(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_patch_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_patch_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OrganizationSecurityPoliciesRestTransport(interceptor=MyCustomOrganizationSecurityPoliciesInterceptor())
        client = OrganizationSecurityPoliciesClient(transport=transport)


    """

    def pre_add_association(
        self,
        request: compute.AddAssociationOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.AddAssociationOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_add_association(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for add_association

        DEPRECATED. Please use the `post_add_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_add_association` interceptor runs
        before the `post_add_association_with_metadata` interceptor.
        """
        return response

    def post_add_association_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_add_association_with_metadata`
        interceptor in new development instead of the `post_add_association` interceptor.
        When both interceptors are used, this `post_add_association_with_metadata` interceptor runs after the
        `post_add_association` interceptor. The (possibly modified) response returned by
        `post_add_association` will be passed to
        `post_add_association_with_metadata`.
        """
        return response, metadata

    def pre_add_rule(
        self,
        request: compute.AddRuleOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.AddRuleOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_add_rule(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for add_rule

        DEPRECATED. Please use the `post_add_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_add_rule` interceptor runs
        before the `post_add_rule_with_metadata` interceptor.
        """
        return response

    def post_add_rule_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_add_rule_with_metadata`
        interceptor in new development instead of the `post_add_rule` interceptor.
        When both interceptors are used, this `post_add_rule_with_metadata` interceptor runs after the
        `post_add_rule` interceptor. The (possibly modified) response returned by
        `post_add_rule` will be passed to
        `post_add_rule_with_metadata`.
        """
        return response, metadata

    def pre_copy_rules(
        self,
        request: compute.CopyRulesOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.CopyRulesOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for copy_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_copy_rules(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for copy_rules

        DEPRECATED. Please use the `post_copy_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_copy_rules` interceptor runs
        before the `post_copy_rules_with_metadata` interceptor.
        """
        return response

    def post_copy_rules_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for copy_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_copy_rules_with_metadata`
        interceptor in new development instead of the `post_copy_rules` interceptor.
        When both interceptors are used, this `post_copy_rules_with_metadata` interceptor runs after the
        `post_copy_rules` interceptor. The (possibly modified) response returned by
        `post_copy_rules` will be passed to
        `post_copy_rules_with_metadata`.
        """
        return response, metadata

    def pre_delete(
        self,
        request: compute.DeleteOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DeleteOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_delete(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for delete

        DEPRECATED. Please use the `post_delete_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_delete` interceptor runs
        before the `post_delete_with_metadata` interceptor.
        """
        return response

    def post_delete_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_delete_with_metadata`
        interceptor in new development instead of the `post_delete` interceptor.
        When both interceptors are used, this `post_delete_with_metadata` interceptor runs after the
        `post_delete` interceptor. The (possibly modified) response returned by
        `post_delete` will be passed to
        `post_delete_with_metadata`.
        """
        return response, metadata

    def pre_get(
        self,
        request: compute.GetOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_get(self, response: compute.SecurityPolicy) -> compute.SecurityPolicy:
        """Post-rpc interceptor for get

        DEPRECATED. Please use the `post_get_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_get` interceptor runs
        before the `post_get_with_metadata` interceptor.
        """
        return response

    def post_get_with_metadata(
        self,
        response: compute.SecurityPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.SecurityPolicy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_get_with_metadata`
        interceptor in new development instead of the `post_get` interceptor.
        When both interceptors are used, this `post_get_with_metadata` interceptor runs after the
        `post_get` interceptor. The (possibly modified) response returned by
        `post_get` will be passed to
        `post_get_with_metadata`.
        """
        return response, metadata

    def pre_get_association(
        self,
        request: compute.GetAssociationOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetAssociationOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_get_association(
        self, response: compute.SecurityPolicyAssociation
    ) -> compute.SecurityPolicyAssociation:
        """Post-rpc interceptor for get_association

        DEPRECATED. Please use the `post_get_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_get_association` interceptor runs
        before the `post_get_association_with_metadata` interceptor.
        """
        return response

    def post_get_association_with_metadata(
        self,
        response: compute.SecurityPolicyAssociation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SecurityPolicyAssociation, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_get_association_with_metadata`
        interceptor in new development instead of the `post_get_association` interceptor.
        When both interceptors are used, this `post_get_association_with_metadata` interceptor runs after the
        `post_get_association` interceptor. The (possibly modified) response returned by
        `post_get_association` will be passed to
        `post_get_association_with_metadata`.
        """
        return response, metadata

    def pre_get_rule(
        self,
        request: compute.GetRuleOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetRuleOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_get_rule(
        self, response: compute.SecurityPolicyRule
    ) -> compute.SecurityPolicyRule:
        """Post-rpc interceptor for get_rule

        DEPRECATED. Please use the `post_get_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_get_rule` interceptor runs
        before the `post_get_rule_with_metadata` interceptor.
        """
        return response

    def post_get_rule_with_metadata(
        self,
        response: compute.SecurityPolicyRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.SecurityPolicyRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_get_rule_with_metadata`
        interceptor in new development instead of the `post_get_rule` interceptor.
        When both interceptors are used, this `post_get_rule_with_metadata` interceptor runs after the
        `post_get_rule` interceptor. The (possibly modified) response returned by
        `post_get_rule` will be passed to
        `post_get_rule_with_metadata`.
        """
        return response, metadata

    def pre_insert(
        self,
        request: compute.InsertOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.InsertOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for insert

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_insert(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for insert

        DEPRECATED. Please use the `post_insert_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_insert` interceptor runs
        before the `post_insert_with_metadata` interceptor.
        """
        return response

    def post_insert_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for insert

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_insert_with_metadata`
        interceptor in new development instead of the `post_insert` interceptor.
        When both interceptors are used, this `post_insert_with_metadata` interceptor runs after the
        `post_insert` interceptor. The (possibly modified) response returned by
        `post_insert` will be passed to
        `post_insert_with_metadata`.
        """
        return response, metadata

    def pre_list(
        self,
        request: compute.ListOrganizationSecurityPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListOrganizationSecurityPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_list(
        self, response: compute.SecurityPolicyList
    ) -> compute.SecurityPolicyList:
        """Post-rpc interceptor for list

        DEPRECATED. Please use the `post_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_list` interceptor runs
        before the `post_list_with_metadata` interceptor.
        """
        return response

    def post_list_with_metadata(
        self,
        response: compute.SecurityPolicyList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.SecurityPolicyList, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_list_with_metadata`
        interceptor in new development instead of the `post_list` interceptor.
        When both interceptors are used, this `post_list_with_metadata` interceptor runs after the
        `post_list` interceptor. The (possibly modified) response returned by
        `post_list` will be passed to
        `post_list_with_metadata`.
        """
        return response, metadata

    def pre_list_associations(
        self,
        request: compute.ListAssociationsOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListAssociationsOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_associations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_list_associations(
        self, response: compute.OrganizationSecurityPoliciesListAssociationsResponse
    ) -> compute.OrganizationSecurityPoliciesListAssociationsResponse:
        """Post-rpc interceptor for list_associations

        DEPRECATED. Please use the `post_list_associations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_list_associations` interceptor runs
        before the `post_list_associations_with_metadata` interceptor.
        """
        return response

    def post_list_associations_with_metadata(
        self,
        response: compute.OrganizationSecurityPoliciesListAssociationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.OrganizationSecurityPoliciesListAssociationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_associations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_list_associations_with_metadata`
        interceptor in new development instead of the `post_list_associations` interceptor.
        When both interceptors are used, this `post_list_associations_with_metadata` interceptor runs after the
        `post_list_associations` interceptor. The (possibly modified) response returned by
        `post_list_associations` will be passed to
        `post_list_associations_with_metadata`.
        """
        return response, metadata

    def pre_list_preconfigured_expression_sets(
        self,
        request: compute.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_preconfigured_expression_sets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_list_preconfigured_expression_sets(
        self, response: compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse
    ) -> compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse:
        """Post-rpc interceptor for list_preconfigured_expression_sets

        DEPRECATED. Please use the `post_list_preconfigured_expression_sets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_list_preconfigured_expression_sets` interceptor runs
        before the `post_list_preconfigured_expression_sets_with_metadata` interceptor.
        """
        return response

    def post_list_preconfigured_expression_sets_with_metadata(
        self,
        response: compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_preconfigured_expression_sets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_list_preconfigured_expression_sets_with_metadata`
        interceptor in new development instead of the `post_list_preconfigured_expression_sets` interceptor.
        When both interceptors are used, this `post_list_preconfigured_expression_sets_with_metadata` interceptor runs after the
        `post_list_preconfigured_expression_sets` interceptor. The (possibly modified) response returned by
        `post_list_preconfigured_expression_sets` will be passed to
        `post_list_preconfigured_expression_sets_with_metadata`.
        """
        return response, metadata

    def pre_move(
        self,
        request: compute.MoveOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.MoveOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for move

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_move(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for move

        DEPRECATED. Please use the `post_move_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_move` interceptor runs
        before the `post_move_with_metadata` interceptor.
        """
        return response

    def post_move_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for move

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_move_with_metadata`
        interceptor in new development instead of the `post_move` interceptor.
        When both interceptors are used, this `post_move_with_metadata` interceptor runs after the
        `post_move` interceptor. The (possibly modified) response returned by
        `post_move` will be passed to
        `post_move_with_metadata`.
        """
        return response, metadata

    def pre_patch(
        self,
        request: compute.PatchOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.PatchOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for patch

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_patch(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for patch

        DEPRECATED. Please use the `post_patch_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_patch` interceptor runs
        before the `post_patch_with_metadata` interceptor.
        """
        return response

    def post_patch_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for patch

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_patch_with_metadata`
        interceptor in new development instead of the `post_patch` interceptor.
        When both interceptors are used, this `post_patch_with_metadata` interceptor runs after the
        `post_patch` interceptor. The (possibly modified) response returned by
        `post_patch` will be passed to
        `post_patch_with_metadata`.
        """
        return response, metadata

    def pre_patch_rule(
        self,
        request: compute.PatchRuleOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.PatchRuleOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for patch_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_patch_rule(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for patch_rule

        DEPRECATED. Please use the `post_patch_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_patch_rule` interceptor runs
        before the `post_patch_rule_with_metadata` interceptor.
        """
        return response

    def post_patch_rule_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for patch_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_patch_rule_with_metadata`
        interceptor in new development instead of the `post_patch_rule` interceptor.
        When both interceptors are used, this `post_patch_rule_with_metadata` interceptor runs after the
        `post_patch_rule` interceptor. The (possibly modified) response returned by
        `post_patch_rule` will be passed to
        `post_patch_rule_with_metadata`.
        """
        return response, metadata

    def pre_remove_association(
        self,
        request: compute.RemoveAssociationOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.RemoveAssociationOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_remove_association(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for remove_association

        DEPRECATED. Please use the `post_remove_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_remove_association` interceptor runs
        before the `post_remove_association_with_metadata` interceptor.
        """
        return response

    def post_remove_association_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_remove_association_with_metadata`
        interceptor in new development instead of the `post_remove_association` interceptor.
        When both interceptors are used, this `post_remove_association_with_metadata` interceptor runs after the
        `post_remove_association` interceptor. The (possibly modified) response returned by
        `post_remove_association` will be passed to
        `post_remove_association_with_metadata`.
        """
        return response, metadata

    def pre_remove_rule(
        self,
        request: compute.RemoveRuleOrganizationSecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.RemoveRuleOrganizationSecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityPolicies server.
        """
        return request, metadata

    def post_remove_rule(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for remove_rule

        DEPRECATED. Please use the `post_remove_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityPolicies server but before
        it is returned to user code. This `post_remove_rule` interceptor runs
        before the `post_remove_rule_with_metadata` interceptor.
        """
        return response

    def post_remove_rule_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityPolicies server but before it is returned to user code.

        We recommend only using this `post_remove_rule_with_metadata`
        interceptor in new development instead of the `post_remove_rule` interceptor.
        When both interceptors are used, this `post_remove_rule_with_metadata` interceptor runs after the
        `post_remove_rule` interceptor. The (possibly modified) response returned by
        `post_remove_rule` will be passed to
        `post_remove_rule_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class OrganizationSecurityPoliciesRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OrganizationSecurityPoliciesRestInterceptor


class OrganizationSecurityPoliciesRestTransport(
    _BaseOrganizationSecurityPoliciesRestTransport
):
    """REST backend synchronous transport for OrganizationSecurityPolicies.

    The OrganizationSecurityPolicies API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "compute.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[OrganizationSecurityPoliciesRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        NOTE: This REST transport functionality is currently in a beta
        state (preview). We welcome your feedback via a GitHub issue in
        this library's repository. Thank you!

         Args:
             host (Optional[str]):
                  The hostname to connect to (default: 'compute.googleapis.com').
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
             interceptor (Optional[OrganizationSecurityPoliciesRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or OrganizationSecurityPoliciesRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AddAssociation(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseAddAssociation,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.AddAssociation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.AddAssociationOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the add association method over HTTP.

            Args:
                request (~.compute.AddAssociationOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.AddAssociation.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseAddAssociation._get_http_options()
            request, metadata = self._interceptor.pre_add_association(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseAddAssociation,
                    "_BaseAddAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.AddAssociation",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "AddAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OrganizationSecurityPoliciesRestTransport._AddAssociation._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_association_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.add_association",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "AddAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AddRule(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseAddRule,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.AddRule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.AddRuleOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the add rule method over HTTP.

            Args:
                request (~.compute.AddRuleOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.AddRule.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseAddRule._get_http_options()
            request, metadata = self._interceptor.pre_add_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseAddRule,
                    "_BaseAddRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.AddRule",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "AddRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._AddRule._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.add_rule",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "AddRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CopyRules(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseCopyRules,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.CopyRules")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.CopyRulesOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the copy rules method over HTTP.

            Args:
                request (~.compute.CopyRulesOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.CopyRules.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseCopyRules._get_http_options()
            request, metadata = self._interceptor.pre_copy_rules(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseCopyRules,
                    "_BaseCopyRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.CopyRules",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "CopyRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OrganizationSecurityPoliciesRestTransport._CopyRules._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_copy_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_copy_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.copy_rules",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "CopyRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Delete(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseDelete,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.Delete")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.DeleteOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the delete method over HTTP.

            Args:
                request (~.compute.DeleteOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.Delete. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseDelete._get_http_options()
            request, metadata = self._interceptor.pre_delete(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseDelete,
                    "_BaseDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.Delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Delete",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._Delete._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Delete",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Get(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseGet,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.Get")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.SecurityPolicy:
            r"""Call the get method over HTTP.

            Args:
                request (~.compute.GetOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.Get. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.SecurityPolicy:
                    Represents a Google Cloud Armor
                security policy resource.
                Only external backend services that use
                load balancers can reference a security
                policy. For more information, see Google
                Cloud Armor security policy overview.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseGet._get_http_options()
            request, metadata = self._interceptor.pre_get(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseGet,
                    "_BaseGet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.Get",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Get",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._Get._get_response(
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
            resp = compute.SecurityPolicy()
            pb_resp = compute.SecurityPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.SecurityPolicy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.get",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Get",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAssociation(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseGetAssociation,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.GetAssociation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetAssociationOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.SecurityPolicyAssociation:
            r"""Call the get association method over HTTP.

            Args:
                request (~.compute.GetAssociationOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.GetAssociation.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.SecurityPolicyAssociation:

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseGetAssociation._get_http_options()
            request, metadata = self._interceptor.pre_get_association(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseGetAssociation,
                    "_BaseGetAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.GetAssociation",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "GetAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OrganizationSecurityPoliciesRestTransport._GetAssociation._get_response(
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
            resp = compute.SecurityPolicyAssociation()
            pb_resp = compute.SecurityPolicyAssociation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_association_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.SecurityPolicyAssociation.to_json(
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
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.get_association",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "GetAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRule(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseGetRule,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.GetRule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetRuleOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.SecurityPolicyRule:
            r"""Call the get rule method over HTTP.

            Args:
                request (~.compute.GetRuleOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.GetRule.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.SecurityPolicyRule:
                    Represents a rule that describes one
                or more match conditions along with the
                action to be taken when traffic matches
                this condition (allow or deny).

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseGetRule._get_http_options()
            request, metadata = self._interceptor.pre_get_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseGetRule,
                    "_BaseGetRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.GetRule",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "GetRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._GetRule._get_response(
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
            resp = compute.SecurityPolicyRule()
            pb_resp = compute.SecurityPolicyRule.pb(resp)

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
                    response_payload = compute.SecurityPolicyRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.get_rule",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "GetRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Insert(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseInsert,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.Insert")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.InsertOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the insert method over HTTP.

            Args:
                request (~.compute.InsertOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.Insert. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseInsert._get_http_options()
            request, metadata = self._interceptor.pre_insert(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseInsert,
                    "_BaseInsert__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.Insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Insert",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._Insert._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Insert",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _List(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseList,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.List")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.ListOrganizationSecurityPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.SecurityPolicyList:
            r"""Call the list method over HTTP.

            Args:
                request (~.compute.ListOrganizationSecurityPoliciesRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.List. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.SecurityPolicyList:

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseList._get_http_options()
            request, metadata = self._interceptor.pre_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseList,
                    "_BaseList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.List",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "List",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._List._get_response(
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
            resp = compute.SecurityPolicyList()
            pb_resp = compute.SecurityPolicyList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.SecurityPolicyList.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.list",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "List",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAssociations(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseListAssociations,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.ListAssociations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.ListAssociationsOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.OrganizationSecurityPoliciesListAssociationsResponse:
            r"""Call the list associations method over HTTP.

            Args:
                request (~.compute.ListAssociationsOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.ListAssociations.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.OrganizationSecurityPoliciesListAssociationsResponse:

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseListAssociations._get_http_options()
            request, metadata = self._interceptor.pre_list_associations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseListAssociations,
                    "_BaseListAssociations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.ListAssociations",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "ListAssociations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._ListAssociations._get_response(
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
            resp = compute.OrganizationSecurityPoliciesListAssociationsResponse()
            pb_resp = compute.OrganizationSecurityPoliciesListAssociationsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_associations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_associations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.OrganizationSecurityPoliciesListAssociationsResponse.to_json(
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
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.list_associations",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "ListAssociations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPreconfiguredExpressionSets(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseListPreconfiguredExpressionSets,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityPoliciesRestTransport.ListPreconfiguredExpressionSets"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse:
            r"""Call the list preconfigured
            expression sets method over HTTP.

                Args:
                    request (~.compute.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest):
                        The request object. A request message for
                    OrganizationSecurityPolicies.ListPreconfiguredExpressionSets.
                    See the method description for details.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse:

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseListPreconfiguredExpressionSets._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_preconfigured_expression_sets(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseListPreconfiguredExpressionSets,
                    "_BaseListPreconfiguredExpressionSets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.ListPreconfiguredExpressionSets",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "ListPreconfiguredExpressionSets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._ListPreconfiguredExpressionSets._get_response(
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
            resp = compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse()
            pb_resp = (
                compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse.pb(resp)
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_preconfigured_expression_sets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_preconfigured_expression_sets_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse.to_json(
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
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.list_preconfigured_expression_sets",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "ListPreconfiguredExpressionSets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Move(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseMove,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.Move")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.MoveOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the move method over HTTP.

            Args:
                request (~.compute.MoveOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.Move. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseMove._get_http_options()
            request, metadata = self._interceptor.pre_move(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseMove,
                    "_BaseMove__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.Move",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Move",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._Move._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_move(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_move_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.move",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Move",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Patch(
        _BaseOrganizationSecurityPoliciesRestTransport._BasePatch,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.Patch")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.PatchOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the patch method over HTTP.

            Args:
                request (~.compute.PatchOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.Patch. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BasePatch._get_http_options()
            request, metadata = self._interceptor.pre_patch(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BasePatch,
                    "_BasePatch__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.Patch",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Patch",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._Patch._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_patch(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_patch_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.patch",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "Patch",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PatchRule(
        _BaseOrganizationSecurityPoliciesRestTransport._BasePatchRule,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.PatchRule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.PatchRuleOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the patch rule method over HTTP.

            Args:
                request (~.compute.PatchRuleOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.PatchRule.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BasePatchRule._get_http_options()
            request, metadata = self._interceptor.pre_patch_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BasePatchRule,
                    "_BasePatchRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.PatchRule",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "PatchRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OrganizationSecurityPoliciesRestTransport._PatchRule._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_patch_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_patch_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.patch_rule",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "PatchRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveAssociation(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseRemoveAssociation,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.RemoveAssociation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.RemoveAssociationOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the remove association method over HTTP.

            Args:
                request (~.compute.RemoveAssociationOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.RemoveAssociation.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseRemoveAssociation._get_http_options()
            request, metadata = self._interceptor.pre_remove_association(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseRemoveAssociation,
                    "_BaseRemoveAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.RemoveAssociation",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "RemoveAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityPoliciesRestTransport._RemoveAssociation._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_association_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.remove_association",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "RemoveAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveRule(
        _BaseOrganizationSecurityPoliciesRestTransport._BaseRemoveRule,
        OrganizationSecurityPoliciesRestStub,
    ):
        def __hash__(self):
            return hash("OrganizationSecurityPoliciesRestTransport.RemoveRule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.RemoveRuleOrganizationSecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the remove rule method over HTTP.

            Args:
                request (~.compute.RemoveRuleOrganizationSecurityPolicyRequest):
                    The request object. A request message for
                OrganizationSecurityPolicies.RemoveRule.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseOrganizationSecurityPoliciesRestTransport._BaseRemoveRule._get_http_options()
            request, metadata = self._interceptor.pre_remove_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityPoliciesRestTransport._BaseRemoveRule,
                    "_BaseRemoveRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.RemoveRule",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "RemoveRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OrganizationSecurityPoliciesRestTransport._RemoveRule._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.OrganizationSecurityPoliciesClient.remove_rule",
                    extra={
                        "serviceName": "google.cloud.compute.v1.OrganizationSecurityPolicies",
                        "rpcName": "RemoveRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def add_association(
        self,
    ) -> Callable[
        [compute.AddAssociationOrganizationSecurityPolicyRequest], compute.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddAssociation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_rule(
        self,
    ) -> Callable[
        [compute.AddRuleOrganizationSecurityPolicyRequest], compute.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def copy_rules(
        self,
    ) -> Callable[
        [compute.CopyRulesOrganizationSecurityPolicyRequest], compute.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CopyRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete(
        self,
    ) -> Callable[[compute.DeleteOrganizationSecurityPolicyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Delete(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get(
        self,
    ) -> Callable[
        [compute.GetOrganizationSecurityPolicyRequest], compute.SecurityPolicy
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Get(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_association(
        self,
    ) -> Callable[
        [compute.GetAssociationOrganizationSecurityPolicyRequest],
        compute.SecurityPolicyAssociation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAssociation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_rule(
        self,
    ) -> Callable[
        [compute.GetRuleOrganizationSecurityPolicyRequest], compute.SecurityPolicyRule
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def insert(
        self,
    ) -> Callable[[compute.InsertOrganizationSecurityPolicyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Insert(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list(
        self,
    ) -> Callable[
        [compute.ListOrganizationSecurityPoliciesRequest], compute.SecurityPolicyList
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._List(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_associations(
        self,
    ) -> Callable[
        [compute.ListAssociationsOrganizationSecurityPolicyRequest],
        compute.OrganizationSecurityPoliciesListAssociationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAssociations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_preconfigured_expression_sets(
        self,
    ) -> Callable[
        [compute.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest],
        compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPreconfiguredExpressionSets(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def move(
        self,
    ) -> Callable[[compute.MoveOrganizationSecurityPolicyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Move(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def patch(
        self,
    ) -> Callable[[compute.PatchOrganizationSecurityPolicyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Patch(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def patch_rule(
        self,
    ) -> Callable[
        [compute.PatchRuleOrganizationSecurityPolicyRequest], compute.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PatchRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_association(
        self,
    ) -> Callable[
        [compute.RemoveAssociationOrganizationSecurityPolicyRequest], compute.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveAssociation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_rule(
        self,
    ) -> Callable[
        [compute.RemoveRuleOrganizationSecurityPolicyRequest], compute.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("OrganizationSecurityPoliciesRestTransport",)
