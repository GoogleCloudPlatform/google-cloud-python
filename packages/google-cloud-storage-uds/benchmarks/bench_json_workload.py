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

"""Benchmark comparing Pure Python JSON vs Rust UDS gRPC (Socket & Zero-Copy SHM) vs PyO3 FFI.

Workloads tested against regional bucket ``princer-flat``:
1. ReadObject / Range Reads (HTTP GET with Range header):
   - 100 x 64 KiB concurrent ranges (High-IOPS metadata/index lookup)
   - 64 x 1 MiB concurrent ranges (Medium tensor/parquet column chunks)
   - 16 x 16 MiB concurrent ranges (256 MiB total download)
   - 1 x 100 MiB single-stream download
2. WriteObject (HTTP Upload):
   - 1 x 256 KiB object upload
   - 1 x 16 MiB object upload
   - 1 x 64 MiB object upload
3. ListObjects:
   - 1,000 objects listed from ``princer-flat``
"""

from __future__ import annotations

import asyncio
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import statistics
import time
from typing import Any, Literal

from google.cloud import storage
from requests.adapters import HTTPAdapter

from google.cloud.storage_uds import (
    AsyncUdsStorageClient,
    read_process_metrics,
)

BackendMode = Literal["python_json", "rust_uds_grpc", "rust_uds_zerocopy"]

# Reference PyO3 FFI numbers captured on the same machine & bucket (`princer-flat`)
# from branch `python-sdk-rust`.
PYO3_REFERENCE: dict[tuple[str, str], dict[str, Any]] = {
    ("ReadObject", "100 x 64 KiB"): {
        "median_latency_ms": 45.68,
        "p99_latency_ms": 50.74,
        "throughput_mib_s": 136.8,
        "cpu_s_per_gib": 4.724,
    },
    ("ReadObject", "64 x 1024 KiB"): {
        "median_latency_ms": 56.68,
        "p99_latency_ms": 78.87,
        "throughput_mib_s": 1129.1,
        "cpu_s_per_gib": 1.428,
    },
    ("ReadObject", "16 x 16384 KiB"): {
        "median_latency_ms": 164.22,
        "p99_latency_ms": 175.55,
        "throughput_mib_s": 1558.9,
        "cpu_s_per_gib": 1.306,
    },
    ("ReadObject", "1 x 102400 KiB"): {
        "median_latency_ms": 337.88,
        "p99_latency_ms": 386.70,
        "throughput_mib_s": 296.0,
        "cpu_s_per_gib": 1.656,
    },
    ("WriteObject (HTTP Upload)", "1 x 256 KiB"): {
        "median_latency_ms": 72.62,
        "p99_latency_ms": 74.60,
        "throughput_mib_s": 3.4,
        "cpu_s_per_gib": 2.231,
    },
    ("WriteObject (HTTP Upload)", "1 x 16384 KiB"): {
        "median_latency_ms": 207.29,
        "p99_latency_ms": 239.69,
        "throughput_mib_s": 77.2,
        "cpu_s_per_gib": 0.427,
    },
    ("WriteObject (HTTP Upload)", "1 x 65536 KiB"): {
        "median_latency_ms": 521.70,
        "p99_latency_ms": 563.29,
        "throughput_mib_s": 122.7,
        "cpu_s_per_gib": 0.812,
    },
    ("ListObjects (Paginator)", "1,000 objects"): {
        "median_latency_ms": 56.95,
        "p99_latency_ms": 58.56,
        "objects_per_sec": 17558.0,
        "cpu_ms_per_call": 2.52,
    },
}


def _create_python_json_client(pool_maxsize: int = 128) -> storage.Client:
    """Create a Python ``google.cloud.storage.Client`` with a sized urllib3 pool."""
    client = storage.Client()
    adapter = HTTPAdapter(
        pool_connections=pool_maxsize,
        pool_maxsize=pool_maxsize,
    )
    client._http.mount("https://", adapter)
    client._http.mount("http://", adapter)
    return client


def _server_cpu_seconds(uds_client: AsyncUdsStorageClient) -> float:
    metrics = uds_client.get_server_metrics()
    return metrics.cpu_seconds if metrics is not None else 0.0


async def bench_json_read(
    backend: BackendMode,
    py_client: storage.Client,
    uds_client: AsyncUdsStorageClient,
    bucket_name: str,
    object_name: str,
    obj_size: int,
    num_ranges: int,
    range_size: int,
    iterations: int = 5,
) -> dict[str, Any]:
    """Benchmark HTTP/JSON range reads across Pure Python, UDS Socket, and UDS Zero-Copy SHM."""
    max_offset = max(0, obj_size - range_size)
    step = max(1, max_offset // max(1, num_ranges))
    ranges_spec = [
        ((i * step) % max(1, max_offset), range_size) for i in range(num_ranges)
    ]

    bucket = py_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    max_workers = max(1, num_ranges)

    def _py_download_one(off_len: tuple[int, int]) -> bytes:
        off, length = off_len
        return blob.download_as_bytes(
            start=off,
            end=off + length - 1,
            raw_download=True,
            checksum=None,
        )

    pool = (
        ThreadPoolExecutor(max_workers=max_workers)
        if backend == "python_json"
        else None
    )
    try:

        async def _run_once() -> None:
            if backend == "python_json":
                assert pool is not None
                loop = asyncio.get_running_loop()
                await asyncio.gather(
                    *(
                        loop.run_in_executor(pool, _py_download_one, spec)
                        for spec in ranges_spec
                    )
                )
            elif backend == "rust_uds_zerocopy":
                views = await uds_client.read_ranges_zerocopy(
                    bucket_name,
                    object_name,
                    ranges_spec,
                )
                assert len(views) == num_ranges
            else:
                chunks = await uds_client.read_ranges(
                    bucket_name,
                    object_name,
                    ranges_spec,
                    zero_copy=False,
                )
                assert len(chunks) == num_ranges

        # Warmup
        await _run_once()

        wall_times: list[float] = []
        py_cpu_times: list[float] = []
        srv_cpu_times: list[float] = []
        total_bytes_per_iter = num_ranges * range_size

        for _ in range(iterations):
            t0_wall = time.perf_counter()
            t0_py_cpu = time.process_time()
            t0_srv_cpu = _server_cpu_seconds(uds_client)

            await _run_once()

            wall_times.append(time.perf_counter() - t0_wall)
            py_cpu_times.append(time.process_time() - t0_py_cpu)
            srv_cpu_times.append(
                max(0.0, _server_cpu_seconds(uds_client) - t0_srv_cpu)
                if backend != "python_json"
                else 0.0
            )
    finally:
        if pool is not None:
            pool.shutdown(wait=True)

    median_wall = statistics.median(wall_times)
    p99_wall = sorted(wall_times)[int(len(wall_times) * 0.99) - 1]
    mean_py_cpu = statistics.mean(py_cpu_times)
    mean_srv_cpu = statistics.mean(srv_cpu_times)
    mean_total_cpu = mean_py_cpu + mean_srv_cpu
    gib_per_iter = total_bytes_per_iter / (1024**3)
    throughput_mib_s = (total_bytes_per_iter / (1024**2)) / median_wall

    return {
        "operation": "ReadObject",
        "backend": backend,
        "workload": f"{num_ranges} x {range_size // 1024} KiB",
        "median_latency_ms": round(median_wall * 1000.0, 2),
        "p99_latency_ms": round(p99_wall * 1000.0, 2),
        "throughput_mib_s": round(throughput_mib_s, 1),
        "cpu_s_per_gib": round(mean_total_cpu / gib_per_iter, 3),
        "python_cpu_s_per_gib": round(mean_py_cpu / gib_per_iter, 3),
        "server_cpu_s_per_gib": round(mean_srv_cpu / gib_per_iter, 3),
    }


async def bench_json_write(
    backend: BackendMode,
    py_client: storage.Client,
    uds_client: AsyncUdsStorageClient,
    bucket_name: str,
    payload_size: int,
    iterations: int = 5,
) -> dict[str, Any]:
    """Benchmark HTTP/JSON object writes across Pure Python, UDS Socket, and UDS Zero-Copy SHM."""
    payload = b"J" * payload_size
    bucket = py_client.bucket(bucket_name)

    wall_times: list[float] = []
    py_cpu_times: list[float] = []
    srv_cpu_times: list[float] = []

    for idx in range(iterations + 1):
        object_name = f"bench/tmp_uds_write_{backend}_{payload_size}_{idx}.bin"
        t0_wall = time.perf_counter()
        t0_py_cpu = time.process_time()
        t0_srv_cpu = _server_cpu_seconds(uds_client)

        if backend == "python_json":
            blob = bucket.blob(object_name)
            await asyncio.to_thread(
                blob.upload_from_string,
                payload,
                content_type="application/octet-stream",
            )
        elif backend == "rust_uds_zerocopy":
            await uds_client.write_object(
                bucket_name,
                object_name,
                payload,
                zero_copy=True,
            )
        else:
            await uds_client.write_object(
                bucket_name,
                object_name,
                payload,
                zero_copy=False,
            )

        dt_wall = time.perf_counter() - t0_wall
        dt_py_cpu = time.process_time() - t0_py_cpu
        dt_srv_cpu = (
            max(0.0, _server_cpu_seconds(uds_client) - t0_srv_cpu)
            if backend != "python_json"
            else 0.0
        )
        if idx > 0:
            wall_times.append(dt_wall)
            py_cpu_times.append(dt_py_cpu)
            srv_cpu_times.append(dt_srv_cpu)

    median_wall = statistics.median(wall_times)
    p99_wall = sorted(wall_times)[int(len(wall_times) * 0.99) - 1]
    mean_py_cpu = statistics.mean(py_cpu_times)
    mean_srv_cpu = statistics.mean(srv_cpu_times)
    mean_total_cpu = mean_py_cpu + mean_srv_cpu
    gib_per_iter = payload_size / (1024**3)
    throughput_mib_s = (payload_size / (1024**2)) / median_wall

    return {
        "operation": "WriteObject (HTTP Upload)",
        "backend": backend,
        "workload": f"1 x {payload_size // 1024} KiB",
        "median_latency_ms": round(median_wall * 1000.0, 2),
        "p99_latency_ms": round(p99_wall * 1000.0, 2),
        "throughput_mib_s": round(throughput_mib_s, 1),
        "cpu_s_per_gib": round(mean_total_cpu / gib_per_iter, 3),
        "python_cpu_s_per_gib": round(mean_py_cpu / gib_per_iter, 3),
        "server_cpu_s_per_gib": round(mean_srv_cpu / gib_per_iter, 3),
    }


async def bench_json_list(
    backend: BackendMode,
    py_client: storage.Client,
    uds_client: AsyncUdsStorageClient,
    bucket_name: str,
    prefix: str,
    object_count: int = 1000,
    iterations: int = 5,
) -> dict[str, Any]:
    """Benchmark ListObjects across Pure Python JSON and Rust gRPC-over-UDS."""

    def _py_list() -> int:
        blobs = list(
            py_client.list_blobs(
                bucket_name,
                prefix=prefix,
                max_results=object_count,
                page_size=min(1000, object_count),
            )
        )
        return len(blobs)

    async def _run_once() -> int:
        if backend == "python_json":
            return await asyncio.to_thread(_py_list)
        res = await uds_client.list_objects(
            bucket_name,
            prefix=prefix,
            max_results=object_count,
        )
        return len(res.objects)

    actual_count = await _run_once()
    wall_times: list[float] = []
    py_cpu_times: list[float] = []
    srv_cpu_times: list[float] = []

    for _ in range(iterations):
        t0_wall = time.perf_counter()
        t0_py_cpu = time.process_time()
        t0_srv_cpu = _server_cpu_seconds(uds_client)

        cnt = await _run_once()
        assert cnt == actual_count

        wall_times.append(time.perf_counter() - t0_wall)
        py_cpu_times.append(time.process_time() - t0_py_cpu)
        srv_cpu_times.append(
            max(0.0, _server_cpu_seconds(uds_client) - t0_srv_cpu)
            if backend != "python_json"
            else 0.0
        )

    median_wall = statistics.median(wall_times)
    p99_wall = sorted(wall_times)[int(len(wall_times) * 0.99) - 1]
    mean_py_cpu = statistics.mean(py_cpu_times)
    mean_srv_cpu = statistics.mean(srv_cpu_times)
    mean_total_cpu = mean_py_cpu + mean_srv_cpu
    objs_per_sec = actual_count / median_wall

    return {
        "operation": "ListObjects (Paginator)",
        "backend": backend,
        "workload": f"{actual_count:,} objects",
        "median_latency_ms": round(median_wall * 1000.0, 2),
        "p99_latency_ms": round(p99_wall * 1000.0, 2),
        "objects_per_sec": round(objs_per_sec, 0),
        "cpu_ms_per_call": round(mean_total_cpu * 1000.0, 2),
        "python_cpu_ms_per_call": round(mean_py_cpu * 1000.0, 2),
        "server_cpu_ms_per_call": round(mean_srv_cpu * 1000.0, 2),
    }


async def run_json_benchmarks() -> dict[str, Any]:
    bucket_name = os.environ.get("GCS_JSON_BUCKET", "princer-flat")
    py_client = _create_python_json_client(pool_maxsize=128)

    results: list[dict[str, Any]] = []

    async with AsyncUdsStorageClient(worker_threads=4) as uds_client:
        ping_info = await uds_client.ping()
        obj_name = "bench/bench_20GB.bin"
        obj_sz = 20 * 1024 * 1024 * 1024

        # 1. ReadObject Benchmarks
        for num_ranges, range_size in [
            (100, 64 * 1024),
            (64, 1024 * 1024),
            (16, 16 * 1024 * 1024),
            (1, 100 * 1024 * 1024),
        ]:
            workload_label = f"{num_ranges} x {range_size // 1024} KiB"
            for backend in (
                "python_json",
                "rust_uds_grpc",
                "rust_uds_zerocopy",
            ):
                res = await bench_json_read(
                    backend=backend,  # type: ignore[arg-type]
                    py_client=py_client,
                    uds_client=uds_client,
                    bucket_name=bucket_name,
                    object_name=obj_name,
                    obj_size=obj_sz,
                    num_ranges=num_ranges,
                    range_size=range_size,
                )
                results.append(res)
            if ("ReadObject", workload_label) in PYO3_REFERENCE:
                ref = dict(PYO3_REFERENCE[("ReadObject", workload_label)])
                results.append(
                    {
                        "operation": "ReadObject",
                        "backend": "rust_pyo3_ffi",
                        "workload": workload_label,
                        **ref,
                    }
                )

        # 2. WriteObject Benchmarks
        for payload_size in [
            256 * 1024,
            16 * 1024 * 1024,
            64 * 1024 * 1024,
        ]:
            workload_label = f"1 x {payload_size // 1024} KiB"
            for backend in (
                "python_json",
                "rust_uds_grpc",
                "rust_uds_zerocopy",
            ):
                res = await bench_json_write(
                    backend=backend,  # type: ignore[arg-type]
                    py_client=py_client,
                    uds_client=uds_client,
                    bucket_name=bucket_name,
                    payload_size=payload_size,
                )
                results.append(res)
            if ("WriteObject (HTTP Upload)", workload_label) in PYO3_REFERENCE:
                ref = dict(
                    PYO3_REFERENCE[("WriteObject (HTTP Upload)", workload_label)]
                )
                results.append(
                    {
                        "operation": "WriteObject (HTTP Upload)",
                        "backend": "rust_pyo3_ffi",
                        "workload": workload_label,
                        **ref,
                    }
                )

        # 3. ListObjects Benchmarks
        for obj_count in (1000,):
            workload_label = f"{obj_count:,} objects"
            for backend in ("python_json", "rust_uds_grpc"):
                res = await bench_json_list(
                    backend=backend,  # type: ignore[arg-type]
                    py_client=py_client,
                    uds_client=uds_client,
                    bucket_name=bucket_name,
                    prefix="benchmark-static/list_flat_1procs_1threads_131072files_0depth_1folders_ls_regional/folder_0/",
                    object_count=obj_count,
                )
                results.append(res)
            if ("ListObjects (Paginator)", workload_label) in PYO3_REFERENCE:
                ref = dict(
                    PYO3_REFERENCE[("ListObjects (Paginator)", workload_label)]
                )
                results.append(
                    {
                        "operation": "ListObjects (Paginator)",
                        "backend": "rust_pyo3_ffi",
                        "workload": workload_label,
                        **ref,
                    }
                )

        py_mem = read_process_metrics(os.getpid())
        srv_mem = uds_client.get_server_metrics()

    summary: dict[str, Any] = {
        "mode": f"live_json_bucket ({bucket_name})",
        "server_info": {
            "pid": ping_info.pid,
            "worker_threads": ping_info.worker_threads,
            "version": ping_info.version,
            "python_rss_mib": round(py_mem.rss_mib, 1),
            "rust_server_rss_mib": (
                round(srv_mem.rss_mib, 1) if srv_mem is not None else 0.0
            ),
        },
        "results": results,
    }
    out_path = Path(__file__).parent / "uds_json_benchmark_results.json"
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def main() -> int:
    summary = asyncio.run(run_json_benchmarks())
    srv = summary["server_info"]
    print(
        f"\n=== GCS HTTP/JSON 4-Way Benchmark: Pure Python vs UDS gRPC vs UDS ZeroCopy SHM vs PyO3 FFI ({summary['mode']}) ==="
    )
    print(
        f"Server PID={srv['pid']} (workers={srv['worker_threads']}) | "
        f"RSS Memory: Python={srv['python_rss_mib']} MiB, Rust UDS Server={srv['rust_server_rss_mib']} MiB"
    )
    print(
        f"{'Operation':<26} | {'Workload':<15} | {'Backend':<17} | {'Median (ms)':>11} | {'p99 (ms)':>9} | {'Throughput / Rate':>18} | {'Total CPU (Py+Srv)':>28}"
    )
    print("-" * 139)
    for row in summary["results"]:
        if "throughput_mib_s" in row:
            rate_str = f"{row['throughput_mib_s']:,.1f} MiB/s"
            if "python_cpu_s_per_gib" in row and row["backend"].startswith(
                "rust_uds"
            ):
                cpu_str = (
                    f"{row['cpu_s_per_gib']:.2f} s/GiB "
                    f"({row['python_cpu_s_per_gib']:.2f}+{row['server_cpu_s_per_gib']:.2f})"
                )
            else:
                cpu_str = f"{row['cpu_s_per_gib']:.3f} CPU-s/GiB"
        else:
            rate_str = f"{row['objects_per_sec']:,.0f} obj/s"
            if "python_cpu_ms_per_call" in row and row["backend"].startswith(
                "rust_uds"
            ):
                cpu_str = (
                    f"{row['cpu_ms_per_call']:.2f} ms "
                    f"({row['python_cpu_ms_per_call']:.2f}+{row['server_cpu_ms_per_call']:.2f})"
                )
            else:
                cpu_str = f"{row['cpu_ms_per_call']:.2f} ms/call"
        print(
            f"{row['operation']:<26} | {row['workload']:<15} | {row['backend']:<17} | "
            f"{row['median_latency_ms']:>11.2f} | {row['p99_latency_ms']:>9.2f} | "
            f"{rate_str:>18} | {cpu_str:>28}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

