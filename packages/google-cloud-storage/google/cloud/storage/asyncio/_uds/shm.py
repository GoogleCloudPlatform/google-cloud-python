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

"""Shared-memory regions received from ``gcs-core-server`` over ``<socket>.shm``.

On connect the server creates a sealed ``memfd`` (``F_SEAL_SHRINK|F_SEAL_GROW|
F_SEAL_SEAL``; an unlinked POSIX shm object on macOS), and sends a 16-byte
little-endian header ``(region_id: u64, size: u64)`` with the file descriptor attached
via ``SCM_RIGHTS``. The region lives until the client closes that socket (and the
server's last slot lease on it is dropped). Regions are mapped once and reused.
"""

from __future__ import annotations

import asyncio
import collections
import contextlib
import mmap
import os
import socket
import struct
from typing import Iterable, Optional

from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError

_HEADER = struct.Struct("<QQ")


class ShmRegion:
    """A server-created shared-memory region mapped into this process."""

    def __init__(
        self,
        sock: socket.socket,
        mm: mmap.mmap,
        region_id: int,
        size: int,
        slot_size: int,
        writable: bool,
    ) -> None:
        if slot_size <= 0 or size < slot_size:
            raise CoreSdkUnavailableError(
                f"shm region of {size} bytes cannot hold {slot_size}-byte slots"
            )
        self._sock = sock
        self.mm = mm
        self.region_id = region_id
        self.size = size
        self.slot_size = slot_size
        self.writable = writable
        self.n_slots = size // slot_size
        self.closed = False

    @classmethod
    def connect(
        cls,
        shm_socket_path: str,
        slot_size: int,
        writable: bool,
        timeout: float = 5.0,
        verify_peer: bool = True,
    ) -> "ShmRegion":
        """Connects to ``<socket>.shm`` and maps the region it hands out."""
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        fds = []
        try:
            sock.connect(shm_socket_path)
            if verify_peer:
                from google.cloud.storage.asyncio._uds.server_manager import peer_uid

                uid = peer_uid(sock)
                if uid != os.getuid():
                    raise CoreSdkUnavailableError(
                        f"{shm_socket_path} is served by uid {uid}, not {os.getuid()}"
                    )
            msg, fds, _flags, _addr = socket.recv_fds(sock, _HEADER.size, 1)
            if len(msg) != _HEADER.size or len(fds) != 1:
                raise CoreSdkUnavailableError(
                    f"malformed shm handshake from {shm_socket_path} "
                    f"({len(msg)} bytes, {len(fds)} fds)"
                )
            region_id, size = _HEADER.unpack(msg)
            if os.fstat(fds[0]).st_size < size:
                raise CoreSdkUnavailableError("shm fd is smaller than advertised")
            prot = mmap.PROT_READ | (mmap.PROT_WRITE if writable else 0)
            mm = mmap.mmap(fds[0], size, flags=mmap.MAP_SHARED, prot=prot)
        except CoreSdkUnavailableError:
            sock.close()
            raise
        except OSError as exc:
            sock.close()
            raise CoreSdkUnavailableError(
                f"shm handshake with {shm_socket_path} failed: {exc}"
            ) from exc
        finally:
            for fd in fds:
                os.close(fd)
        sock.settimeout(None)
        return cls(sock, mm, region_id, size, slot_size, writable)

    def _bounds(self, slot: int, length: int) -> int:
        if not 0 <= slot < self.n_slots:
            raise ValueError(f"slot {slot} out of range (n={self.n_slots})")
        if not 0 <= length <= self.slot_size:
            raise ValueError(f"length {length} exceeds slot size {self.slot_size}")
        return slot * self.slot_size

    @contextlib.contextmanager
    def view(self, slot: int, length: int):
        """Yields a transient ``memoryview`` of ``length`` bytes of ``slot``.

        The view is released on exit so :meth:`close` never hits ``BufferError``.
        """
        off = self._bounds(slot, length)
        base = memoryview(self.mm)
        try:
            mv = base[off : off + length]
            try:
                yield mv
            finally:
                mv.release()
        finally:
            base.release()

    def write(self, slot: int, offset_in_slot: int, data) -> None:
        """Copies ``data`` into ``slot`` at ``offset_in_slot`` (one memcpy)."""
        n = len(data)
        off = self._bounds(slot, offset_in_slot + n) + offset_in_slot
        self.mm[off : off + n] = data

    def close(self) -> None:
        if self.closed:
            return
        self.closed = True
        try:
            self.mm.close()
        finally:
            self._sock.close()


class WriteRegion(ShmRegion):
    """A region whose slots are allocated by the client (write path).

    A slot is FREE on the client only until it is submitted in an ``Append``; it becomes
    FREE again only when the server reports it in ``SlotsReleased`` (i.e. after the Rust
    SDK dropped the last ``Bytes`` referencing it).
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._free = collections.deque(range(self.n_slots))
        self._leased = set()
        self._event: Optional[asyncio.Event] = None

    def _ev(self) -> asyncio.Event:
        if self._event is None:
            self._event = asyncio.Event()
        return self._event

    @property
    def free_count(self) -> int:
        return len(self._free)

    def all_free(self) -> bool:
        return not self._leased and len(self._free) == self.n_slots

    def try_acquire(self) -> Optional[int]:
        if not self._free:
            return None
        slot = self._free.popleft()
        self._leased.add(slot)
        return slot

    async def acquire_slot(self, on_starved=None) -> int:
        """Returns a free slot, waiting for ``SlotsReleased`` if necessary.

        ``on_starved`` (async callable) is invoked when no slot is free so the caller can
        issue an internal ``Flush`` (forcing the SDK to ack and drop its replay buffer).
        """
        while True:
            slot = self.try_acquire()
            if slot is not None:
                return slot
            ev = self._ev()
            ev.clear()
            if on_starved is not None:
                await on_starved()
            if self._free:
                continue
            await ev.wait()

    def unacquire(self, slot: int) -> None:
        """Returns a slot that was acquired but never submitted."""
        if slot in self._leased:
            self._leased.discard(slot)
            self._free.appendleft(slot)
            self._ev().set()

    def on_released(self, slots: Iterable[int]) -> None:
        for s in slots:
            if s in self._leased:
                self._leased.discard(s)
                self._free.append(s)
        self._ev().set()

    def fail_waiters(self) -> None:
        """Wakes waiters (e.g. when the session failed)."""
        self._ev().set()
