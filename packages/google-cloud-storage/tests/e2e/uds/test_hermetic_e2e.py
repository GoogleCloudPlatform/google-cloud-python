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

"""Hermetic end-to-end tests for the gRPC-over-UDS backend.

Chain under test::

    public Python API (AsyncAppendableObjectWriter / AsyncMultiRangeDownloader)
        -> gcs-core-server (real Rust binary, spawned per test in ``child`` mode)
        -> fake ``google.storage.v2.Storage`` gRPC server (``fake_gcs_server``)

``GOOGLE_CLOUD_STORAGE_UDS_BINARY`` must point at a built ``gcs-core-server``;
the tests fail (never skip) when it is missing.
"""

import asyncio
import os
import shutil
import tempfile
from io import BytesIO

import google_crc32c
import pytest
import pytest_asyncio
from google.api_core import exceptions
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials

from google.cloud.storage.asyncio.async_appendable_object_writer import (
    AsyncAppendableObjectWriter,
    Preconditions,
)
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from google.cloud.storage.exceptions import DataCorruption

from .fake_gcs_server import start_fake_gcs

BUCKET = "test-bucket"
MiB = 1024 * 1024
BINARY_ENV = "GOOGLE_CLOUD_STORAGE_UDS_BINARY"


def _crc(data: bytes) -> int:
    return google_crc32c.value(data)


def _payload(size: int, seed: int = 0) -> bytes:
    # Deterministic, non-repeating-per-2MiB content so misplaced bytes are caught.
    block = bytes((i * 31 + seed) % 251 for i in range(4093))
    return (block * (size // len(block) + 1))[:size]


@pytest.fixture(params=["shm", "inline"])
def transport_mode(request):
    return request.param


@pytest_asyncio.fixture
async def e2e(monkeypatch):
    """Starts the fake GCS + a per-test gcs-core-server and yields a client."""
    binary = os.environ.get(BINARY_ENV)
    assert binary, (
        f"{BINARY_ENV} must point at a built gcs-core-server binary "
        "(e.g. google-cloud-rust/target/release/gcs-core-server)"
    )
    assert os.access(binary, os.X_OK), f"{BINARY_ENV}={binary} is not executable"

    # A short private runtime dir keeps socket paths well under the AF_UNIX limit
    # and isolates daemons / logs per test.
    runtime_root = tempfile.mkdtemp(prefix="gcsuds-")
    monkeypatch.setenv("XDG_RUNTIME_DIR", runtime_root)
    monkeypatch.setenv("GOOGLE_CLOUD_STORAGE_FORCE_USE_CORE_SDK", "1")
    monkeypatch.setenv("GOOGLE_CLOUD_STORAGE_UDS_MODE", "child")
    monkeypatch.delenv("GOOGLE_CLOUD_STORAGE_UDS_SOCKET", raising=False)
    monkeypatch.delenv("GOOGLE_CLOUD_STORAGE_UDS_SHM", raising=False)

    endpoint, server, state = await start_fake_gcs()
    client = AsyncGrpcClient(
        credentials=AnonymousCredentials(),
        client_options=ClientOptions(api_endpoint=endpoint[len("http://") :]),
        attempt_direct_path=False,
    )
    try:
        yield client, state
    finally:
        from google.cloud.storage.asyncio._uds import runtime

        processes = [
            rt.manager.process
            for rt in list(runtime._instances.values())
            if rt.manager is not None and rt.manager.process is not None
        ]
        await runtime.close_all()
        await server.stop(None)
        # Child-mode daemons die with their parent; stop them eagerly so tests
        # don't accumulate daemons.
        for proc in processes:
            if proc.poll() is None:
                proc.terminate()
                try:
                    await asyncio.get_running_loop().run_in_executor(
                        None, lambda p=proc: p.wait(timeout=10)
                    )
                except Exception:
                    proc.kill()
        _dump_daemon_logs_on_failure(runtime_root)
        shutil.rmtree(runtime_root, ignore_errors=True)


def _dump_daemon_logs_on_failure(runtime_root: str) -> None:
    """Prints gcs-core-server logs (captured by pytest, shown on failure)."""
    log_dir = os.path.join(runtime_root, "gcs-core")
    if not os.path.isdir(log_dir):
        return
    for name in sorted(os.listdir(log_dir)):
        if name.endswith(".log"):
            with open(os.path.join(log_dir, name), "rb") as f:
                print(f"----- {name} -----")
                print(f.read()[-20000:].decode("utf-8", "replace"))


def _set_transport(monkeypatch, transport_mode):
    if transport_mode == "inline":
        monkeypatch.setenv("GOOGLE_CLOUD_STORAGE_UDS_SHM", "off")


def _assert_via_rust(state, method):
    """Asserts the fake saw ``method`` calls, all issued by the Rust SDK."""
    calls = [md for m, md in state.call_metadata if m == method]
    assert calls, f"the fake GCS server saw no {method} calls"
    for md in calls:
        assert "gl-rust/" in md.get("x-goog-api-client", ""), md


async def _write_object(client, name, data, *, finalize=True):
    writer = AsyncAppendableObjectWriter(client, BUCKET, name)
    await writer.open()
    assert writer._uds is not None, "writer did not take the Rust (UDS) path"
    await writer.append(data)
    if finalize:
        obj = await writer.finalize(full_object_checksum=_crc(data))
        return writer, obj
    size = await writer.close()
    return writer, size


async def _open_mrd(client, name, **kwargs):
    mrd = await AsyncMultiRangeDownloader.create_mrd(client, BUCKET, name, **kwargs)
    assert mrd._uds is not None, "MRD did not take the Rust (UDS) path"
    return mrd


@pytest.mark.asyncio
async def test_appendable_writer_lifecycle(e2e, monkeypatch, transport_mode):
    _set_transport(monkeypatch, transport_mode)
    client, state = e2e
    name = f"aaow-{transport_mode}"
    data = _payload(10 * MiB + 12345, seed=1)

    # open / append in uneven slices / flush / close.
    writer = AsyncAppendableObjectWriter(client, BUCKET, name)
    await writer.open()
    assert writer._uds is not None, "writer did not take the Rust (UDS) path"
    assert writer.generation
    generation = writer.generation
    assert writer.persisted_size == 0
    first_part = 6 * MiB + 777
    slices = [1, 4095, 1 * MiB + 3, 333_333, 2 * MiB, 5]
    pos = 0
    for n in slices:
        await writer.append(data[pos : pos + n])
        pos += n
    await writer.append(data[pos:first_part])
    pos = first_part
    persisted = await writer.flush()
    assert persisted == first_part
    assert await writer.close() == first_part
    assert writer.is_stream_open is False

    stored = state.get_object(BUCKET, name)
    assert stored.generation == generation
    assert not stored.finalized
    assert bytes(stored.data) == data[:first_part]

    # Reopen the same generation (takeover) and finalize with the right crc.
    writer = AsyncAppendableObjectWriter(client, BUCKET, name, generation=generation)
    await writer.open()
    assert writer._uds is not None
    assert writer.generation == generation
    assert writer.persisted_size == first_part
    for n in (999_999, 3, 1 * MiB):
        await writer.append(data[pos : pos + n])
        pos += n
    await writer.append(data[pos:])
    obj = await writer.finalize(full_object_checksum=_crc(data))
    assert obj.size == len(data)
    assert obj.generation == generation
    assert obj.checksums.crc32c == _crc(data)
    assert writer.object_resource.size == len(data)
    assert writer.persisted_size == len(data)

    stored = state.get_object(BUCKET, name)
    assert stored.finalized
    assert bytes(stored.data) == data

    _assert_via_rust(state, "BidiWriteObject")
    write_requests = state.requests_for("BidiWriteObject")
    assert any("write_object_spec" in r for r in write_requests)
    assert any("append_object_spec" in r for r in write_requests)
    assert any(r.finish_write for r in write_requests)


@pytest.mark.asyncio
async def test_finalize_with_wrong_crc32c(e2e):
    client, state = e2e
    data = _payload(3 * MiB + 1, seed=2)
    writer = AsyncAppendableObjectWriter(client, BUCKET, "bad-crc")
    await writer.open()
    assert writer._uds is not None
    await writer.append(data)
    with pytest.raises(exceptions.InvalidArgument) as excinfo:
        await writer.finalize(full_object_checksum=_crc(data) ^ 0x1)
    assert "crc32c" in str(excinfo.value).lower()
    _assert_via_rust(state, "BidiWriteObject")


@pytest.mark.asyncio
async def test_generation_zero_on_existing_object(e2e):
    client, state = e2e
    state.put_object(BUCKET, "exists", b"already here")
    writer = AsyncAppendableObjectWriter(client, BUCKET, "exists", generation=0)
    with pytest.raises(exceptions.FailedPrecondition):
        await writer.open()
    first = state.requests_for("BidiWriteObject")[0]
    assert first.write_object_spec.if_generation_match == 0
    assert bytes(state.get_object(BUCKET, "exists").data) == b"already here"


def _write_specs(state, field):
    return [
        getattr(r, field) for r in state.requests_for("BidiWriteObject") if field in r
    ]


@pytest.mark.asyncio
async def test_preconditions_on_create_overwrite_and_reopen(e2e):
    """`Preconditions` (#18641) reach GCS through the Rust SDK on open and reopen."""
    client, state = e2e
    name = "preconditions"

    # Create: if_generation_match=0 only succeeds while no live object exists.
    writer = AsyncAppendableObjectWriter(
        client, BUCKET, name, preconditions=Preconditions(if_generation_match=0)
    )
    await writer.open()
    assert writer._uds is not None, "writer did not take the Rust (UDS) path"
    await writer.append(b"first")
    assert await writer.close() == 5
    first_gen = writer.generation
    create = _write_specs(state, "write_object_spec")[-1]
    assert "if_generation_match" in create and create.if_generation_match == 0
    with pytest.raises(exceptions.FailedPrecondition):
        await AsyncAppendableObjectWriter(
            client, BUCKET, name, preconditions=Preconditions(if_generation_match=0)
        ).open()

    # Overwrite: generation + metageneration preconditions on WriteObjectSpec.
    for bad in (
        Preconditions(if_generation_match=first_gen + 100),
        Preconditions(if_generation_not_match=first_gen),
        Preconditions(if_metageneration_match=99),
        Preconditions(if_metageneration_not_match=1),
    ):
        with pytest.raises(exceptions.FailedPrecondition):
            await AsyncAppendableObjectWriter(
                client, BUCKET, name, preconditions=bad
            ).open()
    assert state.get_object(BUCKET, name).generation == first_gen

    overwrite = AsyncAppendableObjectWriter(
        client,
        BUCKET,
        name,
        preconditions=Preconditions(
            if_generation_match=first_gen,
            if_generation_not_match=first_gen + 100,
            if_metageneration_match=1,
            if_metageneration_not_match=7,
        ),
    )
    await overwrite.open()
    await overwrite.append(b"second")
    assert await overwrite.close() == 6
    second_gen = overwrite.generation
    assert second_gen != first_gen
    spec = _write_specs(state, "write_object_spec")[-1]
    assert (
        spec.if_generation_match,
        spec.if_generation_not_match,
        spec.if_metageneration_match,
        spec.if_metageneration_not_match,
    ) == (first_gen, first_gen + 100, 1, 7)

    # Reopen (append to generation > 0): metageneration preconditions only.
    for bad in (
        Preconditions(if_metageneration_match=2),
        Preconditions(if_metageneration_not_match=1),
    ):
        with pytest.raises(exceptions.FailedPrecondition):
            await AsyncAppendableObjectWriter(
                client, BUCKET, name, generation=second_gen, preconditions=bad
            ).open()

    reopen = AsyncAppendableObjectWriter(
        client,
        BUCKET,
        name,
        generation=second_gen,
        preconditions=Preconditions(
            if_metageneration_match=1, if_metageneration_not_match=3
        ),
    )
    await reopen.open()
    assert reopen._uds is not None and reopen.persisted_size == 6
    await reopen.append(b"+more")
    obj = await reopen.finalize(full_object_checksum=_crc(b"second+more"))
    assert obj.generation == second_gen and obj.size == 11
    append = _write_specs(state, "append_object_spec")[-1]
    assert append.generation == second_gen
    assert (append.if_metageneration_match, append.if_metageneration_not_match) == (
        1,
        3,
    )
    assert bytes(state.get_object(BUCKET, name).data) == b"second+more"
    _assert_via_rust(state, "BidiWriteObject")


@pytest.mark.asyncio
async def test_mrd_reads(e2e, monkeypatch, transport_mode):
    _set_transport(monkeypatch, transport_mode)
    client, state = e2e
    name = f"mrd-{transport_mode}"
    data = _payload(7 * MiB + 4321, seed=3)
    _, obj = await _write_object(client, name, data)

    mrd = await _open_mrd(client, name)
    try:
        assert mrd.generation == obj.generation
        assert mrd.persisted_size == len(data)
        assert mrd.is_finalized is True
        assert mrd.full_obj_server_crc32c == _crc(data)

        # Several ranges in one call: full object, > 2 MiB, small, at EOF.
        full, big, small, tail = BytesIO(), BytesIO(), BytesIO(), BytesIO()
        await mrd.download_ranges(
            [
                (0, 0, full),
                (1234, 5 * MiB + 17, big),
                (len(data) - 10, 10, small),
                (len(data) - 100, 0, tail),
            ]
        )
        assert full.getvalue() == data
        assert big.getvalue() == data[1234 : 1234 + 5 * MiB + 17]
        assert small.getvalue() == data[-10:]
        assert tail.getvalue() == data[-100:]

        # Concurrent download_ranges calls on the same MRD.
        bufs = [BytesIO() for _ in range(6)]
        specs = [(i * MiB + i, MiB + 3 * i + 1) for i in range(6)]
        await asyncio.gather(
            *(
                mrd.download_ranges([(off, ln, buf)])
                for (off, ln), buf in zip(specs, bufs)
            )
        )
        for (off, ln), buf in zip(specs, bufs):
            assert buf.getvalue() == data[off : off + ln]

        # One range past EOF fails with OutOfRange while the others succeed.
        ok1, ok2, bad = BytesIO(), BytesIO(), BytesIO()
        with pytest.raises(exceptions.OutOfRange):
            await mrd.download_ranges(
                [
                    (0, 3 * MiB, ok1),
                    (len(data) + 10, 5, bad),
                    (MiB, 0, ok2),
                ]
            )
        assert ok1.getvalue() == data[: 3 * MiB]
        assert ok2.getvalue() == data[MiB:]
        assert bad.getvalue() == b""

        # The session survives the per-range error.
        again = BytesIO()
        await mrd.download_ranges([(5, 50, again)])
        assert again.getvalue() == data[5:55]
    finally:
        await mrd.close()

    _assert_via_rust(state, "BidiReadObject")
    read_requests = state.requests_for("BidiReadObject")
    assert read_requests[0].read_object_spec.object_ == name


@pytest.mark.asyncio
async def test_mrd_reads_into_buffer_destinations(e2e, monkeypatch, transport_mode):
    """Buffer-protocol destinations (#18627 contract) are filled in place."""
    _set_transport(monkeypatch, transport_mode)
    client, state = e2e
    data = _payload(3 * MiB + 17, seed=9)
    state.put_object(BUCKET, f"buffers-{transport_mode}", data)

    mrd = await _open_mrd(client, f"buffers-{transport_mode}")
    try:
        whole = bytearray(len(data))
        backing = bytearray(2 * MiB)
        middle = memoryview(backing)[MiB:]
        chunks = []

        class Collector:
            def write(self, chunk):
                chunks.append(chunk)

        await mrd.download_ranges(
            [
                (0, len(data), whole),
                (MiB + 5, MiB, middle),
                (17, 4096, Collector()),
            ],
            accepts_memoryview=True,
        )
        assert whole == data
        assert backing[MiB:] == data[MiB + 5 : 2 * MiB + 5]
        assert b"".join(chunks) == data[17 : 17 + 4096]
        assert all(type(c) is bytes for c in chunks)
        middle.release()
        whole.extend(b"!")  # exports released after the call

        short = bytearray(64)
        with pytest.raises(BufferError):
            await mrd.download_ranges([(len(data) - 10, 64, short)])
        assert short[:10] == data[-10:]
        assert mrd.is_stream_open
    finally:
        await mrd.close()
    _assert_via_rust(state, "BidiReadObject")


@pytest.mark.asyncio
async def test_mrd_reads_unfinalized_appendable_object(e2e):
    client, state = e2e
    data = _payload(3 * MiB + 5, seed=4)
    _, size = await _write_object(client, "unfinalized", data, finalize=False)
    assert size == len(data)

    mrd = await _open_mrd(client, "unfinalized")
    try:
        assert mrd.is_finalized is False
        assert mrd.full_obj_server_crc32c is None
        assert mrd.persisted_size == len(data)
        buf = BytesIO()
        await mrd.download_ranges([(0, 0, buf)])
        assert buf.getvalue() == data
        # The size of an unfinalized object is not fixed, so gcs-core-server
        # forwards the range and the (fake) service aborts the GCS stream with
        # OUT_OF_RANGE + BidiReadObjectError, like real GCS.
        with pytest.raises(exceptions.OutOfRange):
            await mrd.download_ranges([(len(data) + 10, 5, BytesIO())])
    finally:
        await mrd.close()


@pytest.mark.asyncio
async def test_mrd_chunk_checksum_mismatch_raises_data_corruption(e2e):
    client, state = e2e
    data = _payload(1 * MiB + 99, seed=5)
    state.put_object(BUCKET, "corrupt", data)

    mrd = await _open_mrd(client, "corrupt")
    state.corrupt_next_read_chunks(1)
    try:
        with pytest.raises(DataCorruption):
            await mrd.download_ranges([(0, 0, BytesIO())])
    finally:
        if mrd.is_stream_open:
            await mrd.close()
    _assert_via_rust(state, "BidiReadObject")


@pytest.mark.asyncio
async def test_mrd_not_found(e2e):
    client, _ = e2e
    with pytest.raises(exceptions.NotFound):
        await AsyncMultiRangeDownloader.create_mrd(client, BUCKET, "missing")
