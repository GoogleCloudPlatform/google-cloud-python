# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Helper methods for loading data into BigQuery"""

import decimal
import io
from typing import Any, Callable, Dict, List, Optional

# db-dtypes does not have type hints nor stubs that mypy uses for type checking.
# Remove this comment and the ignore pragma upon completing:
# https://github.com/googleapis/google-cloud-python/issues/17045
import db_dtypes  # type: ignore[import-untyped]
import pandas
import pyarrow.lib
from google.cloud import bigquery

import pandas_gbq.schema
import pandas_gbq.schema.bigquery
import pandas_gbq.schema.pandas_to_bigquery
from pandas_gbq import exceptions


def encode_chunk(dataframe):
    """Return a file-like object of CSV-encoded rows.

    Args:
      dataframe (pandas.DataFrame): A chunk of a dataframe to encode
    """
    csv_buffer = io.StringIO()
    dataframe.to_csv(
        csv_buffer,
        index=False,
        header=False,
        encoding="utf-8",
        float_format="%.17g",
        date_format="%Y-%m-%d %H:%M:%S.%f",
    )

    # Convert to a BytesIO buffer so that unicode text is properly handled.
    # See: https://github.com/pydata/pandas-gbq/issues/106
    body = csv_buffer.getvalue()
    body_bytes = body.encode("utf-8")
    return io.BytesIO(body_bytes)


def split_dataframe(dataframe, chunksize=None):
    dataframe = dataframe.reset_index(drop=True)
    if chunksize is None:
        yield 0, dataframe
        return

    remaining_rows = len(dataframe)
    total_rows = remaining_rows
    start_index = 0
    while start_index < total_rows:
        end_index = start_index + chunksize
        chunk = dataframe[start_index:end_index]
        start_index += chunksize
        remaining_rows = max(0, remaining_rows - chunksize)
        yield remaining_rows, chunk


def cast_dataframe_for_parquet(
    dataframe: pandas.DataFrame,
    schema: Optional[Dict[str, Any]],
) -> pandas.DataFrame:
    """Cast columns to needed dtype when writing parquet files.

    See: https://github.com/googleapis/python-bigquery-pandas/issues/421
    """

    columns = schema.get("fields", []) if schema is not None else []

    # Protect against an explicit None in the dictionary.
    columns = columns if columns is not None else []

    for column in columns:
        # Schema can be a superset of the columns in the dataframe, so ignore
        # columns that aren't present.
        column_name = column.get("name")
        if column_name not in dataframe.columns:
            continue

        # Skip array columns for now. Potentially casting the elements of the
        # array would be possible, but not worth the effort until there is
        # demand for it.
        if column.get("mode", "NULLABLE").upper() == "REPEATED":
            continue

        column_type = column.get("type", "").upper()
        if (
            column_type == "DATE"
            # Use extension dtype first so that it uses the correct equality operator.
            and db_dtypes.DateDtype() != dataframe[column_name].dtype
        ):
            cast_column = dataframe[column_name].astype(
                dtype=db_dtypes.DateDtype(),
                # Return the original column if there was an error converting
                # to the dtype, such as is there is a date outside the
                # supported range.
                # https://github.com/googleapis/python-bigquery-pandas/issues/441
                errors="ignore",
            )
        elif column_type in {"NUMERIC", "DECIMAL", "BIGNUMERIC", "BIGDECIMAL"}:
            # decimal.Decimal does not support `None` or `pandas.NA` input, add
            # support here.
            # https://github.com/googleapis/python-bigquery-pandas/issues/719
            def convert(x):
                if pandas.isna(x):  # true for `None` and `pandas.NA`
                    return decimal.Decimal("NaN")
                else:
                    return decimal.Decimal(x)

            cast_column = dataframe[column_name].map(convert)
        elif column_type == "STRING":
            # Allow non-string columns to be uploaded to STRING in BigQuery.
            # https://github.com/googleapis/python-bigquery-pandas/issues/875
            # TODO: Use pyarrow as the storage when the minimum pandas version allows for it.
            cast_column = dataframe[column_name].astype(pandas.StringDtype())
        else:
            cast_column = None

        if cast_column is not None:
            dataframe = dataframe.assign(**{column_name: cast_column})
    return dataframe


def cast_dataframe_for_csv(
    dataframe: pandas.DataFrame,
    schema: Optional[Dict[str, Any]],
) -> pandas.DataFrame:
    """Cast columns to needed dtype when writing CSV files."""

    columns = schema.get("fields", []) if schema is not None else []

    # Protect against an explicit None in the dictionary.
    columns = columns if columns is not None else []

    new_columns = {}
    for column in columns:
        # Schema can be a superset of the columns in the dataframe, so ignore
        # columns that aren't present.
        column_name = column.get("name")
        if column_name not in dataframe.columns:
            continue

        column_type = column.get("type", "").upper()
        if column_type in {"DATETIME", "TIMESTAMP"}:
            # Use isoformat to ensure that the years are 4 digits.
            # https://github.com/googleapis/python-bigquery-pandas/issues/365
            def convert(x):
                if pandas.isna(x):
                    return None
                try:
                    return x.isoformat(sep=" ")
                except AttributeError:
                    # It might be a string already or some other type.
                    return x

            new_columns[column_name] = dataframe[column_name].map(convert)

    if new_columns:
        dataframe = dataframe.assign(**new_columns)
    return dataframe


def load_parquet(
    client: bigquery.Client,
    dataframe: pandas.DataFrame,
    destination_table_ref: bigquery.TableReference,
    write_disposition: str,
    location: Optional[str],
    schema: Optional[Dict[str, Any]],
    billing_project: Optional[str] = None,
):
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = write_disposition
    job_config.source_format = "PARQUET"

    if schema is not None:
        schema = pandas_gbq.schema.remove_policy_tags(schema)
        job_config.schema = pandas_gbq.schema.to_google_cloud_bigquery(schema)
        dataframe = cast_dataframe_for_parquet(dataframe, schema)

    try:
        client.load_table_from_dataframe(
            dataframe,
            destination_table_ref,
            job_config=job_config,
            location=location,
            project=billing_project,
        ).result()
    except pyarrow.lib.ArrowInvalid as exc:
        raise exceptions.ConversionError(
            "Could not convert DataFrame to Parquet."
        ) from exc


def load_csv(
    dataframe: pandas.DataFrame,
    write_disposition: str,
    chunksize: Optional[int],
    bq_schema: Optional[List[bigquery.SchemaField]],
    load_chunk: Callable,
):
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = write_disposition
    job_config.source_format = "CSV"
    job_config.allow_quoted_newlines = True

    if bq_schema is not None:
        job_config.schema = bq_schema

    # TODO: Remove chunking feature for load jobs. Deprecated in 0.16.0.
    chunks = split_dataframe(dataframe, chunksize=chunksize)
    for remaining_rows, chunk in chunks:
        yield remaining_rows
        load_chunk(chunk, job_config)


def load_csv_from_dataframe(
    client: bigquery.Client,
    dataframe: pandas.DataFrame,
    destination_table_ref: bigquery.TableReference,
    write_disposition: str,
    location: Optional[str],
    chunksize: Optional[int],
    schema: Optional[Dict[str, Any]],
    billing_project: Optional[str] = None,
):
    bq_schema = None

    if schema is not None:
        schema = pandas_gbq.schema.remove_policy_tags(schema)
        bq_schema = pandas_gbq.schema.to_google_cloud_bigquery(schema)

    def load_chunk(chunk, job_config):
        if schema is not None:
            chunk = cast_dataframe_for_csv(chunk, schema)

        client.load_table_from_dataframe(
            chunk,
            destination_table_ref,
            job_config=job_config,
            location=location,
            project=billing_project,
        ).result()

    return load_csv(dataframe, write_disposition, chunksize, bq_schema, load_chunk)


def load_csv_from_file(
    client: bigquery.Client,
    dataframe: pandas.DataFrame,
    destination_table_ref: bigquery.TableReference,
    write_disposition: str,
    location: Optional[str],
    chunksize: Optional[int],
    schema: Optional[Dict[str, Any]],
    billing_project: Optional[str] = None,
):
    """Manually encode a DataFrame to CSV and use the buffer in a load job.

    This method is needed for writing with google-cloud-bigquery versions that
    don't implment load_table_from_dataframe with the CSV serialization format.
    """
    bq_schema = pandas_gbq.schema.pandas_to_bigquery.dataframe_to_bigquery_fields(
        dataframe, schema
    )

    def load_chunk(chunk, job_config):
        try:
            chunk_buffer = encode_chunk(chunk)
            client.load_table_from_file(
                chunk_buffer,
                destination_table_ref,
                job_config=job_config,
                location=location,
                project=billing_project,
            ).result()
        finally:
            chunk_buffer.close()

    return load_csv(
        dataframe, write_disposition, chunksize, list(bq_schema), load_chunk
    )


def load_chunks(
    client,
    dataframe,
    destination_table_ref,
    chunksize=None,
    schema=None,
    location=None,
    api_method="load_parquet",
    write_disposition="WRITE_EMPTY",
    billing_project: Optional[str] = None,
):
    if api_method == "load_parquet":
        load_parquet(
            client,
            dataframe,
            destination_table_ref,
            write_disposition,
            location,
            schema,
            billing_project=billing_project,
        )
        # TODO: yield progress depending on result() with timeout
        return [0]
    elif api_method == "load_csv":
        return load_csv_from_dataframe(
            client,
            dataframe,
            destination_table_ref,
            write_disposition,
            location,
            chunksize,
            schema,
            billing_project=billing_project,
        )
    else:
        raise ValueError(
            f"Got unexpected api_method: {api_method!r}, expected one of 'load_parquet', 'load_csv'."
        )
