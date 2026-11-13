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

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import gapic_v1, path_template
from google.cloud.location import locations_pb2  # type: ignore
from google.protobuf import json_format

from google.cloud.dlp_v2.types import dlp

from .base import DEFAULT_CLIENT_INFO, DlpServiceTransport


class _BaseDlpServiceRestTransport(DlpServiceTransport):
    """Base REST backend transport for DlpService.

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
        host: str = "dlp.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dlp.googleapis.com').
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

    class _BaseActivateJobTrigger:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/jobTriggers/*}:activate",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/locations/*/jobTriggers/*}:activate",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCancelDlpJob:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/dlpJobs/*}:cancel",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/locations/*/dlpJobs/*}:cancel",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateConnection:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/connections",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/locations/*}/connections",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateContentPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/contentPolicies",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateDeidentifyTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*}/deidentifyTemplates",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/locations/*}/deidentifyTemplates",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/deidentifyTemplates",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/deidentifyTemplates",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateDiscoveryConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/discoveryConfigs",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/locations/*}/discoveryConfigs",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateDlpJob:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/dlpJobs",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/dlpJobs",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateInspectTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/inspectTemplates",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/locations/*}/inspectTemplates",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/inspectTemplates",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*}/inspectTemplates",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateJobTrigger:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/jobTriggers",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/jobTriggers",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/locations/*}/jobTriggers",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateStoredInfoType:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*}/storedInfoTypes",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*/locations/*}/storedInfoTypes",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/storedInfoTypes",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/storedInfoTypes",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseDeidentifyContent:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/content:deidentify",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/content:deidentify",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseDeleteConnection:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/connections/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/connections/*}",
                },
            ]
            return http_options

    class _BaseDeleteContentPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/contentPolicies/*}",
                },
            ]
            return http_options

    class _BaseDeleteDeidentifyTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/deidentifyTemplates/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/deidentifyTemplates/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/deidentifyTemplates/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/deidentifyTemplates/*}",
                },
            ]
            return http_options

    class _BaseDeleteDiscoveryConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/discoveryConfigs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/discoveryConfigs/*}",
                },
            ]
            return http_options

    class _BaseDeleteDlpJob:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/dlpJobs/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/dlpJobs/*}",
                },
            ]
            return http_options

    class _BaseDeleteFileStoreDataProfile:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/fileStoreDataProfiles/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/fileStoreDataProfiles/*}",
                },
            ]
            return http_options

    class _BaseDeleteInspectTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/inspectTemplates/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/inspectTemplates/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/inspectTemplates/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/inspectTemplates/*}",
                },
            ]
            return http_options

    class _BaseDeleteJobTrigger:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/jobTriggers/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/jobTriggers/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/jobTriggers/*}",
                },
            ]
            return http_options

    class _BaseDeleteStoredInfoType:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/storedInfoTypes/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/storedInfoTypes/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/storedInfoTypes/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/storedInfoTypes/*}",
                },
            ]
            return http_options

    class _BaseDeleteTableDataProfile:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/locations/*/tableDataProfiles/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/locations/*/tableDataProfiles/*}",
                },
            ]
            return http_options

    class _BaseFinishDlpJob:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/locations/*/dlpJobs/*}:finish",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseGetColumnDataProfile:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/columnDataProfiles/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/columnDataProfiles/*}",
                },
            ]
            return http_options

    class _BaseGetConnection:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/connections/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/connections/*}",
                },
            ]
            return http_options

    class _BaseGetContentPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/contentPolicies/*}",
                },
            ]
            return http_options

    class _BaseGetDeidentifyTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/deidentifyTemplates/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/deidentifyTemplates/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/deidentifyTemplates/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/deidentifyTemplates/*}",
                },
            ]
            return http_options

    class _BaseGetDiscoveryConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/discoveryConfigs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/discoveryConfigs/*}",
                },
            ]
            return http_options

    class _BaseGetDlpJob:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/dlpJobs/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/dlpJobs/*}",
                },
            ]
            return http_options

    class _BaseGetFileStoreDataProfile:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/fileStoreDataProfiles/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/fileStoreDataProfiles/*}",
                },
            ]
            return http_options

    class _BaseGetInspectTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/inspectTemplates/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/inspectTemplates/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/inspectTemplates/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/inspectTemplates/*}",
                },
            ]
            return http_options

    class _BaseGetJobTrigger:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/jobTriggers/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/jobTriggers/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/jobTriggers/*}",
                },
            ]
            return http_options

    class _BaseGetProjectDataProfile:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/projectDataProfiles/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/projectDataProfiles/*}",
                },
            ]
            return http_options

    class _BaseGetStoredInfoType:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/storedInfoTypes/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/storedInfoTypes/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/storedInfoTypes/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/storedInfoTypes/*}",
                },
            ]
            return http_options

    class _BaseGetTableDataProfile:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/locations/*/tableDataProfiles/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/locations/*/tableDataProfiles/*}",
                },
            ]
            return http_options

    class _BaseHybridInspectDlpJob:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/locations/*/dlpJobs/*}:hybridInspect",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseHybridInspectJobTrigger:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{name=projects/*/locations/*/jobTriggers/*}:hybridInspect",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseInspectContent:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/content:inspect",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/content:inspect",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseListColumnDataProfiles:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/columnDataProfiles",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/columnDataProfiles",
                },
            ]
            return http_options

    class _BaseListConnections:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/connections",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/connections",
                },
            ]
            return http_options

    class _BaseListContentPolicies:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/contentPolicies",
                },
            ]
            return http_options

    class _BaseListDeidentifyTemplates:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*}/deidentifyTemplates",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/deidentifyTemplates",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/deidentifyTemplates",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/deidentifyTemplates",
                },
            ]
            return http_options

    class _BaseListDiscoveryConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/discoveryConfigs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/discoveryConfigs",
                },
            ]
            return http_options

    class _BaseListDlpJobs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/dlpJobs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/dlpJobs",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/dlpJobs",
                },
            ]
            return http_options

    class _BaseListFileStoreDataProfiles:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/fileStoreDataProfiles",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/fileStoreDataProfiles",
                },
            ]
            return http_options

    class _BaseListInfoTypes:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/infoTypes",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=locations/*}/infoTypes",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/infoTypes",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/infoTypes",
                },
            ]
            return http_options

    class _BaseListInspectTemplates:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/inspectTemplates",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/inspectTemplates",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/inspectTemplates",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*}/inspectTemplates",
                },
            ]
            return http_options

    class _BaseListJobTriggers:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/jobTriggers",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/jobTriggers",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/jobTriggers",
                },
            ]
            return http_options

    class _BaseListProjectDataProfiles:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/projectDataProfiles",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/projectDataProfiles",
                },
            ]
            return http_options

    class _BaseListStoredInfoTypes:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*}/storedInfoTypes",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/storedInfoTypes",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/storedInfoTypes",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/storedInfoTypes",
                },
            ]
            return http_options

    class _BaseListTableDataProfiles:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/tableDataProfiles",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/tableDataProfiles",
                },
            ]
            return http_options

    class _BaseRedactImage:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/image:redact",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/image:redact",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseReidentifyContent:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/content:reidentify",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*/locations/*}/content:reidentify",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSearchConnections:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*/locations/*}/connections:search",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*/locations/*}/connections:search",
                },
            ]
            return http_options

    class _BaseUpdateConnection:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/locations/*/connections/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/locations/*/connections/*}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateContentPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/locations/*/contentPolicies/*}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateDeidentifyTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/deidentifyTemplates/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/locations/*/deidentifyTemplates/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/deidentifyTemplates/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/locations/*/deidentifyTemplates/*}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateDiscoveryConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/locations/*/discoveryConfigs/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/locations/*/discoveryConfigs/*}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateInspectTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/locations/*/inspectTemplates/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/locations/*/inspectTemplates/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/inspectTemplates/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/inspectTemplates/*}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateJobTrigger:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/jobTriggers/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/locations/*/jobTriggers/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/locations/*/jobTriggers/*}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateStoredInfoType:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/storedInfoTypes/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=organizations/*/locations/*/storedInfoTypes/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/storedInfoTypes/*}",
                    "body": "*",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{name=projects/*/locations/*/storedInfoTypes/*}",
                    "body": "*",
                },
            ]
            return http_options


__all__ = ("_BaseDlpServiceRestTransport",)
