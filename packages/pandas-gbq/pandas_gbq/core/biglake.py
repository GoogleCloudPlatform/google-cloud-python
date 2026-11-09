# Copyright (c) 2026 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""
Utilities for working with BigLake tables.
"""

# TODO(tswast): Synchronize with bigframes/session/iceberg.py, which uses
# pyiceberg and the BigLake APIs, rather than relying on dry run.

from __future__ import annotations

import dataclasses
from typing import Sequence

import google.cloud.bigquery

import pandas_gbq.core.resource_references

_DRY_RUN_TEMPLATE = """
SELECT *
FROM `{project}.{catalog}.{namespace}.{table}`
"""


_COUNT_TEMPLATE = """
SELECT COUNT(*) as total_rows
FROM `{project}.{catalog}.{namespace}.{table}`
"""


@dataclasses.dataclass(frozen=True)
class BigLakeTableMetadata:
    schema: Sequence[google.cloud.bigquery.SchemaField]
    num_rows: int


def get_table_metadata(
    *,
    reference: pandas_gbq.core.resource_references.BigLakeTableId,
    bqclient: google.cloud.bigquery.Client,
) -> BigLakeTableMetadata:
    """
    Get the schema for a BigLake table.

    Currently, this does some BigQuery queries. In the future, we'll want to get
    other metadata like the number of rows and storage bytes so that we can do a
    more accurate estimate of how many rows to sample.
    """
    dry_run_config = google.cloud.bigquery.QueryJobConfig(dry_run=True)
    query = _DRY_RUN_TEMPLATE.format(
        project=reference.project,
        catalog=reference.catalog,
        namespace=".".join(reference.namespace),
        table=reference.table,
    )
    job = bqclient.query(query, job_config=dry_run_config)
    job.result()
    schema = job.schema

    count_rows = list(
        bqclient.query_and_wait(
            _COUNT_TEMPLATE.format(
                project=reference.project,
                catalog=reference.catalog,
                namespace=".".join(reference.namespace),
                table=reference.table,
            )
        )
    )
    assert (
        len(count_rows) == 1
    ), "got unexpected query response when determining number of rows"
    total_rows = count_rows[0].total_rows

    return BigLakeTableMetadata(
        schema=schema if schema is not None else [],
        num_rows=total_rows,
    )
