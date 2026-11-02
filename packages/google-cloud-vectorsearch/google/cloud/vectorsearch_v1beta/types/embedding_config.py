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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.vectorsearch.v1beta",
    manifest={
        "EmbeddingTaskType",
        "VertexEmbeddingConfig",
    },
)


class EmbeddingTaskType(proto.Enum):
    r"""Represents the task the embeddings will be used for.

    Values:
        EMBEDDING_TASK_TYPE_UNSPECIFIED (0):
            Unspecified task type.
        RETRIEVAL_QUERY (1):
            Specifies the given text is a query in a
            search/retrieval setting.
        RETRIEVAL_DOCUMENT (2):
            Specifies the given text is a document from
            the corpus being searched.
        SEMANTIC_SIMILARITY (3):
            Specifies the given text will be used for
            STS.
        CLASSIFICATION (4):
            Specifies that the given text will be
            classified.
        CLUSTERING (5):
            Specifies that the embeddings will be used
            for clustering.
        QUESTION_ANSWERING (6):
            Specifies that the embeddings will be used
            for question answering.
        FACT_VERIFICATION (7):
            Specifies that the embeddings will be used
            for fact verification.
        CODE_RETRIEVAL_QUERY (8):
            Specifies that the embeddings will be used
            for code retrieval.
    """

    EMBEDDING_TASK_TYPE_UNSPECIFIED = 0
    RETRIEVAL_QUERY = 1
    RETRIEVAL_DOCUMENT = 2
    SEMANTIC_SIMILARITY = 3
    CLASSIFICATION = 4
    CLUSTERING = 5
    QUESTION_ANSWERING = 6
    FACT_VERIFICATION = 7
    CODE_RETRIEVAL_QUERY = 8


class VertexEmbeddingConfig(proto.Message):
    r"""Message describing the configuration for generating
    embeddings for a vector field using Vertex AI embeddings API.

    Attributes:
        model_id (str):
            Required. Required: ID of the embedding model
            to use. See
            https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#embeddings-models
            for the list of supported models.
        text_template (str):
            Optional. Text template for the input to the
            model. The template must contain one or more
            references to fields in the DataObject, e.g.:
            "Movie Title: {title} ---- Movie Plot: {plot}".

            Required when using the text-only path.
        task_type (google.cloud.vectorsearch_v1beta.types.EmbeddingTaskType):
            Optional. Optional: Task type for the
            embeddings. Required for text-only embedding
            models, see
            https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/task-types
            Not needed for multi modal embedding models, see
            https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings#specify-task-instructions
    """

    model_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    text_template: str = proto.Field(
        proto.STRING,
        number=2,
    )
    task_type: "EmbeddingTaskType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="EmbeddingTaskType",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
