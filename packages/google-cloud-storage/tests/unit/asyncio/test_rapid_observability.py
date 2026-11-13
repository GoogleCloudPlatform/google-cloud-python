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

"""Unit tests for OpenTelemetry tracing in Rapid Storage async gRPC classes."""

import asyncio
import importlib
from io import BytesIO
from unittest import mock

import pytest
from google.api_core import exceptions as api_exceptions

from google.cloud import _storage_v2 as storage_v2
from google.cloud.storage import _opentelemetry_tracing
from google.cloud.storage.asyncio import _utils, async_grpc_client
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    AsyncAppendableObjectWriter,
)
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from google.cloud.storage.asyncio.async_read_object_stream import (
    _AsyncReadObjectStream,
)
from google.cloud.storage.asyncio.async_write_object_stream import (
    _AsyncWriteObjectStream,
)


async def _noop_coro(value):
    return value


def _custom_eager_task_factory(loop, coro, **kwargs):
    """Minimal eager task factory for coroutines that finish without suspending."""
    result = None
    try:
        coro.send(None)
    except StopIteration as stop:
        result = stop.value
    return asyncio.Task(_noop_coro(result), **kwargs)


@pytest.fixture
def exporter(monkeypatch):
    """Set up OpenTelemetry InMemorySpanExporter and enable tracing."""
    try:
        from opentelemetry import trace as trace_api
        from opentelemetry.sdk.trace import TracerProvider, export
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
    except ImportError:  # pragma: NO COVER
        pytest.skip("OpenTelemetry SDK packages are required for this test suite.")

    monkeypatch.setenv("ENABLE_GCS_PYTHON_CLIENT_OTEL_TRACES", "true")
    monkeypatch.delenv("DISABLE_GCS_PYTHON_CLIENT_OTEL_BUCKET_METADATA", raising=False)

    tracer_provider = TracerProvider()
    memory_exporter = InMemorySpanExporter()
    span_processor = export.SimpleSpanProcessor(memory_exporter)
    tracer_provider.add_span_processor(span_processor)

    with mock.patch.object(
        trace_api, "get_tracer", side_effect=tracer_provider.get_tracer
    ):
        importlib.reload(_opentelemetry_tracing)
        yield memory_exporter
        memory_exporter.clear()

    monkeypatch.setenv("ENABLE_GCS_PYTHON_CLIENT_OTEL_TRACES", "false")
    importlib.reload(_opentelemetry_tracing)


@pytest.fixture
def mock_client():
    """Create an AsyncGrpcClient with a mocked underlying GAPIC client."""
    with mock.patch("google.cloud._storage_v2.StorageAsyncClient"):
        client = async_grpc_client.AsyncGrpcClient(
            credentials=mock.Mock(),
        )
        client._grpc_client = mock.AsyncMock()
        # Pre-populate ACO bucket metadata cache for Rapid Storage bucket verification
        client._bucket_metadata_cache.update_cache(
            "my-rapid-bucket",
            "//storage.googleapis.com/projects/123456789/buckets/my-rapid-bucket",
            "us-east1-a",
        )
        return client


def test_inject_traceparent_to_metadata_when_disabled(monkeypatch):
    monkeypatch.setattr(_opentelemetry_tracing, "enable_otel_traces", False)

    orig = (("x-goog-request-params", "bucket=foo"),)
    result = _utils.inject_traceparent_to_metadata(orig)
    assert result == orig


def test_inject_traceparent_to_metadata_when_enabled(exporter):
    with _opentelemetry_tracing.create_trace_span("Test.ParentSpan", rpc_system="grpc"):
        orig = (("x-goog-request-params", "bucket=foo"),)
        result = _utils.inject_traceparent_to_metadata(orig)
        keys = [k for k, _ in result]
        assert "traceparent" in keys
        traceparent_val = dict(result)["traceparent"]
        assert traceparent_val.startswith("00-")


@pytest.mark.asyncio
async def test_async_write_object_stream_open_injects_traceparent(exporter):
    mock_grpc_client = mock.MagicMock()
    mock_grpc_client._client._transport.bidi_write_object = mock.sentinel.write_rpc
    mock_grpc_client._client._transport._wrapped_methods = {
        mock.sentinel.write_rpc: mock.sentinel.wrapped_write_rpc
    }

    with mock.patch(
        "google.cloud.storage.asyncio.async_write_object_stream.AsyncBidiRpc"
    ) as mock_bidi_rpc_cls:
        mock_rpc = mock_bidi_rpc_cls.return_value
        mock_rpc.open = mock.AsyncMock()
        mock_rpc.recv = mock.AsyncMock(
            return_value=storage_v2.BidiWriteObjectResponse(persisted_size=0)
        )

        stream = _AsyncWriteObjectStream(mock_grpc_client, "my-rapid-bucket", "obj1")
        with _opentelemetry_tracing.create_trace_span(
            "Test.WriteStreamOpen", rpc_system="grpc"
        ):
            await stream.open()

        metadata = dict(mock_bidi_rpc_cls.call_args.kwargs["metadata"])
        assert (
            metadata["x-goog-request-params"]
            == "bucket=projects/_/buckets/my-rapid-bucket"
        )
        assert metadata["traceparent"].startswith("00-")


@pytest.mark.asyncio
async def test_async_write_object_stream_open_skips_traceparent_when_disabled(
    exporter, monkeypatch
):
    from opentelemetry import trace as trace_api

    monkeypatch.setattr(_opentelemetry_tracing, "enable_otel_traces", False)

    mock_grpc_client = mock.MagicMock()
    mock_grpc_client._client._transport.bidi_write_object = mock.sentinel.write_rpc
    mock_grpc_client._client._transport._wrapped_methods = {
        mock.sentinel.write_rpc: mock.sentinel.wrapped_write_rpc
    }

    with mock.patch(
        "google.cloud.storage.asyncio.async_write_object_stream.AsyncBidiRpc"
    ) as mock_bidi_rpc_cls:
        mock_rpc = mock_bidi_rpc_cls.return_value
        mock_rpc.open = mock.AsyncMock()
        mock_rpc.recv = mock.AsyncMock(
            return_value=storage_v2.BidiWriteObjectResponse(persisted_size=0)
        )

        stream = _AsyncWriteObjectStream(mock_grpc_client, "my-rapid-bucket", "obj1")
        with trace_api.get_tracer(__name__).start_as_current_span("AmbientSpan"):
            await stream.open()

        metadata = dict(mock_bidi_rpc_cls.call_args.kwargs["metadata"])
        assert (
            metadata["x-goog-request-params"]
            == "bucket=projects/_/buckets/my-rapid-bucket"
        )
        assert "traceparent" not in metadata


@pytest.mark.asyncio
async def test_async_read_object_stream_open_injects_traceparent(exporter):
    mock_grpc_client = mock.MagicMock()
    mock_grpc_client._client._transport.bidi_read_object = mock.sentinel.read_rpc
    mock_grpc_client._client._transport._wrapped_methods = {
        mock.sentinel.read_rpc: mock.sentinel.wrapped_read_rpc
    }

    with mock.patch(
        "google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc"
    ) as mock_bidi_rpc_cls:
        mock_rpc = mock_bidi_rpc_cls.return_value
        mock_rpc.open = mock.AsyncMock()
        mock_rpc.recv = mock.AsyncMock(
            return_value=storage_v2.BidiReadObjectResponse(
                read_handle=storage_v2.BidiReadHandle(handle=b"rh-1")
            )
        )

        stream = _AsyncReadObjectStream(mock_grpc_client, "my-rapid-bucket", "obj1")
        with _opentelemetry_tracing.create_trace_span(
            "Test.ReadStreamOpen", rpc_system="grpc"
        ):
            await stream.open()

        metadata = dict(mock_bidi_rpc_cls.call_args.kwargs["metadata"])
        assert (
            metadata["x-goog-request-params"]
            == "bucket=projects/_/buckets/my-rapid-bucket"
        )
        assert metadata["traceparent"].startswith("00-")


@pytest.mark.asyncio
async def test_async_read_object_stream_open_skips_traceparent_when_disabled(
    exporter, monkeypatch
):
    from opentelemetry import trace as trace_api

    monkeypatch.setattr(_opentelemetry_tracing, "enable_otel_traces", False)

    mock_grpc_client = mock.MagicMock()
    mock_grpc_client._client._transport.bidi_read_object = mock.sentinel.read_rpc
    mock_grpc_client._client._transport._wrapped_methods = {
        mock.sentinel.read_rpc: mock.sentinel.wrapped_read_rpc
    }

    with mock.patch(
        "google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc"
    ) as mock_bidi_rpc_cls:
        mock_rpc = mock_bidi_rpc_cls.return_value
        mock_rpc.open = mock.AsyncMock()
        mock_rpc.recv = mock.AsyncMock(
            return_value=storage_v2.BidiReadObjectResponse(
                read_handle=storage_v2.BidiReadHandle(handle=b"rh-1")
            )
        )

        stream = _AsyncReadObjectStream(mock_grpc_client, "my-rapid-bucket", "obj1")
        with trace_api.get_tracer(__name__).start_as_current_span("AmbientSpan"):
            await stream.open()

        metadata = dict(mock_bidi_rpc_cls.call_args.kwargs["metadata"])
        assert (
            metadata["x-goog-request-params"]
            == "bucket=projects/_/buckets/my-rapid-bucket"
        )
        assert "traceparent" not in metadata


@pytest.mark.asyncio
async def test_async_grpc_client_get_and_delete_object_spans(exporter, mock_client):
    mock_client._grpc_client.get_object.return_value = storage_v2.Object(
        name="obj1", bucket="projects/_/buckets/my-rapid-bucket"
    )
    mock_client._grpc_client.delete_object.return_value = None

    await mock_client.get_object("my-rapid-bucket", "obj1")
    await mock_client.delete_object("my-rapid-bucket", "obj1")

    spans = exporter.get_finished_spans()
    assert len(spans) == 2

    get_span, del_span = spans[0], spans[1]
    assert get_span.name == "Storage.AsyncGrpcClient.getObject"
    assert get_span.attributes["rpc.system"] == "grpc"
    assert get_span.attributes["gcp.client.service"] == "storage"
    assert (
        get_span.attributes["gcp.resource.destination.id"]
        == "//storage.googleapis.com/projects/123456789/buckets/my-rapid-bucket"
    )
    assert get_span.attributes["gcp.resource.destination.location"] == "us-east1-a"

    assert del_span.name == "Storage.AsyncGrpcClient.deleteObject"
    assert del_span.attributes["rpc.system"] == "grpc"

    # Verify traceparent was injected into GAPIC call metadata
    get_kwargs = mock_client._grpc_client.get_object.call_args.kwargs
    metadata_keys = [k for k, _ in get_kwargs["metadata"]]
    assert "traceparent" in metadata_keys


@pytest.mark.asyncio
async def test_async_appendable_object_writer_spans(exporter, mock_client):
    writer = AsyncAppendableObjectWriter(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="append-obj",
    )

    with mock.patch(
        "google.cloud.storage.asyncio.async_appendable_object_writer._AsyncWriteObjectStream"
    ) as mock_stream_cls:
        mock_stream = mock.AsyncMock()
        mock_stream.generation_number = 1001
        mock_stream.write_handle = storage_v2.BidiWriteHandle(handle=b"handle-1")
        mock_stream.persisted_size = 0
        mock_stream.recv.return_value = storage_v2.BidiWriteObjectResponse(
            persisted_size=11
        )
        mock_stream_cls.return_value = mock_stream

        await writer.open()
        await writer.append(b"hello world")
        await writer.simple_flush()
        await writer.flush()
        await writer.close()

    spans = exporter.get_finished_spans()
    span_names = [s.name for s in spans]
    assert span_names == [
        "Storage.AsyncAppendableObjectWriter.open",
        "Storage.AsyncAppendableObjectWriter.append",
        "Storage.AsyncAppendableObjectWriter.simpleFlush",
        "Storage.AsyncAppendableObjectWriter.flush",
        "Storage.AsyncAppendableObjectWriter.close",
    ]

    append_span = spans[1]
    assert append_span.attributes["rpc.system"] == "grpc"
    assert append_span.attributes["gcp.storage.payload.size_bytes"] == 11
    assert "gcp.storage.append.bytes" not in append_span.attributes
    assert "gcp.storage.chunk.size" not in append_span.attributes
    assert (
        append_span.attributes["gcp.resource.destination.id"]
        == "//storage.googleapis.com/projects/123456789/buckets/my-rapid-bucket"
    )
    assert append_span.attributes["gcp.resource.destination.location"] == "us-east1-a"


@pytest.mark.asyncio
async def test_async_appendable_object_writer_state_lookup_and_append_from_file_spans(
    exporter, mock_client
):
    writer = AsyncAppendableObjectWriter(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="append-obj",
    )

    with mock.patch(
        "google.cloud.storage.asyncio.async_appendable_object_writer._AsyncWriteObjectStream"
    ) as mock_stream_cls:
        mock_stream = mock.AsyncMock()
        mock_stream.generation_number = 1001
        mock_stream.write_handle = storage_v2.BidiWriteHandle(handle=b"handle-1")
        mock_stream.persisted_size = 0
        mock_stream.recv.return_value = storage_v2.BidiWriteObjectResponse(
            persisted_size=12
        )
        mock_stream_cls.return_value = mock_stream

        await writer.open()
        persisted = await writer.state_lookup()
        assert persisted == 12

        # Multi-block file emits a single appendFromFile span and suppresses nested append spans
        await writer.append_from_file(BytesIO(b"a" * 12), block_size=4)
        # Empty file still emits a single appendFromFile span
        await writer.append_from_file(BytesIO(b""), block_size=4)

        await writer.close()

    spans = exporter.get_finished_spans()
    assert [s.name for s in spans] == [
        "Storage.AsyncAppendableObjectWriter.open",
        "Storage.AsyncAppendableObjectWriter.stateLookup",
        "Storage.AsyncAppendableObjectWriter.appendFromFile",
        "Storage.AsyncAppendableObjectWriter.appendFromFile",
        "Storage.AsyncAppendableObjectWriter.close",
    ]


@pytest.mark.asyncio
async def test_async_appendable_object_writer_finalize_and_no_nested_spans(
    exporter, mock_client
):
    writer = AsyncAppendableObjectWriter(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="append-obj",
    )

    with mock.patch(
        "google.cloud.storage.asyncio.async_appendable_object_writer._AsyncWriteObjectStream"
    ) as mock_stream_cls:
        mock_stream = mock.AsyncMock()
        mock_stream.generation_number = 1001
        mock_stream.write_handle = storage_v2.BidiWriteHandle(handle=b"handle-1")
        mock_stream.persisted_size = 0
        mock_stream.recv.return_value = storage_v2.BidiWriteObjectResponse(
            resource=storage_v2.Object(size=5)
        )
        mock_stream_cls.return_value = mock_stream

        # 1. Direct finalize() call emits Storage.AsyncAppendableObjectWriter.finalize
        await writer.open()
        await writer.finalize()

        # 2. close(finalize_on_close=True) emits only close(), without nested finalize()
        await writer.open()
        # Simulate a retry on finalize inside close(finalize_on_close=True) that re-opens stream
        mock_stream.send.side_effect = [
            api_exceptions.ServiceUnavailable("transient error"),
            None,
        ]
        await writer.close(finalize_on_close=True)

    spans = exporter.get_finished_spans()
    span_names = [s.name for s in spans]
    assert span_names == [
        "Storage.AsyncAppendableObjectWriter.open",
        "Storage.AsyncAppendableObjectWriter.finalize",
        "Storage.AsyncAppendableObjectWriter.open",
        "Storage.AsyncAppendableObjectWriter.close",
    ]


@pytest.mark.asyncio
async def test_async_multi_range_downloader_spans(exporter, mock_client):
    mrd = AsyncMultiRangeDownloader(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="read-obj",
    )

    with (
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
        ) as mock_stream_cls,
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._StreamMultiplexer"
        ) as mock_mux_cls,
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._BidiStreamRetryManager"
        ) as mock_retry_mgr_cls,
    ):
        mock_stream = mock.AsyncMock()
        mock_stream.generation_number = 2002
        mock_stream.read_handle = storage_v2.BidiReadHandle(handle=b"rhandle-1")
        mock_stream.persisted_size = 1024
        mock_stream.is_finalized = True
        mock_stream.full_obj_server_crc32c = None
        mock_stream_cls.return_value = mock_stream

        mock_mux = mock.AsyncMock()
        mock_mux.register = mock.Mock(return_value=mock.AsyncMock())
        mock_mux.unregister = mock.Mock()
        mock_mux_cls.return_value = mock_mux

        mock_retry_mgr = mock.AsyncMock()
        mock_retry_mgr_cls.return_value = mock_retry_mgr

        await mrd.open()
        buf1, buf2 = BytesIO(), BytesIO()
        await mrd.download_ranges(
            [(0, 100, buf1), (200, 300, buf2)], enable_checksum=False
        )
        await mrd.close()

    spans = exporter.get_finished_spans()
    span_names = [s.name for s in spans]
    assert span_names == [
        "Storage.AsyncMultiRangeDownloader.open",
        "Storage.AsyncMultiRangeDownloader.downloadRanges",
        "Storage.AsyncMultiRangeDownloader.close",
    ]

    download_span = spans[1]
    assert download_span.attributes["rpc.system"] == "grpc"
    assert download_span.attributes["gcp.storage.range.count"] == 2
    assert (
        download_span.attributes["gcp.resource.destination.id"]
        == "//storage.googleapis.com/projects/123456789/buckets/my-rapid-bucket"
    )
    assert download_span.attributes["gcp.resource.destination.location"] == "us-east1-a"


@pytest.mark.asyncio
async def test_async_multi_range_downloader_data_corruption_marks_span_error(
    exporter, mock_client
):
    from opentelemetry import trace as trace_api

    from google.cloud.storage.exceptions import DataCorruption

    mrd = AsyncMultiRangeDownloader(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="read-obj",
    )

    with (
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
        ) as mock_stream_cls,
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._StreamMultiplexer"
        ) as mock_mux_cls,
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._BidiStreamRetryManager"
        ) as mock_retry_mgr_cls,
    ):
        mock_stream = mock.AsyncMock()
        mock_stream.generation_number = 2002
        mock_stream.read_handle = storage_v2.BidiReadHandle(handle=b"rhandle-1")
        mock_stream.persisted_size = 1024
        mock_stream.is_finalized = True
        mock_stream.full_obj_server_crc32c = None
        mock_stream_cls.return_value = mock_stream

        mock_mux = mock.AsyncMock()
        mock_mux.register = mock.Mock(return_value=mock.AsyncMock())
        mock_mux.unregister = mock.Mock()
        mock_mux_cls.return_value = mock_mux

        mock_retry_mgr = mock.AsyncMock()
        mock_retry_mgr.execute.side_effect = DataCorruption(
            mock.Mock(), "CRC32C checksum mismatch"
        )
        mock_retry_mgr_cls.return_value = mock_retry_mgr

        await mrd.open()
        with pytest.raises(DataCorruption):
            await mrd.download_ranges([(0, 100, BytesIO())], enable_checksum=False)

    assert not mrd.is_stream_open
    spans = exporter.get_finished_spans()
    assert [s.name for s in spans] == [
        "Storage.AsyncMultiRangeDownloader.open",
        "Storage.AsyncMultiRangeDownloader.downloadRanges",
    ]

    download_span = spans[1]
    assert download_span.status.status_code == trace_api.StatusCode.ERROR
    assert len(download_span.events) == 1
    assert download_span.events[0].name == "exception"


@pytest.mark.asyncio
async def test_concurrent_tasks_emit_independent_t2_spans(exporter, mock_client):
    """Concurrent tasks sharing an MRD or writer must not suppress each other's T2 spans."""
    mrd = AsyncMultiRangeDownloader(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="read-obj",
    )
    writer = AsyncAppendableObjectWriter(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="append-obj",
    )

    with (
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
        ) as mock_read_stream_cls,
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._StreamMultiplexer"
        ) as mock_mux_cls,
        mock.patch(
            "google.cloud.storage.asyncio.async_multi_range_downloader._BidiStreamRetryManager"
        ) as mock_retry_mgr_cls,
        mock.patch(
            "google.cloud.storage.asyncio.async_appendable_object_writer._AsyncWriteObjectStream"
        ) as mock_write_stream_cls,
    ):
        mock_read_stream = mock.AsyncMock()
        mock_read_stream.generation_number = 2002
        mock_read_stream.read_handle = storage_v2.BidiReadHandle(handle=b"rhandle-1")
        mock_read_stream.persisted_size = 1024
        mock_read_stream.is_finalized = True
        mock_read_stream.full_obj_server_crc32c = None
        mock_read_stream_cls.return_value = mock_read_stream

        mock_mux = mock.AsyncMock()
        mock_mux.register = mock.Mock(return_value=mock.AsyncMock())
        mock_mux.unregister = mock.Mock()
        mock_mux_cls.return_value = mock_mux

        async def yielding_execute(*args, **kwargs):
            await asyncio.sleep(0)

        mock_retry_mgr = mock.AsyncMock()
        mock_retry_mgr.execute.side_effect = yielding_execute
        mock_retry_mgr_cls.return_value = mock_retry_mgr

        mock_write_stream = mock.AsyncMock()
        mock_write_stream.generation_number = 1001
        mock_write_stream.write_handle = storage_v2.BidiWriteHandle(handle=b"wh-1")
        mock_write_stream.persisted_size = 0

        async def yielding_recv(*args, **kwargs):
            await asyncio.sleep(0)
            return storage_v2.BidiWriteObjectResponse(persisted_size=8)

        mock_write_stream.recv.side_effect = yielding_recv
        mock_write_stream_cls.return_value = mock_write_stream

        await mrd.open()
        await asyncio.gather(
            mrd.download_ranges([(0, 10, BytesIO())], enable_checksum=False),
            mrd.download_ranges([(10, 20, BytesIO())], enable_checksum=False),
        )
        await mrd.close()

        await writer.open()
        await asyncio.gather(writer.flush(), writer.flush())
        await writer.close()

    span_names = [s.name for s in exporter.get_finished_spans()]
    assert span_names.count("Storage.AsyncMultiRangeDownloader.downloadRanges") == 2
    assert span_names.count("Storage.AsyncAppendableObjectWriter.flush") == 2


@pytest.mark.asyncio
async def test_top_level_span_context_resets_owner_on_aenter_error(
    exporter, mock_client
):
    owner = object()
    failing_cm = mock.MagicMock()
    failing_cm.__aenter__ = mock.AsyncMock(side_effect=RuntimeError("aenter failed"))

    with mock.patch.object(_utils, "create_trace_span_helper", return_value=failing_cm):
        with pytest.raises(RuntimeError, match="aenter failed"):
            async with _utils.create_top_level_trace_span(
                owner, mock_client, "my-rapid-bucket", "Test.AenterFailure"
            ):
                pass  # pragma: NO COVER

    assert _utils._ACTIVE_T2_SPAN_OWNERS.get() == frozenset()


@pytest.mark.asyncio
async def test_bucket_metadata_cache_async_grpc_fetch(mock_client):
    cache = mock_client._bucket_metadata_cache
    cache.clear()

    mock_client._grpc_client.get_bucket.return_value = storage_v2.Bucket(
        name="projects/_/buckets/new-rapid-bucket",
        project="projects/987654321",
        location="US-WEST1-B",
        location_type="zone",
    )

    # First call misses cache and schedules _fetch_background_async on event loop
    res = cache.get_or_queue_fetch("new-rapid-bucket")
    assert res is None

    # Deterministically await tracked background tasks
    await asyncio.gather(*cache._background_tasks)

    cached = cache.get("new-rapid-bucket")
    assert cached == (
        "//storage.googleapis.com/projects/987654321/buckets/new-rapid-bucket",
        "us-west1-b",
    )


@pytest.mark.asyncio
async def test_bucket_metadata_cache_async_grpc_403_fallback(mock_client):
    cache = mock_client._bucket_metadata_cache
    cache.clear()

    mock_client._grpc_client.get_bucket.side_effect = api_exceptions.Forbidden(
        "storage.buckets.get denied"
    )

    res = cache.get_or_queue_fetch("restricted-bucket")
    assert res is None

    await asyncio.gather(*cache._background_tasks)

    cached = cache.get("restricted-bucket")
    assert cached == (
        "//storage.googleapis.com/projects/_/buckets/restricted-bucket",
        "global",
    )


@pytest.mark.asyncio
async def test_bucket_metadata_cache_async_grpc_404_eviction_and_refresh(mock_client):
    cache = mock_client._bucket_metadata_cache

    # 1. If bucket still exists on 404 check, refresh cache entry from GetBucket response
    mock_client._grpc_client.get_bucket.return_value = storage_v2.Bucket(
        name="projects/_/buckets/my-rapid-bucket",
        project="projects/123456789",
        location="US-EAST1-B",
        location_type="zone",
    )
    cache.check_and_evict("my-rapid-bucket")
    await asyncio.gather(*cache._background_tasks)
    assert cache.get("my-rapid-bucket") == (
        "//storage.googleapis.com/projects/123456789/buckets/my-rapid-bucket",
        "us-east1-b",
    )

    # 2. If GetBucket returns 404 NotFound, evict bucket from cache
    mock_client._grpc_client.get_bucket.side_effect = api_exceptions.NotFound(
        "Bucket not found"
    )
    cache.check_and_evict("my-rapid-bucket")
    await asyncio.gather(*cache._background_tasks)
    assert cache.get("my-rapid-bucket") is None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "task_factory",
    [
        _custom_eager_task_factory,
        pytest.param(
            getattr(asyncio, "eager_task_factory", None),
            marks=pytest.mark.skipif(
                not hasattr(asyncio, "eager_task_factory"),
                reason="asyncio.eager_task_factory requires Python 3.12+",
            ),
        ),
    ],
)
async def test_bucket_metadata_cache_eager_task_no_deadlock(mock_client, task_factory):
    """Verify eager task execution does not deadlock on BucketMetadataCache._lock."""
    cache = mock_client._bucket_metadata_cache
    cache.clear()
    loop = asyncio.get_running_loop()
    orig_factory = loop.get_task_factory()

    async def immediate_get_bucket(**kwargs):
        assert not cache._lock.locked(), "Lock must be released before spawning task"
        return storage_v2.Bucket(
            name="projects/_/buckets/eager-bucket",
            project="projects/555555",
            location="US-CENTRAL1-A",
            location_type="zone",
        )

    async def immediate_missing_bucket(**kwargs):
        assert not cache._lock.locked(), "Lock must be released before spawning task"
        raise api_exceptions.NotFound("Bucket deleted")

    loop.set_task_factory(task_factory)
    try:
        mock_client._grpc_client.get_bucket = immediate_get_bucket
        assert cache.get_or_queue_fetch("eager-bucket") is None
        assert cache.get("eager-bucket") == (
            "//storage.googleapis.com/projects/555555/buckets/eager-bucket",
            "us-central1-a",
        )
        assert "eager-bucket" not in cache._inflight_fetches

        mock_client._grpc_client.get_bucket = immediate_missing_bucket
        cache.check_and_evict("eager-bucket")
        assert cache.get("eager-bucket") is None
        assert "eager-bucket" not in cache._inflight_checks
    finally:
        loop.set_task_factory(orig_factory)

    await asyncio.gather(*cache._background_tasks)
    await asyncio.sleep(0)
    assert len(cache._background_tasks) == 0


@pytest.mark.asyncio
async def test_bucket_metadata_cache_background_get_bucket_detaches_trace_context(
    exporter, mock_client
):
    """Background GetBucket tasks must run in an empty contextvars.Context."""
    from opentelemetry import trace as trace_api

    cache = mock_client._bucket_metadata_cache
    observed_span_valid = []

    async def inspect_context_get_bucket(**kwargs):
        span_ctx = trace_api.get_current_span().get_span_context()
        observed_span_valid.append(span_ctx.is_valid)
        return storage_v2.Bucket(
            name="projects/_/buckets/detached-bucket",
            project="projects/123456789",
            location="US-EAST1-A",
            location_type="zone",
        )

    mock_client._grpc_client.get_bucket.side_effect = inspect_context_get_bucket
    mock_client._grpc_client.get_object.side_effect = api_exceptions.NotFound(
        "Object not found"
    )

    with trace_api.get_tracer(__name__).start_as_current_span("CallerParentSpan"):
        cache.get_or_queue_fetch("detached-bucket")
        await asyncio.gather(*cache._background_tasks)

        cache.check_and_evict("my-rapid-bucket")
        await asyncio.gather(*cache._background_tasks)

    finished_counts_at_not_found = []
    orig_check_and_evict = cache.check_and_evict

    def spy_check_and_evict(bucket_name):
        finished_counts_at_not_found.append(len(exporter.get_finished_spans()))
        return orig_check_and_evict(bucket_name)

    with mock.patch.object(cache, "check_and_evict", side_effect=spy_check_and_evict):
        with pytest.raises(api_exceptions.NotFound):
            await mock_client.get_object("my-rapid-bucket", "missing-obj")
        await asyncio.gather(*cache._background_tasks)

    assert observed_span_valid == [False, False, False]
    # CallerParentSpan + getObject span both finished before _handle_not_found ran
    assert finished_counts_at_not_found == [2]


def test_bucket_metadata_cache_async_client_no_running_loop_fallback(mock_client):
    """When no event loop is running, _spawn_async_task closes coro and clears inflight."""
    cache = mock_client._bucket_metadata_cache
    assert cache.get_or_queue_fetch("sync-miss-bucket") is None
    assert "sync-miss-bucket" not in cache._inflight_fetches

    cache.check_and_evict("my-rapid-bucket")
    assert "my-rapid-bucket" not in cache._inflight_checks
    assert len(cache._background_tasks) == 0


def test_trace_span_helper_exit_suppressed_and_uninitialized(exporter, mock_client):
    """Verify _TraceSpanHelperContext.__exit__ handles uninitialized and suppressing base CMs."""
    from google.cloud.storage import _helpers

    uninit_cm = _helpers._TraceSpanHelperContext(
        mock_client, "my-rapid-bucket", "Test.Uninitialized"
    )
    assert uninit_cm.__exit__(None, None, None) is False

    suppressing_base_cm = mock.MagicMock()
    suppressing_base_cm.__enter__.return_value = object()
    suppressing_base_cm.__exit__.return_value = True

    with (
        mock.patch.object(
            _helpers, "_base_create_trace_span", return_value=suppressing_base_cm
        ),
        mock.patch.object(
            mock_client._bucket_metadata_cache, "check_and_evict"
        ) as mock_evict,
    ):
        with _helpers.create_trace_span_helper(
            mock_client, "my-rapid-bucket", "Test.Suppressed404"
        ):
            raise api_exceptions.NotFound("suppressed 404")

        mock_evict.assert_not_called()


@pytest.mark.asyncio
async def test_async_grpc_error_records_span_exception_once_and_evicts_on_404(
    exporter, mock_client
):
    from opentelemetry import trace as trace_api

    mock_client._grpc_client.get_object.side_effect = api_exceptions.NotFound(
        "Object or bucket not found"
    )
    mock_client._grpc_client.get_bucket.side_effect = api_exceptions.NotFound(
        "Bucket not found"
    )

    with pytest.raises(api_exceptions.NotFound):
        await mock_client.get_object("my-rapid-bucket", "missing-obj")

    await asyncio.gather(*mock_client._bucket_metadata_cache._background_tasks)

    # Verify bucket was evicted after 404 background existence check
    assert mock_client._bucket_metadata_cache.get("my-rapid-bucket") is None

    spans = exporter.get_finished_spans()
    assert len(spans) == 1
    span = spans[0]
    assert span.name == "Storage.AsyncGrpcClient.getObject"
    assert span.status.status_code == trace_api.StatusCode.ERROR
    # Exception event should be recorded exactly once (no duplicate event)
    exception_events = [e for e in span.events if e.name == "exception"]
    assert len(exception_events) == 1


@pytest.mark.asyncio
async def test_create_trace_span_helper_with_sync_mock_context_manager(mock_client):
    """Verify fallback when _base_create_trace_span returns a synchronous context manager."""
    from contextlib import contextmanager

    from google.cloud.storage import _helpers

    fake_span = object()

    @contextmanager
    def sync_cm(*args, **kwargs):
        yield fake_span

    with mock.patch.object(_helpers, "_base_create_trace_span", side_effect=sync_cm):
        async with _helpers.create_trace_span_helper(
            mock_client, "my-rapid-bucket", "Test.SyncFallback"
        ) as span:
            assert span is fake_span


@pytest.mark.asyncio
async def test_noop_trace_span_fast_path_when_disabled(monkeypatch, mock_client):
    """Verify zero-allocation singleton context manager is returned when tracing is disabled."""
    from google.cloud.storage import _helpers

    monkeypatch.setattr(_opentelemetry_tracing, "enable_otel_traces", False)

    cm1 = _opentelemetry_tracing.create_trace_span("Test.NoOp")
    cm2 = _helpers.create_trace_span_helper(mock_client, "my-rapid-bucket", "Test.NoOp")
    writer = AsyncAppendableObjectWriter(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="append-obj",
    )
    mrd = AsyncMultiRangeDownloader(
        client=mock_client,
        bucket_name="my-rapid-bucket",
        object_name="read-obj",
    )
    cm3 = writer._trace_span("Test.NoOp")
    cm4 = mrd._trace_span("Test.NoOp")

    assert cm1 is _opentelemetry_tracing._NOOP_TRACE_SPAN_CONTEXT
    assert cm2 is _opentelemetry_tracing._NOOP_TRACE_SPAN_CONTEXT
    assert cm3 is _opentelemetry_tracing._NOOP_TRACE_SPAN_CONTEXT
    assert cm4 is _opentelemetry_tracing._NOOP_TRACE_SPAN_CONTEXT

    with cm1 as s1:
        assert s1 is None
    async with cm2 as s2:
        assert s2 is None
    async with cm3 as s3:
        assert s3 is None
    async with cm4 as s4:
        assert s4 is None


@pytest.mark.asyncio
async def test_async_grpc_client_tracing_coexists_with_metrics_and_interconnect_options(
    exporter,
):
    """Verify tracing, ACO cache, OTel metrics gating, and DirectPath Interconnect compose cleanly."""
    from google.cloud.storage import _opentelemetry_metrics

    with (
        mock.patch("google.cloud._storage_v2.StorageAsyncClient"),
        mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=True,
        ),
    ):
        client = async_grpc_client.AsyncGrpcClient(
            credentials=mock.Mock(),
            attempt_direct_path_xds_over_interconnect=True,
            enable_metrics=True,
            enable_debug_metrics=True,
        )
        client._grpc_client = mock.AsyncMock()
        client._grpc_client.get_object.return_value = storage_v2.Object(
            name="obj1", bucket="projects/_/buckets/my-rapid-bucket"
        )
        client._bucket_metadata_cache.update_cache(
            "my-rapid-bucket",
            "//storage.googleapis.com/projects/123456789/buckets/my-rapid-bucket",
            "us-east1-a",
        )

        assert client.metrics_enabled is True
        assert client.debug_metrics_enabled is True
        assert client._is_async_grpc_client is True

        await client.get_object("my-rapid-bucket", "obj1")

        spans = exporter.get_finished_spans()
        assert len(spans) == 1
        assert spans[0].name == "Storage.AsyncGrpcClient.getObject"
        assert spans[0].attributes["gcp.resource.destination.location"] == "us-east1-a"
