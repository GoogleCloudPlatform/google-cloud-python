Introduction
============

The pandas-gbq package reads data from `Google BigQuery
<https://cloud.google.com/bigquery/docs/>`__ to a :class:`pandas.DataFrame`
object and also writes :class:`pandas.DataFrame` objects to BigQuery tables.

Authenticating to BigQuery
--------------------------

Before you begin, you must create a Google Cloud Platform project. Use the
`BigQuery sandbox <https://cloud.google.com/bigquery/docs/sandbox>`__ to try
the service for free.

If you do not provide any credentials, this module attempts to load
credentials from the environment. If no credentials are found, pandas-gbq
prompts you to open a web browser, where you can grant it permissions to
access your cloud resources. These credentials are only used locally. See the
:doc:`privacy policy <privacy>` for details.

Learn about authentication methods in the :doc:`authentication guide
<howto/authentication>`.

Reading data from BigQuery
--------------------------

Use the :func:`pandas_gbq.read_gbq` function to run a BigQuery query and
download the results as a :class:`pandas.DataFrame` object.

.. literalinclude:: samples/snippets/read_gbq_simple.py
   :language: python
   :dedent: 4
   :start-after: [S bigquery_pandas_gbq_read_gbq_simple]
   :end-before: [E bigquery_pandas_gbq_read_gbq_simple]

By default, queries use standard SQL syntax. Visit the :doc:`reading tables
guide <reading>` to learn about the available options.

Adjusting log vebosity
^^^^^^^^^^^^^^^^^^^^^^

Because some requests take some time, this library will log its progress of
longer queries. IPython & Jupyter by default attach a handler to the logger.
If you're running in another process and want to see logs, or you want to see
more verbose logs, you can do something like:

.. code-block:: python

   import logging
   logger = logging.getLogger('pandas_gbq')
   logger.setLevel(logging.DEBUG)
   logger.addHandler(logging.StreamHandler())

Writing data to BigQuery
------------------------

Use the :func:`pandas_gbq.to_gbq` function to write a
:class:`pandas.DataFrame` object to a BigQuery table.

.. literalinclude:: samples/snippets/to_gbq_simple.py
   :language: python
   :dedent: 4
   :start-after: [S bigquery_pandas_gbq_to_gbq_simple]
   :end-before: [E bigquery_pandas_gbq_to_gbq_simple]

The destination table and destination dataset will automatically be created.
By default, writes to BigQuery fail if the table already exists. Visit the
:doc:`writing tables guide <writing>` to learn about the available options.
