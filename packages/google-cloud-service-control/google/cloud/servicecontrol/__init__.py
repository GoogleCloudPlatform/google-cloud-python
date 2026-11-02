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
from google.cloud.servicecontrol import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.servicecontrol_v1.services.quota_controller.async_client import (
    QuotaControllerAsyncClient,
)
from google.cloud.servicecontrol_v1.services.quota_controller.client import (
    QuotaControllerClient,
)
from google.cloud.servicecontrol_v1.services.service_controller.async_client import (
    ServiceControllerAsyncClient,
)
from google.cloud.servicecontrol_v1.services.service_controller.client import (
    ServiceControllerClient,
)
from google.cloud.servicecontrol_v1.types.check_error import CheckError
from google.cloud.servicecontrol_v1.types.distribution import Distribution
from google.cloud.servicecontrol_v1.types.http_request import HttpRequest
from google.cloud.servicecontrol_v1.types.log_entry import (
    LogEntry,
    LogEntryOperation,
    LogEntrySourceLocation,
)
from google.cloud.servicecontrol_v1.types.metric_value import (
    MetricValue,
    MetricValueSet,
)
from google.cloud.servicecontrol_v1.types.operation import Operation
from google.cloud.servicecontrol_v1.types.quota_controller import (
    AllocateQuotaRequest,
    AllocateQuotaResponse,
    QuotaError,
    QuotaOperation,
)
from google.cloud.servicecontrol_v1.types.service_controller import (
    CheckRequest,
    CheckResponse,
    ReportRequest,
    ReportResponse,
)

__all__ = (
    "QuotaControllerClient",
    "QuotaControllerAsyncClient",
    "ServiceControllerClient",
    "ServiceControllerAsyncClient",
    "CheckError",
    "Distribution",
    "HttpRequest",
    "LogEntry",
    "LogEntryOperation",
    "LogEntrySourceLocation",
    "MetricValue",
    "MetricValueSet",
    "Operation",
    "AllocateQuotaRequest",
    "AllocateQuotaResponse",
    "QuotaError",
    "QuotaOperation",
    "CheckRequest",
    "CheckResponse",
    "ReportRequest",
    "ReportResponse",
)
