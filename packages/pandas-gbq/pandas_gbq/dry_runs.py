# Copyright (c) 2025 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

import copy
from typing import Any, List

import pandas
from google.cloud import bigquery


def get_query_stats(
    query_job: bigquery.QueryJob,
) -> pandas.Series:
    """Returns important stats from the query job as a Pandas Series."""

    index: List[Any] = []
    values: List[Any] = []

    # Add raw BQ schema
    index.append("bigquerySchema")
    values.append(query_job.schema)

    job_api_repr = copy.deepcopy(query_job._properties)

    # jobReference might not be populated for "job optional" queries.
    job_ref = job_api_repr.get("jobReference", {})
    for key, val in job_ref.items():
        index.append(key)
        values.append(val)

    configuration = job_api_repr.get("configuration", {})
    index.append("jobType")
    values.append(configuration.get("jobType", None))
    index.append("dispatchedSql")
    values.append(configuration.get("query", {}).get("query", None))

    query_config = configuration.get("query", {})
    for key in ("destinationTable", "useLegacySql"):
        index.append(key)
        values.append(query_config.get(key, None))

    statistics = job_api_repr.get("statistics", {})
    query_stats = statistics.get("query", {})
    for key in (
        "referencedTables",
        "totalBytesProcessed",
        "cacheHit",
        "statementType",
    ):
        index.append(key)
        values.append(query_stats.get(key, None))

    creation_time = statistics.get("creationTime", None)
    index.append("creationTime")
    values.append(
        pandas.Timestamp(creation_time, unit="ms", tz="UTC")
        if creation_time is not None
        else None
    )

    result = pandas.Series(values, index=index)
    if result["totalBytesProcessed"] is None:
        result["totalBytesProcessed"] = 0
    else:
        result["totalBytesProcessed"] = int(result["totalBytesProcessed"])

    return result
