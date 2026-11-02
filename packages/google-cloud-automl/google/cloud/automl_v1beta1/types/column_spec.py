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

from google.cloud.automl_v1beta1.types import data_stats as gca_data_stats
from google.cloud.automl_v1beta1.types import data_types

__protobuf__ = proto.module(
    package="google.cloud.automl.v1beta1",
    manifest={
        "ColumnSpec",
    },
)


class ColumnSpec(proto.Message):
    r"""A representation of a column in a relational table. When listing
    them, column specs are returned in the same order in which they were
    given on import . Used by:

    - Tables

    Attributes:
        name (str):
            Output only. The resource name of the column specs. Form:

            ``projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/tableSpecs/{table_spec_id}/columnSpecs/{column_spec_id}``
        data_type (google.cloud.automl_v1beta1.types.DataType):
            The data type of elements stored in the
            column.
        display_name (str):
            Output only. The name of the column to show in the
            interface. The name can be up to 100 characters long and can
            consist only of ASCII Latin letters A-Z and a-z, ASCII
            digits 0-9, underscores(\_), and forward slashes(/), and
            must start with a letter or a digit.
        data_stats (google.cloud.automl_v1beta1.types.DataStats):
            Output only. Stats of the series of values in the column.
            This field may be stale, see the ancestor's
            Dataset.tables_dataset_metadata.stats_update_time field for
            the timestamp at which these stats were last updated.
        top_correlated_columns (MutableSequence[google.cloud.automl_v1beta1.types.ColumnSpec.CorrelatedColumn]):
            Deprecated.
        etag (str):
            Used to perform consistent read-modify-write
            updates. If not set, a blind "overwrite" update
            happens.
    """

    class CorrelatedColumn(proto.Message):
        r"""Identifies the table's column, and its correlation with the
        column this ColumnSpec describes.

        Attributes:
            column_spec_id (str):
                The column_spec_id of the correlated column, which belongs
                to the same table as the in-context column.
            correlation_stats (google.cloud.automl_v1beta1.types.CorrelationStats):
                Correlation between this and the in-context
                column.
        """

        column_spec_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        correlation_stats: gca_data_stats.CorrelationStats = proto.Field(
            proto.MESSAGE,
            number=2,
            message=gca_data_stats.CorrelationStats,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_type: data_types.DataType = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_types.DataType,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    data_stats: gca_data_stats.DataStats = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gca_data_stats.DataStats,
    )
    top_correlated_columns: MutableSequence[CorrelatedColumn] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=CorrelatedColumn,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
