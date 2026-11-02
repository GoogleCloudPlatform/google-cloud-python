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
import json  # type: ignore
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import gapic_v1, path_template
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format

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

from .base import DEFAULT_CLIENT_INFO, SecurityCenterTransport


class _BaseSecurityCenterRestTransport(SecurityCenterTransport):
    """Base REST backend transport for SecurityCenter.

    Note: This class is not meant to be used directly. Use its sync and
    async sub-classes instead.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "securitycenter.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'securitycenter.googleapis.com').
            credentials (Optional[Any]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
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
        """
        # Run the base constructor
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

    class _BaseBatchCreateResourceValueConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/resourceValueConfigs:batchCreate",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseBulkMuteFindings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/findings:bulkMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*}/findings:bulkMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*}/findings:bulkMute",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateBigQueryExport:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "bigQueryExportId": "",
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/bigQueryExports",
                    "body": "big_query_export",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*}/bigQueryExports",
                    "body": "big_query_export",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*}/bigQueryExports",
                    "body": "big_query_export",
                },
            ]
            return http_options

    class _BaseCreateEventThreatDetectionCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/eventThreatDetectionSettings}/customModules",
                    "body": "event_threat_detection_custom_module",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*/eventThreatDetectionSettings}/customModules",
                    "body": "event_threat_detection_custom_module",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/eventThreatDetectionSettings}/customModules",
                    "body": "event_threat_detection_custom_module",
                },
            ]
            return http_options

    class _BaseCreateFinding:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "findingId": "",
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/sources/*}/findings",
                    "body": "finding",
                },
            ]
            return http_options

    class _BaseCreateMuteConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "muteConfigId": "",
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/locations/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*/locations/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*}/muteConfigs",
                    "body": "mute_config",
                },
            ]
            return http_options

    class _BaseCreateNotificationConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "configId": "",
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/notificationConfigs",
                    "body": "notification_config",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*}/notificationConfigs",
                    "body": "notification_config",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*}/notificationConfigs",
                    "body": "notification_config",
                },
            ]
            return http_options

    class _BaseCreateSecurityHealthAnalyticsCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/securityHealthAnalyticsSettings}/customModules",
                    "body": "security_health_analytics_custom_module",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*/securityHealthAnalyticsSettings}/customModules",
                    "body": "security_health_analytics_custom_module",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/securityHealthAnalyticsSettings}/customModules",
                    "body": "security_health_analytics_custom_module",
                },
            ]
            return http_options

    class _BaseCreateSource:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/sources",
                    "body": "source",
                },
            ]
            return http_options

    class _BaseDeleteBigQueryExport:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/bigQueryExports/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/bigQueryExports/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/bigQueryExports/*}",
                },
            ]
            return http_options

    class _BaseDeleteEventThreatDetectionCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/eventThreatDetectionSettings/customModules/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/eventThreatDetectionSettings/customModules/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/eventThreatDetectionSettings/customModules/*}",
                },
            ]
            return http_options

    class _BaseDeleteMuteConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/locations/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/locations/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/muteConfigs/*}",
                },
            ]
            return http_options

    class _BaseDeleteNotificationConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/notificationConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/notificationConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/notificationConfigs/*}",
                },
            ]
            return http_options

    class _BaseDeleteResourceValueConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/resourceValueConfigs/*}",
                },
            ]
            return http_options

    class _BaseDeleteSecurityHealthAnalyticsCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/securityHealthAnalyticsSettings/customModules/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/securityHealthAnalyticsSettings/customModules/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/securityHealthAnalyticsSettings/customModules/*}",
                },
            ]
            return http_options

    class _BaseGetBigQueryExport:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/bigQueryExports/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/bigQueryExports/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/bigQueryExports/*}",
                },
            ]
            return http_options

    class _BaseGetEffectiveEventThreatDetectionCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/eventThreatDetectionSettings/effectiveCustomModules/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/eventThreatDetectionSettings/effectiveCustomModules/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/eventThreatDetectionSettings/effectiveCustomModules/*}",
                },
            ]
            return http_options

    class _BaseGetEffectiveSecurityHealthAnalyticsCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/securityHealthAnalyticsSettings/effectiveCustomModules/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/securityHealthAnalyticsSettings/effectiveCustomModules/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/securityHealthAnalyticsSettings/effectiveCustomModules/*}",
                },
            ]
            return http_options

    class _BaseGetEventThreatDetectionCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/eventThreatDetectionSettings/customModules/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/eventThreatDetectionSettings/customModules/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/eventThreatDetectionSettings/customModules/*}",
                },
            ]
            return http_options

    class _BaseGetIamPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{resource=organizations/*/sources/*}:getIamPolicy",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseGetMuteConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/locations/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/muteConfigs/*}",
                },
            ]
            return http_options

    class _BaseGetNotificationConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/notificationConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/notificationConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/notificationConfigs/*}",
                },
            ]
            return http_options

    class _BaseGetOrganizationSettings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/organizationSettings}",
                },
            ]
            return http_options

    class _BaseGetResourceValueConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/resourceValueConfigs/*}",
                },
            ]
            return http_options

    class _BaseGetSecurityHealthAnalyticsCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/securityHealthAnalyticsSettings/customModules/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/securityHealthAnalyticsSettings/customModules/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/securityHealthAnalyticsSettings/customModules/*}",
                },
            ]
            return http_options

    class _BaseGetSimulation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/simulations/*}",
                },
            ]
            return http_options

    class _BaseGetSource:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/sources/*}",
                },
            ]
            return http_options

    class _BaseGetValuedResource:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/simulations/*/valuedResources/*}",
                },
            ]
            return http_options

    class _BaseGroupAssets:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/assets:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*}/assets:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*}/assets:group",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseGroupFindings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/sources/*}/findings:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*/sources/*}/findings:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/sources/*}/findings:group",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseListAssets:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/assets",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*}/assets",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/assets",
                },
            ]
            return http_options

    class _BaseListAttackPaths:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/simulations/*}/attackPaths",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/simulations/*/valuedResources/*}/attackPaths",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/simulations/*/attackExposureResults/*}/attackPaths",
                },
            ]
            return http_options

    class _BaseListBigQueryExports:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/bigQueryExports",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*}/bigQueryExports",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/bigQueryExports",
                },
            ]
            return http_options

    class _BaseListDescendantEventThreatDetectionCustomModules:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/eventThreatDetectionSettings}/customModules:listDescendant",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/eventThreatDetectionSettings}/customModules:listDescendant",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/eventThreatDetectionSettings}/customModules:listDescendant",
                },
            ]
            return http_options

    class _BaseListDescendantSecurityHealthAnalyticsCustomModules:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/securityHealthAnalyticsSettings}/customModules:listDescendant",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/securityHealthAnalyticsSettings}/customModules:listDescendant",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/securityHealthAnalyticsSettings}/customModules:listDescendant",
                },
            ]
            return http_options

    class _BaseListEffectiveEventThreatDetectionCustomModules:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/eventThreatDetectionSettings}/effectiveCustomModules",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/eventThreatDetectionSettings}/effectiveCustomModules",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/eventThreatDetectionSettings}/effectiveCustomModules",
                },
            ]
            return http_options

    class _BaseListEffectiveSecurityHealthAnalyticsCustomModules:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/securityHealthAnalyticsSettings}/effectiveCustomModules",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/securityHealthAnalyticsSettings}/effectiveCustomModules",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/securityHealthAnalyticsSettings}/effectiveCustomModules",
                },
            ]
            return http_options

    class _BaseListEventThreatDetectionCustomModules:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/eventThreatDetectionSettings}/customModules",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/eventThreatDetectionSettings}/customModules",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/eventThreatDetectionSettings}/customModules",
                },
            ]
            return http_options

    class _BaseListFindings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/sources/*}/findings",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/sources/*}/findings",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/sources/*}/findings",
                },
            ]
            return http_options

    class _BaseListMuteConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/muteConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*}/muteConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/muteConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/locations/*/muteConfigs}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/locations/*/muteConfigs}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/muteConfigs}",
                },
            ]
            return http_options

    class _BaseListNotificationConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/notificationConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*}/notificationConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/notificationConfigs",
                },
            ]
            return http_options

    class _BaseListResourceValueConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/resourceValueConfigs",
                },
            ]
            return http_options

    class _BaseListSecurityHealthAnalyticsCustomModules:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/securityHealthAnalyticsSettings}/customModules",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/securityHealthAnalyticsSettings}/customModules",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/securityHealthAnalyticsSettings}/customModules",
                },
            ]
            return http_options

    class _BaseListSources:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/sources",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*}/sources",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/sources",
                },
            ]
            return http_options

    class _BaseListValuedResources:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/simulations/*}/valuedResources",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/simulations/*/attackExposureResults/*}/valuedResources",
                },
            ]
            return http_options

    class _BaseRunAssetDiscovery:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/assets:runDiscovery",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetFindingState:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/sources/*/findings/*}:setState",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/sources/*/findings/*}:setState",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/sources/*/findings/*}:setState",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetIamPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{resource=organizations/*/sources/*}:setIamPolicy",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetMute:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/sources/*/findings/*}:setMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/sources/*/findings/*}:setMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/sources/*/findings/*}:setMute",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSimulateSecurityHealthAnalyticsCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/securityHealthAnalyticsSettings}/customModules:simulate",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*/securityHealthAnalyticsSettings}/customModules:simulate",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/securityHealthAnalyticsSettings}/customModules:simulate",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseTestIamPermissions:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{resource=organizations/*/sources/*}:testIamPermissions",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateBigQueryExport:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{big_query_export.name=organizations/*/bigQueryExports/*}",
                    "body": "big_query_export",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{big_query_export.name=folders/*/bigQueryExports/*}",
                    "body": "big_query_export",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{big_query_export.name=projects/*/bigQueryExports/*}",
                    "body": "big_query_export",
                },
            ]
            return http_options

    class _BaseUpdateEventThreatDetectionCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{event_threat_detection_custom_module.name=organizations/*/eventThreatDetectionSettings/customModules/*}",
                    "body": "event_threat_detection_custom_module",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{event_threat_detection_custom_module.name=folders/*/eventThreatDetectionSettings/customModules/*}",
                    "body": "event_threat_detection_custom_module",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{event_threat_detection_custom_module.name=projects/*/eventThreatDetectionSettings/customModules/*}",
                    "body": "event_threat_detection_custom_module",
                },
            ]
            return http_options

    class _BaseUpdateExternalSystem:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{external_system.name=organizations/*/sources/*/findings/*/externalSystems/*}",
                    "body": "external_system",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{external_system.name=folders/*/sources/*/findings/*/externalSystems/*}",
                    "body": "external_system",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{external_system.name=projects/*/sources/*/findings/*/externalSystems/*}",
                    "body": "external_system",
                },
            ]
            return http_options

    class _BaseUpdateFinding:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{finding.name=organizations/*/sources/*/findings/*}",
                    "body": "finding",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{finding.name=folders/*/sources/*/findings/*}",
                    "body": "finding",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{finding.name=projects/*/sources/*/findings/*}",
                    "body": "finding",
                },
            ]
            return http_options

    class _BaseUpdateMuteConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{mute_config.name=organizations/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{mute_config.name=folders/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{mute_config.name=projects/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{mute_config.name=organizations/*/locations/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{mute_config.name=folders/*/locations/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{mute_config.name=projects/*/locations/*/muteConfigs/*}",
                    "body": "mute_config",
                },
            ]
            return http_options

    class _BaseUpdateNotificationConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{notification_config.name=organizations/*/notificationConfigs/*}",
                    "body": "notification_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{notification_config.name=folders/*/notificationConfigs/*}",
                    "body": "notification_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{notification_config.name=projects/*/notificationConfigs/*}",
                    "body": "notification_config",
                },
            ]
            return http_options

    class _BaseUpdateOrganizationSettings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{organization_settings.name=organizations/*/organizationSettings}",
                    "body": "organization_settings",
                },
            ]
            return http_options

    class _BaseUpdateResourceValueConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{resource_value_config.name=organizations/*/resourceValueConfigs/*}",
                    "body": "resource_value_config",
                },
            ]
            return http_options

    class _BaseUpdateSecurityHealthAnalyticsCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{security_health_analytics_custom_module.name=organizations/*/securityHealthAnalyticsSettings/customModules/*}",
                    "body": "security_health_analytics_custom_module",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{security_health_analytics_custom_module.name=folders/*/securityHealthAnalyticsSettings/customModules/*}",
                    "body": "security_health_analytics_custom_module",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{security_health_analytics_custom_module.name=projects/*/securityHealthAnalyticsSettings/customModules/*}",
                    "body": "security_health_analytics_custom_module",
                },
            ]
            return http_options

    class _BaseUpdateSecurityMarks:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{security_marks.name=organizations/*/assets/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{security_marks.name=folders/*/assets/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{security_marks.name=projects/*/assets/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{security_marks.name=organizations/*/sources/*/findings/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{security_marks.name=folders/*/sources/*/findings/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{security_marks.name=projects/*/sources/*/findings/*/securityMarks}",
                    "body": "security_marks",
                },
            ]
            return http_options

    class _BaseUpdateSource:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{source.name=organizations/*/sources/*}",
                    "body": "source",
                },
            ]
            return http_options

    class _BaseValidateEventThreatDetectionCustomModule:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/eventThreatDetectionSettings}:validateCustomModule",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*/eventThreatDetectionSettings}:validateCustomModule",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/eventThreatDetectionSettings}:validateCustomModule",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCancelOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/operations/*}:cancel",
                },
            ]
            return http_options

    class _BaseDeleteOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/operations/*}",
                },
            ]
            return http_options

    class _BaseGetOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/operations/*}",
                },
            ]
            return http_options

    class _BaseListOperations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/operations}",
                },
            ]
            return http_options


__all__ = ("_BaseSecurityCenterRestTransport",)
