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
from google.cloud.appoptimize import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.appoptimize_v1beta.services.app_optimize.async_client import (
    AppOptimizeAsyncClient,
)
from google.cloud.appoptimize_v1beta.services.app_optimize.client import (
    AppOptimizeClient,
)
from google.cloud.appoptimize_v1beta.types.app_optimize import (
    Column,
    CreateReportRequest,
    DeleteReportRequest,
    GetReportRequest,
    ListReportsRequest,
    ListReportsResponse,
    OperationMetadata,
    ReadReportRequest,
    ReadReportResponse,
    Report,
    Scope,
)

__all__ = (
    "AppOptimizeClient",
    "AppOptimizeAsyncClient",
    "Column",
    "CreateReportRequest",
    "DeleteReportRequest",
    "GetReportRequest",
    "ListReportsRequest",
    "ListReportsResponse",
    "OperationMetadata",
    "ReadReportRequest",
    "ReadReportResponse",
    "Report",
    "Scope",
)
