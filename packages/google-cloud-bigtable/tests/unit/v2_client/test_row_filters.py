# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pytest

from google.cloud.bigtable import row_filters
from google.cloud.bigtable.row_filters import (
    _BoolFilter as _BaseBoolFilter,
)
from google.cloud.bigtable.row_filters import (
    _CellCountFilter as _BaseCellCountFilter,
)
from google.cloud.bigtable.row_filters import (
    _FilterCombination as _BaseFilterCombination,
)
from google.cloud.bigtable.row_filters import (
    _RegexFilter as _BaseRegexFilter,
)


def test_bool_filter_constructor():
    flag = object()
    row_filter = _BoolFilter(flag)
    assert row_filter.flag is flag


def test_bool_filter___eq__type_differ():
    flag = object()
    row_filter1 = _BoolFilter(flag)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_bool_filter___eq__same_value():
    flag = object()
    row_filter1 = _BoolFilter(flag)
    row_filter2 = _BoolFilter(flag)
    assert row_filter1 == row_filter2


def test_bool_filter___ne__same_value():
    flag = object()
    row_filter1 = _BoolFilter(flag)
    row_filter2 = _BoolFilter(flag)
    assert not (row_filter1 != row_filter2)


def test_sink_filter_to_pb():
    from google.cloud.bigtable.row_filters import SinkFilter

    flag = True
    row_filter = SinkFilter(flag)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(sink=flag)
    assert pb_val == expected_pb


def test_pass_all_filter_to_pb():
    from google.cloud.bigtable.row_filters import PassAllFilter

    flag = True
    row_filter = PassAllFilter(flag)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(pass_all_filter=flag)
    assert pb_val == expected_pb


def test_block_all_filter_to_pb():
    from google.cloud.bigtable.row_filters import BlockAllFilter

    flag = True
    row_filter = BlockAllFilter(flag)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(block_all_filter=flag)
    assert pb_val == expected_pb


def test_regex_filterconstructor():
    regex = b"abc"
    row_filter = _RegexFilter(regex)
    assert row_filter.regex is regex


def test_regex_filterconstructor_non_bytes():
    regex = "abc"
    row_filter = _RegexFilter(regex)
    assert row_filter.regex == b"abc"


def test_regex_filter__eq__type_differ():
    regex = b"def-rgx"
    row_filter1 = _RegexFilter(regex)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_regex_filter__eq__same_value():
    regex = b"trex-regex"
    row_filter1 = _RegexFilter(regex)
    row_filter2 = _RegexFilter(regex)
    assert row_filter1 == row_filter2


def test_regex_filter__ne__same_value():
    regex = b"abc"
    row_filter1 = _RegexFilter(regex)
    row_filter2 = _RegexFilter(regex)
    assert not (row_filter1 != row_filter2)


def test_row_key_regex_filter_to_pb():
    from google.cloud.bigtable.row_filters import RowKeyRegexFilter

    regex = b"row-key-regex"
    row_filter = RowKeyRegexFilter(regex)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(row_key_regex_filter=regex)
    assert pb_val == expected_pb


def test_row_sample_filter_constructor():
    from google.cloud.bigtable.row_filters import RowSampleFilter

    sample = object()
    row_filter = RowSampleFilter(sample)
    assert row_filter.sample is sample


def test_row_sample_filter___eq__type_differ():
    from google.cloud.bigtable.row_filters import RowSampleFilter

    sample = object()
    row_filter1 = RowSampleFilter(sample)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_row_sample_filter___eq__same_value():
    from google.cloud.bigtable.row_filters import RowSampleFilter

    sample = object()
    row_filter1 = RowSampleFilter(sample)
    row_filter2 = RowSampleFilter(sample)
    assert row_filter1 == row_filter2


def test_row_sample_filter___ne__():
    from google.cloud.bigtable.row_filters import RowSampleFilter

    sample = object()
    other_sample = object()
    row_filter1 = RowSampleFilter(sample)
    row_filter2 = RowSampleFilter(other_sample)
    assert row_filter1 != row_filter2


def test_row_sample_filter_to_pb():
    from google.cloud.bigtable.row_filters import RowSampleFilter

    sample = 0.25
    row_filter = RowSampleFilter(sample)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(row_sample_filter=sample)
    assert pb_val == expected_pb


def test_family_name_regex_filter_to_pb():
    from google.cloud.bigtable.row_filters import FamilyNameRegexFilter

    regex = "family-regex"
    row_filter = FamilyNameRegexFilter(regex)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(family_name_regex_filter=regex)
    assert pb_val == expected_pb


def test_column_qualifier_regext_filter_to_pb():
    from google.cloud.bigtable.row_filters import ColumnQualifierRegexFilter

    regex = b"column-regex"
    row_filter = ColumnQualifierRegexFilter(regex)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(column_qualifier_regex_filter=regex)
    assert pb_val == expected_pb


def test_timestamp_range_constructor():
    from google.cloud.bigtable.row_filters import TimestampRange

    start = object()
    end = object()
    time_range = TimestampRange(start=start, end=end)
    assert time_range.start is start
    assert time_range.end is end


def test_timestamp_range___eq__():
    from google.cloud.bigtable.row_filters import TimestampRange

    start = object()
    end = object()
    time_range1 = TimestampRange(start=start, end=end)
    time_range2 = TimestampRange(start=start, end=end)
    assert time_range1 == time_range2


def test_timestamp_range___eq__type_differ():
    from google.cloud.bigtable.row_filters import TimestampRange

    start = object()
    end = object()
    time_range1 = TimestampRange(start=start, end=end)
    time_range2 = object()
    assert not (time_range1 == time_range2)


def test_timestamp_range___ne__same_value():
    from google.cloud.bigtable.row_filters import TimestampRange

    start = object()
    end = object()
    time_range1 = TimestampRange(start=start, end=end)
    time_range2 = TimestampRange(start=start, end=end)
    assert not (time_range1 != time_range2)


def _timestamp_range_to_pb_helper(pb_kwargs, start=None, end=None):
    import datetime

    from google.cloud._helpers import _EPOCH

    from google.cloud.bigtable.row_filters import TimestampRange

    if start is not None:
        start = _EPOCH + datetime.timedelta(microseconds=start)
    if end is not None:
        end = _EPOCH + datetime.timedelta(microseconds=end)
    time_range = TimestampRange(start=start, end=end)
    expected_pb = _TimestampRangePB(**pb_kwargs)
    time_pb = time_range._to_pb()
    assert time_pb.start_timestamp_micros == expected_pb.start_timestamp_micros
    assert time_pb.end_timestamp_micros == expected_pb.end_timestamp_micros
    assert time_pb == expected_pb


def test_timestamp_range_to_pb():
    start_micros = 30871234
    end_micros = 12939371234
    start_millis = start_micros // 1000 * 1000
    assert start_millis == 30871000
    end_millis = end_micros // 1000 * 1000 + 1000
    assert end_millis == 12939372000
    pb_kwargs = {}
    pb_kwargs["start_timestamp_micros"] = start_millis
    pb_kwargs["end_timestamp_micros"] = end_millis
    _timestamp_range_to_pb_helper(pb_kwargs, start=start_micros, end=end_micros)


def test_timestamp_range_to_pb_start_only():
    # Makes sure already milliseconds granularity
    start_micros = 30871000
    start_millis = start_micros // 1000 * 1000
    assert start_millis == 30871000
    pb_kwargs = {}
    pb_kwargs["start_timestamp_micros"] = start_millis
    _timestamp_range_to_pb_helper(pb_kwargs, start=start_micros, end=None)


def test_timestamp_range_to_pb_end_only():
    # Makes sure already milliseconds granularity
    end_micros = 12939371000
    end_millis = end_micros // 1000 * 1000
    assert end_millis == 12939371000
    pb_kwargs = {}
    pb_kwargs["end_timestamp_micros"] = end_millis
    _timestamp_range_to_pb_helper(pb_kwargs, start=None, end=end_micros)


def test_timestamp_range_filter_constructor():
    from google.cloud.bigtable.row_filters import TimestampRangeFilter

    range_ = object()
    row_filter = TimestampRangeFilter(range_)
    assert row_filter.range_ is range_


def test_timestamp_range_filter___eq__type_differ():
    from google.cloud.bigtable.row_filters import TimestampRangeFilter

    range_ = object()
    row_filter1 = TimestampRangeFilter(range_)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_timestamp_range_filter___eq__same_value():
    from google.cloud.bigtable.row_filters import TimestampRangeFilter

    range_ = object()
    row_filter1 = TimestampRangeFilter(range_)
    row_filter2 = TimestampRangeFilter(range_)
    assert row_filter1 == row_filter2


def test_timestamp_range_filter___ne__():
    from google.cloud.bigtable.row_filters import TimestampRangeFilter

    range_ = object()
    other_range_ = object()
    row_filter1 = TimestampRangeFilter(range_)
    row_filter2 = TimestampRangeFilter(other_range_)
    assert row_filter1 != row_filter2


def test_timestamp_range_filter_to_pb():
    from google.cloud.bigtable.row_filters import TimestampRange, TimestampRangeFilter

    range_ = TimestampRange()
    row_filter = TimestampRangeFilter(range_)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(timestamp_range_filter=_TimestampRangePB())
    assert pb_val == expected_pb


def test_column_range_filter_constructor_defaults():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = object()
    row_filter = ColumnRangeFilter(column_family_id)
    assert row_filter.column_family_id is column_family_id
    assert row_filter.start_column is None
    assert row_filter.end_column is None
    assert row_filter.inclusive_start
    assert row_filter.inclusive_end


def test_column_range_filter_constructor_explicit():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = object()
    start_column = object()
    end_column = object()
    inclusive_start = object()
    inclusive_end = object()
    row_filter = ColumnRangeFilter(
        column_family_id,
        start_column=start_column,
        end_column=end_column,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    assert row_filter.column_family_id is column_family_id
    assert row_filter.start_column is start_column
    assert row_filter.end_column is end_column
    assert row_filter.inclusive_start is inclusive_start
    assert row_filter.inclusive_end is inclusive_end


def test_column_range_filter_constructor_bad_start():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = object()
    with pytest.raises(ValueError):
        ColumnRangeFilter(column_family_id, inclusive_start=True)


def test_column_range_filter_constructor_bad_end():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = object()
    with pytest.raises(ValueError):
        ColumnRangeFilter(column_family_id, inclusive_end=True)


def test_column_range_filter___eq__():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = object()
    start_column = object()
    end_column = object()
    inclusive_start = object()
    inclusive_end = object()
    row_filter1 = ColumnRangeFilter(
        column_family_id,
        start_column=start_column,
        end_column=end_column,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    row_filter2 = ColumnRangeFilter(
        column_family_id,
        start_column=start_column,
        end_column=end_column,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    assert row_filter1 == row_filter2


def test_column_range_filter___eq__type_differ():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = object()
    row_filter1 = ColumnRangeFilter(column_family_id)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_column_range_filter___ne__():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = object()
    other_column_family_id = object()
    start_column = object()
    end_column = object()
    inclusive_start = object()
    inclusive_end = object()
    row_filter1 = ColumnRangeFilter(
        column_family_id,
        start_column=start_column,
        end_column=end_column,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    row_filter2 = ColumnRangeFilter(
        other_column_family_id,
        start_column=start_column,
        end_column=end_column,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    assert row_filter1 != row_filter2


def test_column_range_filter_to_pb():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = "column-family-id"
    row_filter = ColumnRangeFilter(column_family_id)
    col_range_pb = _ColumnRangePB(family_name=column_family_id)
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter_to_pb_inclusive_start():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = "column-family-id"
    column = b"column"
    row_filter = ColumnRangeFilter(column_family_id, start_column=column)
    col_range_pb = _ColumnRangePB(
        family_name=column_family_id, start_qualifier_closed=column
    )
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter_to_pb_exclusive_start():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = "column-family-id"
    column = b"column"
    row_filter = ColumnRangeFilter(
        column_family_id, start_column=column, inclusive_start=False
    )
    col_range_pb = _ColumnRangePB(
        family_name=column_family_id, start_qualifier_open=column
    )
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter_to_pb_inclusive_end():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = "column-family-id"
    column = b"column"
    row_filter = ColumnRangeFilter(column_family_id, end_column=column)
    col_range_pb = _ColumnRangePB(
        family_name=column_family_id, end_qualifier_closed=column
    )
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter_to_pb_exclusive_end():
    from google.cloud.bigtable.row_filters import ColumnRangeFilter

    column_family_id = "column-family-id"
    column = b"column"
    row_filter = ColumnRangeFilter(
        column_family_id, end_column=column, inclusive_end=False
    )
    col_range_pb = _ColumnRangePB(
        family_name=column_family_id, end_qualifier_open=column
    )
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_value_regex_filter_to_pb_w_bytes():
    from google.cloud.bigtable.row_filters import ValueRegexFilter

    value = regex = b"value-regex"
    row_filter = ValueRegexFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_value_regex_filter_to_pb_w_str():
    from google.cloud.bigtable.row_filters import ValueRegexFilter

    value = "value-regex"
    regex = value.encode("ascii")
    row_filter = ValueRegexFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_value_bitmask_filter_to_pb_w_bytes():
    from google.cloud.bigtable.row_filters import ValueBitmaskFilter

    mask = b"value-mask"
    row_filter = ValueBitmaskFilter(mask)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_bitmask_filter=_ValueBitmaskPB(mask=mask))
    assert pb_val == expected_pb


def test_value_bitmask_filter_to_pb_w_str():
    from google.cloud.bigtable.row_filters import ValueBitmaskFilter

    mask = "value-mask"
    mask_bytes = mask.encode("ascii")
    row_filter = ValueBitmaskFilter(mask)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_bitmask_filter=_ValueBitmaskPB(mask=mask_bytes))
    assert pb_val == expected_pb


def test_exact_value_filter_to_pb_w_bytes():
    from google.cloud.bigtable.row_filters import ExactValueFilter

    value = regex = b"value-regex"
    row_filter = ExactValueFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_exact_value_filter_to_pb_w_str():
    from google.cloud.bigtable.row_filters import ExactValueFilter

    value = "value-regex"
    regex = value.encode("ascii")
    row_filter = ExactValueFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_exact_value_filter_to_pb_w_int():
    import struct

    from google.cloud.bigtable.row_filters import ExactValueFilter

    value = 1
    regex = struct.Struct(">q").pack(value)
    row_filter = ExactValueFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_value_range_filter_constructor_defaults():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    row_filter = ValueRangeFilter()

    assert row_filter.start_value is None
    assert row_filter.end_value is None
    assert row_filter.inclusive_start
    assert row_filter.inclusive_end


def test_value_range_filter_constructor_explicit():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    start_value = object()
    end_value = object()
    inclusive_start = object()
    inclusive_end = object()

    row_filter = ValueRangeFilter(
        start_value=start_value,
        end_value=end_value,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )

    assert row_filter.start_value is start_value
    assert row_filter.end_value is end_value
    assert row_filter.inclusive_start is inclusive_start
    assert row_filter.inclusive_end is inclusive_end


def test_value_range_filter_constructor_w_int_values():
    import struct

    from google.cloud.bigtable.row_filters import ValueRangeFilter

    start_value = 1
    end_value = 10

    row_filter = ValueRangeFilter(start_value=start_value, end_value=end_value)

    expected_start_value = struct.Struct(">q").pack(start_value)
    expected_end_value = struct.Struct(">q").pack(end_value)

    assert row_filter.start_value == expected_start_value
    assert row_filter.end_value == expected_end_value
    assert row_filter.inclusive_start
    assert row_filter.inclusive_end


def test_value_range_filter_constructor_bad_start():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    with pytest.raises(ValueError):
        ValueRangeFilter(inclusive_start=True)


def test_value_range_filter_constructor_bad_end():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    with pytest.raises(ValueError):
        ValueRangeFilter(inclusive_end=True)


def test_value_range_filter___eq__():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    start_value = object()
    end_value = object()
    inclusive_start = object()
    inclusive_end = object()
    row_filter1 = ValueRangeFilter(
        start_value=start_value,
        end_value=end_value,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    row_filter2 = ValueRangeFilter(
        start_value=start_value,
        end_value=end_value,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    assert row_filter1 == row_filter2


def test_value_range_filter___eq__type_differ():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    row_filter1 = ValueRangeFilter()
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_value_range_filter___ne__():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    start_value = object()
    other_start_value = object()
    end_value = object()
    inclusive_start = object()
    inclusive_end = object()
    row_filter1 = ValueRangeFilter(
        start_value=start_value,
        end_value=end_value,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    row_filter2 = ValueRangeFilter(
        start_value=other_start_value,
        end_value=end_value,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    assert row_filter1 != row_filter2


def test_value_range_filter_to_pb():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    row_filter = ValueRangeFilter()
    expected_pb = _RowFilterPB(value_range_filter=_ValueRangePB())
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter_to_pb_inclusive_start():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    value = b"some-value"
    row_filter = ValueRangeFilter(start_value=value)
    val_range_pb = _ValueRangePB(start_value_closed=value)
    expected_pb = _RowFilterPB(value_range_filter=val_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter_to_pb_exclusive_start():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    value = b"some-value"
    row_filter = ValueRangeFilter(start_value=value, inclusive_start=False)
    val_range_pb = _ValueRangePB(start_value_open=value)
    expected_pb = _RowFilterPB(value_range_filter=val_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter_to_pb_inclusive_end():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    value = b"some-value"
    row_filter = ValueRangeFilter(end_value=value)
    val_range_pb = _ValueRangePB(end_value_closed=value)
    expected_pb = _RowFilterPB(value_range_filter=val_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter_to_pb_exclusive_end():
    from google.cloud.bigtable.row_filters import ValueRangeFilter

    value = b"some-value"
    row_filter = ValueRangeFilter(end_value=value, inclusive_end=False)
    val_range_pb = _ValueRangePB(end_value_open=value)
    expected_pb = _RowFilterPB(value_range_filter=val_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_cell_count_constructor():
    num_cells = object()
    row_filter = _CellCountFilter(num_cells)
    assert row_filter.num_cells is num_cells


def test_cell_count___eq__type_differ():
    num_cells = object()
    row_filter1 = _CellCountFilter(num_cells)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_cell_count___eq__same_value():
    num_cells = object()
    row_filter1 = _CellCountFilter(num_cells)
    row_filter2 = _CellCountFilter(num_cells)
    assert row_filter1 == row_filter2


def test_cell_count___ne__same_value():
    num_cells = object()
    row_filter1 = _CellCountFilter(num_cells)
    row_filter2 = _CellCountFilter(num_cells)
    assert not (row_filter1 != row_filter2)


def test_cells_row_offset_filter_to_pb():
    from google.cloud.bigtable.row_filters import CellsRowOffsetFilter

    num_cells = 76
    row_filter = CellsRowOffsetFilter(num_cells)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(cells_per_row_offset_filter=num_cells)
    assert pb_val == expected_pb


def test_cells_row_limit_filter_to_pb():
    from google.cloud.bigtable.row_filters import CellsRowLimitFilter

    num_cells = 189
    row_filter = CellsRowLimitFilter(num_cells)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(cells_per_row_limit_filter=num_cells)
    assert pb_val == expected_pb


def test_cells_column_limit_filter_to_pb():
    from google.cloud.bigtable.row_filters import CellsColumnLimitFilter

    num_cells = 10
    row_filter = CellsColumnLimitFilter(num_cells)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(cells_per_column_limit_filter=num_cells)
    assert pb_val == expected_pb


def test_strip_value_transformer_filter_to_pb():
    from google.cloud.bigtable.row_filters import StripValueTransformerFilter

    flag = True
    row_filter = StripValueTransformerFilter(flag)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(strip_value_transformer=flag)
    assert pb_val == expected_pb


def test_apply_label_filter_constructor():
    from google.cloud.bigtable.row_filters import ApplyLabelFilter

    label = object()
    row_filter = ApplyLabelFilter(label)
    assert row_filter.label is label


def test_apply_label_filter___eq__type_differ():
    from google.cloud.bigtable.row_filters import ApplyLabelFilter

    label = object()
    row_filter1 = ApplyLabelFilter(label)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_apply_label_filter___eq__same_value():
    from google.cloud.bigtable.row_filters import ApplyLabelFilter

    label = object()
    row_filter1 = ApplyLabelFilter(label)
    row_filter2 = ApplyLabelFilter(label)
    assert row_filter1 == row_filter2


def test_apply_label_filter___ne__():
    from google.cloud.bigtable.row_filters import ApplyLabelFilter

    label = object()
    other_label = object()
    row_filter1 = ApplyLabelFilter(label)
    row_filter2 = ApplyLabelFilter(other_label)
    assert row_filter1 != row_filter2


def test_apply_label_filter_to_pb():
    from google.cloud.bigtable.row_filters import ApplyLabelFilter

    label = "label"
    row_filter = ApplyLabelFilter(label)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(apply_label_transformer=label)
    assert pb_val == expected_pb


def test_filter_combination_constructor_defaults():
    row_filter = _FilterCombination()
    assert row_filter.filters == []


def test_filter_combination_constructor_explicit():
    filters = object()
    row_filter = _FilterCombination(filters=filters)
    assert row_filter.filters is filters


def test_filter_combination___eq__():
    filters = object()
    row_filter1 = _FilterCombination(filters=filters)
    row_filter2 = _FilterCombination(filters=filters)
    assert row_filter1 == row_filter2


def test_filter_combination___eq__type_differ():
    filters = object()
    row_filter1 = _FilterCombination(filters=filters)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_filter_combination___ne__():
    filters = object()
    other_filters = object()
    row_filter1 = _FilterCombination(filters=filters)
    row_filter2 = _FilterCombination(filters=other_filters)
    assert row_filter1 != row_filter2


def test_row_filter_chain_to_pb():
    from google.cloud.bigtable.row_filters import (
        RowFilterChain,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_pb = row_filter1._to_pb()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_pb = row_filter2._to_pb()

    row_filter3 = RowFilterChain(filters=[row_filter1, row_filter2])
    filter_pb = row_filter3._to_pb()

    expected_pb = _RowFilterPB(
        chain=_RowFilterChainPB(filters=[row_filter1_pb, row_filter2_pb])
    )
    assert filter_pb == expected_pb


def test_row_filter_chain_to_pb_nested():
    from google.cloud.bigtable.row_filters import (
        CellsRowLimitFilter,
        RowFilterChain,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter2 = RowSampleFilter(0.25)

    row_filter3 = RowFilterChain(filters=[row_filter1, row_filter2])
    row_filter3_pb = row_filter3._to_pb()

    row_filter4 = CellsRowLimitFilter(11)
    row_filter4_pb = row_filter4._to_pb()

    row_filter5 = RowFilterChain(filters=[row_filter3, row_filter4])
    filter_pb = row_filter5._to_pb()

    expected_pb = _RowFilterPB(
        chain=_RowFilterChainPB(filters=[row_filter3_pb, row_filter4_pb])
    )
    assert filter_pb == expected_pb


def test_row_filter_union_to_pb():
    from google.cloud.bigtable.row_filters import (
        RowFilterUnion,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_pb = row_filter1._to_pb()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_pb = row_filter2._to_pb()

    row_filter3 = RowFilterUnion(filters=[row_filter1, row_filter2])
    filter_pb = row_filter3._to_pb()

    expected_pb = _RowFilterPB(
        interleave=_RowFilterInterleavePB(filters=[row_filter1_pb, row_filter2_pb])
    )
    assert filter_pb == expected_pb


def test_row_filter_union_to_pb_nested():
    from google.cloud.bigtable.row_filters import (
        CellsRowLimitFilter,
        RowFilterUnion,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter2 = RowSampleFilter(0.25)

    row_filter3 = RowFilterUnion(filters=[row_filter1, row_filter2])
    row_filter3_pb = row_filter3._to_pb()

    row_filter4 = CellsRowLimitFilter(11)
    row_filter4_pb = row_filter4._to_pb()

    row_filter5 = RowFilterUnion(filters=[row_filter3, row_filter4])
    filter_pb = row_filter5._to_pb()

    expected_pb = _RowFilterPB(
        interleave=_RowFilterInterleavePB(filters=[row_filter3_pb, row_filter4_pb])
    )
    assert filter_pb == expected_pb


def test_conditional_row_filter_constructor():
    from google.cloud.bigtable.row_filters import ConditionalRowFilter

    base_filter = object()
    true_filter = object()
    false_filter = object()
    cond_filter = ConditionalRowFilter(
        base_filter, true_filter=true_filter, false_filter=false_filter
    )
    assert cond_filter.base_filter is base_filter
    assert cond_filter.true_filter is true_filter
    assert cond_filter.false_filter is false_filter


def test_conditional_row_filter___eq__():
    from google.cloud.bigtable.row_filters import ConditionalRowFilter

    base_filter = object()
    true_filter = object()
    false_filter = object()
    cond_filter1 = ConditionalRowFilter(
        base_filter, true_filter=true_filter, false_filter=false_filter
    )
    cond_filter2 = ConditionalRowFilter(
        base_filter, true_filter=true_filter, false_filter=false_filter
    )
    assert cond_filter1 == cond_filter2


def test_conditional_row_filter___eq__type_differ():
    from google.cloud.bigtable.row_filters import ConditionalRowFilter

    base_filter = object()
    true_filter = object()
    false_filter = object()
    cond_filter1 = ConditionalRowFilter(
        base_filter, true_filter=true_filter, false_filter=false_filter
    )
    cond_filter2 = object()
    assert not (cond_filter1 == cond_filter2)


def test_conditional_row_filter___ne__():
    from google.cloud.bigtable.row_filters import ConditionalRowFilter

    base_filter = object()
    other_base_filter = object()
    true_filter = object()
    false_filter = object()
    cond_filter1 = ConditionalRowFilter(
        base_filter, true_filter=true_filter, false_filter=false_filter
    )
    cond_filter2 = ConditionalRowFilter(
        other_base_filter, true_filter=true_filter, false_filter=false_filter
    )
    assert cond_filter1 != cond_filter2


def test_conditional_row_filter_to_pb():
    from google.cloud.bigtable.row_filters import (
        CellsRowOffsetFilter,
        ConditionalRowFilter,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_pb = row_filter1._to_pb()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_pb = row_filter2._to_pb()

    row_filter3 = CellsRowOffsetFilter(11)
    row_filter3_pb = row_filter3._to_pb()

    row_filter4 = ConditionalRowFilter(
        row_filter1, true_filter=row_filter2, false_filter=row_filter3
    )
    filter_pb = row_filter4._to_pb()

    expected_pb = _RowFilterPB(
        condition=_RowFilterConditionPB(
            predicate_filter=row_filter1_pb,
            true_filter=row_filter2_pb,
            false_filter=row_filter3_pb,
        )
    )
    assert filter_pb == expected_pb


def test_conditional_row_filter_to_pb_true_only():
    from google.cloud.bigtable.row_filters import (
        ConditionalRowFilter,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_pb = row_filter1._to_pb()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_pb = row_filter2._to_pb()

    row_filter3 = ConditionalRowFilter(row_filter1, true_filter=row_filter2)
    filter_pb = row_filter3._to_pb()

    expected_pb = _RowFilterPB(
        condition=_RowFilterConditionPB(
            predicate_filter=row_filter1_pb, true_filter=row_filter2_pb
        )
    )
    assert filter_pb == expected_pb


def test_conditional_row_filter_to_pb_false_only():
    from google.cloud.bigtable.row_filters import (
        ConditionalRowFilter,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_pb = row_filter1._to_pb()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_pb = row_filter2._to_pb()

    row_filter3 = ConditionalRowFilter(row_filter1, false_filter=row_filter2)
    filter_pb = row_filter3._to_pb()

    expected_pb = _RowFilterPB(
        condition=_RowFilterConditionPB(
            predicate_filter=row_filter1_pb, false_filter=row_filter2_pb
        )
    )
    assert filter_pb == expected_pb


class _BoolFilter(_BaseBoolFilter):
    def _to_dict(self):
        pass


class _RegexFilter(_BaseRegexFilter):
    def _to_dict(self):
        pass


class _CellCountFilter(_BaseCellCountFilter):
    def _to_dict(self):
        pass


class _FilterCombination(_BaseFilterCombination):
    def _to_dict(self):
        pass


def _ColumnRangePB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.ColumnRange(*args, **kw)


def _RowFilterPB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.RowFilter(*args, **kw)


def _RowFilterChainPB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.RowFilter.Chain(*args, **kw)


def _RowFilterConditionPB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.RowFilter.Condition(*args, **kw)


def _RowFilterInterleavePB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.RowFilter.Interleave(*args, **kw)


def _TimestampRangePB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.TimestampRange(*args, **kw)


def _ValueRangePB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.ValueRange(*args, **kw)


def _ValueBitmaskPB(*args, **kw):
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    return data_v2_pb2.ValueBitmask(*args, **kw)


@pytest.mark.parametrize(
    "filter_instance",
    [
        row_filters.SinkFilter(True),
        row_filters.PassAllFilter(True),
        row_filters.BlockAllFilter(True),
        row_filters.RowKeyRegexFilter(b"key.*"),
        row_filters.RowSampleFilter(0.5),
        row_filters.FamilyNameRegexFilter("fam.*"),
        row_filters.ColumnQualifierRegexFilter(b"col.*"),
        row_filters.TimestampRangeFilter(row_filters.TimestampRange()),
        row_filters.ColumnRangeFilter("fam", start_column=b"a", end_column=b"b"),
        row_filters.ValueRegexFilter(b"val.*"),
        row_filters.ExactValueFilter(b"exact"),
        row_filters.ValueRangeFilter(start_value=b"a", end_value=b"b"),
        row_filters.ValueBitmaskFilter(b"mask"),
        row_filters.CellsRowOffsetFilter(5),
        row_filters.CellsRowLimitFilter(10),
        row_filters.CellsColumnLimitFilter(2),
        row_filters.StripValueTransformerFilter(True),
        row_filters.ApplyLabelFilter("label"),
        row_filters.RowFilterChain(filters=[row_filters.PassAllFilter(True)]),
        row_filters.RowFilterUnion(filters=[row_filters.PassAllFilter(True)]),
        row_filters.ConditionalRowFilter(base_filter=row_filters.PassAllFilter(True)),
    ],
)
def test_all_row_filters_to_pb_backwards_compatibility(filter_instance):
    assert hasattr(filter_instance, "to_pb")
    with pytest.deprecated_call():
        assert filter_instance.to_pb() == filter_instance._to_pb()


def test_timestamp_range_to_pb_backwards_compatibility():
    from datetime import datetime, timezone

    from google.cloud.bigtable.row_filters import TimestampRange

    start = datetime(2023, 1, 1, tzinfo=timezone.utc)
    end = datetime(2023, 1, 2, tzinfo=timezone.utc)
    tr = TimestampRange(start=start, end=end)
    assert hasattr(tr, "to_pb")
    with pytest.deprecated_call():
        assert tr.to_pb() == tr._to_pb()


def test_timestamp_range_filter_repr_and_cross_layer_eq():
    from datetime import datetime, timezone

    from google.cloud.bigtable import row_filters as classic_rf
    from google.cloud.bigtable.data import row_filters as data_rf

    t1 = datetime(2023, 1, 1, tzinfo=timezone.utc)
    t2 = datetime(2023, 1, 2, tzinfo=timezone.utc)
    tr = classic_rf.TimestampRange(start=t1, end=t2)
    classic_trf = classic_rf.TimestampRangeFilter(tr)

    assert repr(classic_trf) == f"TimestampRangeFilter(range_={tr!r})"
    assert (
        eval(
            repr(classic_trf),
            {
                "TimestampRangeFilter": classic_rf.TimestampRangeFilter,
                "TimestampRange": classic_rf.TimestampRange,
                "datetime": __import__("datetime"),
            },
        )
        == classic_trf
    )

    empty_trf = classic_rf.TimestampRangeFilter(None)
    assert repr(empty_trf) == "TimestampRangeFilter(range_=None)"

    data_trf = data_rf.TimestampRangeFilter(start=t1, end=t2)
    data_trf_from_range = data_rf.TimestampRangeFilter(tr)
    assert data_trf_from_range._to_pb() == classic_trf._to_pb()
    assert classic_trf == data_trf
    assert data_trf == classic_trf
    assert classic_trf.__eq__(data_trf) is True
    assert data_trf.__eq__(classic_trf) is True

    classic_crf = classic_rf.ColumnRangeFilter(
        "cf1", start_column=b"c1", end_column=b"c2"
    )
    data_crf = data_rf.ColumnRangeFilter(
        "cf1", start_qualifier=b"c1", end_qualifier=b"c2"
    )
    assert classic_crf == data_crf
    assert data_crf == classic_crf
    assert classic_crf.__eq__(data_crf) is True
    assert data_crf.__eq__(classic_crf) is True

    classic_cond = classic_rf.ConditionalRowFilter(
        classic_rf.PassAllFilter(True),
        true_filter=classic_rf.StripValueTransformerFilter(True),
    )
    data_cond = data_rf.ConditionalRowFilter(
        data_rf.PassAllFilter(True),
        true_filter=data_rf.StripValueTransformerFilter(True),
    )
    assert classic_cond == data_cond
    assert data_cond == classic_cond
    assert classic_cond.__eq__(data_cond) is True
    assert data_cond.__eq__(classic_cond) is True

    assert classic_rf.ValueRegexFilter(b"abc") != classic_rf.ExactValueFilter(b"abc")
    assert classic_rf.ExactValueFilter(b"abc") != classic_rf.ValueRegexFilter(b"abc")
