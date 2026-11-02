Table Admin Usage
=================

After creating an :class:`~google.cloud.spanner_v1.database.Database`, you can
interact with individual tables for that instance.


List Tables
-----------

To iterate over all existing tables for an database, use its
:meth:`~google.cloud.spanner_v1.database.Database.list_tables` method:

.. code:: python

    for table in database.list_tables():
        # `table` is a `Table` object.

This method yields :class:`~google.cloud.spanner_v1.table.Table` objects.


Table Factory
-------------

A :class:`~google.cloud.spanner_v1.table.Table` object can be created with the
:meth:`~google.cloud.spanner_v1.database.Database.table` factory method:

.. code:: python

    table = database.table("my_table_id")
    if table.exists():
        print("Table with ID 'my_table' exists.")
    else:
        print("Table with ID 'my_table' does not exist."


Getting the Table Schema
------------------------

Use the :attr:`~google.cloud.spanner_v1.table.Table.schema` property to inspect
the columns of a table as a list of
:class:`~google.cloud.spanner_v1.types.StructType.Field` objects.

.. code:: python

    for field in table.schema
        # `field` is a `Field` object.
