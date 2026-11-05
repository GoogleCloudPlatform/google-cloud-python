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

from unittest import mock

import pytest

import google.cloud.bigtable.data.mutations as mutations


class TestBaseMutation:
    def _target_class(self):
        from google.cloud.bigtable.data.mutations import Mutation

        return Mutation

    def test__to_dict(self):
        """Should be unimplemented in the base class"""
        with pytest.raises(NotImplementedError):
            self._target_class()._to_dict(mock.Mock())

    def test_is_idempotent(self):
        """is_idempotent should assume True"""
        assert self._target_class().is_idempotent(mock.Mock())

    def test___str__(self):
        """Str representation of mutations should be to_dict"""
        self_mock = mock.Mock()
        str_value = self._target_class().__str__(self_mock)
        assert self_mock._to_dict.called
        assert str_value == str(self_mock._to_dict.return_value)

    @pytest.mark.parametrize("test_dict", [{}, {"key": "value"}])
    def test_size(self, test_dict):
        from sys import getsizeof

        """Size should return size of dict representation"""
        self_mock = mock.Mock()
        self_mock._to_dict.return_value = test_dict
        size_value = self._target_class().size(self_mock)
        assert size_value == getsizeof(test_dict)

    @pytest.mark.parametrize(
        "expected_class,input_dict",
        [
            (
                mutations.SetCell,
                {
                    "set_cell": {
                        "family_name": "foo",
                        "column_qualifier": b"bar",
                        "value": b"test",
                        "timestamp_micros": 12345,
                    }
                },
            ),
            (
                mutations.DeleteRangeFromColumn,
                {
                    "delete_from_column": {
                        "family_name": "foo",
                        "column_qualifier": b"bar",
                        "time_range": {},
                    }
                },
            ),
            (
                mutations.DeleteRangeFromColumn,
                {
                    "delete_from_column": {
                        "family_name": "foo",
                        "column_qualifier": b"bar",
                        "time_range": {"start_timestamp_micros": 123456789},
                    }
                },
            ),
            (
                mutations.DeleteRangeFromColumn,
                {
                    "delete_from_column": {
                        "family_name": "foo",
                        "column_qualifier": b"bar",
                        "time_range": {"end_timestamp_micros": 123456789},
                    }
                },
            ),
            (
                mutations.DeleteRangeFromColumn,
                {
                    "delete_from_column": {
                        "family_name": "foo",
                        "column_qualifier": b"bar",
                        "time_range": {
                            "start_timestamp_micros": 123,
                            "end_timestamp_micros": 123456789,
                        },
                    }
                },
            ),
            (
                mutations.DeleteAllFromFamily,
                {"delete_from_family": {"family_name": "foo"}},
            ),
            (mutations.DeleteAllFromRow, {"delete_from_row": {}}),
            (
                mutations.AddToCell,
                {
                    "add_to_cell": {
                        "family_name": "foo",
                        "column_qualifier": {"raw_value": b"bar"},
                        "timestamp": {"raw_timestamp_micros": 12345},
                        "input": {"int_value": 123},
                    }
                },
            ),
        ],
    )
    def test__from_dict(self, expected_class, input_dict):
        """Should be able to create instance from dict"""
        instance = self._target_class()._from_dict(input_dict)
        assert isinstance(instance, expected_class)
        found_dict = instance._to_dict()
        assert found_dict == input_dict

    @pytest.mark.parametrize(
        "input_dict",
        [
            {"set_cell": {}},
            {
                "set_cell": {
                    "column_qualifier": b"bar",
                    "value": b"test",
                    "timestamp_micros": 12345,
                }
            },
            {
                "set_cell": {
                    "family_name": "f",
                    "column_qualifier": b"bar",
                    "value": b"test",
                }
            },
            {"delete_from_family": {}},
            {"delete_from_column": {}},
            {"fake-type"},
            {},
        ],
    )
    def test__from_dict_missing_fields(self, input_dict):
        """If dict is malformed or fields are missing, should raise ValueError"""
        with pytest.raises(ValueError):
            self._target_class()._from_dict(input_dict)

    def test__from_dict_wrong_subclass(self):
        """You shouldn't be able to instantiate one mutation type using the dict of another"""
        subclasses = [
            mutations.SetCell("foo", b"bar", b"test"),
            mutations.DeleteRangeFromColumn("foo", b"bar"),
            mutations.DeleteAllFromFamily("foo"),
            mutations.DeleteAllFromRow(),
            mutations.AddToCell("foo", b"bar", 123, 456),
        ]
        for instance in subclasses:
            others = [other for other in subclasses if other != instance]
            for other in others:
                with pytest.raises(ValueError) as e:
                    type(other)._from_dict(instance._to_dict())
                assert "Mutation type mismatch" in str(e.value)


class TestSetCell:
    def _target_class(self):
        from google.cloud.bigtable.data.mutations import SetCell

        return SetCell

    def _make_one(self, *args, **kwargs):
        return self._target_class()(*args, **kwargs)

    @pytest.mark.parametrize("input_val", [2**63, -(2**63) - 1, 2**64, -(2**64)])
    def test_ctor_large_int(self, input_val):
        with pytest.raises(ValueError) as e:
            self._make_one(family="f", qualifier=b"b", new_value=input_val)
        assert "int values must be between" in str(e.value)

    @pytest.mark.parametrize("input_val", [True, False])
    def test_ctor_bool_value(self, input_val):
        with pytest.raises(TypeError) as e:
            self._make_one(family="f", qualifier=b"b", new_value=input_val)
        assert "new_value must be bytes, str, or int" in str(e.value)

    @pytest.mark.parametrize("input_val", ["", "a", "abc", "hello world!"])
    def test_ctor_str_value(self, input_val):
        found = self._make_one(family="f", qualifier=b"b", new_value=input_val)
        assert found.new_value == input_val.encode("utf-8")

    def test_ctor(self):
        """Ensure constructor sets expected values"""
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = b"test-value"
        expected_timestamp = 1234567890
        instance = self._make_one(
            expected_family, expected_qualifier, expected_value, expected_timestamp
        )
        assert instance.family == expected_family
        assert instance.qualifier == expected_qualifier
        assert instance.new_value == expected_value
        assert instance.timestamp_micros == expected_timestamp

    def test_ctor_str_inputs(self):
        """Test with string qualifier and value"""
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = b"test-value"
        instance = self._make_one(expected_family, "test-qualifier", "test-value")
        assert instance.family == expected_family
        assert instance.qualifier == expected_qualifier
        assert instance.new_value == expected_value

    @pytest.mark.parametrize(
        "input_val", [-(2**63), -20, -1, 0, 1, 100, int(2**60), 2**63 - 1]
    )
    def test_ctor_int_value(self, input_val):
        found = self._make_one(family="f", qualifier=b"b", new_value=input_val)
        assert found.new_value == input_val.to_bytes(8, "big", signed=True)

    @pytest.mark.parametrize(
        "int_value,expected_bytes",
        [
            (-(2**63), b"\x80\x00\x00\x00\x00\x00\x00\x00"),
            (-42, b"\xff\xff\xff\xff\xff\xff\xff\xd6"),
            (-2, b"\xff\xff\xff\xff\xff\xff\xff\xfe"),
            (-1, b"\xff\xff\xff\xff\xff\xff\xff\xff"),
            (0, b"\x00\x00\x00\x00\x00\x00\x00\x00"),
            (1, b"\x00\x00\x00\x00\x00\x00\x00\x01"),
            (2, b"\x00\x00\x00\x00\x00\x00\x00\x02"),
            (100, b"\x00\x00\x00\x00\x00\x00\x00d"),
            (2**63 - 1, b"\x7f\xff\xff\xff\xff\xff\xff\xff"),
        ],
    )
    def test_ctor_int_value_bytes(self, int_value, expected_bytes):
        """Test with int value"""
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        instance = self._make_one(expected_family, expected_qualifier, int_value)
        assert instance.family == expected_family
        assert instance.qualifier == expected_qualifier
        assert instance.new_value == expected_bytes

    def test_ctor_negative_timestamp(self):
        """Only positive or -1 timestamps are valid"""
        with pytest.raises(ValueError) as e:
            self._make_one("test-family", b"test-qualifier", b"test-value", -2)
        assert (
            "timestamp_micros must be positive (or -1 for server-side timestamp)"
            in str(e.value)
        )

    @pytest.mark.parametrize(
        "timestamp_ns,expected_timestamp_micros",
        [
            (0, 0),
            (1, 0),
            (123, 0),
            (999, 0),
            (999_999, 0),
            (1_000_000, 1000),
            (1_234_567, 1000),
            (1_999_999, 1000),
            (2_000_000, 2000),
            (1_234_567_890_123, 1_234_567_000),
        ],
    )
    def test_ctor_no_timestamp(self, timestamp_ns, expected_timestamp_micros):
        """If no timestamp is given, should use current time with millisecond precision"""
        with mock.patch("time.time_ns", return_value=timestamp_ns):
            instance = self._make_one("test-family", b"test-qualifier", b"test-value")
            assert instance.timestamp_micros == expected_timestamp_micros

    def test__to_dict(self):
        """ensure dict representation is as expected"""
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = b"test-value"
        expected_timestamp = 123456789
        instance = self._make_one(
            expected_family, expected_qualifier, expected_value, expected_timestamp
        )
        got_dict = instance._to_dict()
        assert list(got_dict.keys()) == ["set_cell"]
        got_inner_dict = got_dict["set_cell"]
        assert got_inner_dict["family_name"] == expected_family
        assert got_inner_dict["column_qualifier"] == expected_qualifier
        assert got_inner_dict["timestamp_micros"] == expected_timestamp
        assert got_inner_dict["value"] == expected_value
        assert len(got_inner_dict.keys()) == 4

    def test__to_dict_server_timestamp(self):
        """test with server side timestamp -1 value"""
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = b"test-value"
        expected_timestamp = -1
        instance = self._make_one(
            expected_family, expected_qualifier, expected_value, expected_timestamp
        )
        got_dict = instance._to_dict()
        assert list(got_dict.keys()) == ["set_cell"]
        got_inner_dict = got_dict["set_cell"]
        assert got_inner_dict["family_name"] == expected_family
        assert got_inner_dict["column_qualifier"] == expected_qualifier
        assert got_inner_dict["timestamp_micros"] == expected_timestamp
        assert got_inner_dict["value"] == expected_value
        assert len(got_inner_dict.keys()) == 4

    def test__to_pb(self):
        """ensure proto representation is as expected"""
        import google.cloud.bigtable_v2.types.data as data_pb

        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = b"test-value"
        expected_timestamp = 123456789
        instance = self._make_one(
            expected_family, expected_qualifier, expected_value, expected_timestamp
        )
        got_pb = instance._to_pb()
        assert isinstance(got_pb, data_pb.Mutation)
        assert got_pb.set_cell.family_name == expected_family
        assert got_pb.set_cell.column_qualifier == expected_qualifier
        assert got_pb.set_cell.timestamp_micros == expected_timestamp
        assert got_pb.set_cell.value == expected_value

    def test__to_pb_server_timestamp(self):
        """test with server side timestamp -1 value"""
        import google.cloud.bigtable_v2.types.data as data_pb

        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = b"test-value"
        expected_timestamp = -1
        instance = self._make_one(
            expected_family, expected_qualifier, expected_value, expected_timestamp
        )
        got_pb = instance._to_pb()
        assert isinstance(got_pb, data_pb.Mutation)
        assert got_pb.set_cell.family_name == expected_family
        assert got_pb.set_cell.column_qualifier == expected_qualifier
        assert got_pb.set_cell.timestamp_micros == expected_timestamp
        assert got_pb.set_cell.value == expected_value

    @pytest.mark.parametrize(
        "timestamp,expected_value",
        [
            (1234567890, True),
            (1, True),
            (0, True),
            (-1, False),
            (None, True),
        ],
    )
    def test_is_idempotent(self, timestamp, expected_value):
        """is_idempotent is based on whether an explicit timestamp is set"""
        instance = self._make_one(
            "test-family", b"test-qualifier", b"test-value", timestamp
        )
        assert instance.is_idempotent() is expected_value

    def test___str__(self):
        """Str representation of mutations should be to_dict"""
        instance = self._make_one(
            "test-family", b"test-qualifier", b"test-value", 1234567890
        )
        str_value = instance.__str__()
        dict_value = instance._to_dict()
        assert str_value == str(dict_value)


class TestDeleteRangeFromColumn:
    def _target_class(self):
        from google.cloud.bigtable.data.mutations import DeleteRangeFromColumn

        return DeleteRangeFromColumn

    def _make_one(self, *args, **kwargs):
        return self._target_class()(*args, **kwargs)

    def test_ctor(self):
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_start = 1234567890
        expected_end = 1234567891
        instance = self._make_one(
            expected_family, expected_qualifier, expected_start, expected_end
        )
        assert instance.family == expected_family
        assert instance.qualifier == expected_qualifier
        assert instance.start_timestamp_micros == expected_start
        assert instance.end_timestamp_micros == expected_end

    def test_ctor_no_timestamps(self):
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        instance = self._make_one(expected_family, expected_qualifier)
        assert instance.family == expected_family
        assert instance.qualifier == expected_qualifier
        assert instance.start_timestamp_micros is None
        assert instance.end_timestamp_micros is None

    @pytest.mark.parametrize("qualifier_str", ["", "a", "col", "my_column", "qual_str"])
    def test_ctor_str_qualifier(self, qualifier_str):
        instance = self._make_one("test-family", qualifier_str)
        expected_bytes = qualifier_str.encode("utf-8")
        assert instance.qualifier == expected_bytes
        assert instance._to_pb().delete_from_column.column_qualifier == expected_bytes

    @pytest.mark.parametrize("bad_qualifier", [123, None, object()])
    def test_ctor_invalid_qualifier(self, bad_qualifier):
        with pytest.raises(TypeError, match="qualifier must be bytes or str"):
            self._make_one("test-family", bad_qualifier)

    def test_ctor_timestamps_out_of_order(self):
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_start = 10
        expected_end = 1
        with pytest.raises(ValueError) as excinfo:
            self._make_one(
                expected_family, expected_qualifier, expected_start, expected_end
            )
        assert "start_timestamp_micros must be <= end_timestamp_micros" in str(
            excinfo.value
        )

    @pytest.mark.parametrize(
        "start,end",
        [
            (0, 1),
            (None, 1),
            (0, None),
        ],
    )
    def test__to_dict(self, start, end):
        """Should be unimplemented in the base class"""
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"

        instance = self._make_one(expected_family, expected_qualifier, start, end)
        got_dict = instance._to_dict()
        assert list(got_dict.keys()) == ["delete_from_column"]
        got_inner_dict = got_dict["delete_from_column"]
        assert len(got_inner_dict.keys()) == 3
        assert got_inner_dict["family_name"] == expected_family
        assert got_inner_dict["column_qualifier"] == expected_qualifier
        time_range_dict = got_inner_dict["time_range"]
        expected_len = int(isinstance(start, int)) + int(isinstance(end, int))
        assert len(time_range_dict.keys()) == expected_len
        if start is not None:
            assert time_range_dict["start_timestamp_micros"] == start
        if end is not None:
            assert time_range_dict["end_timestamp_micros"] == end

    def test__to_pb(self):
        """ensure proto representation is as expected"""
        import google.cloud.bigtable_v2.types.data as data_pb

        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        instance = self._make_one(expected_family, expected_qualifier)
        got_pb = instance._to_pb()
        assert isinstance(got_pb, data_pb.Mutation)
        assert got_pb.delete_from_column.family_name == expected_family
        assert got_pb.delete_from_column.column_qualifier == expected_qualifier

    def test_is_idempotent(self):
        """is_idempotent is always true"""
        instance = self._make_one(
            "test-family", b"test-qualifier", 1234567890, 1234567891
        )
        assert instance.is_idempotent() is True

    def test___str__(self):
        """Str representation of mutations should be to_dict"""
        instance = self._make_one("test-family", b"test-qualifier")
        str_value = instance.__str__()
        dict_value = instance._to_dict()
        assert str_value == str(dict_value)


class TestDeleteAllFromFamily:
    def _target_class(self):
        from google.cloud.bigtable.data.mutations import DeleteAllFromFamily

        return DeleteAllFromFamily

    def _make_one(self, *args, **kwargs):
        return self._target_class()(*args, **kwargs)

    def test_ctor(self):
        expected_family = "test-family"
        instance = self._make_one(expected_family)
        assert instance.family_to_delete == expected_family

    def test__to_dict(self):
        """Should be unimplemented in the base class"""
        expected_family = "test-family"
        instance = self._make_one(expected_family)
        got_dict = instance._to_dict()
        assert list(got_dict.keys()) == ["delete_from_family"]
        got_inner_dict = got_dict["delete_from_family"]
        assert len(got_inner_dict.keys()) == 1
        assert got_inner_dict["family_name"] == expected_family

    def test__to_pb(self):
        """ensure proto representation is as expected"""
        import google.cloud.bigtable_v2.types.data as data_pb

        expected_family = "test-family"
        instance = self._make_one(expected_family)
        got_pb = instance._to_pb()
        assert isinstance(got_pb, data_pb.Mutation)
        assert got_pb.delete_from_family.family_name == expected_family

    def test_is_idempotent(self):
        """is_idempotent is always true"""
        instance = self._make_one("test-family")
        assert instance.is_idempotent() is True

    def test___str__(self):
        """Str representation of mutations should be to_dict"""
        instance = self._make_one("test-family")
        str_value = instance.__str__()
        dict_value = instance._to_dict()
        assert str_value == str(dict_value)


class TestDeleteFromRow:
    def _target_class(self):
        from google.cloud.bigtable.data.mutations import DeleteAllFromRow

        return DeleteAllFromRow

    def _make_one(self, *args, **kwargs):
        return self._target_class()(*args, **kwargs)

    def test_ctor(self):
        self._make_one()

    def test__to_dict(self):
        """Should be unimplemented in the base class"""
        instance = self._make_one()
        got_dict = instance._to_dict()
        assert list(got_dict.keys()) == ["delete_from_row"]
        assert len(got_dict["delete_from_row"].keys()) == 0

    def test__to_pb(self):
        """ensure proto representation is as expected"""
        import google.cloud.bigtable_v2.types.data as data_pb

        instance = self._make_one()
        got_pb = instance._to_pb()
        assert isinstance(got_pb, data_pb.Mutation)
        assert "delete_from_row" in str(got_pb)

    def test_is_idempotent(self):
        """is_idempotent is always true"""
        instance = self._make_one()
        assert instance.is_idempotent() is True

    def test___str__(self):
        """Str representation of mutations should be to_dict"""
        instance = self._make_one()
        assert instance.__str__() == "{'delete_from_row': {}}"


class TestRowMutationEntry:
    def _target_class(self):
        from google.cloud.bigtable.data.mutations import RowMutationEntry

        return RowMutationEntry

    def _make_one(self, row_key, mutations):
        return self._target_class()(row_key, mutations)

    def test_ctor(self):
        expected_key = b"row_key"
        expected_mutations = [mock.Mock()]
        instance = self._make_one(expected_key, expected_mutations)
        assert instance.row_key == expected_key
        assert list(instance.mutations) == expected_mutations

    def test_ctor_over_limit(self):
        """Should raise error if mutations exceed MAX_MUTATIONS_PER_ENTRY"""
        from google.cloud.bigtable.data.mutations import (
            _MUTATE_ROWS_REQUEST_MUTATION_LIMIT,
        )

        assert _MUTATE_ROWS_REQUEST_MUTATION_LIMIT == 100_000
        # no errors at limit
        expected_mutations = [None for _ in range(_MUTATE_ROWS_REQUEST_MUTATION_LIMIT)]
        self._make_one(b"row_key", expected_mutations)
        # error if over limit
        with pytest.raises(ValueError) as e:
            self._make_one("key", expected_mutations + [mock.Mock()])
        assert "entries must have <= 100000 mutations" in str(e.value)

    def test_ctor_str_key(self):
        expected_key = "row_key"
        expected_mutations = [mock.Mock(), mock.Mock()]
        instance = self._make_one(expected_key, expected_mutations)
        assert instance.row_key == b"row_key"
        assert list(instance.mutations) == expected_mutations

    def test_ctor_single_mutation(self):
        from google.cloud.bigtable.data.mutations import DeleteAllFromRow

        expected_key = b"row_key"
        expected_mutations = DeleteAllFromRow()
        instance = self._make_one(expected_key, expected_mutations)
        assert instance.row_key == expected_key
        assert instance.mutations == (expected_mutations,)

    def test__to_dict(self):
        expected_key = "row_key"
        mutation_mock = mock.Mock()
        n_mutations = 3
        expected_mutations = [mutation_mock for i in range(n_mutations)]
        for mock_mutations in expected_mutations:
            mock_mutations._to_dict.return_value = {"test": "data"}
        instance = self._make_one(expected_key, expected_mutations)
        expected_result = {
            "row_key": b"row_key",
            "mutations": [{"test": "data"}] * n_mutations,
        }
        assert instance._to_dict() == expected_result
        assert mutation_mock._to_dict.call_count == n_mutations

    def test__to_pb(self):
        from google.cloud.bigtable_v2.types.bigtable import MutateRowsRequest
        from google.cloud.bigtable_v2.types.data import Mutation

        expected_key = "row_key"
        mutation_mock = mock.Mock()
        n_mutations = 3
        expected_mutations = [mutation_mock for i in range(n_mutations)]
        for mock_mutations in expected_mutations:
            mock_mutations._to_pb.return_value = Mutation()
        instance = self._make_one(expected_key, expected_mutations)
        pb_result = instance._to_pb()
        assert isinstance(pb_result, MutateRowsRequest.Entry)
        assert pb_result.row_key == b"row_key"
        assert pb_result.mutations == [Mutation()] * n_mutations
        assert mutation_mock._to_pb.call_count == n_mutations

    @pytest.mark.parametrize(
        "mutations,result",
        [
            ([mock.Mock(is_idempotent=lambda: True)], True),
            ([mock.Mock(is_idempotent=lambda: False)], False),
            (
                [
                    mock.Mock(is_idempotent=lambda: True),
                    mock.Mock(is_idempotent=lambda: False),
                ],
                False,
            ),
            (
                [
                    mock.Mock(is_idempotent=lambda: True),
                    mock.Mock(is_idempotent=lambda: True),
                ],
                True,
            ),
        ],
    )
    def test_is_idempotent(self, mutations, result):
        instance = self._make_one("row_key", mutations)
        assert instance.is_idempotent() == result

    def test_empty_mutations(self):
        with pytest.raises(ValueError) as e:
            self._make_one("row_key", [])
        assert "must not be empty" in str(e.value)

    @pytest.mark.parametrize("test_dict", [{}, {"key": "value"}])
    def test_size(self, test_dict):
        from sys import getsizeof

        """Size should return size of dict representation"""
        self_mock = mock.Mock()
        self_mock._to_dict.return_value = test_dict
        size_value = self._target_class().size(self_mock)
        assert size_value == getsizeof(test_dict)

    def test__from_dict_mock(self):
        """
        test creating instance from entry dict, with mocked mutation._from_dict
        """
        expected_key = b"row_key"
        expected_mutations = [mock.Mock(), mock.Mock()]
        input_dict = {
            "row_key": expected_key,
            "mutations": [{"test": "data"}, {"another": "data"}],
        }
        with mock.patch.object(mutations.Mutation, "_from_dict") as inner_from_dict:
            inner_from_dict.side_effect = expected_mutations
            instance = self._target_class()._from_dict(input_dict)
        assert instance.row_key == b"row_key"
        assert inner_from_dict.call_count == 2
        assert len(instance.mutations) == 2
        assert instance.mutations[0] == expected_mutations[0]
        assert instance.mutations[1] == expected_mutations[1]

    def test__from_dict(self):
        """
        test creating end-to-end with a real mutation instance
        """
        input_dict = {
            "row_key": b"row_key",
            "mutations": [{"delete_from_family": {"family_name": "test_family"}}],
        }
        instance = self._target_class()._from_dict(input_dict)
        assert instance.row_key == b"row_key"
        assert len(instance.mutations) == 1
        assert isinstance(instance.mutations[0], mutations.DeleteAllFromFamily)
        assert instance.mutations[0].family_to_delete == "test_family"


class TestAddToCell:
    def _target_class(self):
        from google.cloud.bigtable.data.mutations import AddToCell

        return AddToCell

    def _make_one(self, *args, **kwargs):
        return self._target_class()(*args, **kwargs)

    @pytest.mark.parametrize("input_val", [2**63, -(2**63) - 1, 2**64, -(2**64)])
    def test_ctor_large_int(self, input_val):
        with pytest.raises(ValueError) as e:
            self._make_one(
                family="f", qualifier=b"b", value=input_val, timestamp_micros=123
            )
        assert "int values must be between" in str(e.value)

    @pytest.mark.parametrize("input_val", [-(2**63), 2**63 - 1])
    def test_ctor_int64_bounds(self, input_val):
        instance = self._make_one(
            family="f", qualifier=b"b", value=input_val, timestamp_micros=123
        )
        assert instance.value == input_val
        assert instance._to_pb().add_to_cell.input.int_value == input_val

    @pytest.mark.parametrize("input_val", [True, False])
    def test_ctor_bool_value(self, input_val):
        with pytest.raises(TypeError) as e:
            self._make_one(
                family="f", qualifier=b"b", value=input_val, timestamp_micros=123
            )
        assert "value must be int" in str(e.value)

    @pytest.mark.parametrize("input_ts", [True, False])
    def test_ctor_bool_timestamp(self, input_ts):
        with pytest.raises(TypeError) as e:
            self._make_one(
                family="f", qualifier=b"b", value=123, timestamp_micros=input_ts
            )
        assert "timestamp_micros must be int" in str(e.value)

    @pytest.mark.parametrize("input_val", ["", "a", "abc", "hello world!"])
    def test_ctor_str_value(self, input_val):
        with pytest.raises(TypeError) as e:
            self._make_one(
                family="f", qualifier=b"b", value=input_val, timestamp_micros=123
            )
        assert "value must be int" in str(e.value)

    def test_ctor(self):
        """Ensure constructor sets expected values"""
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = 1234
        expected_timestamp = 1234567890
        instance = self._make_one(
            expected_family, expected_qualifier, expected_value, expected_timestamp
        )
        assert instance.family == expected_family
        assert instance.qualifier == expected_qualifier
        assert instance.value == expected_value
        assert instance.timestamp == expected_timestamp

    def test_ctor_negative_timestamp(self):
        """Only non-negative timestamps are valid"""
        with pytest.raises(ValueError) as e:
            self._make_one("test-family", b"test-qualifier", 1234, -2)
        assert "timestamp must be non-negative" in str(e.value)

    def test__to_dict(self):
        """ensure dict representation is as expected"""
        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = 1234
        expected_timestamp = 123456789
        instance = self._make_one(
            expected_family, expected_qualifier, expected_value, expected_timestamp
        )
        got_dict = instance._to_dict()
        assert list(got_dict.keys()) == ["add_to_cell"]
        got_inner_dict = got_dict["add_to_cell"]
        assert got_inner_dict["family_name"] == expected_family
        assert got_inner_dict["column_qualifier"]["raw_value"] == expected_qualifier
        assert got_inner_dict["timestamp"]["raw_timestamp_micros"] == expected_timestamp
        assert got_inner_dict["input"]["int_value"] == expected_value
        assert len(got_inner_dict.keys()) == 4

    def test__to_pb(self):
        """ensure proto representation is as expected"""
        import google.cloud.bigtable_v2.types.data as data_pb

        expected_family = "test-family"
        expected_qualifier = b"test-qualifier"
        expected_value = 1234
        expected_timestamp = 123456789
        instance = self._make_one(
            expected_family, expected_qualifier, expected_value, expected_timestamp
        )
        got_pb = instance._to_pb()
        assert isinstance(got_pb, data_pb.Mutation)
        assert got_pb.add_to_cell.family_name == expected_family
        assert got_pb.add_to_cell.column_qualifier.raw_value == expected_qualifier
        assert got_pb.add_to_cell.timestamp.raw_timestamp_micros == expected_timestamp
        assert got_pb.add_to_cell.input.int_value == expected_value

    @pytest.mark.parametrize(
        "timestamp",
        [
            (1234567890),
            (1),
            (0),
        ],
    )
    def test_is_idempotent(self, timestamp):
        """is_idempotent is not based on the timestamp"""
        instance = self._make_one("test-family", b"test-qualifier", 1234, timestamp)
        assert not instance.is_idempotent()

    def test___str__(self):
        """Str representation of mutations should be to_dict"""
        instance = self._make_one("test-family", b"test-qualifier", 1234, 1234567890)
        str_value = instance.__str__()
        dict_value = instance._to_dict()
        assert str_value == str(dict_value)
