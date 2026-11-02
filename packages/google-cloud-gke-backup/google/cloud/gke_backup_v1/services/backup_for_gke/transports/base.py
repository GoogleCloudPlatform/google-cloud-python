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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.gke_backup_v1 import gapic_version as package_version
from google.cloud.gke_backup_v1.types import (
    backup,
    backup_channel,
    backup_plan,
    backup_plan_binding,
    gkebackup,
    restore,
    restore_channel,
    restore_plan,
    restore_plan_binding,
    volume,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class BackupForGKETransport(abc.ABC):
    """Abstract transport class for BackupForGKE."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "gkebackup.googleapis.com"

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
                 The hostname to connect to (default: 'gkebackup.googleapis.com').
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
            self.create_backup_plan: gapic_v1.method.wrap_method(
                self.create_backup_plan,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_backup_plans: gapic_v1.method.wrap_method(
                self.list_backup_plans,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup_plan: gapic_v1.method.wrap_method(
                self.get_backup_plan,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_backup_plan: gapic_v1.method.wrap_method(
                self.update_backup_plan,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup_plan: gapic_v1.method.wrap_method(
                self.delete_backup_plan,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_backup_channel: gapic_v1.method.wrap_method(
                self.create_backup_channel,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_backup_channels: gapic_v1.method.wrap_method(
                self.list_backup_channels,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup_channel: gapic_v1.method.wrap_method(
                self.get_backup_channel,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_backup_channel: gapic_v1.method.wrap_method(
                self.update_backup_channel,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup_channel: gapic_v1.method.wrap_method(
                self.delete_backup_channel,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_backup_plan_bindings: gapic_v1.method.wrap_method(
                self.list_backup_plan_bindings,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup_plan_binding: gapic_v1.method.wrap_method(
                self.get_backup_plan_binding,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_backup: gapic_v1.method.wrap_method(
                self.create_backup,
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.list_backups: gapic_v1.method.wrap_method(
                self.list_backups,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup: gapic_v1.method.wrap_method(
                self.get_backup,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_backup: gapic_v1.method.wrap_method(
                self.update_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup: gapic_v1.method.wrap_method(
                self.delete_backup,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_volume_backups: gapic_v1.method.wrap_method(
                self.list_volume_backups,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_volume_backup: gapic_v1.method.wrap_method(
                self.get_volume_backup,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_restore_plan: gapic_v1.method.wrap_method(
                self.create_restore_plan,
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.list_restore_plans: gapic_v1.method.wrap_method(
                self.list_restore_plans,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_restore_plan: gapic_v1.method.wrap_method(
                self.get_restore_plan,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_restore_plan: gapic_v1.method.wrap_method(
                self.update_restore_plan,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_restore_plan: gapic_v1.method.wrap_method(
                self.delete_restore_plan,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_restore_channel: gapic_v1.method.wrap_method(
                self.create_restore_channel,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_restore_channels: gapic_v1.method.wrap_method(
                self.list_restore_channels,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_restore_channel: gapic_v1.method.wrap_method(
                self.get_restore_channel,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_restore_channel: gapic_v1.method.wrap_method(
                self.update_restore_channel,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_restore_channel: gapic_v1.method.wrap_method(
                self.delete_restore_channel,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_restore_plan_bindings: gapic_v1.method.wrap_method(
                self.list_restore_plan_bindings,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_restore_plan_binding: gapic_v1.method.wrap_method(
                self.get_restore_plan_binding,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_restore: gapic_v1.method.wrap_method(
                self.create_restore,
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.list_restores: gapic_v1.method.wrap_method(
                self.list_restores,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_restore: gapic_v1.method.wrap_method(
                self.get_restore,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_restore: gapic_v1.method.wrap_method(
                self.update_restore,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_restore: gapic_v1.method.wrap_method(
                self.delete_restore,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_volume_restores: gapic_v1.method.wrap_method(
                self.list_volume_restores,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_volume_restore: gapic_v1.method.wrap_method(
                self.get_volume_restore,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup_index_download_url: gapic_v1.method.wrap_method(
                self.get_backup_index_download_url,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
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
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
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
    def create_backup_plan(
        self,
    ) -> Callable[
        [gkebackup.CreateBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_plans(
        self,
    ) -> Callable[
        [gkebackup.ListBackupPlansRequest],
        Union[
            gkebackup.ListBackupPlansResponse,
            Awaitable[gkebackup.ListBackupPlansResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_plan(
        self,
    ) -> Callable[
        [gkebackup.GetBackupPlanRequest],
        Union[backup_plan.BackupPlan, Awaitable[backup_plan.BackupPlan]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_plan(
        self,
    ) -> Callable[
        [gkebackup.UpdateBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_plan(
        self,
    ) -> Callable[
        [gkebackup.DeleteBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_backup_channel(
        self,
    ) -> Callable[
        [gkebackup.CreateBackupChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_channels(
        self,
    ) -> Callable[
        [gkebackup.ListBackupChannelsRequest],
        Union[
            gkebackup.ListBackupChannelsResponse,
            Awaitable[gkebackup.ListBackupChannelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_channel(
        self,
    ) -> Callable[
        [gkebackup.GetBackupChannelRequest],
        Union[backup_channel.BackupChannel, Awaitable[backup_channel.BackupChannel]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_channel(
        self,
    ) -> Callable[
        [gkebackup.UpdateBackupChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_channel(
        self,
    ) -> Callable[
        [gkebackup.DeleteBackupChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_plan_bindings(
        self,
    ) -> Callable[
        [gkebackup.ListBackupPlanBindingsRequest],
        Union[
            gkebackup.ListBackupPlanBindingsResponse,
            Awaitable[gkebackup.ListBackupPlanBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_plan_binding(
        self,
    ) -> Callable[
        [gkebackup.GetBackupPlanBindingRequest],
        Union[
            backup_plan_binding.BackupPlanBinding,
            Awaitable[backup_plan_binding.BackupPlanBinding],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_backup(
        self,
    ) -> Callable[
        [gkebackup.CreateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backups(
        self,
    ) -> Callable[
        [gkebackup.ListBackupsRequest],
        Union[gkebackup.ListBackupsResponse, Awaitable[gkebackup.ListBackupsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup(
        self,
    ) -> Callable[
        [gkebackup.GetBackupRequest], Union[backup.Backup, Awaitable[backup.Backup]]
    ]:
        raise NotImplementedError()

    @property
    def update_backup(
        self,
    ) -> Callable[
        [gkebackup.UpdateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [gkebackup.DeleteBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_volume_backups(
        self,
    ) -> Callable[
        [gkebackup.ListVolumeBackupsRequest],
        Union[
            gkebackup.ListVolumeBackupsResponse,
            Awaitable[gkebackup.ListVolumeBackupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_volume_backup(
        self,
    ) -> Callable[
        [gkebackup.GetVolumeBackupRequest],
        Union[volume.VolumeBackup, Awaitable[volume.VolumeBackup]],
    ]:
        raise NotImplementedError()

    @property
    def create_restore_plan(
        self,
    ) -> Callable[
        [gkebackup.CreateRestorePlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_restore_plans(
        self,
    ) -> Callable[
        [gkebackup.ListRestorePlansRequest],
        Union[
            gkebackup.ListRestorePlansResponse,
            Awaitable[gkebackup.ListRestorePlansResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_restore_plan(
        self,
    ) -> Callable[
        [gkebackup.GetRestorePlanRequest],
        Union[restore_plan.RestorePlan, Awaitable[restore_plan.RestorePlan]],
    ]:
        raise NotImplementedError()

    @property
    def update_restore_plan(
        self,
    ) -> Callable[
        [gkebackup.UpdateRestorePlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_restore_plan(
        self,
    ) -> Callable[
        [gkebackup.DeleteRestorePlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_restore_channel(
        self,
    ) -> Callable[
        [gkebackup.CreateRestoreChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_restore_channels(
        self,
    ) -> Callable[
        [gkebackup.ListRestoreChannelsRequest],
        Union[
            gkebackup.ListRestoreChannelsResponse,
            Awaitable[gkebackup.ListRestoreChannelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_restore_channel(
        self,
    ) -> Callable[
        [gkebackup.GetRestoreChannelRequest],
        Union[
            restore_channel.RestoreChannel, Awaitable[restore_channel.RestoreChannel]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_restore_channel(
        self,
    ) -> Callable[
        [gkebackup.UpdateRestoreChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_restore_channel(
        self,
    ) -> Callable[
        [gkebackup.DeleteRestoreChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_restore_plan_bindings(
        self,
    ) -> Callable[
        [gkebackup.ListRestorePlanBindingsRequest],
        Union[
            gkebackup.ListRestorePlanBindingsResponse,
            Awaitable[gkebackup.ListRestorePlanBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_restore_plan_binding(
        self,
    ) -> Callable[
        [gkebackup.GetRestorePlanBindingRequest],
        Union[
            restore_plan_binding.RestorePlanBinding,
            Awaitable[restore_plan_binding.RestorePlanBinding],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_restore(
        self,
    ) -> Callable[
        [gkebackup.CreateRestoreRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_restores(
        self,
    ) -> Callable[
        [gkebackup.ListRestoresRequest],
        Union[
            gkebackup.ListRestoresResponse, Awaitable[gkebackup.ListRestoresResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_restore(
        self,
    ) -> Callable[
        [gkebackup.GetRestoreRequest],
        Union[restore.Restore, Awaitable[restore.Restore]],
    ]:
        raise NotImplementedError()

    @property
    def update_restore(
        self,
    ) -> Callable[
        [gkebackup.UpdateRestoreRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_restore(
        self,
    ) -> Callable[
        [gkebackup.DeleteRestoreRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_volume_restores(
        self,
    ) -> Callable[
        [gkebackup.ListVolumeRestoresRequest],
        Union[
            gkebackup.ListVolumeRestoresResponse,
            Awaitable[gkebackup.ListVolumeRestoresResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_volume_restore(
        self,
    ) -> Callable[
        [gkebackup.GetVolumeRestoreRequest],
        Union[volume.VolumeRestore, Awaitable[volume.VolumeRestore]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_index_download_url(
        self,
    ) -> Callable[
        [gkebackup.GetBackupIndexDownloadUrlRequest],
        Union[
            gkebackup.GetBackupIndexDownloadUrlResponse,
            Awaitable[gkebackup.GetBackupIndexDownloadUrlResponse],
        ],
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
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
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


__all__ = ("BackupForGKETransport",)
