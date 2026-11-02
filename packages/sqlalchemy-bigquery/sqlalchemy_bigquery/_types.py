# Copyright (c) 2021 The sqlalchemy-bigquery Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sqlalchemy.types
import sqlalchemy.util
from google.cloud.bigquery.schema import SchemaField

try:
    from .geography import GEOGRAPHY
except ImportError:  # pragma: NO COVER
    pass

from ._struct import STRUCT

_type_map = {
    "ARRAY": sqlalchemy.types.ARRAY,
    "BIGNUMERIC": sqlalchemy.types.Numeric,
    "BOOLEAN": sqlalchemy.types.Boolean,
    "BOOL": sqlalchemy.types.Boolean,
    "BYTES": sqlalchemy.types.BINARY,
    "DATETIME": sqlalchemy.types.DATETIME,
    "DATE": sqlalchemy.types.DATE,
    "FLOAT64": sqlalchemy.types.Float,
    "FLOAT": sqlalchemy.types.Float,
    "INT64": sqlalchemy.types.Integer,
    "INTEGER": sqlalchemy.types.Integer,
    "NUMERIC": sqlalchemy.types.Numeric,
    "RECORD": STRUCT,
    "STRING": sqlalchemy.types.String,
    "STRUCT": STRUCT,
    "TIMESTAMP": sqlalchemy.types.TIMESTAMP,
    "TIME": sqlalchemy.types.TIME,
}

# By convention, dialect-provided types are spelled with all upper case.
ARRAY = _type_map["ARRAY"]
BIGNUMERIC = _type_map["NUMERIC"]
BOOLEAN = _type_map["BOOLEAN"]
BOOL = _type_map["BOOL"]
BYTES = _type_map["BYTES"]
DATETIME = _type_map["DATETIME"]
DATE = _type_map["DATE"]
FLOAT64 = _type_map["FLOAT64"]
FLOAT = _type_map["FLOAT"]
INT64 = _type_map["INT64"]
INTEGER = _type_map["INTEGER"]
NUMERIC = _type_map["NUMERIC"]
RECORD = _type_map["RECORD"]
STRING = _type_map["STRING"]
TIMESTAMP = _type_map["TIMESTAMP"]
TIME = _type_map["TIME"]

try:
    _type_map["GEOGRAPHY"] = GEOGRAPHY
except NameError:  # pragma: NO COVER
    pass

STRUCT_FIELD_TYPES = "RECORD", "STRUCT"


def _get_transitive_schema_fields(fields):
    """
    Recurse into record type and return all the nested field names.
    As contributed by @sumedhsakdeo on issue #17
    """
    results = []
    for field in fields:
        results += [field]
        if field.field_type in STRUCT_FIELD_TYPES and field.mode != "REPEATED":
            sub_fields = [
                SchemaField.from_api_repr(
                    dict(f.to_api_repr(), name=f"{field.name}.{f.name}")
                )
                for f in field.fields
            ]
            results += _get_transitive_schema_fields(sub_fields)
    return results


def _get_sqla_column_type(field):
    try:
        coltype = _type_map[field.field_type]
    except KeyError:
        sqlalchemy.util.warn(
            "Did not recognize type '%s' of column '%s'"
            % (field.field_type, field.name)
        )
        coltype = sqlalchemy.types.NullType
    else:
        if field.field_type.endswith("NUMERIC"):
            coltype = coltype(precision=field.precision, scale=field.scale)
        elif field.field_type == "STRING" or field.field_type == "BYTES":
            coltype = coltype(field.max_length)
        elif field.field_type == "RECORD" or field.field_type == "STRUCT":
            coltype = STRUCT(
                *(
                    (subfield.name, _get_sqla_column_type(subfield))
                    for subfield in field.fields
                )
            )
        else:
            coltype = coltype()

    if field.mode == "REPEATED":
        coltype = ARRAY(coltype)

    return coltype


def get_columns(bq_schema):
    fields = _get_transitive_schema_fields(bq_schema)
    return [
        {
            "name": field.name,
            "type": _get_sqla_column_type(field),
            "nullable": field.mode == "NULLABLE" or field.mode == "REPEATED",
            "comment": field.description,
            "default": None,
            "precision": field.precision,
            "scale": field.scale,
            "max_length": field.max_length,
        }
        for field in fields
    ]
