Table Admin API
===============

After creating an :class:`Instance <google.cloud.bigtable.instance.Instance>`, you can
interact with individual tables, groups of tables or column families within
a table.

List Tables
-----------

If you want a comprehensive list of all existing tables in a instance, make a
`ListTables`_ API request with
:meth:`Instance.list_tables() <google.cloud.bigtable.instance.Instance.list_tables>`:

.. code:: python

    >>> instance.list_tables()
    [<google.cloud.bigtable.table.Table at 0x7ff6a1de8f50>,
     <google.cloud.bigtable.table.Table at 0x7ff6a1de8350>]

Table Factory
-------------

To create a :class:`Table <google.cloud.bigtable.table.Table>` object:

.. code:: python

    table = instance.table(table_id)

Even if this :class:`Table <google.cloud.bigtable.table.Table>` already
has been created with the API, you'll want this object to use as a
parent of a :class:`ColumnFamily <google.cloud.bigtable.column_family.ColumnFamily>`
or :class:`Row <google.cloud.bigtable.row.Row>`.

Create a new Table
------------------

After creating the table object, make a `CreateTable`_ API request
with :meth:`create() <google.cloud.bigtable.table.Table.create>`:

.. code:: python

    table.create()

If you would like to initially split the table into several tablets (tablets are
similar to HBase regions):

.. code:: python

    table.create(initial_split_keys=['s1', 's2'])

Delete an existing Table
------------------------

Make a `DeleteTable`_ API request with
:meth:`delete() <google.cloud.bigtable.table.Table.delete>`:

.. code:: python

    table.delete()

List Column Families in a Table
-------------------------------

Though there is no **official** method for retrieving `column families`_
associated with a table, the `GetTable`_ API method returns a
table object with the names of the column families.

To retrieve the list of column families use
:meth:`list_column_families() <google.cloud.bigtable.table.Table.list_column_families>`:

.. code:: python

    column_families = table.list_column_families()

Column Family Factory
---------------------

To create a
:class:`ColumnFamily <google.cloud.bigtable.column_family.ColumnFamily>` object:

.. code:: python

    column_family = table.column_family(column_family_id)

There is no real reason to use this factory unless you intend to
create or delete a column family.

In addition, you can specify an optional ``gc_rule`` (a
:class:`GarbageCollectionRule <google.cloud.bigtable.column_family.GarbageCollectionRule>`
or similar):

.. code:: python

    column_family = table.column_family(column_family_id,
                                        gc_rule=gc_rule)

This rule helps the backend determine when and how to clean up old cells
in the column family.

See :doc:`column-family` for more information about
:class:`GarbageCollectionRule <google.cloud.bigtable.column_family.GarbageCollectionRule>`
and related classes.

Create a new Column Family
--------------------------

After creating the column family object, make a `CreateColumnFamily`_ API
request with
:meth:`ColumnFamily.create() <google.cloud.bigtable.column_family.ColumnFamily.create>`

.. code:: python

    column_family.create()

Delete an existing Column Family
--------------------------------

Make a `DeleteColumnFamily`_ API request with
:meth:`ColumnFamily.delete() <google.cloud.bigtable.column_family.ColumnFamily.delete>`

.. code:: python

    column_family.delete()

Update an existing Column Family
--------------------------------

Make an `UpdateColumnFamily`_ API request with
:meth:`ColumnFamily.delete() <google.cloud.bigtable.column_family.ColumnFamily.update>`

.. code:: python

    column_family.update()

Next Step
---------

Now we go down the final step of the hierarchy from
:class:`Table <google.cloud.bigtable.table.Table>` to
:class:`Row <google.cloud.bigtable.row.Row>` as well as streaming
data directly via a :class:`Table <google.cloud.bigtable.table.Table>`.

Head next to learn about the :doc:`data-api`.

.. _ListTables: https://googleapis.dev/python/bigtable/latest/table-api.html#list-tables
.. _CreateTable: https://googleapis.dev/python/bigtable/latest/table-api.html#create-a-new-table
.. _DeleteTable: https://googleapis.dev/python/bigtable/latest/table-api.html#delete-an-existing-table
.. _GetTable: https://github.com/googleapis/python-bigtable/blob/main/google/cloud/bigtable_admin_v2/proto/bigtable_table_admin.proto#L97-L102
.. _CreateColumnFamily: https://googleapis.dev/python/bigtable/latest/table-api.html?highlight=gettable#create-a-new-column-family
.. _UpdateColumnFamily: https://googleapis.dev/python/bigtable/latest/table-api.html?highlight=gettable#update-an-existing-column-family
.. _DeleteColumnFamily: https://googleapis.dev/python/bigtable/latest/table-api.html?highlight=gettable#delete-an-existing-column-family
.. _column families: https://cloud.google.com/bigtable/docs/schema-design#column_families_and_column_qualifiers
