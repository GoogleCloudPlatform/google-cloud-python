# Writing Tables

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

The destination table and destination dataset will automatically be created
if they do not already exist.

## Writing to an Existing Table

Use the `if_exists` argument to dictate whether to `'fail'`,
`'replace'` or `'append'` if the destination table already exists. The
default value is `'fail'`.

For example, assume that `if_exists` is set to `'fail'`. The following snippet will raise
a `TableCreationError` if the destination table already exists.

```python
import pandas_gbq
pandas_gbq.to_gbq(
    df, 'my_dataset.my_table', project_id=projectid, if_exists='fail',
)
```

If the `if_exists` argument is set to `'append'`, the destination
dataframe will be written to the table using the defined table schema and
column types. The dataframe must contain fields (matching name and type)
currently in the destination table.

## Inferring the Table Schema

The [`to_gbq()`](api.md#pandas_gbq.to_gbq) method infers the BigQuery table schema based
on the dtypes of the uploaded [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame).

| dtype

 | BigQuery Data Type

 |
| ------------------------------------------- | -------------------------------------------------------- |  |  |  |  |
| i (integer)

                                 | INTEGER

                                                  |
| b (boolean)

                                 | BOOLEAN

                                                  |
| f (float)

                                   | FLOAT

                                                    |
| O (object)

                                  | STRING

                                                   |
| S (zero-terminated bytes)

                   | STRING

                                                   |
| U (Unicode string)

                          | STRING

                                                   |
| M (datetime)

                                | TIMESTAMP

                                                |
If the data type inference does not suit your needs, supply a BigQuery schema
as the `table_schema` parameter of [`to_gbq()`](api.md#pandas_gbq.to_gbq).

## Troubleshooting Errors

If an error occurs while writing data to BigQuery, see
[Troubleshooting BigQuery Errors](https://cloud.google.com/bigquery/troubleshooting-errors).
