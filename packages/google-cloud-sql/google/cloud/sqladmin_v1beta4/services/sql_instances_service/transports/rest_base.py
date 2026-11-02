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

from google.api_core import gapic_v1, path_template
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format

from google.cloud.sqladmin_v1beta4.types import cloud_sql, cloud_sql_resources

from .base import DEFAULT_CLIENT_INFO, SqlInstancesServiceTransport


class _BaseSqlInstancesServiceRestTransport(SqlInstancesServiceTransport):
    """Base REST backend transport for SqlInstancesService.

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
        host: str = "sqladmin.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'sqladmin.googleapis.com').
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

    class _BaseAcquireSsrsLease:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/acquireSsrsLease",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseAddEntraIdCertificate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/addEntraIdCertificate",
                },
            ]
            return http_options

    class _BaseAddServerCa:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/addServerCa",
                },
            ]
            return http_options

    class _BaseAddServerCertificate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/addServerCertificate",
                },
            ]
            return http_options

    class _BaseClone:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/clone",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseCreateEphemeral:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/createEphemeral",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseDelete:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}",
                },
            ]
            return http_options

    class _BaseDemote:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/demote",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseDemoteMaster:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/demoteMaster",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseExecuteSql:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/executeSql",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseExport:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/export",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseFailover:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/failover",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseGet:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}",
                },
            ]
            return http_options

    class _BaseGetDiskShrinkConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/getDiskShrinkConfig",
                },
            ]
            return http_options

    class _BaseGetLatestRecoveryTime:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/getLatestRecoveryTime",
                },
            ]
            return http_options

    class _BaseImport:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/import",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseInsert:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseList:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/sql/v1beta4/projects/{project}/instances",
                },
            ]
            return http_options

    class _BaseListEntraIdCertificates:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/listEntraIdCertificates",
                },
            ]
            return http_options

    class _BaseListServerCas:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/listServerCas",
                },
            ]
            return http_options

    class _BaseListServerCertificates:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/listServerCertificates",
                },
            ]
            return http_options

    class _BasePatch:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}",
                    "body": "body",
                },
            ]
            return http_options

    class _BasePerformDiskShrink:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/performDiskShrink",
                    "body": "body",
                },
            ]
            return http_options

    class _BasePointInTimeRestore:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/{parent=projects/*}:pointInTimeRestore",
                    "body": "context",
                },
            ]
            return http_options

    class _BasePreCheckMajorVersionUpgrade:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/preCheckMajorVersionUpgrade",
                    "body": "body",
                },
            ]
            return http_options

    class _BasePromoteReplica:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/promoteReplica",
                },
            ]
            return http_options

    class _BaseReencrypt:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/reencrypt",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseReleaseSsrsLease:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/releaseSsrsLease",
                },
            ]
            return http_options

    class _BaseRescheduleMaintenance:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/rescheduleMaintenance",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseResetReplicaSize:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/resetReplicaSize",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseResetSslConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/resetSslConfig",
                },
            ]
            return http_options

    class _BaseRestart:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/restart",
                },
            ]
            return http_options

    class _BaseRestoreBackup:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/restoreBackup",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseRotateEntraIdCertificate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/rotateEntraIdCertificate",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseRotateServerCa:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/rotateServerCa",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseRotateServerCertificate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/rotateServerCertificate",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseStartExternalSync:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/startExternalSync",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseStartReplica:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/startReplica",
                },
            ]
            return http_options

    class _BaseStopReplica:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/stopReplica",
                },
            ]
            return http_options

    class _BaseSwitchover:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/switchover",
                },
            ]
            return http_options

    class _BaseTruncateLog:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/truncateLog",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseUpdate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "put",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}",
                    "body": "body",
                },
            ]
            return http_options

    class _BaseVerifyExternalSyncSettings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/sql/v1beta4/projects/{project}/instances/{instance}/verifyExternalSyncSettings",
                    "body": "*",
                },
            ]
            return http_options


__all__ = ("_BaseSqlInstancesServiceRestTransport",)
