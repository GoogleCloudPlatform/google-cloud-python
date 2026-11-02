# pandas-gbq benchmarks

This directory contains a few scripts which are useful for performance
testing the pandas-gbq library. Use cProfile to time the script and see
details about where time is spent. To avoid timing how long BigQuery takes to
execute a query, run the benchmark twice to ensure the results are cached.

## `read_gbq`

Read a small table (a few KB).

    python -m cProfile --sort=cumtime read_gbq_small_results.py

Read a large-ish table (100+ MB).

    python -m cProfile --sort=cumtime read_gbq_large_results.py
