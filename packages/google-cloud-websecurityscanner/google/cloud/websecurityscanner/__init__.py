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
from google.cloud.websecurityscanner import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.websecurityscanner_v1.services.web_security_scanner.async_client import (
    WebSecurityScannerAsyncClient,
)
from google.cloud.websecurityscanner_v1.services.web_security_scanner.client import (
    WebSecurityScannerClient,
)
from google.cloud.websecurityscanner_v1.types.crawled_url import CrawledUrl
from google.cloud.websecurityscanner_v1.types.finding import Finding
from google.cloud.websecurityscanner_v1.types.finding_addon import (
    Form,
    OutdatedLibrary,
    ViolatingResource,
    VulnerableHeaders,
    VulnerableParameters,
    Xss,
    Xxe,
)
from google.cloud.websecurityscanner_v1.types.finding_type_stats import FindingTypeStats
from google.cloud.websecurityscanner_v1.types.scan_config import ScanConfig
from google.cloud.websecurityscanner_v1.types.scan_config_error import ScanConfigError
from google.cloud.websecurityscanner_v1.types.scan_run import ScanRun
from google.cloud.websecurityscanner_v1.types.scan_run_error_trace import (
    ScanRunErrorTrace,
)
from google.cloud.websecurityscanner_v1.types.scan_run_log import ScanRunLog
from google.cloud.websecurityscanner_v1.types.scan_run_warning_trace import (
    ScanRunWarningTrace,
)
from google.cloud.websecurityscanner_v1.types.web_security_scanner import (
    CreateScanConfigRequest,
    DeleteScanConfigRequest,
    GetFindingRequest,
    GetScanConfigRequest,
    GetScanRunRequest,
    ListCrawledUrlsRequest,
    ListCrawledUrlsResponse,
    ListFindingsRequest,
    ListFindingsResponse,
    ListFindingTypeStatsRequest,
    ListFindingTypeStatsResponse,
    ListScanConfigsRequest,
    ListScanConfigsResponse,
    ListScanRunsRequest,
    ListScanRunsResponse,
    StartScanRunRequest,
    StopScanRunRequest,
    UpdateScanConfigRequest,
)

__all__ = (
    "WebSecurityScannerClient",
    "WebSecurityScannerAsyncClient",
    "CrawledUrl",
    "Finding",
    "Form",
    "OutdatedLibrary",
    "ViolatingResource",
    "VulnerableHeaders",
    "VulnerableParameters",
    "Xss",
    "Xxe",
    "FindingTypeStats",
    "ScanConfig",
    "ScanConfigError",
    "ScanRun",
    "ScanRunErrorTrace",
    "ScanRunLog",
    "ScanRunWarningTrace",
    "CreateScanConfigRequest",
    "DeleteScanConfigRequest",
    "GetFindingRequest",
    "GetScanConfigRequest",
    "GetScanRunRequest",
    "ListCrawledUrlsRequest",
    "ListCrawledUrlsResponse",
    "ListFindingsRequest",
    "ListFindingsResponse",
    "ListFindingTypeStatsRequest",
    "ListFindingTypeStatsResponse",
    "ListScanConfigsRequest",
    "ListScanConfigsResponse",
    "ListScanRunsRequest",
    "ListScanRunsResponse",
    "StartScanRunRequest",
    "StopScanRunRequest",
    "UpdateScanConfigRequest",
)
