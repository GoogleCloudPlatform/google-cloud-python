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
"""Microbenchmarks for Google Cloud Storage read operations.

This module contains performance benchmarks for various read patterns from Google Cloud Storage.
It includes three main test functions:
- `test_downloads_single_proc_single_coro`: Benchmarks reads using a single process and a single coroutine.
- `test_downloads_single_proc_multi_coro`: Benchmarks reads using a single process and multiple coroutines.
- `test_downloads_multi_proc_multi_coro`: Benchmarks reads using multiple processes and multiple coroutines.

All other functions in this module are helper methods for these three tests.
"""

import asyncio
import logging
import multiprocessing
import random
import time
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

import pytest

import tests.perf.microbenchmarks.reads.config as config
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from tests.perf.microbenchmarks._utils import publish_benchmark_extra_info
from tests.perf.microbenchmarks.conftest import (
    publish_resource_metrics,
)

all_params = config._get_params()


async def create_client():
    """Initializes async client and gets the current event loop."""
    return AsyncGrpcClient()


async def download_chunks_using_mrd_async(client, filename, other_params, chunks):
    # start timer.
    start_time = time.monotonic_ns()

    total_bytes_downloaded = 0
    mrd = AsyncMultiRangeDownloader(client, other_params.bucket_name, filename)
    await mrd.open()
    for offset, size in chunks:
        buffer = BytesIO()
        await mrd.download_ranges([(offset, size, buffer)])
        total_bytes_downloaded += buffer.tell()
    await mrd.close()

    assert total_bytes_downloaded == other_params.file_size_bytes

    # end timer.
    end_time = time.monotonic_ns()
    elapsed_time = end_time - start_time
    return elapsed_time / 1_000_000_000


def download_chunks_using_mrd(loop, client, filename, other_params, chunks):
    return loop.run_until_complete(
        download_chunks_using_mrd_async(client, filename, other_params, chunks)
    )


def download_chunks_using_json(_, json_client, filename, other_params, chunks):
    bucket = json_client.bucket(other_params.bucket_name)
    blob = bucket.blob(filename)
    start_time = time.monotonic_ns()
    for offset, size in chunks:
        _ = blob.download_as_bytes(start=offset, end=offset + size - 1)
    return (time.monotonic_ns() - start_time) / 1_000_000_000


@pytest.mark.parametrize(
    "workload_params",
    all_params["read_rand"] + all_params["read_seq"],
    indirect=True,
    ids=lambda p: p.name,
)
def test_downloads_single_proc_single_coro(
    benchmark, storage_client, blobs_to_delete, monitor, workload_params
):
    """
    Benchmarks reads using a single process and a single coroutine.
    It creates chunks based on object size and chunk_size, then passes them to either
    `download_chunks_using_mrd` (for rapid buckets) or `download_chunks_using_json` (for regional buckets)
    for benchmarking using `benchmark.pedantic`.
    """
    params, files_names = workload_params

    object_size = params.file_size_bytes
    chunk_size = params.chunk_size_bytes
    chunks = []
    for offset in range(0, object_size, chunk_size):
        size = min(chunk_size, object_size - offset)
        chunks.append((offset, size))

    if params.pattern == "rand":
        logging.info("randomizing chunks")
        random.shuffle(chunks)

    if params.bucket_type == "rapid":
        logging.info("bucket type rapid")
        target_func = download_chunks_using_mrd
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = loop.run_until_complete(create_client())
    else:
        logging.info("bucket type regional")
        target_func = download_chunks_using_json
        loop = None
        client = storage_client

    output_times = []

    def target_wrapper(*args, **kwargs):
        result = target_func(*args, **kwargs)
        output_times.append(result)
        return output_times

    try:
        with monitor() as m:
            output_times = benchmark.pedantic(
                target=target_wrapper,
                iterations=1,
                rounds=params.rounds,
                args=(
                    loop,
                    client,
                    files_names[0],
                    params,
                    chunks,
                ),
            )
    finally:
        if loop is not None:
            tasks = asyncio.all_tasks(loop=loop)
            for task in tasks:
                task.cancel()
            loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
            loop.close()
    publish_benchmark_extra_info(benchmark, params, true_times=output_times)
    publish_resource_metrics(benchmark, m)

    blobs_to_delete.extend(
        storage_client.bucket(params.bucket_name).blob(f) for f in files_names
    )


def download_files_using_mrd_multi_coro(loop, client, files, other_params, chunks):
    """
    Downloads multiple files concurrently using AsyncMultiRangeDownloader (MRD) with asyncio.

    For each file, it creates a coroutine to download its chunks using `download_chunks_using_mrd_async`.
    All coroutines are then executed concurrently using `asyncio.gather`.
    The function returns the maximum latency observed among all coroutines.

    Args:
        loop: The asyncio event loop.
        client: The AsyncGrpcClient instance.
        files (list): A list of filenames to download.
        other_params: An object containing benchmark parameters (e.g., bucket_name, file_size_bytes).
        chunks (list): A list of (offset, size) tuples representing the parts of each file to download.

    Returns:
        float: The maximum latency (in seconds) among all coroutines.
    """

    async def main():
        if len(files) == 1:
            result = await download_chunks_using_mrd_async(
                client, files[0], other_params, chunks
            )
            return [result]
        else:
            tasks = []
            for f in files:
                tasks.append(
                    download_chunks_using_mrd_async(client, f, other_params, chunks)
                )
            return await asyncio.gather(*tasks)

    results = loop.run_until_complete(main())
    return max(results)


def download_files_using_json_multi_threaded(
    _, json_client, files, other_params, chunks
):
    """
    Downloads multiple files concurrently using the JSON API with a ThreadPoolExecutor.

    For each file, it submits a task to a `ThreadPoolExecutor` to download its chunks
    using `download_chunks_using_json`. The number of concurrent downloads is
    determined by `other_params.num_coros` (which acts as `max_workers`).
    The function returns the maximum latency among all concurrent downloads.

    The `chunks` parameter is a list of (offset, size) tuples representing
    the parts of each file to download.
    """
    results = []
    # In the context of multi-coro, num_coros is the number of files to download concurrently.
    # So we can use it as max_workers for the thread pool.
    with ThreadPoolExecutor(max_workers=other_params.num_coros) as executor:
        futures = []
        for f in files:
            future = executor.submit(
                download_chunks_using_json, None, json_client, f, other_params, chunks
            )
            futures.append(future)

        for future in futures:
            results.append(future.result())

    return max(results)


@pytest.mark.parametrize(
    "workload_params",
    all_params["read_seq_multi_coros"] + all_params["read_rand_multi_coros"],
    indirect=True,
    ids=lambda p: p.name,
)
def test_downloads_single_proc_multi_coro(
    benchmark, storage_client, blobs_to_delete, monitor, workload_params
):
    params, files_names = workload_params

    object_size = params.file_size_bytes
    chunk_size = params.chunk_size_bytes
    chunks = []
    for offset in range(0, object_size, chunk_size):
        size = min(chunk_size, object_size - offset)
        chunks.append((offset, size))

    if params.pattern == "rand":
        logging.info("randomizing chunks")
        random.shuffle(chunks)

    if params.bucket_type == "rapid":
        logging.info("bucket type rapid")
        target_func = download_files_using_mrd_multi_coro
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = loop.run_until_complete(create_client())
    else:
        logging.info("bucket type regional")
        target_func = download_files_using_json_multi_threaded
        loop = None
        client = storage_client

    output_times = []

    def target_wrapper(*args, **kwargs):
        result = target_func(*args, **kwargs)
        output_times.append(result)
        return output_times

    try:
        with monitor() as m:
            output_times = benchmark.pedantic(
                target=target_wrapper,
                iterations=1,
                rounds=params.rounds,
                args=(
                    loop,
                    client,
                    files_names,
                    params,
                    chunks,
                ),
            )
    finally:
        if loop is not None:
            tasks = asyncio.all_tasks(loop=loop)
            for task in tasks:
                task.cancel()
            loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
            loop.close()
    publish_benchmark_extra_info(benchmark, params, true_times=output_times)
    publish_resource_metrics(benchmark, m)

    blobs_to_delete.extend(
        storage_client.bucket(params.bucket_name).blob(f) for f in files_names
    )


# --- Global Variables for Worker Process ---
worker_loop = None
worker_client = None
worker_json_client = None


def _worker_init(bucket_type):
    """Initializes a persistent event loop and client for each worker process."""
    global worker_loop, worker_client, worker_json_client
    if bucket_type == "rapid":
        worker_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(worker_loop)
        worker_client = worker_loop.run_until_complete(create_client())
    else:  # regional
        from google.cloud import storage

        worker_json_client = storage.Client()


def _download_files_worker(files_to_download, other_params, chunks, bucket_type):
    if bucket_type == "rapid":
        # The loop and client are already initialized in _worker_init.
        # download_files_using_mrd_multi_coro returns max latency of coros
        return download_files_using_mrd_multi_coro(
            worker_loop, worker_client, files_to_download, other_params, chunks
        )
    else:  # regional
        # download_files_using_json_multi_threaded returns max latency of threads
        return download_files_using_json_multi_threaded(
            None, worker_json_client, files_to_download, other_params, chunks
        )


def download_files_mp_mc_wrapper(pool, files_names, params, chunks, bucket_type):
    num_coros = params.num_coros  # This is n, number of files per process

    # Distribute filenames to processes
    filenames_per_process = [
        files_names[i : i + num_coros] for i in range(0, len(files_names), num_coros)
    ]
    args = [
        (
            filenames,
            params,
            chunks,
            bucket_type,
        )
        for filenames in filenames_per_process
    ]

    results = pool.starmap(_download_files_worker, args)
    return max(results)


@pytest.mark.parametrize(
    "workload_params",
    all_params["read_seq_multi_process"] + all_params["read_rand_multi_process"],
    indirect=True,
    ids=lambda p: p.name,
)
def test_downloads_multi_proc_multi_coro(
    benchmark, storage_client, blobs_to_delete, monitor, workload_params
):
    """
    Benchmarks reads using multiple processes and multiple coroutines.

    This test distributes `m*n` files among `m` processes, where each process
    downloads `n` files concurrently using `n` coroutines. The processes are spawned
    in "spawn" mode. The reported latency for each round is the maximum latency
    observed across all processes.
    """
    params, files_names = workload_params
    logging.info(f"num files: {len(files_names)}")

    object_size = params.file_size_bytes
    chunk_size = params.chunk_size_bytes
    chunks = []
    for offset in range(0, object_size, chunk_size):
        size = min(chunk_size, object_size - offset)
        chunks.append((offset, size))

    if params.pattern == "rand":
        logging.info("randomizing chunks")
        random.shuffle(chunks)

    ctx = multiprocessing.get_context("spawn")
    pool = ctx.Pool(
        processes=params.num_processes,
        initializer=_worker_init,
        initargs=(params.bucket_type,),
    )
    output_times = []

    def target_wrapper(*args, **kwargs):
        result = download_files_mp_mc_wrapper(pool, *args, **kwargs)
        output_times.append(result)
        return output_times

    try:
        with monitor() as m:
            output_times = benchmark.pedantic(
                target=target_wrapper,
                iterations=1,
                rounds=params.rounds,
                args=(
                    files_names,
                    params,
                    chunks,
                    params.bucket_type,
                ),
            )
    finally:
        pool.close()
        pool.join()
        publish_benchmark_extra_info(benchmark, params, true_times=output_times)
        publish_resource_metrics(benchmark, m)

    blobs_to_delete.extend(
        storage_client.bucket(params.bucket_name).blob(f) for f in files_names
    )
