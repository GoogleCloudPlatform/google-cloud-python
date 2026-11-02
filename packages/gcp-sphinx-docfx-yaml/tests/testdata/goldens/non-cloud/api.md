# API Reference

**NOTE**: Only functions and classes which are members of the `pandas_gbq` module
are considered public. Submodules and their members are considered private.

| `read_gbq`(query_or_table[, project_id, ...])

 | Load data from Google BigQuery using google-cloud-python

 |
| `to_gbq`(dataframe, destination_table[, ...])

 | Write a DataFrame to a Google BigQuery table.

            |
| `context`
                                     | Storage for objects to be used throughout a session.

     |
| `Context`()

                                   | Storage for objects to be used throughout a session.

     |

### pandas_gbq.read_gbq(query_or_table, project_id=None, index_col=None, col_order=None, reauth=False, auth_local_webserver=True, dialect=None, location=None, configuration=None, credentials=None, use_bqstorage_api=False, max_results=None, verbose=None, private_key=None, progress_bar_type='tqdm', dtypes=None, auth_redirect_uri=None, client_id=None, client_secret=None)
Load data from Google BigQuery using google-cloud-python

The main method a user calls to execute a Query in Google BigQuery
and read results into a pandas DataFrame.

This method uses the Google Cloud client library to make requests to
Google BigQuery, documented [here](https://googleapis.dev/python/bigquery/latest/index.html).

See the [How to authenticate with Google BigQuery](howto/authentication.md#id1)
guide for authentication instructions.


* **Parameters**

    
    * **query_or_table** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – SQL query to return data values. If the string is a table ID, fetch the
    rows directly from the table without running a query.


    * **project_id** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **optional*) – Google Cloud Platform project ID. Optional when available from
    the environment.


    * **index_col** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **optional*) – Name of result column to use for index in results DataFrame.


    * **col_order** ([*list*](https://python.readthedocs.io/en/latest/library/stdtypes.html#list)*(*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*)**, **optional*) – List of BigQuery column names in the desired order for results
    DataFrame.


    * **reauth** (*boolean**, **default False*) – Force Google BigQuery to re-authenticate the user. This is useful
    if multiple accounts are used.


    * **auth_local_webserver** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*, **default True*) – Use the [local webserver flow](https://googleapis.dev/python/google-auth-oauthlib/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_local_server)
    instead of the [console flow](https://googleapis.dev/python/google-auth-oauthlib/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_console)
    when getting user credentials. Your code must run on the same machine
    as your web browser and your web browser can access your application
    via `localhost:808X`.

    **Versionadded:** New in version 0.2.0.



    * **dialect** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **default 'standard'*) – Note: The default value changed to ‘standard’ in version 0.10.0.

    SQL syntax dialect to use. Value can be one of:

    `'legacy'`

        Use BigQuery’s legacy SQL dialect. For more information see
        [BigQuery Legacy SQL Reference](https://cloud.google.com/bigquery/docs/reference/legacy-sql).

    `'standard'`

        Use BigQuery’s standard SQL, which is
        compliant with the SQL 2011 standard. For more information
        see [BigQuery Standard SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/).



    * **location** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **optional*) – Location where the query job should run. See the [BigQuery locations
    documentation](https://cloud.google.com/bigquery/docs/dataset-locations) for a
    list of available locations. The location must match that of any
    datasets used in the query.

    **Versionadded:** New in version 0.5.0.



    * **configuration** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)*, **optional*) – Query config parameters for job processing.
    For example:

    > configuration = {‘query’: {‘useQueryCache’: False}}

    For more information see [BigQuery REST API Reference](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs#configuration.query).



    * **credentials** ([*google.auth.credentials.Credentials*](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials)*, **optional*) – Credentials for accessing Google APIs. Use this parameter to override
    default credentials, such as to use Compute Engine
    [`google.auth.compute_engine.Credentials`](https://googleapis.dev/python/google-auth/latest/reference/google.auth.compute_engine.html#google.auth.compute_engine.Credentials) or Service Account
    [`google.oauth2.service_account.Credentials`](https://googleapis.dev/python/google-auth/latest/reference/google.oauth2.service_account.html#google.oauth2.service_account.Credentials) directly.

    **Versionadded:** New in version 0.8.0.



    * **use_bqstorage_api** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*, **default False*) – Use the [BigQuery Storage API](https://cloud.google.com/bigquery/docs/reference/storage/) to
    download query results quickly, but at an increased cost. To use this
    API, first [enable it in the Cloud Console](https://console.cloud.google.com/apis/library/bigquerystorage.googleapis.com).
    You must also have the [bigquery.readsessions.create](https://cloud.google.com/bigquery/docs/access-control#roles)
    permission on the project you are billing queries to.

    This feature requires the `google-cloud-bigquery-storage` and
    `pyarrow` packages.

    This value is ignored if `max_results` is set.

    **Versionadded:** New in version 0.10.0.



    * **max_results** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)*, **optional*) – If set, limit the maximum number of rows to fetch from the query
    results.

    **Versionadded:** New in version 0.12.0.



    * **(****Optional****[****str****]****)** (*progress_bar_type*) – If set, use the [tqdm](https://tqdm.github.io/) library to
    display a progress bar while the data downloads. Install the
    `tqdm` package to use this feature.
    Possible values of `progress_bar_type` include:

    `None`

        No progress bar.

    `'tqdm'`

        Use the `tqdm.tqdm()` function to print a progress bar
        to [`sys.stderr`](https://python.readthedocs.io/en/latest/library/sys.html#sys.stderr).

    `'tqdm_notebook'`

        Use the `tqdm.tqdm_notebook()` function to display a
        progress bar as a Jupyter notebook widget.

    `'tqdm_gui'`

        Use the `tqdm.tqdm_gui()` function to display a
        progress bar as a graphical dialog box.



    * **dtypes** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)*, **optional*) – A dictionary of column names to pandas `dtype`. The provided
    `dtype` is used when constructing the series for the column
    specified. Otherwise, a default `dtype` is used.


    * **verbose** (*None**, **deprecated*) – Deprecated in Pandas-GBQ 0.4.0. Use the [logging module
    to adjust verbosity instead](https://pandas-gbq.readthedocs.io/en/latest/intro.html#logging).


    * **private_key** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **deprecated*) – Deprecated in pandas-gbq version 0.8.0. Use the `credentials`
    parameter and
    `google.oauth2.service_account.Credentials.from_service_account_info()`
    or
    `google.oauth2.service_account.Credentials.from_service_account_file()`
    instead.


    * **auth_redirect_uri** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – Path to the authentication page for organization-specific authentication
    workflows. Used when `auth_local_webserver=False`.


    * **client_id** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The Client ID for the Google Cloud Project the user is attempting to
    connect to.


    * **client_secret** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The Client Secret associated with the Client ID for the Google Cloud Project
    the user is attempting to connect to.



* **Returns**

    **df** – DataFrame representing results of query.



* **Return type**

    DataFrame



### pandas_gbq.to_gbq(dataframe, destination_table, project_id=None, chunksize=None, reauth=False, if_exists='fail', auth_local_webserver=True, table_schema=None, location=None, progress_bar=True, credentials=None, api_method: [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str) = 'default', verbose=None, private_key=None, auth_redirect_uri=None, client_id=None, client_secret=None)
Write a DataFrame to a Google BigQuery table.

The main method a user calls to export pandas DataFrame contents to Google BigQuery table.

This method uses the Google Cloud client library to make requests to Google BigQuery, documented [here](https://googleapis.dev/python/bigquery/latest/index.html).

See the [How to authenticate with Google BigQuery](howto/authentication.md#id1)
guide for authentication instructions.


* **Parameters**

    
    * **dataframe** ([*pandas.DataFrame*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame)) – DataFrame to be written to a Google BigQuery table.


    * **destination_table** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – Name of table to be written, in the form `dataset.tablename` or
    `project.dataset.tablename`.


    * **project_id** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **optional*) – Google Cloud Platform project ID. Optional when available from
    the environment.


    * **chunksize** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)*, **optional*) – Number of rows to be inserted in each chunk from the dataframe.
    Set to `None` to load the whole dataframe at once.


    * **reauth** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*, **default False*) – Force Google BigQuery to re-authenticate the user. This is useful
    if multiple accounts are used.


    * **if_exists** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **default 'fail'*) – Behavior when the destination table exists. Value can be one of:

    `'fail'`

        If table exists, do nothing.

    `'replace'`

        If table exists, drop it, recreate it, and insert data.

    `'append'`

        If table exists, insert data. Create if does not exist.



    * **auth_local_webserver** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*, **default True*) – Use the [local webserver flow](https://googleapis.dev/python/google-auth-oauthlib/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_local_server)
    instead of the [console flow](https://googleapis.dev/python/google-auth-oauthlib/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_console)
    when getting user credentials. Your code must run on the same machine
    as your web browser and your web browser can access your application
    via `localhost:808X`.

    **Versionadded:** New in version 0.2.0.



    * **table_schema** (*list of dicts**, **optional*) – List of BigQuery table fields to which according DataFrame
    columns conform to, e.g. `[{'name': 'col1', 'type':
    'STRING'},...]`.  The `type` values must be BigQuery type names.


        * If `table_schema` is provided, it may contain all or a subset of
    DataFrame columns. If a subset is provided, the rest will be
    inferred from the DataFrame dtypes.  If `table_schema` contains
    columns not in the DataFrame, they’ll be ignored.


        * If `table_schema` is **not** provided, it will be
    generated according to dtypes of DataFrame columns. See
    [Inferring the Table Schema](https://pandas-gbq.readthedocs.io/en/latest/writing.html#writing-schema).
    for a description of the schema inference.

    See BigQuery API documentation on valid column names
    <https://cloud.google.com/bigquery/docs/schemas#column_names>__.

    **Versionadded:** New in version 0.3.1.



    * **location** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **optional*) – Location where the load job should run. See the [BigQuery locations
    documentation](https://cloud.google.com/bigquery/docs/dataset-locations) for a
    list of available locations. The location must match that of the
    target dataset.

    **Versionadded:** New in version 0.5.0.



    * **progress_bar** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*, **default True*) – Use the library tqdm to show the progress bar for the upload,
    chunk by chunk.

    **Versionadded:** New in version 0.5.0.



    * **credentials** ([*google.auth.credentials.Credentials*](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials)*, **optional*) – Credentials for accessing Google APIs. Use this parameter to override
    default credentials, such as to use Compute Engine
    [`google.auth.compute_engine.Credentials`](https://googleapis.dev/python/google-auth/latest/reference/google.auth.compute_engine.html#google.auth.compute_engine.Credentials) or Service Account
    [`google.oauth2.service_account.Credentials`](https://googleapis.dev/python/google-auth/latest/reference/google.oauth2.service_account.html#google.oauth2.service_account.Credentials) directly.

    **Versionadded:** New in version 0.8.0.



    * **api_method** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **optional*) – API method used to upload DataFrame to BigQuery. One of “load_parquet”,
    “load_csv”. Default “load_parquet” if pandas is version 1.1.0+,
    otherwise “load_csv”.

    **Versionadded:** New in version 0.16.0.



    * **verbose** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*, **deprecated*) – Deprecated in Pandas-GBQ 0.4.0. Use the [logging module
    to adjust verbosity instead](https://pandas-gbq.readthedocs.io/en/latest/intro.html#logging).


    * **private_key** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **deprecated*) – Deprecated in pandas-gbq version 0.8.0. Use the `credentials`
    parameter and
    `google.oauth2.service_account.Credentials.from_service_account_info()`
    or
    `google.oauth2.service_account.Credentials.from_service_account_file()`
    instead.


    * **auth_redirect_uri** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – Path to the authentication page for organization-specific authentication
    workflows. Used when `auth_local_webserver=False`.


    * **client_id** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The Client ID for the Google Cloud Project the user is attempting to
    connect to.


    * **client_secret** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The Client Secret associated with the Client ID for the Google Cloud Project
    the user is attempting to connect to.



### pandas_gbq.context(_ = <pandas_gbq.gbq.Context object_ )
Storage for objects to be used throughout a session.

A Context object is initialized when the `pandas_gbq` module is
imported, and can be found at `pandas_gbq.context`.


### _class_ pandas_gbq.Context()
Storage for objects to be used throughout a session.

A Context object is initialized when the `pandas_gbq` module is
imported, and can be found at `pandas_gbq.context`.


#### _property_ credentials()
Credentials to use for Google APIs.

These credentials are automatically cached in memory by calls to
`pandas_gbq.read_gbq()` and `pandas_gbq.to_gbq()`. To
manually set the credentials, construct an
[`google.auth.credentials.Credentials`](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials) object and set it as
the context credentials as demonstrated in the example below. See
[auth docs](http://google-auth.readthedocs.io/en/latest/user-guide.html#obtaining-credentials) for more information on obtaining credentials.


* **Return type**

    [google.auth.credentials.Credentials](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials)


### Examples

Manually setting the context credentials:

```python
>>> import pandas_gbq
>>> from google.oauth2 import service_account
>>> credentials = service_account.Credentials.from_service_account_file(
...     '/path/to/key.json',
... )
>>> pandas_gbq.context.credentials = credentials
```


#### _property_ dialect()
Default dialect to use in `pandas_gbq.read_gbq()`.

Allowed values for the BigQuery SQL syntax dialect:

`'legacy'`

    Use BigQuery’s legacy SQL dialect. For more information see
    [BigQuery Legacy SQL Reference](https://cloud.google.com/bigquery/docs/reference/legacy-sql).

`'standard'`

    Use BigQuery’s standard SQL, which is
    compliant with the SQL 2011 standard. For more information
    see [BigQuery Standard SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/).


* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)


### Examples

Setting the default syntax to standard:

```python
>>> import pandas_gbq
>>> pandas_gbq.context.dialect = 'standard'
```


#### _property_ project()
Default project to use for calls to Google APIs.


* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)


### Examples

Manually setting the context project:

```python
>>> import pandas_gbq
>>> pandas_gbq.context.project = 'my-project'
```
