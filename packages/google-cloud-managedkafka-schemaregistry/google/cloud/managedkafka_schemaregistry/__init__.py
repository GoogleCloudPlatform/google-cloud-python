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
from google.cloud.managedkafka_schemaregistry import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.async_client import (
    ManagedSchemaRegistryAsyncClient,
)
from google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.client import (
    ManagedSchemaRegistryClient,
)
from google.cloud.managedkafka_schemaregistry_v1.types.schema_registry import (
    CheckCompatibilityRequest,
    CheckCompatibilityResponse,
    CreateSchemaRegistryRequest,
    CreateVersionRequest,
    CreateVersionResponse,
    DeleteSchemaConfigRequest,
    DeleteSchemaModeRequest,
    DeleteSchemaRegistryRequest,
    DeleteSubjectRequest,
    DeleteVersionRequest,
    GetContextRequest,
    GetSchemaConfigRequest,
    GetSchemaModeRequest,
    GetSchemaRegistryRequest,
    GetSchemaRequest,
    GetVersionRequest,
    ListContextsRequest,
    ListReferencedSchemasRequest,
    ListSchemaRegistriesRequest,
    ListSchemaRegistriesResponse,
    ListSchemaTypesRequest,
    ListSchemaVersionsRequest,
    ListSubjectsBySchemaIdRequest,
    ListSubjectsRequest,
    ListVersionsRequest,
    LookupVersionRequest,
    UpdateSchemaConfigRequest,
    UpdateSchemaModeRequest,
)
from google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources import (
    Context,
    Schema,
    SchemaConfig,
    SchemaMode,
    SchemaRegistry,
    SchemaSubject,
    SchemaVersion,
)

__all__ = (
    "ManagedSchemaRegistryClient",
    "ManagedSchemaRegistryAsyncClient",
    "CheckCompatibilityRequest",
    "CheckCompatibilityResponse",
    "CreateSchemaRegistryRequest",
    "CreateVersionRequest",
    "CreateVersionResponse",
    "DeleteSchemaConfigRequest",
    "DeleteSchemaModeRequest",
    "DeleteSchemaRegistryRequest",
    "DeleteSubjectRequest",
    "DeleteVersionRequest",
    "GetContextRequest",
    "GetSchemaConfigRequest",
    "GetSchemaModeRequest",
    "GetSchemaRegistryRequest",
    "GetSchemaRequest",
    "GetVersionRequest",
    "ListContextsRequest",
    "ListReferencedSchemasRequest",
    "ListSchemaRegistriesRequest",
    "ListSchemaRegistriesResponse",
    "ListSchemaTypesRequest",
    "ListSchemaVersionsRequest",
    "ListSubjectsBySchemaIdRequest",
    "ListSubjectsRequest",
    "ListVersionsRequest",
    "LookupVersionRequest",
    "UpdateSchemaConfigRequest",
    "UpdateSchemaModeRequest",
    "Context",
    "Schema",
    "SchemaConfig",
    "SchemaMode",
    "SchemaRegistry",
    "SchemaSubject",
    "SchemaVersion",
)
