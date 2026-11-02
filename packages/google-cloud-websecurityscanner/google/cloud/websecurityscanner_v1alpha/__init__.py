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

from google.cloud.websecurityscanner_v1alpha import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.websecurityscanner_v1alpha.services.web_security_scanner",
    "google.cloud.websecurityscanner_v1alpha.types.crawled_url",
    "google.cloud.websecurityscanner_v1alpha.types.finding",
    "google.cloud.websecurityscanner_v1alpha.types.finding_addon",
    "google.cloud.websecurityscanner_v1alpha.types.finding_type_stats",
    "google.cloud.websecurityscanner_v1alpha.types.scan_config",
    "google.cloud.websecurityscanner_v1alpha.types.scan_run",
    "google.cloud.websecurityscanner_v1alpha.types.web_security_scanner",
}


from .services.web_security_scanner import (
    WebSecurityScannerAsyncClient,
    WebSecurityScannerClient,
)
from .types.crawled_url import CrawledUrl
from .types.finding import Finding
from .types.finding_addon import (
    OutdatedLibrary,
    ViolatingResource,
    VulnerableHeaders,
    VulnerableParameters,
    Xss,
)
from .types.finding_type_stats import FindingTypeStats
from .types.scan_config import ScanConfig
from .types.scan_run import ScanRun
from .types.web_security_scanner import (
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
    "WebSecurityScannerAsyncClient",
    "CrawledUrl",
    "CreateScanConfigRequest",
    "DeleteScanConfigRequest",
    "Finding",
    "FindingTypeStats",
    "GetFindingRequest",
    "GetScanConfigRequest",
    "GetScanRunRequest",
    "ListCrawledUrlsRequest",
    "ListCrawledUrlsResponse",
    "ListFindingTypeStatsRequest",
    "ListFindingTypeStatsResponse",
    "ListFindingsRequest",
    "ListFindingsResponse",
    "ListScanConfigsRequest",
    "ListScanConfigsResponse",
    "ListScanRunsRequest",
    "ListScanRunsResponse",
    "OutdatedLibrary",
    "ScanConfig",
    "ScanRun",
    "StartScanRunRequest",
    "StopScanRunRequest",
    "UpdateScanConfigRequest",
    "ViolatingResource",
    "VulnerableHeaders",
    "VulnerableParameters",
    "WebSecurityScannerClient",
    "Xss",
)

api_core.check_python_version("google.cloud.websecurityscanner_v1alpha")
api_core.check_dependency_versions("google.cloud.websecurityscanner_v1alpha")
