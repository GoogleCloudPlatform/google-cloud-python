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


class TestBaseReadModifyWriteRule:
    def _target_class(self):
        from google.cloud.bigtable.data.read_modify_write_rules import (
            ReadModifyWriteRule,
        )

        return ReadModifyWriteRule

    def test_abstract(self):
        """should not be able to instantiate"""
        with pytest.raises(TypeError):
            self._target_class()(family="foo", qualifier=b"bar")

    def test__to_dict(self):
        """
        to_dict not implemented in base class
        """
        with pytest.raises(NotImplementedError):
            self._target_class()._to_dict(mock.Mock())


class TestIncrementRule:
    def _target_class(self):
        from google.cloud.bigtable.data.read_modify_write_rules import IncrementRule

        return IncrementRule

    @pytest.mark.parametrize(
        "args,expected",
        [
            (("fam", b"qual", 1), ("fam", b"qual", 1)),
            (("fam", b"qual", -12), ("fam", b"qual", -12)),
            (("fam", b"qual", -(2**63)), ("fam", b"qual", -(2**63))),
            (("fam", b"qual", 2**63 - 1), ("fam", b"qual", 2**63 - 1)),
            (("fam", "qual", 1), ("fam", b"qual", 1)),
            (("fam", "qual", 0), ("fam", b"qual", 0)),
            (("", "", 0), ("", b"", 0)),
            (("f", b"q"), ("f", b"q", 1)),
        ],
    )
    def test_ctor(self, args, expected):
        instance = self._target_class()(*args)
        assert instance.family == expected[0]
        assert instance.qualifier == expected[1]
        assert instance.increment_amount == expected[2]

    @pytest.mark.parametrize(
        "input_amount", [True, False, 1.1, None, "1", object(), "", b"", b"1"]
    )
    def test_ctor_bad_input(self, input_amount):
        with pytest.raises(TypeError) as e:
            self._target_class()("fam", b"qual", input_amount)
        assert "increment_amount must be an integer" in str(e.value)

    @pytest.mark.parametrize(
        "large_value", [2**63, -(2**63) - 1, 2**64, 2**64 + 1, -(2**64), -(2**64) - 1]
    )
    def test_ctor_large_values(self, large_value):
        with pytest.raises(ValueError) as e:
            self._target_class()("fam", b"qual", large_value)
        assert "increment_amount must be between -2**63 and 2**63" in str(e.value)

    @pytest.mark.parametrize(
        "args,expected",
        [
            (("fam", b"qual", 1), ("fam", b"qual", 1)),
            (("fam", b"qual", -12), ("fam", b"qual", -12)),
            (("fam", "qual", 1), ("fam", b"qual", 1)),
            (("fam", "qual", 0), ("fam", b"qual", 0)),
            (("", "", 0), ("", b"", 0)),
            (("f", b"q"), ("f", b"q", 1)),
        ],
    )
    def test__to_dict(self, args, expected):
        instance = self._target_class()(*args)
        expected = {
            "family_name": expected[0],
            "column_qualifier": expected[1],
            "increment_amount": expected[2],
        }
        assert instance._to_dict() == expected

    @pytest.mark.parametrize(
        "args,expected",
        [
            (("fam", b"qual", 1), ("fam", b"qual", 1)),
            (("fam", b"qual", -12), ("fam", b"qual", -12)),
            (("fam", "qual", 1), ("fam", b"qual", 1)),
            (("fam", "qual", 0), ("fam", b"qual", 0)),
            (("", "", 0), ("", b"", 0)),
            (("f", b"q"), ("f", b"q", 1)),
        ],
    )
    def test__to_pb(self, args, expected):
        import google.cloud.bigtable_v2.types.data as data_pb

        instance = self._target_class()(*args)
        pb_result = instance._to_pb()
        assert isinstance(pb_result, data_pb.ReadModifyWriteRule)
        assert pb_result.family_name == expected[0]
        assert pb_result.column_qualifier == expected[1]
        assert pb_result.increment_amount == expected[2]


class TestAppendValueRule:
    def _target_class(self):
        from google.cloud.bigtable.data.read_modify_write_rules import AppendValueRule

        return AppendValueRule

    @pytest.mark.parametrize(
        "args,expected",
        [
            (("fam", b"qual", b"val"), ("fam", b"qual", b"val")),
            (("fam", "qual", b"val"), ("fam", b"qual", b"val")),
            (("", "", b""), ("", b"", b"")),
            (("f", "q", "str_val"), ("f", b"q", b"str_val")),
            (("f", "q", ""), ("f", b"q", b"")),
        ],
    )
    def test_ctor(self, args, expected):
        instance = self._target_class()(*args)
        assert instance.family == expected[0]
        assert instance.qualifier == expected[1]
        assert instance.append_value == expected[2]

    @pytest.mark.parametrize("input_val", [5, 1.1, None, object()])
    def test_ctor_bad_input(self, input_val):
        with pytest.raises(TypeError) as e:
            self._target_class()("fam", b"qual", input_val)
        assert "append_value must be bytes or str" in str(e.value)

    @pytest.mark.parametrize(
        "args,expected",
        [
            (("fam", b"qual", b"val"), ("fam", b"qual", b"val")),
            (("fam", "qual", b"val"), ("fam", b"qual", b"val")),
            (("", "", b""), ("", b"", b"")),
        ],
    )
    def test__to_dict(self, args, expected):
        instance = self._target_class()(*args)
        expected = {
            "family_name": expected[0],
            "column_qualifier": expected[1],
            "append_value": expected[2],
        }
        assert instance._to_dict() == expected

    @pytest.mark.parametrize(
        "args,expected",
        [
            (("fam", b"qual", b"val"), ("fam", b"qual", b"val")),
            (("fam", "qual", b"val"), ("fam", b"qual", b"val")),
            (("", "", b""), ("", b"", b"")),
        ],
    )
    def test__to_pb(self, args, expected):
        import google.cloud.bigtable_v2.types.data as data_pb

        instance = self._target_class()(*args)
        pb_result = instance._to_pb()
        assert isinstance(pb_result, data_pb.ReadModifyWriteRule)
        assert pb_result.family_name == expected[0]
        assert pb_result.column_qualifier == expected[1]
        assert pb_result.append_value == expected[2]
