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

"""Scripts for benchmarking BigQuery queries performance."""

import argparse
from datetime import datetime
import json
import os

from google.api_core import exceptions

from google.cloud import bigquery

_run_schema = [
    bigquery.SchemaField("groupname", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("name", "STRING", mode="NULLABLE"),
    bigquery.SchemaField(
        "tags",
        "RECORD",
        mode="REPEATED",
        fields=[
            bigquery.SchemaField("key", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("value", "STRING", mode="NULLABLE"),
        ],
    ),
    bigquery.SchemaField("SQL", "STRING", mode="NULLABLE"),
    bigquery.SchemaField(
        "runs",
        "RECORD",
        mode="REPEATED",
        fields=[
            bigquery.SchemaField("errorstring", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("start_time", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField("query_end_time", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField(
                "first_row_returned_time", "TIMESTAMP", mode="NULLABLE"
            ),
            bigquery.SchemaField(
                "all_rows_returned_time", "TIMESTAMP", mode="NULLABLE"
            ),
            bigquery.SchemaField("total_rows", "INTEGER", mode="NULLABLE"),
        ],
    ),
    bigquery.SchemaField("event_time", "TIMESTAMP", mode="NULLABLE"),
]


def _check_pos_int(value):
    """Verifies the value is a positive integer."""
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            f"Argument rerun should be positive int. Actual value: {value}"
        )
    return ivalue


def _parse_tag(tag):
    """Parses input tag into key value pair as a dict."""
    tagstring = str(tag)
    key, value = tagstring.split(":")
    if not key or not value:
        raise argparse.ArgumentTypeError(
            "key and value in tag need to be non-empty. Actual value: "
            + f"key={key}, value={value}"
        )
    return {"key": key, "value": value}


def _parse_args() -> dict:
    """Parses input flags."""
    parser = argparse.ArgumentParser(description="Benchmark for BigQuery.")

    parser.add_argument(
        "--reruns",
        action="store",
        type=_check_pos_int,
        default=3,
        metavar="",
        help="how many times each query is run. Must be a positive integer."
        + "Default 3 times",
    )

    parser.add_argument(
        "--projectid",
        action="store",
        type=str,
        metavar="",
        help="run benchmarks in a different project. If unset, the "
        + "GOOGLE_CLOUD_PROJECT environment variable is used",
    )

    parser.add_argument(
        "--queryfile",
        action="store",
        type=str,
        metavar="",
        default="queries.json",
        help="override the default file which contains queries to be instrumented",
    )

    parser.add_argument(
        "--table",
        action="store",
        type=str,
        metavar="",
        help="specify a table to which benchmarking results should be "
        + "streamed. The format for this string is in BigQuery standard SQL "
        + "notation without escapes, e.g. projectid.datasetid.tableid",
    )

    parser.add_argument(
        "--create_table",
        action="store_true",
        help="let the benchmarking tool create the destination table prior to"
        + " streaming; if set, also need to set --table to specify table name",
    )

    parser.add_argument(
        "--tag",
        action="append",
        type=_parse_tag,
        metavar="",
        help="set arbitrary key:value pairs, can be set multiple times",
    )

    args = parser.parse_args()
    args_dict = vars(args)

    # Verifies that project id is set.
    if not args_dict.get("projectid"):
        if projectid_env := os.environ["GOOGLE_CLOUD_PROJECT"]:
            args_dict["projectid"] = projectid_env
        else:
            raise ValueError(
                "Must provide --projectid or set "
                "GOOGLE_CLOUD_PROJECT environment variable"
            )

    # Verifies that table name is specified when `create_table == True`.
    if args_dict.get("create_table") and not args_dict.get("table"):
        raise ValueError(
            "When --create_table is present, must specify table name with --table"
        )

    return args_dict


def _prepare_table(client, create_table: bool, table_name: str) -> str:
    """Ensures a table exists, and optionally creates it if directed."""

    # Verifies that table destination is of valid format.
    parts = table_name.split(".")
    if len(parts) != 3:
        raise ValueError(f"Expected table in p.d.t format, got: {table_name}")

    table = bigquery.Table(table_name, schema=_run_schema)

    # Create table if create_table == True.
    if create_table:
        table = client.create_table(table)
        print(f"Created table {table.project}.{table.dataset_id}." f"{table.table_id}")

    # Verifies that table exists.
    client.get_table(table_name)
    return table_name


def _run_query(client, query: str, rerun: int) -> list:
    """Runs individual query for `rerun` times, and returns run results."""
    runs = []

    for _ in range(rerun):
        print(".", end="", flush=True)
        run = {}
        num_rows = 0
        num_cols = 0
        start_time = datetime.now()
        first_row_time = datetime.min
        end_time = datetime.min

        job = client.query(query)
        query_end_time = datetime.now()

        try:
            rows = job.result()
            for row in rows:
                if num_rows == 0:
                    num_cols = len(row)
                    first_row_time = datetime.now()
                elif num_cols != len(row):
                    raise RuntimeError(f"found {len(row)} columns, expected {num_cols}")
                num_rows += 1
            end_time = datetime.now()
        except exceptions.BadRequest as exc:
            run["errorstring"] = repr(exc)

        run["start_time"] = start_time.isoformat()
        run["query_end_time"] = query_end_time.isoformat()
        run["first_row_returned_time"] = first_row_time.isoformat()
        run["all_rows_returned_time"] = end_time.isoformat()
        run["total_rows"] = num_rows
        runs.append(run)

    print("")
    return runs


def _get_delta(time_str_1: str, time_str_2: str) -> str:
    """Calculates delta of two ISO format time string, and return as a string."""
    time_1 = datetime.fromisoformat(time_str_1)
    time_2 = datetime.fromisoformat(time_str_2)
    delta = time_1 - time_2
    return str(delta)


def _is_datetime_min(time_str: str) -> bool:
    return datetime.fromisoformat(time_str) == datetime.min


def _summary(run: dict) -> str:
    """Converts run dict to run summary string."""
    no_val = "NODATA"
    output = ["QUERYTIME "]

    if not _is_datetime_min(run.get("query_end_time")):
        output.append(f"{_get_delta(run.get('query_end_time'), run.get('start_time'))}")
    else:
        output.append(no_val)
    output.append(" FIRSTROW ")

    if not _is_datetime_min(run.get("first_row_returned_time")):
        output.append(
            f"{_get_delta(run.get('first_row_returned_time'), run.get('start_time'))}"
        )
    else:
        output.append(no_val)
    output += " ALLROWS "

    if not _is_datetime_min(run.get("all_rows_returned_time")):
        output.append(
            f"{_get_delta(run.get('all_rows_returned_time'), run.get('start_time'))}"
        )
    else:
        output.append(no_val)

    if run.get("total_rows"):
        output.append(f" ROWS {run.get('total_rows')}")
    if run.get("errorstring"):
        output.append(f" ERRORED {run.get('errorstring')}")

    return "".join(output)


def _print_results(profiles: list):
    for i, prof in enumerate(profiles):
        print(f"{i + 1}: ({prof['groupname']}:{prof['name']})")
        print(f"SQL: {prof['SQL']}")
        print("MEASUREMENTS")
        for j, run in enumerate(prof["runs"]):
            print(f"\t\t({j}) {_summary(run)}")


def _run_benchmarks(args: dict) -> list:
    client = bigquery.Client()

    # If we're going to stream results, let's make sure we can do that
    # before running all the tests.
    table_id = ""
    if args.get("create_table") or args.get("table"):
        table_id = _prepare_table(client, args.get("create_table"), args.get("table"))

    queries_file = args.get("queryfile")
    with open(queries_file, "r") as f:
        groups = json.loads(f.read())

    measure_start = datetime.now()
    profiles = []
    for group_name, group in groups.items():
        for name, query in group.items():
            print(f"Measuring {group_name} : {name}", end="", flush=True)
            event_time = datetime.now()
            runs = _run_query(client, query, args.get("reruns"))

            profile = {}
            profile["groupname"] = group_name
            profile["name"] = name
            profile["tags"] = args.get("tag") or []
            profile["SQL"] = query
            profile["runs"] = runs
            profile["event_time"] = event_time.isoformat()
            profiles.append(profile)

    measure_end = datetime.now()
    print(f"Measurement time: {str(measure_end - measure_start)}")

    # Stream benchmarking results to table, if required.
    if table_id:
        print(f"Streaming test results to table {table_id}...")
        errors = client.insert_rows_json(table_id, profiles)
        if errors:
            raise RuntimeError(f"Cannot upload queries profiles: {errors}")
        print("Streaming complete.")

    return profiles


if __name__ == "__main__":
    args = _parse_args()
    profiles = _run_benchmarks(args)
    _print_results(profiles)
