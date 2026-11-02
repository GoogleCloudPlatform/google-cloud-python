# Benchmarks

The performance test suite is located in [test/benchmark.py](https://github.com/cloudspannerecosystem/python-spanner-sqlalchemy/blob/main/test/benchmark.py) and intended to compare execution time difference between SQLAlchemy dialect for Spanner and pure Spanner client.

The test suite requirements:
- `scipy` Python package installed
- the original dialect requirements

Use `PROJECT`, `INSTANCE` and `DATABASE` module constants to set a project to execute tests on.

The following measurements were made on a VM instance.

# 25-11-2021

|Test|mean, sec|error|std_dev|
|----|-------|-----|--------|
|SPANNER insert_one_row_with_fetch_after| 0.16|0.0|0.03|
|ALCHEMY insert_one_row_with_fetch_after|  0.11| 0.0|0.02|
|SPANNER read_one_row| 0.04| 0.0| 0.01|
|ALCHEMY read_one_row| 0.01| 0.0| 0.0|
|SPANNER insert_many_rows|  0.33| 0.01| 0.05|
|ALCHEMY insert_many_rows|  0.32| 0.01| 0.06|
|SPANNER select_many_rows| 0.04| 0.0| 0.01|
|ALCHEMY select_many_rows|   0.03| 0.0| 0.0|
|SPANNER insert_many_rows_with_mutations| 0.07| 0.0| 0.03|
|SQLALCHEMY insert_many_rows_with_mutations| 0.31| 0.01| 0.07|
