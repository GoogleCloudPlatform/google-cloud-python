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
from google.cloud.workloadidentity import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.workloadidentity_v1.services.workload_identity.async_client import (
    WorkloadIdentityAsyncClient,
)
from google.cloud.workloadidentity_v1.services.workload_identity.client import (
    WorkloadIdentityClient,
)
from google.cloud.workloadidentity_v1.types.service import (
    GenerateServiceAgentsRequest,
    GenerateServiceAgentsResponse,
    OperationMetadata,
    ServiceAgent,
)

__all__ = (
    "WorkloadIdentityClient",
    "WorkloadIdentityAsyncClient",
    "GenerateServiceAgentsRequest",
    "GenerateServiceAgentsResponse",
    "OperationMetadata",
    "ServiceAgent",
)
