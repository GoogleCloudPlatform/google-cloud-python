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
    package="google.cloud.ces.v1beta",
    manifest={
        "FileSearchTool",
    },
)


class FileSearchTool(proto.Message):
    r"""The file search tool allows the agent to search across the
    files uploaded by the app/agent developer. It has presets to
    give relatively good quality search over the uploaded files and
    summarization of the retrieved results.

    Attributes:
        corpus_type (google.cloud.ces_v1beta.types.FileSearchTool.CorpusType):
            Optional. The type of the corpus. Default is FULLY_MANAGED.
        name (str):
            Required. The tool name.
        description (str):
            Optional. The tool description.
        file_corpus (str):
            Optional. The corpus where files are stored. Format:
            projects/{project}/locations/{location}/ragCorpora/{rag_corpus}
    """

    class CorpusType(proto.Enum):
        r"""The type of the Vertex RAG corpus.

        Values:
            CORPUS_TYPE_UNSPECIFIED (0):
                Unspecified corpus type.
            USER_OWNED (1):
                The corpus is created and owned by the user.
            FULLY_MANAGED (2):
                The corpus is created by the agent.
        """

        CORPUS_TYPE_UNSPECIFIED = 0
        USER_OWNED = 1
        FULLY_MANAGED = 2

    corpus_type: CorpusType = proto.Field(
        proto.ENUM,
        number=3,
        enum=CorpusType,
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    file_corpus: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
