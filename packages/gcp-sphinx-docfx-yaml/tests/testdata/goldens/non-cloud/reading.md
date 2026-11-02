# Reading Tables

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

**NOTE**: A project ID is optional if it can be inferred during authentication, but
it is required when authenticating with user credentials. You can find
your project ID in the [Google Cloud console](https://console.cloud.google.com).

You can define which column from BigQuery to use as an index in the
destination DataFrame as well as a preferred column order as follows:

```python
data_frame = pandas_gbq.read_gbq(
    'SELECT * FROM `test_dataset.test_table`',
    project_id=projectid,
    index_col='index_column_name',
    col_order=['col1', 'col2', 'col3'])
```

## Querying with legacy SQL syntax

The `dialect` argument can be used to indicate whether to use
BigQuery’s `'legacy'` SQL or BigQuery’s `'standard'` SQL. The
default value is `'standard'`.

```python
sql = """
SELECT country_name, alpha_2_code
FROM [bigquery-public-data:utility_us.country_code_iso]
WHERE alpha_2_code LIKE 'Z%'
"""
df = pandas_gbq.read_gbq(
    sql,
    project_id=project_id,
    # Set the dialect to "legacy" to use legacy SQL syntax. As of
    # pandas-gbq version 0.10.0, the default dialect is "standard".
    dialect="legacy",
)
```


* [Standard SQL reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/)


* [Legacy SQL reference](https://cloud.google.com/bigquery/docs/reference/legacy-sql)

## Inferring the DataFrame’s dtypes

The [`read_gbq()`](api.md#pandas_gbq.read_gbq) method infers the pandas dtype for each
column, based on the BigQuery table schema.

| BigQuery Data Type

 | dtype

 |
| ------------------------------------------- | -------------------------------------------------------- |  |  |
| DATE

                                        | datetime64[ns]

                                           |
| DATETIME

                                    | datetime64[ns]

                                           |
| BOOL

                                        | boolean

                                                  |
| FLOAT

                                       | float

                                                    |
| INT64

                                       | Int64

                                                    |
| TIME

                                        | datetime64[ns]

                                           |
| TIMESTAMP

                                   | [`DatetimeTZDtype`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype) with `unit='ns'` and `tz='UTC'`

              |
## Improving download performance

Use the BigQuery Storage API to download large (>125 MB) query results more
quickly (but at an [increased cost](https://cloud.google.com/bigquery/pricing#storage-api)) by setting
`use_bqstorage_api` to `True`.


1. Enable the BigQuery Storage API on the project you are using to run
queries.

[Enable the API](https://console.cloud.google.com/apis/library/bigquerystorage.googleapis.com).


2. Ensure you have the [bigquery.readsessions.create permission](https://cloud.google.com/bigquery/docs/access-control#bq-permissions). to
create BigQuery Storage API read sessions. This permission is provided by
the [bigquery.user role](https://cloud.google.com/bigquery/docs/access-control#roles).


3. Install the `google-cloud-bigquery-storage` and `pyarrow`

    packages.

With pip:

```sh
pip install --upgrade google-cloud-bigquery-storage pyarrow
```

With conda:

```sh
conda install -c conda-forge google-cloud-bigquery-storage
```


4. Set `use_bqstorage_api` to `True` when calling the
[`read_gbq()`](api.md#pandas_gbq.read_gbq) function. As of the `google-cloud-bigquery`
package, version 1.11.1 or later,the function will fallback to the
BigQuery API if the BigQuery Storage API cannot be used, such as with
small query results.

## Advanced configuration

You can specify the query config as parameter to use additional options of
your job. Refer to the [JobConfiguration REST resource reference](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfiguration)
for details.

```python
configuration = {
   'query': {
     "useQueryCache": False
   }
}
data_frame = read_gbq(
    'SELECT * FROM `test_dataset.test_table`',
    project_id=projectid,
    configuration=configuration)
```
