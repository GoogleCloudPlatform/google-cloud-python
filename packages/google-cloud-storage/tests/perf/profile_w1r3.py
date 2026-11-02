# Copyright 2022 Google LLC
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

"""Workload W1R3 profiling script. This is not an officially supported Google product."""

import logging
import os
import random
import time
import uuid
from functools import partial, update_wrapper

import _perf_utils as _pu

from google.cloud import storage


def WRITE(bucket, blob_name, checksum, size, args, **kwargs):
    """Perform an upload and return latency."""
    blob = bucket.blob(blob_name)
    file_path = f"{os.getcwd()}/{uuid.uuid4().hex}"
    # Create random file locally on disk
    with open(file_path, "wb") as file_obj:
        file_obj.write(os.urandom(size))

    start_time = time.monotonic_ns()
    blob.upload_from_filename(file_path, checksum=checksum, if_generation_match=0)
    end_time = time.monotonic_ns()

    elapsed_time = round(
        (end_time - start_time) / 1000
    )  # convert nanoseconds to microseconds

    # Clean up local file
    _pu.cleanup_file(file_path)

    return elapsed_time


def READ(bucket, blob_name, checksum, args, **kwargs):
    """Perform a download and return latency."""
    blob = bucket.blob(blob_name)
    if not blob.exists():
        raise Exception("Blob does not exist. Previous WRITE failed.")

    range_read_size = args.range_read_size
    range_read_offset = kwargs.get("range_read_offset")
    # Perfor range read if range_read_size is specified, else get full object.
    if range_read_size != 0:
        start = range_read_offset
        end = start + range_read_size - 1
    else:
        start = 0
        end = -1

    file_path = f"{os.getcwd()}/{blob_name}"
    with open(file_path, "wb") as file_obj:
        start_time = time.monotonic_ns()
        blob.download_to_file(file_obj, checksum=checksum, start=start, end=end)
        end_time = time.monotonic_ns()

    elapsed_time = round(
        (end_time - start_time) / 1000
    )  # convert nanoseconds to microseconds

    # Clean up local file
    _pu.cleanup_file(file_path)

    return elapsed_time


def _wrapped_partial(func, *args, **kwargs):
    """Helper method to create partial and propagate function name and doc from original function."""
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func


def _generate_func_list(args):
    """Generate Write-1-Read-3 workload."""
    bucket_name = args.bucket
    blob_name = f"{_pu.TIMESTAMP}-{uuid.uuid4().hex}"

    # parse min_size and max_size from object_size
    min_size, max_size = _pu.get_min_max_size(args.object_size)
    # generate randmon size in bytes using a uniform distribution
    size = random.randint(min_size, max_size)

    # generate random checksumming type: md5, crc32c or None
    idx_checksum = random.choice([0, 1, 2])
    checksum = _pu.CHECKSUM[idx_checksum]

    # generated random read_offset
    range_read_offset = random.randint(
        args.minimum_read_offset, args.maximum_read_offset
    )

    func_list = [
        _wrapped_partial(
            WRITE,
            storage.Client().bucket(bucket_name),
            blob_name,
            size=size,
            checksum=checksum,
            args=args,
        ),
        *[
            _wrapped_partial(
                READ,
                storage.Client().bucket(bucket_name),
                blob_name,
                size=size,
                checksum=checksum,
                args=args,
                num=i,
                range_read_offset=range_read_offset,
            )
            for i in range(3)
        ],
    ]
    return func_list


def log_performance(func, args, elapsed_time, status, failure_msg):
    """Hold benchmarking results per operation call."""
    size = func.keywords.get("size")
    checksum = func.keywords.get("checksum", None)
    num = func.keywords.get("num", None)
    range_read_size = args.range_read_size

    res = {
        "Op": func.__name__,
        "ElapsedTimeUs": elapsed_time,
        "ApiName": args.api,
        "RunID": _pu.TIMESTAMP,
        "CpuTimeUs": _pu.NOT_SUPPORTED,
        "AppBufferSize": _pu.NOT_SUPPORTED,
        "LibBufferSize": _pu.DEFAULT_LIB_BUFFER_SIZE,
        "ChunkSize": 0,
        "ObjectSize": size,
        "TransferSize": size,
        "TransferOffset": 0,
        "RangeReadSize": range_read_size,
        "BucketName": args.bucket,
        "Library": "python-storage",
        "Crc32cEnabled": checksum == "crc32c",
        "MD5Enabled": checksum == "md5",
        "FailureMsg": failure_msg,
        "Status": status,
    }

    if res["Op"] == "READ":
        res["Op"] += f"[{num}]"

        # For range reads (workload 2), record additional outputs
        if range_read_size > 0:
            res["TransferSize"] = range_read_size
            res["TransferOffset"] = func.keywords.get("range_read_offset", 0)

    return res


def run_profile_w1r3(args):
    """Run w1r3 benchmarking. This is a wrapper used with the main benchmarking framework."""
    results = []

    for func in _generate_func_list(args):
        failure_msg = ""
        try:
            elapsed_time = func()
        except Exception as e:
            failure_msg = (
                f"Caught an exception while running operation {func.__name__}\n {e}"
            )
            logging.exception(failure_msg)
            status = ["FAIL"]
            elapsed_time = _pu.NOT_SUPPORTED
        else:
            status = ["OK"]

        res = log_performance(func, args, elapsed_time, status, failure_msg)
        results.append(res)

    return results


def run_profile_range_read(args):
    """Run range read W2 benchmarking. This is a wrapper used with the main benchmarking framework."""
    results = []

    for func in _generate_func_list(args):
        failure_msg = ""
        try:
            elapsed_time = func()
        except Exception as e:
            failure_msg = (
                f"Caught an exception while running operation {func.__name__}\n {e}"
            )
            logging.exception(failure_msg)
            status = ["FAIL"]
            elapsed_time = _pu.NOT_SUPPORTED
        else:
            status = ["OK"]

    # Only measure the last read
    res = log_performance(func, args, elapsed_time, status, failure_msg)
    results.append(res)

    return results
