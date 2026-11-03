# Copyright 2021 Google LLC
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

import datetime
import decimal
import json
from typing import Tuple

import pytest
from google.api_core import exceptions
from google.cloud import bigquery
from google.cloud.bigquery import enums
from google.cloud.bigquery.query import (
    ArrayQueryParameter,
    RangeQueryParameter,
    ScalarQueryParameter,
    ScalarQueryParameterType,
    StructQueryParameter,
    StructQueryParameterType,
)


@pytest.fixture(params=["INSERT", "QUERY"])
def query_api_method(request):
    return request.param


@pytest.fixture(scope="session")
def table_with_9999_columns_10_rows(bigquery_client, project_id, dataset_id):
    """Generate a table of maximum width via CREATE TABLE AS SELECT.

    The first column is named 'rowval', and has a value from 1..rowcount
    Subsequent columns are named col_<N> and contain the value N*rowval, where
    N is between 1 and 9999 inclusive.
    """
    table_id = "many_columns"
    row_count = 10
    col_projections = ",".join(f"r * {n} as col_{n}" for n in range(1, 10000))
    sql = f"""
    CREATE TABLE `{project_id}.{dataset_id}.{table_id}`
    AS
    SELECT
        r as rowval,
        {col_projections}
    FROM
      UNNEST(GENERATE_ARRAY(1,{row_count},1)) as r
    """
    query_job = bigquery_client.query(sql)
    query_job.result()

    return f"{project_id}.{dataset_id}.{table_id}"


def test_query_many_columns(
    bigquery_client, table_with_9999_columns_10_rows, query_api_method
):
    # Test working with the widest schema BigQuery supports, 10k columns.
    query_job = bigquery_client.query(
        f"SELECT * FROM `{table_with_9999_columns_10_rows}`",
        api_method=query_api_method,
    )
    rows = list(query_job)
    assert len(rows) == 10

    # check field representations adhere to expected values.
    for row in rows:
        rowval = row["rowval"]
        for column in range(1, 10000):
            assert row[f"col_{column}"] == rowval * column


def test_query_statistics(bigquery_client, query_api_method):
    """
    A system test to exercise some of the extended query statistics.

    Note:  We construct a query that should need at least three stages by
    specifying a JOIN query.  Exact plan and stats are effectively
    non-deterministic, so we're largely interested in confirming values
    are present.
    """

    job_config = bigquery.QueryJobConfig()
    job_config.use_query_cache = False

    query_job = bigquery_client.query(
        """
        SELECT
          COUNT(1)
        FROM
        (
          SELECT
            year,
            wban_number
          FROM `bigquery-public-data.samples.gsod`
          LIMIT 1000
        ) lside
        INNER JOIN
        (
          SELECT
            year,
            state
          FROM `bigquery-public-data.samples.natality`
          LIMIT 1000
        ) rside
        ON
        lside.year = rside.year
        """,
        location="US",
        job_config=job_config,
        api_method=query_api_method,
    )

    # run the job to completion
    query_job.result()

    # Must reload job to get stats if jobs.query was used.
    if query_api_method == "QUERY":
        query_job.reload()

    # Assert top-level stats
    assert not query_job.cache_hit
    assert query_job.destination is not None
    assert query_job.done
    assert not query_job.dry_run
    assert query_job.num_dml_affected_rows is None
    assert query_job.priority == "INTERACTIVE"
    assert query_job.total_bytes_billed > 1
    assert query_job.total_bytes_processed > 1
    assert query_job.statement_type == "SELECT"
    assert query_job.slot_millis > 1

    # Make assertions on the shape of the query plan.
    plan = query_job.query_plan
    assert len(plan) >= 3
    first_stage = plan[0]
    assert first_stage.start is not None
    assert first_stage.end is not None
    assert first_stage.entry_id is not None
    assert first_stage.name is not None
    assert first_stage.parallel_inputs > 0
    assert first_stage.completed_parallel_inputs > 0
    assert first_stage.shuffle_output_bytes > 0
    assert first_stage.status == "COMPLETE"

    # Query plan is a digraph.  Ensure it has inter-stage links,
    # but not every stage has inputs.
    stages_with_inputs = 0
    for entry in plan:
        if len(entry.input_stages) > 0:
            stages_with_inputs = stages_with_inputs + 1
    assert stages_with_inputs > 0
    assert len(plan) > stages_with_inputs


_QUERY_PARAMETER_CASES = pytest.mark.parametrize(
    ("sql", "expected", "query_parameters"),
    (
        (
            "SELECT @question",
            "What is the answer to life, the universe, and everything?",
            [
                ScalarQueryParameter(
                    name="question",
                    type_="STRING",
                    value="What is the answer to life, the universe, and everything?",
                )
            ],
        ),
        (
            "SELECT @answer",
            42,
            [ScalarQueryParameter(name="answer", type_="INT64", value=42)],
        ),
        (
            "SELECT @pi",
            3.1415926,
            [ScalarQueryParameter(name="pi", type_="FLOAT64", value=3.1415926)],
        ),
        (
            "SELECT @pi_numeric_param",
            decimal.Decimal("3.141592654"),
            [
                ScalarQueryParameter(
                    name="pi_numeric_param",
                    type_="NUMERIC",
                    value=decimal.Decimal("3.141592654"),
                )
            ],
        ),
        (
            "SELECT @bignum_param",
            decimal.Decimal("-{d38}.{d38}".format(d38="9" * 38)),
            [
                ScalarQueryParameter(
                    name="bignum_param",
                    type_="BIGNUMERIC",
                    value=decimal.Decimal("-{d38}.{d38}".format(d38="9" * 38)),
                )
            ],
        ),
        (
            "SELECT @truthy",
            True,
            [ScalarQueryParameter(name="truthy", type_="BOOL", value=True)],
        ),
        (
            "SELECT @beef",
            b"DEADBEEF",
            [ScalarQueryParameter(name="beef", type_="BYTES", value=b"DEADBEEF")],
        ),
        (
            "SELECT @naive",
            datetime.datetime(2016, 12, 5, 12, 41, 9),
            [
                ScalarQueryParameter(
                    name="naive",
                    type_="DATETIME",
                    value=datetime.datetime(2016, 12, 5, 12, 41, 9),
                )
            ],
        ),
        (
            "SELECT @naive_date",
            datetime.date(2016, 12, 5),
            [
                ScalarQueryParameter(
                    name="naive_date", type_="DATE", value=datetime.date(2016, 12, 5)
                )
            ],
        ),
        pytest.param(
            "SELECT @json",
            {"alpha": "abc", "num": [1, 2, 3]},
            [
                ScalarQueryParameter(
                    name="json",
                    type_="JSON",
                    value={"alpha": "abc", "num": [1, 2, 3]},
                )
            ],
            id="scalar-json",
        ),
        (
            "SELECT @naive_time",
            datetime.time(12, 41, 9, 62500),
            [
                ScalarQueryParameter(
                    name="naive_time",
                    type_="TIME",
                    value=datetime.time(12, 41, 9, 62500),
                )
            ],
        ),
        (
            "SELECT @zoned",
            datetime.datetime(2016, 12, 5, 12, 41, 9, tzinfo=datetime.timezone.utc),
            [
                ScalarQueryParameter(
                    name="zoned",
                    type_="TIMESTAMP",
                    value=datetime.datetime(
                        2016, 12, 5, 12, 41, 9, tzinfo=datetime.timezone.utc
                    ),
                )
            ],
        ),
        (
            "SELECT @array_param",
            [1, 2],
            [
                ArrayQueryParameter(
                    name="array_param", array_type="INT64", values=[1, 2]
                )
            ],
        ),
        (
            "SELECT (@hitchhiker.question, @hitchhiker.answer)",
            ({"_field_1": "What is the answer?", "_field_2": 42}),
            [
                StructQueryParameter(
                    "hitchhiker",
                    ScalarQueryParameter(
                        name="question",
                        type_="STRING",
                        value="What is the answer?",
                    ),
                    ScalarQueryParameter(
                        name="answer",
                        type_="INT64",
                        value=42,
                    ),
                ),
            ],
        ),
        (
            "SELECT "
            "((@rectangle.bottom_right.x - @rectangle.top_left.x) "
            "* (@rectangle.top_left.y - @rectangle.bottom_right.y))",
            100,
            [
                StructQueryParameter(
                    "rectangle",
                    StructQueryParameter(
                        "top_left",
                        ScalarQueryParameter("x", "INT64", 12),
                        ScalarQueryParameter("y", "INT64", 102),
                    ),
                    StructQueryParameter(
                        "bottom_right",
                        ScalarQueryParameter("x", "INT64", 22),
                        ScalarQueryParameter("y", "INT64", 92),
                    ),
                )
            ],
        ),
        (
            "SELECT ?",
            [
                {"name": "Phred Phlyntstone", "age": 32},
                {"name": "Bharney Rhubbyl", "age": 31},
            ],
            [
                ArrayQueryParameter(
                    name=None,
                    array_type="RECORD",
                    values=[
                        StructQueryParameter(
                            None,
                            ScalarQueryParameter(
                                name="name", type_="STRING", value="Phred Phlyntstone"
                            ),
                            ScalarQueryParameter(name="age", type_="INT64", value=32),
                        ),
                        StructQueryParameter(
                            None,
                            ScalarQueryParameter(
                                name="name", type_="STRING", value="Bharney Rhubbyl"
                            ),
                            ScalarQueryParameter(name="age", type_="INT64", value=31),
                        ),
                    ],
                )
            ],
        ),
        (
            "SELECT @empty_array_param",
            [],
            [
                ArrayQueryParameter(
                    name="empty_array_param",
                    values=[],
                    array_type=StructQueryParameterType(
                        ScalarQueryParameterType(name="foo", type_="INT64"),
                        ScalarQueryParameterType(name="bar", type_="STRING"),
                    ),
                )
            ],
        ),
        (
            "SELECT @roles",
            {
                "hero": {"name": "Phred Phlyntstone", "age": 32},
                "sidekick": {"name": "Bharney Rhubbyl", "age": 31},
            },
            [
                StructQueryParameter(
                    "roles",
                    StructQueryParameter(
                        "hero",
                        ScalarQueryParameter(
                            name="name", type_="STRING", value="Phred Phlyntstone"
                        ),
                        ScalarQueryParameter(name="age", type_="INT64", value=32),
                    ),
                    StructQueryParameter(
                        "sidekick",
                        ScalarQueryParameter(
                            name="name", type_="STRING", value="Bharney Rhubbyl"
                        ),
                        ScalarQueryParameter(name="age", type_="INT64", value=31),
                    ),
                ),
            ],
        ),
        (
            "SELECT ?",
            {"friends": ["Jack", "Jill"]},
            [
                StructQueryParameter(
                    None,
                    ArrayQueryParameter(
                        name="friends", array_type="STRING", values=["Jack", "Jill"]
                    ),
                )
            ],
        ),
        (
            "SELECT @range_date",
            {"end": None, "start": datetime.date(2016, 12, 5)},
            [
                RangeQueryParameter(
                    name="range_date",
                    range_element_type="DATE",
                    start=datetime.date(2016, 12, 5),
                )
            ],
        ),
        (
            "SELECT @range_datetime",
            {"end": None, "start": datetime.datetime(2016, 12, 5, 0, 0)},
            [
                RangeQueryParameter(
                    name="range_datetime",
                    range_element_type="DATETIME",
                    start=datetime.datetime(2016, 12, 5),
                )
            ],
        ),
        (
            "SELECT @range_unbounded",
            {"end": None, "start": None},
            [
                RangeQueryParameter(
                    name="range_unbounded",
                    range_element_type="DATETIME",
                )
            ],
        ),
    ),
)


@_QUERY_PARAMETER_CASES
def test_query_parameters(
    bigquery_client, query_api_method, sql, expected, query_parameters
):
    jconfig = bigquery.QueryJobConfig()
    jconfig.query_parameters = query_parameters
    query_job = bigquery_client.query(
        sql,
        job_config=jconfig,
        api_method=query_api_method,
    )
    rows = list(query_job.result())
    assert len(rows) == 1
    assert len(rows[0]) == 1
    assert rows[0][0] == expected


@_QUERY_PARAMETER_CASES
def test_query_parameters_arrow(bigquery_client, sql, expected, query_parameters):
    job_config = bigquery.QueryJobConfig(
        query_parameters=query_parameters, use_query_cache=False
    )
    try:
        rows = bigquery_client.query_and_wait(
            sql,
            job_config=job_config,
            # jobs.query fails unnamed STRUCT fields with a jobInternalError,
            # which job_retry would retry until its deadline.
            job_retry=None,
            query_results_format=enums.QueryResultsFormat.ARROW,
        )
    except exceptions.BadRequest as exc:
        if not any(error.get("reason") == "jobInternalError" for error in exc.errors):
            raise
        pytest.xfail(f"jobs.query can't send unnamed STRUCT fields: {exc.message}")
    (batch,) = rows.to_arrow_iterable()
    assert batch.num_rows == 1
    assert batch.num_columns == 1
    (value,) = batch.column(0).to_pylist()
    if batch.schema.field(0).metadata == {
        b"ARROW:extension:name": b"google:sqlType:json"
    }:
        value = json.loads(value)
    assert value == expected


def test_dry_run(
    bigquery_client: bigquery.Client,
    query_api_method: str,
    scalars_table_multi_location: Tuple[str, str],
):
    location, full_table_id = scalars_table_multi_location
    query_config = bigquery.QueryJobConfig()
    query_config.dry_run = True

    query_string = f"SELECT * FROM {full_table_id}"
    query_job = bigquery_client.query(
        query_string,
        location=location,
        job_config=query_config,
        api_method=query_api_method,
    )

    # Note: `query_job.result()` is not necessary on a dry run query. All
    # necessary information is returned in the initial response.
    assert query_job.dry_run is True
    assert query_job.total_bytes_processed > 0
    assert len(query_job.schema) > 0


def test_query_error_w_api_method_query(bigquery_client: bigquery.Client):
    """No job is returned from jobs.query if the query fails."""

    with pytest.raises(exceptions.NotFound, match="not_a_real_dataset"):
        bigquery_client.query(
            "SELECT * FROM not_a_real_dataset.doesnt_exist", api_method="QUERY"
        )


def test_query_error_w_api_method_default(bigquery_client: bigquery.Client):
    """Test that an exception is not thrown until fetching the results.

    For backwards compatibility, jobs.insert is the default API method. With
    jobs.insert, a failed query job is "successfully" created. An exception is
    thrown when fetching the results.
    """

    query_job = bigquery_client.query("SELECT * FROM not_a_real_dataset.doesnt_exist")

    with pytest.raises(exceptions.NotFound, match="not_a_real_dataset"):
        query_job.result()


def test_session(bigquery_client: bigquery.Client, query_api_method: str):
    initial_config = bigquery.QueryJobConfig()
    initial_config.create_session = True
    initial_query = """
    CREATE TEMPORARY TABLE numbers(id INT64)
    AS
    SELECT * FROM UNNEST([1, 2, 3, 4, 5]) AS id;
    """
    initial_job = bigquery_client.query(
        initial_query, job_config=initial_config, api_method=query_api_method
    )
    initial_job.result()
    session_id = initial_job.session_info.session_id
    assert session_id is not None

    second_config = bigquery.QueryJobConfig()
    second_config.connection_properties = [
        bigquery.ConnectionProperty("session_id", session_id),
    ]
    second_job = bigquery_client.query(
        "SELECT COUNT(*) FROM numbers;", job_config=second_config
    )
    rows = list(second_job.result())

    assert len(rows) == 1
    assert rows[0][0] == 5


def test_query_picosecond(bigquery_client: bigquery.Client):
    try:
        job = bigquery_client.query(
            "SELECT CAST('2025-10-20' AS TIMESTAMP(12));",
            api_method="QUERY",
            timestamp_precision=enums.TimestampPrecision.PICOSECOND,
        )
    except exceptions.BadRequest as exc:
        if "timestamp_output_format" in str(exc):
            pytest.skip(
                "Timestamp output format not supported or parameter invalid for this environment"
            )
        raise exc

    result = job.result()
    rows = list(result)
    assert rows[0][0] == "2025-10-20T00:00:00.000000000000Z"
