# Design of query retries in the BigQuery client libraries for Python


## Overview

The BigQuery client libraries for Python must safely retry API requests related to initiating a query. By "safely", it is meant that the BigQuery backend never successfully executes the query twice. This avoids duplicated rows from INSERT DML queries, among other problems.

To achieve this goal, the client library only retries an API request relating to queries if at least one of the following is true: (1) issuing this exact request is idempotent, meaning that it won't result in a duplicate query being issued, or (2) the query has already failed in such a way that it is safe to re-issue the query.


## Background


### API-level retries

Retries for nearly all API requests were [added in 2017](https://github.com/googleapis/google-cloud-python/pull/4148) and are [configurable via a Retry object](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry) passed to the retry argument. Notably, this includes the "query" method on the Python client, corresponding to the [jobs.insert REST API method](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert). The Python client always populates the [jobReference.jobId](https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference#FIELDS.job_id) field of the request body. If the BigQuery REST API receives a jobs.insert request for a job with the same ID, the REST API fails because the job already exists.


### jobs.insert and jobs.query API requests

By default, the Python client starts a query using the [jobs.insert REST API
method](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert).
Support for the [jobs.query REST API
method](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query)
was [added via the `api_method`
parameter](https://github.com/googleapis/python-bigquery/pull/967) and is
included in version 3.0 of the Python client library.

The jobs.query REST API method differs from jobs.insert in that it does not accept a job ID. Instead, the [requestId parameter](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#QueryRequest.FIELDS.request_id) provides a window of idempotency for duplicate requests.


### Re-issuing a query

The ability to re-issue a query automatically was a [long](https://github.com/googleapis/google-cloud-python/issues/5555) [requested](https://github.com/googleapis/python-bigquery/issues/14) [feature](https://github.com/googleapis/python-bigquery/issues/539). As work ramped up on the SQLAlchemy connector, it became clear that this feature was necessary to keep the test suite, which issues hundreds of queries, from being [too flakey](https://github.com/googleapis/python-bigquery-sqlalchemy/issues?q=is%3Aissue+is%3Aclosed+author%3Aapp%2Fflaky-bot+sort%3Acreated-asc).

Retrying a query is not as simple as retrying a single API request. In many
cases the client library does not "know" about a query job failure until it
tries to fetch the query results.  To solve this, the [client re-issues a
query](https://github.com/googleapis/python-bigquery/pull/837) as it was
originally issued only if the query job has failed for a retryable reason.


### getQueryResults error behavior

The client library uses [the jobs.getQueryResults REST API method](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/getQueryResults) to wait for a query to finish. This REST API has a unique behavior in that it translates query job failures into HTTP error status codes. To disambiguate these error responses from one that may have occurred further up the REST API stack (such as from the Google load balancer), the client library inspects the error response body.

When the error corresponds to a query job failure, BigQuery populates the
"errors" array field, with the first element in the list corresponding to the
error which directly caused the job failure. There are many [error response
messages](https://cloud.google.com/bigquery/docs/error-messages), but only some
of them indicate that re-issuing the query job may help. For example, if the
job fails due to invalid query syntax, re-issuing the query won't help. If a
query job fails due to "backendError" or "rateLimitExceeded", we know that the
job did not successfully execute for some other reason.


## Detailed design

As mentioned in the "Overview" section, the Python client only retries a query request if at least one of the following is true: (1) issuing this exact request is idempotent, meaning that it won't result in a duplicate query being issued, or (2) the query has already failed in such a way that it is safe to re-issue the query.

A developer can configure when to retry an API request (corresponding to #1 "issuing this exact request is idempotent") via the query method's `retry` parameter. A developer can configure when to re-issue a query job after a job failure (corresponding to #2 "the query has already failed") via the query method's `job_retry` parameter.


### Retrying API requests via the `retry` parameter

The first set of retries are at the API layer. The client library sends an
identical request if the request is idempotent.

#### Retrying the jobs.insert API via the retry parameter

When the `api_method` parameter is set to `"INSERT"`, which is the default
value, the client library uses the jobs.insert REST API to start a query job.
Before it issues this request, it sets a job ID. This job ID remains constant
across API retries.

If the job ID was randomly generated, and the jobs.insert request and all retries fail, the client library sends a request to the jobs.get API. This covers the case when a query request succeeded, but there was a transient issue that prevented the client from receiving a successful response. Note: `jobs.get` requires the location of the query. It will fail with 404 if the location is not specified and the job is not in the US multi-region.


#### Retrying the jobs.query API via the retry parameter

When the `api_method` parameter is set to `"QUERY"` (available in version 3 of
the client library), the client library sends a request to the jobs.query REST
API. The client library automatically populates the `requestId` parameter in
the request body. The `requestId` remains constant across API retries, ensuring
that requests are idempotent.

As there is no job ID available, the client library cannot call jobs.get if the query happened to succeed, but all retries resulted in an error response. In this case, the client library throws an exception.


#### Retrying the jobs.getQueryResults API via the retry parameter

The jobs.getQueryResults REST API is read-only. Thus, it is always safe to
retry. As noted in the "Background" section, HTTP error response codes can
indicate that the job itself has failed, so this may retry more often than is
strictly needed 
([Issue #1122](https://github.com/googleapis/python-bigquery/issues/1122)
has been opened to investigate this).


### Re-issuing queries via the `job_retry` parameter

The first set of retries are at the "job" layer, called "re-issue" in this
document. The client library sends an identical query request (except for the
job or request identifier) if the query job has failed for a re-issuable reason.


#### Deciding when it is safe to re-issue a query

The conditions when it is safe to re-issue a query are different from the conditions when it is safe to retry an individual API request. As such, the `job_retry` parameter is provided to configure this behavior.

The `job_retry` parameter is only used if (1) a query job fails and (2) a job ID is not provided by the developer. This is because it must generate a new job ID (or request ID, depending on the method used to create the query job) to avoid getting the same failed job.

The `job_retry` parameter logic only happens after the client makes a request to the `jobs.getQueryRequest` REST API, which fails. The client examines the exception to determine if this failure was caused by a failed job and that the failure reason (e.g. "backendError" or "rateLimitExceeded") indicates that re-issuing the query may help.

If it is determined that the query job can be re-issued safely, the original logic to issue the query is executed. If the jobs.insert REST API was originally used, a new job ID is generated. Otherwise, if the jobs.query REST API was originally used, a new request ID is generated. All other parts of the request body remain identical to the original request body for the failed query job, and the process repeats until `job_retry` is exhausted.
