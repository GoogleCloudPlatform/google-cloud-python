# Performance Microbenchmarks

This directory contains performance microbenchmarks for the Python Storage client library.

## Usage

To run the benchmarks, use `pytest` with the `--benchmark-json` flag to specify an output file for the results.

Example:
```bash
pytest --benchmark-json=output.json -vv -s tests/perf/microbenchmarks/reads/test_reads.py
```

### Running a Specific Test

To run a single test, append `::` followed by the test name to the file path.

Examples:
```bash
pytest --benchmark-json=output.json -vv -s tests/perf/microbenchmarks/reads/test_reads.py::test_downloads_single_proc_single_coro
```
```bash
pytest --benchmark-json=output.json -vv -s tests/perf/microbenchmarks/writes/test_writes.py::test_uploads_single_proc_single_coro
```

## Configuration

The benchmarks are configured using `config.yaml` files located in the respective subdirectories (e.g., `reads/config.yaml`).

## Overriding Buckets

You can override the buckets used in the benchmarks by setting environment variables. Please refer to the specific benchmark implementation for the environment variable names.

## Output

The benchmarks produce a JSON file with the results. This file can be converted to a CSV file for easier analysis in spreadsheets using the provided `json_to_csv.py` script.

Example:
```bash
python3 tests/perf/microbenchmarks/json_to_csv.py output.json
```
