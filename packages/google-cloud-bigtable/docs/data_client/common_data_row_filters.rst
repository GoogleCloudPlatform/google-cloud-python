Bigtable Row Filters
====================

It is possible to use a
:class:`RowFilter <google.cloud.bigtable.data.row_filters.RowFilter>`
when constructing a :class:`ReadRowsQuery <google.cloud.bigtable.data.read_rows_query.ReadRowsQuery>`

The following basic filters
are provided:

* :class:`SinkFilter <.data.row_filters.SinkFilter>`
* :class:`PassAllFilter <.data.row_filters.PassAllFilter>`
* :class:`BlockAllFilter <.data.row_filters.BlockAllFilter>`
* :class:`RowKeyRegexFilter <.data.row_filters.RowKeyRegexFilter>`
* :class:`RowSampleFilter <.data.row_filters.RowSampleFilter>`
* :class:`FamilyNameRegexFilter <.data.row_filters.FamilyNameRegexFilter>`
* :class:`ColumnQualifierRegexFilter <.data.row_filters.ColumnQualifierRegexFilter>`
* :class:`TimestampRangeFilter <.data.row_filters.TimestampRangeFilter>`
* :class:`ColumnRangeFilter <.data.row_filters.ColumnRangeFilter>`
* :class:`ValueRegexFilter <.data.row_filters.ValueRegexFilter>`
* :class:`ValueRangeFilter <.data.row_filters.ValueRangeFilter>`
* :class:`CellsRowOffsetFilter <.data.row_filters.CellsRowOffsetFilter>`
* :class:`CellsRowLimitFilter <.data.row_filters.CellsRowLimitFilter>`
* :class:`CellsColumnLimitFilter <.data.row_filters.CellsColumnLimitFilter>`
* :class:`StripValueTransformerFilter <.data.row_filters.StripValueTransformerFilter>`
* :class:`ApplyLabelFilter <.data.row_filters.ApplyLabelFilter>`

In addition, these filters can be combined into composite filters with

* :class:`RowFilterChain <.data.row_filters.RowFilterChain>`
* :class:`RowFilterUnion <.data.row_filters.RowFilterUnion>`
* :class:`ConditionalRowFilter <.data.row_filters.ConditionalRowFilter>`

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

.. automodule:: google.cloud.bigtable.data.row_filters
  :members:
  :show-inheritance:
