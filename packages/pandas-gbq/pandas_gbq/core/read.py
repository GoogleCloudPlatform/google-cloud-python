# Copyright (c) 2025 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

import typing
import warnings
from typing import Any, Dict, Optional, Sequence

import google.cloud.bigquery
import google.cloud.bigquery.table
import numpy as np

import pandas_gbq
import pandas_gbq.constants
import pandas_gbq.exceptions
import pandas_gbq.features
import pandas_gbq.timestamp

# Only import at module-level at type checking time to avoid circular
# dependencies in the pandas package, which has an optional dependency on
# pandas-gbq.
if typing.TYPE_CHECKING:  # pragma: NO COVER
    import pandas


def _bqschema_to_nullsafe_dtypes(schema_fields):
    """Specify explicit dtypes based on BigQuery schema.

    This function only specifies a dtype when the dtype allows nulls.
    Otherwise, use pandas's default dtype choice.

    See: http://pandas.pydata.org/pandas-docs/dev/missing_data.html
    #missing-data-casting-rules-and-indexing
    """
    # db-dtypes does not have type hints nor stubs that mypy uses for type checking.
    # Remove this comment and the ignore pragma upon completing:
    # https://github.com/googleapis/google-cloud-python/issues/17045
    import db_dtypes  # type: ignore[import-untyped]

    # If you update this mapping, also update the table at
    # `docs/reading.rst`.
    dtype_map = {
        "FLOAT": np.dtype(float),
        "INTEGER": "Int64",
        "TIME": db_dtypes.TimeDtype(),
        # Note: Other types such as 'datetime64[ns]' and db_types.DateDtype()
        # are not included because the pandas range does not align with the
        # BigQuery range. We need to attempt a conversion to those types and
        # fall back to 'object' when there are out-of-range values.
    }

    # Amend dtype_map with newer extension types if pandas version allows.
    if pandas_gbq.features.FEATURES.pandas_has_boolean_dtype:
        dtype_map["BOOLEAN"] = "boolean"

    dtypes = {}
    for field in schema_fields:
        name = str(field["name"])
        # Array BigQuery type is represented as an object column containing
        # list objects.
        if field["mode"].upper() == "REPEATED":
            dtypes[name] = "object"
            continue

        dtype = dtype_map.get(field["type"].upper())
        if dtype:
            dtypes[name] = dtype

    return dtypes


def _finalize_dtypes(
    df: pandas.DataFrame, schema_fields: Sequence[Dict[str, Any]]
) -> pandas.DataFrame:
    """
    Attempt to change the dtypes of those columns that don't map exactly.

    For example db_dtypes.DateDtype() and datetime64[ns] cannot represent
    0001-01-01, but they can represent dates within a couple hundred years of
    1970. See:
    https://github.com/googleapis/python-bigquery-pandas/issues/365
    """
    # db-dtypes does not have type hints nor stubs that mypy uses for type checking.
    # Remove this comment and the ignore pragma upon completing:
    # https://github.com/googleapis/google-cloud-python/issues/17045
    import db_dtypes  # type: ignore[import-untyped]
    import pandas.api.types

    # If you update this mapping, also update the table at
    # `docs/reading.rst`.
    dtype_map = {
        "DATE": db_dtypes.DateDtype(),
        "DATETIME": "datetime64[ns]",
        "TIMESTAMP": "datetime64[ns]",
    }

    for field in schema_fields:
        # This method doesn't modify ARRAY/REPEATED columns.
        if field["mode"].upper() == "REPEATED":
            continue

        name = str(field["name"])
        dtype = dtype_map.get(field["type"].upper())

        # Avoid deprecated conversion to timezone-naive dtype by only casting
        # object dtypes.
        if dtype and pandas.api.types.is_object_dtype(df[name]):
            df[name] = df[name].astype(dtype, errors="ignore")

    # Ensure any TIMESTAMP columns are tz-aware.
    df = pandas_gbq.timestamp.localize_df(df, schema_fields)

    return df


def download_results(
    results: google.cloud.bigquery.table.RowIterator,
    *,
    bqclient: google.cloud.bigquery.Client,
    progress_bar_type: Optional[str],
    warn_on_large_results: bool = True,
    max_results: Optional[int],
    user_dtypes: Optional[dict],
    use_bqstorage_api: bool,
) -> Optional[pandas.DataFrame]:
    # No results are desired, so don't bother downloading anything.
    if max_results == 0:
        return None

    if user_dtypes is None:
        user_dtypes = {}

    create_bqstorage_client = use_bqstorage_api
    if max_results is not None:
        create_bqstorage_client = False

    # If we're downloading a large table, BigQuery DataFrames might be a
    # better fit. Not all code paths will populate rows_iter._table, but
    # if it's not populated that means we are working with a small result
    # set.
    if (
        warn_on_large_results
        and (table_ref := getattr(results, "_table", None)) is not None
    ):
        table = bqclient.get_table(table_ref)
        if (
            isinstance((num_bytes := table.num_bytes), int)
            and num_bytes > pandas_gbq.constants.BYTES_TO_RECOMMEND_BIGFRAMES
        ):
            num_gib = num_bytes / pandas_gbq.constants.BYTES_IN_GIB
            warnings.warn(
                f"Recommendation: Your results are {num_gib:.1f} GiB. "
                "Consider using BigQuery DataFrames (https://dataframes.bigquery.dev)"
                "to process large results with pandas compatible APIs with transparent SQL "
                "pushdown to BigQuery engine. This provides an opportunity to save on costs "
                "and improve performance. "
                "Please reach out to bigframes-feedback@google.com with any "
                "questions or concerns. To disable this message, run "
                "warnings.simplefilter('ignore', category=pandas_gbq.exceptions.LargeResultsWarning)",
                category=pandas_gbq.exceptions.LargeResultsWarning,
                # user's code
                # -> read_gbq
                # -> run_query
                # -> download_results
                stacklevel=4,
            )

    try:
        schema_fields = [field.to_api_repr() for field in results.schema]
        conversion_dtypes = _bqschema_to_nullsafe_dtypes(schema_fields)
        conversion_dtypes.update(user_dtypes)
        df = results.to_dataframe(
            dtypes=conversion_dtypes,
            progress_bar_type=progress_bar_type,
            create_bqstorage_client=create_bqstorage_client,
        )
    except pandas_gbq.constants.HTTP_ERRORS as ex:
        raise pandas_gbq.exceptions.translate_exception(ex) from ex

    df = _finalize_dtypes(df, schema_fields)

    pandas_gbq.logger.debug("Got {} rows.\n".format(results.total_rows))
    return df
