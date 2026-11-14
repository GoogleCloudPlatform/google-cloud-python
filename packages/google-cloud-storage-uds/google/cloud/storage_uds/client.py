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

"""Thin Python sync and async clients communicating with the Rust GCS UDS server."""

from __future__ import annotations

from dataclasses import dataclass
import mmap
import os
from pathlib import Path
from typing import Any, Sequence
import uuid

import grpc
import grpc.aio

from google.cloud.storage_uds import storage_accelerator_pb2 as pb2
from google.cloud.storage_uds.server_manager import (
    AcceleratorServerManager,
    ProcessMetrics,
)
from google.cloud.storage_uds.storage_accelerator_pb2_grpc import (
    StorageAcceleratorStub,
)

MAX_MESSAGE_BYTES = 512 * 1024 * 1024  # 512 MiB
MAX_HTTP2_FRAME_BYTES = 16 * 1024 * 1024 - 1  # 16 MiB - 1 (RFC 9113 max)
DEFAULT_SHM_INITIAL_BYTES = 64 * 1024 * 1024  # 64 MiB initial shared mmap arena

DEFAULT_CHANNEL_OPTIONS: tuple[tuple[str, Any], ...] = (
    ("grpc.default_authority", "localhost"),
    ("grpc.max_send_message_length", MAX_MESSAGE_BYTES),
    ("grpc.max_receive_message_length", MAX_MESSAGE_BYTES),
    ("grpc.http2.max_frame_size", MAX_HTTP2_FRAME_BYTES),
    ("grpc.http2.lookahead_bytes", 64 * 1024 * 1024),
)


class SharedMemoryArena:
    """Reusable POSIX `/dev/shm` `mmap` arena shared between Python and Rust."""

    def __init__(self, shm_dir: Path | None = None) -> None:
        base_dir = (
            shm_dir
            if shm_dir is not None
            else (
                Path("/dev/shm")
                if Path("/dev/shm").is_dir()
                else Path("/tmp")
            )
        )
        self._path = (
            base_dir / f"gcs_uds_shm_{os.getpid()}_{uuid.uuid4().hex[:8]}.bin"
        )
        self._fd: int | None = None
        self._mmap: mmap.mmap | None = None
        self._capacity: int = 0

    @property
    def path(self) -> str:
        """Filesystem path to the shared-memory backing file."""
        return str(self._path)

    def ensure_capacity(self, required_bytes: int) -> mmap.mmap:
        """Ensure the shared `mmap` region is at least `required_bytes` long."""
        target_cap = max(required_bytes, 4096)
        if self._mmap is not None and self._capacity >= target_cap:
            return self._mmap

        new_cap = max(target_cap, DEFAULT_SHM_INITIAL_BYTES)
        if self._mmap is not None:
            self._mmap.close()
            self._mmap = None

        if self._fd is None:
            self._fd = os.open(
                str(self._path),
                os.O_CREAT | os.O_RDWR,
                0o600,
            )
        os.ftruncate(self._fd, new_cap)
        self._mmap = mmap.mmap(
            self._fd,
            new_cap,
            mmap.MAP_SHARED,
            mmap.PROT_READ | mmap.PROT_WRITE,
        )
        self._capacity = new_cap
        return self._mmap

    def slice_ranges(
        self,
        requested_ranges: Sequence[tuple[int, int]],
        actual_lengths: Sequence[int],
    ) -> list[memoryview]:
        """Return zero-copy `memoryview` slices into the shared `mmap` region."""
        assert self._mmap is not None
        base_view = memoryview(self._mmap)
        out: list[memoryview] = []
        cursor = 0
        for (_, req_len), actual_len in zip(requested_ranges, actual_lengths):
            slot_cap = req_len if req_len > 0 else 1024
            out.append(base_view[cursor : cursor + actual_len])
            cursor += slot_cap
        return out

    def write_payload(self, data: bytes | memoryview) -> int:
        """Copy or stage `data` into the shared `mmap` region for zero-copy upload."""
        nbytes = len(data)
        mm = self.ensure_capacity(nbytes)
        memoryview(mm)[:nbytes] = data
        return nbytes

    def close(self) -> None:
        """Unmap and remove the `/dev/shm` backing file."""
        if self._mmap is not None:
            try:
                self._mmap.close()
            except BufferError:
                # A caller still holds an exported memoryview slice; unlink the
                # file now and let the OS reclaim pages when views drop.
                pass
            self._mmap = None
        if self._fd is not None:
            try:
                os.close(self._fd)
            except OSError:
                pass
            self._fd = None
        try:
            if self._path.exists():
                self._path.unlink()
        except OSError:
            pass
        self._capacity = 0


@dataclass(frozen=True)
class PingInfo:
    """Server status returned by the `Ping` RPC."""

    pid: int
    worker_threads: int
    version: str


@dataclass(frozen=True)
class ObjectMetadata:
    """GCS object metadata returned by `WriteObject` and `ListObjects`."""

    name: str
    bucket: str
    generation: int
    metageneration: int
    size: int
    storage_class: str
    etag: str
    crc32c: int | None = None


@dataclass(frozen=True)
class ListObjectsResult:
    """Paginated object list result returned by `ListObjects`."""

    objects: list[ObjectMetadata]
    prefixes: list[str]


def _proto_to_metadata(msg: Any) -> ObjectMetadata:
    """Convert a protobuf `ObjectMetadata` message to a Python dataclass."""
    return ObjectMetadata(
        name=msg.name,
        bucket=msg.bucket,
        generation=msg.generation,
        metageneration=msg.metageneration,
        size=msg.size,
        storage_class=msg.storage_class,
        etag=msg.etag,
        crc32c=msg.crc32c if msg.has_crc32c else None,
    )


class AsyncUdsStorageClient:
    """Async thin Python client over `grpc.aio` connected to the Rust UDS sidecar."""

    def __init__(
        self,
        server_manager: AcceleratorServerManager | None = None,
        *,
        uds_path: str | Path | None = None,
        worker_threads: int = 4,
        shutdown_server_on_close: bool = True,
        endpoint: str = "",
    ) -> None:
        """Initialize the async UDS client and ensure the Rust sidecar is running.

        Args:
            server_manager: Optional pre-configured `AcceleratorServerManager`.
            uds_path: Optional UDS socket path when creating a default manager.
            worker_threads: Tokio worker threads for the sidecar server.
            shutdown_server_on_close: Whether closing this client stops the
                sidecar subprocess.
            endpoint: Optional custom GCS endpoint override.
        """
        """Initialize the async UDS client and ensure the Rust sidecar is running."""
        self._manager = (
            server_manager
            if server_manager is not None
            else AcceleratorServerManager(
                uds_path=uds_path,
                worker_threads=worker_threads,
                shutdown_on_close=shutdown_server_on_close,
            )
        )
        self._manager.ensure_running()
        self._endpoint = endpoint
        self._channel: grpc.aio.Channel = grpc.aio.insecure_channel(
            self._manager.target_uri,
            options=DEFAULT_CHANNEL_OPTIONS,
        )
        self._stub = StorageAcceleratorStub(self._channel)
        self._shm = SharedMemoryArena()

    @property
    def server_manager(self) -> AcceleratorServerManager:
        """Underlying `AcceleratorServerManager` managing the Rust sidecar."""
        return self._manager

    @property
    def server_pid(self) -> int | None:
        """PID of the Rust `gcs-accelerator-server` sidecar process."""
        return self._manager.pid

    def get_server_metrics(self) -> ProcessMetrics | None:
        """Return cumulative CPU seconds and RSS MiB of the Rust sidecar."""
        return self._manager.get_server_metrics()

    async def ping(self) -> PingInfo:
        """Send a health-check `Ping` RPC over UDS to the Rust server."""
        resp = await self._stub.Ping(pb2.PingRequest())
        return PingInfo(
            pid=resp.pid,
            worker_threads=resp.worker_threads,
            version=resp.version,
        )

    async def read_ranges_zerocopy(
        self,
        bucket_name: str,
        object_name: str,
        ranges: Sequence[tuple[int, int]],
        *,
        endpoint: str | None = None,
        simulated: bool = False,
    ) -> list[memoryview]:
        """Read multiple `(offset, length)` ranges into shared `/dev/shm` `mmap` memory.

        The Rust sidecar writes downloaded GCS bytes directly into the shared
        `mmap` arena, and only the byte counts traverse the UDS gRPC socket.

        Returns:
            List of zero-copy `memoryview` slices backed by the shared `mmap`.
        """
        total_req = sum(length if length > 0 else 1024 for _, length in ranges)
        self._shm.ensure_capacity(total_req)
        req = pb2.ReadRangesRequest(
            bucket=bucket_name,
            object=object_name,
            ranges=[
                pb2.ByteRange(offset=offset, length=length)
                for offset, length in ranges
            ],
            endpoint=self._endpoint if endpoint is None else endpoint,
            simulated=simulated,
            shm_path=self._shm.path,
        )
        resp = await self._stub.ReadRanges(req)
        return self._shm.slice_ranges(ranges, resp.actual_lengths)

    async def read_ranges(
        self,
        bucket_name: str,
        object_name: str,
        ranges: Sequence[tuple[int, int]],
        *,
        stream: bool | None = None,
        zero_copy: bool = False,
        endpoint: str | None = None,
        simulated: bool = False,
    ) -> list[bytes] | list[memoryview]:
        """Read multiple `(offset, length)` byte ranges concurrently via the Rust sidecar.

        Args:
            bucket_name: GCS bucket name.
            object_name: GCS object name.
            ranges: Sequence of `(offset, length)` pairs.
            stream: If True, use the server-streaming `ReadObjectStream` RPC;
                if False, use the unary `ReadRanges` RPC; if None (default),
                automatically stream when total requested bytes >= 4 MiB.
            zero_copy: If True, transfer payload bytes via `/dev/shm` `mmap`
                and return zero-copy `memoryview` slices instead of copying
                bytes over the UDS socket.
            endpoint: Optional custom endpoint override.
            simulated: If True, generate synthetic payload bytes inside the Rust
                server to measure pure UDS IPC overhead without network I/O.

        Returns:
            List of `bytes` buffers (or `memoryview` slices when `zero_copy=True`).
        """
        if zero_copy:
            return await self.read_ranges_zerocopy(
                bucket_name=bucket_name,
                object_name=object_name,
                ranges=ranges,
                endpoint=endpoint,
                simulated=simulated,
            )

        use_stream = (
            stream
            if stream is not None
            else (
                sum(length for _, length in ranges) >= 4 * 1024 * 1024
                or any(length == 0 for _, length in ranges)
            )
        )
        req = pb2.ReadRangesRequest(
            bucket=bucket_name,
            object=object_name,
            ranges=[
                pb2.ByteRange(offset=offset, length=length)
                for offset, length in ranges
            ],
            endpoint=self._endpoint if endpoint is None else endpoint,
            simulated=simulated,
        )
        if not use_stream:
            resp = await self._stub.ReadRanges(req)
            return list(resp.chunks)

        buckets: list[list[bytes]] = [[] for _ in range(max(len(ranges), 1))]
        async for chunk in self._stub.ReadObjectStream(req):
            buckets[chunk.range_index].append(chunk.data)
        return [
            parts[0] if len(parts) == 1 else b"".join(parts)
            for parts in buckets
        ]

    async def read_object(
        self,
        bucket_name: str,
        object_name: str,
        offset: int = 0,
        length: int = 0,
        *,
        zero_copy: bool = False,
        endpoint: str | None = None,
        simulated: bool = False,
    ) -> bytes | memoryview:
        """Read an entire object or a single byte range via the Rust sidecar."""
        chunks = await self.read_ranges(
            bucket_name=bucket_name,
            object_name=object_name,
            ranges=[(offset, length)],
            zero_copy=zero_copy,
            endpoint=endpoint,
            simulated=simulated,
        )
        return chunks[0] if chunks else b""

    async def write_object(
        self,
        bucket_name: str,
        object_name: str,
        data: bytes | memoryview,
        *,
        zero_copy: bool = False,
        endpoint: str | None = None,
        simulated: bool = False,
    ) -> ObjectMetadata:
        """Upload an object via Rust `Storage::write_object` over UDS."""
        if zero_copy and len(data) > 0:
            nbytes = self._shm.write_payload(data)
            req = pb2.WriteObjectRequest(
                bucket=bucket_name,
                object=object_name,
                endpoint=self._endpoint if endpoint is None else endpoint,
                simulated=simulated,
                shm_path=self._shm.path,
                shm_length=nbytes,
            )
        else:
            req = pb2.WriteObjectRequest(
                bucket=bucket_name,
                object=object_name,
                data=bytes(data),
                endpoint=self._endpoint if endpoint is None else endpoint,
                simulated=simulated,
            )
        resp = await self._stub.WriteObject(req)
        return _proto_to_metadata(resp)

    async def list_objects(
        self,
        bucket_name: str,
        *,
        prefix: str = "",
        delimiter: str = "",
        versions: bool = False,
        include_folders_as_prefixes: bool = False,
        max_results: int = 0,
        endpoint: str | None = None,
        simulated_count: int = 0,
    ) -> ListObjectsResult:
        """List objects in a bucket via Rust `StorageControl::list_objects` over UDS."""
        req = pb2.ListObjectsRequest(
            bucket=bucket_name,
            prefix=prefix,
            delimiter=delimiter,
            versions=versions,
            include_folders_as_prefixes=include_folders_as_prefixes,
            max_results=max_results,
            endpoint=self._endpoint if endpoint is None else endpoint,
            simulated_count=simulated_count,
        )
        resp = await self._stub.ListObjects(req)
        return ListObjectsResult(
            objects=[_proto_to_metadata(o) for o in resp.objects],
            prefixes=list(resp.prefixes),
        )

    async def close(self) -> None:
        """Close the async gRPC UDS channel, shared memory, and sidecar."""
        self._shm.close()
        await self._channel.close()
        self._manager.close()

    async def __aenter__(self) -> AsyncUdsStorageClient:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        await self.close()


class UdsStorageClient:
    """Synchronous thin Python client over `grpc` connected to the Rust UDS sidecar."""

    def __init__(
        self,
        server_manager: AcceleratorServerManager | None = None,
        *,
        uds_path: str | Path | None = None,
        worker_threads: int = 4,
        shutdown_server_on_close: bool = True,
        endpoint: str = "",
    ) -> None:
        """Initialize the synchronous UDS client and ensure the Rust sidecar is running."""
        self._manager = (
            server_manager
            if server_manager is not None
            else AcceleratorServerManager(
                uds_path=uds_path,
                worker_threads=worker_threads,
                shutdown_on_close=shutdown_server_on_close,
            )
        )
        self._manager.ensure_running()
        self._endpoint = endpoint
        self._channel: grpc.Channel = grpc.insecure_channel(
            self._manager.target_uri,
            options=DEFAULT_CHANNEL_OPTIONS,
        )
        self._stub = StorageAcceleratorStub(self._channel)
        self._shm = SharedMemoryArena()

    @property
    def server_pid(self) -> int | None:
        """PID of the Rust `gcs-accelerator-server` sidecar process."""
        return self._manager.pid

    def ping(self) -> PingInfo:
        """Send a synchronous health-check `Ping` RPC over UDS."""
        resp = self._stub.Ping(pb2.PingRequest())
        return PingInfo(
            pid=resp.pid,
            worker_threads=resp.worker_threads,
            version=resp.version,
        )

    def read_ranges(
        self,
        bucket_name: str,
        object_name: str,
        ranges: Sequence[tuple[int, int]],
        *,
        zero_copy: bool = False,
        endpoint: str | None = None,
        simulated: bool = False,
    ) -> list[bytes] | list[memoryview]:
        """Synchronously read one or more byte ranges via the Rust UDS sidecar."""
        if zero_copy:
            total_req = sum(
                length if length > 0 else 1024 for _, length in ranges
            )
            self._shm.ensure_capacity(total_req)
            req = pb2.ReadRangesRequest(
                bucket=bucket_name,
                object=object_name,
                ranges=[
                    pb2.ByteRange(offset=offset, length=length)
                    for offset, length in ranges
                ],
                endpoint=self._endpoint if endpoint is None else endpoint,
                simulated=simulated,
                shm_path=self._shm.path,
            )
            resp = self._stub.ReadRanges(req)
            return self._shm.slice_ranges(ranges, resp.actual_lengths)

        req = pb2.ReadRangesRequest(
            bucket=bucket_name,
            object=object_name,
            ranges=[
                pb2.ByteRange(offset=offset, length=length)
                for offset, length in ranges
            ],
            endpoint=self._endpoint if endpoint is None else endpoint,
            simulated=simulated,
        )
        resp = self._stub.ReadRanges(req)
        return list(resp.chunks)

    def write_object(
        self,
        bucket_name: str,
        object_name: str,
        data: bytes | memoryview,
        *,
        zero_copy: bool = False,
        endpoint: str | None = None,
        simulated: bool = False,
    ) -> ObjectMetadata:
        """Synchronously upload an object via the Rust UDS sidecar."""
        if zero_copy and len(data) > 0:
            nbytes = self._shm.write_payload(data)
            req = pb2.WriteObjectRequest(
                bucket=bucket_name,
                object=object_name,
                endpoint=self._endpoint if endpoint is None else endpoint,
                simulated=simulated,
                shm_path=self._shm.path,
                shm_length=nbytes,
            )
        else:
            req = pb2.WriteObjectRequest(
                bucket=bucket_name,
                object=object_name,
                data=bytes(data),
                endpoint=self._endpoint if endpoint is None else endpoint,
                simulated=simulated,
            )
        resp = self._stub.WriteObject(req)
        return _proto_to_metadata(resp)

    def list_objects(
        self,
        bucket_name: str,
        *,
        prefix: str = "",
        delimiter: str = "",
        versions: bool = False,
        include_folders_as_prefixes: bool = False,
        max_results: int = 0,
        endpoint: str | None = None,
        simulated_count: int = 0,
    ) -> ListObjectsResult:
        """Synchronously list objects in a bucket via the Rust UDS sidecar."""
        req = pb2.ListObjectsRequest(
            bucket=bucket_name,
            prefix=prefix,
            delimiter=delimiter,
            versions=versions,
            include_folders_as_prefixes=include_folders_as_prefixes,
            max_results=max_results,
            endpoint=self._endpoint if endpoint is None else endpoint,
            simulated_count=simulated_count,
        )
        resp = self._stub.ListObjects(req)
        return ListObjectsResult(
            objects=[_proto_to_metadata(o) for o in resp.objects],
            prefixes=list(resp.prefixes),
        )

    def close(self) -> None:
        """Close the sync gRPC UDS channel, shared memory, and sidecar."""
        self._shm.close()
        self._channel.close()
        self._manager.close()

    def __enter__(self) -> UdsStorageClient:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()
