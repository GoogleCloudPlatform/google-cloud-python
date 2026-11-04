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

"""Hermetic tests for the UDS ``BidiWriteObject`` session (``UdsWriteSession``).

A fake ``gcscore.v1.GcsCore`` gRPC server (``grpc.aio``) listens on a Unix domain
socket in this process, together with a fake ``<socket>.shm`` side channel that hands
out ``memfd`` regions via ``SCM_RIGHTS``. The fake reads the client-written slot bytes
straight out of the shared mapping and releases slots only when it gets a ``Flush``
(or ``Close`` / ``Finalize``), like the Rust SDK's replay buffer.
"""

import array
import asyncio
import itertools
import mmap
import os
import random
import shutil
import socket
import struct
import tempfile
import threading
from unittest import mock

import google_crc32c
import grpc
import pytest
import pytest_asyncio
from google.api_core import exceptions
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials

from google.cloud.storage.asyncio._uds import _config, runtime
from google.cloud.storage.asyncio._uds import gcscore_pb2 as pb
from google.cloud.storage.asyncio._uds.write_session import (
    INLINE_CHUNK,
    UdsWriteSession,
)
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    AsyncAppendableObjectWriter,
)
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient

MiB = 1024 * 1024
SLOT = 2 * MiB
REGION = 8 * MiB  # 4 slots
N_SLOTS = REGION // SLOT
GENERATION = 777
TIMEOUT = 10.0


def _payload(n, seed=0):
    return random.Random(seed).randbytes(n)


async def _w(coro, timeout=TIMEOUT):
    return await asyncio.wait_for(coro, timeout)


# --------------------------------------------------------------------------- fakes


class FakeShmListener:
    """Fake ``<socket>.shm`` side channel handing out ``memfd`` regions."""

    def __init__(self, path, region_size):
        self.path = path
        self.region_size = region_size
        self.regions = {}  # region_id -> (conn, fd, mm)
        self._ids = itertools.count(41)
        self._lock = threading.Lock()
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
            except OSError:  # accept() timeout: re-check the stop flag
                continue
            conn.setblocking(True)
            rid = next(self._ids)
            fd = os.memfd_create("fake", 0)
            os.ftruncate(fd, self.region_size)
            mm = mmap.mmap(fd, self.region_size)
            with self._lock:
                self.regions[rid] = (conn, fd, mm)
            socket.send_fds(conn, [struct.pack("<QQ", rid, self.region_size)], [fd])

    def read(self, region_id, offset, length):
        with self._lock:
            mm = self.regions[region_id][2]
        return bytes(mm[offset : offset + length])

    def close(self):
        self._stop.set()
        self._thread.join(2)
        self._sock.close()
        with self._lock:
            for conn, fd, mm in self.regions.values():
                mm.close()
                os.close(fd)
                conn.close()
            self.regions.clear()


class StreamState:
    """What the fake observed on one ``BidiWriteObject`` stream."""

    def __init__(self):
        self.spec = None
        self.metadata = {}
        self.ops = []  # (kind, op_id, detail)
        self.replies = []  # (kind, op_id)
        self.data = bytearray()
        self.outstanding = set()  # submitted, not yet released slots
        self.max_outstanding = 0
        self.violations = []

    def kinds(self):
        return [k for k, _, _ in self.ops]


class FakeGcsCore:
    def __init__(self, shm, region_size=REGION, slot_size=SLOT):
        self.shm = shm
        self.region_size = region_size
        self.slot_size = slot_size
        self.streams = []
        self.session_requests = []
        self.release_on_flush = True
        self.release_on_close = True
        self.open_error = None  # grpc.StatusCode
        self.open_replies = None  # replace WriteOpened with these replies, then end
        self.close_error = None  # grpc.StatusCode
        self.noise = False  # send replies with unknown op_ids first
        self.persisted_bias = 0

    @property
    def last(self):
        return self.streams[-1]

    async def get_server_info(self, request, context):
        return pb.ServerInfo(
            server_version="fake",
            features=["bidi-read", "bidi-write", "bidi-read-shm", "bidi-write-shm"],
            shm_region_size=self.region_size,
            shm_slot_size=self.slot_size,
        )

    async def create_session(self, request, context):
        self.session_requests.append(request)
        return pb.CreateSessionResponse(session_id="s1")

    def _reply(self, st, **kwargs):
        resp = pb.BidiWriteObjectResponse(**kwargs)
        st.replies.append((resp.WhichOneof("msg"), resp.op_id))
        return resp

    def _release(self, st):
        slots = sorted(st.outstanding)
        st.outstanding.clear()
        return pb.BidiWriteObjectResponse(released=pb.SlotsReleased(slots=slots))

    def _noise(self, st):
        return [
            self._reply(st, op_id=987654, flushed=pb.Flushed(persisted_size=-5)),
            self._reply(st, op_id=987655, closed=pb.Closed(persisted_size=-6)),
        ]

    async def bidi_write(self, request_iterator, context):
        st = StreamState()
        self.streams.append(st)
        st.metadata = dict(context.invocation_metadata())
        async for req in request_iterator:
            kind = req.WhichOneof("op")
            if kind == "open":
                st.spec = req.open
                st.ops.append(("open", req.op_id, None))
                if self.open_error is not None:
                    await context.abort(self.open_error, "fake open failure")
                if self.open_replies is not None:
                    for kwargs in self.open_replies:
                        yield self._reply(st, op_id=req.op_id, **kwargs)
                    return
                yield self._reply(
                    st,
                    op_id=req.op_id,
                    opened=pb.WriteOpened(generation=GENERATION, persisted_size=0),
                )
            elif kind == "append":
                ap = req.append
                if ap.HasField("slot"):
                    ref = ap.slot
                    if ref.region_id != st.spec.write_region_id:
                        st.violations.append(("region", ref.region_id))
                    if ref.slot in st.outstanding:
                        st.violations.append(("reused-unreleased", ref.slot))
                    st.outstanding.add(ref.slot)
                    st.max_outstanding = max(st.max_outstanding, len(st.outstanding))
                    st.data += self.shm.read(
                        ref.region_id, ref.slot * self.slot_size, ref.length
                    )
                    st.ops.append(("append", req.op_id, (ref.slot, ref.length)))
                else:
                    st.data += ap.inline_data
                    st.ops.append(("inline", req.op_id, len(ap.inline_data)))
            elif kind == "flush":
                st.ops.append(("flush", req.op_id, None))
                if self.release_on_flush and st.outstanding:
                    yield self._release(st)
                if self.noise:
                    for r in self._noise(st):
                        yield r
                yield self._reply(
                    st,
                    op_id=req.op_id,
                    flushed=pb.Flushed(
                        persisted_size=len(st.data) + self.persisted_bias
                    ),
                )
            elif kind == "close":
                st.ops.append(("close", req.op_id, None))
                if self.close_error is not None:
                    await context.abort(self.close_error, "fake close failure")
                if self.release_on_close and st.outstanding:
                    yield self._release(st)
                if self.noise:
                    for r in self._noise(st):
                        yield r
                yield self._reply(
                    st,
                    op_id=req.op_id,
                    closed=pb.Closed(persisted_size=len(st.data) + self.persisted_bias),
                )
            else:  # "finalize" (the only remaining ``op``)
                fin = req.finalize
                crc = (
                    fin.full_object_crc32c
                    if fin.HasField("full_object_crc32c")
                    else None
                )
                st.ops.append(("finalize", req.op_id, crc))
                actual = google_crc32c.value(bytes(st.data))
                if crc is not None and crc != actual:
                    await context.abort(
                        grpc.StatusCode.INVALID_ARGUMENT, "full_object_crc32c mismatch"
                    )
                if st.outstanding:
                    yield self._release(st)
                yield self._reply(
                    st,
                    op_id=req.op_id,
                    finalized=pb.Finalized(
                        object=pb.ObjectResource(
                            bucket="projects/_/buckets/" + st.spec.bucket,
                            name=st.spec.object,
                            generation=GENERATION,
                            metageneration=1,
                            size=len(st.data),
                            finalized=True,
                            crc32c=actual,
                        )
                    ),
                )


class Env:
    def __init__(self, fake, shm, client, rt, sock):
        self.fake = fake
        self.shm = shm
        self.client = client
        self.rt = rt
        self.sock = sock


@pytest_asyncio.fixture
async def env(monkeypatch):
    tmpdir = tempfile.mkdtemp(prefix="uw", dir="/tmp")
    sock = os.path.join(tmpdir, "s.sock")
    shm = FakeShmListener(sock + ".shm", REGION)
    fake = FakeGcsCore(shm)
    server = grpc.aio.server()
    server.add_generic_rpc_handlers(
        [
            grpc.method_handlers_generic_handler(
                "gcscore.v1.GcsCore",
                {
                    "GetServerInfo": grpc.unary_unary_rpc_method_handler(
                        fake.get_server_info,
                        request_deserializer=pb.Empty.FromString,
                        response_serializer=pb.ServerInfo.SerializeToString,
                    ),
                    "CreateSession": grpc.unary_unary_rpc_method_handler(
                        fake.create_session,
                        request_deserializer=pb.CreateSessionRequest.FromString,
                        response_serializer=pb.CreateSessionResponse.SerializeToString,
                    ),
                    "BidiWriteObject": grpc.stream_stream_rpc_method_handler(
                        fake.bidi_write,
                        request_deserializer=pb.BidiWriteObjectRequest.FromString,
                        response_serializer=pb.BidiWriteObjectResponse.SerializeToString,
                    ),
                },
            )
        ]
    )
    server.add_insecure_port(f"unix:{sock}")
    await server.start()

    monkeypatch.setenv("GOOGLE_CLOUD_STORAGE_UDS", "auto")
    monkeypatch.setenv("GOOGLE_CLOUD_STORAGE_UDS_SOCKET", sock)
    monkeypatch.delenv("GOOGLE_CLOUD_STORAGE_FORCE_USE_CORE_SDK", raising=False)
    monkeypatch.delenv("GOOGLE_CLOUD_STORAGE_UDS_SHM", raising=False)
    monkeypatch.delenv("GOOGLE_CLOUD_STORAGE_UDS_MAX_REGIONS", raising=False)
    monkeypatch.delenv("GOOGLE_CLOUD_STORAGE_UDS_PREWARM", raising=False)
    monkeypatch.setattr(_config, "_fallback_logged", False)

    try:
        client = AsyncGrpcClient(
            credentials=AnonymousCredentials(),
            client_options=ClientOptions(api_endpoint="127.0.0.1:1"),
            attempt_direct_path=False,
        )
        rt = await _w(runtime.UdsRuntime.get(client))
        yield Env(fake, shm, client, rt, sock)
    finally:
        await runtime.close_all()
        await server.stop(None)
        shm.close()
        shutil.rmtree(tmpdir, ignore_errors=True)


async def _open(env, bucket="b", obj="o"):
    session = UdsWriteSession(env.rt)
    result = await _w(session.open(pb.OpenAppendSpec(bucket=bucket, object=obj)))
    return session, result


def _assert_slot_packing(st):
    """Every slot Append is exactly one full slot, except one tail right before a
    Flush / Close / Finalize."""
    ops = st.ops
    for i, (kind, _op_id, detail) in enumerate(ops):
        if kind != "append":
            continue
        _slot, length = detail
        assert 0 < length <= SLOT
        if length != SLOT:
            assert i + 1 < len(ops), ops
            assert ops[i + 1][0] in ("flush", "close", "finalize"), ops


# --------------------------------------------------------------------------- tests


@pytest.mark.asyncio
async def test_runtime_handshake_and_open(env):
    session, (generation, persisted) = await _open(env)
    assert (generation, persisted) == (GENERATION, 0)
    assert session.is_open
    assert session.generation == GENERATION
    assert session.last_persisted_size == 0

    req = env.fake.session_requests[0]
    assert req.anonymous is True
    assert req.endpoint == "http://127.0.0.1:1"

    st = env.fake.last
    assert st.metadata.get("x-session") == "s1"
    assert st.spec.bucket == "b" and st.spec.object == "o"
    assert session.region is not None
    assert st.spec.write_region_id == session.region.region_id != 0
    assert st.spec.write_region_id in env.shm.regions
    assert session.region.n_slots == N_SLOTS
    assert st.spec.user_agent.startswith("gcloud-python/")
    assert st.spec.user_agent.endswith("uds/fake")
    await _w(session.close())


@pytest.mark.asyncio
async def test_slot_packing_uneven_appends(env):
    session, _ = await _open(env)
    part1_sizes = [1 * MiB, 3 * MiB, MiB // 2, 1, 700_001, 3]
    part2_sizes = [5 * MiB // 2, 1 * MiB]
    part1 = [_payload(n, seed=i) for i, n in enumerate(part1_sizes)]
    part2 = [_payload(n, seed=100 + i) for i, n in enumerate(part2_sizes)]

    for chunk in part1:
        await _w(session.append(chunk))
    # Only full slots have been submitted so far; the tail is still buffered.
    st = env.fake.last
    await _w(session.flush())  # flush also round-trips, so the fake saw everything
    expected1 = b"".join(part1)
    assert bytes(st.data) == expected1

    for chunk in part2:
        await _w(session.append(bytearray(chunk)))
    persisted = await _w(session.close())
    expected = expected1 + b"".join(part2)
    assert persisted == len(expected)
    assert bytes(st.data) == expected

    _assert_slot_packing(st)
    fake_slots = [d for k, _, d in st.ops if k == "append"]
    assert session.slot_submissions == fake_slots
    lengths = [n for _, n in fake_slots]
    total1 = len(expected1)
    total2 = len(expected) - total1
    assert lengths == (
        [SLOT] * (total1 // SLOT)
        + [total1 % SLOT]
        + [SLOT] * (total2 // SLOT)
        + [total2 % SLOT]
    )
    assert st.kinds()[-1] == "close"
    assert st.violations == []


@pytest.mark.asyncio
async def test_exact_slot_multiple_sends_no_empty_tail(env):
    session, _ = await _open(env)
    data = _payload(2 * SLOT, seed=7)
    await _w(session.append(memoryview(data)))
    assert await _w(session.flush()) == len(data)
    st = env.fake.last
    assert [d[1] for k, _, d in st.ops if k == "append"] == [SLOT, SLOT]
    assert st.kinds() == ["open", "append", "append", "flush"]
    await _w(session.close())


@pytest.mark.asyncio
async def test_starvation_triggers_internal_flush_without_deadlock(env):
    env.fake.release_on_flush = True
    env.fake.release_on_close = True
    session, _ = await _open(env)
    sizes = [3 * MiB, 5 * MiB + 123, MiB // 3, 4 * MiB]  # > 12 MiB, region is 8 MiB
    chunks = [_payload(n, seed=200 + i) for i, n in enumerate(sizes)]
    for chunk in chunks:
        await _w(session.append(chunk))
    persisted = await _w(session.close())
    expected = b"".join(chunks)

    st = env.fake.last
    assert persisted == len(expected)
    assert bytes(st.data) == expected
    # The client never called flush(): every Flush the fake saw was internal.
    internal = [op_id for k, op_id, _ in st.ops if k == "flush"]
    assert len(internal) >= 1
    assert all(op_id > 0 for op_id in internal)
    assert ("flushed", internal[0]) in st.replies
    assert st.violations == []
    assert st.max_outstanding <= N_SLOTS
    # Internal flushes never submit a partial slot: only the final tail (before
    # Close) may be shorter than a slot.
    lengths = [d[1] for k, _, d in st.ops if k == "append"]
    assert all(n == SLOT for n in lengths[:-1])
    assert lengths[-1] == len(expected) % SLOT
    _assert_slot_packing(st)
    assert session._internal_flush is None


@pytest.mark.asyncio
async def test_flush_returns_flushed_persisted_size(env):
    env.fake.persisted_bias = 1000
    session, _ = await _open(env)
    data = _payload(3 * MiB + 17, seed=3)
    await _w(session.append(data))
    assert session.has_unflushed_bytes()
    persisted = await _w(session.flush())
    assert persisted == len(data) + 1000
    assert session.last_persisted_size == len(data) + 1000
    assert session.submitted_since_flush == 0
    assert not session.has_unflushed_bytes()
    # Flushing with nothing pending sends no Append.
    assert await _w(session.flush()) == len(data) + 1000
    st = env.fake.last
    assert st.kinds() == ["open", "append", "append", "flush", "flush"]
    await _w(session.close())


@pytest.mark.asyncio
async def test_close_returns_region_to_idle_pool_and_reuses_it(env):
    rt = env.rt
    session, _ = await _open(env)
    region = session.region
    data = _payload(3 * MiB, seed=4)
    await _w(session.append(data))
    persisted = await _w(session.close())
    assert persisted == len(data)
    assert not session.is_open
    assert session.region is None
    assert region in rt._idle_write_regions
    assert not region.closed
    assert region.all_free()
    assert rt._live_regions == 1

    session2, _ = await _open(env)
    assert session2.region is region
    assert env.fake.last.spec.write_region_id == region.region_id
    assert len(env.shm.regions) == 1  # no new region was handed out
    await _w(session2.append(b"x"))
    assert await _w(session2.close()) == 1
    assert bytes(env.fake.last.data) == b"x"


@pytest.mark.asyncio
async def test_close_discards_region_when_slots_not_released(env):
    env.fake.release_on_close = False
    rt = env.rt
    session, _ = await _open(env)
    region = session.region
    assert rt._live_regions == 1
    data = _payload(3 * MiB, seed=5)
    await _w(session.append(data))
    persisted = await _w(session.close())
    assert persisted == len(data)
    assert bytes(env.fake.last.data) == data
    assert region not in rt._idle_write_regions
    assert region.closed
    assert rt._live_regions == 0


@pytest.mark.asyncio
async def test_finalize_with_matching_crc_returns_object_resource(env):
    session, _ = await _open(env, obj="fin")
    data = _payload(5 * MiB + 9, seed=6)
    for i in range(0, len(data), 1_500_000):
        await _w(session.append(data[i : i + 1_500_000]))
    crc = google_crc32c.value(data)
    obj = await _w(session.finalize(crc))
    assert isinstance(obj, pb.ObjectResource)
    assert obj.size == len(data)
    assert obj.name == "fin"
    assert obj.generation == GENERATION
    assert obj.crc32c == crc
    st = env.fake.last
    assert bytes(st.data) == data
    assert st.ops[-1] == ("finalize", st.ops[-1][1], crc)
    _assert_slot_packing(st)
    assert not session.is_open
    assert env.rt._idle_write_regions and not env.rt._idle_write_regions[-1].closed


@pytest.mark.asyncio
async def test_finalize_without_crc_omits_field(env):
    session, _ = await _open(env)
    await _w(session.append(b"abc"))
    obj = await _w(session.finalize(None))
    assert obj.size == 3
    assert env.fake.last.ops[-1][0] == "finalize"
    assert env.fake.last.ops[-1][2] is None


@pytest.mark.asyncio
async def test_finalize_with_mismatching_crc_raises_invalid_argument(env):
    session, _ = await _open(env)
    region = session.region
    data = _payload(3 * MiB, seed=8)
    await _w(session.append(data))
    bad = google_crc32c.value(data) ^ 0x1
    with pytest.raises(exceptions.InvalidArgument):
        await _w(session.finalize(bad))
    assert not session.is_open
    assert session.region is None
    assert region.closed
    assert region not in env.rt._idle_write_regions
    assert env.rt._live_regions == 0


@pytest.mark.asyncio
async def test_op_id_echo_routing_ignores_unknown_op_ids(env):
    env.fake.noise = True
    session, _ = await _open(env)
    await _w(session.append(_payload(MiB, seed=9)))
    assert await _w(session.flush()) == MiB
    await _w(session.append(_payload(SLOT + 5, seed=10)))
    assert await _w(session.flush()) == MiB + SLOT + 5
    assert await _w(session.close()) == MiB + SLOT + 5

    st = env.fake.last
    req_ids = [op_id for k, op_id, _ in st.ops if k in ("open", "flush", "close")]
    assert req_ids == sorted(req_ids)
    assert len(set(req_ids)) == len(req_ids)
    assert all(op_id > 0 for op_id in req_ids)
    # Every control op got its own op_id echoed back.
    for kind, op_id, _ in st.ops:
        reply = {"open": "opened", "flush": "flushed", "close": "closed"}.get(kind)
        if reply:
            assert (reply, op_id) in st.replies
    assert st.violations == []


@pytest.mark.asyncio
async def test_inline_mode_when_shm_disabled(env, monkeypatch):
    monkeypatch.setenv("GOOGLE_CLOUD_STORAGE_UDS_SHM", "off")
    session, _ = await _open(env)
    assert session.region is None
    st = env.fake.last
    assert st.spec.write_region_id == 0
    sizes = [3 * MiB + 1, MiB, 5]
    chunks = [_payload(n, seed=300 + i) for i, n in enumerate(sizes)]
    for chunk in chunks:
        await _w(session.append(chunk))
    expected = b"".join(chunks)
    assert await _w(session.flush()) == len(expected)
    await _w(session.append(b"tail"))
    expected += b"tail"
    assert await _w(session.close()) == len(expected)

    assert bytes(st.data) == expected
    inline = [(i, n) for i, (k, _, n) in enumerate(st.ops) if k == "inline"]
    assert inline
    assert all(0 < n <= INLINE_CHUNK for _, n in inline)
    for i, n in inline:
        if n != INLINE_CHUNK:
            assert st.ops[i + 1][0] in ("flush", "close", "finalize")
    assert not [k for k, _, _ in st.ops if k == "append"]
    assert session.slot_submissions == []
    assert env.shm.regions == {}


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "code, exc_type",
    [
        (grpc.StatusCode.NOT_FOUND, exceptions.NotFound),
        (grpc.StatusCode.FAILED_PRECONDITION, exceptions.FailedPrecondition),
    ],
)
async def test_open_error_maps_exception_and_returns_region(env, code, exc_type):
    env.fake.open_error = code
    session = UdsWriteSession(env.rt)
    with pytest.raises(exc_type):
        await _w(session.open(pb.OpenAppendSpec(bucket="b", object="missing")))
    assert not session.is_open
    assert session.region is None
    assert env.fake.last.spec.write_region_id != 0
    idle = env.rt._idle_write_regions
    assert len(idle) == 1
    assert idle[0].region_id == env.fake.last.spec.write_region_id
    assert not idle[0].closed and idle[0].all_free()


@pytest.mark.asyncio
async def test_public_appendable_writer_goes_through_uds(env):
    writer = AsyncAppendableObjectWriter(
        env.client, "b", "pub", writer_options={"FLUSH_INTERVAL_BYTES": 4 * MiB}
    )
    await _w(writer.open())
    assert writer._uds is not None
    assert writer.is_stream_open
    assert writer.generation == GENERATION
    assert writer.persisted_size == 0

    first = _payload(5 * MiB, seed=11)
    await _w(writer.append(first))
    st = env.fake.last
    # The 4 MiB flush interval forced one Flush in the middle of the append.
    assert st.kinds().count("flush") == 1
    assert writer.persisted_size == 4 * MiB
    assert await _w(writer.flush()) == len(first)
    assert writer.persisted_size == len(first)

    second = _payload(MiB + 3, seed=12)
    await _w(writer.append(second))
    data = first + second
    crc = google_crc32c.value(data)
    obj = await _w(writer.close(finalize_on_close=True, full_object_checksum=crc))
    assert obj is writer.object_resource
    assert obj.size == len(data)
    assert obj.name == "pub"
    assert writer.persisted_size == len(data)
    assert writer._uds is None
    assert not writer.is_stream_open
    assert bytes(st.data) == data
    assert st.spec.bucket == "b" and st.spec.object == "pub"
    assert st.ops[-1][0] == "finalize" and st.ops[-1][2] == crc
    _assert_slot_packing(st)


@pytest.mark.asyncio
async def test_open_keeps_caller_user_agent(env):
    session = UdsWriteSession(env.rt)
    spec = pb.OpenAppendSpec(bucket="b", object="o", user_agent="custom-agent/1.0")
    await _w(session.open(spec))
    assert env.fake.last.spec.user_agent == "custom-agent/1.0"
    await _w(session.close())


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "open_replies",
    [[], [{"flushed": pb.Flushed(persisted_size=0)}]],
    ids=["eof", "wrong-reply"],
)
async def test_open_without_write_opened_raises_and_returns_region(env, open_replies):
    env.fake.open_replies = open_replies
    session = UdsWriteSession(env.rt)
    with pytest.raises(exceptions.GoogleAPICallError, match="before WriteOpened"):
        await _w(session.open(pb.OpenAppendSpec(bucket="b", object="o")))
    assert not session.is_open
    assert session.region is None
    idle = env.rt._idle_write_regions
    assert len(idle) == 1 and not idle[0].closed and idle[0].all_free()


@pytest.mark.asyncio
async def test_append_casts_non_byte_buffers(env):
    session, _ = await _open(env)
    data = array.array("I", range(300_000))  # itemsize 4: not a "B" memoryview
    await _w(session.append(data))
    await _w(session.flush())
    assert bytes(env.fake.last.data) == data.tobytes()
    await _w(session.close())


@pytest.mark.asyncio
async def test_close_error_discards_region(env):
    env.fake.close_error = grpc.StatusCode.ABORTED
    session, _ = await _open(env)
    region = session.region
    await _w(session.append(b"abc"))
    with pytest.raises(exceptions.Aborted):
        await _w(session.close())
    assert not session.is_open
    assert session.region is None
    assert region.closed
    assert region not in env.rt._idle_write_regions
    assert env.rt._live_regions == 0


@pytest.mark.asyncio
async def test_abort_releases_partial_slot_discards_region_and_is_idempotent(env):
    session, _ = await _open(env)
    region = session.region
    await _w(session.append(b"partial"))
    assert session._cur_slot is not None
    await _w(session.abort())
    assert not session.is_open
    assert session.region is None
    assert session._cur_slot is None
    assert session._reader.done()
    assert region.closed
    assert env.rt._live_regions == 0
    assert "close" not in env.fake.last.kinds()
    await _w(session.abort())  # nothing left to tear down
    assert not session.is_open


@pytest.mark.asyncio
async def test_finalize_empty_object(env):
    session, _ = await _open(env, obj="empty")
    obj = await _w(session.finalize(None))
    assert obj.size == 0
    assert env.fake.last.kinds() == ["open", "finalize"]


@pytest.mark.asyncio
async def test_fake_records_protocol_violations(env):
    """Self-check: the ``violations == []`` assertions above can actually fail."""
    session, _ = await _open(env)
    other, _ = await _open(env)
    own_id = session.region.region_id
    other_id = other.region.region_id
    assert own_id != other_id

    def ref(region_id, slot):
        slot_ref = pb.ShmSlotRef(region_id=region_id, slot=slot, length=1)
        return pb.BidiWriteObjectRequest(append=pb.Append(slot=slot_ref))

    await _w(session._send(ref(own_id, 0)))
    await _w(session._send(ref(own_id, 0)))  # slot 0 again, never released
    await _w(session._send(ref(other_id, 1)))  # someone else's region
    await _w(session.flush())
    assert env.fake.streams[0].violations == [
        ("reused-unreleased", 0),
        ("region", other_id),
    ]
    await _w(session.close())
    await _w(other.close())


# ------------------------------------------------------- unit tests (no server)


def _rpc_error(code=grpc.StatusCode.UNAVAILABLE, details="boom"):
    return grpc.aio.AioRpcError(code, grpc.aio.Metadata(), grpc.aio.Metadata(), details)


class _ScriptedCall:
    """Minimal stand-in for a ``grpc.aio`` stream-stream call.

    ``read()`` returns the scripted replies in order, then blocks forever.
    """

    def __init__(self, replies=(), write_exc=None, done_writing_exc=None):
        self._replies = list(replies)
        self._write_exc = write_exc
        self._done_writing_exc = done_writing_exc
        self.written = []
        self.cancelled = False

    async def read(self):
        if not self._replies:
            await asyncio.Event().wait()
        return self._replies.pop(0)

    async def write(self, req):
        if self._write_exc is not None:
            raise self._write_exc
        self.written.append(req)

    async def done_writing(self):
        if self._done_writing_exc is not None:
            raise self._done_writing_exc

    def cancel(self):
        self.cancelled = True


async def _forever():
    await asyncio.Event().wait()


@pytest.mark.asyncio
async def test_read_loop_without_region_tolerates_releases_and_internal_flush():
    session = UdsWriteSession(mock.Mock())
    session._internal_flush = 5
    call = _ScriptedCall(
        [
            pb.BidiWriteObjectResponse(released=pb.SlotsReleased(slots=[1])),
            pb.BidiWriteObjectResponse(op_id=5, flushed=pb.Flushed(persisted_size=9)),
            grpc.aio.EOF,
        ]
    )
    await _w(session._read_loop(call))
    assert session._internal_flush is None
    assert session.last_persisted_size == 9
    assert session._error is None
    assert not session.is_open


@pytest.mark.asyncio
async def test_read_loop_eof_fails_pending_ops():
    loop = asyncio.get_running_loop()
    session = UdsWriteSession(mock.Mock())
    session._region = mock.Mock()
    done, pending = loop.create_future(), loop.create_future()
    done.set_result("already answered")
    session._waiters = {1: done, 2: pending}
    await _w(session._read_loop(_ScriptedCall([grpc.aio.EOF])))
    assert isinstance(session._error, exceptions.ServiceUnavailable)
    assert pending.exception() is session._error
    assert done.result() == "already answered"
    assert session._waiters == {}
    session._region.fail_waiters.assert_called_once_with()


@pytest.mark.asyncio
async def test_read_loop_cancellation_records_cancelled_error():
    session = UdsWriteSession(mock.Mock())
    session.is_open = True
    task = asyncio.ensure_future(session._read_loop(_ScriptedCall()))
    await asyncio.sleep(0)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert isinstance(session._error, exceptions.Cancelled)
    assert not session.is_open


@pytest.mark.asyncio
async def test_append_raises_stored_error_or_not_open():
    session = UdsWriteSession(mock.Mock())
    with pytest.raises(ValueError, match="Stream is not open"):
        await session.append(b"x")
    session._error = exceptions.Aborted("stream broke")
    with pytest.raises(exceptions.Aborted, match="stream broke"):
        await session.append(b"x")


@pytest.mark.asyncio
async def test_op_write_failure_maps_rpc_error_and_drops_waiter():
    session = UdsWriteSession(mock.Mock())
    session._call = _ScriptedCall(write_exc=_rpc_error())
    with pytest.raises(exceptions.ServiceUnavailable, match="boom"):
        await _w(session._op(flush=pb.Flush()))
    assert session._waiters == {}


@pytest.mark.asyncio
async def test_op_write_failure_prefers_reader_error():
    session = UdsWriteSession(mock.Mock())
    session._call = _ScriptedCall(write_exc=asyncio.InvalidStateError())

    async def _failing_reader():
        session._error = exceptions.NotFound("object gone")

    session._reader = asyncio.ensure_future(_failing_reader())
    with pytest.raises(exceptions.NotFound, match="object gone"):
        await _w(session._op(flush=pb.Flush()))
    assert session._waiters == {}


@pytest.mark.asyncio
async def test_wait_reader_swallows_timeouts_and_reader_errors():
    session = UdsWriteSession(mock.Mock())
    await session._wait_reader()  # no reader

    session._reader = asyncio.ensure_future(_forever())
    await _w(session._wait_reader(timeout=0.01))
    assert not session._reader.done()  # shielded: the reader keeps running
    session._reader.cancel()
    with pytest.raises(asyncio.CancelledError):
        await session._reader
    await session._wait_reader()  # reader already done

    async def _broken():
        raise RuntimeError("reader crashed")

    session._reader = asyncio.ensure_future(_broken())
    await _w(session._wait_reader())
    assert isinstance(session._reader.exception(), RuntimeError)


@pytest.mark.asyncio
async def test_acquire_slot_sends_one_internal_flush_and_rechecks_free():
    session = UdsWriteSession(mock.Mock())
    session._call = _ScriptedCall()
    region = mock.Mock(free_count=1)  # a release raced in after try_acquire()
    region.try_acquire.side_effect = [None, None, 3]
    region._ev.return_value = asyncio.Event()
    session._region = region
    assert await _w(session._acquire_slot()) == 3
    # The second starved iteration reuses the in-flight starvation Flush.
    assert len(session._call.written) == 1
    assert session._call.written[0].HasField("flush")
    assert session._internal_flush == session._call.written[0].op_id


@pytest.mark.asyncio
async def test_submit_current_returns_empty_slot_unsubmitted():
    session = UdsWriteSession(mock.Mock())
    session._region = mock.Mock()
    session._cur_slot, session._cur_fill = 2, 0
    await session._submit_current()
    session._region.unacquire.assert_called_once_with(2)
    assert session._cur_slot is None
    assert session.slot_submissions == []


@pytest.mark.asyncio
@pytest.mark.parametrize("done_writing_exc", [None, _rpc_error()], ids=["ok", "error"])
async def test_teardown_reusable_tolerates_done_writing_errors(done_writing_exc):
    rt = mock.Mock()
    session = UdsWriteSession(rt)
    call = _ScriptedCall(done_writing_exc=done_writing_exc)
    session._call, session.is_open = call, True
    await _w(session._teardown(reusable=True))
    assert call.cancelled
    assert session._call is None
    assert not session.is_open
    rt.return_write_region.assert_not_called()
