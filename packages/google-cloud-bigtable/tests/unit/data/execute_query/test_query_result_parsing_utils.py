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
from google.type import date_pb2

from google.cloud.bigtable.data.execute_query._query_result_parsing_utils import (
    _parse_pb_value_to_python_value,
)
from google.cloud.bigtable.data.execute_query.metadata import (
    SqlType,
    _pb_type_to_metadata_type,
)
from google.cloud.bigtable.data.execute_query.values import Struct
from google.cloud.bigtable_v2 import Type as PBType
from google.cloud.bigtable_v2 import Value as PBValue
from tests.unit.data.execute_query.sql_helpers import enum_type, int64_type, proto_type

from .resources import singer_pb2

TYPE_BYTES = {"bytes_type": {}}
TYPE_TIMESTAMP = {"timestamp_type": {}}


class TestQueryResultParsingUtils:
    @pytest.mark.parametrize(
        "type_dict,value_dict,expected_metadata_type,expected_value",
        [
            (int64_type(), {"int_value": 1}, SqlType.Int64, 1),
            (
                {"string_type": {}},
                {"string_value": "test"},
                SqlType.String,
                "test",
            ),
            ({"bool_type": {}}, {"bool_value": False}, SqlType.Bool, False),
            (
                {"bytes_type": {}},
                {"bytes_value": b"test"},
                SqlType.Bytes,
                b"test",
            ),
            (
                {"float64_type": {}},
                {"float_value": 17.21},
                SqlType.Float64,
                17.21,
            ),
            (
                {"timestamp_type": {}},
                {"timestamp_value": {"seconds": 1715864647, "nanos": 12}},
                SqlType.Timestamp,
                DatetimeWithNanoseconds(
                    2024, 5, 16, 13, 4, 7, nanosecond=12, tzinfo=datetime.timezone.utc
                ),
            ),
            (
                {"date_type": {}},
                {"date_value": {"year": 1800, "month": 12, "day": 0}},
                SqlType.Date,
                date_pb2.Date(year=1800, month=12, day=0),
            ),
        ],
    )
    def test_basic_types(
        self, type_dict, value_dict, expected_metadata_type, expected_value
    ):
        _type = PBType(type_dict)
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is expected_metadata_type
        value = PBValue(value_dict)
        assert (
            _parse_pb_value_to_python_value(value._pb, metadata_type, "my_field")
            == expected_value
        )

    def test__proto(self):
        _type = PBType({"proto_type": {}})
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Proto

        singer = singer_pb2.Singer(name="John")
        value = PBValue({"bytes_value": singer.SerializeToString()})

        # without proto definition
        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, "proto_field"
        )
        assert result == singer.SerializeToString()
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            None,
            {"proto_field": singer_pb2.Singer()},
        )
        assert result == singer.SerializeToString()

        # with proto definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "proto_field",
            {"proto_field": singer_pb2.Singer()},
        )
        assert result == singer

    def test__enum(self):
        _type = PBType({"enum_type": {}})
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Enum

        value = PBValue({"int_value": 1})

        # without enum definition
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "enum_field")
        assert result == 1
        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, None, {"enum_field": singer_pb2.Genre}
        )
        assert result == 1

        # with enum definition
        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, "enum_field", {"enum_field": singer_pb2.Genre}
        )
        assert result == "JAZZ"

    # Larger test cases were extracted for readability
    def test__array(self):
        _type = PBType({"array_type": {"element_type": int64_type()}})
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Array
        assert type(metadata_type.element_type) is SqlType.Int64
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {"int_value": 1},
                        {"int_value": 2},
                        {"int_value": 3},
                        {"int_value": 4},
                    ]
                }
            }
        )
        assert _parse_pb_value_to_python_value(
            value._pb, metadata_type, "array_field"
        ) == [1, 2, 3, 4]

    def test__array_of_protos(self):
        _type = PBType({"array_type": {"element_type": proto_type()}})
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Array
        assert type(metadata_type.element_type) is SqlType.Proto

        singer1 = singer_pb2.Singer(name="John")
        singer2 = singer_pb2.Singer(name="Taylor")
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {"bytes_value": singer1.SerializeToString()},
                        {"bytes_value": singer2.SerializeToString()},
                    ]
                }
            }
        )

        # without proto definition
        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, "array_field"
        )
        assert result == [singer1.SerializeToString(), singer2.SerializeToString()]
        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, None, {"array_field": singer_pb2.Singer()}
        )
        assert result == [singer1.SerializeToString(), singer2.SerializeToString()]

        # with proto definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "array_field",
            {"array_field": singer_pb2.Singer()},
        )
        assert result == [singer1, singer2]

    def test__array_of_enums(self):
        _type = PBType({"array_type": {"element_type": enum_type()}})
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Array
        assert type(metadata_type.element_type) is SqlType.Enum

        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {"int_value": 0},  # POP
                        {"int_value": 1},  # JAZZ
                    ]
                }
            }
        )

        # without enum definition
        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, "array_field"
        )
        assert result == [0, 1]

        # with enum definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "array_field",
            {"array_field": singer_pb2.Genre},
        )
        assert result == ["POP", "JAZZ"]

    def test__struct(self):
        _type = PBType(
            {
                "struct_type": {
                    "fields": [
                        {
                            "field_name": "field1",
                            "type_": int64_type(),
                        },
                        {
                            "field_name": None,
                            "type_": {"string_type": {}},
                        },
                        {
                            "field_name": "field3",
                            "type_": {"array_type": {"element_type": int64_type()}},
                        },
                        {
                            "field_name": "field3",
                            "type_": {"string_type": {}},
                        },
                    ]
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {"int_value": 1},
                        {"string_value": "test2"},
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 2},
                                    {"int_value": 3},
                                    {"int_value": 4},
                                    {"int_value": 5},
                                ]
                            }
                        },
                        {"string_value": "test4"},
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Struct
        assert type(metadata_type["field1"]) is SqlType.Int64
        assert type(metadata_type[1]) is SqlType.String
        assert type(metadata_type[2]) is SqlType.Array
        assert type(metadata_type[2].element_type) is SqlType.Int64
        assert type(metadata_type[3]) is SqlType.String

        # duplicate fields not accesible by name
        with pytest.raises(KeyError, match="Ambigious field name"):
            metadata_type["field3"]

        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, "struct_field"
        )
        assert isinstance(result, Struct)
        assert result["field1"] == result[0] == 1
        assert result[1] == "test2"

        # duplicate fields not accesible by name
        with pytest.raises(KeyError, match="Ambigious field name"):
            result["field3"]

        # duplicate fields accessible by index
        assert result[2] == [2, 3, 4, 5]
        assert result[3] == "test4"

    def test__struct_with_proto_and_enum(self):
        singer1 = singer_pb2.Singer(name="John")
        singer2 = singer_pb2.Singer(name="Taylor")
        _type = PBType(
            {
                "struct_type": {
                    "fields": [
                        {
                            "field_name": "field1",
                            "type_": proto_type(),
                        },
                        {
                            "field_name": None,
                            "type_": proto_type(),
                        },
                        {
                            "field_name": "field2",
                            "type_": enum_type(),
                        },
                        {
                            "field_name": None,
                            "type_": enum_type(),
                        },
                    ]
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {"bytes_value": singer1.SerializeToString()},
                        {"bytes_value": singer2.SerializeToString()},
                        {"int_value": 0},
                        {"int_value": 1},
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Struct
        assert type(metadata_type["field1"]) is SqlType.Proto
        assert type(metadata_type["field2"]) is SqlType.Enum
        assert type(metadata_type[0]) is SqlType.Proto
        assert type(metadata_type[1]) is SqlType.Proto
        assert type(metadata_type[2]) is SqlType.Enum
        assert type(metadata_type[3]) is SqlType.Enum

        # without proto definition
        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, "struct_field"
        )
        assert isinstance(result, Struct)
        assert result["field1"] == singer1.SerializeToString()
        assert result["field2"] == 0
        assert result[0] == singer1.SerializeToString()
        assert result[1] == singer2.SerializeToString()
        assert result[2] == 0
        assert result[3] == 1

        # with proto definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "struct_field",
            {
                "struct_field.field1": singer_pb2.Singer(),
                "struct_field.field2": singer_pb2.Genre,
            },
        )
        assert isinstance(result, Struct)
        assert result["field1"] == singer1
        assert result["field2"] == "POP"
        assert result[0] == singer1
        # unnamed proto fields won't get parsed
        assert result[1] == singer2.SerializeToString()
        assert result[2] == "POP"
        # unnamed enum fields won't get parsed
        assert result[3] == 1

    def test__array_of_structs(self):
        _type = PBType(
            {
                "array_type": {
                    "element_type": {
                        "struct_type": {
                            "fields": [
                                {
                                    "field_name": "field1",
                                    "type_": int64_type(),
                                },
                                {
                                    "field_name": None,
                                    "type_": {"string_type": {}},
                                },
                                {
                                    "field_name": "field3",
                                    "type_": {"bool_type": {}},
                                },
                            ]
                        }
                    }
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 1},
                                    {"string_value": "test1"},
                                    {"bool_value": True},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 2},
                                    {"string_value": "test2"},
                                    {"bool_value": False},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 3},
                                    {"string_value": "test3"},
                                    {"bool_value": True},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 4},
                                    {"string_value": "test4"},
                                    {"bool_value": False},
                                ]
                            }
                        },
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Array
        assert type(metadata_type.element_type) is SqlType.Struct
        assert type(metadata_type.element_type["field1"]) is SqlType.Int64
        assert type(metadata_type.element_type[1]) is SqlType.String
        assert type(metadata_type.element_type["field3"]) is SqlType.Bool

        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, "array_field"
        )
        assert isinstance(result, list)
        assert len(result) == 4

        assert isinstance(result[0], Struct)
        assert result[0]["field1"] == 1
        assert result[0][1] == "test1"
        assert result[0]["field3"]

        assert isinstance(result[1], Struct)
        assert result[1]["field1"] == 2
        assert result[1][1] == "test2"
        assert not result[1]["field3"]

        assert isinstance(result[2], Struct)
        assert result[2]["field1"] == 3
        assert result[2][1] == "test3"
        assert result[2]["field3"]

        assert isinstance(result[3], Struct)
        assert result[3]["field1"] == 4
        assert result[3][1] == "test4"
        assert not result[3]["field3"]

    def test__array_of_structs_with_proto_and_enum(self):
        singer1 = singer_pb2.Singer(name="John")
        singer2 = singer_pb2.Singer(name="Taylor")
        _type = PBType(
            {
                "array_type": {
                    "element_type": {
                        "struct_type": {
                            "fields": [
                                {
                                    "field_name": "proto_field",
                                    "type_": proto_type(),
                                },
                                {
                                    "field_name": "enum_field",
                                    "type_": enum_type(),
                                },
                                {
                                    "field_name": None,
                                    "type_": proto_type(),
                                },
                            ]
                        }
                    }
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {
                            "array_value": {
                                "values": [
                                    {"bytes_value": singer1.SerializeToString()},
                                    {"int_value": 0},  # POP
                                    {"bytes_value": singer1.SerializeToString()},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"bytes_value": singer2.SerializeToString()},
                                    {"int_value": 1},  # JAZZ
                                    {"bytes_value": singer2.SerializeToString()},
                                ]
                            }
                        },
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Array
        assert type(metadata_type.element_type) is SqlType.Struct
        assert type(metadata_type.element_type["proto_field"]) is SqlType.Proto
        assert type(metadata_type.element_type["enum_field"]) is SqlType.Enum
        assert type(metadata_type.element_type[2]) is SqlType.Proto

        # without proto definition
        result = _parse_pb_value_to_python_value(
            value._pb, metadata_type, "array_field"
        )
        assert isinstance(result, list)
        assert len(result) == 2
        assert isinstance(result[0], Struct)
        assert result[0]["proto_field"] == singer1.SerializeToString()
        assert result[0]["enum_field"] == 0
        assert result[0][2] == singer1.SerializeToString()
        assert isinstance(result[1], Struct)
        assert result[1]["proto_field"] == singer2.SerializeToString()
        assert result[1]["enum_field"] == 1
        assert result[1][2] == singer2.SerializeToString()

        # with proto definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "array_field",
            {
                "array_field.proto_field": singer_pb2.Singer(),
                "array_field.enum_field": singer_pb2.Genre,
                "array_field": singer_pb2.Singer(),  # unused
            },
        )
        assert isinstance(result, list)
        assert len(result) == 2
        assert isinstance(result[0], Struct)
        assert result[0]["proto_field"] == singer1
        assert result[0]["enum_field"] == "POP"
        # unnamed proto fields won't get parsed
        assert result[0][2] == singer1.SerializeToString()
        assert isinstance(result[1], Struct)
        assert result[1]["proto_field"] == singer2
        assert result[1]["enum_field"] == "JAZZ"
        # unnamed proto fields won't get parsed
        assert result[1][2] == singer2.SerializeToString()

    def test__map(self):
        _type = PBType(
            {
                "map_type": {
                    "key_type": int64_type(),
                    "value_type": {"string_type": {}},
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 1},
                                    {"string_value": "test1"},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 2},
                                    {"string_value": "test2"},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 3},
                                    {"string_value": "test3"},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 4},
                                    {"string_value": "test4"},
                                ]
                            }
                        },
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Map
        assert type(metadata_type.key_type) is SqlType.Int64
        assert type(metadata_type.value_type) is SqlType.String

        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")
        assert isinstance(result, dict)
        assert len(result) == 4

        assert result == {
            1: "test1",
            2: "test2",
            3: "test3",
            4: "test4",
        }

    def test__map_repeated_values(self):
        _type = PBType(
            {
                "map_type": {
                    "key_type": int64_type(),
                    "value_type": {"string_type": {}},
                }
            },
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 1},
                                    {"string_value": "test1"},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 1},
                                    {"string_value": "test2"},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 1},
                                    {"string_value": "test3"},
                                ]
                            }
                        },
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")
        assert len(result) == 1

        assert result == {
            1: "test3",
        }

    def test__map_with_protos(self):
        singer1 = singer_pb2.Singer(name="John")
        singer2 = singer_pb2.Singer(name="Taylor")
        _type = PBType(
            {
                "map_type": {
                    "key_type": int64_type(),
                    "value_type": proto_type(),
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 1},
                                    {"bytes_value": singer1.SerializeToString()},
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 2},
                                    {"bytes_value": singer2.SerializeToString()},
                                ]
                            }
                        },
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Map
        assert type(metadata_type.key_type) is SqlType.Int64
        assert type(metadata_type.value_type) is SqlType.Proto

        # without proto definition
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")
        assert isinstance(result, dict)
        assert len(result) == 2
        assert result[1] == singer1.SerializeToString()
        assert result[2] == singer2.SerializeToString()

        # with proto definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "map_field",
            {
                "map_field.value": singer_pb2.Singer(),
            },
        )
        assert isinstance(result, dict)
        assert len(result) == 2
        assert result[1] == singer1
        assert result[2] == singer2

    def test__map_with_enums(self):
        _type = PBType(
            {
                "map_type": {
                    "key_type": int64_type(),
                    "value_type": enum_type(),
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 1},
                                    {"int_value": 0},  # POP
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [
                                    {"int_value": 2},
                                    {"int_value": 1},  # JAZZ
                                ]
                            }
                        },
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Map
        assert type(metadata_type.key_type) is SqlType.Int64
        assert type(metadata_type.value_type) is SqlType.Enum

        # without enum definition
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")
        assert isinstance(result, dict)
        assert len(result) == 2
        assert result[1] == 0
        assert result[2] == 1

        # with enum definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "map_field",
            {
                "map_field.value": singer_pb2.Genre,
            },
        )
        assert isinstance(result, dict)
        assert len(result) == 2
        assert result[1] == "POP"
        assert result[2] == "JAZZ"

    def test__map_of_maps_of_structs(self):
        _type = PBType(
            {
                "map_type": {
                    "key_type": int64_type(),
                    "value_type": {
                        "map_type": {
                            "key_type": {"string_type": {}},
                            "value_type": {
                                "struct_type": {
                                    "fields": [
                                        {
                                            "field_name": "field1",
                                            "type_": int64_type(),
                                        },
                                        {
                                            "field_name": "field2",
                                            "type_": {"string_type": {}},
                                        },
                                    ]
                                }
                            },
                        }
                    },
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [  # list of (int, map) tuples
                        {
                            "array_value": {
                                "values": [  # (int, map) tuple
                                    {"int_value": 1},
                                    {
                                        "array_value": {
                                            "values": [  # list of (str, struct) tuples
                                                {
                                                    "array_value": {
                                                        "values": [  # (str, struct) tuple
                                                            {"string_value": "1_1"},
                                                            {
                                                                "array_value": {
                                                                    "values": [
                                                                        {
                                                                            "int_value": 1
                                                                        },
                                                                        {
                                                                            "string_value": "test1"
                                                                        },
                                                                    ]
                                                                }
                                                            },
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (str, struct) tuple
                                                            {"string_value": "1_2"},
                                                            {
                                                                "array_value": {
                                                                    "values": [
                                                                        {
                                                                            "int_value": 2
                                                                        },
                                                                        {
                                                                            "string_value": "test2"
                                                                        },
                                                                    ]
                                                                }
                                                            },
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [  # (int, map) tuple
                                    {"int_value": 2},
                                    {
                                        "array_value": {
                                            "values": [  # list of (str, struct) tuples
                                                {
                                                    "array_value": {
                                                        "values": [  # (str, struct) tuple
                                                            {"string_value": "2_1"},
                                                            {
                                                                "array_value": {
                                                                    "values": [
                                                                        {
                                                                            "int_value": 3
                                                                        },
                                                                        {
                                                                            "string_value": "test3"
                                                                        },
                                                                    ]
                                                                }
                                                            },
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (str, struct) tuple
                                                            {"string_value": "2_2"},
                                                            {
                                                                "array_value": {
                                                                    "values": [
                                                                        {
                                                                            "int_value": 4
                                                                        },
                                                                        {
                                                                            "string_value": "test4"
                                                                        },
                                                                    ]
                                                                }
                                                            },
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                    ]
                }
            }
        )
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Map
        assert type(metadata_type.key_type) is SqlType.Int64
        assert type(metadata_type.value_type) is SqlType.Map
        assert type(metadata_type.value_type.key_type) is SqlType.String
        assert type(metadata_type.value_type.value_type) is SqlType.Struct
        assert type(metadata_type.value_type.value_type["field1"]) is SqlType.Int64
        assert type(metadata_type.value_type.value_type["field2"]) is SqlType.String
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")

        assert result[1]["1_1"]["field1"] == 1
        assert result[1]["1_1"]["field2"] == "test1"

        assert result[1]["1_2"]["field1"] == 2
        assert result[1]["1_2"]["field2"] == "test2"

        assert result[2]["2_1"]["field1"] == 3
        assert result[2]["2_1"]["field2"] == "test3"

        assert result[2]["2_2"]["field1"] == 4
        assert result[2]["2_2"]["field2"] == "test4"

    def test__map_of_maps_of_structs_with_proto_and_enum(self):
        singer1 = singer_pb2.Singer(name="John")
        singer2 = singer_pb2.Singer(name="Taylor")

        _type = PBType(
            {
                "map_type": {
                    "key_type": int64_type(),
                    "value_type": {
                        "map_type": {
                            "key_type": {"string_type": {}},
                            "value_type": {
                                "struct_type": {
                                    "fields": [
                                        {
                                            "field_name": "int_field",
                                            "type_": int64_type(),
                                        },
                                        {
                                            "field_name": "singer",
                                            "type_": proto_type(),
                                        },
                                        {
                                            "field_name": "genre",
                                            "type_": enum_type(),
                                        },
                                    ]
                                }
                            },
                        }
                    },
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [  # list of (int, map) tuples
                        {
                            "array_value": {
                                "values": [  # (int, map) tuples
                                    {"int_value": 1},
                                    {
                                        "array_value": {
                                            "values": [  # list of (str, struct) tuples
                                                {
                                                    "array_value": {
                                                        "values": [  # (str, struct) tuples
                                                            {"string_value": "1_1"},
                                                            {
                                                                "array_value": {
                                                                    "values": [
                                                                        {
                                                                            "int_value": 12
                                                                        },
                                                                        {
                                                                            "bytes_value": singer1.SerializeToString()
                                                                        },
                                                                        {
                                                                            "int_value": 0
                                                                        },
                                                                    ]
                                                                }
                                                            },
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (str, struct) tuples
                                                            {"string_value": "1_2"},
                                                            {
                                                                "array_value": {
                                                                    "values": [
                                                                        {
                                                                            "int_value": 34
                                                                        },
                                                                        {
                                                                            "bytes_value": singer2.SerializeToString()
                                                                        },
                                                                        {
                                                                            "int_value": 1
                                                                        },
                                                                    ]
                                                                }
                                                            },
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [  # (int, map) tuples
                                    {"int_value": 2},
                                    {
                                        "array_value": {
                                            "values": [  # list of (str, struct) tuples
                                                {
                                                    "array_value": {
                                                        "values": [  # (str, struct) tuples
                                                            {"string_value": "2_1"},
                                                            {
                                                                "array_value": {
                                                                    "values": [
                                                                        {
                                                                            "int_value": 56
                                                                        },
                                                                        {
                                                                            "bytes_value": singer1.SerializeToString()
                                                                        },
                                                                        {
                                                                            "int_value": 2
                                                                        },
                                                                    ]
                                                                }
                                                            },
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (str, struct) tuples
                                                            {"string_value": "2_2"},
                                                            {
                                                                "array_value": {
                                                                    "values": [
                                                                        {
                                                                            "int_value": 78
                                                                        },
                                                                        {
                                                                            "bytes_value": singer2.SerializeToString()
                                                                        },
                                                                        {
                                                                            "int_value": 3
                                                                        },
                                                                    ]
                                                                }
                                                            },
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                    ]
                }
            }
        )

        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Map
        assert type(metadata_type.key_type) is SqlType.Int64
        assert type(metadata_type.value_type) is SqlType.Map
        assert type(metadata_type.value_type.key_type) is SqlType.String
        assert type(metadata_type.value_type.value_type) is SqlType.Struct
        assert type(metadata_type.value_type.value_type["int_field"]) is SqlType.Int64
        assert type(metadata_type.value_type.value_type["singer"]) is SqlType.Proto
        assert type(metadata_type.value_type.value_type["genre"]) is SqlType.Enum

        # without proto definition
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")

        assert result[1]["1_1"]["int_field"] == 12
        assert result[1]["1_1"]["singer"] == singer1.SerializeToString()
        assert result[1]["1_1"]["genre"] == 0

        assert result[1]["1_2"]["int_field"] == 34
        assert result[1]["1_2"]["singer"] == singer2.SerializeToString()
        assert result[1]["1_2"]["genre"] == 1

        assert result[2]["2_1"]["int_field"] == 56
        assert result[2]["2_1"]["singer"] == singer1.SerializeToString()
        assert result[2]["2_1"]["genre"] == 2

        assert result[2]["2_2"]["int_field"] == 78
        assert result[2]["2_2"]["singer"] == singer2.SerializeToString()
        assert result[2]["2_2"]["genre"] == 3

        # with proto definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "map_field",
            {
                "map_field.value.value.singer": singer_pb2.Singer(),
                "map_field.value.value.genre": singer_pb2.Genre,
            },
        )

        assert result[1]["1_1"]["int_field"] == 12
        assert result[1]["1_1"]["singer"] == singer1
        assert result[1]["1_1"]["genre"] == "POP"

        assert result[1]["1_2"]["int_field"] == 34
        assert result[1]["1_2"]["singer"] == singer2
        assert result[1]["1_2"]["genre"] == "JAZZ"

        assert result[2]["2_1"]["int_field"] == 56
        assert result[2]["2_1"]["singer"] == singer1
        assert result[2]["2_1"]["genre"] == "FOLK"

        assert result[2]["2_2"]["int_field"] == 78
        assert result[2]["2_2"]["singer"] == singer2
        assert result[2]["2_2"]["genre"] == "ROCK"

    def test__map_of_lists_of_structs(self):
        _type = PBType(
            {
                "map_type": {
                    "key_type": TYPE_BYTES,
                    "value_type": {
                        "array_type": {
                            "element_type": {
                                "struct_type": {
                                    "fields": [
                                        {
                                            "field_name": "timestamp",
                                            "type_": TYPE_TIMESTAMP,
                                        },
                                        {
                                            "field_name": "value",
                                            "type_": TYPE_BYTES,
                                        },
                                    ]
                                }
                            },
                        }
                    },
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [  # list of (byte, list) tuples
                        {
                            "array_value": {
                                "values": [  # (byte, list) tuple
                                    {"bytes_value": b"key1"},
                                    {
                                        "array_value": {
                                            "values": [  # list of structs
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 1111111111
                                                                }
                                                            },
                                                            {
                                                                "bytes_value": b"key1-value1"
                                                            },
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 2222222222
                                                                }
                                                            },
                                                            {
                                                                "bytes_value": b"key1-value2"
                                                            },
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [  # (byte, list) tuple
                                    {"bytes_value": b"key2"},
                                    {
                                        "array_value": {
                                            "values": [  # list of structs
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 3333333333
                                                                }
                                                            },
                                                            {
                                                                "bytes_value": b"key2-value1"
                                                            },
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 4444444444
                                                                }
                                                            },
                                                            {
                                                                "bytes_value": b"key2-value2"
                                                            },
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                    ]
                }
            }
        )
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Map
        assert type(metadata_type.key_type) is SqlType.Bytes
        assert type(metadata_type.value_type) is SqlType.Array
        assert type(metadata_type.value_type.element_type) is SqlType.Struct
        assert (
            type(metadata_type.value_type.element_type["timestamp"])
            is SqlType.Timestamp
        )
        assert type(metadata_type.value_type.element_type["value"]) is SqlType.Bytes
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")

        timestamp1 = DatetimeWithNanoseconds(
            2005, 3, 18, 1, 58, 31, tzinfo=datetime.timezone.utc
        )
        timestamp2 = DatetimeWithNanoseconds(
            2040, 6, 2, 3, 57, 2, tzinfo=datetime.timezone.utc
        )
        timestamp3 = DatetimeWithNanoseconds(
            2075, 8, 18, 5, 55, 33, tzinfo=datetime.timezone.utc
        )
        timestamp4 = DatetimeWithNanoseconds(
            2110, 11, 3, 7, 54, 4, tzinfo=datetime.timezone.utc
        )

        assert result[b"key1"][0]["timestamp"] == timestamp1
        assert result[b"key1"][0]["value"] == b"key1-value1"
        assert result[b"key1"][1]["timestamp"] == timestamp2
        assert result[b"key1"][1]["value"] == b"key1-value2"
        assert result[b"key2"][0]["timestamp"] == timestamp3
        assert result[b"key2"][0]["value"] == b"key2-value1"
        assert result[b"key2"][1]["timestamp"] == timestamp4
        assert result[b"key2"][1]["value"] == b"key2-value2"

    def test__map_of_lists_of_structs_with_protos(self):
        singer1 = singer_pb2.Singer(name="John")
        singer2 = singer_pb2.Singer(name="Taylor")
        singer3 = singer_pb2.Singer(name="Jay")
        singer4 = singer_pb2.Singer(name="Eric")

        _type = PBType(
            {
                "map_type": {
                    "key_type": TYPE_BYTES,
                    "value_type": {
                        "array_type": {
                            "element_type": {
                                "struct_type": {
                                    "fields": [
                                        {
                                            "field_name": "timestamp",
                                            "type_": TYPE_TIMESTAMP,
                                        },
                                        {
                                            "field_name": "value",
                                            "type_": proto_type(),
                                        },
                                    ]
                                }
                            },
                        }
                    },
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [  # list of (byte, list) tuples
                        {
                            "array_value": {
                                "values": [  # (byte, list) tuple
                                    {"bytes_value": b"key1"},
                                    {
                                        "array_value": {
                                            "values": [  # list of structs
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 1111111111
                                                                }
                                                            },
                                                            {
                                                                "bytes_value": singer1.SerializeToString()
                                                            },
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 2222222222
                                                                }
                                                            },
                                                            {
                                                                "bytes_value": singer2.SerializeToString()
                                                            },
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [  # (byte, list) tuple
                                    {"bytes_value": b"key2"},
                                    {
                                        "array_value": {
                                            "values": [  # list of structs
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 3333333333
                                                                }
                                                            },
                                                            {
                                                                "bytes_value": singer3.SerializeToString()
                                                            },
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 4444444444
                                                                }
                                                            },
                                                            {
                                                                "bytes_value": singer4.SerializeToString()
                                                            },
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                    ]
                }
            }
        )
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Map
        assert type(metadata_type.key_type) is SqlType.Bytes
        assert type(metadata_type.value_type) is SqlType.Array
        assert type(metadata_type.value_type.element_type) is SqlType.Struct
        assert (
            type(metadata_type.value_type.element_type["timestamp"])
            is SqlType.Timestamp
        )
        assert type(metadata_type.value_type.element_type["value"]) is SqlType.Proto

        timestamp1 = DatetimeWithNanoseconds(
            2005, 3, 18, 1, 58, 31, tzinfo=datetime.timezone.utc
        )
        timestamp2 = DatetimeWithNanoseconds(
            2040, 6, 2, 3, 57, 2, tzinfo=datetime.timezone.utc
        )
        timestamp3 = DatetimeWithNanoseconds(
            2075, 8, 18, 5, 55, 33, tzinfo=datetime.timezone.utc
        )
        timestamp4 = DatetimeWithNanoseconds(
            2110, 11, 3, 7, 54, 4, tzinfo=datetime.timezone.utc
        )

        # without proto definition
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")
        assert result[b"key1"][0]["timestamp"] == timestamp1
        assert result[b"key1"][0]["value"] == singer1.SerializeToString()
        assert result[b"key1"][1]["timestamp"] == timestamp2
        assert result[b"key1"][1]["value"] == singer2.SerializeToString()
        assert result[b"key2"][0]["timestamp"] == timestamp3
        assert result[b"key2"][0]["value"] == singer3.SerializeToString()
        assert result[b"key2"][1]["timestamp"] == timestamp4
        assert result[b"key2"][1]["value"] == singer4.SerializeToString()

        # with proto definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "map_field",
            {
                "map_field.value.value": singer_pb2.Singer(),
            },
        )
        assert result[b"key1"][0]["timestamp"] == timestamp1
        assert result[b"key1"][0]["value"] == singer1
        assert result[b"key1"][1]["timestamp"] == timestamp2
        assert result[b"key1"][1]["value"] == singer2
        assert result[b"key2"][0]["timestamp"] == timestamp3
        assert result[b"key2"][0]["value"] == singer3
        assert result[b"key2"][1]["timestamp"] == timestamp4
        assert result[b"key2"][1]["value"] == singer4

    def test__map_of_lists_of_structs_with_enums(self):
        _type = PBType(
            {
                "map_type": {
                    "key_type": TYPE_BYTES,
                    "value_type": {
                        "array_type": {
                            "element_type": {
                                "struct_type": {
                                    "fields": [
                                        {
                                            "field_name": "timestamp",
                                            "type_": TYPE_TIMESTAMP,
                                        },
                                        {
                                            "field_name": "value",
                                            "type_": enum_type(),
                                        },
                                    ]
                                }
                            },
                        }
                    },
                }
            }
        )
        value = PBValue(
            {
                "array_value": {
                    "values": [  # list of (byte, list) tuples
                        {
                            "array_value": {
                                "values": [  # (byte, list) tuple
                                    {"bytes_value": b"key1"},
                                    {
                                        "array_value": {
                                            "values": [  # list of structs
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 1111111111
                                                                }
                                                            },
                                                            {"int_value": 0},
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 2222222222
                                                                }
                                                            },
                                                            {"int_value": 1},
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                        {
                            "array_value": {
                                "values": [  # (byte, list) tuple
                                    {"bytes_value": b"key2"},
                                    {
                                        "array_value": {
                                            "values": [  # list of structs
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 3333333333
                                                                }
                                                            },
                                                            {"int_value": 2},
                                                        ]
                                                    }
                                                },
                                                {
                                                    "array_value": {
                                                        "values": [  # (timestamp, bytes) tuple
                                                            {
                                                                "timestamp_value": {
                                                                    "seconds": 4444444444
                                                                }
                                                            },
                                                            {"int_value": 3},
                                                        ]
                                                    }
                                                },
                                            ]
                                        }
                                    },
                                ]
                            }
                        },
                    ]
                }
            }
        )
        metadata_type = _pb_type_to_metadata_type(_type)
        assert type(metadata_type) is SqlType.Map
        assert type(metadata_type.key_type) is SqlType.Bytes
        assert type(metadata_type.value_type) is SqlType.Array
        assert type(metadata_type.value_type.element_type) is SqlType.Struct
        assert (
            type(metadata_type.value_type.element_type["timestamp"])
            is SqlType.Timestamp
        )
        assert type(metadata_type.value_type.element_type["value"]) is SqlType.Enum

        timestamp1 = DatetimeWithNanoseconds(
            2005, 3, 18, 1, 58, 31, tzinfo=datetime.timezone.utc
        )
        timestamp2 = DatetimeWithNanoseconds(
            2040, 6, 2, 3, 57, 2, tzinfo=datetime.timezone.utc
        )
        timestamp3 = DatetimeWithNanoseconds(
            2075, 8, 18, 5, 55, 33, tzinfo=datetime.timezone.utc
        )
        timestamp4 = DatetimeWithNanoseconds(
            2110, 11, 3, 7, 54, 4, tzinfo=datetime.timezone.utc
        )

        # without enum definition
        result = _parse_pb_value_to_python_value(value._pb, metadata_type, "map_field")
        assert result[b"key1"][0]["timestamp"] == timestamp1
        assert result[b"key1"][0]["value"] == 0
        assert result[b"key1"][1]["timestamp"] == timestamp2
        assert result[b"key1"][1]["value"] == 1
        assert result[b"key2"][0]["timestamp"] == timestamp3
        assert result[b"key2"][0]["value"] == 2
        assert result[b"key2"][1]["timestamp"] == timestamp4
        assert result[b"key2"][1]["value"] == 3

        # with enum definition
        result = _parse_pb_value_to_python_value(
            value._pb,
            metadata_type,
            "map_field",
            {
                "map_field.value.value": singer_pb2.Genre,
            },
        )
        assert result[b"key1"][0]["timestamp"] == timestamp1
        assert result[b"key1"][0]["value"] == "POP"
        assert result[b"key1"][1]["timestamp"] == timestamp2
        assert result[b"key1"][1]["value"] == "JAZZ"
        assert result[b"key2"][0]["timestamp"] == timestamp3
        assert result[b"key2"][0]["value"] == "FOLK"
        assert result[b"key2"][1]["timestamp"] == timestamp4
        assert result[b"key2"][1]["value"] == "ROCK"

    def test__invalid_type_throws_exception(self):
        _type = PBType({"string_type": {}})
        value = PBValue({"int_value": 1})
        metadata_type = _pb_type_to_metadata_type(_type)

        with pytest.raises(
            ValueError,
            match="string_value field for String type not found in a Value.",
        ):
            _parse_pb_value_to_python_value(value._pb, metadata_type, "string_field")
