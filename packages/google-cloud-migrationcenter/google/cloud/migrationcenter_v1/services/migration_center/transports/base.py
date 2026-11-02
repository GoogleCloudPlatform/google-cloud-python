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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.migrationcenter_v1 import gapic_version as package_version
from google.cloud.migrationcenter_v1.types import migrationcenter

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class MigrationCenterTransport(abc.ABC):
    """Abstract transport class for MigrationCenter."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "migrationcenter.googleapis.com"

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
                 The hostname to connect to (default: 'migrationcenter.googleapis.com').
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
            self.list_assets: gapic_v1.method.wrap_method(
                self.list_assets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_asset: gapic_v1.method.wrap_method(
                self.get_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_asset: gapic_v1.method.wrap_method(
                self.update_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_update_assets: gapic_v1.method.wrap_method(
                self.batch_update_assets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_asset: gapic_v1.method.wrap_method(
                self.delete_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_delete_assets: gapic_v1.method.wrap_method(
                self.batch_delete_assets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.report_asset_frames: gapic_v1.method.wrap_method(
                self.report_asset_frames,
                default_timeout=None,
                client_info=client_info,
            ),
            self.aggregate_assets_values: gapic_v1.method.wrap_method(
                self.aggregate_assets_values,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_import_job: gapic_v1.method.wrap_method(
                self.create_import_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_import_jobs: gapic_v1.method.wrap_method(
                self.list_import_jobs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_import_job: gapic_v1.method.wrap_method(
                self.get_import_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_import_job: gapic_v1.method.wrap_method(
                self.delete_import_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_import_job: gapic_v1.method.wrap_method(
                self.update_import_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.validate_import_job: gapic_v1.method.wrap_method(
                self.validate_import_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.run_import_job: gapic_v1.method.wrap_method(
                self.run_import_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_import_data_file: gapic_v1.method.wrap_method(
                self.get_import_data_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_import_data_files: gapic_v1.method.wrap_method(
                self.list_import_data_files,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_import_data_file: gapic_v1.method.wrap_method(
                self.create_import_data_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_import_data_file: gapic_v1.method.wrap_method(
                self.delete_import_data_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_groups: gapic_v1.method.wrap_method(
                self.list_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_group: gapic_v1.method.wrap_method(
                self.get_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_group: gapic_v1.method.wrap_method(
                self.create_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_group: gapic_v1.method.wrap_method(
                self.update_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_group: gapic_v1.method.wrap_method(
                self.delete_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_assets_to_group: gapic_v1.method.wrap_method(
                self.add_assets_to_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_assets_from_group: gapic_v1.method.wrap_method(
                self.remove_assets_from_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_error_frames: gapic_v1.method.wrap_method(
                self.list_error_frames,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_error_frame: gapic_v1.method.wrap_method(
                self.get_error_frame,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_sources: gapic_v1.method.wrap_method(
                self.list_sources,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_source: gapic_v1.method.wrap_method(
                self.get_source,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_source: gapic_v1.method.wrap_method(
                self.create_source,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_source: gapic_v1.method.wrap_method(
                self.update_source,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_source: gapic_v1.method.wrap_method(
                self.delete_source,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_preference_sets: gapic_v1.method.wrap_method(
                self.list_preference_sets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_preference_set: gapic_v1.method.wrap_method(
                self.get_preference_set,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_preference_set: gapic_v1.method.wrap_method(
                self.create_preference_set,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_preference_set: gapic_v1.method.wrap_method(
                self.update_preference_set,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_preference_set: gapic_v1.method.wrap_method(
                self.delete_preference_set,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_settings: gapic_v1.method.wrap_method(
                self.get_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_settings: gapic_v1.method.wrap_method(
                self.update_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_report_config: gapic_v1.method.wrap_method(
                self.create_report_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_report_config: gapic_v1.method.wrap_method(
                self.get_report_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_report_configs: gapic_v1.method.wrap_method(
                self.list_report_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_report_config: gapic_v1.method.wrap_method(
                self.delete_report_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_report: gapic_v1.method.wrap_method(
                self.create_report,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_report: gapic_v1.method.wrap_method(
                self.get_report,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_reports: gapic_v1.method.wrap_method(
                self.list_reports,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_report: gapic_v1.method.wrap_method(
                self.delete_report,
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
    def list_assets(
        self,
    ) -> Callable[
        [migrationcenter.ListAssetsRequest],
        Union[
            migrationcenter.ListAssetsResponse,
            Awaitable[migrationcenter.ListAssetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_asset(
        self,
    ) -> Callable[
        [migrationcenter.GetAssetRequest],
        Union[migrationcenter.Asset, Awaitable[migrationcenter.Asset]],
    ]:
        raise NotImplementedError()

    @property
    def update_asset(
        self,
    ) -> Callable[
        [migrationcenter.UpdateAssetRequest],
        Union[migrationcenter.Asset, Awaitable[migrationcenter.Asset]],
    ]:
        raise NotImplementedError()

    @property
    def batch_update_assets(
        self,
    ) -> Callable[
        [migrationcenter.BatchUpdateAssetsRequest],
        Union[
            migrationcenter.BatchUpdateAssetsResponse,
            Awaitable[migrationcenter.BatchUpdateAssetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_asset(
        self,
    ) -> Callable[
        [migrationcenter.DeleteAssetRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def batch_delete_assets(
        self,
    ) -> Callable[
        [migrationcenter.BatchDeleteAssetsRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def report_asset_frames(
        self,
    ) -> Callable[
        [migrationcenter.ReportAssetFramesRequest],
        Union[
            migrationcenter.ReportAssetFramesResponse,
            Awaitable[migrationcenter.ReportAssetFramesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def aggregate_assets_values(
        self,
    ) -> Callable[
        [migrationcenter.AggregateAssetsValuesRequest],
        Union[
            migrationcenter.AggregateAssetsValuesResponse,
            Awaitable[migrationcenter.AggregateAssetsValuesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_import_job(
        self,
    ) -> Callable[
        [migrationcenter.CreateImportJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_import_jobs(
        self,
    ) -> Callable[
        [migrationcenter.ListImportJobsRequest],
        Union[
            migrationcenter.ListImportJobsResponse,
            Awaitable[migrationcenter.ListImportJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_import_job(
        self,
    ) -> Callable[
        [migrationcenter.GetImportJobRequest],
        Union[migrationcenter.ImportJob, Awaitable[migrationcenter.ImportJob]],
    ]:
        raise NotImplementedError()

    @property
    def delete_import_job(
        self,
    ) -> Callable[
        [migrationcenter.DeleteImportJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_import_job(
        self,
    ) -> Callable[
        [migrationcenter.UpdateImportJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def validate_import_job(
        self,
    ) -> Callable[
        [migrationcenter.ValidateImportJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def run_import_job(
        self,
    ) -> Callable[
        [migrationcenter.RunImportJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_import_data_file(
        self,
    ) -> Callable[
        [migrationcenter.GetImportDataFileRequest],
        Union[
            migrationcenter.ImportDataFile, Awaitable[migrationcenter.ImportDataFile]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_import_data_files(
        self,
    ) -> Callable[
        [migrationcenter.ListImportDataFilesRequest],
        Union[
            migrationcenter.ListImportDataFilesResponse,
            Awaitable[migrationcenter.ListImportDataFilesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_import_data_file(
        self,
    ) -> Callable[
        [migrationcenter.CreateImportDataFileRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_import_data_file(
        self,
    ) -> Callable[
        [migrationcenter.DeleteImportDataFileRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_groups(
        self,
    ) -> Callable[
        [migrationcenter.ListGroupsRequest],
        Union[
            migrationcenter.ListGroupsResponse,
            Awaitable[migrationcenter.ListGroupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_group(
        self,
    ) -> Callable[
        [migrationcenter.GetGroupRequest],
        Union[migrationcenter.Group, Awaitable[migrationcenter.Group]],
    ]:
        raise NotImplementedError()

    @property
    def create_group(
        self,
    ) -> Callable[
        [migrationcenter.CreateGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_group(
        self,
    ) -> Callable[
        [migrationcenter.UpdateGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_group(
        self,
    ) -> Callable[
        [migrationcenter.DeleteGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def add_assets_to_group(
        self,
    ) -> Callable[
        [migrationcenter.AddAssetsToGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def remove_assets_from_group(
        self,
    ) -> Callable[
        [migrationcenter.RemoveAssetsFromGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_error_frames(
        self,
    ) -> Callable[
        [migrationcenter.ListErrorFramesRequest],
        Union[
            migrationcenter.ListErrorFramesResponse,
            Awaitable[migrationcenter.ListErrorFramesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_error_frame(
        self,
    ) -> Callable[
        [migrationcenter.GetErrorFrameRequest],
        Union[migrationcenter.ErrorFrame, Awaitable[migrationcenter.ErrorFrame]],
    ]:
        raise NotImplementedError()

    @property
    def list_sources(
        self,
    ) -> Callable[
        [migrationcenter.ListSourcesRequest],
        Union[
            migrationcenter.ListSourcesResponse,
            Awaitable[migrationcenter.ListSourcesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_source(
        self,
    ) -> Callable[
        [migrationcenter.GetSourceRequest],
        Union[migrationcenter.Source, Awaitable[migrationcenter.Source]],
    ]:
        raise NotImplementedError()

    @property
    def create_source(
        self,
    ) -> Callable[
        [migrationcenter.CreateSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_source(
        self,
    ) -> Callable[
        [migrationcenter.UpdateSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_source(
        self,
    ) -> Callable[
        [migrationcenter.DeleteSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_preference_sets(
        self,
    ) -> Callable[
        [migrationcenter.ListPreferenceSetsRequest],
        Union[
            migrationcenter.ListPreferenceSetsResponse,
            Awaitable[migrationcenter.ListPreferenceSetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_preference_set(
        self,
    ) -> Callable[
        [migrationcenter.GetPreferenceSetRequest],
        Union[migrationcenter.PreferenceSet, Awaitable[migrationcenter.PreferenceSet]],
    ]:
        raise NotImplementedError()

    @property
    def create_preference_set(
        self,
    ) -> Callable[
        [migrationcenter.CreatePreferenceSetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_preference_set(
        self,
    ) -> Callable[
        [migrationcenter.UpdatePreferenceSetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_preference_set(
        self,
    ) -> Callable[
        [migrationcenter.DeletePreferenceSetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_settings(
        self,
    ) -> Callable[
        [migrationcenter.GetSettingsRequest],
        Union[migrationcenter.Settings, Awaitable[migrationcenter.Settings]],
    ]:
        raise NotImplementedError()

    @property
    def update_settings(
        self,
    ) -> Callable[
        [migrationcenter.UpdateSettingsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_report_config(
        self,
    ) -> Callable[
        [migrationcenter.CreateReportConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_report_config(
        self,
    ) -> Callable[
        [migrationcenter.GetReportConfigRequest],
        Union[migrationcenter.ReportConfig, Awaitable[migrationcenter.ReportConfig]],
    ]:
        raise NotImplementedError()

    @property
    def list_report_configs(
        self,
    ) -> Callable[
        [migrationcenter.ListReportConfigsRequest],
        Union[
            migrationcenter.ListReportConfigsResponse,
            Awaitable[migrationcenter.ListReportConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_report_config(
        self,
    ) -> Callable[
        [migrationcenter.DeleteReportConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_report(
        self,
    ) -> Callable[
        [migrationcenter.CreateReportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_report(
        self,
    ) -> Callable[
        [migrationcenter.GetReportRequest],
        Union[migrationcenter.Report, Awaitable[migrationcenter.Report]],
    ]:
        raise NotImplementedError()

    @property
    def list_reports(
        self,
    ) -> Callable[
        [migrationcenter.ListReportsRequest],
        Union[
            migrationcenter.ListReportsResponse,
            Awaitable[migrationcenter.ListReportsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_report(
        self,
    ) -> Callable[
        [migrationcenter.DeleteReportRequest],
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


__all__ = ("MigrationCenterTransport",)
