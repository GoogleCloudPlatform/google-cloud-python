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
from google.developer_knowledge import gapic_version as package_version

__version__ = package_version.__version__


from google.developer_knowledge_v1.services.developer_knowledge.async_client import (
    DeveloperKnowledgeAsyncClient,
)
from google.developer_knowledge_v1.services.developer_knowledge.client import (
    DeveloperKnowledgeClient,
)
from google.developer_knowledge_v1.types.developerknowledge import (
    Answer,
    AnswerQueryRequest,
    AnswerQueryResponse,
    BatchGetDocumentsRequest,
    BatchGetDocumentsResponse,
    Document,
    DocumentChunk,
    DocumentView,
    GetDocumentRequest,
    SearchDocumentChunksRequest,
    SearchDocumentChunksResponse,
)

__all__ = (
    "DeveloperKnowledgeClient",
    "DeveloperKnowledgeAsyncClient",
    "Answer",
    "AnswerQueryRequest",
    "AnswerQueryResponse",
    "BatchGetDocumentsRequest",
    "BatchGetDocumentsResponse",
    "Document",
    "DocumentChunk",
    "GetDocumentRequest",
    "SearchDocumentChunksRequest",
    "SearchDocumentChunksResponse",
    "DocumentView",
)
