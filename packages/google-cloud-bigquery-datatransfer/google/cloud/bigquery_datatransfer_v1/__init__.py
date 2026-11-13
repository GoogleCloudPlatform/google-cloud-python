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
import google.api_core as api_core

from google.cloud.bigquery_datatransfer_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.bigquery_datatransfer_v1.services.data_transfer_service",
    "google.cloud.bigquery_datatransfer_v1.types.datatransfer",
    "google.cloud.bigquery_datatransfer_v1.types.transfer",
}


from .services.data_transfer_service import (
    DataTransferServiceAsyncClient,
    DataTransferServiceClient,
)
from .types.datatransfer import (
    CheckValidCredsRequest,
    CheckValidCredsResponse,
    CreateTransferConfigRequest,
    DataSource,
    DataSourceParameter,
    DeleteTransferConfigRequest,
    DeleteTransferRunRequest,
    EnrollDataSourcesRequest,
    GetDataSourceRequest,
    GetTransferConfigRequest,
    GetTransferRunRequest,
    ListDataSourcesRequest,
    ListDataSourcesResponse,
    ListTransferConfigsRequest,
    ListTransferConfigsResponse,
    ListTransferLogsRequest,
    ListTransferLogsResponse,
    ListTransferRunsRequest,
    ListTransferRunsResponse,
    ScheduleTransferRunsRequest,
    ScheduleTransferRunsResponse,
    StartManualTransferRunsRequest,
    StartManualTransferRunsResponse,
    UnenrollDataSourcesRequest,
    UpdateTransferConfigRequest,
)
from .types.transfer import (
    EmailPreferences,
    EncryptionConfiguration,
    EventDrivenSchedule,
    ManualSchedule,
    ScheduleOptions,
    ScheduleOptionsV2,
    TimeBasedSchedule,
    TransferConfig,
    TransferMessage,
    TransferRun,
    TransferState,
    TransferType,
    UserInfo,
)

__all__ = (
    "DataTransferServiceAsyncClient",
    "CheckValidCredsRequest",
    "CheckValidCredsResponse",
    "CreateTransferConfigRequest",
    "DataSource",
    "DataSourceParameter",
    "DataTransferServiceClient",
    "DeleteTransferConfigRequest",
    "DeleteTransferRunRequest",
    "EmailPreferences",
    "EncryptionConfiguration",
    "EnrollDataSourcesRequest",
    "EventDrivenSchedule",
    "GetDataSourceRequest",
    "GetTransferConfigRequest",
    "GetTransferRunRequest",
    "ListDataSourcesRequest",
    "ListDataSourcesResponse",
    "ListTransferConfigsRequest",
    "ListTransferConfigsResponse",
    "ListTransferLogsRequest",
    "ListTransferLogsResponse",
    "ListTransferRunsRequest",
    "ListTransferRunsResponse",
    "ManualSchedule",
    "ScheduleOptions",
    "ScheduleOptionsV2",
    "ScheduleTransferRunsRequest",
    "ScheduleTransferRunsResponse",
    "StartManualTransferRunsRequest",
    "StartManualTransferRunsResponse",
    "TimeBasedSchedule",
    "TransferConfig",
    "TransferMessage",
    "TransferRun",
    "TransferState",
    "TransferType",
    "UnenrollDataSourcesRequest",
    "UpdateTransferConfigRequest",
    "UserInfo",
)

api_core.check_python_version("google.cloud.bigquery_datatransfer_v1")
api_core.check_dependency_versions("google.cloud.bigquery_datatransfer_v1")
