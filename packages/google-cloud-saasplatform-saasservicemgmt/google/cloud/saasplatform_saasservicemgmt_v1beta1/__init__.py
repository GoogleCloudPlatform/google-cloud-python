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

from google.cloud.saasplatform_saasservicemgmt_v1beta1 import (
    gapic_version as package_version,
)

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_deployments",
    "google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts",
    "google.cloud.saasplatform_saasservicemgmt_v1beta1.types.common",
    "google.cloud.saasplatform_saasservicemgmt_v1beta1.types.deployments_resources",
    "google.cloud.saasplatform_saasservicemgmt_v1beta1.types.deployments_service",
    "google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources",
    "google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service",
}


from .services.saas_deployments import SaasDeploymentsAsyncClient, SaasDeploymentsClient
from .services.saas_rollouts import SaasRolloutsAsyncClient, SaasRolloutsClient
from .types.common import (
    Aggregate,
    Blueprint,
    SaasCondition,
    UnitCondition,
    UnitOperationCondition,
    UnitOperationErrorCategory,
    UnitVariable,
)
from .types.deployments_resources import (
    AppParams,
    ComponentRef,
    CompositeRef,
    Dependency,
    Deprovision,
    FromMapping,
    Location,
    Provision,
    Release,
    Saas,
    Schedule,
    Tenant,
    ToMapping,
    Unit,
    UnitDependency,
    UnitKind,
    UnitOperation,
    Upgrade,
    VariableMapping,
)
from .types.deployments_service import (
    CreateReleaseRequest,
    CreateSaasRequest,
    CreateTenantRequest,
    CreateUnitKindRequest,
    CreateUnitOperationRequest,
    CreateUnitRequest,
    DeleteReleaseRequest,
    DeleteSaasRequest,
    DeleteTenantRequest,
    DeleteUnitKindRequest,
    DeleteUnitOperationRequest,
    DeleteUnitRequest,
    GetReleaseRequest,
    GetSaasRequest,
    GetTenantRequest,
    GetUnitKindRequest,
    GetUnitOperationRequest,
    GetUnitRequest,
    ListReleasesRequest,
    ListReleasesResponse,
    ListSaasRequest,
    ListSaasResponse,
    ListTenantsRequest,
    ListTenantsResponse,
    ListUnitKindsRequest,
    ListUnitKindsResponse,
    ListUnitOperationsRequest,
    ListUnitOperationsResponse,
    ListUnitsRequest,
    ListUnitsResponse,
    UpdateReleaseRequest,
    UpdateSaasRequest,
    UpdateTenantRequest,
    UpdateUnitKindRequest,
    UpdateUnitOperationRequest,
    UpdateUnitRequest,
)
from .types.rollouts_resources import (
    ErrorBudget,
    Rollout,
    RolloutAction,
    RolloutControl,
    RolloutKind,
    RolloutStats,
)
from .types.rollouts_service import (
    CreateRolloutKindRequest,
    CreateRolloutRequest,
    DeleteRolloutKindRequest,
    DeleteRolloutRequest,
    GetRolloutKindRequest,
    GetRolloutRequest,
    ListRolloutKindsRequest,
    ListRolloutKindsResponse,
    ListRolloutsRequest,
    ListRolloutsResponse,
    UpdateRolloutKindRequest,
    UpdateRolloutRequest,
)

__all__ = (
    "SaasDeploymentsAsyncClient",
    "SaasRolloutsAsyncClient",
    "Aggregate",
    "AppParams",
    "Blueprint",
    "ComponentRef",
    "CompositeRef",
    "CreateReleaseRequest",
    "CreateRolloutKindRequest",
    "CreateRolloutRequest",
    "CreateSaasRequest",
    "CreateTenantRequest",
    "CreateUnitKindRequest",
    "CreateUnitOperationRequest",
    "CreateUnitRequest",
    "DeleteReleaseRequest",
    "DeleteRolloutKindRequest",
    "DeleteRolloutRequest",
    "DeleteSaasRequest",
    "DeleteTenantRequest",
    "DeleteUnitKindRequest",
    "DeleteUnitOperationRequest",
    "DeleteUnitRequest",
    "Dependency",
    "Deprovision",
    "ErrorBudget",
    "FromMapping",
    "GetReleaseRequest",
    "GetRolloutKindRequest",
    "GetRolloutRequest",
    "GetSaasRequest",
    "GetTenantRequest",
    "GetUnitKindRequest",
    "GetUnitOperationRequest",
    "GetUnitRequest",
    "ListReleasesRequest",
    "ListReleasesResponse",
    "ListRolloutKindsRequest",
    "ListRolloutKindsResponse",
    "ListRolloutsRequest",
    "ListRolloutsResponse",
    "ListSaasRequest",
    "ListSaasResponse",
    "ListTenantsRequest",
    "ListTenantsResponse",
    "ListUnitKindsRequest",
    "ListUnitKindsResponse",
    "ListUnitOperationsRequest",
    "ListUnitOperationsResponse",
    "ListUnitsRequest",
    "ListUnitsResponse",
    "Location",
    "Provision",
    "Release",
    "Rollout",
    "RolloutAction",
    "RolloutControl",
    "RolloutKind",
    "RolloutStats",
    "Saas",
    "SaasCondition",
    "SaasDeploymentsClient",
    "SaasRolloutsClient",
    "Schedule",
    "Tenant",
    "ToMapping",
    "Unit",
    "UnitCondition",
    "UnitDependency",
    "UnitKind",
    "UnitOperation",
    "UnitOperationCondition",
    "UnitOperationErrorCategory",
    "UnitVariable",
    "UpdateReleaseRequest",
    "UpdateRolloutKindRequest",
    "UpdateRolloutRequest",
    "UpdateSaasRequest",
    "UpdateTenantRequest",
    "UpdateUnitKindRequest",
    "UpdateUnitOperationRequest",
    "UpdateUnitRequest",
    "Upgrade",
    "VariableMapping",
)

api_core.check_python_version("google.cloud.saasplatform_saasservicemgmt_v1beta1")
api_core.check_dependency_versions("google.cloud.saasplatform_saasservicemgmt_v1beta1")
