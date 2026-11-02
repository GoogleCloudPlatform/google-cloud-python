Managing Tables
~~~~~~~~~~~~~~~

Tables exist within datasets. See BigQuery documentation for more information
on `Tables <https://cloud.google.com/bigquery/docs/tables>`_.

Listing Tables
^^^^^^^^^^^^^^

List the tables belonging to a dataset with the
:func:`~google.cloud.bigquery.client.Client.list_tables` method:

.. literalinclude:: ../samples/list_tables.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_list_tables]
   :end-before: [END bigquery_list_tables]

Getting a Table
^^^^^^^^^^^^^^^

Get a table resource with the
:func:`~google.cloud.bigquery.client.Client.get_table` method:

.. literalinclude:: ../samples/get_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_get_table]
   :end-before: [END bigquery_get_table]

Determine if a table exists with the
:func:`~google.cloud.bigquery.client.Client.get_table` method:

.. literalinclude:: ../samples/table_exists.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_table_exists]
   :end-before: [END bigquery_table_exists]

Browse data rows in a table with the
:func:`~google.cloud.bigquery.client.Client.list_rows` method:

.. literalinclude:: ../samples/browse_table_data.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_browse_table]
   :end-before: [END bigquery_browse_table]

Creating a Table
^^^^^^^^^^^^^^^^

Create an empty table with the
:func:`~google.cloud.bigquery.client.Client.create_table` method:

.. literalinclude:: ../samples/create_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_create_table]
   :end-before: [END bigquery_create_table]

Create a table using an external data source with the
:func:`~google.cloud.bigquery.client.Client.create_table` method:

.. literalinclude:: ../samples/snippets/create_table_external_data_configuration.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_create_table_external_data_configuration]
   :end-before: [END bigquery_create_table_external_data_configuration]

Create a clustered table with the
:func:`~google.cloud.bigquery.client.Client.create_table` method:

.. literalinclude:: ../samples/create_table_clustered.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_create_table_clustered]
   :end-before: [END bigquery_create_table_clustered]

Create an integer range partitioned table with the
:func:`~google.cloud.bigquery.client.Client.create_table` method:

.. literalinclude:: ../samples/create_table_range_partitioned.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_create_table_range_partitioned]
   :end-before: [END bigquery_create_table_range_partitioned]

Load table data from a file with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_file` method:

.. literalinclude:: ../samples/load_table_file.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_from_file]
   :end-before: [END bigquery_load_from_file]

Creating a clustered table from a query result:

.. literalinclude:: ../samples/client_query_destination_table_clustered.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_clustered_table]
   :end-before: [END bigquery_query_clustered_table]

Creating a clustered table when you load data with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_uri` method:

.. literalinclude:: ../samples/load_table_clustered.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_clustered]
   :end-before: [END bigquery_load_table_clustered]

Load a CSV file from Cloud Storage with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_uri` method:

.. literalinclude:: ../samples/load_table_uri_csv.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_csv]
   :end-before: [END bigquery_load_table_gcs_csv]

See also: `Loading CSV data from Cloud Storage
<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv>`_.

Load a JSON file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_json.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_json]
   :end-before: [END bigquery_load_table_gcs_json]

See also: `Loading JSON data from Cloud Storage
<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json>`_.

Load a Parquet file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_parquet.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_parquet]
   :end-before: [END bigquery_load_table_gcs_parquet]

See also: `Loading Parquet data from Cloud Storage
<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet>`_.

Load an Avro file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_avro.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_avro]
   :end-before: [END bigquery_load_table_gcs_avro]

See also: `Loading Avro data from Cloud Storage
<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro>`_.

Load an ORC file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_orc.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_orc]
   :end-before: [END bigquery_load_table_gcs_orc]

See also: `Loading ORC data from Cloud Storage
<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-orc>`_.

Load a CSV file from Cloud Storage and auto-detect schema:

.. literalinclude:: ../samples/load_table_uri_autodetect_csv.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_csv_autodetect]
   :end-before: [END bigquery_load_table_gcs_csv_autodetect]

Load a JSON file from Cloud Storage and auto-detect schema:

.. literalinclude:: ../samples/load_table_uri_autodetect_json.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_json_autodetect]
   :end-before: [END bigquery_load_table_gcs_json_autodetect]

Column Data Policies
^^^^^^^^^^^^^^^^^^^^

Use :class:`~google.cloud.bigquery.schema.SchemaField` to represent data policies
attached directly to a column. Pass :class:`~google.cloud.bigquery.schema.DataPolicy`
objects as the keyword argument ``data_policies``:

.. code-block:: python

    from google.cloud import bigquery

    field = bigquery.SchemaField(
        "ssn",
        "STRING",
        data_policies=[
            bigquery.DataPolicy(
                name="projects/my-project/locations/us/dataPolicies/mask_ssn"
            )
        ],
    )

The ``data_policies`` property returns a tuple of ``DataPolicy`` objects, or
``None`` when the property is unset. Each object's ``name`` property contains
the resource name. Its ``to_api_repr()`` method preserves all properties from
the REST representation, including any not yet exposed by the client.
The client serializes the objects as ``dataPolicies`` in the table schema.
Omitting the argument leaves that property out of the API representation;
``None`` produces ``null`` and an empty iterable produces an empty array.

This property represents ``dataPolicies``, not the separate ``dataPolicyList``
REST field. When ``dataPolicyList`` is present, BigQuery uses it as the source of
truth for data policy information.

BigQuery does not allow policy tags and data policies on the same column. To
remove the last data policy from a column, use ``ALTER COLUMN SET OPTIONS`` with
``data_policies = []``. Serializing an empty array does not change the service's
policy-removal behavior. See `Mask data with data policies directly on a column
<https://cloud.google.com/bigquery/docs/column-data-masking>`_
for permissions and service limitations.

Updating a Table
^^^^^^^^^^^^^^^^

Update a property in a table's metadata with the
:func:`~google.cloud.bigquery.client.Client.update_table` method:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_update_table_description]
   :end-before: [END bigquery_update_table_description]

Insert rows into a table's data with the
:func:`~google.cloud.bigquery.client.Client.insert_rows` method:

.. literalinclude:: ../samples/table_insert_rows.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_table_insert_rows]
   :end-before: [END bigquery_table_insert_rows]

Insert rows into a table's data with the
:func:`~google.cloud.bigquery.client.Client.insert_rows` method, achieving
higher write limit:

.. literalinclude:: ../samples/table_insert_rows_explicit_none_insert_ids.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_table_insert_rows_explicit_none_insert_ids]
   :end-before: [END bigquery_table_insert_rows_explicit_none_insert_ids]

Mind that inserting data with ``None`` row insert IDs can come at the expense of
more duplicate inserts. See also:
`Streaming inserts <https://cloud.google.com/bigquery/quotas#streaming_inserts>`_.

Add an empty column to the existing table with the
:func:`~google.cloud.bigquery.update_table` method:

.. literalinclude:: ../samples/add_empty_column.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_add_empty_column]
   :end-before: [END bigquery_add_empty_column]

Copying a Table
^^^^^^^^^^^^^^^

Copy a table with the
:func:`~google.cloud.bigquery.client.Client.copy_table` method:

.. literalinclude:: ../samples/copy_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_copy_table]
   :end-before: [END bigquery_copy_table]

Copy table data to Google Cloud Storage with the
:func:`~google.cloud.bigquery.client.Client.extract_table` method:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_extract_table]
   :end-before: [END bigquery_extract_table]

Deleting a Table
^^^^^^^^^^^^^^^^

Delete a table with the
:func:`~google.cloud.bigquery.client.Client.delete_table` method:

.. literalinclude:: ../samples/delete_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_delete_table]
   :end-before: [END bigquery_delete_table]

Restoring a Deleted Table
^^^^^^^^^^^^^^^^^^^^^^^^^

Restore a deleted table from a snapshot by using the
:func:`~google.cloud.bigquery.client.Client.copy_table` method:

.. literalinclude:: ../samples/undelete_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_undelete_table]
   :end-before: [END bigquery_undelete_table]

Overwrite a Table
^^^^^^^^^^^^^^^^^

Replace the table data with an Avro file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_truncate_avro.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_avro_truncate]
   :end-before: [END bigquery_load_table_gcs_avro_truncate]

Replace the table data with a CSV file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_truncate_csv.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_csv_truncate]
   :end-before: [END bigquery_load_table_gcs_csv_truncate]

Replace the table data with a JSON file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_truncate_json.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_json_truncate]
   :end-before: [END bigquery_load_table_gcs_json_truncate]

Replace the table data with an ORC file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_truncate_orc.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_orc_truncate]
   :end-before: [END bigquery_load_table_gcs_orc_truncate]

Replace the table data with a Parquet file from Cloud Storage:

.. literalinclude:: ../samples/load_table_uri_truncate_parquet.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_parquet_truncate]
   :end-before: [END bigquery_load_table_gcs_parquet_truncate]
