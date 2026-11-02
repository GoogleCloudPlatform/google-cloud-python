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
    VideoClassificationAnnotation,
)
from .column_spec import (
    ColumnSpec,
)
from .data_items import (
    Document,
    DocumentDimensions,
    ExamplePayload,
    Image,
    Row,
    TextSnippet,
)
from .data_stats import (
    ArrayStats,
    CategoryStats,
    CorrelationStats,
    DataStats,
    Float64Stats,
    StringStats,
    StructStats,
    TimestampStats,
)
from .data_types import (
    DataType,
    StructType,
    TypeCode,
)
from .dataset import (
    Dataset,
)
from .detection import (
    BoundingBoxMetricsEntry,
    ImageObjectDetectionAnnotation,
    ImageObjectDetectionEvaluationMetrics,
    VideoObjectTrackingAnnotation,
    VideoObjectTrackingEvaluationMetrics,
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
    BigQueryDestination,
    BigQuerySource,
    DocumentInputConfig,
    ExportEvaluatedExamplesOutputConfig,
    GcrDestination,
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
    CreateModelOperationMetadata,
    DeleteOperationMetadata,
    DeployModelOperationMetadata,
    ExportDataOperationMetadata,
    ExportEvaluatedExamplesOperationMetadata,
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
from .ranges import (
    DoubleRange,
)
from .regression import (
    RegressionEvaluationMetrics,
)
from .service import (
    CreateDatasetRequest,
    CreateModelRequest,
    DeleteDatasetRequest,
    DeleteModelRequest,
    DeployModelRequest,
    ExportDataRequest,
    ExportEvaluatedExamplesRequest,
    ExportModelRequest,
    GetAnnotationSpecRequest,
    GetColumnSpecRequest,
    GetDatasetRequest,
    GetModelEvaluationRequest,
    GetModelRequest,
    GetTableSpecRequest,
    ImportDataRequest,
    ListColumnSpecsRequest,
    ListColumnSpecsResponse,
    ListDatasetsRequest,
    ListDatasetsResponse,
    ListModelEvaluationsRequest,
    ListModelEvaluationsResponse,
    ListModelsRequest,
    ListModelsResponse,
    ListTableSpecsRequest,
    ListTableSpecsResponse,
    UndeployModelRequest,
    UpdateColumnSpecRequest,
    UpdateDatasetRequest,
    UpdateTableSpecRequest,
)
from .table_spec import (
    TableSpec,
)
from .tables import (
    TablesAnnotation,
    TablesDatasetMetadata,
    TablesModelColumnInfo,
    TablesModelMetadata,
)
from .temporal import (
    TimeSegment,
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
from .video import (
    VideoClassificationDatasetMetadata,
    VideoClassificationModelMetadata,
    VideoObjectTrackingDatasetMetadata,
    VideoObjectTrackingModelMetadata,
)

__all__ = (
    "AnnotationPayload",
    "AnnotationSpec",
    "ClassificationAnnotation",
    "ClassificationEvaluationMetrics",
    "VideoClassificationAnnotation",
    "ClassificationType",
    "ColumnSpec",
    "Document",
    "DocumentDimensions",
    "ExamplePayload",
    "Image",
    "Row",
    "TextSnippet",
    "ArrayStats",
    "CategoryStats",
    "CorrelationStats",
    "DataStats",
    "Float64Stats",
    "StringStats",
    "StructStats",
    "TimestampStats",
    "DataType",
    "StructType",
    "TypeCode",
    "Dataset",
    "BoundingBoxMetricsEntry",
    "ImageObjectDetectionAnnotation",
    "ImageObjectDetectionEvaluationMetrics",
    "VideoObjectTrackingAnnotation",
    "VideoObjectTrackingEvaluationMetrics",
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
    "BigQueryDestination",
    "BigQuerySource",
    "DocumentInputConfig",
    "ExportEvaluatedExamplesOutputConfig",
    "GcrDestination",
    "GcsDestination",
    "GcsSource",
    "InputConfig",
    "ModelExportOutputConfig",
    "OutputConfig",
    "Model",
    "ModelEvaluation",
    "BatchPredictOperationMetadata",
    "CreateModelOperationMetadata",
    "DeleteOperationMetadata",
    "DeployModelOperationMetadata",
    "ExportDataOperationMetadata",
    "ExportEvaluatedExamplesOperationMetadata",
    "ExportModelOperationMetadata",
    "ImportDataOperationMetadata",
    "OperationMetadata",
    "UndeployModelOperationMetadata",
    "BatchPredictRequest",
    "BatchPredictResult",
    "PredictRequest",
    "PredictResponse",
    "DoubleRange",
    "RegressionEvaluationMetrics",
    "CreateDatasetRequest",
    "CreateModelRequest",
    "DeleteDatasetRequest",
    "DeleteModelRequest",
    "DeployModelRequest",
    "ExportDataRequest",
    "ExportEvaluatedExamplesRequest",
    "ExportModelRequest",
    "GetAnnotationSpecRequest",
    "GetColumnSpecRequest",
    "GetDatasetRequest",
    "GetModelEvaluationRequest",
    "GetModelRequest",
    "GetTableSpecRequest",
    "ImportDataRequest",
    "ListColumnSpecsRequest",
    "ListColumnSpecsResponse",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "ListModelEvaluationsRequest",
    "ListModelEvaluationsResponse",
    "ListModelsRequest",
    "ListModelsResponse",
    "ListTableSpecsRequest",
    "ListTableSpecsResponse",
    "UndeployModelRequest",
    "UpdateColumnSpecRequest",
    "UpdateDatasetRequest",
    "UpdateTableSpecRequest",
    "TableSpec",
    "TablesAnnotation",
    "TablesDatasetMetadata",
    "TablesModelColumnInfo",
    "TablesModelMetadata",
    "TimeSegment",
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
    "VideoClassificationDatasetMetadata",
    "VideoClassificationModelMetadata",
    "VideoObjectTrackingDatasetMetadata",
    "VideoObjectTrackingModelMetadata",
)
