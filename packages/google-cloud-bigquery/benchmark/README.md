# BigQuery Benchmark
This directory contains benchmark scripts for BigQuery client. It is created primarily for project
maintainers to measure library performance.

## Usage
`python benchmark.py`


### Flags
Run `python benchmark.py -h` for detailed information on available flags.

`--reruns` can be used to override the default number of times a query is rerun. Must be a positive
integer. Default value is 3.

`--projectid` can be used to run benchmarks in a different project.  If unset, the GOOGLE_CLOUD_PROJECT
 environment variable is used.

`--queryfile` can be used to override the default file which contains queries to be instrumented.

`--table` can be used to specify a table to which benchmarking results should be streamed.  The format
for this string is in BigQuery standard SQL notation without escapes, e.g. `projectid.datasetid.tableid`

`--create_table` can be used to have the benchmarking tool create the destination table prior to streaming.

`--tag` allows arbitrary key:value pairs to be set.  This flag can be specified multiple times.

When `--create_table` flag is set, must also specify the name of the new table using `--table`.

### Example invocations

Setting all the flags
```
python benchmark.py \
  --reruns 5 \
  --projectid test_project_id \
  --table logging_project_id.querybenchmarks.measurements \
  --create_table \
  --tag source:myhostname \
  --tag somekeywithnovalue \
  --tag experiment:special_environment_thing
```

Or, a more realistic invocation using shell substitions:
```
python benchmark.py \
  --reruns 5 \
  --table $BENCHMARK_TABLE \
  --tag origin:$(hostname) \
  --tag branch:$(git branch --show-current) \
  --tag latestcommit:$(git log --pretty=format:'%H' -n 1)
```

## Stream Results To A BigQuery Table

When streaming benchmarking results to a BigQuery table, the table schema is as follows:
```
[
  {
    "name": "groupname",
    "type": "STRING"
  },
  {
    "name": "name",
    "type": "STRING"
  },
  {
    "name": "tags",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {
        "name": "key",
        "type": "STRING"
      },
      {
        "name": "value",
        "type": "STRING"
      }
    ]
  },
  {
    "name": "SQL",
    "type": "STRING"
  },
  {
    "name": "runs",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {
        "name": "errorstring",
        "type": "STRING"
      },
      {
        "name": "start_time",
        "type": "TIMESTAMP"
      },
      {
        "name": "query_end_time",
        "type": "TIMESTAMP"
      },
      {
        "name": "first_row_returned_time",
        "type": "TIMESTAMP"
      },
      {
        "name": "all_rows_returned_time",
        "type": "TIMESTAMP"
      },
      {
        "name": "total_rows",
        "type": "INTEGER"
      }
    ]
  },
  {
    "name": "event_time",
    "type": "TIMESTAMP"
  }
]
```

The table schema is the same as the [benchmark in go](https://github.com/googleapis/google-cloud-go/tree/main/bigquery/benchmarks),
so results from both languages can be streamed to the same table.

## BigQuery Benchmarks In Other Languages
* Go: https://github.com/googleapis/google-cloud-go/tree/main/bigquery/benchmarks
* JAVA: https://github.com/googleapis/java-bigquery/tree/main/benchmark
