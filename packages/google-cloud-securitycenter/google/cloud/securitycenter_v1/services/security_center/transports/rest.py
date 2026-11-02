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
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.securitycenter_v1._compat import transcode_request
from google.cloud.securitycenter_v1.types import (
    bigquery_export,
    effective_event_threat_detection_custom_module,
    effective_security_health_analytics_custom_module,
    event_threat_detection_custom_module,
    finding,
    mute_config,
    notification_config,
    organization_settings,
    resource_value_config,
    security_health_analytics_custom_module,
    securitycenter_service,
    simulation,
    source,
    valued_resource,
)
from google.cloud.securitycenter_v1.types import (
    event_threat_detection_custom_module as gcs_event_threat_detection_custom_module,
)
from google.cloud.securitycenter_v1.types import external_system as gcs_external_system
from google.cloud.securitycenter_v1.types import finding as gcs_finding
from google.cloud.securitycenter_v1.types import mute_config as gcs_mute_config
from google.cloud.securitycenter_v1.types import (
    notification_config as gcs_notification_config,
)
from google.cloud.securitycenter_v1.types import (
    organization_settings as gcs_organization_settings,
)
from google.cloud.securitycenter_v1.types import (
    resource_value_config as gcs_resource_value_config,
)
from google.cloud.securitycenter_v1.types import (
    security_health_analytics_custom_module as gcs_security_health_analytics_custom_module,
)
from google.cloud.securitycenter_v1.types import security_marks as gcs_security_marks
from google.cloud.securitycenter_v1.types import source as gcs_source

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
            def pre_batch_create_resource_value_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_resource_value_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_bulk_mute_findings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_mute_findings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_big_query_export(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_big_query_export(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_event_threat_detection_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_finding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_finding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_mute_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_mute_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_notification_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_notification_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_security_health_analytics_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_big_query_export(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_mute_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_notification_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_resource_value_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_big_query_export(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_big_query_export(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_effective_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_effective_event_threat_detection_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_effective_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_effective_security_health_analytics_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_event_threat_detection_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_mute_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mute_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_notification_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_notification_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_organization_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_organization_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_resource_value_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_resource_value_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_security_health_analytics_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_simulation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_simulation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_valued_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_valued_resource(self, response):
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

            def pre_list_attack_paths(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_attack_paths(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_big_query_exports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_big_query_exports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_descendant_event_threat_detection_custom_modules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_descendant_event_threat_detection_custom_modules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_descendant_security_health_analytics_custom_modules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_descendant_security_health_analytics_custom_modules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_effective_event_threat_detection_custom_modules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_effective_event_threat_detection_custom_modules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_effective_security_health_analytics_custom_modules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_effective_security_health_analytics_custom_modules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_event_threat_detection_custom_modules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_event_threat_detection_custom_modules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_findings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_findings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_mute_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_mute_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_notification_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_notification_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_resource_value_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_resource_value_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_security_health_analytics_custom_modules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_security_health_analytics_custom_modules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_sources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_valued_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_valued_resources(self, response):
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

            def pre_set_mute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_mute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_simulate_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_simulate_security_health_analytics_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_iam_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_big_query_export(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_big_query_export(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_event_threat_detection_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_external_system(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_external_system(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_finding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_finding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_mute_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_mute_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_notification_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_notification_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_organization_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_organization_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_resource_value_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_resource_value_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_security_health_analytics_custom_module(self, response):
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

            def pre_validate_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_event_threat_detection_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SecurityCenterRestTransport(interceptor=MyCustomSecurityCenterInterceptor())
        client = SecurityCenterClient(transport=transport)


    """

    def pre_batch_create_resource_value_configs(
        self,
        request: securitycenter_service.BatchCreateResourceValueConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.BatchCreateResourceValueConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_resource_value_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_batch_create_resource_value_configs(
        self, response: securitycenter_service.BatchCreateResourceValueConfigsResponse
    ) -> securitycenter_service.BatchCreateResourceValueConfigsResponse:
        """Post-rpc interceptor for batch_create_resource_value_configs

        DEPRECATED. Please use the `post_batch_create_resource_value_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_batch_create_resource_value_configs` interceptor runs
        before the `post_batch_create_resource_value_configs_with_metadata` interceptor.
        """
        return response

    def post_batch_create_resource_value_configs_with_metadata(
        self,
        response: securitycenter_service.BatchCreateResourceValueConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.BatchCreateResourceValueConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_resource_value_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_batch_create_resource_value_configs_with_metadata`
        interceptor in new development instead of the `post_batch_create_resource_value_configs` interceptor.
        When both interceptors are used, this `post_batch_create_resource_value_configs_with_metadata` interceptor runs after the
        `post_batch_create_resource_value_configs` interceptor. The (possibly modified) response returned by
        `post_batch_create_resource_value_configs` will be passed to
        `post_batch_create_resource_value_configs_with_metadata`.
        """
        return response, metadata

    def pre_bulk_mute_findings(
        self,
        request: securitycenter_service.BulkMuteFindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.BulkMuteFindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for bulk_mute_findings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_bulk_mute_findings(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for bulk_mute_findings

        DEPRECATED. Please use the `post_bulk_mute_findings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_bulk_mute_findings` interceptor runs
        before the `post_bulk_mute_findings_with_metadata` interceptor.
        """
        return response

    def post_bulk_mute_findings_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for bulk_mute_findings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_bulk_mute_findings_with_metadata`
        interceptor in new development instead of the `post_bulk_mute_findings` interceptor.
        When both interceptors are used, this `post_bulk_mute_findings_with_metadata` interceptor runs after the
        `post_bulk_mute_findings` interceptor. The (possibly modified) response returned by
        `post_bulk_mute_findings` will be passed to
        `post_bulk_mute_findings_with_metadata`.
        """
        return response, metadata

    def pre_create_big_query_export(
        self,
        request: securitycenter_service.CreateBigQueryExportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.CreateBigQueryExportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_big_query_export

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_create_big_query_export(
        self, response: bigquery_export.BigQueryExport
    ) -> bigquery_export.BigQueryExport:
        """Post-rpc interceptor for create_big_query_export

        DEPRECATED. Please use the `post_create_big_query_export_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_create_big_query_export` interceptor runs
        before the `post_create_big_query_export_with_metadata` interceptor.
        """
        return response

    def post_create_big_query_export_with_metadata(
        self,
        response: bigquery_export.BigQueryExport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[bigquery_export.BigQueryExport, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_big_query_export

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_create_big_query_export_with_metadata`
        interceptor in new development instead of the `post_create_big_query_export` interceptor.
        When both interceptors are used, this `post_create_big_query_export_with_metadata` interceptor runs after the
        `post_create_big_query_export` interceptor. The (possibly modified) response returned by
        `post_create_big_query_export` will be passed to
        `post_create_big_query_export_with_metadata`.
        """
        return response, metadata

    def pre_create_event_threat_detection_custom_module(
        self,
        request: securitycenter_service.CreateEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.CreateEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_create_event_threat_detection_custom_module(
        self,
        response: gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    ) -> gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule:
        """Post-rpc interceptor for create_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_create_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_create_event_threat_detection_custom_module` interceptor runs
        before the `post_create_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_create_event_threat_detection_custom_module_with_metadata(
        self,
        response: gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_create_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_create_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_create_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_create_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_create_event_threat_detection_custom_module` will be passed to
        `post_create_event_threat_detection_custom_module_with_metadata`.
        """
        return response, metadata

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

    def pre_create_mute_config(
        self,
        request: securitycenter_service.CreateMuteConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.CreateMuteConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_mute_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_create_mute_config(
        self, response: gcs_mute_config.MuteConfig
    ) -> gcs_mute_config.MuteConfig:
        """Post-rpc interceptor for create_mute_config

        DEPRECATED. Please use the `post_create_mute_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_create_mute_config` interceptor runs
        before the `post_create_mute_config_with_metadata` interceptor.
        """
        return response

    def post_create_mute_config_with_metadata(
        self,
        response: gcs_mute_config.MuteConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcs_mute_config.MuteConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_mute_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_create_mute_config_with_metadata`
        interceptor in new development instead of the `post_create_mute_config` interceptor.
        When both interceptors are used, this `post_create_mute_config_with_metadata` interceptor runs after the
        `post_create_mute_config` interceptor. The (possibly modified) response returned by
        `post_create_mute_config` will be passed to
        `post_create_mute_config_with_metadata`.
        """
        return response, metadata

    def pre_create_notification_config(
        self,
        request: securitycenter_service.CreateNotificationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.CreateNotificationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_notification_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_create_notification_config(
        self, response: gcs_notification_config.NotificationConfig
    ) -> gcs_notification_config.NotificationConfig:
        """Post-rpc interceptor for create_notification_config

        DEPRECATED. Please use the `post_create_notification_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_create_notification_config` interceptor runs
        before the `post_create_notification_config_with_metadata` interceptor.
        """
        return response

    def post_create_notification_config_with_metadata(
        self,
        response: gcs_notification_config.NotificationConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_notification_config.NotificationConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_notification_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_create_notification_config_with_metadata`
        interceptor in new development instead of the `post_create_notification_config` interceptor.
        When both interceptors are used, this `post_create_notification_config_with_metadata` interceptor runs after the
        `post_create_notification_config` interceptor. The (possibly modified) response returned by
        `post_create_notification_config` will be passed to
        `post_create_notification_config_with_metadata`.
        """
        return response, metadata

    def pre_create_security_health_analytics_custom_module(
        self,
        request: securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_create_security_health_analytics_custom_module(
        self,
        response: gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
    ) -> (
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    ):
        """Post-rpc interceptor for create_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_create_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_create_security_health_analytics_custom_module` interceptor runs
        before the `post_create_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_create_security_health_analytics_custom_module_with_metadata(
        self,
        response: gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_create_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_create_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_create_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_create_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_create_security_health_analytics_custom_module` will be passed to
        `post_create_security_health_analytics_custom_module_with_metadata`.
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

    def pre_delete_big_query_export(
        self,
        request: securitycenter_service.DeleteBigQueryExportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.DeleteBigQueryExportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_big_query_export

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def pre_delete_event_threat_detection_custom_module(
        self,
        request: securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def pre_delete_mute_config(
        self,
        request: securitycenter_service.DeleteMuteConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.DeleteMuteConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_mute_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def pre_delete_notification_config(
        self,
        request: securitycenter_service.DeleteNotificationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.DeleteNotificationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_notification_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def pre_delete_resource_value_config(
        self,
        request: securitycenter_service.DeleteResourceValueConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.DeleteResourceValueConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_resource_value_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def pre_delete_security_health_analytics_custom_module(
        self,
        request: securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def pre_get_big_query_export(
        self,
        request: securitycenter_service.GetBigQueryExportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetBigQueryExportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_big_query_export

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_big_query_export(
        self, response: bigquery_export.BigQueryExport
    ) -> bigquery_export.BigQueryExport:
        """Post-rpc interceptor for get_big_query_export

        DEPRECATED. Please use the `post_get_big_query_export_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_big_query_export` interceptor runs
        before the `post_get_big_query_export_with_metadata` interceptor.
        """
        return response

    def post_get_big_query_export_with_metadata(
        self,
        response: bigquery_export.BigQueryExport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[bigquery_export.BigQueryExport, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_big_query_export

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_big_query_export_with_metadata`
        interceptor in new development instead of the `post_get_big_query_export` interceptor.
        When both interceptors are used, this `post_get_big_query_export_with_metadata` interceptor runs after the
        `post_get_big_query_export` interceptor. The (possibly modified) response returned by
        `post_get_big_query_export` will be passed to
        `post_get_big_query_export_with_metadata`.
        """
        return response, metadata

    def pre_get_effective_event_threat_detection_custom_module(
        self,
        request: securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_effective_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_effective_event_threat_detection_custom_module(
        self,
        response: effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule,
    ) -> effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule:
        """Post-rpc interceptor for get_effective_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_get_effective_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_effective_event_threat_detection_custom_module` interceptor runs
        before the `post_get_effective_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_get_effective_event_threat_detection_custom_module_with_metadata(
        self,
        response: effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_effective_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_effective_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_get_effective_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_get_effective_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_get_effective_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_get_effective_event_threat_detection_custom_module` will be passed to
        `post_get_effective_event_threat_detection_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_get_effective_security_health_analytics_custom_module(
        self,
        request: securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_effective_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_effective_security_health_analytics_custom_module(
        self,
        response: effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule,
    ) -> effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule:
        """Post-rpc interceptor for get_effective_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_get_effective_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_effective_security_health_analytics_custom_module` interceptor runs
        before the `post_get_effective_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_get_effective_security_health_analytics_custom_module_with_metadata(
        self,
        response: effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_effective_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_effective_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_get_effective_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_get_effective_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_get_effective_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_get_effective_security_health_analytics_custom_module` will be passed to
        `post_get_effective_security_health_analytics_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_get_event_threat_detection_custom_module(
        self,
        request: securitycenter_service.GetEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_event_threat_detection_custom_module(
        self,
        response: event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    ) -> event_threat_detection_custom_module.EventThreatDetectionCustomModule:
        """Post-rpc interceptor for get_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_get_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_event_threat_detection_custom_module` interceptor runs
        before the `post_get_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_get_event_threat_detection_custom_module_with_metadata(
        self,
        response: event_threat_detection_custom_module.EventThreatDetectionCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_threat_detection_custom_module.EventThreatDetectionCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_get_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_get_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_get_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_get_event_threat_detection_custom_module` will be passed to
        `post_get_event_threat_detection_custom_module_with_metadata`.
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

    def pre_get_mute_config(
        self,
        request: securitycenter_service.GetMuteConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetMuteConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_mute_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_mute_config(
        self, response: mute_config.MuteConfig
    ) -> mute_config.MuteConfig:
        """Post-rpc interceptor for get_mute_config

        DEPRECATED. Please use the `post_get_mute_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_mute_config` interceptor runs
        before the `post_get_mute_config_with_metadata` interceptor.
        """
        return response

    def post_get_mute_config_with_metadata(
        self,
        response: mute_config.MuteConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[mute_config.MuteConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_mute_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_mute_config_with_metadata`
        interceptor in new development instead of the `post_get_mute_config` interceptor.
        When both interceptors are used, this `post_get_mute_config_with_metadata` interceptor runs after the
        `post_get_mute_config` interceptor. The (possibly modified) response returned by
        `post_get_mute_config` will be passed to
        `post_get_mute_config_with_metadata`.
        """
        return response, metadata

    def pre_get_notification_config(
        self,
        request: securitycenter_service.GetNotificationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetNotificationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_notification_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_notification_config(
        self, response: notification_config.NotificationConfig
    ) -> notification_config.NotificationConfig:
        """Post-rpc interceptor for get_notification_config

        DEPRECATED. Please use the `post_get_notification_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_notification_config` interceptor runs
        before the `post_get_notification_config_with_metadata` interceptor.
        """
        return response

    def post_get_notification_config_with_metadata(
        self,
        response: notification_config.NotificationConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notification_config.NotificationConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_notification_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_notification_config_with_metadata`
        interceptor in new development instead of the `post_get_notification_config` interceptor.
        When both interceptors are used, this `post_get_notification_config_with_metadata` interceptor runs after the
        `post_get_notification_config` interceptor. The (possibly modified) response returned by
        `post_get_notification_config` will be passed to
        `post_get_notification_config_with_metadata`.
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

    def pre_get_resource_value_config(
        self,
        request: securitycenter_service.GetResourceValueConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetResourceValueConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_resource_value_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_resource_value_config(
        self, response: resource_value_config.ResourceValueConfig
    ) -> resource_value_config.ResourceValueConfig:
        """Post-rpc interceptor for get_resource_value_config

        DEPRECATED. Please use the `post_get_resource_value_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_resource_value_config` interceptor runs
        before the `post_get_resource_value_config_with_metadata` interceptor.
        """
        return response

    def post_get_resource_value_config_with_metadata(
        self,
        response: resource_value_config.ResourceValueConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        resource_value_config.ResourceValueConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_resource_value_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_resource_value_config_with_metadata`
        interceptor in new development instead of the `post_get_resource_value_config` interceptor.
        When both interceptors are used, this `post_get_resource_value_config_with_metadata` interceptor runs after the
        `post_get_resource_value_config` interceptor. The (possibly modified) response returned by
        `post_get_resource_value_config` will be passed to
        `post_get_resource_value_config_with_metadata`.
        """
        return response, metadata

    def pre_get_security_health_analytics_custom_module(
        self,
        request: securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_security_health_analytics_custom_module(
        self,
        response: security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
    ) -> security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule:
        """Post-rpc interceptor for get_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_get_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_security_health_analytics_custom_module` interceptor runs
        before the `post_get_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_get_security_health_analytics_custom_module_with_metadata(
        self,
        response: security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_get_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_get_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_get_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_get_security_health_analytics_custom_module` will be passed to
        `post_get_security_health_analytics_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_get_simulation(
        self,
        request: securitycenter_service.GetSimulationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetSimulationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_simulation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_simulation(
        self, response: simulation.Simulation
    ) -> simulation.Simulation:
        """Post-rpc interceptor for get_simulation

        DEPRECATED. Please use the `post_get_simulation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_simulation` interceptor runs
        before the `post_get_simulation_with_metadata` interceptor.
        """
        return response

    def post_get_simulation_with_metadata(
        self,
        response: simulation.Simulation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[simulation.Simulation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_simulation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_simulation_with_metadata`
        interceptor in new development instead of the `post_get_simulation` interceptor.
        When both interceptors are used, this `post_get_simulation_with_metadata` interceptor runs after the
        `post_get_simulation` interceptor. The (possibly modified) response returned by
        `post_get_simulation` will be passed to
        `post_get_simulation_with_metadata`.
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

    def pre_get_valued_resource(
        self,
        request: securitycenter_service.GetValuedResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.GetValuedResourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_valued_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_valued_resource(
        self, response: valued_resource.ValuedResource
    ) -> valued_resource.ValuedResource:
        """Post-rpc interceptor for get_valued_resource

        DEPRECATED. Please use the `post_get_valued_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_get_valued_resource` interceptor runs
        before the `post_get_valued_resource_with_metadata` interceptor.
        """
        return response

    def post_get_valued_resource_with_metadata(
        self,
        response: valued_resource.ValuedResource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[valued_resource.ValuedResource, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_valued_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_get_valued_resource_with_metadata`
        interceptor in new development instead of the `post_get_valued_resource` interceptor.
        When both interceptors are used, this `post_get_valued_resource_with_metadata` interceptor runs after the
        `post_get_valued_resource` interceptor. The (possibly modified) response returned by
        `post_get_valued_resource` will be passed to
        `post_get_valued_resource_with_metadata`.
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

    def pre_list_attack_paths(
        self,
        request: securitycenter_service.ListAttackPathsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListAttackPathsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_attack_paths

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_attack_paths(
        self, response: securitycenter_service.ListAttackPathsResponse
    ) -> securitycenter_service.ListAttackPathsResponse:
        """Post-rpc interceptor for list_attack_paths

        DEPRECATED. Please use the `post_list_attack_paths_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_attack_paths` interceptor runs
        before the `post_list_attack_paths_with_metadata` interceptor.
        """
        return response

    def post_list_attack_paths_with_metadata(
        self,
        response: securitycenter_service.ListAttackPathsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListAttackPathsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_attack_paths

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_attack_paths_with_metadata`
        interceptor in new development instead of the `post_list_attack_paths` interceptor.
        When both interceptors are used, this `post_list_attack_paths_with_metadata` interceptor runs after the
        `post_list_attack_paths` interceptor. The (possibly modified) response returned by
        `post_list_attack_paths` will be passed to
        `post_list_attack_paths_with_metadata`.
        """
        return response, metadata

    def pre_list_big_query_exports(
        self,
        request: securitycenter_service.ListBigQueryExportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListBigQueryExportsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_big_query_exports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_big_query_exports(
        self, response: securitycenter_service.ListBigQueryExportsResponse
    ) -> securitycenter_service.ListBigQueryExportsResponse:
        """Post-rpc interceptor for list_big_query_exports

        DEPRECATED. Please use the `post_list_big_query_exports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_big_query_exports` interceptor runs
        before the `post_list_big_query_exports_with_metadata` interceptor.
        """
        return response

    def post_list_big_query_exports_with_metadata(
        self,
        response: securitycenter_service.ListBigQueryExportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListBigQueryExportsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_big_query_exports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_big_query_exports_with_metadata`
        interceptor in new development instead of the `post_list_big_query_exports` interceptor.
        When both interceptors are used, this `post_list_big_query_exports_with_metadata` interceptor runs after the
        `post_list_big_query_exports` interceptor. The (possibly modified) response returned by
        `post_list_big_query_exports` will be passed to
        `post_list_big_query_exports_with_metadata`.
        """
        return response, metadata

    def pre_list_descendant_event_threat_detection_custom_modules(
        self,
        request: securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_descendant_event_threat_detection_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_descendant_event_threat_detection_custom_modules(
        self,
        response: securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse,
    ) -> securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse:
        """Post-rpc interceptor for list_descendant_event_threat_detection_custom_modules

        DEPRECATED. Please use the `post_list_descendant_event_threat_detection_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_descendant_event_threat_detection_custom_modules` interceptor runs
        before the `post_list_descendant_event_threat_detection_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_descendant_event_threat_detection_custom_modules_with_metadata(
        self,
        response: securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_descendant_event_threat_detection_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_descendant_event_threat_detection_custom_modules_with_metadata`
        interceptor in new development instead of the `post_list_descendant_event_threat_detection_custom_modules` interceptor.
        When both interceptors are used, this `post_list_descendant_event_threat_detection_custom_modules_with_metadata` interceptor runs after the
        `post_list_descendant_event_threat_detection_custom_modules` interceptor. The (possibly modified) response returned by
        `post_list_descendant_event_threat_detection_custom_modules` will be passed to
        `post_list_descendant_event_threat_detection_custom_modules_with_metadata`.
        """
        return response, metadata

    def pre_list_descendant_security_health_analytics_custom_modules(
        self,
        request: securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_descendant_security_health_analytics_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_descendant_security_health_analytics_custom_modules(
        self,
        response: securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
    ) -> securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse:
        """Post-rpc interceptor for list_descendant_security_health_analytics_custom_modules

        DEPRECATED. Please use the `post_list_descendant_security_health_analytics_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_descendant_security_health_analytics_custom_modules` interceptor runs
        before the `post_list_descendant_security_health_analytics_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_descendant_security_health_analytics_custom_modules_with_metadata(
        self,
        response: securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_descendant_security_health_analytics_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_descendant_security_health_analytics_custom_modules_with_metadata`
        interceptor in new development instead of the `post_list_descendant_security_health_analytics_custom_modules` interceptor.
        When both interceptors are used, this `post_list_descendant_security_health_analytics_custom_modules_with_metadata` interceptor runs after the
        `post_list_descendant_security_health_analytics_custom_modules` interceptor. The (possibly modified) response returned by
        `post_list_descendant_security_health_analytics_custom_modules` will be passed to
        `post_list_descendant_security_health_analytics_custom_modules_with_metadata`.
        """
        return response, metadata

    def pre_list_effective_event_threat_detection_custom_modules(
        self,
        request: securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_effective_event_threat_detection_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_effective_event_threat_detection_custom_modules(
        self,
        response: securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse,
    ) -> securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse:
        """Post-rpc interceptor for list_effective_event_threat_detection_custom_modules

        DEPRECATED. Please use the `post_list_effective_event_threat_detection_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_effective_event_threat_detection_custom_modules` interceptor runs
        before the `post_list_effective_event_threat_detection_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_effective_event_threat_detection_custom_modules_with_metadata(
        self,
        response: securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_effective_event_threat_detection_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_effective_event_threat_detection_custom_modules_with_metadata`
        interceptor in new development instead of the `post_list_effective_event_threat_detection_custom_modules` interceptor.
        When both interceptors are used, this `post_list_effective_event_threat_detection_custom_modules_with_metadata` interceptor runs after the
        `post_list_effective_event_threat_detection_custom_modules` interceptor. The (possibly modified) response returned by
        `post_list_effective_event_threat_detection_custom_modules` will be passed to
        `post_list_effective_event_threat_detection_custom_modules_with_metadata`.
        """
        return response, metadata

    def pre_list_effective_security_health_analytics_custom_modules(
        self,
        request: securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_effective_security_health_analytics_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_effective_security_health_analytics_custom_modules(
        self,
        response: securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
    ) -> (
        securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse
    ):
        """Post-rpc interceptor for list_effective_security_health_analytics_custom_modules

        DEPRECATED. Please use the `post_list_effective_security_health_analytics_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_effective_security_health_analytics_custom_modules` interceptor runs
        before the `post_list_effective_security_health_analytics_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_effective_security_health_analytics_custom_modules_with_metadata(
        self,
        response: securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_effective_security_health_analytics_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_effective_security_health_analytics_custom_modules_with_metadata`
        interceptor in new development instead of the `post_list_effective_security_health_analytics_custom_modules` interceptor.
        When both interceptors are used, this `post_list_effective_security_health_analytics_custom_modules_with_metadata` interceptor runs after the
        `post_list_effective_security_health_analytics_custom_modules` interceptor. The (possibly modified) response returned by
        `post_list_effective_security_health_analytics_custom_modules` will be passed to
        `post_list_effective_security_health_analytics_custom_modules_with_metadata`.
        """
        return response, metadata

    def pre_list_event_threat_detection_custom_modules(
        self,
        request: securitycenter_service.ListEventThreatDetectionCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListEventThreatDetectionCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_event_threat_detection_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_event_threat_detection_custom_modules(
        self,
        response: securitycenter_service.ListEventThreatDetectionCustomModulesResponse,
    ) -> securitycenter_service.ListEventThreatDetectionCustomModulesResponse:
        """Post-rpc interceptor for list_event_threat_detection_custom_modules

        DEPRECATED. Please use the `post_list_event_threat_detection_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_event_threat_detection_custom_modules` interceptor runs
        before the `post_list_event_threat_detection_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_event_threat_detection_custom_modules_with_metadata(
        self,
        response: securitycenter_service.ListEventThreatDetectionCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListEventThreatDetectionCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_event_threat_detection_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_event_threat_detection_custom_modules_with_metadata`
        interceptor in new development instead of the `post_list_event_threat_detection_custom_modules` interceptor.
        When both interceptors are used, this `post_list_event_threat_detection_custom_modules_with_metadata` interceptor runs after the
        `post_list_event_threat_detection_custom_modules` interceptor. The (possibly modified) response returned by
        `post_list_event_threat_detection_custom_modules` will be passed to
        `post_list_event_threat_detection_custom_modules_with_metadata`.
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

    def pre_list_mute_configs(
        self,
        request: securitycenter_service.ListMuteConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListMuteConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_mute_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_mute_configs(
        self, response: securitycenter_service.ListMuteConfigsResponse
    ) -> securitycenter_service.ListMuteConfigsResponse:
        """Post-rpc interceptor for list_mute_configs

        DEPRECATED. Please use the `post_list_mute_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_mute_configs` interceptor runs
        before the `post_list_mute_configs_with_metadata` interceptor.
        """
        return response

    def post_list_mute_configs_with_metadata(
        self,
        response: securitycenter_service.ListMuteConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListMuteConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_mute_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_mute_configs_with_metadata`
        interceptor in new development instead of the `post_list_mute_configs` interceptor.
        When both interceptors are used, this `post_list_mute_configs_with_metadata` interceptor runs after the
        `post_list_mute_configs` interceptor. The (possibly modified) response returned by
        `post_list_mute_configs` will be passed to
        `post_list_mute_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_notification_configs(
        self,
        request: securitycenter_service.ListNotificationConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListNotificationConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_notification_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_notification_configs(
        self, response: securitycenter_service.ListNotificationConfigsResponse
    ) -> securitycenter_service.ListNotificationConfigsResponse:
        """Post-rpc interceptor for list_notification_configs

        DEPRECATED. Please use the `post_list_notification_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_notification_configs` interceptor runs
        before the `post_list_notification_configs_with_metadata` interceptor.
        """
        return response

    def post_list_notification_configs_with_metadata(
        self,
        response: securitycenter_service.ListNotificationConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListNotificationConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_notification_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_notification_configs_with_metadata`
        interceptor in new development instead of the `post_list_notification_configs` interceptor.
        When both interceptors are used, this `post_list_notification_configs_with_metadata` interceptor runs after the
        `post_list_notification_configs` interceptor. The (possibly modified) response returned by
        `post_list_notification_configs` will be passed to
        `post_list_notification_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_resource_value_configs(
        self,
        request: securitycenter_service.ListResourceValueConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListResourceValueConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_resource_value_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_resource_value_configs(
        self, response: securitycenter_service.ListResourceValueConfigsResponse
    ) -> securitycenter_service.ListResourceValueConfigsResponse:
        """Post-rpc interceptor for list_resource_value_configs

        DEPRECATED. Please use the `post_list_resource_value_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_resource_value_configs` interceptor runs
        before the `post_list_resource_value_configs_with_metadata` interceptor.
        """
        return response

    def post_list_resource_value_configs_with_metadata(
        self,
        response: securitycenter_service.ListResourceValueConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListResourceValueConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_resource_value_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_resource_value_configs_with_metadata`
        interceptor in new development instead of the `post_list_resource_value_configs` interceptor.
        When both interceptors are used, this `post_list_resource_value_configs_with_metadata` interceptor runs after the
        `post_list_resource_value_configs` interceptor. The (possibly modified) response returned by
        `post_list_resource_value_configs` will be passed to
        `post_list_resource_value_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_security_health_analytics_custom_modules(
        self,
        request: securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_security_health_analytics_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_security_health_analytics_custom_modules(
        self,
        response: securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse,
    ) -> securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse:
        """Post-rpc interceptor for list_security_health_analytics_custom_modules

        DEPRECATED. Please use the `post_list_security_health_analytics_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_security_health_analytics_custom_modules` interceptor runs
        before the `post_list_security_health_analytics_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_security_health_analytics_custom_modules_with_metadata(
        self,
        response: securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_security_health_analytics_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_security_health_analytics_custom_modules_with_metadata`
        interceptor in new development instead of the `post_list_security_health_analytics_custom_modules` interceptor.
        When both interceptors are used, this `post_list_security_health_analytics_custom_modules_with_metadata` interceptor runs after the
        `post_list_security_health_analytics_custom_modules` interceptor. The (possibly modified) response returned by
        `post_list_security_health_analytics_custom_modules` will be passed to
        `post_list_security_health_analytics_custom_modules_with_metadata`.
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

    def pre_list_valued_resources(
        self,
        request: securitycenter_service.ListValuedResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListValuedResourcesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_valued_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_valued_resources(
        self, response: securitycenter_service.ListValuedResourcesResponse
    ) -> securitycenter_service.ListValuedResourcesResponse:
        """Post-rpc interceptor for list_valued_resources

        DEPRECATED. Please use the `post_list_valued_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_list_valued_resources` interceptor runs
        before the `post_list_valued_resources_with_metadata` interceptor.
        """
        return response

    def post_list_valued_resources_with_metadata(
        self,
        response: securitycenter_service.ListValuedResourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ListValuedResourcesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_valued_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_list_valued_resources_with_metadata`
        interceptor in new development instead of the `post_list_valued_resources` interceptor.
        When both interceptors are used, this `post_list_valued_resources_with_metadata` interceptor runs after the
        `post_list_valued_resources` interceptor. The (possibly modified) response returned by
        `post_list_valued_resources` will be passed to
        `post_list_valued_resources_with_metadata`.
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

    def pre_set_mute(
        self,
        request: securitycenter_service.SetMuteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.SetMuteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_mute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_set_mute(self, response: finding.Finding) -> finding.Finding:
        """Post-rpc interceptor for set_mute

        DEPRECATED. Please use the `post_set_mute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_set_mute` interceptor runs
        before the `post_set_mute_with_metadata` interceptor.
        """
        return response

    def post_set_mute_with_metadata(
        self,
        response: finding.Finding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[finding.Finding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_mute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_set_mute_with_metadata`
        interceptor in new development instead of the `post_set_mute` interceptor.
        When both interceptors are used, this `post_set_mute_with_metadata` interceptor runs after the
        `post_set_mute` interceptor. The (possibly modified) response returned by
        `post_set_mute` will be passed to
        `post_set_mute_with_metadata`.
        """
        return response, metadata

    def pre_simulate_security_health_analytics_custom_module(
        self,
        request: securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for simulate_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_simulate_security_health_analytics_custom_module(
        self,
        response: securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse,
    ) -> securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse:
        """Post-rpc interceptor for simulate_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_simulate_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_simulate_security_health_analytics_custom_module` interceptor runs
        before the `post_simulate_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_simulate_security_health_analytics_custom_module_with_metadata(
        self,
        response: securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for simulate_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_simulate_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_simulate_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_simulate_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_simulate_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_simulate_security_health_analytics_custom_module` will be passed to
        `post_simulate_security_health_analytics_custom_module_with_metadata`.
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

    def pre_update_big_query_export(
        self,
        request: securitycenter_service.UpdateBigQueryExportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateBigQueryExportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_big_query_export

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_big_query_export(
        self, response: bigquery_export.BigQueryExport
    ) -> bigquery_export.BigQueryExport:
        """Post-rpc interceptor for update_big_query_export

        DEPRECATED. Please use the `post_update_big_query_export_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_big_query_export` interceptor runs
        before the `post_update_big_query_export_with_metadata` interceptor.
        """
        return response

    def post_update_big_query_export_with_metadata(
        self,
        response: bigquery_export.BigQueryExport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[bigquery_export.BigQueryExport, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_big_query_export

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_big_query_export_with_metadata`
        interceptor in new development instead of the `post_update_big_query_export` interceptor.
        When both interceptors are used, this `post_update_big_query_export_with_metadata` interceptor runs after the
        `post_update_big_query_export` interceptor. The (possibly modified) response returned by
        `post_update_big_query_export` will be passed to
        `post_update_big_query_export_with_metadata`.
        """
        return response, metadata

    def pre_update_event_threat_detection_custom_module(
        self,
        request: securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_event_threat_detection_custom_module(
        self,
        response: gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    ) -> gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule:
        """Post-rpc interceptor for update_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_update_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_event_threat_detection_custom_module` interceptor runs
        before the `post_update_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_update_event_threat_detection_custom_module_with_metadata(
        self,
        response: gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_update_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_update_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_update_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_update_event_threat_detection_custom_module` will be passed to
        `post_update_event_threat_detection_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_update_external_system(
        self,
        request: securitycenter_service.UpdateExternalSystemRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateExternalSystemRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_external_system

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_external_system(
        self, response: gcs_external_system.ExternalSystem
    ) -> gcs_external_system.ExternalSystem:
        """Post-rpc interceptor for update_external_system

        DEPRECATED. Please use the `post_update_external_system_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_external_system` interceptor runs
        before the `post_update_external_system_with_metadata` interceptor.
        """
        return response

    def post_update_external_system_with_metadata(
        self,
        response: gcs_external_system.ExternalSystem,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_external_system.ExternalSystem, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_external_system

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_external_system_with_metadata`
        interceptor in new development instead of the `post_update_external_system` interceptor.
        When both interceptors are used, this `post_update_external_system_with_metadata` interceptor runs after the
        `post_update_external_system` interceptor. The (possibly modified) response returned by
        `post_update_external_system` will be passed to
        `post_update_external_system_with_metadata`.
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

    def pre_update_mute_config(
        self,
        request: securitycenter_service.UpdateMuteConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateMuteConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_mute_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_mute_config(
        self, response: gcs_mute_config.MuteConfig
    ) -> gcs_mute_config.MuteConfig:
        """Post-rpc interceptor for update_mute_config

        DEPRECATED. Please use the `post_update_mute_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_mute_config` interceptor runs
        before the `post_update_mute_config_with_metadata` interceptor.
        """
        return response

    def post_update_mute_config_with_metadata(
        self,
        response: gcs_mute_config.MuteConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcs_mute_config.MuteConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_mute_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_mute_config_with_metadata`
        interceptor in new development instead of the `post_update_mute_config` interceptor.
        When both interceptors are used, this `post_update_mute_config_with_metadata` interceptor runs after the
        `post_update_mute_config` interceptor. The (possibly modified) response returned by
        `post_update_mute_config` will be passed to
        `post_update_mute_config_with_metadata`.
        """
        return response, metadata

    def pre_update_notification_config(
        self,
        request: securitycenter_service.UpdateNotificationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateNotificationConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_notification_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_notification_config(
        self, response: gcs_notification_config.NotificationConfig
    ) -> gcs_notification_config.NotificationConfig:
        """Post-rpc interceptor for update_notification_config

        DEPRECATED. Please use the `post_update_notification_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_notification_config` interceptor runs
        before the `post_update_notification_config_with_metadata` interceptor.
        """
        return response

    def post_update_notification_config_with_metadata(
        self,
        response: gcs_notification_config.NotificationConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_notification_config.NotificationConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_notification_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_notification_config_with_metadata`
        interceptor in new development instead of the `post_update_notification_config` interceptor.
        When both interceptors are used, this `post_update_notification_config_with_metadata` interceptor runs after the
        `post_update_notification_config` interceptor. The (possibly modified) response returned by
        `post_update_notification_config` will be passed to
        `post_update_notification_config_with_metadata`.
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

    def pre_update_resource_value_config(
        self,
        request: securitycenter_service.UpdateResourceValueConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateResourceValueConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_resource_value_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_resource_value_config(
        self, response: gcs_resource_value_config.ResourceValueConfig
    ) -> gcs_resource_value_config.ResourceValueConfig:
        """Post-rpc interceptor for update_resource_value_config

        DEPRECATED. Please use the `post_update_resource_value_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_resource_value_config` interceptor runs
        before the `post_update_resource_value_config_with_metadata` interceptor.
        """
        return response

    def post_update_resource_value_config_with_metadata(
        self,
        response: gcs_resource_value_config.ResourceValueConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_resource_value_config.ResourceValueConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_resource_value_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_resource_value_config_with_metadata`
        interceptor in new development instead of the `post_update_resource_value_config` interceptor.
        When both interceptors are used, this `post_update_resource_value_config_with_metadata` interceptor runs after the
        `post_update_resource_value_config` interceptor. The (possibly modified) response returned by
        `post_update_resource_value_config` will be passed to
        `post_update_resource_value_config_with_metadata`.
        """
        return response, metadata

    def pre_update_security_health_analytics_custom_module(
        self,
        request: securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_update_security_health_analytics_custom_module(
        self,
        response: gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
    ) -> (
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    ):
        """Post-rpc interceptor for update_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_update_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_update_security_health_analytics_custom_module` interceptor runs
        before the `post_update_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_update_security_health_analytics_custom_module_with_metadata(
        self,
        response: gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_update_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_update_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_update_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_update_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_update_security_health_analytics_custom_module` will be passed to
        `post_update_security_health_analytics_custom_module_with_metadata`.
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

    def pre_validate_event_threat_detection_custom_module(
        self,
        request: securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for validate_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_validate_event_threat_detection_custom_module(
        self,
        response: securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse,
    ) -> securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse:
        """Post-rpc interceptor for validate_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_validate_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code. This `post_validate_event_threat_detection_custom_module` interceptor runs
        before the `post_validate_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_validate_event_threat_detection_custom_module_with_metadata(
        self,
        response: securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for validate_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenter server but before it is returned to user code.

        We recommend only using this `post_validate_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_validate_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_validate_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_validate_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_validate_event_threat_detection_custom_module` will be passed to
        `post_validate_event_threat_detection_custom_module_with_metadata`.
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
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the SecurityCenter server but before
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
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the SecurityCenter server but before
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
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the SecurityCenter server but before
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
        before they are sent to the SecurityCenter server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the SecurityCenter server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SecurityCenterRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SecurityCenterRestInterceptor


class SecurityCenterRestTransport(_BaseSecurityCenterRestTransport):
    """REST backend synchronous transport for SecurityCenter.

    V1 APIs for Security Center service.

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
                        "uri": "/v1/{name=organizations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=organizations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/operations}",
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

    class _BatchCreateResourceValueConfigs(
        _BaseSecurityCenterRestTransport._BaseBatchCreateResourceValueConfigs,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.BatchCreateResourceValueConfigs")

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
            request: securitycenter_service.BatchCreateResourceValueConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.BatchCreateResourceValueConfigsResponse:
            r"""Call the batch create resource
            value configs method over HTTP.

                Args:
                    request (~.securitycenter_service.BatchCreateResourceValueConfigsRequest):
                        The request object. Request message to create multiple
                    resource value configs
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.BatchCreateResourceValueConfigsResponse:
                        Response message for
                    BatchCreateResourceValueConfigs

            """

            http_options = _BaseSecurityCenterRestTransport._BaseBatchCreateResourceValueConfigs._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_create_resource_value_configs(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseBatchCreateResourceValueConfigs,
                    "_BaseBatchCreateResourceValueConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.BatchCreateResourceValueConfigs",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "BatchCreateResourceValueConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._BatchCreateResourceValueConfigs._get_response(
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
            resp = securitycenter_service.BatchCreateResourceValueConfigsResponse()
            pb_resp = securitycenter_service.BatchCreateResourceValueConfigsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_resource_value_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_resource_value_configs_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.BatchCreateResourceValueConfigsResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.batch_create_resource_value_configs",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "BatchCreateResourceValueConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BulkMuteFindings(
        _BaseSecurityCenterRestTransport._BaseBulkMuteFindings, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.BulkMuteFindings")

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
            request: securitycenter_service.BulkMuteFindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the bulk mute findings method over HTTP.

            Args:
                request (~.securitycenter_service.BulkMuteFindingsRequest):
                    The request object. Request message for bulk findings
                update.
                Note:

                1. If multiple bulk update requests
                    match the same resource, the order
                    in which they get executed is not
                    defined.
                2. Once a bulk operation is started,
                    there is no way to stop it.
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

            http_options = _BaseSecurityCenterRestTransport._BaseBulkMuteFindings._get_http_options()
            request, metadata = self._interceptor.pre_bulk_mute_findings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseBulkMuteFindings,
                    "_BaseBulkMuteFindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.BulkMuteFindings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "BulkMuteFindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._BulkMuteFindings._get_response(
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

            resp = self._interceptor.post_bulk_mute_findings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_mute_findings_with_metadata(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.bulk_mute_findings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "BulkMuteFindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBigQueryExport(
        _BaseSecurityCenterRestTransport._BaseCreateBigQueryExport,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.CreateBigQueryExport")

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
            request: securitycenter_service.CreateBigQueryExportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> bigquery_export.BigQueryExport:
            r"""Call the create big query export method over HTTP.

            Args:
                request (~.securitycenter_service.CreateBigQueryExportRequest):
                    The request object. Request message for creating a
                BigQuery export.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.bigquery_export.BigQueryExport:
                    Configures how to deliver Findings to
                BigQuery Instance.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseCreateBigQueryExport._get_http_options()
            request, metadata = self._interceptor.pre_create_big_query_export(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseCreateBigQueryExport,
                    "_BaseCreateBigQueryExport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.CreateBigQueryExport",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateBigQueryExport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._CreateBigQueryExport._get_response(
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
            resp = bigquery_export.BigQueryExport()
            pb_resp = bigquery_export.BigQueryExport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_big_query_export(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_big_query_export_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = bigquery_export.BigQueryExport.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.create_big_query_export",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateBigQueryExport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEventThreatDetectionCustomModule(
        _BaseSecurityCenterRestTransport._BaseCreateEventThreatDetectionCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.CreateEventThreatDetectionCustomModule"
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
            request: securitycenter_service.CreateEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule:
            r"""Call the create event threat
            detection custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.CreateEventThreatDetectionCustomModuleRequest):
                        The request object. Request to create an Event Threat
                    Detection custom module.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule:
                        Represents an instance of an Event
                    Threat Detection custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by child folders and projects.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseCreateEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseCreateEventThreatDetectionCustomModule,
                    "_BaseCreateEventThreatDetectionCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.CreateEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._CreateEventThreatDetectionCustomModule._get_response(
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
            resp = gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule()
            pb_resp = gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_event_threat_detection_custom_module(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_event_threat_detection_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.create_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

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
                like security, risk, health, or privacy,
                that is ingested into Security Command
                Center for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, a cross-site
                scripting (XSS) vulnerability in an App
                Engine application is a finding.

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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.CreateFinding",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.create_finding",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateFinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMuteConfig(
        _BaseSecurityCenterRestTransport._BaseCreateMuteConfig, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.CreateMuteConfig")

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
            request: securitycenter_service.CreateMuteConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_mute_config.MuteConfig:
            r"""Call the create mute config method over HTTP.

            Args:
                request (~.securitycenter_service.CreateMuteConfigRequest):
                    The request object. Request message for creating a mute
                config.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_mute_config.MuteConfig:
                    A mute config is a Cloud SCC resource
                that contains the configuration to mute
                create/update events of findings.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseCreateMuteConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_mute_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseCreateMuteConfig,
                    "_BaseCreateMuteConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.CreateMuteConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateMuteConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._CreateMuteConfig._get_response(
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
            resp = gcs_mute_config.MuteConfig()
            pb_resp = gcs_mute_config.MuteConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_mute_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_mute_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_mute_config.MuteConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.create_mute_config",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateMuteConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateNotificationConfig(
        _BaseSecurityCenterRestTransport._BaseCreateNotificationConfig,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.CreateNotificationConfig")

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
            request: securitycenter_service.CreateNotificationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_notification_config.NotificationConfig:
            r"""Call the create notification
            config method over HTTP.

                Args:
                    request (~.securitycenter_service.CreateNotificationConfigRequest):
                        The request object. Request message for creating a
                    notification config.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_notification_config.NotificationConfig:
                        Cloud Security Command Center (Cloud
                    SCC) notification configs.
                    A notification config is a Cloud SCC
                    resource that contains the configuration
                    to send notifications for create/update
                    events of findings, assets and etc.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseCreateNotificationConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_notification_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseCreateNotificationConfig,
                    "_BaseCreateNotificationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.CreateNotificationConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateNotificationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._CreateNotificationConfig._get_response(
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
            resp = gcs_notification_config.NotificationConfig()
            pb_resp = gcs_notification_config.NotificationConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_notification_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_notification_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcs_notification_config.NotificationConfig.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.create_notification_config",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateNotificationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterRestTransport._BaseCreateSecurityHealthAnalyticsCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.CreateSecurityHealthAnalyticsCustomModule"
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
            request: securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule:
            r"""Call the create security health
            analytics custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for creating Security
                    Health Analytics custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule:
                        Represents an instance of a Security
                    Health Analytics custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by the child folders and
                    projects.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseCreateSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseCreateSecurityHealthAnalyticsCustomModule,
                    "_BaseCreateSecurityHealthAnalyticsCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.CreateSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._CreateSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule()
            pb_resp = gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = (
                self._interceptor.post_create_security_health_analytics_custom_module(
                    resp
                )
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_security_health_analytics_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.create_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateSecurityHealthAnalyticsCustomModule",
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
                monitor, and other tools.

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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.CreateSource",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.create_source",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CreateSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBigQueryExport(
        _BaseSecurityCenterRestTransport._BaseDeleteBigQueryExport,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.DeleteBigQueryExport")

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
            request: securitycenter_service.DeleteBigQueryExportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete big query export method over HTTP.

            Args:
                request (~.securitycenter_service.DeleteBigQueryExportRequest):
                    The request object. Request message for deleting a
                BigQuery export.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseSecurityCenterRestTransport._BaseDeleteBigQueryExport._get_http_options()
            request, metadata = self._interceptor.pre_delete_big_query_export(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseDeleteBigQueryExport,
                    "_BaseDeleteBigQueryExport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.DeleteBigQueryExport",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "DeleteBigQueryExport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._DeleteBigQueryExport._get_response(
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

    class _DeleteEventThreatDetectionCustomModule(
        _BaseSecurityCenterRestTransport._BaseDeleteEventThreatDetectionCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.DeleteEventThreatDetectionCustomModule"
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
            request: securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete event threat
            detection custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest):
                        The request object. Request to delete an Event Threat
                    Detection custom module.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseSecurityCenterRestTransport._BaseDeleteEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseDeleteEventThreatDetectionCustomModule,
                    "_BaseDeleteEventThreatDetectionCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.DeleteEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "DeleteEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._DeleteEventThreatDetectionCustomModule._get_response(
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

    class _DeleteMuteConfig(
        _BaseSecurityCenterRestTransport._BaseDeleteMuteConfig, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.DeleteMuteConfig")

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
            request: securitycenter_service.DeleteMuteConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete mute config method over HTTP.

            Args:
                request (~.securitycenter_service.DeleteMuteConfigRequest):
                    The request object. Request message for deleting a mute
                config.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseSecurityCenterRestTransport._BaseDeleteMuteConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_mute_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseDeleteMuteConfig,
                    "_BaseDeleteMuteConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.DeleteMuteConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "DeleteMuteConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._DeleteMuteConfig._get_response(
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

    class _DeleteNotificationConfig(
        _BaseSecurityCenterRestTransport._BaseDeleteNotificationConfig,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.DeleteNotificationConfig")

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
            request: securitycenter_service.DeleteNotificationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete notification
            config method over HTTP.

                Args:
                    request (~.securitycenter_service.DeleteNotificationConfigRequest):
                        The request object. Request message for deleting a
                    notification config.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseSecurityCenterRestTransport._BaseDeleteNotificationConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_notification_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseDeleteNotificationConfig,
                    "_BaseDeleteNotificationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.DeleteNotificationConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "DeleteNotificationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._DeleteNotificationConfig._get_response(
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

    class _DeleteResourceValueConfig(
        _BaseSecurityCenterRestTransport._BaseDeleteResourceValueConfig,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.DeleteResourceValueConfig")

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
            request: securitycenter_service.DeleteResourceValueConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete resource value
            config method over HTTP.

                Args:
                    request (~.securitycenter_service.DeleteResourceValueConfigRequest):
                        The request object. Request message to delete resource
                    value config
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseSecurityCenterRestTransport._BaseDeleteResourceValueConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_resource_value_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseDeleteResourceValueConfig,
                    "_BaseDeleteResourceValueConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.DeleteResourceValueConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "DeleteResourceValueConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._DeleteResourceValueConfig._get_response(
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

    class _DeleteSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterRestTransport._BaseDeleteSecurityHealthAnalyticsCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.DeleteSecurityHealthAnalyticsCustomModule"
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
            request: securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete security health
            analytics custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for deleting Security
                    Health Analytics custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseSecurityCenterRestTransport._BaseDeleteSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseDeleteSecurityHealthAnalyticsCustomModule,
                    "_BaseDeleteSecurityHealthAnalyticsCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.DeleteSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "DeleteSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._DeleteSecurityHealthAnalyticsCustomModule._get_response(
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

    class _GetBigQueryExport(
        _BaseSecurityCenterRestTransport._BaseGetBigQueryExport, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetBigQueryExport")

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
            request: securitycenter_service.GetBigQueryExportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> bigquery_export.BigQueryExport:
            r"""Call the get big query export method over HTTP.

            Args:
                request (~.securitycenter_service.GetBigQueryExportRequest):
                    The request object. Request message for retrieving a
                BigQuery export.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.bigquery_export.BigQueryExport:
                    Configures how to deliver Findings to
                BigQuery Instance.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetBigQueryExport._get_http_options()
            request, metadata = self._interceptor.pre_get_big_query_export(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetBigQueryExport,
                    "_BaseGetBigQueryExport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetBigQueryExport",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetBigQueryExport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetBigQueryExport._get_response(
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
            resp = bigquery_export.BigQueryExport()
            pb_resp = bigquery_export.BigQueryExport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_big_query_export(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_big_query_export_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = bigquery_export.BigQueryExport.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_big_query_export",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetBigQueryExport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEffectiveEventThreatDetectionCustomModule(
        _BaseSecurityCenterRestTransport._BaseGetEffectiveEventThreatDetectionCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.GetEffectiveEventThreatDetectionCustomModule"
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
            request: securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule:
            r"""Call the get effective event
            threat detection custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest):
                        The request object. Request to get an
                    EffectiveEventThreatDetectionCustomModule.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule:
                        An EffectiveEventThreatDetectionCustomModule is the
                    representation of an Event Threat Detection custom
                    module at a specified level of the resource hierarchy:
                    organization, folder, or project. If a custom module is
                    inherited from a parent organization or folder, the
                    value of the ``enablement_state`` property in
                    EffectiveEventThreatDetectionCustomModule is set to the
                    value that is effective in the parent, instead of
                    ``INHERITED``. For example, if the module is enabled in
                    a parent organization or folder, the effective
                    ``enablement_state`` for the module in all child folders
                    or projects is also ``enabled``.
                    EffectiveEventThreatDetectionCustomModule is read-only.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetEffectiveEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_effective_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetEffectiveEventThreatDetectionCustomModule,
                    "_BaseGetEffectiveEventThreatDetectionCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetEffectiveEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetEffectiveEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetEffectiveEventThreatDetectionCustomModule._get_response(
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
            resp = effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule()
            pb_resp = effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_effective_event_threat_detection_custom_module(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_effective_event_threat_detection_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_effective_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetEffectiveEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEffectiveSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterRestTransport._BaseGetEffectiveSecurityHealthAnalyticsCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.GetEffectiveSecurityHealthAnalyticsCustomModule"
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
            request: securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule:
            r"""Call the get effective security
            health analytics custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for getting effective
                    Security Health Analytics custom
                    modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule:
                        An EffectiveSecurityHealthAnalyticsCustomModule is the
                    representation of a Security Health Analytics custom
                    module at a specified level of the resource hierarchy:
                    organization, folder, or project. If a custom module is
                    inherited from a parent organization or folder, the
                    value of the ``enablementState`` property in
                    EffectiveSecurityHealthAnalyticsCustomModule is set to
                    the value that is effective in the parent, instead of
                    ``INHERITED``. For example, if the module is enabled in
                    a parent organization or folder, the effective
                    enablement_state for the module in all child folders or
                    projects is also ``enabled``.
                    EffectiveSecurityHealthAnalyticsCustomModule is
                    read-only.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetEffectiveSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_effective_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetEffectiveSecurityHealthAnalyticsCustomModule,
                    "_BaseGetEffectiveSecurityHealthAnalyticsCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetEffectiveSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetEffectiveSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetEffectiveSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule()
            pb_resp = effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_effective_security_health_analytics_custom_module(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_effective_security_health_analytics_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_effective_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetEffectiveSecurityHealthAnalyticsCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEventThreatDetectionCustomModule(
        _BaseSecurityCenterRestTransport._BaseGetEventThreatDetectionCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.GetEventThreatDetectionCustomModule"
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
            request: securitycenter_service.GetEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> event_threat_detection_custom_module.EventThreatDetectionCustomModule:
            r"""Call the get event threat
            detection custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.GetEventThreatDetectionCustomModuleRequest):
                        The request object. Request to get an Event Threat
                    Detection custom module.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.event_threat_detection_custom_module.EventThreatDetectionCustomModule:
                        Represents an instance of an Event
                    Threat Detection custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by child folders and projects.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetEventThreatDetectionCustomModule,
                    "_BaseGetEventThreatDetectionCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetEventThreatDetectionCustomModule._get_response(
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
                event_threat_detection_custom_module.EventThreatDetectionCustomModule()
            )
            pb_resp = event_threat_detection_custom_module.EventThreatDetectionCustomModule.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_event_threat_detection_custom_module(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_event_threat_detection_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = event_threat_detection_custom_module.EventThreatDetectionCustomModule.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetEventThreatDetectionCustomModule",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_iam_policy",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMuteConfig(
        _BaseSecurityCenterRestTransport._BaseGetMuteConfig, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetMuteConfig")

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
            request: securitycenter_service.GetMuteConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mute_config.MuteConfig:
            r"""Call the get mute config method over HTTP.

            Args:
                request (~.securitycenter_service.GetMuteConfigRequest):
                    The request object. Request message for retrieving a mute
                config.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.mute_config.MuteConfig:
                    A mute config is a Cloud SCC resource
                that contains the configuration to mute
                create/update events of findings.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseGetMuteConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_mute_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetMuteConfig,
                    "_BaseGetMuteConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetMuteConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetMuteConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetMuteConfig._get_response(
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
            resp = mute_config.MuteConfig()
            pb_resp = mute_config.MuteConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mute_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_mute_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = mute_config.MuteConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_mute_config",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetMuteConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNotificationConfig(
        _BaseSecurityCenterRestTransport._BaseGetNotificationConfig,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetNotificationConfig")

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
            request: securitycenter_service.GetNotificationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> notification_config.NotificationConfig:
            r"""Call the get notification config method over HTTP.

            Args:
                request (~.securitycenter_service.GetNotificationConfigRequest):
                    The request object. Request message for getting a
                notification config.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.notification_config.NotificationConfig:
                    Cloud Security Command Center (Cloud
                SCC) notification configs.
                A notification config is a Cloud SCC
                resource that contains the configuration
                to send notifications for create/update
                events of findings, assets and etc.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetNotificationConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_notification_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetNotificationConfig,
                    "_BaseGetNotificationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetNotificationConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetNotificationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetNotificationConfig._get_response(
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
            resp = notification_config.NotificationConfig()
            pb_resp = notification_config.NotificationConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_notification_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_notification_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = notification_config.NotificationConfig.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_notification_config",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetNotificationConfig",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetOrganizationSettings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_organization_settings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetOrganizationSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetResourceValueConfig(
        _BaseSecurityCenterRestTransport._BaseGetResourceValueConfig,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetResourceValueConfig")

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
            request: securitycenter_service.GetResourceValueConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resource_value_config.ResourceValueConfig:
            r"""Call the get resource value config method over HTTP.

            Args:
                request (~.securitycenter_service.GetResourceValueConfigRequest):
                    The request object. Request message to get resource value
                config
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resource_value_config.ResourceValueConfig:
                    A resource value configuration (RVC)
                is a mapping configuration of user's
                resources to resource values. Used in
                Attack path simulations.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetResourceValueConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_resource_value_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetResourceValueConfig,
                    "_BaseGetResourceValueConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetResourceValueConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetResourceValueConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._GetResourceValueConfig._get_response(
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
            resp = resource_value_config.ResourceValueConfig()
            pb_resp = resource_value_config.ResourceValueConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_resource_value_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_resource_value_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        resource_value_config.ResourceValueConfig.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_resource_value_config",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetResourceValueConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterRestTransport._BaseGetSecurityHealthAnalyticsCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.GetSecurityHealthAnalyticsCustomModule"
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
            request: securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> (
            security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
        ):
            r"""Call the get security health
            analytics custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for getting Security
                    Health Analytics custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule:
                        Represents an instance of a Security
                    Health Analytics custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by the child folders and
                    projects.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetSecurityHealthAnalyticsCustomModule,
                    "_BaseGetSecurityHealthAnalyticsCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule()
            pb_resp = security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_security_health_analytics_custom_module(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_security_health_analytics_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetSecurityHealthAnalyticsCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSimulation(
        _BaseSecurityCenterRestTransport._BaseGetSimulation, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetSimulation")

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
            request: securitycenter_service.GetSimulationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> simulation.Simulation:
            r"""Call the get simulation method over HTTP.

            Args:
                request (~.securitycenter_service.GetSimulationRequest):
                    The request object. Request message for getting
                simulation. Simulation name can include
                "latest" to retrieve the latest
                simulation For example,
                "organizations/123/simulations/latest".
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.simulation.Simulation:
                    Attack path simulation
            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseGetSimulation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_simulation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetSimulation,
                    "_BaseGetSimulation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetSimulation",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetSimulation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetSimulation._get_response(
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
            resp = simulation.Simulation()
            pb_resp = simulation.Simulation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_simulation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_simulation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = simulation.Simulation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_simulation",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetSimulation",
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
                monitor, and other tools.

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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetSource",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_source",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetValuedResource(
        _BaseSecurityCenterRestTransport._BaseGetValuedResource, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetValuedResource")

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
            request: securitycenter_service.GetValuedResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> valued_resource.ValuedResource:
            r"""Call the get valued resource method over HTTP.

            Args:
                request (~.securitycenter_service.GetValuedResourceRequest):
                    The request object. Request message for getting a valued
                resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.valued_resource.ValuedResource:
                    A resource that is determined to have
                value to a user's system

            """

            http_options = _BaseSecurityCenterRestTransport._BaseGetValuedResource._get_http_options()
            request, metadata = self._interceptor.pre_get_valued_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetValuedResource,
                    "_BaseGetValuedResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetValuedResource",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetValuedResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetValuedResource._get_response(
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
            resp = valued_resource.ValuedResource()
            pb_resp = valued_resource.ValuedResource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_valued_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_valued_resource_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = valued_resource.ValuedResource.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.get_valued_resource",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetValuedResource",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GroupAssets",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.group_assets",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GroupFindings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.group_findings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListAssets",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_assets",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListAssets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAttackPaths(
        _BaseSecurityCenterRestTransport._BaseListAttackPaths, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListAttackPaths")

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
            request: securitycenter_service.ListAttackPathsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListAttackPathsResponse:
            r"""Call the list attack paths method over HTTP.

            Args:
                request (~.securitycenter_service.ListAttackPathsRequest):
                    The request object. Request message for listing the
                attack paths for a given simulation or
                valued resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.ListAttackPathsResponse:
                    Response message for listing the
                attack paths for a given simulation or
                valued resource.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListAttackPaths._get_http_options()
            request, metadata = self._interceptor.pre_list_attack_paths(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListAttackPaths,
                    "_BaseListAttackPaths__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListAttackPaths",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListAttackPaths",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListAttackPaths._get_response(
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
            resp = securitycenter_service.ListAttackPathsResponse()
            pb_resp = securitycenter_service.ListAttackPathsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_attack_paths(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_attack_paths_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListAttackPathsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_attack_paths",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListAttackPaths",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBigQueryExports(
        _BaseSecurityCenterRestTransport._BaseListBigQueryExports,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListBigQueryExports")

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
            request: securitycenter_service.ListBigQueryExportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListBigQueryExportsResponse:
            r"""Call the list big query exports method over HTTP.

            Args:
                request (~.securitycenter_service.ListBigQueryExportsRequest):
                    The request object. Request message for listing BigQuery
                exports at a given scope e.g.
                organization, folder or project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.ListBigQueryExportsResponse:
                    Response message for listing BigQuery
                exports.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListBigQueryExports._get_http_options()
            request, metadata = self._interceptor.pre_list_big_query_exports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListBigQueryExports,
                    "_BaseListBigQueryExports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListBigQueryExports",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListBigQueryExports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListBigQueryExports._get_response(
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
            resp = securitycenter_service.ListBigQueryExportsResponse()
            pb_resp = securitycenter_service.ListBigQueryExportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_big_query_exports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_big_query_exports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListBigQueryExportsResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_big_query_exports",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListBigQueryExports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDescendantEventThreatDetectionCustomModules(
        _BaseSecurityCenterRestTransport._BaseListDescendantEventThreatDetectionCustomModules,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.ListDescendantEventThreatDetectionCustomModules"
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
            request: securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse:
            r"""Call the list descendant event
            threat detection custom modules method over HTTP.

                Args:
                    request (~.securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest):
                        The request object. Request to list current and
                    descendant resident Event Threat
                    Detection custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse:
                        Response for listing current and
                    descendant resident Event Threat
                    Detection custom modules.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListDescendantEventThreatDetectionCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_descendant_event_threat_detection_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListDescendantEventThreatDetectionCustomModules,
                    "_BaseListDescendantEventThreatDetectionCustomModules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListDescendantEventThreatDetectionCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListDescendantEventThreatDetectionCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListDescendantEventThreatDetectionCustomModules._get_response(
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
            resp = securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse()
            pb_resp = securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_descendant_event_threat_detection_custom_modules(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_descendant_event_threat_detection_custom_modules_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_descendant_event_threat_detection_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListDescendantEventThreatDetectionCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDescendantSecurityHealthAnalyticsCustomModules(
        _BaseSecurityCenterRestTransport._BaseListDescendantSecurityHealthAnalyticsCustomModules,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.ListDescendantSecurityHealthAnalyticsCustomModules"
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
            request: securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse:
            r"""Call the list descendant security
            health analytics custom modules method over HTTP.

                Args:
                    request (~.securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest):
                        The request object. Request message for listing
                    descendant Security Health Analytics
                    custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse:
                        Response message for listing
                    descendant Security Health Analytics
                    custom modules.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListDescendantSecurityHealthAnalyticsCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_descendant_security_health_analytics_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListDescendantSecurityHealthAnalyticsCustomModules,
                    "_BaseListDescendantSecurityHealthAnalyticsCustomModules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListDescendantSecurityHealthAnalyticsCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListDescendantSecurityHealthAnalyticsCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListDescendantSecurityHealthAnalyticsCustomModules._get_response(
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
            resp = securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse()
            pb_resp = securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_descendant_security_health_analytics_custom_modules(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_descendant_security_health_analytics_custom_modules_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_descendant_security_health_analytics_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListDescendantSecurityHealthAnalyticsCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEffectiveEventThreatDetectionCustomModules(
        _BaseSecurityCenterRestTransport._BaseListEffectiveEventThreatDetectionCustomModules,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.ListEffectiveEventThreatDetectionCustomModules"
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
            request: securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse:
            r"""Call the list effective event
            threat detection custom modules method over HTTP.

                Args:
                    request (~.securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest):
                        The request object. Request to list effective Event
                    Threat Detection custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse:
                        Response for listing
                    EffectiveEventThreatDetectionCustomModules.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListEffectiveEventThreatDetectionCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_effective_event_threat_detection_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListEffectiveEventThreatDetectionCustomModules,
                    "_BaseListEffectiveEventThreatDetectionCustomModules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListEffectiveEventThreatDetectionCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListEffectiveEventThreatDetectionCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListEffectiveEventThreatDetectionCustomModules._get_response(
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
            resp = securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse()
            pb_resp = securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_effective_event_threat_detection_custom_modules(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_effective_event_threat_detection_custom_modules_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_effective_event_threat_detection_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListEffectiveEventThreatDetectionCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEffectiveSecurityHealthAnalyticsCustomModules(
        _BaseSecurityCenterRestTransport._BaseListEffectiveSecurityHealthAnalyticsCustomModules,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.ListEffectiveSecurityHealthAnalyticsCustomModules"
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
            request: securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse:
            r"""Call the list effective security
            health analytics custom modules method over HTTP.

                Args:
                    request (~.securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest):
                        The request object. Request message for listing effective
                    Security Health Analytics custom
                    modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse:
                        Response message for listing
                    effective Security Health Analytics
                    custom modules.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListEffectiveSecurityHealthAnalyticsCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_effective_security_health_analytics_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListEffectiveSecurityHealthAnalyticsCustomModules,
                    "_BaseListEffectiveSecurityHealthAnalyticsCustomModules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListEffectiveSecurityHealthAnalyticsCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListEffectiveSecurityHealthAnalyticsCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListEffectiveSecurityHealthAnalyticsCustomModules._get_response(
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
            resp = securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse()
            pb_resp = securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_effective_security_health_analytics_custom_modules(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_effective_security_health_analytics_custom_modules_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_effective_security_health_analytics_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListEffectiveSecurityHealthAnalyticsCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEventThreatDetectionCustomModules(
        _BaseSecurityCenterRestTransport._BaseListEventThreatDetectionCustomModules,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.ListEventThreatDetectionCustomModules"
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
            request: securitycenter_service.ListEventThreatDetectionCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListEventThreatDetectionCustomModulesResponse:
            r"""Call the list event threat
            detection custom modules method over HTTP.

                Args:
                    request (~.securitycenter_service.ListEventThreatDetectionCustomModulesRequest):
                        The request object. Request to list Event Threat
                    Detection custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.ListEventThreatDetectionCustomModulesResponse:
                        Response for listing Event Threat
                    Detection custom modules.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListEventThreatDetectionCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_event_threat_detection_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListEventThreatDetectionCustomModules,
                    "_BaseListEventThreatDetectionCustomModules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListEventThreatDetectionCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListEventThreatDetectionCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListEventThreatDetectionCustomModules._get_response(
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
                securitycenter_service.ListEventThreatDetectionCustomModulesResponse()
            )
            pb_resp = (
                securitycenter_service.ListEventThreatDetectionCustomModulesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_event_threat_detection_custom_modules(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_event_threat_detection_custom_modules_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.ListEventThreatDetectionCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_event_threat_detection_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListEventThreatDetectionCustomModules",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListFindings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_findings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListFindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMuteConfigs(
        _BaseSecurityCenterRestTransport._BaseListMuteConfigs, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListMuteConfigs")

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
            request: securitycenter_service.ListMuteConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListMuteConfigsResponse:
            r"""Call the list mute configs method over HTTP.

            Args:
                request (~.securitycenter_service.ListMuteConfigsRequest):
                    The request object. Request message for listing  mute
                configs at a given scope e.g.
                organization, folder or project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.ListMuteConfigsResponse:
                    Response message for listing mute
                configs.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListMuteConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_mute_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListMuteConfigs,
                    "_BaseListMuteConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListMuteConfigs",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListMuteConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListMuteConfigs._get_response(
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
            resp = securitycenter_service.ListMuteConfigsResponse()
            pb_resp = securitycenter_service.ListMuteConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_mute_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_mute_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListMuteConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_mute_configs",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListMuteConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNotificationConfigs(
        _BaseSecurityCenterRestTransport._BaseListNotificationConfigs,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListNotificationConfigs")

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
            request: securitycenter_service.ListNotificationConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListNotificationConfigsResponse:
            r"""Call the list notification configs method over HTTP.

            Args:
                request (~.securitycenter_service.ListNotificationConfigsRequest):
                    The request object. Request message for listing
                notification configs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.ListNotificationConfigsResponse:
                    Response message for listing
                notification configs.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListNotificationConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_notification_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListNotificationConfigs,
                    "_BaseListNotificationConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListNotificationConfigs",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListNotificationConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._ListNotificationConfigs._get_response(
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
            resp = securitycenter_service.ListNotificationConfigsResponse()
            pb_resp = securitycenter_service.ListNotificationConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_notification_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_notification_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListNotificationConfigsResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_notification_configs",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListNotificationConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListResourceValueConfigs(
        _BaseSecurityCenterRestTransport._BaseListResourceValueConfigs,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListResourceValueConfigs")

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
            request: securitycenter_service.ListResourceValueConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListResourceValueConfigsResponse:
            r"""Call the list resource value
            configs method over HTTP.

                Args:
                    request (~.securitycenter_service.ListResourceValueConfigsRequest):
                        The request object. Request message to list resource
                    value configs of a parent
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.ListResourceValueConfigsResponse:
                        Response message to list resource
                    value configs

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListResourceValueConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_resource_value_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListResourceValueConfigs,
                    "_BaseListResourceValueConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListResourceValueConfigs",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListResourceValueConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._ListResourceValueConfigs._get_response(
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
            resp = securitycenter_service.ListResourceValueConfigsResponse()
            pb_resp = securitycenter_service.ListResourceValueConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_resource_value_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_resource_value_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListResourceValueConfigsResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_resource_value_configs",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListResourceValueConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSecurityHealthAnalyticsCustomModules(
        _BaseSecurityCenterRestTransport._BaseListSecurityHealthAnalyticsCustomModules,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.ListSecurityHealthAnalyticsCustomModules"
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
            request: securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse:
            r"""Call the list security health
            analytics custom modules method over HTTP.

                Args:
                    request (~.securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest):
                        The request object. Request message for listing Security
                    Health Analytics custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse:
                        Response message for listing Security
                    Health Analytics custom modules.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListSecurityHealthAnalyticsCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_security_health_analytics_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListSecurityHealthAnalyticsCustomModules,
                    "_BaseListSecurityHealthAnalyticsCustomModules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListSecurityHealthAnalyticsCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListSecurityHealthAnalyticsCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListSecurityHealthAnalyticsCustomModules._get_response(
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
            resp = securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse()
            pb_resp = securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_security_health_analytics_custom_modules(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_security_health_analytics_custom_modules_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_security_health_analytics_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListSecurityHealthAnalyticsCustomModules",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListSources",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_sources",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListSources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListValuedResources(
        _BaseSecurityCenterRestTransport._BaseListValuedResources,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListValuedResources")

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
            request: securitycenter_service.ListValuedResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ListValuedResourcesResponse:
            r"""Call the list valued resources method over HTTP.

            Args:
                request (~.securitycenter_service.ListValuedResourcesRequest):
                    The request object. Request message for listing the
                valued resources for a given simulation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.securitycenter_service.ListValuedResourcesResponse:
                    Response message for listing the
                valued resources for a given simulation.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseListValuedResources._get_http_options()
            request, metadata = self._interceptor.pre_list_valued_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListValuedResources,
                    "_BaseListValuedResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListValuedResources",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListValuedResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListValuedResources._get_response(
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
            resp = securitycenter_service.ListValuedResourcesResponse()
            pb_resp = securitycenter_service.ListValuedResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_valued_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_valued_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        securitycenter_service.ListValuedResourcesResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.list_valued_resources",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListValuedResources",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.RunAssetDiscovery",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.run_asset_discovery",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                like security, risk, health, or privacy,
                that is ingested into Security Command
                Center for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, a cross-site
                scripting (XSS) vulnerability in an App
                Engine application is a finding.

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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.SetFindingState",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.set_finding_state",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.set_iam_policy",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "SetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetMute(
        _BaseSecurityCenterRestTransport._BaseSetMute, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.SetMute")

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
            request: securitycenter_service.SetMuteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> finding.Finding:
            r"""Call the set mute method over HTTP.

            Args:
                request (~.securitycenter_service.SetMuteRequest):
                    The request object. Request message for updating a
                finding's mute status.
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
                like security, risk, health, or privacy,
                that is ingested into Security Command
                Center for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, a cross-site
                scripting (XSS) vulnerability in an App
                Engine application is a finding.

            """

            http_options = (
                _BaseSecurityCenterRestTransport._BaseSetMute._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_mute(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseSetMute,
                    "_BaseSetMute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.SetMute",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "SetMute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._SetMute._get_response(
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

            resp = self._interceptor.post_set_mute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_mute_with_metadata(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.set_mute",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "SetMute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SimulateSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterRestTransport._BaseSimulateSecurityHealthAnalyticsCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.SimulateSecurityHealthAnalyticsCustomModule"
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
            request: securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse:
            r"""Call the simulate security health
            analytics custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message to simulate a
                    CustomConfig against a given test
                    resource. Maximum size of the request is
                    4 MB by default.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse:
                        Response message for simulating a
                    ``SecurityHealthAnalyticsCustomModule`` against a given
                    resource.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseSimulateSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_simulate_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseSimulateSecurityHealthAnalyticsCustomModule,
                    "_BaseSimulateSecurityHealthAnalyticsCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.SimulateSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "SimulateSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._SimulateSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse()
            pb_resp = securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = (
                self._interceptor.post_simulate_security_health_analytics_custom_module(
                    resp
                )
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_simulate_security_health_analytics_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.simulate_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "SimulateSecurityHealthAnalyticsCustomModule",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.test_iam_permissions",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "TestIamPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBigQueryExport(
        _BaseSecurityCenterRestTransport._BaseUpdateBigQueryExport,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateBigQueryExport")

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
            request: securitycenter_service.UpdateBigQueryExportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> bigquery_export.BigQueryExport:
            r"""Call the update big query export method over HTTP.

            Args:
                request (~.securitycenter_service.UpdateBigQueryExportRequest):
                    The request object. Request message for updating a
                BigQuery export.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.bigquery_export.BigQueryExport:
                    Configures how to deliver Findings to
                BigQuery Instance.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateBigQueryExport._get_http_options()
            request, metadata = self._interceptor.pre_update_big_query_export(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateBigQueryExport,
                    "_BaseUpdateBigQueryExport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateBigQueryExport",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateBigQueryExport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._UpdateBigQueryExport._get_response(
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
            resp = bigquery_export.BigQueryExport()
            pb_resp = bigquery_export.BigQueryExport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_big_query_export(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_big_query_export_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = bigquery_export.BigQueryExport.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_big_query_export",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateBigQueryExport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEventThreatDetectionCustomModule(
        _BaseSecurityCenterRestTransport._BaseUpdateEventThreatDetectionCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.UpdateEventThreatDetectionCustomModule"
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
            request: securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule:
            r"""Call the update event threat
            detection custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest):
                        The request object. Request to update an Event Threat
                    Detection custom module.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule:
                        Represents an instance of an Event
                    Threat Detection custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by child folders and projects.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateEventThreatDetectionCustomModule,
                    "_BaseUpdateEventThreatDetectionCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._UpdateEventThreatDetectionCustomModule._get_response(
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
            resp = gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule()
            pb_resp = gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_event_threat_detection_custom_module(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_event_threat_detection_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateExternalSystem(
        _BaseSecurityCenterRestTransport._BaseUpdateExternalSystem,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateExternalSystem")

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
            request: securitycenter_service.UpdateExternalSystemRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_external_system.ExternalSystem:
            r"""Call the update external system method over HTTP.

            Args:
                request (~.securitycenter_service.UpdateExternalSystemRequest):
                    The request object. Request message for updating a
                ExternalSystem resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_external_system.ExternalSystem:
                    Representation of third party
                SIEM/SOAR fields within SCC.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateExternalSystem._get_http_options()
            request, metadata = self._interceptor.pre_update_external_system(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateExternalSystem,
                    "_BaseUpdateExternalSystem__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateExternalSystem",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateExternalSystem",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._UpdateExternalSystem._get_response(
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
            resp = gcs_external_system.ExternalSystem()
            pb_resp = gcs_external_system.ExternalSystem.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_external_system(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_external_system_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_external_system.ExternalSystem.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_external_system",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateExternalSystem",
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
                like security, risk, health, or privacy,
                that is ingested into Security Command
                Center for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, a cross-site
                scripting (XSS) vulnerability in an App
                Engine application is a finding.

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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateFinding",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_finding",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateFinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMuteConfig(
        _BaseSecurityCenterRestTransport._BaseUpdateMuteConfig, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateMuteConfig")

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
            request: securitycenter_service.UpdateMuteConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_mute_config.MuteConfig:
            r"""Call the update mute config method over HTTP.

            Args:
                request (~.securitycenter_service.UpdateMuteConfigRequest):
                    The request object. Request message for updating a mute
                config.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcs_mute_config.MuteConfig:
                    A mute config is a Cloud SCC resource
                that contains the configuration to mute
                create/update events of findings.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateMuteConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_mute_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateMuteConfig,
                    "_BaseUpdateMuteConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateMuteConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateMuteConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._UpdateMuteConfig._get_response(
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
            resp = gcs_mute_config.MuteConfig()
            pb_resp = gcs_mute_config.MuteConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_mute_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_mute_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_mute_config.MuteConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_mute_config",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateMuteConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNotificationConfig(
        _BaseSecurityCenterRestTransport._BaseUpdateNotificationConfig,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateNotificationConfig")

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
            request: securitycenter_service.UpdateNotificationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_notification_config.NotificationConfig:
            r"""Call the update notification
            config method over HTTP.

                Args:
                    request (~.securitycenter_service.UpdateNotificationConfigRequest):
                        The request object. Request message for updating a
                    notification config.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_notification_config.NotificationConfig:
                        Cloud Security Command Center (Cloud
                    SCC) notification configs.
                    A notification config is a Cloud SCC
                    resource that contains the configuration
                    to send notifications for create/update
                    events of findings, assets and etc.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateNotificationConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_notification_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateNotificationConfig,
                    "_BaseUpdateNotificationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateNotificationConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateNotificationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._UpdateNotificationConfig._get_response(
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
            resp = gcs_notification_config.NotificationConfig()
            pb_resp = gcs_notification_config.NotificationConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_notification_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_notification_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcs_notification_config.NotificationConfig.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_notification_config",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateNotificationConfig",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateOrganizationSettings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_organization_settings",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateOrganizationSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateResourceValueConfig(
        _BaseSecurityCenterRestTransport._BaseUpdateResourceValueConfig,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.UpdateResourceValueConfig")

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
            request: securitycenter_service.UpdateResourceValueConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_resource_value_config.ResourceValueConfig:
            r"""Call the update resource value
            config method over HTTP.

                Args:
                    request (~.securitycenter_service.UpdateResourceValueConfigRequest):
                        The request object. Request message to update resource
                    value config
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_resource_value_config.ResourceValueConfig:
                        A resource value configuration (RVC)
                    is a mapping configuration of user's
                    resources to resource values. Used in
                    Attack path simulations.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateResourceValueConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_resource_value_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateResourceValueConfig,
                    "_BaseUpdateResourceValueConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateResourceValueConfig",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateResourceValueConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterRestTransport._UpdateResourceValueConfig._get_response(
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
            resp = gcs_resource_value_config.ResourceValueConfig()
            pb_resp = gcs_resource_value_config.ResourceValueConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_resource_value_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_resource_value_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcs_resource_value_config.ResourceValueConfig.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_resource_value_config",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateResourceValueConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterRestTransport._BaseUpdateSecurityHealthAnalyticsCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.UpdateSecurityHealthAnalyticsCustomModule"
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
            request: securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule:
            r"""Call the update security health
            analytics custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for updating Security
                    Health Analytics custom modules.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule:
                        Represents an instance of a Security
                    Health Analytics custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by the child folders and
                    projects.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseUpdateSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseUpdateSecurityHealthAnalyticsCustomModule,
                    "_BaseUpdateSecurityHealthAnalyticsCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._UpdateSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule()
            pb_resp = gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = (
                self._interceptor.post_update_security_health_analytics_custom_module(
                    resp
                )
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_security_health_analytics_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateSecurityHealthAnalyticsCustomModule",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateSecurityMarks",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_security_marks",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                monitor, and other tools.

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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.UpdateSource",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.update_source",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "UpdateSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ValidateEventThreatDetectionCustomModule(
        _BaseSecurityCenterRestTransport._BaseValidateEventThreatDetectionCustomModule,
        SecurityCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterRestTransport.ValidateEventThreatDetectionCustomModule"
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
            request: securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse:
            r"""Call the validate event threat
            detection custom module method over HTTP.

                Args:
                    request (~.securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest):
                        The request object. Request to validate an Event Threat
                    Detection custom module.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse:
                        Response to validating an Event
                    Threat Detection custom module.

            """

            http_options = _BaseSecurityCenterRestTransport._BaseValidateEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_validate_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseValidateEventThreatDetectionCustomModule,
                    "_BaseValidateEventThreatDetectionCustomModule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ValidateEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ValidateEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ValidateEventThreatDetectionCustomModule._get_response(
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
            resp = securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse()
            pb_resp = securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_validate_event_threat_detection_custom_module(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_validate_event_threat_detection_custom_module_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse.to_json(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterClient.validate_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ValidateEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_resource_value_configs(
        self,
    ) -> Callable[
        [securitycenter_service.BatchCreateResourceValueConfigsRequest],
        securitycenter_service.BatchCreateResourceValueConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateResourceValueConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def bulk_mute_findings(
        self,
    ) -> Callable[
        [securitycenter_service.BulkMuteFindingsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkMuteFindings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.CreateBigQueryExportRequest],
        bigquery_export.BigQueryExport,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBigQueryExport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.CreateEventThreatDetectionCustomModuleRequest],
        gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_finding(
        self,
    ) -> Callable[[securitycenter_service.CreateFindingRequest], gcs_finding.Finding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.CreateMuteConfigRequest], gcs_mute_config.MuteConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMuteConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.CreateNotificationConfigRequest],
        gcs_notification_config.NotificationConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNotificationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest],
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_source(
        self,
    ) -> Callable[[securitycenter_service.CreateSourceRequest], gcs_source.Source]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteBigQueryExportRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBigQueryExport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest],
        empty_pb2.Empty,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_mute_config(
        self,
    ) -> Callable[[securitycenter_service.DeleteMuteConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMuteConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteNotificationConfigRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNotificationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteResourceValueConfigRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteResourceValueConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest],
        empty_pb2.Empty,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.GetBigQueryExportRequest],
        bigquery_export.BigQueryExport,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBigQueryExport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_effective_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest],
        effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEffectiveEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_effective_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest],
        effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEffectiveSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.GetEventThreatDetectionCustomModuleRequest],
        event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetMuteConfigRequest], mute_config.MuteConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMuteConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetNotificationConfigRequest],
        notification_config.NotificationConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNotificationConfig(self._session, self._host, self._interceptor)  # type: ignore

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
    def get_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetResourceValueConfigRequest],
        resource_value_config.ResourceValueConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetResourceValueConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest],
        security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_simulation(
        self,
    ) -> Callable[[securitycenter_service.GetSimulationRequest], simulation.Simulation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSimulation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_source(
        self,
    ) -> Callable[[securitycenter_service.GetSourceRequest], source.Source]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_valued_resource(
        self,
    ) -> Callable[
        [securitycenter_service.GetValuedResourceRequest],
        valued_resource.ValuedResource,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetValuedResource(self._session, self._host, self._interceptor)  # type: ignore

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
    def list_attack_paths(
        self,
    ) -> Callable[
        [securitycenter_service.ListAttackPathsRequest],
        securitycenter_service.ListAttackPathsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAttackPaths(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_big_query_exports(
        self,
    ) -> Callable[
        [securitycenter_service.ListBigQueryExportsRequest],
        securitycenter_service.ListBigQueryExportsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBigQueryExports(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_descendant_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest],
        securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDescendantEventThreatDetectionCustomModules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_descendant_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [
            securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest
        ],
        securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDescendantSecurityHealthAnalyticsCustomModules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_effective_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest],
        securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEffectiveEventThreatDetectionCustomModules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_effective_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [
            securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest
        ],
        securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEffectiveSecurityHealthAnalyticsCustomModules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [securitycenter_service.ListEventThreatDetectionCustomModulesRequest],
        securitycenter_service.ListEventThreatDetectionCustomModulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEventThreatDetectionCustomModules(
            self._session, self._host, self._interceptor
        )  # type: ignore

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
    def list_mute_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListMuteConfigsRequest],
        securitycenter_service.ListMuteConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMuteConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_notification_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListNotificationConfigsRequest],
        securitycenter_service.ListNotificationConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNotificationConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_resource_value_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListResourceValueConfigsRequest],
        securitycenter_service.ListResourceValueConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListResourceValueConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest],
        securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSecurityHealthAnalyticsCustomModules(
            self._session, self._host, self._interceptor
        )  # type: ignore

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
    def list_valued_resources(
        self,
    ) -> Callable[
        [securitycenter_service.ListValuedResourcesRequest],
        securitycenter_service.ListValuedResourcesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListValuedResources(self._session, self._host, self._interceptor)  # type: ignore

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
    def set_mute(
        self,
    ) -> Callable[[securitycenter_service.SetMuteRequest], finding.Finding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetMute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def simulate_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest],
        securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SimulateSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

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
    def update_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateBigQueryExportRequest],
        bigquery_export.BigQueryExport,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBigQueryExport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest],
        gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_external_system(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateExternalSystemRequest],
        gcs_external_system.ExternalSystem,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateExternalSystem(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_finding(
        self,
    ) -> Callable[[securitycenter_service.UpdateFindingRequest], gcs_finding.Finding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateMuteConfigRequest], gcs_mute_config.MuteConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMuteConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateNotificationConfigRequest],
        gcs_notification_config.NotificationConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNotificationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

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
    def update_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateResourceValueConfigRequest],
        gcs_resource_value_config.ResourceValueConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateResourceValueConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest],
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSecurityHealthAnalyticsCustomModule(
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
    def validate_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest],
        securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseSecurityCenterRestTransport._BaseCancelOperation, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.CancelOperation")

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

            http_options = _BaseSecurityCenterRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseSecurityCenterRestTransport._BaseDeleteOperation, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.DeleteOperation")

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

            http_options = _BaseSecurityCenterRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._DeleteOperation._get_response(
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
        _BaseSecurityCenterRestTransport._BaseGetOperation, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.GetOperation")

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
                _BaseSecurityCenterRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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
        _BaseSecurityCenterRestTransport._BaseListOperations, SecurityCenterRestStub
    ):
        def __hash__(self):
            return hash("SecurityCenterRestTransport.ListOperations")

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
                _BaseSecurityCenterRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.securitycenter_v1.SecurityCenterClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.securitycenter_v1.SecurityCenterAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
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


__all__ = ("SecurityCenterRestTransport",)
