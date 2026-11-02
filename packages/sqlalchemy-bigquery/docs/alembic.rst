Alembic support
^^^^^^^^^^^^^^^

`Alembic <https://alembic.sqlalchemy.org>`_ is a lightweight database
migration tool for usage with the SQLAlchemy Database Toolkit for
Python.  It can use this BigQuery SQLAlchemy support to manage
BigQuery shemas.

Some features, like management of constrains and indexes, aren't
supported because `BigQuery doesn't support them
<https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language>`_.

Supported operations:

`add_column(table_name, column, schema=None)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.add_column>`_

`alter_column(table_name, column_name, nullable=None, schema=None, type_=None)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.alter_column>`_

`bulk_insert(table, rows, multiinsert=True)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.bulk_insert>`_

`create_table(table_name, *columns, **kw)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.create_table>`_

`create_table_comment(table_name, comment, schema=None)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.create_table_comment>`_

`drop_column(table_name, column_name, schema=None)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.drop_column>`_

`drop_table(table_name, schema=None)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.drop_table>`_

`drop_table_comment(table_name, schema=None)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.drop_table_comment>`_

`execute(sqltext, execution_options=None)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.execute>`_

`rename_table(old_table_name, new_table_name, schema=None)
<https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.rename_table>`_

Note that some of the operations above have limited capability, again
due to `BigQuery limitations
<https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language>`_.

The `execute` operation allows access to BigQuery-specific
`data-definition-language
<https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language>`_.
