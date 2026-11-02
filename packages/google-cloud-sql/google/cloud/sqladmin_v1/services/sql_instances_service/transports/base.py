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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.sqladmin_v1 import gapic_version as package_version
from google.cloud.sqladmin_v1.types import cloud_sql_instances, cloud_sql_resources

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class SqlInstancesServiceTransport(abc.ABC):
    """Abstract transport class for SqlInstancesService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/sqlservice.admin",
    )

    DEFAULT_HOST: str = "sqladmin.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'sqladmin.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.add_server_ca: gapic_v1.method.wrap_method(
                self.add_server_ca,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_server_certificate: gapic_v1.method.wrap_method(
                self.add_server_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_entra_id_certificate: gapic_v1.method.wrap_method(
                self.add_entra_id_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.clone: gapic_v1.method.wrap_method(
                self.clone,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete: gapic_v1.method.wrap_method(
                self.delete,
                default_timeout=None,
                client_info=client_info,
            ),
            self.demote_master: gapic_v1.method.wrap_method(
                self.demote_master,
                default_timeout=None,
                client_info=client_info,
            ),
            self.demote: gapic_v1.method.wrap_method(
                self.demote,
                default_timeout=None,
                client_info=client_info,
            ),
            self.export: gapic_v1.method.wrap_method(
                self.export,
                default_timeout=None,
                client_info=client_info,
            ),
            self.failover: gapic_v1.method.wrap_method(
                self.failover,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reencrypt: gapic_v1.method.wrap_method(
                self.reencrypt,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get: gapic_v1.method.wrap_method(
                self.get,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_: gapic_v1.method.wrap_method(
                self.import_,
                default_timeout=None,
                client_info=client_info,
            ),
            self.insert: gapic_v1.method.wrap_method(
                self.insert,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list: gapic_v1.method.wrap_method(
                self.list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_server_cas: gapic_v1.method.wrap_method(
                self.list_server_cas,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_server_certificates: gapic_v1.method.wrap_method(
                self.list_server_certificates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entra_id_certificates: gapic_v1.method.wrap_method(
                self.list_entra_id_certificates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.patch: gapic_v1.method.wrap_method(
                self.patch,
                default_timeout=None,
                client_info=client_info,
            ),
            self.promote_replica: gapic_v1.method.wrap_method(
                self.promote_replica,
                default_timeout=None,
                client_info=client_info,
            ),
            self.switchover: gapic_v1.method.wrap_method(
                self.switchover,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_ssl_config: gapic_v1.method.wrap_method(
                self.reset_ssl_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restart: gapic_v1.method.wrap_method(
                self.restart,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_backup: gapic_v1.method.wrap_method(
                self.restore_backup,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rotate_server_ca: gapic_v1.method.wrap_method(
                self.rotate_server_ca,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rotate_server_certificate: gapic_v1.method.wrap_method(
                self.rotate_server_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rotate_entra_id_certificate: gapic_v1.method.wrap_method(
                self.rotate_entra_id_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_replica: gapic_v1.method.wrap_method(
                self.start_replica,
                default_timeout=None,
                client_info=client_info,
            ),
            self.stop_replica: gapic_v1.method.wrap_method(
                self.stop_replica,
                default_timeout=None,
                client_info=client_info,
            ),
            self.truncate_log: gapic_v1.method.wrap_method(
                self.truncate_log,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update: gapic_v1.method.wrap_method(
                self.update,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_ephemeral: gapic_v1.method.wrap_method(
                self.create_ephemeral,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reschedule_maintenance: gapic_v1.method.wrap_method(
                self.reschedule_maintenance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.verify_external_sync_settings: gapic_v1.method.wrap_method(
                self.verify_external_sync_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_external_sync: gapic_v1.method.wrap_method(
                self.start_external_sync,
                default_timeout=None,
                client_info=client_info,
            ),
            self.perform_disk_shrink: gapic_v1.method.wrap_method(
                self.perform_disk_shrink,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_disk_shrink_config: gapic_v1.method.wrap_method(
                self.get_disk_shrink_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_replica_size: gapic_v1.method.wrap_method(
                self.reset_replica_size,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_latest_recovery_time: gapic_v1.method.wrap_method(
                self.get_latest_recovery_time,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_sql: gapic_v1.method.wrap_method(
                self.execute_sql,
                default_timeout=None,
                client_info=client_info,
            ),
            self.acquire_ssrs_lease: gapic_v1.method.wrap_method(
                self.acquire_ssrs_lease,
                default_timeout=None,
                client_info=client_info,
            ),
            self.release_ssrs_lease: gapic_v1.method.wrap_method(
                self.release_ssrs_lease,
                default_timeout=None,
                client_info=client_info,
            ),
            self.pre_check_major_version_upgrade: gapic_v1.method.wrap_method(
                self.pre_check_major_version_upgrade,
                default_timeout=None,
                client_info=client_info,
            ),
            self.point_in_time_restore: gapic_v1.method.wrap_method(
                self.point_in_time_restore,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def add_server_ca(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesAddServerCaRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def add_server_certificate(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesAddServerCertificateRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def add_entra_id_certificate(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def clone(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesCloneRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesDeleteRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def demote_master(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesDemoteMasterRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def demote(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesDemoteRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesExportRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def failover(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesFailoverRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reencrypt(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesReencryptRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesGetRequest],
        Union[
            cloud_sql_instances.DatabaseInstance,
            Awaitable[cloud_sql_instances.DatabaseInstance],
        ],
    ]:
        raise NotImplementedError()

    @property
    def import_(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesImportRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def insert(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesInsertRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesListRequest],
        Union[
            cloud_sql_instances.InstancesListResponse,
            Awaitable[cloud_sql_instances.InstancesListResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_server_cas(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesListServerCasRequest],
        Union[
            cloud_sql_instances.InstancesListServerCasResponse,
            Awaitable[cloud_sql_instances.InstancesListServerCasResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_server_certificates(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesListServerCertificatesRequest],
        Union[
            cloud_sql_instances.InstancesListServerCertificatesResponse,
            Awaitable[cloud_sql_instances.InstancesListServerCertificatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_entra_id_certificates(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest],
        Union[
            cloud_sql_instances.InstancesListEntraIdCertificatesResponse,
            Awaitable[cloud_sql_instances.InstancesListEntraIdCertificatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def patch(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesPatchRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def promote_replica(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesPromoteReplicaRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def switchover(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesSwitchoverRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reset_ssl_config(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesResetSslConfigRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restart(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesRestartRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restore_backup(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesRestoreBackupRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def rotate_server_ca(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesRotateServerCaRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def rotate_server_certificate(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesRotateServerCertificateRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def rotate_entra_id_certificate(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_replica(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesStartReplicaRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def stop_replica(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesStopReplicaRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def truncate_log(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesTruncateLogRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesUpdateRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_ephemeral(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest],
        Union[cloud_sql_resources.SslCert, Awaitable[cloud_sql_resources.SslCert]],
    ]:
        raise NotImplementedError()

    @property
    def reschedule_maintenance(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def verify_external_sync_settings(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest],
        Union[
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse,
            Awaitable[
                cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def start_external_sync(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesStartExternalSyncRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def perform_disk_shrink(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_disk_shrink_config(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest],
        Union[
            cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse,
            Awaitable[cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def reset_replica_size(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesResetReplicaSizeRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_latest_recovery_time(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest],
        Union[
            cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse,
            Awaitable[cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def execute_sql(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesExecuteSqlRequest],
        Union[
            cloud_sql_instances.SqlInstancesExecuteSqlResponse,
            Awaitable[cloud_sql_instances.SqlInstancesExecuteSqlResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def acquire_ssrs_lease(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest],
        Union[
            cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse,
            Awaitable[cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def release_ssrs_lease(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest],
        Union[
            cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse,
            Awaitable[cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def pre_check_major_version_upgrade(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def point_in_time_restore(
        self,
    ) -> Callable[
        [cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest],
        Union[cloud_sql_resources.Operation, Awaitable[cloud_sql_resources.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("SqlInstancesServiceTransport",)
