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

from google.cloud.notebooks_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.notebooks_v1beta1.services.notebook_service",
    "google.cloud.notebooks_v1beta1.types.environment",
    "google.cloud.notebooks_v1beta1.types.instance",
    "google.cloud.notebooks_v1beta1.types.service",
}


from .services.notebook_service import NotebookServiceAsyncClient, NotebookServiceClient
from .types.environment import ContainerImage, Environment, VmImage
from .types.instance import Instance, ReservationAffinity
from .types.service import (
    CreateEnvironmentRequest,
    CreateInstanceRequest,
    DeleteEnvironmentRequest,
    DeleteInstanceRequest,
    GetEnvironmentRequest,
    GetInstanceRequest,
    IsInstanceUpgradeableRequest,
    IsInstanceUpgradeableResponse,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    OperationMetadata,
    RegisterInstanceRequest,
    ReportInstanceInfoRequest,
    ResetInstanceRequest,
    SetInstanceAcceleratorRequest,
    SetInstanceLabelsRequest,
    SetInstanceMachineTypeRequest,
    StartInstanceRequest,
    StopInstanceRequest,
    UpgradeInstanceInternalRequest,
    UpgradeInstanceRequest,
)

__all__ = (
    "NotebookServiceAsyncClient",
    "ContainerImage",
    "CreateEnvironmentRequest",
    "CreateInstanceRequest",
    "DeleteEnvironmentRequest",
    "DeleteInstanceRequest",
    "Environment",
    "GetEnvironmentRequest",
    "GetInstanceRequest",
    "Instance",
    "IsInstanceUpgradeableRequest",
    "IsInstanceUpgradeableResponse",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "NotebookServiceClient",
    "OperationMetadata",
    "RegisterInstanceRequest",
    "ReportInstanceInfoRequest",
    "ReservationAffinity",
    "ResetInstanceRequest",
    "SetInstanceAcceleratorRequest",
    "SetInstanceLabelsRequest",
    "SetInstanceMachineTypeRequest",
    "StartInstanceRequest",
    "StopInstanceRequest",
    "UpgradeInstanceInternalRequest",
    "UpgradeInstanceRequest",
    "VmImage",
)

api_core.check_python_version("google.cloud.notebooks_v1beta1")
api_core.check_dependency_versions("google.cloud.notebooks_v1beta1")
