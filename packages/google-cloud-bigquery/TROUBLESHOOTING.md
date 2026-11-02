# Troubleshooting steps

## Enable logging of BQ Storage Read API session creation

It can be helpful to get the BQ Storage Read API session to allow the BigQuery
backend team to debug cases of API instability. The logs that share the session
creation are in a module-specific logger. To enable the logs, refer to the
following code sample:

```python
import logging
import google.cloud.bigquery

# Configure the basic logging to show DEBUG level messages
log_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)
handler = logging.StreamHandler()
handler.setFormatter(log_formatter)
default_logger = logging.getLogger()
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(handler)
to_dataframe_logger = logging.getLogger("google.cloud.bigquery._pandas_helpers")
to_dataframe_logger.setLevel(logging.DEBUG)
to_dataframe_logger.addHandler(handler)

# Example code that touches the BQ Storage Read API.
bqclient = google.cloud.bigquery.Client()
results = bqclient.query_and_wait("SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013`")
print(results.to_dataframe().head())
```

In particular, watch for the text "with BQ Storage API session" in the logs
to get the streaming API session ID to share with your support person.
