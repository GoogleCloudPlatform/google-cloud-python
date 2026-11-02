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
from google.cloud.dataqna import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.dataqna_v1alpha.services.auto_suggestion_service.async_client import (
    AutoSuggestionServiceAsyncClient,
)
from google.cloud.dataqna_v1alpha.services.auto_suggestion_service.client import (
    AutoSuggestionServiceClient,
)
from google.cloud.dataqna_v1alpha.services.question_service.async_client import (
    QuestionServiceAsyncClient,
)
from google.cloud.dataqna_v1alpha.services.question_service.client import (
    QuestionServiceClient,
)
from google.cloud.dataqna_v1alpha.types.annotated_string import AnnotatedString
from google.cloud.dataqna_v1alpha.types.auto_suggestion_service import (
    Suggestion,
    SuggestionInfo,
    SuggestionType,
    SuggestQueriesRequest,
    SuggestQueriesResponse,
)
from google.cloud.dataqna_v1alpha.types.question import (
    BigQueryJob,
    DataQuery,
    DebugFlags,
    ExecutionInfo,
    HumanReadable,
    Interpretation,
    InterpretationStructure,
    InterpretEntity,
    InterpretError,
    Question,
)
from google.cloud.dataqna_v1alpha.types.question_service import (
    CreateQuestionRequest,
    ExecuteQuestionRequest,
    GetQuestionRequest,
    GetUserFeedbackRequest,
    UpdateUserFeedbackRequest,
)
from google.cloud.dataqna_v1alpha.types.user_feedback import UserFeedback

__all__ = (
    "AutoSuggestionServiceClient",
    "AutoSuggestionServiceAsyncClient",
    "QuestionServiceClient",
    "QuestionServiceAsyncClient",
    "AnnotatedString",
    "Suggestion",
    "SuggestionInfo",
    "SuggestQueriesRequest",
    "SuggestQueriesResponse",
    "SuggestionType",
    "BigQueryJob",
    "DataQuery",
    "DebugFlags",
    "ExecutionInfo",
    "HumanReadable",
    "Interpretation",
    "InterpretationStructure",
    "InterpretError",
    "Question",
    "InterpretEntity",
    "CreateQuestionRequest",
    "ExecuteQuestionRequest",
    "GetQuestionRequest",
    "GetUserFeedbackRequest",
    "UpdateUserFeedbackRequest",
    "UserFeedback",
)
