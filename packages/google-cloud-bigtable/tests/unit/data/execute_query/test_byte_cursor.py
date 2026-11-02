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
import pytest

from google.cloud.bigtable.data.execute_query._byte_cursor import _ByteCursor

from .sql_helpers import (
    batch_response,
    checksum,
    token_only_response,
)


def pass_values_to_byte_cursor(byte_cursor, iterable):
    for value in iterable:
        result = byte_cursor.consume(value)
        if result is not None:
            yield result


class TestByteCursor:
    def test__proto_rows_batch__complete_data(self):
        byte_cursor = _ByteCursor()
        stream = [
            batch_response(b"123"),
            batch_response(b"456"),
            batch_response(b"789"),
            batch_response(b"0", token=b"token1", checksum=checksum(b"1234567890")),
            batch_response(b"abc"),
            batch_response(b"def"),
            batch_response(b"ghi"),
            batch_response(b"j", token=b"token2", checksum=checksum(b"abcdefghij")),
        ]
        byte_cursor_iter = pass_values_to_byte_cursor(byte_cursor, stream)
        value = next(byte_cursor_iter)
        assert value[0] == b"1234567890"
        assert byte_cursor._resume_token == b"token1"

        value = next(byte_cursor_iter)
        assert value[0] == b"abcdefghij"
        assert byte_cursor._resume_token == b"token2"

    def test__proto_rows_batch__empty_proto_rows_batch(self):
        byte_cursor = _ByteCursor()
        stream = [
            batch_response(b"", token=b"token1"),
            batch_response(b"123"),
            batch_response(b"0", token=b"token2", checksum=checksum(b"1230")),
        ]

        byte_cursor_iter = pass_values_to_byte_cursor(byte_cursor, stream)
        value = next(byte_cursor_iter)
        assert value[0] == b"1230"
        assert byte_cursor._resume_token == b"token2"

    def test__proto_rows_batch__handles_response_with_just_a_token(self):
        byte_cursor = _ByteCursor()
        stream = [
            token_only_response(b"token1"),
            batch_response(b"123"),
            batch_response(b"0", token=b"token2", checksum=checksum(b"1230")),
        ]

        byte_cursor_iter = pass_values_to_byte_cursor(byte_cursor, stream)
        value = next(byte_cursor_iter)
        assert value[0] == b"1230"
        assert byte_cursor._resume_token == b"token2"

    def test__proto_rows_batch__no_resume_token_at_the_end_of_stream(self):
        byte_cursor = _ByteCursor()
        stream = [
            batch_response(b"0", token=b"token1", checksum=checksum(b"0")),
            batch_response(b"abc"),
            batch_response(b"def"),
            batch_response(b"ghi"),
            batch_response(b"j", checksum=checksum(b"abcdefghij")),
        ]
        value = byte_cursor.consume(stream[0])
        assert value[0] == b"0"
        assert byte_cursor._resume_token == b"token1"

        assert byte_cursor.consume(stream[1]) is None
        assert byte_cursor.consume(stream[2]) is None
        assert byte_cursor.consume(stream[3]) is None
        assert byte_cursor.consume(stream[4]) is None
        # Empty should be checked by the iterator and should throw an error if this happens
        assert not byte_cursor.empty()

    def test__proto_rows_batch__prepare_for_new_request_resets_buffer(self):
        byte_cursor = _ByteCursor()
        assert byte_cursor.consume(batch_response(b"abc")) is None
        assert (
            byte_cursor.consume(
                batch_response(b"def", token=b"token1", checksum=checksum(b"abcdef"))
            )[0]
            == b"abcdef"
        )
        assert byte_cursor.consume(batch_response(b"foo")) is None
        assert byte_cursor.prepare_for_new_request() == b"token1"
        # foo is dropped because of new request
        assert (
            byte_cursor.consume(
                batch_response(b"bar", token=b"token2", checksum=checksum(b"bar"))
            )[0]
            == b"bar"
        )

    def test__proto_rows_batch__multiple_batches_before_token(self):
        byte_cursor = _ByteCursor()
        assert byte_cursor.consume(batch_response(b"foo")) is None
        assert (
            byte_cursor.consume(batch_response(b"bar", checksum=checksum(b"foobar")))
            is None
        )
        assert byte_cursor.consume(batch_response(b"1")) is None
        assert byte_cursor.consume(batch_response(b"2")) is None
        assert (
            byte_cursor.consume(batch_response(b"3", checksum=checksum(b"123"))) is None
        )
        batches = byte_cursor.consume(
            batch_response(b"done", token=b"token", checksum=checksum(b"done"))
        )
        assert len(batches) == 3
        assert batches[0] == b"foobar"
        assert batches[1] == b"123"
        assert batches[2] == b"done"

    def test__proto_rows_batch__reset_on_partial_batch(self):
        byte_cursor = _ByteCursor()
        assert byte_cursor.consume(batch_response(b"foo")) is None
        assert byte_cursor.consume(batch_response(b"bar", reset=True)) is None
        batches = byte_cursor.consume(
            batch_response(b"baz", token=b"token", checksum=checksum(b"barbaz"))
        )
        assert len(batches) == 1
        assert batches[0] == b"barbaz"

    def test__proto_rows_batch__reset_on_complete_batch(self):
        byte_cursor = _ByteCursor()
        assert byte_cursor.consume(batch_response(b"foo")) is None
        assert (
            byte_cursor.consume(batch_response(b"bar", checksum=checksum(b"foobar")))
            is None
        )
        assert byte_cursor.consume(batch_response(b"discard")) is None
        assert byte_cursor.consume(batch_response(b"1", reset=True)) is None
        assert byte_cursor.consume(batch_response(b"2")) is None
        batches = byte_cursor.consume(
            batch_response(b"3", token=b"token", checksum=checksum(b"123"))
        )
        assert len(batches) == 1
        assert batches[0] == b"123"

    def test__proto_rows_batch__checksum_mismatch(self):
        byte_cursor = _ByteCursor()
        with pytest.raises(
            ValueError,
            match="Unexpected checksum mismatch.",
        ):
            byte_cursor.consume(batch_response(b"foo", checksum=1234))
