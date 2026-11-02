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
from google.cloud.automl import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.automl_v1.services.auto_ml.async_client import AutoMlAsyncClient
from google.cloud.automl_v1.services.auto_ml.client import AutoMlClient
from google.cloud.automl_v1.services.prediction_service.async_client import (
    PredictionServiceAsyncClient,
)
from google.cloud.automl_v1.services.prediction_service.client import (
    PredictionServiceClient,
)
from google.cloud.automl_v1.types.annotation_payload import AnnotationPayload
from google.cloud.automl_v1.types.annotation_spec import AnnotationSpec
from google.cloud.automl_v1.types.classification import (
    ClassificationAnnotation,
    ClassificationEvaluationMetrics,
    ClassificationType,
)
from google.cloud.automl_v1.types.data_items import (
    Document,
    DocumentDimensions,
    ExamplePayload,
    Image,
    TextSnippet,
)
from google.cloud.automl_v1.types.dataset import Dataset
from google.cloud.automl_v1.types.detection import (
    BoundingBoxMetricsEntry,
    ImageObjectDetectionAnnotation,
    ImageObjectDetectionEvaluationMetrics,
)
from google.cloud.automl_v1.types.geometry import BoundingPoly, NormalizedVertex
from google.cloud.automl_v1.types.image import (
    ImageClassificationDatasetMetadata,
    ImageClassificationModelDeploymentMetadata,
    ImageClassificationModelMetadata,
    ImageObjectDetectionDatasetMetadata,
    ImageObjectDetectionModelDeploymentMetadata,
    ImageObjectDetectionModelMetadata,
)
from google.cloud.automl_v1.types.io import (
    BatchPredictInputConfig,
    BatchPredictOutputConfig,
    DocumentInputConfig,
    GcsDestination,
    GcsSource,
    InputConfig,
    ModelExportOutputConfig,
    OutputConfig,
)
from google.cloud.automl_v1.types.model import Model
from google.cloud.automl_v1.types.model_evaluation import ModelEvaluation
from google.cloud.automl_v1.types.operations import (
    BatchPredictOperationMetadata,
    CreateDatasetOperationMetadata,
    CreateModelOperationMetadata,
    DeleteOperationMetadata,
    DeployModelOperationMetadata,
    ExportDataOperationMetadata,
    ExportModelOperationMetadata,
    ImportDataOperationMetadata,
    OperationMetadata,
    UndeployModelOperationMetadata,
)
from google.cloud.automl_v1.types.prediction_service import (
    BatchPredictRequest,
    BatchPredictResult,
    PredictRequest,
    PredictResponse,
)
from google.cloud.automl_v1.types.service import (
    CreateDatasetRequest,
    CreateModelRequest,
    DeleteDatasetRequest,
    DeleteModelRequest,
    DeployModelRequest,
    ExportDataRequest,
    ExportModelRequest,
    GetAnnotationSpecRequest,
    GetDatasetRequest,
    GetModelEvaluationRequest,
    GetModelRequest,
    ImportDataRequest,
    ListDatasetsRequest,
    ListDatasetsResponse,
    ListModelEvaluationsRequest,
    ListModelEvaluationsResponse,
    ListModelsRequest,
    ListModelsResponse,
    UndeployModelRequest,
    UpdateDatasetRequest,
    UpdateModelRequest,
)
from google.cloud.automl_v1.types.text import (
    TextClassificationDatasetMetadata,
    TextClassificationModelMetadata,
    TextExtractionDatasetMetadata,
    TextExtractionModelMetadata,
    TextSentimentDatasetMetadata,
    TextSentimentModelMetadata,
)
from google.cloud.automl_v1.types.text_extraction import (
    TextExtractionAnnotation,
    TextExtractionEvaluationMetrics,
)
from google.cloud.automl_v1.types.text_segment import TextSegment
from google.cloud.automl_v1.types.text_sentiment import (
    TextSentimentAnnotation,
    TextSentimentEvaluationMetrics,
)
from google.cloud.automl_v1.types.translation import (
    TranslationAnnotation,
    TranslationDatasetMetadata,
    TranslationEvaluationMetrics,
    TranslationModelMetadata,
)

__all__ = (
    "AutoMlClient",
    "AutoMlAsyncClient",
    "PredictionServiceClient",
    "PredictionServiceAsyncClient",
    "AnnotationPayload",
    "AnnotationSpec",
    "ClassificationAnnotation",
    "ClassificationEvaluationMetrics",
    "ClassificationType",
    "Document",
    "DocumentDimensions",
    "ExamplePayload",
    "Image",
    "TextSnippet",
    "Dataset",
    "BoundingBoxMetricsEntry",
    "ImageObjectDetectionAnnotation",
    "ImageObjectDetectionEvaluationMetrics",
    "BoundingPoly",
    "NormalizedVertex",
    "ImageClassificationDatasetMetadata",
    "ImageClassificationModelDeploymentMetadata",
    "ImageClassificationModelMetadata",
    "ImageObjectDetectionDatasetMetadata",
    "ImageObjectDetectionModelDeploymentMetadata",
    "ImageObjectDetectionModelMetadata",
    "BatchPredictInputConfig",
    "BatchPredictOutputConfig",
    "DocumentInputConfig",
    "GcsDestination",
    "GcsSource",
    "InputConfig",
    "ModelExportOutputConfig",
    "OutputConfig",
    "Model",
    "ModelEvaluation",
    "BatchPredictOperationMetadata",
    "CreateDatasetOperationMetadata",
    "CreateModelOperationMetadata",
    "DeleteOperationMetadata",
    "DeployModelOperationMetadata",
    "ExportDataOperationMetadata",
    "ExportModelOperationMetadata",
    "ImportDataOperationMetadata",
    "OperationMetadata",
    "UndeployModelOperationMetadata",
    "BatchPredictRequest",
    "BatchPredictResult",
    "PredictRequest",
    "PredictResponse",
    "CreateDatasetRequest",
    "CreateModelRequest",
    "DeleteDatasetRequest",
    "DeleteModelRequest",
    "DeployModelRequest",
    "ExportDataRequest",
    "ExportModelRequest",
    "GetAnnotationSpecRequest",
    "GetDatasetRequest",
    "GetModelEvaluationRequest",
    "GetModelRequest",
    "ImportDataRequest",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "ListModelEvaluationsRequest",
    "ListModelEvaluationsResponse",
    "ListModelsRequest",
    "ListModelsResponse",
    "UndeployModelRequest",
    "UpdateDatasetRequest",
    "UpdateModelRequest",
    "TextClassificationDatasetMetadata",
    "TextClassificationModelMetadata",
    "TextExtractionDatasetMetadata",
    "TextExtractionModelMetadata",
    "TextSentimentDatasetMetadata",
    "TextSentimentModelMetadata",
    "TextExtractionAnnotation",
    "TextExtractionEvaluationMetrics",
    "TextSegment",
    "TextSentimentAnnotation",
    "TextSentimentEvaluationMetrics",
    "TranslationAnnotation",
    "TranslationDatasetMetadata",
    "TranslationEvaluationMetrics",
    "TranslationModelMetadata",
)
