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
    package="google.cloud.bigquery.migration.v2",
    manifest={
        "AssessmentTaskDetails",
        "AssessmentFeatureHandle",
    },
)


class AssessmentTaskDetails(proto.Message):
    r"""Assessment task config.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        input_path (str):
            Required. The Cloud Storage path for
            assessment input files.
        output_dataset (str):
            Required. The BigQuery dataset for output.
        querylogs_path (str):
            Optional. An optional Cloud Storage path to
            write the query logs (which is then used as an
            input path on the translation task)
        data_source (str):
            Required. The data source or data warehouse
            type (eg: TERADATA/REDSHIFT) from which the
            input data is extracted.
        feature_handle (google.cloud.bigquery_migration_v2.types.AssessmentFeatureHandle):
            Optional. A collection of additional feature
            flags for this assessment.

            This field is a member of `oneof`_ ``_feature_handle``.
    """

    input_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_dataset: str = proto.Field(
        proto.STRING,
        number=2,
    )
    querylogs_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=4,
    )
    feature_handle: "AssessmentFeatureHandle" = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message="AssessmentFeatureHandle",
    )


class AssessmentFeatureHandle(proto.Message):
    r"""User-definable feature flags for assessment tasks.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        add_shareable_dataset (bool):
            Optional. Whether to create a dataset
            containing non-PII data in addition to the
            output dataset.

            This field is a member of `oneof`_ ``_add_shareable_dataset``.
    """

    add_shareable_dataset: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
