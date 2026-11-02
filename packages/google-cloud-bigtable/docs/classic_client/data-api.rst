Data API
========

.. note::
   This page describes how to use the Data API with the synchronous Bigtable client.
   Examples for using the Data API with the async client can be found in the
   `Getting Started Guide`_.

.. _Getting Started Guide: https://cloud.google.com/bigtable/docs/samples-python-hello

After creating a :class:`Table <google.cloud.bigtable.table.Table>` and some
column families, you are ready to store and retrieve data.

Cells vs. Columns vs. Column Families
+++++++++++++++++++++++++++++++++++++

* As explained in the :doc:`table overview <table-api>`, tables can
  have many column families.
* As described below, a table can also have many rows which are
  specified by row keys.
* Within a row, data is stored in a cell. A cell simply has a value (as
  bytes) and a timestamp. The number of cells in each row can be
  different, depending on what was stored in each row.
* Each cell lies in a column (**not** a column family). A column is really
  just a more **specific** modifier within a column family. A column
  can be present in every column family, in only one or anywhere in between.
* Within a column family there can be many columns. For example, within
  the column family ``foo`` we could have columns ``bar`` and ``baz``.
  These would typically be represented as ``foo:bar`` and ``foo:baz``.

Modifying Data
++++++++++++++

Since data is stored in cells, which are stored in rows, we
use the metaphor of a **row** in classes that are used to modify
(write, update, delete) data in a
:class:`Table <google.cloud.bigtable.table.Table>`.

Direct vs. Conditional vs. Append
---------------------------------

There are three ways to modify data in a table, described by the
`MutateRow`_, `CheckAndMutateRow`_ and `ReadModifyWriteRow`_ API
methods.

* The **direct** way is via `MutateRow`_ which involves simply
  adding, overwriting or deleting cells. The
  :class:`DirectRow <google.cloud.bigtable.row.DirectRow>` class
  handles direct mutations.
* The **conditional** way is via `CheckAndMutateRow`_. This method
  first checks if some filter is matched in a given row, then
  applies one of two sets of mutations, depending on if a match
  occurred or not. (These mutation sets are called the "true
  mutations" and "false mutations".) The
  :class:`ConditionalRow <google.cloud.bigtable.row.ConditionalRow>` class
  handles conditional mutations.
* The **append** way is via `ReadModifyWriteRow`_. This simply
  appends (as bytes) or increments (as an integer) data in a presumed
  existing cell in a row. The
  :class:`AppendRow <google.cloud.bigtable.row.AppendRow>` class
  handles append mutations.

Row Factory
-----------

A single factory can be used to create any of the three row types.
To create a :class:`DirectRow <google.cloud.bigtable.row.DirectRow>`:

.. code:: python

    row = table.row(row_key)

Unlike the previous string values we've used before, the row key must
be ``bytes``.

To create a :class:`ConditionalRow <google.cloud.bigtable.row.ConditionalRow>`,
first create a :class:`RowFilter <google.cloud.bigtable.row.RowFilter>` and
then

.. code:: python

    cond_row = table.row(row_key, filter_=filter_)

To create an :class:`AppendRow <google.cloud.bigtable.row.AppendRow>`

.. code:: python

    append_row = table.row(row_key, append=True)

Building Up Mutations
---------------------

In all three cases, a set of mutations (or two sets) are built up
on a row before they are sent off in a batch via

.. code:: python

    row.commit()

Direct Mutations
----------------

Direct mutations can be added via one of four methods

* :meth:`set_cell() <google.cloud.bigtable.row.DirectRow.set_cell>` allows a
  single value to be written to a column

  .. code:: python

      row.set_cell(column_family_id, column, value,
                   timestamp=timestamp)

  If the ``timestamp`` is omitted, the current time on the Google Cloud
  Bigtable server will be used when the cell is stored.

  The value can either be bytes or an integer, which will be converted to
  bytes as a signed 64-bit integer.

* :meth:`delete_cell() <google.cloud.bigtable.row.DirectRow.delete_cell>` deletes
  all cells (i.e. for all timestamps) in a given column

  .. code:: python

      row.delete_cell(column_family_id, column)

  Remember, this only happens in the ``row`` we are using.

  If we only want to delete cells from a limited range of time, a
  :class:`TimestampRange <google.cloud.bigtable.row.TimestampRange>` can
  be used

  .. code:: python

      row.delete_cell(column_family_id, column,
                      time_range=time_range)

* :meth:`delete_cells() <google.cloud.bigtable.row.DirectRow.delete_cells>` does
  the same thing as
  :meth:`delete_cell() <google.cloud.bigtable.row.DirectRow.delete_cell>`,
  but accepts a list of columns in a column family rather than a single one.

  .. code:: python

      row.delete_cells(column_family_id, [column1, column2],
                       time_range=time_range)

  In addition, if we want to delete cells from every column in a column family,
  the special :attr:`ALL_COLUMNS <google.cloud.bigtable.row.DirectRow.ALL_COLUMNS>`
  value can be used

  .. code:: python

      row.delete_cells(column_family_id, row.ALL_COLUMNS,
                       time_range=time_range)

* :meth:`delete() <google.cloud.bigtable.row.DirectRow.delete>` will delete the
  entire row

  .. code:: python

      row.delete()

Conditional Mutations
---------------------

Making **conditional** modifications is essentially identical
to **direct** modifications: it uses the exact same methods
to accumulate mutations.

However, each mutation added must specify a ``state``: will the mutation be
applied if the filter matches or if it fails to match.

For example:

.. code:: python

    cond_row.set_cell(column_family_id, column, value,
                      timestamp=timestamp, state=True)

will add to the set of true mutations.

Append Mutations
----------------

Append mutations can be added via one of two methods

* :meth:`append_cell_value() <google.cloud.bigtable.row.AppendRow.append_cell_value>`
  appends a bytes value to an existing cell:

  .. code:: python

      append_row.append_cell_value(column_family_id, column, bytes_value)

* :meth:`increment_cell_value() <google.cloud.bigtable.row.AppendRow.increment_cell_value>`
  increments an integer value in an existing cell:

  .. code:: python

      append_row.increment_cell_value(column_family_id, column, int_value)

  Since only bytes are stored in a cell, the cell value is decoded as
  a signed 64-bit integer before being incremented. (This happens on
  the Google Cloud Bigtable server, not in the library.)

Notice that no timestamp was specified. This is because **append** mutations
operate on the latest value of the specified column.

If there are no cells in the specified column, then the empty string (bytes
case) or zero (integer case) are the assumed values.

Starting Fresh
--------------

If accumulated mutations need to be dropped, use

.. code:: python

    row.clear()

Reading Data
++++++++++++

Read Single Row from a Table
----------------------------

To make a `ReadRows`_ API request for a single row key, use
:meth:`Table.read_row() <google.cloud.bigtable.table.Table.read_row>`:

.. code:: python

    >>> row_data = table.read_row(row_key)
    >>> row_data.cells
    {
        u'fam1': {
            b'col1': [
                <google.cloud.bigtable.row_data.Cell at 0x7f80d150ef10>,
                <google.cloud.bigtable.row_data.Cell at 0x7f80d150ef10>,
            ],
            b'col2': [
                <google.cloud.bigtable.row_data.Cell at 0x7f80d150ef10>,
            ],
        },
        u'fam2': {
            b'col3': [
                <google.cloud.bigtable.row_data.Cell at 0x7f80d150ef10>,
                <google.cloud.bigtable.row_data.Cell at 0x7f80d150ef10>,
                <google.cloud.bigtable.row_data.Cell at 0x7f80d150ef10>,
            ],
        },
    }
    >>> cell = row_data.cells[u'fam1'][b'col1'][0]
    >>> cell
    <google.cloud.bigtable.row_data.Cell at 0x7f80d150ef10>
    >>> cell.value
    b'val1'
    >>> cell.timestamp
    datetime.datetime(2016, 2, 27, 3, 41, 18, 122823, tzinfo=<UTC>)

Rather than returning a :class:`DirectRow <google.cloud.bigtable.row.DirectRow>`
or similar class, this method returns a
:class:`PartialRowData <google.cloud.bigtable.row_data.PartialRowData>`
instance. This class is used for reading and parsing data rather than for
modifying data (as :class:`DirectRow <google.cloud.bigtable.row.DirectRow>` is).

A filter can also be applied to the results:

.. code:: python

    row_data = table.read_row(row_key, filter_=filter_val)

The allowable ``filter_`` values are the same as those used for a
:class:`ConditionalRow <google.cloud.bigtable.row.ConditionalRow>`. For
more information, see the
:meth:`Table.read_row() <google.cloud.bigtable.table.Table.read_row>` documentation.

Stream Many Rows from a Table
-----------------------------

To make a `ReadRows`_ API request for a stream of rows, use
:meth:`Table.read_rows() <google.cloud.bigtable.table.Table.read_rows>`:

.. code:: python

    row_data = table.read_rows()

Using gRPC over HTTP/2, a continual stream of responses will be delivered.
In particular

* :meth:`consume_next() <google.cloud.bigtable.row_data.PartialRowsData.consume_next>`
  pulls the next result from the stream, parses it and stores it on the
  :class:`PartialRowsData <google.cloud.bigtable.row_data.PartialRowsData>` instance
* :meth:`consume_all() <google.cloud.bigtable.row_data.PartialRowsData.consume_all>`
  pulls results from the stream until there are no more
* :meth:`cancel() <google.cloud.bigtable.row_data.PartialRowsData.cancel>` closes
  the stream

See the :class:`PartialRowsData <google.cloud.bigtable.row_data.PartialRowsData>`
documentation for more information.

As with
:meth:`Table.read_row() <google.cloud.bigtable.table.Table.read_row>`, an optional
``filter_`` can be applied. In addition a ``start_key`` and / or ``end_key``
can be supplied for the stream, a ``limit`` can be set and a boolean
``allow_row_interleaving`` can be specified to allow faster streamed results
at the potential cost of non-sequential reads.

See the :meth:`Table.read_rows() <google.cloud.bigtable.table.Table.read_rows>`
documentation for more information on the optional arguments.

Sample Keys in a Table
----------------------

Make a `SampleRowKeys`_ API request with
:meth:`Table.sample_row_keys() <google.cloud.bigtable.table.Table.sample_row_keys>`:

.. code:: python

    keys_iterator = table.sample_row_keys()

The returned row keys will delimit contiguous sections of the table of
approximately equal size, which can be used to break up the data for
distributed tasks like mapreduces.

As with
:meth:`Table.read_rows() <google.cloud.bigtable.table.Table.read_rows>`, the
returned ``keys_iterator`` is connected to a cancellable HTTP/2 stream.

The next key in the result can be accessed via

.. code:: python

    next_key = keys_iterator.next()

or all keys can be iterated over via

.. code:: python

    for curr_key in keys_iterator:
        do_something(curr_key)

Just as with reading, the stream can be canceled:

.. code:: python

    keys_iterator.cancel()

.. _ReadRows: https://github.com/googleapis/python-bigtable/blob/d6bff70654b41e31d2ac83d307bdc6bbd111201e/google/cloud/bigtable_v2/types/bigtable.py#L42-L72
.. _SampleRowKeys: https://github.com/googleapis/python-bigtable/blob/d6bff70654b41e31d2ac83d307bdc6bbd111201e/google/cloud/bigtable_v2/types/bigtable.py#L184-L199
.. _MutateRow: https://github.com/googleapis/python-bigtable/blob/d6bff70654b41e31d2ac83d307bdc6bbd111201e/google/cloud/bigtable_v2/types/bigtable.py#L230-L256
.. _CheckAndMutateRow: https://github.com/googleapis/python-bigtable/blob/d6bff70654b41e31d2ac83d307bdc6bbd111201e/google/cloud/bigtable_v2/types/bigtable.py#L339-L386
.. _ReadModifyWriteRow: https://github.com/googleapis/python-bigtable/blob/d6bff70654b41e31d2ac83d307bdc6bbd111201e/google/cloud/bigtable_v2/types/bigtable.py#L401-L430
