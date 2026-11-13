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
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.securitycenter_v1beta1._compat import transcode_request
from google.cloud.securitycenter_v1beta1.types import (
    finding,
    organization_settings,
    securitycenter_service,
    source,
)
from google.cloud.securitycenter_v1beta1.types import finding as gcs_finding
from google.cloud.securitycenter_v1beta1.types import (
    organization_settings as gcs_organization_settings,
)
from google.cloud.securitycenter_v1beta1.types import (
    security_marks as gcs_security_marks,
)
from google.cloud.securitycenter_v1beta1.types import source as gcs_source

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSecurityCenterRestTransport

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


class SecurityCenterRestInterceptor:
    """Interceptor for SecurityCenter.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SecurityCenterRestTransport.

    .. code-block:: python
        class MyCustomSecurityCenterInterceptor(SecurityCenterRestInterceptor):
            def pre_create_finding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_finding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_organization_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_organization_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_group_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_group_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_group_findings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_group_findings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_assets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_assets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_findings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_findings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_sources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_asset_discovery(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_asset_discovery(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_finding_state(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_finding_state(self, response):
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

            def pre_update_finding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_finding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_organization_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_organization_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_security_marks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_security_marks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_source(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SecurityCenterRestTransport(interceptor=MyCustomSecurityCenterInterceptor())
        client = SecurityCenterClient(transport=transport)


    """

    def pre_create_finding(
        self,
        request: securitycenter_service.CreateFindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.CreateFindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_finding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_create_finding(self, response: gcs_finding.Finding) -> gcs_finding.Finding:
        """Post-rpc interceptor for create_finding

        DEPRECATED. Please use the `post_create_finding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_create_finding` interceptor runs
        before the `post_create_finding_with_metadata` interceptor.
        """
        return response

    def post_create_finding_with_metadata(
        self,
        response: gcs_finding.Finding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcs_finding.Finding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_finding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_create_finding_with_metadata`
        interceptor in new development instead of the `post_create_finding` interceptor.
        When both interceptors are used, this `post_create_finding_with_metadata` interceptor runs after the
        `post_create_finding` interceptor. The (possibly modified) response returned by
        `post_create_finding` will be passed to
        `post_create_finding_with_metadata`.
        """
        return response, metadata

    def pre_create_source(
        self,
        request: securitycenter_service.CreateSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.CreateSourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_create_source(self, response: gcs_source.Source) -> gcs_source.Source:
        """Post-rpc interceptor for create_source

        DEPRECATED. Please use the `post_create_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_create_source` interceptor runs
        before the `post_create_source_with_metadata` interceptor.
        """
        return response

    def post_create_source_with_metadata(
        self,
        response: gcs_source.Source,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcs_source.Source, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_create_source_with_metadata`
        interceptor in new development instead of the `post_create_source` interceptor.
        When both interceptors are used, this `post_create_source_with_metadata` interceptor runs after the
        `post_create_source` interceptor. The (possibly modified) response returned by
        `post_create_source` will be passed to
        `post_create_source_with_metadata`.
        """
        return response, metadata

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        DEPRECATED. Please use the `post_get_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
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
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_iam_policy_with_metadata`
        interceptor in new development instead of the `post_get_iam_policy` interceptor.
        When both interceptors are used, this `post_get_iam_policy_with_metadata` interceptor runs after the
        `post_get_iam_policy` interceptor. The (possibly modified) response returned by
        `post_get_iam_policy` will be passed to
        `post_get_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_organization_settings(
        self,
        request: securitycenter_service.GetOrganizationSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetOrganizationSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_organization_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_organization_settings(
        self, response: organization_settings.OrganizationSettings
    ) -> organization_settings.OrganizationSettings:
        """Post-rpc interceptor for get_organization_settings

        DEPRECATED. Please use the `post_get_organization_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_organization_settings` interceptor runs
        before the `post_get_organization_settings_with_metadata` interceptor.
        """
        return response

    def post_get_organization_settings_with_metadata(
        self,
        response: organization_settings.OrganizationSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        organization_settings.OrganizationSettings,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_organization_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_organization_settings_with_metadata`
        interceptor in new development instead of the `post_get_organization_settings` interceptor.
        When both interceptors are used, this `post_get_organization_settings_with_metadata` interceptor runs after the
        `post_get_organization_settings` interceptor. The (possibly modified) response returned by
        `post_get_organization_settings` will be passed to
        `post_get_organization_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_source(
        self,
        request: securitycenter_service.GetSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_source(self, response: source.Source) -> source.Source:
        """Post-rpc interceptor for get_source

        DEPRECATED. Please use the `post_get_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_source` interceptor runs
        before the `post_get_source_with_metadata` interceptor.
        """
        return response

    def post_get_source_with_metadata(
        self, response: source.Source, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[source.Source, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_source_with_metadata`
        interceptor in new development instead of the `post_get_source` interceptor.
        When both interceptors are used, this `post_get_source_with_metadata` interceptor runs after the
        `post_get_source` interceptor. The (possibly modified) response returned by
        `post_get_source` will be passed to
        `post_get_source_with_metadata`.
        """
        return response, metadata

    def pre_group_assets(
        self,
        request: securitycenter_service.GroupAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GroupAssetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for group_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_group_assets(
        self, response: securitycenter_service.GroupAssetsResponse
    ) -> securitycenter_service.GroupAssetsResponse:
        """Post-rpc interceptor for group_assets

        DEPRECATED. Please use the `post_group_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_group_assets` interceptor runs
        before the `post_group_assets_with_metadata` interceptor.
        """
        return response

    def post_group_assets_with_metadata(
        self,
        response: securitycenter_service.GroupAssetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GroupAssetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for group_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_group_assets_with_metadata`
        interceptor in new development instead of the `post_group_assets` interceptor.
        When both interceptors are used, this `post_group_assets_with_metadata` interceptor runs after the
        `post_group_assets` interceptor. The (possibly modified) response returned by
        `post_group_assets` will be passed to
        `post_group_assets_with_metadata`.
        """
        return response, metadata

    def pre_group_findings(
        self,
        request: securitycenter_service.GroupFindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GroupFindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for group_findings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_group_findings(
        self, response: securitycenter_service.GroupFindingsResponse
    ) -> securitycenter_service.GroupFindingsResponse:
        """Post-rpc interceptor for group_findings

        DEPRECATED. Please use the `post_group_findings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_group_findings` interceptor runs
        before the `post_group_findings_with_metadata` interceptor.
        """
        return response

    def post_group_findings_with_metadata(
        self,
        response: securitycenter_service.GroupFindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GroupFindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for group_findings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_group_findings_with_metadata`
        interceptor in new development instead of the `post_group_findings` interceptor.
        When both interceptors are used, this `post_group_findings_with_metadata` interceptor runs after the
        `post_group_findings` interceptor. The (possibly modified) response returned by
        `post_group_findings` will be passed to
        `post_group_findings_with_metadata`.
        """
        return response, metadata

    def pre_list_assets(
        self,
        request: securitycenter_service.ListAssetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListAssetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_assets(
        self, response: securitycenter_service.ListAssetsResponse
    ) -> securitycenter_service.ListAssetsResponse:
        """Post-rpc interceptor for list_assets

        DEPRECATED. Please use the `post_list_assets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_assets` interceptor runs
        before the `post_list_assets_with_metadata` interceptor.
        """
        return response

    def post_list_assets_with_metadata(
        self,
        response: securitycenter_service.ListAssetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListAssetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_assets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_assets_with_metadata`
        interceptor in new development instead of the `post_list_assets` interceptor.
        When both interceptors are used, this `post_list_assets_with_metadata` interceptor runs after the
        `post_list_assets` interceptor. The (possibly modified) response returned by
        `post_list_assets` will be passed to
        `post_list_assets_with_metadata`.
        """
        return response, metadata

    def pre_list_findings(
        self,
        request: securitycenter_service.ListFindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListFindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_findings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_findings(
        self, response: securitycenter_service.ListFindingsResponse
    ) -> securitycenter_service.ListFindingsResponse:
        """Post-rpc interceptor for list_findings

        DEPRECATED. Please use the `post_list_findings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_findings` interceptor runs
        before the `post_list_findings_with_metadata` interceptor.
        """
        return response

    def post_list_findings_with_metadata(
        self,
        response: securitycenter_service.ListFindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListFindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_findings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_findings_with_metadata`
        interceptor in new development instead of the `post_list_findings` interceptor.
        When both interceptors are used, this `post_list_findings_with_metadata` interceptor runs after the
        `post_list_findings` interceptor. The (possibly modified) response returned by
        `post_list_findings` will be passed to
        `post_list_findings_with_metadata`.
        """
        return response, metadata

    def pre_list_sources(
        self,
        request: securitycenter_service.ListSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListSourcesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_sources(
        self, response: securitycenter_service.ListSourcesResponse
    ) -> securitycenter_service.ListSourcesResponse:
        """Post-rpc interceptor for list_sources

        DEPRECATED. Please use the `post_list_sources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_sources` interceptor runs
        before the `post_list_sources_with_metadata` interceptor.
        """
        return response

    def post_list_sources_with_metadata(
        self,
        response: securitycenter_service.ListSourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListSourcesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_sources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_sources_with_metadata`
        interceptor in new development instead of the `post_list_sources` interceptor.
        When both interceptors are used, this `post_list_sources_with_metadata` interceptor runs after the
        `post_list_sources` interceptor. The (possibly modified) response returned by
        `post_list_sources` will be passed to
        `post_list_sources_with_metadata`.
        """
        return response, metadata

    def pre_run_asset_discovery(
        self,
        request: securitycenter_service.RunAssetDiscoveryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.RunAssetDiscoveryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for run_asset_discovery

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_run_asset_discovery(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_asset_discovery

        DEPRECATED. Please use the `post_run_asset_discovery_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_run_asset_discovery` interceptor runs
        before the `post_run_asset_discovery_with_metadata` interceptor.
        """
        return response

    def post_run_asset_discovery_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_asset_discovery

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_run_asset_discovery_with_metadata`
        interceptor in new development instead of the `post_run_asset_discovery` interceptor.
        When both interceptors are used, this `post_run_asset_discovery_with_metadata` interceptor runs after the
        `post_run_asset_discovery` interceptor. The (possibly modified) response returned by
        `post_run_asset_discovery` will be passed to
        `post_run_asset_discovery_with_metadata`.
        """
        return response, metadata

    def pre_set_finding_state(
        self,
        request: securitycenter_service.SetFindingStateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.SetFindingStateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_finding_state

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_set_finding_state(self, response: finding.Finding) -> finding.Finding:
        """Post-rpc interceptor for set_finding_state

        DEPRECATED. Please use the `post_set_finding_state_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_set_finding_state` interceptor runs
        before the `post_set_finding_state_with_metadata` interceptor.
        """
        return response

    def post_set_finding_state_with_metadata(
        self,
        response: finding.Finding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[finding.Finding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_finding_state

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_set_finding_state_with_metadata`
        interceptor in new development instead of the `post_set_finding_state` interceptor.
        When both interceptors are used, this `post_set_finding_state_with_metadata` interceptor runs after the
        `post_set_finding_state` interceptor. The (possibly modified) response returned by
        `post_set_finding_state` will be passed to
        `post_set_finding_state_with_metadata`.
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
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        DEPRECATED. Please use the `post_set_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
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
        is returned by the SecurityCenter server but before it is returned to user code.

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
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        DEPRECATED. Please use the `post_test_iam_permissions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
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
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_test_iam_permissions_with_metadata`
        interceptor in new development instead of the `post_test_iam_permissions` interceptor.
        When both interceptors are used, this `post_test_iam_permissions_with_metadata` interceptor runs after the
        `post_test_iam_permissions` interceptor. The (possibly modified) response returned by
        `post_test_iam_permissions` will be passed to
        `post_test_iam_permissions_with_metadata`.
        """
        return response, metadata

    def pre_update_finding(
        self,
        request: securitycenter_service.UpdateFindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateFindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_finding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_finding(self, response: gcs_finding.Finding) -> gcs_finding.Finding:
        """Post-rpc interceptor for update_finding

        DEPRECATED. Please use the `post_update_finding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_finding` interceptor runs
        before the `post_update_finding_with_metadata` interceptor.
        """
        return response

    def post_update_finding_with_metadata(
        self,
        response: gcs_finding.Finding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcs_finding.Finding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_finding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_finding_with_metadata`
        interceptor in new development instead of the `post_update_finding` interceptor.
        When both interceptors are used, this `post_update_finding_with_metadata` interceptor runs after the
        `post_update_finding` interceptor. The (possibly modified) response returned by
        `post_update_finding` will be passed to
        `post_update_finding_with_metadata`.
        """
        return response, metadata

    def pre_update_organization_settings(
        self,
        request: securitycenter_service.UpdateOrganizationSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateOrganizationSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_organization_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_organization_settings(
        self, response: gcs_organization_settings.OrganizationSettings
    ) -> gcs_organization_settings.OrganizationSettings:
        """Post-rpc interceptor for update_organization_settings

        DEPRECATED. Please use the `post_update_organization_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_organization_settings` interceptor runs
        before the `post_update_organization_settings_with_metadata` interceptor.
        """
        return response

    def post_update_organization_settings_with_metadata(
        self,
        response: gcs_organization_settings.OrganizationSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_organization_settings.OrganizationSettings,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_organization_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_organization_settings_with_metadata`
        interceptor in new development instead of the `post_update_organization_settings` interceptor.
        When both interceptors are used, this `post_update_organization_settings_with_metadata` interceptor runs after the
        `post_update_organization_settings` interceptor. The (possibly modified) response returned by
        `post_update_organization_settings` will be passed to
        `post_update_organization_settings_with_metadata`.
        """
        return response, metadata

    def pre_update_security_marks(
        self,
        request: securitycenter_service.UpdateSecurityMarksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateSecurityMarksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_security_marks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_security_marks(
        self, response: gcs_security_marks.SecurityMarks
    ) -> gcs_security_marks.SecurityMarks:
        """Post-rpc interceptor for update_security_marks

        DEPRECATED. Please use the `post_update_security_marks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_security_marks` interceptor runs
        before the `post_update_security_marks_with_metadata` interceptor.
        """
        return response

    def post_update_security_marks_with_metadata(
        self,
        response: gcs_security_marks.SecurityMarks,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_security_marks.SecurityMarks, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_security_marks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_security_marks_with_metadata`
        interceptor in new development instead of the `post_update_security_marks` interceptor.
        When both interceptors are used, this `post_update_security_marks_with_metadata` interceptor runs after the
        `post_update_security_marks` interceptor. The (possibly modified) response returned by
        `post_update_security_marks` will be passed to
        `post_update_security_marks_with_metadata`.
        """
        return response, metadata

    def pre_update_source(
        self,
        request: securitycenter_service.UpdateSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateSourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_source(self, response: gcs_source.Source) -> gcs_source.Source:
        """Post-rpc interceptor for update_source

        DEPRECATED. Please use the `post_update_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_source` interceptor runs
        before the `post_update_source_with_metadata` interceptor.
        """
        return response

    def post_update_source_with_metadata(
        self,
        response: gcs_source.Source,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcs_source.Source, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_source_with_metadata`
        interceptor in new development instead of the `post_update_source` interceptor.
        When both interceptors are used, this `post_update_source_with_metadata` interceptor runs after the
        `post_update_source` interceptor. The (possibly modified) response returned by
        `post_update_source` will be passed to
        `post_update_source_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class SecurityCenterRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SecurityCenterRestInterceptor


class SecurityCenterRestTransport(_BaseSecurityCenterRestTransport):
    """REST backend synchronous transport for SecurityCenter.

    V1 Beta APIs for Security Center service.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "securitycenter.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SecurityCenterRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'securitycenter.googleapis.com').
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
            interceptor (Optional[SecurityCenterRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SecurityCenterRestInterceptor()
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
                        "uri": "/v1beta1/{name=organizations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=organizations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=organizations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=organizations/*/operations}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateFinding(
        _BaseSecurityCenterRestTransport._BaseCreateFinding, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.CreateFinding")

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
            request: securitycenter_service.CreateFindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_finding.Finding:
            r"""Call the create finding method over HTTP.

            Args:
                request (~.securitycenter_service.CreateFindingRequest):
                    The request object. Request message for creating a
                finding.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_finding.Finding:
                    Security Command Center finding.

                A finding is a record of assessment data
                (security, risk, health or privacy)
                ingested into Security Command Center
                for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, an XSS
                vulnerability in an App Engine
                application is a finding.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseCreateFinding._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_finding(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseCreateFinding,
                    "_BaseCreateFinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.CreateFinding",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "CreateFinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._CreateFinding._get_response(
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
            resp = gcs_finding.Finding()
            pb_resp = gcs_finding.Finding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_finding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_finding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_finding.Finding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.create_finding",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "CreateFinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSource(
        _BaseSecurityCenterRestTransport._BaseCreateSource, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.CreateSource")

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
            request: securitycenter_service.CreateSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_source.Source:
            r"""Call the create source method over HTTP.

            Args:
                request (~.securitycenter_service.CreateSourceRequest):
                    The request object. Request message for creating a
                source.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_source.Source:
                    Security Command Center finding
                source. A finding source is an entity or
                a mechanism that can produce a finding.
                A source is like a container of findings
                that come from the same scanner, logger,
                monitor, etc.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseCreateSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseCreateSource,
                    "_BaseCreateSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.CreateSource",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "CreateSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._CreateSource._get_response(
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
            resp = gcs_source.Source()
            pb_resp = gcs_source.Source.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_source.Source.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.create_source",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "CreateSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIamPolicy(
        _BaseSecurityCenterRestTransport._BaseGetIamPolicy, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetIamPolicy")

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

            http_options = (
                _BaseSecurityCenterRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.get_iam_policy",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOrganizationSettings(
        _BaseSecurityCenterRestTransport._BaseGetOrganizationSettings,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetOrganizationSettings")

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
            request: securitycenter_service.GetOrganizationSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> organization_settings.OrganizationSettings:
            r"""Call the get organization settings method over HTTP.

            Args:
                request (~.securitycenter_service.GetOrganizationSettingsRequest):
                    The request object. Request message for getting
                organization settings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.organization_settings.OrganizationSettings:
                    User specified settings that are
                attached to the Security Command Center
                organization.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetOrganizationSettings._get_http_options()
            request, metadata = self._interceptor.pre_get_organization_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetOrganizationSettings,
                    "_BaseGetOrganizationSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.GetOrganizationSettings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GetOrganizationSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._GetOrganizationSettings._get_response(
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
            resp = organization_settings.OrganizationSettings()
            pb_resp = organization_settings.OrganizationSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_organization_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_organization_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        organization_settings.OrganizationSettings.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.get_organization_settings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GetOrganizationSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSource(
        _BaseSecurityCenterRestTransport._BaseGetSource, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetSource")

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
            request: securitycenter_service.GetSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> source.Source:
            r"""Call the get source method over HTTP.

            Args:
                request (~.securitycenter_service.GetSourceRequest):
                    The request object. Request message for getting a source.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.source.Source:
                    Security Command Center finding
                source. A finding source is an entity or
                a mechanism that can produce a finding.
                A source is like a container of findings
                that come from the same scanner, logger,
                monitor, etc.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseGetSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetSource,
                    "_BaseGetSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.GetSource",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GetSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetSource._get_response(
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
            resp = source.Source()
            pb_resp = source.Source.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = source.Source.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.get_source",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GetSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GroupAssets(
        _BaseSecurityCenterRestTransport._BaseGroupAssets, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GroupAssets")

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
            request: securitycenter_service.GroupAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.GroupAssetsResponse:
            r"""Call the group assets method over HTTP.

            Args:
                request (~.securitycenter_service.GroupAssetsRequest):
                    The request object. Request message for grouping by
                assets.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.GroupAssetsResponse:
                    Response message for grouping by
                assets.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseGroupAssets._get_http_options()
            )
            request, metadata = self._interceptor.pre_group_assets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGroupAssets,
                    "_BaseGroupAssets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.GroupAssets",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GroupAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GroupAssets._get_response(
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
            resp = securitycenter_service.GroupAssetsResponse()
            pb_resp = securitycenter_service.GroupAssetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_group_assets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_group_assets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.GroupAssetsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.group_assets",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GroupAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GroupFindings(
        _BaseSecurityCenterRestTransport._BaseGroupFindings, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GroupFindings")

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
            request: securitycenter_service.GroupFindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.GroupFindingsResponse:
            r"""Call the group findings method over HTTP.

            Args:
                request (~.securitycenter_service.GroupFindingsRequest):
                    The request object. Request message for grouping by
                findings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.GroupFindingsResponse:
                    Response message for group by
                findings.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseGroupFindings._get_http_options()
            )
            request, metadata = self._interceptor.pre_group_findings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGroupFindings,
                    "_BaseGroupFindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.GroupFindings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GroupFindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GroupFindings._get_response(
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
            resp = securitycenter_service.GroupFindingsResponse()
            pb_resp = securitycenter_service.GroupFindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_group_findings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_group_findings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.GroupFindingsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.group_findings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "GroupFindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAssets(
        _BaseSecurityCenterRestTransport._BaseListAssets, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListAssets")

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
            request: securitycenter_service.ListAssetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListAssetsResponse:
            r"""Call the list assets method over HTTP.

            Args:
                request (~.securitycenter_service.ListAssetsRequest):
                    The request object. Request message for listing assets.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.ListAssetsResponse:
                    Response message for listing assets.
            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseListAssets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_assets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListAssets,
                    "_BaseListAssets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.ListAssets",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "ListAssets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListAssets._get_response(
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
            resp = securitycenter_service.ListAssetsResponse()
            pb_resp = securitycenter_service.ListAssetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_assets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_assets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListAssetsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.list_assets",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "ListAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFindings(
        _BaseSecurityCenterRestTransport._BaseListFindings, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListFindings")

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
            request: securitycenter_service.ListFindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListFindingsResponse:
            r"""Call the list findings method over HTTP.

            Args:
                request (~.securitycenter_service.ListFindingsRequest):
                    The request object. Request message for listing findings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.ListFindingsResponse:
                    Response message for listing
                findings.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseListFindings._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_findings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListFindings,
                    "_BaseListFindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.ListFindings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "ListFindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListFindings._get_response(
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
            resp = securitycenter_service.ListFindingsResponse()
            pb_resp = securitycenter_service.ListFindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_findings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_findings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListFindingsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.list_findings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "ListFindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSources(
        _BaseSecurityCenterRestTransport._BaseListSources, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListSources")

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
            request: securitycenter_service.ListSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListSourcesResponse:
            r"""Call the list sources method over HTTP.

            Args:
                request (~.securitycenter_service.ListSourcesRequest):
                    The request object. Request message for listing sources.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.ListSourcesResponse:
                    Response message for listing sources.
            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseListSources._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_sources(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListSources,
                    "_BaseListSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.ListSources",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "ListSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListSources._get_response(
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
            resp = securitycenter_service.ListSourcesResponse()
            pb_resp = securitycenter_service.ListSourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_sources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_sources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListSourcesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.list_sources",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "ListSources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunAssetDiscovery(
        _BaseSecurityCenterRestTransport._BaseRunAssetDiscovery, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.RunAssetDiscovery")

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
            request: securitycenter_service.RunAssetDiscoveryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run asset discovery method over HTTP.

            Args:
                request (~.securitycenter_service.RunAssetDiscoveryRequest):
                    The request object. Request message for running asset
                discovery for an organization.
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

            http_options = _BaseSecurityCenterRestTransport._BaseRunAssetDiscovery._get_http_options()
            request, metadata = self._interceptor.pre_run_asset_discovery(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseRunAssetDiscovery,
                    "_BaseRunAssetDiscovery__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.RunAssetDiscovery",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "RunAssetDiscovery",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._RunAssetDiscovery._get_response(
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

            resp = self._interceptor.post_run_asset_discovery(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_asset_discovery_with_metadata(
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
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.run_asset_discovery",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "RunAssetDiscovery",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetFindingState(
        _BaseSecurityCenterRestTransport._BaseSetFindingState, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.SetFindingState")

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
            request: securitycenter_service.SetFindingStateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> finding.Finding:
            r"""Call the set finding state method over HTTP.

            Args:
                request (~.securitycenter_service.SetFindingStateRequest):
                    The request object. Request message for updating a
                finding's state.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.finding.Finding:
                    Security Command Center finding.

                A finding is a record of assessment data
                (security, risk, health or privacy)
                ingested into Security Command Center
                for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, an XSS
                vulnerability in an App Engine
                application is a finding.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseSetFindingState._get_http_options()
            request, metadata = self._interceptor.pre_set_finding_state(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseSetFindingState,
                    "_BaseSetFindingState__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.SetFindingState",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "SetFindingState",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._SetFindingState._get_response(
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
            resp = finding.Finding()
            pb_resp = finding.Finding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_finding_state(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_finding_state_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = finding.Finding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.set_finding_state",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "SetFindingState",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetIamPolicy(
        _BaseSecurityCenterRestTransport._BaseSetIamPolicy, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.SetIamPolicy")

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

            http_options = (
                _BaseSecurityCenterRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.set_iam_policy",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "SetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestIamPermissions(
        _BaseSecurityCenterRestTransport._BaseTestIamPermissions, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.TestIamPermissions")

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

            http_options = _BaseSecurityCenterRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.test_iam_permissions",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "TestIamPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFinding(
        _BaseSecurityCenterRestTransport._BaseUpdateFinding, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateFinding")

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
            request: securitycenter_service.UpdateFindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_finding.Finding:
            r"""Call the update finding method over HTTP.

            Args:
                request (~.securitycenter_service.UpdateFindingRequest):
                    The request object. Request message for updating or
                creating a finding.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_finding.Finding:
                    Security Command Center finding.

                A finding is a record of assessment data
                (security, risk, health or privacy)
                ingested into Security Command Center
                for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, an XSS
                vulnerability in an App Engine
                application is a finding.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseUpdateFinding._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_finding(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateFinding,
                    "_BaseUpdateFinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.UpdateFinding",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "UpdateFinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._UpdateFinding._get_response(
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
            resp = gcs_finding.Finding()
            pb_resp = gcs_finding.Finding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_finding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_finding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_finding.Finding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.update_finding",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "UpdateFinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateOrganizationSettings(
        _BaseSecurityCenterRestTransport._BaseUpdateOrganizationSettings,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateOrganizationSettings")

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
            request: securitycenter_service.UpdateOrganizationSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_organization_settings.OrganizationSettings:
            r"""Call the update organization
            settings method over HTTP.

                Args:
                    request (~.securitycenter_service.UpdateOrganizationSettingsRequest):
                        The request object. Request message for updating an
                    organization's settings.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_organization_settings.OrganizationSettings:
                        User specified settings that are
                    attached to the Security Command Center
                    organization.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateOrganizationSettings._get_http_options()
            request, metadata = self._interceptor.pre_update_organization_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateOrganizationSettings,
                    "_BaseUpdateOrganizationSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.UpdateOrganizationSettings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "UpdateOrganizationSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._UpdateOrganizationSettings._get_response(
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
            resp = gcs_organization_settings.OrganizationSettings()
            pb_resp = gcs_organization_settings.OrganizationSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_organization_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_organization_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcs_organization_settings.OrganizationSettings.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.update_organization_settings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "UpdateOrganizationSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSecurityMarks(
        _BaseSecurityCenterRestTransport._BaseUpdateSecurityMarks,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateSecurityMarks")

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
            request: securitycenter_service.UpdateSecurityMarksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_security_marks.SecurityMarks:
            r"""Call the update security marks method over HTTP.

            Args:
                request (~.securitycenter_service.UpdateSecurityMarksRequest):
                    The request object. Request message for updating a
                SecurityMarks resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_security_marks.SecurityMarks:
                    User specified security marks that
                are attached to the parent Security
                Command Center resource. Security marks
                are scoped within a Security Command
                Center organization -- they can be
                modified and viewed by all users who
                have proper permissions on the
                organization.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateSecurityMarks._get_http_options()
            request, metadata = self._interceptor.pre_update_security_marks(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateSecurityMarks,
                    "_BaseUpdateSecurityMarks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.UpdateSecurityMarks",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "UpdateSecurityMarks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._UpdateSecurityMarks._get_response(
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
            resp = gcs_security_marks.SecurityMarks()
            pb_resp = gcs_security_marks.SecurityMarks.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_security_marks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_security_marks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_security_marks.SecurityMarks.to_json(
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
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.update_security_marks",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "UpdateSecurityMarks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSource(
        _BaseSecurityCenterRestTransport._BaseUpdateSource, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateSource")

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
            request: securitycenter_service.UpdateSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_source.Source:
            r"""Call the update source method over HTTP.

            Args:
                request (~.securitycenter_service.UpdateSourceRequest):
                    The request object. Request message for updating a
                source.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_source.Source:
                    Security Command Center finding
                source. A finding source is an entity or
                a mechanism that can produce a finding.
                A source is like a container of findings
                that come from the same scanner, logger,
                monitor, etc.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseUpdateSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateSource,
                    "_BaseUpdateSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1beta1.SecurityCenterClient.UpdateSource",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "UpdateSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._UpdateSource._get_response(
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
            resp = gcs_source.Source()
            pb_resp = gcs_source.Source.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_source.Source.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1beta1.SecurityCenterClient.update_source",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1beta1.SecurityCenter",
                        "rpcName": "UpdateSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_finding(
        self,
    ) -> Callable[[securitycenter_service.CreateFindingRequest], gcs_finding.Finding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_source(
        self,
    ) -> Callable[[securitycenter_service.CreateSourceRequest], gcs_source.Source]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_organization_settings(
        self,
    ) -> Callable[
        [securitycenter_service.GetOrganizationSettingsRequest],
        organization_settings.OrganizationSettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOrganizationSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_source(
        self,
    ) -> Callable[[securitycenter_service.GetSourceRequest], source.Source]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def group_assets(
        self,
    ) -> Callable[
        [securitycenter_service.GroupAssetsRequest],
        securitycenter_service.GroupAssetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GroupAssets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def group_findings(
        self,
    ) -> Callable[
        [securitycenter_service.GroupFindingsRequest],
        securitycenter_service.GroupFindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GroupFindings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_assets(
        self,
    ) -> Callable[
        [securitycenter_service.ListAssetsRequest],
        securitycenter_service.ListAssetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAssets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_findings(
        self,
    ) -> Callable[
        [securitycenter_service.ListFindingsRequest],
        securitycenter_service.ListFindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFindings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_sources(
        self,
    ) -> Callable[
        [securitycenter_service.ListSourcesRequest],
        securitycenter_service.ListSourcesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_asset_discovery(
        self,
    ) -> Callable[
        [securitycenter_service.RunAssetDiscoveryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunAssetDiscovery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_finding_state(
        self,
    ) -> Callable[[securitycenter_service.SetFindingStateRequest], finding.Finding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetFindingState(self._session, self._host, self._interceptor)  # type: ignore

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
    def update_finding(
        self,
    ) -> Callable[[securitycenter_service.UpdateFindingRequest], gcs_finding.Finding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_organization_settings(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateOrganizationSettingsRequest],
        gcs_organization_settings.OrganizationSettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateOrganizationSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_security_marks(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateSecurityMarksRequest],
        gcs_security_marks.SecurityMarks,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSecurityMarks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_source(
        self,
    ) -> Callable[[securitycenter_service.UpdateSourceRequest], gcs_source.Source]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("SecurityCenterRestTransport",)
