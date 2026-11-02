Bigtable Row Filters
====================

It is possible to use a
:class:`RowFilter <google.cloud.bigtable.row_filters.RowFilter>`
when adding mutations to a
:class:`ConditionalRow <google.cloud.bigtable.row.ConditionalRow>` and when
reading row data with :meth:`read_row() <google.cloud.bigtable.table.Table.read_row>`
or :meth:`read_rows() <google.cloud.bigtable.table.Table.read_rows>`.

As laid out in the `RowFilter definition`_, the following basic filters
are provided:

* :class:`SinkFilter <.row_filters.SinkFilter>`
* :class:`PassAllFilter <.row_filters.PassAllFilter>`
* :class:`BlockAllFilter <.row_filters.BlockAllFilter>`
* :class:`RowKeyRegexFilter <.row_filters.RowKeyRegexFilter>`
* :class:`RowSampleFilter <.row_filters.RowSampleFilter>`
* :class:`FamilyNameRegexFilter <.row_filters.FamilyNameRegexFilter>`
* :class:`ColumnQualifierRegexFilter <.row_filters.ColumnQualifierRegexFilter>`
* :class:`TimestampRangeFilter <.row_filters.TimestampRangeFilter>`
* :class:`ColumnRangeFilter <.row_filters.ColumnRangeFilter>`
* :class:`ValueRegexFilter <.row_filters.ValueRegexFilter>`
* :class:`ValueRangeFilter <.row_filters.ValueRangeFilter>`
* :class:`CellsRowOffsetFilter <.row_filters.CellsRowOffsetFilter>`
* :class:`CellsRowLimitFilter <.row_filters.CellsRowLimitFilter>`
* :class:`CellsColumnLimitFilter <.row_filters.CellsColumnLimitFilter>`
* :class:`StripValueTransformerFilter <.row_filters.StripValueTransformerFilter>`
* :class:`ApplyLabelFilter <.row_filters.ApplyLabelFilter>`

In addition, these filters can be combined into composite filters with

* :class:`RowFilterChain <.row_filters.RowFilterChain>`
* :class:`RowFilterUnion <.row_filters.RowFilterUnion>`
* :class:`ConditionalRowFilter <.row_filters.ConditionalRowFilter>`

These rules can be nested arbitrarily, with a basic filter at the lowest
level. For example:

.. code:: python

    # Filter in a specified column (matching any column family).
    col1_filter = ColumnQualifierRegexFilter(b'columnbia')

    # Create a filter to label results.
    label1 = u'label-red'
    label1_filter = ApplyLabelFilter(label1)

    # Combine the filters to label all the cells in columnbia.
    chain1 = RowFilterChain(filters=[col1_filter, label1_filter])

    # Create a similar filter to label cells blue.
    col2_filter = ColumnQualifierRegexFilter(b'columnseeya')
    label2 = u'label-blue'
    label2_filter = ApplyLabelFilter(label2)
    chain2 = RowFilterChain(filters=[col2_filter, label2_filter])

    # Bring our two labeled columns together.
    row_filter = RowFilterUnion(filters=[chain1, chain2])

----

.. automodule:: google.cloud.bigtable.row_filters
  :members:
  :show-inheritance:

.. _RowFilter definition: https://googleapis.dev/python/bigtable/latest/row-filters.html?highlight=rowfilter#google.cloud.bigtable.row_filters.RowFilter
