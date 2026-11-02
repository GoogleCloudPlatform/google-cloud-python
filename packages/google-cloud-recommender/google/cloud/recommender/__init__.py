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
from google.cloud.recommender import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.recommender_v1.services.recommender.async_client import (
    RecommenderAsyncClient,
)
from google.cloud.recommender_v1.services.recommender.client import RecommenderClient
from google.cloud.recommender_v1.types.insight import Insight, InsightStateInfo
from google.cloud.recommender_v1.types.insight_type_config import (
    InsightTypeConfig,
    InsightTypeGenerationConfig,
)
from google.cloud.recommender_v1.types.recommendation import (
    CostProjection,
    Impact,
    Operation,
    OperationGroup,
    Recommendation,
    RecommendationContent,
    RecommendationStateInfo,
    ReliabilityProjection,
    SecurityProjection,
    SustainabilityProjection,
    ValueMatcher,
)
from google.cloud.recommender_v1.types.recommender_config import (
    RecommenderConfig,
    RecommenderGenerationConfig,
)
from google.cloud.recommender_v1.types.recommender_service import (
    GetInsightRequest,
    GetInsightTypeConfigRequest,
    GetRecommendationRequest,
    GetRecommenderConfigRequest,
    ListInsightsRequest,
    ListInsightsResponse,
    ListRecommendationsRequest,
    ListRecommendationsResponse,
    MarkInsightAcceptedRequest,
    MarkRecommendationClaimedRequest,
    MarkRecommendationDismissedRequest,
    MarkRecommendationFailedRequest,
    MarkRecommendationSucceededRequest,
    UpdateInsightTypeConfigRequest,
    UpdateRecommenderConfigRequest,
)

__all__ = (
    "RecommenderClient",
    "RecommenderAsyncClient",
    "Insight",
    "InsightStateInfo",
    "InsightTypeConfig",
    "InsightTypeGenerationConfig",
    "CostProjection",
    "Impact",
    "Operation",
    "OperationGroup",
    "Recommendation",
    "RecommendationContent",
    "RecommendationStateInfo",
    "ReliabilityProjection",
    "SecurityProjection",
    "SustainabilityProjection",
    "ValueMatcher",
    "RecommenderConfig",
    "RecommenderGenerationConfig",
    "GetInsightRequest",
    "GetInsightTypeConfigRequest",
    "GetRecommendationRequest",
    "GetRecommenderConfigRequest",
    "ListInsightsRequest",
    "ListInsightsResponse",
    "ListRecommendationsRequest",
    "ListRecommendationsResponse",
    "MarkInsightAcceptedRequest",
    "MarkRecommendationClaimedRequest",
    "MarkRecommendationDismissedRequest",
    "MarkRecommendationFailedRequest",
    "MarkRecommendationSucceededRequest",
    "UpdateInsightTypeConfigRequest",
    "UpdateRecommenderConfigRequest",
)
