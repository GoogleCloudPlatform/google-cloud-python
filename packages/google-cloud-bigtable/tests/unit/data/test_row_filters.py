# Copyright 2023 Google LLC
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


def test_abstract_class_constructors():
    from google.cloud.bigtable.data.row_filters import (
        RowFilter,
        _BoolFilter,
        _CellCountFilter,
        _FilterCombination,
    )

    with pytest.raises(TypeError):
        RowFilter()
    with pytest.raises(TypeError):
        _BoolFilter(False)
    with pytest.raises(TypeError):
        _FilterCombination([])
    with pytest.raises(TypeError):
        _CellCountFilter(0)


def test_bool_filter_constructor():
    for FilterType in _get_bool_filters():
        flag = True
        row_filter = FilterType(flag)
        assert row_filter.flag is flag


def test_bool_filter___eq__type_differ():
    for FilterType in _get_bool_filters():
        flag = object()
        row_filter1 = FilterType(flag)
        row_filter2 = object()
        assert not (row_filter1 == row_filter2)


def test_bool_filter___eq__same_value():
    for FilterType in _get_bool_filters():
        flag = object()
        row_filter1 = FilterType(flag)
        row_filter2 = FilterType(flag)
        assert row_filter1 == row_filter2


def test_bool_filter___ne__same_value():
    for FilterType in _get_bool_filters():
        flag = object()
        row_filter1 = FilterType(flag)
        row_filter2 = FilterType(flag)
        assert not (row_filter1 != row_filter2)


def test_sink_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import SinkFilter

    flag = True
    row_filter = SinkFilter(flag)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(sink=flag)
    assert pb_val == expected_pb


def test_sink_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import SinkFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    flag = True
    row_filter = SinkFilter(flag)
    expected_dict = {"sink": flag}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_sink_filter___repr__():
    from google.cloud.bigtable.data.row_filters import SinkFilter

    flag = True
    row_filter = SinkFilter(flag)
    assert repr(row_filter) == "SinkFilter(flag={})".format(flag)
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_pass_all_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import PassAllFilter

    flag = True
    row_filter = PassAllFilter(flag)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(pass_all_filter=flag)
    assert pb_val == expected_pb


def test_pass_all_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import PassAllFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    flag = True
    row_filter = PassAllFilter(flag)
    expected_dict = {"pass_all_filter": flag}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_pass_all_filter___repr__():
    from google.cloud.bigtable.data.row_filters import PassAllFilter

    flag = True
    row_filter = PassAllFilter(flag)
    assert repr(row_filter) == "PassAllFilter(flag={})".format(flag)
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_block_all_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import BlockAllFilter

    flag = True
    row_filter = BlockAllFilter(flag)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(block_all_filter=flag)
    assert pb_val == expected_pb


def test_block_all_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import BlockAllFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    flag = True
    row_filter = BlockAllFilter(flag)
    expected_dict = {"block_all_filter": flag}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_block_all_filter___repr__():
    from google.cloud.bigtable.data.row_filters import BlockAllFilter

    flag = True
    row_filter = BlockAllFilter(flag)
    assert repr(row_filter) == "BlockAllFilter(flag={})".format(flag)
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_regex_filterconstructor():
    for FilterType in _get_regex_filters():
        regex = b"abc"
        row_filter = FilterType(regex)
        assert row_filter.regex == regex


def test_regex_filterconstructor_non_bytes():
    for FilterType in _get_regex_filters():
        regex = "abc"
        row_filter = FilterType(regex)
        assert row_filter.regex == b"abc"


def test_regex_filter__eq__type_differ():
    for FilterType in _get_regex_filters():
        regex = b"def-rgx"
        row_filter1 = FilterType(regex)
        row_filter2 = object()
        assert not (row_filter1 == row_filter2)


def test_regex_filter__eq__same_value():
    for FilterType in _get_regex_filters():
        regex = b"trex-regex"
        row_filter1 = FilterType(regex)
        row_filter2 = FilterType(regex)
        assert row_filter1 == row_filter2


def test_regex_filter__ne__same_value():
    for FilterType in _get_regex_filters():
        regex = b"abc"
        row_filter1 = FilterType(regex)
        row_filter2 = FilterType(regex)
        assert not (row_filter1 != row_filter2)


def test_row_key_regex_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import RowKeyRegexFilter

    regex = b"row-key-regex"
    row_filter = RowKeyRegexFilter(regex)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(row_key_regex_filter=regex)
    assert pb_val == expected_pb


def test_row_key_regex_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import RowKeyRegexFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    regex = b"row-key-regex"
    row_filter = RowKeyRegexFilter(regex)
    expected_dict = {"row_key_regex_filter": regex}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_row_key_regex_filter___repr__():
    from google.cloud.bigtable.data.row_filters import RowKeyRegexFilter

    regex = b"row-key-regex"
    row_filter = RowKeyRegexFilter(regex)
    assert repr(row_filter) == "RowKeyRegexFilter(regex={})".format(regex)
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_row_sample_filter_constructor():
    from google.cloud.bigtable.data.row_filters import RowSampleFilter

    sample = object()
    row_filter = RowSampleFilter(sample)
    assert row_filter.sample is sample


def test_row_sample_filter___eq__type_differ():
    from google.cloud.bigtable.data.row_filters import RowSampleFilter

    sample = object()
    row_filter1 = RowSampleFilter(sample)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_row_sample_filter___eq__same_value():
    from google.cloud.bigtable.data.row_filters import RowSampleFilter

    sample = object()
    row_filter1 = RowSampleFilter(sample)
    row_filter2 = RowSampleFilter(sample)
    assert row_filter1 == row_filter2


def test_row_sample_filter___ne__():
    from google.cloud.bigtable.data.row_filters import RowSampleFilter

    sample = object()
    other_sample = object()
    row_filter1 = RowSampleFilter(sample)
    row_filter2 = RowSampleFilter(other_sample)
    assert row_filter1 != row_filter2


def test_row_sample_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import RowSampleFilter

    sample = 0.25
    row_filter = RowSampleFilter(sample)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(row_sample_filter=sample)
    assert pb_val == expected_pb


def test_row_sample_filter___repr__():
    from google.cloud.bigtable.data.row_filters import RowSampleFilter

    sample = 0.25
    row_filter = RowSampleFilter(sample)
    assert repr(row_filter) == "RowSampleFilter(sample={})".format(sample)
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_family_name_regex_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import FamilyNameRegexFilter

    regex = "family-regex"
    row_filter = FamilyNameRegexFilter(regex)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(family_name_regex_filter=regex)
    assert pb_val == expected_pb


def test_family_name_regex_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import FamilyNameRegexFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    regex = "family-regex"
    row_filter = FamilyNameRegexFilter(regex)
    expected_dict = {"family_name_regex_filter": regex.encode()}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_family_name_regex_filter___repr__():
    from google.cloud.bigtable.data.row_filters import FamilyNameRegexFilter

    regex = "family-regex"
    row_filter = FamilyNameRegexFilter(regex)
    expected = "FamilyNameRegexFilter(regex=b'family-regex')"
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_column_qualifier_regex_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import ColumnQualifierRegexFilter

    regex = b"column-regex"
    row_filter = ColumnQualifierRegexFilter(regex)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(column_qualifier_regex_filter=regex)
    assert pb_val == expected_pb


def test_column_qualifier_regex_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import ColumnQualifierRegexFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    regex = b"column-regex"
    row_filter = ColumnQualifierRegexFilter(regex)
    expected_dict = {"column_qualifier_regex_filter": regex}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_column_qualifier_regex_filter___repr__():
    from google.cloud.bigtable.data.row_filters import ColumnQualifierRegexFilter

    regex = b"column-regex"
    row_filter = ColumnQualifierRegexFilter(regex)
    assert repr(row_filter) == "ColumnQualifierRegexFilter(regex={})".format(regex)
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_timestamp_range_constructor():
    from google.cloud.bigtable.data.row_filters import TimestampRange

    start = object()
    end = object()
    time_range = TimestampRange(start=start, end=end)
    assert time_range.start is start
    assert time_range.end is end


def test_timestamp_range___eq__():
    from google.cloud.bigtable.data.row_filters import TimestampRange

    start = object()
    end = object()
    time_range1 = TimestampRange(start=start, end=end)
    time_range2 = TimestampRange(start=start, end=end)
    assert time_range1 == time_range2


def test_timestamp_range___eq__type_differ():
    from google.cloud.bigtable.data.row_filters import TimestampRange

    start = object()
    end = object()
    time_range1 = TimestampRange(start=start, end=end)
    time_range2 = object()
    assert not (time_range1 == time_range2)


def test_timestamp_range___ne__same_value():
    from google.cloud.bigtable.data.row_filters import TimestampRange

    start = object()
    end = object()
    time_range1 = TimestampRange(start=start, end=end)
    time_range2 = TimestampRange(start=start, end=end)
    assert not (time_range1 != time_range2)


def _timestamp_range_to_pb_helper(pb_kwargs, start=None, end=None):
    import datetime

    from google.cloud._helpers import _EPOCH

    from google.cloud.bigtable.data.row_filters import TimestampRange

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


def test_timestamp_range_to_dict():
    import datetime

    from google.cloud.bigtable.data.row_filters import TimestampRange
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter = TimestampRange(
        start=datetime.datetime(2019, 1, 1), end=datetime.datetime(2019, 1, 2)
    )
    expected_dict = {
        "start_timestamp_micros": 1546300800000000,
        "end_timestamp_micros": 1546387200000000,
    }
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.TimestampRange(**expected_dict) == expected_pb_value


def test_timestamp_range_to_pb_start_only():
    # Makes sure already milliseconds granularity
    start_micros = 30871000
    start_millis = start_micros // 1000 * 1000
    assert start_millis == 30871000
    pb_kwargs = {}
    pb_kwargs["start_timestamp_micros"] = start_millis
    _timestamp_range_to_pb_helper(pb_kwargs, start=start_micros, end=None)


def test_timestamp_range_to_dict_start_only():
    import datetime

    from google.cloud.bigtable.data.row_filters import TimestampRange
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter = TimestampRange(start=datetime.datetime(2019, 1, 1))
    expected_dict = {"start_timestamp_micros": 1546300800000000}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.TimestampRange(**expected_dict) == expected_pb_value


def test_timestamp_range_to_pb_end_only():
    # Makes sure already milliseconds granularity
    end_micros = 12939371000
    end_millis = end_micros // 1000 * 1000
    assert end_millis == 12939371000
    pb_kwargs = {}
    pb_kwargs["end_timestamp_micros"] = end_millis
    _timestamp_range_to_pb_helper(pb_kwargs, start=None, end=end_micros)


def test_timestamp_range_to_dict_end_only():
    import datetime

    from google.cloud.bigtable.data.row_filters import TimestampRange
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter = TimestampRange(end=datetime.datetime(2019, 1, 2))
    expected_dict = {"end_timestamp_micros": 1546387200000000}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.TimestampRange(**expected_dict) == expected_pb_value


def timestamp_range___repr__():
    from google.cloud.bigtable.data.row_filters import TimestampRange

    start = object()
    end = object()
    time_range = TimestampRange(start=start, end=end)
    assert repr(time_range) == "TimestampRange(start={}, end={})".format(start, end)
    assert repr(time_range) == str(time_range)
    assert eval(repr(time_range)) == time_range


def test_timestamp_range_filter___eq__type_differ():
    from google.cloud.bigtable.data.row_filters import TimestampRangeFilter

    range_ = object()
    row_filter1 = TimestampRangeFilter(range_)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_timestamp_range_filter___eq__same_value():
    from google.cloud.bigtable.data.row_filters import TimestampRangeFilter

    range_ = object()
    row_filter1 = TimestampRangeFilter(range_)
    row_filter2 = TimestampRangeFilter(range_)
    assert row_filter1 == row_filter2


def test_timestamp_range_filter___ne__():
    from google.cloud.bigtable.data.row_filters import TimestampRangeFilter

    range_ = object()
    other_range_ = object()
    row_filter1 = TimestampRangeFilter(range_)
    row_filter2 = TimestampRangeFilter(other_range_)
    assert row_filter1 != row_filter2


def test_timestamp_range_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import TimestampRangeFilter

    row_filter = TimestampRangeFilter()
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(timestamp_range_filter=_TimestampRangePB())
    assert pb_val == expected_pb


def test_timestamp_range_filter_to_dict():
    import datetime

    from google.cloud.bigtable.data.row_filters import TimestampRangeFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter = TimestampRangeFilter(
        start=datetime.datetime(2019, 1, 1), end=datetime.datetime(2019, 1, 2)
    )
    expected_dict = {
        "timestamp_range_filter": {
            "start_timestamp_micros": 1546300800000000,
            "end_timestamp_micros": 1546387200000000,
        }
    }
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_timestamp_range_filter_empty_to_dict():
    from google.cloud.bigtable.data.row_filters import TimestampRangeFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter = TimestampRangeFilter()
    expected_dict = {"timestamp_range_filter": {}}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_timestamp_range_filter___repr__():
    import datetime

    from google.cloud.bigtable.data.row_filters import TimestampRangeFilter

    start = datetime.datetime(2019, 1, 1)
    end = datetime.datetime(2019, 1, 2)
    row_filter = TimestampRangeFilter(start, end)
    assert (
        repr(row_filter)
        == f"TimestampRangeFilter(start={repr(start)}, end={repr(end)})"
    )
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_column_range_filter_constructor_defaults():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = object()
    row_filter = ColumnRangeFilter(family_id)
    assert row_filter.family_id is family_id
    assert row_filter.start_qualifier is None
    assert row_filter.end_qualifier is None
    assert row_filter.inclusive_start
    assert row_filter.inclusive_end


def test_column_range_filter_constructor_explicit():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = object()
    start_qualifier = object()
    end_qualifier = object()
    inclusive_start = object()
    inclusive_end = object()
    row_filter = ColumnRangeFilter(
        family_id,
        start_qualifier=start_qualifier,
        end_qualifier=end_qualifier,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    assert row_filter.family_id is family_id
    assert row_filter.start_qualifier is start_qualifier
    assert row_filter.end_qualifier is end_qualifier
    assert row_filter.inclusive_start is inclusive_start
    assert row_filter.inclusive_end is inclusive_end


def test_column_range_filter_constructor_():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = object()
    with pytest.raises(ValueError):
        ColumnRangeFilter(family_id, inclusive_start=True)


def test_column_range_filter_constructor_bad_end():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = object()
    with pytest.raises(ValueError):
        ColumnRangeFilter(family_id, inclusive_end=True)


def test_column_range_filter___eq__():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = object()
    start_qualifier = object()
    end_qualifier = object()
    inclusive_start = object()
    inclusive_end = object()
    row_filter1 = ColumnRangeFilter(
        family_id,
        start_qualifier=start_qualifier,
        end_qualifier=end_qualifier,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    row_filter2 = ColumnRangeFilter(
        family_id,
        start_qualifier=start_qualifier,
        end_qualifier=end_qualifier,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    assert row_filter1 == row_filter2


def test_column_range_filter___eq__type_differ():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = object()
    row_filter1 = ColumnRangeFilter(family_id)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_column_range_filter___ne__():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = object()
    other_family_id = object()
    start_qualifier = object()
    end_qualifier = object()
    inclusive_start = object()
    inclusive_end = object()
    row_filter1 = ColumnRangeFilter(
        family_id,
        start_qualifier=start_qualifier,
        end_qualifier=end_qualifier,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    row_filter2 = ColumnRangeFilter(
        other_family_id,
        start_qualifier=start_qualifier,
        end_qualifier=end_qualifier,
        inclusive_start=inclusive_start,
        inclusive_end=inclusive_end,
    )
    assert row_filter1 != row_filter2


def test_column_range_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = "column-family-id"
    row_filter = ColumnRangeFilter(family_id)
    col_range_pb = _ColumnRangePB(family_name=family_id)
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    family_id = "column-family-id"
    row_filter = ColumnRangeFilter(family_id)
    expected_dict = {"column_range_filter": {"family_name": family_id}}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_column_range_filter_to_pb_inclusive_start():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = "column-family-id"
    column = b"column"
    row_filter = ColumnRangeFilter(family_id, start_qualifier=column)
    col_range_pb = _ColumnRangePB(family_name=family_id, start_qualifier_closed=column)
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter_to_pb_exclusive_start():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = "column-family-id"
    column = b"column"
    row_filter = ColumnRangeFilter(
        family_id, start_qualifier=column, inclusive_start=False
    )
    col_range_pb = _ColumnRangePB(family_name=family_id, start_qualifier_open=column)
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter_to_pb_inclusive_end():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = "column-family-id"
    column = b"column"
    row_filter = ColumnRangeFilter(family_id, end_qualifier=column)
    col_range_pb = _ColumnRangePB(family_name=family_id, end_qualifier_closed=column)
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter_to_pb_exclusive_end():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = "column-family-id"
    column = b"column"
    row_filter = ColumnRangeFilter(family_id, end_qualifier=column, inclusive_end=False)
    col_range_pb = _ColumnRangePB(family_name=family_id, end_qualifier_open=column)
    expected_pb = _RowFilterPB(column_range_filter=col_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_column_range_filter___repr__():
    from google.cloud.bigtable.data.row_filters import ColumnRangeFilter

    family_id = "column-family-id"
    start_qualifier = b"column"
    end_qualifier = b"column2"
    row_filter = ColumnRangeFilter(family_id, start_qualifier, end_qualifier)
    expected = "ColumnRangeFilter(family_id='column-family-id', start_qualifier=b'column', end_qualifier=b'column2', inclusive_start=True, inclusive_end=True)"
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_value_regex_filter_to_pb_w_bytes():
    from google.cloud.bigtable.data.row_filters import ValueRegexFilter

    value = regex = b"value-regex"
    row_filter = ValueRegexFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_value_regex_filter_to_dict_w_bytes():
    from google.cloud.bigtable.data.row_filters import ValueRegexFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    value = regex = b"value-regex"
    row_filter = ValueRegexFilter(value)
    expected_dict = {"value_regex_filter": regex}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_value_regex_filter_to_pb_w_str():
    from google.cloud.bigtable.data.row_filters import ValueRegexFilter

    value = "value-regex"
    regex = value.encode("ascii")
    row_filter = ValueRegexFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_value_regex_filter_to_dict_w_str():
    from google.cloud.bigtable.data.row_filters import ValueRegexFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    value = "value-regex"
    regex = value.encode("ascii")
    row_filter = ValueRegexFilter(value)
    expected_dict = {"value_regex_filter": regex}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_value_regex_filter___repr__():
    from google.cloud.bigtable.data.row_filters import ValueRegexFilter

    value = "value-regex"
    row_filter = ValueRegexFilter(value)
    expected = "ValueRegexFilter(regex=b'value-regex')"
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_value_regex_filter_not_equal_to_literal_value_filter():
    from google.cloud.bigtable.data.row_filters import (
        LiteralValueFilter,
        ValueRegexFilter,
    )

    vrf = ValueRegexFilter(b"abc")
    lvf = LiteralValueFilter(b"abc")
    assert vrf != lvf
    assert lvf != vrf


def test_literal_value_filter_to_pb_w_bytes():
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter

    value = regex = b"value_regex"
    row_filter = LiteralValueFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_literal_value_filter_to_dict_w_bytes():
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    value = regex = b"value_regex"
    row_filter = LiteralValueFilter(value)
    expected_dict = {"value_regex_filter": regex}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_literal_value_filter_to_pb_w_str():
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter

    value = "value_regex"
    regex = value.encode("ascii")
    row_filter = LiteralValueFilter(value)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=regex)
    assert pb_val == expected_pb


def test_literal_value_filter_to_dict_w_str():
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    value = "value_regex"
    regex = value.encode("ascii")
    row_filter = LiteralValueFilter(value)
    expected_dict = {"value_regex_filter": regex}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


@pytest.mark.parametrize(
    "value,expected_byte_string",
    [
        # null bytes are encoded as "\x00" in ascii characters
        # others are just prefixed with "\"
        (0, b"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00"),
        (1, b"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\\x01"),
        (
            68,
            b"\\x00\\x00\\x00\\x00\\x00\\x00\\x00D",
        ),  # bytes that encode to alphanum are not escaped
        (570, b"\\x00\\x00\\x00\\x00\\x00\\x00\\\x02\\\x3a"),
        (2852126720, b"\\x00\\x00\\x00\\x00\xaa\\x00\\x00\\x00"),
        (-1, b"\xff\xff\xff\xff\xff\xff\xff\xff"),
        (-1096642724096, b"\xff\xff\xff\\x00\xaa\xff\xff\\x00"),
    ],
)
def test_literal_value_filter_w_int(value, expected_byte_string):
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter = LiteralValueFilter(value)
    # test pb
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(value_regex_filter=expected_byte_string)
    assert pb_val == expected_pb
    # test dict
    expected_dict = {"value_regex_filter": expected_byte_string}
    assert row_filter._to_dict() == expected_dict
    assert data_v2_pb2.RowFilter(**expected_dict) == pb_val


def test_literal_value_filter___repr__():
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter

    value = "value_regex"
    row_filter = LiteralValueFilter(value)
    expected = "LiteralValueFilter(value=b'value_regex')"
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_value_range_filter_constructor_defaults():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    row_filter = ValueRangeFilter()

    assert row_filter.start_value is None
    assert row_filter.end_value is None
    assert row_filter.inclusive_start
    assert row_filter.inclusive_end


def test_value_range_filter_constructor_explicit():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

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

    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

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
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    with pytest.raises(ValueError):
        ValueRangeFilter(inclusive_start=True)


def test_value_range_filter_constructor_bad_end():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    with pytest.raises(ValueError):
        ValueRangeFilter(inclusive_end=True)


def test_value_range_filter___eq__():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

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
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    row_filter1 = ValueRangeFilter()
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_value_range_filter___ne__():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

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
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    row_filter = ValueRangeFilter()
    expected_pb = _RowFilterPB(value_range_filter=_ValueRangePB())
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter = ValueRangeFilter()
    expected_dict = {"value_range_filter": {}}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_value_range_filter_to_pb_inclusive_start():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    value = b"some-value"
    row_filter = ValueRangeFilter(start_value=value)
    val_range_pb = _ValueRangePB(start_value_closed=value)
    expected_pb = _RowFilterPB(value_range_filter=val_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter_to_pb_exclusive_start():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    value = b"some-value"
    row_filter = ValueRangeFilter(start_value=value, inclusive_start=False)
    val_range_pb = _ValueRangePB(start_value_open=value)
    expected_pb = _RowFilterPB(value_range_filter=val_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter_to_pb_inclusive_end():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    value = b"some-value"
    row_filter = ValueRangeFilter(end_value=value)
    val_range_pb = _ValueRangePB(end_value_closed=value)
    expected_pb = _RowFilterPB(value_range_filter=val_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter_to_pb_exclusive_end():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    value = b"some-value"
    row_filter = ValueRangeFilter(end_value=value, inclusive_end=False)
    val_range_pb = _ValueRangePB(end_value_open=value)
    expected_pb = _RowFilterPB(value_range_filter=val_range_pb)
    assert row_filter._to_pb() == expected_pb


def test_value_range_filter___repr__():
    from google.cloud.bigtable.data.row_filters import ValueRangeFilter

    start_value = b"some-value"
    end_value = b"some-other-value"
    row_filter = ValueRangeFilter(
        start_value=start_value, end_value=end_value, inclusive_end=False
    )
    expected = "ValueRangeFilter(start_value=b'some-value', end_value=b'some-other-value', inclusive_start=True, inclusive_end=False)"
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_cell_count_constructor():
    for FilerType in _get_cell_count_filters():
        num_cells = object()
        row_filter = FilerType(num_cells)
        assert row_filter.num_cells is num_cells


def test_cell_count___eq__type_differ():
    for FilerType in _get_cell_count_filters():
        num_cells = object()
        row_filter1 = FilerType(num_cells)
        row_filter2 = object()
        assert not (row_filter1 == row_filter2)


def test_cell_count___eq__same_value():
    for FilerType in _get_cell_count_filters():
        num_cells = object()
        row_filter1 = FilerType(num_cells)
        row_filter2 = FilerType(num_cells)
        assert row_filter1 == row_filter2


def test_cell_count___ne__same_value():
    for FilerType in _get_cell_count_filters():
        num_cells = object()
        row_filter1 = FilerType(num_cells)
        row_filter2 = FilerType(num_cells)
        assert not (row_filter1 != row_filter2)


def test_cells_row_offset_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import CellsRowOffsetFilter

    num_cells = 76
    row_filter = CellsRowOffsetFilter(num_cells)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(cells_per_row_offset_filter=num_cells)
    assert pb_val == expected_pb


def test_cells_row_offset_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import CellsRowOffsetFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    num_cells = 76
    row_filter = CellsRowOffsetFilter(num_cells)
    expected_dict = {"cells_per_row_offset_filter": num_cells}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_cells_row_offset_filter___repr__():
    from google.cloud.bigtable.data.row_filters import CellsRowOffsetFilter

    num_cells = 76
    row_filter = CellsRowOffsetFilter(num_cells)
    expected = "CellsRowOffsetFilter(num_cells={})".format(num_cells)
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_cells_row_limit_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import CellsRowLimitFilter

    num_cells = 189
    row_filter = CellsRowLimitFilter(num_cells)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(cells_per_row_limit_filter=num_cells)
    assert pb_val == expected_pb


def test_cells_row_limit_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import CellsRowLimitFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    num_cells = 189
    row_filter = CellsRowLimitFilter(num_cells)
    expected_dict = {"cells_per_row_limit_filter": num_cells}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_cells_row_limit_filter___repr__():
    from google.cloud.bigtable.data.row_filters import CellsRowLimitFilter

    num_cells = 189
    row_filter = CellsRowLimitFilter(num_cells)
    expected = "CellsRowLimitFilter(num_cells={})".format(num_cells)
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_cells_column_limit_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import CellsColumnLimitFilter

    num_cells = 10
    row_filter = CellsColumnLimitFilter(num_cells)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(cells_per_column_limit_filter=num_cells)
    assert pb_val == expected_pb


def test_cells_column_limit_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import CellsColumnLimitFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    num_cells = 10
    row_filter = CellsColumnLimitFilter(num_cells)
    expected_dict = {"cells_per_column_limit_filter": num_cells}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_cells_column_limit_filter___repr__():
    from google.cloud.bigtable.data.row_filters import CellsColumnLimitFilter

    num_cells = 10
    row_filter = CellsColumnLimitFilter(num_cells)
    expected = "CellsColumnLimitFilter(num_cells={})".format(num_cells)
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_strip_value_transformer_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import StripValueTransformerFilter

    flag = True
    row_filter = StripValueTransformerFilter(flag)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(strip_value_transformer=flag)
    assert pb_val == expected_pb


def test_strip_value_transformer_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import StripValueTransformerFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    flag = True
    row_filter = StripValueTransformerFilter(flag)
    expected_dict = {"strip_value_transformer": flag}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_strip_value_transformer_filter___repr__():
    from google.cloud.bigtable.data.row_filters import StripValueTransformerFilter

    flag = True
    row_filter = StripValueTransformerFilter(flag)
    expected = "StripValueTransformerFilter(flag={})".format(flag)
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_apply_label_filter_constructor():
    from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

    label = object()
    row_filter = ApplyLabelFilter(label)
    assert row_filter.label is label


def test_apply_label_filter___eq__type_differ():
    from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

    label = object()
    row_filter1 = ApplyLabelFilter(label)
    row_filter2 = object()
    assert not (row_filter1 == row_filter2)


def test_apply_label_filter___eq__same_value():
    from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

    label = object()
    row_filter1 = ApplyLabelFilter(label)
    row_filter2 = ApplyLabelFilter(label)
    assert row_filter1 == row_filter2


def test_apply_label_filter___ne__():
    from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

    label = object()
    other_label = object()
    row_filter1 = ApplyLabelFilter(label)
    row_filter2 = ApplyLabelFilter(other_label)
    assert row_filter1 != row_filter2


def test_apply_label_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

    label = "label"
    row_filter = ApplyLabelFilter(label)
    pb_val = row_filter._to_pb()
    expected_pb = _RowFilterPB(apply_label_transformer=label)
    assert pb_val == expected_pb


def test_apply_label_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import ApplyLabelFilter
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    label = "label"
    row_filter = ApplyLabelFilter(label)
    expected_dict = {"apply_label_transformer": label}
    assert row_filter._to_dict() == expected_dict
    expected_pb_value = row_filter._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_apply_label_filter___repr__():
    from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

    label = "label"
    row_filter = ApplyLabelFilter(label)
    expected = "ApplyLabelFilter(label={})".format(label)
    assert repr(row_filter) == expected
    assert repr(row_filter) == str(row_filter)
    assert eval(repr(row_filter)) == row_filter


def test_filter_combination_constructor_defaults():
    for FilterType in _get_filter_combination_filters():
        row_filter = FilterType()
        assert row_filter.filters == []


def test_filter_combination_constructor_explicit():
    for FilterType in _get_filter_combination_filters():
        filters = object()
        row_filter = FilterType(filters=filters)
        assert row_filter.filters is filters


def test_filter_combination___eq__():
    for FilterType in _get_filter_combination_filters():
        filters = object()
        row_filter1 = FilterType(filters=filters)
        row_filter2 = FilterType(filters=filters)
        assert row_filter1 == row_filter2


def test_filter_combination___eq__type_differ():
    for FilterType in _get_filter_combination_filters():
        filters = object()
        row_filter1 = FilterType(filters=filters)
        row_filter2 = object()
        assert not (row_filter1 == row_filter2)


def test_filter_combination___ne__():
    for FilterType in _get_filter_combination_filters():
        filters = object()
        other_filters = object()
        row_filter1 = FilterType(filters=filters)
        row_filter2 = FilterType(filters=other_filters)
        assert row_filter1 != row_filter2


def test_filter_combination_len():
    for FilterType in _get_filter_combination_filters():
        filters = [object(), object()]
        row_filter = FilterType(filters=filters)
        assert len(row_filter) == len(filters)


def test_filter_combination_iter():
    for FilterType in _get_filter_combination_filters():
        filters = [object(), object()]
        row_filter = FilterType(filters=filters)
        assert list(iter(row_filter)) == filters
        for filter_, expected in zip(row_filter, filters):
            assert filter_ is expected


def test_filter_combination___getitem__():
    for FilterType in _get_filter_combination_filters():
        filters = [object(), object()]
        row_filter = FilterType(filters=filters)
        row_filter[0] is filters[0]
        row_filter[1] is filters[1]
        with pytest.raises(IndexError):
            row_filter[2]
        row_filter[:] is filters[:]


def test_filter_combination___str__():
    from google.cloud.bigtable.data.row_filters import PassAllFilter

    for FilterType in _get_filter_combination_filters():
        filters = [PassAllFilter(True), PassAllFilter(False)]
        row_filter = FilterType(filters=filters)
        expected = (
            "([\n    PassAllFilter(flag=True),\n    PassAllFilter(flag=False),\n])"
        )
        assert expected in str(row_filter)


def test_row_filter_chain_to_pb():
    from google.cloud.bigtable.data.row_filters import (
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


def test_row_filter_chain_to_dict():
    from google.cloud.bigtable.data.row_filters import (
        RowFilterChain,
        RowSampleFilter,
        StripValueTransformerFilter,
    )
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_dict = row_filter1._to_dict()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_dict = row_filter2._to_dict()

    row_filter3 = RowFilterChain(filters=[row_filter1, row_filter2])
    filter_dict = row_filter3._to_dict()

    expected_dict = {"chain": {"filters": [row_filter1_dict, row_filter2_dict]}}
    assert filter_dict == expected_dict
    expected_pb_value = row_filter3._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_row_filter_chain_to_pb_nested():
    from google.cloud.bigtable.data.row_filters import (
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


def test_row_filter_chain_to_dict_nested():
    from google.cloud.bigtable.data.row_filters import (
        CellsRowLimitFilter,
        RowFilterChain,
        RowSampleFilter,
        StripValueTransformerFilter,
    )
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter1 = StripValueTransformerFilter(True)

    row_filter2 = RowSampleFilter(0.25)

    row_filter3 = RowFilterChain(filters=[row_filter1, row_filter2])
    row_filter3_dict = row_filter3._to_dict()

    row_filter4 = CellsRowLimitFilter(11)
    row_filter4_dict = row_filter4._to_dict()

    row_filter5 = RowFilterChain(filters=[row_filter3, row_filter4])
    filter_dict = row_filter5._to_dict()

    expected_dict = {"chain": {"filters": [row_filter3_dict, row_filter4_dict]}}
    assert filter_dict == expected_dict
    expected_pb_value = row_filter5._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_row_filter_chain___repr__():
    from google.cloud.bigtable.data.row_filters import (
        RowFilterChain,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter2 = RowSampleFilter(0.25)

    row_filter3 = RowFilterChain(filters=[row_filter1, row_filter2])
    expected = f"RowFilterChain(filters={[row_filter1, row_filter2]})"
    assert repr(row_filter3) == expected
    assert eval(repr(row_filter3)) == row_filter3


def test_row_filter_chain___str__():
    from google.cloud.bigtable.data.row_filters import (
        RowFilterChain,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter2 = RowSampleFilter(0.25)

    row_filter3 = RowFilterChain(filters=[row_filter1, row_filter2])
    expected = "RowFilterChain([\n    StripValueTransformerFilter(flag=True),\n    RowSampleFilter(sample=0.25),\n])"
    assert str(row_filter3) == expected
    # test nested
    row_filter4 = RowFilterChain(filters=[row_filter3])
    expected = "RowFilterChain([\n    RowFilterChain([\n        StripValueTransformerFilter(flag=True),\n        RowSampleFilter(sample=0.25),\n    ]),\n])"
    assert str(row_filter4) == expected


def test_row_filter_union_to_pb():
    from google.cloud.bigtable.data.row_filters import (
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


def test_row_filter_union_to_dict():
    from google.cloud.bigtable.data.row_filters import (
        RowFilterUnion,
        RowSampleFilter,
        StripValueTransformerFilter,
    )
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_dict = row_filter1._to_dict()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_dict = row_filter2._to_dict()

    row_filter3 = RowFilterUnion(filters=[row_filter1, row_filter2])
    filter_dict = row_filter3._to_dict()

    expected_dict = {"interleave": {"filters": [row_filter1_dict, row_filter2_dict]}}
    assert filter_dict == expected_dict
    expected_pb_value = row_filter3._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_row_filter_union_to_pb_nested():
    from google.cloud.bigtable.data.row_filters import (
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


def test_row_filter_union_to_dict_nested():
    from google.cloud.bigtable.data.row_filters import (
        CellsRowLimitFilter,
        RowFilterUnion,
        RowSampleFilter,
        StripValueTransformerFilter,
    )
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter1 = StripValueTransformerFilter(True)

    row_filter2 = RowSampleFilter(0.25)

    row_filter3 = RowFilterUnion(filters=[row_filter1, row_filter2])
    row_filter3_dict = row_filter3._to_dict()

    row_filter4 = CellsRowLimitFilter(11)
    row_filter4_dict = row_filter4._to_dict()

    row_filter5 = RowFilterUnion(filters=[row_filter3, row_filter4])
    filter_dict = row_filter5._to_dict()

    expected_dict = {"interleave": {"filters": [row_filter3_dict, row_filter4_dict]}}
    assert filter_dict == expected_dict
    expected_pb_value = row_filter5._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_row_filter_union___repr__():
    from google.cloud.bigtable.data.row_filters import (
        RowFilterUnion,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter2 = RowSampleFilter(0.25)

    row_filter3 = RowFilterUnion(filters=[row_filter1, row_filter2])
    expected = "RowFilterUnion(filters=[StripValueTransformerFilter(flag=True), RowSampleFilter(sample=0.25)])"
    assert repr(row_filter3) == expected
    assert eval(repr(row_filter3)) == row_filter3


def test_row_filter_union___str__():
    from google.cloud.bigtable.data.row_filters import (
        RowFilterUnion,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter2 = RowSampleFilter(0.25)

    row_filter3 = RowFilterUnion(filters=[row_filter1, row_filter2])
    expected = "RowFilterUnion([\n    StripValueTransformerFilter(flag=True),\n    RowSampleFilter(sample=0.25),\n])"
    assert str(row_filter3) == expected
    # test nested
    row_filter4 = RowFilterUnion(filters=[row_filter3])
    expected = "RowFilterUnion([\n    RowFilterUnion([\n        StripValueTransformerFilter(flag=True),\n        RowSampleFilter(sample=0.25),\n    ]),\n])"
    assert str(row_filter4) == expected


def test_conditional_row_filter_constructor():
    from google.cloud.bigtable.data.row_filters import ConditionalRowFilter

    predicate_filter = object()
    true_filter = object()
    false_filter = object()
    cond_filter = ConditionalRowFilter(
        predicate_filter, true_filter=true_filter, false_filter=false_filter
    )
    assert cond_filter.predicate_filter is predicate_filter
    assert cond_filter.true_filter is true_filter
    assert cond_filter.false_filter is false_filter


def test_conditional_row_filter___eq__():
    from google.cloud.bigtable.data.row_filters import ConditionalRowFilter

    predicate_filter = object()
    true_filter = object()
    false_filter = object()
    cond_filter1 = ConditionalRowFilter(
        predicate_filter, true_filter=true_filter, false_filter=false_filter
    )
    cond_filter2 = ConditionalRowFilter(
        predicate_filter, true_filter=true_filter, false_filter=false_filter
    )
    assert cond_filter1 == cond_filter2


def test_conditional_row_filter___eq__type_differ():
    from google.cloud.bigtable.data.row_filters import ConditionalRowFilter

    predicate_filter = object()
    true_filter = object()
    false_filter = object()
    cond_filter1 = ConditionalRowFilter(
        predicate_filter, true_filter=true_filter, false_filter=false_filter
    )
    cond_filter2 = object()
    assert not (cond_filter1 == cond_filter2)


def test_conditional_row_filter___ne__():
    from google.cloud.bigtable.data.row_filters import ConditionalRowFilter

    predicate_filter = object()
    other_predicate_filter = object()
    true_filter = object()
    false_filter = object()
    cond_filter1 = ConditionalRowFilter(
        predicate_filter, true_filter=true_filter, false_filter=false_filter
    )
    cond_filter2 = ConditionalRowFilter(
        other_predicate_filter, true_filter=true_filter, false_filter=false_filter
    )
    assert cond_filter1 != cond_filter2


def test_conditional_row_filter_to_pb():
    from google.cloud.bigtable.data.row_filters import (
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


def test_conditional_row_filter_to_dict():
    from google.cloud.bigtable.data.row_filters import (
        CellsRowOffsetFilter,
        ConditionalRowFilter,
        RowSampleFilter,
        StripValueTransformerFilter,
    )
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_dict = row_filter1._to_dict()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_dict = row_filter2._to_dict()

    row_filter3 = CellsRowOffsetFilter(11)
    row_filter3_dict = row_filter3._to_dict()

    row_filter4 = ConditionalRowFilter(
        row_filter1, true_filter=row_filter2, false_filter=row_filter3
    )
    filter_dict = row_filter4._to_dict()

    expected_dict = {
        "condition": {
            "predicate_filter": row_filter1_dict,
            "true_filter": row_filter2_dict,
            "false_filter": row_filter3_dict,
        }
    }
    assert filter_dict == expected_dict
    expected_pb_value = row_filter4._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_conditional_row_filter_to_pb_true_only():
    from google.cloud.bigtable.data.row_filters import (
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


def test_conditional_row_filter_to_dict_true_only():
    from google.cloud.bigtable.data.row_filters import (
        ConditionalRowFilter,
        RowSampleFilter,
        StripValueTransformerFilter,
    )
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_dict = row_filter1._to_dict()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_dict = row_filter2._to_dict()

    row_filter3 = ConditionalRowFilter(row_filter1, true_filter=row_filter2)
    filter_dict = row_filter3._to_dict()

    expected_dict = {
        "condition": {
            "predicate_filter": row_filter1_dict,
            "true_filter": row_filter2_dict,
        }
    }
    assert filter_dict == expected_dict
    expected_pb_value = row_filter3._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_conditional_row_filter_to_pb_false_only():
    from google.cloud.bigtable.data.row_filters import (
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


def test_conditional_row_filter_to_dict_false_only():
    from google.cloud.bigtable.data.row_filters import (
        ConditionalRowFilter,
        RowSampleFilter,
        StripValueTransformerFilter,
    )
    from google.cloud.bigtable_v2.types import data as data_v2_pb2

    row_filter1 = StripValueTransformerFilter(True)
    row_filter1_dict = row_filter1._to_dict()

    row_filter2 = RowSampleFilter(0.25)
    row_filter2_dict = row_filter2._to_dict()

    row_filter3 = ConditionalRowFilter(row_filter1, false_filter=row_filter2)
    filter_dict = row_filter3._to_dict()

    expected_dict = {
        "condition": {
            "predicate_filter": row_filter1_dict,
            "false_filter": row_filter2_dict,
        }
    }
    assert filter_dict == expected_dict
    expected_pb_value = row_filter3._to_pb()
    assert data_v2_pb2.RowFilter(**expected_dict) == expected_pb_value


def test_conditional_row_filter___repr__():
    from google.cloud.bigtable.data.row_filters import (
        ConditionalRowFilter,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter2 = RowSampleFilter(0.25)
    row_filter3 = ConditionalRowFilter(row_filter1, true_filter=row_filter2)
    expected = (
        "ConditionalRowFilter(predicate_filter=StripValueTransformerFilter("
        "flag=True), true_filter=RowSampleFilter(sample=0.25), false_filter=None)"
    )
    assert repr(row_filter3) == expected
    assert eval(repr(row_filter3)) == row_filter3
    # test nested
    row_filter4 = ConditionalRowFilter(row_filter3, true_filter=row_filter2)
    expected = "ConditionalRowFilter(predicate_filter=ConditionalRowFilter(predicate_filter=StripValueTransformerFilter(flag=True), true_filter=RowSampleFilter(sample=0.25), false_filter=None), true_filter=RowSampleFilter(sample=0.25), false_filter=None)"
    assert repr(row_filter4) == expected
    assert eval(repr(row_filter4)) == row_filter4


def test_conditional_row_filter___str__():
    from google.cloud.bigtable.data.row_filters import (
        ConditionalRowFilter,
        RowFilterUnion,
        RowSampleFilter,
        StripValueTransformerFilter,
    )

    row_filter1 = StripValueTransformerFilter(True)
    row_filter2 = RowSampleFilter(0.25)
    row_filter3 = ConditionalRowFilter(row_filter1, true_filter=row_filter2)
    expected = "ConditionalRowFilter(\n    predicate_filter=StripValueTransformerFilter(flag=True),\n    true_filter=RowSampleFilter(sample=0.25),\n)"
    assert str(row_filter3) == expected
    # test nested
    row_filter4 = ConditionalRowFilter(
        row_filter3,
        true_filter=row_filter2,
        false_filter=RowFilterUnion([row_filter1, row_filter2]),
    )
    expected = "ConditionalRowFilter(\n    predicate_filter=ConditionalRowFilter(\n        predicate_filter=StripValueTransformerFilter(flag=True),\n        true_filter=RowSampleFilter(sample=0.25),\n    ),\n    true_filter=RowSampleFilter(sample=0.25),\n    false_filter=RowFilterUnion([\n        StripValueTransformerFilter(flag=True),\n        RowSampleFilter(sample=0.25),\n    ]),\n)"
    assert str(row_filter4) == expected


@pytest.mark.parametrize(
    "input_arg, expected_bytes",
    [
        (b"abc", b"abc"),
        ("abc", b"abc"),
        (1, b"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\\x01"),  # null bytes are ascii
        (b"*", b"\\*"),
        (".", b"\\."),
        (b"\\", b"\\\\"),
        (b"h.*i", b"h\\.\\*i"),
        (b'""', b'\\"\\"'),
        (b"[xyz]", b"\\[xyz\\]"),
        (b"\xe2\x98\xba\xef\xb8\x8f", b"\xe2\x98\xba\xef\xb8\x8f"),
        ("☃", b"\xe2\x98\x83"),
        (r"\C☃", b"\\\\C\xe2\x98\x83"),
    ],
)
def test_literal_value__write_literal_regex(input_arg, expected_bytes):
    from google.cloud.bigtable.data.row_filters import LiteralValueFilter

    filter_ = LiteralValueFilter(input_arg)
    assert filter_.regex == expected_bytes


class TestValueBitmaskFilter:
    @staticmethod
    def _target_class():
        from google.cloud.bigtable.data.row_filters import ValueBitmaskFilter

        return ValueBitmaskFilter

    def test_to_dict(self):
        mask = b"\xaa" * 8
        row_filter = self._target_class()(mask)
        expected = {"value_bitmask_filter": {"mask": mask}}
        assert row_filter._to_dict() == expected

    def test_to_pb(self):
        mask = b"\xaa" * 8
        row_filter = self._target_class()(mask)
        pb = row_filter._to_pb()
        assert pb.value_bitmask_filter.mask == mask


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


def _get_regex_filters():
    from google.cloud.bigtable.data.row_filters import (
        ColumnQualifierRegexFilter,
        FamilyNameRegexFilter,
        LiteralValueFilter,
        RowKeyRegexFilter,
        ValueRegexFilter,
    )

    return [
        RowKeyRegexFilter,
        FamilyNameRegexFilter,
        ColumnQualifierRegexFilter,
        ValueRegexFilter,
        LiteralValueFilter,
    ]


def _get_bool_filters():
    from google.cloud.bigtable.data.row_filters import (
        BlockAllFilter,
        PassAllFilter,
        SinkFilter,
        StripValueTransformerFilter,
    )

    return [
        SinkFilter,
        PassAllFilter,
        BlockAllFilter,
        StripValueTransformerFilter,
    ]


def _get_cell_count_filters():
    from google.cloud.bigtable.data.row_filters import (
        CellsColumnLimitFilter,
        CellsRowLimitFilter,
        CellsRowOffsetFilter,
    )

    return [
        CellsRowLimitFilter,
        CellsRowOffsetFilter,
        CellsColumnLimitFilter,
    ]


def _get_filter_combination_filters():
    from google.cloud.bigtable.data.row_filters import (
        RowFilterChain,
        RowFilterUnion,
    )

    return [
        RowFilterChain,
        RowFilterUnion,
    ]
