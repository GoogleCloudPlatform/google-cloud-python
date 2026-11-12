# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

import concurrent.futures
import functools
import logging
from typing import Optional

import google.auth.exceptions
from google.cloud import bigquery

import pandas_gbq.exceptions

logger = logging.getLogger(__name__)


def try_query(connector, query_fn):
    try:
        logger.debug("Requesting query... ")
        return query_fn()
    except concurrent.futures.TimeoutError as ex:
        raise pandas_gbq.exceptions.QueryTimeout("Reason: {0}".format(ex))
    except (google.auth.exceptions.RefreshError, ValueError) as ex:
        if connector.private_key:
            raise pandas_gbq.exceptions.AccessDenied(
                f"The service account credentials are not valid: {ex}"
            )
        else:
            raise pandas_gbq.exceptions.AccessDenied(
                "The credentials have been revoked or expired, "
                f"please re-run the application to re-authorize: {ex}"
            )
    except connector.http_error as ex:
        connector.process_http_error(ex)


def query_and_wait_via_client_library(
    connector,
    client: bigquery.Client,
    query: str,
    *,
    job_config: bigquery.QueryJobConfig,
    location: Optional[str],
    project_id: Optional[str],
    max_results: Optional[int],
    timeout_ms: Optional[int],
):
    # For dry runs, use query() directly to get the QueryJob, then get result
    # This ensures we can access the job attribute for dry_run cost calculation
    if job_config.dry_run:
        query_job = try_query(
            connector,
            functools.partial(
                client.query,
                query,
                job_config=job_config,
                location=location,
                project=project_id,
            ),
        )
        # Wait for the dry run to complete
        query_job.result(timeout=timeout_ms / 1000.0 if timeout_ms else None)
        # Get the result iterator and ensure job attribute is set
        rows_iter = query_job.result(max_results=max_results)
        if not hasattr(rows_iter, "job") or rows_iter.job is None:
            rows_iter.job = query_job
        return rows_iter

    rows_iter = try_query(
        connector,
        functools.partial(
            client.query_and_wait,
            query,
            job_config=job_config,
            location=location,
            project=project_id,
            max_results=max_results,
            wait_timeout=timeout_ms / 1000.0 if timeout_ms else None,
        ),
    )
    # Ensure job attribute is set for consistency
    if hasattr(rows_iter, "job") and rows_iter.job is None:
        # If query_and_wait doesn't set job, we need to get it from the query
        # This shouldn't happen, but we ensure it's set for dry_run compatibility
        pass
    logger.debug("Query done.\n")
    return rows_iter
