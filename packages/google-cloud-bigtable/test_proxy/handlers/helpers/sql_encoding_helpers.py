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
"""
This module contains helpers for handling sql data types for the test proxy.
"""
from datetime import date
from typing import Any

from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.bigtable.data.execute_query.metadata import SqlType


PRIMITIVE_TYPE_MAPPING = {
    "bytes_type": SqlType.Bytes(),
    "string_type": SqlType.String(),
    "int64_type": SqlType.Int64(),
    "float32_type": SqlType.Float32(),
    "float64_type": SqlType.Float64(),
    "bool_type": SqlType.Bool(),
    "timestamp_type": SqlType.Timestamp(),
    "date_type": SqlType.Date(),
}

PRIMITIVE_VALUE_FIELDS = [
    "bytes_value",
    "string_value",
    "int_value",
    "float_value",
    "bool_value",
]


def snake_to_camel(snake_string):
    """
    Used to convert query parameter names back to camel case. This needs to be handled
    specifically because the python test proxy converts all keys to snake case when it
    converts proto messages to dicts.
    """
    components = snake_string.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def convert_value(type: SqlType, val: Any):
    """
    Converts python value to a dict representation of a protobuf Value message.
    """
    if val is None:
        return {}
    elif isinstance(type, SqlType.Date):
        return {"date_value": val}
    elif isinstance(type, SqlType.Map):
        key_type = type.key_type
        val_type = type.value_type
        results = []
        for k, v in val.items():
            results.append(
                {
                    "array_value": {
                        "values": [
                            convert_value(key_type, k),
                            convert_value(val_type, v),
                        ]
                    }
                }
            )
        return {"array_value": {"values": results}}
    elif isinstance(type, SqlType.Struct):
        results = []
        for i, (_, field_val) in enumerate(val.fields):
            results.append(convert_value(type[i], field_val))
        return {"array_value": {"values": results}}
    elif isinstance(type, SqlType.Array):
        elem_type = type.element_type
        results = []
        for e in val:
            results.append(convert_value(elem_type, e))
        return {"array_value": {"values": results}}
    else:
        return type._to_value_pb_dict(val)


def convert_type(type: SqlType):
    if isinstance(type, SqlType.Map):
        return {
            "map_type": {
                "key_type": convert_type(type.key_type),
                "value_type": convert_type(type.value_type),
            }
        }
    elif isinstance(type, SqlType.Struct):
        fields = []
        for field_name, field_type in type.fields:
            fields.append({"field_name": field_name, "type": convert_type(field_type)})
        return {"struct_type": {"fields": fields}}
    elif isinstance(type, SqlType.Array):
        return {"array_type": {"element_type": convert_type(type.element_type)}}
    else:
        return type._to_type_pb_dict()


def to_sql_type(proto_type_dict):
    if len(proto_type_dict.keys()) != 1:
        raise ValueError("Invalid type: ", proto_type_dict)
    type_field = list(proto_type_dict.keys())[0]
    if type_field in PRIMITIVE_TYPE_MAPPING:
        return PRIMITIVE_TYPE_MAPPING[type_field]
    elif type_field == "array_type":
        elem_type_dict = proto_type_dict["array_type"]["element_type"]
        return SqlType.Array(to_sql_type(elem_type_dict))
    else:
        raise ValueError("Invalid query parameter type: ", proto_type_dict)


def convert_to_python_value(proto_val: Any, sql_type: SqlType):
    """
    Converts the given dict representation of a proto Value message to the correct
    python value. This is used to convert query params to the represetation expected
    from users. We can't reuse existing parsers because they expect actual proto messages
    rather than dicts.
    """
    value_field = sql_type.value_pb_dict_field_name
    if isinstance(sql_type, SqlType.Array):
        if "array_value" not in proto_val:
            return None
        elem_type = sql_type.element_type
        return [
            convert_to_python_value(v, elem_type)
            for v in proto_val["array_value"]["values"]
        ]
    if value_field and value_field not in proto_val:
        return None
    if value_field in PRIMITIVE_VALUE_FIELDS:
        return proto_val[value_field]
    if isinstance(sql_type, SqlType.Timestamp):
        if "timestamp_value" not in proto_val:
            return None
        return DatetimeWithNanoseconds.from_rfc3339(proto_val["timestamp_value"])
    if isinstance(sql_type, SqlType.Date):
        if "date_value" not in proto_val:
            return None
        return date(
            year=proto_val["date_value"]["year"],
            month=proto_val["date_value"]["month"],
            day=proto_val["date_value"]["day"],
        )
    raise ValueError("Unexpected parameter: %s, %s", proto_val, sql_type)


def convert_params(request_params):
    """
    Converts the given dictionary of parameters to a python representation.
    This converts parameter names from snake to camel case and protobuf Value dicts
    to python values.
    """
    python_params = {}
    param_types = {}
    for param_key, param_value in request_params.items():
        if "type" not in param_value:
            raise ValueError("type must be set for query params")

        sql_type = to_sql_type(param_value["type"])
        readjusted_param_name = snake_to_camel(param_key)
        param_types[readjusted_param_name] = sql_type
        if len(param_value.keys()) == 1:
            # this means type is set and nothing else
            python_params[readjusted_param_name] = None
        elif len(param_value) > 2:
            raise ValueError("Unexpected Value format: ", param_value)
        python_params[readjusted_param_name] = convert_to_python_value(
            param_value, sql_type
        )
    return python_params, param_types
