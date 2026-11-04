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

"""Hermetic tests for the UDS ``BidiReadObject`` session.

A fake ``gcscore.v1.GcsCore`` gRPC server listens on a Unix domain socket and a
fake ``<socket>.shm`` side channel hands out ``memfd`` regions via ``SCM_RIGHTS``,
so the real :class:`UdsRuntime` / :class:`UdsReadSession` code paths are exercised
end to end without the ``gcs-core-server`` binary or any network access.
"""

import asyncio
import collections
import io
import mmap
import os
import random
import shutil
import socket
import struct
import tempfile
import threading

import grpc
import pytest
import pytest_asyncio
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions
from google.auth.credentials import AnonymousCredentials

from google.cloud import _storage_v2
from google.cloud.storage import __version__
from google.cloud.storage.asyncio._uds import _config, read_session, runtime
from google.cloud.storage.asyncio._uds import gcscore_pb2 as pb
from google.cloud.storage.asyncio._uds.read_session import UdsReadSession
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from google.cloud.storage.exceptions import DataCorruption

MiB = 1024 * 1024
SLOT = 2 * MiB
N_SLOTS = 4  # fewer slots than a full-object read needs => exercises ReleaseSlots
REGION_SIZE = N_SLOTS * SLOT
REGION_ID_BASE = 41
INLINE_CHUNK = 1 * MiB
GENERATION = 123
CRC32C = 0x1234ABCD
OBJ_SIZE = 10 * MiB + 123
DATA = random.Random(1234).randbytes(OBJ_SIZE)
TIMEOUT = 10
OUT_OF_RANGE = grpc.StatusCode.OUT_OF_RANGE.value[0]
INTERNAL = grpc.StatusCode.INTERNAL.value[0]


# --------------------------------------------------------------------------- infra


class _ShmListener:
    """Fake ``<socket>.shm``: one sealed-ish memfd region per connection."""

    def __init__(self, path, size):
        self.path = path
        self.size = size
        self.regions = {}  # region_id -> (conn, fd, mmap)
        self._lock = threading.Lock()
        self._next_id = REGION_ID_BASE
        self._stop = threading.Event()
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._sock.bind(path)
        self._sock.listen(16)
        self._sock.settimeout(0.05)
        self._thread = threading.Thread(target=self._serve, daemon=True)
        self._thread.start()

    def _serve(self):
        while not self._stop.is_set():
            try:
                conn, _ = self._sock.accept()
            except socket.timeout:
                continue
            fd = os.memfd_create("fake", 0)
            os.ftruncate(fd, self.size)
            mm = mmap.mmap(fd, self.size, flags=mmap.MAP_SHARED)
            with self._lock:
                region_id = self._next_id
                self._next_id += 1
                self.regions[region_id] = (conn, fd, mm)
            socket.send_fds(conn, [struct.pack("<QQ", region_id, self.size)], [fd])

    def mm(self, region_id):
        with self._lock:
            return self.regions[region_id][2]

    def region_ids(self):
        with self._lock:
            return sorted(self.regions)

    def close(self):
        self._stop.set()
        self._thread.join(timeout=5)
        self._sock.close()
        with self._lock:
            for conn, fd, mm in self.regions.values():
                mm.close()
                os.close(fd)
                conn.close()
            self.regions.clear()


class _ReadCall:
    """Server-side state of one ``BidiReadObject`` stream."""

    def __init__(self, srv, idx, context):
        self.srv = srv
        self.idx = idx
        self.context = context
        self.metadata = {m.key: m.value for m in context.invocation_metadata()}
        self.open_spec = None
        self.requests = []
        self.read_requests = []  # ReadRanges messages
        self.read_specs = []  # flattened RangeSpecs
        self.cancelled_ids = []
        self.release_requests = 0
        self.handed_out = []  # slots sent to the client
        self.released = []  # slots the client returned
        self.leased = set()
        self.reclaimed = []  # slots freed by the server when the stream ended
        self.inline_msgs = 0
        self.slot_msgs = 0
        self.tasks = {}
        self.ended = False
        self.finished = asyncio.get_running_loop().create_future()
        self._wlock = asyncio.Lock()

    @property
    def region_id(self):
        return self.open_spec.read_region_id if self.open_spec is not None else 0

    def finish(self, status=None):
        if not self.finished.done():
            self.finished.set_result(status)

    async def send(self, resp):
        async with self._wlock:
            await self.context.write(resp)

    async def send_data(self, range_id, range_offset, payload, range_end):
        if self.region_id and payload:
            slot = await self.srv.acquire_slot(self.region_id)
            self.leased.add(slot)
            self.handed_out.append(slot)
            mm = self.srv.shm.mm(self.region_id)
            mm[slot * SLOT : slot * SLOT + len(payload)] = payload
            data = pb.RangeData(
                range_id=range_id,
                range_offset=range_offset,
                slot=pb.ShmSlotRef(
                    region_id=self.region_id, slot=slot, length=len(payload)
                ),
                range_end=range_end,
            )
            self.slot_msgs += 1
        else:
            data = pb.RangeData(
                range_id=range_id,
                range_offset=range_offset,
                inline_data=bytes(payload),
                range_end=range_end,
            )
            if payload:
                self.inline_msgs += 1
        await self.send(pb.BidiReadObjectResponse(data=data))

    async def send_range_error(self, range_id, code, message, checksum_mismatch=False):
        await self.send(
            pb.BidiReadObjectResponse(
                range_error=pb.RangeError(
                    range_id=range_id,
                    code=code,
                    message=message,
                    checksum_mismatch=checksum_mismatch,
                )
            )
        )

    def on_release(self, slots):
        self.release_requests += 1
        self.released.extend(slots)
        self.srv.bogus_releases.extend(
            (self.idx, s) for s in slots if s not in self.leased
        )
        for s in self.leased.intersection(slots):
            self.leased.discard(s)
            self.srv.free_slot(self.region_id, s)

    async def serve(self, spec):
        data = self.srv.data
        action = self.srv.range_action(self.idx, spec) or ("serve",)
        kind = action[0]
        if kind == "error":
            _, code, message, checksum_mismatch = action
            await self.send_range_error(spec.range_id, code, message, checksum_mismatch)
            return
        if spec.offset > len(data):
            await self.send_range_error(
                spec.range_id, OUT_OF_RANGE, f"offset {spec.offset} > size {len(data)}"
            )
            return
        end = (
            len(data) if spec.length == 0 else min(len(data), spec.offset + spec.length)
        )
        limit = action[1] if kind in ("abort_after", "partial_hold") else None
        chunk = SLOT if self.region_id else INLINE_CHUNK
        pos = spec.offset
        while True:
            n = min(chunk, end - pos)
            if limit is not None:
                n = min(n, spec.offset + limit - pos)
            last = limit is None and pos + n >= end
            if n <= 0 and not last:
                break
            await self.send_data(spec.range_id, pos, data[pos : pos + n], last)
            pos += n
            if last:
                return
        if kind == "abort_after":
            self.finish(
                (grpc.StatusCode.UNAVAILABLE, "fake gcs-core-server restarting")
            )
        # "partial_hold": keep the range open forever.

    async def read_loop(self):
        try:
            while True:
                req = await self.context.read()
                if req is grpc.aio.EOF:
                    break
                self.requests.append(req)
                kind = req.WhichOneof("op")
                if kind == "open":
                    self.open_spec = req.open
                    self.srv.opens.append(req.open)
                    await self.send(
                        pb.BidiReadObjectResponse(
                            opened=pb.ReadOpened(object=self.srv.resource_factory())
                        )
                    )
                elif kind == "read":
                    self.read_requests.append(req.read)
                    for spec in req.read.ranges:
                        self.read_specs.append(spec)
                        self.tasks[spec.range_id] = asyncio.ensure_future(
                            self.serve(spec)
                        )
                elif kind == "release":
                    self.on_release(req.release.slots)
                else:  # "cancel": every id was announced by an earlier "read"
                    self.cancelled_ids.extend(req.cancel.range_ids)
                    for rid in req.cancel.range_ids:
                        self.tasks[rid].cancel()
        finally:
            self.finish(None)


def _default_resource():
    return pb.ObjectResource(
        bucket="projects/_/buckets/b",
        name="o",
        generation=GENERATION,
        metageneration=4,
        size=OBJ_SIZE,
        storage_class="STANDARD",
        etag="etag-1",
        content_type="application/octet-stream",
        content_encoding="identity",
        finalized=True,
        crc32c=CRC32C,
        md5_hash=b"0123456789abcdef",
        metadata={"k": "v"},
    )


class _FakeGcsCore:
    def __init__(self, data):
        self.data = data
        self.shm = None
        self.calls = []
        self.opens = []
        self.sessions = []
        self.server_info_calls = 0
        self.bogus_releases = []
        self.errors = []
        self.resource_factory = _default_resource
        self.range_action = lambda call_idx, spec: None
        self._free = {}
        self._slot_event = asyncio.Event()

    # Slots of a region are shared by every stream reading through that region.
    async def acquire_slot(self, region_id):
        free = self._free.setdefault(region_id, collections.deque(range(N_SLOTS)))
        while not free:
            self._slot_event.clear()
            await self._slot_event.wait()
        return free.popleft()

    def free_slot(self, region_id, slot):
        self._free[region_id].append(slot)
        self._slot_event.set()

    async def GetServerInfo(self, request, context):
        self.server_info_calls += 1
        return pb.ServerInfo(
            server_version="fake",
            features=["bidi-read", "bidi-write", "bidi-read-shm", "bidi-write-shm"],
            shm_region_size=REGION_SIZE,
            shm_slot_size=SLOT,
        )

    async def CreateSession(self, request, context):
        self.sessions.append(request)
        return pb.CreateSessionResponse(session_id="s1")

    async def BidiReadObject(self, request_iterator, context):
        call = _ReadCall(self, len(self.calls), context)
        self.calls.append(call)
        reader = asyncio.ensure_future(call.read_loop())
        try:
            status = await call.finished
        finally:
            reader.cancel()
            tasks = list(call.tasks.values())
            for t in tasks:
                t.cancel()
            results = await asyncio.gather(reader, *tasks, return_exceptions=True)
            # Recorded and asserted on by the fixture (cancellation is expected).
            self.errors.extend(r for r in results if isinstance(r, Exception))
            # Like gcs-core-server: a dead stream drops its slot leases.
            call.reclaimed = sorted(call.leased)
            for s in call.reclaimed:
                self.free_slot(call.region_id, s)
            call.leased.clear()
            call.ended = True
        if status is not None:
            await context.abort(*status)

    def handler(self):
        return grpc.method_handlers_generic_handler(
            "gcscore.v1.GcsCore",
            {
                "GetServerInfo": grpc.unary_unary_rpc_method_handler(
                    self.GetServerInfo,
                    request_deserializer=pb.Empty.FromString,
                    response_serializer=pb.ServerInfo.SerializeToString,
                ),
                "CreateSession": grpc.unary_unary_rpc_method_handler(
                    self.CreateSession,
                    request_deserializer=pb.CreateSessionRequest.FromString,
                    response_serializer=pb.CreateSessionResponse.SerializeToString,
                ),
                "BidiReadObject": grpc.stream_stream_rpc_method_handler(
                    self.BidiReadObject,
                    request_deserializer=pb.BidiReadObjectRequest.FromString,
                    response_serializer=pb.BidiReadObjectResponse.SerializeToString,
                ),
            },
        )


async def _eventually(predicate, what, timeout=5.0):
    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout
    while not predicate():
        if loop.time() > deadline:
            raise AssertionError(f"timed out waiting for {what}")
        await asyncio.sleep(0.005)


async def _wait_all_released(call):
    await _eventually(
        lambda: not call.leased
        and collections.Counter(call.released) == collections.Counter(call.handed_out),
        f"client to release every slot of call {call.idx} "
        f"(handed out {call.handed_out}, released {call.released})",
    )


def _w(coro):
    return asyncio.wait_for(coro, TIMEOUT)


@pytest_asyncio.fixture
async def fake(monkeypatch):
    tmpdir = tempfile.mkdtemp(prefix="udsrd", dir="/tmp")
    sock = os.path.join(tmpdir, "s.sock")
    srv = _FakeGcsCore(DATA)
    server = grpc.aio.server()
    server.add_generic_rpc_handlers([srv.handler()])
    server.add_insecure_port(f"unix:{sock}")
    await server.start()
    srv.shm = _ShmListener(sock + ".shm", REGION_SIZE)

    monkeypatch.setenv(_config.ENV_MODE, "auto")
    monkeypatch.setenv(_config.ENV_SOCKET, sock)
    for name in (
        _config.ENV_FORCE,
        _config.ENV_SHM,
        _config.ENV_PREWARM,
        _config.ENV_DIRECT_PATH_XDS,
        _config.ENV_TOPOLOGY,
        runtime.ENV_MAX_REGIONS,
    ):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(_config, "_fallback_logged", _config._fallback_logged)
    srv.clients = []
    try:
        yield srv
    finally:
        await runtime.close_all()
        for client in srv.clients:
            try:
                await client._grpc_client.transport.close()
            except Exception:  # pragma: NO COVER - best effort
                pass
        await server.stop(None)
        srv.shm.close()
        shutil.rmtree(tmpdir, ignore_errors=True)
    assert srv.errors == []


def _client(fake):
    client = AsyncGrpcClient(
        credentials=AnonymousCredentials(),
        client_options=client_options_lib.ClientOptions(api_endpoint="127.0.0.1:1"),
        attempt_direct_path=False,
    )
    fake.clients.append(client)
    return client


async def _open_session(fake, **kwargs):
    rt = await _w(runtime.UdsRuntime.get(_client(fake)))
    session = UdsReadSession(rt, "b", "o", **kwargs)
    await _w(session.open())
    return session


def _spec_tuples(specs):
    return [(s.offset, s.length) for s in specs]


# --------------------------------------------------------------------------- tests


@pytest.mark.asyncio
async def test_open_handshake_resource_and_object_metadata(fake):
    session = await _open_session(fake, metadata=[("x-goog-user-project", "qp")])
    try:
        # Runtime: anonymous session against the custom endpoint.
        assert fake.server_info_calls == 1
        assert len(fake.sessions) == 1
        assert fake.sessions[0].anonymous is True
        assert fake.sessions[0].endpoint == "http://127.0.0.1:1"

        # OpenReadSpec.
        call = fake.calls[0]
        assert call.metadata.get("x-session") == "s1"
        spec = fake.opens[0]
        assert spec.bucket == "b"
        assert spec.object == "o"
        assert spec.generation == 0
        assert spec.compute_full_crc32c is True
        assert spec.quota_project == "qp"
        assert spec.user_agent == f"gcloud-python/{__version__} uds/fake"
        assert fake.shm.region_ids() == [REGION_ID_BASE]
        assert spec.read_region_id == REGION_ID_BASE

        # ReadOpened -> resource / object_metadata (typed-field fallback).
        assert session.is_open
        assert session.resource == _default_resource()
        assert session.generation == GENERATION
        md = session.object_metadata
        assert isinstance(md, _storage_v2.Object)
        assert md.bucket == "projects/_/buckets/b"
        assert md.name == "o"
        assert md.generation == GENERATION
        assert md.metageneration == 4
        assert md.size == OBJ_SIZE
        assert md.storage_class == "STANDARD"
        assert md.etag == "etag-1"
        assert md.content_type == "application/octet-stream"
        assert dict(md.metadata) == {"k": "v"}
        assert md.checksums.crc32c == CRC32C
        assert md.checksums.md5_hash == b"0123456789abcdef"
    finally:
        await _w(session.close())
    assert not session.is_open


@pytest.mark.asyncio
async def test_object_metadata_from_object_json(fake):
    obj = _storage_v2.Object(
        bucket="projects/_/buckets/b",
        name="o",
        generation=77,
        size=OBJ_SIZE,
        content_type="text/plain",
        content_language="en",
    )

    def resource():
        r = _default_resource()
        r.generation = 77
        r.object_json = _storage_v2.Object.to_json(obj)
        return r

    fake.resource_factory = resource
    session = await _open_session(fake, generation=77)
    try:
        assert fake.opens[0].generation == 77
        assert session.generation == 77
        md = session.object_metadata
        assert md.generation == 77
        assert md.content_type == "text/plain"
        assert md.content_language == "en"  # only present in object_json
    finally:
        await _w(session.close())


@pytest.mark.asyncio
async def test_download_ranges_dispatch_multi_slot_and_to_eof(fake):
    session = await _open_session(fake)
    try:
        call = fake.calls[0]
        small, multi, to_eof, at_eof = (io.BytesIO() for _ in range(4))
        ranges = [
            (0, 100, small),
            (3 * MiB + 7, 5 * MiB, multi),  # 3 slots
            (1000, 0, to_eof),  # length 0 => to EOF; needs > N_SLOTS slots
            (OBJ_SIZE, 0, at_eof),  # empty range at EOF
        ]
        await _w(session.download_ranges(ranges))

        assert small.getvalue() == DATA[:100]
        assert multi.getvalue() == DATA[3 * MiB + 7 : 8 * MiB + 7]
        assert to_eof.getvalue() == DATA[1000:]
        assert at_eof.getvalue() == b""

        assert len(call.read_requests) == 1
        assert _spec_tuples(call.read_specs) == [
            (0, 100),
            (3 * MiB + 7, 5 * MiB),
            (1000, 0),
            (OBJ_SIZE, 0),
        ]
        ids = [s.range_id for s in call.read_specs]
        assert len(set(ids)) == len(ids)

        # Payloads travelled through shared memory, never inline.
        assert call.inline_msgs == 0
        to_eof_slots = -(-(OBJ_SIZE - 1000) // SLOT)
        assert to_eof_slots == 5
        assert call.slot_msgs == 1 + 3 + to_eof_slots
        assert len(call.handed_out) > N_SLOTS  # slots were recycled via ReleaseSlots
        await _wait_all_released(call)
        assert fake.bogus_releases == []
    finally:
        await _w(session.close())


@pytest.mark.asyncio
async def test_concurrent_download_ranges_calls(fake):
    session = await _open_session(fake)
    try:
        call = fake.calls[0]
        bufs = [io.BytesIO() for _ in range(6)]
        calls = [
            [(0, 3 * MiB, bufs[0]), (OBJ_SIZE - 10, 0, bufs[1])],
            [(5 * MiB, 2 * MiB + 1, bufs[2])],
            [(17, 4 * MiB, bufs[3]), (9 * MiB, 0, bufs[4]), (1, 1, bufs[5])],
        ]
        await _w(asyncio.gather(*(session.download_ranges(c) for c in calls)))

        assert bufs[0].getvalue() == DATA[: 3 * MiB]
        assert bufs[1].getvalue() == DATA[OBJ_SIZE - 10 :]
        assert bufs[2].getvalue() == DATA[5 * MiB : 7 * MiB + 1]
        assert bufs[3].getvalue() == DATA[17 : 17 + 4 * MiB]
        assert bufs[4].getvalue() == DATA[9 * MiB :]
        assert bufs[5].getvalue() == DATA[1:2]

        assert len(call.read_requests) == 3
        ids = [s.range_id for s in call.read_specs]
        assert len(ids) == 6 and len(set(ids)) == 6
        await _wait_all_released(call)
        assert fake.bogus_releases == []
        assert session._ranges == {}
    finally:
        await _w(session.close())


@pytest.mark.asyncio
async def test_cancel_sends_cancel_ranges_and_releases_every_slot(fake):
    session = await _open_session(fake)
    try:
        call = fake.calls[0]
        held_offset = 1 * MiB
        fake.range_action = lambda idx, spec: (
            ("partial_hold", SLOT) if spec.offset == held_offset else None
        )
        done_buf, held_buf = io.BytesIO(), io.BytesIO()
        task = asyncio.ensure_future(
            session.download_ranges(
                [(0, 1000, done_buf), (held_offset, 3 * MiB, held_buf)]
            )
        )
        # Both ranges got one slot each and the client processed (released) both.
        await _eventually(
            lambda: len(call.read_specs) == 2 and len(call.released) == 2,
            "first slots of both ranges to be consumed",
        )
        assert not task.done()
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await _w(task)

        held_id = next(s.range_id for s in call.read_specs if s.offset == held_offset)
        await _eventually(lambda: call.cancelled_ids == [held_id], "CancelRanges")
        assert done_buf.getvalue() == DATA[:1000]
        assert held_buf.getvalue() == DATA[held_offset : held_offset + SLOT]
        assert session._ranges == {}
        assert session.is_open

        # Late data for the cancelled range and data for an unknown range still
        # hand out slots; the client must return them without touching buffers.
        await call.send_data(
            held_id,
            held_offset + SLOT,
            DATA[held_offset + SLOT : held_offset + 3 * MiB],
            True,
        )
        await call.send_data(999, 0, b"x" * 10, True)
        await _wait_all_released(call)
        assert len(call.handed_out) == 4
        assert held_buf.getvalue() == DATA[held_offset : held_offset + SLOT]

        # The session stays usable.
        fake.range_action = lambda idx, spec: None
        full = io.BytesIO()
        await _w(session.download_ranges([(0, 0, full)]))
        assert full.getvalue() == DATA
        await _wait_all_released(call)
        assert fake.bogus_releases == []
        assert len(fake.calls) == 1
    finally:
        await _w(session.close())


@pytest.mark.asyncio
async def test_range_error_out_of_range_while_other_ranges_succeed(fake):
    session = await _open_session(fake)
    try:
        call = fake.calls[0]
        before, bad, after = io.BytesIO(), io.BytesIO(), io.BytesIO()
        with pytest.raises(exceptions.OutOfRange):
            await _w(
                session.download_ranges(
                    [(0, 100, before), (OBJ_SIZE + 10, 5, bad), (200, 3 * MiB, after)]
                )
            )
        assert before.getvalue() == DATA[:100]
        assert bad.getvalue() == b""
        assert after.getvalue() == DATA[200 : 200 + 3 * MiB]
        assert session.is_open
        assert session._ranges == {}

        again = io.BytesIO()
        await _w(session.download_ranges([(5, 10, again)]))
        assert again.getvalue() == DATA[5:15]
        await _wait_all_released(call)
        assert len(fake.calls) == 1  # per-range errors never reopen the stream
    finally:
        await _w(session.close())


@pytest.mark.asyncio
async def test_range_error_checksum_mismatch_raises_data_corruption(fake):
    session = await _open_session(fake)
    try:
        call = fake.calls[0]
        fake.range_action = lambda idx, spec: (
            ("error", INTERNAL, "crc32c mismatch", True)
            if spec.offset == 4 * MiB
            else None
        )
        good, corrupt = io.BytesIO(), io.BytesIO()
        with pytest.raises(DataCorruption) as exc_info:
            await _w(
                session.download_ranges([(0, 3 * MiB, good), (4 * MiB, 10, corrupt)])
            )
        assert "crc32c mismatch" in str(exc_info.value)
        assert good.getvalue() == DATA[: 3 * MiB]
        assert corrupt.getvalue() == b""
        assert session.is_open
        await _wait_all_released(call)
        assert len(fake.calls) == 1
    finally:
        await _w(session.close())


@pytest.mark.asyncio
@pytest.mark.parametrize("length", [6 * MiB, 0], ids=["bounded", "to_eof"])
async def test_unavailable_mid_range_reopens_and_resumes_remaining_bytes(fake, length):
    offset = 1 * MiB + 5
    delivered = 3 * MiB  # 2 MiB slot + 1 MiB slot, then UNAVAILABLE
    fake.range_action = lambda idx, spec: (
        ("abort_after", delivered) if idx == 0 else None
    )
    session = await _open_session(fake)
    try:
        buf = io.BytesIO()
        await _w(session.download_ranges([(offset, length, buf)]))
        end = OBJ_SIZE if length == 0 else offset + length
        assert buf.getvalue() == DATA[offset:end]

        # A second BidiReadObject stream was opened, pinned to the generation.
        assert len(fake.calls) == 2
        assert fake.calls[0].ended
        assert len(fake.opens) == 2
        assert fake.opens[1].generation == GENERATION
        assert fake.opens[1].read_region_id == REGION_ID_BASE

        first, second = fake.calls
        assert _spec_tuples(first.read_specs) == [(offset, length)]
        # Only the REMAINING bytes are requested on the new stream.
        expected_len = 0 if length == 0 else length - delivered
        assert _spec_tuples(second.read_specs) == [(offset + delivered, expected_len)]
        assert second.read_specs[0].range_id != first.read_specs[0].range_id
        assert session.is_open
        await _wait_all_released(second)
        assert fake.bogus_releases == []
    finally:
        await _w(session.close())


@pytest.mark.asyncio
async def test_unavailable_with_concurrent_calls_reopens_once(fake):
    """Two download_ranges calls in flight when the stream dies share ONE reopen."""
    fake.range_action = lambda idx, spec: (("partial_hold", SLOT) if idx == 0 else None)
    session = await _open_session(fake)
    try:
        first = fake.calls[0]
        a, b = io.BytesIO(), io.BytesIO()
        tasks = [
            asyncio.ensure_future(session.download_ranges([(0, 3 * MiB, a)])),
            asyncio.ensure_future(session.download_ranges([(5 * MiB, 0, b)])),
        ]
        await _eventually(
            lambda: len(first.read_specs) == 2 and len(first.released) == 2,
            "partial data of both calls to be consumed",
        )
        first.finish((grpc.StatusCode.UNAVAILABLE, "fake gcs-core-server restarting"))
        await _w(asyncio.gather(*tasks))

        assert a.getvalue() == DATA[: 3 * MiB]
        assert b.getvalue() == DATA[5 * MiB :]
        assert len(fake.calls) == 2, "expected exactly one reopened stream"
        resumed = sorted(_spec_tuples(fake.calls[1].read_specs))
        assert resumed == [(SLOT, 3 * MiB - SLOT), (5 * MiB + SLOT, 0)]
        await _wait_all_released(fake.calls[1])
    finally:
        await _w(session.close())
    await _eventually(
        lambda: all(c.ended for c in fake.calls),
        "every server stream to end after close",
    )


@pytest.mark.asyncio
async def test_inline_mode_when_shm_disabled(fake, monkeypatch):
    monkeypatch.setenv(_config.ENV_SHM, "off")
    session = await _open_session(fake)
    try:
        call = fake.calls[0]
        assert fake.opens[0].read_region_id == 0
        assert fake.shm.region_ids() == []  # never connected to <socket>.shm
        a, b = io.BytesIO(), io.BytesIO()
        await _w(session.download_ranges([(0, 0, a), (100, 3 * MiB, b)]))
        assert a.getvalue() == DATA
        assert b.getvalue() == DATA[100 : 100 + 3 * MiB]
        assert call.inline_msgs > 0
        assert call.slot_msgs == 0
        assert call.handed_out == []
        assert call.release_requests == 0
    finally:
        await _w(session.close())


@pytest.mark.asyncio
async def test_public_multi_range_downloader_uses_uds(fake):
    client = _client(fake)
    mrd = await _w(AsyncMultiRangeDownloader.create_mrd(client, "b", "o"))
    try:
        assert mrd._uds is not None
        assert mrd.is_stream_open
        assert mrd.persisted_size == OBJ_SIZE
        assert mrd.generation == GENERATION
        assert mrd.is_finalized is True
        assert mrd.full_obj_server_crc32c == CRC32C
        assert mrd.object_metadata.name == "o"

        whole, part = io.BytesIO(), io.BytesIO()
        await _w(mrd.download_ranges([(0, 0, whole), (2 * MiB - 3, 2 * MiB + 6, part)]))
        assert whole.getvalue() == DATA
        assert part.getvalue() == DATA[2 * MiB - 3 : 4 * MiB + 3]
        assert len(fake.calls) == 1
        assert fake.opens[0].read_region_id == REGION_ID_BASE
        await _wait_all_released(fake.calls[0])
    finally:
        await _w(mrd.close())
    assert not mrd.is_stream_open
    assert mrd._uds is None
    await _eventually(lambda: fake.calls[0].ended, "server stream to end after close")


@pytest.mark.asyncio
async def test_eventually_times_out():
    with pytest.raises(AssertionError, match="timed out waiting for never"):
        await _eventually(lambda: False, "never", timeout=0)


# ------------------------------------------------------- scripted-stream unit tests
#
# Edge cases that a well-behaved server never produces are driven through a scripted
# client-side stand-in for the ``grpc.aio`` stream instead of the fake server.


class _ScriptedCall:
    """Client-side ``BidiReadObject`` call whose responses are pushed by the test."""

    def __init__(self, *responses, write_exc=None, code=None, eof_on_half_close=True):
        self._responses = asyncio.Queue()
        for resp in responses:
            self.push(resp)
        self.write_exc = write_exc
        self._code = code
        self.eof_on_half_close = eof_on_half_close
        self.written = []
        self.cancelled = False

    def push(self, resp):
        self._responses.put_nowait(resp)

    async def write(self, req):
        if self.write_exc is not None:
            raise self.write_exc
        self.written.append(req)

    async def read(self):
        return await self._responses.get()

    async def done_writing(self):
        if self.eof_on_half_close:
            self.push(grpc.aio.EOF)

    def cancel(self):
        self.cancelled = True

    async def code(self):
        return self._code

    def requests(self, op):
        return [getattr(r, op) for r in self.written if r.WhichOneof("op") == op]


class _ScriptedRuntime:
    user_agent = "ua"
    metadata = (("x-session", "s1"),)

    def __init__(self, call):
        self.call = call

    async def read_region(self):
        return None

    def bidi_read(self, metadata):
        assert metadata == self.metadata
        return self.call


def _opened():
    return pb.BidiReadObjectResponse(opened=pb.ReadOpened(object=_default_resource()))


def _rpc_error(code):
    return grpc.aio.AioRpcError(
        code, grpc.aio.Metadata(), grpc.aio.Metadata(), details="scripted"
    )


async def _scripted_session(call=None, **kwargs):
    call = call or _ScriptedCall(_opened())
    session = UdsReadSession(_ScriptedRuntime(call), "b", "o", **kwargs)
    await _w(session.open())
    return session, call


def _pending_range(range_id, done=False):
    fut = asyncio.get_running_loop().create_future()
    if done:
        fut.set_result(0)
    return read_session._RangeState(range_id, 0, 1, io.BytesIO(), fut)


@pytest.mark.asyncio
async def test_open_maps_rpc_error_and_ignores_unknown_metadata():
    call = _ScriptedCall(write_exc=_rpc_error(grpc.StatusCode.UNAVAILABLE))
    session = UdsReadSession(
        _ScriptedRuntime(call),
        "b",
        "o",
        metadata=[("x-goog-api-client", "gl-python"), ("X-Goog-User-Project", "qp")],
    )
    assert session._quota_project == "qp"
    with pytest.raises(exceptions.ServiceUnavailable):
        await _w(session.open())
    assert call.cancelled
    assert not session.is_open


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "first, code, expected",
    [
        (grpc.aio.EOF, None, exceptions.InternalServerError),
        (
            pb.BidiReadObjectResponse(data=pb.RangeData(range_id=1)),
            grpc.StatusCode.NOT_FOUND,
            exceptions.NotFound,
        ),
    ],
    ids=["eof", "data-before-opened"],
)
async def test_open_fails_when_stream_ends_before_opened(first, code, expected):
    call = _ScriptedCall(first, code=code)
    session = UdsReadSession(_ScriptedRuntime(call), "b", "o")
    with pytest.raises(expected, match="ended before ReadOpened"):
        await _w(session.open())
    assert call.cancelled
    assert not session.is_open
    assert session._send_q is None
    session._send_nowait(pb.BidiReadObjectRequest())  # no queue => dropped
    await _w(session.close())  # never-opened session: nothing to tear down


@pytest.mark.asyncio
async def test_reader_skips_unexpected_messages_and_fails_pending_on_eof():
    session, call = await _scripted_session()
    finished, pending = _pending_range(7, done=True), _pending_range(8)
    session._ranges.update({7: finished, 8: pending})

    call.push(_opened())  # unexpected message kind: ignored
    for range_id in (999, 7):  # unknown range / already finished range
        call.push(
            pb.BidiReadObjectResponse(
                range_error=pb.RangeError(range_id=range_id, code=OUT_OF_RANGE)
            )
        )
    call.push(grpc.aio.EOF)  # server ended the stream while a range is pending
    await _w(session._reader)

    assert finished.fut.result() == 0
    assert isinstance(pending.fut.exception(), exceptions.ServiceUnavailable)
    assert isinstance(session._error, exceptions.ServiceUnavailable)
    assert not session.is_open
    assert session._ranges == {}
    await _w(session.close())


@pytest.mark.asyncio
async def test_writer_stops_quietly_when_stream_write_fails():
    session, call = await _scripted_session()
    call.write_exc = RuntimeError("stream broken")
    session._send_nowait(pb.BidiReadObjectRequest(release=pb.ReleaseSlots(slots=[1])))
    await _w(session._writer)  # swallowed; the reader reports the stream status
    assert session._writer.exception() is None
    call.push(grpc.aio.EOF)
    await _w(session.close())


class _FailingBuffer:
    def write(self, data):
        raise OSError("disk full")


@pytest.mark.asyncio
async def test_user_buffer_failure_fails_only_that_download():
    session, call = await _scripted_session()
    task = asyncio.ensure_future(session.download_ranges([(0, 10, _FailingBuffer())]))
    await _eventually(lambda: call.requests("read"), "ReadRanges")
    (spec,) = call.requests("read")[0].ranges
    call.push(
        pb.BidiReadObjectResponse(
            data=pb.RangeData(range_id=spec.range_id, inline_data=b"x" * 10)
        )
    )
    with pytest.raises(OSError, match="disk full"):
        await _w(task)
    assert session.is_open
    await _w(session.close())


@pytest.mark.asyncio
async def test_slot_release_failure_for_unknown_range_is_contained():
    class _BrokenQueue:
        def put_nowait(self, item):
            raise asyncio.QueueFull

    session = UdsReadSession(_ScriptedRuntime(None), "b", "o")
    session._send_q = _BrokenQueue()
    session._on_data(
        pb.RangeData(range_id=5, slot=pb.ShmSlotRef(slot=2, length=3), range_end=True)
    )
    assert session._ranges == {}


@pytest.mark.asyncio
async def test_download_ranges_on_closed_session():
    session = UdsReadSession(_ScriptedRuntime(None), "b", "o")
    assert await session.download_ranges([]) is None
    with pytest.raises(ValueError, match="stream is not open"):
        await session.download_ranges([(0, 1, io.BytesIO())])
    session._error = exceptions.NotFound("gone")
    with pytest.raises(exceptions.NotFound, match="gone"):
        await session.download_ranges([(0, 1, io.BytesIO())])


@pytest.mark.asyncio
async def test_cancel_racing_completion_sends_no_cancel_ranges():
    session, call = await _scripted_session()
    task = None

    class _CancellingBuffer(io.BytesIO):
        def write(self, data):
            task.cancel()  # cancelled while the range completes
            return super().write(data)

    buf = _CancellingBuffer()
    task = asyncio.ensure_future(session.download_ranges([(0, 3, buf)]))
    await _eventually(lambda: call.requests("read"), "ReadRanges")
    (spec,) = call.requests("read")[0].ranges
    call.push(
        pb.BidiReadObjectResponse(
            data=pb.RangeData(
                range_id=spec.range_id, inline_data=b"abc", range_end=True
            )
        )
    )
    with pytest.raises(asyncio.CancelledError):
        await _w(task)
    assert buf.getvalue() == b"abc"
    assert call.requests("cancel") == []
    assert session.is_open
    await _w(session.close())


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "error, expected",
    [
        (exceptions.ServiceUnavailable("died again"), exceptions.ServiceUnavailable),
        (None, exceptions.ServiceUnavailable),
    ],
    ids=["replacement-failed", "replacement-closed"],
)
async def test_reopen_once_raises_when_replacement_stream_is_down(error, expected):
    # A concurrent caller already replaced the stream of epoch 0, and the
    # replacement is down as well: report instead of reopening again.
    session = UdsReadSession(_ScriptedRuntime(None), "b", "o")
    session._epoch = 1
    session._error = error
    with pytest.raises(expected):
        await session._reopen_once(0)


@pytest.mark.asyncio
async def test_close_times_out_waiting_for_server_and_cancels_reader(monkeypatch):
    session, call = await _scripted_session(
        _ScriptedCall(_opened(), eof_on_half_close=False)
    )
    reader = session._reader
    real_wait_for = asyncio.wait_for

    def short_wait_for(aw, timeout):
        assert timeout == 10
        return real_wait_for(aw, 0.01)

    monkeypatch.setattr(asyncio, "wait_for", short_wait_for)
    await session.close()

    assert call.cancelled
    assert reader.cancelled()
    assert isinstance(session._error, exceptions.Cancelled)
    assert not session.is_open


@pytest.mark.asyncio
async def test_close_without_reader_task():
    session, call = await _scripted_session()
    reader = session._reader
    session._reader = None
    await _w(session.close())
    assert call.cancelled
    assert not session.is_open
    call.push(grpc.aio.EOF)
    await _w(reader)
