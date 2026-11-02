# Copyright (c) 2026 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

import typing
from typing import Optional, Sequence, Union

import google.cloud.bigquery
import google.cloud.bigquery.table
import google.oauth2.credentials
import psutil

import pandas_gbq.constants
import pandas_gbq.core.biglake
import pandas_gbq.core.read
import pandas_gbq.core.resource_references
import pandas_gbq.gbq_connector

# Only import at module-level at type checking time to avoid circular
# dependencies in the pandas package, which has an optional dependency on
# pandas-gbq.
if typing.TYPE_CHECKING:  # pragma: NO COVER
    import pandas


_READ_API_ELIGIBLE_TYPES = ("TABLE", "MATERIALIZED_VIEW", "EXTERNAL")
_TABLESAMPLE_ELIGIBLE_TYPES = ("TABLE", "EXTERNAL")

# Base logical sizes for non-complex and non-variable types.
# https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#data_type_sizes
_TYPE_SIZES = {
    # Fixed size types
    "BOOL": 1,
    "DATE": 8,
    "DATETIME": 8,
    "FLOAT64": 8,
    "INT64": 8,
    "TIME": 8,
    "TIMESTAMP": 8,
    "INTERVAL": 16,
    "NUMERIC": 16,
    "RANGE": 16,
    "BIGNUMERIC": 32,
    # Variable types with a fixed-size assumption
    "STRING": pandas_gbq.constants.BYTES_IN_KIB,
    "JSON": pandas_gbq.constants.BYTES_IN_KIB,
    "BYTES": pandas_gbq.constants.BYTES_IN_MIB,
    # Formula: 16 logical bytes + 24 logical bytes * num_vertices
    # Assuming a small, fixed number of vertices (e.g., 5) for estimation:
    "GEOGRAPHY": 16 + (24 * 5),
}
# TODO(tswast): Choose an estimate based on actual BigQuery stats.
_ARRAY_LENGTH_ESTIMATE = 5
_UNKNOWN_TYPE_SIZE_ESTIMATE = 4
_MAX_AUTO_TARGET_BYTES = 1 * pandas_gbq.constants.BYTES_IN_GIB


def _calculate_target_bytes(target_mb: Optional[int]) -> int:
    if target_mb is not None:
        return target_mb * pandas_gbq.constants.BYTES_IN_MIB

    mem = psutil.virtual_memory()
    return min(_MAX_AUTO_TARGET_BYTES, mem.available // 4)


def _estimate_limit(
    *,
    fields: Sequence[google.cloud.bigquery.SchemaField],
    target_bytes: int,
    table_bytes: Optional[int] = None,
    table_rows: Optional[int] = None,
) -> int:
    if table_bytes and table_rows:
        proportion = target_bytes / table_bytes
        return max(1, int(table_rows * proportion))

    row_bytes_estimate = _estimate_row_bytes(fields)
    assert row_bytes_estimate >= 0

    if row_bytes_estimate == 0:
        # Assume there's some overhead per row so we have some kind of limit.
        return target_bytes

    return max(1, target_bytes // row_bytes_estimate)


def _estimate_field_bytes(field: google.cloud.bigquery.SchemaField) -> int:
    """Recursive helper function to calculate the size of a single field."""
    field_type = field.field_type

    # If the field is REPEATED (ARRAY), its size is the sum of its elements.
    if field.mode == "REPEATED":
        # Create a temporary single-element field for size calculation
        temp_field = google.cloud.bigquery.SchemaField(
            field.name, field.field_type, mode="NULLABLE", fields=field.fields
        )
        element_size = _estimate_field_bytes(temp_field)
        return _ARRAY_LENGTH_ESTIMATE * element_size

    if field_type == "STRUCT" or field_type == "RECORD":
        # STRUCT has 0 logical bytes + the size of its contained fields.
        return _estimate_row_bytes(field.fields)

    return _TYPE_SIZES.get(field_type.upper(), _UNKNOWN_TYPE_SIZE_ESTIMATE)


def _estimate_row_bytes(fields: Sequence[google.cloud.bigquery.SchemaField]) -> int:
    """
    Estimates the logical row size in bytes for a list of BigQuery SchemaField objects,
    using the provided data type size chart and assuming 1MB for all STRING and BYTES
    fields.

    Args:
        schema_fields: A list of google.cloud.bigquery.SchemaField objects
                       representing the table schema.

    Returns:
        An integer representing the estimated total row size in logical bytes.
    """
    total_size = max(
        1,
        sum(_estimate_field_bytes(field) for field in fields),
    )
    return total_size


def _download_results_in_parallel(
    rows: google.cloud.bigquery.table.RowIterator,
    *,
    bqclient: google.cloud.bigquery.Client,
    progress_bar_type: Union[str, None] = None,
    use_bqstorage_api: bool = True,
):
    table_reference = getattr(rows, "_table", None)
    schema = getattr(rows, "_schema", None)

    # If the results are large enough to materialize a table, break the
    # connection to the original query that contains an ORDER BY clause to allow
    # reading with multiple streams.
    if table_reference is not None and schema is not None:
        rows = bqclient.list_rows(
            table_reference,
            selected_fields=schema,
        )

    return pandas_gbq.core.read.download_results(
        rows,
        bqclient=bqclient,
        progress_bar_type=progress_bar_type,
        warn_on_large_results=False,
        max_results=None,
        user_dtypes=None,
        use_bqstorage_api=use_bqstorage_api,
    )


def _sample_with_tablesample(
    table_id: str,
    *,
    bqclient: google.cloud.bigquery.Client,
    proportion: float,
    target_row_count: int,
    progress_bar_type: Union[str, None] = None,
    use_bqstorage_api: bool = True,
) -> Optional[pandas.DataFrame]:
    sample_percent = min(100, max(1, int(proportion * 100)))
    query = f"""
    SELECT *
    FROM `{table_id}` t
    TABLESAMPLE SYSTEM ({sample_percent} PERCENT)
    ORDER BY RAND() DESC
    LIMIT {int(target_row_count)};
    """
    rows = bqclient.query_and_wait(query)
    return _download_results_in_parallel(
        rows,
        bqclient=bqclient,
        progress_bar_type=progress_bar_type,
        use_bqstorage_api=use_bqstorage_api,
    )


def _sample_with_limit(
    table_id: str,
    *,
    bqclient: google.cloud.bigquery.Client,
    target_row_count: int,
    progress_bar_type: Union[str, None] = None,
    use_bqstorage_api: bool = True,
) -> Optional[pandas.DataFrame]:
    query = f"""
    SELECT *
    FROM `{table_id}`
    ORDER BY RAND() DESC
    LIMIT {int(target_row_count)};
    """
    rows = bqclient.query_and_wait(query)
    return _download_results_in_parallel(
        rows,
        bqclient=bqclient,
        progress_bar_type=progress_bar_type,
        use_bqstorage_api=use_bqstorage_api,
    )


def _sample_biglake_table(
    *,
    reference: pandas_gbq.core.resource_references.BigLakeTableId,
    bqclient: google.cloud.bigquery.Client,
    target_bytes: int,
    progress_bar_type: Union[str, None],
    use_bqstorage_api: bool,
) -> Optional[pandas.DataFrame]:
    metadata = pandas_gbq.core.biglake.get_table_metadata(
        reference=reference,
        bqclient=bqclient,
    )
    total_rows = metadata.num_rows

    # Avoid divide by 0 when calculating proportions.
    if total_rows == 0:
        total_rows = 1

    target_row_count = _estimate_limit(
        target_bytes=target_bytes,
        fields=metadata.schema,
        table_rows=total_rows,
    )
    proportion = max(0.01, target_row_count / total_rows)

    # BigLake tables should always support table sample, since they are backed
    # by parquet files.
    return _sample_with_tablesample(
        f"{reference.project}.{reference.catalog}.{'.'.join(reference.namespace)}.{reference.table}",
        bqclient=bqclient,
        proportion=proportion,
        target_row_count=target_row_count,
        progress_bar_type=progress_bar_type,
        use_bqstorage_api=use_bqstorage_api,
    )


def _sample_bq_table(
    *,
    reference: pandas_gbq.core.resource_references.BigQueryTableId,
    bqclient: google.cloud.bigquery.Client,
    target_bytes: int,
    progress_bar_type: Union[str, None],
    use_bqstorage_api: bool,
) -> Optional[pandas.DataFrame]:
    table = bqclient.get_table(
        google.cloud.bigquery.TableReference(
            google.cloud.bigquery.DatasetReference(
                reference.project_id, reference.dataset_id
            ),
            reference.table_id,
        )
    )
    num_rows = table.num_rows
    num_bytes = table.num_bytes
    table_type = table.table_type

    # Some tables such as views report 0 despite actually having rows.
    if num_bytes == 0:
        num_bytes = None

    # Table is small enough to download the whole thing.
    if (
        table_type in _READ_API_ELIGIBLE_TYPES
        and num_bytes is not None
        and num_bytes <= target_bytes
    ):
        rows_iter = bqclient.list_rows(table)
        return pandas_gbq.core.read.download_results(
            rows_iter,
            bqclient=bqclient,
            progress_bar_type=progress_bar_type,
            warn_on_large_results=False,
            max_results=None,
            user_dtypes=None,
            use_bqstorage_api=use_bqstorage_api,
        )

    target_row_count = _estimate_limit(
        target_bytes=target_bytes,
        table_bytes=num_bytes,
        table_rows=num_rows,
        fields=table.schema,
    )

    # Table is eligible for TABLESAMPLE.
    if num_bytes is not None and table_type in _TABLESAMPLE_ELIGIBLE_TYPES:
        proportion = target_bytes / num_bytes
        return _sample_with_tablesample(
            f"{table.project}.{table.dataset_id}.{table.table_id}",
            bqclient=bqclient,
            proportion=proportion,
            target_row_count=target_row_count,
            progress_bar_type=progress_bar_type,
            use_bqstorage_api=use_bqstorage_api,
        )

    # Not eligible for TABLESAMPLE or reading directly, so take a random sample
    # with a full table scan.
    return _sample_with_limit(
        f"{table.project}.{table.dataset_id}.{table.table_id}",
        bqclient=bqclient,
        target_row_count=target_row_count,
        progress_bar_type=progress_bar_type,
        use_bqstorage_api=use_bqstorage_api,
    )


def sample(
    table_id: str,
    *,
    target_mb: Optional[int] = None,
    credentials: Optional[google.oauth2.credentials.Credentials] = None,
    billing_project_id: Optional[str] = None,
    progress_bar_type: Union[str, None] = None,
    use_bqstorage_api: bool = True,
) -> Optional[pandas.DataFrame]:
    """Sample a BigQuery table, attempting to limit the amount of data read.

    This function attempts to sample a BigQuery table to a target size in
    memory. It prioritizes methods that minimize data scanned and downloaded.

    The target size is based on an estimate of the row size and this method
    return more or less than expected. If the table metadata doesn't include
    a size, such as with views, an estimate based on the table schema is
    used.

    Sampling is based on the `BigQuery TABLESAMPLE
    <https://docs.cloud.google.com/bigquery/docs/table-sampling>`_ feature,
    which can provide a biased sample if data is not randomly distributed
    among file blocks. For more control over sampling, use BigQuery
    DataFrames ``read_gbq_table`` and ``DataFrame.sample`` methods.

    Specificially, the sampling strategy is as follows:

    1. If the table is small enough (based on `target_mb` or available memory)
       and eligible for the BigQuery Storage Read API, the entire table is
       downloaded.
    2. If the table is larger than the target size and eligible for
       `TABLESAMPLE SYSTEM` (e.g., a regular table), a `TABLESAMPLE` query
       is used to retrieve a proportion of rows, followed by `ORDER BY RAND()`
       and `LIMIT` to get the `target_row_count`.
    3. If `TABLESAMPLE` is not applicable (e.g., for views) or `num_bytes` is
       not available, a full table scan is performed with `ORDER BY RAND()`
       and `LIMIT` to retrieve the `target_row_count`.

    Args:
        table_id: The BigQuery table ID to sample, in the format
            "project.dataset.table" or "dataset.table".
        target_mb: Optional. The target size in megabytes for the sampled
            DataFrame. If not specified, it defaults to 1/4 of available
            system memory, with a minimum of 100MB and maximum of 1 GB.
        credentials: Optional. The credentials to use for BigQuery access.
            If not provided, `pandas_gbq` will attempt to infer them.
        billing_project_id: Optional. The ID of the Google Cloud project to
            bill for the BigQuery job. If not provided, `pandas_gbq` will
            attempt to infer it.
        progress_bar_type: Optional. Type of progress bar to display.
            See `pandas_gbq.core.read.download_results` for options.
        use_bqstorage_api: Optional. If `True`, use the BigQuery Storage Read
            API for faster downloads. Defaults to `True`.

    Returns:
        A `pandas.DataFrame` containing the sampled data, or `None` if no data
        could be sampled.
    """
    target_bytes = _calculate_target_bytes(target_mb)
    connector = pandas_gbq.gbq_connector.GbqConnector(
        project_id=billing_project_id, credentials=credentials
    )
    bqclient = connector.get_client()

    # BigLake tables can't be read directly by the BQ Storage Read API, so make
    # sure we run a query first.
    reference = pandas_gbq.core.resource_references.parse_table_id(table_id)
    if isinstance(reference, pandas_gbq.core.resource_references.BigLakeTableId):
        return _sample_biglake_table(
            reference=reference,
            bqclient=bqclient,
            target_bytes=target_bytes,
            progress_bar_type=progress_bar_type,
            use_bqstorage_api=use_bqstorage_api,
        )
    else:
        return _sample_bq_table(
            reference=reference,
            bqclient=bqclient,
            target_bytes=target_bytes,
            progress_bar_type=progress_bar_type,
            use_bqstorage_api=use_bqstorage_api,
        )
