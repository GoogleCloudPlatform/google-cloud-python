Running Queries
~~~~~~~~~~~~~~~

Querying data
^^^^^^^^^^^^^

Run a query and wait for it to finish with the
:func:`~google.cloud.bigquery.client.Client.query_and_wait` method:

.. literalinclude:: ../samples/snippets/client_query.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query]
   :end-before: [END bigquery_query]


Run a dry run query
^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../samples/client_query_dry_run.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_dry_run]
   :end-before: [END bigquery_query_dry_run]


Writing query results to a destination table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See BigQuery documentation for more information on
`writing query results <https://cloud.google.com/bigquery/docs/writing-results>`_.

.. literalinclude:: ../samples/client_query_destination_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_destination_table]
   :end-before: [END bigquery_query_destination_table]


Run a query using a named query parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See BigQuery documentation for more information on
`parameterized queries <https://cloud.google.com/bigquery/docs/parameterized-queries>`_.

.. literalinclude:: ../samples/client_query_w_named_params.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_params_named]
   :end-before: [END bigquery_query_params_named]

Run a script
^^^^^^^^^^^^

See BigQuery documentation for more information on `scripting in BigQuery
standard SQL
<https://cloud.google.com/bigquery/docs/reference/standard-sql/scripting>`_.

.. literalinclude:: ../samples/query_script.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_script]
   :end-before: [END bigquery_query_script]
