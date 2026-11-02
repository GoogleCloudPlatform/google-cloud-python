.. _reader:

Reading Tables
==============

Use the :func:`pandas_gbq.read_gbq` function to run a BigQuery query and
download the results as a :class:`pandas.DataFrame` object.

.. literalinclude:: samples/snippets/read_gbq_simple.py
   :language: python
   :dedent: 4
   :start-after: [S bigquery_pandas_gbq_read_gbq_simple]
   :end-before: [E bigquery_pandas_gbq_read_gbq_simple]

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
       col_order=['col1', 'col2', 'col3'])

Querying with legacy SQL syntax
-------------------------------

The ``dialect`` argument can be used to indicate whether to use
BigQuery's ``'legacy'`` SQL or BigQuery's ``'standard'`` SQL. The
default value is ``'standard'``.

.. literalinclude:: samples/snippets/read_gbq_legacy.py
   :language: python
   :dedent: 4
   :start-after: [S bigquery_pandas_gbq_read_gbq_legacy]
   :end-before: [E bigquery_pandas_gbq_read_gbq_legacy]

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
DATE               datetime64[ns]
DATETIME           datetime64[ns]
BOOL               boolean
FLOAT              float
INT64              Int64
TIME               datetime64[ns]
TIMESTAMP          :class:`~pandas.DatetimeTZDtype` with ``unit='ns'`` and ``tz='UTC'``
================== =========================

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

   With conda:

   .. code-block:: sh

      conda install -c conda-forge google-cloud-bigquery-storage
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
