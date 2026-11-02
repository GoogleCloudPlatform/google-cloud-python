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

import decimal
import math
from enum import Enum
from typing import Any

from google.cloud.firestore_v1._helpers import GeoPoint, decode_value


def _to_number(val: Any) -> Any:
    """Extract a numeric value (int, float, Decimal) from a Value protobuf or Python value.

    Directly inspects the protobuf value_type without calling decode_value()
    for optimal performance.
    """
    value_pb = getattr(val, "_pb", val)
    which = (
        value_pb.WhichOneof("value_type") if hasattr(value_pb, "WhichOneof") else None
    )

    if which == "integer_value":
        return value_pb.integer_value
    elif which == "double_value":
        return value_pb.double_value
    elif which == "map_value":
        fields = value_pb.map_value.fields
        if "__int__" in fields:
            return fields["__int__"].integer_value
        elif "__decimal128__" in fields:
            return decimal.Decimal(fields["__decimal128__"].string_value)

    num = decode_value(val, None)
    to_decimal = getattr(num, "to_decimal", None)
    return to_decimal() if callable(to_decimal) else getattr(num, "value", num)


def _is_nan(val: Any) -> bool:
    """Check if a numeric value is NaN, safely handling OverflowError and non-floats."""
    if hasattr(val, "is_nan"):
        return val.is_nan()
    if isinstance(val, (int, decimal.Decimal)):
        return False
    try:
        return math.isnan(val)
    except (TypeError, OverflowError):
        return False


class TypeOrder(Enum):
    """The supported Data Type.

    Note: The Enum value does not imply the sort order.
    """

    NULL = 0
    BOOLEAN = 1
    NUMBER = 2
    TIMESTAMP = 3
    STRING = 4
    BLOB = 5
    REF = 6
    GEO_POINT = 7
    ARRAY = 8
    OBJECT = 9
    VECTOR = 10
    BSON_MIN_KEY = 11
    BSON_MAX_KEY = 12
    BSON_OBJECT_ID = 13
    BSON_BINARY = 14
    BSON_REGEX = 15
    BSON_TIMESTAMP = 16

    @staticmethod
    def from_value(value) -> Any:
        value_pb = getattr(value, "_pb", value)
        v = value_pb.WhichOneof("value_type")
        lut = {
            "null_value": TypeOrder.NULL,
            "boolean_value": TypeOrder.BOOLEAN,
            "integer_value": TypeOrder.NUMBER,
            "double_value": TypeOrder.NUMBER,
            "timestamp_value": TypeOrder.TIMESTAMP,
            "string_value": TypeOrder.STRING,
            "bytes_value": TypeOrder.BLOB,
            "reference_value": TypeOrder.REF,
            "geo_point_value": TypeOrder.GEO_POINT,
            "array_value": TypeOrder.ARRAY,
            "map_value": TypeOrder.OBJECT,
        }

        if v not in lut:
            raise ValueError(f"Could not detect value type for {v}")

        if v == "map_value":
            fields = value_pb.map_value.fields
            if len(fields) == 1:
                key = next(iter(fields))
                bson_order = _BSON_KEY_TO_TYPE_ORDER.get(key)
                if bson_order is not None:
                    return bson_order
            if "__type__" in fields and fields["__type__"].string_value == "__vector__":
                return TypeOrder.VECTOR
        return lut[v]


# Maps BSON wire map keys directly to their corresponding TypeOrder.
# BSONInt32 and BSONDecimal128 map to TypeOrder.NUMBER, enabling cross-type comparisons.
_BSON_KEY_TO_TYPE_ORDER = {
    "__min__": TypeOrder.BSON_MIN_KEY,
    "__max__": TypeOrder.BSON_MAX_KEY,
    "__oid__": TypeOrder.BSON_OBJECT_ID,
    "__int__": TypeOrder.NUMBER,
    "__decimal128__": TypeOrder.NUMBER,
    "__binary__": TypeOrder.BSON_BINARY,
    "__request_timestamp__": TypeOrder.BSON_TIMESTAMP,
    "__regex__": TypeOrder.BSON_REGEX,
}


# NOTE: This order is defined by the backend and cannot be changed.
_TYPE_ORDER_MAP = {
    TypeOrder.NULL: 0,
    TypeOrder.BSON_MIN_KEY: 1,
    TypeOrder.BOOLEAN: 2,
    TypeOrder.NUMBER: 3,
    TypeOrder.TIMESTAMP: 4,
    TypeOrder.BSON_TIMESTAMP: 5,
    TypeOrder.STRING: 6,
    TypeOrder.BLOB: 7,
    TypeOrder.BSON_BINARY: 8,
    TypeOrder.REF: 9,
    TypeOrder.BSON_OBJECT_ID: 10,
    TypeOrder.GEO_POINT: 11,
    TypeOrder.BSON_REGEX: 12,
    TypeOrder.ARRAY: 13,
    TypeOrder.VECTOR: 14,
    TypeOrder.OBJECT: 15,
    TypeOrder.BSON_MAX_KEY: 16,
}


class Order(object):
    """
    Order implements the ordering semantics of the backend.
    """

    @classmethod
    def compare(cls, left, right) -> int:
        """
        Main comparison function for all Firestore types.
        @return -1 is left < right, 0 if left == right, otherwise 1
        """
        # First compare the types.
        leftType = TypeOrder.from_value(left)
        rightType = TypeOrder.from_value(right)
        if leftType != rightType:
            if _TYPE_ORDER_MAP[leftType] < _TYPE_ORDER_MAP[rightType]:
                return -1
            else:
                return 1

        if (
            leftType == TypeOrder.NULL
            or leftType == TypeOrder.BSON_MIN_KEY
            or leftType == TypeOrder.BSON_MAX_KEY
        ):
            return 0  # sentinels are equal
        elif leftType == TypeOrder.BOOLEAN:
            return cls._compare_to(left.boolean_value, right.boolean_value)
        elif leftType == TypeOrder.NUMBER:
            # Handles int64, double, BSONInt32, and BSONDecimal128.
            return cls.compare_numbers(left, right)
        elif leftType == TypeOrder.TIMESTAMP:
            return cls.compare_timestamps(left, right)
        elif leftType == TypeOrder.BSON_TIMESTAMP:
            return cls.compare_bson_timestamps(left, right)
        elif leftType == TypeOrder.STRING:
            return cls._compare_to(left.string_value, right.string_value)
        elif leftType == TypeOrder.BLOB:
            return cls.compare_blobs(left, right)
        elif leftType == TypeOrder.BSON_BINARY:
            return cls.compare_bson_binaries(left, right)
        elif leftType == TypeOrder.REF:
            return cls.compare_resource_paths(left, right)
        elif leftType == TypeOrder.BSON_OBJECT_ID:
            return cls.compare_bson_object_ids(left, right)
        elif leftType == TypeOrder.GEO_POINT:
            return cls.compare_geo_points(left, right)
        elif leftType == TypeOrder.BSON_REGEX:
            return cls.compare_bson_regexes(left, right)
        elif leftType == TypeOrder.ARRAY:
            return cls.compare_arrays(left, right)
        elif leftType == TypeOrder.VECTOR:
            # ARRAYs < VECTORs < MAPs
            return cls.compare_vectors(left, right)
        elif leftType == TypeOrder.OBJECT:
            return cls.compare_objects(left, right)
        else:
            raise ValueError(f"Unknown TypeOrder {leftType}")

    @staticmethod
    def compare_blobs(left, right) -> int:
        left_bytes = left.bytes_value
        right_bytes = right.bytes_value

        return Order._compare_to(left_bytes, right_bytes)

    @staticmethod
    def compare_bson_binaries(left, right) -> int:
        l_bin = left.map_value.fields["__binary__"].bytes_value
        r_bin = right.map_value.fields["__binary__"].bytes_value

        l_subtype = l_bin[0] if l_bin else 0
        r_subtype = r_bin[0] if r_bin else 0

        cmp_subtype = Order._compare_to(l_subtype, r_subtype)
        if cmp_subtype != 0:
            return cmp_subtype

        return Order._compare_to(
            l_bin[1:] if l_bin else b"", r_bin[1:] if r_bin else b""
        )

    @staticmethod
    def compare_bson_object_ids(left, right) -> int:
        l_oid = left.map_value.fields["__oid__"].string_value
        r_oid = right.map_value.fields["__oid__"].string_value
        return Order._compare_to(l_oid, r_oid)

    @staticmethod
    def compare_bson_regexes(left, right) -> int:
        l_regex = left.map_value.fields["__regex__"].map_value.fields
        r_regex = right.map_value.fields["__regex__"].map_value.fields

        l_pattern = l_regex["pattern"].string_value if "pattern" in l_regex else ""
        r_pattern = r_regex["pattern"].string_value if "pattern" in r_regex else ""
        cmp_pat = Order._compare_to(l_pattern, r_pattern)
        if cmp_pat != 0:
            return cmp_pat

        l_options = l_regex["options"].string_value if "options" in l_regex else ""
        r_options = r_regex["options"].string_value if "options" in r_regex else ""
        return Order._compare_to(l_options, r_options)

    @staticmethod
    def compare_timestamps(left, right) -> Any:
        left_pb = getattr(left, "_pb", left)
        right_pb = getattr(right, "_pb", right)

        seconds = Order._compare_to(
            left_pb.timestamp_value.seconds, right_pb.timestamp_value.seconds
        )
        if seconds != 0:
            return seconds

        return Order._compare_to(
            left_pb.timestamp_value.nanos, right_pb.timestamp_value.nanos
        )

    @staticmethod
    def compare_bson_timestamps(left, right) -> Any:
        left_pb = getattr(left, "_pb", left)
        right_pb = getattr(right, "_pb", right)

        l_ts = left_pb.map_value.fields["__request_timestamp__"].map_value.fields
        l_sec = l_ts["seconds"].integer_value if "seconds" in l_ts else 0
        l_inc = l_ts["increment"].integer_value if "increment" in l_ts else 0

        r_ts = right_pb.map_value.fields["__request_timestamp__"].map_value.fields
        r_sec = r_ts["seconds"].integer_value if "seconds" in r_ts else 0
        r_inc = r_ts["increment"].integer_value if "increment" in r_ts else 0

        seconds = Order._compare_to(l_sec, r_sec)
        if seconds != 0:
            return seconds

        return Order._compare_to(l_inc, r_inc)

    @staticmethod
    def compare_geo_points(left, right) -> Any:
        left_value = decode_value(left, None)
        right_value = decode_value(right, None)
        if not isinstance(left_value, GeoPoint) or not isinstance(
            right_value, GeoPoint
        ):
            raise AttributeError("invalid geopoint encountered")
        cmp = (left_value.latitude > right_value.latitude) - (
            left_value.latitude < right_value.latitude
        )

        if cmp != 0:
            return cmp
        return (left_value.longitude > right_value.longitude) - (
            left_value.longitude < right_value.longitude
        )

    @staticmethod
    def compare_resource_paths(left, right) -> int:
        left = left.reference_value
        right = right.reference_value

        left_segments = left.split("/")
        right_segments = right.split("/")
        shorter = min(len(left_segments), len(right_segments))
        # compare segments
        for i in range(shorter):
            if left_segments[i] < right_segments[i]:
                return -1
            if left_segments[i] > right_segments[i]:
                return 1

        left_length = len(left)
        right_length = len(right)
        return (left_length > right_length) - (left_length < right_length)

    @staticmethod
    def compare_arrays(left, right) -> int:
        l_values = left.array_value.values
        r_values = right.array_value.values

        length = min(len(l_values), len(r_values))
        for i in range(length):
            cmp = Order.compare(l_values[i], r_values[i])
            if cmp != 0:
                return cmp

        return Order._compare_to(len(l_values), len(r_values))

    @staticmethod
    def compare_vectors(left, right) -> int:
        # First compare the size of vector.
        l_values = left.map_value.fields["value"]
        r_values = right.map_value.fields["value"]

        left_length = len(l_values.array_value.values)
        right_length = len(r_values.array_value.values)

        if left_length != right_length:
            return Order._compare_to(left_length, right_length)

        # Compare element if the size matches.
        return Order.compare_arrays(l_values, r_values)

    @staticmethod
    def compare_objects(left, right) -> int:
        left_fields = left.map_value.fields
        right_fields = right.map_value.fields

        for left_key, right_key in zip(sorted(left_fields), sorted(right_fields)):
            keyCompare = Order._compare_to(left_key, right_key)
            if keyCompare != 0:
                return keyCompare

            value_compare = Order.compare(
                left_fields[left_key], right_fields[right_key]
            )
            if value_compare != 0:
                return value_compare

        return Order._compare_to(len(left_fields), len(right_fields))

    @staticmethod
    def compare_numbers(left, right) -> int:
        """Compare numeric values across int, float, BSONInt32, and BSONDecimal128."""
        left_val = _to_number(left)
        right_val = _to_number(right)

        left_nan = _is_nan(left_val)
        right_nan = _is_nan(right_val)
        if left_nan or right_nan:
            return 0 if (left_nan and right_nan) else (-1 if left_nan else 1)

        # Python raises TypeError when comparing Decimal with float directly,
        # but allows comparing Decimal with int. Convert float to Decimal
        # to ensure safe cross-type comparison without float overflow.
        if isinstance(left_val, decimal.Decimal) and isinstance(right_val, float):
            right_val = decimal.Decimal(str(right_val))
        elif isinstance(right_val, decimal.Decimal) and isinstance(left_val, float):
            left_val = decimal.Decimal(str(left_val))

        return Order._compare_to(left_val, right_val)

    @staticmethod
    def compare_doubles(left, right) -> int:
        if math.isnan(left):
            if math.isnan(right):
                return 0
            return -1
        if math.isnan(right):
            return 1

        return Order._compare_to(left, right)

    @staticmethod
    def _compare_to(left, right) -> int:
        # We can't just use cmp(left, right) because cmp doesn't exist
        # in Python 3, so this is an equivalent suggested by
        # https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons
        return (left > right) - (left < right)
