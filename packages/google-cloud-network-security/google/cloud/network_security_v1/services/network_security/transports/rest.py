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

from google.cloud.network_security_v1._compat import transcode_request
from google.cloud.network_security_v1.types import (
    authorization_policy,
    authz_policy,
    backend_authentication_config,
    client_tls_policy,
    gateway_security_policy,
    gateway_security_policy_rule,
    server_tls_policy,
    tls_inspection_policy,
    url_list,
)
from google.cloud.network_security_v1.types import (
    authorization_policy as gcn_authorization_policy,
)
from google.cloud.network_security_v1.types import authz_policy as gcn_authz_policy
from google.cloud.network_security_v1.types import (
    backend_authentication_config as gcn_backend_authentication_config,
)
from google.cloud.network_security_v1.types import (
    client_tls_policy as gcn_client_tls_policy,
)
from google.cloud.network_security_v1.types import (
    gateway_security_policy as gcn_gateway_security_policy,
)
from google.cloud.network_security_v1.types import (
    gateway_security_policy_rule as gcn_gateway_security_policy_rule,
)
from google.cloud.network_security_v1.types import (
    server_tls_policy as gcn_server_tls_policy,
)
from google.cloud.network_security_v1.types import (
    tls_inspection_policy as gcn_tls_inspection_policy,
)
from google.cloud.network_security_v1.types import url_list as gcn_url_list

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseNetworkSecurityRestTransport

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


class NetworkSecurityRestInterceptor:
    """Interceptor for NetworkSecurity.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the NetworkSecurityRestTransport.

    .. code-block:: python
        class MyCustomNetworkSecurityInterceptor(NetworkSecurityRestInterceptor):
            def pre_create_authorization_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_authorization_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_authz_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_authz_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backend_authentication_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backend_authentication_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_client_tls_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_client_tls_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_gateway_security_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_gateway_security_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_gateway_security_policy_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_gateway_security_policy_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_server_tls_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_server_tls_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tls_inspection_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tls_inspection_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_url_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_url_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_authorization_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_authorization_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_authz_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_authz_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backend_authentication_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backend_authentication_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_client_tls_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_client_tls_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_gateway_security_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_gateway_security_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_gateway_security_policy_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_gateway_security_policy_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_server_tls_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_server_tls_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tls_inspection_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_tls_inspection_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_url_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_url_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_authorization_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_authorization_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_authz_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_authz_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backend_authentication_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backend_authentication_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_client_tls_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_client_tls_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_gateway_security_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_gateway_security_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_gateway_security_policy_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_gateway_security_policy_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_server_tls_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_server_tls_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tls_inspection_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tls_inspection_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_url_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_url_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_authorization_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_authorization_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_authz_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_authz_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backend_authentication_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backend_authentication_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_client_tls_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_client_tls_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_gateway_security_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_gateway_security_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_gateway_security_policy_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_gateway_security_policy_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_server_tls_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_server_tls_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tls_inspection_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tls_inspection_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_url_lists(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_url_lists(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_authorization_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_authorization_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_authz_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_authz_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backend_authentication_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backend_authentication_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_client_tls_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_client_tls_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_gateway_security_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_gateway_security_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_gateway_security_policy_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_gateway_security_policy_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_server_tls_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_server_tls_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tls_inspection_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tls_inspection_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_url_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_url_list(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = NetworkSecurityRestTransport(interceptor=MyCustomNetworkSecurityInterceptor())
        client = NetworkSecurityClient(transport=transport)


    """

    def pre_create_authorization_policy(
        self,
        request: gcn_authorization_policy.CreateAuthorizationPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_authorization_policy.CreateAuthorizationPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_authorization_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_authorization_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_authorization_policy

        DEPRECATED. Please use the `post_create_authorization_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_authorization_policy` interceptor runs
        before the `post_create_authorization_policy_with_metadata` interceptor.
        """
        return response

    def post_create_authorization_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_authorization_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_authorization_policy_with_metadata`
        interceptor in new development instead of the `post_create_authorization_policy` interceptor.
        When both interceptors are used, this `post_create_authorization_policy_with_metadata` interceptor runs after the
        `post_create_authorization_policy` interceptor. The (possibly modified) response returned by
        `post_create_authorization_policy` will be passed to
        `post_create_authorization_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_authz_policy(
        self,
        request: gcn_authz_policy.CreateAuthzPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_authz_policy.CreateAuthzPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_authz_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_authz_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_authz_policy

        DEPRECATED. Please use the `post_create_authz_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_authz_policy` interceptor runs
        before the `post_create_authz_policy_with_metadata` interceptor.
        """
        return response

    def post_create_authz_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_authz_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_authz_policy_with_metadata`
        interceptor in new development instead of the `post_create_authz_policy` interceptor.
        When both interceptors are used, this `post_create_authz_policy_with_metadata` interceptor runs after the
        `post_create_authz_policy` interceptor. The (possibly modified) response returned by
        `post_create_authz_policy` will be passed to
        `post_create_authz_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_backend_authentication_config(
        self,
        request: gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_backend_authentication_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_backend_authentication_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backend_authentication_config

        DEPRECATED. Please use the `post_create_backend_authentication_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_backend_authentication_config` interceptor runs
        before the `post_create_backend_authentication_config_with_metadata` interceptor.
        """
        return response

    def post_create_backend_authentication_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_backend_authentication_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_backend_authentication_config_with_metadata`
        interceptor in new development instead of the `post_create_backend_authentication_config` interceptor.
        When both interceptors are used, this `post_create_backend_authentication_config_with_metadata` interceptor runs after the
        `post_create_backend_authentication_config` interceptor. The (possibly modified) response returned by
        `post_create_backend_authentication_config` will be passed to
        `post_create_backend_authentication_config_with_metadata`.
        """
        return response, metadata

    def pre_create_client_tls_policy(
        self,
        request: gcn_client_tls_policy.CreateClientTlsPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_client_tls_policy.CreateClientTlsPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_client_tls_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_client_tls_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_client_tls_policy

        DEPRECATED. Please use the `post_create_client_tls_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_client_tls_policy` interceptor runs
        before the `post_create_client_tls_policy_with_metadata` interceptor.
        """
        return response

    def post_create_client_tls_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_client_tls_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_client_tls_policy_with_metadata`
        interceptor in new development instead of the `post_create_client_tls_policy` interceptor.
        When both interceptors are used, this `post_create_client_tls_policy_with_metadata` interceptor runs after the
        `post_create_client_tls_policy` interceptor. The (possibly modified) response returned by
        `post_create_client_tls_policy` will be passed to
        `post_create_client_tls_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_gateway_security_policy(
        self,
        request: gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_gateway_security_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_gateway_security_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_gateway_security_policy

        DEPRECATED. Please use the `post_create_gateway_security_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_gateway_security_policy` interceptor runs
        before the `post_create_gateway_security_policy_with_metadata` interceptor.
        """
        return response

    def post_create_gateway_security_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_gateway_security_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_gateway_security_policy_with_metadata`
        interceptor in new development instead of the `post_create_gateway_security_policy` interceptor.
        When both interceptors are used, this `post_create_gateway_security_policy_with_metadata` interceptor runs after the
        `post_create_gateway_security_policy` interceptor. The (possibly modified) response returned by
        `post_create_gateway_security_policy` will be passed to
        `post_create_gateway_security_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_gateway_security_policy_rule(
        self,
        request: gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_gateway_security_policy_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_gateway_security_policy_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_gateway_security_policy_rule

        DEPRECATED. Please use the `post_create_gateway_security_policy_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_gateway_security_policy_rule` interceptor runs
        before the `post_create_gateway_security_policy_rule_with_metadata` interceptor.
        """
        return response

    def post_create_gateway_security_policy_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_gateway_security_policy_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_gateway_security_policy_rule_with_metadata`
        interceptor in new development instead of the `post_create_gateway_security_policy_rule` interceptor.
        When both interceptors are used, this `post_create_gateway_security_policy_rule_with_metadata` interceptor runs after the
        `post_create_gateway_security_policy_rule` interceptor. The (possibly modified) response returned by
        `post_create_gateway_security_policy_rule` will be passed to
        `post_create_gateway_security_policy_rule_with_metadata`.
        """
        return response, metadata

    def pre_create_server_tls_policy(
        self,
        request: gcn_server_tls_policy.CreateServerTlsPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_server_tls_policy.CreateServerTlsPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_server_tls_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_server_tls_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_server_tls_policy

        DEPRECATED. Please use the `post_create_server_tls_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_server_tls_policy` interceptor runs
        before the `post_create_server_tls_policy_with_metadata` interceptor.
        """
        return response

    def post_create_server_tls_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_server_tls_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_server_tls_policy_with_metadata`
        interceptor in new development instead of the `post_create_server_tls_policy` interceptor.
        When both interceptors are used, this `post_create_server_tls_policy_with_metadata` interceptor runs after the
        `post_create_server_tls_policy` interceptor. The (possibly modified) response returned by
        `post_create_server_tls_policy` will be passed to
        `post_create_server_tls_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_tls_inspection_policy(
        self,
        request: gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_tls_inspection_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_tls_inspection_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_tls_inspection_policy

        DEPRECATED. Please use the `post_create_tls_inspection_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_tls_inspection_policy` interceptor runs
        before the `post_create_tls_inspection_policy_with_metadata` interceptor.
        """
        return response

    def post_create_tls_inspection_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_tls_inspection_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_tls_inspection_policy_with_metadata`
        interceptor in new development instead of the `post_create_tls_inspection_policy` interceptor.
        When both interceptors are used, this `post_create_tls_inspection_policy_with_metadata` interceptor runs after the
        `post_create_tls_inspection_policy` interceptor. The (possibly modified) response returned by
        `post_create_tls_inspection_policy` will be passed to
        `post_create_tls_inspection_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_url_list(
        self,
        request: gcn_url_list.CreateUrlListRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_url_list.CreateUrlListRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_url_list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_create_url_list(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_url_list

        DEPRECATED. Please use the `post_create_url_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_create_url_list` interceptor runs
        before the `post_create_url_list_with_metadata` interceptor.
        """
        return response

    def post_create_url_list_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_url_list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_create_url_list_with_metadata`
        interceptor in new development instead of the `post_create_url_list` interceptor.
        When both interceptors are used, this `post_create_url_list_with_metadata` interceptor runs after the
        `post_create_url_list` interceptor. The (possibly modified) response returned by
        `post_create_url_list` will be passed to
        `post_create_url_list_with_metadata`.
        """
        return response, metadata

    def pre_delete_authorization_policy(
        self,
        request: authorization_policy.DeleteAuthorizationPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authorization_policy.DeleteAuthorizationPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_authorization_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_authorization_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_authorization_policy

        DEPRECATED. Please use the `post_delete_authorization_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_authorization_policy` interceptor runs
        before the `post_delete_authorization_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_authorization_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_authorization_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_authorization_policy_with_metadata`
        interceptor in new development instead of the `post_delete_authorization_policy` interceptor.
        When both interceptors are used, this `post_delete_authorization_policy_with_metadata` interceptor runs after the
        `post_delete_authorization_policy` interceptor. The (possibly modified) response returned by
        `post_delete_authorization_policy` will be passed to
        `post_delete_authorization_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_authz_policy(
        self,
        request: authz_policy.DeleteAuthzPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authz_policy.DeleteAuthzPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_authz_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_authz_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_authz_policy

        DEPRECATED. Please use the `post_delete_authz_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_authz_policy` interceptor runs
        before the `post_delete_authz_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_authz_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_authz_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_authz_policy_with_metadata`
        interceptor in new development instead of the `post_delete_authz_policy` interceptor.
        When both interceptors are used, this `post_delete_authz_policy_with_metadata` interceptor runs after the
        `post_delete_authz_policy` interceptor. The (possibly modified) response returned by
        `post_delete_authz_policy` will be passed to
        `post_delete_authz_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_backend_authentication_config(
        self,
        request: backend_authentication_config.DeleteBackendAuthenticationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backend_authentication_config.DeleteBackendAuthenticationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_backend_authentication_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_backend_authentication_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backend_authentication_config

        DEPRECATED. Please use the `post_delete_backend_authentication_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_backend_authentication_config` interceptor runs
        before the `post_delete_backend_authentication_config_with_metadata` interceptor.
        """
        return response

    def post_delete_backend_authentication_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_backend_authentication_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_backend_authentication_config_with_metadata`
        interceptor in new development instead of the `post_delete_backend_authentication_config` interceptor.
        When both interceptors are used, this `post_delete_backend_authentication_config_with_metadata` interceptor runs after the
        `post_delete_backend_authentication_config` interceptor. The (possibly modified) response returned by
        `post_delete_backend_authentication_config` will be passed to
        `post_delete_backend_authentication_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_client_tls_policy(
        self,
        request: client_tls_policy.DeleteClientTlsPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        client_tls_policy.DeleteClientTlsPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_client_tls_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_client_tls_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_client_tls_policy

        DEPRECATED. Please use the `post_delete_client_tls_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_client_tls_policy` interceptor runs
        before the `post_delete_client_tls_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_client_tls_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_client_tls_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_client_tls_policy_with_metadata`
        interceptor in new development instead of the `post_delete_client_tls_policy` interceptor.
        When both interceptors are used, this `post_delete_client_tls_policy_with_metadata` interceptor runs after the
        `post_delete_client_tls_policy` interceptor. The (possibly modified) response returned by
        `post_delete_client_tls_policy` will be passed to
        `post_delete_client_tls_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_gateway_security_policy(
        self,
        request: gateway_security_policy.DeleteGatewaySecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy.DeleteGatewaySecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_gateway_security_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_gateway_security_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_gateway_security_policy

        DEPRECATED. Please use the `post_delete_gateway_security_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_gateway_security_policy` interceptor runs
        before the `post_delete_gateway_security_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_gateway_security_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_gateway_security_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_gateway_security_policy_with_metadata`
        interceptor in new development instead of the `post_delete_gateway_security_policy` interceptor.
        When both interceptors are used, this `post_delete_gateway_security_policy_with_metadata` interceptor runs after the
        `post_delete_gateway_security_policy` interceptor. The (possibly modified) response returned by
        `post_delete_gateway_security_policy` will be passed to
        `post_delete_gateway_security_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_gateway_security_policy_rule(
        self,
        request: gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_gateway_security_policy_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_gateway_security_policy_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_gateway_security_policy_rule

        DEPRECATED. Please use the `post_delete_gateway_security_policy_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_gateway_security_policy_rule` interceptor runs
        before the `post_delete_gateway_security_policy_rule_with_metadata` interceptor.
        """
        return response

    def post_delete_gateway_security_policy_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_gateway_security_policy_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_gateway_security_policy_rule_with_metadata`
        interceptor in new development instead of the `post_delete_gateway_security_policy_rule` interceptor.
        When both interceptors are used, this `post_delete_gateway_security_policy_rule_with_metadata` interceptor runs after the
        `post_delete_gateway_security_policy_rule` interceptor. The (possibly modified) response returned by
        `post_delete_gateway_security_policy_rule` will be passed to
        `post_delete_gateway_security_policy_rule_with_metadata`.
        """
        return response, metadata

    def pre_delete_server_tls_policy(
        self,
        request: server_tls_policy.DeleteServerTlsPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        server_tls_policy.DeleteServerTlsPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_server_tls_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_server_tls_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_server_tls_policy

        DEPRECATED. Please use the `post_delete_server_tls_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_server_tls_policy` interceptor runs
        before the `post_delete_server_tls_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_server_tls_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_server_tls_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_server_tls_policy_with_metadata`
        interceptor in new development instead of the `post_delete_server_tls_policy` interceptor.
        When both interceptors are used, this `post_delete_server_tls_policy_with_metadata` interceptor runs after the
        `post_delete_server_tls_policy` interceptor. The (possibly modified) response returned by
        `post_delete_server_tls_policy` will be passed to
        `post_delete_server_tls_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_tls_inspection_policy(
        self,
        request: tls_inspection_policy.DeleteTlsInspectionPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tls_inspection_policy.DeleteTlsInspectionPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_tls_inspection_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_tls_inspection_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_tls_inspection_policy

        DEPRECATED. Please use the `post_delete_tls_inspection_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_tls_inspection_policy` interceptor runs
        before the `post_delete_tls_inspection_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_tls_inspection_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_tls_inspection_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_tls_inspection_policy_with_metadata`
        interceptor in new development instead of the `post_delete_tls_inspection_policy` interceptor.
        When both interceptors are used, this `post_delete_tls_inspection_policy_with_metadata` interceptor runs after the
        `post_delete_tls_inspection_policy` interceptor. The (possibly modified) response returned by
        `post_delete_tls_inspection_policy` will be passed to
        `post_delete_tls_inspection_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_url_list(
        self,
        request: url_list.DeleteUrlListRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[url_list.DeleteUrlListRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_url_list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_url_list(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_url_list

        DEPRECATED. Please use the `post_delete_url_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_delete_url_list` interceptor runs
        before the `post_delete_url_list_with_metadata` interceptor.
        """
        return response

    def post_delete_url_list_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_url_list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_delete_url_list_with_metadata`
        interceptor in new development instead of the `post_delete_url_list` interceptor.
        When both interceptors are used, this `post_delete_url_list_with_metadata` interceptor runs after the
        `post_delete_url_list` interceptor. The (possibly modified) response returned by
        `post_delete_url_list` will be passed to
        `post_delete_url_list_with_metadata`.
        """
        return response, metadata

    def pre_get_authorization_policy(
        self,
        request: authorization_policy.GetAuthorizationPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authorization_policy.GetAuthorizationPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_authorization_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_authorization_policy(
        self, response: authorization_policy.AuthorizationPolicy
    ) -> authorization_policy.AuthorizationPolicy:
        """Post-rpc interceptor for get_authorization_policy

        DEPRECATED. Please use the `post_get_authorization_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_authorization_policy` interceptor runs
        before the `post_get_authorization_policy_with_metadata` interceptor.
        """
        return response

    def post_get_authorization_policy_with_metadata(
        self,
        response: authorization_policy.AuthorizationPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authorization_policy.AuthorizationPolicy,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_authorization_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_authorization_policy_with_metadata`
        interceptor in new development instead of the `post_get_authorization_policy` interceptor.
        When both interceptors are used, this `post_get_authorization_policy_with_metadata` interceptor runs after the
        `post_get_authorization_policy` interceptor. The (possibly modified) response returned by
        `post_get_authorization_policy` will be passed to
        `post_get_authorization_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_authz_policy(
        self,
        request: authz_policy.GetAuthzPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authz_policy.GetAuthzPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_authz_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_authz_policy(
        self, response: authz_policy.AuthzPolicy
    ) -> authz_policy.AuthzPolicy:
        """Post-rpc interceptor for get_authz_policy

        DEPRECATED. Please use the `post_get_authz_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_authz_policy` interceptor runs
        before the `post_get_authz_policy_with_metadata` interceptor.
        """
        return response

    def post_get_authz_policy_with_metadata(
        self,
        response: authz_policy.AuthzPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authz_policy.AuthzPolicy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_authz_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_authz_policy_with_metadata`
        interceptor in new development instead of the `post_get_authz_policy` interceptor.
        When both interceptors are used, this `post_get_authz_policy_with_metadata` interceptor runs after the
        `post_get_authz_policy` interceptor. The (possibly modified) response returned by
        `post_get_authz_policy` will be passed to
        `post_get_authz_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_backend_authentication_config(
        self,
        request: backend_authentication_config.GetBackendAuthenticationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backend_authentication_config.GetBackendAuthenticationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_backend_authentication_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_backend_authentication_config(
        self, response: backend_authentication_config.BackendAuthenticationConfig
    ) -> backend_authentication_config.BackendAuthenticationConfig:
        """Post-rpc interceptor for get_backend_authentication_config

        DEPRECATED. Please use the `post_get_backend_authentication_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_backend_authentication_config` interceptor runs
        before the `post_get_backend_authentication_config_with_metadata` interceptor.
        """
        return response

    def post_get_backend_authentication_config_with_metadata(
        self,
        response: backend_authentication_config.BackendAuthenticationConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backend_authentication_config.BackendAuthenticationConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_backend_authentication_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_backend_authentication_config_with_metadata`
        interceptor in new development instead of the `post_get_backend_authentication_config` interceptor.
        When both interceptors are used, this `post_get_backend_authentication_config_with_metadata` interceptor runs after the
        `post_get_backend_authentication_config` interceptor. The (possibly modified) response returned by
        `post_get_backend_authentication_config` will be passed to
        `post_get_backend_authentication_config_with_metadata`.
        """
        return response, metadata

    def pre_get_client_tls_policy(
        self,
        request: client_tls_policy.GetClientTlsPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        client_tls_policy.GetClientTlsPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_client_tls_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_client_tls_policy(
        self, response: client_tls_policy.ClientTlsPolicy
    ) -> client_tls_policy.ClientTlsPolicy:
        """Post-rpc interceptor for get_client_tls_policy

        DEPRECATED. Please use the `post_get_client_tls_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_client_tls_policy` interceptor runs
        before the `post_get_client_tls_policy_with_metadata` interceptor.
        """
        return response

    def post_get_client_tls_policy_with_metadata(
        self,
        response: client_tls_policy.ClientTlsPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        client_tls_policy.ClientTlsPolicy, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_client_tls_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_client_tls_policy_with_metadata`
        interceptor in new development instead of the `post_get_client_tls_policy` interceptor.
        When both interceptors are used, this `post_get_client_tls_policy_with_metadata` interceptor runs after the
        `post_get_client_tls_policy` interceptor. The (possibly modified) response returned by
        `post_get_client_tls_policy` will be passed to
        `post_get_client_tls_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_gateway_security_policy(
        self,
        request: gateway_security_policy.GetGatewaySecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy.GetGatewaySecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_gateway_security_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_gateway_security_policy(
        self, response: gateway_security_policy.GatewaySecurityPolicy
    ) -> gateway_security_policy.GatewaySecurityPolicy:
        """Post-rpc interceptor for get_gateway_security_policy

        DEPRECATED. Please use the `post_get_gateway_security_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_gateway_security_policy` interceptor runs
        before the `post_get_gateway_security_policy_with_metadata` interceptor.
        """
        return response

    def post_get_gateway_security_policy_with_metadata(
        self,
        response: gateway_security_policy.GatewaySecurityPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy.GatewaySecurityPolicy,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_gateway_security_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_gateway_security_policy_with_metadata`
        interceptor in new development instead of the `post_get_gateway_security_policy` interceptor.
        When both interceptors are used, this `post_get_gateway_security_policy_with_metadata` interceptor runs after the
        `post_get_gateway_security_policy` interceptor. The (possibly modified) response returned by
        `post_get_gateway_security_policy` will be passed to
        `post_get_gateway_security_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_gateway_security_policy_rule(
        self,
        request: gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_gateway_security_policy_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_gateway_security_policy_rule(
        self, response: gateway_security_policy_rule.GatewaySecurityPolicyRule
    ) -> gateway_security_policy_rule.GatewaySecurityPolicyRule:
        """Post-rpc interceptor for get_gateway_security_policy_rule

        DEPRECATED. Please use the `post_get_gateway_security_policy_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_gateway_security_policy_rule` interceptor runs
        before the `post_get_gateway_security_policy_rule_with_metadata` interceptor.
        """
        return response

    def post_get_gateway_security_policy_rule_with_metadata(
        self,
        response: gateway_security_policy_rule.GatewaySecurityPolicyRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy_rule.GatewaySecurityPolicyRule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_gateway_security_policy_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_gateway_security_policy_rule_with_metadata`
        interceptor in new development instead of the `post_get_gateway_security_policy_rule` interceptor.
        When both interceptors are used, this `post_get_gateway_security_policy_rule_with_metadata` interceptor runs after the
        `post_get_gateway_security_policy_rule` interceptor. The (possibly modified) response returned by
        `post_get_gateway_security_policy_rule` will be passed to
        `post_get_gateway_security_policy_rule_with_metadata`.
        """
        return response, metadata

    def pre_get_server_tls_policy(
        self,
        request: server_tls_policy.GetServerTlsPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        server_tls_policy.GetServerTlsPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_server_tls_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_server_tls_policy(
        self, response: server_tls_policy.ServerTlsPolicy
    ) -> server_tls_policy.ServerTlsPolicy:
        """Post-rpc interceptor for get_server_tls_policy

        DEPRECATED. Please use the `post_get_server_tls_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_server_tls_policy` interceptor runs
        before the `post_get_server_tls_policy_with_metadata` interceptor.
        """
        return response

    def post_get_server_tls_policy_with_metadata(
        self,
        response: server_tls_policy.ServerTlsPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        server_tls_policy.ServerTlsPolicy, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_server_tls_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_server_tls_policy_with_metadata`
        interceptor in new development instead of the `post_get_server_tls_policy` interceptor.
        When both interceptors are used, this `post_get_server_tls_policy_with_metadata` interceptor runs after the
        `post_get_server_tls_policy` interceptor. The (possibly modified) response returned by
        `post_get_server_tls_policy` will be passed to
        `post_get_server_tls_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_tls_inspection_policy(
        self,
        request: tls_inspection_policy.GetTlsInspectionPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tls_inspection_policy.GetTlsInspectionPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_tls_inspection_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_tls_inspection_policy(
        self, response: tls_inspection_policy.TlsInspectionPolicy
    ) -> tls_inspection_policy.TlsInspectionPolicy:
        """Post-rpc interceptor for get_tls_inspection_policy

        DEPRECATED. Please use the `post_get_tls_inspection_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_tls_inspection_policy` interceptor runs
        before the `post_get_tls_inspection_policy_with_metadata` interceptor.
        """
        return response

    def post_get_tls_inspection_policy_with_metadata(
        self,
        response: tls_inspection_policy.TlsInspectionPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tls_inspection_policy.TlsInspectionPolicy,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_tls_inspection_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_tls_inspection_policy_with_metadata`
        interceptor in new development instead of the `post_get_tls_inspection_policy` interceptor.
        When both interceptors are used, this `post_get_tls_inspection_policy_with_metadata` interceptor runs after the
        `post_get_tls_inspection_policy` interceptor. The (possibly modified) response returned by
        `post_get_tls_inspection_policy` will be passed to
        `post_get_tls_inspection_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_url_list(
        self,
        request: url_list.GetUrlListRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[url_list.GetUrlListRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_url_list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_url_list(self, response: url_list.UrlList) -> url_list.UrlList:
        """Post-rpc interceptor for get_url_list

        DEPRECATED. Please use the `post_get_url_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_get_url_list` interceptor runs
        before the `post_get_url_list_with_metadata` interceptor.
        """
        return response

    def post_get_url_list_with_metadata(
        self,
        response: url_list.UrlList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[url_list.UrlList, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_url_list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_get_url_list_with_metadata`
        interceptor in new development instead of the `post_get_url_list` interceptor.
        When both interceptors are used, this `post_get_url_list_with_metadata` interceptor runs after the
        `post_get_url_list` interceptor. The (possibly modified) response returned by
        `post_get_url_list` will be passed to
        `post_get_url_list_with_metadata`.
        """
        return response, metadata

    def pre_list_authorization_policies(
        self,
        request: authorization_policy.ListAuthorizationPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authorization_policy.ListAuthorizationPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_authorization_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_authorization_policies(
        self, response: authorization_policy.ListAuthorizationPoliciesResponse
    ) -> authorization_policy.ListAuthorizationPoliciesResponse:
        """Post-rpc interceptor for list_authorization_policies

        DEPRECATED. Please use the `post_list_authorization_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_authorization_policies` interceptor runs
        before the `post_list_authorization_policies_with_metadata` interceptor.
        """
        return response

    def post_list_authorization_policies_with_metadata(
        self,
        response: authorization_policy.ListAuthorizationPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authorization_policy.ListAuthorizationPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_authorization_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_authorization_policies_with_metadata`
        interceptor in new development instead of the `post_list_authorization_policies` interceptor.
        When both interceptors are used, this `post_list_authorization_policies_with_metadata` interceptor runs after the
        `post_list_authorization_policies` interceptor. The (possibly modified) response returned by
        `post_list_authorization_policies` will be passed to
        `post_list_authorization_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_authz_policies(
        self,
        request: authz_policy.ListAuthzPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authz_policy.ListAuthzPoliciesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_authz_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_authz_policies(
        self, response: authz_policy.ListAuthzPoliciesResponse
    ) -> authz_policy.ListAuthzPoliciesResponse:
        """Post-rpc interceptor for list_authz_policies

        DEPRECATED. Please use the `post_list_authz_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_authz_policies` interceptor runs
        before the `post_list_authz_policies_with_metadata` interceptor.
        """
        return response

    def post_list_authz_policies_with_metadata(
        self,
        response: authz_policy.ListAuthzPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authz_policy.ListAuthzPoliciesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_authz_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_authz_policies_with_metadata`
        interceptor in new development instead of the `post_list_authz_policies` interceptor.
        When both interceptors are used, this `post_list_authz_policies_with_metadata` interceptor runs after the
        `post_list_authz_policies` interceptor. The (possibly modified) response returned by
        `post_list_authz_policies` will be passed to
        `post_list_authz_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_backend_authentication_configs(
        self,
        request: backend_authentication_config.ListBackendAuthenticationConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backend_authentication_config.ListBackendAuthenticationConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_backend_authentication_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_backend_authentication_configs(
        self,
        response: backend_authentication_config.ListBackendAuthenticationConfigsResponse,
    ) -> backend_authentication_config.ListBackendAuthenticationConfigsResponse:
        """Post-rpc interceptor for list_backend_authentication_configs

        DEPRECATED. Please use the `post_list_backend_authentication_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_backend_authentication_configs` interceptor runs
        before the `post_list_backend_authentication_configs_with_metadata` interceptor.
        """
        return response

    def post_list_backend_authentication_configs_with_metadata(
        self,
        response: backend_authentication_config.ListBackendAuthenticationConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backend_authentication_config.ListBackendAuthenticationConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_backend_authentication_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_backend_authentication_configs_with_metadata`
        interceptor in new development instead of the `post_list_backend_authentication_configs` interceptor.
        When both interceptors are used, this `post_list_backend_authentication_configs_with_metadata` interceptor runs after the
        `post_list_backend_authentication_configs` interceptor. The (possibly modified) response returned by
        `post_list_backend_authentication_configs` will be passed to
        `post_list_backend_authentication_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_client_tls_policies(
        self,
        request: client_tls_policy.ListClientTlsPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        client_tls_policy.ListClientTlsPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_client_tls_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_client_tls_policies(
        self, response: client_tls_policy.ListClientTlsPoliciesResponse
    ) -> client_tls_policy.ListClientTlsPoliciesResponse:
        """Post-rpc interceptor for list_client_tls_policies

        DEPRECATED. Please use the `post_list_client_tls_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_client_tls_policies` interceptor runs
        before the `post_list_client_tls_policies_with_metadata` interceptor.
        """
        return response

    def post_list_client_tls_policies_with_metadata(
        self,
        response: client_tls_policy.ListClientTlsPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        client_tls_policy.ListClientTlsPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_client_tls_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_client_tls_policies_with_metadata`
        interceptor in new development instead of the `post_list_client_tls_policies` interceptor.
        When both interceptors are used, this `post_list_client_tls_policies_with_metadata` interceptor runs after the
        `post_list_client_tls_policies` interceptor. The (possibly modified) response returned by
        `post_list_client_tls_policies` will be passed to
        `post_list_client_tls_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_gateway_security_policies(
        self,
        request: gateway_security_policy.ListGatewaySecurityPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy.ListGatewaySecurityPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_gateway_security_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_gateway_security_policies(
        self, response: gateway_security_policy.ListGatewaySecurityPoliciesResponse
    ) -> gateway_security_policy.ListGatewaySecurityPoliciesResponse:
        """Post-rpc interceptor for list_gateway_security_policies

        DEPRECATED. Please use the `post_list_gateway_security_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_gateway_security_policies` interceptor runs
        before the `post_list_gateway_security_policies_with_metadata` interceptor.
        """
        return response

    def post_list_gateway_security_policies_with_metadata(
        self,
        response: gateway_security_policy.ListGatewaySecurityPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy.ListGatewaySecurityPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_gateway_security_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_gateway_security_policies_with_metadata`
        interceptor in new development instead of the `post_list_gateway_security_policies` interceptor.
        When both interceptors are used, this `post_list_gateway_security_policies_with_metadata` interceptor runs after the
        `post_list_gateway_security_policies` interceptor. The (possibly modified) response returned by
        `post_list_gateway_security_policies` will be passed to
        `post_list_gateway_security_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_gateway_security_policy_rules(
        self,
        request: gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_gateway_security_policy_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_gateway_security_policy_rules(
        self,
        response: gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse,
    ) -> gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse:
        """Post-rpc interceptor for list_gateway_security_policy_rules

        DEPRECATED. Please use the `post_list_gateway_security_policy_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_gateway_security_policy_rules` interceptor runs
        before the `post_list_gateway_security_policy_rules_with_metadata` interceptor.
        """
        return response

    def post_list_gateway_security_policy_rules_with_metadata(
        self,
        response: gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_gateway_security_policy_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_gateway_security_policy_rules_with_metadata`
        interceptor in new development instead of the `post_list_gateway_security_policy_rules` interceptor.
        When both interceptors are used, this `post_list_gateway_security_policy_rules_with_metadata` interceptor runs after the
        `post_list_gateway_security_policy_rules` interceptor. The (possibly modified) response returned by
        `post_list_gateway_security_policy_rules` will be passed to
        `post_list_gateway_security_policy_rules_with_metadata`.
        """
        return response, metadata

    def pre_list_server_tls_policies(
        self,
        request: server_tls_policy.ListServerTlsPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        server_tls_policy.ListServerTlsPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_server_tls_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_server_tls_policies(
        self, response: server_tls_policy.ListServerTlsPoliciesResponse
    ) -> server_tls_policy.ListServerTlsPoliciesResponse:
        """Post-rpc interceptor for list_server_tls_policies

        DEPRECATED. Please use the `post_list_server_tls_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_server_tls_policies` interceptor runs
        before the `post_list_server_tls_policies_with_metadata` interceptor.
        """
        return response

    def post_list_server_tls_policies_with_metadata(
        self,
        response: server_tls_policy.ListServerTlsPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        server_tls_policy.ListServerTlsPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_server_tls_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_server_tls_policies_with_metadata`
        interceptor in new development instead of the `post_list_server_tls_policies` interceptor.
        When both interceptors are used, this `post_list_server_tls_policies_with_metadata` interceptor runs after the
        `post_list_server_tls_policies` interceptor. The (possibly modified) response returned by
        `post_list_server_tls_policies` will be passed to
        `post_list_server_tls_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_tls_inspection_policies(
        self,
        request: tls_inspection_policy.ListTlsInspectionPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tls_inspection_policy.ListTlsInspectionPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_tls_inspection_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_tls_inspection_policies(
        self, response: tls_inspection_policy.ListTlsInspectionPoliciesResponse
    ) -> tls_inspection_policy.ListTlsInspectionPoliciesResponse:
        """Post-rpc interceptor for list_tls_inspection_policies

        DEPRECATED. Please use the `post_list_tls_inspection_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_tls_inspection_policies` interceptor runs
        before the `post_list_tls_inspection_policies_with_metadata` interceptor.
        """
        return response

    def post_list_tls_inspection_policies_with_metadata(
        self,
        response: tls_inspection_policy.ListTlsInspectionPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tls_inspection_policy.ListTlsInspectionPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_tls_inspection_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_tls_inspection_policies_with_metadata`
        interceptor in new development instead of the `post_list_tls_inspection_policies` interceptor.
        When both interceptors are used, this `post_list_tls_inspection_policies_with_metadata` interceptor runs after the
        `post_list_tls_inspection_policies` interceptor. The (possibly modified) response returned by
        `post_list_tls_inspection_policies` will be passed to
        `post_list_tls_inspection_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_url_lists(
        self,
        request: url_list.ListUrlListsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[url_list.ListUrlListsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_url_lists

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_url_lists(
        self, response: url_list.ListUrlListsResponse
    ) -> url_list.ListUrlListsResponse:
        """Post-rpc interceptor for list_url_lists

        DEPRECATED. Please use the `post_list_url_lists_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_list_url_lists` interceptor runs
        before the `post_list_url_lists_with_metadata` interceptor.
        """
        return response

    def post_list_url_lists_with_metadata(
        self,
        response: url_list.ListUrlListsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[url_list.ListUrlListsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_url_lists

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_list_url_lists_with_metadata`
        interceptor in new development instead of the `post_list_url_lists` interceptor.
        When both interceptors are used, this `post_list_url_lists_with_metadata` interceptor runs after the
        `post_list_url_lists` interceptor. The (possibly modified) response returned by
        `post_list_url_lists` will be passed to
        `post_list_url_lists_with_metadata`.
        """
        return response, metadata

    def pre_update_authorization_policy(
        self,
        request: gcn_authorization_policy.UpdateAuthorizationPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_authorization_policy.UpdateAuthorizationPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_authorization_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_authorization_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_authorization_policy

        DEPRECATED. Please use the `post_update_authorization_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_authorization_policy` interceptor runs
        before the `post_update_authorization_policy_with_metadata` interceptor.
        """
        return response

    def post_update_authorization_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_authorization_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_authorization_policy_with_metadata`
        interceptor in new development instead of the `post_update_authorization_policy` interceptor.
        When both interceptors are used, this `post_update_authorization_policy_with_metadata` interceptor runs after the
        `post_update_authorization_policy` interceptor. The (possibly modified) response returned by
        `post_update_authorization_policy` will be passed to
        `post_update_authorization_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_authz_policy(
        self,
        request: gcn_authz_policy.UpdateAuthzPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_authz_policy.UpdateAuthzPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_authz_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_authz_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_authz_policy

        DEPRECATED. Please use the `post_update_authz_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_authz_policy` interceptor runs
        before the `post_update_authz_policy_with_metadata` interceptor.
        """
        return response

    def post_update_authz_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_authz_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_authz_policy_with_metadata`
        interceptor in new development instead of the `post_update_authz_policy` interceptor.
        When both interceptors are used, this `post_update_authz_policy_with_metadata` interceptor runs after the
        `post_update_authz_policy` interceptor. The (possibly modified) response returned by
        `post_update_authz_policy` will be passed to
        `post_update_authz_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_backend_authentication_config(
        self,
        request: gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_backend_authentication_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_backend_authentication_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backend_authentication_config

        DEPRECATED. Please use the `post_update_backend_authentication_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_backend_authentication_config` interceptor runs
        before the `post_update_backend_authentication_config_with_metadata` interceptor.
        """
        return response

    def post_update_backend_authentication_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_backend_authentication_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_backend_authentication_config_with_metadata`
        interceptor in new development instead of the `post_update_backend_authentication_config` interceptor.
        When both interceptors are used, this `post_update_backend_authentication_config_with_metadata` interceptor runs after the
        `post_update_backend_authentication_config` interceptor. The (possibly modified) response returned by
        `post_update_backend_authentication_config` will be passed to
        `post_update_backend_authentication_config_with_metadata`.
        """
        return response, metadata

    def pre_update_client_tls_policy(
        self,
        request: gcn_client_tls_policy.UpdateClientTlsPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_client_tls_policy.UpdateClientTlsPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_client_tls_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_client_tls_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_client_tls_policy

        DEPRECATED. Please use the `post_update_client_tls_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_client_tls_policy` interceptor runs
        before the `post_update_client_tls_policy_with_metadata` interceptor.
        """
        return response

    def post_update_client_tls_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_client_tls_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_client_tls_policy_with_metadata`
        interceptor in new development instead of the `post_update_client_tls_policy` interceptor.
        When both interceptors are used, this `post_update_client_tls_policy_with_metadata` interceptor runs after the
        `post_update_client_tls_policy` interceptor. The (possibly modified) response returned by
        `post_update_client_tls_policy` will be passed to
        `post_update_client_tls_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_gateway_security_policy(
        self,
        request: gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_gateway_security_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_gateway_security_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_gateway_security_policy

        DEPRECATED. Please use the `post_update_gateway_security_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_gateway_security_policy` interceptor runs
        before the `post_update_gateway_security_policy_with_metadata` interceptor.
        """
        return response

    def post_update_gateway_security_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_gateway_security_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_gateway_security_policy_with_metadata`
        interceptor in new development instead of the `post_update_gateway_security_policy` interceptor.
        When both interceptors are used, this `post_update_gateway_security_policy_with_metadata` interceptor runs after the
        `post_update_gateway_security_policy` interceptor. The (possibly modified) response returned by
        `post_update_gateway_security_policy` will be passed to
        `post_update_gateway_security_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_gateway_security_policy_rule(
        self,
        request: gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_gateway_security_policy_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_gateway_security_policy_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_gateway_security_policy_rule

        DEPRECATED. Please use the `post_update_gateway_security_policy_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_gateway_security_policy_rule` interceptor runs
        before the `post_update_gateway_security_policy_rule_with_metadata` interceptor.
        """
        return response

    def post_update_gateway_security_policy_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_gateway_security_policy_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_gateway_security_policy_rule_with_metadata`
        interceptor in new development instead of the `post_update_gateway_security_policy_rule` interceptor.
        When both interceptors are used, this `post_update_gateway_security_policy_rule_with_metadata` interceptor runs after the
        `post_update_gateway_security_policy_rule` interceptor. The (possibly modified) response returned by
        `post_update_gateway_security_policy_rule` will be passed to
        `post_update_gateway_security_policy_rule_with_metadata`.
        """
        return response, metadata

    def pre_update_server_tls_policy(
        self,
        request: gcn_server_tls_policy.UpdateServerTlsPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_server_tls_policy.UpdateServerTlsPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_server_tls_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_server_tls_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_server_tls_policy

        DEPRECATED. Please use the `post_update_server_tls_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_server_tls_policy` interceptor runs
        before the `post_update_server_tls_policy_with_metadata` interceptor.
        """
        return response

    def post_update_server_tls_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_server_tls_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_server_tls_policy_with_metadata`
        interceptor in new development instead of the `post_update_server_tls_policy` interceptor.
        When both interceptors are used, this `post_update_server_tls_policy_with_metadata` interceptor runs after the
        `post_update_server_tls_policy` interceptor. The (possibly modified) response returned by
        `post_update_server_tls_policy` will be passed to
        `post_update_server_tls_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_tls_inspection_policy(
        self,
        request: gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_tls_inspection_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_tls_inspection_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_tls_inspection_policy

        DEPRECATED. Please use the `post_update_tls_inspection_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_tls_inspection_policy` interceptor runs
        before the `post_update_tls_inspection_policy_with_metadata` interceptor.
        """
        return response

    def post_update_tls_inspection_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_tls_inspection_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_tls_inspection_policy_with_metadata`
        interceptor in new development instead of the `post_update_tls_inspection_policy` interceptor.
        When both interceptors are used, this `post_update_tls_inspection_policy_with_metadata` interceptor runs after the
        `post_update_tls_inspection_policy` interceptor. The (possibly modified) response returned by
        `post_update_tls_inspection_policy` will be passed to
        `post_update_tls_inspection_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_url_list(
        self,
        request: gcn_url_list.UpdateUrlListRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_url_list.UpdateUrlListRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_url_list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_update_url_list(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_url_list

        DEPRECATED. Please use the `post_update_url_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code. This `post_update_url_list` interceptor runs
        before the `post_update_url_list_with_metadata` interceptor.
        """
        return response

    def post_update_url_list_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_url_list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkSecurity server but before it is returned to user code.

        We recommend only using this `post_update_url_list_with_metadata`
        interceptor in new development instead of the `post_update_url_list` interceptor.
        When both interceptors are used, this `post_update_url_list_with_metadata` interceptor runs after the
        `post_update_url_list` interceptor. The (possibly modified) response returned by
        `post_update_url_list` will be passed to
        `post_update_url_list_with_metadata`.
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
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
        before they are sent to the NetworkSecurity server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the NetworkSecurity server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class NetworkSecurityRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: NetworkSecurityRestInterceptor


class NetworkSecurityRestTransport(_BaseNetworkSecurityRestTransport):
    """REST backend synchronous transport for NetworkSecurity.

    Network Security API provides resources to configure
    authentication and authorization policies. Refer to per API
    resource documentation for more information.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "networksecurity.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[NetworkSecurityRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'networksecurity.googleapis.com').
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
            interceptor (Optional[NetworkSecurityRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or NetworkSecurityRestInterceptor()
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
                    {
                        "method": "post",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*}/operations",
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

    class _CreateAuthorizationPolicy(
        _BaseNetworkSecurityRestTransport._BaseCreateAuthorizationPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CreateAuthorizationPolicy")

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
            request: gcn_authorization_policy.CreateAuthorizationPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create authorization
            policy method over HTTP.

                Args:
                    request (~.gcn_authorization_policy.CreateAuthorizationPolicyRequest):
                        The request object. Request used by the
                    CreateAuthorizationPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseCreateAuthorizationPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_authorization_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateAuthorizationPolicy,
                    "_BaseCreateAuthorizationPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateAuthorizationPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateAuthorizationPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._CreateAuthorizationPolicy._get_response(
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

            resp = self._interceptor.post_create_authorization_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_authorization_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_authorization_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateAuthorizationPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAuthzPolicy(
        _BaseNetworkSecurityRestTransport._BaseCreateAuthzPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CreateAuthzPolicy")

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
            request: gcn_authz_policy.CreateAuthzPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create authz policy method over HTTP.

            Args:
                request (~.gcn_authz_policy.CreateAuthzPolicyRequest):
                    The request object. Message for creating an ``AuthzPolicy`` resource.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseCreateAuthzPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_authz_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateAuthzPolicy,
                    "_BaseCreateAuthzPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateAuthzPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateAuthzPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._CreateAuthzPolicy._get_response(
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

            resp = self._interceptor.post_create_authz_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_authz_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_authz_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateAuthzPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackendAuthenticationConfig(
        _BaseNetworkSecurityRestTransport._BaseCreateBackendAuthenticationConfig,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash(
                "NetworkSecurityRestTransport.CreateBackendAuthenticationConfig"
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
                data=body,
            )
            return response

        def __call__(
            self,
            request: gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backend
            authentication config method over HTTP.

                Args:
                    request (~.gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest):
                        The request object. Request used by the
                    CreateBackendAuthenticationConfig
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

            http_options = _BaseNetworkSecurityRestTransport._BaseCreateBackendAuthenticationConfig._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_backend_authentication_config(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateBackendAuthenticationConfig,
                    "_BaseCreateBackendAuthenticationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateBackendAuthenticationConfig",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateBackendAuthenticationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._CreateBackendAuthenticationConfig._get_response(
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

            resp = self._interceptor.post_create_backend_authentication_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_backend_authentication_config_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_backend_authentication_config",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateBackendAuthenticationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateClientTlsPolicy(
        _BaseNetworkSecurityRestTransport._BaseCreateClientTlsPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CreateClientTlsPolicy")

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
            request: gcn_client_tls_policy.CreateClientTlsPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create client tls policy method over HTTP.

            Args:
                request (~.gcn_client_tls_policy.CreateClientTlsPolicyRequest):
                    The request object. Request used by the
                CreateClientTlsPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseCreateClientTlsPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_client_tls_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateClientTlsPolicy,
                    "_BaseCreateClientTlsPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateClientTlsPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateClientTlsPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._CreateClientTlsPolicy._get_response(
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

            resp = self._interceptor.post_create_client_tls_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_client_tls_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_client_tls_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateClientTlsPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGatewaySecurityPolicy(
        _BaseNetworkSecurityRestTransport._BaseCreateGatewaySecurityPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CreateGatewaySecurityPolicy")

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
            request: gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create gateway security
            policy method over HTTP.

                Args:
                    request (~.gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest):
                        The request object. Request used by the
                    CreateGatewaySecurityPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseCreateGatewaySecurityPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_gateway_security_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateGatewaySecurityPolicy,
                    "_BaseCreateGatewaySecurityPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateGatewaySecurityPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateGatewaySecurityPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._CreateGatewaySecurityPolicy._get_response(
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

            resp = self._interceptor.post_create_gateway_security_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_gateway_security_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_gateway_security_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateGatewaySecurityPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGatewaySecurityPolicyRule(
        _BaseNetworkSecurityRestTransport._BaseCreateGatewaySecurityPolicyRule,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CreateGatewaySecurityPolicyRule")

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
            request: gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create gateway security
            policy rule method over HTTP.

                Args:
                    request (~.gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest):
                        The request object. Methods for GatewaySecurityPolicy
                    RULES/GatewaySecurityPolicyRules.
                    Request used by the
                    CreateGatewaySecurityPolicyRule method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseCreateGatewaySecurityPolicyRule._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_gateway_security_policy_rule(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateGatewaySecurityPolicyRule,
                    "_BaseCreateGatewaySecurityPolicyRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateGatewaySecurityPolicyRule",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateGatewaySecurityPolicyRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._CreateGatewaySecurityPolicyRule._get_response(
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

            resp = self._interceptor.post_create_gateway_security_policy_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_gateway_security_policy_rule_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_gateway_security_policy_rule",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateGatewaySecurityPolicyRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateServerTlsPolicy(
        _BaseNetworkSecurityRestTransport._BaseCreateServerTlsPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CreateServerTlsPolicy")

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
            request: gcn_server_tls_policy.CreateServerTlsPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create server tls policy method over HTTP.

            Args:
                request (~.gcn_server_tls_policy.CreateServerTlsPolicyRequest):
                    The request object. Request used by the
                CreateServerTlsPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseCreateServerTlsPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_server_tls_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateServerTlsPolicy,
                    "_BaseCreateServerTlsPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateServerTlsPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateServerTlsPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._CreateServerTlsPolicy._get_response(
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

            resp = self._interceptor.post_create_server_tls_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_server_tls_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_server_tls_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateServerTlsPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTlsInspectionPolicy(
        _BaseNetworkSecurityRestTransport._BaseCreateTlsInspectionPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CreateTlsInspectionPolicy")

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
            request: gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create tls inspection
            policy method over HTTP.

                Args:
                    request (~.gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest):
                        The request object. Request used by the
                    CreateTlsInspectionPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseCreateTlsInspectionPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_tls_inspection_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateTlsInspectionPolicy,
                    "_BaseCreateTlsInspectionPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateTlsInspectionPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateTlsInspectionPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._CreateTlsInspectionPolicy._get_response(
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

            resp = self._interceptor.post_create_tls_inspection_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_tls_inspection_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_tls_inspection_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateTlsInspectionPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUrlList(
        _BaseNetworkSecurityRestTransport._BaseCreateUrlList, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CreateUrlList")

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
            request: gcn_url_list.CreateUrlListRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create url list method over HTTP.

            Args:
                request (~.gcn_url_list.CreateUrlListRequest):
                    The request object. Request used by the CreateUrlList
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
                _BaseNetworkSecurityRestTransport._BaseCreateUrlList._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_url_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCreateUrlList,
                    "_BaseCreateUrlList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CreateUrlList",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateUrlList",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._CreateUrlList._get_response(
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

            resp = self._interceptor.post_create_url_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_url_list_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.create_url_list",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CreateUrlList",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAuthorizationPolicy(
        _BaseNetworkSecurityRestTransport._BaseDeleteAuthorizationPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteAuthorizationPolicy")

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
            request: authorization_policy.DeleteAuthorizationPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete authorization
            policy method over HTTP.

                Args:
                    request (~.authorization_policy.DeleteAuthorizationPolicyRequest):
                        The request object. Request used by the
                    DeleteAuthorizationPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteAuthorizationPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_authorization_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteAuthorizationPolicy,
                    "_BaseDeleteAuthorizationPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteAuthorizationPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteAuthorizationPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._DeleteAuthorizationPolicy._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_authorization_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_authorization_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_authorization_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteAuthorizationPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAuthzPolicy(
        _BaseNetworkSecurityRestTransport._BaseDeleteAuthzPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteAuthzPolicy")

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
            request: authz_policy.DeleteAuthzPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete authz policy method over HTTP.

            Args:
                request (~.authz_policy.DeleteAuthzPolicyRequest):
                    The request object. Message for deleting an ``AuthzPolicy`` resource.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteAuthzPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_authz_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteAuthzPolicy,
                    "_BaseDeleteAuthzPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteAuthzPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteAuthzPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._DeleteAuthzPolicy._get_response(
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

            resp = self._interceptor.post_delete_authz_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_authz_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_authz_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteAuthzPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackendAuthenticationConfig(
        _BaseNetworkSecurityRestTransport._BaseDeleteBackendAuthenticationConfig,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash(
                "NetworkSecurityRestTransport.DeleteBackendAuthenticationConfig"
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
            request: backend_authentication_config.DeleteBackendAuthenticationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backend
            authentication config method over HTTP.

                Args:
                    request (~.backend_authentication_config.DeleteBackendAuthenticationConfigRequest):
                        The request object. Request used by the
                    DeleteBackendAuthenticationConfig
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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteBackendAuthenticationConfig._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_backend_authentication_config(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteBackendAuthenticationConfig,
                    "_BaseDeleteBackendAuthenticationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteBackendAuthenticationConfig",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteBackendAuthenticationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._DeleteBackendAuthenticationConfig._get_response(
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

            resp = self._interceptor.post_delete_backend_authentication_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_backend_authentication_config_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_backend_authentication_config",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteBackendAuthenticationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteClientTlsPolicy(
        _BaseNetworkSecurityRestTransport._BaseDeleteClientTlsPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteClientTlsPolicy")

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
            request: client_tls_policy.DeleteClientTlsPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete client tls policy method over HTTP.

            Args:
                request (~.client_tls_policy.DeleteClientTlsPolicyRequest):
                    The request object. Request used by the
                DeleteClientTlsPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteClientTlsPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_client_tls_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteClientTlsPolicy,
                    "_BaseDeleteClientTlsPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteClientTlsPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteClientTlsPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._DeleteClientTlsPolicy._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_client_tls_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_client_tls_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_client_tls_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteClientTlsPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGatewaySecurityPolicy(
        _BaseNetworkSecurityRestTransport._BaseDeleteGatewaySecurityPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteGatewaySecurityPolicy")

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
            request: gateway_security_policy.DeleteGatewaySecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete gateway security
            policy method over HTTP.

                Args:
                    request (~.gateway_security_policy.DeleteGatewaySecurityPolicyRequest):
                        The request object. Request used by the
                    DeleteGatewaySecurityPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteGatewaySecurityPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_gateway_security_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteGatewaySecurityPolicy,
                    "_BaseDeleteGatewaySecurityPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteGatewaySecurityPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteGatewaySecurityPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._DeleteGatewaySecurityPolicy._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_gateway_security_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_gateway_security_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_gateway_security_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteGatewaySecurityPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGatewaySecurityPolicyRule(
        _BaseNetworkSecurityRestTransport._BaseDeleteGatewaySecurityPolicyRule,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteGatewaySecurityPolicyRule")

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
            request: gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete gateway security
            policy rule method over HTTP.

                Args:
                    request (~.gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest):
                        The request object. Request used by the
                    DeleteGatewaySecurityPolicyRule method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteGatewaySecurityPolicyRule._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_gateway_security_policy_rule(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteGatewaySecurityPolicyRule,
                    "_BaseDeleteGatewaySecurityPolicyRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteGatewaySecurityPolicyRule",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteGatewaySecurityPolicyRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._DeleteGatewaySecurityPolicyRule._get_response(
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

            resp = self._interceptor.post_delete_gateway_security_policy_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_gateway_security_policy_rule_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_gateway_security_policy_rule",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteGatewaySecurityPolicyRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteServerTlsPolicy(
        _BaseNetworkSecurityRestTransport._BaseDeleteServerTlsPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteServerTlsPolicy")

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
            request: server_tls_policy.DeleteServerTlsPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete server tls policy method over HTTP.

            Args:
                request (~.server_tls_policy.DeleteServerTlsPolicyRequest):
                    The request object. Request used by the
                DeleteServerTlsPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteServerTlsPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_server_tls_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteServerTlsPolicy,
                    "_BaseDeleteServerTlsPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteServerTlsPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteServerTlsPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._DeleteServerTlsPolicy._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_server_tls_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_server_tls_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_server_tls_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteServerTlsPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTlsInspectionPolicy(
        _BaseNetworkSecurityRestTransport._BaseDeleteTlsInspectionPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteTlsInspectionPolicy")

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
            request: tls_inspection_policy.DeleteTlsInspectionPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete tls inspection
            policy method over HTTP.

                Args:
                    request (~.tls_inspection_policy.DeleteTlsInspectionPolicyRequest):
                        The request object. Request used by the
                    DeleteTlsInspectionPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteTlsInspectionPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_tls_inspection_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteTlsInspectionPolicy,
                    "_BaseDeleteTlsInspectionPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteTlsInspectionPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteTlsInspectionPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._DeleteTlsInspectionPolicy._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_tls_inspection_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_tls_inspection_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_tls_inspection_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteTlsInspectionPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteUrlList(
        _BaseNetworkSecurityRestTransport._BaseDeleteUrlList, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteUrlList")

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
            request: url_list.DeleteUrlListRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete url list method over HTTP.

            Args:
                request (~.url_list.DeleteUrlListRequest):
                    The request object. Request used by the DeleteUrlList
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
                _BaseNetworkSecurityRestTransport._BaseDeleteUrlList._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_url_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteUrlList,
                    "_BaseDeleteUrlList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteUrlList",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteUrlList",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._DeleteUrlList._get_response(
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

            resp = self._interceptor.post_delete_url_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_url_list_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.delete_url_list",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteUrlList",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAuthorizationPolicy(
        _BaseNetworkSecurityRestTransport._BaseGetAuthorizationPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetAuthorizationPolicy")

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
            request: authorization_policy.GetAuthorizationPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authorization_policy.AuthorizationPolicy:
            r"""Call the get authorization policy method over HTTP.

            Args:
                request (~.authorization_policy.GetAuthorizationPolicyRequest):
                    The request object. Request used by the
                GetAuthorizationPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authorization_policy.AuthorizationPolicy:
                    AuthorizationPolicy is a resource
                that specifies how a server should
                authorize incoming connections. This
                resource in itself does not change the
                configuration unless it's attached to a
                target https proxy or endpoint config
                selector resource.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseGetAuthorizationPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_authorization_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetAuthorizationPolicy,
                    "_BaseGetAuthorizationPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetAuthorizationPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetAuthorizationPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._GetAuthorizationPolicy._get_response(
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
            resp = authorization_policy.AuthorizationPolicy()
            pb_resp = authorization_policy.AuthorizationPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_authorization_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_authorization_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authorization_policy.AuthorizationPolicy.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_authorization_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetAuthorizationPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAuthzPolicy(
        _BaseNetworkSecurityRestTransport._BaseGetAuthzPolicy, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetAuthzPolicy")

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
            request: authz_policy.GetAuthzPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authz_policy.AuthzPolicy:
            r"""Call the get authz policy method over HTTP.

            Args:
                request (~.authz_policy.GetAuthzPolicyRequest):
                    The request object. Message for getting a ``AuthzPolicy`` resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authz_policy.AuthzPolicy:
                    ``AuthzPolicy`` is a resource that allows to forward
                traffic to a callout backend designed to scan the
                traffic for security purposes.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseGetAuthzPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_authz_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetAuthzPolicy,
                    "_BaseGetAuthzPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetAuthzPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetAuthzPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetAuthzPolicy._get_response(
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
            resp = authz_policy.AuthzPolicy()
            pb_resp = authz_policy.AuthzPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_authz_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_authz_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authz_policy.AuthzPolicy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_authz_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetAuthzPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackendAuthenticationConfig(
        _BaseNetworkSecurityRestTransport._BaseGetBackendAuthenticationConfig,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetBackendAuthenticationConfig")

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
            request: backend_authentication_config.GetBackendAuthenticationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backend_authentication_config.BackendAuthenticationConfig:
            r"""Call the get backend
            authentication config method over HTTP.

                Args:
                    request (~.backend_authentication_config.GetBackendAuthenticationConfigRequest):
                        The request object. Request used by the
                    GetBackendAuthenticationConfig method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.backend_authentication_config.BackendAuthenticationConfig:
                        BackendAuthenticationConfig message groups the
                    TrustConfig together with other settings that control
                    how the load balancer authenticates, and expresses its
                    identity to, the backend:

                    - ``trustConfig`` is the attached TrustConfig.

                    - ``wellKnownRoots`` indicates whether the load balance
                      should trust backend server certificates that are
                      issued by public certificate authorities, in addition
                      to certificates trusted by the TrustConfig.

                    - ``clientCertificate`` is a client certificate that the
                      load balancer uses to express its identity to the
                      backend, if the connection to the backend uses mTLS.

                    You can attach the BackendAuthenticationConfig to the
                    load balancer's BackendService directly determining how
                    that BackendService negotiates TLS.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseGetBackendAuthenticationConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_backend_authentication_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetBackendAuthenticationConfig,
                    "_BaseGetBackendAuthenticationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetBackendAuthenticationConfig",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetBackendAuthenticationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetBackendAuthenticationConfig._get_response(
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
            resp = backend_authentication_config.BackendAuthenticationConfig()
            pb_resp = backend_authentication_config.BackendAuthenticationConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backend_authentication_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_backend_authentication_config_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backend_authentication_config.BackendAuthenticationConfig.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_backend_authentication_config",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetBackendAuthenticationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetClientTlsPolicy(
        _BaseNetworkSecurityRestTransport._BaseGetClientTlsPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetClientTlsPolicy")

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
            request: client_tls_policy.GetClientTlsPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> client_tls_policy.ClientTlsPolicy:
            r"""Call the get client tls policy method over HTTP.

            Args:
                request (~.client_tls_policy.GetClientTlsPolicyRequest):
                    The request object. Request used by the
                GetClientTlsPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.client_tls_policy.ClientTlsPolicy:
                    ClientTlsPolicy is a resource that
                specifies how a client should
                authenticate connections to backends of
                a service. This resource itself does not
                affect configuration unless it is
                attached to a backend service resource.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseGetClientTlsPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_client_tls_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetClientTlsPolicy,
                    "_BaseGetClientTlsPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetClientTlsPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetClientTlsPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetClientTlsPolicy._get_response(
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
            resp = client_tls_policy.ClientTlsPolicy()
            pb_resp = client_tls_policy.ClientTlsPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_client_tls_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_client_tls_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = client_tls_policy.ClientTlsPolicy.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_client_tls_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetClientTlsPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGatewaySecurityPolicy(
        _BaseNetworkSecurityRestTransport._BaseGetGatewaySecurityPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetGatewaySecurityPolicy")

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
            request: gateway_security_policy.GetGatewaySecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gateway_security_policy.GatewaySecurityPolicy:
            r"""Call the get gateway security
            policy method over HTTP.

                Args:
                    request (~.gateway_security_policy.GetGatewaySecurityPolicyRequest):
                        The request object. Request used by the
                    GetGatewaySecurityPolicy method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gateway_security_policy.GatewaySecurityPolicy:
                        The GatewaySecurityPolicy resource
                    contains a collection of
                    GatewaySecurityPolicyRules and
                    associated metadata.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseGetGatewaySecurityPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_gateway_security_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetGatewaySecurityPolicy,
                    "_BaseGetGatewaySecurityPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetGatewaySecurityPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetGatewaySecurityPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._GetGatewaySecurityPolicy._get_response(
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
            resp = gateway_security_policy.GatewaySecurityPolicy()
            pb_resp = gateway_security_policy.GatewaySecurityPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_gateway_security_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_gateway_security_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gateway_security_policy.GatewaySecurityPolicy.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_gateway_security_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetGatewaySecurityPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGatewaySecurityPolicyRule(
        _BaseNetworkSecurityRestTransport._BaseGetGatewaySecurityPolicyRule,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetGatewaySecurityPolicyRule")

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
            request: gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gateway_security_policy_rule.GatewaySecurityPolicyRule:
            r"""Call the get gateway security
            policy rule method over HTTP.

                Args:
                    request (~.gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest):
                        The request object. Request used by the
                    GetGatewaySecurityPolicyRule method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gateway_security_policy_rule.GatewaySecurityPolicyRule:
                        The GatewaySecurityPolicyRule
                    resource is in a nested collection
                    within a GatewaySecurityPolicy and
                    represents a traffic matching condition
                    and associated action to perform.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseGetGatewaySecurityPolicyRule._get_http_options()
            request, metadata = self._interceptor.pre_get_gateway_security_policy_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetGatewaySecurityPolicyRule,
                    "_BaseGetGatewaySecurityPolicyRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetGatewaySecurityPolicyRule",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetGatewaySecurityPolicyRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetGatewaySecurityPolicyRule._get_response(
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
            resp = gateway_security_policy_rule.GatewaySecurityPolicyRule()
            pb_resp = gateway_security_policy_rule.GatewaySecurityPolicyRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_gateway_security_policy_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_gateway_security_policy_rule_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gateway_security_policy_rule.GatewaySecurityPolicyRule.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_gateway_security_policy_rule",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetGatewaySecurityPolicyRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetServerTlsPolicy(
        _BaseNetworkSecurityRestTransport._BaseGetServerTlsPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetServerTlsPolicy")

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
            request: server_tls_policy.GetServerTlsPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> server_tls_policy.ServerTlsPolicy:
            r"""Call the get server tls policy method over HTTP.

            Args:
                request (~.server_tls_policy.GetServerTlsPolicyRequest):
                    The request object. Request used by the
                GetServerTlsPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.server_tls_policy.ServerTlsPolicy:
                    ServerTlsPolicy is a resource that specifies how a
                server should authenticate incoming requests. This
                resource itself does not affect configuration unless it
                is attached to a target HTTPS proxy or endpoint config
                selector resource.

                ServerTlsPolicy in the form accepted by Application Load
                Balancers can be attached only to TargetHttpsProxy with
                an ``EXTERNAL``, ``EXTERNAL_MANAGED`` or
                ``INTERNAL_MANAGED`` load balancing scheme. Traffic
                Director compatible ServerTlsPolicies can be attached to
                EndpointPolicy and TargetHttpsProxy with Traffic
                Director ``INTERNAL_SELF_MANAGED`` load balancing
                scheme.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseGetServerTlsPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_server_tls_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetServerTlsPolicy,
                    "_BaseGetServerTlsPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetServerTlsPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetServerTlsPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetServerTlsPolicy._get_response(
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
            resp = server_tls_policy.ServerTlsPolicy()
            pb_resp = server_tls_policy.ServerTlsPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_server_tls_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_server_tls_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = server_tls_policy.ServerTlsPolicy.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_server_tls_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetServerTlsPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTlsInspectionPolicy(
        _BaseNetworkSecurityRestTransport._BaseGetTlsInspectionPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetTlsInspectionPolicy")

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
            request: tls_inspection_policy.GetTlsInspectionPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tls_inspection_policy.TlsInspectionPolicy:
            r"""Call the get tls inspection policy method over HTTP.

            Args:
                request (~.tls_inspection_policy.GetTlsInspectionPolicyRequest):
                    The request object. Request used by the
                GetTlsInspectionPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tls_inspection_policy.TlsInspectionPolicy:
                    The TlsInspectionPolicy resource
                contains references to CA pools in
                Certificate Authority Service and
                associated metadata.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseGetTlsInspectionPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_tls_inspection_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetTlsInspectionPolicy,
                    "_BaseGetTlsInspectionPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetTlsInspectionPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetTlsInspectionPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._GetTlsInspectionPolicy._get_response(
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
            resp = tls_inspection_policy.TlsInspectionPolicy()
            pb_resp = tls_inspection_policy.TlsInspectionPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_tls_inspection_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_tls_inspection_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        tls_inspection_policy.TlsInspectionPolicy.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_tls_inspection_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetTlsInspectionPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUrlList(
        _BaseNetworkSecurityRestTransport._BaseGetUrlList, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetUrlList")

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
            request: url_list.GetUrlListRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> url_list.UrlList:
            r"""Call the get url list method over HTTP.

            Args:
                request (~.url_list.GetUrlListRequest):
                    The request object. Request used by the GetUrlList
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.url_list.UrlList:
                    UrlList proto helps users to set
                reusable, independently manageable lists
                of hosts, host patterns, URLs, URL
                patterns.

            """

            http_options = (
                _BaseNetworkSecurityRestTransport._BaseGetUrlList._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_url_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetUrlList,
                    "_BaseGetUrlList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetUrlList",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetUrlList",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetUrlList._get_response(
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
            resp = url_list.UrlList()
            pb_resp = url_list.UrlList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_url_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_url_list_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = url_list.UrlList.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.get_url_list",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetUrlList",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAuthorizationPolicies(
        _BaseNetworkSecurityRestTransport._BaseListAuthorizationPolicies,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListAuthorizationPolicies")

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
            request: authorization_policy.ListAuthorizationPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authorization_policy.ListAuthorizationPoliciesResponse:
            r"""Call the list authorization
            policies method over HTTP.

                Args:
                    request (~.authorization_policy.ListAuthorizationPoliciesRequest):
                        The request object. Request used with the
                    ListAuthorizationPolicies method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authorization_policy.ListAuthorizationPoliciesResponse:
                        Response returned by the
                    ListAuthorizationPolicies method.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseListAuthorizationPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_authorization_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListAuthorizationPolicies,
                    "_BaseListAuthorizationPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListAuthorizationPolicies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListAuthorizationPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._ListAuthorizationPolicies._get_response(
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
            resp = authorization_policy.ListAuthorizationPoliciesResponse()
            pb_resp = authorization_policy.ListAuthorizationPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_authorization_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_authorization_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        authorization_policy.ListAuthorizationPoliciesResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_authorization_policies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListAuthorizationPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAuthzPolicies(
        _BaseNetworkSecurityRestTransport._BaseListAuthzPolicies,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListAuthzPolicies")

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
            request: authz_policy.ListAuthzPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authz_policy.ListAuthzPoliciesResponse:
            r"""Call the list authz policies method over HTTP.

            Args:
                request (~.authz_policy.ListAuthzPoliciesRequest):
                    The request object. Message for requesting list of ``AuthzPolicy``
                resources.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authz_policy.ListAuthzPoliciesResponse:
                    Message for response to listing ``AuthzPolicy``
                resources.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseListAuthzPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_authz_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListAuthzPolicies,
                    "_BaseListAuthzPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListAuthzPolicies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListAuthzPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._ListAuthzPolicies._get_response(
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
            resp = authz_policy.ListAuthzPoliciesResponse()
            pb_resp = authz_policy.ListAuthzPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_authz_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_authz_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authz_policy.ListAuthzPoliciesResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_authz_policies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListAuthzPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackendAuthenticationConfigs(
        _BaseNetworkSecurityRestTransport._BaseListBackendAuthenticationConfigs,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListBackendAuthenticationConfigs")

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
            request: backend_authentication_config.ListBackendAuthenticationConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backend_authentication_config.ListBackendAuthenticationConfigsResponse:
            r"""Call the list backend
            authentication configs method over HTTP.

                Args:
                    request (~.backend_authentication_config.ListBackendAuthenticationConfigsRequest):
                        The request object. Request used by the
                    ListBackendAuthenticationConfigs method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.backend_authentication_config.ListBackendAuthenticationConfigsResponse:
                        Response returned by the
                    ListBackendAuthenticationConfigs method.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseListBackendAuthenticationConfigs._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_backend_authentication_configs(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListBackendAuthenticationConfigs,
                    "_BaseListBackendAuthenticationConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListBackendAuthenticationConfigs",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListBackendAuthenticationConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._ListBackendAuthenticationConfigs._get_response(
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
            resp = (
                backend_authentication_config.ListBackendAuthenticationConfigsResponse()
            )
            pb_resp = backend_authentication_config.ListBackendAuthenticationConfigsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backend_authentication_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_backend_authentication_configs_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backend_authentication_config.ListBackendAuthenticationConfigsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_backend_authentication_configs",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListBackendAuthenticationConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListClientTlsPolicies(
        _BaseNetworkSecurityRestTransport._BaseListClientTlsPolicies,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListClientTlsPolicies")

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
            request: client_tls_policy.ListClientTlsPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> client_tls_policy.ListClientTlsPoliciesResponse:
            r"""Call the list client tls policies method over HTTP.

            Args:
                request (~.client_tls_policy.ListClientTlsPoliciesRequest):
                    The request object. Request used by the
                ListClientTlsPolicies method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.client_tls_policy.ListClientTlsPoliciesResponse:
                    Response returned by the
                ListClientTlsPolicies method.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseListClientTlsPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_client_tls_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListClientTlsPolicies,
                    "_BaseListClientTlsPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListClientTlsPolicies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListClientTlsPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._ListClientTlsPolicies._get_response(
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
            resp = client_tls_policy.ListClientTlsPoliciesResponse()
            pb_resp = client_tls_policy.ListClientTlsPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_client_tls_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_client_tls_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        client_tls_policy.ListClientTlsPoliciesResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_client_tls_policies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListClientTlsPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGatewaySecurityPolicies(
        _BaseNetworkSecurityRestTransport._BaseListGatewaySecurityPolicies,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListGatewaySecurityPolicies")

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
            request: gateway_security_policy.ListGatewaySecurityPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gateway_security_policy.ListGatewaySecurityPoliciesResponse:
            r"""Call the list gateway security
            policies method over HTTP.

                Args:
                    request (~.gateway_security_policy.ListGatewaySecurityPoliciesRequest):
                        The request object. Request used with the
                    ListGatewaySecurityPolicies method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gateway_security_policy.ListGatewaySecurityPoliciesResponse:
                        Response returned by the
                    ListGatewaySecurityPolicies method.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseListGatewaySecurityPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_gateway_security_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListGatewaySecurityPolicies,
                    "_BaseListGatewaySecurityPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListGatewaySecurityPolicies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListGatewaySecurityPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._ListGatewaySecurityPolicies._get_response(
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
            resp = gateway_security_policy.ListGatewaySecurityPoliciesResponse()
            pb_resp = gateway_security_policy.ListGatewaySecurityPoliciesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_gateway_security_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_gateway_security_policies_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gateway_security_policy.ListGatewaySecurityPoliciesResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_gateway_security_policies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListGatewaySecurityPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGatewaySecurityPolicyRules(
        _BaseNetworkSecurityRestTransport._BaseListGatewaySecurityPolicyRules,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListGatewaySecurityPolicyRules")

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
            request: gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse:
            r"""Call the list gateway security
            policy rules method over HTTP.

                Args:
                    request (~.gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest):
                        The request object. Request used with the
                    ListGatewaySecurityPolicyRules method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse:
                        Response returned by the
                    ListGatewaySecurityPolicyRules method.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseListGatewaySecurityPolicyRules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_gateway_security_policy_rules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListGatewaySecurityPolicyRules,
                    "_BaseListGatewaySecurityPolicyRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListGatewaySecurityPolicyRules",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListGatewaySecurityPolicyRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._ListGatewaySecurityPolicyRules._get_response(
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
            resp = gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse()
            pb_resp = (
                gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_gateway_security_policy_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_gateway_security_policy_rules_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_gateway_security_policy_rules",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListGatewaySecurityPolicyRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServerTlsPolicies(
        _BaseNetworkSecurityRestTransport._BaseListServerTlsPolicies,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListServerTlsPolicies")

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
            request: server_tls_policy.ListServerTlsPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> server_tls_policy.ListServerTlsPoliciesResponse:
            r"""Call the list server tls policies method over HTTP.

            Args:
                request (~.server_tls_policy.ListServerTlsPoliciesRequest):
                    The request object. Request used by the
                ListServerTlsPolicies method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.server_tls_policy.ListServerTlsPoliciesResponse:
                    Response returned by the
                ListServerTlsPolicies method.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseListServerTlsPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_server_tls_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListServerTlsPolicies,
                    "_BaseListServerTlsPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListServerTlsPolicies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListServerTlsPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._ListServerTlsPolicies._get_response(
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
            resp = server_tls_policy.ListServerTlsPoliciesResponse()
            pb_resp = server_tls_policy.ListServerTlsPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_server_tls_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_server_tls_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        server_tls_policy.ListServerTlsPoliciesResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_server_tls_policies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListServerTlsPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTlsInspectionPolicies(
        _BaseNetworkSecurityRestTransport._BaseListTlsInspectionPolicies,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListTlsInspectionPolicies")

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
            request: tls_inspection_policy.ListTlsInspectionPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tls_inspection_policy.ListTlsInspectionPoliciesResponse:
            r"""Call the list tls inspection
            policies method over HTTP.

                Args:
                    request (~.tls_inspection_policy.ListTlsInspectionPoliciesRequest):
                        The request object. Request used with the
                    ListTlsInspectionPolicies method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.tls_inspection_policy.ListTlsInspectionPoliciesResponse:
                        Response returned by the
                    ListTlsInspectionPolicies method.

            """

            http_options = _BaseNetworkSecurityRestTransport._BaseListTlsInspectionPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_tls_inspection_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListTlsInspectionPolicies,
                    "_BaseListTlsInspectionPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListTlsInspectionPolicies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListTlsInspectionPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._ListTlsInspectionPolicies._get_response(
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
            resp = tls_inspection_policy.ListTlsInspectionPoliciesResponse()
            pb_resp = tls_inspection_policy.ListTlsInspectionPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tls_inspection_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tls_inspection_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        tls_inspection_policy.ListTlsInspectionPoliciesResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_tls_inspection_policies",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListTlsInspectionPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUrlLists(
        _BaseNetworkSecurityRestTransport._BaseListUrlLists, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListUrlLists")

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
            request: url_list.ListUrlListsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> url_list.ListUrlListsResponse:
            r"""Call the list url lists method over HTTP.

            Args:
                request (~.url_list.ListUrlListsRequest):
                    The request object. Request used by the ListUrlList
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.url_list.ListUrlListsResponse:
                    Response returned by the ListUrlLists
                method.

            """

            http_options = (
                _BaseNetworkSecurityRestTransport._BaseListUrlLists._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_url_lists(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListUrlLists,
                    "_BaseListUrlLists__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListUrlLists",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListUrlLists",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._ListUrlLists._get_response(
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
            resp = url_list.ListUrlListsResponse()
            pb_resp = url_list.ListUrlListsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_url_lists(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_url_lists_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = url_list.ListUrlListsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.list_url_lists",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListUrlLists",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAuthorizationPolicy(
        _BaseNetworkSecurityRestTransport._BaseUpdateAuthorizationPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.UpdateAuthorizationPolicy")

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
            request: gcn_authorization_policy.UpdateAuthorizationPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update authorization
            policy method over HTTP.

                Args:
                    request (~.gcn_authorization_policy.UpdateAuthorizationPolicyRequest):
                        The request object. Request used by the
                    UpdateAuthorizationPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseUpdateAuthorizationPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_authorization_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateAuthorizationPolicy,
                    "_BaseUpdateAuthorizationPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateAuthorizationPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateAuthorizationPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._UpdateAuthorizationPolicy._get_response(
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

            resp = self._interceptor.post_update_authorization_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_authorization_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_authorization_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateAuthorizationPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAuthzPolicy(
        _BaseNetworkSecurityRestTransport._BaseUpdateAuthzPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.UpdateAuthzPolicy")

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
            request: gcn_authz_policy.UpdateAuthzPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update authz policy method over HTTP.

            Args:
                request (~.gcn_authz_policy.UpdateAuthzPolicyRequest):
                    The request object. Message for updating an ``AuthzPolicy`` resource.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseUpdateAuthzPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_authz_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateAuthzPolicy,
                    "_BaseUpdateAuthzPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateAuthzPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateAuthzPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._UpdateAuthzPolicy._get_response(
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

            resp = self._interceptor.post_update_authz_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_authz_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_authz_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateAuthzPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackendAuthenticationConfig(
        _BaseNetworkSecurityRestTransport._BaseUpdateBackendAuthenticationConfig,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash(
                "NetworkSecurityRestTransport.UpdateBackendAuthenticationConfig"
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
                data=body,
            )
            return response

        def __call__(
            self,
            request: gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backend
            authentication config method over HTTP.

                Args:
                    request (~.gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest):
                        The request object. Request used by
                    UpdateBackendAuthenticationConfig
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

            http_options = _BaseNetworkSecurityRestTransport._BaseUpdateBackendAuthenticationConfig._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_backend_authentication_config(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateBackendAuthenticationConfig,
                    "_BaseUpdateBackendAuthenticationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateBackendAuthenticationConfig",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateBackendAuthenticationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._UpdateBackendAuthenticationConfig._get_response(
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

            resp = self._interceptor.post_update_backend_authentication_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_backend_authentication_config_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_backend_authentication_config",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateBackendAuthenticationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateClientTlsPolicy(
        _BaseNetworkSecurityRestTransport._BaseUpdateClientTlsPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.UpdateClientTlsPolicy")

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
            request: gcn_client_tls_policy.UpdateClientTlsPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update client tls policy method over HTTP.

            Args:
                request (~.gcn_client_tls_policy.UpdateClientTlsPolicyRequest):
                    The request object. Request used by UpdateClientTlsPolicy
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

            http_options = _BaseNetworkSecurityRestTransport._BaseUpdateClientTlsPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_client_tls_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateClientTlsPolicy,
                    "_BaseUpdateClientTlsPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateClientTlsPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateClientTlsPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._UpdateClientTlsPolicy._get_response(
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

            resp = self._interceptor.post_update_client_tls_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_client_tls_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_client_tls_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateClientTlsPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGatewaySecurityPolicy(
        _BaseNetworkSecurityRestTransport._BaseUpdateGatewaySecurityPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.UpdateGatewaySecurityPolicy")

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
            request: gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update gateway security
            policy method over HTTP.

                Args:
                    request (~.gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest):
                        The request object. Request used by the
                    UpdateGatewaySecurityPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseUpdateGatewaySecurityPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_gateway_security_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateGatewaySecurityPolicy,
                    "_BaseUpdateGatewaySecurityPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateGatewaySecurityPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateGatewaySecurityPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._UpdateGatewaySecurityPolicy._get_response(
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

            resp = self._interceptor.post_update_gateway_security_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_gateway_security_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_gateway_security_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateGatewaySecurityPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGatewaySecurityPolicyRule(
        _BaseNetworkSecurityRestTransport._BaseUpdateGatewaySecurityPolicyRule,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.UpdateGatewaySecurityPolicyRule")

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
            request: gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update gateway security
            policy rule method over HTTP.

                Args:
                    request (~.gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest):
                        The request object. Request used by the
                    UpdateGatewaySecurityPolicyRule method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseUpdateGatewaySecurityPolicyRule._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_gateway_security_policy_rule(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateGatewaySecurityPolicyRule,
                    "_BaseUpdateGatewaySecurityPolicyRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateGatewaySecurityPolicyRule",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateGatewaySecurityPolicyRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._UpdateGatewaySecurityPolicyRule._get_response(
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

            resp = self._interceptor.post_update_gateway_security_policy_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_gateway_security_policy_rule_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_gateway_security_policy_rule",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateGatewaySecurityPolicyRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateServerTlsPolicy(
        _BaseNetworkSecurityRestTransport._BaseUpdateServerTlsPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.UpdateServerTlsPolicy")

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
            request: gcn_server_tls_policy.UpdateServerTlsPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update server tls policy method over HTTP.

            Args:
                request (~.gcn_server_tls_policy.UpdateServerTlsPolicyRequest):
                    The request object. Request used by UpdateServerTlsPolicy
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

            http_options = _BaseNetworkSecurityRestTransport._BaseUpdateServerTlsPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_server_tls_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateServerTlsPolicy,
                    "_BaseUpdateServerTlsPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateServerTlsPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateServerTlsPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._UpdateServerTlsPolicy._get_response(
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

            resp = self._interceptor.post_update_server_tls_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_server_tls_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_server_tls_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateServerTlsPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTlsInspectionPolicy(
        _BaseNetworkSecurityRestTransport._BaseUpdateTlsInspectionPolicy,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.UpdateTlsInspectionPolicy")

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
            request: gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update tls inspection
            policy method over HTTP.

                Args:
                    request (~.gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest):
                        The request object. Request used by the
                    UpdateTlsInspectionPolicy method.
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

            http_options = _BaseNetworkSecurityRestTransport._BaseUpdateTlsInspectionPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_tls_inspection_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateTlsInspectionPolicy,
                    "_BaseUpdateTlsInspectionPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateTlsInspectionPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateTlsInspectionPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkSecurityRestTransport._UpdateTlsInspectionPolicy._get_response(
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

            resp = self._interceptor.post_update_tls_inspection_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_tls_inspection_policy_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_tls_inspection_policy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateTlsInspectionPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUrlList(
        _BaseNetworkSecurityRestTransport._BaseUpdateUrlList, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.UpdateUrlList")

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
            request: gcn_url_list.UpdateUrlListRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update url list method over HTTP.

            Args:
                request (~.gcn_url_list.UpdateUrlListRequest):
                    The request object. Request used by UpdateUrlList method.
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
                _BaseNetworkSecurityRestTransport._BaseUpdateUrlList._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_url_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseUpdateUrlList,
                    "_BaseUpdateUrlList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.UpdateUrlList",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateUrlList",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._UpdateUrlList._get_response(
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

            resp = self._interceptor.post_update_url_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_url_list_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityClient.update_url_list",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "UpdateUrlList",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_authorization_policy(
        self,
    ) -> Callable[
        [gcn_authorization_policy.CreateAuthorizationPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAuthorizationPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_authz_policy(
        self,
    ) -> Callable[
        [gcn_authz_policy.CreateAuthzPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAuthzPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_backend_authentication_config(
        self,
    ) -> Callable[
        [gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackendAuthenticationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_client_tls_policy(
        self,
    ) -> Callable[
        [gcn_client_tls_policy.CreateClientTlsPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateClientTlsPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_gateway_security_policy(
        self,
    ) -> Callable[
        [gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGatewaySecurityPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_gateway_security_policy_rule(
        self,
    ) -> Callable[
        [gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGatewaySecurityPolicyRule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_server_tls_policy(
        self,
    ) -> Callable[
        [gcn_server_tls_policy.CreateServerTlsPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateServerTlsPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tls_inspection_policy(
        self,
    ) -> Callable[
        [gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTlsInspectionPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_url_list(
        self,
    ) -> Callable[[gcn_url_list.CreateUrlListRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUrlList(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_authorization_policy(
        self,
    ) -> Callable[
        [authorization_policy.DeleteAuthorizationPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAuthorizationPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_authz_policy(
        self,
    ) -> Callable[[authz_policy.DeleteAuthzPolicyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAuthzPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backend_authentication_config(
        self,
    ) -> Callable[
        [backend_authentication_config.DeleteBackendAuthenticationConfigRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackendAuthenticationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_client_tls_policy(
        self,
    ) -> Callable[
        [client_tls_policy.DeleteClientTlsPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteClientTlsPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_gateway_security_policy(
        self,
    ) -> Callable[
        [gateway_security_policy.DeleteGatewaySecurityPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGatewaySecurityPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_gateway_security_policy_rule(
        self,
    ) -> Callable[
        [gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGatewaySecurityPolicyRule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_server_tls_policy(
        self,
    ) -> Callable[
        [server_tls_policy.DeleteServerTlsPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteServerTlsPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tls_inspection_policy(
        self,
    ) -> Callable[
        [tls_inspection_policy.DeleteTlsInspectionPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTlsInspectionPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_url_list(
        self,
    ) -> Callable[[url_list.DeleteUrlListRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUrlList(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_authorization_policy(
        self,
    ) -> Callable[
        [authorization_policy.GetAuthorizationPolicyRequest],
        authorization_policy.AuthorizationPolicy,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAuthorizationPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_authz_policy(
        self,
    ) -> Callable[[authz_policy.GetAuthzPolicyRequest], authz_policy.AuthzPolicy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAuthzPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backend_authentication_config(
        self,
    ) -> Callable[
        [backend_authentication_config.GetBackendAuthenticationConfigRequest],
        backend_authentication_config.BackendAuthenticationConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackendAuthenticationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_client_tls_policy(
        self,
    ) -> Callable[
        [client_tls_policy.GetClientTlsPolicyRequest], client_tls_policy.ClientTlsPolicy
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetClientTlsPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_gateway_security_policy(
        self,
    ) -> Callable[
        [gateway_security_policy.GetGatewaySecurityPolicyRequest],
        gateway_security_policy.GatewaySecurityPolicy,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGatewaySecurityPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_gateway_security_policy_rule(
        self,
    ) -> Callable[
        [gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest],
        gateway_security_policy_rule.GatewaySecurityPolicyRule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGatewaySecurityPolicyRule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_server_tls_policy(
        self,
    ) -> Callable[
        [server_tls_policy.GetServerTlsPolicyRequest], server_tls_policy.ServerTlsPolicy
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetServerTlsPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tls_inspection_policy(
        self,
    ) -> Callable[
        [tls_inspection_policy.GetTlsInspectionPolicyRequest],
        tls_inspection_policy.TlsInspectionPolicy,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTlsInspectionPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_url_list(self) -> Callable[[url_list.GetUrlListRequest], url_list.UrlList]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUrlList(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_authorization_policies(
        self,
    ) -> Callable[
        [authorization_policy.ListAuthorizationPoliciesRequest],
        authorization_policy.ListAuthorizationPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAuthorizationPolicies(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_authz_policies(
        self,
    ) -> Callable[
        [authz_policy.ListAuthzPoliciesRequest], authz_policy.ListAuthzPoliciesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAuthzPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backend_authentication_configs(
        self,
    ) -> Callable[
        [backend_authentication_config.ListBackendAuthenticationConfigsRequest],
        backend_authentication_config.ListBackendAuthenticationConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackendAuthenticationConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_client_tls_policies(
        self,
    ) -> Callable[
        [client_tls_policy.ListClientTlsPoliciesRequest],
        client_tls_policy.ListClientTlsPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListClientTlsPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_gateway_security_policies(
        self,
    ) -> Callable[
        [gateway_security_policy.ListGatewaySecurityPoliciesRequest],
        gateway_security_policy.ListGatewaySecurityPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGatewaySecurityPolicies(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_gateway_security_policy_rules(
        self,
    ) -> Callable[
        [gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest],
        gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGatewaySecurityPolicyRules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_server_tls_policies(
        self,
    ) -> Callable[
        [server_tls_policy.ListServerTlsPoliciesRequest],
        server_tls_policy.ListServerTlsPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServerTlsPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tls_inspection_policies(
        self,
    ) -> Callable[
        [tls_inspection_policy.ListTlsInspectionPoliciesRequest],
        tls_inspection_policy.ListTlsInspectionPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTlsInspectionPolicies(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_url_lists(
        self,
    ) -> Callable[[url_list.ListUrlListsRequest], url_list.ListUrlListsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUrlLists(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_authorization_policy(
        self,
    ) -> Callable[
        [gcn_authorization_policy.UpdateAuthorizationPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAuthorizationPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_authz_policy(
        self,
    ) -> Callable[
        [gcn_authz_policy.UpdateAuthzPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAuthzPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backend_authentication_config(
        self,
    ) -> Callable[
        [gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackendAuthenticationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_client_tls_policy(
        self,
    ) -> Callable[
        [gcn_client_tls_policy.UpdateClientTlsPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateClientTlsPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_gateway_security_policy(
        self,
    ) -> Callable[
        [gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGatewaySecurityPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_gateway_security_policy_rule(
        self,
    ) -> Callable[
        [gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGatewaySecurityPolicyRule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_server_tls_policy(
        self,
    ) -> Callable[
        [gcn_server_tls_policy.UpdateServerTlsPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateServerTlsPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tls_inspection_policy(
        self,
    ) -> Callable[
        [gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTlsInspectionPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_url_list(
        self,
    ) -> Callable[[gcn_url_list.UpdateUrlListRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUrlList(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseNetworkSecurityRestTransport._BaseGetLocation, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetLocation")

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
                _BaseNetworkSecurityRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
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
        _BaseNetworkSecurityRestTransport._BaseListLocations, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListLocations")

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
                _BaseNetworkSecurityRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
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
        _BaseNetworkSecurityRestTransport._BaseGetIamPolicy, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetIamPolicy")

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
                _BaseNetworkSecurityRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
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
        _BaseNetworkSecurityRestTransport._BaseSetIamPolicy, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.SetIamPolicy")

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
                _BaseNetworkSecurityRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
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
        _BaseNetworkSecurityRestTransport._BaseTestIamPermissions,
        NetworkSecurityRestStub,
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.TestIamPermissions")

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

            http_options = _BaseNetworkSecurityRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
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
        _BaseNetworkSecurityRestTransport._BaseCancelOperation, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.CancelOperation")

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

            http_options = _BaseNetworkSecurityRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._CancelOperation._get_response(
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
        _BaseNetworkSecurityRestTransport._BaseDeleteOperation, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.DeleteOperation")

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

            http_options = _BaseNetworkSecurityRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._DeleteOperation._get_response(
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
        _BaseNetworkSecurityRestTransport._BaseGetOperation, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.GetOperation")

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
                _BaseNetworkSecurityRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
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
        _BaseNetworkSecurityRestTransport._BaseListOperations, NetworkSecurityRestStub
    ):
        def __hash__(self):
            return hash("NetworkSecurityRestTransport.ListOperations")

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

            http_options = _BaseNetworkSecurityRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkSecurityRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.networksecurity_v1.NetworkSecurityClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkSecurityRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.NetworkSecurityAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.NetworkSecurity",
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


__all__ = ("NetworkSecurityRestTransport",)
