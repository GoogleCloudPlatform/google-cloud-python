Database Admin Usage
====================

After creating an :class:`~google.cloud.spanner_v1.instance.Instance`, you can
interact with individual databases for that instance.


List Databases
--------------

To iterate over all existing databases for an instance, use its
:meth:`~google.cloud.spanner_v1.instance.Instance.list_databases` method:

.. code:: python

    for database in instance.list_databases():
        # `database` is a `Database` object.

This method yields :class:`~google.cloud.spanner_v1.database.Database`
objects.


Database Factory
----------------

To create a :class:`~google.cloud.spanner_v1.database.Database` object:

.. code:: python

    database = instance.database(database_id, ddl_statements)

- ``ddl_statements`` is a list of strings containing DDL statements for the new database.

You can also use the :meth:`~google.cloud.spanner_v1.instance.Instance.database` method
on an :class:`~google.cloud.spanner_v1.instance.Instance` object to create a local wrapper
for a database that has already been created:

.. code:: python

    database = instance.database(existing_database_id)


Create a new Database
---------------------

After creating the database object, use its
:meth:`~google.cloud.spanner_v1.database.Database.create` method to
trigger its creation on the server:

.. code:: python

    operation = database.create()

.. note::

    Creating a database triggers a "long-running operation" and
    returns a :class:`~concurrent.futures.Future`-like object. Use
    the :meth:`~concurrent.futures.Future.result` method to wait for
    and inspect the result.


Update an existing Database
---------------------------

After creating the database object, you can apply additional DDL statements
via its :meth:`~google.cloud.spanner_v1.database.Database.update_ddl` method:

.. code:: python

    operation = database.update_ddl(ddl_statements, operation_id)

- ``ddl_statements`` is a list of strings containing DDL statements to be
  applied to the database.

- ``operation_id`` is a string ID for the long-running operation.

.. note::

    Updating a database triggers a "long-running operation" and
    returns an :class:`~google.cloud.spanner_v1.database.Operation`
    object.  See :ref:`check-on-current-database-operation` for polling
    to find out if the operation is completed.


Drop a Database
---------------

Drop a database using its
:meth:`~google.cloud.spanner_v1.database.Database.drop` method:

.. code:: python

    database.drop()


.. _check-on-current-database-operation:

Check on Current Database Operation
-----------------------------------

The :meth:`~google.cloud.spanner_v1.database.Database.create` and
:meth:`~google.cloud.spanner_v1.database.Database.update_ddl` methods of the
:class:`~google.cloud.spanner_v1.database.Database` object trigger
long-running operations on the server, and return operations
conforming to the :class:`~.concurrent.futures.Future` class.

.. code:: python

    >>> operation = database.create()
    >>> operation.result()


Non-Admin Database Usage
========================

Use a Snapshot to Read / Query the Database
-------------------------------------------

A snapshot represents a read-only point-in-time view of the database.

Calling :meth:`~google.cloud.spanner_v1.database.Database.snapshot` with
no arguments creates a snapshot with strong concurrency:

.. code:: python

   with database.snapshot() as snapshot:
       do_something_with(snapshot)

See :class:`~google.cloud.spanner_v1.snapshot.Snapshot` for the other options
which can be passed.

.. note::

   :meth:`~google.cloud.spanner_v1.database.Database.snapshot` returns an
   object intended to be used as a Python context manager (i.e., as the
   target of a ``with`` statement).  Perform all iterations within the
   context of the ``with database.snapshot()`` block.



See :doc:`snapshot-usage` for more complete examples of snapshot usage.

Use a Batch to Modify Rows in the Database
------------------------------------------

A batch represents a bundled set of insert/upsert/update/delete operations
on the rows of tables in the database.

.. code:: python

   with database.batch() as batch:
        batch.insert_or_update(table, columns, rows)
        batch.delete(table, keyset_to_delete)

.. note::

   :meth:`~google.cloud.spanner_v1.database.Database.batch` returns an
   object intended to be used as a Python context manager (i.e., as the
   target of a ``with`` statement).  It applies any changes made inside
   the block of its ``with`` statement when exiting the block, unless an
   exception is raised within the block.  Use the batch only inside
   the block created by the ``with`` statement.

See :doc:`batch-usage` for more complete examples of batch usage.

Use a Transaction to Query / Modify Rows in the Database
--------------------------------------------------------

A transaction represents the union of a "strong" snapshot and a batch:
it allows ``read`` and ``execute_sql`` operations, and accumulates
insert/upsert/update/delete operations.

Because other applications may be performing concurrent updates which
would invalidate the reads / queries, the work done by a transaction needs
to be bundled as a retryable "unit of work" function, which takes the
transaction as a required argument:

.. code:: python

   def unit_of_work(transaction):
       result = transaction.execute_sql(QUERY)

       for emp_id, hours, pay in _compute_pay(result):
           transaction.insert_or_update(
               table='monthly_hours',
               columns=['employee_id', 'month', 'hours', 'pay'],
               values=[emp_id, month_start, hours, pay])

   database.run_in_transaction(unit_of_work)

.. note::

   :meth:`~google.cloud.spanner_v1.database.Database.run_in_transaction`
   commits the transaction automatically if the "unit of work" function
   returns without raising an exception.

.. note::

   :meth:`~google.cloud.spanner_v1.database.Database.run_in_transaction`
   retries the "unit of work" function if the read / query operations
   or the commit are aborted due to concurrent updates.

See :doc:`transaction-usage` for more complete examples of transaction usage.

Configuring a session pool for a database
-----------------------------------------

Under the covers, the ``snapshot``, ``batch``, and ``run_in_transaction``
methods use a pool of :class:`~google.cloud.spanner_v1.session.Session` objects
to manage their communication with the back-end.  You can configure
one of the pools manually to control the number of sessions, timeouts, etc.,
and then pass it to the :class:`~google.cloud.spanner_v1.database.Database`
constructor:

.. code-block:: python

    from google.cloud import spanner

    # Instantiate the Spanner client, and get the appropriate instance.
    client = spanner.Client()
    instance = client.instance(INSTANCE_NAME)

    # Create a database with a pool of a fixed size.
    pool = spanner.FixedSizePool(size=10, default_timeout=5)
    database = instance.database(DATABASE_NAME, pool=pool)

Note that creating a database with a pool will require the database to
already exist if the pool implementation needs to pre-create sessions
(rather than creating them on demand, as the default implementation does).

You can supply your own pool implementation, which must satisfy the
contract laid out in :class:`~google.cloud.spanner_v1.pool.AbstractSessionPool`:

.. code-block:: python

   from google.cloud.spanner import AbstractSessionPool

   class MyCustomPool(AbstractSessionPool):

        def __init__(self, database, custom_param):
            super(MyCustomPool, self).__init__(database)
            self.custom_param = custom_param

        def get(self, read_only=False):
            ...

        def put(self, session, discard_if_full=True):
            ...

   database = instance.database(DATABASE_NAME, pool=pool)
   pool = MyCustomPool(database, custom_param=42)

See :doc:`advanced-session-pool-topics` for more advanced coverage of
session pools.
