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
    security_profile_group,
    security_profile_group_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOrganizationSecurityProfileGroupServiceRestTransport

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


class OrganizationSecurityProfileGroupServiceRestInterceptor:
    """Interceptor for OrganizationSecurityProfileGroupService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OrganizationSecurityProfileGroupServiceRestTransport.

    .. code-block:: python
        class MyCustomOrganizationSecurityProfileGroupServiceInterceptor(OrganizationSecurityProfileGroupServiceRestInterceptor):
            def pre_create_security_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_security_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_security_profile_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_security_profile_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_security_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_security_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_security_profile_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_security_profile_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_security_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_security_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_security_profile_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_security_profile_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_security_profile_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_security_profile_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_security_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_security_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_security_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_security_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_security_profile_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_security_profile_group(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OrganizationSecurityProfileGroupServiceRestTransport(interceptor=MyCustomOrganizationSecurityProfileGroupServiceInterceptor())
        client = OrganizationSecurityProfileGroupServiceClient(transport=transport)


    """

    def pre_create_security_profile(
        self,
        request: security_profile_group_service.CreateSecurityProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.CreateSecurityProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_security_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_create_security_profile(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_security_profile

        DEPRECATED. Please use the `post_create_security_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_create_security_profile` interceptor runs
        before the `post_create_security_profile_with_metadata` interceptor.
        """
        return response

    def post_create_security_profile_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_security_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_create_security_profile_with_metadata`
        interceptor in new development instead of the `post_create_security_profile` interceptor.
        When both interceptors are used, this `post_create_security_profile_with_metadata` interceptor runs after the
        `post_create_security_profile` interceptor. The (possibly modified) response returned by
        `post_create_security_profile` will be passed to
        `post_create_security_profile_with_metadata`.
        """
        return response, metadata

    def pre_create_security_profile_group(
        self,
        request: security_profile_group_service.CreateSecurityProfileGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.CreateSecurityProfileGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_security_profile_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_create_security_profile_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_security_profile_group

        DEPRECATED. Please use the `post_create_security_profile_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_create_security_profile_group` interceptor runs
        before the `post_create_security_profile_group_with_metadata` interceptor.
        """
        return response

    def post_create_security_profile_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_security_profile_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_create_security_profile_group_with_metadata`
        interceptor in new development instead of the `post_create_security_profile_group` interceptor.
        When both interceptors are used, this `post_create_security_profile_group_with_metadata` interceptor runs after the
        `post_create_security_profile_group` interceptor. The (possibly modified) response returned by
        `post_create_security_profile_group` will be passed to
        `post_create_security_profile_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_security_profile(
        self,
        request: security_profile_group_service.DeleteSecurityProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.DeleteSecurityProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_security_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_delete_security_profile(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_security_profile

        DEPRECATED. Please use the `post_delete_security_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_delete_security_profile` interceptor runs
        before the `post_delete_security_profile_with_metadata` interceptor.
        """
        return response

    def post_delete_security_profile_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_security_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_delete_security_profile_with_metadata`
        interceptor in new development instead of the `post_delete_security_profile` interceptor.
        When both interceptors are used, this `post_delete_security_profile_with_metadata` interceptor runs after the
        `post_delete_security_profile` interceptor. The (possibly modified) response returned by
        `post_delete_security_profile` will be passed to
        `post_delete_security_profile_with_metadata`.
        """
        return response, metadata

    def pre_delete_security_profile_group(
        self,
        request: security_profile_group_service.DeleteSecurityProfileGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.DeleteSecurityProfileGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_security_profile_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_delete_security_profile_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_security_profile_group

        DEPRECATED. Please use the `post_delete_security_profile_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_delete_security_profile_group` interceptor runs
        before the `post_delete_security_profile_group_with_metadata` interceptor.
        """
        return response

    def post_delete_security_profile_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_security_profile_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_delete_security_profile_group_with_metadata`
        interceptor in new development instead of the `post_delete_security_profile_group` interceptor.
        When both interceptors are used, this `post_delete_security_profile_group_with_metadata` interceptor runs after the
        `post_delete_security_profile_group` interceptor. The (possibly modified) response returned by
        `post_delete_security_profile_group` will be passed to
        `post_delete_security_profile_group_with_metadata`.
        """
        return response, metadata

    def pre_get_security_profile(
        self,
        request: security_profile_group_service.GetSecurityProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.GetSecurityProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_security_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_get_security_profile(
        self, response: security_profile_group.SecurityProfile
    ) -> security_profile_group.SecurityProfile:
        """Post-rpc interceptor for get_security_profile

        DEPRECATED. Please use the `post_get_security_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_get_security_profile` interceptor runs
        before the `post_get_security_profile_with_metadata` interceptor.
        """
        return response

    def post_get_security_profile_with_metadata(
        self,
        response: security_profile_group.SecurityProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group.SecurityProfile, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_security_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_get_security_profile_with_metadata`
        interceptor in new development instead of the `post_get_security_profile` interceptor.
        When both interceptors are used, this `post_get_security_profile_with_metadata` interceptor runs after the
        `post_get_security_profile` interceptor. The (possibly modified) response returned by
        `post_get_security_profile` will be passed to
        `post_get_security_profile_with_metadata`.
        """
        return response, metadata

    def pre_get_security_profile_group(
        self,
        request: security_profile_group_service.GetSecurityProfileGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.GetSecurityProfileGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_security_profile_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_get_security_profile_group(
        self, response: security_profile_group.SecurityProfileGroup
    ) -> security_profile_group.SecurityProfileGroup:
        """Post-rpc interceptor for get_security_profile_group

        DEPRECATED. Please use the `post_get_security_profile_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_get_security_profile_group` interceptor runs
        before the `post_get_security_profile_group_with_metadata` interceptor.
        """
        return response

    def post_get_security_profile_group_with_metadata(
        self,
        response: security_profile_group.SecurityProfileGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group.SecurityProfileGroup,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_security_profile_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_get_security_profile_group_with_metadata`
        interceptor in new development instead of the `post_get_security_profile_group` interceptor.
        When both interceptors are used, this `post_get_security_profile_group_with_metadata` interceptor runs after the
        `post_get_security_profile_group` interceptor. The (possibly modified) response returned by
        `post_get_security_profile_group` will be passed to
        `post_get_security_profile_group_with_metadata`.
        """
        return response, metadata

    def pre_list_security_profile_groups(
        self,
        request: security_profile_group_service.ListSecurityProfileGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.ListSecurityProfileGroupsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_security_profile_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_list_security_profile_groups(
        self, response: security_profile_group_service.ListSecurityProfileGroupsResponse
    ) -> security_profile_group_service.ListSecurityProfileGroupsResponse:
        """Post-rpc interceptor for list_security_profile_groups

        DEPRECATED. Please use the `post_list_security_profile_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_list_security_profile_groups` interceptor runs
        before the `post_list_security_profile_groups_with_metadata` interceptor.
        """
        return response

    def post_list_security_profile_groups_with_metadata(
        self,
        response: security_profile_group_service.ListSecurityProfileGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.ListSecurityProfileGroupsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_security_profile_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_list_security_profile_groups_with_metadata`
        interceptor in new development instead of the `post_list_security_profile_groups` interceptor.
        When both interceptors are used, this `post_list_security_profile_groups_with_metadata` interceptor runs after the
        `post_list_security_profile_groups` interceptor. The (possibly modified) response returned by
        `post_list_security_profile_groups` will be passed to
        `post_list_security_profile_groups_with_metadata`.
        """
        return response, metadata

    def pre_list_security_profiles(
        self,
        request: security_profile_group_service.ListSecurityProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.ListSecurityProfilesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_security_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_list_security_profiles(
        self, response: security_profile_group_service.ListSecurityProfilesResponse
    ) -> security_profile_group_service.ListSecurityProfilesResponse:
        """Post-rpc interceptor for list_security_profiles

        DEPRECATED. Please use the `post_list_security_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_list_security_profiles` interceptor runs
        before the `post_list_security_profiles_with_metadata` interceptor.
        """
        return response

    def post_list_security_profiles_with_metadata(
        self,
        response: security_profile_group_service.ListSecurityProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.ListSecurityProfilesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_security_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_list_security_profiles_with_metadata`
        interceptor in new development instead of the `post_list_security_profiles` interceptor.
        When both interceptors are used, this `post_list_security_profiles_with_metadata` interceptor runs after the
        `post_list_security_profiles` interceptor. The (possibly modified) response returned by
        `post_list_security_profiles` will be passed to
        `post_list_security_profiles_with_metadata`.
        """
        return response, metadata

    def pre_update_security_profile(
        self,
        request: security_profile_group_service.UpdateSecurityProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.UpdateSecurityProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_security_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_update_security_profile(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_security_profile

        DEPRECATED. Please use the `post_update_security_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_update_security_profile` interceptor runs
        before the `post_update_security_profile_with_metadata` interceptor.
        """
        return response

    def post_update_security_profile_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_security_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_update_security_profile_with_metadata`
        interceptor in new development instead of the `post_update_security_profile` interceptor.
        When both interceptors are used, this `post_update_security_profile_with_metadata` interceptor runs after the
        `post_update_security_profile` interceptor. The (possibly modified) response returned by
        `post_update_security_profile` will be passed to
        `post_update_security_profile_with_metadata`.
        """
        return response, metadata

    def pre_update_security_profile_group(
        self,
        request: security_profile_group_service.UpdateSecurityProfileGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_profile_group_service.UpdateSecurityProfileGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_security_profile_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_update_security_profile_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_security_profile_group

        DEPRECATED. Please use the `post_update_security_profile_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code. This `post_update_security_profile_group` interceptor runs
        before the `post_update_security_profile_group_with_metadata` interceptor.
        """
        return response

    def post_update_security_profile_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_security_profile_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OrganizationSecurityProfileGroupService server but before it is returned to user code.

        We recommend only using this `post_update_security_profile_group_with_metadata`
        interceptor in new development instead of the `post_update_security_profile_group` interceptor.
        When both interceptors are used, this `post_update_security_profile_group_with_metadata` interceptor runs after the
        `post_update_security_profile_group` interceptor. The (possibly modified) response returned by
        `post_update_security_profile_group` will be passed to
        `post_update_security_profile_group_with_metadata`.
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
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
        before they are sent to the OrganizationSecurityProfileGroupService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the OrganizationSecurityProfileGroupService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class OrganizationSecurityProfileGroupServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OrganizationSecurityProfileGroupServiceRestInterceptor


class OrganizationSecurityProfileGroupServiceRestTransport(
    _BaseOrganizationSecurityProfileGroupServiceRestTransport
):
    """REST backend synchronous transport for OrganizationSecurityProfileGroupService.

    Organization SecurityProfileGroup is created under
    organization.

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
        interceptor: Optional[
            OrganizationSecurityProfileGroupServiceRestInterceptor
        ] = None,
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
            interceptor (Optional[OrganizationSecurityProfileGroupServiceRestInterceptor]): Interceptor used
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
        self._interceptor = (
            interceptor or OrganizationSecurityProfileGroupServiceRestInterceptor()
        )
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

    class _CreateSecurityProfile(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCreateSecurityProfile,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.CreateSecurityProfile"
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
            request: security_profile_group_service.CreateSecurityProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create security profile method over HTTP.

            Args:
                request (~.security_profile_group_service.CreateSecurityProfileRequest):
                    The request object. Request used by the
                CreateSecurityProfile method.
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCreateSecurityProfile._get_http_options()
            request, metadata = self._interceptor.pre_create_security_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCreateSecurityProfile,
                    "_BaseCreateSecurityProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.CreateSecurityProfile",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "CreateSecurityProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._CreateSecurityProfile._get_response(
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

            resp = self._interceptor.post_create_security_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_security_profile_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.create_security_profile",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "CreateSecurityProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSecurityProfileGroup(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCreateSecurityProfileGroup,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.CreateSecurityProfileGroup"
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
            request: security_profile_group_service.CreateSecurityProfileGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create security profile
            group method over HTTP.

                Args:
                    request (~.security_profile_group_service.CreateSecurityProfileGroupRequest):
                        The request object. Request used by the
                    CreateSecurityProfileGroup method.
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCreateSecurityProfileGroup._get_http_options()
            request, metadata = self._interceptor.pre_create_security_profile_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCreateSecurityProfileGroup,
                    "_BaseCreateSecurityProfileGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.CreateSecurityProfileGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "CreateSecurityProfileGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._CreateSecurityProfileGroup._get_response(
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

            resp = self._interceptor.post_create_security_profile_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_security_profile_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.create_security_profile_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "CreateSecurityProfileGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSecurityProfile(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteSecurityProfile,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.DeleteSecurityProfile"
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
            request: security_profile_group_service.DeleteSecurityProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete security profile method over HTTP.

            Args:
                request (~.security_profile_group_service.DeleteSecurityProfileRequest):
                    The request object. Request used by the
                DeleteSecurityProfile method.
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteSecurityProfile._get_http_options()
            request, metadata = self._interceptor.pre_delete_security_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteSecurityProfile,
                    "_BaseDeleteSecurityProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.DeleteSecurityProfile",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "DeleteSecurityProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._DeleteSecurityProfile._get_response(
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

            resp = self._interceptor.post_delete_security_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_security_profile_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.delete_security_profile",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "DeleteSecurityProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSecurityProfileGroup(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteSecurityProfileGroup,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.DeleteSecurityProfileGroup"
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
            request: security_profile_group_service.DeleteSecurityProfileGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete security profile
            group method over HTTP.

                Args:
                    request (~.security_profile_group_service.DeleteSecurityProfileGroupRequest):
                        The request object. Request used by the
                    DeleteSecurityProfileGroup method.
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteSecurityProfileGroup._get_http_options()
            request, metadata = self._interceptor.pre_delete_security_profile_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteSecurityProfileGroup,
                    "_BaseDeleteSecurityProfileGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.DeleteSecurityProfileGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "DeleteSecurityProfileGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._DeleteSecurityProfileGroup._get_response(
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

            resp = self._interceptor.post_delete_security_profile_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_security_profile_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.delete_security_profile_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "DeleteSecurityProfileGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSecurityProfile(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetSecurityProfile,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.GetSecurityProfile"
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
            request: security_profile_group_service.GetSecurityProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_profile_group.SecurityProfile:
            r"""Call the get security profile method over HTTP.

            Args:
                request (~.security_profile_group_service.GetSecurityProfileRequest):
                    The request object. Request used by the
                GetSecurityProfile method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.security_profile_group.SecurityProfile:
                    SecurityProfile is a resource that
                defines the behavior for one of many
                ProfileTypes.

            """

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetSecurityProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_security_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetSecurityProfile,
                    "_BaseGetSecurityProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.GetSecurityProfile",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "GetSecurityProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._GetSecurityProfile._get_response(
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
            resp = security_profile_group.SecurityProfile()
            pb_resp = security_profile_group.SecurityProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_security_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_security_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = security_profile_group.SecurityProfile.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.get_security_profile",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "GetSecurityProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSecurityProfileGroup(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetSecurityProfileGroup,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.GetSecurityProfileGroup"
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
            request: security_profile_group_service.GetSecurityProfileGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_profile_group.SecurityProfileGroup:
            r"""Call the get security profile
            group method over HTTP.

                Args:
                    request (~.security_profile_group_service.GetSecurityProfileGroupRequest):
                        The request object. Request used by the
                    GetSecurityProfileGroup method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_profile_group.SecurityProfileGroup:
                        SecurityProfileGroup is a resource
                    that defines the behavior for various
                    ProfileTypes.

            """

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetSecurityProfileGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_security_profile_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetSecurityProfileGroup,
                    "_BaseGetSecurityProfileGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.GetSecurityProfileGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "GetSecurityProfileGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._GetSecurityProfileGroup._get_response(
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
            resp = security_profile_group.SecurityProfileGroup()
            pb_resp = security_profile_group.SecurityProfileGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_security_profile_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_security_profile_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        security_profile_group.SecurityProfileGroup.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.get_security_profile_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "GetSecurityProfileGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSecurityProfileGroups(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListSecurityProfileGroups,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.ListSecurityProfileGroups"
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
            request: security_profile_group_service.ListSecurityProfileGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_profile_group_service.ListSecurityProfileGroupsResponse:
            r"""Call the list security profile
            groups method over HTTP.

                Args:
                    request (~.security_profile_group_service.ListSecurityProfileGroupsRequest):
                        The request object. Request used with the
                    ListSecurityProfileGroups method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_profile_group_service.ListSecurityProfileGroupsResponse:
                        Response returned by the
                    ListSecurityProfileGroups method.

            """

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListSecurityProfileGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_security_profile_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListSecurityProfileGroups,
                    "_BaseListSecurityProfileGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.ListSecurityProfileGroups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "ListSecurityProfileGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._ListSecurityProfileGroups._get_response(
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
            resp = security_profile_group_service.ListSecurityProfileGroupsResponse()
            pb_resp = (
                security_profile_group_service.ListSecurityProfileGroupsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_security_profile_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_security_profile_groups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = security_profile_group_service.ListSecurityProfileGroupsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.list_security_profile_groups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "ListSecurityProfileGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSecurityProfiles(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListSecurityProfiles,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.ListSecurityProfiles"
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
            request: security_profile_group_service.ListSecurityProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_profile_group_service.ListSecurityProfilesResponse:
            r"""Call the list security profiles method over HTTP.

            Args:
                request (~.security_profile_group_service.ListSecurityProfilesRequest):
                    The request object. Request used with the
                ListSecurityProfiles method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.security_profile_group_service.ListSecurityProfilesResponse:
                    Response returned by the
                ListSecurityProfiles method.

            """

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListSecurityProfiles._get_http_options()
            request, metadata = self._interceptor.pre_list_security_profiles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListSecurityProfiles,
                    "_BaseListSecurityProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.ListSecurityProfiles",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "ListSecurityProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._ListSecurityProfiles._get_response(
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
            resp = security_profile_group_service.ListSecurityProfilesResponse()
            pb_resp = security_profile_group_service.ListSecurityProfilesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_security_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_security_profiles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = security_profile_group_service.ListSecurityProfilesResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.list_security_profiles",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "ListSecurityProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSecurityProfile(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseUpdateSecurityProfile,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.UpdateSecurityProfile"
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
            request: security_profile_group_service.UpdateSecurityProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update security profile method over HTTP.

            Args:
                request (~.security_profile_group_service.UpdateSecurityProfileRequest):
                    The request object. Request used by the
                UpdateSecurityProfile method.
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseUpdateSecurityProfile._get_http_options()
            request, metadata = self._interceptor.pre_update_security_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseUpdateSecurityProfile,
                    "_BaseUpdateSecurityProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.UpdateSecurityProfile",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "UpdateSecurityProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._UpdateSecurityProfile._get_response(
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

            resp = self._interceptor.post_update_security_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_security_profile_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.update_security_profile",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "UpdateSecurityProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSecurityProfileGroup(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseUpdateSecurityProfileGroup,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.UpdateSecurityProfileGroup"
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
            request: security_profile_group_service.UpdateSecurityProfileGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update security profile
            group method over HTTP.

                Args:
                    request (~.security_profile_group_service.UpdateSecurityProfileGroupRequest):
                        The request object. Request used by the
                    UpdateSecurityProfileGroup method.
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseUpdateSecurityProfileGroup._get_http_options()
            request, metadata = self._interceptor.pre_update_security_profile_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseUpdateSecurityProfileGroup,
                    "_BaseUpdateSecurityProfileGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.UpdateSecurityProfileGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "UpdateSecurityProfileGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._UpdateSecurityProfileGroup._get_response(
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

            resp = self._interceptor.post_update_security_profile_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_security_profile_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.update_security_profile_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "UpdateSecurityProfileGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_security_profile(
        self,
    ) -> Callable[
        [security_profile_group_service.CreateSecurityProfileRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSecurityProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_security_profile_group(
        self,
    ) -> Callable[
        [security_profile_group_service.CreateSecurityProfileGroupRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSecurityProfileGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_security_profile(
        self,
    ) -> Callable[
        [security_profile_group_service.DeleteSecurityProfileRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSecurityProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_security_profile_group(
        self,
    ) -> Callable[
        [security_profile_group_service.DeleteSecurityProfileGroupRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSecurityProfileGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_security_profile(
        self,
    ) -> Callable[
        [security_profile_group_service.GetSecurityProfileRequest],
        security_profile_group.SecurityProfile,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSecurityProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_security_profile_group(
        self,
    ) -> Callable[
        [security_profile_group_service.GetSecurityProfileGroupRequest],
        security_profile_group.SecurityProfileGroup,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSecurityProfileGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_security_profile_groups(
        self,
    ) -> Callable[
        [security_profile_group_service.ListSecurityProfileGroupsRequest],
        security_profile_group_service.ListSecurityProfileGroupsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSecurityProfileGroups(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_security_profiles(
        self,
    ) -> Callable[
        [security_profile_group_service.ListSecurityProfilesRequest],
        security_profile_group_service.ListSecurityProfilesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSecurityProfiles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_security_profile(
        self,
    ) -> Callable[
        [security_profile_group_service.UpdateSecurityProfileRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSecurityProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_security_profile_group(
        self,
    ) -> Callable[
        [security_profile_group_service.UpdateSecurityProfileGroupRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSecurityProfileGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetLocation,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.GetLocation"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
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
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListLocations,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.ListLocations"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
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
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetIamPolicy,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.GetIamPolicy"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
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
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseSetIamPolicy,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.SetIamPolicy"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
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
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseTestIamPermissions,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.TestIamPermissions"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
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
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCancelOperation,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.CancelOperation"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._CancelOperation._get_response(
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
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteOperation,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.DeleteOperation"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._DeleteOperation._get_response(
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
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetOperation,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.GetOperation"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
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
        _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListOperations,
        OrganizationSecurityProfileGroupServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OrganizationSecurityProfileGroupServiceRestTransport.ListOperations"
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

            http_options = _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOrganizationSecurityProfileGroupServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OrganizationSecurityProfileGroupServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.OrganizationSecurityProfileGroupServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService",
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


__all__ = ("OrganizationSecurityProfileGroupServiceRestTransport",)
