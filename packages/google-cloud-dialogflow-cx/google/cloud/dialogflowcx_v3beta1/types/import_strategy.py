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
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "ImportStrategy",
    },
)


class ImportStrategy(proto.Enum):
    r"""Import strategies for the conflict resolution of resources
    (i.e. intents, entities, and webhooks) with identical display
    names during import operations.

    Values:
        IMPORT_STRATEGY_UNSPECIFIED (0):
            Unspecified. Treated as 'CREATE_NEW'.
        IMPORT_STRATEGY_CREATE_NEW (1):
            Create a new resource with a numeric suffix
            appended to the end of the existing display
            name.
        IMPORT_STRATEGY_REPLACE (2):
            Replace existing resource with incoming
            resource in the content to be imported.
        IMPORT_STRATEGY_KEEP (3):
            Keep existing resource and discard incoming
            resource in the content to be imported.
        IMPORT_STRATEGY_MERGE (4):
            Combine existing and incoming resources when
            a conflict is encountered.
        IMPORT_STRATEGY_THROW_ERROR (5):
            Throw error if a conflict is encountered.
    """

    IMPORT_STRATEGY_UNSPECIFIED = 0
    IMPORT_STRATEGY_CREATE_NEW = 1
    IMPORT_STRATEGY_REPLACE = 2
    IMPORT_STRATEGY_KEEP = 3
    IMPORT_STRATEGY_MERGE = 4
    IMPORT_STRATEGY_THROW_ERROR = 5


__all__ = tuple(sorted(__protobuf__.manifest))
