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
from google.cloud.binaryauthorization import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.binaryauthorization_v1.services.binauthz_management_service_v1.async_client import (
    BinauthzManagementServiceV1AsyncClient,
)
from google.cloud.binaryauthorization_v1.services.binauthz_management_service_v1.client import (
    BinauthzManagementServiceV1Client,
)
from google.cloud.binaryauthorization_v1.services.system_policy_v1.async_client import (
    SystemPolicyV1AsyncClient,
)
from google.cloud.binaryauthorization_v1.services.system_policy_v1.client import (
    SystemPolicyV1Client,
)
from google.cloud.binaryauthorization_v1.services.validation_helper_v1.async_client import (
    ValidationHelperV1AsyncClient,
)
from google.cloud.binaryauthorization_v1.services.validation_helper_v1.client import (
    ValidationHelperV1Client,
)
from google.cloud.binaryauthorization_v1.types.resources import (
    AdmissionRule,
    AdmissionWhitelistPattern,
    Attestor,
    AttestorPublicKey,
    PkixPublicKey,
    Policy,
    UserOwnedGrafeasNote,
)
from google.cloud.binaryauthorization_v1.types.service import (
    CreateAttestorRequest,
    DeleteAttestorRequest,
    GetAttestorRequest,
    GetPolicyRequest,
    GetSystemPolicyRequest,
    ListAttestorsRequest,
    ListAttestorsResponse,
    UpdateAttestorRequest,
    UpdatePolicyRequest,
    ValidateAttestationOccurrenceRequest,
    ValidateAttestationOccurrenceResponse,
)

__all__ = (
    "BinauthzManagementServiceV1Client",
    "BinauthzManagementServiceV1AsyncClient",
    "SystemPolicyV1Client",
    "SystemPolicyV1AsyncClient",
    "ValidationHelperV1Client",
    "ValidationHelperV1AsyncClient",
    "AdmissionRule",
    "AdmissionWhitelistPattern",
    "Attestor",
    "AttestorPublicKey",
    "PkixPublicKey",
    "Policy",
    "UserOwnedGrafeasNote",
    "CreateAttestorRequest",
    "DeleteAttestorRequest",
    "GetAttestorRequest",
    "GetPolicyRequest",
    "GetSystemPolicyRequest",
    "ListAttestorsRequest",
    "ListAttestorsResponse",
    "UpdateAttestorRequest",
    "UpdatePolicyRequest",
    "ValidateAttestationOccurrenceRequest",
    "ValidateAttestationOccurrenceResponse",
)
