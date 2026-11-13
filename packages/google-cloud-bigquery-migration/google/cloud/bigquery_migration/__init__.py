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
from google.cloud.bigquery_migration import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.bigquery_migration_v2.services.migration_service.async_client import (
    MigrationServiceAsyncClient,
)
from google.cloud.bigquery_migration_v2.services.migration_service.client import (
    MigrationServiceClient,
)
from google.cloud.bigquery_migration_v2.types.assessment_task import (
    AssessmentFeatureHandle,
    AssessmentTaskDetails,
)
from google.cloud.bigquery_migration_v2.types.migration_entities import (
    LineageOutput,
    MigrationSubtask,
    MigrationTask,
    MigrationTaskResult,
    MigrationWorkflow,
    TaskOutput,
    TranslationTaskResult,
)
from google.cloud.bigquery_migration_v2.types.migration_error_details import (
    ErrorDetail,
    ErrorLocation,
    ResourceErrorDetail,
)
from google.cloud.bigquery_migration_v2.types.migration_metrics import (
    Point,
    TimeInterval,
    TimeSeries,
    TypedValue,
)
from google.cloud.bigquery_migration_v2.types.migration_service import (
    CreateMigrationWorkflowRequest,
    DeleteMigrationWorkflowRequest,
    GetMigrationSubtaskRequest,
    GetMigrationWorkflowRequest,
    ListMigrationSubtasksRequest,
    ListMigrationSubtasksResponse,
    ListMigrationWorkflowsRequest,
    ListMigrationWorkflowsResponse,
    StartMigrationWorkflowRequest,
)
from google.cloud.bigquery_migration_v2.types.translation_config import (
    AzureSynapseDialect,
    BigQueryDialect,
    DB2Dialect,
    Dialect,
    GreenplumDialect,
    HiveQLDialect,
    MySQLDialect,
    NameMappingKey,
    NameMappingValue,
    NetezzaDialect,
    ObjectNameMapping,
    ObjectNameMappingList,
    OracleDialect,
    PostgresqlDialect,
    PrestoDialect,
    RedshiftDialect,
    SnowflakeDialect,
    SourceEnv,
    SparkSQLDialect,
    SQLiteDialect,
    SQLServerDialect,
    TeradataDialect,
    TranslationConfigDetails,
    VerticaDialect,
)
from google.cloud.bigquery_migration_v2.types.translation_details import (
    Literal,
    SourceEnvironment,
    SourceSpec,
    SourceTargetMapping,
    SuggestionConfig,
    SuggestionStep,
    TargetSpec,
    TranslationDetails,
)
from google.cloud.bigquery_migration_v2.types.translation_suggestion import (
    TranslationReportRecord,
)
from google.cloud.bigquery_migration_v2.types.translation_usability import (
    GcsReportLogMessage,
)

__all__ = (
    "MigrationServiceClient",
    "MigrationServiceAsyncClient",
    "AssessmentFeatureHandle",
    "AssessmentTaskDetails",
    "LineageOutput",
    "MigrationSubtask",
    "MigrationTask",
    "MigrationTaskResult",
    "MigrationWorkflow",
    "TaskOutput",
    "TranslationTaskResult",
    "ErrorDetail",
    "ErrorLocation",
    "ResourceErrorDetail",
    "Point",
    "TimeInterval",
    "TimeSeries",
    "TypedValue",
    "CreateMigrationWorkflowRequest",
    "DeleteMigrationWorkflowRequest",
    "GetMigrationSubtaskRequest",
    "GetMigrationWorkflowRequest",
    "ListMigrationSubtasksRequest",
    "ListMigrationSubtasksResponse",
    "ListMigrationWorkflowsRequest",
    "ListMigrationWorkflowsResponse",
    "StartMigrationWorkflowRequest",
    "AzureSynapseDialect",
    "BigQueryDialect",
    "DB2Dialect",
    "Dialect",
    "GreenplumDialect",
    "HiveQLDialect",
    "MySQLDialect",
    "NameMappingKey",
    "NameMappingValue",
    "NetezzaDialect",
    "ObjectNameMapping",
    "ObjectNameMappingList",
    "OracleDialect",
    "PostgresqlDialect",
    "PrestoDialect",
    "RedshiftDialect",
    "SnowflakeDialect",
    "SourceEnv",
    "SparkSQLDialect",
    "SQLiteDialect",
    "SQLServerDialect",
    "TeradataDialect",
    "TranslationConfigDetails",
    "VerticaDialect",
    "Literal",
    "SourceEnvironment",
    "SourceSpec",
    "SourceTargetMapping",
    "SuggestionConfig",
    "SuggestionStep",
    "TargetSpec",
    "TranslationDetails",
    "TranslationReportRecord",
    "GcsReportLogMessage",
)
