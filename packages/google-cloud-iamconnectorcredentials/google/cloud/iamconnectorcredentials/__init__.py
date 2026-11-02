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
from google.cloud.iamconnectorcredentials import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.iamconnectorcredentials_v1alpha.services.iam_connector_credentials_service.async_client import (
    IAMConnectorCredentialsServiceAsyncClient,
)
from google.cloud.iamconnectorcredentials_v1alpha.services.iam_connector_credentials_service.client import (
    IAMConnectorCredentialsServiceClient,
)
from google.cloud.iamconnectorcredentials_v1alpha.types.connector_credentials import (
    FinalizeCredentialsRequest,
    FinalizeCredentialsResponse,
    RetrieveCredentialsMetadata,
    RetrieveCredentialsRequest,
    RetrieveCredentialsResponse,
)

__all__ = (
    "IAMConnectorCredentialsServiceClient",
    "IAMConnectorCredentialsServiceAsyncClient",
    "FinalizeCredentialsRequest",
    "FinalizeCredentialsResponse",
    "RetrieveCredentialsMetadata",
    "RetrieveCredentialsRequest",
    "RetrieveCredentialsResponse",
)
