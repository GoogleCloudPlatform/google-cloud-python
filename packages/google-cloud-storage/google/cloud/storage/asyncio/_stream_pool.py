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

from __future__ import annotations

import asyncio
import inspect
import logging
import math
from dataclasses import dataclass
from io import BytesIO
from typing import Awaitable, Callable, Dict, List, Optional, Tuple

from google.cloud.storage.asyncio._stream_multiplexer import _StreamMultiplexer
from google.cloud.storage.asyncio.async_read_object_stream import (
    _AsyncReadObjectStream,
)

logger = logging.getLogger(__name__)


@dataclass
class MultiStreamConfig:
    """Configuration parameters for multi-stream download scaling and load balancing.

    :type min_streams: int
    :param min_streams: Minimum number of streams opened at initialization. Defaults to 1.

    :type max_streams: int
    :param max_streams: Maximum concurrent streams allowed. Defaults to 8.

    :type target_io_depth: int
    :param target_io_depth: Target outstanding requests per stream before scaling up. Defaults to 8.

    :type target_bytes: int
    :param target_bytes: Target outstanding bytes per stream before scaling up. Defaults to 8 MB.
    """

    min_streams: int = 1
    max_streams: int = 8
    target_io_depth: int = 8
    target_bytes: int = 8 * 1024 * 1024

    def __post_init__(self) -> None:
        if self.min_streams < 1:
            raise ValueError("min_streams must be >= 1")
        if self.max_streams < self.min_streams:
            raise ValueError("max_streams must be >= min_streams")
        if self.target_io_depth <= 0:
            raise ValueError("target_io_depth must be > 0")
        if self.target_bytes <= 0:
            raise ValueError("target_bytes must be > 0")


class _PooledStream:
    """Wraps an active stream and its multiplexer with local load counters."""

    def __init__(
        self,
        stream: _AsyncReadObjectStream,
        multiplexer: _StreamMultiplexer,
    ):
        self.stream = stream
        self.multiplexer = multiplexer
        self.pending_ranges: int = 0
        self.pending_bytes: int = 0

    def calculate_load(self, target_io_depth: int, target_bytes: int) -> float:
        """Returns normalized load metric combining request count and bytes."""
        u_req = self.pending_ranges / target_io_depth if target_io_depth > 0 else 0.0
        u_bytes = self.pending_bytes / target_bytes if target_bytes > 0 else 0.0
        return 0.5 * (u_req + u_bytes)

    def is_fully_loaded(self, target_io_depth: int, target_bytes: int) -> bool:
        """Returns True if normalized load is at or above 1.0."""
        return self.calculate_load(target_io_depth, target_bytes) >= 1.0

    def record_request(self, range_count: int, byte_count: int) -> None:
        self.pending_ranges += range_count
        self.pending_bytes += byte_count

    def record_completion(self, range_count: int, byte_count: int) -> None:
        self.pending_ranges = max(0, self.pending_ranges - range_count)
        self.pending_bytes = max(0, self.pending_bytes - byte_count)

    async def close(self) -> None:
        """Closes the underlying multiplexer and stream cleanly."""
        try:
            await self.multiplexer.close()
        except Exception as e:
            logger.warning(f"Failed to close stream multiplexer: {e}")
        try:
            res = self.stream.close()
            if inspect.isawaitable(res):
                await res
        except Exception as e:
            logger.warning(f"Failed to close underlying read stream: {e}")


class _StreamPool:
    """Manages a pool of ``_PooledStream`` instances with dynamic scaling,
    hybrid stream selection, and contiguous range distribution.

    Each stream's normalized load is computed as an equal-weighted average of
    its request-count utilization and byte utilization relative to target
    thresholds::

        load = 0.5 * (pending_ranges / target_io_depth + pending_bytes / target_bytes)

    A stream is considered *fully loaded* when ``load >= 1.0``.

    **Hybrid Stream Selection Strategy:**

    1. **Least-Loaded across Base Streams (``streams[:min_streams]``):**
       Incoming ranges are first balanced across the initial ``min_streams``
       base streams by selecting the stream with the lowest normalized load,
       as long as that stream is not yet fully loaded (``load < 1.0``).
    2. **First-Fit across Scaled Streams (``streams[min_streams:]``):**
       Once all base streams are fully loaded (``load >= 1.0``), dynamically
       scaled streams are checked in creation order and the first stream with
       ``load < 1.0`` is selected. This packs work onto earlier scaled streams
       rather than spreading small amounts of load across all scaled streams.
    3. **Least-Loaded Fallback:**
       If every open stream in the pool is already at or above target capacity
       (``load >= 1.0``), the stream with the lowest normalized load across the
       entire pool is selected.

    **Contiguous Range Distribution:**
    When distributing a batch of ranges via :meth:`distribute_ranges`,
    consecutive ranges are assigned to the currently selected stream until its
    normalized load reaches ``1.0`` (or a water-filling target load cap when
    all streams are saturated and no further scale-up is possible), before
    moving to the next stream or triggering background scale-up for remaining
    overflow ranges.
    """

    def __init__(
        self,
        stream_factory: Callable[[], Awaitable[_PooledStream]],
        multi_stream_config: Optional[MultiStreamConfig] = None,
    ):
        config = multi_stream_config or MultiStreamConfig()
        self._stream_factory = stream_factory
        self.min_streams = config.min_streams
        self.max_streams = config.max_streams
        self.target_io_depth = config.target_io_depth
        self.target_bytes = config.target_bytes

        self.streams: List[_PooledStream] = []
        self._lock = asyncio.Lock()
        self._pending_scale_ups: int = 0
        self._closed = False
        self._background_tasks: set[asyncio.Task] = set()

    def effective_range_bytes(
        self,
        offset: int,
        length: int,
        persisted_size: Optional[int] = None,
    ) -> int:
        """Returns normalized byte length for load accounting, resolving
        ``length == 0`` ("read to end of object") using ``persisted_size`` or
        ``target_bytes`` as a fallback.
        """
        if length > 0:
            return length
        if persisted_size is not None:
            return max(0, persisted_size - offset)
        return self.target_bytes

    def _batch_load(
        self,
        ranges: List[Tuple[int, int, BytesIO]],
        persisted_size: Optional[int] = None,
    ) -> float:
        total_bytes = sum(
            self.effective_range_bytes(offset, length, persisted_size)
            for offset, length, _ in ranges
        )
        return 0.5 * (
            len(ranges) / self.target_io_depth + total_bytes / self.target_bytes
        )

    async def add_stream(self, pooled_stream: _PooledStream) -> None:
        async with self._lock:
            self.streams.append(pooled_stream)

    def _acquire_stream(self) -> _PooledStream:
        base_streams = self.streams[: self.min_streams]
        best_base = min(
            base_streams,
            key=lambda s: s.calculate_load(self.target_io_depth, self.target_bytes),
        )
        if not best_base.is_fully_loaded(self.target_io_depth, self.target_bytes):
            return best_base

        for stream in self.streams[self.min_streams :]:
            if not stream.is_fully_loaded(self.target_io_depth, self.target_bytes):
                return stream

        return min(
            self.streams,
            key=lambda s: s.calculate_load(self.target_io_depth, self.target_bytes),
        )

    def _maybe_scale_up(self, extra_load: float = 0.0) -> List[asyncio.Task]:
        total_load = (
            sum(
                s.calculate_load(self.target_io_depth, self.target_bytes)
                for s in self.streams
            )
            + extra_load
        )
        desired_streams = math.ceil(total_load)
        planned_streams = len(self.streams) + self._pending_scale_ups
        needed_scale_ups = max(
            0, min(desired_streams, self.max_streams) - planned_streams
        )

        tasks = []
        for _ in range(needed_scale_ups):
            self._pending_scale_ups += 1
            task = asyncio.create_task(self._scale_up())
            self._background_tasks.add(task)
            task.add_done_callback(self._background_tasks.discard)
            tasks.append(task)
        return tasks

    async def distribute_ranges(
        self,
        read_ranges: List[Tuple[int, int, BytesIO]],
        allow_scale_up: bool = True,
        persisted_size: Optional[int] = None,
    ) -> Tuple[
        Dict[_PooledStream, List[Tuple[int, int, BytesIO]]],
        List[Tuple[int, int, BytesIO]],
        List[asyncio.Task],
    ]:
        """Distributes ``read_ranges`` across open streams and triggers background
        scale-up when all currently open streams become fully loaded.

        :type read_ranges: List[Tuple[int, int, BytesIO]]
        :param read_ranges: List of ``(offset, length, buffer)`` tuples to distribute.

        :type allow_scale_up: bool
        :param allow_scale_up: If True, triggers background scale-up and defers
            remaining overflow ranges when all open streams reach full capacity.

        :type persisted_size: Optional[int]
        :param persisted_size: Known persisted object size used to estimate byte
            load when ``bytes_to_read == 0`` (read to end of object).

        :rtype: Tuple[Dict[_PooledStream, List[Tuple[int, int, BytesIO]]], List[Tuple[int, int, BytesIO]], List[asyncio.Task]]
        :returns: A 3-tuple ``(assignments, overflow, scale_tasks)``:
            - ``assignments``: Dictionary mapping each selected ``_PooledStream``
              to the contiguous list of ``read_ranges`` assigned to it for immediate
              download.
            - ``overflow``: List of remaining ``read_ranges`` that could not fit on
              the currently open streams because all streams reached full load and
              background scale-up tasks were started or are in flight. Empty if all
              ranges were assigned immediately.
            - ``scale_tasks``: List of background ``asyncio.Task`` objects currently
              opening new streams for ``overflow``. Empty if no scale-up was
              triggered or in flight for overflow.
        """
        async with self._lock:
            if self._closed:
                raise ValueError("Pool is closed")
            if not self.streams:
                raise ValueError("No streams available in stream pool")

            can_overflow = (
                allow_scale_up
                and (len(read_ranges) > 1 or bool(self._background_tasks))
                and (
                    len(self.streams) < self.max_streams or bool(self._background_tasks)
                )
            )
            existing_load = sum(
                s.calculate_load(self.target_io_depth, self.target_bytes)
                for s in self.streams
            )
            load_cap = (
                1.0
                if can_overflow
                else max(
                    1.0,
                    (existing_load + self._batch_load(read_ranges, persisted_size))
                    / len(self.streams),
                )
            )

            assignments: Dict[_PooledStream, List[Tuple[int, int, BytesIO]]] = {}
            current_stream: Optional[_PooledStream] = None

            for idx, read_range in enumerate(read_ranges):
                if current_stream is None or (
                    current_stream.calculate_load(
                        self.target_io_depth, self.target_bytes
                    )
                    >= load_cap
                    and (
                        can_overflow
                        or any(
                            s.calculate_load(self.target_io_depth, self.target_bytes)
                            < load_cap
                            for s in self.streams
                        )
                    )
                ):
                    current_stream = self._acquire_stream()
                    if can_overflow and all(
                        s.is_fully_loaded(self.target_io_depth, self.target_bytes)
                        for s in self.streams
                    ):
                        overflow = read_ranges[idx:]
                        self._maybe_scale_up(
                            extra_load=self._batch_load(overflow, persisted_size)
                        )
                        return assignments, overflow, list(self._background_tasks)

                req_bytes = self.effective_range_bytes(
                    read_range[0], read_range[1], persisted_size
                )
                current_stream.record_request(1, req_bytes)
                assignments.setdefault(current_stream, []).append(read_range)

            if allow_scale_up:
                self._maybe_scale_up()
            return assignments, [], []

    async def _scale_up(self) -> None:
        new_stream: Optional[_PooledStream] = None
        added = False
        try:
            new_stream = await self._stream_factory()
            async with self._lock:
                if not self._closed:
                    self.streams.append(new_stream)
                    added = True
        except Exception as e:
            logger.warning(f"Failed to scale up MRD stream: {e}")
        finally:
            if new_stream is not None and not added:
                await new_stream.close()
            async with self._lock:
                self._pending_scale_ups = max(0, self._pending_scale_ups - 1)

    def release_stream(
        self, pooled_stream: _PooledStream, range_count: int, req_bytes: int
    ) -> None:
        pooled_stream.record_completion(range_count, req_bytes)

    async def close(self) -> None:
        async with self._lock:
            self._closed = True
            self._pending_scale_ups = 0
            streams = list(self.streams)
            self.streams.clear()
            bg_tasks = list(self._background_tasks)
            for task in bg_tasks:
                task.cancel()
        if bg_tasks:
            await asyncio.gather(*bg_tasks, return_exceptions=True)
        for s in streams:
            await s.close()
