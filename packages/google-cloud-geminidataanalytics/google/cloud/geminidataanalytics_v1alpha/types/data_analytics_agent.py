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

from google.cloud.geminidataanalytics_v1alpha.types import context

__protobuf__ = proto.module(
    package="google.cloud.geminidataanalytics.v1alpha",
    manifest={
        "DataAnalyticsAgent",
    },
)


class DataAnalyticsAgent(proto.Message):
    r"""Message describing a DataAnalyticsAgent object.

    Attributes:
        staging_context (google.cloud.geminidataanalytics_v1alpha.types.Context):
            Optional. The staging context for the agent.
            This context is used to test and validate
            changes before publishing.
        published_context (google.cloud.geminidataanalytics_v1alpha.types.Context):
            Optional. The published context for the
            agent. This context is used by the Chat API in
            production.
        last_published_context (google.cloud.geminidataanalytics_v1alpha.types.Context):
            Output only. The last published context for
            the agent. This is an output-only field
            populated by the system when the published
            context is updated. It is used to restore the
            agent to a previous state.
    """

    staging_context: context.Context = proto.Field(
        proto.MESSAGE,
        number=5,
        message=context.Context,
    )
    published_context: context.Context = proto.Field(
        proto.MESSAGE,
        number=6,
        message=context.Context,
    )
    last_published_context: context.Context = proto.Field(
        proto.MESSAGE,
        number=7,
        message=context.Context,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
