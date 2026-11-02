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
from google.cloud.devtools.containeranalysis import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.devtools.containeranalysis_v1.services.container_analysis.async_client import (
    ContainerAnalysisAsyncClient,
)
from google.cloud.devtools.containeranalysis_v1.services.container_analysis.client import (
    ContainerAnalysisClient,
)
from google.cloud.devtools.containeranalysis_v1.types.containeranalysis import (
    ExportSBOMRequest,
    ExportSBOMResponse,
    GetVulnerabilityOccurrencesSummaryRequest,
    VulnerabilityOccurrencesSummary,
)

__all__ = (
    "ContainerAnalysisClient",
    "ContainerAnalysisAsyncClient",
    "ExportSBOMRequest",
    "ExportSBOMResponse",
    "GetVulnerabilityOccurrencesSummaryRequest",
    "VulnerabilityOccurrencesSummary",
)
