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

from google.cloud.iam_v3beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.iam_v3beta.services.access_policies",
    "google.cloud.iam_v3beta.services.policy_bindings",
    "google.cloud.iam_v3beta.services.principal_access_boundary_policies",
    "google.cloud.iam_v3beta.types.access_policies_service",
    "google.cloud.iam_v3beta.types.access_policy_resources",
    "google.cloud.iam_v3beta.types.operation_metadata",
    "google.cloud.iam_v3beta.types.policy_binding_resources",
    "google.cloud.iam_v3beta.types.policy_bindings_service",
    "google.cloud.iam_v3beta.types.principal_access_boundary_policies_service",
    "google.cloud.iam_v3beta.types.principal_access_boundary_policy_resources",
}


from .services.access_policies import AccessPoliciesAsyncClient, AccessPoliciesClient
from .services.policy_bindings import PolicyBindingsAsyncClient, PolicyBindingsClient
from .services.principal_access_boundary_policies import (
    PrincipalAccessBoundaryPoliciesAsyncClient,
    PrincipalAccessBoundaryPoliciesClient,
)
from .types.access_policies_service import (
    CreateAccessPolicyRequest,
    DeleteAccessPolicyRequest,
    GetAccessPolicyRequest,
    ListAccessPoliciesRequest,
    ListAccessPoliciesResponse,
    SearchAccessPolicyBindingsRequest,
    SearchAccessPolicyBindingsResponse,
    UpdateAccessPolicyRequest,
)
from .types.access_policy_resources import (
    AccessPolicy,
    AccessPolicyDetails,
    AccessPolicyRule,
)
from .types.operation_metadata import OperationMetadata
from .types.policy_binding_resources import PolicyBinding
from .types.policy_bindings_service import (
    CreatePolicyBindingRequest,
    DeletePolicyBindingRequest,
    GetPolicyBindingRequest,
    ListPolicyBindingsRequest,
    ListPolicyBindingsResponse,
    SearchTargetPolicyBindingsRequest,
    SearchTargetPolicyBindingsResponse,
    UpdatePolicyBindingRequest,
)
from .types.principal_access_boundary_policies_service import (
    CreatePrincipalAccessBoundaryPolicyRequest,
    DeletePrincipalAccessBoundaryPolicyRequest,
    GetPrincipalAccessBoundaryPolicyRequest,
    ListPrincipalAccessBoundaryPoliciesRequest,
    ListPrincipalAccessBoundaryPoliciesResponse,
    SearchPrincipalAccessBoundaryPolicyBindingsRequest,
    SearchPrincipalAccessBoundaryPolicyBindingsResponse,
    UpdatePrincipalAccessBoundaryPolicyRequest,
)
from .types.principal_access_boundary_policy_resources import (
    PrincipalAccessBoundaryPolicy,
    PrincipalAccessBoundaryPolicyDetails,
    PrincipalAccessBoundaryPolicyRule,
)

__all__ = (
    "AccessPoliciesAsyncClient",
    "PolicyBindingsAsyncClient",
    "PrincipalAccessBoundaryPoliciesAsyncClient",
    "AccessPoliciesClient",
    "AccessPolicy",
    "AccessPolicyDetails",
    "AccessPolicyRule",
    "CreateAccessPolicyRequest",
    "CreatePolicyBindingRequest",
    "CreatePrincipalAccessBoundaryPolicyRequest",
    "DeleteAccessPolicyRequest",
    "DeletePolicyBindingRequest",
    "DeletePrincipalAccessBoundaryPolicyRequest",
    "GetAccessPolicyRequest",
    "GetPolicyBindingRequest",
    "GetPrincipalAccessBoundaryPolicyRequest",
    "ListAccessPoliciesRequest",
    "ListAccessPoliciesResponse",
    "ListPolicyBindingsRequest",
    "ListPolicyBindingsResponse",
    "ListPrincipalAccessBoundaryPoliciesRequest",
    "ListPrincipalAccessBoundaryPoliciesResponse",
    "OperationMetadata",
    "PolicyBinding",
    "PolicyBindingsClient",
    "PrincipalAccessBoundaryPoliciesClient",
    "PrincipalAccessBoundaryPolicy",
    "PrincipalAccessBoundaryPolicyDetails",
    "PrincipalAccessBoundaryPolicyRule",
    "SearchAccessPolicyBindingsRequest",
    "SearchAccessPolicyBindingsResponse",
    "SearchPrincipalAccessBoundaryPolicyBindingsRequest",
    "SearchPrincipalAccessBoundaryPolicyBindingsResponse",
    "SearchTargetPolicyBindingsRequest",
    "SearchTargetPolicyBindingsResponse",
    "UpdateAccessPolicyRequest",
    "UpdatePolicyBindingRequest",
    "UpdatePrincipalAccessBoundaryPolicyRequest",
)

api_core.check_python_version("google.cloud.iam_v3beta")
api_core.check_dependency_versions("google.cloud.iam_v3beta")
