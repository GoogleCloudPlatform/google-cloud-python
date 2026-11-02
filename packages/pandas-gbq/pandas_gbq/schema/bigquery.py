# Copyright (c) 2019 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import collections

import google.cloud.bigquery


def to_schema_fields(schema):
    """Coerce `schema` to a list of schema field instances.

    Args:
        schema(Sequence[Union[ \
            :class:`~google.cloud.bigquery.schema.SchemaField`, \
            Mapping[str, Any] \
        ]]):
            Table schema to convert. If some items are passed as mappings,
            their content must be compatible with
            :meth:`~google.cloud.bigquery.schema.SchemaField.from_api_repr`.

    Returns:
        Sequence[:class:`~google.cloud.bigquery.schema.SchemaField`]

    Raises:
        Exception: If ``schema`` is not a sequence, or if any item in the
        sequence is not a :class:`~google.cloud.bigquery.schema.SchemaField`
        instance or a compatible mapping representation of the field.
    """
    for field in schema:
        if not isinstance(
            field, (google.cloud.bigquery.SchemaField, collections.abc.Mapping)
        ):
            raise ValueError(
                "Schema items must either be fields or compatible "
                "mapping representations."
            )

    return [
        field
        if isinstance(field, google.cloud.bigquery.SchemaField)
        else google.cloud.bigquery.SchemaField.from_api_repr(field)
        for field in schema
    ]
