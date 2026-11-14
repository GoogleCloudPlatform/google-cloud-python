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

"""End-to-end unit tests for the Python-to-Rust gRPC-over-UDS client and server."""

from __future__ import annotations

from pathlib import Path
from typing import AsyncIterator

import grpc
import pytest
import pytest_asyncio

from google.cloud.storage_uds import (
    AcceleratorServerManager,
    AsyncUdsStorageClient,
    UdsStorageClient,
)


@pytest_asyncio.fixture
async def uds_client(tmp_path: Path) -> AsyncIterator[AsyncUdsStorageClient]:
    """Provide an `AsyncUdsStorageClient` backed by an isolated UDS sidecar."""
    sock_path = tmp_path / "test_accelerator.sock"
    pid_path = tmp_path / "test_accelerator.pid"
    manager = AcceleratorServerManager(
        uds_path=sock_path,
        pid_file=pid_path,
        worker_threads=2,
        shutdown_on_close=True,
    )
    async with AsyncUdsStorageClient(server_manager=manager) as client:
        yield client


@pytest.mark.asyncio
async def test_ping_returns_server_pid_and_worker_threads(
    uds_client: AsyncUdsStorageClient,
) -> None:
    # Arrange
    expected_pid = uds_client.server_pid

    # Act
    info = await uds_client.ping()

    # Assert
    assert info.pid == expected_pid
    assert info.worker_threads == 2
    assert info.version == "0.1.0"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("ranges", "stream_mode"),
    [
        pytest.param([(0, 4096)], False, id="single-range-unary"),
        pytest.param([(0, 4096)], True, id="single-range-stream"),
        pytest.param(
            [(i * 65536, 65536) for i in range(16)],
            False,
            id="multi-range-16x64kib-unary",
        ),
        pytest.param(
            [(i * 65536, 65536) for i in range(16)],
            True,
            id="multi-range-16x64kib-stream",
        ),
        pytest.param(
            [(0, 8 * 1024 * 1024)],
            False,
            id="large-8mib-exceeding-default-grpc-limit",
        ),
    ],
)
async def test_read_ranges_returns_expected_byte_slices(
    uds_client: AsyncUdsStorageClient,
    ranges: list[tuple[int, int]],
    stream_mode: bool,
) -> None:
    # Arrange
    bucket = "test-bucket"
    obj_name = "bench/object.bin"

    # Act
    chunks = await uds_client.read_ranges(
        bucket,
        obj_name,
        ranges,
        stream=stream_mode,
        simulated=True,
    )

    # Assert
    assert [len(c) for c in chunks] == [length for _, length in ranges]
    first_offset, _ = ranges[0]
    assert chunks[0][0] == (first_offset & 0xFF)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "ranges",
    [
        pytest.param([(256, 4096)], id="single-range-zerocopy-shm"),
        pytest.param(
            [(i * 65536, 65536) for i in range(16)],
            id="multi-range-16x64kib-zerocopy-shm",
        ),
        pytest.param(
            [(0, 16 * 1024 * 1024)],
            id="large-16mib-zerocopy-shm",
        ),
    ],
)
async def test_read_ranges_zerocopy_returns_memoryviews_from_shared_mmap(
    uds_client: AsyncUdsStorageClient,
    ranges: list[tuple[int, int]],
) -> None:
    # Arrange
    bucket = "test-bucket"
    obj_name = "bench/object.bin"

    # Act
    views = await uds_client.read_ranges_zerocopy(
        bucket,
        obj_name,
        ranges,
        simulated=True,
    )

    # Assert
    assert all(isinstance(v, memoryview) for v in views)
    assert [len(v) for v in views] == [length for _, length in ranges]
    first_offset, _ = ranges[0]
    assert views[0][0] == (first_offset & 0xFF)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "use_zero_copy",
    [
        pytest.param(False, id="socket-copy"),
        pytest.param(True, id="shm-zerocopy"),
    ],
)
async def test_write_object_returns_object_metadata(
    uds_client: AsyncUdsStorageClient,
    use_zero_copy: bool,
) -> None:
    # Arrange
    payload = b"W" * (6 * 1024 * 1024)  # 6 MiB (> 4 MiB default gRPC limit)

    # Act
    meta = await uds_client.write_object(
        "test-bucket",
        "bench/upload.bin",
        payload,
        zero_copy=use_zero_copy,
        simulated=True,
    )

    # Assert
    assert meta.name == "bench/upload.bin"
    assert meta.bucket == "projects/_/buckets/test-bucket"
    assert meta.size == len(payload)


@pytest.mark.asyncio
async def test_list_objects_returns_paginated_metadata(
    uds_client: AsyncUdsStorageClient,
) -> None:
    # Arrange
    expected_count = 250

    # Act
    result = await uds_client.list_objects(
        "test-bucket",
        prefix="folder_0/",
        simulated_count=expected_count,
    )

    # Assert
    assert len(result.objects) == expected_count
    assert result.objects[0].name == "folder_0/object_000000.bin"
    assert result.objects[-1].name == "folder_0/object_000249.bin"


@pytest.mark.asyncio
async def test_empty_bucket_raises_invalid_argument_rpc_error(
    uds_client: AsyncUdsStorageClient,
) -> None:
    # Arrange / Act / Assert
    with pytest.raises(grpc.aio.AioRpcError) as exc_info:
        await uds_client.read_object("", "object.bin", simulated=True)

    assert exc_info.value.code() == grpc.StatusCode.INVALID_ARGUMENT


def test_server_manager_reuses_persistent_sidecar_across_clients(
    tmp_path: Path,
) -> None:
    # Arrange
    sock_path = tmp_path / "shared_accelerator.sock"
    pid_path = tmp_path / "shared_accelerator.pid"
    mgr1 = AcceleratorServerManager(
        uds_path=sock_path,
        pid_file=pid_path,
        shutdown_on_close=False,
    )
    mgr2 = AcceleratorServerManager(
        uds_path=sock_path,
        pid_file=pid_path,
        shutdown_on_close=False,
    )

    try:
        # Act
        with UdsStorageClient(server_manager=mgr1) as client1:
            info1 = client1.ping()
        with UdsStorageClient(server_manager=mgr2) as client2:
            info2 = client2.ping()

        # Assert
        assert mgr1.reused_existing is False
        assert mgr2.reused_existing is True
        assert info1.pid == info2.pid
    finally:
        mgr1.close(force=True)
        assert not sock_path.exists()
        assert not pid_path.exists()

