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

"""Self-test for the fake GCS gRPC server, driven by the GAPIC async client."""

import asyncio
import os

import google_crc32c
import grpc
import pytest
import pytest_asyncio
from google.api_core import exceptions as api_exceptions
from google.auth import credentials as auth_credentials
from google.rpc import code_pb2, status_pb2

from google.cloud import _storage_v2
from google.cloud._storage_v2.services.storage.transports import (
    StorageGrpcAsyncIOTransport,
)

from .fake_gcs_server import MAX_READ_CHUNK_SIZE, start_fake_gcs

BUCKET = "projects/_/buckets/test-bucket"


def _crc(data: bytes) -> int:
    return google_crc32c.value(data)


class _Stream:
    """Drives a GAPIC bidi call with explicit send / recv / done_writing."""

    def __init__(self, method):
        self._queue: asyncio.Queue = asyncio.Queue()

        async def requests():
            while True:
                request = await self._queue.get()
                if request is None:
                    return
                yield request

        self._pending = method(requests=requests())
        self.call = None

    async def send(self, request):
        await self._queue.put(request)
        if self.call is None:
            # The async GAPIC callable returns an awaitable resolving to the call.
            self.call = await self._pending

    async def recv(self):
        return await asyncio.wait_for(self.call.read(), timeout=10)

    async def done_writing(self):
        await self._queue.put(None)


@pytest_asyncio.fixture
async def fake():
    endpoint, server, state = await start_fake_gcs()
    channel = grpc.aio.insecure_channel(endpoint[len("http://") :])
    transport = StorageGrpcAsyncIOTransport(
        channel=channel, credentials=auth_credentials.AnonymousCredentials()
    )
    client = _storage_v2.StorageAsyncClient(transport=transport)
    try:
        yield endpoint, state, client
    finally:
        await channel.close()
        await server.stop(None)


def _write_stream(client):
    return _Stream(client.bidi_write_object)


def _read_stream(client):
    return _Stream(client.bidi_read_object)


def _data(content: bytes, offset: int, **kwargs):
    return _storage_v2.BidiWriteObjectRequest(
        write_offset=offset,
        checksummed_data=_storage_v2.ChecksummedData(
            content=content, crc32c=_crc(content)
        ),
        **kwargs,
    )


def _open_spec(name, **kwargs):
    return _storage_v2.WriteObjectSpec(
        resource=_storage_v2.Object(bucket=BUCKET, name=name),
        appendable=True,
        **kwargs,
    )


async def _read_all(client, name, ranges, generation=None):
    """Opens a BidiReadObject, requests ``ranges`` and collects the data."""
    spec = _storage_v2.BidiReadObjectSpec(bucket=BUCKET, object=name)
    if generation is not None:
        spec.generation = generation
    stream = _read_stream(client)
    await stream.send(
        _storage_v2.BidiReadObjectRequest(
            read_object_spec=spec,
            read_ranges=[
                _storage_v2.ReadRange(read_offset=o, read_length=l, read_id=i)
                for i, (o, l) in enumerate(ranges)
            ],
        )
    )
    first = await stream.recv()
    assert first.metadata.name == name
    assert first.read_handle.handle
    pending = set(range(len(ranges)))
    chunks = {i: [] for i in pending}
    while pending:
        response = await stream.recv()
        for rd in response.object_data_ranges:
            chunks[rd.read_range.read_id].append(rd)
            if rd.range_end:
                pending.remove(rd.read_range.read_id)
    await stream.done_writing()
    return first.metadata, chunks


def _join(range_chunks):
    return b"".join(rd.checksummed_data.content for rd in range_chunks)


@pytest.mark.asyncio
async def test_binds_loopback_only(fake):
    endpoint, _, _ = fake
    assert endpoint.startswith("http://127.0.0.1:")
    assert int(endpoint.rsplit(":", 1)[1]) > 0


@pytest.mark.asyncio
async def test_appendable_write_flush_finalize_and_read(fake):
    _, state, client = fake
    name = "appendable"
    payload = os.urandom(5 * 1024 * 1024 + 123)

    stream = _write_stream(client)
    # The first request carries the spec plus an initial chunk, like the Rust
    # client's open_appendable_object().send_and_append().
    first_chunk = payload[:1000]
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(
            write_object_spec=_open_spec(name, if_generation_match=0),
            write_offset=0,
            checksummed_data=_storage_v2.ChecksummedData(
                content=first_chunk, crc32c=_crc(first_chunk)
            ),
        )
    )
    handshake = await stream.recv()
    assert "resource" in handshake
    assert handshake.resource.generation > 0
    assert handshake.resource.size == len(first_chunk)
    assert not handshake.resource.finalize_time
    assert handshake.write_handle.handle
    assert handshake.persisted_data_checksums.crc32c == _crc(first_chunk)
    generation = handshake.resource.generation

    # The appendable object is visible while being written.
    obj = await client.get_object(
        request=_storage_v2.GetObjectRequest(bucket=BUCKET, object=name)
    )
    assert obj.generation == generation
    assert obj.size == len(first_chunk)
    assert "checksums" not in obj

    # Append in 2 MiB chunks; flush alone produces no response.
    offset = len(first_chunk)
    step = 2 * 1024 * 1024
    while offset < len(payload):
        chunk = payload[offset : offset + step]
        await stream.send(_data(chunk, offset))
        offset += len(chunk)
        await stream.send(_storage_v2.BidiWriteObjectRequest(flush=True, write_offset=offset))
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(
            flush=True, state_lookup=True, write_offset=offset
        )
    )
    lookup = await stream.recv()
    assert "persisted_size" in lookup
    assert lookup.persisted_size == len(payload)
    assert lookup.write_handle.handle

    await stream.send(
        _storage_v2.BidiWriteObjectRequest(
            finish_write=True,
            flush=True,
            write_offset=offset,
            object_checksums=_storage_v2.ObjectChecksums(crc32c=_crc(payload)),
        )
    )
    final = await stream.recv()
    assert "resource" in final
    assert final.resource.size == len(payload)
    assert final.resource.generation == generation
    assert final.resource.finalize_time
    assert final.resource.checksums.crc32c == _crc(payload)
    await stream.done_writing()
    assert await stream.recv() is grpc.aio.EOF

    stored = state.get_object(BUCKET, name)
    assert stored.finalized and bytes(stored.data) == payload

    # Full read + ranged + tail + zero-length-at-EOF reads in one stream.
    metadata, chunks = await _read_all(
        client,
        name,
        [(0, 0), (10, 100), (-50, 0), (len(payload), 0), (step - 5, step + 10)],
        generation=generation,
    )
    assert metadata.size == len(payload)
    assert metadata.generation == generation
    assert metadata.finalize_time
    assert metadata.checksums.crc32c == _crc(payload)

    full = chunks[0]
    assert len(full) == 3  # 2 MiB + 2 MiB + remainder.
    assert all(len(rd.checksummed_data.content) <= MAX_READ_CHUNK_SIZE for rd in full)
    assert [rd.range_end for rd in full] == [False, False, True]
    expected_offset = 0
    for rd in full:
        assert rd.read_range.read_offset == expected_offset
        assert rd.read_range.read_length == len(rd.checksummed_data.content)
        assert rd.checksummed_data.crc32c == _crc(rd.checksummed_data.content)
        expected_offset += rd.read_range.read_length
    assert _join(full) == payload
    assert _join(chunks[1]) == payload[10:110]
    assert _join(chunks[2]) == payload[-50:]
    assert len(chunks[3]) == 1 and chunks[3][0].range_end
    assert "checksummed_data" not in chunks[3][0]
    assert chunks[3][0].read_range.read_offset == len(payload)
    assert _join(chunks[4]) == payload[step - 5 : 2 * step + 5]


@pytest.mark.asyncio
async def test_if_generation_match_zero_on_existing_object(fake):
    _, state, client = fake
    state.put_object(BUCKET, "exists", b"abc")
    stream = _write_stream(client)
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(
            write_object_spec=_open_spec("exists", if_generation_match=0)
        )
    )
    with pytest.raises(api_exceptions.FailedPrecondition):
        await stream.recv()


@pytest.mark.asyncio
async def test_write_chunk_crc32c_mismatch(fake):
    _, state, client = fake
    stream = _write_stream(client)
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(write_object_spec=_open_spec("bad-crc"))
    )
    await stream.recv()
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(
            write_offset=0,
            checksummed_data=_storage_v2.ChecksummedData(
                content=b"hello", crc32c=_crc(b"hello") ^ 1
            ),
            state_lookup=True,
        )
    )
    with pytest.raises(api_exceptions.InvalidArgument):
        await stream.recv()
    assert state.get_object(BUCKET, "bad-crc").size == 0


@pytest.mark.asyncio
async def test_finalize_object_checksum_mismatch(fake):
    _, state, client = fake
    stream = _write_stream(client)
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(write_object_spec=_open_spec("bad-full"))
    )
    await stream.recv()
    await stream.send(_data(b"hello", 0))
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(
            finish_write=True,
            flush=True,
            write_offset=5,
            object_checksums=_storage_v2.ObjectChecksums(crc32c=_crc(b"hellx")),
        )
    )
    with pytest.raises(api_exceptions.InvalidArgument):
        await stream.recv()
    assert not state.get_object(BUCKET, "bad-full").finalized


@pytest.mark.asyncio
async def test_write_offset_mismatch(fake):
    _, _, client = fake
    stream = _write_stream(client)
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(write_object_spec=_open_spec("gap"))
    )
    await stream.recv()
    await stream.send(_data(b"hello", 3, state_lookup=True))
    with pytest.raises(api_exceptions.OutOfRange):
        await stream.recv()


@pytest.mark.asyncio
async def test_close_unfinalized_then_takeover_append(fake):
    _, state, client = fake
    name = "takeover"
    stream = _write_stream(client)
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(write_object_spec=_open_spec(name))
    )
    handshake = await stream.recv()
    generation = handshake.resource.generation
    assert handshake.resource.size == 0
    await stream.send(_data(b"hello ", 0, flush=True))
    await stream.done_writing()
    # Closing an unfinalized upload yields a final persisted-size response.
    closing = await stream.recv()
    assert closing.persisted_size == 6
    assert await stream.recv() is grpc.aio.EOF

    # A second writer takes over the same generation (AppendObjectSpec).
    old = _write_stream(client)
    await old.send(
        _storage_v2.BidiWriteObjectRequest(
            append_object_spec=_storage_v2.AppendObjectSpec(
                bucket=BUCKET, object=name, generation=generation
            ),
            state_lookup=True,
        )
    )
    await old.recv()

    new = _write_stream(client)
    await new.send(
        _storage_v2.BidiWriteObjectRequest(
            append_object_spec=_storage_v2.AppendObjectSpec(
                bucket=BUCKET,
                object=name,
                generation=generation,
                write_handle=handshake.write_handle,
            ),
            state_lookup=True,
        )
    )
    reopened = await new.recv()
    assert reopened.resource.generation == generation
    assert reopened.resource.size == 6
    assert reopened.persisted_data_checksums.crc32c == _crc(b"hello ")
    assert reopened.write_handle.handle

    # The superseded writer is rejected.
    await old.send(_data(b"zzz", 6, state_lookup=True))
    with pytest.raises(api_exceptions.FailedPrecondition):
        await old.recv()

    await new.send(_data(b"world", 6))
    await new.send(
        _storage_v2.BidiWriteObjectRequest(
            finish_write=True,
            flush=True,
            write_offset=11,
            object_checksums=_storage_v2.ObjectChecksums(crc32c=_crc(b"hello world")),
        )
    )
    final = await new.recv()
    assert final.resource.size == 11 and final.resource.finalize_time
    await new.done_writing()
    assert await new.recv() is grpc.aio.EOF

    _, chunks = await _read_all(client, name, [(0, 0)])
    assert _join(chunks[0]) == b"hello world"

    # Finalized objects cannot be taken over.
    again = _write_stream(client)
    await again.send(
        _storage_v2.BidiWriteObjectRequest(
            append_object_spec=_storage_v2.AppendObjectSpec(
                bucket=BUCKET, object=name, generation=generation
            ),
            state_lookup=True,
        )
    )
    with pytest.raises(api_exceptions.FailedPrecondition):
        await again.recv()


@pytest.mark.asyncio
async def test_non_appendable_write_visible_only_after_finalize(fake):
    _, state, client = fake
    stream = _write_stream(client)
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(
            write_object_spec=_storage_v2.WriteObjectSpec(
                resource=_storage_v2.Object(
                    bucket=BUCKET, name="plain", content_type="text/plain"
                )
            )
        )
    )
    await stream.recv()
    assert state.get_object(BUCKET, "plain") is None
    await stream.send(
        _data(
            b"abc",
            0,
            finish_write=True,
            object_checksums=_storage_v2.ObjectChecksums(crc32c=_crc(b"abc")),
        )
    )
    final = await stream.recv()
    assert final.resource.size == 3 and final.resource.finalize_time
    assert final.resource.content_type == "text/plain"
    assert state.get_object(BUCKET, "plain").finalized


@pytest.mark.asyncio
async def test_read_out_of_range_has_bidi_read_object_error(fake):
    _, state, client = fake
    state.put_object(BUCKET, "small", b"0123456789")
    stream = _read_stream(client)
    await stream.send(
        _storage_v2.BidiReadObjectRequest(
            read_object_spec=_storage_v2.BidiReadObjectSpec(
                bucket=BUCKET, object="small"
            )
        )
    )
    first = await stream.recv()
    assert first.metadata.size == 10
    await stream.send(
        _storage_v2.BidiReadObjectRequest(
            read_ranges=[_storage_v2.ReadRange(read_offset=11, read_length=1, read_id=7)]
        )
    )
    with pytest.raises(api_exceptions.OutOfRange):
        await stream.recv()
    trailing = await stream.call._call.trailing_metadata()
    raw = dict(trailing)["grpc-status-details-bin"]
    status = status_pb2.Status.FromString(raw)
    assert status.code == code_pb2.OUT_OF_RANGE
    assert len(status.details) == 1
    error_pb = _storage_v2.BidiReadObjectError.pb()()
    assert status.details[0].Unpack(error_pb)
    error = _storage_v2.BidiReadObjectError.wrap(error_pb)
    assert [e.read_id for e in error.read_range_errors] == [7]
    assert error.read_range_errors[0].status.code == code_pb2.OUT_OF_RANGE


@pytest.mark.asyncio
async def test_read_chunk_crc32c_corruption_hook(fake):
    _, state, client = fake
    state.put_object(BUCKET, "corrupt", b"payload")
    state.corrupt_next_read_chunks(1)
    _, chunks = await _read_all(client, "corrupt", [(0, 0), (0, 0)])
    first, second = chunks[0][0], chunks[1][0]
    assert first.checksummed_data.content == b"payload"
    assert first.checksummed_data.crc32c != _crc(b"payload")
    assert second.checksummed_data.crc32c == _crc(b"payload")


@pytest.mark.asyncio
async def test_object_crc32c_corruption_hook(fake):
    _, state, client = fake
    state.put_object(BUCKET, "meta-corrupt", b"payload")
    state.corrupt_object_crc32c(BUCKET, "meta-corrupt")
    metadata, chunks = await _read_all(client, "meta-corrupt", [(0, 0)])
    assert metadata.checksums.crc32c != _crc(b"payload")
    assert chunks[0][0].checksummed_data.crc32c == _crc(b"payload")


@pytest.mark.asyncio
async def test_get_delete_and_not_found(fake):
    _, state, client = fake
    seeded = state.put_object(BUCKET, "obj", b"xyz", content_type="a/b")
    got = await client.get_object(
        request=_storage_v2.GetObjectRequest(bucket=BUCKET, object="obj")
    )
    assert got.size == 3 and got.content_type == "a/b"
    assert got.checksums.crc32c == _crc(b"xyz")
    with pytest.raises(api_exceptions.NotFound):
        await client.get_object(
            request=_storage_v2.GetObjectRequest(
                bucket=BUCKET, object="obj", generation=seeded.generation + 1
            )
        )
    await client.delete_object(
        request=_storage_v2.DeleteObjectRequest(bucket=BUCKET, object="obj")
    )
    with pytest.raises(api_exceptions.NotFound):
        await client.get_object(
            request=_storage_v2.GetObjectRequest(bucket=BUCKET, object="obj")
        )
    with pytest.raises(api_exceptions.NotFound):
        await client.delete_object(
            request=_storage_v2.DeleteObjectRequest(bucket=BUCKET, object="obj")
        )
    stream = _read_stream(client)
    await stream.send(
        _storage_v2.BidiReadObjectRequest(
            read_object_spec=_storage_v2.BidiReadObjectSpec(bucket=BUCKET, object="obj")
        )
    )
    with pytest.raises(api_exceptions.NotFound):
        await stream.recv()


@pytest.mark.asyncio
async def test_inject_error(fake):
    _, state, client = fake
    state.put_object(BUCKET, "obj", b"xyz")
    state.inject_error("GetObject", grpc.StatusCode.UNAVAILABLE)
    with pytest.raises(api_exceptions.ServiceUnavailable):
        await client.get_object(
            request=_storage_v2.GetObjectRequest(bucket=BUCKET, object="obj"),
            retry=None,
        )
    got = await client.get_object(
        request=_storage_v2.GetObjectRequest(bucket=BUCKET, object="obj")
    )
    assert got.size == 3

    # Mid-stream failure: the second request on the write stream fails.
    state.inject_error("BidiWriteObject", grpc.StatusCode.UNAVAILABLE, after_requests=1)
    stream = _write_stream(client)
    await stream.send(
        _storage_v2.BidiWriteObjectRequest(write_object_spec=_open_spec("mid"))
    )
    await stream.recv()
    await stream.send(_data(b"abc", 0, state_lookup=True))
    with pytest.raises(api_exceptions.ServiceUnavailable):
        await stream.recv()
    assert state.get_object(BUCKET, "mid").size == 0
    assert len(state.requests_for("BidiWriteObject")) == 2
