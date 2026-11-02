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
from google.cloud.shell import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.shell_v1.services.cloud_shell_service.async_client import (
    CloudShellServiceAsyncClient,
)
from google.cloud.shell_v1.services.cloud_shell_service.client import (
    CloudShellServiceClient,
)
from google.cloud.shell_v1.types.cloudshell import (
    AddPublicKeyMetadata,
    AddPublicKeyRequest,
    AddPublicKeyResponse,
    AuthorizeEnvironmentMetadata,
    AuthorizeEnvironmentRequest,
    AuthorizeEnvironmentResponse,
    CloudShellErrorDetails,
    CreateEnvironmentMetadata,
    DeleteEnvironmentMetadata,
    Environment,
    GetEnvironmentRequest,
    RemovePublicKeyMetadata,
    RemovePublicKeyRequest,
    RemovePublicKeyResponse,
    StartEnvironmentMetadata,
    StartEnvironmentRequest,
    StartEnvironmentResponse,
)

__all__ = (
    "CloudShellServiceClient",
    "CloudShellServiceAsyncClient",
    "AddPublicKeyMetadata",
    "AddPublicKeyRequest",
    "AddPublicKeyResponse",
    "AuthorizeEnvironmentMetadata",
    "AuthorizeEnvironmentRequest",
    "AuthorizeEnvironmentResponse",
    "CloudShellErrorDetails",
    "CreateEnvironmentMetadata",
    "DeleteEnvironmentMetadata",
    "Environment",
    "GetEnvironmentRequest",
    "RemovePublicKeyMetadata",
    "RemovePublicKeyRequest",
    "RemovePublicKeyResponse",
    "StartEnvironmentMetadata",
    "StartEnvironmentRequest",
    "StartEnvironmentResponse",
)
