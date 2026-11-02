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
    package="google.cloud.alloydb.v1alpha",
    manifest={
        "SqlResult",
        "SqlResultColumn",
        "SqlResultRow",
        "SqlResultValue",
    },
)


class SqlResult(proto.Message):
    r"""SqlResult represents the result for the execution of a sql
    statement.

    Attributes:
        columns (MutableSequence[google.cloud.alloydb_v1alpha.types.SqlResultColumn]):
            List of columns included in the result. This
            also includes the data type of the column.
        rows (MutableSequence[google.cloud.alloydb_v1alpha.types.SqlResultRow]):
            Rows returned by the SQL statement.
    """

    columns: MutableSequence["SqlResultColumn"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SqlResultColumn",
    )
    rows: MutableSequence["SqlResultRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SqlResultRow",
    )


class SqlResultColumn(proto.Message):
    r"""Contains the name and datatype of a column in a SQL Result.

    Attributes:
        name (str):
            Name of the column.
        type_ (str):
            Datatype of the column as reported by the
            postgres driver. Common type names are
            "VARCHAR", "TEXT", "NVARCHAR", "DECIMAL",
            "BOOL", "INT", and "BIGINT".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SqlResultRow(proto.Message):
    r"""A single row from a sql result.

    Attributes:
        values (MutableSequence[google.cloud.alloydb_v1alpha.types.SqlResultValue]):
            List of values in a row of sql result.
    """

    values: MutableSequence["SqlResultValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SqlResultValue",
    )


class SqlResultValue(proto.Message):
    r"""A single value in a row from a sql result.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (str):
            The cell value represented in string format.
            Timestamps are converted to string using
            RFC3339Nano format.

            This field is a member of `oneof`_ ``_value``.
        null_value (bool):
            Set to true if cell value is null.

            This field is a member of `oneof`_ ``_null_value``.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    null_value: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
