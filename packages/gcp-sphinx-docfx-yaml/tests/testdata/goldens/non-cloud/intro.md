# Introduction

The pandas-gbq package reads data from [Google BigQuery](https://cloud.google.com/bigquery/docs/) to a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame)
object and also writes [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) objects to BigQuery tables.

## Authenticating to BigQuery

Before you begin, you must create a Google Cloud Platform project. Use the
[BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox) to try
the service for free.

If you do not provide any credentials, this module attempts to load
credentials from the environment. If no credentials are found, pandas-gbq
prompts you to open a web browser, where you can grant it permissions to
access your cloud resources. These credentials are only used locally. See the
[privacy policy](privacy.md) for details.

Learn about authentication methods in the [authentication guide](howto/authentication.md).

## Reading data from BigQuery

Use the [`pandas_gbq.read_gbq()`](api.md#pandas_gbq.read_gbq) function to run a BigQuery query and
download the results as a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) object.

```python
import pandas_gbq

# TODO: Set project_id to your Google Cloud Platform project ID.
# project_id = "my-project"

sql = """
SELECT country_name, alpha_2_code
FROM `bigquery-public-data.utility_us.country_code_iso`
WHERE alpha_2_code LIKE 'A%'
"""
df = pandas_gbq.read_gbq(sql, project_id=project_id)
```

By default, queries use standard SQL syntax. Visit the [reading tables
guide](reading.md) to learn about the available options.

### Adjusting log vebosity

Because some requests take some time, this library will log its progress of
longer queries. IPython & Jupyter by default attach a handler to the logger.
If you’re running in another process and want to see logs, or you want to see
more verbose logs, you can do something like:

```python
import logging
logger = logging.getLogger('pandas_gbq')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
```

## Writing data to BigQuery

Use the [`pandas_gbq.to_gbq()`](api.md#pandas_gbq.to_gbq) function to write a
[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) object to a BigQuery table.

```python
import pandas
import pandas_gbq

# TODO: Set project_id to your Google Cloud Platform project ID.
# project_id = "my-project"

# TODO: Set table_id to the full destination table ID (including the
#       dataset ID).
# table_id = 'my_dataset.my_table'

df = pandas.DataFrame(
    {
        "my_string": ["a", "b", "c"],
        "my_int64": [1, 2, 3],
        "my_float64": [4.0, 5.0, 6.0],
        "my_bool1": [True, False, True],
        "my_bool2": [False, True, False],
        "my_dates": pandas.date_range("now", periods=3),
    }
)

pandas_gbq.to_gbq(df, table_id, project_id=project_id)
```

The destination table and destination dataset will automatically be created.
By default, writes to BigQuery fail if the table already exists. Visit the
[writing tables guide](writing.md) to learn about the available options.
