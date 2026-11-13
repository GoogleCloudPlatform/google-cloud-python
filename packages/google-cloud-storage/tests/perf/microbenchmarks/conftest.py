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
import asyncio
import contextlib
import multiprocessing
import os
import uuid
from typing import Any

import pytest

from google.cloud import storage
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    AsyncAppendableObjectWriter,
)
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from tests.perf.microbenchmarks.resource_monitor import ResourceMonitor
from tests.perf.microbenchmarks.writes.parameters import WriteParameters
from tests.system._helpers import delete_blob

_OBJECT_NAME_PREFIX = "micro-benchmark"


@pytest.fixture(scope="function")
def blobs_to_delete():
    blobs_to_delete = []

    yield blobs_to_delete

    for blob in blobs_to_delete:
        delete_blob(blob)


@pytest.fixture(scope="session")
def storage_client():
    from google.cloud.storage import Client

    client = Client()
    with contextlib.closing(client):
        yield client


@pytest.fixture
def monitor():
    """
    Provides the ResourceMonitor class.
    Usage: with monitor() as m: ...
    """
    return ResourceMonitor


def publish_resource_metrics(benchmark: Any, monitor: ResourceMonitor) -> None:
    """
    Helper function to publish resource monitor results to the extra_info property.
    """
    benchmark.extra_info.update(
        {
            "cpu_max_global": f"{monitor.max_cpu:.2f}",
            "mem_max": f"{monitor.max_mem:.2f}",
            "net_throughput_mb_s": f"{monitor.throughput_mb_s:.2f}",
            "vcpus": monitor.vcpus,
        }
    )


async def upload_appendable_object(bucket_name, object_name, object_size, chunk_size):
    # flush interval set to little over 1GiB to minimize number of flushes.
    # this method is to write "appendable" objects which will be used for
    # benchmarking reads, hence not concerned performance of writes here.
    writer = AsyncAppendableObjectWriter(
        AsyncGrpcClient(),
        bucket_name,
        object_name,
        writer_options={"FLUSH_INTERVAL_BYTES": 1026 * 1024**2},
    )
    await writer.open()
    uploaded_bytes = 0
    while uploaded_bytes < object_size:
        bytes_to_upload = min(chunk_size, object_size - uploaded_bytes)
        await writer.append(os.urandom(bytes_to_upload))
        uploaded_bytes += bytes_to_upload
    object_metdata = await writer.close(finalize_on_close=True)
    assert object_metdata.size == uploaded_bytes
    return uploaded_bytes


def upload_simple_object(bucket_name, object_name, object_size, chunk_size):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.chunk_size = chunk_size
    data = os.urandom(object_size)
    blob.upload_from_string(data)
    return object_size


def _upload_worker(args):
    bucket_name, object_name, object_size, chunk_size, bucket_type = args
    if bucket_type == "rapid":
        uploaded_bytes = asyncio.run(
            upload_appendable_object(bucket_name, object_name, object_size, chunk_size)
        )
    else:
        uploaded_bytes = upload_simple_object(
            bucket_name, object_name, object_size, chunk_size
        )
    return object_name, uploaded_bytes


def _create_files(
    num_files, bucket_name, bucket_type, object_size, chunk_size=1024 * 1024 * 1024
):
    """
    Create/Upload objects for benchmarking and return a list of their names.
    """
    object_names = [
        f"{_OBJECT_NAME_PREFIX}-{uuid.uuid4().hex[:5]}" for _ in range(num_files)
    ]

    args_list = [
        (bucket_name, object_names[i], object_size, chunk_size, bucket_type)
        for i in range(num_files)
    ]

    ctx = multiprocessing.get_context("spawn")
    with ctx.Pool() as pool:
        results = pool.map(_upload_worker, args_list)

    total_uploaded_bytes = sum(r[1] for r in results)
    assert total_uploaded_bytes == object_size * num_files

    return [r[0] for r in results]


@pytest.fixture
def workload_params(request):
    params = request.param
    if isinstance(params, WriteParameters):
        files_names = [
            f"{_OBJECT_NAME_PREFIX}-{uuid.uuid4().hex[:5]}"
            for _ in range(params.num_files)
        ]
    else:
        files_names = _create_files(
            params.num_files,
            params.bucket_name,
            params.bucket_type,
            params.file_size_bytes,
        )
    return params, files_names
