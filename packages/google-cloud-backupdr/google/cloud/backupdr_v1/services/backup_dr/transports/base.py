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

from google.cloud.backupdr_v1 import gapic_version as package_version
from google.cloud.backupdr_v1.types import (
    backupdr,
    backupplan,
    backupplanassociation,
    backupvault,
    datasourcereference,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class BackupDRTransport(abc.ABC):
    """Abstract transport class for BackupDR."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "backupdr.googleapis.com"

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
                 The hostname to connect to (default: 'backupdr.googleapis.com').
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
            self.list_management_servers: gapic_v1.method.wrap_method(
                self.list_management_servers,
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
            self.get_management_server: gapic_v1.method.wrap_method(
                self.get_management_server,
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
            self.create_management_server: gapic_v1.method.wrap_method(
                self.create_management_server,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_management_server: gapic_v1.method.wrap_method(
                self.delete_management_server,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_backup_vault: gapic_v1.method.wrap_method(
                self.create_backup_vault,
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
            self.fetch_usable_backup_vaults: gapic_v1.method.wrap_method(
                self.fetch_usable_backup_vaults,
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
            self.update_backup_vault: gapic_v1.method.wrap_method(
                self.update_backup_vault,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup_vault: gapic_v1.method.wrap_method(
                self.delete_backup_vault,
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
            self.list_data_sources: gapic_v1.method.wrap_method(
                self.list_data_sources,
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
            self.get_data_source: gapic_v1.method.wrap_method(
                self.get_data_source,
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
            self.update_data_source: gapic_v1.method.wrap_method(
                self.update_data_source,
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
            self.fetch_backups_for_resource_type: gapic_v1.method.wrap_method(
                self.fetch_backups_for_resource_type,
                default_timeout=None,
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
            self.update_backup: gapic_v1.method.wrap_method(
                self.update_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup: gapic_v1.method.wrap_method(
                self.delete_backup,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_backup: gapic_v1.method.wrap_method(
                self.restore_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_backup_plan: gapic_v1.method.wrap_method(
                self.create_backup_plan,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_backup_plan: gapic_v1.method.wrap_method(
                self.update_backup_plan,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_backup_plan: gapic_v1.method.wrap_method(
                self.get_backup_plan,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_backup_plans: gapic_v1.method.wrap_method(
                self.list_backup_plans,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_backup_plan: gapic_v1.method.wrap_method(
                self.delete_backup_plan,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_backup_plan_revision: gapic_v1.method.wrap_method(
                self.get_backup_plan_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_backup_plan_revisions: gapic_v1.method.wrap_method(
                self.list_backup_plan_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_backup_plan_association: gapic_v1.method.wrap_method(
                self.create_backup_plan_association,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_backup_plan_association: gapic_v1.method.wrap_method(
                self.update_backup_plan_association,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_backup_plan_association: gapic_v1.method.wrap_method(
                self.get_backup_plan_association,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_backup_plan_associations: gapic_v1.method.wrap_method(
                self.list_backup_plan_associations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_backup_plan_associations_for_resource_type: gapic_v1.method.wrap_method(
                self.fetch_backup_plan_associations_for_resource_type,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_backup_plan_association: gapic_v1.method.wrap_method(
                self.delete_backup_plan_association,
                default_timeout=None,
                client_info=client_info,
            ),
            self.trigger_backup: gapic_v1.method.wrap_method(
                self.trigger_backup,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_data_source_reference: gapic_v1.method.wrap_method(
                self.get_data_source_reference,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_data_source_references: gapic_v1.method.wrap_method(
                self.list_data_source_references,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_data_source_references_for_resource_type: gapic_v1.method.wrap_method(
                self.fetch_data_source_references_for_resource_type,
                default_timeout=None,
                client_info=client_info,
            ),
            self.initialize_service: gapic_v1.method.wrap_method(
                self.initialize_service,
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
    def list_management_servers(
        self,
    ) -> Callable[
        [backupdr.ListManagementServersRequest],
        Union[
            backupdr.ListManagementServersResponse,
            Awaitable[backupdr.ListManagementServersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_management_server(
        self,
    ) -> Callable[
        [backupdr.GetManagementServerRequest],
        Union[backupdr.ManagementServer, Awaitable[backupdr.ManagementServer]],
    ]:
        raise NotImplementedError()

    @property
    def create_management_server(
        self,
    ) -> Callable[
        [backupdr.CreateManagementServerRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_management_server(
        self,
    ) -> Callable[
        [backupdr.DeleteManagementServerRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_backup_vault(
        self,
    ) -> Callable[
        [backupvault.CreateBackupVaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_vaults(
        self,
    ) -> Callable[
        [backupvault.ListBackupVaultsRequest],
        Union[
            backupvault.ListBackupVaultsResponse,
            Awaitable[backupvault.ListBackupVaultsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_usable_backup_vaults(
        self,
    ) -> Callable[
        [backupvault.FetchUsableBackupVaultsRequest],
        Union[
            backupvault.FetchUsableBackupVaultsResponse,
            Awaitable[backupvault.FetchUsableBackupVaultsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_vault(
        self,
    ) -> Callable[
        [backupvault.GetBackupVaultRequest],
        Union[backupvault.BackupVault, Awaitable[backupvault.BackupVault]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_vault(
        self,
    ) -> Callable[
        [backupvault.UpdateBackupVaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_vault(
        self,
    ) -> Callable[
        [backupvault.DeleteBackupVaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_data_sources(
        self,
    ) -> Callable[
        [backupvault.ListDataSourcesRequest],
        Union[
            backupvault.ListDataSourcesResponse,
            Awaitable[backupvault.ListDataSourcesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_data_source(
        self,
    ) -> Callable[
        [backupvault.GetDataSourceRequest],
        Union[backupvault.DataSource, Awaitable[backupvault.DataSource]],
    ]:
        raise NotImplementedError()

    @property
    def update_data_source(
        self,
    ) -> Callable[
        [backupvault.UpdateDataSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backups(
        self,
    ) -> Callable[
        [backupvault.ListBackupsRequest],
        Union[
            backupvault.ListBackupsResponse, Awaitable[backupvault.ListBackupsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_backups_for_resource_type(
        self,
    ) -> Callable[
        [backupvault.FetchBackupsForResourceTypeRequest],
        Union[
            backupvault.FetchBackupsForResourceTypeResponse,
            Awaitable[backupvault.FetchBackupsForResourceTypeResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup(
        self,
    ) -> Callable[
        [backupvault.GetBackupRequest],
        Union[backupvault.Backup, Awaitable[backupvault.Backup]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup(
        self,
    ) -> Callable[
        [backupvault.UpdateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [backupvault.DeleteBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restore_backup(
        self,
    ) -> Callable[
        [backupvault.RestoreBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_backup_plan(
        self,
    ) -> Callable[
        [backupplan.CreateBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_plan(
        self,
    ) -> Callable[
        [backupplan.UpdateBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_plan(
        self,
    ) -> Callable[
        [backupplan.GetBackupPlanRequest],
        Union[backupplan.BackupPlan, Awaitable[backupplan.BackupPlan]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_plans(
        self,
    ) -> Callable[
        [backupplan.ListBackupPlansRequest],
        Union[
            backupplan.ListBackupPlansResponse,
            Awaitable[backupplan.ListBackupPlansResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_plan(
        self,
    ) -> Callable[
        [backupplan.DeleteBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_plan_revision(
        self,
    ) -> Callable[
        [backupplan.GetBackupPlanRevisionRequest],
        Union[backupplan.BackupPlanRevision, Awaitable[backupplan.BackupPlanRevision]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_plan_revisions(
        self,
    ) -> Callable[
        [backupplan.ListBackupPlanRevisionsRequest],
        Union[
            backupplan.ListBackupPlanRevisionsResponse,
            Awaitable[backupplan.ListBackupPlanRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_backup_plan_association(
        self,
    ) -> Callable[
        [backupplanassociation.CreateBackupPlanAssociationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_plan_association(
        self,
    ) -> Callable[
        [backupplanassociation.UpdateBackupPlanAssociationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_plan_association(
        self,
    ) -> Callable[
        [backupplanassociation.GetBackupPlanAssociationRequest],
        Union[
            backupplanassociation.BackupPlanAssociation,
            Awaitable[backupplanassociation.BackupPlanAssociation],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_plan_associations(
        self,
    ) -> Callable[
        [backupplanassociation.ListBackupPlanAssociationsRequest],
        Union[
            backupplanassociation.ListBackupPlanAssociationsResponse,
            Awaitable[backupplanassociation.ListBackupPlanAssociationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_backup_plan_associations_for_resource_type(
        self,
    ) -> Callable[
        [backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest],
        Union[
            backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
            Awaitable[
                backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_plan_association(
        self,
    ) -> Callable[
        [backupplanassociation.DeleteBackupPlanAssociationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def trigger_backup(
        self,
    ) -> Callable[
        [backupplanassociation.TriggerBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_data_source_reference(
        self,
    ) -> Callable[
        [datasourcereference.GetDataSourceReferenceRequest],
        Union[
            datasourcereference.DataSourceReference,
            Awaitable[datasourcereference.DataSourceReference],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_data_source_references(
        self,
    ) -> Callable[
        [datasourcereference.ListDataSourceReferencesRequest],
        Union[
            datasourcereference.ListDataSourceReferencesResponse,
            Awaitable[datasourcereference.ListDataSourceReferencesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_data_source_references_for_resource_type(
        self,
    ) -> Callable[
        [datasourcereference.FetchDataSourceReferencesForResourceTypeRequest],
        Union[
            datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
            Awaitable[
                datasourcereference.FetchDataSourceReferencesForResourceTypeResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def initialize_service(
        self,
    ) -> Callable[
        [backupdr.InitializeServiceRequest],
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


__all__ = ("BackupDRTransport",)
