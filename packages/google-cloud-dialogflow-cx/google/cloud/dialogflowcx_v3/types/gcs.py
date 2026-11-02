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
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "GcsDestination",
    },
)


class GcsDestination(proto.Message):
    r"""Google Cloud Storage location for a Dialogflow operation that
    writes or exports objects (e.g. exported agent or transcripts)
    outside of Dialogflow.

    Attributes:
        uri (str):
            Required. The Google Cloud Storage URI for the exported
            objects. A URI is of the form:
            ``gs://bucket/object-name-or-prefix`` Whether a full object
            name, or just a prefix, its usage depends on the Dialogflow
            operation.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
