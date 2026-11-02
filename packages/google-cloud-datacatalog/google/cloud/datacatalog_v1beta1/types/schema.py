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
    package="google.cloud.datacatalog.v1beta1",
    manifest={
        "Schema",
        "ColumnSchema",
    },
)


class Schema(proto.Message):
    r"""Represents a schema (e.g. BigQuery, GoogleSQL, Avro schema).

    Attributes:
        columns (MutableSequence[google.cloud.datacatalog_v1beta1.types.ColumnSchema]):
            Required. Schema of columns. A maximum of
            10,000 columns and sub-columns can be specified.
    """

    columns: MutableSequence["ColumnSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ColumnSchema",
    )


class ColumnSchema(proto.Message):
    r"""Representation of a column within a schema. Columns could be
    nested inside other columns.

    Attributes:
        column (str):
            Required. Name of the column.
        type_ (str):
            Required. Type of the column.
        description (str):
            Optional. Description of the column. Default
            value is an empty string.
        mode (str):
            Optional. A column's mode indicates whether the values in
            this column are required, nullable, etc. Only ``NULLABLE``,
            ``REQUIRED`` and ``REPEATED`` are supported. Default mode is
            ``NULLABLE``.
        subcolumns (MutableSequence[google.cloud.datacatalog_v1beta1.types.ColumnSchema]):
            Optional. Schema of sub-columns. A column can
            have zero or more sub-columns.
    """

    column: str = proto.Field(
        proto.STRING,
        number=6,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mode: str = proto.Field(
        proto.STRING,
        number=3,
    )
    subcolumns: MutableSequence["ColumnSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ColumnSchema",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
