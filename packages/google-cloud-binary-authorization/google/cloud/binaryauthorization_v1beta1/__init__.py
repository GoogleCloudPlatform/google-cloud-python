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

from google.cloud.binaryauthorization_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.binaryauthorization_v1beta1.services.binauthz_management_service_v1_beta1",
    "google.cloud.binaryauthorization_v1beta1.services.system_policy_v1_beta1",
    "google.cloud.binaryauthorization_v1beta1.types.continuous_validation_logging",
    "google.cloud.binaryauthorization_v1beta1.types.resources",
    "google.cloud.binaryauthorization_v1beta1.types.service",
}


from .services.binauthz_management_service_v1_beta1 import (
    BinauthzManagementServiceV1Beta1AsyncClient,
    BinauthzManagementServiceV1Beta1Client,
)
from .services.system_policy_v1_beta1 import (
    SystemPolicyV1Beta1AsyncClient,
    SystemPolicyV1Beta1Client,
)
from .types.continuous_validation_logging import ContinuousValidationEvent
from .types.resources import (
    AdmissionRule,
    AdmissionWhitelistPattern,
    Attestor,
    AttestorPublicKey,
    PkixPublicKey,
    Policy,
    UserOwnedDrydockNote,
)
from .types.service import (
    CreateAttestorRequest,
    DeleteAttestorRequest,
    GetAttestorRequest,
    GetPolicyRequest,
    GetSystemPolicyRequest,
    ListAttestorsRequest,
    ListAttestorsResponse,
    UpdateAttestorRequest,
    UpdatePolicyRequest,
)

__all__ = (
    "BinauthzManagementServiceV1Beta1AsyncClient",
    "SystemPolicyV1Beta1AsyncClient",
    "AdmissionRule",
    "AdmissionWhitelistPattern",
    "Attestor",
    "AttestorPublicKey",
    "BinauthzManagementServiceV1Beta1Client",
    "ContinuousValidationEvent",
    "CreateAttestorRequest",
    "DeleteAttestorRequest",
    "GetAttestorRequest",
    "GetPolicyRequest",
    "GetSystemPolicyRequest",
    "ListAttestorsRequest",
    "ListAttestorsResponse",
    "PkixPublicKey",
    "Policy",
    "SystemPolicyV1Beta1Client",
    "UpdateAttestorRequest",
    "UpdatePolicyRequest",
    "UserOwnedDrydockNote",
)

api_core.check_python_version("google.cloud.binaryauthorization_v1beta1")
api_core.check_dependency_versions("google.cloud.binaryauthorization_v1beta1")
