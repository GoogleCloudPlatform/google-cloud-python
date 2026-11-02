# Copyright (c) 2019 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import collections.abc
import datetime
import warnings
from typing import Any, Optional, Tuple

# db-dtypes does not have type hints nor stubs that mypy uses for type checking.
# Remove this comment and the ignore pragma upon completing:
# https://github.com/googleapis/google-cloud-python/issues/17045
import db_dtypes  # type: ignore[import-untyped]
import pandas
import pyarrow
from google.cloud.bigquery import schema

import pandas_gbq.core.pandas
import pandas_gbq.schema.bigquery
import pandas_gbq.schema.pyarrow_to_bigquery

try:
    # _BaseGeometry is used to detect shapely objects in `bq_to_arrow_array`
    from shapely.geometry.base import BaseGeometry as _BaseGeometry  # type: ignore
except ImportError:
    # No shapely, use NoneType for _BaseGeometry as a placeholder.
    _BaseGeometry = type(None)


# If you update this mapping, also update the table at
# `docs/source/writing.rst`.
_PANDAS_DTYPE_TO_BQ = {
    "bool": "BOOLEAN",
    "boolean": "BOOLEAN",
    "datetime64[ns, UTC]": "TIMESTAMP",
    "datetime64[us, UTC]": "TIMESTAMP",
    "datetime64[ns]": "DATETIME",
    "datetime64[us]": "DATETIME",
    "float32": "FLOAT",
    "float64": "FLOAT",
    "int8": "INTEGER",
    "int16": "INTEGER",
    "int32": "INTEGER",
    "int64": "INTEGER",
    "Int8": "INTEGER",
    "Int16": "INTEGER",
    "Int32": "INTEGER",
    "Int64": "INTEGER",
    "uint8": "INTEGER",
    "uint16": "INTEGER",
    "uint32": "INTEGER",
    "geometry": "GEOGRAPHY",
    db_dtypes.DateDtype.name: "DATE",
    db_dtypes.TimeDtype.name: "TIME",
    # TODO(tswast): Add support for JSON.
}


def dataframe_to_bigquery_fields(
    dataframe,
    override_bigquery_fields=None,
    default_type="STRING",
    index=False,
) -> Tuple[schema.SchemaField]:
    """Convert a pandas DataFrame schema to a BigQuery schema.

    Args:
        dataframe (pandas.DataFrame):
            DataFrame for which the client determines the BigQuery schema.
        override_bigquery_fields (Sequence[Union[ \
            :class:`~google.cloud.bigquery.schema.SchemaField`, \
            Mapping[str, Any] \
        ]]):
            A BigQuery schema. Use this argument to override the autodetected
            type for some or all of the DataFrame columns.

    Returns:
        Optional[Sequence[google.cloud.bigquery.schema.SchemaField]]:
            The automatically determined schema. Returns None if the type of
            any column cannot be determined.
    """
    if override_bigquery_fields:
        override_bigquery_fields = pandas_gbq.schema.bigquery.to_schema_fields(
            override_bigquery_fields
        )
        override_fields_by_name = {
            field.name: field for field in override_bigquery_fields
        }
        override_fields_unused = set(override_fields_by_name.keys())
    else:
        override_fields_by_name = {}
        override_fields_unused = set()

    bq_schema_out = []
    unknown_type_fields = []

    # TODO(tswast): Support index=True in to_gbq.
    for column, dtype in pandas_gbq.core.pandas.list_columns_and_indexes(
        dataframe, index=index
    ):
        # Use provided type from schema, if present.
        bq_field = override_fields_by_name.get(column)
        if bq_field:
            bq_schema_out.append(bq_field)
            override_fields_unused.discard(bq_field.name)
            continue

        # Try to automatically determine the type based on the pandas dtype.
        bq_field = dtype_to_bigquery_field(column, dtype)
        if bq_field:
            bq_schema_out.append(bq_field)
            continue

        # Try to automatically determine the type based on a few rows of the data.
        values = dataframe.reset_index()[column]
        bq_field = values_to_bigquery_field(column, values, default_type=default_type)

        if bq_field:
            bq_schema_out.append(bq_field)
            continue

        # Try to automatically determine the type based on the arrow conversion.
        try:
            arrow_value = pyarrow.array(values)
            bq_field = (
                pandas_gbq.schema.pyarrow_to_bigquery.arrow_type_to_bigquery_field(
                    column,
                    arrow_value.type,
                    default_type=default_type,
                )
            )

            if bq_field:
                bq_schema_out.append(bq_field)
                continue
        except pyarrow.lib.ArrowInvalid:
            # TODO(tswast): Better error message if conversion to arrow fails.
            pass

        # Unknown field type.
        bq_field = schema.SchemaField(column, default_type)
        bq_schema_out.append(bq_field)
        unknown_type_fields.append(bq_field)

    # Append any fields from the BigQuery schema that are not in the
    # DataFrame.
    if override_fields_unused:
        warnings.warn(
            "Provided BigQuery fields contain field(s) not present in "
            "DataFrame: {}".format(sorted(override_fields_unused)),
            UserWarning,
        )
        for field_name in sorted(override_fields_unused):
            bq_schema_out.append(override_fields_by_name[field_name])

    # If schema detection was not successful for all columns, also try with
    # pyarrow, if available.
    if unknown_type_fields:
        msg = "Could not determine the type of columns: {}".format(
            ", ".join(field.name for field in unknown_type_fields)
        )
        warnings.warn(msg)

    return tuple(bq_schema_out)


def dtype_to_bigquery_field(name, dtype) -> Optional[schema.SchemaField]:
    """Infers the BigQuery schema field type from a pandas dtype.

    Args:
        name (str):
            Name of the column/field.
        dtype:
            A pandas / numpy dtype object.

    Returns:
        Optional[schema.SchemaField]:
            The schema field, or None if a type cannot be inferred, such as if
            it is ambiguous like the object dtype.
    """
    bq_type = _PANDAS_DTYPE_TO_BQ.get(dtype.name)

    if bq_type is not None:
        return schema.SchemaField(name, bq_type)

    if hasattr(pandas, "ArrowDtype") and isinstance(dtype, pandas.ArrowDtype):
        return pandas_gbq.schema.pyarrow_to_bigquery.arrow_type_to_bigquery_field(
            name, dtype.pyarrow_dtype
        )

    return None


def value_to_bigquery_field(
    name: str, value: Any, default_type: Optional[str] = None
) -> Optional[schema.SchemaField]:
    """Infers the BigQuery schema field type from a single value.

    Args:
        name:
            The name of the field.
        value:
            The value to infer the type from. If None, the default type is used
            if available.
        default_type:
            The default field type.  Defaults to None.

    Returns:
        The schema field, or None if a type cannot be inferred.
    """

    # Set the SchemaField datatype to the given default_type if the value
    # being assessed is None.
    if value is None:
        return schema.SchemaField(name, default_type or "STRING")

    # Map from Python types to BigQuery types. This isn't super exhaustive
    # because we rely more on pyarrow, which can check more than one value to
    # determine the type.
    type_mapping = {
        str: "STRING",
    }

    # geopandas and shapely are optional dependencies, so only check if those
    # are installed.
    if _BaseGeometry is not None:
        type_mapping[_BaseGeometry] = "GEOGRAPHY"

    for type_, bq_type in type_mapping.items():
        if isinstance(value, type_):
            return schema.SchemaField(name, bq_type)

    # For timezone-naive datetimes, the later pyarrow conversion to try and
    # learn the type add a timezone to such datetimes, causing them to be
    # recognized as TIMESTAMP type. We thus additionally check the actual data
    # to see if we need to overrule that and choose DATETIME instead.
    #
    # See: https://github.com/googleapis/python-bigquery/issues/985
    # and https://github.com/googleapis/python-bigquery/pull/1061
    # and https://github.com/googleapis/python-bigquery-pandas/issues/450
    if isinstance(value, datetime.datetime):
        if value.tzinfo is not None:
            return schema.SchemaField(name, "TIMESTAMP")
        else:
            return schema.SchemaField(name, "DATETIME")

    return None


def values_to_bigquery_field(
    name: str, values: Any, default_type: str = "STRING"
) -> Optional[schema.SchemaField]:
    """Infers the BigQuery schema field type from a list of values.

    This function iterates through the given values to determine the
    corresponding schema field type.

    Args:
        name:
            The name of the field.
        values:
            An iterable of values to infer the type from. If all the values
            are None or the iterable is empty, the function returns None.
        default_type:
            The default field type to use if a specific type cannot be
            determined from the values. Defaults to "STRING".

    Returns:
        The schema field, or None if a type cannot be inferred.
    """
    value = pandas_gbq.core.pandas.first_valid(values)

    # All values came back as NULL, thus type not determinable by this method.
    # Return None so we can try other methods.
    if value is None:
        return None

    field = value_to_bigquery_field(name, value, default_type=default_type)
    if field:
        return field

    # Check plain ARRAY values here. Exclude mapping types to let STRUCT get
    # determined by pyarrow, which can examine more values to determine all
    # keys.
    if isinstance(value, collections.abc.Iterable) and not isinstance(
        value, collections.abc.Mapping
    ):
        # It could be that this value contains all None or is empty, so get the
        # first non-None value we can find.
        valid_item = pandas_gbq.core.pandas.first_array_valid(values)
        field = value_to_bigquery_field(name, valid_item, default_type=default_type)

        if field is not None:
            return schema.SchemaField(name, field.field_type, mode="REPEATED")

    return None
