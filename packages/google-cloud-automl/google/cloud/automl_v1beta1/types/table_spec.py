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

from google.cloud.automl_v1beta1.types import io

__protobuf__ = proto.module(
    package="google.cloud.automl.v1beta1",
    manifest={
        "TableSpec",
    },
)


class TableSpec(proto.Message):
    r"""A specification of a relational table. The table's schema is
    represented via its child column specs. It is pre-populated as part
    of ImportData by schema inference algorithm, the version of which is
    a required parameter of ImportData InputConfig. Note: While working
    with a table, at times the schema may be inconsistent with the data
    in the table (e.g. string in a FLOAT64 column). The consistency
    validation is done upon creation of a model. Used by:

    - Tables

    Attributes:
        name (str):
            Output only. The resource name of the table spec. Form:

            ``projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/tableSpecs/{table_spec_id}``
        time_column_spec_id (str):
            column_spec_id of the time column. Only used if the parent
            dataset's ml_use_column_spec_id is not set. Used to split
            rows into TRAIN, VALIDATE and TEST sets such that oldest
            rows go to TRAIN set, newest to TEST, and those in between
            to VALIDATE. Required type: TIMESTAMP. If both this column
            and ml_use_column are not set, then ML use of all rows will
            be assigned by AutoML. NOTE: Updates of this field will
            instantly affect any other users concurrently working with
            the dataset.
        row_count (int):
            Output only. The number of rows (i.e.
            examples) in the table.
        valid_row_count (int):
            Output only. The number of valid rows (i.e.
            without values that don't match DataType-s of
            their columns).
        column_count (int):
            Output only. The number of columns of the
            table. That is, the number of child
            ColumnSpec-s.
        input_configs (MutableSequence[google.cloud.automl_v1beta1.types.InputConfig]):
            Output only. Input configs via which data
            currently residing in the table had been
            imported.
        etag (str):
            Used to perform consistent read-modify-write
            updates. If not set, a blind "overwrite" update
            happens.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    time_column_spec_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    row_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    valid_row_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    column_count: int = proto.Field(
        proto.INT64,
        number=7,
    )
    input_configs: MutableSequence[io.InputConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=io.InputConfig,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
