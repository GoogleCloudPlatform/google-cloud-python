.. _reader:

Reading Tables
==============

Use the :func:`pandas_gbq.read_gbq` function to run a BigQuery query and
download the results as a :class:`pandas.DataFrame` object.

.. code-block:: python

    import pandas_gbq

    # TODO: Set project_id to your Google Cloud Platform project ID.
    # project_id = "my-project"

    sql = """
    SELECT country_name, alpha_2_code
    FROM `bigquery-public-data.utility_us.country_code_iso`
    WHERE alpha_2_code LIKE 'A%'
    """
    df = pandas_gbq.read_gbq(sql, project_id=project_id)
    print(df)

.. note::

    A project ID is optional if it can be inferred during authentication, but
    it is required when authenticating with user credentials. You can find
    your project ID in the `Google Cloud console
    <https://console.cloud.google.com>`__.

You can define which column from BigQuery to use as an index in the
destination DataFrame as well as a preferred column order as follows:

.. code-block:: python

   data_frame = pandas_gbq.read_gbq(
       'SELECT * FROM `test_dataset.test_table`',
       project_id=projectid,
       index_col='index_column_name',
       columns=['col1', 'col2'])

Querying with legacy SQL syntax
-------------------------------

The ``dialect`` argument can be used to indicate whether to use
BigQuery's ``'legacy'`` SQL or BigQuery's ``'standard'`` SQL. The
default value is ``'standard'``.

.. code-block:: python

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
    print(df)

* `Standard SQL reference
  <https://cloud.google.com/bigquery/docs/reference/standard-sql/>`__
* `Legacy SQL reference
  <https://cloud.google.com/bigquery/docs/reference/legacy-sql>`__

.. _reading-dtypes:

Inferring the DataFrame's dtypes
--------------------------------

The :func:`~pandas_gbq.read_gbq` method infers the pandas dtype for each
column, based on the BigQuery table schema.

================== =========================
BigQuery Data Type dtype
================== =========================
BOOL               boolean
INT64              Int64
FLOAT64            float64
TIME               dbtime
DATE               dbdate or object
DATETIME           datetime64[ns] or object
TIMESTAMP          datetime64[ns, UTC] or object
================== =========================

If any DATE/DATETIME/TIMESTAMP value is outside of the range of `pandas.Timestamp.min
<https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.min.html>`__
(1677-09-22) and `pandas.Timestamp.max
<https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.max.html>`__
(2262-04-11), the data type maps to the pandas `object` dtype.

.. _reading-bqstorage-api:

Improving download performance
------------------------------

Use the BigQuery Storage API to download large (>125 MB) query results more
quickly (but at an `increased cost
<https://cloud.google.com/bigquery/pricing#storage-api>`__) by setting
``use_bqstorage_api`` to ``True``.

#. Enable the BigQuery Storage API on the project you are using to run
   queries.

   `Enable the API
   <https://console.cloud.google.com/apis/library/bigquerystorage.googleapis.com>`__.
#. Ensure you have the `bigquery.readsessions.create permission
   <https://cloud.google.com/bigquery/docs/access-control#bq-permissions>`__. to
   create BigQuery Storage API read sessions. This permission is provided by
   the `bigquery.user role
   <https://cloud.google.com/bigquery/docs/access-control#roles>`__.
#. Install the ``google-cloud-bigquery-storage`` and ``pyarrow``
    packages.

   With pip:

   .. code-block:: sh

      pip install --upgrade google-cloud-bigquery-storage pyarrow

#. Set ``use_bqstorage_api`` to ``True`` when calling the
   :func:`~pandas_gbq.read_gbq` function. As of the ``google-cloud-bigquery``
   package, version 1.11.1 or later,the function will fallback to the
   BigQuery API if the BigQuery Storage API cannot be used, such as with
   small query results.

Advanced configuration
----------------------

You can specify the query config as parameter to use additional options of
your job. Refer to the `JobConfiguration REST resource reference
<https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfiguration>`__
for details.

.. code-block:: python

   configuration = {
      'query': {
        "useQueryCache": False
      }
   }
   data_frame = read_gbq(
       'SELECT * FROM `test_dataset.test_table`',
       project_id=projectid,
       configuration=configuration)
