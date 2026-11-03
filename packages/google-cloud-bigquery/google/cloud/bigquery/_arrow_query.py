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

"""Read query results returned in Apache Arrow format."""

from __future__ import annotations

import base64
from typing import Any, Dict, Iterator, Optional, Sequence, Tuple, TYPE_CHECKING

from google.cloud.bigquery import _versions_helpers
from google.cloud.bigquery import enums
from google.cloud.bigquery import exceptions

try:
    import pyarrow  # type: ignore
except ImportError:
    pyarrow = None  # type: ignore[assignment]

if TYPE_CHECKING:  # pragma: NO COVER
    from google.cloud import bigquery_storage
    from google.cloud.bigquery.table import RowIterator

_NO_PYARROW_ERROR = (
    "The pyarrow library is not installed, please install "
    "pyarrow to use the to_arrow() function."
)

_NO_ARROW_SCHEMA_ERROR = "Got an Arrow record batch before its schema."


def validate_query(
    query_results_format: Optional[str],
    *,
    compression_codec: Optional[str] = None,
    timestamp_precision: Optional[enums.TimestampPrecision] = None,
) -> None:
    """Raise before sending a query whose ``ARROW`` results can't be read.

    Args:
        query_results_format: The ``query_results_format`` passed to
            ``query_and_wait()``.
        compression_codec: The ``compression_codec`` passed to
            ``query_and_wait()``.
        timestamp_precision: The ``timestamp_precision`` passed to
            ``query_and_wait()``.

    Raises:
        ValueError:
            If ``compression_codec`` or ``timestamp_precision`` is set
            without ``ARROW``.
        google.cloud.bigquery.exceptions.BigQueryError:
            If pyarrow or google-cloud-bigquery-storage is missing or too old
            to read ``ARROW`` results.
    """
    if query_results_format != enums.QueryResultsFormat.ARROW:
        if compression_codec is not None:
            raise ValueError("compression_codec requires query_results_format=ARROW.")
        if timestamp_precision is not None:
            raise ValueError("timestamp_precision requires query_results_format=ARROW.")
        return

    # Check before the query runs, so a query doesn't succeed while its
    # results fit in the first page and then fail once they need a stream.
    _check_dependencies()


def _check_dependencies() -> None:
    """Raise if pyarrow or google-cloud-bigquery-storage can't read ``ARROW``
    results."""
    _versions_helpers.PYARROW_VERSIONS.try_import(raise_if_error=True)
    _versions_helpers.BQ_STORAGE_VERSIONS.try_import(raise_if_error=True)
    if not _versions_helpers.BQ_STORAGE_VERSIONS.supports_arrow_serialization_options:
        raise exceptions.LegacyBigQueryStorageError(
            "query_results_format=ARROW needs a newer google-cloud-bigquery-storage, "
            "please upgrade it "
            '(`pip install "google-cloud-bigquery[bqstorage]"`) '
            "(version found: "
            f"{_versions_helpers.BQ_STORAGE_VERSIONS.installed_version})."
        )


def serialization_options(
    compression_codec: Optional[str],
    timestamp_precision: Optional[enums.TimestampPrecision] = None,
) -> Dict[str, str]:
    """Build the ``arrowSerializationOptions`` sent on ``jobs.query``.

    ``ReadRows`` gets the same options. Options the caller didn't set are sent
    with their defaults, so every batch uses one encoding, whatever each
    endpoint would default to.
    """
    return {
        "bufferCompression": getattr(compression_codec, "value", compression_codec)
        or "COMPRESSION_UNSPECIFIED",
        # Picosecond values come back as ISO 8601 strings at full precision,
        # so there's no need to offer nanoseconds.
        "picosTimestampPrecision": (
            "TIMESTAMP_PRECISION_PICOS"
            if timestamp_precision == enums.TimestampPrecision.PICOSECOND
            else "TIMESTAMP_PRECISION_MICROS"
        ),
    }


def reached_max_results(response: Dict[str, Any], max_results: Optional[int]) -> bool:
    """Return True if an ``ARROW`` ``jobs.query`` response's first page
    already holds ``max_results`` rows."""
    return (
        max_results is not None and int(response.get("pageRowCount", 0)) >= max_results
    )


def _slice_batch(
    batch: "pyarrow.RecordBatch", remaining: Optional[int]
) -> Tuple["pyarrow.RecordBatch", Optional[int]]:
    """Cut ``batch`` to at most ``remaining`` rows, and return it with the
    number of rows still wanted after it (``None`` for no limit)."""
    if remaining is None:
        return batch, None
    if batch.num_rows > remaining:
        batch = batch.slice(0, remaining)
    return batch, remaining - batch.num_rows


def _empty_batch(
    pa_schema: Optional["pyarrow.Schema"], bq_schema: Sequence[Any]
) -> "pyarrow.RecordBatch":
    """Build a batch without rows that keeps the result's schema.

    Use the Arrow schema BigQuery sent if there is one. The default job
    stream sends nothing for zero rows, so fall back to the schema from
    ``jobs.getQueryResults``, and else to no columns.
    """
    if pa_schema is None and bq_schema:
        # Imported here: _pandas_helpers imports pandas_gbq, which imports
        # this package's table module.
        from google.cloud.bigquery import _pandas_helpers

        pa_schema = _pandas_helpers.bq_to_arrow_schema(bq_schema)
    if pa_schema is None:
        pa_schema = pyarrow.schema([])
    return pyarrow.RecordBatch.from_arrays(
        [pyarrow.array([], type=field.type) for field in pa_schema],
        schema=pa_schema,
    )


def _read_rows_options(options: Optional[Dict[str, str]]) -> Dict[str, str]:
    """Convert ``jobs.query`` ``arrowSerializationOptions`` to the
    ``ArrowSerializationOptions`` fields that ``ReadRows`` takes."""
    options = options or serialization_options(None)
    return {
        "buffer_compression": options["bufferCompression"],
        "picos_timestamp_precision": options["picosTimestampPrecision"],
    }


def _open_job_stream(
    row_iterator: "RowIterator",
    bqstorage_client: "bigquery_storage.BigQueryReadClient",
    offset: int,
    timeout: Optional[float],
):
    """Open the job's default stream, starting at row ``offset``."""
    project = row_iterator._project or (
        row_iterator.client.project if row_iterator.client else None
    )
    location = row_iterator._location or (
        row_iterator.client.location if row_iterator.client else None
    )
    stream_name = f"projects/{project}/locations/{location}/jobs/{row_iterator._job_id}/streams/_default"
    return bqstorage_client.read_rows(
        stream_name,
        offset=offset,
        timeout=timeout,
        arrow_serialization_options=_read_rows_options(
            row_iterator._arrow_serialization_options
        ),
    )


def _open_destination_stream(
    row_iterator: "RowIterator",
    bqstorage_client: "bigquery_storage.BigQueryReadClient",
    timeout: Optional[float],
    pa_schema: Optional["pyarrow.Schema"],
):
    """Open a read session on the query's explicit destination table.

    The default job stream rejects jobs with an explicit destination table
    ("This API does not support explicitly-specified destination tables"), so
    read the table instead. One stream keeps the rows in order, and the
    session's read options carry the same serialization options as
    ``jobs.query``. Explicit destinations always go through ``jobs.insert``,
    so there's no first page and the stream starts at row 0.

    Returns ``(reader, pa_schema)``, with ``reader`` set to ``None`` if the
    table is empty and the session has no streams.
    """
    from google.cloud import bigquery_storage

    session = bqstorage_client.create_read_session(
        parent=f"projects/{row_iterator._billing_project}",
        read_session=bigquery_storage.types.stream.ReadSession(
            table=row_iterator._table.to_bqstorage(),
            data_format=bigquery_storage.types.stream.DataFormat.ARROW,
            read_options=bigquery_storage.types.stream.ReadSession.TableReadOptions(
                arrow_serialization_options=_read_rows_options(
                    row_iterator._arrow_serialization_options
                )
            ),
        ),
        max_stream_count=1,
        timeout=timeout,
    )
    if pa_schema is None and session.arrow_schema.serialized_schema:
        pa_schema = pyarrow.ipc.read_schema(
            pyarrow.py_buffer(session.arrow_schema.serialized_schema)
        )
    if not session.streams:
        return None, pa_schema
    return (
        bqstorage_client.read_rows(session.streams[0].name, offset=0, timeout=timeout),
        pa_schema,
    )


def download_arrow_from_job(
    row_iterator: "RowIterator",
    bqstorage_client: Optional["bigquery_storage.BigQueryReadClient"] = None,
    timeout: Optional[float] = None,
) -> Iterator["pyarrow.RecordBatch"]:
    """Yield Arrow record batches for ``row_iterator``'s ARROW query results.

    See :meth:`google.cloud.bigquery.table.RowIterator._download_arrow_from_job_id`.
    """
    if pyarrow is None:
        raise ValueError(_NO_PYARROW_ERROR)

    offset = 0
    pa_schema = None
    page_token = None
    job_complete = False
    remaining = row_iterator.max_results
    # Results without rows still yield one empty batch, so callers get the
    # schema.
    yielded = False

    # Step 1: Process initial inline Arrow response from jobs.query if available.
    if row_iterator._first_page_response:
        # Keep the first page on the iterator so the result can be read
        # again. The row pager clears its own copy in
        # RowIterator._get_next_page_response().
        first_page = row_iterator._first_page_response

        job_complete = bool(first_page.get("jobComplete", False))
        page_token = first_page.get("pageToken")

        arrow_schema_json = first_page.get("arrowSchema")
        if isinstance(arrow_schema_json, dict):
            schema_bytes = arrow_schema_json.get("serializedSchema")
            if schema_bytes:
                if isinstance(schema_bytes, str):
                    schema_bytes = base64.b64decode(schema_bytes)
                pa_schema = pyarrow.ipc.read_schema(pyarrow.py_buffer(schema_bytes))

        arrow_batch_json = first_page.get("arrowRecordBatch")
        if isinstance(arrow_batch_json, dict):
            batch_bytes = arrow_batch_json.get("serializedRecordBatch")
            if batch_bytes:
                if pa_schema is None:
                    raise ValueError(_NO_ARROW_SCHEMA_ERROR)
                if isinstance(batch_bytes, str):
                    batch_bytes = base64.b64decode(batch_bytes)
                batch = pyarrow.ipc.read_record_batch(
                    pyarrow.py_buffer(batch_bytes),
                    pa_schema,
                )
                offset += batch.num_rows
                batch, remaining = _slice_batch(batch, remaining)
                yielded = True
                yield batch

    # Step 2: Return early if all results were delivered in the first page
    # response, or if the first page already reached max_results. Only a
    # pageToken says rows remain: totalRows is 0 when cached results are too
    # large to return inline.
    if (job_complete and page_token is None) or remaining == 0:
        if not yielded:
            yield _empty_batch(pa_schema, row_iterator._schema)
        return

    # Step 3: Stream remaining Arrow record batches from the job default stream,
    # or from the destination table if the job config set one, with the
    # BigQuery client's shared BigQuery Storage client unless the caller passed
    # one. Results that fit in the first page never create it.
    if bqstorage_client is None:
        if row_iterator.client is None:
            raise ValueError("RowIterator client is None.")
        bqstorage_client = row_iterator.client._get_shared_bqstorage_client()
        if bqstorage_client is None:
            raise ValueError(
                "The google-cloud-bigquery-storage library is required to read Arrow results."
            )
    if row_iterator._explicit_destination and row_iterator._table is not None:
        reader, pa_schema = _open_destination_stream(
            row_iterator, bqstorage_client, timeout, pa_schema
        )
    else:
        reader = _open_job_stream(row_iterator, bqstorage_client, offset, timeout)
    if reader is None:
        # An empty destination table has no streams.
        yield _empty_batch(pa_schema, row_iterator._schema)
        return
    finished = False
    try:
        for response in reader:
            if (
                response.arrow_schema
                and response.arrow_schema.serialized_schema
                and pa_schema is None
            ):
                pa_schema = pyarrow.ipc.read_schema(
                    pyarrow.py_buffer(response.arrow_schema.serialized_schema)
                )
            if (
                response.arrow_record_batch
                and response.arrow_record_batch.serialized_record_batch
            ):
                if pa_schema is None:
                    raise ValueError(_NO_ARROW_SCHEMA_ERROR)
                batch = pyarrow.ipc.read_record_batch(
                    pyarrow.py_buffer(
                        response.arrow_record_batch.serialized_record_batch
                    ),
                    pa_schema,
                )
                batch, remaining = _slice_batch(batch, remaining)
                yielded = True
                yield batch
                if remaining == 0:
                    break
        else:
            finished = True
    finally:
        # Stop the stream if reading ends before it does: at max_results, on
        # an error, or when the caller closes the iterator.
        if not finished:
            reader.cancel()
    if not yielded:
        yield _empty_batch(pa_schema, row_iterator._schema)
