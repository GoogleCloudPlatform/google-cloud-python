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

"""``BidiReadObject`` session over UDS: one stream == one Rust ``ObjectDescriptor``."""

from __future__ import annotations

import asyncio
import itertools
import logging
from typing import Dict, List, Optional, Sequence, Tuple

import grpc
from google.api_core import exceptions

from google.cloud.storage.asyncio._uds import gcscore_pb2 as pb
from google.cloud.storage.asyncio._uds.errors import (
    object_from_resource,
    range_error_to_exception,
    to_api_exception,
)

logger = logging.getLogger(__name__)

_MAX_RESUME_ATTEMPTS = 3


class _RangeState:
    __slots__ = ("range_id", "offset", "length", "buf", "written", "fut")

    def __init__(self, range_id, offset, length, buf, fut):
        self.range_id = range_id
        self.offset = offset
        self.length = length
        self.buf = buf
        self.written = 0
        self.fut = fut


class UdsReadSession:
    """Thin client for one ``gcscore.v1.GcsCore/BidiReadObject`` stream."""

    def __init__(
        self,
        runtime,
        bucket_name: str,
        object_name: str,
        generation: Optional[int] = None,
        metadata: Optional[Sequence[Tuple[str, str]]] = None,
    ) -> None:
        self._rt = runtime
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.generation = generation
        self._quota_project = ""
        for k, v in metadata or ():
            if k.lower() == "x-goog-user-project":
                self._quota_project = v
            else:
                logger.debug("UDS read session ignores metadata %r", k)
        self.resource: Optional[pb.ObjectResource] = None
        self.object_metadata = None
        self._call = None
        self._region = None
        self._ids = itertools.count(1)
        self._ranges: Dict[int, _RangeState] = {}
        self._cancelled: set = set()
        self._send_q: Optional[asyncio.Queue] = None
        self._reader: Optional[asyncio.Task] = None
        self._writer: Optional[asyncio.Task] = None
        self._error: Optional[BaseException] = None
        self._closing = False
        self._epoch = 0  # incremented on every (re)open
        self._reopen_lock: Optional[asyncio.Lock] = None
        self.is_open = False

    # ----------------------------------------------------------------- open

    async def open(self) -> pb.ObjectResource:
        self._region = await self._rt.read_region()
        spec = pb.OpenReadSpec(
            bucket=self.bucket_name,
            object=self.object_name,
            generation=self.generation or 0,
            read_region_id=self._region.region_id if self._region else 0,
            compute_full_crc32c=True,
            quota_project=self._quota_project,
            user_agent=self._rt.user_agent,
        )
        call = self._rt.bidi_read(metadata=self._rt.metadata)
        try:
            await call.write(pb.BidiReadObjectRequest(open=spec))
            resp = await call.read()
        except grpc.RpcError as exc:
            call.cancel()
            raise to_api_exception(exc) from None
        if resp is grpc.aio.EOF or resp.WhichOneof("msg") != "opened":
            code = await call.code()
            call.cancel()
            raise exceptions.from_grpc_status(
                code or grpc.StatusCode.INTERNAL,
                "BidiReadObject ended before ReadOpened",
            )
        self._call = call
        self._epoch += 1
        self.resource = resp.opened.object
        self.object_metadata = object_from_resource(self.resource)
        if not self.generation:
            self.generation = self.resource.generation
        self._error = None
        self._send_q = asyncio.Queue()
        loop = asyncio.get_running_loop()
        self._writer = loop.create_task(self._write_loop(call, self._send_q))
        self._reader = loop.create_task(self._read_loop(call))
        self.is_open = True
        return self.resource

    # ----------------------------------------------------------- background

    def _send_nowait(self, req) -> None:
        if self._send_q is not None:
            self._send_q.put_nowait(req)

    async def _write_loop(self, call, q: asyncio.Queue) -> None:
        try:
            while True:
                req = await q.get()
                if req is None:
                    await call.done_writing()
                    return
                await call.write(req)
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # stream broken; the reader reports the status
            logger.debug("UDS read session writer stopped: %s", exc)

    async def _read_loop(self, call) -> None:
        err: Optional[BaseException] = None
        try:
            while True:
                resp = await call.read()
                if resp is grpc.aio.EOF:
                    break
                kind = resp.WhichOneof("msg")
                if kind == "data":
                    self._on_data(resp.data)
                elif kind == "range_error":
                    e = resp.range_error
                    st = self._ranges.pop(e.range_id, None)
                    self._cancelled.discard(e.range_id)
                    if st is not None and not st.fut.done():
                        st.fut.set_exception(range_error_to_exception(e))
        except asyncio.CancelledError:
            err = exceptions.Cancelled("read session closed")
            raise
        except grpc.RpcError as exc:
            err = to_api_exception(exc)
        except Exception as exc:  # pragma: NO COVER - defensive
            err = exc
        finally:
            if err is None and not self._closing:
                err = exceptions.ServiceUnavailable(
                    "UDS BidiReadObject stream ended with pending ranges"
                )
            if err is not None:
                self._error = err
            self.is_open = False
            for st in list(self._ranges.values()):
                if not st.fut.done():
                    st.fut.set_exception(
                        err or exceptions.Cancelled("read session closed")
                    )
            self._ranges.clear()

    def _on_data(self, d) -> None:
        st = self._ranges.get(d.range_id)
        try:
            if d.HasField("slot"):
                n = d.slot.length
                try:
                    if st is not None and not st.fut.done() and n:
                        with self._region.view(d.slot.slot, n) as mv:
                            st.buf.write(mv)
                        st.written += n
                finally:
                    # Always return the slot, also for cancelled / unknown ranges.
                    self._send_nowait(
                        pb.BidiReadObjectRequest(
                            release=pb.ReleaseSlots(slots=[d.slot.slot])
                        )
                    )
            elif d.inline_data and st is not None and not st.fut.done():
                st.buf.write(d.inline_data)
                st.written += len(d.inline_data)
        except Exception as exc:  # user buffer failed
            if st is not None and not st.fut.done():
                st.fut.set_exception(exc)
            return
        if d.range_end:
            self._ranges.pop(d.range_id, None)
            self._cancelled.discard(d.range_id)
            if st is not None and not st.fut.done():
                st.fut.set_result(st.written)

    # ---------------------------------------------------------------- reads

    async def download_ranges(self, read_ranges: List[Tuple[int, int, object]]) -> None:
        """Downloads ``(offset, length, buffer)`` ranges; ``length == 0`` reads to EOF."""
        if not read_ranges:
            return
        loop = asyncio.get_running_loop()
        states = []
        for offset, length, buf in read_ranges:
            states.append(_RangeState(0, offset, length, buf, None))
        attempt = 0
        pending = states
        epoch = self._epoch
        while True:
            attempt += 1
            if self._error is not None or not self.is_open:
                if isinstance(self._error, exceptions.ServiceUnavailable) and (
                    attempt <= _MAX_RESUME_ATTEMPTS
                ):
                    await self._reopen_once(epoch)
                else:
                    raise self._error or ValueError(
                        "Underlying bidi-gRPC stream is not open"
                    )
            epoch = self._epoch
            specs = []
            for st in pending:
                st.range_id = next(self._ids)
                st.fut = loop.create_future()
                self._ranges[st.range_id] = st
                if st.length > 0:
                    length = st.length - st.written
                else:
                    length = 0
                specs.append(
                    pb.RangeSpec(
                        range_id=st.range_id,
                        offset=st.offset + st.written,
                        length=length,
                    )
                )
            self._send_nowait(
                pb.BidiReadObjectRequest(read=pb.ReadRanges(ranges=specs))
            )
            try:
                await asyncio.wait([st.fut for st in pending])
            except asyncio.CancelledError:
                ids = [st.range_id for st in pending if not st.fut.done()]
                for st in pending:
                    if not st.fut.done():
                        self._ranges.pop(st.range_id, None)
                        self._cancelled.add(st.range_id)
                        st.fut.cancel()
                if ids and self.is_open:
                    self._send_nowait(
                        pb.BidiReadObjectRequest(cancel=pb.CancelRanges(range_ids=ids))
                    )
                raise
            errors = []
            for st in pending:
                exc = st.fut.exception()
                if exc is not None:
                    errors.append((st, exc))
            if not errors:
                return
            # Resume only ranges lost to a broken UDS stream (the stream of this attempt
            # died with UNAVAILABLE, possibly already replaced by a concurrent call);
            # per-range GCS errors reported while the stream stayed up are final.
            stream_lost = self._epoch != epoch or isinstance(
                self._error, exceptions.ServiceUnavailable
            )
            resumable = [
                st
                for st, exc in errors
                if stream_lost and isinstance(exc, exceptions.ServiceUnavailable)
            ]
            if len(resumable) == len(errors) and attempt <= _MAX_RESUME_ATTEMPTS:
                logger.info(
                    "UDS read stream lost (%s); resuming %d range(s)",
                    self._error,
                    len(resumable),
                )
                pending = resumable
                continue
            raise errors[0][1]

    async def _reopen_once(self, failed_epoch: int) -> None:
        """Re-opens the stream that broke at ``failed_epoch`` exactly once.

        Concurrent ``download_ranges`` calls that observed the same broken stream share a
        single re-open; later callers just reuse the replacement stream.
        """
        if self._reopen_lock is None:
            self._reopen_lock = asyncio.Lock()
        async with self._reopen_lock:
            if self._epoch == failed_epoch and (
                self._error is not None or not self.is_open
            ):
                await self._shutdown(cancel=True)
                await self.open()
        if not self.is_open:
            raise self._error or exceptions.ServiceUnavailable(
                "UDS BidiReadObject stream could not be re-opened"
            )

    # ---------------------------------------------------------------- close

    async def _shutdown(self, cancel: bool) -> None:
        self._closing = True
        try:
            if self._send_q is not None and not cancel:
                self._send_q.put_nowait(None)
                if self._reader is not None:
                    try:
                        await asyncio.wait_for(asyncio.shield(self._reader), timeout=10)
                    except (asyncio.TimeoutError, Exception):
                        pass
            if self._call is not None:
                self._call.cancel()
            for t in (self._writer, self._reader):
                if t is not None and not t.done():
                    t.cancel()
                    try:
                        await t
                    except (asyncio.CancelledError, Exception):
                        pass
        finally:
            self._call = None
            self._send_q = None
            self._writer = None
            self._reader = None
            self.is_open = False
            self._closing = False

    async def close(self) -> None:
        await self._shutdown(cancel=False)
