# Copyright (c) 2023 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

from typing import Optional, cast

import pyarrow
import pyarrow.types
from google.cloud.bigquery import schema

_ARROW_SCALAR_IDS_TO_BQ = {
    # https://arrow.apache.org/docs/python/api/datatypes.html#type-classes
    pyarrow.bool_().id: "BOOLEAN",
    pyarrow.int8().id: "INTEGER",
    pyarrow.int16().id: "INTEGER",
    pyarrow.int32().id: "INTEGER",
    pyarrow.int64().id: "INTEGER",
    pyarrow.uint8().id: "INTEGER",
    pyarrow.uint16().id: "INTEGER",
    pyarrow.uint32().id: "INTEGER",
    pyarrow.uint64().id: "INTEGER",
    pyarrow.float16().id: "FLOAT",
    pyarrow.float32().id: "FLOAT",
    pyarrow.float64().id: "FLOAT",
    pyarrow.time32("ms").id: "TIME",
    pyarrow.time64("ns").id: "TIME",
    pyarrow.timestamp("ns").id: "TIMESTAMP",
    pyarrow.date32().id: "DATE",
    pyarrow.date64().id: "DATETIME",  # because millisecond resolution
    pyarrow.binary().id: "BYTES",
    pyarrow.string().id: "STRING",  # also alias for pyarrow.utf8()
    pyarrow.large_string().id: "STRING",
    # The exact decimal's scale and precision are not important, as only
    # the type ID matters, and it's the same for all decimal256 instances.
    pyarrow.decimal128(38, scale=9).id: "NUMERIC",
    pyarrow.decimal256(76, scale=38).id: "BIGNUMERIC",
}


def arrow_type_to_bigquery_field(
    name, type_, default_type="STRING"
) -> Optional[schema.SchemaField]:
    """Infers the BigQuery schema field type from an arrow type.

    Args:
        name (str):
            Name of the column/field.
        type_:
            A pyarrow type object.

    Returns:
        Optional[schema.SchemaField]:
            The schema field, or None if a type cannot be inferred, such as if
            it is a type that doesn't have a clear mapping in BigQuery.

            null() are assumed to be the ``default_type``, since there are no
            values that contradict that.
    """
    # If a sub-field is the null type, then assume it's the default type, as
    # that's the best we can do.
    # https://github.com/googleapis/python-bigquery-pandas/issues/836
    if pyarrow.types.is_null(type_):
        return schema.SchemaField(name, default_type)

    # Since both TIMESTAMP/DATETIME use pyarrow.timestamp(...), we need to use
    # a special case to disambiguate them. See:
    # https://github.com/googleapis/python-bigquery-pandas/issues/450
    if pyarrow.types.is_timestamp(type_):
        if type_.tz is None:
            return schema.SchemaField(name, "DATETIME")
        else:
            return schema.SchemaField(name, "TIMESTAMP")

    detected_type = _ARROW_SCALAR_IDS_TO_BQ.get(type_.id, None)

    # We need a special case for values that might fit in Arrow decimal128 but
    # not with the scale/precision that is used in BigQuery's NUMERIC type.
    # See: https://github.com/googleapis/python-bigquery/issues/1650
    if detected_type == "NUMERIC" and type_.scale > 9:
        detected_type = "BIGNUMERIC"

    if detected_type is not None:
        return schema.SchemaField(name, detected_type)

    if pyarrow.types.is_list(type_):
        return arrow_list_type_to_bigquery(name, type_, default_type=default_type)

    if pyarrow.types.is_struct(type_):
        inner_fields: list[pyarrow.Field] = []
        struct_type = cast(pyarrow.StructType, type_)
        for field_index in range(struct_type.num_fields):
            field = struct_type[field_index]
            inner_fields.append(
                arrow_type_to_bigquery_field(
                    field.name, field.type, default_type=default_type
                )
            )

        return schema.SchemaField(name, "RECORD", fields=inner_fields)

    return None


def arrow_list_type_to_bigquery(
    name, type_, default_type="STRING"
) -> Optional[schema.SchemaField]:
    """Infers the BigQuery schema field type from an arrow list type.

    Args:
        name (str):
            Name of the column/field.
        type_:
            A pyarrow type object.

    Returns:
        Optional[schema.SchemaField]:
            The schema field, or None if a type cannot be inferred, such as if
            it is a type that doesn't have a clear mapping in BigQuery.

            null() are assumed to be the ``default_type``, since there are no
            values that contradict that.
    """
    inner_field = arrow_type_to_bigquery_field(
        name, type_.value_type, default_type=default_type
    )

    # If this is None, it means we got some type that we can't cleanly map to
    # a BigQuery type, so bubble that status up.
    if inner_field is None:
        return None

    return schema.SchemaField(
        name, inner_field.field_type, mode="REPEATED", fields=inner_field.fields
    )
