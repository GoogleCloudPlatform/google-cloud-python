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

import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.iap_v1._compat import transcode_request
from google.cloud.iap_v1.types import service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseIdentityAwareProxyAdminServiceRestTransport

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


class IdentityAwareProxyAdminServiceRestInterceptor:
    """Interceptor for IdentityAwareProxyAdminService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the IdentityAwareProxyAdminServiceRestTransport.

    .. code-block:: python
        class MyCustomIdentityAwareProxyAdminServiceInterceptor(IdentityAwareProxyAdminServiceRestInterceptor):
            def pre_create_tunnel_dest_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tunnel_dest_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tunnel_dest_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iap_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iap_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tunnel_dest_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tunnel_dest_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tunnel_dest_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tunnel_dest_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_iam_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_iap_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_iap_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tunnel_dest_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tunnel_dest_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_validate_iap_attribute_expression(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_iap_attribute_expression(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = IdentityAwareProxyAdminServiceRestTransport(interceptor=MyCustomIdentityAwareProxyAdminServiceInterceptor())
        client = IdentityAwareProxyAdminServiceClient(transport=transport)


    """

    def pre_create_tunnel_dest_group(
        self,
        request: service.CreateTunnelDestGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateTunnelDestGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_tunnel_dest_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_create_tunnel_dest_group(
        self, response: service.TunnelDestGroup
    ) -> service.TunnelDestGroup:
        """Post-rpc interceptor for create_tunnel_dest_group

        DEPRECATED. Please use the `post_create_tunnel_dest_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_create_tunnel_dest_group` interceptor runs
        before the `post_create_tunnel_dest_group_with_metadata` interceptor.
        """
        return response

    def post_create_tunnel_dest_group_with_metadata(
        self,
        response: service.TunnelDestGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.TunnelDestGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_tunnel_dest_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_create_tunnel_dest_group_with_metadata`
        interceptor in new development instead of the `post_create_tunnel_dest_group` interceptor.
        When both interceptors are used, this `post_create_tunnel_dest_group_with_metadata` interceptor runs after the
        `post_create_tunnel_dest_group` interceptor. The (possibly modified) response returned by
        `post_create_tunnel_dest_group` will be passed to
        `post_create_tunnel_dest_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_tunnel_dest_group(
        self,
        request: service.DeleteTunnelDestGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteTunnelDestGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_tunnel_dest_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        DEPRECATED. Please use the `post_get_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_get_iam_policy` interceptor runs
        before the `post_get_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_get_iam_policy_with_metadata(
        self,
        response: policy_pb2.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[policy_pb2.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_get_iam_policy_with_metadata`
        interceptor in new development instead of the `post_get_iam_policy` interceptor.
        When both interceptors are used, this `post_get_iam_policy_with_metadata` interceptor runs after the
        `post_get_iam_policy` interceptor. The (possibly modified) response returned by
        `post_get_iam_policy` will be passed to
        `post_get_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_iap_settings(
        self,
        request: service.GetIapSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetIapSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_iap_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_get_iap_settings(
        self, response: service.IapSettings
    ) -> service.IapSettings:
        """Post-rpc interceptor for get_iap_settings

        DEPRECATED. Please use the `post_get_iap_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_get_iap_settings` interceptor runs
        before the `post_get_iap_settings_with_metadata` interceptor.
        """
        return response

    def post_get_iap_settings_with_metadata(
        self,
        response: service.IapSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.IapSettings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_iap_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_get_iap_settings_with_metadata`
        interceptor in new development instead of the `post_get_iap_settings` interceptor.
        When both interceptors are used, this `post_get_iap_settings_with_metadata` interceptor runs after the
        `post_get_iap_settings` interceptor. The (possibly modified) response returned by
        `post_get_iap_settings` will be passed to
        `post_get_iap_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_tunnel_dest_group(
        self,
        request: service.GetTunnelDestGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetTunnelDestGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_tunnel_dest_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_get_tunnel_dest_group(
        self, response: service.TunnelDestGroup
    ) -> service.TunnelDestGroup:
        """Post-rpc interceptor for get_tunnel_dest_group

        DEPRECATED. Please use the `post_get_tunnel_dest_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_get_tunnel_dest_group` interceptor runs
        before the `post_get_tunnel_dest_group_with_metadata` interceptor.
        """
        return response

    def post_get_tunnel_dest_group_with_metadata(
        self,
        response: service.TunnelDestGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.TunnelDestGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_tunnel_dest_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_get_tunnel_dest_group_with_metadata`
        interceptor in new development instead of the `post_get_tunnel_dest_group` interceptor.
        When both interceptors are used, this `post_get_tunnel_dest_group_with_metadata` interceptor runs after the
        `post_get_tunnel_dest_group` interceptor. The (possibly modified) response returned by
        `post_get_tunnel_dest_group` will be passed to
        `post_get_tunnel_dest_group_with_metadata`.
        """
        return response, metadata

    def pre_list_tunnel_dest_groups(
        self,
        request: service.ListTunnelDestGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListTunnelDestGroupsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_tunnel_dest_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_list_tunnel_dest_groups(
        self, response: service.ListTunnelDestGroupsResponse
    ) -> service.ListTunnelDestGroupsResponse:
        """Post-rpc interceptor for list_tunnel_dest_groups

        DEPRECATED. Please use the `post_list_tunnel_dest_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_list_tunnel_dest_groups` interceptor runs
        before the `post_list_tunnel_dest_groups_with_metadata` interceptor.
        """
        return response

    def post_list_tunnel_dest_groups_with_metadata(
        self,
        response: service.ListTunnelDestGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListTunnelDestGroupsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_tunnel_dest_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_list_tunnel_dest_groups_with_metadata`
        interceptor in new development instead of the `post_list_tunnel_dest_groups` interceptor.
        When both interceptors are used, this `post_list_tunnel_dest_groups_with_metadata` interceptor runs after the
        `post_list_tunnel_dest_groups` interceptor. The (possibly modified) response returned by
        `post_list_tunnel_dest_groups` will be passed to
        `post_list_tunnel_dest_groups_with_metadata`.
        """
        return response, metadata

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        DEPRECATED. Please use the `post_set_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_set_iam_policy` interceptor runs
        before the `post_set_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_set_iam_policy_with_metadata(
        self,
        response: policy_pb2.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[policy_pb2.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_set_iam_policy_with_metadata`
        interceptor in new development instead of the `post_set_iam_policy` interceptor.
        When both interceptors are used, this `post_set_iam_policy_with_metadata` interceptor runs after the
        `post_set_iam_policy` interceptor. The (possibly modified) response returned by
        `post_set_iam_policy` will be passed to
        `post_set_iam_policy_with_metadata`.
        """
        return response, metadata

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
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        DEPRECATED. Please use the `post_test_iam_permissions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_test_iam_permissions` interceptor runs
        before the `post_test_iam_permissions_with_metadata` interceptor.
        """
        return response

    def post_test_iam_permissions_with_metadata(
        self,
        response: iam_policy_pb2.TestIamPermissionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_test_iam_permissions_with_metadata`
        interceptor in new development instead of the `post_test_iam_permissions` interceptor.
        When both interceptors are used, this `post_test_iam_permissions_with_metadata` interceptor runs after the
        `post_test_iam_permissions` interceptor. The (possibly modified) response returned by
        `post_test_iam_permissions` will be passed to
        `post_test_iam_permissions_with_metadata`.
        """
        return response, metadata

    def pre_update_iap_settings(
        self,
        request: service.UpdateIapSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateIapSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_iap_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_update_iap_settings(
        self, response: service.IapSettings
    ) -> service.IapSettings:
        """Post-rpc interceptor for update_iap_settings

        DEPRECATED. Please use the `post_update_iap_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_update_iap_settings` interceptor runs
        before the `post_update_iap_settings_with_metadata` interceptor.
        """
        return response

    def post_update_iap_settings_with_metadata(
        self,
        response: service.IapSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.IapSettings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_iap_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_update_iap_settings_with_metadata`
        interceptor in new development instead of the `post_update_iap_settings` interceptor.
        When both interceptors are used, this `post_update_iap_settings_with_metadata` interceptor runs after the
        `post_update_iap_settings` interceptor. The (possibly modified) response returned by
        `post_update_iap_settings` will be passed to
        `post_update_iap_settings_with_metadata`.
        """
        return response, metadata

    def pre_update_tunnel_dest_group(
        self,
        request: service.UpdateTunnelDestGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateTunnelDestGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_tunnel_dest_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_update_tunnel_dest_group(
        self, response: service.TunnelDestGroup
    ) -> service.TunnelDestGroup:
        """Post-rpc interceptor for update_tunnel_dest_group

        DEPRECATED. Please use the `post_update_tunnel_dest_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_update_tunnel_dest_group` interceptor runs
        before the `post_update_tunnel_dest_group_with_metadata` interceptor.
        """
        return response

    def post_update_tunnel_dest_group_with_metadata(
        self,
        response: service.TunnelDestGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.TunnelDestGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_tunnel_dest_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_update_tunnel_dest_group_with_metadata`
        interceptor in new development instead of the `post_update_tunnel_dest_group` interceptor.
        When both interceptors are used, this `post_update_tunnel_dest_group_with_metadata` interceptor runs after the
        `post_update_tunnel_dest_group` interceptor. The (possibly modified) response returned by
        `post_update_tunnel_dest_group` will be passed to
        `post_update_tunnel_dest_group_with_metadata`.
        """
        return response, metadata

    def pre_validate_iap_attribute_expression(
        self,
        request: service.ValidateIapAttributeExpressionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ValidateIapAttributeExpressionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for validate_iap_attribute_expression

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyAdminService server.
        """
        return request, metadata

    def post_validate_iap_attribute_expression(
        self, response: service.ValidateIapAttributeExpressionResponse
    ) -> service.ValidateIapAttributeExpressionResponse:
        """Post-rpc interceptor for validate_iap_attribute_expression

        DEPRECATED. Please use the `post_validate_iap_attribute_expression_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyAdminService server but before
        it is returned to user code. This `post_validate_iap_attribute_expression` interceptor runs
        before the `post_validate_iap_attribute_expression_with_metadata` interceptor.
        """
        return response

    def post_validate_iap_attribute_expression_with_metadata(
        self,
        response: service.ValidateIapAttributeExpressionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ValidateIapAttributeExpressionResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for validate_iap_attribute_expression

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyAdminService server but before it is returned to user code.

        We recommend only using this `post_validate_iap_attribute_expression_with_metadata`
        interceptor in new development instead of the `post_validate_iap_attribute_expression` interceptor.
        When both interceptors are used, this `post_validate_iap_attribute_expression_with_metadata` interceptor runs after the
        `post_validate_iap_attribute_expression` interceptor. The (possibly modified) response returned by
        `post_validate_iap_attribute_expression` will be passed to
        `post_validate_iap_attribute_expression_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class IdentityAwareProxyAdminServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: IdentityAwareProxyAdminServiceRestInterceptor


class IdentityAwareProxyAdminServiceRestTransport(
    _BaseIdentityAwareProxyAdminServiceRestTransport
):
    """REST backend synchronous transport for IdentityAwareProxyAdminService.

    APIs for Identity-Aware Proxy Admin configurations.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "iap.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[IdentityAwareProxyAdminServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'iap.googleapis.com').
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
            interceptor (Optional[IdentityAwareProxyAdminServiceRestInterceptor]): Interceptor used
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
        self._interceptor = (
            interceptor or IdentityAwareProxyAdminServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _CreateTunnelDestGroup(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseCreateTunnelDestGroup,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyAdminServiceRestTransport.CreateTunnelDestGroup"
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
            request: service.CreateTunnelDestGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.TunnelDestGroup:
            r"""Call the create tunnel dest group method over HTTP.

            Args:
                request (~.service.CreateTunnelDestGroupRequest):
                    The request object. The request to CreateTunnelDestGroup.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.TunnelDestGroup:
                    A TunnelDestGroup.
            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseCreateTunnelDestGroup._get_http_options()
            request, metadata = self._interceptor.pre_create_tunnel_dest_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseCreateTunnelDestGroup,
                    "_BaseCreateTunnelDestGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.CreateTunnelDestGroup",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "CreateTunnelDestGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._CreateTunnelDestGroup._get_response(
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
            resp = service.TunnelDestGroup()
            pb_resp = service.TunnelDestGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_tunnel_dest_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_tunnel_dest_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.TunnelDestGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.create_tunnel_dest_group",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "CreateTunnelDestGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTunnelDestGroup(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseDeleteTunnelDestGroup,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyAdminServiceRestTransport.DeleteTunnelDestGroup"
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
            request: service.DeleteTunnelDestGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete tunnel dest group method over HTTP.

            Args:
                request (~.service.DeleteTunnelDestGroupRequest):
                    The request object. The request to DeleteTunnelDestGroup.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseDeleteTunnelDestGroup._get_http_options()
            request, metadata = self._interceptor.pre_delete_tunnel_dest_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseDeleteTunnelDestGroup,
                    "_BaseDeleteTunnelDestGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.DeleteTunnelDestGroup",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "DeleteTunnelDestGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._DeleteTunnelDestGroup._get_response(
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

    class _GetIamPolicy(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetIamPolicy,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("IdentityAwareProxyAdminServiceRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (~.iam_policy_pb2.GetIamPolicyRequest):
                    The request object. Request message for ``GetIamPolicy`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.policy_pb2.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources.

                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role.

                For some types of Google Cloud resources, a ``binding``
                can also specify a ``condition``, which is a logical
                expression that allows access to a resource only if the
                expression evaluates to ``true``. A condition can add
                constraints based on attributes of the request, the
                resource, or both. To learn which resources support
                conditions in their IAM policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.

                **JSON example:**

                ::

                       {
                         "bindings": [
                           {
                             "role": "roles/resourcemanager.organizationAdmin",
                             "members": [
                               "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                             ]
                           },
                           {
                             "role": "roles/resourcemanager.organizationViewer",
                             "members": [
                               "user:eve@example.com"
                             ],
                             "condition": {
                               "title": "expirable access",
                               "description": "Does not grant access after Sep 2020",
                               "expression": "request.time <
                               timestamp('2020-10-01T00:00:00.000Z')",
                             }
                           }
                         ],
                         "etag": "BwWWja0YfJA=",
                         "version": 3
                       }

                **YAML example:**

                ::

                       bindings:
                       - members:
                         - user:mike@example.com
                         - group:admins@example.com
                         - domain:google.com
                         - serviceAccount:my-project-id@appspot.gserviceaccount.com
                         role: roles/resourcemanager.organizationAdmin
                       - members:
                         - user:eve@example.com
                         role: roles/resourcemanager.organizationViewer
                         condition:
                           title: expirable access
                           description: Does not grant access after Sep 2020
                           expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
                       etag: BwWWja0YfJA=
                       version: 3

                For a description of IAM and its features, see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IdentityAwareProxyAdminServiceRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_iam_policy_with_metadata(
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
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.get_iam_policy",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "GetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIapSettings(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetIapSettings,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("IdentityAwareProxyAdminServiceRestTransport.GetIapSettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.GetIapSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.IapSettings:
            r"""Call the get iap settings method over HTTP.

            Args:
                request (~.service.GetIapSettingsRequest):
                    The request object. The request sent to GetIapSettings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.IapSettings:
                    The IAP configurable settings.
            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetIapSettings._get_http_options()
            request, metadata = self._interceptor.pre_get_iap_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetIapSettings,
                    "_BaseGetIapSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.GetIapSettings",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "GetIapSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._GetIapSettings._get_response(
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
            resp = service.IapSettings()
            pb_resp = service.IapSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_iap_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_iap_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.IapSettings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.get_iap_settings",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "GetIapSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTunnelDestGroup(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetTunnelDestGroup,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyAdminServiceRestTransport.GetTunnelDestGroup"
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
            request: service.GetTunnelDestGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.TunnelDestGroup:
            r"""Call the get tunnel dest group method over HTTP.

            Args:
                request (~.service.GetTunnelDestGroupRequest):
                    The request object. The request to GetTunnelDestGroup.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.TunnelDestGroup:
                    A TunnelDestGroup.
            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetTunnelDestGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_tunnel_dest_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseGetTunnelDestGroup,
                    "_BaseGetTunnelDestGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.GetTunnelDestGroup",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "GetTunnelDestGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._GetTunnelDestGroup._get_response(
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
            resp = service.TunnelDestGroup()
            pb_resp = service.TunnelDestGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_tunnel_dest_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_tunnel_dest_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.TunnelDestGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.get_tunnel_dest_group",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "GetTunnelDestGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTunnelDestGroups(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseListTunnelDestGroups,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyAdminServiceRestTransport.ListTunnelDestGroups"
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
            request: service.ListTunnelDestGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListTunnelDestGroupsResponse:
            r"""Call the list tunnel dest groups method over HTTP.

            Args:
                request (~.service.ListTunnelDestGroupsRequest):
                    The request object. The request to ListTunnelDestGroups.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListTunnelDestGroupsResponse:
                    The response from
                ListTunnelDestGroups.

            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseListTunnelDestGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_tunnel_dest_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseListTunnelDestGroups,
                    "_BaseListTunnelDestGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.ListTunnelDestGroups",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "ListTunnelDestGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._ListTunnelDestGroups._get_response(
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
            resp = service.ListTunnelDestGroupsResponse()
            pb_resp = service.ListTunnelDestGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tunnel_dest_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tunnel_dest_groups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListTunnelDestGroupsResponse.to_json(
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
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.list_tunnel_dest_groups",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "ListTunnelDestGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetIamPolicy(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseSetIamPolicy,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("IdentityAwareProxyAdminServiceRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                request (~.iam_policy_pb2.SetIamPolicyRequest):
                    The request object. Request message for ``SetIamPolicy`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.policy_pb2.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources.

                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role.

                For some types of Google Cloud resources, a ``binding``
                can also specify a ``condition``, which is a logical
                expression that allows access to a resource only if the
                expression evaluates to ``true``. A condition can add
                constraints based on attributes of the request, the
                resource, or both. To learn which resources support
                conditions in their IAM policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.

                **JSON example:**

                ::

                       {
                         "bindings": [
                           {
                             "role": "roles/resourcemanager.organizationAdmin",
                             "members": [
                               "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                             ]
                           },
                           {
                             "role": "roles/resourcemanager.organizationViewer",
                             "members": [
                               "user:eve@example.com"
                             ],
                             "condition": {
                               "title": "expirable access",
                               "description": "Does not grant access after Sep 2020",
                               "expression": "request.time <
                               timestamp('2020-10-01T00:00:00.000Z')",
                             }
                           }
                         ],
                         "etag": "BwWWja0YfJA=",
                         "version": 3
                       }

                **YAML example:**

                ::

                       bindings:
                       - members:
                         - user:mike@example.com
                         - group:admins@example.com
                         - domain:google.com
                         - serviceAccount:my-project-id@appspot.gserviceaccount.com
                         role: roles/resourcemanager.organizationAdmin
                       - members:
                         - user:eve@example.com
                         role: roles/resourcemanager.organizationViewer
                         condition:
                           title: expirable access
                           description: Does not grant access after Sep 2020
                           expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
                       etag: BwWWja0YfJA=
                       version: 3

                For a description of IAM and its features, see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IdentityAwareProxyAdminServiceRestTransport._SetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_iam_policy_with_metadata(
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
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.set_iam_policy",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "SetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestIamPermissions(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseTestIamPermissions,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyAdminServiceRestTransport.TestIamPermissions"
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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (~.iam_policy_pb2.TestIamPermissionsRequest):
                    The request object. Request message for ``TestIamPermissions`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.iam_policy_pb2.TestIamPermissionsResponse:
                    Response message for ``TestIamPermissions`` method.
            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._TestIamPermissions._get_response(
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
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_test_iam_permissions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_test_iam_permissions_with_metadata(
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
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.test_iam_permissions",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "TestIamPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateIapSettings(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseUpdateIapSettings,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("IdentityAwareProxyAdminServiceRestTransport.UpdateIapSettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: service.UpdateIapSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.IapSettings:
            r"""Call the update iap settings method over HTTP.

            Args:
                request (~.service.UpdateIapSettingsRequest):
                    The request object. The request sent to
                UpdateIapSettings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.IapSettings:
                    The IAP configurable settings.
            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseUpdateIapSettings._get_http_options()
            request, metadata = self._interceptor.pre_update_iap_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseUpdateIapSettings,
                    "_BaseUpdateIapSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.UpdateIapSettings",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "UpdateIapSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._UpdateIapSettings._get_response(
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
            resp = service.IapSettings()
            pb_resp = service.IapSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_iap_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_iap_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.IapSettings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.update_iap_settings",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "UpdateIapSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTunnelDestGroup(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseUpdateTunnelDestGroup,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyAdminServiceRestTransport.UpdateTunnelDestGroup"
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
            request: service.UpdateTunnelDestGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.TunnelDestGroup:
            r"""Call the update tunnel dest group method over HTTP.

            Args:
                request (~.service.UpdateTunnelDestGroupRequest):
                    The request object. The request to UpdateTunnelDestGroup.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.TunnelDestGroup:
                    A TunnelDestGroup.
            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseUpdateTunnelDestGroup._get_http_options()
            request, metadata = self._interceptor.pre_update_tunnel_dest_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseUpdateTunnelDestGroup,
                    "_BaseUpdateTunnelDestGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.UpdateTunnelDestGroup",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "UpdateTunnelDestGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._UpdateTunnelDestGroup._get_response(
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
            resp = service.TunnelDestGroup()
            pb_resp = service.TunnelDestGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_tunnel_dest_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_tunnel_dest_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.TunnelDestGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.update_tunnel_dest_group",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "UpdateTunnelDestGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ValidateIapAttributeExpression(
        _BaseIdentityAwareProxyAdminServiceRestTransport._BaseValidateIapAttributeExpression,
        IdentityAwareProxyAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyAdminServiceRestTransport.ValidateIapAttributeExpression"
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
            request: service.ValidateIapAttributeExpressionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ValidateIapAttributeExpressionResponse:
            r"""Call the validate iap attribute
            expression method over HTTP.

                Args:
                    request (~.service.ValidateIapAttributeExpressionRequest):
                        The request object. Request sent to IAP Expression Linter
                    endpoint.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.ValidateIapAttributeExpressionResponse:
                        IAP Expression Linter endpoint
                    returns empty response body.

            """

            http_options = _BaseIdentityAwareProxyAdminServiceRestTransport._BaseValidateIapAttributeExpression._get_http_options()
            request, metadata = self._interceptor.pre_validate_iap_attribute_expression(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyAdminServiceRestTransport._BaseValidateIapAttributeExpression,
                    "_BaseValidateIapAttributeExpression__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.ValidateIapAttributeExpression",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "ValidateIapAttributeExpression",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyAdminServiceRestTransport._ValidateIapAttributeExpression._get_response(
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
            resp = service.ValidateIapAttributeExpressionResponse()
            pb_resp = service.ValidateIapAttributeExpressionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_validate_iap_attribute_expression(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_validate_iap_attribute_expression_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.ValidateIapAttributeExpressionResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyAdminServiceClient.validate_iap_attribute_expression",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyAdminService",
                        "rpcName": "ValidateIapAttributeExpression",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_tunnel_dest_group(
        self,
    ) -> Callable[[service.CreateTunnelDestGroupRequest], service.TunnelDestGroup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTunnelDestGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tunnel_dest_group(
        self,
    ) -> Callable[[service.DeleteTunnelDestGroupRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTunnelDestGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iap_settings(
        self,
    ) -> Callable[[service.GetIapSettingsRequest], service.IapSettings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIapSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tunnel_dest_group(
        self,
    ) -> Callable[[service.GetTunnelDestGroupRequest], service.TunnelDestGroup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTunnelDestGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tunnel_dest_groups(
        self,
    ) -> Callable[
        [service.ListTunnelDestGroupsRequest], service.ListTunnelDestGroupsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTunnelDestGroups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_iap_settings(
        self,
    ) -> Callable[[service.UpdateIapSettingsRequest], service.IapSettings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateIapSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tunnel_dest_group(
        self,
    ) -> Callable[[service.UpdateTunnelDestGroupRequest], service.TunnelDestGroup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTunnelDestGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def validate_iap_attribute_expression(
        self,
    ) -> Callable[
        [service.ValidateIapAttributeExpressionRequest],
        service.ValidateIapAttributeExpressionResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateIapAttributeExpression(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("IdentityAwareProxyAdminServiceRestTransport",)
