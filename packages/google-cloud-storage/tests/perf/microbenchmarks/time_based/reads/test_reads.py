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
"""Microbenchmarks for time-based Google Cloud Storage read operations."""

import asyncio
import logging
import multiprocessing
import os
import random
import time
from typing import List, NamedTuple, Optional

import pytest

import tests.perf.microbenchmarks.time_based.reads.config as config
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from tests.perf.microbenchmarks._utils import (
    get_irq_affinity,
    publish_benchmark_extra_info,
)
from tests.perf.microbenchmarks.conftest import (
    publish_resource_metrics,
)

all_params = config._get_params()


class DownloadResult(NamedTuple):
    total_bytes: int
    measured_start_time: float
    measured_end_time: float


async def create_client():
    """Initializes async client and gets the current event loop."""
    return AsyncGrpcClient()


def _aggregate_download_results(results: List[DownloadResult]) -> DownloadResult:
    if not results:
        raise ValueError("At least one download result is required.")

    total_bytes = sum(result.total_bytes for result in results)
    measured_start_time = min(result.measured_start_time for result in results)
    measured_end_time = max(result.measured_end_time for result in results)
    if measured_end_time <= measured_start_time:
        raise ValueError("Measured elapsed time must be positive.")

    return DownloadResult(
        total_bytes=total_bytes,
        measured_start_time=measured_start_time,
        measured_end_time=measured_end_time,
    )


def _calculate_average_throughput_mib_s(
    download_bytes_list: List[int], download_elapsed_times: List[float]
) -> float:
    total_bytes_downloaded = sum(download_bytes_list)
    total_elapsed_time = sum(download_elapsed_times)
    if total_elapsed_time <= 0:
        raise ValueError("Total measured elapsed time must be positive.")

    return (total_bytes_downloaded / total_elapsed_time) / (1024 * 1024)


def _build_download_result(
    total_bytes_downloaded: int,
    measured_start_time: Optional[float],
    measured_end_time: Optional[float],
) -> DownloadResult:
    if measured_start_time is None or measured_end_time is None:
        raise ValueError("No downloads completed during the measured interval.")

    return DownloadResult(
        total_bytes=total_bytes_downloaded,
        measured_start_time=measured_start_time,
        measured_end_time=measured_end_time,
    )


# --- Global Variables for Worker Process ---
worker_loop = None
worker_client = None
worker_json_client = None


# TODO: b/479135274 close clients properly.
def _worker_init(bucket_type):
    """Initializes a persistent event loop and client for each worker process."""
    cpu_affinity = get_irq_affinity()
    if cpu_affinity:
        os.sched_setaffinity(
            0, {i for i in range(0, os.cpu_count()) if i not in cpu_affinity}
        )

    global worker_loop, worker_client, worker_json_client
    if bucket_type == "rapid":
        worker_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(worker_loop)
        worker_client = worker_loop.run_until_complete(create_client())
    else:  # regional
        from google.cloud import storage

        worker_json_client = storage.Client()


def _download_time_based_json(client, filename, params):
    """Performs time-based downloads using the JSON API."""
    total_bytes_downloaded = 0
    bucket = client.bucket(params.bucket_name)
    blob = bucket.blob(filename)

    offset = 0
    is_warming_up = True
    start_time = time.perf_counter()
    warmup_end_time = start_time + params.warmup_duration
    test_end_time = warmup_end_time + params.duration
    measured_start_time = None
    measured_end_time = None

    while time.perf_counter() < test_end_time:
        current_time = time.perf_counter()
        if is_warming_up and current_time >= warmup_end_time:
            is_warming_up = False
            total_bytes_downloaded = 0  # Reset counter after warmup
            measured_start_time = current_time

        bytes_in_iteration = 0
        # For JSON, we can't batch ranges like gRPC, so we download one by one
        for _ in range(params.num_ranges):
            if params.pattern == "rand":
                offset = random.randint(
                    0, params.file_size_bytes - params.chunk_size_bytes
                )

            data = blob.download_as_bytes(
                start=offset, end=offset + params.chunk_size_bytes - 1
            )
            bytes_in_iteration += len(data)

            if params.pattern == "seq":
                offset += params.chunk_size_bytes
                if offset + params.chunk_size_bytes > params.file_size_bytes:
                    offset = 0

        assert bytes_in_iteration == params.chunk_size_bytes * params.num_ranges

        if not is_warming_up:
            total_bytes_downloaded += bytes_in_iteration
            measured_end_time = time.perf_counter()

    return _build_download_result(
        total_bytes_downloaded, measured_start_time, measured_end_time
    )


# _DummyListBuffer is used instead of io.BytesIO to avoid GIL contention
# during profiling. io.BytesIO.write() holds the GIL while copying data,
# which introduces significant noise and bottlenecks in performance tests
# with high concurrency or large data transfers.
# This buffer simply collects chunks in a list and tracks the total size.
class _DummyListBuffer:
    def __init__(self):
        self.chunks = []
        self.size = 0

    def write(self, data):
        self.chunks.append(data)
        nbytes = len(data)
        self.size += nbytes
        return nbytes

    def getvalue(self):
        return b"".join(self.chunks)


async def _download_time_based_async(client, filename, params):
    mrd = AsyncMultiRangeDownloader(client, params.bucket_name, filename)
    await mrd.open()

    async def _worker_coro():
        total_bytes_downloaded = 0
        offset = 0
        is_warming_up = True
        start_time = time.perf_counter()
        warmup_end_time = start_time + params.warmup_duration
        test_end_time = warmup_end_time + params.duration
        measured_start_time = None
        measured_end_time = None

        while time.perf_counter() < test_end_time:
            current_time = time.perf_counter()
            if is_warming_up and current_time >= warmup_end_time:
                is_warming_up = False
                total_bytes_downloaded = 0  # Reset counter after warmup
                measured_start_time = current_time

            ranges = []
            if params.pattern == "rand":
                for _ in range(params.num_ranges):
                    offset = random.randint(
                        0, params.file_size_bytes - params.chunk_size_bytes
                    )
                    ranges.append((offset, params.chunk_size_bytes, _DummyListBuffer()))
            else:  # seq
                for _ in range(params.num_ranges):
                    ranges.append((offset, params.chunk_size_bytes, _DummyListBuffer()))
                    offset += params.chunk_size_bytes
                    if offset + params.chunk_size_bytes > params.file_size_bytes:
                        offset = 0  # Reset offset if end of file is reached

            await mrd.download_ranges(ranges)

            bytes_in_buffers = sum(r[2].size for r in ranges)
            assert bytes_in_buffers == params.chunk_size_bytes * params.num_ranges

            if not is_warming_up:
                total_bytes_downloaded += params.chunk_size_bytes * params.num_ranges
                measured_end_time = time.perf_counter()
        return _build_download_result(
            total_bytes_downloaded, measured_start_time, measured_end_time
        )

    tasks = [asyncio.create_task(_worker_coro()) for _ in range(params.num_coros)]
    results = await asyncio.gather(*tasks)

    await mrd.close()
    return _aggregate_download_results(results)


def _download_files_worker(process_idx, filename, params, bucket_type):
    if bucket_type == "rapid":
        return worker_loop.run_until_complete(
            _download_time_based_async(worker_client, filename, params)
        )
    else:  # regional
        return _download_time_based_json(worker_json_client, filename, params)


def download_files_mp_mc_wrapper(pool, files_names, params, bucket_type):
    args = [(i, files_names[i], params, bucket_type) for i in range(len(files_names))]

    results = pool.starmap(_download_files_worker, args)
    agg_res = _aggregate_download_results(results)
    return agg_res.total_bytes, agg_res.measured_end_time - agg_res.measured_start_time


@pytest.mark.parametrize(
    "workload_params",
    all_params["read_seq_multi_process"] + all_params["read_rand_multi_process"],
    indirect=True,
    ids=lambda p: p.name,
)
def test_downloads_multi_proc_multi_coro(
    benchmark, storage_client, monitor, workload_params
):
    params, files_names = workload_params
    logging.info(f"num files: {len(files_names)}")

    ctx = multiprocessing.get_context("spawn")
    pool = ctx.Pool(
        processes=params.num_processes,
        initializer=_worker_init,
        initargs=(params.bucket_type,),
    )

    download_bytes_list = []
    download_elapsed_times = []

    def target_wrapper(*args, **kwargs):
        total_bytes, measured_elapsed_time = download_files_mp_mc_wrapper(
            pool, *args, **kwargs
        )
        download_bytes_list.append(total_bytes)
        download_elapsed_times.append(measured_elapsed_time)
        return

    try:
        with monitor() as m:
            benchmark.pedantic(
                target=target_wrapper,
                iterations=1,
                rounds=params.rounds,
                args=(files_names, params, params.bucket_type),
            )
    finally:
        pool.close()
        pool.join()
        throughput_mib_s = _calculate_average_throughput_mib_s(
            download_bytes_list, download_elapsed_times
        )
        benchmark.extra_info["avg_throughput_mib_s"] = f"{throughput_mib_s:.2f}"
        print(
            f"Avg Throughput of {params.rounds} round(s): {throughput_mib_s:.2f} MiB/s"
        )
        publish_benchmark_extra_info(
            benchmark,
            params,
            download_bytes_list=download_bytes_list,
            duration=download_elapsed_times,
        )
        publish_resource_metrics(benchmark, m)
