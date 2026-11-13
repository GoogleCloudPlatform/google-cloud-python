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
from google.cloud.location import locations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.securitycentermanagement_v1._compat import transcode_request
from google.cloud.securitycentermanagement_v1.types import security_center_management

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSecurityCenterManagementRestTransport

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


class SecurityCenterManagementRestInterceptor:
    """Interceptor for SecurityCenterManagement.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SecurityCenterManagementRestTransport.

    .. code-block:: python
        class MyCustomSecurityCenterManagementInterceptor(SecurityCenterManagementRestInterceptor):
            def pre_create_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_event_threat_detection_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_security_health_analytics_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

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

            def pre_get_security_center_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_security_center_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_security_health_analytics_custom_module(self, response):
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

            def pre_list_security_center_services(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_security_center_services(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_security_health_analytics_custom_modules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_security_health_analytics_custom_modules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_simulate_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_simulate_security_health_analytics_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_event_threat_detection_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_security_center_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_security_center_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_security_health_analytics_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_security_health_analytics_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_validate_event_threat_detection_custom_module(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_event_threat_detection_custom_module(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SecurityCenterManagementRestTransport(interceptor=MyCustomSecurityCenterManagementInterceptor())
        client = SecurityCenterManagementClient(transport=transport)


    """

    def pre_create_event_threat_detection_custom_module(
        self,
        request: security_center_management.CreateEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.CreateEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_create_event_threat_detection_custom_module(
        self, response: security_center_management.EventThreatDetectionCustomModule
    ) -> security_center_management.EventThreatDetectionCustomModule:
        """Post-rpc interceptor for create_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_create_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_create_event_threat_detection_custom_module` interceptor runs
        before the `post_create_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_create_event_threat_detection_custom_module_with_metadata(
        self,
        response: security_center_management.EventThreatDetectionCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.EventThreatDetectionCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_create_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_create_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_create_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_create_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_create_event_threat_detection_custom_module` will be passed to
        `post_create_event_threat_detection_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_create_security_health_analytics_custom_module(
        self,
        request: security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_create_security_health_analytics_custom_module(
        self, response: security_center_management.SecurityHealthAnalyticsCustomModule
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        """Post-rpc interceptor for create_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_create_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_create_security_health_analytics_custom_module` interceptor runs
        before the `post_create_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_create_security_health_analytics_custom_module_with_metadata(
        self,
        response: security_center_management.SecurityHealthAnalyticsCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.SecurityHealthAnalyticsCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_create_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_create_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_create_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_create_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_create_security_health_analytics_custom_module` will be passed to
        `post_create_security_health_analytics_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_delete_event_threat_detection_custom_module(
        self,
        request: security_center_management.DeleteEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.DeleteEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def pre_delete_security_health_analytics_custom_module(
        self,
        request: security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def pre_get_effective_event_threat_detection_custom_module(
        self,
        request: security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_effective_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_get_effective_event_threat_detection_custom_module(
        self,
        response: security_center_management.EffectiveEventThreatDetectionCustomModule,
    ) -> security_center_management.EffectiveEventThreatDetectionCustomModule:
        """Post-rpc interceptor for get_effective_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_get_effective_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_get_effective_event_threat_detection_custom_module` interceptor runs
        before the `post_get_effective_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_get_effective_event_threat_detection_custom_module_with_metadata(
        self,
        response: security_center_management.EffectiveEventThreatDetectionCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.EffectiveEventThreatDetectionCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_effective_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

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
        request: security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_effective_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_get_effective_security_health_analytics_custom_module(
        self,
        response: security_center_management.EffectiveSecurityHealthAnalyticsCustomModule,
    ) -> security_center_management.EffectiveSecurityHealthAnalyticsCustomModule:
        """Post-rpc interceptor for get_effective_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_get_effective_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_get_effective_security_health_analytics_custom_module` interceptor runs
        before the `post_get_effective_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_get_effective_security_health_analytics_custom_module_with_metadata(
        self,
        response: security_center_management.EffectiveSecurityHealthAnalyticsCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.EffectiveSecurityHealthAnalyticsCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_effective_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

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
        request: security_center_management.GetEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.GetEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_get_event_threat_detection_custom_module(
        self, response: security_center_management.EventThreatDetectionCustomModule
    ) -> security_center_management.EventThreatDetectionCustomModule:
        """Post-rpc interceptor for get_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_get_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_get_event_threat_detection_custom_module` interceptor runs
        before the `post_get_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_get_event_threat_detection_custom_module_with_metadata(
        self,
        response: security_center_management.EventThreatDetectionCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.EventThreatDetectionCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_get_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_get_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_get_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_get_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_get_event_threat_detection_custom_module` will be passed to
        `post_get_event_threat_detection_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_get_security_center_service(
        self,
        request: security_center_management.GetSecurityCenterServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.GetSecurityCenterServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_security_center_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_get_security_center_service(
        self, response: security_center_management.SecurityCenterService
    ) -> security_center_management.SecurityCenterService:
        """Post-rpc interceptor for get_security_center_service

        DEPRECATED. Please use the `post_get_security_center_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_get_security_center_service` interceptor runs
        before the `post_get_security_center_service_with_metadata` interceptor.
        """
        return response

    def post_get_security_center_service_with_metadata(
        self,
        response: security_center_management.SecurityCenterService,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.SecurityCenterService,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_security_center_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_get_security_center_service_with_metadata`
        interceptor in new development instead of the `post_get_security_center_service` interceptor.
        When both interceptors are used, this `post_get_security_center_service_with_metadata` interceptor runs after the
        `post_get_security_center_service` interceptor. The (possibly modified) response returned by
        `post_get_security_center_service` will be passed to
        `post_get_security_center_service_with_metadata`.
        """
        return response, metadata

    def pre_get_security_health_analytics_custom_module(
        self,
        request: security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_get_security_health_analytics_custom_module(
        self, response: security_center_management.SecurityHealthAnalyticsCustomModule
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        """Post-rpc interceptor for get_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_get_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_get_security_health_analytics_custom_module` interceptor runs
        before the `post_get_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_get_security_health_analytics_custom_module_with_metadata(
        self,
        response: security_center_management.SecurityHealthAnalyticsCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.SecurityHealthAnalyticsCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_get_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_get_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_get_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_get_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_get_security_health_analytics_custom_module` will be passed to
        `post_get_security_health_analytics_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_list_descendant_event_threat_detection_custom_modules(
        self,
        request: security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_descendant_event_threat_detection_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_list_descendant_event_threat_detection_custom_modules(
        self,
        response: security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
    ) -> security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse:
        """Post-rpc interceptor for list_descendant_event_threat_detection_custom_modules

        DEPRECATED. Please use the `post_list_descendant_event_threat_detection_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_list_descendant_event_threat_detection_custom_modules` interceptor runs
        before the `post_list_descendant_event_threat_detection_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_descendant_event_threat_detection_custom_modules_with_metadata(
        self,
        response: security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_descendant_event_threat_detection_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

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
        request: security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_descendant_security_health_analytics_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_list_descendant_security_health_analytics_custom_modules(
        self,
        response: security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
    ) -> security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse:
        """Post-rpc interceptor for list_descendant_security_health_analytics_custom_modules

        DEPRECATED. Please use the `post_list_descendant_security_health_analytics_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_list_descendant_security_health_analytics_custom_modules` interceptor runs
        before the `post_list_descendant_security_health_analytics_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_descendant_security_health_analytics_custom_modules_with_metadata(
        self,
        response: security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_descendant_security_health_analytics_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

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
        request: security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_effective_event_threat_detection_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_list_effective_event_threat_detection_custom_modules(
        self,
        response: security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
    ) -> security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse:
        """Post-rpc interceptor for list_effective_event_threat_detection_custom_modules

        DEPRECATED. Please use the `post_list_effective_event_threat_detection_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_list_effective_event_threat_detection_custom_modules` interceptor runs
        before the `post_list_effective_event_threat_detection_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_effective_event_threat_detection_custom_modules_with_metadata(
        self,
        response: security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_effective_event_threat_detection_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

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
        request: security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_effective_security_health_analytics_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_list_effective_security_health_analytics_custom_modules(
        self,
        response: security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
    ) -> security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse:
        """Post-rpc interceptor for list_effective_security_health_analytics_custom_modules

        DEPRECATED. Please use the `post_list_effective_security_health_analytics_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_list_effective_security_health_analytics_custom_modules` interceptor runs
        before the `post_list_effective_security_health_analytics_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_effective_security_health_analytics_custom_modules_with_metadata(
        self,
        response: security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_effective_security_health_analytics_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

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
        request: security_center_management.ListEventThreatDetectionCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListEventThreatDetectionCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_event_threat_detection_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_list_event_threat_detection_custom_modules(
        self,
        response: security_center_management.ListEventThreatDetectionCustomModulesResponse,
    ) -> security_center_management.ListEventThreatDetectionCustomModulesResponse:
        """Post-rpc interceptor for list_event_threat_detection_custom_modules

        DEPRECATED. Please use the `post_list_event_threat_detection_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_list_event_threat_detection_custom_modules` interceptor runs
        before the `post_list_event_threat_detection_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_event_threat_detection_custom_modules_with_metadata(
        self,
        response: security_center_management.ListEventThreatDetectionCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListEventThreatDetectionCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_event_threat_detection_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_list_event_threat_detection_custom_modules_with_metadata`
        interceptor in new development instead of the `post_list_event_threat_detection_custom_modules` interceptor.
        When both interceptors are used, this `post_list_event_threat_detection_custom_modules_with_metadata` interceptor runs after the
        `post_list_event_threat_detection_custom_modules` interceptor. The (possibly modified) response returned by
        `post_list_event_threat_detection_custom_modules` will be passed to
        `post_list_event_threat_detection_custom_modules_with_metadata`.
        """
        return response, metadata

    def pre_list_security_center_services(
        self,
        request: security_center_management.ListSecurityCenterServicesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListSecurityCenterServicesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_security_center_services

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_list_security_center_services(
        self, response: security_center_management.ListSecurityCenterServicesResponse
    ) -> security_center_management.ListSecurityCenterServicesResponse:
        """Post-rpc interceptor for list_security_center_services

        DEPRECATED. Please use the `post_list_security_center_services_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_list_security_center_services` interceptor runs
        before the `post_list_security_center_services_with_metadata` interceptor.
        """
        return response

    def post_list_security_center_services_with_metadata(
        self,
        response: security_center_management.ListSecurityCenterServicesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListSecurityCenterServicesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_security_center_services

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_list_security_center_services_with_metadata`
        interceptor in new development instead of the `post_list_security_center_services` interceptor.
        When both interceptors are used, this `post_list_security_center_services_with_metadata` interceptor runs after the
        `post_list_security_center_services` interceptor. The (possibly modified) response returned by
        `post_list_security_center_services` will be passed to
        `post_list_security_center_services_with_metadata`.
        """
        return response, metadata

    def pre_list_security_health_analytics_custom_modules(
        self,
        request: security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_security_health_analytics_custom_modules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_list_security_health_analytics_custom_modules(
        self,
        response: security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
    ) -> security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse:
        """Post-rpc interceptor for list_security_health_analytics_custom_modules

        DEPRECATED. Please use the `post_list_security_health_analytics_custom_modules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_list_security_health_analytics_custom_modules` interceptor runs
        before the `post_list_security_health_analytics_custom_modules_with_metadata` interceptor.
        """
        return response

    def post_list_security_health_analytics_custom_modules_with_metadata(
        self,
        response: security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_security_health_analytics_custom_modules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_list_security_health_analytics_custom_modules_with_metadata`
        interceptor in new development instead of the `post_list_security_health_analytics_custom_modules` interceptor.
        When both interceptors are used, this `post_list_security_health_analytics_custom_modules_with_metadata` interceptor runs after the
        `post_list_security_health_analytics_custom_modules` interceptor. The (possibly modified) response returned by
        `post_list_security_health_analytics_custom_modules` will be passed to
        `post_list_security_health_analytics_custom_modules_with_metadata`.
        """
        return response, metadata

    def pre_simulate_security_health_analytics_custom_module(
        self,
        request: security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for simulate_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_simulate_security_health_analytics_custom_module(
        self,
        response: security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse,
    ) -> security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse:
        """Post-rpc interceptor for simulate_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_simulate_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_simulate_security_health_analytics_custom_module` interceptor runs
        before the `post_simulate_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_simulate_security_health_analytics_custom_module_with_metadata(
        self,
        response: security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for simulate_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_simulate_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_simulate_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_simulate_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_simulate_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_simulate_security_health_analytics_custom_module` will be passed to
        `post_simulate_security_health_analytics_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_update_event_threat_detection_custom_module(
        self,
        request: security_center_management.UpdateEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.UpdateEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_update_event_threat_detection_custom_module(
        self, response: security_center_management.EventThreatDetectionCustomModule
    ) -> security_center_management.EventThreatDetectionCustomModule:
        """Post-rpc interceptor for update_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_update_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_update_event_threat_detection_custom_module` interceptor runs
        before the `post_update_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_update_event_threat_detection_custom_module_with_metadata(
        self,
        response: security_center_management.EventThreatDetectionCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.EventThreatDetectionCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_update_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_update_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_update_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_update_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_update_event_threat_detection_custom_module` will be passed to
        `post_update_event_threat_detection_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_update_security_center_service(
        self,
        request: security_center_management.UpdateSecurityCenterServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.UpdateSecurityCenterServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_security_center_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_update_security_center_service(
        self, response: security_center_management.SecurityCenterService
    ) -> security_center_management.SecurityCenterService:
        """Post-rpc interceptor for update_security_center_service

        DEPRECATED. Please use the `post_update_security_center_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_update_security_center_service` interceptor runs
        before the `post_update_security_center_service_with_metadata` interceptor.
        """
        return response

    def post_update_security_center_service_with_metadata(
        self,
        response: security_center_management.SecurityCenterService,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.SecurityCenterService,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_security_center_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_update_security_center_service_with_metadata`
        interceptor in new development instead of the `post_update_security_center_service` interceptor.
        When both interceptors are used, this `post_update_security_center_service_with_metadata` interceptor runs after the
        `post_update_security_center_service` interceptor. The (possibly modified) response returned by
        `post_update_security_center_service` will be passed to
        `post_update_security_center_service_with_metadata`.
        """
        return response, metadata

    def pre_update_security_health_analytics_custom_module(
        self,
        request: security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_security_health_analytics_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_update_security_health_analytics_custom_module(
        self, response: security_center_management.SecurityHealthAnalyticsCustomModule
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        """Post-rpc interceptor for update_security_health_analytics_custom_module

        DEPRECATED. Please use the `post_update_security_health_analytics_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_update_security_health_analytics_custom_module` interceptor runs
        before the `post_update_security_health_analytics_custom_module_with_metadata` interceptor.
        """
        return response

    def post_update_security_health_analytics_custom_module_with_metadata(
        self,
        response: security_center_management.SecurityHealthAnalyticsCustomModule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.SecurityHealthAnalyticsCustomModule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_security_health_analytics_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_update_security_health_analytics_custom_module_with_metadata`
        interceptor in new development instead of the `post_update_security_health_analytics_custom_module` interceptor.
        When both interceptors are used, this `post_update_security_health_analytics_custom_module_with_metadata` interceptor runs after the
        `post_update_security_health_analytics_custom_module` interceptor. The (possibly modified) response returned by
        `post_update_security_health_analytics_custom_module` will be passed to
        `post_update_security_health_analytics_custom_module_with_metadata`.
        """
        return response, metadata

    def pre_validate_event_threat_detection_custom_module(
        self,
        request: security_center_management.ValidateEventThreatDetectionCustomModuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ValidateEventThreatDetectionCustomModuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for validate_event_threat_detection_custom_module

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_validate_event_threat_detection_custom_module(
        self,
        response: security_center_management.ValidateEventThreatDetectionCustomModuleResponse,
    ) -> security_center_management.ValidateEventThreatDetectionCustomModuleResponse:
        """Post-rpc interceptor for validate_event_threat_detection_custom_module

        DEPRECATED. Please use the `post_validate_event_threat_detection_custom_module_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code. This `post_validate_event_threat_detection_custom_module` interceptor runs
        before the `post_validate_event_threat_detection_custom_module_with_metadata` interceptor.
        """
        return response

    def post_validate_event_threat_detection_custom_module_with_metadata(
        self,
        response: security_center_management.ValidateEventThreatDetectionCustomModuleResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        security_center_management.ValidateEventThreatDetectionCustomModuleResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for validate_event_threat_detection_custom_module

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SecurityCenterManagement server but before it is returned to user code.

        We recommend only using this `post_validate_event_threat_detection_custom_module_with_metadata`
        interceptor in new development instead of the `post_validate_event_threat_detection_custom_module` interceptor.
        When both interceptors are used, this `post_validate_event_threat_detection_custom_module_with_metadata` interceptor runs after the
        `post_validate_event_threat_detection_custom_module` interceptor. The (possibly modified) response returned by
        `post_validate_event_threat_detection_custom_module` will be passed to
        `post_validate_event_threat_detection_custom_module_with_metadata`.
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
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the SecurityCenterManagement server but before
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
        before they are sent to the SecurityCenterManagement server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the SecurityCenterManagement server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SecurityCenterManagementRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SecurityCenterManagementRestInterceptor


class SecurityCenterManagementRestTransport(_BaseSecurityCenterManagementRestTransport):
    """REST backend synchronous transport for SecurityCenterManagement.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "securitycentermanagement.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SecurityCenterManagementRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'securitycentermanagement.googleapis.com').
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
            interceptor (Optional[SecurityCenterManagementRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SecurityCenterManagementRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateEventThreatDetectionCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseCreateEventThreatDetectionCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.CreateEventThreatDetectionCustomModule"
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
            request: security_center_management.CreateEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.EventThreatDetectionCustomModule:
            r"""Call the create event threat
            detection custom module method over HTTP.

                Args:
                    request (~.security_center_management.CreateEventThreatDetectionCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.CreateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateEventThreatDetectionCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.EventThreatDetectionCustomModule:
                        A Security Command Center resource
                    that contains the configuration and
                    enablement state of a custom module,
                    which enables Event Threat Detection to
                    write certain findings to Security
                    Command Center.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseCreateEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseCreateEventThreatDetectionCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.CreateEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "CreateEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._CreateEventThreatDetectionCustomModule._get_response(
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
            resp = security_center_management.EventThreatDetectionCustomModule()
            pb_resp = security_center_management.EventThreatDetectionCustomModule.pb(
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
                    response_payload = security_center_management.EventThreatDetectionCustomModule.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.create_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "CreateEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseCreateSecurityHealthAnalyticsCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.CreateSecurityHealthAnalyticsCustomModule"
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
            request: security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
            r"""Call the create security health
            analytics custom module method over HTTP.

                Args:
                    request (~.security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.SecurityHealthAnalyticsCustomModule:
                        Represents an instance of a Security
                    Health Analytics custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by the descendant folders and
                    projects.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseCreateSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseCreateSecurityHealthAnalyticsCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.CreateSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "CreateSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._CreateSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = security_center_management.SecurityHealthAnalyticsCustomModule()
            pb_resp = security_center_management.SecurityHealthAnalyticsCustomModule.pb(
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
                    response_payload = security_center_management.SecurityHealthAnalyticsCustomModule.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.create_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "CreateSecurityHealthAnalyticsCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEventThreatDetectionCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseDeleteEventThreatDetectionCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.DeleteEventThreatDetectionCustomModule"
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
            request: security_center_management.DeleteEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete event threat
            detection custom module method over HTTP.

                Args:
                    request (~.security_center_management.DeleteEventThreatDetectionCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.DeleteEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteEventThreatDetectionCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseDeleteEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseDeleteEventThreatDetectionCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.DeleteEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "DeleteEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._DeleteEventThreatDetectionCustomModule._get_response(
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

    class _DeleteSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseDeleteSecurityHealthAnalyticsCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.DeleteSecurityHealthAnalyticsCustomModule"
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
            request: security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete security health
            analytics custom module method over HTTP.

                Args:
                    request (~.security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseDeleteSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseDeleteSecurityHealthAnalyticsCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.DeleteSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "DeleteSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._DeleteSecurityHealthAnalyticsCustomModule._get_response(
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

    class _GetEffectiveEventThreatDetectionCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseGetEffectiveEventThreatDetectionCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.GetEffectiveEventThreatDetectionCustomModule"
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
            request: security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.EffectiveEventThreatDetectionCustomModule:
            r"""Call the get effective event
            threat detection custom module method over HTTP.

                Args:
                    request (~.security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.EffectiveEventThreatDetectionCustomModule:
                        The representation of an
                    [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule]
                    at a given level, taking hierarchy into account and
                    resolving various fields accordingly. For example, if
                    the module is enabled at the ancestor level, then
                    effective modules at all descendant levels will have
                    their enablement state set to ``ENABLED``. Similarly, if
                    ``module.inherited`` is set, then the effective module's
                    configuration will reflect the ancestor's configuration.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseGetEffectiveEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_effective_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseGetEffectiveEventThreatDetectionCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.GetEffectiveEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetEffectiveEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._GetEffectiveEventThreatDetectionCustomModule._get_response(
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
                security_center_management.EffectiveEventThreatDetectionCustomModule()
            )
            pb_resp = (
                security_center_management.EffectiveEventThreatDetectionCustomModule.pb(
                    resp
                )
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
                    response_payload = security_center_management.EffectiveEventThreatDetectionCustomModule.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.get_effective_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetEffectiveEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEffectiveSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseGetEffectiveSecurityHealthAnalyticsCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.GetEffectiveSecurityHealthAnalyticsCustomModule"
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
            request: security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.EffectiveSecurityHealthAnalyticsCustomModule:
            r"""Call the get effective security
            health analytics custom module method over HTTP.

                Args:
                    request (~.security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.EffectiveSecurityHealthAnalyticsCustomModule:
                        The representation of a Security Health Analytics custom
                    module at a specified level of the resource hierarchy:
                    organization, folder, or project. If a custom module is
                    inherited from an ancestor organization or folder, then
                    the enablement state is set to the value that is
                    effective in the parent, not to ``INHERITED``. For
                    example, if the module is enabled in an organization or
                    folder, then the effective enablement state for the
                    module is ``ENABLED`` in all descendant folders or
                    projects.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseGetEffectiveSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_effective_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseGetEffectiveSecurityHealthAnalyticsCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.GetEffectiveSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetEffectiveSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._GetEffectiveSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = security_center_management.EffectiveSecurityHealthAnalyticsCustomModule()
            pb_resp = security_center_management.EffectiveSecurityHealthAnalyticsCustomModule.pb(
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
                    response_payload = security_center_management.EffectiveSecurityHealthAnalyticsCustomModule.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.get_effective_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetEffectiveSecurityHealthAnalyticsCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEventThreatDetectionCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseGetEventThreatDetectionCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.GetEventThreatDetectionCustomModule"
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
            request: security_center_management.GetEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.EventThreatDetectionCustomModule:
            r"""Call the get event threat
            detection custom module method over HTTP.

                Args:
                    request (~.security_center_management.GetEventThreatDetectionCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.GetEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEventThreatDetectionCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.EventThreatDetectionCustomModule:
                        A Security Command Center resource
                    that contains the configuration and
                    enablement state of a custom module,
                    which enables Event Threat Detection to
                    write certain findings to Security
                    Command Center.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseGetEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseGetEventThreatDetectionCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.GetEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._GetEventThreatDetectionCustomModule._get_response(
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
            resp = security_center_management.EventThreatDetectionCustomModule()
            pb_resp = security_center_management.EventThreatDetectionCustomModule.pb(
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
                    response_payload = security_center_management.EventThreatDetectionCustomModule.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.get_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSecurityCenterService(
        _BaseSecurityCenterManagementRestTransport._BaseGetSecurityCenterService,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.GetSecurityCenterService"
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
            request: security_center_management.GetSecurityCenterServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.SecurityCenterService:
            r"""Call the get security center
            service method over HTTP.

                Args:
                    request (~.security_center_management.GetSecurityCenterServiceRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.GetSecurityCenterService][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityCenterService].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.SecurityCenterService:
                        Represents a particular Security
                    Command Center service. This includes
                    settings information such as top-level
                    enablement in addition to individual
                    module settings. Service settings can be
                    configured at the organization, folder,
                    or project level. Service settings at
                    the organization or folder level are
                    inherited by those in descendant folders
                    and projects.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseGetSecurityCenterService._get_http_options()
            request, metadata = self._interceptor.pre_get_security_center_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseGetSecurityCenterService,
                    "_BaseGetSecurityCenterService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.GetSecurityCenterService",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetSecurityCenterService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._GetSecurityCenterService._get_response(
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
            resp = security_center_management.SecurityCenterService()
            pb_resp = security_center_management.SecurityCenterService.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_security_center_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_security_center_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        security_center_management.SecurityCenterService.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.get_security_center_service",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetSecurityCenterService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseGetSecurityHealthAnalyticsCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.GetSecurityHealthAnalyticsCustomModule"
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
            request: security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
            r"""Call the get security health
            analytics custom module method over HTTP.

                Args:
                    request (~.security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.SecurityHealthAnalyticsCustomModule:
                        Represents an instance of a Security
                    Health Analytics custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by the descendant folders and
                    projects.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseGetSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseGetSecurityHealthAnalyticsCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.GetSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._GetSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = security_center_management.SecurityHealthAnalyticsCustomModule()
            pb_resp = security_center_management.SecurityHealthAnalyticsCustomModule.pb(
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
                    response_payload = security_center_management.SecurityHealthAnalyticsCustomModule.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.get_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetSecurityHealthAnalyticsCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDescendantEventThreatDetectionCustomModules(
        _BaseSecurityCenterManagementRestTransport._BaseListDescendantEventThreatDetectionCustomModules,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.ListDescendantEventThreatDetectionCustomModules"
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
            request: security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse:
            r"""Call the list descendant event
            threat detection custom modules method over HTTP.

                Args:
                    request (~.security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse:
                        Response message for
                    [SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseListDescendantEventThreatDetectionCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_descendant_event_threat_detection_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseListDescendantEventThreatDetectionCustomModules,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListDescendantEventThreatDetectionCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._ListDescendantEventThreatDetectionCustomModules._get_response(
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
            resp = security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse()
            pb_resp = security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse.pb(
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
                    response_payload = security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.list_descendant_event_threat_detection_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListDescendantEventThreatDetectionCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDescendantSecurityHealthAnalyticsCustomModules(
        _BaseSecurityCenterManagementRestTransport._BaseListDescendantSecurityHealthAnalyticsCustomModules,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.ListDescendantSecurityHealthAnalyticsCustomModules"
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
            request: security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse:
            r"""Call the list descendant security
            health analytics custom modules method over HTTP.

                Args:
                    request (~.security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse:
                        Response message for
                    [SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseListDescendantSecurityHealthAnalyticsCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_descendant_security_health_analytics_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseListDescendantSecurityHealthAnalyticsCustomModules,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListDescendantSecurityHealthAnalyticsCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._ListDescendantSecurityHealthAnalyticsCustomModules._get_response(
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
            resp = security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse()
            pb_resp = security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse.pb(
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
                    response_payload = security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.list_descendant_security_health_analytics_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListDescendantSecurityHealthAnalyticsCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEffectiveEventThreatDetectionCustomModules(
        _BaseSecurityCenterManagementRestTransport._BaseListEffectiveEventThreatDetectionCustomModules,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.ListEffectiveEventThreatDetectionCustomModules"
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
            request: security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse:
            r"""Call the list effective event
            threat detection custom modules method over HTTP.

                Args:
                    request (~.security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse:
                        Response message for
                    [SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseListEffectiveEventThreatDetectionCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_effective_event_threat_detection_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseListEffectiveEventThreatDetectionCustomModules,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListEffectiveEventThreatDetectionCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._ListEffectiveEventThreatDetectionCustomModules._get_response(
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
            resp = security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse()
            pb_resp = security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse.pb(
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
                    response_payload = security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.list_effective_event_threat_detection_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListEffectiveEventThreatDetectionCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEffectiveSecurityHealthAnalyticsCustomModules(
        _BaseSecurityCenterManagementRestTransport._BaseListEffectiveSecurityHealthAnalyticsCustomModules,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.ListEffectiveSecurityHealthAnalyticsCustomModules"
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
            request: security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse:
            r"""Call the list effective security
            health analytics custom modules method over HTTP.

                Args:
                    request (~.security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse:
                        Response message for
                    [SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseListEffectiveSecurityHealthAnalyticsCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_effective_security_health_analytics_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseListEffectiveSecurityHealthAnalyticsCustomModules,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListEffectiveSecurityHealthAnalyticsCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._ListEffectiveSecurityHealthAnalyticsCustomModules._get_response(
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
            resp = security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse()
            pb_resp = security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse.pb(
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
                    response_payload = security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.list_effective_security_health_analytics_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListEffectiveSecurityHealthAnalyticsCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEventThreatDetectionCustomModules(
        _BaseSecurityCenterManagementRestTransport._BaseListEventThreatDetectionCustomModules,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.ListEventThreatDetectionCustomModules"
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
            request: security_center_management.ListEventThreatDetectionCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.ListEventThreatDetectionCustomModulesResponse:
            r"""Call the list event threat
            detection custom modules method over HTTP.

                Args:
                    request (~.security_center_management.ListEventThreatDetectionCustomModulesRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.ListEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.ListEventThreatDetectionCustomModulesResponse:
                        Response message for
                    [SecurityCenterManagement.ListEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseListEventThreatDetectionCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_event_threat_detection_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseListEventThreatDetectionCustomModules,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ListEventThreatDetectionCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListEventThreatDetectionCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._ListEventThreatDetectionCustomModules._get_response(
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
            resp = security_center_management.ListEventThreatDetectionCustomModulesResponse()
            pb_resp = security_center_management.ListEventThreatDetectionCustomModulesResponse.pb(
                resp
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
                    response_payload = security_center_management.ListEventThreatDetectionCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.list_event_threat_detection_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListEventThreatDetectionCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSecurityCenterServices(
        _BaseSecurityCenterManagementRestTransport._BaseListSecurityCenterServices,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.ListSecurityCenterServices"
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
            request: security_center_management.ListSecurityCenterServicesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.ListSecurityCenterServicesResponse:
            r"""Call the list security center
            services method over HTTP.

                Args:
                    request (~.security_center_management.ListSecurityCenterServicesRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.ListSecurityCenterServices][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.ListSecurityCenterServicesResponse:
                        Response message for
                    [SecurityCenterManagement.ListSecurityCenterServices][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseListSecurityCenterServices._get_http_options()
            request, metadata = self._interceptor.pre_list_security_center_services(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseListSecurityCenterServices,
                    "_BaseListSecurityCenterServices__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ListSecurityCenterServices",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListSecurityCenterServices",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._ListSecurityCenterServices._get_response(
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
            resp = security_center_management.ListSecurityCenterServicesResponse()
            pb_resp = security_center_management.ListSecurityCenterServicesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_security_center_services(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_security_center_services_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = security_center_management.ListSecurityCenterServicesResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.list_security_center_services",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListSecurityCenterServices",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSecurityHealthAnalyticsCustomModules(
        _BaseSecurityCenterManagementRestTransport._BaseListSecurityHealthAnalyticsCustomModules,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.ListSecurityHealthAnalyticsCustomModules"
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
            request: security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> (
            security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse
        ):
            r"""Call the list security health
            analytics custom modules method over HTTP.

                Args:
                    request (~.security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse:
                        Response message for
                    [SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseListSecurityHealthAnalyticsCustomModules._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_security_health_analytics_custom_modules(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseListSecurityHealthAnalyticsCustomModules,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListSecurityHealthAnalyticsCustomModules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._ListSecurityHealthAnalyticsCustomModules._get_response(
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
            resp = security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse()
            pb_resp = security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse.pb(
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
                    response_payload = security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.list_security_health_analytics_custom_modules",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListSecurityHealthAnalyticsCustomModules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SimulateSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseSimulateSecurityHealthAnalyticsCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.SimulateSecurityHealthAnalyticsCustomModule"
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
            request: security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse:
            r"""Call the simulate security health
            analytics custom module method over HTTP.

                Args:
                    request (~.security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule].
                    The maximum size of the request is 4 MiB.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse:
                        Response message for
                    [SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseSimulateSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_simulate_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseSimulateSecurityHealthAnalyticsCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.SimulateSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "SimulateSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._SimulateSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse()
            pb_resp = security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse.pb(
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
                    response_payload = security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.simulate_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "SimulateSecurityHealthAnalyticsCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEventThreatDetectionCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseUpdateEventThreatDetectionCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.UpdateEventThreatDetectionCustomModule"
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
            request: security_center_management.UpdateEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.EventThreatDetectionCustomModule:
            r"""Call the update event threat
            detection custom module method over HTTP.

                Args:
                    request (~.security_center_management.UpdateEventThreatDetectionCustomModuleRequest):
                        The request object. Message for updating a
                    EventThreatDetectionCustomModule
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.EventThreatDetectionCustomModule:
                        A Security Command Center resource
                    that contains the configuration and
                    enablement state of a custom module,
                    which enables Event Threat Detection to
                    write certain findings to Security
                    Command Center.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseUpdateEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseUpdateEventThreatDetectionCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.UpdateEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "UpdateEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._UpdateEventThreatDetectionCustomModule._get_response(
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
            resp = security_center_management.EventThreatDetectionCustomModule()
            pb_resp = security_center_management.EventThreatDetectionCustomModule.pb(
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
                    response_payload = security_center_management.EventThreatDetectionCustomModule.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.update_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "UpdateEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSecurityCenterService(
        _BaseSecurityCenterManagementRestTransport._BaseUpdateSecurityCenterService,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.UpdateSecurityCenterService"
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
            request: security_center_management.UpdateSecurityCenterServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.SecurityCenterService:
            r"""Call the update security center
            service method over HTTP.

                Args:
                    request (~.security_center_management.UpdateSecurityCenterServiceRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.UpdateSecurityCenterService][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityCenterService].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.SecurityCenterService:
                        Represents a particular Security
                    Command Center service. This includes
                    settings information such as top-level
                    enablement in addition to individual
                    module settings. Service settings can be
                    configured at the organization, folder,
                    or project level. Service settings at
                    the organization or folder level are
                    inherited by those in descendant folders
                    and projects.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseUpdateSecurityCenterService._get_http_options()
            request, metadata = self._interceptor.pre_update_security_center_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseUpdateSecurityCenterService,
                    "_BaseUpdateSecurityCenterService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.UpdateSecurityCenterService",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "UpdateSecurityCenterService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._UpdateSecurityCenterService._get_response(
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
            resp = security_center_management.SecurityCenterService()
            pb_resp = security_center_management.SecurityCenterService.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_security_center_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_security_center_service_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        security_center_management.SecurityCenterService.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.update_security_center_service",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "UpdateSecurityCenterService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSecurityHealthAnalyticsCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseUpdateSecurityHealthAnalyticsCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.UpdateSecurityHealthAnalyticsCustomModule"
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
            request: security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
            r"""Call the update security health
            analytics custom module method over HTTP.

                Args:
                    request (~.security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.SecurityHealthAnalyticsCustomModule:
                        Represents an instance of a Security
                    Health Analytics custom module,
                    including its full module name, display
                    name, enablement state, and last updated
                    time. You can create a custom module at
                    the organization, folder, or project
                    level. Custom modules that you create at
                    the organization or folder level are
                    inherited by the descendant folders and
                    projects.

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseUpdateSecurityHealthAnalyticsCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_security_health_analytics_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseUpdateSecurityHealthAnalyticsCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.UpdateSecurityHealthAnalyticsCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "UpdateSecurityHealthAnalyticsCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._UpdateSecurityHealthAnalyticsCustomModule._get_response(
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
            resp = security_center_management.SecurityHealthAnalyticsCustomModule()
            pb_resp = security_center_management.SecurityHealthAnalyticsCustomModule.pb(
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
                    response_payload = security_center_management.SecurityHealthAnalyticsCustomModule.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.update_security_health_analytics_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "UpdateSecurityHealthAnalyticsCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ValidateEventThreatDetectionCustomModule(
        _BaseSecurityCenterManagementRestTransport._BaseValidateEventThreatDetectionCustomModule,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "SecurityCenterManagementRestTransport.ValidateEventThreatDetectionCustomModule"
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
            request: security_center_management.ValidateEventThreatDetectionCustomModuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> (
            security_center_management.ValidateEventThreatDetectionCustomModuleResponse
        ):
            r"""Call the validate event threat
            detection custom module method over HTTP.

                Args:
                    request (~.security_center_management.ValidateEventThreatDetectionCustomModuleRequest):
                        The request object. Request message for
                    [SecurityCenterManagement.ValidateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.security_center_management.ValidateEventThreatDetectionCustomModuleResponse:
                        Response message for
                    [SecurityCenterManagement.ValidateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule].

            """

            http_options = _BaseSecurityCenterManagementRestTransport._BaseValidateEventThreatDetectionCustomModule._get_http_options()
            request, metadata = (
                self._interceptor.pre_validate_event_threat_detection_custom_module(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseValidateEventThreatDetectionCustomModule,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ValidateEventThreatDetectionCustomModule",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ValidateEventThreatDetectionCustomModule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._ValidateEventThreatDetectionCustomModule._get_response(
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
            resp = security_center_management.ValidateEventThreatDetectionCustomModuleResponse()
            pb_resp = security_center_management.ValidateEventThreatDetectionCustomModuleResponse.pb(
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
                    response_payload = security_center_management.ValidateEventThreatDetectionCustomModuleResponse.to_json(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.validate_event_threat_detection_custom_module",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ValidateEventThreatDetectionCustomModule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.CreateEventThreatDetectionCustomModuleRequest],
        security_center_management.EventThreatDetectionCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest],
        security_center_management.SecurityHealthAnalyticsCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.DeleteEventThreatDetectionCustomModuleRequest],
        empty_pb2.Empty,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest],
        empty_pb2.Empty,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_effective_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [
            security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest
        ],
        security_center_management.EffectiveEventThreatDetectionCustomModule,
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
        [
            security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest
        ],
        security_center_management.EffectiveSecurityHealthAnalyticsCustomModule,
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
        [security_center_management.GetEventThreatDetectionCustomModuleRequest],
        security_center_management.EventThreatDetectionCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_security_center_service(
        self,
    ) -> Callable[
        [security_center_management.GetSecurityCenterServiceRequest],
        security_center_management.SecurityCenterService,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSecurityCenterService(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest],
        security_center_management.SecurityHealthAnalyticsCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_descendant_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest
        ],
        security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
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
            security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest
        ],
        security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
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
        [
            security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest
        ],
        security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
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
            security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest
        ],
        security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
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
        [security_center_management.ListEventThreatDetectionCustomModulesRequest],
        security_center_management.ListEventThreatDetectionCustomModulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEventThreatDetectionCustomModules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_security_center_services(
        self,
    ) -> Callable[
        [security_center_management.ListSecurityCenterServicesRequest],
        security_center_management.ListSecurityCenterServicesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSecurityCenterServices(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest],
        security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSecurityHealthAnalyticsCustomModules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def simulate_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest],
        security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SimulateSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.UpdateEventThreatDetectionCustomModuleRequest],
        security_center_management.EventThreatDetectionCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_security_center_service(
        self,
    ) -> Callable[
        [security_center_management.UpdateSecurityCenterServiceRequest],
        security_center_management.SecurityCenterService,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSecurityCenterService(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest],
        security_center_management.SecurityHealthAnalyticsCustomModule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSecurityHealthAnalyticsCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def validate_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.ValidateEventThreatDetectionCustomModuleRequest],
        security_center_management.ValidateEventThreatDetectionCustomModuleResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateEventThreatDetectionCustomModule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseSecurityCenterManagementRestTransport._BaseGetLocation,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterManagementRestTransport.GetLocation")

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

            http_options = _BaseSecurityCenterManagementRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SecurityCenterManagementRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
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
        _BaseSecurityCenterManagementRestTransport._BaseListLocations,
        SecurityCenterManagementRestStub,
    ):
        def __hash__(self):
            return hash("SecurityCenterManagementRestTransport.ListLocations")

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

            http_options = _BaseSecurityCenterManagementRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSecurityCenterManagementRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SecurityCenterManagementRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.securitycentermanagement_v1.SecurityCenterManagementAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "rpcName": "ListLocations",
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


__all__ = ("SecurityCenterManagementRestTransport",)
