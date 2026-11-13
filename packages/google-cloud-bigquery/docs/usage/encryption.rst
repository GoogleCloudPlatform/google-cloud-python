Using Customer Managed Encryption Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table data is always encrypted at rest, but BigQuery also provides a way for
you to control what keys it uses to encrypt they data. See `Protecting data
with Cloud KMS keys
<https://cloud.google.com/bigquery/docs/customer-managed-encryption>`_
in the BigQuery documentation for more details.

Create a new table, using a customer-managed encryption key from
Cloud KMS to encrypt it.

.. literalinclude:: ../samples/snippets/create_table_cmek.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_create_table_cmek]
   :end-before: [END bigquery_create_table_cmek]

Change the key used to encrypt a table.

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_update_table_cmek]
   :end-before: [END bigquery_update_table_cmek]

Load a file from Cloud Storage, using a customer-managed encryption key from
Cloud KMS for the destination table.

.. literalinclude:: ../samples/load_table_uri_cmek.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_json_cmek]
   :end-before: [END bigquery_load_table_gcs_json_cmek]

Copy a table, using a customer-managed encryption key from Cloud KMS for the
destination table.

.. literalinclude:: ../samples/copy_table_cmek.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_copy_table_cmek]
   :end-before: [END bigquery_copy_table_cmek]

Write query results to a table, using a customer-managed encryption key from
Cloud KMS for the destination table.

.. literalinclude:: ../samples/client_query_destination_table_cmek.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_destination_table_cmek]
   :end-before: [END bigquery_query_destination_table_cmek]
