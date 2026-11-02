# Copyright 2024 Google LLC
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

import datetime

import pytest
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.protobuf import timestamp_pb2
from google.type import date_pb2

from google.cloud.bigtable.data.execute_query._parameters_formatting import (
    _format_execute_query_params,
    _to_param_types,
)
from google.cloud.bigtable.data.execute_query.metadata import SqlType
from google.cloud.bigtable.data.execute_query.values import Struct

from .resources import singer_pb2

timestamp = int(
    datetime.datetime(2024, 5, 12, 17, 44, 12, tzinfo=datetime.timezone.utc).timestamp()
)
dt_micros_non_zero = DatetimeWithNanoseconds(
    2024, 5, 12, 17, 44, 12, 123, nanosecond=0, tzinfo=datetime.timezone.utc
).timestamp_pb()
dt_nanos_zero = DatetimeWithNanoseconds(
    2024, 5, 12, 17, 44, 12, nanosecond=0, tzinfo=datetime.timezone.utc
).timestamp_pb()
dt_nanos_non_zero = DatetimeWithNanoseconds(
    2024, 5, 12, 17, 44, 12, nanosecond=12, tzinfo=datetime.timezone.utc
).timestamp_pb()
pb_date = date_pb2.Date(year=2024, month=5, day=15)


@pytest.mark.parametrize(
    "input_value,value_field,type_field,expected_value",
    [
        (1, "int_value", "int64_type", 1),
        ("2", "string_value", "string_type", "2"),
        (b"3", "bytes_value", "bytes_type", b"3"),
        (True, "bool_value", "bool_type", True),
        (
            datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc),
            "timestamp_value",
            "timestamp_type",
            dt_nanos_zero,
        ),
        (
            datetime.datetime(
                2024, 5, 12, 17, 44, 12, 123, tzinfo=datetime.timezone.utc
            ),
            "timestamp_value",
            "timestamp_type",
            dt_micros_non_zero,
        ),
        (datetime.date(2024, 5, 15), "date_value", "date_type", pb_date),
        (
            DatetimeWithNanoseconds(
                2024, 5, 12, 17, 44, 12, nanosecond=12, tzinfo=datetime.timezone.utc
            ),
            "timestamp_value",
            "timestamp_type",
            dt_nanos_non_zero,
        ),
    ],
)
def test_execute_query_parameters_inferred_types_parsing(
    input_value, value_field, type_field, expected_value
):
    result = _format_execute_query_params(
        {
            "test": input_value,
        },
        None,
    )
    assert result["test"][value_field] == expected_value
    assert type_field in result["test"]["type_"]


@pytest.mark.parametrize(
    "value, sql_type, proto_result",
    [
        (1.3, SqlType.Float32(), {"type_": {"float32_type": {}}, "float_value": 1.3}),
        (1.3, SqlType.Float64(), {"type_": {"float64_type": {}}, "float_value": 1.3}),
        (
            [1, 2, 3, 4],
            SqlType.Array(SqlType.Int64()),
            {
                "type_": {"array_type": {"element_type": {"int64_type": {}}}},
                "array_value": {
                    "values": [
                        {"int_value": 1},
                        {"int_value": 2},
                        {"int_value": 3},
                        {"int_value": 4},
                    ]
                },
            },
        ),
        (
            [1, None, 2, None],
            SqlType.Array(SqlType.Int64()),
            {
                "type_": {"array_type": {"element_type": {"int64_type": {}}}},
                "array_value": {
                    "values": [
                        {"int_value": 1},
                        {},
                        {"int_value": 2},
                        {},
                    ]
                },
            },
        ),
        (
            None,
            SqlType.Array(SqlType.Int64()),
            {
                "type_": {"array_type": {"element_type": {"int64_type": {}}}},
            },
        ),
        (
            ["foo", "bar", None],
            SqlType.Array(SqlType.String()),
            {
                "type_": {"array_type": {"element_type": {"string_type": {}}}},
                "array_value": {
                    "values": [
                        {"string_value": "foo"},
                        {"string_value": "bar"},
                        {},
                    ]
                },
            },
        ),
        (
            [b"foo", b"bar", None],
            SqlType.Array(SqlType.Bytes()),
            {
                "type_": {"array_type": {"element_type": {"bytes_type": {}}}},
                "array_value": {
                    "values": [
                        {"bytes_value": b"foo"},
                        {"bytes_value": b"bar"},
                        {},
                    ]
                },
            },
        ),
        (
            [
                datetime.datetime.fromtimestamp(1000, tz=datetime.timezone.utc),
                datetime.datetime.fromtimestamp(2000, tz=datetime.timezone.utc),
                None,
            ],
            SqlType.Array(SqlType.Timestamp()),
            {
                "type_": {"array_type": {"element_type": {"timestamp_type": {}}}},
                "array_value": {
                    "values": [
                        {"timestamp_value": timestamp_pb2.Timestamp(seconds=1000)},
                        {"timestamp_value": timestamp_pb2.Timestamp(seconds=2000)},
                        {},
                    ],
                },
            },
        ),
        (
            [True, False, None],
            SqlType.Array(SqlType.Bool()),
            {
                "type_": {"array_type": {"element_type": {"bool_type": {}}}},
                "array_value": {
                    "values": [
                        {"bool_value": True},
                        {"bool_value": False},
                        {},
                    ],
                },
            },
        ),
        (
            [datetime.date(2025, 1, 16), datetime.date(2025, 1, 17), None],
            SqlType.Array(SqlType.Date()),
            {
                "type_": {"array_type": {"element_type": {"date_type": {}}}},
                "array_value": {
                    "values": [
                        {"date_value": date_pb2.Date(year=2025, month=1, day=16)},
                        {"date_value": date_pb2.Date(year=2025, month=1, day=17)},
                        {},
                    ],
                },
            },
        ),
        (
            [1.1, 1.2, None],
            SqlType.Array(SqlType.Float32()),
            {
                "type_": {"array_type": {"element_type": {"float32_type": {}}}},
                "array_value": {
                    "values": [
                        {"float_value": 1.1},
                        {"float_value": 1.2},
                        {},
                    ]
                },
            },
        ),
        (
            [1.1, 1.2, None],
            SqlType.Array(SqlType.Float64()),
            {
                "type_": {"array_type": {"element_type": {"float64_type": {}}}},
                "array_value": {
                    "values": [
                        {"float_value": 1.1},
                        {"float_value": 1.2},
                        {},
                    ]
                },
            },
        ),
    ],
)
def test_execute_query_explicit_parameter_parsing(value, sql_type, proto_result):
    result = _format_execute_query_params(
        {"param_name": value}, {"param_name": sql_type}
    )
    print(result)
    assert result["param_name"] == proto_result


def test_execute_query_parameters_not_supported_types():
    with pytest.raises(ValueError):
        _format_execute_query_params({"test1": 1.1}, None)

    with pytest.raises(ValueError):
        _format_execute_query_params({"test1": {"a": 1}}, None)

    with pytest.raises(ValueError):
        _format_execute_query_params({"test1": [1]}, None)

    with pytest.raises(ValueError):
        _format_execute_query_params({"test1": Struct([("field1", 1)])}, None)

    with pytest.raises(NotImplementedError, match="not supported"):
        _format_execute_query_params(
            {"test1": {"a": 1}},
            {
                "test1": SqlType.Map(SqlType.String(), SqlType.Int64()),
            },
        )

    with pytest.raises(NotImplementedError, match="not supported"):
        _format_execute_query_params(
            {"test1": Struct([("field1", 1)])},
            {"test1": SqlType.Struct([("field1", SqlType.Int64())])},
        )

    with pytest.raises(NotImplementedError, match="not supported"):
        _format_execute_query_params(
            {"test1": singer_pb2.Singer()},
            {"test1": SqlType.Proto()},
        )

    with pytest.raises(NotImplementedError, match="not supported"):
        _format_execute_query_params(
            {"test1": singer_pb2.Genre.ROCK},
            {"test1": SqlType.Enum()},
        )


def test_instance_execute_query_parameters_not_match():
    with pytest.raises(ValueError, match="test2"):
        _format_execute_query_params(
            {
                "test1": 1,
                "test2": 1,
            },
            {
                "test1": SqlType.Int64(),
                "test2": SqlType.String(),
            },
        )


def test_array_params_enforce_element_type():
    with pytest.raises(ValueError, match="Error when parsing parameter p") as e1:
        _format_execute_query_params(
            {"p": ["a", 1, None]}, {"p": SqlType.Array(SqlType.String())}
        )
    with pytest.raises(ValueError, match="Error when parsing parameter p") as e2:
        _format_execute_query_params(
            {"p": ["a", 1, None]}, {"p": SqlType.Array(SqlType.Int64())}
        )
    assert "Expected query parameter of type str, got int" in str(e1.value.__cause__)
    assert "Expected query parameter of type int, got str" in str(e2.value.__cause__)


def test_to_params_types():
    results = _to_param_types(
        {"a": 1, "s": "str", "b": b"bytes", "array": ["foo", "bar"]},
        {"array": SqlType.Array(SqlType.String())},
    )
    assert results == {
        "a": SqlType.Int64()._to_type_pb_dict(),
        "s": SqlType.String()._to_type_pb_dict(),
        "b": SqlType.Bytes()._to_type_pb_dict(),
        "array": SqlType.Array(SqlType.String())._to_type_pb_dict(),
    }


def test_to_param_types_empty():
    results = _to_param_types({}, {})
    assert results == {}
