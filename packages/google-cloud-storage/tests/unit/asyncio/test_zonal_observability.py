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

"""Unit tests for OpenTelemetry tracing in Zonal Buckets (Rapid Storage) async gRPC classes."""

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


@pytest.fixture
def exporter(monkeypatch):
    """Set up OpenTelemetry InMemorySpanExporter and enable tracing."""
    try:
        from opentelemetry import trace as trace_api
        from opentelemetry.sdk.trace import TracerProvider, export
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
    except ImportError:
        pytest.skip("OpenTelemetry SDK packages are required for this test suite.")

    monkeypatch.setenv("ENABLE_GCS_PYTHON_CLIENT_OTEL_TRACES", "true")
    monkeypatch.delenv("DISABLE_GCS_PYTHON_CLIENT_OTEL_BUCKET_METADATA", raising=False)
    importlib.reload(_opentelemetry_tracing)

    if hasattr(trace_api, "_TRACER_PROVIDER_SET_ONCE"):
        trace_api._TRACER_PROVIDER_SET_ONCE._done = False
    trace_api._TRACER_PROVIDER = None

    tracer_provider = TracerProvider()
    memory_exporter = InMemorySpanExporter()
    span_processor = export.SimpleSpanProcessor(memory_exporter)
    tracer_provider.add_span_processor(span_processor)
    trace_api.set_tracer_provider(tracer_provider)

    yield memory_exporter
    memory_exporter.clear()
    if hasattr(trace_api, "_TRACER_PROVIDER_SET_ONCE"):
        trace_api._TRACER_PROVIDER_SET_ONCE._done = False
    trace_api._TRACER_PROVIDER = None
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
        # Pre-populate ACO bucket metadata cache for zonal bucket verification
        client._bucket_metadata_cache.update_cache(
            "my-zonal-bucket",
            "//storage.googleapis.com/projects/123456789/buckets/my-zonal-bucket",
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
async def test_async_grpc_client_get_and_delete_object_spans(exporter, mock_client):
    mock_client._grpc_client.get_object.return_value = storage_v2.Object(
        name="obj1", bucket="projects/_/buckets/my-zonal-bucket"
    )
    mock_client._grpc_client.delete_object.return_value = None

    await mock_client.get_object("my-zonal-bucket", "obj1")
    await mock_client.delete_object("my-zonal-bucket", "obj1")

    spans = exporter.get_finished_spans()
    assert len(spans) == 2

    get_span, del_span = spans[0], spans[1]
    assert get_span.name == "Storage.AsyncGrpcClient.getObject"
    assert get_span.attributes["rpc.system"] == "grpc"
    assert get_span.attributes["gcp.client.service"] == "storage"
    assert (
        get_span.attributes["gcp.resource.destination.id"]
        == "//storage.googleapis.com/projects/123456789/buckets/my-zonal-bucket"
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
        bucket_name="my-zonal-bucket",
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
    assert append_span.attributes["gcp.storage.chunk.size"] == 11
    assert (
        append_span.attributes["gcp.resource.destination.id"]
        == "//storage.googleapis.com/projects/123456789/buckets/my-zonal-bucket"
    )
    assert append_span.attributes["gcp.resource.destination.location"] == "us-east1-a"


@pytest.mark.asyncio
async def test_async_appendable_object_writer_finalize_and_no_nested_spans(
    exporter, mock_client
):
    writer = AsyncAppendableObjectWriter(
        client=mock_client,
        bucket_name="my-zonal-bucket",
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
        bucket_name="my-zonal-bucket",
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
        == "//storage.googleapis.com/projects/123456789/buckets/my-zonal-bucket"
    )
    assert download_span.attributes["gcp.resource.destination.location"] == "us-east1-a"


@pytest.mark.asyncio
async def test_bucket_metadata_cache_async_grpc_fetch(mock_client):
    cache = mock_client._bucket_metadata_cache
    cache.clear()

    mock_client._grpc_client.get_bucket.return_value = storage_v2.Bucket(
        name="projects/_/buckets/new-zonal-bucket",
        project="projects/987654321",
        location="US-WEST1-B",
        location_type="zone",
    )

    # First call misses cache and schedules _fetch_background_async on event loop
    res = cache.get_or_queue_fetch("new-zonal-bucket")
    assert res is None

    # Deterministically await tracked background tasks
    await asyncio.gather(*cache._background_tasks)

    cached = cache.get("new-zonal-bucket")
    assert cached == (
        "//storage.googleapis.com/projects/987654321/buckets/new-zonal-bucket",
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
        name="projects/_/buckets/my-zonal-bucket",
        project="projects/123456789",
        location="US-EAST1-B",
        location_type="zone",
    )
    cache.check_and_evict("my-zonal-bucket")
    await asyncio.gather(*cache._background_tasks)
    assert cache.get("my-zonal-bucket") == (
        "//storage.googleapis.com/projects/123456789/buckets/my-zonal-bucket",
        "us-east1-b",
    )

    # 2. If GetBucket returns 404 NotFound, evict bucket from cache
    mock_client._grpc_client.get_bucket.side_effect = api_exceptions.NotFound(
        "Bucket not found"
    )
    cache.check_and_evict("my-zonal-bucket")
    await asyncio.gather(*cache._background_tasks)
    assert cache.get("my-zonal-bucket") is None


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
        await mock_client.get_object("my-zonal-bucket", "missing-obj")

    await asyncio.gather(*mock_client._bucket_metadata_cache._background_tasks)

    # Verify bucket was evicted after 404 background existence check
    assert mock_client._bucket_metadata_cache.get("my-zonal-bucket") is None

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
            mock_client, "my-zonal-bucket", "Test.SyncFallback"
        ) as span:
            assert span is fake_span
