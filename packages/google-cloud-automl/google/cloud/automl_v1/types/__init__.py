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
from .annotation_payload import (
    AnnotationPayload,
)
from .annotation_spec import (
    AnnotationSpec,
)
from .classification import (
    ClassificationAnnotation,
    ClassificationEvaluationMetrics,
    ClassificationType,
)
from .data_items import (
    Document,
    DocumentDimensions,
    ExamplePayload,
    Image,
    TextSnippet,
)
from .dataset import (
    Dataset,
)
from .detection import (
    BoundingBoxMetricsEntry,
    ImageObjectDetectionAnnotation,
    ImageObjectDetectionEvaluationMetrics,
)
from .geometry import (
    BoundingPoly,
    NormalizedVertex,
)
from .image import (
    ImageClassificationDatasetMetadata,
    ImageClassificationModelDeploymentMetadata,
    ImageClassificationModelMetadata,
    ImageObjectDetectionDatasetMetadata,
    ImageObjectDetectionModelDeploymentMetadata,
    ImageObjectDetectionModelMetadata,
)
from .io import (
    BatchPredictInputConfig,
    BatchPredictOutputConfig,
    DocumentInputConfig,
    GcsDestination,
    GcsSource,
    InputConfig,
    ModelExportOutputConfig,
    OutputConfig,
)
from .model import (
    Model,
)
from .model_evaluation import (
    ModelEvaluation,
)
from .operations import (
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
from .prediction_service import (
    BatchPredictRequest,
    BatchPredictResult,
    PredictRequest,
    PredictResponse,
)
from .service import (
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
from .text import (
    TextClassificationDatasetMetadata,
    TextClassificationModelMetadata,
    TextExtractionDatasetMetadata,
    TextExtractionModelMetadata,
    TextSentimentDatasetMetadata,
    TextSentimentModelMetadata,
)
from .text_extraction import (
    TextExtractionAnnotation,
    TextExtractionEvaluationMetrics,
)
from .text_segment import (
    TextSegment,
)
from .text_sentiment import (
    TextSentimentAnnotation,
    TextSentimentEvaluationMetrics,
)
from .translation import (
    TranslationAnnotation,
    TranslationDatasetMetadata,
    TranslationEvaluationMetrics,
    TranslationModelMetadata,
)

__all__ = (
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
