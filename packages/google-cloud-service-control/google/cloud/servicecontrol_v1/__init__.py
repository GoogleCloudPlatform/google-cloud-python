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

from google.cloud.servicecontrol_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.servicecontrol_v1.services.quota_controller",
    "google.cloud.servicecontrol_v1.services.service_controller",
    "google.cloud.servicecontrol_v1.types.check_error",
    "google.cloud.servicecontrol_v1.types.distribution",
    "google.cloud.servicecontrol_v1.types.http_request",
    "google.cloud.servicecontrol_v1.types.log_entry",
    "google.cloud.servicecontrol_v1.types.metric_value",
    "google.cloud.servicecontrol_v1.types.operation",
    "google.cloud.servicecontrol_v1.types.quota_controller",
    "google.cloud.servicecontrol_v1.types.service_controller",
}


from .services.quota_controller import QuotaControllerAsyncClient, QuotaControllerClient
from .services.service_controller import (
    ServiceControllerAsyncClient,
    ServiceControllerClient,
)
from .types.check_error import CheckError
from .types.distribution import Distribution
from .types.http_request import HttpRequest
from .types.log_entry import LogEntry, LogEntryOperation, LogEntrySourceLocation
from .types.metric_value import MetricValue, MetricValueSet
from .types.operation import Operation
from .types.quota_controller import (
    AllocateQuotaRequest,
    AllocateQuotaResponse,
    QuotaError,
    QuotaOperation,
)
from .types.service_controller import (
    CheckRequest,
    CheckResponse,
    ReportRequest,
    ReportResponse,
)

__all__ = (
    "QuotaControllerAsyncClient",
    "ServiceControllerAsyncClient",
    "AllocateQuotaRequest",
    "AllocateQuotaResponse",
    "CheckError",
    "CheckRequest",
    "CheckResponse",
    "Distribution",
    "HttpRequest",
    "LogEntry",
    "LogEntryOperation",
    "LogEntrySourceLocation",
    "MetricValue",
    "MetricValueSet",
    "Operation",
    "QuotaControllerClient",
    "QuotaError",
    "QuotaOperation",
    "ReportRequest",
    "ReportResponse",
    "ServiceControllerClient",
)

api_core.check_python_version("google.cloud.servicecontrol_v1")
api_core.check_dependency_versions("google.cloud.servicecontrol_v1")
