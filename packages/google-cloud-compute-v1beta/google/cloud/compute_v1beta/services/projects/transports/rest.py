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

from google.cloud.compute_v1beta._compat import transcode_request
from google.cloud.compute_v1beta.types import compute

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseProjectsRestTransport

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


class ProjectsRestInterceptor:
    """Interceptor for Projects.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ProjectsRestTransport.

    .. code-block:: python
        class MyCustomProjectsInterceptor(ProjectsRestInterceptor):
            def pre_disable_xpn_host(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_xpn_host(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_disable_xpn_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_xpn_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_xpn_host(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_xpn_host(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_xpn_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_xpn_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_xpn_host(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_xpn_host(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_xpn_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_xpn_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_xpn_hosts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_xpn_hosts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_move_disk(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_move_disk(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_move_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_move_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_cloud_armor_tier(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_cloud_armor_tier(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_common_instance_metadata(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_common_instance_metadata(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_default_network_tier(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_default_network_tier(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_managed_protection_tier(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_managed_protection_tier(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_usage_export_bucket(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_usage_export_bucket(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ProjectsRestTransport(interceptor=MyCustomProjectsInterceptor())
        client = ProjectsClient(transport=transport)


    """

    def pre_disable_xpn_host(
        self,
        request: compute.DisableXpnHostProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DisableXpnHostProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for disable_xpn_host

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_disable_xpn_host(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for disable_xpn_host

        DEPRECATED. Please use the `post_disable_xpn_host_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_disable_xpn_host` interceptor runs
        before the `post_disable_xpn_host_with_metadata` interceptor.
        """
        return response

    def post_disable_xpn_host_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for disable_xpn_host

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_disable_xpn_host_with_metadata`
        interceptor in new development instead of the `post_disable_xpn_host` interceptor.
        When both interceptors are used, this `post_disable_xpn_host_with_metadata` interceptor runs after the
        `post_disable_xpn_host` interceptor. The (possibly modified) response returned by
        `post_disable_xpn_host` will be passed to
        `post_disable_xpn_host_with_metadata`.
        """
        return response, metadata

    def pre_disable_xpn_resource(
        self,
        request: compute.DisableXpnResourceProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DisableXpnResourceProjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for disable_xpn_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_disable_xpn_resource(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for disable_xpn_resource

        DEPRECATED. Please use the `post_disable_xpn_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_disable_xpn_resource` interceptor runs
        before the `post_disable_xpn_resource_with_metadata` interceptor.
        """
        return response

    def post_disable_xpn_resource_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for disable_xpn_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_disable_xpn_resource_with_metadata`
        interceptor in new development instead of the `post_disable_xpn_resource` interceptor.
        When both interceptors are used, this `post_disable_xpn_resource_with_metadata` interceptor runs after the
        `post_disable_xpn_resource` interceptor. The (possibly modified) response returned by
        `post_disable_xpn_resource` will be passed to
        `post_disable_xpn_resource_with_metadata`.
        """
        return response, metadata

    def pre_enable_xpn_host(
        self,
        request: compute.EnableXpnHostProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.EnableXpnHostProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for enable_xpn_host

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_enable_xpn_host(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for enable_xpn_host

        DEPRECATED. Please use the `post_enable_xpn_host_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_enable_xpn_host` interceptor runs
        before the `post_enable_xpn_host_with_metadata` interceptor.
        """
        return response

    def post_enable_xpn_host_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enable_xpn_host

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_enable_xpn_host_with_metadata`
        interceptor in new development instead of the `post_enable_xpn_host` interceptor.
        When both interceptors are used, this `post_enable_xpn_host_with_metadata` interceptor runs after the
        `post_enable_xpn_host` interceptor. The (possibly modified) response returned by
        `post_enable_xpn_host` will be passed to
        `post_enable_xpn_host_with_metadata`.
        """
        return response, metadata

    def pre_enable_xpn_resource(
        self,
        request: compute.EnableXpnResourceProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.EnableXpnResourceProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for enable_xpn_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_enable_xpn_resource(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for enable_xpn_resource

        DEPRECATED. Please use the `post_enable_xpn_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_enable_xpn_resource` interceptor runs
        before the `post_enable_xpn_resource_with_metadata` interceptor.
        """
        return response

    def post_enable_xpn_resource_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enable_xpn_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_enable_xpn_resource_with_metadata`
        interceptor in new development instead of the `post_enable_xpn_resource` interceptor.
        When both interceptors are used, this `post_enable_xpn_resource_with_metadata` interceptor runs after the
        `post_enable_xpn_resource` interceptor. The (possibly modified) response returned by
        `post_enable_xpn_resource` will be passed to
        `post_enable_xpn_resource_with_metadata`.
        """
        return response, metadata

    def pre_get(
        self,
        request: compute.GetProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.GetProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_get(self, response: compute.Project) -> compute.Project:
        """Post-rpc interceptor for get

        DEPRECATED. Please use the `post_get_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_get` interceptor runs
        before the `post_get_with_metadata` interceptor.
        """
        return response

    def post_get_with_metadata(
        self,
        response: compute.Project,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Project, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_get_with_metadata`
        interceptor in new development instead of the `post_get` interceptor.
        When both interceptors are used, this `post_get_with_metadata` interceptor runs after the
        `post_get` interceptor. The (possibly modified) response returned by
        `post_get` will be passed to
        `post_get_with_metadata`.
        """
        return response, metadata

    def pre_get_xpn_host(
        self,
        request: compute.GetXpnHostProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetXpnHostProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_xpn_host

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_get_xpn_host(self, response: compute.Project) -> compute.Project:
        """Post-rpc interceptor for get_xpn_host

        DEPRECATED. Please use the `post_get_xpn_host_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_get_xpn_host` interceptor runs
        before the `post_get_xpn_host_with_metadata` interceptor.
        """
        return response

    def post_get_xpn_host_with_metadata(
        self,
        response: compute.Project,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Project, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_xpn_host

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_get_xpn_host_with_metadata`
        interceptor in new development instead of the `post_get_xpn_host` interceptor.
        When both interceptors are used, this `post_get_xpn_host_with_metadata` interceptor runs after the
        `post_get_xpn_host` interceptor. The (possibly modified) response returned by
        `post_get_xpn_host` will be passed to
        `post_get_xpn_host_with_metadata`.
        """
        return response, metadata

    def pre_get_xpn_resources(
        self,
        request: compute.GetXpnResourcesProjectsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetXpnResourcesProjectsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_xpn_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_get_xpn_resources(
        self, response: compute.ProjectsGetXpnResources
    ) -> compute.ProjectsGetXpnResources:
        """Post-rpc interceptor for get_xpn_resources

        DEPRECATED. Please use the `post_get_xpn_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_get_xpn_resources` interceptor runs
        before the `post_get_xpn_resources_with_metadata` interceptor.
        """
        return response

    def post_get_xpn_resources_with_metadata(
        self,
        response: compute.ProjectsGetXpnResources,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ProjectsGetXpnResources, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_xpn_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_get_xpn_resources_with_metadata`
        interceptor in new development instead of the `post_get_xpn_resources` interceptor.
        When both interceptors are used, this `post_get_xpn_resources_with_metadata` interceptor runs after the
        `post_get_xpn_resources` interceptor. The (possibly modified) response returned by
        `post_get_xpn_resources` will be passed to
        `post_get_xpn_resources_with_metadata`.
        """
        return response, metadata

    def pre_list_xpn_hosts(
        self,
        request: compute.ListXpnHostsProjectsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListXpnHostsProjectsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_xpn_hosts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_list_xpn_hosts(self, response: compute.XpnHostList) -> compute.XpnHostList:
        """Post-rpc interceptor for list_xpn_hosts

        DEPRECATED. Please use the `post_list_xpn_hosts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_list_xpn_hosts` interceptor runs
        before the `post_list_xpn_hosts_with_metadata` interceptor.
        """
        return response

    def post_list_xpn_hosts_with_metadata(
        self,
        response: compute.XpnHostList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.XpnHostList, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_xpn_hosts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_list_xpn_hosts_with_metadata`
        interceptor in new development instead of the `post_list_xpn_hosts` interceptor.
        When both interceptors are used, this `post_list_xpn_hosts_with_metadata` interceptor runs after the
        `post_list_xpn_hosts` interceptor. The (possibly modified) response returned by
        `post_list_xpn_hosts` will be passed to
        `post_list_xpn_hosts_with_metadata`.
        """
        return response, metadata

    def pre_move_disk(
        self,
        request: compute.MoveDiskProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.MoveDiskProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for move_disk

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_move_disk(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for move_disk

        DEPRECATED. Please use the `post_move_disk_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_move_disk` interceptor runs
        before the `post_move_disk_with_metadata` interceptor.
        """
        return response

    def post_move_disk_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for move_disk

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_move_disk_with_metadata`
        interceptor in new development instead of the `post_move_disk` interceptor.
        When both interceptors are used, this `post_move_disk_with_metadata` interceptor runs after the
        `post_move_disk` interceptor. The (possibly modified) response returned by
        `post_move_disk` will be passed to
        `post_move_disk_with_metadata`.
        """
        return response, metadata

    def pre_move_instance(
        self,
        request: compute.MoveInstanceProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.MoveInstanceProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for move_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_move_instance(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for move_instance

        DEPRECATED. Please use the `post_move_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_move_instance` interceptor runs
        before the `post_move_instance_with_metadata` interceptor.
        """
        return response

    def post_move_instance_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for move_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_move_instance_with_metadata`
        interceptor in new development instead of the `post_move_instance` interceptor.
        When both interceptors are used, this `post_move_instance_with_metadata` interceptor runs after the
        `post_move_instance` interceptor. The (possibly modified) response returned by
        `post_move_instance` will be passed to
        `post_move_instance_with_metadata`.
        """
        return response, metadata

    def pre_set_cloud_armor_tier(
        self,
        request: compute.SetCloudArmorTierProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetCloudArmorTierProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_cloud_armor_tier

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_set_cloud_armor_tier(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_cloud_armor_tier

        DEPRECATED. Please use the `post_set_cloud_armor_tier_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_set_cloud_armor_tier` interceptor runs
        before the `post_set_cloud_armor_tier_with_metadata` interceptor.
        """
        return response

    def post_set_cloud_armor_tier_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_cloud_armor_tier

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_set_cloud_armor_tier_with_metadata`
        interceptor in new development instead of the `post_set_cloud_armor_tier` interceptor.
        When both interceptors are used, this `post_set_cloud_armor_tier_with_metadata` interceptor runs after the
        `post_set_cloud_armor_tier` interceptor. The (possibly modified) response returned by
        `post_set_cloud_armor_tier` will be passed to
        `post_set_cloud_armor_tier_with_metadata`.
        """
        return response, metadata

    def pre_set_common_instance_metadata(
        self,
        request: compute.SetCommonInstanceMetadataProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetCommonInstanceMetadataProjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_common_instance_metadata

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_set_common_instance_metadata(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_common_instance_metadata

        DEPRECATED. Please use the `post_set_common_instance_metadata_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_set_common_instance_metadata` interceptor runs
        before the `post_set_common_instance_metadata_with_metadata` interceptor.
        """
        return response

    def post_set_common_instance_metadata_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_common_instance_metadata

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_set_common_instance_metadata_with_metadata`
        interceptor in new development instead of the `post_set_common_instance_metadata` interceptor.
        When both interceptors are used, this `post_set_common_instance_metadata_with_metadata` interceptor runs after the
        `post_set_common_instance_metadata` interceptor. The (possibly modified) response returned by
        `post_set_common_instance_metadata` will be passed to
        `post_set_common_instance_metadata_with_metadata`.
        """
        return response, metadata

    def pre_set_default_network_tier(
        self,
        request: compute.SetDefaultNetworkTierProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetDefaultNetworkTierProjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_default_network_tier

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_set_default_network_tier(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_default_network_tier

        DEPRECATED. Please use the `post_set_default_network_tier_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_set_default_network_tier` interceptor runs
        before the `post_set_default_network_tier_with_metadata` interceptor.
        """
        return response

    def post_set_default_network_tier_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_default_network_tier

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_set_default_network_tier_with_metadata`
        interceptor in new development instead of the `post_set_default_network_tier` interceptor.
        When both interceptors are used, this `post_set_default_network_tier_with_metadata` interceptor runs after the
        `post_set_default_network_tier` interceptor. The (possibly modified) response returned by
        `post_set_default_network_tier` will be passed to
        `post_set_default_network_tier_with_metadata`.
        """
        return response, metadata

    def pre_set_managed_protection_tier(
        self,
        request: compute.SetManagedProtectionTierProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetManagedProtectionTierProjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_managed_protection_tier

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_set_managed_protection_tier(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_managed_protection_tier

        DEPRECATED. Please use the `post_set_managed_protection_tier_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_set_managed_protection_tier` interceptor runs
        before the `post_set_managed_protection_tier_with_metadata` interceptor.
        """
        return response

    def post_set_managed_protection_tier_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_managed_protection_tier

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_set_managed_protection_tier_with_metadata`
        interceptor in new development instead of the `post_set_managed_protection_tier` interceptor.
        When both interceptors are used, this `post_set_managed_protection_tier_with_metadata` interceptor runs after the
        `post_set_managed_protection_tier` interceptor. The (possibly modified) response returned by
        `post_set_managed_protection_tier` will be passed to
        `post_set_managed_protection_tier_with_metadata`.
        """
        return response, metadata

    def pre_set_usage_export_bucket(
        self,
        request: compute.SetUsageExportBucketProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetUsageExportBucketProjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_usage_export_bucket

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Projects server.
        """
        return request, metadata

    def post_set_usage_export_bucket(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_usage_export_bucket

        DEPRECATED. Please use the `post_set_usage_export_bucket_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Projects server but before
        it is returned to user code. This `post_set_usage_export_bucket` interceptor runs
        before the `post_set_usage_export_bucket_with_metadata` interceptor.
        """
        return response

    def post_set_usage_export_bucket_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_usage_export_bucket

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Projects server but before it is returned to user code.

        We recommend only using this `post_set_usage_export_bucket_with_metadata`
        interceptor in new development instead of the `post_set_usage_export_bucket` interceptor.
        When both interceptors are used, this `post_set_usage_export_bucket_with_metadata` interceptor runs after the
        `post_set_usage_export_bucket` interceptor. The (possibly modified) response returned by
        `post_set_usage_export_bucket` will be passed to
        `post_set_usage_export_bucket_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class ProjectsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ProjectsRestInterceptor


class ProjectsRestTransport(_BaseProjectsRestTransport):
    """REST backend synchronous transport for Projects.

    The Projects API.

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
        interceptor: Optional[ProjectsRestInterceptor] = None,
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
             interceptor (Optional[ProjectsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ProjectsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _DisableXpnHost(
        _BaseProjectsRestTransport._BaseDisableXpnHost, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.DisableXpnHost")

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
            request: compute.DisableXpnHostProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the disable xpn host method over HTTP.

            Args:
                request (~.compute.DisableXpnHostProjectRequest):
                    The request object. A request message for
                Projects.DisableXpnHost. See the method
                description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = (
                _BaseProjectsRestTransport._BaseDisableXpnHost._get_http_options()
            )
            request, metadata = self._interceptor.pre_disable_xpn_host(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseDisableXpnHost,
                    "_BaseDisableXpnHost__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.DisableXpnHost",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "DisableXpnHost",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._DisableXpnHost._get_response(
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

            resp = self._interceptor.post_disable_xpn_host(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_disable_xpn_host_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.disable_xpn_host",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "DisableXpnHost",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DisableXpnResource(
        _BaseProjectsRestTransport._BaseDisableXpnResource, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.DisableXpnResource")

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
            request: compute.DisableXpnResourceProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the disable xpn resource method over HTTP.

            Args:
                request (~.compute.DisableXpnResourceProjectRequest):
                    The request object. A request message for
                Projects.DisableXpnResource. See the
                method description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = (
                _BaseProjectsRestTransport._BaseDisableXpnResource._get_http_options()
            )
            request, metadata = self._interceptor.pre_disable_xpn_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseDisableXpnResource,
                    "_BaseDisableXpnResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.DisableXpnResource",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "DisableXpnResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._DisableXpnResource._get_response(
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

            resp = self._interceptor.post_disable_xpn_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_disable_xpn_resource_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.disable_xpn_resource",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "DisableXpnResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnableXpnHost(
        _BaseProjectsRestTransport._BaseEnableXpnHost, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.EnableXpnHost")

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
            request: compute.EnableXpnHostProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the enable xpn host method over HTTP.

            Args:
                request (~.compute.EnableXpnHostProjectRequest):
                    The request object. A request message for
                Projects.EnableXpnHost. See the method
                description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = (
                _BaseProjectsRestTransport._BaseEnableXpnHost._get_http_options()
            )
            request, metadata = self._interceptor.pre_enable_xpn_host(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseEnableXpnHost,
                    "_BaseEnableXpnHost__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.EnableXpnHost",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "EnableXpnHost",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._EnableXpnHost._get_response(
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

            resp = self._interceptor.post_enable_xpn_host(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enable_xpn_host_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.enable_xpn_host",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "EnableXpnHost",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnableXpnResource(
        _BaseProjectsRestTransport._BaseEnableXpnResource, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.EnableXpnResource")

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
            request: compute.EnableXpnResourceProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the enable xpn resource method over HTTP.

            Args:
                request (~.compute.EnableXpnResourceProjectRequest):
                    The request object. A request message for
                Projects.EnableXpnResource. See the
                method description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = (
                _BaseProjectsRestTransport._BaseEnableXpnResource._get_http_options()
            )
            request, metadata = self._interceptor.pre_enable_xpn_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseEnableXpnResource,
                    "_BaseEnableXpnResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.EnableXpnResource",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "EnableXpnResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._EnableXpnResource._get_response(
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

            resp = self._interceptor.post_enable_xpn_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enable_xpn_resource_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.enable_xpn_resource",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "EnableXpnResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Get(_BaseProjectsRestTransport._BaseGet, ProjectsRestStub):
        def __hash__(self):
            return hash("ProjectsRestTransport.Get")

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
            request: compute.GetProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Project:
            r"""Call the get method over HTTP.

            Args:
                request (~.compute.GetProjectRequest):
                    The request object. A request message for Projects.Get.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Project:
                    Represents a Project resource.

                A project is used to organize resources
                in a Google Cloud Platform environment.
                For more information, read about the
                Resource Hierarchy.

            """

            http_options = _BaseProjectsRestTransport._BaseGet._get_http_options()
            request, metadata = self._interceptor.pre_get(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseGet,
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.Get",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "Get",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._Get._get_response(
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
            resp = compute.Project()
            pb_resp = compute.Project.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Project.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.get",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "Get",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetXpnHost(_BaseProjectsRestTransport._BaseGetXpnHost, ProjectsRestStub):
        def __hash__(self):
            return hash("ProjectsRestTransport.GetXpnHost")

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
            request: compute.GetXpnHostProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Project:
            r"""Call the get xpn host method over HTTP.

            Args:
                request (~.compute.GetXpnHostProjectRequest):
                    The request object. A request message for
                Projects.GetXpnHost. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Project:
                    Represents a Project resource.

                A project is used to organize resources
                in a Google Cloud Platform environment.
                For more information, read about the
                Resource Hierarchy.

            """

            http_options = (
                _BaseProjectsRestTransport._BaseGetXpnHost._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_xpn_host(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseGetXpnHost,
                    "_BaseGetXpnHost__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.GetXpnHost",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "GetXpnHost",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._GetXpnHost._get_response(
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
            resp = compute.Project()
            pb_resp = compute.Project.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_xpn_host(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_xpn_host_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Project.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.get_xpn_host",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "GetXpnHost",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetXpnResources(
        _BaseProjectsRestTransport._BaseGetXpnResources, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.GetXpnResources")

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
            request: compute.GetXpnResourcesProjectsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.ProjectsGetXpnResources:
            r"""Call the get xpn resources method over HTTP.

            Args:
                request (~.compute.GetXpnResourcesProjectsRequest):
                    The request object. A request message for
                Projects.GetXpnResources. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.ProjectsGetXpnResources:

            """

            http_options = (
                _BaseProjectsRestTransport._BaseGetXpnResources._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_xpn_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseGetXpnResources,
                    "_BaseGetXpnResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.GetXpnResources",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "GetXpnResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._GetXpnResources._get_response(
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
            resp = compute.ProjectsGetXpnResources()
            pb_resp = compute.ProjectsGetXpnResources.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_xpn_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_xpn_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.ProjectsGetXpnResources.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.get_xpn_resources",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "GetXpnResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListXpnHosts(_BaseProjectsRestTransport._BaseListXpnHosts, ProjectsRestStub):
        def __hash__(self):
            return hash("ProjectsRestTransport.ListXpnHosts")

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
            request: compute.ListXpnHostsProjectsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.XpnHostList:
            r"""Call the list xpn hosts method over HTTP.

            Args:
                request (~.compute.ListXpnHostsProjectsRequest):
                    The request object. A request message for
                Projects.ListXpnHosts. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.XpnHostList:

            """

            http_options = (
                _BaseProjectsRestTransport._BaseListXpnHosts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_xpn_hosts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseListXpnHosts,
                    "_BaseListXpnHosts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.ListXpnHosts",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "ListXpnHosts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._ListXpnHosts._get_response(
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
            resp = compute.XpnHostList()
            pb_resp = compute.XpnHostList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_xpn_hosts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_xpn_hosts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.XpnHostList.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.list_xpn_hosts",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "ListXpnHosts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MoveDisk(_BaseProjectsRestTransport._BaseMoveDisk, ProjectsRestStub):
        def __hash__(self):
            return hash("ProjectsRestTransport.MoveDisk")

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
            request: compute.MoveDiskProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the move disk method over HTTP.

            Args:
                request (~.compute.MoveDiskProjectRequest):
                    The request object. A request message for
                Projects.MoveDisk. See the method
                description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = _BaseProjectsRestTransport._BaseMoveDisk._get_http_options()
            request, metadata = self._interceptor.pre_move_disk(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseMoveDisk,
                    "_BaseMoveDisk__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.MoveDisk",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "MoveDisk",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._MoveDisk._get_response(
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

            resp = self._interceptor.post_move_disk(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_move_disk_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.move_disk",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "MoveDisk",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MoveInstance(_BaseProjectsRestTransport._BaseMoveInstance, ProjectsRestStub):
        def __hash__(self):
            return hash("ProjectsRestTransport.MoveInstance")

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
            request: compute.MoveInstanceProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the move instance method over HTTP.

            Args:
                request (~.compute.MoveInstanceProjectRequest):
                    The request object. A request message for
                Projects.MoveInstance. See the method
                description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = (
                _BaseProjectsRestTransport._BaseMoveInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_move_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseMoveInstance,
                    "_BaseMoveInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.MoveInstance",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "MoveInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._MoveInstance._get_response(
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

            resp = self._interceptor.post_move_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_move_instance_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.move_instance",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "MoveInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetCloudArmorTier(
        _BaseProjectsRestTransport._BaseSetCloudArmorTier, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.SetCloudArmorTier")

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
            request: compute.SetCloudArmorTierProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set cloud armor tier method over HTTP.

            Args:
                request (~.compute.SetCloudArmorTierProjectRequest):
                    The request object. A request message for
                Projects.SetCloudArmorTier. See the
                method description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = (
                _BaseProjectsRestTransport._BaseSetCloudArmorTier._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_cloud_armor_tier(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseSetCloudArmorTier,
                    "_BaseSetCloudArmorTier__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.SetCloudArmorTier",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetCloudArmorTier",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._SetCloudArmorTier._get_response(
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

            resp = self._interceptor.post_set_cloud_armor_tier(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_cloud_armor_tier_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.set_cloud_armor_tier",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetCloudArmorTier",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetCommonInstanceMetadata(
        _BaseProjectsRestTransport._BaseSetCommonInstanceMetadata, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.SetCommonInstanceMetadata")

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
            request: compute.SetCommonInstanceMetadataProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set common instance
            metadata method over HTTP.

                Args:
                    request (~.compute.SetCommonInstanceMetadataProjectRequest):
                        The request object. A request message for
                    Projects.SetCommonInstanceMetadata. See
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

                    - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                    - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                    - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = _BaseProjectsRestTransport._BaseSetCommonInstanceMetadata._get_http_options()
            request, metadata = self._interceptor.pre_set_common_instance_metadata(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseSetCommonInstanceMetadata,
                    "_BaseSetCommonInstanceMetadata__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.SetCommonInstanceMetadata",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetCommonInstanceMetadata",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._SetCommonInstanceMetadata._get_response(
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

            resp = self._interceptor.post_set_common_instance_metadata(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_common_instance_metadata_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.set_common_instance_metadata",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetCommonInstanceMetadata",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetDefaultNetworkTier(
        _BaseProjectsRestTransport._BaseSetDefaultNetworkTier, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.SetDefaultNetworkTier")

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
            request: compute.SetDefaultNetworkTierProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set default network tier method over HTTP.

            Args:
                request (~.compute.SetDefaultNetworkTierProjectRequest):
                    The request object. A request message for
                Projects.SetDefaultNetworkTier. See the
                method description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = _BaseProjectsRestTransport._BaseSetDefaultNetworkTier._get_http_options()
            request, metadata = self._interceptor.pre_set_default_network_tier(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseSetDefaultNetworkTier,
                    "_BaseSetDefaultNetworkTier__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.SetDefaultNetworkTier",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetDefaultNetworkTier",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._SetDefaultNetworkTier._get_response(
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

            resp = self._interceptor.post_set_default_network_tier(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_default_network_tier_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.set_default_network_tier",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetDefaultNetworkTier",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetManagedProtectionTier(
        _BaseProjectsRestTransport._BaseSetManagedProtectionTier, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.SetManagedProtectionTier")

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
            request: compute.SetManagedProtectionTierProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set managed protection
            tier method over HTTP.

                Args:
                    request (~.compute.SetManagedProtectionTierProjectRequest):
                        The request object. A request message for
                    Projects.SetManagedProtectionTier. See
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

                    - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                    - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                    - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = _BaseProjectsRestTransport._BaseSetManagedProtectionTier._get_http_options()
            request, metadata = self._interceptor.pre_set_managed_protection_tier(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseSetManagedProtectionTier,
                    "_BaseSetManagedProtectionTier__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.SetManagedProtectionTier",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetManagedProtectionTier",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._SetManagedProtectionTier._get_response(
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

            resp = self._interceptor.post_set_managed_protection_tier(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_managed_protection_tier_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.set_managed_protection_tier",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetManagedProtectionTier",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetUsageExportBucket(
        _BaseProjectsRestTransport._BaseSetUsageExportBucket, ProjectsRestStub
    ):
        def __hash__(self):
            return hash("ProjectsRestTransport.SetUsageExportBucket")

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
            request: compute.SetUsageExportBucketProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set usage export bucket method over HTTP.

            Args:
                request (~.compute.SetUsageExportBucketProjectRequest):
                    The request object. A request message for
                Projects.SetUsageExportBucket. See the
                method description for details.
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

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

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

            http_options = (
                _BaseProjectsRestTransport._BaseSetUsageExportBucket._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_usage_export_bucket(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectsRestTransport._BaseSetUsageExportBucket,
                    "_BaseSetUsageExportBucket__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.ProjectsClient.SetUsageExportBucket",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetUsageExportBucket",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectsRestTransport._SetUsageExportBucket._get_response(
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

            resp = self._interceptor.post_set_usage_export_bucket(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_usage_export_bucket_with_metadata(
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
                    "Received response for google.cloud.compute_v1beta.ProjectsClient.set_usage_export_bucket",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.Projects",
                        "rpcName": "SetUsageExportBucket",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def disable_xpn_host(
        self,
    ) -> Callable[[compute.DisableXpnHostProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisableXpnHost(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def disable_xpn_resource(
        self,
    ) -> Callable[[compute.DisableXpnResourceProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisableXpnResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enable_xpn_host(
        self,
    ) -> Callable[[compute.EnableXpnHostProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnableXpnHost(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enable_xpn_resource(
        self,
    ) -> Callable[[compute.EnableXpnResourceProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnableXpnResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get(self) -> Callable[[compute.GetProjectRequest], compute.Project]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Get(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_xpn_host(
        self,
    ) -> Callable[[compute.GetXpnHostProjectRequest], compute.Project]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetXpnHost(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_xpn_resources(
        self,
    ) -> Callable[
        [compute.GetXpnResourcesProjectsRequest], compute.ProjectsGetXpnResources
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetXpnResources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_xpn_hosts(
        self,
    ) -> Callable[[compute.ListXpnHostsProjectsRequest], compute.XpnHostList]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListXpnHosts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def move_disk(
        self,
    ) -> Callable[[compute.MoveDiskProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MoveDisk(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def move_instance(
        self,
    ) -> Callable[[compute.MoveInstanceProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MoveInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_cloud_armor_tier(
        self,
    ) -> Callable[[compute.SetCloudArmorTierProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetCloudArmorTier(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_common_instance_metadata(
        self,
    ) -> Callable[[compute.SetCommonInstanceMetadataProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetCommonInstanceMetadata(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_default_network_tier(
        self,
    ) -> Callable[[compute.SetDefaultNetworkTierProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetDefaultNetworkTier(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_managed_protection_tier(
        self,
    ) -> Callable[[compute.SetManagedProtectionTierProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetManagedProtectionTier(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_usage_export_bucket(
        self,
    ) -> Callable[[compute.SetUsageExportBucketProjectRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetUsageExportBucket(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("ProjectsRestTransport",)
