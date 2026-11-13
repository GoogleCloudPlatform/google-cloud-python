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
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.netapp_v1 import gapic_version as package_version
from google.cloud.netapp_v1.types import (
    active_directory,
    backup,
    backup_policy,
    backup_vault,
    host_group,
    kms,
    ontap,
    quota_rule,
    replication,
    snapshot,
    storage_pool,
    volume,
)
from google.cloud.netapp_v1.types import active_directory as gcn_active_directory
from google.cloud.netapp_v1.types import backup as gcn_backup
from google.cloud.netapp_v1.types import backup_policy as gcn_backup_policy
from google.cloud.netapp_v1.types import backup_vault as gcn_backup_vault
from google.cloud.netapp_v1.types import host_group as gcn_host_group
from google.cloud.netapp_v1.types import quota_rule as gcn_quota_rule
from google.cloud.netapp_v1.types import replication as gcn_replication
from google.cloud.netapp_v1.types import snapshot as gcn_snapshot
from google.cloud.netapp_v1.types import storage_pool as gcn_storage_pool
from google.cloud.netapp_v1.types import volume as gcn_volume

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class NetAppTransport(abc.ABC):
    """Abstract transport class for NetApp."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "netapp.googleapis.com"

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
                 The hostname to connect to (default: 'netapp.googleapis.com').
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
            self.list_storage_pools: gapic_v1.method.wrap_method(
                self.list_storage_pools,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_storage_pool: gapic_v1.method.wrap_method(
                self.create_storage_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_storage_pool: gapic_v1.method.wrap_method(
                self.get_storage_pool,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_storage_pool: gapic_v1.method.wrap_method(
                self.update_storage_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_storage_pool: gapic_v1.method.wrap_method(
                self.delete_storage_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.validate_directory_service: gapic_v1.method.wrap_method(
                self.validate_directory_service,
                default_timeout=None,
                client_info=client_info,
            ),
            self.switch_active_replica_zone: gapic_v1.method.wrap_method(
                self.switch_active_replica_zone,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_volumes: gapic_v1.method.wrap_method(
                self.list_volumes,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_volume: gapic_v1.method.wrap_method(
                self.get_volume,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_volume: gapic_v1.method.wrap_method(
                self.create_volume,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_volume: gapic_v1.method.wrap_method(
                self.update_volume,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_volume: gapic_v1.method.wrap_method(
                self.delete_volume,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.revert_volume: gapic_v1.method.wrap_method(
                self.revert_volume,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.start_split: gapic_v1.method.wrap_method(
                self.start_split,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_split_status: gapic_v1.method.wrap_method(
                self.get_split_status,
                default_timeout=None,
                client_info=client_info,
            ),
            self.establish_volume_peering: gapic_v1.method.wrap_method(
                self.establish_volume_peering,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_snapshots: gapic_v1.method.wrap_method(
                self.list_snapshots,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_snapshot: gapic_v1.method.wrap_method(
                self.get_snapshot,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_snapshot: gapic_v1.method.wrap_method(
                self.create_snapshot,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_snapshot: gapic_v1.method.wrap_method(
                self.delete_snapshot,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_snapshot: gapic_v1.method.wrap_method(
                self.update_snapshot,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_active_directories: gapic_v1.method.wrap_method(
                self.list_active_directories,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_active_directory: gapic_v1.method.wrap_method(
                self.get_active_directory,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_active_directory: gapic_v1.method.wrap_method(
                self.create_active_directory,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_active_directory: gapic_v1.method.wrap_method(
                self.update_active_directory,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_active_directory: gapic_v1.method.wrap_method(
                self.delete_active_directory,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_kms_configs: gapic_v1.method.wrap_method(
                self.list_kms_configs,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_kms_config: gapic_v1.method.wrap_method(
                self.create_kms_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_kms_config: gapic_v1.method.wrap_method(
                self.get_kms_config,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_kms_config: gapic_v1.method.wrap_method(
                self.update_kms_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.encrypt_volumes: gapic_v1.method.wrap_method(
                self.encrypt_volumes,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.verify_kms_config: gapic_v1.method.wrap_method(
                self.verify_kms_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_kms_config: gapic_v1.method.wrap_method(
                self.delete_kms_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_replications: gapic_v1.method.wrap_method(
                self.list_replications,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_replication: gapic_v1.method.wrap_method(
                self.get_replication,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_replication: gapic_v1.method.wrap_method(
                self.create_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_replication: gapic_v1.method.wrap_method(
                self.delete_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_replication: gapic_v1.method.wrap_method(
                self.update_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.stop_replication: gapic_v1.method.wrap_method(
                self.stop_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.resume_replication: gapic_v1.method.wrap_method(
                self.resume_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.reverse_replication_direction: gapic_v1.method.wrap_method(
                self.reverse_replication_direction,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.establish_peering: gapic_v1.method.wrap_method(
                self.establish_peering,
                default_timeout=None,
                client_info=client_info,
            ),
            self.sync_replication: gapic_v1.method.wrap_method(
                self.sync_replication,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_backup_vault: gapic_v1.method.wrap_method(
                self.create_backup_vault,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup_vault: gapic_v1.method.wrap_method(
                self.get_backup_vault,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_backup_vaults: gapic_v1.method.wrap_method(
                self.list_backup_vaults,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_backup_vault: gapic_v1.method.wrap_method(
                self.update_backup_vault,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup_vault: gapic_v1.method.wrap_method(
                self.delete_backup_vault,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_backup: gapic_v1.method.wrap_method(
                self.create_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup: gapic_v1.method.wrap_method(
                self.get_backup,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_backups: gapic_v1.method.wrap_method(
                self.list_backups,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup: gapic_v1.method.wrap_method(
                self.delete_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_backup: gapic_v1.method.wrap_method(
                self.update_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_backup_policy: gapic_v1.method.wrap_method(
                self.create_backup_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup_policy: gapic_v1.method.wrap_method(
                self.get_backup_policy,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_backup_policies: gapic_v1.method.wrap_method(
                self.list_backup_policies,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_backup_policy: gapic_v1.method.wrap_method(
                self.update_backup_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup_policy: gapic_v1.method.wrap_method(
                self.delete_backup_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_quota_rules: gapic_v1.method.wrap_method(
                self.list_quota_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_quota_rule: gapic_v1.method.wrap_method(
                self.get_quota_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_quota_rule: gapic_v1.method.wrap_method(
                self.create_quota_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_quota_rule: gapic_v1.method.wrap_method(
                self.update_quota_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_quota_rule: gapic_v1.method.wrap_method(
                self.delete_quota_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_backup_files: gapic_v1.method.wrap_method(
                self.restore_backup_files,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_host_groups: gapic_v1.method.wrap_method(
                self.list_host_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_host_group: gapic_v1.method.wrap_method(
                self.get_host_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_host_group: gapic_v1.method.wrap_method(
                self.create_host_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_host_group: gapic_v1.method.wrap_method(
                self.update_host_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_host_group: gapic_v1.method.wrap_method(
                self.delete_host_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_ontap_post: gapic_v1.method.wrap_method(
                self.execute_ontap_post,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_ontap_get: gapic_v1.method.wrap_method(
                self.execute_ontap_get,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_ontap_delete: gapic_v1.method.wrap_method(
                self.execute_ontap_delete,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_ontap_patch: gapic_v1.method.wrap_method(
                self.execute_ontap_patch,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_volume: gapic_v1.method.wrap_method(
                self.restore_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_backup_configs: gapic_v1.method.wrap_method(
                self.list_backup_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_backup_config: gapic_v1.method.wrap_method(
                self.update_backup_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
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
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_storage_pools(
        self,
    ) -> Callable[
        [storage_pool.ListStoragePoolsRequest],
        Union[
            storage_pool.ListStoragePoolsResponse,
            Awaitable[storage_pool.ListStoragePoolsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_storage_pool(
        self,
    ) -> Callable[
        [gcn_storage_pool.CreateStoragePoolRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_storage_pool(
        self,
    ) -> Callable[
        [storage_pool.GetStoragePoolRequest],
        Union[storage_pool.StoragePool, Awaitable[storage_pool.StoragePool]],
    ]:
        raise NotImplementedError()

    @property
    def update_storage_pool(
        self,
    ) -> Callable[
        [gcn_storage_pool.UpdateStoragePoolRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_storage_pool(
        self,
    ) -> Callable[
        [storage_pool.DeleteStoragePoolRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def validate_directory_service(
        self,
    ) -> Callable[
        [storage_pool.ValidateDirectoryServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def switch_active_replica_zone(
        self,
    ) -> Callable[
        [storage_pool.SwitchActiveReplicaZoneRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_volumes(
        self,
    ) -> Callable[
        [volume.ListVolumesRequest],
        Union[volume.ListVolumesResponse, Awaitable[volume.ListVolumesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_volume(
        self,
    ) -> Callable[
        [volume.GetVolumeRequest], Union[volume.Volume, Awaitable[volume.Volume]]
    ]:
        raise NotImplementedError()

    @property
    def create_volume(
        self,
    ) -> Callable[
        [gcn_volume.CreateVolumeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_volume(
        self,
    ) -> Callable[
        [gcn_volume.UpdateVolumeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_volume(
        self,
    ) -> Callable[
        [volume.DeleteVolumeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def revert_volume(
        self,
    ) -> Callable[
        [volume.RevertVolumeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_split(
        self,
    ) -> Callable[
        [volume.StartSplitRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_split_status(
        self,
    ) -> Callable[
        [volume.GetSplitStatusRequest],
        Union[volume.SplitStatus, Awaitable[volume.SplitStatus]],
    ]:
        raise NotImplementedError()

    @property
    def establish_volume_peering(
        self,
    ) -> Callable[
        [volume.EstablishVolumePeeringRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_snapshots(
        self,
    ) -> Callable[
        [snapshot.ListSnapshotsRequest],
        Union[
            snapshot.ListSnapshotsResponse, Awaitable[snapshot.ListSnapshotsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_snapshot(
        self,
    ) -> Callable[
        [snapshot.GetSnapshotRequest],
        Union[snapshot.Snapshot, Awaitable[snapshot.Snapshot]],
    ]:
        raise NotImplementedError()

    @property
    def create_snapshot(
        self,
    ) -> Callable[
        [gcn_snapshot.CreateSnapshotRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_snapshot(
        self,
    ) -> Callable[
        [snapshot.DeleteSnapshotRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_snapshot(
        self,
    ) -> Callable[
        [gcn_snapshot.UpdateSnapshotRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_active_directories(
        self,
    ) -> Callable[
        [active_directory.ListActiveDirectoriesRequest],
        Union[
            active_directory.ListActiveDirectoriesResponse,
            Awaitable[active_directory.ListActiveDirectoriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_active_directory(
        self,
    ) -> Callable[
        [active_directory.GetActiveDirectoryRequest],
        Union[
            active_directory.ActiveDirectory,
            Awaitable[active_directory.ActiveDirectory],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_active_directory(
        self,
    ) -> Callable[
        [gcn_active_directory.CreateActiveDirectoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_active_directory(
        self,
    ) -> Callable[
        [gcn_active_directory.UpdateActiveDirectoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_active_directory(
        self,
    ) -> Callable[
        [active_directory.DeleteActiveDirectoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_kms_configs(
        self,
    ) -> Callable[
        [kms.ListKmsConfigsRequest],
        Union[kms.ListKmsConfigsResponse, Awaitable[kms.ListKmsConfigsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def create_kms_config(
        self,
    ) -> Callable[
        [kms.CreateKmsConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_kms_config(
        self,
    ) -> Callable[
        [kms.GetKmsConfigRequest], Union[kms.KmsConfig, Awaitable[kms.KmsConfig]]
    ]:
        raise NotImplementedError()

    @property
    def update_kms_config(
        self,
    ) -> Callable[
        [kms.UpdateKmsConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def encrypt_volumes(
        self,
    ) -> Callable[
        [kms.EncryptVolumesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def verify_kms_config(
        self,
    ) -> Callable[
        [kms.VerifyKmsConfigRequest],
        Union[kms.VerifyKmsConfigResponse, Awaitable[kms.VerifyKmsConfigResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_kms_config(
        self,
    ) -> Callable[
        [kms.DeleteKmsConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_replications(
        self,
    ) -> Callable[
        [replication.ListReplicationsRequest],
        Union[
            replication.ListReplicationsResponse,
            Awaitable[replication.ListReplicationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_replication(
        self,
    ) -> Callable[
        [replication.GetReplicationRequest],
        Union[replication.Replication, Awaitable[replication.Replication]],
    ]:
        raise NotImplementedError()

    @property
    def create_replication(
        self,
    ) -> Callable[
        [gcn_replication.CreateReplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_replication(
        self,
    ) -> Callable[
        [replication.DeleteReplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_replication(
        self,
    ) -> Callable[
        [gcn_replication.UpdateReplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def stop_replication(
        self,
    ) -> Callable[
        [replication.StopReplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def resume_replication(
        self,
    ) -> Callable[
        [replication.ResumeReplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reverse_replication_direction(
        self,
    ) -> Callable[
        [replication.ReverseReplicationDirectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def establish_peering(
        self,
    ) -> Callable[
        [replication.EstablishPeeringRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def sync_replication(
        self,
    ) -> Callable[
        [replication.SyncReplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_backup_vault(
        self,
    ) -> Callable[
        [gcn_backup_vault.CreateBackupVaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_vault(
        self,
    ) -> Callable[
        [backup_vault.GetBackupVaultRequest],
        Union[backup_vault.BackupVault, Awaitable[backup_vault.BackupVault]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_vaults(
        self,
    ) -> Callable[
        [backup_vault.ListBackupVaultsRequest],
        Union[
            backup_vault.ListBackupVaultsResponse,
            Awaitable[backup_vault.ListBackupVaultsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_vault(
        self,
    ) -> Callable[
        [gcn_backup_vault.UpdateBackupVaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_vault(
        self,
    ) -> Callable[
        [backup_vault.DeleteBackupVaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_backup(
        self,
    ) -> Callable[
        [gcn_backup.CreateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup(
        self,
    ) -> Callable[
        [backup.GetBackupRequest], Union[backup.Backup, Awaitable[backup.Backup]]
    ]:
        raise NotImplementedError()

    @property
    def list_backups(
        self,
    ) -> Callable[
        [backup.ListBackupsRequest],
        Union[backup.ListBackupsResponse, Awaitable[backup.ListBackupsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [backup.DeleteBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup(
        self,
    ) -> Callable[
        [gcn_backup.UpdateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_backup_policy(
        self,
    ) -> Callable[
        [gcn_backup_policy.CreateBackupPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_policy(
        self,
    ) -> Callable[
        [backup_policy.GetBackupPolicyRequest],
        Union[backup_policy.BackupPolicy, Awaitable[backup_policy.BackupPolicy]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_policies(
        self,
    ) -> Callable[
        [backup_policy.ListBackupPoliciesRequest],
        Union[
            backup_policy.ListBackupPoliciesResponse,
            Awaitable[backup_policy.ListBackupPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_policy(
        self,
    ) -> Callable[
        [gcn_backup_policy.UpdateBackupPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_policy(
        self,
    ) -> Callable[
        [backup_policy.DeleteBackupPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_quota_rules(
        self,
    ) -> Callable[
        [quota_rule.ListQuotaRulesRequest],
        Union[
            quota_rule.ListQuotaRulesResponse,
            Awaitable[quota_rule.ListQuotaRulesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_quota_rule(
        self,
    ) -> Callable[
        [quota_rule.GetQuotaRuleRequest],
        Union[quota_rule.QuotaRule, Awaitable[quota_rule.QuotaRule]],
    ]:
        raise NotImplementedError()

    @property
    def create_quota_rule(
        self,
    ) -> Callable[
        [gcn_quota_rule.CreateQuotaRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_quota_rule(
        self,
    ) -> Callable[
        [gcn_quota_rule.UpdateQuotaRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_quota_rule(
        self,
    ) -> Callable[
        [quota_rule.DeleteQuotaRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restore_backup_files(
        self,
    ) -> Callable[
        [volume.RestoreBackupFilesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_host_groups(
        self,
    ) -> Callable[
        [host_group.ListHostGroupsRequest],
        Union[
            host_group.ListHostGroupsResponse,
            Awaitable[host_group.ListHostGroupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_host_group(
        self,
    ) -> Callable[
        [host_group.GetHostGroupRequest],
        Union[host_group.HostGroup, Awaitable[host_group.HostGroup]],
    ]:
        raise NotImplementedError()

    @property
    def create_host_group(
        self,
    ) -> Callable[
        [gcn_host_group.CreateHostGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_host_group(
        self,
    ) -> Callable[
        [gcn_host_group.UpdateHostGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_host_group(
        self,
    ) -> Callable[
        [host_group.DeleteHostGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def execute_ontap_post(
        self,
    ) -> Callable[
        [ontap.ExecuteOntapPostRequest],
        Union[
            ontap.ExecuteOntapPostResponse, Awaitable[ontap.ExecuteOntapPostResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def execute_ontap_get(
        self,
    ) -> Callable[
        [ontap.ExecuteOntapGetRequest],
        Union[ontap.ExecuteOntapGetResponse, Awaitable[ontap.ExecuteOntapGetResponse]],
    ]:
        raise NotImplementedError()

    @property
    def execute_ontap_delete(
        self,
    ) -> Callable[
        [ontap.ExecuteOntapDeleteRequest],
        Union[
            ontap.ExecuteOntapDeleteResponse,
            Awaitable[ontap.ExecuteOntapDeleteResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def execute_ontap_patch(
        self,
    ) -> Callable[
        [ontap.ExecuteOntapPatchRequest],
        Union[
            ontap.ExecuteOntapPatchResponse, Awaitable[ontap.ExecuteOntapPatchResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def restore_volume(
        self,
    ) -> Callable[
        [volume.RestoreVolumeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_configs(
        self,
    ) -> Callable[
        [volume.ListBackupConfigsRequest],
        Union[
            volume.ListBackupConfigsResponse,
            Awaitable[volume.ListBackupConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_config(
        self,
    ) -> Callable[
        [volume.UpdateBackupConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("NetAppTransport",)
