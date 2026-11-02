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

"""Performance benchmarking main script. This is not an officially supported Google product."""

import argparse
import logging
import multiprocessing
import sys

import _perf_utils as _pu
import profile_w1r3 as w1r3

from google.cloud import storage

##### PROFILE BENCHMARKING TEST TYPES #####
PROFILE_WRITE_ONE_READ_THREE = "w1r3"
PROFILE_RANGE_READ = "range"


def main(args):
    # Track error logging for BBMC reporting.
    counter = _pu.logCount()
    logging.basicConfig(
        level=logging.ERROR,
        handlers=[counter, logging.StreamHandler(sys.stderr)],
    )

    # Create a storage bucket to run benchmarking.
    if args.project is not None:
        client = storage.Client(project=args.project)
    else:
        client = storage.Client()

    bucket = client.bucket(args.bucket)
    if not bucket.exists():
        bucket = client.create_bucket(bucket, location=args.bucket_region)

    # Define test type and number of processes to run benchmarking.
    # Note that transfer manager tests defaults to using 1 process.
    num_processes = 1
    test_type = args.test_type
    if test_type == PROFILE_WRITE_ONE_READ_THREE:
        num_processes = args.workers
        benchmark_runner = w1r3.run_profile_w1r3
        logging.info(
            f"A total of {num_processes} processes are created to run benchmarking {test_type}"
        )
    elif test_type == PROFILE_RANGE_READ:
        num_processes = args.workers
        benchmark_runner = w1r3.run_profile_range_read
        logging.info(
            f"A total of {num_processes} processes are created to run benchmarking {test_type}"
        )

    # Allow multiprocessing to speed up benchmarking tests; Defaults to 1 for no concurrency.
    p = multiprocessing.Pool(num_processes)
    pool_output = p.map(benchmark_runner, [args for _ in range(args.samples)])

    # Output to Cloud Monitoring or CSV file.
    output_type = args.output_type
    if output_type == "cloud-monitoring":
        _pu.convert_to_cloud_monitoring(args.bucket, pool_output, num_processes)
    elif output_type == "csv":
        _pu.convert_to_csv(args.output_file, pool_output, num_processes)
        logging.info(
            f"Succesfully ran benchmarking. Please find your output log at {args.output_file}"
        )

    # Cleanup and delete blobs.
    _pu.cleanup_bucket(bucket, delete_bucket=args.delete_bucket)

    # BBMC will not surface errors unless the process is terminated with a non zero code.
    if counter.count.errors != 0:
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        type=str,
        default=None,
        help="GCP project identifier",
    )
    parser.add_argument(
        "--api",
        type=str,
        default="JSON",
        help="API to use",
    )
    parser.add_argument(
        "--test_type",
        type=str,
        default=PROFILE_WRITE_ONE_READ_THREE,
        help="Benchmarking test type",
    )
    parser.add_argument(
        "--object_size",
        type=str,
        default=_pu.DEFAULT_OBJECT_RANGE_SIZE_BYTES,
        help="Object size in bytes; can be a range min..max",
    )
    parser.add_argument(
        "--range_read_size",
        type=int,
        default=0,
        help="Size of the range to read in bytes",
    )
    parser.add_argument(
        "--minimum_read_offset",
        type=int,
        default=0,
        help="Minimum offset for the start of the range to be read in bytes",
    )
    parser.add_argument(
        "--maximum_read_offset",
        type=int,
        default=0,
        help="Maximum offset for the start of the range to be read in bytes",
    )
    parser.add_argument(
        "--samples",
        type=int,
        default=_pu.DEFAULT_NUM_SAMPLES,
        help="Number of samples to report",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=_pu.DEFAULT_NUM_PROCESSES,
        help="Number of processes- multiprocessing enabled",
    )
    parser.add_argument(
        "--bucket",
        type=str,
        default=_pu.DEFAULT_BUCKET_NAME,
        help="Storage bucket name",
    )
    parser.add_argument(
        "--bucket_region",
        type=str,
        default=_pu.DEFAULT_BUCKET_REGION,
        help="Bucket region",
    )
    parser.add_argument(
        "--output_type",
        type=str,
        default="cloud-monitoring",
        help="Ouput format, csv or cloud-monitoring",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default=_pu.DEFAULT_OUTPUT_FILE,
        help="File to output results to",
    )
    parser.add_argument(
        "--tmp_dir",
        type=str,
        default=_pu.DEFAULT_BASE_DIR,
        help="Temp directory path on file system",
    )
    parser.add_argument(
        "--delete_bucket",
        type=bool,
        default=False,
        help="Whether or not to delete GCS bucket used for benchmarking",
    )
    args = parser.parse_args()

    main(args)
