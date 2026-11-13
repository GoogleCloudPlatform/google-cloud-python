# -*- coding: utf-8 -*-
# Copyright 2017 Google LLC All rights reserved.
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

import mock
import pytest


def _make_order(*args, **kwargs):
    from google.cloud.firestore_v1.order import Order

    return Order(*args, **kwargs)


def test_order_compare_across_heterogenous_values():
    from google.cloud.firestore_v1.order import Order

    # Constants used to represent min/max values of storage types.
    int_max_value = 2**31 - 1
    int_min_value = -(2**31)
    float_min_value = 1.175494351**-38
    float_nan = float("nan")
    inf = float("inf")

    groups = [None] * 68

    groups[0] = [nullValue()]

    groups[1] = [_boolean_value(False)]
    groups[2] = [_boolean_value(True)]

    # numbers
    groups[3] = [_double_value(float_nan), _double_value(float_nan)]
    groups[4] = [_double_value(-inf)]
    groups[5] = [_int_value(int_min_value - 1)]
    groups[6] = [_int_value(int_min_value)]
    groups[7] = [_double_value(-1.1)]
    # Integers and Doubles order the same.
    groups[8] = [_int_value(-1), _double_value(-1.0)]
    groups[9] = [_double_value(-float_min_value)]
    # zeros all compare the same.
    groups[10] = [
        _int_value(0),
        _double_value(-0.0),
        _double_value(0.0),
        _double_value(+0.0),
    ]
    groups[11] = [_double_value(float_min_value)]
    groups[12] = [_int_value(1), _double_value(1.0)]
    groups[13] = [_double_value(1.1)]
    groups[14] = [_int_value(int_max_value)]
    groups[15] = [_int_value(int_max_value + 1)]
    groups[16] = [_double_value(inf)]

    groups[17] = [_timestamp_value(123, 0)]
    groups[18] = [_timestamp_value(123, 123)]
    groups[19] = [_timestamp_value(345, 0)]

    # strings
    groups[20] = [_string_value("")]
    groups[21] = [_string_value("\u0000\ud7ff\ue000\uffff")]
    groups[22] = [_string_value("(╯°□°）╯︵ ┻━┻")]
    groups[23] = [_string_value("a")]
    groups[24] = [_string_value("abc def")]
    # latin small letter e + combining acute accent + latin small letter b
    groups[25] = [_string_value("e\u0301b")]
    groups[26] = [_string_value("æ")]
    # latin small letter e with acute accent + latin small letter a
    groups[27] = [_string_value("\u00e9a")]

    # blobs
    groups[28] = [_blob_value(b"")]
    groups[29] = [_blob_value(b"\x00")]
    groups[30] = [_blob_value(b"\x00\x01\x02\x03\x04")]
    groups[31] = [_blob_value(b"\x00\x01\x02\x04\x03")]
    groups[32] = [_blob_value(b"\x7f")]

    # resource names
    groups[33] = [_reference_value("projects/p1/databases/d1/documents/c1/doc1")]
    groups[34] = [_reference_value("projects/p1/databases/d1/documents/c1/doc2")]
    groups[35] = [
        _reference_value("projects/p1/databases/d1/documents/c1/doc2/c2/doc1")
    ]
    groups[36] = [
        _reference_value("projects/p1/databases/d1/documents/c1/doc2/c2/doc2")
    ]
    groups[37] = [_reference_value("projects/p1/databases/d1/documents/c10/doc1")]
    groups[38] = [_reference_value("projects/p1/databases/d1/documents/c2/doc1")]
    groups[39] = [_reference_value("projects/p2/databases/d2/documents/c1/doc1")]
    groups[40] = [_reference_value("projects/p2/databases/d2/documents/c1-/doc1")]
    groups[41] = [_reference_value("projects/p2/databases/d3/documents/c1-/doc1")]

    # geo points
    groups[42] = [_geoPoint_value(-90, -180)]
    groups[43] = [_geoPoint_value(-90, 0)]
    groups[44] = [_geoPoint_value(-90, 180)]
    groups[45] = [_geoPoint_value(0, -180)]
    groups[46] = [_geoPoint_value(0, 0)]
    groups[47] = [_geoPoint_value(0, 180)]
    groups[48] = [_geoPoint_value(1, -180)]
    groups[49] = [_geoPoint_value(1, 0)]
    groups[50] = [_geoPoint_value(1, 180)]
    groups[51] = [_geoPoint_value(90, -180)]
    groups[52] = [_geoPoint_value(90, 0)]
    groups[53] = [_geoPoint_value(90, 180)]

    # arrays
    groups[54] = [_array_value()]
    groups[55] = [_array_value(["bar"])]
    groups[56] = [_array_value(["foo"])]
    groups[57] = [_array_value(["foo", 0])]
    groups[58] = [_array_value(["foo", 1])]
    groups[59] = [_array_value(["foo", "0"])]

    # vectors
    groups[60] = [_object_value({"__type__": "__vector__", "value": [3.0, 2.0]})]
    groups[61] = [_object_value({"__type__": "__vector__", "value": [1.0, 2.0, 5.0]})]
    groups[62] = [_object_value({"__type__": "__vector__", "value": [2.0, 2.0, 5.0]})]

    # objects
    groups[63] = [_object_value({"bar": 0})]
    groups[64] = [_object_value({"bar": 0, "foo": 1})]
    groups[65] = [_object_value({"bar": 1})]
    groups[66] = [_object_value({"bar": 2})]
    groups[67] = [_object_value({"bar": "0"})]

    target = _make_order()

    for i in range(len(groups)):
        for left in groups[i]:
            for j in range(len(groups)):
                for right in groups[j]:
                    expected = Order._compare_to(i, j)
                    assert target.compare(left, right) == expected

                    expected = Order._compare_to(j, i)
                    assert target.compare(right, left) == expected


def test_order_compare_w_typeorder_type_failure():
    target = _make_order()
    left = mock.Mock()
    left.WhichOneof.return_value = "imaginary-type"

    with pytest.raises(ValueError) as exc_info:
        target.compare(left, mock.Mock())

    (message,) = exc_info.value.args
    assert message.startswith("Could not detect value")


def test_order_compare_w_failure_to_find_type():
    from google.cloud.firestore_v1.order import TypeOrder

    target = _make_order()
    left = mock.Mock()
    left.WhichOneof.return_value = "imaginary-type"
    right = mock.Mock()
    # Patch from value to get to the deep compare. Since left is a bad type
    # expect this to fail with value error.
    with mock.patch.object(TypeOrder, "from_value") as to:
        to.value = None
        with pytest.raises(ValueError) as exc_info:
            target.compare(left, right)

    (message,) = exc_info.value.args
    assert message.startswith("Unknown TypeOrder")


@pytest.mark.parametrize("invalid_point_is_left", [True, False])
def test_order_compare_invalid_geo_points(invalid_point_is_left):
    """
    comparing invalid geopoints should raise exception
    """
    target = _make_order()
    points = [_array_value(), _geoPoint_value(10, 10)]
    if not invalid_point_is_left:
        # reverse points
        points = points[::-1]
    with pytest.raises(AttributeError):
        target.compare_geo_points(*points)


def test_order_all_value_present():
    from google.cloud.firestore_v1.order import _TYPE_ORDER_MAP, TypeOrder

    for type_order in TypeOrder:
        assert type_order in _TYPE_ORDER_MAP


def test_order_bson_type_ordering():
    from google.cloud.firestore_v1._helpers import encode_value
    from google.cloud.firestore_v1.bson import (
        BSONBinary,
        BSONDecimal128,
        BSONInt32,
        BSONMaxKey,
        BSONMinKey,
        BSONObjectId,
        BSONRegex,
        BSONTimestamp,
    )
    from google.cloud.firestore_v1.order import Order

    min_k = encode_value(BSONMinKey())
    max_k = encode_value(BSONMaxKey())
    null_v = nullValue()
    int32_v = encode_value(BSONInt32(10))
    int64_v = _int_value(10)
    dec_v = encode_value(BSONDecimal128("10.0"))
    ts_bson = encode_value(BSONTimestamp(100, 1))
    ts_native = _timestamp_value(100, 0)
    bin_b = encode_value(BSONBinary(b"xyz", subtype=1))
    bytes_native = _blob_value(b"xyz")
    ref_v = _reference_value("projects/p1/databases/d1/documents/c1/doc1")
    oid_v = encode_value(BSONObjectId("507f191e810c19729de860ea"))
    geo_v = _geoPoint_value(0, 0)
    regex_v = encode_value(BSONRegex("abc"))
    arr_v = _array_value()
    map_v = _object_value({"a": 1})

    # Test 16-rank ordering bounds
    target = Order()
    assert target.compare(null_v, min_k) == -1
    assert target.compare(min_k, null_v) == 1

    assert target.compare(max_k, map_v) == 1
    assert target.compare(map_v, max_k) == -1

    # Test numbers comparison equality across int32, int64, decimal128
    assert target.compare(int32_v, int64_v) == 0
    assert target.compare(int32_v, dec_v) == 0

    # Test large decimal comparison exceeding float limit
    large_dec = encode_value(BSONDecimal128("1e1000"))
    assert target.compare(large_dec, _double_value(1e300)) == 1
    assert target.compare(_double_value(1e300), large_dec) == -1

    # Test decimal NaN comparison
    nan_dec = encode_value(BSONDecimal128("NaN"))
    assert target.compare(nan_dec, int32_v) == -1
    assert target.compare(int32_v, nan_dec) == 1

    # Test timestamp comparison (native timestamp < BSON timestamp with increment)
    assert target.compare(ts_native, ts_bson) == -1
    assert target.compare(ts_bson, ts_native) == 1

    # Test BSON timestamp comparison
    ts_bson2 = encode_value(BSONTimestamp(100, 2))
    ts_bson_later = encode_value(BSONTimestamp(101, 0))
    assert target.compare(ts_bson, ts_bson2) == -1
    assert target.compare(ts_bson2, ts_bson) == 1
    assert target.compare(ts_bson, ts_bson_later) == -1
    assert target.compare(ts_bson_later, ts_bson) == 1
    assert target.compare(ts_bson, ts_bson) == 0

    # Test BSON binary > bytes
    assert target.compare(bytes_native, bin_b) == -1

    # Test ObjectId rank (REF < OID < GEO_POINT)
    assert target.compare(ref_v, oid_v) == -1
    assert target.compare(oid_v, geo_v) == -1

    # Test Regex rank (GEO_POINT < REGEX < ARRAY)
    assert target.compare(geo_v, regex_v) == -1
    assert target.compare(regex_v, arr_v) == -1

    # Verify _BSON_KEY_TO_TYPE_ORDER mapping directly
    from google.cloud.firestore_v1.order import _BSON_KEY_TO_TYPE_ORDER, TypeOrder

    expected_orders = {
        "__min__": TypeOrder.BSON_MIN_KEY,
        "__max__": TypeOrder.BSON_MAX_KEY,
        "__oid__": TypeOrder.BSON_OBJECT_ID,
        "__int__": TypeOrder.NUMBER,
        "__decimal128__": TypeOrder.NUMBER,
        "__binary__": TypeOrder.BSON_BINARY,
        "__regex__": TypeOrder.BSON_REGEX,
        "__request_timestamp__": TypeOrder.BSON_TIMESTAMP,
    }
    for key, expected_order in expected_orders.items():
        assert _BSON_KEY_TO_TYPE_ORDER.get(key) == expected_order


def test_order_compare_w_objects_different_keys():
    left = _object_value({"foo": 0})
    right = _object_value({"bar": 0})

    target = _make_order()
    target.compare(left, right)


def _boolean_value(b):
    from google.cloud.firestore_v1._helpers import encode_value

    return encode_value(b)


def _double_value(d):
    from google.cloud.firestore_v1._helpers import encode_value

    return encode_value(d)


def _int_value(value):
    from google.cloud.firestore_v1._helpers import encode_value

    return encode_value(value)


def _string_value(s):
    from google.cloud.firestore_v1._helpers import encode_value

    return encode_value(s)


def _reference_value(r):
    from google.cloud.firestore_v1.types import document

    return document.Value(reference_value=r)


def _blob_value(b):
    from google.cloud.firestore_v1._helpers import encode_value

    return encode_value(b)


def nullValue():
    from google.cloud.firestore_v1._helpers import encode_value

    return encode_value(None)


def _timestamp_value(seconds, nanos):
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1.types import document

    return document.Value(
        timestamp_value=timestamp_pb2.Timestamp(seconds=seconds, nanos=nanos)
    )


def _geoPoint_value(latitude, longitude):
    from google.cloud.firestore_v1._helpers import GeoPoint, encode_value

    return encode_value(GeoPoint(latitude, longitude))


def _array_value(values=[]):
    from google.cloud.firestore_v1._helpers import encode_value

    return encode_value(values)


def _object_value(keysAndValues):
    from google.cloud.firestore_v1._helpers import encode_value

    return encode_value(keysAndValues)
