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
"""Hermetic tests for ``google.cloud.storage.asyncio._uds.shm``.

A fake ``<socket>.shm`` server (AF_UNIX listener in a thread) hands out a
``memfd`` with the 16-byte little-endian ``(region_id, size)`` header via
``SCM_RIGHTS``, exactly like ``gcs-core-server``.
"""

import asyncio
import mmap
import os
import shutil
import socket
import struct
import tempfile
import threading
import time

import pytest

from google.cloud.storage.asyncio._uds import server_manager, shm
from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError

_SLOT = 64 * 1024
_SLOTS = 4
_SIZE = _SLOT * _SLOTS
_REGION_ID = 0xDEADBEEF01


class _FakeShmServer:
    """Serves one memfd region per connection on ``path``.

    ``mode`` selects the handshake: ``"ok"``, ``"no_fd"`` (header only),
    ``"short_header"`` (8 bytes + fd) or ``"small_fd"`` (fd smaller than advertised).
    """

    def __init__(self, path, size=_SIZE, region_id=_REGION_ID, mode="ok"):
        self.path = path
        self.size = size
        self.region_id = region_id
        self.mode = mode
        self.maps = []  # server-side mmaps (shared with the client)
        self.conns = []
        self._fds = []
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._sock.bind(path)
        self._sock.listen(8)
        self._sock.settimeout(0.2)
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._serve, daemon=True)
        self._thread.start()

    def _serve(self):
        while not self._stop.is_set():
            try:
                conn, _ = self._sock.accept()
            except (socket.timeout, OSError):
                continue
            self.conns.append(conn)
            fd = os.memfd_create("fake-gcs-core-shm", 0)
            self._fds.append(fd)
            actual = self.size // 2 if self.mode == "small_fd" else self.size
            os.ftruncate(fd, actual)
            self.maps.append(mmap.mmap(fd, actual, flags=mmap.MAP_SHARED))
            try:
                if self.mode == "no_fd":
                    conn.sendall(struct.pack("<QQ", self.region_id, self.size))
                elif self.mode == "short_header":
                    socket.send_fds(conn, [struct.pack("<Q", self.region_id)], [fd])
                else:
                    socket.send_fds(
                        conn, [struct.pack("<QQ", self.region_id, self.size)], [fd]
                    )
            except OSError:
                # The client may hang up before the handshake (e.g. peer-uid check).
                pass

    def close(self):
        self._stop.set()
        self._thread.join(timeout=5)
        self._sock.close()
        for c in self.conns:
            c.close()
        for m in self.maps:
            m.close()
        for fd in self._fds:
            os.close(fd)


@pytest.fixture
def sock_dir():
    # Short path: AF_UNIX socket paths are limited to ~108 bytes.
    d = tempfile.mkdtemp(prefix="shm", dir="/tmp")
    yield d
    shutil.rmtree(d, ignore_errors=True)


@pytest.fixture
def fake_server(sock_dir):
    servers = []

    def _make(**kwargs):
        srv = _FakeShmServer(os.path.join(sock_dir, f"s{len(servers)}.sock.shm"), **kwargs)
        servers.append(srv)
        return srv

    yield _make
    for srv in servers:
        srv.close()


def _wait_for_map(srv, n=1):
    for _ in range(500):
        if len(srv.maps) >= n:
            return srv.maps[n - 1]
        time.sleep(0.01)
    raise AssertionError("fake shm server never mapped the region")


def _anon_region(cls=shm.WriteRegion, n_slots=_SLOTS, writable=True):
    a, b = socket.socketpair()
    b.close()
    return cls(a, mmap.mmap(-1, _SLOT * n_slots), 7, _SLOT * n_slots, _SLOT, writable)


# --------------------------------------------------------------------- connect


def test_connect_maps_region_and_reads_server_bytes(fake_server):
    srv = fake_server()
    region = shm.ShmRegion.connect(srv.path, _SLOT, writable=False)
    try:
        assert region.region_id == _REGION_ID
        assert region.size == _SIZE
        assert region.slot_size == _SLOT
        assert region.n_slots == _SLOTS
        assert region.writable is False
        server_map = _wait_for_map(srv)
        payload = os.urandom(1000)
        server_map[2 * _SLOT : 2 * _SLOT + len(payload)] = payload
        with region.view(2, len(payload)) as mv:
            assert isinstance(mv, memoryview)
            assert bytes(mv) == payload
        with region.view(3, 0) as mv:
            assert len(mv) == 0
    finally:
        region.close()


def test_view_is_released_so_close_never_raises_buffer_error(fake_server):
    srv = fake_server()
    region = shm.ShmRegion.connect(srv.path, _SLOT, writable=False)
    for slot in range(_SLOTS):
        with region.view(slot, _SLOT) as mv:
            leaked = mv
    # The views were released on context exit: the mmap can be closed.
    region.close()
    assert region.closed is True
    with pytest.raises(ValueError):
        bytes(leaked)  # released memoryview
    region.close()  # idempotent


def test_view_bounds_errors(fake_server):
    srv = fake_server()
    region = shm.ShmRegion.connect(srv.path, _SLOT, writable=False)
    try:
        for slot, length in ((-1, 1), (_SLOTS, 1), (0, _SLOT + 1), (0, -1)):
            with pytest.raises(ValueError):
                with region.view(slot, length):
                    pass  # pragma: NO COVER
        # A failed bounds check leaves no exported buffer behind.
    finally:
        region.close()


def test_read_only_region_is_not_writable(fake_server):
    srv = fake_server()
    region = shm.ShmRegion.connect(srv.path, _SLOT, writable=False)
    try:
        with pytest.raises(TypeError):
            region.write(0, 0, b"nope")
        with region.view(0, 4) as mv:
            assert mv.readonly
            with pytest.raises(TypeError):
                mv[0:4] = b"nope"
    finally:
        region.close()


def test_writable_region_write_is_visible_to_server(fake_server):
    srv = fake_server()
    region = shm.WriteRegion.connect(srv.path, _SLOT, writable=True)
    try:
        assert isinstance(region, shm.WriteRegion)
        server_map = _wait_for_map(srv)
        region.write(1, 10, b"hello")
        region.write(1, 15, memoryview(b" world"))
        assert server_map[_SLOT + 10 : _SLOT + 21] == b"hello world"
        region.write(3, _SLOT - 3, b"end")
        assert server_map[_SIZE - 3 : _SIZE] == b"end"
        with region.view(1, 21) as mv:
            assert bytes(mv[10:]) == b"hello world"
    finally:
        region.close()


def test_write_bounds_errors(fake_server):
    srv = fake_server()
    region = shm.WriteRegion.connect(srv.path, _SLOT, writable=True)
    try:
        with pytest.raises(ValueError):
            region.write(0, _SLOT - 2, b"abc")  # crosses the slot boundary
        with pytest.raises(ValueError):
            region.write(_SLOTS, 0, b"a")
        with pytest.raises(ValueError):
            region.write(-1, 0, b"a")
    finally:
        region.close()


def test_slot_size_larger_than_region_is_rejected(fake_server):
    srv = fake_server(size=_SLOT)
    with pytest.raises(CoreSdkUnavailableError):
        shm.ShmRegion.connect(srv.path, 2 * _SLOT, writable=False)


def test_zero_slot_size_is_rejected():
    a, b = socket.socketpair()
    b.close()
    with pytest.raises(CoreSdkUnavailableError):
        shm.ShmRegion(a, mmap.mmap(-1, _SLOT), 1, _SLOT, 0, False)
    a.close()


def test_handshake_without_fd_is_rejected(fake_server):
    srv = fake_server(mode="no_fd")
    with pytest.raises(CoreSdkUnavailableError, match="malformed shm handshake"):
        shm.ShmRegion.connect(srv.path, _SLOT, writable=False)


def test_short_header_is_rejected(fake_server):
    srv = fake_server(mode="short_header")
    with pytest.raises(CoreSdkUnavailableError, match="malformed shm handshake"):
        shm.ShmRegion.connect(srv.path, _SLOT, writable=False)


def test_fd_smaller_than_advertised_is_rejected(fake_server):
    srv = fake_server(mode="small_fd")
    with pytest.raises(CoreSdkUnavailableError, match="smaller than advertised"):
        shm.ShmRegion.connect(srv.path, _SLOT, writable=False)


def test_connect_without_server_raises_core_sdk_unavailable(sock_dir):
    with pytest.raises(CoreSdkUnavailableError, match="handshake"):
        shm.ShmRegion.connect(os.path.join(sock_dir, "missing.shm"), _SLOT, writable=False)


def test_connect_rejects_server_owned_by_other_uid(fake_server, monkeypatch):
    srv = fake_server()
    monkeypatch.setattr(server_manager, "peer_uid", lambda s: os.getuid() + 1)
    with pytest.raises(CoreSdkUnavailableError, match="served by uid"):
        shm.ShmRegion.connect(srv.path, _SLOT, writable=False)
    # verify_peer=False skips the check entirely.
    region = shm.ShmRegion.connect(srv.path, _SLOT, writable=False, verify_peer=False)
    region.close()


def test_connect_verifies_peer_uid_by_default(fake_server, monkeypatch):
    srv = fake_server()
    seen = []
    real = server_manager.peer_uid

    def _spy(sock):
        uid = real(sock)
        seen.append(uid)
        return uid

    monkeypatch.setattr(server_manager, "peer_uid", _spy)
    shm.ShmRegion.connect(srv.path, _SLOT, writable=False).close()
    assert seen == [os.getuid()]


# ------------------------------------------------------------- WriteRegion slots


def test_write_region_acquire_release_bookkeeping():
    region = _anon_region()
    try:
        assert region.n_slots == _SLOTS
        assert region.free_count == _SLOTS
        assert region.all_free()
        got = [region.try_acquire() for _ in range(_SLOTS)]
        assert got == [0, 1, 2, 3]
        assert region.try_acquire() is None
        assert region.free_count == 0
        assert not region.all_free()
        region.on_released([2, 0])
        assert region.free_count == 2
        assert region.try_acquire() == 2  # FIFO over released slots
        region.on_released([99, 1])  # unknown slots are ignored
        assert region.free_count == 2
        region.on_released([1])  # double release is ignored
        assert region.free_count == 2
        region.on_released([2, 3])
        assert region.all_free()
    finally:
        region.close()


def test_unacquire_returns_slot_to_front():
    region = _anon_region()
    try:
        a = region.try_acquire()
        b = region.try_acquire()
        region.unacquire(b)
        assert region.try_acquire() == b
        region.unacquire(5)  # never leased: no-op
        region.unacquire(a)
        region.unacquire(a)  # second unacquire is a no-op
        assert region.free_count == _SLOTS - 1
        region.unacquire(b)
        assert region.all_free()
    finally:
        region.close()


@pytest.mark.asyncio
async def test_acquire_slot_waits_for_released_slot():
    region = _anon_region(n_slots=1)
    try:
        assert await region.acquire_slot() == 0
        waiter = asyncio.ensure_future(region.acquire_slot())
        await asyncio.sleep(0.05)
        assert not waiter.done()
        region.fail_waiters()  # wakes the waiter, which re-checks and keeps waiting
        await asyncio.sleep(0.05)
        assert not waiter.done()
        region.on_released([0])
        assert await asyncio.wait_for(waiter, 5) == 0
    finally:
        region.close()


@pytest.mark.asyncio
async def test_acquire_slot_calls_on_starved_when_exhausted():
    region = _anon_region(n_slots=2)
    calls = []

    async def on_starved():
        calls.append(region.free_count)
        region.on_released([1])  # e.g. an internal Flush made the server release

    try:
        assert await region.acquire_slot(on_starved) == 0
        assert await region.acquire_slot(on_starved) == 1
        assert calls == []
        assert await asyncio.wait_for(region.acquire_slot(on_starved), 5) == 1
        assert calls == [0]
    finally:
        region.close()


@pytest.mark.asyncio
async def test_acquire_slot_on_starved_then_waits_for_release():
    region = _anon_region(n_slots=1)
    calls = []

    async def on_starved():
        calls.append(True)

    try:
        await region.acquire_slot()
        waiter = asyncio.ensure_future(region.acquire_slot(on_starved))
        await asyncio.sleep(0.05)
        assert calls == [True]
        assert not waiter.done()
        region.unacquire(0)
        assert await asyncio.wait_for(waiter, 5) == 0
    finally:
        region.close()


def test_region_close_is_idempotent_and_closes_socket():
    region = _anon_region()
    sock = region._sock
    region.close()
    region.close()
    assert region.closed
    assert sock.fileno() == -1
    assert region.mm.closed
