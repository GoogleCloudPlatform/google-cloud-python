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

from google.cloud.firestore_v1.types import document

__protobuf__ = proto.module(
    package="google.firestore.v1",
    manifest={
        "StructuredPipeline",
    },
)


class StructuredPipeline(proto.Message):
    r"""A Firestore query represented as an ordered list of operations /
    stages.

    This is considered the top-level function which plans and executes a
    query. It is logically equivalent to ``query(stages, options)``, but
    prevents the client from having to build a function wrapper.

    Attributes:
        pipeline (google.cloud.firestore_v1.types.Pipeline):
            Required. The pipeline query to execute.
        options (MutableMapping[str, google.cloud.firestore_v1.types.Value]):
            Optional. Optional query-level arguments.
    """

    pipeline: document.Pipeline = proto.Field(
        proto.MESSAGE,
        number=1,
        message=document.Pipeline,
    )
    options: MutableMapping[str, document.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message=document.Value,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
