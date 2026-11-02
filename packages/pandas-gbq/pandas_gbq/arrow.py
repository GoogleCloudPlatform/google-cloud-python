"""Arrow integration submodule for pandas-gbq."""

from typing import Any, Optional

try:
    import pyarrow as pa
except ImportError:
    pa = None  # type: ignore[assignment]


def from_read_rows_response(
    message: Any,
    arrow_schema: Optional[Any] = None,
) -> Any:
    """Decodes a ReadRowsResponse protobuf message into a pyarrow.RecordBatch."""
    if pa is None:
        raise ImportError(
            "pyarrow is required to use 'from_read_rows_response'. "
            "Please install pyarrow to use this function."
        )

    if (
        not hasattr(message, "arrow_record_batch")
        or not message.arrow_record_batch.serialized_record_batch
    ):
        empty_schema = arrow_schema or pa.schema([])
        return pa.RecordBatch.from_pylist([], schema=empty_schema)

    serialized_batch = message.arrow_record_batch.serialized_record_batch
    buffer = pa.py_buffer(serialized_batch)

    if arrow_schema is not None:
        try:
            return pa.ipc.read_record_batch(buffer, arrow_schema)
        except (pa.ArrowException, OSError):
            pass

    try:
        reader = pa.ipc.RecordBatchStreamReader(buffer)
        return reader.read_next_batch()
    except (pa.ArrowException, OSError):
        if arrow_schema is None:
            raise ValueError(
                "arrow_schema is required to decode a serialized record batch message "
                "when it is not formatted as an Arrow IPC stream."
            )
        msg = pa.ipc.read_message(buffer)
        return pa.ipc.read_record_batch(msg, arrow_schema)
