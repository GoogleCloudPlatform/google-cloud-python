# Benchwrapper

A small gRPC wrapper around the Spanner client library. This allows the
benchmarking code to prod at Spanner without speaking Python.

## Running
Run the following commands from python-spanner/ directory.
```
export SPANNER_EMULATOR_HOST=localhost:9010
python3 -m benchmark.benchwrapper.main --port 8081
