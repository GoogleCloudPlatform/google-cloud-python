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

from unittest import mock

import pytest

import google.cloud.bigtable.data.execute_query._reader
from google.cloud.bigtable.data.execute_query._reader import _QueryResultRowReader
from google.cloud.bigtable.data.execute_query.metadata import (
    Metadata,
    SqlType,
    _pb_metadata_to_metadata_types,
)
from google.cloud.bigtable_v2.types.data import Value as PBValue
from tests.unit.data.execute_query.sql_helpers import (
    bytes_val,
    chunked_responses,
    column,
    int64_type,
    int_val,
    metadata,
    proto_rows_bytes,
    str_val,
)

from .resources import singer_pb2


class TestQueryResultRowReader:
    def test__single_values_received(self):
        metadata = Metadata([("test1", SqlType.Int64()), ("test2", SqlType.Int64())])
        values = [
            proto_rows_bytes(int_val(1), int_val(2)),
            proto_rows_bytes(int_val(3), int_val(4)),
        ]

        reader = _QueryResultRowReader()

        result = reader.consume(values[0:1], metadata)
        assert len(result) == 1
        assert len(result[0]) == 2
        result = reader.consume(values[1:], metadata)
        assert len(result) == 1
        assert len(result[0]) == 2

    def test__multiple_rows_received(self):
        values = [
            proto_rows_bytes(int_val(1), int_val(2), int_val(3), int_val(4)),
            proto_rows_bytes(int_val(5), int_val(6)),
            proto_rows_bytes(int_val(7), int_val(8)),
        ]

        metadata = Metadata([("test1", SqlType.Int64()), ("test2", SqlType.Int64())])
        reader = _QueryResultRowReader()

        result = reader.consume(values[0:1], metadata)
        assert len(result) == 2
        assert len(result[0]) == 2
        assert result[0][0] == result[0]["test1"] == 1
        assert result[0][1] == result[0]["test2"] == 2

        assert len(result[1]) == 2
        assert result[1][0] == result[1]["test1"] == 3
        assert result[1][1] == result[1]["test2"] == 4

        result = reader.consume(values[1:2], metadata)
        assert len(result) == 1
        assert len(result[0]) == 2
        assert result[0][0] == result[0]["test1"] == 5
        assert result[0][1] == result[0]["test2"] == 6

        result = reader.consume(values[2:], metadata)
        assert len(result) == 1
        assert len(result[0]) == 2
        assert result[0][0] == result[0]["test1"] == 7
        assert result[0][1] == result[0]["test2"] == 8

    def test__received_values_are_passed_to_parser_in_batches(self):
        metadata = Metadata([("test1", SqlType.Int64()), ("test2", SqlType.Int64())])

        # TODO move to a SqlType test
        assert SqlType.Struct([("a", SqlType.Int64())]) == SqlType.Struct(
            [("a", SqlType.Int64())]
        )
        assert SqlType.Struct([("a", SqlType.String())]) != SqlType.Struct(
            [("a", SqlType.Int64())]
        )
        assert SqlType.Struct([("a", SqlType.Int64())]) != SqlType.Struct(
            [("b", SqlType.Int64())]
        )

        assert SqlType.Array(SqlType.Int64()) == SqlType.Array(SqlType.Int64())
        assert SqlType.Array(SqlType.Int64()) != SqlType.Array(SqlType.String())

        assert SqlType.Map(SqlType.Int64(), SqlType.String()) == SqlType.Map(
            SqlType.Int64(), SqlType.String()
        )
        assert SqlType.Map(SqlType.Int64(), SqlType.String()) != SqlType.Map(
            SqlType.String(), SqlType.String()
        )

        reader = _QueryResultRowReader()
        with mock.patch.object(
            google.cloud.bigtable.data.execute_query._reader,
            "_parse_pb_value_to_python_value",
        ) as parse_mock:
            reader.consume([proto_rows_bytes(int_val(1), int_val(2))], metadata)
            parse_mock.assert_has_calls(
                [
                    mock.call(PBValue(int_val(1)), SqlType.Int64(), "test1", None),
                    mock.call(PBValue(int_val(2)), SqlType.Int64(), "test2", None),
                ]
            )

    def test__parser_errors_are_forwarded(self):
        metadata = Metadata([("test1", SqlType.Int64())])

        values = [str_val("test")]

        reader = _QueryResultRowReader()
        with mock.patch.object(
            google.cloud.bigtable.data.execute_query._reader,
            "_parse_pb_value_to_python_value",
            side_effect=ValueError("test"),
        ) as parse_mock:
            with pytest.raises(ValueError, match="test"):
                reader.consume([proto_rows_bytes(values[0])], metadata)

            parse_mock.assert_has_calls(
                [
                    mock.call(PBValue(values[0]), SqlType.Int64(), "test1", None),
                ]
            )

    def test__multiple_proto_rows_received_with_one_resume_token(self):
        from google.cloud.bigtable.data.execute_query._byte_cursor import _ByteCursor

        def pass_values_to_byte_cursor(byte_cursor, iterable):
            for value in iterable:
                result = byte_cursor.consume(value)
                if result is not None:
                    yield result

        stream = [
            *chunked_responses(
                4, int_val(1), int_val(2), int_val(3), int_val(4), token=b"token1"
            ),
            *chunked_responses(1, int_val(5), int_val(6), token=b"token2"),
        ]

        byte_cursor = _ByteCursor()
        reader = _QueryResultRowReader()
        byte_cursor_iter = pass_values_to_byte_cursor(byte_cursor, stream)
        md = _pb_metadata_to_metadata_types(
            metadata(column("test1", int64_type()), column("test2", int64_type()))
        )

        returned_values = []

        def intercept_return_values(func):
            nonlocal intercept_return_values  # noqa: F824

            def wrapped(*args, **kwargs):
                value = func(*args, **kwargs)
                returned_values.append(value)
                return value

            return wrapped

        with mock.patch.object(
            reader,
            "_parse_proto_rows",
            wraps=intercept_return_values(reader._parse_proto_rows),
        ):
            result = reader.consume(next(byte_cursor_iter), md)

        # Despite the fact that two ProtoRows were received, a single resume_token after the second ProtoRows object forces us to parse them together.
        # We will interpret them as one larger ProtoRows object.
        assert len(returned_values) == 1
        assert len(returned_values[0]) == 4
        assert returned_values[0][0].int_value == 1
        assert returned_values[0][1].int_value == 2
        assert returned_values[0][2].int_value == 3
        assert returned_values[0][3].int_value == 4

        assert len(result) == 2
        assert len(result[0]) == 2
        assert result[0][0] == 1
        assert result[0]["test1"] == 1
        assert result[0][1] == 2
        assert result[0]["test2"] == 2
        assert len(result[1]) == 2
        assert result[1][0] == 3
        assert result[1]["test1"] == 3
        assert result[1][1] == 4
        assert result[1]["test2"] == 4
        assert byte_cursor._resume_token == b"token1"

        returned_values = []
        with mock.patch.object(
            reader,
            "_parse_proto_rows",
            wraps=intercept_return_values(reader._parse_proto_rows),
        ):
            result = reader.consume(next(byte_cursor_iter), md)

        assert len(result) == 1
        assert len(result[0]) == 2
        assert result[0][0] == 5
        assert result[0]["test1"] == 5
        assert result[0][1] == 6
        assert result[0]["test2"] == 6
        assert byte_cursor._resume_token == b"token2"

    def test_multiple_batches(self):
        reader = _QueryResultRowReader()
        batches = [
            proto_rows_bytes(int_val(1), int_val(2), int_val(3), int_val(4)),
            proto_rows_bytes(int_val(5), int_val(6)),
            proto_rows_bytes(int_val(7), int_val(8)),
        ]
        results = reader.consume(
            batches,
            Metadata([("test1", SqlType.Int64()), ("test2", SqlType.Int64())]),
        )
        assert len(results) == 4
        [row1, row2, row3, row4] = results
        assert row1["test1"] == 1
        assert row1["test2"] == 2
        assert row2["test1"] == 3
        assert row2["test2"] == 4
        assert row3["test1"] == 5
        assert row3["test2"] == 6
        assert row4["test1"] == 7
        assert row4["test2"] == 8

    def test_multiple_batches_with_proto_and_enum_types(self):
        singer1 = singer_pb2.Singer(name="John")
        singer2 = singer_pb2.Singer(name="Taylor")
        singer3 = singer_pb2.Singer(name="Jay")
        singer4 = singer_pb2.Singer(name="Eric")

        reader = _QueryResultRowReader()
        batches = [
            proto_rows_bytes(
                bytes_val(singer1.SerializeToString()),
                int_val(0),
                bytes_val(singer2.SerializeToString()),
                int_val(1),
            ),
            proto_rows_bytes(bytes_val(singer3.SerializeToString()), int_val(2)),
            proto_rows_bytes(bytes_val(singer4.SerializeToString()), int_val(3)),
        ]

        results = reader.consume(
            batches,
            Metadata([("singer", SqlType.Proto()), ("genre", SqlType.Enum())]),
            {"singer": singer_pb2.Singer(), "genre": singer_pb2.Genre},
        )
        assert len(results) == 4
        [row1, row2, row3, row4] = results
        assert row1["singer"] == singer1
        assert row1["genre"] == "POP"
        assert row2["singer"] == singer2
        assert row2["genre"] == "JAZZ"
        assert row3["singer"] == singer3
        assert row3["genre"] == "FOLK"
        assert row4["singer"] == singer4
        assert row4["genre"] == "ROCK"


class TestMetadata:
    def test__duplicate_column_names(self):
        metadata = Metadata(
            [
                ("test1", SqlType.Int64()),
                ("test2", SqlType.Bytes()),
                ("test2", SqlType.String()),
            ]
        )
        assert metadata[0].column_name == "test1"
        assert metadata["test1"].column_type == SqlType.Int64()

        # duplicate columns not accesible by name
        with pytest.raises(KeyError, match="Ambigious column name"):
            metadata["test2"]

        # duplicate columns accessible by index
        assert metadata[1].column_type == SqlType.Bytes()
        assert metadata[1].column_name == "test2"
        assert metadata[2].column_type == SqlType.String()
        assert metadata[2].column_name == "test2"
