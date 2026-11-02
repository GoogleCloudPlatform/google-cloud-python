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
from google.cloud.gsuiteaddons import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.gsuiteaddons_v1.services.g_suite_add_ons.async_client import (
    GSuiteAddOnsAsyncClient,
)
from google.cloud.gsuiteaddons_v1.services.g_suite_add_ons.client import (
    GSuiteAddOnsClient,
)
from google.cloud.gsuiteaddons_v1.types.gsuiteaddons import (
    AddOns,
    Authorization,
    CreateDeploymentRequest,
    DeleteDeploymentRequest,
    Deployment,
    GetAuthorizationRequest,
    GetDeploymentRequest,
    GetInstallStatusRequest,
    InstallDeploymentRequest,
    InstallStatus,
    ListDeploymentsRequest,
    ListDeploymentsResponse,
    ReplaceDeploymentRequest,
    UninstallDeploymentRequest,
)

__all__ = (
    "GSuiteAddOnsClient",
    "GSuiteAddOnsAsyncClient",
    "AddOns",
    "Authorization",
    "CreateDeploymentRequest",
    "DeleteDeploymentRequest",
    "Deployment",
    "GetAuthorizationRequest",
    "GetDeploymentRequest",
    "GetInstallStatusRequest",
    "InstallDeploymentRequest",
    "InstallStatus",
    "ListDeploymentsRequest",
    "ListDeploymentsResponse",
    "ReplaceDeploymentRequest",
    "UninstallDeploymentRequest",
)
