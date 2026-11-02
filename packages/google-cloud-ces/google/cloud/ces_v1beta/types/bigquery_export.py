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
        "BigQueryExportSettings",
    },
)


class BigQueryExportSettings(proto.Message):
    r"""Settings to describe the BigQuery export behaviors for the
    app.

    Attributes:
        enabled (bool):
            Optional. Indicates whether the BigQuery
            export is enabled.
        project (str):
            Optional. The **project ID** of the BigQuery dataset to
            export the data to.

            Note: If the BigQuery dataset is in a different project from
            the app, you should grant ``roles/bigquery.admin`` role to
            the CES service agent
            ``service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com``.
        dataset (str):
            Optional. The BigQuery **dataset ID** to export the data to.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dataset: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
