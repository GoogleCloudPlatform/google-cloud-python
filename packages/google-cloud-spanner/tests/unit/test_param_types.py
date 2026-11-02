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


import unittest


class Test_ArrayParamType(unittest.TestCase):
    def test_it(self):
        from google.cloud.spanner_v1 import Type, TypeCode, param_types

        expected = Type(
            code=TypeCode.ARRAY, array_element_type=Type(code=TypeCode.INT64)
        )

        found = param_types.Array(param_types.INT64)

        self.assertEqual(found, expected)


class Test_Struct(unittest.TestCase):
    def test_it(self):
        from google.cloud.spanner_v1 import StructType, Type, TypeCode, param_types

        struct_type = StructType(
            fields=[
                StructType.Field(name="name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="count", type_=Type(code=TypeCode.INT64)),
                StructType.Field(name="float32", type_=Type(code=TypeCode.FLOAT32)),
            ]
        )
        expected = Type(code=TypeCode.STRUCT, struct_type=struct_type)

        found = param_types.Struct(
            [
                param_types.StructField("name", param_types.STRING),
                param_types.StructField("count", param_types.INT64),
                param_types.StructField("float32", param_types.FLOAT32),
            ]
        )

        self.assertEqual(found, expected)


class Test_JsonbParamType(unittest.TestCase):
    def test_it(self):
        from google.cloud.spanner_v1 import (
            Type,
            TypeAnnotationCode,
            TypeCode,
            param_types,
        )

        expected = Type(
            code=TypeCode.JSON,
            type_annotation=TypeAnnotationCode(TypeAnnotationCode.PG_JSONB),
        )

        found = param_types.PG_JSONB

        self.assertEqual(found, expected)


class Test_OidParamType(unittest.TestCase):
    def test_it(self):
        from google.cloud.spanner_v1 import (
            Type,
            TypeAnnotationCode,
            TypeCode,
            param_types,
        )

        expected = Type(
            code=TypeCode.INT64,
            type_annotation=TypeAnnotationCode.PG_OID,
        )

        found = param_types.PG_OID

        self.assertEqual(found, expected)


class Test_ProtoMessageParamType(unittest.TestCase):
    def test_it(self):
        from google.cloud.spanner_v1 import Type, TypeCode, param_types

        from .testdata import singer_pb2

        singer_info = singer_pb2.SingerInfo()
        expected = Type(
            code=TypeCode.PROTO, proto_type_fqn=singer_info.DESCRIPTOR.full_name
        )

        found = param_types.ProtoMessage(singer_info)

        self.assertEqual(found, expected)


class Test_ProtoEnumParamType(unittest.TestCase):
    def test_it(self):
        from google.cloud.spanner_v1 import Type, TypeCode, param_types

        from .testdata import singer_pb2

        singer_genre = singer_pb2.Genre
        expected = Type(
            code=TypeCode.ENUM, proto_type_fqn=singer_genre.DESCRIPTOR.full_name
        )

        found = param_types.ProtoEnum(singer_genre)

        self.assertEqual(found, expected)
