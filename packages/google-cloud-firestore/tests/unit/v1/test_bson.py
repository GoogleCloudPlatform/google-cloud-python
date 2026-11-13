# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#
"""Unit tests for google.cloud.firestore_v1.bson classes."""

import copy
import decimal
import math
import pickle

import pytest

from google.cloud.firestore_v1.bson import (
    BSONBinary,
    BSONDecimal128,
    BSONInt32,
    BSONMaxKey,
    BSONMinKey,
    BSONObjectId,
    BSONRegex,
    BSONTimestamp,
    BSONType,
)


def test_bson_type_abc_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BSONType()  # type: ignore


def test_bson_type_inheritance():
    oid = BSONObjectId("507f191e810c19729de860ea")
    assert isinstance(oid, BSONType)


def test_bson_object_id_from_hex_string():
    hex_str = "507f191e810c19729de860ea"
    oid = BSONObjectId(hex_str)
    assert oid.value == hex_str


def test_bson_object_id_from_uppercase_hex_string():
    oid = BSONObjectId("507F191E810C19729DE860EA")
    assert oid.value == "507f191e810c19729de860ea"


def test_bson_object_id_from_bytes():
    raw_bytes = b"\x50\x7f\x19\x1e\x81\x0c\x19\x72\x9d\xe8\x60\xea"
    oid = BSONObjectId(raw_bytes)
    assert oid.value == "507f191e810c19729de860ea"


def test_bson_object_id_to_map_value():
    hex_str = "507f191e810c19729de860ea"
    oid = BSONObjectId(hex_str)
    assert oid._to_map_value() == {"__oid__": hex_str}


@pytest.mark.parametrize(
    "invalid_input, exc_type, match_msg",
    [
        ("invalid_hex", ValueError, "24-character hex string"),
        (b"short", ValueError, "12 raw bytes"),
        (bytearray(b"\x50" * 12), TypeError, "requires str or bytes"),
        (12345, TypeError, "requires str or bytes"),
        (None, TypeError, "requires str or bytes"),
    ],
)
def test_bson_object_id_invalid_inputs(invalid_input, exc_type, match_msg):
    with pytest.raises(exc_type, match=match_msg):
        BSONObjectId(invalid_input)


def test_bson_object_id_equality():
    oid1 = BSONObjectId("507f191e810c19729de860ea")
    oid2 = BSONObjectId("507f191e810c19729de860ea")
    oid3 = BSONObjectId("507f191e810c19729de860eb")

    assert oid1 == oid2
    assert oid1 != oid3
    assert oid1 != "507f191e810c19729de860ea"


def test_bson_object_id_equality_not_implemented():
    oid = BSONObjectId("507f191e810c19729de860ea")

    class CooperativeOther:
        def __eq__(self, other):
            return True

    assert oid == CooperativeOther()


def test_bson_object_id_hash_and_dict_key():
    oid1 = BSONObjectId("507f191e810c19729de860ea")
    oid2 = BSONObjectId("507f191e810c19729de860ea")

    assert hash(oid1) == hash(oid2)
    lookup = {oid1: "success"}
    assert lookup[oid2] == "success"
    assert len({oid1, oid2}) == 1


def test_bson_object_id_repr():
    oid = BSONObjectId("507f191e810c19729de860ea")
    assert repr(oid) == "BSONObjectId('507f191e810c19729de860ea')"


def test_bson_object_id_str():
    oid = BSONObjectId("507f191e810c19729de860ea")
    assert str(oid) == "507f191e810c19729de860ea"


def test_bson_object_id_copy():
    oid = BSONObjectId("507f191e810c19729de860ea")
    assert copy.copy(oid) == oid
    assert copy.deepcopy(oid) == oid


def test_bson_object_id_pickle():
    oid = BSONObjectId("507f191e810c19729de860ea")
    unpickled = pickle.loads(pickle.dumps(oid))
    assert unpickled == oid
    assert unpickled.value == oid.value


def test_bson_minkey_to_map_value():
    assert BSONMinKey()._to_map_value() == {"__min__": None}


def test_bson_minkey_equality():
    key1 = BSONMinKey()
    key2 = BSONMinKey()
    assert key1 == key2
    assert key1 != BSONMaxKey()
    assert key1 != "min"


def test_bson_minkey_hash_and_dict_key():
    key1 = BSONMinKey()
    key2 = BSONMinKey()
    assert hash(key1) == hash(key2)
    assert len({key1, key2}) == 1


def test_bson_minkey_repr():
    assert repr(BSONMinKey()) == "BSONMinKey()"


def test_bson_minkey_copy():
    key = BSONMinKey()
    assert copy.copy(key) == key
    assert copy.deepcopy(key) == key


def test_bson_minkey_pickle():
    key = BSONMinKey()
    assert pickle.loads(pickle.dumps(key)) == key


def test_bson_maxkey_to_map_value():
    assert BSONMaxKey()._to_map_value() == {"__max__": None}


def test_bson_maxkey_equality():
    key1 = BSONMaxKey()
    key2 = BSONMaxKey()
    assert key1 == key2
    assert key1 != BSONMinKey()
    assert key1 != "max"


def test_bson_maxkey_hash_and_dict_key():
    key1 = BSONMaxKey()
    key2 = BSONMaxKey()
    assert hash(key1) == hash(key2)
    assert len({key1, key2}) == 1


def test_bson_maxkey_repr():
    assert repr(BSONMaxKey()) == "BSONMaxKey()"


def test_bson_maxkey_copy():
    key = BSONMaxKey()
    assert copy.copy(key) == key
    assert copy.deepcopy(key) == key


def test_bson_maxkey_pickle():
    key = BSONMaxKey()
    assert pickle.loads(pickle.dumps(key)) == key


def test_bson_int32_valid():
    val = BSONInt32(42)
    assert val.value == 42
    assert int(val) == 42
    assert str(val) == "42"
    assert repr(val) == "BSONInt32(42)"
    assert val._to_map_value() == {"__int__": 42}


def test_bson_int32_boundaries():
    min_val = BSONInt32(-2147483648)
    max_val = BSONInt32(2147483647)
    assert min_val.value == -2147483648
    assert max_val.value == 2147483647


@pytest.mark.parametrize(
    "invalid_input, exc_type, match_msg",
    [
        (2147483648, ValueError, "between -2147483648 and 2147483647"),
        (-2147483649, ValueError, "between -2147483648 and 2147483647"),
        ("42", TypeError, "requires an int"),
        (42.0, TypeError, "requires an int"),
        (True, TypeError, "requires an int"),
        (False, TypeError, "requires an int"),
        (None, TypeError, "requires an int"),
    ],
)
def test_bson_int32_invalid(invalid_input, exc_type, match_msg):
    with pytest.raises(exc_type, match=match_msg):
        BSONInt32(invalid_input)


def test_bson_int32_equality():
    val1 = BSONInt32(42)
    val2 = BSONInt32(42)
    val3 = BSONInt32(100)

    assert val1 == val2
    assert val1 != val3
    assert val1 != 42  # BSONInt32 is not equal to plain int

    class CooperativeOther:
        def __eq__(self, other):
            return True

    assert val1 == CooperativeOther()


def test_bson_int32_hash_and_dict_key():
    val1 = BSONInt32(42)
    val2 = BSONInt32(42)

    assert hash(val1) == hash(val2)
    assert hash(val1) != hash(42)
    lookup = {val1: "success"}
    assert lookup[val2] == "success"
    assert len({val1, val2}) == 1


def test_bson_int32_copy():
    val = BSONInt32(42)
    assert copy.copy(val) == val
    assert copy.deepcopy(val) == val


def test_bson_int32_pickle():
    val = BSONInt32(42)
    assert pickle.loads(pickle.dumps(val)) == val


def test_bson_binary_custom_subtype():
    val = BSONBinary(bytearray(b"world"), subtype=128)
    assert val.data == b"world"
    assert val.subtype == 128


def test_bson_binary_to_map_value():
    assert BSONBinary(b"world", subtype=128)._to_map_value() == {
        "__binary__": b"\x80world"
    }


def test_bson_binary_bytes_coercion():
    assert bytes(BSONBinary(b"hello", subtype=1)) == b"hello"


def test_bson_binary_repr():
    assert (
        repr(BSONBinary(b"world", subtype=128)) == "BSONBinary(b'world', subtype=128)"
    )


def test_bson_binary_boundaries():
    bin_min = BSONBinary(b"test", subtype=1)
    bin_max = BSONBinary(b"test", subtype=255)
    assert bin_min.subtype == 1
    assert bin_max.subtype == 255


@pytest.mark.parametrize(
    "data_input, subtype_input, exc_type, match_msg",
    [
        ("not bytes", 1, TypeError, "must be bytes or bytearray"),
        (123, 1, TypeError, "must be bytes or bytearray"),
        (None, 1, TypeError, "must be bytes or bytearray"),
        (b"data", 256, ValueError, "must be between"),
        (b"data", 0, ValueError, "must be between"),
        (b"data", -1, ValueError, "must be between"),
        (b"data", True, TypeError, "subtype must be an int"),
        (b"data", False, TypeError, "subtype must be an int"),
        (b"data", "1", TypeError, "subtype must be an int"),
    ],
)
def test_bson_binary_invalid_inputs(data_input, subtype_input, exc_type, match_msg):
    with pytest.raises(exc_type, match=match_msg):
        BSONBinary(data_input, subtype=subtype_input)


def test_bson_binary_equality():
    bin1 = BSONBinary(b"abc", subtype=1)
    bin2 = BSONBinary(b"abc", subtype=1)
    bin3 = BSONBinary(b"abc", subtype=2)
    bin4 = BSONBinary(b"xyz", subtype=1)
    assert bin1 == bin2
    assert bin1 != bin3
    assert bin1 != bin4
    assert bin1 != b"abc"


def test_bson_binary_hash_and_dict_key():
    bin1 = BSONBinary(b"abc", subtype=1)
    bin2 = BSONBinary(b"abc", subtype=1)
    assert hash(bin1) == hash(bin2)
    assert len({bin1, bin2}) == 1


def test_bson_binary_copy():
    val = BSONBinary(b"hello", subtype=5)
    assert copy.copy(val) == val
    assert copy.deepcopy(val) == val


def test_bson_binary_pickle():
    val = BSONBinary(b"hello", subtype=5)
    assert pickle.loads(pickle.dumps(val)) == val


def test_bson_timestamp_valid():
    ts = BSONTimestamp(1700000000, 42)
    assert ts.seconds == 1700000000
    assert ts.increment == 42
    assert ts._to_map_value() == {
        "__request_timestamp__": {
            "seconds": 1700000000,
            "increment": 42,
        }
    }
    assert repr(ts) == "BSONTimestamp(seconds=1700000000, increment=42)"


def test_bson_timestamp_boundaries():
    ts_min = BSONTimestamp(0, 0)
    ts_max = BSONTimestamp(4294967295, 4294967295)
    assert ts_min.seconds == 0
    assert ts_min.increment == 0
    assert ts_max.seconds == 4294967295
    assert ts_max.increment == 4294967295


@pytest.mark.parametrize(
    "sec_input, inc_input, exc_type, match_msg",
    [
        (True, 0, TypeError, "seconds must be an int"),
        (0, False, TypeError, "increment must be an int"),
        ("1700000000", 0, TypeError, "seconds must be an int"),
        (0, 1.5, TypeError, "increment must be an int"),
    ],
)
def test_bson_timestamp_invalid_inputs(sec_input, inc_input, exc_type, match_msg):
    with pytest.raises(exc_type, match=match_msg):
        BSONTimestamp(sec_input, inc_input)


def test_bson_timestamp_equality():
    ts1 = BSONTimestamp(100, 1)
    ts2 = BSONTimestamp(100, 1)
    ts3 = BSONTimestamp(100, 2)
    ts4 = BSONTimestamp(200, 1)
    assert ts1 == ts2
    assert ts1 != ts3
    assert ts1 != ts4
    assert ts1 != 100


def test_bson_timestamp_hash_and_dict_key():
    ts1 = BSONTimestamp(100, 1)
    ts2 = BSONTimestamp(100, 1)
    assert hash(ts1) == hash(ts2)
    assert len({ts1, ts2}) == 1


def test_bson_timestamp_copy():
    ts = BSONTimestamp(100, 1)
    assert copy.copy(ts) == ts
    assert copy.deepcopy(ts) == ts


def test_bson_timestamp_pickle():
    ts = BSONTimestamp(100, 1)
    assert pickle.loads(pickle.dumps(ts)) == ts


def test_bson_regex_valid():
    rx = BSONRegex("^hello.*$", options="i")
    assert rx.pattern == "^hello.*$"
    assert rx.options == "i"
    assert rx._to_map_value() == {
        "__regex__": {
            "pattern": "^hello.*$",
            "options": "i",
        }
    }
    assert repr(rx) == "BSONRegex('^hello.*$', options='i')"


def test_bson_regex_options_sorting_and_deduplication():
    rx1 = BSONRegex("foo", options="msi")
    assert rx1.options == "ims"

    rx2 = BSONRegex("foo", options="mmiis")
    assert rx2.options == "ims"

    rx3 = BSONRegex("foo", options="xl")
    assert rx3.options == "lx"


@pytest.mark.parametrize(
    "pattern_input, options_input, exc_type, match_msg",
    [
        (123, "i", TypeError, "pattern must be a str"),
        (None, "i", TypeError, "pattern must be a str"),
        ("foo", 123, TypeError, "options must be a str"),
        ("foo", True, TypeError, "options must be a str"),
        ("foo", [1, 2], TypeError, "options must be a str"),
    ],
)
def test_bson_regex_invalid_inputs(pattern_input, options_input, exc_type, match_msg):
    with pytest.raises(exc_type, match=match_msg):
        BSONRegex(pattern_input, options_input)


def test_bson_regex_equality():
    rx1 = BSONRegex("^abc", options="i")
    rx2 = BSONRegex("^abc", options="i")
    rx3 = BSONRegex("^abc", options="m")
    rx4 = BSONRegex("^xyz", options="i")
    assert rx1 == rx2
    assert rx1 != rx3
    assert rx1 != rx4
    assert rx1 != "^abc"


def test_bson_regex_hash_and_dict_key():
    rx1 = BSONRegex("^abc", options="i")
    rx2 = BSONRegex("^abc", options="i")
    assert hash(rx1) == hash(rx2)
    assert len({rx1, rx2}) == 1


def test_bson_regex_copy():
    rx = BSONRegex("^abc", options="i")
    assert copy.copy(rx) == rx
    assert copy.deepcopy(rx) == rx


def test_bson_regex_pickle():
    rx = BSONRegex("^abc", options="i")
    assert pickle.loads(pickle.dumps(rx)) == rx


def test_bson_decimal128_valid():
    dec1 = BSONDecimal128("123.45")
    assert dec1.value == "123.45"
    assert dec1.to_decimal() == decimal.Decimal("123.45")
    assert dec1._to_map_value() == {"__decimal128__": "123.45"}
    assert repr(dec1) == "BSONDecimal128('123.45')"
    assert str(dec1) == "123.45"

    dec2 = BSONDecimal128(42)
    assert dec2.value == "42"

    dec3 = BSONDecimal128(decimal.Decimal("99.99"))
    assert dec3.value == "99.99"

    dec4 = BSONDecimal128(dec1)
    assert dec4.value == "123.45"


def test_bson_decimal128_float_and_int():
    dec = BSONDecimal128("123.45")
    assert float(dec) == 123.45
    assert int(dec) == 123


@pytest.mark.parametrize(
    "special_val",
    [
        "inf",
        "-inf",
        "Infinity",
        "-Infinity",
        "NaN",
        "-NaN",
        "sNaN",
        "-sNaN",
    ],
)
def test_bson_decimal128_special_values(special_val):
    dec1 = BSONDecimal128(special_val)
    dec2 = BSONDecimal128(special_val)
    assert dec1.value == str(special_val)
    assert dec1._to_map_value() == {"__decimal128__": str(special_val)}
    assert dec1 == dec2
    assert hash(dec1) == hash(dec2)

    if "inf" in str(special_val).lower():
        assert math.isinf(float(dec1))
    elif "nan" in str(special_val).lower():
        assert math.isnan(float(dec1))


@pytest.mark.parametrize(
    "val_input, exc_type, match_msg",
    [
        (True, TypeError, "value must be a Decimal, str, or int"),
        (False, TypeError, "value must be a Decimal, str, or int"),
        ([1, 2], TypeError, "value must be a Decimal, str, or int"),
        (1.5, TypeError, "does not accept float values"),
        (float("inf"), TypeError, "does not accept float values"),
        (float("nan"), TypeError, "does not accept float values"),
        ("not-a-number", ValueError, "Cannot convert 'not-a-number' to Decimal"),
        ("12.34.56", ValueError, "Cannot convert '12.34.56' to Decimal"),
    ],
)
def test_bson_decimal128_invalid_inputs(val_input, exc_type, match_msg):
    with pytest.raises(exc_type, match=match_msg):
        BSONDecimal128(val_input)


def test_bson_decimal128_equality():
    d1 = BSONDecimal128("123.45")
    d2 = BSONDecimal128("123.45")
    d3 = BSONDecimal128("678.90")
    assert d1 == d2
    assert d1 != d3
    assert d1 != "123.45"
    # Pure container parity with PyMongo: BSONDecimal128 does not equate to
    # standard decimal.Decimal directly; developers use .to_decimal() for math/comparison.
    assert d1 != decimal.Decimal("123.45")
    assert d1.to_decimal() == decimal.Decimal("123.45")

    d_trail = BSONDecimal128("1.0")
    d_int = BSONDecimal128("1")
    assert d_trail == d_int

    nan1 = BSONDecimal128("NaN")
    nan2 = BSONDecimal128("NaN")
    # Two BSONDecimal128 instances compare equal for NaN (PyMongo container parity)
    assert nan1 == nan2


def test_bson_decimal128_hash_and_dict_key():
    d1 = BSONDecimal128("123.45")
    d2 = BSONDecimal128("123.45")
    d3 = BSONDecimal128("678.90")

    # Hash invariant test: if a == b, then hash(a) == hash(b)
    assert hash(d1) == hash(d2)
    assert len({d1, d2}) == 1
    assert len({d1, d3}) == 2

    nan1 = BSONDecimal128("NaN")
    nan2 = BSONDecimal128("NaN")
    assert hash(nan1) == hash(nan2)
    assert len({nan1, nan2}) == 1


def test_bson_decimal128_copy():
    d = BSONDecimal128("123.45")
    assert copy.copy(d) == d
    assert copy.deepcopy(d) == d


def test_bson_decimal128_pickle():
    d = BSONDecimal128("123.45")
    assert pickle.loads(pickle.dumps(d)) == d


def test_bson_from_dict_exception_fallback():
    # Corrupted or malformed BSON wire dictionary shapes gracefully return None
    assert BSONType._from_dict({"__int__": "not-an-int"}) is None
    assert BSONType._from_dict({"__oid__": "short"}) is None
    assert BSONType._from_dict({"__decimal128__": "invalid-decimal"}) is None
    assert BSONType._from_dict({"__unknown__": "value"}) is None
    assert BSONType._from_dict("not-a-dict") is None
    assert BSONType._from_dict({"a": 1, "b": 2}) is None
