Managing Jobs
~~~~~~~~~~~~~

Jobs describe actions performed on data in BigQuery tables:

- Load data into a table
- Run a query against data in one or more tables
- Extract data from a table
- Copy a table

Listing jobs
^^^^^^^^^^^^

List jobs for a project with the
:func:`~google.cloud.bigquery.client.Client.list_jobs` method:

.. literalinclude:: ../samples/client_list_jobs.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_list_jobs]
   :end-before: [END bigquery_list_jobs]
