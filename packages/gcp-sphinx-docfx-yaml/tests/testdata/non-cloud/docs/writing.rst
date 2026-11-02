.. _writer:

Writing Tables
==============

Use the :func:`pandas_gbq.to_gbq` function to write a
:class:`pandas.DataFrame` object to a BigQuery table.

.. literalinclude:: samples/snippets/to_gbq_simple.py
   :language: python
   :dedent: 4
   :start-after: [S bigquery_pandas_gbq_to_gbq_simple]
   :end-before: [E bigquery_pandas_gbq_to_gbq_simple]

The destination table and destination dataset will automatically be created
if they do not already exist.

Writing to an Existing Table
----------------------------

Use the ``if_exists`` argument to dictate whether to ``'fail'``,
``'replace'`` or ``'append'`` if the destination table already exists. The
default value is ``'fail'``.

For example, assume that ``if_exists`` is set to ``'fail'``. The following snippet will raise
a ``TableCreationError`` if the destination table already exists.

.. code-block:: python

   import pandas_gbq
   pandas_gbq.to_gbq(
       df, 'my_dataset.my_table', project_id=projectid, if_exists='fail',
   )

If the ``if_exists`` argument is set to ``'append'``, the destination
dataframe will be written to the table using the defined table schema and
column types. The dataframe must contain fields (matching name and type)
currently in the destination table.


.. _writing-schema:

Inferring the Table Schema
--------------------------

The :func:`~pandas_gbq.to_gbq` method infers the BigQuery table schema based
on the dtypes of the uploaded :class:`~pandas.DataFrame`.

========================= ==================
dtype                     BigQuery Data Type
========================= ==================
i (integer)               INTEGER
b (boolean)               BOOLEAN
f (float)                 FLOAT
O (object)                STRING
S (zero-terminated bytes) STRING
U (Unicode string)        STRING
M (datetime)              TIMESTAMP
========================= ==================

If the data type inference does not suit your needs, supply a BigQuery schema
as the ``table_schema`` parameter of :func:`~pandas_gbq.to_gbq`.


Troubleshooting Errors
----------------------

If an error occurs while writing data to BigQuery, see
`Troubleshooting BigQuery Errors <https://cloud.google.com/bigquery/troubleshooting-errors>`__.
