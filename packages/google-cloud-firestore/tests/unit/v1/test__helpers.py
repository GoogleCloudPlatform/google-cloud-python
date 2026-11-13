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

import datetime

import mock
import pytest

from tests.unit.v1._test_helpers import make_test_credentials


def _make_geo_point(lat, lng):
    from google.cloud.firestore_v1._helpers import GeoPoint

    return GeoPoint(lat, lng)


def test_geopoint_constructor():
    lat = 81.25
    lng = 359.984375
    geo_pt = _make_geo_point(lat, lng)
    assert geo_pt.latitude == lat
    assert geo_pt.longitude == lng


def test_geopoint_to_protobuf():
    from google.type import latlng_pb2

    lat = 0.015625
    lng = 20.03125
    geo_pt = _make_geo_point(lat, lng)
    result = geo_pt.to_protobuf()
    geo_pt_pb = latlng_pb2.LatLng(latitude=lat, longitude=lng)
    assert result == geo_pt_pb


def test_encode_value_pymongo_duck_typing():
    from google.cloud.firestore_v1._helpers import encode_value

    class ObjectId:
        def __init__(self, val):
            self.val = val
            self.binary = b"12bytes_raw_"

        def __str__(self):
            return self.val

    class Decimal128:
        def __init__(self, val):
            self.val = val

        def to_decimal(self):
            return self.val

        def __str__(self):
            return self.val

    class Regex:
        def __init__(self, pattern, flags="i"):
            self.pattern = pattern
            self.flags = flags

    class Timestamp:
        def __init__(self, time, inc):
            self.time = time
            self.inc = inc

    class MinKey:
        pass

    class MaxKey:
        pass

    class Binary(bytes):
        def __new__(cls, data, subtype=0):
            obj = super().__new__(cls, data)
            obj.subtype = subtype
            return obj

    oid_obj = ObjectId("507f191e810c19729de860ea")
    oid_pb = encode_value(oid_obj)
    assert oid_pb.map_value.fields["__oid__"].string_value == "507f191e810c19729de860ea"

    dec_obj = Decimal128("123.45")
    dec_pb = encode_value(dec_obj)
    assert dec_pb.map_value.fields["__decimal128__"].string_value == "123.45"

    regex_obj = Regex("^[a-z]+$", "i")
    regex_pb = encode_value(regex_obj)
    assert (
        regex_pb.map_value.fields["__regex__"].map_value.fields["pattern"].string_value
        == "^[a-z]+$"
    )
    assert (
        regex_pb.map_value.fields["__regex__"].map_value.fields["options"].string_value
        == "i"
    )

    import re

    regex_int_flags = Regex("^[a-z]+$", re.IGNORECASE | re.MULTILINE)
    regex_int_pb = encode_value(regex_int_flags)
    assert (
        regex_int_pb.map_value.fields["__regex__"]
        .map_value.fields["options"]
        .string_value
        == "im"
    )

    bin_obj = Binary(b"\x01\x02\x03", subtype=128)
    bin_pb = encode_value(bin_obj)
    assert bin_pb.map_value.fields["__binary__"].bytes_value == b"\x80\x01\x02\x03"

    ts_obj = Timestamp(1700000000, 42)
    ts_pb = encode_value(ts_obj)
    assert (
        ts_pb.map_value.fields["__request_timestamp__"]
        .map_value.fields["seconds"]
        .integer_value
        == 1700000000
    )
    assert (
        ts_pb.map_value.fields["__request_timestamp__"]
        .map_value.fields["increment"]
        .integer_value
        == 42
    )

    min_obj = MinKey()
    min_pb = encode_value(min_obj)
    assert "__min__" in min_pb.map_value.fields

    max_obj = MaxKey()
    max_pb = encode_value(max_obj)
    assert "__max__" in max_pb.map_value.fields

    import pytest

    with pytest.raises(ValueError):
        encode_value(ObjectId("invalid_hex"))


def test_geopoint___eq__w_same_value():
    lat = 0.015625
    lng = 20.03125
    geo_pt1 = _make_geo_point(lat, lng)
    geo_pt2 = _make_geo_point(lat, lng)
    assert geo_pt1 == geo_pt2


def test_geopoint___eq__w_type_differ():
    lat = 0.015625
    lng = 20.03125
    geo_pt1 = _make_geo_point(lat, lng)
    geo_pt2 = object()
    assert geo_pt1 != geo_pt2
    assert geo_pt1.__eq__(geo_pt2) is NotImplemented


def test_geopoint___ne__w_same_value():
    lat = 0.015625
    lng = 20.03125
    geo_pt1 = _make_geo_point(lat, lng)
    geo_pt2 = _make_geo_point(lat, lng)
    assert not geo_pt1 != geo_pt2


def test_geopoint___ne__w_other_value():
    geo_pt1 = _make_geo_point(0.0, 1.0)
    geo_pt2 = _make_geo_point(2.0, 3.0)
    assert geo_pt1 != geo_pt2


def test_geopoint___ne__w_type_differ():
    lat = 0.015625
    lng = 20.03125
    geo_pt1 = _make_geo_point(lat, lng)
    geo_pt2 = object()
    assert geo_pt1 != geo_pt2
    assert geo_pt1.__ne__(geo_pt2) is NotImplemented


def test_verify_path_w_empty():
    from google.cloud.firestore_v1._helpers import verify_path

    path = ()
    with pytest.raises(ValueError):
        verify_path(path, True)
    with pytest.raises(ValueError):
        verify_path(path, False)


def test_verify_path_w_wrong_length_collection():
    from google.cloud.firestore_v1._helpers import verify_path

    path = ("foo", "bar")
    with pytest.raises(ValueError):
        verify_path(path, True)


def test_verify_path_w_wrong_length_document():
    from google.cloud.firestore_v1._helpers import verify_path

    path = ("Kind",)
    with pytest.raises(ValueError):
        verify_path(path, False)


def test_verify_path_w_wrong_type_collection():
    from google.cloud.firestore_v1._helpers import verify_path

    path = (99, "ninety-nine", "zap")
    with pytest.raises(ValueError):
        verify_path(path, True)


def test_verify_path_w_wrong_type_document():
    from google.cloud.firestore_v1._helpers import verify_path

    path = ("Users", "Ada", "Candy", {})
    with pytest.raises(ValueError):
        verify_path(path, False)


def test_verify_path_w_success_collection():
    from google.cloud.firestore_v1._helpers import verify_path

    path = ("Computer", "Magic", "Win")
    ret_val = verify_path(path, True)
    # NOTE: We are just checking that it didn't fail.
    assert ret_val is None


def test_verify_path_w_success_document():
    from google.cloud.firestore_v1._helpers import verify_path

    path = ("Tokenizer", "Seventeen", "Cheese", "Burger")
    ret_val = verify_path(path, False)
    # NOTE: We are just checking that it didn't fail.
    assert ret_val is None


def test_encode_value_w_none():
    from google.protobuf import struct_pb2

    from google.cloud.firestore_v1._helpers import encode_value

    result = encode_value(None)
    expected = _value_pb(null_value=struct_pb2.NULL_VALUE)
    assert result == expected


def test_encode_value_w_boolean():
    from google.cloud.firestore_v1._helpers import encode_value

    result = encode_value(True)
    expected = _value_pb(boolean_value=True)
    assert result == expected


def test_encode_value_w_integer():
    from google.cloud.firestore_v1._helpers import encode_value

    value = 425178
    result = encode_value(value)
    expected = _value_pb(integer_value=value)
    assert result == expected


def test_encode_value_w_float():
    from google.cloud.firestore_v1._helpers import encode_value

    value = 123.4453125
    result = encode_value(value)
    expected = _value_pb(double_value=value)
    assert result == expected


def test_encode_value_w_datetime_with_nanos():
    from google.api_core.datetime_helpers import DatetimeWithNanoseconds
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1._helpers import encode_value

    dt_seconds = 1488768504
    dt_nanos = 458816991
    timestamp_pb = timestamp_pb2.Timestamp(seconds=dt_seconds, nanos=dt_nanos)
    dt_val = DatetimeWithNanoseconds.from_timestamp_pb(timestamp_pb)

    result = encode_value(dt_val)
    expected = _value_pb(timestamp_value=timestamp_pb)
    assert result == expected


def test_encode_value_w_datetime_wo_nanos():
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1._helpers import encode_value

    dt_seconds = 1488768504
    dt_nanos = 458816000
    # Make sure precision is valid in microseconds too.
    assert dt_nanos % 1000 == 0
    dt_val = datetime.datetime.fromtimestamp(
        dt_seconds + 1e-9 * dt_nanos, tz=datetime.timezone.utc
    )

    result = encode_value(dt_val)
    timestamp_pb = timestamp_pb2.Timestamp(seconds=dt_seconds, nanos=dt_nanos)
    expected = _value_pb(timestamp_value=timestamp_pb)
    assert result == expected


def test_encode_value_w_string():
    from google.cloud.firestore_v1._helpers import encode_value

    value = "\u2018left quote, right quote\u2019"
    result = encode_value(value)
    expected = _value_pb(string_value=value)
    assert result == expected


def test_encode_value_w_bytes():
    from google.cloud.firestore_v1._helpers import encode_value

    value = b"\xe3\xf2\xff\x00"
    result = encode_value(value)
    expected = _value_pb(bytes_value=value)
    assert result == expected


def test_encode_value_w_reference_value():
    from google.cloud.firestore_v1._helpers import encode_value

    client = _make_client()

    value = client.document("my", "friend")
    result = encode_value(value)
    expected = _value_pb(reference_value=value._document_path)
    assert result == expected


def test_encode_value_w_geo_point():
    from google.cloud.firestore_v1._helpers import GeoPoint, encode_value

    value = GeoPoint(50.5, 88.75)
    result = encode_value(value)
    expected = _value_pb(geo_point_value=value.to_protobuf())
    assert result == expected


def test_encode_value_w_array():
    from google.cloud.firestore_v1._helpers import encode_value
    from google.cloud.firestore_v1.types.document import ArrayValue

    result = encode_value([99, True, 118.5])

    array_pb = ArrayValue(
        values=[
            _value_pb(integer_value=99),
            _value_pb(boolean_value=True),
            _value_pb(double_value=118.5),
        ]
    )
    expected = _value_pb(array_value=array_pb)
    assert result == expected


def test_encode_value_w_map():
    from google.cloud.firestore_v1._helpers import encode_value
    from google.cloud.firestore_v1.types.document import MapValue

    result = encode_value({"abc": 285, "def": b"piglatin"})

    map_pb = MapValue(
        fields={
            "abc": _value_pb(integer_value=285),
            "def": _value_pb(bytes_value=b"piglatin"),
        }
    )
    expected = _value_pb(map_value=map_pb)
    assert result == expected


def test_encode_value_w_bad_type():
    from google.cloud.firestore_v1._helpers import encode_value

    value = object()
    with pytest.raises(TypeError):
        encode_value(value)


def test_encode_dict_w_many_types():
    from google.protobuf import struct_pb2, timestamp_pb2

    from google.cloud.firestore_v1._helpers import encode_dict
    from google.cloud.firestore_v1.types.document import ArrayValue, MapValue

    dt_seconds = 1497397225
    dt_nanos = 465964000
    # Make sure precision is valid in microseconds too.
    assert dt_nanos % 1000 == 0
    dt_val = datetime.datetime.fromtimestamp(
        dt_seconds + 1e-9 * dt_nanos, tz=datetime.timezone.utc
    )

    client = _make_client()
    document = client.document("most", "adjective", "thing", "here")

    values_dict = {
        "foo": None,
        "bar": True,
        "baz": 981,
        "quux": 2.875,
        "quuz": dt_val,
        "corge": "\N{SNOWMAN}",
        "grault": b"\xe2\x98\x83",
        "wibble": document,
        "garply": ["fork", 4.0],
        "waldo": {"fred": "zap", "thud": False},
    }
    encoded_dict = encode_dict(values_dict)
    expected_dict = {
        "foo": _value_pb(null_value=struct_pb2.NULL_VALUE),
        "bar": _value_pb(boolean_value=True),
        "baz": _value_pb(integer_value=981),
        "quux": _value_pb(double_value=2.875),
        "quuz": _value_pb(
            timestamp_value=timestamp_pb2.Timestamp(seconds=dt_seconds, nanos=dt_nanos)
        ),
        "corge": _value_pb(string_value="\N{SNOWMAN}"),
        "grault": _value_pb(bytes_value=b"\xe2\x98\x83"),
        "wibble": _value_pb(reference_value=document._document_path),
        "garply": _value_pb(
            array_value=ArrayValue(
                values=[_value_pb(string_value="fork"), _value_pb(double_value=4.0)]
            )
        ),
        "waldo": _value_pb(
            map_value=MapValue(
                fields={
                    "fred": _value_pb(string_value="zap"),
                    "thud": _value_pb(boolean_value=False),
                }
            )
        ),
    }
    assert encoded_dict == expected_dict


def test_reference_value_to_document_w_bad_format():
    from google.cloud.firestore_v1._helpers import (
        BAD_REFERENCE_ERROR,
        reference_value_to_document,
    )

    reference_value = "not/the/right/format"
    with pytest.raises(ValueError) as exc_info:
        reference_value_to_document(reference_value, None)

    err_msg = BAD_REFERENCE_ERROR.format(reference_value)
    assert exc_info.value.args == (err_msg,)


def test_reference_value_to_document_w_same_client():
    from google.cloud.firestore_v1._helpers import reference_value_to_document
    from google.cloud.firestore_v1.document import DocumentReference

    client = _make_client()
    document = client.document("that", "this")
    reference_value = document._document_path

    new_document = reference_value_to_document(reference_value, client)

    assert new_document is not document
    assert isinstance(new_document, DocumentReference)
    assert new_document._client is client
    assert new_document._path == document._path


def test_reference_value_to_document_w_different_client():
    from google.cloud.firestore_v1._helpers import (
        WRONG_APP_REFERENCE,
        reference_value_to_document,
    )

    client1 = _make_client(project="kirk")
    document = client1.document("tin", "foil")
    reference_value = document._document_path
    client2 = _make_client(project="spock")

    with pytest.raises(ValueError) as exc_info:
        reference_value_to_document(reference_value, client2)

    err_msg = WRONG_APP_REFERENCE.format(reference_value, client2._database_string)
    assert exc_info.value.args == (err_msg,)


def test_documentreferencevalue_w_normal():
    from google.cloud.firestore_v1._helpers import DocumentReferenceValue

    orig = "projects/name/databases/(default)/documents/col/doc"
    parsed = DocumentReferenceValue(orig)
    assert parsed.collection_name == "col"
    assert parsed.database_name == "(default)"
    assert parsed.document_id == "doc"

    assert parsed.full_path == orig
    parsed._reference_value = None  # type: ignore
    assert parsed.full_path == orig


def test_documentreferencevalue_w_nested():
    from google.cloud.firestore_v1._helpers import DocumentReferenceValue

    parsed = DocumentReferenceValue(
        "projects/name/databases/(default)/documents/col/doc/nested"
    )
    assert parsed.collection_name == "col"
    assert parsed.database_name == "(default)"
    assert parsed.document_id == "doc/nested"


def test_documentreferencevalue_w_broken():
    from google.cloud.firestore_v1._helpers import DocumentReferenceValue

    with pytest.raises(ValueError):
        DocumentReferenceValue("projects/name/databases/(default)/documents/col")


def test_document_snapshot_to_protobuf_w_real_snapshot():
    from google.protobuf import timestamp_pb2  # type: ignore

    from google.cloud.firestore_v1._helpers import document_snapshot_to_protobuf
    from google.cloud.firestore_v1.base_document import DocumentSnapshot
    from google.cloud.firestore_v1.document import DocumentReference
    from google.cloud.firestore_v1.types import Document

    client = _make_client()
    snapshot = DocumentSnapshot(
        data={"hello": "world"},
        reference=DocumentReference("col", "doc", client=client),
        exists=True,
        read_time=timestamp_pb2.Timestamp(seconds=0, nanos=1),
        update_time=timestamp_pb2.Timestamp(seconds=0, nanos=1),
        create_time=timestamp_pb2.Timestamp(seconds=0, nanos=1),
    )
    assert isinstance(document_snapshot_to_protobuf(snapshot), Document)


def test_document_snapshot_to_protobuf_w_non_existant_snapshot():
    from google.cloud.firestore_v1._helpers import document_snapshot_to_protobuf
    from google.cloud.firestore_v1.base_document import DocumentSnapshot
    from google.cloud.firestore_v1.document import DocumentReference

    client = _make_client()
    snapshot = DocumentSnapshot(
        data=None,
        reference=DocumentReference("col", "doc", client=client),
        exists=False,
        read_time=None,
        update_time=None,
        create_time=None,
    )
    assert document_snapshot_to_protobuf(snapshot) is None


def test_decode_value_w_none():
    from google.protobuf import struct_pb2

    from google.cloud.firestore_v1._helpers import decode_value

    value = _value_pb(null_value=struct_pb2.NULL_VALUE)
    assert decode_value(value, mock.sentinel.client) is None


def test_decode_value_w_bool():
    from google.cloud.firestore_v1._helpers import decode_value

    value1 = _value_pb(boolean_value=True)
    assert decode_value(value1, mock.sentinel.client)
    value2 = _value_pb(boolean_value=False)
    assert not decode_value(value2, mock.sentinel.client)


def test_decode_value_w_int():
    from google.cloud.firestore_v1._helpers import decode_value

    int_val = 29871
    value = _value_pb(integer_value=int_val)
    assert decode_value(value, mock.sentinel.client) == int_val


def test_decode_value_w_float():
    from google.cloud.firestore_v1._helpers import decode_value

    float_val = 85.9296875
    value = _value_pb(double_value=float_val)
    assert decode_value(value, mock.sentinel.client) == float_val


def test_decode_value_w_datetime():
    from google.api_core.datetime_helpers import DatetimeWithNanoseconds
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1._helpers import decode_value

    dt_seconds = 552855006
    dt_nanos = 766961828

    timestamp_pb = timestamp_pb2.Timestamp(seconds=dt_seconds, nanos=dt_nanos)
    value = _value_pb(timestamp_value=timestamp_pb)

    expected_dt_val = DatetimeWithNanoseconds.from_timestamp_pb(timestamp_pb)
    assert decode_value(value, mock.sentinel.client) == expected_dt_val


def test_decode_value_w_unicode():
    from google.cloud.firestore_v1._helpers import decode_value

    unicode_val = "zorgon"
    value = _value_pb(string_value=unicode_val)
    assert decode_value(value, mock.sentinel.client) == unicode_val


def test_decode_value_w_bytes():
    from google.cloud.firestore_v1._helpers import decode_value

    bytes_val = b"abc\x80"
    value = _value_pb(bytes_value=bytes_val)
    assert decode_value(value, mock.sentinel.client) == bytes_val


def test_decode_value_w_reference():
    from google.cloud.firestore_v1._helpers import decode_value
    from google.cloud.firestore_v1.document import DocumentReference

    client = _make_client()
    path = ("then", "there-was-one")
    document = client.document(*path)
    ref_string = document._document_path
    value = _value_pb(reference_value=ref_string)

    result = decode_value(value, client)
    assert isinstance(result, DocumentReference)
    assert result._client is client
    assert result._path == path


def test_decode_value_w_geo_point():
    from google.cloud.firestore_v1._helpers import GeoPoint, decode_value

    geo_pt = GeoPoint(latitude=42.5, longitude=99.0625)
    value = _value_pb(geo_point_value=geo_pt.to_protobuf())
    assert decode_value(value, mock.sentinel.client) == geo_pt


def test_decode_value_w_array():
    from google.cloud.firestore_v1._helpers import decode_value
    from google.cloud.firestore_v1.types import document

    sub_value1 = _value_pb(boolean_value=True)
    sub_value2 = _value_pb(double_value=14.1396484375)
    sub_value3 = _value_pb(bytes_value=b"\xde\xad\xbe\xef")
    array_pb = document.ArrayValue(values=[sub_value1, sub_value2, sub_value3])
    value = _value_pb(array_value=array_pb)

    expected = [
        sub_value1.boolean_value,
        sub_value2.double_value,
        sub_value3.bytes_value,
    ]
    assert decode_value(value, mock.sentinel.client) == expected


def test_decode_value_w_map():
    from google.cloud.firestore_v1._helpers import decode_value
    from google.cloud.firestore_v1.types import document

    sub_value1 = _value_pb(integer_value=187680)
    sub_value2 = _value_pb(string_value="how low can you go?")
    map_pb = document.MapValue(fields={"first": sub_value1, "second": sub_value2})
    value = _value_pb(map_value=map_pb)

    expected = {
        "first": sub_value1.integer_value,
        "second": sub_value2.string_value,
    }
    assert decode_value(value, mock.sentinel.client) == expected


def test_decode_value_w_nested_map():
    from google.cloud.firestore_v1._helpers import decode_value
    from google.cloud.firestore_v1.types import document

    actual_value1 = 1009876
    actual_value2 = "hey you guys"
    actual_value3 = 90.875
    map_pb1 = document.MapValue(
        fields={
            "lowest": _value_pb(integer_value=actual_value1),
            "aside": _value_pb(string_value=actual_value2),
        }
    )
    map_pb2 = document.MapValue(
        fields={
            "middle": _value_pb(map_value=map_pb1),
            "aside": _value_pb(boolean_value=True),
        }
    )
    map_pb3 = document.MapValue(
        fields={
            "highest": _value_pb(map_value=map_pb2),
            "aside": _value_pb(double_value=actual_value3),
        }
    )
    value = _value_pb(map_value=map_pb3)

    expected = {
        "highest": {
            "middle": {"lowest": actual_value1, "aside": actual_value2},
            "aside": True,
        },
        "aside": actual_value3,
    }
    assert decode_value(value, mock.sentinel.client) == expected


def test_decode_value_w_unset_value_type():
    from google.cloud.firestore_v1._helpers import decode_value

    with pytest.raises(ValueError):
        decode_value(_value_pb(), mock.sentinel.client)


def test_decode_value_w_unknown_value_type():
    from google.cloud.firestore_v1._helpers import decode_value

    value_pb = mock.Mock()
    value_pb._pb.WhichOneof.return_value = "zoob_value"

    with pytest.raises(ValueError):
        decode_value(value_pb, mock.sentinel.client)

    value_pb._pb.WhichOneof.assert_called_once_with("value_type")


def test_decode_dict_w_many_types():
    from google.protobuf import struct_pb2, timestamp_pb2

    from google.cloud.firestore_v1._helpers import decode_dict
    from google.cloud.firestore_v1.field_path import FieldPath
    from google.cloud.firestore_v1.types.document import ArrayValue, MapValue

    dt_seconds = 1394037350
    dt_nanos = 667285000
    # Make sure precision is valid in microseconds too.
    assert dt_nanos % 1000 == 0
    dt_val = datetime.datetime.fromtimestamp(
        dt_seconds + 1e-9 * dt_nanos, tz=datetime.timezone.utc
    )

    value_fields = {
        "foo": _value_pb(null_value=struct_pb2.NULL_VALUE),
        "bar": _value_pb(boolean_value=True),
        "baz": _value_pb(integer_value=981),
        "quux": _value_pb(double_value=2.875),
        "quuz": _value_pb(
            timestamp_value=timestamp_pb2.Timestamp(seconds=dt_seconds, nanos=dt_nanos)
        ),
        "corge": _value_pb(string_value="\N{SNOWMAN}"),
        "grault": _value_pb(bytes_value=b"\xe2\x98\x83"),
        "garply": _value_pb(
            array_value=ArrayValue(
                values=[_value_pb(string_value="fork"), _value_pb(double_value=4.0)]
            )
        ),
        "waldo": _value_pb(
            map_value=MapValue(
                fields={
                    "fred": _value_pb(string_value="zap"),
                    "thud": _value_pb(boolean_value=False),
                }
            )
        ),
        FieldPath("a", "b", "c").to_api_repr(): _value_pb(boolean_value=False),
    }
    expected = {
        "foo": None,
        "bar": True,
        "baz": 981,
        "quux": 2.875,
        "quuz": dt_val,
        "corge": "\N{SNOWMAN}",
        "grault": b"\xe2\x98\x83",
        "garply": ["fork", 4.0],
        "waldo": {"fred": "zap", "thud": False},
        "a.b.c": False,
    }
    assert decode_dict(value_fields, mock.sentinel.client) == expected


def test_decode_dict_w_bson_types():
    from google.cloud.firestore_v1._helpers import decode_dict, encode_dict
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

    original_dict = {
        "oid": BSONObjectId("507f191e810c19729de860ea"),
        "min_k": BSONMinKey(),
        "max_k": BSONMaxKey(),
        "int32_v": BSONInt32(42),
        "bin_sub0": b"hello",
        "bin_sub0_empty": b"",
        "bin_sub128": BSONBinary(b"world", subtype=128),
        "ts_v": BSONTimestamp(1700000000, 1),
        "regex_v": BSONRegex("^hello.*$", options="i"),
        "dec_v": BSONDecimal128("123.45"),
    }

    pb_fields = encode_dict(original_dict)
    decoded = decode_dict(pb_fields, mock.sentinel.client)
    assert decoded == original_dict


def _dummy_ref_string(collection_id):
    from google.cloud.firestore_v1.base_client import DEFAULT_DATABASE

    project = "bazzzz"
    return "projects/{}/databases/{}/documents/{}".format(
        project, DEFAULT_DATABASE, collection_id
    )


def test_get_doc_id_w_success():
    from google.cloud.firestore_v1._helpers import get_doc_id
    from google.cloud.firestore_v1.types import document

    prefix = _dummy_ref_string("sub-collection")
    actual_id = "this-is-the-one"
    name = "{}/{}".format(prefix, actual_id)

    document_pb = document.Document(name=name)
    document_id = get_doc_id(document_pb, prefix)
    assert document_id == actual_id


def test_get_doc_id_w_failure():
    from google.cloud.firestore_v1._helpers import get_doc_id
    from google.cloud.firestore_v1.types import document

    actual_prefix = _dummy_ref_string("the-right-one")
    wrong_prefix = _dummy_ref_string("the-wrong-one")
    name = "{}/{}".format(actual_prefix, "sorry-wont-works")

    document_pb = document.Document(name=name)
    with pytest.raises(ValueError) as exc_info:
        get_doc_id(document_pb, wrong_prefix)

    exc_args = exc_info.value.args
    assert len(exc_args) == 4
    assert exc_args[1] == name
    assert exc_args[3] == wrong_prefix


def test_extract_fields_w_empty_document():
    from google.cloud.firestore_v1._helpers import _EmptyDict, extract_fields

    document_data = {}
    prefix_path = _make_field_path()
    expected = [(_make_field_path(), _EmptyDict)]

    iterator = extract_fields(document_data, prefix_path)
    assert list(iterator) == expected


def test_extract_fields_w_invalid_key_and_expand_dots():
    from google.cloud.firestore_v1._helpers import extract_fields

    document_data = {"b": 1, "a~d": 2, "c": 3}
    prefix_path = _make_field_path()

    with pytest.raises(ValueError):
        list(extract_fields(document_data, prefix_path, expand_dots=True))


def test_extract_fields_w_shallow_keys():
    from google.cloud.firestore_v1._helpers import extract_fields

    document_data = {"b": 1, "a": 2, "c": 3}
    prefix_path = _make_field_path()
    expected = [
        (_make_field_path("a"), 2),
        (_make_field_path("b"), 1),
        (_make_field_path("c"), 3),
    ]

    iterator = extract_fields(document_data, prefix_path)
    assert list(iterator) == expected


def test_extract_fields_w_nested():
    from google.cloud.firestore_v1._helpers import _EmptyDict, extract_fields

    document_data = {"b": {"a": {"d": 4, "c": 3, "g": {}}, "e": 7}, "f": 5}
    prefix_path = _make_field_path()
    expected = [
        (_make_field_path("b", "a", "c"), 3),
        (_make_field_path("b", "a", "d"), 4),
        (_make_field_path("b", "a", "g"), _EmptyDict),
        (_make_field_path("b", "e"), 7),
        (_make_field_path("f"), 5),
    ]

    iterator = extract_fields(document_data, prefix_path)
    assert list(iterator) == expected


def test_extract_fields_w_expand_dotted():
    from google.cloud.firestore_v1._helpers import _EmptyDict, extract_fields

    document_data = {
        "b": {"a": {"d": 4, "c": 3, "g": {}, "k.l.m": 17}, "e": 7},
        "f": 5,
        "h.i.j": 9,
    }
    prefix_path = _make_field_path()
    expected = [
        (_make_field_path("b", "a", "c"), 3),
        (_make_field_path("b", "a", "d"), 4),
        (_make_field_path("b", "a", "g"), _EmptyDict),
        (_make_field_path("b", "a", "k.l.m"), 17),
        (_make_field_path("b", "e"), 7),
        (_make_field_path("f"), 5),
        (_make_field_path("h", "i", "j"), 9),
    ]

    iterator = extract_fields(document_data, prefix_path, expand_dots=True)
    assert list(iterator) == expected


def test_set_field_value_normal_value_w_shallow():
    from google.cloud.firestore_v1._helpers import set_field_value

    document = {}
    field_path = _make_field_path("a")
    value = 3

    set_field_value(document, field_path, value)

    assert document == {"a": 3}


def test_set_field_value_normal_value_w_nested():
    from google.cloud.firestore_v1._helpers import set_field_value

    document = {}
    field_path = _make_field_path("a", "b", "c")
    value = 3

    set_field_value(document, field_path, value)

    assert document == {"a": {"b": {"c": 3}}}


def test_set_field_value_empty_dict_w_shallow():
    from google.cloud.firestore_v1._helpers import _EmptyDict, set_field_value

    document = {}
    field_path = _make_field_path("a")
    value = _EmptyDict

    set_field_value(document, field_path, value)

    assert document == {"a": {}}


def test_set_field_value_empty_dict_w_nested():
    from google.cloud.firestore_v1._helpers import _EmptyDict, set_field_value

    document = {}
    field_path = _make_field_path("a", "b", "c")
    value = _EmptyDict

    set_field_value(document, field_path, value)

    assert document == {"a": {"b": {"c": {}}}}


def test__get_field_value_w_empty_path():
    from google.cloud.firestore_v1._helpers import get_field_value

    document = {}

    with pytest.raises(ValueError):
        get_field_value(document, _make_field_path())


def test__get_field_value_miss_shallow():
    from google.cloud.firestore_v1._helpers import get_field_value

    document = {}

    with pytest.raises(KeyError):
        get_field_value(document, _make_field_path("nonesuch"))


def test__get_field_value_miss_nested():
    from google.cloud.firestore_v1._helpers import get_field_value

    document = {"a": {"b": {}}}

    with pytest.raises(KeyError):
        get_field_value(document, _make_field_path("a", "b", "c"))


def test__get_field_value_hit_shallow():
    from google.cloud.firestore_v1._helpers import get_field_value

    document = {"a": 1}

    assert get_field_value(document, _make_field_path("a")) == 1


def test__get_field_value_hit_nested():
    from google.cloud.firestore_v1._helpers import get_field_value

    document = {"a": {"b": {"c": 1}}}

    assert get_field_value(document, _make_field_path("a", "b", "c")) == 1


def _make_document_extractor(document_data):
    from google.cloud.firestore_v1._helpers import DocumentExtractor

    return DocumentExtractor(document_data)


def test_documentextractor_ctor_w_empty_document():
    document_data = {}

    inst = _make_document_extractor(document_data)

    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert inst.empty_document
    assert not inst.has_transforms
    assert inst.transform_paths == []


def test_documentextractor_ctor_w_delete_field_shallow():
    from google.cloud.firestore_v1.transforms import DELETE_FIELD

    document_data = {"a": DELETE_FIELD}

    inst = _make_document_extractor(document_data)

    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == [_make_field_path("a")]
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert not inst.has_transforms
    assert inst.transform_paths == []


def test_documentextractor_ctor_w_delete_field_nested():
    from google.cloud.firestore_v1.transforms import DELETE_FIELD

    document_data = {"a": {"b": {"c": DELETE_FIELD}}}

    inst = _make_document_extractor(document_data)

    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == [_make_field_path("a", "b", "c")]
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert not inst.has_transforms
    assert inst.transform_paths == []


def test_documentextractor_ctor_w_server_timestamp_shallow():
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_data = {"a": SERVER_TIMESTAMP}

    inst = _make_document_extractor(document_data)

    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == [_make_field_path("a")]
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a")]


def test_documentextractor_ctor_w_server_timestamp_nested():
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_data = {"a": {"b": {"c": SERVER_TIMESTAMP}}}

    inst = _make_document_extractor(document_data)

    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == [_make_field_path("a", "b", "c")]
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a", "b", "c")]


def test_documentextractor_ctor_w_array_remove_shallow():
    from google.cloud.firestore_v1.transforms import ArrayRemove

    values = [1, 3, 5]
    document_data = {"a": ArrayRemove(values)}

    inst = _make_document_extractor(document_data)

    expected_array_removes = {_make_field_path("a"): values}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == expected_array_removes
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a")]


def test_documentextractor_ctor_w_array_remove_nested():
    from google.cloud.firestore_v1.transforms import ArrayRemove

    values = [2, 4, 8]
    document_data = {"a": {"b": {"c": ArrayRemove(values)}}}

    inst = _make_document_extractor(document_data)

    expected_array_removes = {_make_field_path("a", "b", "c"): values}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == expected_array_removes
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a", "b", "c")]


def test_documentextractor_ctor_w_array_union_shallow():
    from google.cloud.firestore_v1.transforms import ArrayUnion

    values = [1, 3, 5]
    document_data = {"a": ArrayUnion(values)}

    inst = _make_document_extractor(document_data)

    expected_array_unions = {_make_field_path("a"): values}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == expected_array_unions
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a")]


def test_documentextractor__documentextractor_ctor_w_array_union_nested():
    from google.cloud.firestore_v1.transforms import ArrayUnion

    values = [2, 4, 8]
    document_data = {"a": {"b": {"c": ArrayUnion(values)}}}

    inst = _make_document_extractor(document_data)

    expected_array_unions = {_make_field_path("a", "b", "c"): values}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == expected_array_unions
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a", "b", "c")]


def test_documentextractor_ctor_w_increment_shallow():
    from google.cloud.firestore_v1.transforms import Increment

    value = 1
    document_data = {"a": Increment(value)}

    inst = _make_document_extractor(document_data)

    expected_increments = {_make_field_path("a"): value}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == expected_increments
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a")]


def test_documentextractor_ctor_w_increment_nested():
    from google.cloud.firestore_v1.transforms import Increment

    value = 2
    document_data = {"a": {"b": {"c": Increment(value)}}}

    inst = _make_document_extractor(document_data)

    expected_increments = {_make_field_path("a", "b", "c"): value}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == expected_increments
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a", "b", "c")]


def test_documentextractor_ctor_w_maximum_shallow():
    from google.cloud.firestore_v1.transforms import Maximum

    value = 1
    document_data = {"a": Maximum(value)}

    inst = _make_document_extractor(document_data)

    expected_maximums = {_make_field_path("a"): value}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == expected_maximums
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a")]


def test_documentextractor_ctor_w_maximum_nested():
    from google.cloud.firestore_v1.transforms import Maximum

    value = 2
    document_data = {"a": {"b": {"c": Maximum(value)}}}

    inst = _make_document_extractor(document_data)

    expected_maximums = {_make_field_path("a", "b", "c"): value}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == expected_maximums
    assert inst.minimums == {}
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a", "b", "c")]


def test_documentextractor_ctor_w_minimum_shallow():
    from google.cloud.firestore_v1.transforms import Minimum

    value = 1
    document_data = {"a": Minimum(value)}

    inst = _make_document_extractor(document_data)

    expected_minimums = {_make_field_path("a"): value}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == expected_minimums
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a")]


def test_documentextractor_ctor_w_minimum_nested():
    from google.cloud.firestore_v1.transforms import Minimum

    value = 2
    document_data = {"a": {"b": {"c": Minimum(value)}}}

    inst = _make_document_extractor(document_data)

    expected_minimums = {_make_field_path("a", "b", "c"): value}
    assert inst.document_data == document_data
    assert inst.field_paths == []
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == expected_minimums
    assert inst.set_fields == {}
    assert not inst.empty_document
    assert inst.has_transforms
    assert inst.transform_paths == [_make_field_path("a", "b", "c")]


def test_documentextractor_ctor_w_empty_dict_shallow():
    document_data = {"a": {}}

    inst = _make_document_extractor(document_data)

    expected_field_paths = [_make_field_path("a")]
    assert inst.document_data == document_data
    assert inst.field_paths == expected_field_paths
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == document_data
    assert not inst.empty_document
    assert not inst.has_transforms
    assert inst.transform_paths == []


def test_documentextractor_ctor_w_empty_dict_nested():
    document_data = {"a": {"b": {"c": {}}}}

    inst = _make_document_extractor(document_data)

    expected_field_paths = [_make_field_path("a", "b", "c")]
    assert inst.document_data == document_data
    assert inst.field_paths == expected_field_paths
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == document_data
    assert not inst.empty_document
    assert not inst.has_transforms
    assert inst.transform_paths == []


def test_documentextractor_ctor_w_normal_value_shallow():
    document_data = {"b": 1, "a": 2, "c": 3}

    inst = _make_document_extractor(document_data)

    expected_field_paths = [
        _make_field_path("a"),
        _make_field_path("b"),
        _make_field_path("c"),
    ]
    assert inst.document_data == document_data
    assert inst.field_paths == expected_field_paths
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.set_fields == document_data
    assert not inst.empty_document
    assert not inst.has_transforms


def test_documentextractor_ctor_w_normal_value_nested():
    document_data = {"b": {"a": {"d": 4, "c": 3}, "e": 7}, "f": 5}

    inst = _make_document_extractor(document_data)

    expected_field_paths = [
        _make_field_path("b", "a", "c"),
        _make_field_path("b", "a", "d"),
        _make_field_path("b", "e"),
        _make_field_path("f"),
    ]
    assert inst.document_data == document_data
    assert inst.field_paths == expected_field_paths
    assert inst.deleted_fields == []
    assert inst.server_timestamps == []
    assert inst.array_removes == {}
    assert inst.array_unions == {}
    assert inst.increments == {}
    assert inst.maximums == {}
    assert inst.minimums == {}
    assert inst.set_fields == document_data
    assert not inst.empty_document
    assert not inst.has_transforms


def test_documentextractor_get_update_pb_w_exists_precondition():
    from google.cloud.firestore_v1.types import write

    document_data = {}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    update_pb = inst.get_update_pb(document_path, exists=False)

    assert isinstance(update_pb, write.Write)
    assert update_pb.update.name == document_path
    assert update_pb.update.fields == document_data
    assert update_pb._pb.HasField("current_document")
    assert not update_pb.current_document.exists


def test_documentextractor_get_update_pb_wo_exists_precondition():
    from google.cloud.firestore_v1._helpers import encode_dict
    from google.cloud.firestore_v1.types import write

    document_data = {"a": 1}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    update_pb = inst.get_update_pb(document_path)

    assert isinstance(update_pb, write.Write)
    assert update_pb.update.name == document_path
    assert update_pb.update.fields == encode_dict(document_data)
    assert not update_pb._pb.HasField("current_document")


def test_documentextractor_get_field_transform_pbs_miss():
    document_data = {"a": 1}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    field_transform_pbs = inst.get_field_transform_pbs(document_path)

    assert field_transform_pbs == []


def test_documentextractor_get_field_transform_pbs_w_server_timestamp():
    from google.cloud.firestore_v1._helpers import REQUEST_TIME_ENUM
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP
    from google.cloud.firestore_v1.types import write

    document_data = {"a": SERVER_TIMESTAMP}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    field_transform_pbs = inst.get_field_transform_pbs(document_path)

    assert len(field_transform_pbs) == 1
    field_transform_pb = field_transform_pbs[0]
    assert isinstance(field_transform_pb, write.DocumentTransform.FieldTransform)
    assert field_transform_pb.field_path == "a"
    assert field_transform_pb.set_to_server_value == REQUEST_TIME_ENUM


def test_documentextractor_get_transform_pb_w_server_timestamp_w_exists_precondition():
    from google.cloud.firestore_v1._helpers import REQUEST_TIME_ENUM
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP
    from google.cloud.firestore_v1.types import write

    document_data = {"a": SERVER_TIMESTAMP}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path, exists=False)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a"
    assert transform.set_to_server_value == REQUEST_TIME_ENUM
    assert transform_pb._pb.HasField("current_document")
    assert not transform_pb.current_document.exists


def test_documentextractor_get_transform_pb_w_server_timestamp_wo_exists_precondition():
    from google.cloud.firestore_v1._helpers import REQUEST_TIME_ENUM
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP
    from google.cloud.firestore_v1.types import write

    document_data = {"a": {"b": {"c": SERVER_TIMESTAMP}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    assert transform.set_to_server_value == REQUEST_TIME_ENUM
    assert not transform_pb._pb.HasField("current_document")


def _array_value_to_list(array_value):
    from google.cloud.firestore_v1._helpers import decode_value

    return [decode_value(element, client=None) for element in array_value.values]


def test_documentextractor_get_transform_pb_w_array_remove():
    from google.cloud.firestore_v1.transforms import ArrayRemove
    from google.cloud.firestore_v1.types import write

    values = [2, 4, 8]
    document_data = {"a": {"b": {"c": ArrayRemove(values)}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    removed = _array_value_to_list(transform.remove_all_from_array)
    assert removed == values
    assert not transform_pb._pb.HasField("current_document")


def test_documentextractor_get_transform_pb_w_array_union():
    from google.cloud.firestore_v1.transforms import ArrayUnion
    from google.cloud.firestore_v1.types import write

    values = [1, 3, 5]
    document_data = {"a": {"b": {"c": ArrayUnion(values)}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    added = _array_value_to_list(transform.append_missing_elements)
    assert added == values
    assert not transform_pb._pb.HasField("current_document")


def test_documentextractor_get_transform_pb_w_increment_int():
    from google.cloud.firestore_v1.transforms import Increment
    from google.cloud.firestore_v1.types import write

    value = 1
    document_data = {"a": {"b": {"c": Increment(value)}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    added = transform.increment.integer_value
    assert added == value
    assert not transform_pb._pb.HasField("current_document")


def test_documentextractor_get_transform_pb_w_increment_float():
    from google.cloud.firestore_v1.transforms import Increment
    from google.cloud.firestore_v1.types import write

    value = 3.1415926
    document_data = {"a": {"b": {"c": Increment(value)}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    added = transform.increment.double_value
    assert added == value
    assert not transform_pb._pb.HasField("current_document")


def test_documentextractor_get_transform_pb_w_maximum_int():
    from google.cloud.firestore_v1.transforms import Maximum
    from google.cloud.firestore_v1.types import write

    value = 1
    document_data = {"a": {"b": {"c": Maximum(value)}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    added = transform.maximum.integer_value
    assert added == value
    assert not transform_pb._pb.HasField("current_document")


def test_documentextractor_get_transform_pb_w_maximum_float():
    from google.cloud.firestore_v1.transforms import Maximum
    from google.cloud.firestore_v1.types import write

    value = 3.1415926
    document_data = {"a": {"b": {"c": Maximum(value)}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    added = transform.maximum.double_value
    assert added == value
    assert not transform_pb._pb.HasField("current_document")


def test_documentextractor_get_transform_pb_w_minimum_int():
    from google.cloud.firestore_v1.transforms import Minimum
    from google.cloud.firestore_v1.types import write

    value = 1
    document_data = {"a": {"b": {"c": Minimum(value)}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    added = transform.minimum.integer_value
    assert added == value
    assert not transform_pb._pb.HasField("current_document")


def test_documentextractor_get_transform_pb_w_minimum_float():
    from google.cloud.firestore_v1.transforms import Minimum
    from google.cloud.firestore_v1.types import write

    value = 3.1415926
    document_data = {"a": {"b": {"c": Minimum(value)}}}
    inst = _make_document_extractor(document_data)
    document_path = "projects/project-id/databases/(default)/documents/document-id"

    transform_pb = inst.get_transform_pb(document_path)

    assert isinstance(transform_pb, write.Write)
    assert transform_pb.transform.document == document_path
    transforms = transform_pb.transform.field_transforms
    assert len(transforms) == 1
    transform = transforms[0]
    assert transform.field_path == "a.b.c"
    added = transform.minimum.double_value
    assert added == value
    assert not transform_pb._pb.HasField("current_document")


def _make_write_w_document_for_create(document_path, **data):
    from google.cloud.firestore_v1._helpers import encode_dict
    from google.cloud.firestore_v1.types import common, document, write

    return write.Write(
        update=document.Document(name=document_path, fields=encode_dict(data)),
        current_document=common.Precondition(exists=False),
    )


def _add_field_transforms_for_create(update_pb, fields):
    from google.cloud.firestore_v1 import DocumentTransform

    server_val = DocumentTransform.FieldTransform.ServerValue
    for field in fields:
        update_pb.update_transforms.append(
            DocumentTransform.FieldTransform(
                field_path=field, set_to_server_value=server_val.REQUEST_TIME
            )
        )


def __pbs_for_create_helper(do_transform=False, empty_val=False):
    from google.cloud.firestore_v1._helpers import pbs_for_create
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_path = _make_ref_string("little", "town", "of", "ham")
    document_data = {"cheese": 1.5, "crackers": True}

    if do_transform:
        document_data["butter"] = SERVER_TIMESTAMP

    if empty_val:
        document_data["mustard"] = {}

    write_pbs = pbs_for_create(document_path, document_data)

    if empty_val:
        update_pb = _make_write_w_document_for_create(
            document_path, cheese=1.5, crackers=True, mustard={}
        )
    else:
        update_pb = _make_write_w_document_for_create(
            document_path, cheese=1.5, crackers=True
        )
    expected_pbs = [update_pb]

    if do_transform:
        _add_field_transforms_for_create(update_pb, fields=["butter"])

    assert write_pbs == expected_pbs


def test__pbs_for_create_wo_transform():
    __pbs_for_create_helper()


def test__pbs_for_create_w_transform():
    __pbs_for_create_helper(do_transform=True)


def test__pbs_for_create_w_transform_and_empty_value():
    __pbs_for_create_helper(do_transform=True, empty_val=True)


def _make_write_w_document_for_set_no_merge(document_path, **data):
    from google.cloud.firestore_v1._helpers import encode_dict
    from google.cloud.firestore_v1.types import document, write

    return write.Write(
        update=document.Document(name=document_path, fields=encode_dict(data))
    )


def _add_field_transforms_for_set_no_merge(update_pb, fields):
    from google.cloud.firestore_v1 import DocumentTransform

    server_val = DocumentTransform.FieldTransform.ServerValue
    for field in fields:
        update_pb.update_transforms.append(
            DocumentTransform.FieldTransform(
                field_path=field, set_to_server_value=server_val.REQUEST_TIME
            )
        )


def test__pbs_for_set_w_empty_document():
    from google.cloud.firestore_v1._helpers import pbs_for_set_no_merge

    document_path = _make_ref_string("little", "town", "of", "ham")
    document_data = {}

    write_pbs = pbs_for_set_no_merge(document_path, document_data)

    update_pb = _make_write_w_document_for_set_no_merge(document_path)
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def test__pbs_for_set_w_only_server_timestamp():
    from google.cloud.firestore_v1._helpers import pbs_for_set_no_merge
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_path = _make_ref_string("little", "town", "of", "ham")
    document_data = {"butter": SERVER_TIMESTAMP}

    write_pbs = pbs_for_set_no_merge(document_path, document_data)

    update_pb = _make_write_w_document_for_set_no_merge(document_path)
    _add_field_transforms_for_set_no_merge(update_pb, fields=["butter"])
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def _pbs_for_set_no_merge_helper(do_transform=False, empty_val=False):
    from google.cloud.firestore_v1._helpers import pbs_for_set_no_merge
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_path = _make_ref_string("little", "town", "of", "ham")
    document_data = {"cheese": 1.5, "crackers": True}

    if do_transform:
        document_data["butter"] = SERVER_TIMESTAMP

    if empty_val:
        document_data["mustard"] = {}

    write_pbs = pbs_for_set_no_merge(document_path, document_data)

    if empty_val:
        update_pb = _make_write_w_document_for_set_no_merge(
            document_path, cheese=1.5, crackers=True, mustard={}
        )
    else:
        update_pb = _make_write_w_document_for_set_no_merge(
            document_path, cheese=1.5, crackers=True
        )
    expected_pbs = [update_pb]

    if do_transform:
        _add_field_transforms_for_set_no_merge(update_pb, fields=["butter"])

    assert write_pbs == expected_pbs


def test__pbs_for_set_defaults():
    _pbs_for_set_no_merge_helper()


def test__pbs_for_set_w_transform():
    _pbs_for_set_no_merge_helper(do_transform=True)


def test__pbs_for_set_w_transform_and_empty_value():
    # Exercise https://github.com/googleapis/google-cloud-python/issuses/5944
    _pbs_for_set_no_merge_helper(do_transform=True, empty_val=True)


def _make_document_extractor_for_merge(document_data):
    from google.cloud.firestore_v1 import _helpers

    return _helpers.DocumentExtractorForMerge(document_data)


def test_documentextractorformerge_ctor_w_empty_document():
    document_data = {}

    inst = _make_document_extractor_for_merge(document_data)

    assert inst.data_merge == []
    assert inst.transform_merge == []
    assert inst.merge == []


def test_documentextractorformerge_apply_merge_all_w_empty_document():
    document_data = {}
    inst = _make_document_extractor_for_merge(document_data)

    inst.apply_merge(True)

    assert inst.data_merge == []
    assert inst.transform_merge == []
    assert inst.merge == []


def test_documentextractorformerge_apply_merge_all_w_delete():
    from google.cloud.firestore_v1.transforms import DELETE_FIELD

    document_data = {"write_me": "value", "delete_me": DELETE_FIELD}
    inst = _make_document_extractor_for_merge(document_data)

    inst.apply_merge(True)

    expected_data_merge = [
        _make_field_path("delete_me"),
        _make_field_path("write_me"),
    ]
    assert inst.data_merge == expected_data_merge
    assert inst.transform_merge == []
    assert inst.merge == expected_data_merge


def test_documentextractorformerge_apply_merge_all_w_server_timestamp():
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_data = {"write_me": "value", "timestamp": SERVER_TIMESTAMP}
    inst = _make_document_extractor_for_merge(document_data)

    inst.apply_merge(True)

    expected_data_merge = [_make_field_path("write_me")]
    expected_transform_merge = [_make_field_path("timestamp")]
    expected_merge = [_make_field_path("timestamp"), _make_field_path("write_me")]
    assert inst.data_merge == expected_data_merge
    assert inst.transform_merge == expected_transform_merge
    assert inst.merge == expected_merge


def test_documentextractorformerge_apply_merge_list_fields_w_empty_document():
    document_data = {}
    inst = _make_document_extractor_for_merge(document_data)

    with pytest.raises(ValueError):
        inst.apply_merge(["nonesuch", "or.this"])


def test_documentextractorformerge_apply_merge_list_fields_w_unmerged_delete():
    from google.cloud.firestore_v1.transforms import DELETE_FIELD

    document_data = {
        "write_me": "value",
        "delete_me": DELETE_FIELD,
        "ignore_me": 123,
        "unmerged_delete": DELETE_FIELD,
    }
    inst = _make_document_extractor_for_merge(document_data)

    with pytest.raises(ValueError):
        inst.apply_merge(["write_me", "delete_me"])


def test_documentextractorformerge_apply_merge_list_fields_w_delete():
    from google.cloud.firestore_v1.transforms import DELETE_FIELD

    document_data = {
        "write_me": "value",
        "delete_me": DELETE_FIELD,
        "ignore_me": 123,
    }
    inst = _make_document_extractor_for_merge(document_data)

    inst.apply_merge(["write_me", "delete_me"])

    expected_set_fields = {"write_me": "value"}
    expected_deleted_fields = [_make_field_path("delete_me")]
    assert inst.set_fields == expected_set_fields
    assert inst.deleted_fields == expected_deleted_fields


def test_documentextractorformerge_apply_merge_list_fields_w_prefixes():
    document_data = {"a": {"b": {"c": 123}}}
    inst = _make_document_extractor_for_merge(document_data)

    with pytest.raises(ValueError):
        inst.apply_merge(["a", "a.b"])


def test_documentextractorformerge_apply_merge_lists_w_missing_data_paths():
    document_data = {"write_me": "value", "ignore_me": 123}
    inst = _make_document_extractor_for_merge(document_data)

    with pytest.raises(ValueError):
        inst.apply_merge(["write_me", "nonesuch"])


def test_documentextractorformerge_apply_merge_list_fields_w_non_merge_field():
    document_data = {"write_me": "value", "ignore_me": 123}
    inst = _make_document_extractor_for_merge(document_data)

    inst.apply_merge([_make_field_path("write_me")])

    expected_set_fields = {"write_me": "value"}
    assert inst.set_fields == expected_set_fields


def test_documentextractorformerge_apply_merge_list_fields_w_server_timestamp():
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_data = {
        "write_me": "value",
        "timestamp": SERVER_TIMESTAMP,
        "ignored_stamp": SERVER_TIMESTAMP,
    }
    inst = _make_document_extractor_for_merge(document_data)

    inst.apply_merge([_make_field_path("write_me"), _make_field_path("timestamp")])

    expected_data_merge = [_make_field_path("write_me")]
    expected_transform_merge = [_make_field_path("timestamp")]
    expected_merge = [_make_field_path("timestamp"), _make_field_path("write_me")]
    assert inst.data_merge == expected_data_merge
    assert inst.transform_merge == expected_transform_merge
    assert inst.merge == expected_merge
    expected_server_timestamps = [_make_field_path("timestamp")]
    assert inst.server_timestamps == expected_server_timestamps


def test_documentextractorformerge_apply_merge_list_fields_w_array_remove():
    from google.cloud.firestore_v1.transforms import ArrayRemove

    values = [2, 4, 8]
    document_data = {
        "write_me": "value",
        "remove_me": ArrayRemove(values),
        "ignored_remove_me": ArrayRemove((1, 3, 5)),
    }
    inst = _make_document_extractor_for_merge(document_data)

    inst.apply_merge([_make_field_path("write_me"), _make_field_path("remove_me")])

    expected_data_merge = [_make_field_path("write_me")]
    expected_transform_merge = [_make_field_path("remove_me")]
    expected_merge = [_make_field_path("remove_me"), _make_field_path("write_me")]
    assert inst.data_merge == expected_data_merge
    assert inst.transform_merge == expected_transform_merge
    assert inst.merge == expected_merge
    expected_array_removes = {_make_field_path("remove_me"): values}
    assert inst.array_removes == expected_array_removes


def test_documentextractorformerge_apply_merge_list_fields_w_array_union():
    from google.cloud.firestore_v1.transforms import ArrayUnion

    values = [1, 3, 5]
    document_data = {
        "write_me": "value",
        "union_me": ArrayUnion(values),
        "ignored_union_me": ArrayUnion((2, 4, 8)),
    }
    inst = _make_document_extractor_for_merge(document_data)

    inst.apply_merge([_make_field_path("write_me"), _make_field_path("union_me")])

    expected_data_merge = [_make_field_path("write_me")]
    expected_transform_merge = [_make_field_path("union_me")]
    expected_merge = [_make_field_path("union_me"), _make_field_path("write_me")]
    assert inst.data_merge == expected_data_merge
    assert inst.transform_merge == expected_transform_merge
    assert inst.merge == expected_merge
    expected_array_unions = {_make_field_path("union_me"): values}
    assert inst.array_unions == expected_array_unions


def _make_write_w_document_for_set_w_merge(document_path, **data):
    from google.cloud.firestore_v1._helpers import encode_dict
    from google.cloud.firestore_v1.types import document, write

    return write.Write(
        update=document.Document(name=document_path, fields=encode_dict(data))
    )


def _add_field_transforms_for_set_w_merge(update_pb, fields):
    from google.cloud.firestore_v1 import DocumentTransform

    server_val = DocumentTransform.FieldTransform.ServerValue
    for field in fields:
        update_pb.update_transforms.append(
            DocumentTransform.FieldTransform(
                field_path=field, set_to_server_value=server_val.REQUEST_TIME
            )
        )


def _update_document_mask(update_pb, field_paths):
    from google.cloud.firestore_v1.types import common

    update_pb._pb.update_mask.CopyFrom(
        common.DocumentMask(field_paths=sorted(field_paths))._pb
    )


def test__pbs_for_set_with_merge_w_merge_true_wo_transform():
    from google.cloud.firestore_v1._helpers import pbs_for_set_with_merge

    document_path = _make_ref_string("little", "town", "of", "ham")
    document_data = {"cheese": 1.5, "crackers": True}

    write_pbs = pbs_for_set_with_merge(document_path, document_data, merge=True)

    update_pb = _make_write_w_document_for_set_w_merge(document_path, **document_data)
    _update_document_mask(update_pb, field_paths=sorted(document_data))
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def test__pbs_for_set_with_merge_w_merge_field_wo_transform():
    from google.cloud.firestore_v1._helpers import pbs_for_set_with_merge

    document_path = _make_ref_string("little", "town", "of", "ham")
    document_data = {"cheese": 1.5, "crackers": True}

    write_pbs = pbs_for_set_with_merge(document_path, document_data, merge=["cheese"])

    update_pb = _make_write_w_document_for_set_w_merge(
        document_path, cheese=document_data["cheese"]
    )
    _update_document_mask(update_pb, field_paths=["cheese"])
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def test__pbs_for_set_with_merge_w_merge_true_w_only_transform():
    from google.cloud.firestore_v1._helpers import pbs_for_set_with_merge
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_path = _make_ref_string("little", "town", "of", "ham")
    document_data = {"butter": SERVER_TIMESTAMP}

    write_pbs = pbs_for_set_with_merge(document_path, document_data, merge=True)

    update_pb = _make_write_w_document_for_set_w_merge(document_path)
    _update_document_mask(update_pb, field_paths=())
    _add_field_transforms_for_set_w_merge(update_pb, fields=["butter"])
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def test__pbs_for_set_with_merge_w_merge_true_w_transform():
    from google.cloud.firestore_v1._helpers import pbs_for_set_with_merge
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_path = _make_ref_string("little", "town", "of", "ham")
    update_data = {"cheese": 1.5, "crackers": True}
    document_data = update_data.copy()
    document_data["butter"] = SERVER_TIMESTAMP

    write_pbs = pbs_for_set_with_merge(document_path, document_data, merge=True)

    update_pb = _make_write_w_document_for_set_w_merge(document_path, **update_data)
    _update_document_mask(update_pb, field_paths=sorted(update_data))
    _add_field_transforms_for_set_w_merge(update_pb, fields=["butter"])
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def test__pbs_for_set_with_merge_w_merge_field_w_transform():
    from google.cloud.firestore_v1._helpers import pbs_for_set_with_merge
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_path = _make_ref_string("little", "town", "of", "ham")
    update_data = {"cheese": 1.5, "crackers": True}
    document_data = update_data.copy()
    document_data["butter"] = SERVER_TIMESTAMP

    write_pbs = pbs_for_set_with_merge(
        document_path, document_data, merge=["cheese", "butter"]
    )

    update_pb = _make_write_w_document_for_set_w_merge(
        document_path, cheese=document_data["cheese"]
    )
    _update_document_mask(update_pb, ["cheese"])
    _add_field_transforms_for_set_w_merge(update_pb, fields=["butter"])
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def test__pbs_for_set_with_merge_w_merge_field_w_transform_masking_simple():
    from google.cloud.firestore_v1._helpers import pbs_for_set_with_merge
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_path = _make_ref_string("little", "town", "of", "ham")
    update_data = {"cheese": 1.5, "crackers": True}
    document_data = update_data.copy()
    document_data["butter"] = {"pecan": SERVER_TIMESTAMP}

    write_pbs = pbs_for_set_with_merge(
        document_path, document_data, merge=["butter.pecan"]
    )

    update_pb = _make_write_w_document_for_set_w_merge(document_path)
    _update_document_mask(update_pb, field_paths=())
    _add_field_transforms_for_set_w_merge(update_pb, fields=["butter.pecan"])
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def test__pbs_for_set_with_merge_w_merge_field_w_transform_parent():
    from google.cloud.firestore_v1._helpers import pbs_for_set_with_merge
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    document_path = _make_ref_string("little", "town", "of", "ham")
    update_data = {"cheese": 1.5, "crackers": True}
    document_data = update_data.copy()
    document_data["butter"] = {"popcorn": "yum", "pecan": SERVER_TIMESTAMP}

    write_pbs = pbs_for_set_with_merge(
        document_path, document_data, merge=["cheese", "butter"]
    )

    update_pb = _make_write_w_document_for_set_w_merge(
        document_path, cheese=update_data["cheese"], butter={"popcorn": "yum"}
    )
    _update_document_mask(update_pb, ["cheese", "butter"])
    _add_field_transforms_for_set_w_merge(update_pb, fields=["butter.pecan"])
    expected_pbs = [update_pb]
    assert write_pbs == expected_pbs


def _make_document_extractor_for_update(document_data):
    from google.cloud.firestore_v1._helpers import DocumentExtractorForUpdate

    return DocumentExtractorForUpdate(document_data)


def test_documentextractorforupdate_ctor_w_empty_document():
    document_data = {}

    inst = _make_document_extractor_for_update(document_data)
    assert inst.top_level_paths == []


def test_documentextractorforupdate_ctor_w_simple_keys():
    document_data = {"a": 1, "b": 2, "c": 3}

    expected_paths = [
        _make_field_path("a"),
        _make_field_path("b"),
        _make_field_path("c"),
    ]
    inst = _make_document_extractor_for_update(document_data)
    assert inst.top_level_paths == expected_paths


def test_documentextractorforupdate_ctor_w_nested_keys():
    document_data = {"a": {"d": {"e": 1}}, "b": {"f": 7}, "c": 3}

    expected_paths = [
        _make_field_path("a"),
        _make_field_path("b"),
        _make_field_path("c"),
    ]
    inst = _make_document_extractor_for_update(document_data)
    assert inst.top_level_paths == expected_paths


def test_documentextractorforupdate_ctor_w_dotted_keys():
    document_data = {"a.d.e": 1, "b.f": 7, "c": 3}

    expected_paths = [
        _make_field_path("a", "d", "e"),
        _make_field_path("b", "f"),
        _make_field_path("c"),
    ]
    inst = _make_document_extractor_for_update(document_data)
    assert inst.top_level_paths == expected_paths


def test_documentextractorforupdate_ctor_w_nested_dotted_keys():
    document_data = {"a.d.e": 1, "b.f": {"h.i": 9}, "c": 3}

    expected_paths = [
        _make_field_path("a", "d", "e"),
        _make_field_path("b", "f"),
        _make_field_path("c"),
    ]
    expected_set_fields = {"a": {"d": {"e": 1}}, "b": {"f": {"h.i": 9}}, "c": 3}
    inst = _make_document_extractor_for_update(document_data)
    assert inst.top_level_paths == expected_paths
    assert inst.set_fields == expected_set_fields


def _pbs_for_update_helper(option=None, do_transform=False, **write_kwargs):
    from google.cloud.firestore_v1 import DocumentTransform, _helpers
    from google.cloud.firestore_v1._helpers import pbs_for_update
    from google.cloud.firestore_v1.field_path import FieldPath
    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP
    from google.cloud.firestore_v1.types import common, document, write

    document_path = _make_ref_string("toy", "car", "onion", "garlic")
    field_path1 = "bitez.yum"
    value = b"\x00\x01"
    field_path2 = "blog.internet"

    field_updates = {field_path1: value}
    if do_transform:
        field_updates[field_path2] = SERVER_TIMESTAMP

    write_pbs = pbs_for_update(document_path, field_updates, option)

    map_pb = document.MapValue(fields={"yum": _value_pb(bytes_value=value)})

    field_paths = [field_path1]

    expected_update_pb = write.Write(
        update=document.Document(
            name=document_path, fields={"bitez": _value_pb(map_value=map_pb)}
        ),
        update_mask=common.DocumentMask(field_paths=field_paths),
        **write_kwargs,
    )
    if isinstance(option, _helpers.ExistsOption):
        precondition = common.Precondition(exists=False)
        expected_update_pb._pb.current_document.CopyFrom(precondition._pb)

    if do_transform:
        transform_paths = FieldPath.from_string(field_path2)
        server_val = DocumentTransform.FieldTransform.ServerValue
        field_transform_pbs = [
            write.DocumentTransform.FieldTransform(
                field_path=transform_paths.to_api_repr(),
                set_to_server_value=server_val.REQUEST_TIME,
            )
        ]
        expected_update_pb.update_transforms.extend(field_transform_pbs)

    assert write_pbs == [expected_update_pb]


def test__pbs_for_update_wo_option():
    from google.cloud.firestore_v1.types import common

    precondition = common.Precondition(exists=True)
    _pbs_for_update_helper(current_document=precondition)


def test__pbs_for_update_w__exists_option():
    from google.cloud.firestore_v1 import _helpers

    option = _helpers.ExistsOption(False)
    _pbs_for_update_helper(option=option)


def test__pbs_for_update_w_update_and_transform():
    from google.cloud.firestore_v1.types import common

    precondition = common.Precondition(exists=True)
    _pbs_for_update_helper(current_document=precondition, do_transform=True)


def _pb_for_delete_helper(option=None, **write_kwargs):
    from google.cloud.firestore_v1._helpers import pb_for_delete
    from google.cloud.firestore_v1.types import write

    document_path = _make_ref_string("chicken", "philly", "one", "two")
    write_pb = pb_for_delete(document_path, option)

    expected_pb = write.Write(delete=document_path, **write_kwargs)
    assert write_pb == expected_pb


def test__pb_for_delete_wo_option():
    _pb_for_delete_helper()


def test__pb_for_delete_w_option():
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import common

    update_time = timestamp_pb2.Timestamp(seconds=1309700594, nanos=822211297)
    option = _helpers.LastUpdateOption(update_time)
    precondition = common.Precondition(update_time=update_time)
    _pb_for_delete_helper(option=option, current_document=precondition)


def test_get_transaction_id_w_no_transaction():
    from google.cloud.firestore_v1._helpers import get_transaction_id

    ret_val = get_transaction_id(None)
    assert ret_val is None


def test_get_transaction_id_w_invalid_transaction():
    from google.cloud.firestore_v1._helpers import get_transaction_id
    from google.cloud.firestore_v1.transaction import Transaction

    transaction = Transaction(mock.sentinel.client)
    assert not transaction.in_progress
    with pytest.raises(ValueError):
        get_transaction_id(transaction)


def test_get_transaction_id_w_after_writes_not_allowed():
    from google.cloud.firestore_v1._helpers import (
        ReadAfterWriteError,
        get_transaction_id,
    )
    from google.cloud.firestore_v1.transaction import Transaction

    transaction = Transaction(mock.sentinel.client)
    transaction._id = b"under-hook"
    transaction._write_pbs.append(mock.sentinel.write)

    with pytest.raises(ReadAfterWriteError):
        get_transaction_id(transaction)


def test_get_transaction_id_w_after_writes_allowed():
    from google.cloud.firestore_v1._helpers import get_transaction_id
    from google.cloud.firestore_v1.transaction import Transaction

    transaction = Transaction(mock.sentinel.client)
    txn_id = b"we-are-0fine"
    transaction._id = txn_id
    transaction._write_pbs.append(mock.sentinel.write)

    ret_val = get_transaction_id(transaction, read_operation=False)
    assert ret_val == txn_id


def test_get_transaction_id_w_good_transaction():
    from google.cloud.firestore_v1._helpers import get_transaction_id
    from google.cloud.firestore_v1.transaction import Transaction

    transaction = Transaction(mock.sentinel.client)
    txn_id = b"doubt-it"
    transaction._id = txn_id
    assert transaction.in_progress

    assert get_transaction_id(transaction) == txn_id


def test_metadata_with_prefix():
    from google.cloud.firestore_v1._helpers import metadata_with_prefix

    database_string = "projects/prahj/databases/dee-bee"
    metadata = metadata_with_prefix(database_string)

    assert metadata == [("google-cloud-resource-prefix", database_string)]


def test_writeoption_modify_write():
    from google.cloud.firestore_v1._helpers import WriteOption

    option = WriteOption()
    with pytest.raises(NotImplementedError):
        option.modify_write(None)


def test_lastupdateoption_constructor():
    from google.cloud.firestore_v1._helpers import LastUpdateOption

    option = LastUpdateOption(mock.sentinel.timestamp)
    assert option._last_update_time is mock.sentinel.timestamp


def test_lastupdateoption___eq___different_type():
    from google.cloud.firestore_v1._helpers import LastUpdateOption

    option = LastUpdateOption(mock.sentinel.timestamp)
    other = object()
    assert not option == other


def test_lastupdateoption___eq___different_timestamp():
    from google.cloud.firestore_v1._helpers import LastUpdateOption

    option = LastUpdateOption(mock.sentinel.timestamp)
    other = LastUpdateOption(mock.sentinel.other_timestamp)
    assert not option == other


def test_lastupdateoption___eq___same_timestamp():
    from google.cloud.firestore_v1._helpers import LastUpdateOption

    option = LastUpdateOption(mock.sentinel.timestamp)
    other = LastUpdateOption(mock.sentinel.timestamp)
    assert option == other


def test_lastupdateoption_modify_write_update_time():
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1._helpers import LastUpdateOption
    from google.cloud.firestore_v1.types import common, write

    timestamp_pb = timestamp_pb2.Timestamp(seconds=683893592, nanos=229362000)
    option = LastUpdateOption(timestamp_pb)
    write_pb = write.Write()
    ret_val = option.modify_write(write_pb)

    assert ret_val is None
    expected_doc = common.Precondition(update_time=timestamp_pb)
    assert write_pb.current_document == expected_doc


def test_existsoption_constructor():
    from google.cloud.firestore_v1._helpers import ExistsOption

    option = ExistsOption(mock.sentinel.totes_bool)
    assert option._exists is mock.sentinel.totes_bool


def test_existsoption___eq___different_type():
    from google.cloud.firestore_v1._helpers import ExistsOption

    option = ExistsOption(mock.sentinel.timestamp)
    other = object()
    assert not option == other


def test_existsoption___eq___different_exists():
    from google.cloud.firestore_v1._helpers import ExistsOption

    option = ExistsOption(True)
    other = ExistsOption(False)
    assert not option == other


def test_existsoption___eq___same_exists():
    from google.cloud.firestore_v1._helpers import ExistsOption

    option = ExistsOption(True)
    other = ExistsOption(True)
    assert option == other


def test_existsoption_modify_write():
    from google.cloud.firestore_v1._helpers import ExistsOption
    from google.cloud.firestore_v1.types import common, write

    for exists in (True, False):
        option = ExistsOption(exists)
        write_pb = write.Write()
        ret_val = option.modify_write(write_pb)

        assert ret_val is None
        expected_doc = common.Precondition(exists=exists)
        assert write_pb.current_document == expected_doc


def test_make_retry_timeout_kwargs_default():
    from google.api_core.gapic_v1.method import DEFAULT

    from google.cloud.firestore_v1._helpers import make_retry_timeout_kwargs

    kwargs = make_retry_timeout_kwargs(DEFAULT, None)
    expected = {}
    assert kwargs == expected


def test_make_retry_timeout_kwargs_retry_None():
    from google.cloud.firestore_v1._helpers import make_retry_timeout_kwargs

    kwargs = make_retry_timeout_kwargs(None, None)
    expected = {"retry": None}
    assert kwargs == expected


def test_make_retry_timeout_kwargs_retry_only():
    from google.api_core.retry import Retry

    from google.cloud.firestore_v1._helpers import make_retry_timeout_kwargs

    retry = Retry(predicate=object())
    kwargs = make_retry_timeout_kwargs(retry, None)
    expected = {"retry": retry}
    assert kwargs == expected


def test_make_retry_timeout_kwargs_timeout_only():
    from google.api_core.gapic_v1.method import DEFAULT

    from google.cloud.firestore_v1._helpers import make_retry_timeout_kwargs

    timeout = 123.0
    kwargs = make_retry_timeout_kwargs(DEFAULT, timeout)
    expected = {"timeout": timeout}
    assert kwargs == expected


def test_make_retry_timeout_kwargs_retry_and_timeout():
    from google.api_core.retry import Retry

    from google.cloud.firestore_v1._helpers import make_retry_timeout_kwargs

    retry = Retry(predicate=object())
    timeout = 123.0
    kwargs = make_retry_timeout_kwargs(retry, timeout)
    expected = {"retry": retry, "timeout": timeout}
    assert kwargs == expected


@pytest.mark.asyncio
async def test_asyncgenerator_async_iter():
    from typing import List

    consumed: List[int] = []
    async for el in AsyncIter([1, 2, 3]):
        consumed.append(el)
    assert consumed == [1, 2, 3]


class AsyncMock(mock.MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


async def AsyncIter(items):
    """Utility to help recreate the effect of an async generator. Useful when
    you need to mock a system that requires `async for`.
    """
    for i in items:
        yield i


def _value_pb(**kwargs):
    from google.cloud.firestore_v1.types.document import Value

    return Value(**kwargs)


def _make_ref_string(project, database, *path):
    from google.cloud.firestore_v1 import _helpers

    doc_rel_path = _helpers.DOCUMENT_PATH_DELIMITER.join(path)
    return "projects/{}/databases/{}/documents/{}".format(
        project, database, doc_rel_path
    )


def _make_client(project="quark"):
    from google.cloud.firestore_v1.client import Client

    credentials = make_test_credentials()
    return Client(project=project, credentials=credentials)


def _make_field_path(*fields):
    from google.cloud.firestore_v1 import field_path

    return field_path.FieldPath(*fields)
