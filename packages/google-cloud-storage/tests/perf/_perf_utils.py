# Copyright 2023 Google LLC
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

"""Performance benchmarking helper methods. This is not an officially supported Google product."""

import csv
import logging
import os
import random
import shutil
import time
import uuid

from google.cloud import storage

##### DEFAULTS & CONSTANTS #####
HEADER = [
    "Op",
    "ObjectSize",
    "AppBufferSize",
    "LibBufferSize",
    "Crc32cEnabled",
    "MD5Enabled",
    "ApiName",
    "ElapsedTimeUs",
    "CpuTimeUs",
    "Status",
]
CHECKSUM = ["md5", "crc32c", None]
TIMESTAMP = time.strftime("%Y%m%d-%H%M%S")
DEFAULT_API = "JSON"
DEFAULT_BUCKET_NAME = f"pybench{TIMESTAMP}"
DEFAULT_BUCKET_REGION = "US-WEST1"
DEFAULT_OBJECT_RANGE_SIZE_BYTES = "1048576"  # 1 MiB
DEFAULT_NUM_SAMPLES = 8000
DEFAULT_NUM_PROCESSES = 16
DEFAULT_LIB_BUFFER_SIZE = 104857600  # 100MB
DEFAULT_CHUNKSIZE = 104857600  # 100 MB https://github.com/googleapis/python-storage/blob/main/google/cloud/storage/blob.py#L139
NOT_SUPPORTED = -1
DEFAULT_BASE_DIR = "tm-perf-metrics"
DEFAULT_OUTPUT_FILE = f"output_bench{TIMESTAMP}.csv"
DEFAULT_CREATE_SUBDIR_PROBABILITY = 0.1
SSB_SIZE_THRESHOLD_BYTES = 1048576


##### UTILITY METHODS #####


# Returns a boolean value with the provided probability.
def weighted_random_boolean(create_subdir_probability):
    return random.uniform(0.0, 1.0) <= create_subdir_probability


# Creates a random file with the given file name, path and size.
def generate_random_file(file_name, file_path, size):
    with open(os.path.join(file_path, file_name), "wb") as file_obj:
        file_obj.write(os.urandom(size))


# Creates a random directory structure consisting of subdirectories and random files.
# Returns an array of all the generated paths and total size in bytes of all generated files.
def generate_random_directory(
    max_objects,
    min_file_size,
    max_file_size,
    base_dir,
    create_subdir_probability=DEFAULT_CREATE_SUBDIR_PROBABILITY,
):
    directory_info = {
        "paths": [],
        "total_size_in_bytes": 0,
    }

    file_path = base_dir
    os.makedirs(file_path, exist_ok=True)
    for i in range(max_objects):
        if weighted_random_boolean(create_subdir_probability):
            file_path = f"{file_path}/{uuid.uuid4().hex}"
            os.makedirs(file_path, exist_ok=True)
            directory_info["paths"].append(file_path)
        else:
            file_name = uuid.uuid4().hex
            rand_size = random.randint(min_file_size, max_file_size)
            generate_random_file(file_name, file_path, rand_size)
            directory_info["total_size_in_bytes"] += rand_size
            directory_info["paths"].append(os.path.join(file_path, file_name))

    return directory_info


def results_to_csv(res):
    results = []
    for metric in HEADER:
        results.append(res.get(metric, -1))
    return results


def convert_to_csv(filename, results, workers):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)
        # Benchmarking main script uses Multiprocessing Pool.map(),
        # thus results is structured as List[List[Dict[str, any]]].
        for result in results:
            for row in result:
                writer.writerow(results_to_csv(row))


def convert_to_cloud_monitoring(bucket_name, results, workers):
    # Benchmarking main script uses Multiprocessing Pool.map(),
    # thus results is structured as List[List[Dict[str, any]]].
    for result in results:
        for res in result:
            # Only output successful benchmarking runs to cloud monitoring.
            status = res.get("Status").pop()  # convert ["OK"] --> "OK"
            if status != "OK":
                continue

            range_read_size = res.get("RangeReadSize", 0)
            object_size = res.get("ObjectSize")
            elapsed_time_us = res.get("ElapsedTimeUs")

            # Handle range reads and calculate throughput using range_read_size.
            if range_read_size > 0:
                size = range_read_size
            else:
                size = object_size

            # If size is greater than the defined threshold, report in MiB/s, otherwise report in KiB/s.
            if size >= SSB_SIZE_THRESHOLD_BYTES:
                throughput = (size / 1024 / 1024) / (elapsed_time_us / 1_000_000)
            else:
                throughput = (size / 1024) / (elapsed_time_us / 1_000_000)

            cloud_monitoring_output = (
                "throughput{"
                + "library=python-storage,"
                + "api={},".format(res.get("ApiName"))
                + "op={},".format(res.get("Op"))
                + "workers={},".format(workers)
                + "object_size={},".format(object_size)
                + "transfer_offset={},".format(res.get("TransferOffset", 0))
                + "transfer_size={},".format(res.get("TransferSize", object_size))
                + "app_buffer_size={},".format(res.get("AppBufferSize"))
                + "chunksize={},".format(res.get("TransferSize", object_size))
                + "crc32c_enabled={},".format(res.get("Crc32cEnabled"))
                + "md5_enabled={},".format(res.get("MD5Enabled"))
                + "cpu_time_us={},".format(res.get("CpuTimeUs"))
                + "peer='',"
                + f"bucket_name={bucket_name},"
                + "retry_count='',"
                + f"status={status}"
                + "}"
                f"{throughput}"
            )

            print(cloud_monitoring_output)


def cleanup_directory_tree(directory):
    """Clean up directory tree on disk."""
    try:
        shutil.rmtree(directory)
    except Exception as e:
        logging.exception(f"Caught an exception while deleting local directory\n {e}")


def cleanup_file(file_path):
    """Clean up local file on disk."""
    try:
        os.remove(file_path)
    except Exception as e:
        logging.exception(f"Caught an exception while deleting local file\n {e}")


def get_bucket_instance(bucket_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    if not bucket.exists():
        client.create_bucket(bucket)
    return bucket


def cleanup_bucket(bucket, delete_bucket=False):
    # Delete blobs first as the bucket may contain more than 256 blobs.
    try:
        blobs = bucket.list_blobs()
        for blob in blobs:
            blob.delete()
    except Exception as e:
        logging.exception(f"Caught an exception while deleting blobs\n {e}")
    # Delete bucket if delete_bucket is set to True
    if delete_bucket:
        try:
            bucket.delete(force=True)
        except Exception as e:
            logging.exception(f"Caught an exception while deleting bucket\n {e}")


def get_min_max_size(object_size):
    # Object size accepts a single value in bytes or a range in bytes min..max
    if object_size.find("..") < 0:
        min_size = int(object_size)
        max_size = int(object_size)
    else:
        split_sizes = object_size.split("..")
        min_size = int(split_sizes[0])
        max_size = int(split_sizes[1])
    return min_size, max_size


class logCount(logging.Handler):
    class LogType:
        def __init__(self):
            self.errors = 0

    def __init__(self):
        super().__init__()
        self.count = self.LogType()

    def emit(self, record):
        if record.levelname == "ERROR":
            self.count.errors += 1
