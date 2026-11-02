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
from google.cloud.financialservices import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.financialservices_v1.services.aml.async_client import AMLAsyncClient
from google.cloud.financialservices_v1.services.aml.client import AMLClient
from google.cloud.financialservices_v1.types.backtest_result import (
    BacktestResult,
    CreateBacktestResultRequest,
    DeleteBacktestResultRequest,
    ExportBacktestResultMetadataRequest,
    ExportBacktestResultMetadataResponse,
    GetBacktestResultRequest,
    ListBacktestResultsRequest,
    ListBacktestResultsResponse,
    UpdateBacktestResultRequest,
)
from google.cloud.financialservices_v1.types.bigquery_destination import (
    BigQueryDestination,
)
from google.cloud.financialservices_v1.types.dataset import (
    CreateDatasetRequest,
    Dataset,
    DeleteDatasetRequest,
    GetDatasetRequest,
    ListDatasetsRequest,
    ListDatasetsResponse,
    UpdateDatasetRequest,
)
from google.cloud.financialservices_v1.types.engine_config import (
    CreateEngineConfigRequest,
    DeleteEngineConfigRequest,
    EngineConfig,
    ExportEngineConfigMetadataRequest,
    ExportEngineConfigMetadataResponse,
    GetEngineConfigRequest,
    ListEngineConfigsRequest,
    ListEngineConfigsResponse,
    UpdateEngineConfigRequest,
)
from google.cloud.financialservices_v1.types.engine_version import (
    EngineVersion,
    GetEngineVersionRequest,
    ListEngineVersionsRequest,
    ListEngineVersionsResponse,
)
from google.cloud.financialservices_v1.types.instance import (
    CreateInstanceRequest,
    DeleteInstanceRequest,
    ExportRegisteredPartiesRequest,
    ExportRegisteredPartiesResponse,
    GetInstanceRequest,
    ImportRegisteredPartiesRequest,
    ImportRegisteredPartiesResponse,
    Instance,
    ListInstancesRequest,
    ListInstancesResponse,
    UpdateInstanceRequest,
)
from google.cloud.financialservices_v1.types.line_of_business import LineOfBusiness
from google.cloud.financialservices_v1.types.model import (
    CreateModelRequest,
    DeleteModelRequest,
    ExportModelMetadataRequest,
    ExportModelMetadataResponse,
    GetModelRequest,
    ListModelsRequest,
    ListModelsResponse,
    Model,
    UpdateModelRequest,
)
from google.cloud.financialservices_v1.types.prediction_result import (
    CreatePredictionResultRequest,
    DeletePredictionResultRequest,
    ExportPredictionResultMetadataRequest,
    ExportPredictionResultMetadataResponse,
    GetPredictionResultRequest,
    ListPredictionResultsRequest,
    ListPredictionResultsResponse,
    PredictionResult,
    UpdatePredictionResultRequest,
)
from google.cloud.financialservices_v1.types.service import OperationMetadata

__all__ = (
    "AMLClient",
    "AMLAsyncClient",
    "BacktestResult",
    "CreateBacktestResultRequest",
    "DeleteBacktestResultRequest",
    "ExportBacktestResultMetadataRequest",
    "ExportBacktestResultMetadataResponse",
    "GetBacktestResultRequest",
    "ListBacktestResultsRequest",
    "ListBacktestResultsResponse",
    "UpdateBacktestResultRequest",
    "BigQueryDestination",
    "CreateDatasetRequest",
    "Dataset",
    "DeleteDatasetRequest",
    "GetDatasetRequest",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "UpdateDatasetRequest",
    "CreateEngineConfigRequest",
    "DeleteEngineConfigRequest",
    "EngineConfig",
    "ExportEngineConfigMetadataRequest",
    "ExportEngineConfigMetadataResponse",
    "GetEngineConfigRequest",
    "ListEngineConfigsRequest",
    "ListEngineConfigsResponse",
    "UpdateEngineConfigRequest",
    "EngineVersion",
    "GetEngineVersionRequest",
    "ListEngineVersionsRequest",
    "ListEngineVersionsResponse",
    "CreateInstanceRequest",
    "DeleteInstanceRequest",
    "ExportRegisteredPartiesRequest",
    "ExportRegisteredPartiesResponse",
    "GetInstanceRequest",
    "ImportRegisteredPartiesRequest",
    "ImportRegisteredPartiesResponse",
    "Instance",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "UpdateInstanceRequest",
    "LineOfBusiness",
    "CreateModelRequest",
    "DeleteModelRequest",
    "ExportModelMetadataRequest",
    "ExportModelMetadataResponse",
    "GetModelRequest",
    "ListModelsRequest",
    "ListModelsResponse",
    "Model",
    "UpdateModelRequest",
    "CreatePredictionResultRequest",
    "DeletePredictionResultRequest",
    "ExportPredictionResultMetadataRequest",
    "ExportPredictionResultMetadataResponse",
    "GetPredictionResultRequest",
    "ListPredictionResultsRequest",
    "ListPredictionResultsResponse",
    "PredictionResult",
    "UpdatePredictionResultRequest",
    "OperationMetadata",
)
