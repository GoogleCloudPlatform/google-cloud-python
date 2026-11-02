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
        "BigQueryExportSettings",
    },
)


class BigQueryExportSettings(proto.Message):
    r"""The settings of BigQuery export.

    Attributes:
        enabled (bool):
            The field to indicate whether the BigQuery
            export is enabled.
        bigquery_table (str):
            The BigQuery table to export. Format:
            ``projects/<ProjectID>/datasets/<DatasetID>/tables/<TableID>``.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    bigquery_table: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
