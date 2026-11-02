# Configuring Timeouts and Retries

When using object methods which invoke Google Cloud Storage API methods,
you have several options for how the library handles timeouts and
how it retries transient errors.

## Configuring Timeouts

For a number of reasons, methods which invoke API methods may take
longer than expected or desired.  By default, such methods all time out
after a default interval, 60.0 seconds.  Rather than blocking your application
code for that interval, you may choose to configure explicit timeouts
in your code, using one of three forms:


* You can pass a single integer or float which functions as the timeout for the
entire request. E.g.:

```python
bucket = client.get_bucket(BUCKET_NAME, timeout=300.0)  # five minutes
```


* You can also be passed as a two-tuple, `(connect_timeout, read_timeout)`,
where the `connect_timeout` sets the maximum time required to establish
the connection to the server, and the `read_timeout` sets the maximum
time to wait for a completed response.  E.g.:

```python
bucket = client.get_bucket(BUCKET_NAME, timeout=(3, 10))
```


* You can also pass `None` as the timeout value:  in this case, the library
will block indefinitely for a response.  E.g.:

```python
bucket = client.get_bucket(BUCKET_NAME, timeout=None)
```

**NOTE**: Depending on the retry strategy, a request may be
repeated several times using the same timeout each time.

See also:

> [Timeouts in requests](https://requests.readthedocs.io/en/latest/user/advanced/#timeouts)

## Configuring Retries

**NOTE**: For more background on retries, see also the
[GCS Retry Strategies Document](https://cloud.google.com/storage/docs/retry-strategy#python)

Methods which invoke API methods may fail for a number of reasons, some of
which represent “transient” conditions, and thus can be retried
automatically.  The library tries to provide a sensible default retry policy
for each method, base on its semantics:


* For API requests which are always idempotent, the library uses its
[`DEFAULT_RETRY`](retry.md#google.cloud.storage.retry.DEFAULT_RETRY) policy, which
retries any API request which returns a “transient” error.


* For API requests which are idempotent only if the blob has
the same “generation”, the library uses its
[`DEFAULT_RETRY_IF_GENERATION_SPECIFIED`](retry.md#google.cloud.storage.retry.DEFAULT_RETRY_IF_GENERATION_SPECIFIED)
policy, which retries API requests which returns a “transient” error,
but only if the original request includes a `generation` or
`ifGenerationMatch` header.


* For API requests which are idempotent only if the bucket or blob has
the same “metageneration”, the library uses its
[`DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED`](retry.md#google.cloud.storage.retry.DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED)
policy, which retries API requests which returns a “transient” error,
but only if the original request includes an `ifMetagenerationMatch` header.


* For API requests which are idempotent only if the bucket or blob has
the same “etag”, the library uses its
[`DEFAULT_RETRY_IF_ETAG_IN_JSON`](retry.md#google.cloud.storage.retry.DEFAULT_RETRY_IF_ETAG_IN_JSON)
policy, which retries API requests which returns a “transient” error,
but only if the original request includes an `ETAG` in its payload.


* For those API requests which are never idempotent, the library passes
`retry=None` by default, suppressing any retries.

Rather than using one of the default policies, you may choose to configure an
explicit policy in your code.


* You can pass `None` as a retry policy to disable retries.  E.g.:

```python
bucket = client.get_bucket(BUCKET_NAME, retry=None)
```


* You can modify the default retry behavior and create a copy of [`DEFAULT_RETRY`](retry.md#google.cloud.storage.retry.DEFAULT_RETRY)
by calling it with a `with_XXX` method. E.g.:

```python
from google.cloud.storage.retry import DEFAULT_RETRY

# Customize retry with a deadline of 500 seconds (default=120 seconds).
modified_retry = DEFAULT_RETRY.with_deadline(500.0)
# Customize retry with an initial wait time of 1.5 (default=1.0).
# Customize retry with a wait time multiplier per iteration of 1.2 (default=2.0).
# Customize retry with a maximum wait time of 45.0 (default=60.0).
modified_retry = modified_retry.with_delay(initial=1.5, multiplier=1.2, maximum=45.0)
```


* You can pass an instance of [`google.api_core.retry.Retry`](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry) to enable
retries;  the passed object will define retriable response codes and errors,
as well as configuring backoff and retry interval options.  E.g.:

```python
from google.api_core import exceptions
from google.api_core.retry import Retry

_MY_RETRIABLE_TYPES = [
   exceptions.TooManyRequests,  # 429
   exceptions.InternalServerError,  # 500
   exceptions.BadGateway,  # 502
   exceptions.ServiceUnavailable,  # 503
]

def is_retryable(exc):
    return isinstance(exc, _MY_RETRIABLE_TYPES)

my_retry_policy = Retry(predicate=is_retryable)
bucket = client.get_bucket(BUCKET_NAME, retry=my_retry_policy)
```


* You can pass an instance of
[`google.cloud.storage.retry.ConditionalRetryPolicy`](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy), which wraps a
`RetryPolicy`, activating it only if
certain conditions are met. This class exists to provide safe defaults
for RPC calls that are not technically safe to retry normally (due to
potential data duplication or other side-effects) but become safe to retry
if a condition such as if_metageneration_match is set.  E.g.:

```python
from google.api_core.retry import Retry
from google.cloud.storage.retry import ConditionalRetryPolicy
from google.cloud.storage.retry import is_etag_in_data

def is_retryable(exc):
    ... # as above

my_retry_policy = Retry(predicate=is_retryable)
my_cond_policy = ConditionalRetryPolicy(
    my_retry_policy, conditional_predicate=is_etag_in_data, ["query_params"])
bucket = client.get_bucket(BUCKET_NAME, retry=my_cond_policy)
```
