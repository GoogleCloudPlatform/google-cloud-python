# python-storage benchmarking

**This is not an officially supported Google product**

This benchmarking script is used by Storage client library maintainers to benchmark various workloads and collect metrics in order to improve performance of the library.
Currently the benchmarking runs a Write-1-Read-3 workload and measures the usual two QoS performance attributes, latency and throughput.

## Run example:
This runs 10K iterations of Write-1-Read-3 on 5KiB to 16KiB files, and generates output to a default csv file `output_bench<TIMESTAMP>.csv`:
```bash
$ cd python-storage
$ pip install -e . # install google.cloud.storage locally
$ cd tests/perf
$ python3 benchmarking.py --num_samples 10000 --object_size 5120..16384 --output_type csv
```

## CLI parameters

| Parameter | Description | Possible values | Default |
| --------- | ----------- | --------------- |:-------:|
| --project | GCP project identifier | a project id| * |
| --api | API to use | only JSON is currently supported in python benchmarking | `JSON` |
| --output_type | output results as csv records or cloud monitoring | `csv`, `cloud-monitoring` | `cloud-monitoring` |
| --object_size | object size in bytes; can be a range min..max | string | `1048576` (1 MiB) |
| --range_read_size | size of the range to read in bytes | any positive integer <br> <=0 reads the full object | `0` |
| --minimum_read_offset | minimum offset for the start of the range to be read in bytes | any integer >0 | `0` |
| --maximum_read_offset | maximum offset for the start of the range to be read in bytes | any integer >0 | `0` |
| --samples | number of W1R3 iterations | any positive integer | `8000` |
| --bucket | storage bucket name | a bucket name | `pybench<TIMESTAMP>` |
| --bucket_region | bucket region for benchmarks | any GCS region | `US-WEST1` |
| --workers | number of processes (multiprocessing enabled) | any positive integer | 16 (recommend not to exceed 16) |
| --test_type | test type to run benchmarking | `w1r3`, `range` | `w1r3` |
| --output_file | file to output results to | any file path | `output_bench<TIMESTAMP>.csv` |
| --tmp_dir | temp directory path on file system | any file path | `tm-perf-metrics` |
| --delete_bucket | whether or not to delete GCS bucket used for benchmarking| bool | `False` |


## Workload definition and CSV headers

For each invocation of the benchmark, write a new object of random size between `min_size` and `max_size` . After the successful write, download the object in full three times. For each of the 4 operations record the following fields:

| Field | Description |
| ----- | ----------- |
| Op | the name of the operations (WRITE, READ[{0,1,2}]) |
| ObjectSize | the number of bytes of the object |
| LibBufferSize | configured to use the [library default of 100 MiB](https://github.com/googleapis/python-storage/blob/main/google/cloud/storage/blob.py#L135) |
| Crc32cEnabled | bool: whether crc32c was computed for the operation |
| MD5Enabled | bool: whether MD5 was computed for the operation |
| ApiName | default to JSON|
| ElapsedTimeUs | the elapsed time in microseconds the operation took |
| Status | completion state of the operation [OK, FAIL] |
| RunID | timestamp from the benchmarking run |
| AppBufferSize | N/A |
| CpuTimeUs | N/A |