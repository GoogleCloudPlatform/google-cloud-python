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
"""UDS-mode parity with the bidi features merged from ``main``.

Covers OpenTelemetry spans (#18397), ``Preconditions`` (#18641) and the
buffer-destination contract of ``download_ranges`` (#18627) when the
``AsyncMultiRangeDownloader`` / ``AsyncAppendableObjectWriter`` are served by the
Rust Core SDK (gRPC-over-UDS) backend.
"""

import array
import datetime
import inspect
import io
from unittest import mock
from unittest.mock import AsyncMock

import pytest
from google.api_core import exceptions

from google.cloud import _storage_v2
from google.cloud.storage.asyncio import _utils, async_grpc_client
from google.cloud.storage.asyncio._uds import gcscore_pb2 as pb
from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    AsyncAppendableObjectWriter,
    Preconditions,
)
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
    _BufferWriter,
    _BytesWriter,
)
from google.cloud.storage.exceptions import DataCorruption

_MRD_MOD = "google.cloud.storage.asyncio.async_multi_range_downloader"
_AAOW_MOD = "google.cloud.storage.asyncio.async_appendable_object_writer"
_RUNTIME_GET = "google.cloud.storage.asyncio._uds.runtime.get_runtime"
_READ_SESSION = "google.cloud.storage.asyncio._uds.read_session.UdsReadSession"
_WRITE_SESSION = "google.cloud.storage.asyncio._uds.write_session.UdsWriteSession"
_BUCKET = "my-rapid-bucket"
_MiB = 1024 * 1024


# ------------------------------------------------------------------- fixtures


class _SpanRecorder:
    """Stands in for ``create_trace_span_helper`` and records span boundaries.

    It does not need the OpenTelemetry SDK (``opentelemetry-api==1.1.0`` from
    ``constraints-3.10.txt`` cannot be imported without ``pkg_resources``), and it
    proves that each UDS call runs *inside* its top-level span.
    """

    def __init__(self):
        self.events = []
        self.attributes = {}

    def __call__(self, client, bucket_name, name, attributes=None, **kwargs):
        recorder = self
        self.attributes.setdefault(name, []).append(
            dict(attributes or {}, bucket=bucket_name, **kwargs)
        )

        class _Span:
            async def __aenter__(self):
                recorder.events.append(("enter", name))

            async def __aexit__(self, exc_type, exc, tb):
                recorder.events.append(("exit", name, exc_type))
                return False

        return _Span()

    def record(self, session, *methods):
        """Records each awaited ``session.<method>`` call in ``events``."""
        for method_name in methods:
            method = getattr(session, method_name)

            async def _wrapped(
                *args,
                _name=method_name,
                _effect=method.side_effect,
                _value=method.return_value,
                **kwargs,
            ):
                self.events.append(("call", _name))
                if isinstance(_effect, BaseException):
                    raise _effect
                if _effect is None:
                    return _value
                result = _effect(*args, **kwargs)
                return await result if inspect.isawaitable(result) else result

            method.side_effect = _wrapped


@pytest.fixture
def spans():
    recorder = _SpanRecorder()
    with mock.patch.object(_utils, "create_trace_span_helper", recorder):
        yield recorder


@pytest.fixture
def client():
    """An ``AsyncGrpcClient`` with a mocked GAPIC client."""
    with mock.patch("google.cloud._storage_v2.StorageAsyncClient"):
        grpc_client = async_grpc_client.AsyncGrpcClient(credentials=mock.Mock())
    grpc_client._grpc_client = AsyncMock()
    return grpc_client


@pytest.fixture
def uds_selected():
    """Routes both bidi classes through the UDS backend (no GAPIC stream)."""
    with (
        mock.patch(f"{_MRD_MOD}._uds_selected", return_value=True),
        mock.patch(f"{_AAOW_MOD}._uds_selected", return_value=True),
        mock.patch(f"{_MRD_MOD}._AsyncReadObjectStream") as read_stream_cls,
        mock.patch(f"{_AAOW_MOD}._AsyncWriteObjectStream") as write_stream_cls,
        mock.patch(_RUNTIME_GET, AsyncMock(return_value=mock.Mock())),
    ):
        yield read_stream_cls, write_stream_cls


def _read_session(generation=42, size=1024, data=b""):
    """A fake ``UdsReadSession`` writing ``data`` like the shared-memory reader."""
    session = mock.MagicMock()
    session.open = AsyncMock(
        return_value=pb.ObjectResource(
            bucket=_BUCKET, name="o", generation=generation, size=size
        )
    )
    session.close = AsyncMock()
    session.object_metadata = None

    async def download_ranges(read_ranges):
        session.seen = list(read_ranges)
        for offset, length, writer in read_ranges:
            chunk = data[offset : offset + length if length else None]
            if chunk:
                # Shared-memory views are only valid during write().
                with memoryview(bytearray(chunk)) as view:
                    writer.write(view)

    session.download_ranges = AsyncMock(side_effect=download_ranges)
    return session


def _write_session(generation=1001, persisted_size=0):
    session = mock.MagicMock()
    session.open = AsyncMock(return_value=(generation, persisted_size))
    session.append = AsyncMock()
    session.flush = AsyncMock(return_value=11)
    session.close = AsyncMock(return_value=11)
    session.finalize = AsyncMock(
        return_value=pb.ObjectResource(
            bucket=f"projects/_/buckets/{_BUCKET}", name="o", generation=1, size=11
        )
    )
    session.has_unflushed_bytes = mock.Mock(return_value=False)
    session.last_persisted_size = 11
    return session


async def _open_mrd(client, session, **kwargs):
    with mock.patch(_READ_SESSION, return_value=session):
        return await AsyncMultiRangeDownloader.create_mrd(
            client, _BUCKET, "o", **kwargs
        )


async def _open_writer(client, session, **kwargs):
    writer = AsyncAppendableObjectWriter(client, _BUCKET, "o", **kwargs)
    with mock.patch(_WRITE_SESSION, return_value=session):
        await writer.open()
    return writer


# ---------------------------------------------------- #18397 OTel in UDS mode


def _span(name, *calls, error=None):
    return [("enter", name), *[("call", c) for c in calls], ("exit", name, error)]


_MRD = "Storage.AsyncMultiRangeDownloader."
_AAOW = "Storage.AsyncAppendableObjectWriter."


@pytest.mark.asyncio
async def test_mrd_uds_calls_run_inside_the_gapic_spans(spans, client, uds_selected):
    read_stream_cls, _ = uds_selected
    session = _read_session(data=b"x" * 400)
    spans.record(session, "open", "download_ranges", "close")
    mrd = await _open_mrd(client, session)
    past_eof = io.BytesIO()
    await mrd.download_ranges(
        [(0, 100, io.BytesIO()), (200, 100, io.BytesIO()), (500, 10, past_eof)],
        enable_checksum=False,
    )
    assert past_eof.getvalue() == b""
    await mrd.close()

    read_stream_cls.assert_not_called()
    assert spans.events == (
        _span(_MRD + "open", "open")
        + _span(_MRD + "downloadRanges", "download_ranges")
        + _span(_MRD + "close", "close")
    )
    (download,) = spans.attributes[_MRD + "downloadRanges"]
    assert download == {
        "gcp.storage.range.count": 3,
        "bucket": _BUCKET,
        "rpc_system": "grpc",
    }


@pytest.mark.asyncio
async def test_mrd_uds_data_corruption_closes_inside_the_download_span(
    spans, client, uds_selected
):
    session = _read_session()
    session.download_ranges.side_effect = DataCorruption(mock.Mock(), "crc mismatch")
    spans.record(session, "open", "download_ranges", "close")
    mrd = await _open_mrd(client, session)
    with pytest.raises(DataCorruption):
        await mrd.download_ranges([(0, 10, io.BytesIO())], enable_checksum=False)

    assert not mrd.is_stream_open and mrd._uds is None
    # The nested close() is not a top-level call, so it opens no span of its own.
    assert spans.events == _span(_MRD + "open", "open") + _span(
        _MRD + "downloadRanges", "download_ranges", "close", error=DataCorruption
    )


@pytest.mark.asyncio
async def test_mrd_uds_data_corruption_after_stream_closed(client, uds_selected):
    session = _read_session()
    mrd = await _open_mrd(client, session)

    async def corrupt_after_close(read_ranges):
        mrd._is_stream_open = False
        raise DataCorruption(mock.Mock(), "crc mismatch")

    session.download_ranges.side_effect = corrupt_after_close
    with pytest.raises(DataCorruption):
        await mrd.download_ranges([(0, 10, io.BytesIO())], enable_checksum=False)
    session.close.assert_not_awaited()


@pytest.mark.asyncio
async def test_writer_uds_calls_run_inside_the_gapic_spans(spans, client, uds_selected):
    _, write_stream_cls = uds_selected
    session = _write_session()
    spans.record(session, "open", "append", "flush", "close")
    writer = await _open_writer(client, session)
    await writer.append(b"hello world")
    await writer.simple_flush()
    await writer.flush()
    await writer.state_lookup()
    await writer.close()

    write_stream_cls.assert_not_called()
    assert spans.events == (
        _span(_AAOW + "open", "open")
        + _span(_AAOW + "append", "append")
        + _span(_AAOW + "simpleFlush", "flush")
        + _span(_AAOW + "flush", "flush")
        + _span(_AAOW + "stateLookup")
        + _span(_AAOW + "close", "close")
    )
    (append,) = spans.attributes[_AAOW + "append"]
    assert append == {
        "gcp.storage.payload.size_bytes": 11,
        "bucket": _BUCKET,
        "rpc_system": "grpc",
    }


@pytest.mark.asyncio
async def test_writer_uds_finalize_spans_match_gapic(spans, client, uds_selected):
    first_session, second_session = _write_session(), _write_session()
    spans.record(first_session, "open", "finalize")
    spans.record(second_session, "open", "finalize")
    first = await _open_writer(client, first_session)
    await first.finalize(full_object_checksum=7)
    second = await _open_writer(client, second_session)
    await second.close(finalize_on_close=True)

    assert spans.events == (
        _span(_AAOW + "open", "open")
        + _span(_AAOW + "finalize", "finalize")
        + _span(_AAOW + "open", "open")
        # close(finalize_on_close=True) does not open a nested finalize span.
        + _span(_AAOW + "close", "finalize")
    )
    first_session.finalize.assert_awaited_once_with(7)


# --------------------------------------- #18627 download_ranges destinations


@pytest.mark.asyncio
async def test_mrd_uds_buffer_destinations_follow_gapic_contract(client, uds_selected):
    data = bytes(range(256)) * 4
    session = _read_session(size=len(data), data=data)
    mrd = await _open_mrd(client, session)

    class Collector:
        def __init__(self):
            self.chunks = []

        def write(self, chunk):
            self.chunks.append(chunk)

    target = bytearray(16)
    collector = Collector()
    stream = io.BytesIO()
    await mrd.download_ranges(
        [(0, 16, target), (16, 8, collector), (24, 4, stream)],
        accepts_memoryview=True,
    )
    assert target == data[:16]
    # Custom write() destinations always get bytes: shared-memory views are only
    # valid during write(), even with accepts_memoryview=True.
    assert collector.chunks == [data[16:24]]
    assert all(type(c) is bytes for c in collector.chunks)
    assert stream.getvalue() == data[24:28]
    writers = [writer for _, _, writer in session.seen]
    assert isinstance(writers[0], _BufferWriter)
    assert isinstance(writers[1], _BytesWriter)
    assert writers[2] is stream  # stdlib streams copy synchronously
    target.extend(b"!")  # the buffer export was released


@pytest.mark.asyncio
async def test_mrd_uds_short_read_into_buffer_raises_buffer_error(client, uds_selected):
    session = _read_session(size=10, data=b"0123456789")
    mrd = await _open_mrd(client, session)
    target = bytearray(16)
    with pytest.raises(BufferError, match="expected 16 bytes at offset 4, got 6"):
        await mrd.download_ranges([(4, 16, target)])
    assert target[:6] == b"456789"
    target.extend(b"!")  # released even on error
    assert mrd.is_stream_open


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "destination,length,match",
    [
        (bytearray(4), 0, "requires bytes_to_read > 0"),
        (b"read-only", 4, "writable, C-contiguous"),
        (bytearray(2), 4, "smaller than bytes_to_read"),
    ],
)
async def test_mrd_uds_invalid_buffer_destination_raises_before_reading(
    client, uds_selected, destination, length, match
):
    session = _read_session()
    mrd = await _open_mrd(client, session)
    with pytest.raises(ValueError, match=match):
        await mrd.download_ranges([(0, 8, bytearray(8)), (0, length, destination)])
    session.download_ranges.assert_not_awaited()


@pytest.mark.asyncio
async def test_mrd_uds_open_keeps_requested_generation_when_unset(client, uds_selected):
    session = _read_session(generation=0, size=0)
    mrd = await _open_mrd(client, session, generation=None)
    assert mrd.generation is None and mrd.persisted_size == 0


# ----------------------------------------------- #18641 Preconditions in UDS


def _writer(**kwargs):
    return AsyncAppendableObjectWriter(mock.MagicMock(), "b", "o", **kwargs)


_ALL = Preconditions(
    if_generation_match=1,
    if_generation_not_match=2,
    if_metageneration_match=3,
    if_metageneration_not_match=4,
)


def test_uds_open_spec_create_maps_all_preconditions():
    spec = _writer(preconditions=_ALL)._uds_open_spec(None)
    assert not spec.HasField("reopen_generation")
    assert (
        spec.if_generation_match,
        spec.if_generation_not_match,
        spec.if_metageneration_match,
        spec.if_metageneration_not_match,
    ) == (1, 2, 3, 4)


def test_uds_open_spec_create_if_generation_match_zero_overrides_nothing():
    spec = _writer(preconditions=Preconditions(if_generation_match=0))._uds_open_spec(
        None
    )
    assert spec.HasField("if_generation_match") and spec.if_generation_match == 0
    assert not spec.HasField("if_generation_not_match")


def test_uds_open_spec_create_without_generation_preconditions():
    spec = _writer(
        preconditions=Preconditions(if_metageneration_not_match=5)
    )._uds_open_spec(None)
    assert not spec.HasField("if_generation_match")
    assert not spec.HasField("if_metageneration_match")
    assert spec.if_metageneration_not_match == 5


def test_uds_open_spec_generation_zero_with_metageneration_precondition():
    spec = _writer(
        generation=0, preconditions=Preconditions(if_metageneration_match=6)
    )._uds_open_spec(None)
    assert spec.if_generation_match == 0
    assert spec.if_metageneration_match == 6
    assert not spec.HasField("if_generation_not_match")


@pytest.mark.parametrize(
    "preconditions,expected",
    [
        (Preconditions(if_metageneration_match=3), (3, None)),
        (Preconditions(if_metageneration_not_match=4), (None, 4)),
        (
            Preconditions(if_metageneration_match=3, if_metageneration_not_match=4),
            (3, 4),
        ),
        (Preconditions(), (None, None)),
        (None, (None, None)),
    ],
)
def test_uds_open_spec_reopen_maps_metageneration_preconditions(
    preconditions, expected
):
    spec = _writer(generation=9, preconditions=preconditions)._uds_open_spec(
        [("x-goog-custom", "ignored")]
    )
    assert spec.reopen_generation == 9
    assert not spec.write_handle and not spec.routing_token
    assert not spec.quota_project
    got = tuple(
        getattr(spec, f) if spec.HasField(f) else None
        for f in ("if_metageneration_match", "if_metageneration_not_match")
    )
    assert got == expected
    assert not spec.HasField("if_generation_match")
    assert not spec.HasField("if_generation_not_match")


def test_uds_open_spec_skips_preconditions_for_created_generation():
    writer = _writer(preconditions=_ALL)
    writer._created_generation = True
    writer.generation = 77
    spec = writer._uds_open_spec(None)
    assert spec.reopen_generation == 77
    assert not spec.HasField("if_metageneration_match")
    assert not spec.HasField("if_metageneration_not_match")


@pytest.mark.parametrize(
    "kwargs,match",
    [
        (
            {"generation": 5, "preconditions": Preconditions(if_generation_match=5)},
            "require generation=None",
        ),
        (
            {
                "write_handle": _storage_v2.BidiWriteHandle(handle=b"h"),
                "preconditions": Preconditions(if_metageneration_match=1),
            },
            "cannot be combined with write_handle",
        ),
    ],
)
def test_invalid_preconditions_raise_before_any_uds_open(uds_selected, kwargs, match):
    with mock.patch(_WRITE_SESSION) as session_cls:
        with pytest.raises(ValueError, match=match):
            _writer(**kwargs)
    session_cls.assert_not_called()


@pytest.mark.asyncio
async def test_writer_uds_open_create_then_reopen_drops_preconditions(
    client, uds_selected
):
    session = _write_session(generation=1001, persisted_size=0)
    writer = await _open_writer(client, session, preconditions=_ALL)
    create_spec = session.open.call_args.args[0]
    assert create_spec.if_generation_match == 1
    assert writer._created_generation and writer.generation == 1001

    await writer.close()
    reopen = _write_session(generation=1001, persisted_size=11)
    with mock.patch(_WRITE_SESSION, return_value=reopen):
        await writer.open()
    reopen_spec = reopen.open.call_args.args[0]
    assert reopen_spec.reopen_generation == 1001
    assert not reopen_spec.HasField("if_metageneration_match")
    assert writer.offset == 11


@pytest.mark.asyncio
async def test_writer_uds_reopen_keeps_metageneration_preconditions(
    client, uds_selected
):
    session = _write_session(generation=9, persisted_size=3)
    writer = await _open_writer(
        client,
        session,
        generation=9,
        preconditions=Preconditions(if_metageneration_match=2),
    )
    spec = session.open.call_args.args[0]
    assert spec.reopen_generation == 9 and spec.if_metageneration_match == 2
    assert not writer._created_generation


@pytest.mark.asyncio
async def test_writer_uds_open_without_generation_in_response(client, uds_selected):
    writer = await _open_writer(client, _write_session(generation=0))
    assert writer.generation is None and not writer._created_generation


@pytest.mark.asyncio
async def test_writer_uds_precondition_failure_propagates(client, uds_selected):
    session = _write_session()
    session.open.side_effect = exceptions.FailedPrecondition("metageneration")
    writer = AsyncAppendableObjectWriter(client, _BUCKET, "o", preconditions=_ALL)
    with mock.patch(_WRITE_SESSION, return_value=session):
        with pytest.raises(exceptions.FailedPrecondition):
            await writer.open()
    assert not writer.is_stream_open and writer._uds is None


# ------------------------------------------------------- remaining UDS hooks


@pytest.mark.asyncio
@pytest.mark.parametrize("mode", ["auto", "force"])
async def test_writer_runtime_unavailable(client, mode):
    get_rt = AsyncMock(side_effect=CoreSdkUnavailableError("socket gone"))
    with (
        mock.patch(f"{_AAOW_MOD}._uds_selected", return_value=True),
        mock.patch(f"{_AAOW_MOD}._AsyncWriteObjectStream") as write_stream_cls,
        mock.patch(_RUNTIME_GET, get_rt),
        mock.patch(
            "google.cloud.storage.asyncio._uds._config.uds_mode", return_value=mode
        ),
    ):
        stream = write_stream_cls.return_value
        stream.open = AsyncMock()
        stream.generation_number = 3
        stream.write_handle = None
        stream.persisted_size = 0
        writer = AsyncAppendableObjectWriter(client, _BUCKET, "o")
        if mode == "force":
            with pytest.raises(CoreSdkUnavailableError, match="socket gone"):
                await writer.open()
            write_stream_cls.assert_not_called()
        else:
            await writer.open()
            write_stream_cls.assert_called_once()
            assert writer._uds is None and writer.generation == 3


@pytest.mark.asyncio
async def test_writer_uds_append_casts_non_byte_buffers(client, uds_selected):
    session = _write_session()
    writer = await _open_writer(client, session)
    await writer.append(array.array("I", [1, 2, 3]))
    (view,) = session.append.await_args.args
    assert view.format == "B" and len(view) == 12
    assert writer.offset == 12


@pytest.mark.asyncio
async def test_writer_uds_state_lookup_without_known_size(client, uds_selected):
    session = _write_session(persisted_size=4)
    session.last_persisted_size = None
    writer = await _open_writer(client, session)
    assert await writer.state_lookup() == 4
    session.flush.assert_not_awaited()


def test_uds_open_spec_blob_without_optional_attrs_and_with_contexts():
    from google.cloud.storage.blob import Blob
    from google.cloud.storage.bucket import Bucket

    blob = Blob("o", bucket=Bucket(client=None, name="b"))
    spec = AsyncAppendableObjectWriter.from_blob(mock.MagicMock(), blob)._uds_open_spec(
        None
    )
    assert not spec.attrs.metadata and not spec.attrs.custom_time_secs
    assert not spec.attrs.contexts_json

    blob._properties["contexts"] = {"custom": {"team": {"value": "storage"}}}
    blob.custom_time = datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)
    spec = AsyncAppendableObjectWriter.from_blob(mock.MagicMock(), blob)._uds_open_spec(
        None
    )
    assert spec.attrs.contexts_json == (b'{"custom": {"team": {"value": "storage"}}}')
    assert spec.attrs.custom_time_secs == 1767225600


# ----------------------------------------------------- AsyncGrpcClient hooks


def test_attempt_direct_path_default_sentinel_behaves_as_true():
    sentinel = async_grpc_client._ATTEMPT_DIRECT_PATH_DEFAULT
    assert bool(sentinel) is True
    assert repr(sentinel) == "True"


def test_prewarm_uds_ensures_server_on_background_thread():
    client = mock.Mock()
    started = []

    class _InlineThread:
        def __init__(self, target, name, daemon):
            started.append((name, daemon))
            self._target = target

        def start(self):
            self._target()

    with (
        mock.patch("threading.Thread", _InlineThread),
        mock.patch(
            "google.cloud.storage.asyncio._uds.runtime._client_config",
            return_value=("https://storage.example.com", False, None, ""),
        ) as client_config,
        mock.patch(
            "google.cloud.storage.asyncio._uds.server_manager.ServerManager"
        ) as manager_cls,
    ):
        async_grpc_client._prewarm_uds(client)
    assert started == [("gcs-uds-prewarm", True)]
    client_config.assert_called_once_with(client)
    manager_cls.assert_called_once_with(endpoint="https://storage.example.com")
    manager_cls.return_value.ensure_server.assert_called_once_with()
