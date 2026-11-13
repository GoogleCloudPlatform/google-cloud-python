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

from google.cloud.securitycenter_v2.types import (
    bigquery_export,
    finding,
    mute_config,
    notification_config,
    resource_value_config,
    securitycenter_service,
    simulation,
    source,
    valued_resource,
)
from google.cloud.securitycenter_v2.types import external_system as gcs_external_system
from google.cloud.securitycenter_v2.types import finding as gcs_finding
from google.cloud.securitycenter_v2.types import mute_config as gcs_mute_config
from google.cloud.securitycenter_v2.types import (
    notification_config as gcs_notification_config,
)
from google.cloud.securitycenter_v2.types import (
    resource_value_config as gcs_resource_value_config,
)
from google.cloud.securitycenter_v2.types import security_marks as gcs_security_marks
from google.cloud.securitycenter_v2.types import source as gcs_source

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
                    "uri": "/v2/{parent=organizations/*}/resourceValueConfigs:batchCreate",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/locations/*}/resourceValueConfigs:batchCreate",
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
                    "uri": "/v2/{parent=organizations/*}/findings:bulkMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/locations/*}/findings:bulkMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*}/findings:bulkMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*/locations/*}/findings:bulkMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/findings:bulkMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/findings:bulkMute",
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
                    "uri": "/v2/{parent=organizations/*/locations/*}/bigQueryExports",
                    "body": "big_query_export",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*/locations/*}/bigQueryExports",
                    "body": "big_query_export",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/bigQueryExports",
                    "body": "big_query_export",
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
                    "uri": "/v2/{parent=organizations/*/sources/*/locations/*}/findings",
                    "body": "finding",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/sources/*}/findings",
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
                    "uri": "/v2/{parent=organizations/*/locations/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*/locations/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*}/muteConfigs",
                    "body": "mute_config",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/muteConfigs",
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
                    "uri": "/v2/{parent=organizations/*/locations/*}/notificationConfigs",
                    "body": "notification_config",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*/locations/*}/notificationConfigs",
                    "body": "notification_config",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/notificationConfigs",
                    "body": "notification_config",
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
                    "uri": "/v2/{parent=organizations/*}/sources",
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
                    "uri": "/v2/{name=organizations/*/locations/*/bigQueryExports/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=folders/*/locations/*/bigQueryExports/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/bigQueryExports/*}",
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
                    "uri": "/v2/{name=organizations/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=folders/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=folders/*/locations/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/muteConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/muteConfigs/*}",
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
                    "uri": "/v2/{name=organizations/*/locations/*/notificationConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=folders/*/locations/*/notificationConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/notificationConfigs/*}",
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
                    "uri": "/v2/{name=organizations/*/resourceValueConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/resourceValueConfigs/*}",
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
                    "uri": "/v2/{name=organizations/*/locations/*/bigQueryExports/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=folders/*/locations/*/bigQueryExports/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/bigQueryExports/*}",
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
                    "uri": "/v2/{resource=organizations/*/sources/*}:getIamPolicy",
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
                    "uri": "/v2/{name=organizations/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=folders/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=folders/*/locations/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/muteConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/muteConfigs/*}",
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
                    "uri": "/v2/{name=organizations/*/locations/*/notificationConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=folders/*/locations/*/notificationConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/notificationConfigs/*}",
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
                    "uri": "/v2/{name=organizations/*/resourceValueConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/resourceValueConfigs/*}",
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
                    "uri": "/v2/{name=organizations/*/simulations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/simulations/*}",
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
                    "uri": "/v2/{name=organizations/*/sources/*}",
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
                    "uri": "/v2/{name=organizations/*/simulations/*/valuedResources/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/simulations/*/valuedResources/*}",
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
                    "uri": "/v2/{parent=organizations/*/sources/*}/findings:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/sources/*/locations/*}/findings:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*/sources/*}/findings:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*/sources/*/locations/*}/findings:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/sources/*}/findings:group",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/sources/*/locations/*}/findings:group",
                    "body": "*",
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
                    "uri": "/v2/{parent=organizations/*/simulations/*}/attackPaths",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*}/attackPaths",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/simulations/*/valuedResources/*}/attackPaths",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*/simulations/*/valuedResources/*}/attackPaths",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/simulations/*/attackExposureResults/*}/attackPaths",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*/simulations/*/attackExposureResults/*}/attackPaths",
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
                    "uri": "/v2/{parent=organizations/*/locations/*}/bigQueryExports",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*/locations/*}/bigQueryExports",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/bigQueryExports",
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
                    "uri": "/v2/{parent=organizations/*/sources/*}/findings",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/sources/*/locations/*}/findings",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*/sources/*}/findings",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*/sources/*/locations/*}/findings",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/sources/*}/findings",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/sources/*/locations/*}/findings",
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
                    "uri": "/v2/{parent=organizations/*}/muteConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/muteConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*}/muteConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*/locations/*}/muteConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/muteConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/muteConfigs",
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
                    "uri": "/v2/{parent=organizations/*/locations/*}/notificationConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*/locations/*}/notificationConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/notificationConfigs",
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
                    "uri": "/v2/{parent=organizations/*}/resourceValueConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/resourceValueConfigs",
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
                    "uri": "/v2/{parent=organizations/*}/sources",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*}/sources",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/sources",
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
                    "uri": "/v2/{parent=organizations/*/simulations/*}/valuedResources",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/simulations/*/attackExposureResults/*}/valuedResources",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*}/valuedResources",
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
                    "uri": "/v2/{name=organizations/*/sources/*/findings/*}:setState",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=organizations/*/sources/*/locations/*/findings/*}:setState",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=folders/*/sources/*/findings/*}:setState",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=folders/*/sources/*/locations/*/findings/*}:setState",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/sources/*/findings/*}:setState",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/sources/*/locations/*/findings/*}:setState",
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
                    "uri": "/v2/{resource=organizations/*/sources/*}:setIamPolicy",
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
                    "uri": "/v2/{name=organizations/*/sources/*/findings/*}:setMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=organizations/*/sources/*/locations/*/findings/*}:setMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=folders/*/sources/*/findings/*}:setMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=folders/*/sources/*/locations/*/findings/*}:setMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/sources/*/findings/*}:setMute",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/sources/*/locations/*/findings/*}:setMute",
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
                    "uri": "/v2/{resource=organizations/*/sources/*}:testIamPermissions",
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
                    "uri": "/v2/{big_query_export.name=organizations/*/locations/*/bigQueryExports/*}",
                    "body": "big_query_export",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{big_query_export.name=folders/*/locations/*/bigQueryExports/*}",
                    "body": "big_query_export",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{big_query_export.name=projects/*/locations/*/bigQueryExports/*}",
                    "body": "big_query_export",
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
                    "uri": "/v2/{external_system.name=organizations/*/sources/*/findings/*/externalSystems/*}",
                    "body": "external_system",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{external_system.name=organizations/*/sources/*/locations/*/findings/*/externalSystems/*}",
                    "body": "external_system",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{external_system.name=folders/*/sources/*/findings/*/externalSystems/*}",
                    "body": "external_system",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{external_system.name=folders/*/sources/*/locations/*/findings/*/externalSystems/*}",
                    "body": "external_system",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{external_system.name=projects/*/sources/*/findings/*/externalSystems/*}",
                    "body": "external_system",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{external_system.name=projects/*/sources/*/locations/*/findings/*/externalSystems/*}",
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
                    "uri": "/v2/{finding.name=organizations/*/sources/*/findings/*}",
                    "body": "finding",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{finding.name=organizations/*/sources/*/locations/*/findings/*}",
                    "body": "finding",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{finding.name=folders/*/sources/*/findings/*}",
                    "body": "finding",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{finding.name=folders/*/sources/*/locations/*/findings/*}",
                    "body": "finding",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{finding.name=projects/*/sources/*/findings/*}",
                    "body": "finding",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{finding.name=projects/*/sources/*/locations/*/findings/*}",
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
                    "uri": "/v2/{mute_config.name=organizations/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{mute_config.name=organizations/*/locations/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{mute_config.name=folders/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{mute_config.name=folders/*/locations/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{mute_config.name=projects/*/muteConfigs/*}",
                    "body": "mute_config",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{mute_config.name=projects/*/locations/*/muteConfigs/*}",
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
                    "uri": "/v2/{notification_config.name=organizations/*/locations/*/notificationConfigs/*}",
                    "body": "notification_config",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{notification_config.name=folders/*/locations/*/notificationConfigs/*}",
                    "body": "notification_config",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{notification_config.name=projects/*/locations/*/notificationConfigs/*}",
                    "body": "notification_config",
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
                    "uri": "/v2/{resource_value_config.name=organizations/*/resourceValueConfigs/*}",
                    "body": "resource_value_config",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{resource_value_config.name=organizations/*/locations/*/resourceValueConfigs/*}",
                    "body": "resource_value_config",
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
                    "uri": "/v2/{security_marks.name=organizations/*/sources/*/findings/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{security_marks.name=organizations/*/assets/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{security_marks.name=organizations/*/sources/*/locations/*/findings/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{security_marks.name=folders/*/sources/*/findings/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{security_marks.name=folders/*/assets/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{security_marks.name=folders/*/sources/*/locations/*/findings/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{security_marks.name=projects/*/sources/*/findings/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{security_marks.name=projects/*/assets/*/securityMarks}",
                    "body": "security_marks",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{security_marks.name=projects/*/sources/*/locations/*/findings/*/securityMarks}",
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
                    "uri": "/v2/{source.name=organizations/*/sources/*}",
                    "body": "source",
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
                    "uri": "/v2/{name=organizations/*/operations/*}:cancel",
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
                    "uri": "/v2/{name=organizations/*/operations/*}",
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
                    "uri": "/v2/{name=organizations/*/operations/*}",
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
                    "uri": "/v2/{name=organizations/*/operations}",
                },
            ]
            return http_options


__all__ = ("_BaseSecurityCenterRestTransport",)
