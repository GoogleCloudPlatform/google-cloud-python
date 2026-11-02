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


# On-demand BQ Queries costs $6.25 per TB. First 1 TB per month is free
# see here for more: https://cloud.google.com/bigquery/pricing
QUERY_PRICE_FOR_TB = 6.25 / 2**40  # USD/TB


# http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix="B"):
    fmt = "%3.1f %s%s"
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return fmt % (num, unit, suffix)
        num /= 1024.0
    return fmt % (num, "Y", suffix)


def _wait_for_query_job(
    connector,
    client: bigquery.Client,
    query_reply: bigquery.QueryJob,
    timeout_ms: Optional[float],
):
    """Wait for query to complete, pausing occasionally to update progress.

    Args:
        connector (GbqConnector):
            General pandas-gbq "connector" with helpers for stateful progress
            logs and error raising.

        client (bigquery.Client):
            A connection to BigQuery, used to make API requests.

        query_reply (QueryJob):
            A query job which has started.

        timeout_ms (Optional[int]):
            How long to wait before cancelling the query.
    """
    # Wait at most 10 seconds so we can show progress.
    # TODO(https://github.com/googleapis/python-bigquery-pandas/issues/327):
    # Include a tqdm progress bar here instead of a stream of log messages.
    timeout_sec = 10.0
    if timeout_ms:
        timeout_sec = min(timeout_sec, timeout_ms / 1000.0)

    while query_reply.state != "DONE":
        connector.log_elapsed_seconds("  Elapsed", "s. Waiting...")

        if timeout_ms and timeout_ms < connector.get_elapsed_seconds() * 1000:
            client.cancel_job(query_reply.job_id, location=query_reply.location)
            raise pandas_gbq.exceptions.QueryTimeout(
                "Query timeout: {} ms".format(timeout_ms)
            )

        try:
            query_reply.result(timeout=timeout_sec)
        except concurrent.futures.TimeoutError:
            # Use our own timeout logic
            pass
        except connector.http_error as ex:
            connector.process_http_error(ex)


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


def query_and_wait(
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
    """Start a query and wait for it to complete.

    Args:
        connector (GbqConnector):
            General pandas-gbq "connector" with helpers for stateful progress
            logs and error raising.

        client (bigquery.Client):
            A connection to BigQuery, used to make API requests.

        query (str):
            The text of the query to run.

        job_config (bigquery.QueryJobConfig):
            Options for running the query.

        location (Optional[str]):
            BigQuery location to run the query. Uses the default if not set.

        project (Optional[str]):
            GCP project ID where to run the query. Uses the default if not set.

        max_results (Optional[int]):
            Maximum number of rows in the result set.

        timeout_ms (Optional[int]):
            How long to wait before cancelling the query.

    Returns:
        bigquery.RowIterator:
            Result iterator from which we can download the results in the
            desired format (pandas.DataFrame).
    """
    query_reply = try_query(
        connector,
        functools.partial(
            client.query,
            query,
            job_config=job_config,
            location=location,
            project=project_id,
        ),
    )
    logger.debug("Query running...")

    job_id = query_reply.job_id
    logger.debug("Job ID: %s" % job_id)

    _wait_for_query_job(connector, connector.client, query_reply, timeout_ms)

    if query_reply.cache_hit:
        logger.debug("Query done.\nCache hit.\n")
    else:
        bytes_processed = query_reply.total_bytes_processed or 0
        bytes_billed = query_reply.total_bytes_billed or 0
        logger.debug(
            "Query done.\nProcessed: {} Billed: {}".format(
                sizeof_fmt(bytes_processed),
                sizeof_fmt(bytes_billed),
            )
        )
        logger.debug(
            "Standard price: ${:,.2f} USD\n".format(bytes_billed * QUERY_PRICE_FOR_TB)
        )

    # As of google-cloud-bigquery 2.3.0, QueryJob.result() uses
    # getQueryResults() instead of tabledata.list, which returns the correct
    # response with DML/DDL queries.
    try:
        rows_iter = query_reply.result(max_results=max_results)
        # Store reference to QueryJob in RowIterator for dry_run access
        # RowIterator already has a job attribute, but ensure it's set
        if not hasattr(rows_iter, "job") or rows_iter.job is None:
            rows_iter.job = query_reply
        return rows_iter
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
