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

"""``BidiWriteObject`` session over UDS: one stream == one Rust ``AppendableObjectWriter``.

Bytes are packed contiguously into 2 MiB slots of a per-writer shared-memory region; a
slot is submitted (``Append{slot, len}``) only when it is full or right before
``Flush`` / ``Close`` / ``Finalize``, so the Rust SDK's ``CoalescingBuffer`` stays on its
zero-copy fast path. A submitted slot is reused only after the server reports it in
``SlotsReleased`` (the SDK dropped the last ``Bytes`` referencing it). When no slot is
free and no flush is in flight, an internal ``Flush`` forces the SDK to acknowledge and
drop its replay buffer (watermark-deadlock guard).
"""

from __future__ import annotations

import asyncio
import itertools
import logging
from typing import Dict, Optional, Tuple

import grpc
from google.api_core import exceptions

from google.cloud.storage.asyncio._uds import gcscore_pb2 as pb
from google.cloud.storage.asyncio._uds.errors import stream_write, to_api_exception

logger = logging.getLogger(__name__)

INLINE_CHUNK = 2 * 1024 * 1024


class UdsWriteSession:
    """Thin client for one ``gcscore.v1.GcsCore/BidiWriteObject`` stream."""

    def __init__(self, runtime) -> None:
        self._rt = runtime
        self._call = None
        self._region = None
        self._ops = itertools.count(1)
        self._waiters: Dict[int, asyncio.Future] = {}
        self._internal_flush: Optional[int] = None
        self._reader: Optional[asyncio.Task] = None
        self._error: Optional[BaseException] = None
        self._cur_slot: Optional[int] = None
        self._cur_fill = 0
        self._inline_buf = bytearray()
        self.submitted_since_flush = 0
        self.last_persisted_size: Optional[int] = None
        self.generation: Optional[int] = None
        self.is_open = False
        self.slot_submissions = []  # (slot, length) log for diagnostics / tests

    @property
    def region(self):
        return self._region

    # ----------------------------------------------------------------- open

    async def open(self, spec: pb.OpenAppendSpec) -> Tuple[int, int]:
        self._region = await self._rt.lease_write_region()
        spec.write_region_id = self._region.region_id if self._region else 0
        if not spec.user_agent:
            spec.user_agent = self._rt.user_agent
        call = self._rt.bidi_write(metadata=self._rt.metadata)
        try:
            await stream_write(
                call, pb.BidiWriteObjectRequest(open=spec, op_id=next(self._ops))
            )
            resp = await call.read()
        except grpc.RpcError as exc:
            call.cancel()
            self._rt.return_write_region(self._region, reusable=True)
            self._region = None
            raise to_api_exception(exc) from None
        if resp is grpc.aio.EOF or resp.WhichOneof("msg") != "opened":
            code = await call.code()
            call.cancel()
            self._rt.return_write_region(self._region, reusable=True)
            self._region = None
            raise exceptions.from_grpc_status(
                code or grpc.StatusCode.INTERNAL,
                "BidiWriteObject ended before WriteOpened",
            )
        self._call = call
        self.generation = resp.opened.generation
        self.last_persisted_size = resp.opened.persisted_size
        self._reader = asyncio.get_running_loop().create_task(self._read_loop(call))
        self.is_open = True
        return resp.opened.generation, resp.opened.persisted_size

    # ----------------------------------------------------------- background

    async def _read_loop(self, call) -> None:
        err: Optional[BaseException] = None
        try:
            while True:
                resp = await call.read()
                if resp is grpc.aio.EOF:
                    break
                kind = resp.WhichOneof("msg")
                if kind == "released":
                    if self._region is not None:
                        self._region.on_released(resp.released.slots)
                    continue
                if kind == "flushed":
                    self.last_persisted_size = resp.flushed.persisted_size
                    if resp.op_id == self._internal_flush:
                        self._internal_flush = None
                        if self._region is not None:
                            self._region.fail_waiters()  # wake slot waiters to re-check
                fut = self._waiters.pop(resp.op_id, None)
                if fut is not None and not fut.done():
                    fut.set_result(resp)
        except asyncio.CancelledError:
            err = exceptions.Cancelled("write session closed")
            raise
        except grpc.RpcError as exc:
            err = to_api_exception(exc)
        except Exception as exc:  # pragma: NO COVER - defensive
            err = exc
        finally:
            if err is None and self._waiters:
                err = exceptions.ServiceUnavailable(
                    "UDS BidiWriteObject stream ended with pending operations"
                )
            if err is not None:
                self._error = err
            self.is_open = False
            for fut in self._waiters.values():
                if not fut.done():
                    fut.set_exception(
                        err or exceptions.Cancelled("write session closed")
                    )
            self._waiters.clear()
            if self._region is not None:
                self._region.fail_waiters()

    def _raise_if_failed(self) -> None:
        if self._error is not None:
            raise self._error
        if self._call is None:
            raise ValueError("Stream is not open.")

    async def _send(self, req: pb.BidiWriteObjectRequest) -> None:
        self._raise_if_failed()
        try:
            await stream_write(self._call, req)
        except (grpc.RpcError, asyncio.InvalidStateError) as exc:
            await self._wait_reader()
            if self._error is not None:
                raise self._error from None
            raise to_api_exception(exc) from None

    async def _op(self, **kwargs) -> pb.BidiWriteObjectResponse:
        op_id = next(self._ops)
        fut = asyncio.get_running_loop().create_future()
        self._waiters[op_id] = fut
        try:
            await self._send(pb.BidiWriteObjectRequest(op_id=op_id, **kwargs))
        except BaseException:
            self._waiters.pop(op_id, None)
            raise
        return await fut

    async def _wait_reader(self, timeout: float = 10.0) -> None:
        if self._reader is not None and not self._reader.done():
            try:
                await asyncio.wait_for(asyncio.shield(self._reader), timeout)
            except (asyncio.TimeoutError, Exception):
                pass

    # ---------------------------------------------------------------- slots

    async def _acquire_slot(self) -> int:
        region = self._region
        while True:
            self._raise_if_failed()
            slot = region.try_acquire()
            if slot is not None:
                return slot
            ev = region._ev()
            ev.clear()
            if self._internal_flush is None:
                # Starvation guard: force the SDK to ack and drop its replay buffer.
                op_id = next(self._ops)
                self._internal_flush = op_id
                await self._send(
                    pb.BidiWriteObjectRequest(op_id=op_id, flush=pb.Flush())
                )
            if region.free_count:
                continue
            await ev.wait()

    async def _submit_current(self) -> None:
        if self._cur_slot is None:
            return
        slot, n = self._cur_slot, self._cur_fill
        self._cur_slot, self._cur_fill = None, 0
        if n == 0:
            self._region.unacquire(slot)
            return
        self.slot_submissions.append((slot, n))
        await self._send(
            pb.BidiWriteObjectRequest(
                append=pb.Append(
                    slot=pb.ShmSlotRef(
                        region_id=self._region.region_id, slot=slot, length=n
                    )
                )
            )
        )
        self.submitted_since_flush += n

    async def _submit_inline(self, final: bool) -> None:
        while len(self._inline_buf) >= INLINE_CHUNK or (final and self._inline_buf):
            chunk = bytes(self._inline_buf[:INLINE_CHUNK])
            del self._inline_buf[:INLINE_CHUNK]
            await self._send(
                pb.BidiWriteObjectRequest(append=pb.Append(inline_data=chunk))
            )
            self.submitted_since_flush += len(chunk)

    async def _submit_pending(self) -> None:
        if self._region is not None:
            await self._submit_current()
        else:
            await self._submit_inline(final=True)

    # ------------------------------------------------------------------ API

    async def append(self, data) -> None:
        self._raise_if_failed()
        mv = memoryview(data)
        if mv.format != "B" or mv.ndim != 1:
            mv = mv.cast("B")
        if self._region is None:
            self._inline_buf += mv
            await self._submit_inline(final=False)
            return
        slot_size = self._region.slot_size
        pos, total = 0, len(mv)
        while pos < total:
            if self._cur_slot is None:
                self._cur_slot = await self._acquire_slot()
                self._cur_fill = 0
            n = min(slot_size - self._cur_fill, total - pos)
            self._region.write(self._cur_slot, self._cur_fill, mv[pos : pos + n])
            self._cur_fill += n
            pos += n
            if self._cur_fill == slot_size:
                await self._submit_current()

    async def flush(self) -> int:
        await self._submit_pending()
        resp = await self._op(flush=pb.Flush())
        self.submitted_since_flush = 0
        return resp.flushed.persisted_size

    def has_unflushed_bytes(self) -> bool:
        return bool(self.submitted_since_flush or self._cur_fill or self._inline_buf)

    async def close(self) -> int:
        await self._submit_pending()
        try:
            resp = await self._op(close=pb.Close())
        except BaseException:
            await self._teardown(reusable=False)
            raise
        await self._teardown(reusable=True)
        return resp.closed.persisted_size

    async def finalize(self, full_object_crc32c: Optional[int]) -> pb.ObjectResource:
        await self._submit_pending()
        fin = pb.Finalize()
        if full_object_crc32c is not None:
            fin.full_object_crc32c = full_object_crc32c
        try:
            resp = await self._op(finalize=fin)
        except BaseException:
            await self._teardown(reusable=False)
            raise
        await self._teardown(reusable=True)
        return resp.finalized.object

    async def abort(self) -> None:
        """Drops the stream without Close (the Rust writer is dropped unflushed)."""
        await self._teardown(reusable=False)

    async def _teardown(self, reusable: bool) -> None:
        call, self._call = self._call, None
        if call is not None and reusable:
            try:
                await call.done_writing()
            except Exception:
                pass
            await self._wait_reader()
        if call is not None:
            call.cancel()
        if self._reader is not None and not self._reader.done():
            self._reader.cancel()
            try:
                await self._reader
            except (asyncio.CancelledError, Exception):
                pass
        region, self._region = self._region, None
        if region is not None:
            if self._cur_slot is not None:
                region.unacquire(self._cur_slot)
                self._cur_slot = None
            self._rt.return_write_region(region, reusable=reusable)
        self.is_open = False
