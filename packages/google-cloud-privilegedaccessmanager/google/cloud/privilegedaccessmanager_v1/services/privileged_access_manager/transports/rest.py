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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.privilegedaccessmanager_v1._compat import transcode_request
from google.cloud.privilegedaccessmanager_v1.types import privilegedaccessmanager

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BasePrivilegedAccessManagerRestTransport

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


class PrivilegedAccessManagerRestInterceptor:
    """Interceptor for PrivilegedAccessManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PrivilegedAccessManagerRestTransport.

    .. code-block:: python
        class MyCustomPrivilegedAccessManagerInterceptor(PrivilegedAccessManagerRestInterceptor):
            def pre_approve_grant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_approve_grant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_check_onboarding_status(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_check_onboarding_status(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_entitlement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_entitlement(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_grant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_grant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_entitlement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_entitlement(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deny_grant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deny_grant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_entitlement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_entitlement(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_grant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_grant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_entitlements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_entitlements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_grants(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_grants(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_revoke_grant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_revoke_grant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_entitlements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_entitlements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_grants(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_grants(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_entitlement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_entitlement(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PrivilegedAccessManagerRestTransport(interceptor=MyCustomPrivilegedAccessManagerInterceptor())
        client = PrivilegedAccessManagerClient(transport=transport)


    """

    def pre_approve_grant(
        self,
        request: privilegedaccessmanager.ApproveGrantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.ApproveGrantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for approve_grant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_approve_grant(
        self, response: privilegedaccessmanager.Grant
    ) -> privilegedaccessmanager.Grant:
        """Post-rpc interceptor for approve_grant

        DEPRECATED. Please use the `post_approve_grant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_approve_grant` interceptor runs
        before the `post_approve_grant_with_metadata` interceptor.
        """
        return response

    def post_approve_grant_with_metadata(
        self,
        response: privilegedaccessmanager.Grant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[privilegedaccessmanager.Grant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for approve_grant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_approve_grant_with_metadata`
        interceptor in new development instead of the `post_approve_grant` interceptor.
        When both interceptors are used, this `post_approve_grant_with_metadata` interceptor runs after the
        `post_approve_grant` interceptor. The (possibly modified) response returned by
        `post_approve_grant` will be passed to
        `post_approve_grant_with_metadata`.
        """
        return response, metadata

    def pre_check_onboarding_status(
        self,
        request: privilegedaccessmanager.CheckOnboardingStatusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.CheckOnboardingStatusRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for check_onboarding_status

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_check_onboarding_status(
        self, response: privilegedaccessmanager.CheckOnboardingStatusResponse
    ) -> privilegedaccessmanager.CheckOnboardingStatusResponse:
        """Post-rpc interceptor for check_onboarding_status

        DEPRECATED. Please use the `post_check_onboarding_status_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_check_onboarding_status` interceptor runs
        before the `post_check_onboarding_status_with_metadata` interceptor.
        """
        return response

    def post_check_onboarding_status_with_metadata(
        self,
        response: privilegedaccessmanager.CheckOnboardingStatusResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.CheckOnboardingStatusResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for check_onboarding_status

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_check_onboarding_status_with_metadata`
        interceptor in new development instead of the `post_check_onboarding_status` interceptor.
        When both interceptors are used, this `post_check_onboarding_status_with_metadata` interceptor runs after the
        `post_check_onboarding_status` interceptor. The (possibly modified) response returned by
        `post_check_onboarding_status` will be passed to
        `post_check_onboarding_status_with_metadata`.
        """
        return response, metadata

    def pre_create_entitlement(
        self,
        request: privilegedaccessmanager.CreateEntitlementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.CreateEntitlementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_entitlement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_create_entitlement(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_entitlement

        DEPRECATED. Please use the `post_create_entitlement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_create_entitlement` interceptor runs
        before the `post_create_entitlement_with_metadata` interceptor.
        """
        return response

    def post_create_entitlement_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_entitlement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_create_entitlement_with_metadata`
        interceptor in new development instead of the `post_create_entitlement` interceptor.
        When both interceptors are used, this `post_create_entitlement_with_metadata` interceptor runs after the
        `post_create_entitlement` interceptor. The (possibly modified) response returned by
        `post_create_entitlement` will be passed to
        `post_create_entitlement_with_metadata`.
        """
        return response, metadata

    def pre_create_grant(
        self,
        request: privilegedaccessmanager.CreateGrantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.CreateGrantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_grant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_create_grant(
        self, response: privilegedaccessmanager.Grant
    ) -> privilegedaccessmanager.Grant:
        """Post-rpc interceptor for create_grant

        DEPRECATED. Please use the `post_create_grant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_create_grant` interceptor runs
        before the `post_create_grant_with_metadata` interceptor.
        """
        return response

    def post_create_grant_with_metadata(
        self,
        response: privilegedaccessmanager.Grant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[privilegedaccessmanager.Grant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_grant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_create_grant_with_metadata`
        interceptor in new development instead of the `post_create_grant` interceptor.
        When both interceptors are used, this `post_create_grant_with_metadata` interceptor runs after the
        `post_create_grant` interceptor. The (possibly modified) response returned by
        `post_create_grant` will be passed to
        `post_create_grant_with_metadata`.
        """
        return response, metadata

    def pre_delete_entitlement(
        self,
        request: privilegedaccessmanager.DeleteEntitlementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.DeleteEntitlementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_entitlement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_delete_entitlement(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_entitlement

        DEPRECATED. Please use the `post_delete_entitlement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_delete_entitlement` interceptor runs
        before the `post_delete_entitlement_with_metadata` interceptor.
        """
        return response

    def post_delete_entitlement_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_entitlement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_delete_entitlement_with_metadata`
        interceptor in new development instead of the `post_delete_entitlement` interceptor.
        When both interceptors are used, this `post_delete_entitlement_with_metadata` interceptor runs after the
        `post_delete_entitlement` interceptor. The (possibly modified) response returned by
        `post_delete_entitlement` will be passed to
        `post_delete_entitlement_with_metadata`.
        """
        return response, metadata

    def pre_deny_grant(
        self,
        request: privilegedaccessmanager.DenyGrantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.DenyGrantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for deny_grant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_deny_grant(
        self, response: privilegedaccessmanager.Grant
    ) -> privilegedaccessmanager.Grant:
        """Post-rpc interceptor for deny_grant

        DEPRECATED. Please use the `post_deny_grant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_deny_grant` interceptor runs
        before the `post_deny_grant_with_metadata` interceptor.
        """
        return response

    def post_deny_grant_with_metadata(
        self,
        response: privilegedaccessmanager.Grant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[privilegedaccessmanager.Grant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deny_grant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_deny_grant_with_metadata`
        interceptor in new development instead of the `post_deny_grant` interceptor.
        When both interceptors are used, this `post_deny_grant_with_metadata` interceptor runs after the
        `post_deny_grant` interceptor. The (possibly modified) response returned by
        `post_deny_grant` will be passed to
        `post_deny_grant_with_metadata`.
        """
        return response, metadata

    def pre_get_entitlement(
        self,
        request: privilegedaccessmanager.GetEntitlementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.GetEntitlementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_entitlement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_get_entitlement(
        self, response: privilegedaccessmanager.Entitlement
    ) -> privilegedaccessmanager.Entitlement:
        """Post-rpc interceptor for get_entitlement

        DEPRECATED. Please use the `post_get_entitlement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_get_entitlement` interceptor runs
        before the `post_get_entitlement_with_metadata` interceptor.
        """
        return response

    def post_get_entitlement_with_metadata(
        self,
        response: privilegedaccessmanager.Entitlement,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.Entitlement, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_entitlement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_get_entitlement_with_metadata`
        interceptor in new development instead of the `post_get_entitlement` interceptor.
        When both interceptors are used, this `post_get_entitlement_with_metadata` interceptor runs after the
        `post_get_entitlement` interceptor. The (possibly modified) response returned by
        `post_get_entitlement` will be passed to
        `post_get_entitlement_with_metadata`.
        """
        return response, metadata

    def pre_get_grant(
        self,
        request: privilegedaccessmanager.GetGrantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.GetGrantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_grant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_get_grant(
        self, response: privilegedaccessmanager.Grant
    ) -> privilegedaccessmanager.Grant:
        """Post-rpc interceptor for get_grant

        DEPRECATED. Please use the `post_get_grant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_get_grant` interceptor runs
        before the `post_get_grant_with_metadata` interceptor.
        """
        return response

    def post_get_grant_with_metadata(
        self,
        response: privilegedaccessmanager.Grant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[privilegedaccessmanager.Grant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_grant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_get_grant_with_metadata`
        interceptor in new development instead of the `post_get_grant` interceptor.
        When both interceptors are used, this `post_get_grant_with_metadata` interceptor runs after the
        `post_get_grant` interceptor. The (possibly modified) response returned by
        `post_get_grant` will be passed to
        `post_get_grant_with_metadata`.
        """
        return response, metadata

    def pre_list_entitlements(
        self,
        request: privilegedaccessmanager.ListEntitlementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.ListEntitlementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_entitlements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_list_entitlements(
        self, response: privilegedaccessmanager.ListEntitlementsResponse
    ) -> privilegedaccessmanager.ListEntitlementsResponse:
        """Post-rpc interceptor for list_entitlements

        DEPRECATED. Please use the `post_list_entitlements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_list_entitlements` interceptor runs
        before the `post_list_entitlements_with_metadata` interceptor.
        """
        return response

    def post_list_entitlements_with_metadata(
        self,
        response: privilegedaccessmanager.ListEntitlementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.ListEntitlementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_entitlements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_list_entitlements_with_metadata`
        interceptor in new development instead of the `post_list_entitlements` interceptor.
        When both interceptors are used, this `post_list_entitlements_with_metadata` interceptor runs after the
        `post_list_entitlements` interceptor. The (possibly modified) response returned by
        `post_list_entitlements` will be passed to
        `post_list_entitlements_with_metadata`.
        """
        return response, metadata

    def pre_list_grants(
        self,
        request: privilegedaccessmanager.ListGrantsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.ListGrantsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_grants

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_list_grants(
        self, response: privilegedaccessmanager.ListGrantsResponse
    ) -> privilegedaccessmanager.ListGrantsResponse:
        """Post-rpc interceptor for list_grants

        DEPRECATED. Please use the `post_list_grants_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_list_grants` interceptor runs
        before the `post_list_grants_with_metadata` interceptor.
        """
        return response

    def post_list_grants_with_metadata(
        self,
        response: privilegedaccessmanager.ListGrantsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.ListGrantsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_grants

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_list_grants_with_metadata`
        interceptor in new development instead of the `post_list_grants` interceptor.
        When both interceptors are used, this `post_list_grants_with_metadata` interceptor runs after the
        `post_list_grants` interceptor. The (possibly modified) response returned by
        `post_list_grants` will be passed to
        `post_list_grants_with_metadata`.
        """
        return response, metadata

    def pre_revoke_grant(
        self,
        request: privilegedaccessmanager.RevokeGrantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.RevokeGrantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for revoke_grant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_revoke_grant(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for revoke_grant

        DEPRECATED. Please use the `post_revoke_grant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_revoke_grant` interceptor runs
        before the `post_revoke_grant_with_metadata` interceptor.
        """
        return response

    def post_revoke_grant_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for revoke_grant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_revoke_grant_with_metadata`
        interceptor in new development instead of the `post_revoke_grant` interceptor.
        When both interceptors are used, this `post_revoke_grant_with_metadata` interceptor runs after the
        `post_revoke_grant` interceptor. The (possibly modified) response returned by
        `post_revoke_grant` will be passed to
        `post_revoke_grant_with_metadata`.
        """
        return response, metadata

    def pre_search_entitlements(
        self,
        request: privilegedaccessmanager.SearchEntitlementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.SearchEntitlementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_entitlements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_search_entitlements(
        self, response: privilegedaccessmanager.SearchEntitlementsResponse
    ) -> privilegedaccessmanager.SearchEntitlementsResponse:
        """Post-rpc interceptor for search_entitlements

        DEPRECATED. Please use the `post_search_entitlements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_search_entitlements` interceptor runs
        before the `post_search_entitlements_with_metadata` interceptor.
        """
        return response

    def post_search_entitlements_with_metadata(
        self,
        response: privilegedaccessmanager.SearchEntitlementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.SearchEntitlementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_entitlements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_search_entitlements_with_metadata`
        interceptor in new development instead of the `post_search_entitlements` interceptor.
        When both interceptors are used, this `post_search_entitlements_with_metadata` interceptor runs after the
        `post_search_entitlements` interceptor. The (possibly modified) response returned by
        `post_search_entitlements` will be passed to
        `post_search_entitlements_with_metadata`.
        """
        return response, metadata

    def pre_search_grants(
        self,
        request: privilegedaccessmanager.SearchGrantsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.SearchGrantsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_grants

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_search_grants(
        self, response: privilegedaccessmanager.SearchGrantsResponse
    ) -> privilegedaccessmanager.SearchGrantsResponse:
        """Post-rpc interceptor for search_grants

        DEPRECATED. Please use the `post_search_grants_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_search_grants` interceptor runs
        before the `post_search_grants_with_metadata` interceptor.
        """
        return response

    def post_search_grants_with_metadata(
        self,
        response: privilegedaccessmanager.SearchGrantsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.SearchGrantsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_grants

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_search_grants_with_metadata`
        interceptor in new development instead of the `post_search_grants` interceptor.
        When both interceptors are used, this `post_search_grants_with_metadata` interceptor runs after the
        `post_search_grants` interceptor. The (possibly modified) response returned by
        `post_search_grants` will be passed to
        `post_search_grants_with_metadata`.
        """
        return response, metadata

    def pre_update_entitlement(
        self,
        request: privilegedaccessmanager.UpdateEntitlementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        privilegedaccessmanager.UpdateEntitlementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_entitlement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_update_entitlement(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_entitlement

        DEPRECATED. Please use the `post_update_entitlement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code. This `post_update_entitlement` interceptor runs
        before the `post_update_entitlement_with_metadata` interceptor.
        """
        return response

    def post_update_entitlement_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_entitlement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PrivilegedAccessManager server but before it is returned to user code.

        We recommend only using this `post_update_entitlement_with_metadata`
        interceptor in new development instead of the `post_update_entitlement` interceptor.
        When both interceptors are used, this `post_update_entitlement_with_metadata` interceptor runs after the
        `post_update_entitlement` interceptor. The (possibly modified) response returned by
        `post_update_entitlement` will be passed to
        `post_update_entitlement_with_metadata`.
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
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
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
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
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
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
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
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
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
        before they are sent to the PrivilegedAccessManager server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the PrivilegedAccessManager server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class PrivilegedAccessManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PrivilegedAccessManagerRestInterceptor


class PrivilegedAccessManagerRestTransport(_BasePrivilegedAccessManagerRestTransport):
    """REST backend synchronous transport for PrivilegedAccessManager.

    This API allows customers to manage temporary, request based
    privileged access to their resources.

    It defines the following resource model:

    - A collection of ``Entitlement`` resources. An entitlement allows
      configuring (among other things):

      - Some kind of privileged access that users can request.
      - A set of users called *requesters* who can request this access.
      - A maximum duration for which the access can be requested.
      - An optional approval workflow which must be satisfied before
        access is granted.

    - A collection of ``Grant`` resources. A grant is a request by a
      requester to get the privileged access specified in an entitlement
      for some duration.

      After the approval workflow as specified in the entitlement is
      satisfied, the specified access is given to the requester. The
      access is automatically taken back after the requested duration is
      over.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "privilegedaccessmanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[PrivilegedAccessManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'privilegedaccessmanager.googleapis.com').
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
            interceptor (Optional[PrivilegedAccessManagerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or PrivilegedAccessManagerRestInterceptor()
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
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=folders/*/locations/*/operations/*}",
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
                    {
                        "method": "get",
                        "uri": "/v1/{name=folders/*/locations/*/operations/*}",
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
                    {
                        "method": "get",
                        "uri": "/v1/{name=folders/*/locations/*}/operations",
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

    class _ApproveGrant(
        _BasePrivilegedAccessManagerRestTransport._BaseApproveGrant,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.ApproveGrant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.ApproveGrantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.Grant:
            r"""Call the approve grant method over HTTP.

            Args:
                request (~.privilegedaccessmanager.ApproveGrantRequest):
                    The request object. Request message for ``ApproveGrant`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.Grant:
                    A grant represents a request from a
                user for obtaining the access specified
                in an entitlement they are eligible for.

            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseApproveGrant._get_http_options()
            request, metadata = self._interceptor.pre_approve_grant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseApproveGrant,
                    "_BaseApproveGrant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.ApproveGrant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ApproveGrant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._ApproveGrant._get_response(
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
            resp = privilegedaccessmanager.Grant()
            pb_resp = privilegedaccessmanager.Grant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_approve_grant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_approve_grant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = privilegedaccessmanager.Grant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.approve_grant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ApproveGrant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CheckOnboardingStatus(
        _BasePrivilegedAccessManagerRestTransport._BaseCheckOnboardingStatus,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.CheckOnboardingStatus")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.CheckOnboardingStatusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.CheckOnboardingStatusResponse:
            r"""Call the check onboarding status method over HTTP.

            Args:
                request (~.privilegedaccessmanager.CheckOnboardingStatusRequest):
                    The request object. Request message for ``CheckOnboardingStatus`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.CheckOnboardingStatusResponse:
                    Response message for ``CheckOnboardingStatus`` method.
            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseCheckOnboardingStatus._get_http_options()
            request, metadata = self._interceptor.pre_check_onboarding_status(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseCheckOnboardingStatus,
                    "_BaseCheckOnboardingStatus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.CheckOnboardingStatus",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "CheckOnboardingStatus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._CheckOnboardingStatus._get_response(
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
            resp = privilegedaccessmanager.CheckOnboardingStatusResponse()
            pb_resp = privilegedaccessmanager.CheckOnboardingStatusResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_check_onboarding_status(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_check_onboarding_status_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        privilegedaccessmanager.CheckOnboardingStatusResponse.to_json(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.check_onboarding_status",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "CheckOnboardingStatus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEntitlement(
        _BasePrivilegedAccessManagerRestTransport._BaseCreateEntitlement,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.CreateEntitlement")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.CreateEntitlementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create entitlement method over HTTP.

            Args:
                request (~.privilegedaccessmanager.CreateEntitlementRequest):
                    The request object. Message for creating an entitlement.
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseCreateEntitlement._get_http_options()
            request, metadata = self._interceptor.pre_create_entitlement(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseCreateEntitlement,
                    "_BaseCreateEntitlement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.CreateEntitlement",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "CreateEntitlement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._CreateEntitlement._get_response(
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

            resp = self._interceptor.post_create_entitlement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_entitlement_with_metadata(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.create_entitlement",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "CreateEntitlement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGrant(
        _BasePrivilegedAccessManagerRestTransport._BaseCreateGrant,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.CreateGrant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.CreateGrantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.Grant:
            r"""Call the create grant method over HTTP.

            Args:
                request (~.privilegedaccessmanager.CreateGrantRequest):
                    The request object. Message for creating a grant
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.Grant:
                    A grant represents a request from a
                user for obtaining the access specified
                in an entitlement they are eligible for.

            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseCreateGrant._get_http_options()
            request, metadata = self._interceptor.pre_create_grant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseCreateGrant,
                    "_BaseCreateGrant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.CreateGrant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "CreateGrant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._CreateGrant._get_response(
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
            resp = privilegedaccessmanager.Grant()
            pb_resp = privilegedaccessmanager.Grant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_grant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_grant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = privilegedaccessmanager.Grant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.create_grant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "CreateGrant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEntitlement(
        _BasePrivilegedAccessManagerRestTransport._BaseDeleteEntitlement,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.DeleteEntitlement")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.DeleteEntitlementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete entitlement method over HTTP.

            Args:
                request (~.privilegedaccessmanager.DeleteEntitlementRequest):
                    The request object. Message for deleting an entitlement.
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseDeleteEntitlement._get_http_options()
            request, metadata = self._interceptor.pre_delete_entitlement(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseDeleteEntitlement,
                    "_BaseDeleteEntitlement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.DeleteEntitlement",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "DeleteEntitlement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._DeleteEntitlement._get_response(
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

            resp = self._interceptor.post_delete_entitlement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_entitlement_with_metadata(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.delete_entitlement",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "DeleteEntitlement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DenyGrant(
        _BasePrivilegedAccessManagerRestTransport._BaseDenyGrant,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.DenyGrant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.DenyGrantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.Grant:
            r"""Call the deny grant method over HTTP.

            Args:
                request (~.privilegedaccessmanager.DenyGrantRequest):
                    The request object. Request message for ``DenyGrant`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.Grant:
                    A grant represents a request from a
                user for obtaining the access specified
                in an entitlement they are eligible for.

            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseDenyGrant._get_http_options()
            request, metadata = self._interceptor.pre_deny_grant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseDenyGrant,
                    "_BaseDenyGrant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.DenyGrant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "DenyGrant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._DenyGrant._get_response(
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
            resp = privilegedaccessmanager.Grant()
            pb_resp = privilegedaccessmanager.Grant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_deny_grant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deny_grant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = privilegedaccessmanager.Grant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.deny_grant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "DenyGrant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEntitlement(
        _BasePrivilegedAccessManagerRestTransport._BaseGetEntitlement,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.GetEntitlement")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.GetEntitlementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.Entitlement:
            r"""Call the get entitlement method over HTTP.

            Args:
                request (~.privilegedaccessmanager.GetEntitlementRequest):
                    The request object. Message for getting an entitlement.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.Entitlement:
                    An entitlement defines the
                eligibility of a set of users to obtain
                predefined access for some time possibly
                after going through an approval
                workflow.

            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseGetEntitlement._get_http_options()
            request, metadata = self._interceptor.pre_get_entitlement(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseGetEntitlement,
                    "_BaseGetEntitlement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.GetEntitlement",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "GetEntitlement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._GetEntitlement._get_response(
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
            resp = privilegedaccessmanager.Entitlement()
            pb_resp = privilegedaccessmanager.Entitlement.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_entitlement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_entitlement_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = privilegedaccessmanager.Entitlement.to_json(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.get_entitlement",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "GetEntitlement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGrant(
        _BasePrivilegedAccessManagerRestTransport._BaseGetGrant,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.GetGrant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.GetGrantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.Grant:
            r"""Call the get grant method over HTTP.

            Args:
                request (~.privilegedaccessmanager.GetGrantRequest):
                    The request object. Message for getting a grant.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.Grant:
                    A grant represents a request from a
                user for obtaining the access specified
                in an entitlement they are eligible for.

            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseGetGrant._get_http_options()
            request, metadata = self._interceptor.pre_get_grant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseGetGrant,
                    "_BaseGetGrant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.GetGrant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "GetGrant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._GetGrant._get_response(
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
            resp = privilegedaccessmanager.Grant()
            pb_resp = privilegedaccessmanager.Grant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_grant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_grant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = privilegedaccessmanager.Grant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.get_grant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "GetGrant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEntitlements(
        _BasePrivilegedAccessManagerRestTransport._BaseListEntitlements,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.ListEntitlements")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.ListEntitlementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.ListEntitlementsResponse:
            r"""Call the list entitlements method over HTTP.

            Args:
                request (~.privilegedaccessmanager.ListEntitlementsRequest):
                    The request object. Message for requesting list of
                entitlements.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.ListEntitlementsResponse:
                    Message for response to listing
                entitlements.

            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseListEntitlements._get_http_options()
            request, metadata = self._interceptor.pre_list_entitlements(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseListEntitlements,
                    "_BaseListEntitlements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.ListEntitlements",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ListEntitlements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._ListEntitlements._get_response(
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
            resp = privilegedaccessmanager.ListEntitlementsResponse()
            pb_resp = privilegedaccessmanager.ListEntitlementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_entitlements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_entitlements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        privilegedaccessmanager.ListEntitlementsResponse.to_json(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.list_entitlements",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ListEntitlements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGrants(
        _BasePrivilegedAccessManagerRestTransport._BaseListGrants,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.ListGrants")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.ListGrantsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.ListGrantsResponse:
            r"""Call the list grants method over HTTP.

            Args:
                request (~.privilegedaccessmanager.ListGrantsRequest):
                    The request object. Message for requesting list of
                grants.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.ListGrantsResponse:
                    Message for response to listing
                grants.

            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseListGrants._get_http_options()
            request, metadata = self._interceptor.pre_list_grants(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseListGrants,
                    "_BaseListGrants__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.ListGrants",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ListGrants",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._ListGrants._get_response(
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
            resp = privilegedaccessmanager.ListGrantsResponse()
            pb_resp = privilegedaccessmanager.ListGrantsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_grants(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_grants_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        privilegedaccessmanager.ListGrantsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.list_grants",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ListGrants",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RevokeGrant(
        _BasePrivilegedAccessManagerRestTransport._BaseRevokeGrant,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.RevokeGrant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.RevokeGrantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the revoke grant method over HTTP.

            Args:
                request (~.privilegedaccessmanager.RevokeGrantRequest):
                    The request object. Request message for ``RevokeGrant`` method.
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseRevokeGrant._get_http_options()
            request, metadata = self._interceptor.pre_revoke_grant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseRevokeGrant,
                    "_BaseRevokeGrant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.RevokeGrant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "RevokeGrant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._RevokeGrant._get_response(
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

            resp = self._interceptor.post_revoke_grant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_revoke_grant_with_metadata(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.revoke_grant",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "RevokeGrant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchEntitlements(
        _BasePrivilegedAccessManagerRestTransport._BaseSearchEntitlements,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.SearchEntitlements")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.SearchEntitlementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.SearchEntitlementsResponse:
            r"""Call the search entitlements method over HTTP.

            Args:
                request (~.privilegedaccessmanager.SearchEntitlementsRequest):
                    The request object. Request message for ``SearchEntitlements`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.SearchEntitlementsResponse:
                    Response message for ``SearchEntitlements`` method.
            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseSearchEntitlements._get_http_options()
            request, metadata = self._interceptor.pre_search_entitlements(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseSearchEntitlements,
                    "_BaseSearchEntitlements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.SearchEntitlements",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "SearchEntitlements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._SearchEntitlements._get_response(
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
            resp = privilegedaccessmanager.SearchEntitlementsResponse()
            pb_resp = privilegedaccessmanager.SearchEntitlementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_entitlements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_entitlements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        privilegedaccessmanager.SearchEntitlementsResponse.to_json(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.search_entitlements",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "SearchEntitlements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchGrants(
        _BasePrivilegedAccessManagerRestTransport._BaseSearchGrants,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.SearchGrants")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.SearchGrantsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> privilegedaccessmanager.SearchGrantsResponse:
            r"""Call the search grants method over HTTP.

            Args:
                request (~.privilegedaccessmanager.SearchGrantsRequest):
                    The request object. Request message for ``SearchGrants`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.privilegedaccessmanager.SearchGrantsResponse:
                    Response message for ``SearchGrants`` method.
            """

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseSearchGrants._get_http_options()
            request, metadata = self._interceptor.pre_search_grants(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseSearchGrants,
                    "_BaseSearchGrants__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.SearchGrants",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "SearchGrants",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._SearchGrants._get_response(
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
            resp = privilegedaccessmanager.SearchGrantsResponse()
            pb_resp = privilegedaccessmanager.SearchGrantsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_grants(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_grants_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        privilegedaccessmanager.SearchGrantsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.search_grants",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "SearchGrants",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEntitlement(
        _BasePrivilegedAccessManagerRestTransport._BaseUpdateEntitlement,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.UpdateEntitlement")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: privilegedaccessmanager.UpdateEntitlementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update entitlement method over HTTP.

            Args:
                request (~.privilegedaccessmanager.UpdateEntitlementRequest):
                    The request object. Message for updating an entitlement.
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseUpdateEntitlement._get_http_options()
            request, metadata = self._interceptor.pre_update_entitlement(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseUpdateEntitlement,
                    "_BaseUpdateEntitlement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.UpdateEntitlement",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "UpdateEntitlement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._UpdateEntitlement._get_response(
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

            resp = self._interceptor.post_update_entitlement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_entitlement_with_metadata(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.update_entitlement",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "UpdateEntitlement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def approve_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ApproveGrantRequest], privilegedaccessmanager.Grant
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApproveGrant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def check_onboarding_status(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CheckOnboardingStatusRequest],
        privilegedaccessmanager.CheckOnboardingStatusResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CheckOnboardingStatus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CreateEntitlementRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEntitlement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CreateGrantRequest], privilegedaccessmanager.Grant
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGrant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.DeleteEntitlementRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEntitlement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def deny_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.DenyGrantRequest], privilegedaccessmanager.Grant
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DenyGrant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.GetEntitlementRequest],
        privilegedaccessmanager.Entitlement,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEntitlement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.GetGrantRequest], privilegedaccessmanager.Grant
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGrant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_entitlements(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ListEntitlementsRequest],
        privilegedaccessmanager.ListEntitlementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEntitlements(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_grants(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ListGrantsRequest],
        privilegedaccessmanager.ListGrantsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGrants(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def revoke_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.RevokeGrantRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RevokeGrant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_entitlements(
        self,
    ) -> Callable[
        [privilegedaccessmanager.SearchEntitlementsRequest],
        privilegedaccessmanager.SearchEntitlementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchEntitlements(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_grants(
        self,
    ) -> Callable[
        [privilegedaccessmanager.SearchGrantsRequest],
        privilegedaccessmanager.SearchGrantsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchGrants(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.UpdateEntitlementRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEntitlement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BasePrivilegedAccessManagerRestTransport._BaseGetLocation,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
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
        _BasePrivilegedAccessManagerRestTransport._BaseListLocations,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BasePrivilegedAccessManagerRestTransport._BaseDeleteOperation,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BasePrivilegedAccessManagerRestTransport._BaseGetOperation,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PrivilegedAccessManagerRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
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
        _BasePrivilegedAccessManagerRestTransport._BaseListOperations,
        PrivilegedAccessManagerRestStub,
    ):
        def __hash__(self):
            return hash("PrivilegedAccessManagerRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BasePrivilegedAccessManagerRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePrivilegedAccessManagerRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PrivilegedAccessManagerRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.privilegedaccessmanager_v1.PrivilegedAccessManagerAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager",
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


__all__ = ("PrivilegedAccessManagerRestTransport",)
