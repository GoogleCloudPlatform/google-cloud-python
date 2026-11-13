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

from google.cloud.financialservices_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.financialservices_v1.services.aml",
    "google.cloud.financialservices_v1.types.backtest_result",
    "google.cloud.financialservices_v1.types.bigquery_destination",
    "google.cloud.financialservices_v1.types.dataset",
    "google.cloud.financialservices_v1.types.engine_config",
    "google.cloud.financialservices_v1.types.engine_version",
    "google.cloud.financialservices_v1.types.instance",
    "google.cloud.financialservices_v1.types.line_of_business",
    "google.cloud.financialservices_v1.types.model",
    "google.cloud.financialservices_v1.types.prediction_result",
    "google.cloud.financialservices_v1.types.service",
}


from .services.aml import AMLAsyncClient, AMLClient
from .types.backtest_result import (
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
from .types.bigquery_destination import BigQueryDestination
from .types.dataset import (
    CreateDatasetRequest,
    Dataset,
    DeleteDatasetRequest,
    GetDatasetRequest,
    ListDatasetsRequest,
    ListDatasetsResponse,
    UpdateDatasetRequest,
)
from .types.engine_config import (
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
from .types.engine_version import (
    EngineVersion,
    GetEngineVersionRequest,
    ListEngineVersionsRequest,
    ListEngineVersionsResponse,
)
from .types.instance import (
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
from .types.line_of_business import LineOfBusiness
from .types.model import (
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
from .types.prediction_result import (
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
from .types.service import OperationMetadata

__all__ = (
    "AMLAsyncClient",
    "AMLClient",
    "BacktestResult",
    "BigQueryDestination",
    "CreateBacktestResultRequest",
    "CreateDatasetRequest",
    "CreateEngineConfigRequest",
    "CreateInstanceRequest",
    "CreateModelRequest",
    "CreatePredictionResultRequest",
    "Dataset",
    "DeleteBacktestResultRequest",
    "DeleteDatasetRequest",
    "DeleteEngineConfigRequest",
    "DeleteInstanceRequest",
    "DeleteModelRequest",
    "DeletePredictionResultRequest",
    "EngineConfig",
    "EngineVersion",
    "ExportBacktestResultMetadataRequest",
    "ExportBacktestResultMetadataResponse",
    "ExportEngineConfigMetadataRequest",
    "ExportEngineConfigMetadataResponse",
    "ExportModelMetadataRequest",
    "ExportModelMetadataResponse",
    "ExportPredictionResultMetadataRequest",
    "ExportPredictionResultMetadataResponse",
    "ExportRegisteredPartiesRequest",
    "ExportRegisteredPartiesResponse",
    "GetBacktestResultRequest",
    "GetDatasetRequest",
    "GetEngineConfigRequest",
    "GetEngineVersionRequest",
    "GetInstanceRequest",
    "GetModelRequest",
    "GetPredictionResultRequest",
    "ImportRegisteredPartiesRequest",
    "ImportRegisteredPartiesResponse",
    "Instance",
    "LineOfBusiness",
    "ListBacktestResultsRequest",
    "ListBacktestResultsResponse",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "ListEngineConfigsRequest",
    "ListEngineConfigsResponse",
    "ListEngineVersionsRequest",
    "ListEngineVersionsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListModelsRequest",
    "ListModelsResponse",
    "ListPredictionResultsRequest",
    "ListPredictionResultsResponse",
    "Model",
    "OperationMetadata",
    "PredictionResult",
    "UpdateBacktestResultRequest",
    "UpdateDatasetRequest",
    "UpdateEngineConfigRequest",
    "UpdateInstanceRequest",
    "UpdateModelRequest",
    "UpdatePredictionResultRequest",
)

api_core.check_python_version("google.cloud.financialservices_v1")
api_core.check_dependency_versions("google.cloud.financialservices_v1")
