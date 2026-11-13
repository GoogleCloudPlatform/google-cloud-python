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

from google.cloud.orgpolicy_v2._compat import transcode_request
from google.cloud.orgpolicy_v2.types import constraint, orgpolicy

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOrgPolicyRestTransport

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


class OrgPolicyRestInterceptor:
    """Interceptor for OrgPolicy.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OrgPolicyRestTransport.

    .. code-block:: python
        class MyCustomOrgPolicyInterceptor(OrgPolicyRestInterceptor):
            def pre_create_custom_constraint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_custom_constraint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_custom_constraint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_custom_constraint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_custom_constraint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_effective_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_effective_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_constraints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_constraints(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_custom_constraints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_custom_constraints(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_custom_constraint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_custom_constraint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OrgPolicyRestTransport(interceptor=MyCustomOrgPolicyInterceptor())
        client = OrgPolicyClient(transport=transport)


    """

    def pre_create_custom_constraint(
        self,
        request: orgpolicy.CreateCustomConstraintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.CreateCustomConstraintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_custom_constraint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_create_custom_constraint(
        self, response: constraint.CustomConstraint
    ) -> constraint.CustomConstraint:
        """Post-rpc interceptor for create_custom_constraint

        DEPRECATED. Please use the `post_create_custom_constraint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_create_custom_constraint` interceptor runs
        before the `post_create_custom_constraint_with_metadata` interceptor.
        """
        return response

    def post_create_custom_constraint_with_metadata(
        self,
        response: constraint.CustomConstraint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[constraint.CustomConstraint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_custom_constraint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_create_custom_constraint_with_metadata`
        interceptor in new development instead of the `post_create_custom_constraint` interceptor.
        When both interceptors are used, this `post_create_custom_constraint_with_metadata` interceptor runs after the
        `post_create_custom_constraint` interceptor. The (possibly modified) response returned by
        `post_create_custom_constraint` will be passed to
        `post_create_custom_constraint_with_metadata`.
        """
        return response, metadata

    def pre_create_policy(
        self,
        request: orgpolicy.CreatePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.CreatePolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_create_policy(self, response: orgpolicy.Policy) -> orgpolicy.Policy:
        """Post-rpc interceptor for create_policy

        DEPRECATED. Please use the `post_create_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_create_policy` interceptor runs
        before the `post_create_policy_with_metadata` interceptor.
        """
        return response

    def post_create_policy_with_metadata(
        self,
        response: orgpolicy.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_create_policy_with_metadata`
        interceptor in new development instead of the `post_create_policy` interceptor.
        When both interceptors are used, this `post_create_policy_with_metadata` interceptor runs after the
        `post_create_policy` interceptor. The (possibly modified) response returned by
        `post_create_policy` will be passed to
        `post_create_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_custom_constraint(
        self,
        request: orgpolicy.DeleteCustomConstraintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.DeleteCustomConstraintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_custom_constraint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def pre_delete_policy(
        self,
        request: orgpolicy.DeletePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.DeletePolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def pre_get_custom_constraint(
        self,
        request: orgpolicy.GetCustomConstraintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.GetCustomConstraintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_custom_constraint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_get_custom_constraint(
        self, response: constraint.CustomConstraint
    ) -> constraint.CustomConstraint:
        """Post-rpc interceptor for get_custom_constraint

        DEPRECATED. Please use the `post_get_custom_constraint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_get_custom_constraint` interceptor runs
        before the `post_get_custom_constraint_with_metadata` interceptor.
        """
        return response

    def post_get_custom_constraint_with_metadata(
        self,
        response: constraint.CustomConstraint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[constraint.CustomConstraint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_custom_constraint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_get_custom_constraint_with_metadata`
        interceptor in new development instead of the `post_get_custom_constraint` interceptor.
        When both interceptors are used, this `post_get_custom_constraint_with_metadata` interceptor runs after the
        `post_get_custom_constraint` interceptor. The (possibly modified) response returned by
        `post_get_custom_constraint` will be passed to
        `post_get_custom_constraint_with_metadata`.
        """
        return response, metadata

    def pre_get_effective_policy(
        self,
        request: orgpolicy.GetEffectivePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.GetEffectivePolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_effective_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_get_effective_policy(self, response: orgpolicy.Policy) -> orgpolicy.Policy:
        """Post-rpc interceptor for get_effective_policy

        DEPRECATED. Please use the `post_get_effective_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_get_effective_policy` interceptor runs
        before the `post_get_effective_policy_with_metadata` interceptor.
        """
        return response

    def post_get_effective_policy_with_metadata(
        self,
        response: orgpolicy.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_effective_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_get_effective_policy_with_metadata`
        interceptor in new development instead of the `post_get_effective_policy` interceptor.
        When both interceptors are used, this `post_get_effective_policy_with_metadata` interceptor runs after the
        `post_get_effective_policy` interceptor. The (possibly modified) response returned by
        `post_get_effective_policy` will be passed to
        `post_get_effective_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_policy(
        self,
        request: orgpolicy.GetPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.GetPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_get_policy(self, response: orgpolicy.Policy) -> orgpolicy.Policy:
        """Post-rpc interceptor for get_policy

        DEPRECATED. Please use the `post_get_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_get_policy` interceptor runs
        before the `post_get_policy_with_metadata` interceptor.
        """
        return response

    def post_get_policy_with_metadata(
        self,
        response: orgpolicy.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_get_policy_with_metadata`
        interceptor in new development instead of the `post_get_policy` interceptor.
        When both interceptors are used, this `post_get_policy_with_metadata` interceptor runs after the
        `post_get_policy` interceptor. The (possibly modified) response returned by
        `post_get_policy` will be passed to
        `post_get_policy_with_metadata`.
        """
        return response, metadata

    def pre_list_constraints(
        self,
        request: orgpolicy.ListConstraintsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.ListConstraintsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_constraints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_list_constraints(
        self, response: orgpolicy.ListConstraintsResponse
    ) -> orgpolicy.ListConstraintsResponse:
        """Post-rpc interceptor for list_constraints

        DEPRECATED. Please use the `post_list_constraints_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_list_constraints` interceptor runs
        before the `post_list_constraints_with_metadata` interceptor.
        """
        return response

    def post_list_constraints_with_metadata(
        self,
        response: orgpolicy.ListConstraintsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.ListConstraintsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_constraints

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_list_constraints_with_metadata`
        interceptor in new development instead of the `post_list_constraints` interceptor.
        When both interceptors are used, this `post_list_constraints_with_metadata` interceptor runs after the
        `post_list_constraints` interceptor. The (possibly modified) response returned by
        `post_list_constraints` will be passed to
        `post_list_constraints_with_metadata`.
        """
        return response, metadata

    def pre_list_custom_constraints(
        self,
        request: orgpolicy.ListCustomConstraintsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.ListCustomConstraintsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_custom_constraints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_list_custom_constraints(
        self, response: orgpolicy.ListCustomConstraintsResponse
    ) -> orgpolicy.ListCustomConstraintsResponse:
        """Post-rpc interceptor for list_custom_constraints

        DEPRECATED. Please use the `post_list_custom_constraints_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_list_custom_constraints` interceptor runs
        before the `post_list_custom_constraints_with_metadata` interceptor.
        """
        return response

    def post_list_custom_constraints_with_metadata(
        self,
        response: orgpolicy.ListCustomConstraintsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.ListCustomConstraintsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_custom_constraints

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_list_custom_constraints_with_metadata`
        interceptor in new development instead of the `post_list_custom_constraints` interceptor.
        When both interceptors are used, this `post_list_custom_constraints_with_metadata` interceptor runs after the
        `post_list_custom_constraints` interceptor. The (possibly modified) response returned by
        `post_list_custom_constraints` will be passed to
        `post_list_custom_constraints_with_metadata`.
        """
        return response, metadata

    def pre_list_policies(
        self,
        request: orgpolicy.ListPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.ListPoliciesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_list_policies(
        self, response: orgpolicy.ListPoliciesResponse
    ) -> orgpolicy.ListPoliciesResponse:
        """Post-rpc interceptor for list_policies

        DEPRECATED. Please use the `post_list_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_list_policies` interceptor runs
        before the `post_list_policies_with_metadata` interceptor.
        """
        return response

    def post_list_policies_with_metadata(
        self,
        response: orgpolicy.ListPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.ListPoliciesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_list_policies_with_metadata`
        interceptor in new development instead of the `post_list_policies` interceptor.
        When both interceptors are used, this `post_list_policies_with_metadata` interceptor runs after the
        `post_list_policies` interceptor. The (possibly modified) response returned by
        `post_list_policies` will be passed to
        `post_list_policies_with_metadata`.
        """
        return response, metadata

    def pre_update_custom_constraint(
        self,
        request: orgpolicy.UpdateCustomConstraintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        orgpolicy.UpdateCustomConstraintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_custom_constraint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_update_custom_constraint(
        self, response: constraint.CustomConstraint
    ) -> constraint.CustomConstraint:
        """Post-rpc interceptor for update_custom_constraint

        DEPRECATED. Please use the `post_update_custom_constraint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_update_custom_constraint` interceptor runs
        before the `post_update_custom_constraint_with_metadata` interceptor.
        """
        return response

    def post_update_custom_constraint_with_metadata(
        self,
        response: constraint.CustomConstraint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[constraint.CustomConstraint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_custom_constraint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_update_custom_constraint_with_metadata`
        interceptor in new development instead of the `post_update_custom_constraint` interceptor.
        When both interceptors are used, this `post_update_custom_constraint_with_metadata` interceptor runs after the
        `post_update_custom_constraint` interceptor. The (possibly modified) response returned by
        `post_update_custom_constraint` will be passed to
        `post_update_custom_constraint_with_metadata`.
        """
        return response, metadata

    def pre_update_policy(
        self,
        request: orgpolicy.UpdatePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.UpdatePolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrgPolicy server.
        """
        return request, metadata

    def post_update_policy(self, response: orgpolicy.Policy) -> orgpolicy.Policy:
        """Post-rpc interceptor for update_policy

        DEPRECATED. Please use the `post_update_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrgPolicy server but before
        it is returned to user code. This `post_update_policy` interceptor runs
        before the `post_update_policy_with_metadata` interceptor.
        """
        return response

    def post_update_policy_with_metadata(
        self,
        response: orgpolicy.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[orgpolicy.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrgPolicy server but before it is returned to user code.

        We recommend only using this `post_update_policy_with_metadata`
        interceptor in new development instead of the `post_update_policy` interceptor.
        When both interceptors are used, this `post_update_policy_with_metadata` interceptor runs after the
        `post_update_policy` interceptor. The (possibly modified) response returned by
        `post_update_policy` will be passed to
        `post_update_policy_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class OrgPolicyRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OrgPolicyRestInterceptor


class OrgPolicyRestTransport(_BaseOrgPolicyRestTransport):
    """REST backend synchronous transport for OrgPolicy.

    An interface for managing organization policies.

    The Organization Policy Service provides a simple mechanism for
    organizations to restrict the allowed configurations across
    their entire resource hierarchy.

    You can use a policy to configure restrictions on resources. For
    example, you can enforce a policy that restricts which Google
    Cloud APIs can be activated in a certain part of your resource
    hierarchy, or prevents serial port access to VM instances in a
    particular folder.

    Policies are inherited down through the resource hierarchy. A
    policy applied to a parent resource automatically applies to all
    its child resources unless overridden with a policy lower in the
    hierarchy.

    A constraint defines an aspect of a resource's configuration
    that can be controlled by an organization's policy
    administrator. Policies are a collection of constraints that
    defines their allowable configuration on a particular resource
    and its child resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "orgpolicy.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[OrgPolicyRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'orgpolicy.googleapis.com').
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
            interceptor (Optional[OrgPolicyRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or OrgPolicyRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateCustomConstraint(
        _BaseOrgPolicyRestTransport._BaseCreateCustomConstraint, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.CreateCustomConstraint")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.CreateCustomConstraintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> constraint.CustomConstraint:
            r"""Call the create custom constraint method over HTTP.

            Args:
                request (~.orgpolicy.CreateCustomConstraintRequest):
                    The request object. The request sent to the [CreateCustomConstraintRequest]
                [google.cloud.orgpolicy.v2.OrgPolicy.CreateCustomConstraint]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.constraint.CustomConstraint:
                    A custom constraint defined by customers which can
                *only* be applied to the given resource types and
                organization.

                By creating a custom constraint, customers can apply
                policies of this custom constraint. *Creating a custom
                constraint itself does NOT apply any policy
                enforcement*.

            """

            http_options = _BaseOrgPolicyRestTransport._BaseCreateCustomConstraint._get_http_options()
            request, metadata = self._interceptor.pre_create_custom_constraint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseCreateCustomConstraint,
                    "_BaseCreateCustomConstraint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.CreateCustomConstraint",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "CreateCustomConstraint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._CreateCustomConstraint._get_response(
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
            resp = constraint.CustomConstraint()
            pb_resp = constraint.CustomConstraint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_custom_constraint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_custom_constraint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = constraint.CustomConstraint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.create_custom_constraint",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "CreateCustomConstraint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePolicy(
        _BaseOrgPolicyRestTransport._BaseCreatePolicy, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.CreatePolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.CreatePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> orgpolicy.Policy:
            r"""Call the create policy method over HTTP.

            Args:
                request (~.orgpolicy.CreatePolicyRequest):
                    The request object. The request sent to the [CreatePolicyRequest]
                [google.cloud.orgpolicy.v2.OrgPolicy.CreatePolicy]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.orgpolicy.Policy:
                    Defines an organization policy which
                is used to specify constraints for
                configurations of Google Cloud
                resources.

            """

            http_options = (
                _BaseOrgPolicyRestTransport._BaseCreatePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseCreatePolicy,
                    "_BaseCreatePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.CreatePolicy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "CreatePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._CreatePolicy._get_response(
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
            resp = orgpolicy.Policy()
            pb_resp = orgpolicy.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = orgpolicy.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.create_policy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "CreatePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCustomConstraint(
        _BaseOrgPolicyRestTransport._BaseDeleteCustomConstraint, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.DeleteCustomConstraint")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.DeleteCustomConstraintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete custom constraint method over HTTP.

            Args:
                request (~.orgpolicy.DeleteCustomConstraintRequest):
                    The request object. The request sent to the [DeleteCustomConstraint]
                [google.cloud.orgpolicy.v2.OrgPolicy.DeleteCustomConstraint]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseOrgPolicyRestTransport._BaseDeleteCustomConstraint._get_http_options()
            request, metadata = self._interceptor.pre_delete_custom_constraint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseDeleteCustomConstraint,
                    "_BaseDeleteCustomConstraint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.DeleteCustomConstraint",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "DeleteCustomConstraint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._DeleteCustomConstraint._get_response(
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

    class _DeletePolicy(
        _BaseOrgPolicyRestTransport._BaseDeletePolicy, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.DeletePolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.DeletePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete policy method over HTTP.

            Args:
                request (~.orgpolicy.DeletePolicyRequest):
                    The request object. The request sent to the [DeletePolicy]
                [google.cloud.orgpolicy.v2.OrgPolicy.DeletePolicy]
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
                _BaseOrgPolicyRestTransport._BaseDeletePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseDeletePolicy,
                    "_BaseDeletePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.DeletePolicy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "DeletePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._DeletePolicy._get_response(
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

    class _GetCustomConstraint(
        _BaseOrgPolicyRestTransport._BaseGetCustomConstraint, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.GetCustomConstraint")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.GetCustomConstraintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> constraint.CustomConstraint:
            r"""Call the get custom constraint method over HTTP.

            Args:
                request (~.orgpolicy.GetCustomConstraintRequest):
                    The request object. The request sent to the [GetCustomConstraint]
                [google.cloud.orgpolicy.v2.OrgPolicy.GetCustomConstraint]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.constraint.CustomConstraint:
                    A custom constraint defined by customers which can
                *only* be applied to the given resource types and
                organization.

                By creating a custom constraint, customers can apply
                policies of this custom constraint. *Creating a custom
                constraint itself does NOT apply any policy
                enforcement*.

            """

            http_options = (
                _BaseOrgPolicyRestTransport._BaseGetCustomConstraint._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_custom_constraint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseGetCustomConstraint,
                    "_BaseGetCustomConstraint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.GetCustomConstraint",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "GetCustomConstraint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._GetCustomConstraint._get_response(
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
            resp = constraint.CustomConstraint()
            pb_resp = constraint.CustomConstraint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_custom_constraint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_custom_constraint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = constraint.CustomConstraint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.get_custom_constraint",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "GetCustomConstraint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEffectivePolicy(
        _BaseOrgPolicyRestTransport._BaseGetEffectivePolicy, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.GetEffectivePolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.GetEffectivePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> orgpolicy.Policy:
            r"""Call the get effective policy method over HTTP.

            Args:
                request (~.orgpolicy.GetEffectivePolicyRequest):
                    The request object. The request sent to the [GetEffectivePolicy]
                [google.cloud.orgpolicy.v2.OrgPolicy.GetEffectivePolicy]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.orgpolicy.Policy:
                    Defines an organization policy which
                is used to specify constraints for
                configurations of Google Cloud
                resources.

            """

            http_options = (
                _BaseOrgPolicyRestTransport._BaseGetEffectivePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_effective_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseGetEffectivePolicy,
                    "_BaseGetEffectivePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.GetEffectivePolicy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "GetEffectivePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._GetEffectivePolicy._get_response(
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
            resp = orgpolicy.Policy()
            pb_resp = orgpolicy.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_effective_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_effective_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = orgpolicy.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.get_effective_policy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "GetEffectivePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPolicy(_BaseOrgPolicyRestTransport._BaseGetPolicy, OrgPolicyRestStub):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.GetPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.GetPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> orgpolicy.Policy:
            r"""Call the get policy method over HTTP.

            Args:
                request (~.orgpolicy.GetPolicyRequest):
                    The request object. The request sent to the [GetPolicy]
                [google.cloud.orgpolicy.v2.OrgPolicy.GetPolicy] method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.orgpolicy.Policy:
                    Defines an organization policy which
                is used to specify constraints for
                configurations of Google Cloud
                resources.

            """

            http_options = (
                _BaseOrgPolicyRestTransport._BaseGetPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseGetPolicy,
                    "_BaseGetPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.GetPolicy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "GetPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._GetPolicy._get_response(
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
            resp = orgpolicy.Policy()
            pb_resp = orgpolicy.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = orgpolicy.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.get_policy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "GetPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConstraints(
        _BaseOrgPolicyRestTransport._BaseListConstraints, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.ListConstraints")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.ListConstraintsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> orgpolicy.ListConstraintsResponse:
            r"""Call the list constraints method over HTTP.

            Args:
                request (~.orgpolicy.ListConstraintsRequest):
                    The request object. The request sent to the [ListConstraints]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.orgpolicy.ListConstraintsResponse:
                    The response returned from the [ListConstraints]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints]
                method.

            """

            http_options = (
                _BaseOrgPolicyRestTransport._BaseListConstraints._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_constraints(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseListConstraints,
                    "_BaseListConstraints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.ListConstraints",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "ListConstraints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._ListConstraints._get_response(
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
            resp = orgpolicy.ListConstraintsResponse()
            pb_resp = orgpolicy.ListConstraintsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_constraints(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_constraints_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = orgpolicy.ListConstraintsResponse.to_json(
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
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.list_constraints",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "ListConstraints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCustomConstraints(
        _BaseOrgPolicyRestTransport._BaseListCustomConstraints, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.ListCustomConstraints")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.ListCustomConstraintsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> orgpolicy.ListCustomConstraintsResponse:
            r"""Call the list custom constraints method over HTTP.

            Args:
                request (~.orgpolicy.ListCustomConstraintsRequest):
                    The request object. The request sent to the [ListCustomConstraints]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.orgpolicy.ListCustomConstraintsResponse:
                    The response returned from the [ListCustomConstraints]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints]
                method. It will be empty if no custom or managed
                constraints are set on the organization resource.

            """

            http_options = _BaseOrgPolicyRestTransport._BaseListCustomConstraints._get_http_options()
            request, metadata = self._interceptor.pre_list_custom_constraints(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseListCustomConstraints,
                    "_BaseListCustomConstraints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.ListCustomConstraints",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "ListCustomConstraints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._ListCustomConstraints._get_response(
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
            resp = orgpolicy.ListCustomConstraintsResponse()
            pb_resp = orgpolicy.ListCustomConstraintsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_custom_constraints(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_custom_constraints_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = orgpolicy.ListCustomConstraintsResponse.to_json(
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
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.list_custom_constraints",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "ListCustomConstraints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPolicies(
        _BaseOrgPolicyRestTransport._BaseListPolicies, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.ListPolicies")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.ListPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> orgpolicy.ListPoliciesResponse:
            r"""Call the list policies method over HTTP.

            Args:
                request (~.orgpolicy.ListPoliciesRequest):
                    The request object. The request sent to the [ListPolicies]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.orgpolicy.ListPoliciesResponse:
                    The response returned from the [ListPolicies]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies]
                method. It will be empty if no policies are set on the
                resource.

            """

            http_options = (
                _BaseOrgPolicyRestTransport._BaseListPolicies._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_policies(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseListPolicies,
                    "_BaseListPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.ListPolicies",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "ListPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._ListPolicies._get_response(
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
            resp = orgpolicy.ListPoliciesResponse()
            pb_resp = orgpolicy.ListPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = orgpolicy.ListPoliciesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.list_policies",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "ListPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCustomConstraint(
        _BaseOrgPolicyRestTransport._BaseUpdateCustomConstraint, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.UpdateCustomConstraint")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.UpdateCustomConstraintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> constraint.CustomConstraint:
            r"""Call the update custom constraint method over HTTP.

            Args:
                request (~.orgpolicy.UpdateCustomConstraintRequest):
                    The request object. The request sent to the [UpdateCustomConstraintRequest]
                [google.cloud.orgpolicy.v2.OrgPolicy.UpdateCustomConstraint]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.constraint.CustomConstraint:
                    A custom constraint defined by customers which can
                *only* be applied to the given resource types and
                organization.

                By creating a custom constraint, customers can apply
                policies of this custom constraint. *Creating a custom
                constraint itself does NOT apply any policy
                enforcement*.

            """

            http_options = _BaseOrgPolicyRestTransport._BaseUpdateCustomConstraint._get_http_options()
            request, metadata = self._interceptor.pre_update_custom_constraint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseUpdateCustomConstraint,
                    "_BaseUpdateCustomConstraint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.UpdateCustomConstraint",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "UpdateCustomConstraint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._UpdateCustomConstraint._get_response(
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
            resp = constraint.CustomConstraint()
            pb_resp = constraint.CustomConstraint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_custom_constraint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_custom_constraint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = constraint.CustomConstraint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.update_custom_constraint",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "UpdateCustomConstraint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePolicy(
        _BaseOrgPolicyRestTransport._BaseUpdatePolicy, OrgPolicyRestStub
    ):
        def __hash__(self):
            return hash("OrgPolicyRestTransport.UpdatePolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: orgpolicy.UpdatePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> orgpolicy.Policy:
            r"""Call the update policy method over HTTP.

            Args:
                request (~.orgpolicy.UpdatePolicyRequest):
                    The request object. The request sent to the [UpdatePolicyRequest]
                [google.cloud.orgpolicy.v2.OrgPolicy.UpdatePolicy]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.orgpolicy.Policy:
                    Defines an organization policy which
                is used to specify constraints for
                configurations of Google Cloud
                resources.

            """

            http_options = (
                _BaseOrgPolicyRestTransport._BaseUpdatePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrgPolicyRestTransport._BaseUpdatePolicy,
                    "_BaseUpdatePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orgpolicy_v2.OrgPolicyClient.UpdatePolicy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "UpdatePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrgPolicyRestTransport._UpdatePolicy._get_response(
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
            resp = orgpolicy.Policy()
            pb_resp = orgpolicy.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = orgpolicy.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orgpolicy_v2.OrgPolicyClient.update_policy",
                    extra={
                        "serviceName": "google.cloud.orgpolicy.v2.OrgPolicy",
                        "rpcName": "UpdatePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_custom_constraint(
        self,
    ) -> Callable[
        [orgpolicy.CreateCustomConstraintRequest], constraint.CustomConstraint
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCustomConstraint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_policy(
        self,
    ) -> Callable[[orgpolicy.CreatePolicyRequest], orgpolicy.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_custom_constraint(
        self,
    ) -> Callable[[orgpolicy.DeleteCustomConstraintRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCustomConstraint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_policy(
        self,
    ) -> Callable[[orgpolicy.DeletePolicyRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_custom_constraint(
        self,
    ) -> Callable[[orgpolicy.GetCustomConstraintRequest], constraint.CustomConstraint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCustomConstraint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_effective_policy(
        self,
    ) -> Callable[[orgpolicy.GetEffectivePolicyRequest], orgpolicy.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEffectivePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_policy(self) -> Callable[[orgpolicy.GetPolicyRequest], orgpolicy.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_constraints(
        self,
    ) -> Callable[
        [orgpolicy.ListConstraintsRequest], orgpolicy.ListConstraintsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConstraints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_custom_constraints(
        self,
    ) -> Callable[
        [orgpolicy.ListCustomConstraintsRequest],
        orgpolicy.ListCustomConstraintsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCustomConstraints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_policies(
        self,
    ) -> Callable[[orgpolicy.ListPoliciesRequest], orgpolicy.ListPoliciesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_custom_constraint(
        self,
    ) -> Callable[
        [orgpolicy.UpdateCustomConstraintRequest], constraint.CustomConstraint
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCustomConstraint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_policy(
        self,
    ) -> Callable[[orgpolicy.UpdatePolicyRequest], orgpolicy.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("OrgPolicyRestTransport",)
