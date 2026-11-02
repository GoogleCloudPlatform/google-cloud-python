# Copyright 2015 Google LLC
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

import copy
import unittest
from unittest import mock

import pytest

from google.cloud import bigquery
from google.cloud.bigquery import enums, schema
from google.cloud.bigquery.schema import DataPolicy, PolicyTagList
from google.cloud.bigquery.standard_sql import StandardSqlStructType


class TestSchemaField(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.schema import SchemaField

        return SchemaField

    @staticmethod
    def _get_standard_sql_data_type_class():
        from google.cloud.bigquery import standard_sql

        return standard_sql.StandardSqlDataType

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_constructor_defaults(self):
        field = self._make_one("test", "STRING")
        self.assertEqual(field.name, "test")
        self.assertEqual(field.field_type, "STRING")
        self.assertEqual(field.mode, "NULLABLE")
        self.assertIsNone(field.description)
        self.assertEqual(field.fields, ())
        self.assertIsNone(field.policy_tags)
        self.assertIsNone(field.data_policies)
        self.assertIsNone(field.default_value_expression)
        self.assertEqual(field.rounding_mode, None)
        self.assertEqual(field.foreign_type_definition, None)
        self.assertEqual(
            field.timestamp_precision, enums.TimestampPrecision.MICROSECOND
        )

    def test_constructor_explicit(self):
        FIELD_DEFAULT_VALUE_EXPRESSION = "This is the default value for this field"
        field = self._make_one(
            "test",
            "STRING",
            mode="REQUIRED",
            description="Testing",
            policy_tags=PolicyTagList(
                names=(
                    "projects/a/locations/b/taxonomies/c/policyTags/e",
                    "projects/f/locations/g/taxonomies/h/policyTags/i",
                )
            ),
            default_value_expression=FIELD_DEFAULT_VALUE_EXPRESSION,
            rounding_mode=enums.RoundingMode.ROUNDING_MODE_UNSPECIFIED,
            foreign_type_definition="INTEGER",
            timestamp_precision=enums.TimestampPrecision.PICOSECOND,
        )
        self.assertEqual(field.name, "test")
        self.assertEqual(field.field_type, "STRING")
        self.assertEqual(field.mode, "REQUIRED")
        self.assertEqual(field.default_value_expression, FIELD_DEFAULT_VALUE_EXPRESSION)
        self.assertEqual(field.description, "Testing")
        self.assertEqual(field.fields, ())
        self.assertEqual(
            field.policy_tags,
            PolicyTagList(
                names=(
                    "projects/a/locations/b/taxonomies/c/policyTags/e",
                    "projects/f/locations/g/taxonomies/h/policyTags/i",
                )
            ),
        )
        self.assertEqual(field.rounding_mode, "ROUNDING_MODE_UNSPECIFIED")
        self.assertEqual(field.foreign_type_definition, "INTEGER")
        self.assertEqual(
            field.timestamp_precision,
            enums.TimestampPrecision.PICOSECOND,
        )

    def test_constructor_explicit_none(self):
        field = self._make_one("test", "STRING", description=None, policy_tags=None)
        self.assertIsNone(field.description)
        self.assertIsNone(field.policy_tags)
        self.assertIsNone(field.data_policies)

    def test_constructor_subfields(self):
        sub_field1 = self._make_one("area_code", "STRING")
        sub_field2 = self._make_one("local_number", "STRING")
        field = self._make_one(
            "phone_number", "RECORD", fields=[sub_field1, sub_field2]
        )
        self.assertEqual(field.name, "phone_number")
        self.assertEqual(field.field_type, "RECORD")
        self.assertEqual(field.mode, "NULLABLE")
        self.assertIsNone(field.description)
        self.assertEqual(len(field.fields), 2)
        self.assertEqual(field.fields[0], sub_field1)
        self.assertEqual(field.fields[1], sub_field2)

    def test_constructor_range(self):
        from google.cloud.bigquery.schema import FieldElementType

        field = self._make_one(
            "test",
            "RANGE",
            mode="REQUIRED",
            description="Testing",
            range_element_type=FieldElementType("DATETIME"),
        )
        self.assertEqual(field.name, "test")
        self.assertEqual(field.field_type, "RANGE")
        self.assertEqual(field.mode, "REQUIRED")
        self.assertEqual(field.description, "Testing")
        self.assertEqual(field.range_element_type.element_type, "DATETIME")

    def test_constructor_range_str(self):
        field = self._make_one(
            "test",
            "RANGE",
            mode="REQUIRED",
            description="Testing",
            range_element_type="DATETIME",
        )
        self.assertEqual(field.name, "test")
        self.assertEqual(field.field_type, "RANGE")
        self.assertEqual(field.mode, "REQUIRED")
        self.assertEqual(field.description, "Testing")
        self.assertEqual(field.range_element_type.element_type, "DATETIME")

    def test_to_api_repr(self):
        policy = PolicyTagList(names=("foo", "bar"))
        self.assertEqual(
            policy.to_api_repr(),
            {"names": ["foo", "bar"]},
        )

        ROUNDINGMODE = enums.RoundingMode.ROUNDING_MODE_UNSPECIFIED

        field = self._make_one(
            "foo",
            "INTEGER",
            "NULLABLE",
            description="hello world",
            policy_tags=policy,
            rounding_mode=ROUNDINGMODE,
            foreign_type_definition=None,
        )
        self.assertEqual(
            field.to_api_repr(),
            {
                "mode": "NULLABLE",
                "name": "foo",
                "type": "INTEGER",
                "description": "hello world",
                "policyTags": {"names": ["foo", "bar"]},
                "roundingMode": "ROUNDING_MODE_UNSPECIFIED",
            },
        )

    def test_to_api_repr_omits_unset_properties(self):
        # Prevent accidentally modifying fields that aren't explicitly set.
        # https://github.com/googleapis/python-bigquery/issues/981
        field = self._make_one("foo", "INTEGER")
        resource = field.to_api_repr()
        self.assertNotIn("description", resource)
        self.assertNotIn("policyTags", resource)
        self.assertNotIn("dataPolicies", resource)

    def test_to_api_repr_with_subfield(self):
        for record_type in ("RECORD", "STRUCT"):
            subfield = self._make_one("bar", "INTEGER", "NULLABLE")
            field = self._make_one("foo", record_type, "REQUIRED", fields=(subfield,))
            self.assertEqual(
                field.to_api_repr(),
                {
                    "fields": [{"mode": "NULLABLE", "name": "bar", "type": "INTEGER"}],
                    "mode": "REQUIRED",
                    "name": "foo",
                    "type": record_type,
                },
            )

    def test_to_api_repr_w_timestamp_precision(self):
        field = self._make_one(
            "foo",
            "TIMESTAMP",
            "NULLABLE",
            timestamp_precision=enums.TimestampPrecision.PICOSECOND,
        )
        self.assertEqual(
            field.to_api_repr(),
            {
                "mode": "NULLABLE",
                "name": "foo",
                "type": "TIMESTAMP",
                "timestampPrecision": 12,
            },
        )

    def test_from_api_repr(self):
        field = self._get_target_class().from_api_repr(
            {
                "fields": [{"mode": "nullable", "name": "bar", "type": "integer"}],
                "mode": "required",
                "description": "test_description",
                "name": "foo",
                "type": "record",
                "roundingMode": "ROUNDING_MODE_UNSPECIFIED",
                "timestampPrecision": 12,
            }
        )
        self.assertEqual(field.name, "foo")
        self.assertEqual(field.field_type, "RECORD")
        self.assertEqual(field.mode, "REQUIRED")
        self.assertEqual(field.description, "test_description")
        self.assertEqual(len(field.fields), 1)
        self.assertEqual(field.fields[0].name, "bar")
        self.assertEqual(field.fields[0].field_type, "INTEGER")
        self.assertEqual(field.fields[0].mode, "NULLABLE")
        self.assertEqual(field.range_element_type, None)
        self.assertEqual(field.rounding_mode, "ROUNDING_MODE_UNSPECIFIED")
        self.assertEqual(
            field.timestamp_precision,
            enums.TimestampPrecision.PICOSECOND,
        )

    def test_from_api_repr_policy(self):
        field = self._get_target_class().from_api_repr(
            {
                "fields": [{"mode": "nullable", "name": "bar", "type": "integer"}],
                "name": "foo",
                "type": "record",
                "policyTags": {"names": ["one", "two"]},
            }
        )
        self.assertEqual(field.name, "foo")
        self.assertEqual(field.field_type, "RECORD")
        self.assertEqual(field.policy_tags.names, ("one", "two"))
        self.assertEqual(len(field.fields), 1)
        self.assertEqual(field.fields[0].name, "bar")
        self.assertEqual(field.fields[0].field_type, "INTEGER")
        self.assertEqual(field.fields[0].mode, "NULLABLE")

    def test_from_api_repr_range(self):
        field = self._get_target_class().from_api_repr(
            {
                "mode": "nullable",
                "description": "test_range",
                "name": "foo",
                "type": "range",
                "rangeElementType": {"type": "DATETIME"},
            }
        )
        self.assertEqual(field.name, "foo")
        self.assertEqual(field.field_type, "RANGE")
        self.assertEqual(field.mode, "NULLABLE")
        self.assertEqual(field.description, "test_range")
        self.assertEqual(len(field.fields), 0)
        self.assertEqual(field.range_element_type.element_type, "DATETIME")

    def test_from_api_repr_defaults(self):
        field = self._get_target_class().from_api_repr(
            {"name": "foo", "type": "record"}
        )
        self.assertEqual(field.name, "foo")
        self.assertEqual(field.field_type, "RECORD")
        self.assertEqual(field.mode, "NULLABLE")
        self.assertEqual(len(field.fields), 0)
        self.assertEqual(field.default_value_expression, None)

        # Keys not present in API representation shouldn't be included in
        # _properties.
        self.assertIsNone(field.description)
        self.assertIsNone(field.policy_tags)
        self.assertIsNone(field.data_policies)
        self.assertIsNone(field.range_element_type)
        self.assertNotIn("description", field._properties)
        self.assertNotIn("policyTags", field._properties)
        self.assertNotIn("dataPolicies", field._properties)
        self.assertNotIn("rangeElementType", field._properties)

    def test_from_api_repr_timestamp_precision_str(self):
        # The backend would return timestampPrecision field as a string, even
        # if we send over an integer. This test verifies we manually converted
        # it into integer to ensure resending could succeed.
        field = self._get_target_class().from_api_repr(
            {
                "timestampPrecision": "12",
            }
        )
        self.assertEqual(field._properties["timestampPrecision"], 12)

    def test_name_property(self):
        name = "lemon-ness"
        schema_field = self._make_one(name, "INTEGER")
        self.assertEqual(schema_field.name, name)

    def test_field_type_property(self):
        field_type = "BOOLEAN"
        schema_field = self._make_one("whether", field_type)
        self.assertEqual(schema_field.field_type, field_type)

    def test_mode_property(self):
        mode = "REPEATED"
        schema_field = self._make_one("again", "FLOAT", mode=mode)
        self.assertEqual(schema_field.mode, mode)

    def test_is_nullable(self):
        mode = "NULLABLE"
        schema_field = self._make_one("test", "FLOAT", mode=mode)
        self.assertTrue(schema_field.is_nullable)

    def test_is_not_nullable(self):
        mode = "REPEATED"
        schema_field = self._make_one("test", "FLOAT", mode=mode)
        self.assertFalse(schema_field.is_nullable)

    def test_description_property(self):
        description = "It holds some data."
        schema_field = self._make_one("do", "TIMESTAMP", description=description)
        self.assertEqual(schema_field.description, description)

    def test_fields_property(self):
        sub_field1 = self._make_one("one", "STRING")
        sub_field2 = self._make_one("fish", "INTEGER")
        fields = (sub_field1, sub_field2)
        schema_field = self._make_one("boat", "RECORD", fields=fields)
        self.assertEqual(schema_field.fields, fields)

    def test_roundingmode_property_str(self):
        ROUNDINGMODE = "ROUND_HALF_AWAY_FROM_ZERO"
        schema_field = self._make_one("test", "STRING", rounding_mode=ROUNDINGMODE)
        self.assertEqual(schema_field.rounding_mode, ROUNDINGMODE)

        del schema_field
        schema_field = self._make_one("test", "STRING")
        schema_field._properties["roundingMode"] = ROUNDINGMODE
        self.assertEqual(schema_field.rounding_mode, ROUNDINGMODE)

    def test_foreign_type_definition_property_str(self):
        FOREIGN_TYPE_DEFINITION = "INTEGER"
        schema_field = self._make_one(
            "test", "STRING", foreign_type_definition=FOREIGN_TYPE_DEFINITION
        )
        self.assertEqual(schema_field.foreign_type_definition, FOREIGN_TYPE_DEFINITION)

        del schema_field
        schema_field = self._make_one("test", "STRING")
        schema_field._properties["foreignTypeDefinition"] = FOREIGN_TYPE_DEFINITION
        self.assertEqual(schema_field.foreign_type_definition, FOREIGN_TYPE_DEFINITION)

    def test_timestamp_precision_unsupported_type(self):
        with pytest.raises(ValueError) as e:
            self._make_one("test", "TIMESTAMP", timestamp_precision=12)

        assert "timestamp_precision must be class enums.TimestampPrecision" in str(
            e.value
        )

    def test_timestamp_precision_property(self):
        TIMESTAMP_PRECISION = enums.TimestampPrecision.PICOSECOND
        schema_field = self._make_one("test", "TIMESTAMP")
        schema_field._properties[
            "timestampPrecision"
        ] = enums.TimestampPrecision.PICOSECOND.value
        self.assertEqual(schema_field.timestamp_precision, TIMESTAMP_PRECISION)

    def test_to_standard_sql_simple_type(self):
        examples = (
            # a few legacy types
            ("INTEGER", bigquery.StandardSqlTypeNames.INT64),
            ("FLOAT", bigquery.StandardSqlTypeNames.FLOAT64),
            ("BOOLEAN", bigquery.StandardSqlTypeNames.BOOL),
            ("DATETIME", bigquery.StandardSqlTypeNames.DATETIME),
            # a few standard types
            ("INT64", bigquery.StandardSqlTypeNames.INT64),
            ("FLOAT64", bigquery.StandardSqlTypeNames.FLOAT64),
            ("BOOL", bigquery.StandardSqlTypeNames.BOOL),
            ("GEOGRAPHY", bigquery.StandardSqlTypeNames.GEOGRAPHY),
        )
        for legacy_type, standard_type in examples:
            field = self._make_one("some_field", legacy_type)
            standard_field = field.to_standard_sql()
            self.assertEqual(standard_field.name, "some_field")
            self.assertEqual(standard_field.type.type_kind, standard_type)

    def test_to_standard_sql_struct_type(self):
        from google.cloud.bigquery import standard_sql

        # Expected result object:
        #
        # name: "image_usage"
        # type {
        #     type_kind: STRUCT
        #     struct_type {
        #         fields {
        #             name: "image_content"
        #             type {type_kind: BYTES}
        #         }
        #         fields {
        #             name: "last_used"
        #             type {
        #                 type_kind: STRUCT
        #                 struct_type {
        #                     fields {
        #                         name: "date_field"
        #                         type {type_kind: DATE}
        #                     }
        #                     fields {
        #                         name: "time_field"
        #                         type {type_kind: TIME}
        #                     }
        #                 }
        #             }
        #         }
        #     }
        # }

        sql_type = self._get_standard_sql_data_type_class()

        # level 2 fields
        sub_sub_field_date = standard_sql.StandardSqlField(
            name="date_field",
            type=sql_type(type_kind=bigquery.StandardSqlTypeNames.DATE),
        )
        sub_sub_field_time = standard_sql.StandardSqlField(
            name="time_field",
            type=sql_type(type_kind=bigquery.StandardSqlTypeNames.TIME),
        )

        # level 1 fields
        sub_field_struct = standard_sql.StandardSqlField(
            name="last_used",
            type=sql_type(
                type_kind=bigquery.StandardSqlTypeNames.STRUCT,
                struct_type=standard_sql.StandardSqlStructType(
                    fields=[sub_sub_field_date, sub_sub_field_time]
                ),
            ),
        )
        sub_field_bytes = standard_sql.StandardSqlField(
            name="image_content",
            type=sql_type(type_kind=bigquery.StandardSqlTypeNames.BYTES),
        )

        # level 0 (top level)
        expected_result = standard_sql.StandardSqlField(
            name="image_usage",
            type=sql_type(
                type_kind=bigquery.StandardSqlTypeNames.STRUCT,
                struct_type=standard_sql.StandardSqlStructType(
                    fields=[sub_field_bytes, sub_field_struct]
                ),
            ),
        )

        # construct legacy SchemaField object
        sub_sub_field1 = self._make_one("date_field", "DATE")
        sub_sub_field2 = self._make_one("time_field", "TIME")
        sub_field_record = self._make_one(
            "last_used", "RECORD", fields=(sub_sub_field1, sub_sub_field2)
        )
        sub_field_bytes = self._make_one("image_content", "BYTES")

        for type_name in ("RECORD", "STRUCT"):
            schema_field = self._make_one(
                "image_usage", type_name, fields=(sub_field_bytes, sub_field_record)
            )
            standard_field = schema_field.to_standard_sql()
            self.assertEqual(standard_field, expected_result)

    def test_to_standard_sql_array_type_simple(self):
        from google.cloud.bigquery import standard_sql

        sql_type = self._get_standard_sql_data_type_class()

        # construct expected result object
        expected_sql_type = sql_type(
            type_kind=bigquery.StandardSqlTypeNames.ARRAY,
            array_element_type=sql_type(type_kind=bigquery.StandardSqlTypeNames.INT64),
        )
        expected_result = standard_sql.StandardSqlField(
            name="valid_numbers", type=expected_sql_type
        )

        # construct "repeated" SchemaField object and convert to standard SQL
        schema_field = self._make_one("valid_numbers", "INT64", mode="REPEATED")
        standard_field = schema_field.to_standard_sql()

        self.assertEqual(standard_field, expected_result)

    def test_to_standard_sql_array_type_struct(self):
        from google.cloud.bigquery import standard_sql

        sql_type = self._get_standard_sql_data_type_class()

        # define person STRUCT
        name_field = standard_sql.StandardSqlField(
            name="name", type=sql_type(type_kind=bigquery.StandardSqlTypeNames.STRING)
        )
        age_field = standard_sql.StandardSqlField(
            name="age", type=sql_type(type_kind=bigquery.StandardSqlTypeNames.INT64)
        )
        person_struct = standard_sql.StandardSqlField(
            name="person_info",
            type=sql_type(
                type_kind=bigquery.StandardSqlTypeNames.STRUCT,
                struct_type=StandardSqlStructType(fields=[name_field, age_field]),
            ),
        )

        # define expected result - an ARRAY of person structs
        expected_sql_type = sql_type(
            type_kind=bigquery.StandardSqlTypeNames.ARRAY,
            array_element_type=person_struct.type,
        )
        expected_result = standard_sql.StandardSqlField(
            name="known_people", type=expected_sql_type
        )

        # construct legacy repeated SchemaField object
        sub_field1 = self._make_one("name", "STRING")
        sub_field2 = self._make_one("age", "INTEGER")
        schema_field = self._make_one(
            "known_people", "RECORD", fields=(sub_field1, sub_field2), mode="REPEATED"
        )

        standard_field = schema_field.to_standard_sql()
        self.assertEqual(standard_field, expected_result)

    def test_to_standard_sql_unknown_type(self):
        field = self._make_one("weird_field", "TROOLEAN")

        standard_field = field.to_standard_sql()

        self.assertEqual(standard_field.name, "weird_field")
        self.assertEqual(
            standard_field.type.type_kind,
            bigquery.StandardSqlTypeNames.TYPE_KIND_UNSPECIFIED,
        )

    def test_to_standard_sql_foreign_type_valid(self):
        legacy_type = "FOREIGN"
        standard_type = bigquery.StandardSqlTypeNames.FOREIGN
        foreign_type_definition = "INTEGER"

        field = self._make_one(
            "some_field",
            field_type=legacy_type,
            foreign_type_definition=foreign_type_definition,
        )
        standard_field = field.to_standard_sql()
        self.assertEqual(standard_field.name, "some_field")
        self.assertEqual(standard_field.type.type_kind, standard_type)

    def test___eq___wrong_type(self):
        field = self._make_one("test", "STRING")
        other = object()
        self.assertNotEqual(field, other)
        self.assertEqual(field, mock.ANY)

    def test___eq___name_mismatch(self):
        field = self._make_one("test", "STRING")
        other = self._make_one("other", "STRING")
        self.assertNotEqual(field, other)

    def test___eq___field_type_mismatch(self):
        field = self._make_one("test", "STRING")
        other = self._make_one("test", "INTEGER")
        self.assertNotEqual(field, other)

    def test___eq___mode_mismatch(self):
        field = self._make_one("test", "STRING", mode="REQUIRED")
        other = self._make_one("test", "STRING", mode="NULLABLE")
        self.assertNotEqual(field, other)

    def test___eq___description_mismatch(self):
        field = self._make_one("test", "STRING", description="Testing")
        other = self._make_one("test", "STRING", description="Other")
        self.assertNotEqual(field, other)

    def test___eq___fields_mismatch(self):
        sub1 = self._make_one("sub1", "STRING")
        sub2 = self._make_one("sub2", "STRING")
        field = self._make_one("test", "RECORD", fields=[sub1])
        other = self._make_one("test", "RECORD", fields=[sub2])
        self.assertNotEqual(field, other)

    def test___eq___hit(self):
        field = self._make_one("test", "STRING", mode="REQUIRED", description="Testing")
        other = self._make_one("test", "STRING", mode="REQUIRED", description="Testing")
        self.assertEqual(field, other)

    def test___eq___hit_case_diff_on_type(self):
        field = self._make_one("test", "STRING", mode="REQUIRED", description="Testing")
        other = self._make_one("test", "string", mode="REQUIRED", description="Testing")
        self.assertEqual(field, other)

    def test___eq___hit_w_fields(self):
        sub1 = self._make_one("sub1", "STRING")
        sub2 = self._make_one("sub2", "STRING")
        field = self._make_one("test", "RECORD", fields=[sub1, sub2])
        other = self._make_one("test", "RECORD", fields=[sub1, sub2])
        self.assertEqual(field, other)

    def test___eq___hit_w_policy_tags(self):
        field = self._make_one(
            "test",
            "STRING",
            mode="REQUIRED",
            description="Testing",
            policy_tags=PolicyTagList(names=["foo", "bar"]),
        )
        other = self._make_one(
            "test",
            "STRING",
            mode="REQUIRED",
            description="Testing",
            policy_tags=PolicyTagList(names=["bar", "foo"]),
        )
        self.assertEqual(field, other)  # Policy tags order does not matter.

    def test___eq___range_element_type_mismatch(self):
        field = self._make_one("R", "RANGE", range_element_type="DATE")
        other = self._make_one("R", "RANGE", range_element_type="DATETIME")
        self.assertNotEqual(field, other)

    def test___eq___range_element_type_hit(self):
        field = self._make_one("R", "RANGE", range_element_type="DATE")
        other = self._make_one(
            "R", "RANGE", range_element_type=schema.FieldElementType("DATE")
        )
        self.assertEqual(field, other)

    def test___eq___rounding_mode_mismatch(self):
        field = self._make_one(
            "num", "NUMERIC", rounding_mode="ROUND_HALF_AWAY_FROM_ZERO"
        )
        other = self._make_one("num", "NUMERIC", rounding_mode="ROUND_HALF_EVEN")
        self.assertNotEqual(field, other)

    def test___eq___rounding_mode_hit(self):
        field = self._make_one(
            "num", "NUMERIC", rounding_mode=enums.RoundingMode.ROUND_HALF_AWAY_FROM_ZERO
        )
        other = self._make_one(
            "num", "NUMERIC", rounding_mode="ROUND_HALF_AWAY_FROM_ZERO"
        )
        self.assertEqual(field, other)

    def test___eq___foreign_type_definition_mismatch(self):
        field = self._make_one("f", "FOREIGN", foreign_type_definition="type1")
        other = self._make_one("f", "FOREIGN", foreign_type_definition="type2")
        self.assertNotEqual(field, other)

    def test___eq___foreign_type_definition_hit(self):
        field = self._make_one("f", "FOREIGN", foreign_type_definition="type1")
        other = self._make_one("f", "FOREIGN", foreign_type_definition="type1")
        self.assertEqual(field, other)

    def test___ne___wrong_type(self):
        field = self._make_one("toast", "INTEGER")
        other = object()
        self.assertNotEqual(field, other)
        self.assertEqual(field, mock.ANY)

    def test___ne___same_value(self):
        field1 = self._make_one("test", "TIMESTAMP", mode="REPEATED")
        field2 = self._make_one("test", "TIMESTAMP", mode="REPEATED")
        # unittest ``assertEqual`` uses ``==`` not ``!=``.
        comparison_val = field1 != field2
        self.assertFalse(comparison_val)

    def test___ne___different_values(self):
        field1 = self._make_one(
            "test1", "FLOAT", mode="REPEATED", description="Not same"
        )
        field2 = self._make_one(
            "test2", "FLOAT", mode="NULLABLE", description="Knot saym"
        )
        self.assertNotEqual(field1, field2)

    def test___ne___different_policy_tags(self):
        field = self._make_one(
            "test",
            "STRING",
            mode="REQUIRED",
            description="Testing",
            policy_tags=PolicyTagList(names=["foo", "bar"]),
        )
        other = self._make_one(
            "test",
            "STRING",
            mode="REQUIRED",
            description="Testing",
            policy_tags=PolicyTagList(names=["foo", "baz"]),
        )
        self.assertNotEqual(field, other)

    def test___hash__set_equality(self):
        sub1 = self._make_one("sub1", "STRING")
        sub2 = self._make_one("sub2", "STRING")
        field1 = self._make_one("test", "RECORD", fields=[sub1])
        field2 = self._make_one("test", "RECORD", fields=[sub2])
        set_one = {field1, field2}
        set_two = {field1, field2}
        self.assertEqual(set_one, set_two)

    def test___hash__not_equals(self):
        sub1 = self._make_one("sub1", "STRING")
        sub2 = self._make_one("sub2", "STRING")
        field1 = self._make_one("test", "RECORD", fields=[sub1])
        field2 = self._make_one("test", "RECORD", fields=[sub2])
        set_one = {field1}
        set_two = {field2}
        self.assertNotEqual(set_one, set_two)

    def test___repr__(self):
        field1 = self._make_one("field1", "STRING")
        expected = (
            "SchemaField('field1', 'STRING', 'NULLABLE', None, None, (), "
            "None, None, None, None)"
        )
        self.assertEqual(repr(field1), expected)

    def test___repr__evaluable_no_policy_tags(self):
        field = self._make_one("field1", "STRING", "REQUIRED", "Description")
        field_repr = repr(field)
        SchemaField = self._get_target_class()  # needed for eval  # noqa

        evaled_field = eval(field_repr)

        assert field == evaled_field

    def test___repr__evaluable_with_policy_tags(self):
        policy_tags = PolicyTagList(names=["foo", "bar"])
        field = self._make_one(
            "field1",
            "STRING",
            "REQUIRED",
            "Description",
            policy_tags=policy_tags,
        )
        field_repr = repr(field)
        SchemaField = self._get_target_class()  # needed for eval  # noqa

        evaled_field = eval(field_repr)

        assert field == evaled_field


class TestSchemaFieldDataPolicies:
    POLICY_ONE = DataPolicy("projects/project/locations/us/dataPolicies/one")
    POLICY_TWO = DataPolicy("projects/project/locations/us/dataPolicies/two")

    def test_constructor_preserves_legacy_positional_arguments(self):
        arguments = {
            "name": "test",
            "field_type": "TIMESTAMP",
            "mode": "REQUIRED",
            "default_value_expression": "CURRENT_TIMESTAMP()",
            "description": "Description",
            "fields": (),
            "policy_tags": None,
            "precision": 10,
            "scale": 2,
            "max_length": 128,
            "range_element_type": "DATE",
            "rounding_mode": enums.RoundingMode.ROUND_HALF_EVEN,
            "foreign_type_definition": "foreign",
            "timestamp_precision": enums.TimestampPrecision.PICOSECOND,
        }
        positional = schema.SchemaField(
            *arguments.values(), data_policies=[self.POLICY_ONE]
        )
        keyword = schema.SchemaField(**arguments, data_policies=[self.POLICY_ONE])

        assert positional.to_api_repr() == keyword.to_api_repr()
        with pytest.raises(TypeError):
            schema.SchemaField(*arguments.values(), [self.POLICY_ONE])

    @pytest.mark.parametrize(
        "policy", [POLICY_ONE.name, {"name": POLICY_ONE.name}, None]
    )
    def test_constructor_rejects_non_policy_items(self, policy):
        with pytest.raises(TypeError, match="DataPolicy"):
            schema.SchemaField("ssn", "STRING", data_policies=[policy])

    def test_policy_objects_preserve_unknown_api_properties(self):
        resource = {
            "name": "ssn",
            "type": "STRING",
            "mode": "NULLABLE",
            "dataPolicies": [
                {
                    "name": self.POLICY_ONE.name,
                    "futureOption": {"values": ["one", "two"]},
                }
            ],
        }
        original = copy.deepcopy(resource)
        field = schema.SchemaField.from_api_repr(resource)
        policies = field.data_policies

        assert isinstance(policies[0], DataPolicy)
        assert policies[0].name == self.POLICY_ONE.name
        assert policies[0].to_api_repr() == original["dataPolicies"][0]
        assert field.to_api_repr() == original
        rebuilt = schema.SchemaField("ssn", "STRING", data_policies=policies)
        assert rebuilt.to_api_repr() == original

    @pytest.mark.parametrize(
        "policies, expected",
        [
            (None, None),
            ([], []),
            ([POLICY_ONE], [{"name": POLICY_ONE.name}]),
            (
                [POLICY_ONE, POLICY_TWO],
                [{"name": POLICY_ONE.name}, {"name": POLICY_TWO.name}],
            ),
        ],
    )
    def test_constructor_and_round_trip(self, policies, expected):
        field = schema.SchemaField("ssn", "STRING", data_policies=policies)
        resource = {
            "name": "ssn",
            "type": "STRING",
            "mode": "NULLABLE",
            "dataPolicies": expected,
        }

        assert field.to_api_repr() == resource
        assert field.data_policies == (None if policies is None else tuple(policies))
        restored = schema.SchemaField.from_api_repr(copy.deepcopy(resource))
        assert restored == field
        assert hash(restored) == hash(field)
        assert restored.data_policies == field.data_policies
        assert restored.to_api_repr() == resource

    @pytest.mark.parametrize(
        "properties, expected",
        [
            ({}, None),
            ({"dataPolicies": None}, None),
            ({"dataPolicies": []}, ()),
            ({"dataPolicies": [{"name": POLICY_ONE.name}]}, (POLICY_ONE,)),
            (
                {
                    "dataPolicies": [
                        {"name": POLICY_ONE.name},
                        {"name": POLICY_TWO.name},
                    ]
                },
                (POLICY_ONE, POLICY_TWO),
            ),
        ],
    )
    def test_from_api_repr(self, properties, expected):
        resource = {"name": "ssn", "type": "STRING", "mode": "NULLABLE"}
        resource.update(properties)
        original = copy.deepcopy(resource)
        field = schema.SchemaField.from_api_repr(resource)

        assert field.data_policies == expected
        assert field.to_api_repr() == original
        assert field.to_api_repr() is resource

    @pytest.mark.parametrize("container", [list, tuple, iter])
    def test_constructor_accepts_iterables(self, container):
        policies = container([self.POLICY_ONE, self.POLICY_TWO])
        field = schema.SchemaField("ssn", "STRING", data_policies=policies)

        assert field.data_policies == (self.POLICY_ONE, self.POLICY_TWO)
        assert field.to_api_repr()["dataPolicies"] == [
            {"name": self.POLICY_ONE.name},
            {"name": self.POLICY_TWO.name},
        ]

    @pytest.mark.parametrize(
        "policies", [POLICY_ONE.name, POLICY_ONE.name.encode(), "", b""]
    )
    def test_constructor_rejects_strings_and_bytes(self, policies):
        with pytest.raises(TypeError, match="data_policies must be an iterable"):
            schema.SchemaField("ssn", "STRING", data_policies=policies)

    def test_constructor_copies_policy_list(self):
        policies = [self.POLICY_ONE]
        field = schema.SchemaField("ssn", "STRING", data_policies=policies)
        policies.append(self.POLICY_TWO)

        assert field.data_policies == (self.POLICY_ONE,)

    def test_equality_ignores_order(self):
        field = schema.SchemaField(
            "ssn", "STRING", data_policies=[self.POLICY_ONE, self.POLICY_TWO]
        )
        other = schema.SchemaField(
            "ssn", "STRING", data_policies=[self.POLICY_TWO, self.POLICY_ONE]
        )

        assert field == other
        assert not field != other
        assert hash(field) == hash(other)
        assert len({field, other}) == 1
        assert field._key().data_policies == (self.POLICY_ONE, self.POLICY_TWO)
        # Comparing fields must not reorder the API representation.
        assert other.data_policies == (self.POLICY_TWO, self.POLICY_ONE)
        assert other.to_api_repr()["dataPolicies"] == [
            {"name": self.POLICY_TWO.name},
            {"name": self.POLICY_ONE.name},
        ]

    @pytest.mark.parametrize("other_policies", [None, [], [POLICY_TWO]])
    def test_different_policies_are_not_equal(self, other_policies):
        field = schema.SchemaField("ssn", "STRING", data_policies=[self.POLICY_ONE])
        other = schema.SchemaField("ssn", "STRING", data_policies=other_policies)

        assert field != other
        assert len({field, other}) == 2
        assert field._key().data_policies != other._key().data_policies

    def test_absent_and_none_are_equal(self):
        field = schema.SchemaField("ssn", "STRING")
        other = schema.SchemaField("ssn", "STRING", data_policies=None)

        assert field == other
        assert hash(field) == hash(other)

    def test_absent_and_empty_are_not_equal(self):
        field = schema.SchemaField("ssn", "STRING")
        other = schema.SchemaField("ssn", "STRING", data_policies=[])

        assert field != other

    def test_nested_field_round_trip(self):
        child = schema.SchemaField("ssn", "STRING", data_policies=[self.POLICY_ONE])
        field = schema.SchemaField("person", "RECORD", fields=[child])
        resource = {
            "name": "person",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
                {
                    "name": "ssn",
                    "type": "STRING",
                    "mode": "NULLABLE",
                    "dataPolicies": [{"name": self.POLICY_ONE.name}],
                }
            ],
        }

        assert field.to_api_repr() == resource
        restored = schema.SchemaField.from_api_repr(copy.deepcopy(resource))
        assert restored.fields[0].data_policies == (self.POLICY_ONE,)
        assert restored == field
        assert hash(restored) == hash(field)

        other_child = schema.SchemaField(
            "ssn", "STRING", data_policies=[self.POLICY_TWO]
        )
        other = schema.SchemaField("person", "RECORD", fields=[other_child])
        assert field != other

    def test_policy_tags_on_another_field(self):
        tagged = schema.SchemaField(
            "name", "STRING", policy_tags=PolicyTagList(["policy-tag"])
        )
        masked = schema.SchemaField("ssn", "STRING", data_policies=[self.POLICY_ONE])
        fields = schema._to_schema_fields(
            schema._build_schema_resource([tagged, masked])
        )

        assert fields == [tagged, masked]
        assert fields[0].policy_tags.names == ("policy-tag",)
        assert fields[0].data_policies is None
        assert "dataPolicies" not in fields[0].to_api_repr()
        assert fields[1].policy_tags is None
        assert "policyTags" not in fields[1].to_api_repr()
        assert fields[1].data_policies == (self.POLICY_ONE,)

    @pytest.mark.parametrize("policies", [[], [POLICY_ONE], [POLICY_TWO, POLICY_ONE]])
    def test_repr(self, policies):
        field = schema.SchemaField("ssn", "STRING", data_policies=policies)

        restored = eval(
            repr(field), {"SchemaField": schema.SchemaField, "DataPolicy": DataPolicy}
        )
        assert restored == field
        assert restored.data_policies == tuple(
            sorted(policies, key=lambda policy: policy.name)
        )

    def test_repr_with_nested_fields(self):
        field = schema.SchemaField(
            "person",
            "RECORD",
            fields=[
                schema.SchemaField(
                    "name", "STRING", policy_tags=PolicyTagList(["policy-tag"])
                ),
                schema.SchemaField("ssn", "STRING", data_policies=[self.POLICY_ONE]),
            ],
        )

        restored = eval(
            repr(field),
            {
                "SchemaField": schema.SchemaField,
                "PolicyTagList": PolicyTagList,
                "DataPolicy": DataPolicy,
            },
        )
        assert restored == field
        assert restored.fields[0].policy_tags == field.fields[0].policy_tags
        assert restored.fields[1].data_policies == (self.POLICY_ONE,)


class TestDataPolicy:
    NAME = "projects/project/locations/us/dataPolicies/one"

    def test_public_export(self):
        assert bigquery.DataPolicy is DataPolicy
        assert "DataPolicy" in bigquery.__all__

    def test_constructor(self):
        policy = DataPolicy(name=self.NAME)

        assert policy.name == self.NAME
        assert policy.to_api_repr() == {"name": self.NAME}

    def test_from_api_repr_preserves_unknown_properties(self):
        resource = {
            "name": self.NAME,
            "futureOption": {"values": ["one", "two"]},
        }
        original = copy.deepcopy(resource)
        policy = DataPolicy.from_api_repr(resource)

        assert policy.name == self.NAME
        assert policy.to_api_repr() == original
        assert policy.to_api_repr() is resource
        assert DataPolicy.from_api_repr(policy.to_api_repr()).to_api_repr() == original

    def test_equality_and_hash(self):
        policy = DataPolicy(self.NAME)
        equal = DataPolicy(self.NAME)
        different = DataPolicy("projects/project/locations/us/dataPolicies/two")

        assert policy == equal
        assert not policy != equal
        assert policy != different
        assert hash(policy) == hash(equal)
        assert len({policy, equal, different}) == 2

    def test_equality_with_other_types(self):
        policy = DataPolicy(self.NAME)

        assert policy != object()
        assert policy == mock.ANY
        assert policy.__eq__(object()) is NotImplemented

    def test_repr(self):
        policy = DataPolicy(self.NAME)

        assert repr(policy) == f"DataPolicy(name={self.NAME!r})"
        assert eval(repr(policy), {"DataPolicy": DataPolicy}) == policy


class TestFieldElementType(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.schema import FieldElementType

        return FieldElementType

    def _make_one(self, *args):
        return self._get_target_class()(*args)

    def test_constructor(self):
        element_type = self._make_one("DATETIME")
        self.assertEqual(element_type.element_type, "DATETIME")
        self.assertEqual(element_type._properties["type"], "DATETIME")

    def test_to_api_repr(self):
        element_type = self._make_one("DATETIME")
        self.assertEqual(element_type.to_api_repr(), {"type": "DATETIME"})

    def test_from_api_repr(self):
        api_repr = {"type": "DATETIME"}
        expected_element_type = self._make_one("DATETIME")
        self.assertEqual(
            expected_element_type.element_type,
            self._get_target_class().from_api_repr(api_repr).element_type,
        )

    def test_from_api_repr_empty(self):
        self.assertEqual(None, self._get_target_class().from_api_repr({}))

    def test_from_api_repr_none(self):
        self.assertEqual(None, self._get_target_class().from_api_repr(None))

    def test___eq___wrong_type(self):
        element_type = self._make_one("DATE")
        self.assertNotEqual(element_type, "DATE")
        self.assertNotEqual(element_type, object())

    def test___eq___hit(self):
        element_type1 = self._make_one("DATE")
        element_type2 = self._make_one("DATE")
        self.assertEqual(element_type1, element_type2)

    def test___eq___case_insensitive(self):
        element_type1 = self._make_one("date")
        element_type2 = self._make_one("DATE")
        self.assertEqual(element_type1, element_type2)

    def test___eq___mismatch(self):
        element_type1 = self._make_one("DATE")
        element_type2 = self._make_one("DATETIME")
        self.assertNotEqual(element_type1, element_type2)

    def test___hash__(self):
        element_type1 = self._make_one("DATE")
        element_type2 = self._make_one("DATE")
        self.assertEqual(hash(element_type1), hash(element_type2))

    def test___repr__(self):
        element_type = self._make_one("DATE")
        self.assertEqual(repr(element_type), "FieldElementType(element_type='DATE')")


# TODO: dedup with the same class in test_table.py.
class _SchemaBase(object):
    def _verify_field(self, field, r_field):
        self.assertEqual(field.name, r_field["name"])
        self.assertEqual(field.field_type, r_field["type"])
        self.assertEqual(field.mode, r_field.get("mode", "NULLABLE"))

    def _verifySchema(self, schema, resource):
        r_fields = resource["schema"]["fields"]
        self.assertEqual(len(schema), len(r_fields))

        for field, r_field in zip(schema, r_fields):
            self._verify_field(field, r_field)


class Test_parse_schema_resource(unittest.TestCase, _SchemaBase):
    def _call_fut(self, resource):
        from google.cloud.bigquery.schema import _parse_schema_resource

        return _parse_schema_resource(resource)

    def _make_resource(self):
        return {
            "schema": {
                "fields": [
                    {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "age", "type": "INTEGER", "mode": "REQUIRED"},
                ]
            }
        }

    def test__parse_schema_resource_defaults(self):
        RESOURCE = self._make_resource()
        schema = self._call_fut(RESOURCE["schema"])
        self._verifySchema(schema, RESOURCE)

    def test__parse_schema_resource_subfields(self):
        RESOURCE = self._make_resource()
        RESOURCE["schema"]["fields"].append(
            {
                "name": "phone",
                "type": "RECORD",
                "mode": "REPEATED",
                "fields": [
                    {"name": "type", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "number", "type": "STRING", "mode": "REQUIRED"},
                ],
            }
        )
        schema = self._call_fut(RESOURCE["schema"])
        self._verifySchema(schema, RESOURCE)

    def test__parse_schema_resource_fields_without_mode(self):
        RESOURCE = self._make_resource()
        RESOURCE["schema"]["fields"].append({"name": "phone", "type": "STRING"})

        schema = self._call_fut(RESOURCE["schema"])
        self._verifySchema(schema, RESOURCE)


class Test_build_schema_resource:
    """Tests for the _build_schema_resource function."""

    def _call_fut(self, resource):
        return schema._build_schema_resource(resource)

    FULL_NAME = schema.SchemaField(
        name="full_name", field_type="STRING", mode="REQUIRED"
    )
    AGE = schema.SchemaField(name="age", field_type="INTEGER", mode="REQUIRED")
    LIST_RESOURCE = [
        {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
        {"name": "age", "type": "INTEGER", "mode": "REQUIRED"},
    ]
    FOREIGN_TYPE_INFO = schema.ForeignTypeInfo(type_system="TYPE_SYSTEM_UNSPECIFIED")
    FOREIGN_TYPE_INFO_RESOURCE = {"typeSystem": "TYPE_SYSTEM_UNSPECIFIED"}

    @pytest.mark.parametrize(
        "schema,expected",
        [
            pytest.param([], [], id="empty list"),
            pytest.param([FULL_NAME, AGE], LIST_RESOURCE, id="list"),
        ],
    )
    def test_ctor_valid_input(self, schema, expected):
        result = self._call_fut(schema)

        assert result == expected

    @pytest.mark.parametrize(
        "schema,expected",
        [
            pytest.param(123, TypeError, id="invalid type"),
        ],
    )
    def test_ctor_invalid_input(self, schema, expected):
        with pytest.raises(TypeError) as e:
            self._call_fut(schema)

        # Looking for the first phrase from the string "Schema must be a ..."
        assert "Schema must be a " in str(e.value)

    def test_defaults(self):
        from google.cloud.bigquery.schema import SchemaField

        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        age = SchemaField("age", "INTEGER", mode="REQUIRED")
        # test with simple list
        resource = self._call_fut([full_name, age])
        assert len(resource) == 2
        assert resource[0] == {
            "name": "full_name",
            "type": "STRING",
            "mode": "REQUIRED",
        }
        assert resource[1] == {"name": "age", "type": "INTEGER", "mode": "REQUIRED"}

    def test_w_description(self):
        from google.cloud.bigquery.schema import SchemaField

        DESCRIPTION = "DESCRIPTION"
        full_name = SchemaField(
            "full_name", "STRING", mode="REQUIRED", description=DESCRIPTION
        )
        age = SchemaField(
            "age",
            "INTEGER",
            mode="REQUIRED",
            # Explicitly unset description.
            description=None,
        )
        resource = self._call_fut([full_name, age])
        assert len(resource) == 2
        assert resource[0] == {
            "name": "full_name",
            "type": "STRING",
            "mode": "REQUIRED",
            "description": DESCRIPTION,
        }

        assert resource[1] == {
            "name": "age",
            "type": "INTEGER",
            "mode": "REQUIRED",
            "description": None,
        }

    def test_w_subfields(self):
        from google.cloud.bigquery.schema import SchemaField

        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        ph_type = SchemaField("type", "STRING", "REQUIRED")
        ph_num = SchemaField("number", "STRING", "REQUIRED")
        phone = SchemaField(
            "phone", "RECORD", mode="REPEATED", fields=[ph_type, ph_num]
        )
        resource = self._call_fut([full_name, phone])
        assert len(resource) == 2
        assert resource[0] == {
            "name": "full_name",
            "type": "STRING",
            "mode": "REQUIRED",
        }
        assert resource[1] == {
            "name": "phone",
            "type": "RECORD",
            "mode": "REPEATED",
            "fields": [
                {"name": "type", "type": "STRING", "mode": "REQUIRED"},
                {"name": "number", "type": "STRING", "mode": "REQUIRED"},
            ],
        }


class Test_to_schema_fields:
    """Tests for the _to_schema_fields function."""

    @staticmethod
    def _call_fut(schema):
        from google.cloud.bigquery.schema import _to_schema_fields

        return _to_schema_fields(schema)

    FULL_NAME = schema.SchemaField(
        name="full_name", field_type="STRING", mode="REQUIRED"
    )
    AGE = schema.SchemaField(name="age", field_type="INTEGER", mode="REQUIRED")
    LIST_RESOURCE = [
        {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
        {"name": "age", "type": "INTEGER", "mode": "REQUIRED"},
    ]
    FOREIGN_TYPE_INFO = schema.ForeignTypeInfo(type_system="TYPE_SYSTEM_UNSPECIFIED")
    FOREIGN_TYPE_INFO_RESOURCE = {"typeSystem": "TYPE_SYSTEM_UNSPECIFIED"}

    @pytest.mark.parametrize(
        "schema,expected",
        [
            pytest.param([], [], id="empty list"),
            pytest.param((), [], id="empty tuple"),
            pytest.param(LIST_RESOURCE, [FULL_NAME, AGE], id="list"),
        ],
    )
    def test_ctor_valid_input(self, schema, expected):
        result = self._call_fut(schema)

        assert result == expected

    @pytest.mark.parametrize(
        "schema,expected",
        [
            pytest.param(123, TypeError, id="invalid schema type"),
            pytest.param([123, 123], TypeError, id="invalid SchemaField type"),
            pytest.param({"fields": 123}, TypeError, id="invalid type, dict"),
            pytest.param(
                {"fields": 123, "foreignTypeInfo": 123},
                TypeError,
                id="invalid type, dict",
            ),
        ],
    )
    def test_ctor_invalid_input(self, schema, expected):
        with pytest.raises(expected):
            self._call_fut(schema)

    def test_unknown_properties(self):
        schema = [
            {
                "name": "full_name",
                "type": "STRING",
                "mode": "REQUIRED",
                "someNewProperty": "test-value",
            },
            {
                "name": "age",
                # Note: This type should be included, too. Avoid client-side
                # validation, as it could prevent backwards-compatible
                # evolution of the server-side behavior.
                "typo": "INTEGER",
                "mode": "REQUIRED",
                "anotherNewProperty": "another-test",
            },
        ]

        # Make sure the setter doesn't mutate schema.
        expected_schema = copy.deepcopy(schema)

        result = self._call_fut(schema)

        for api_repr, field in zip(expected_schema, result):
            assert field.to_api_repr() == api_repr

    def test_valid_mapping_representation(self):
        from google.cloud.bigquery.schema import SchemaField

        schema = [
            {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
            {
                "name": "residence",
                "type": "STRUCT",
                "mode": "NULLABLE",
                "fields": [
                    {"name": "foo", "type": "DATE", "mode": "NULLABLE"},
                    {"name": "bar", "type": "BYTES", "mode": "REQUIRED"},
                ],
            },
        ]

        expected_schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField(
                "residence",
                "STRUCT",
                mode="NULLABLE",
                fields=[
                    SchemaField("foo", "DATE", mode="NULLABLE"),
                    SchemaField("bar", "BYTES", mode="REQUIRED"),
                ],
            ),
        ]

        result = self._call_fut(schema)
        assert result == expected_schema


class TestPolicyTags(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        return PolicyTagList

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_constructor(self):
        empty_policy_tags = self._make_one()
        self.assertIsNotNone(empty_policy_tags.names)
        self.assertEqual(len(empty_policy_tags.names), 0)
        policy_tags = self._make_one(["foo", "bar"])
        self.assertEqual(policy_tags.names, ("foo", "bar"))

    def test_from_api_repr(self):
        klass = self._get_target_class()
        api_repr = {"names": ["foo"]}
        policy_tags = klass.from_api_repr(api_repr)
        self.assertEqual(policy_tags.to_api_repr(), api_repr)

        # Ensure the None case correctly returns None, rather
        # than an empty instance.
        policy_tags2 = klass.from_api_repr(None)
        self.assertIsNone(policy_tags2)

    def test_to_api_repr(self):
        taglist = self._make_one(names=["foo", "bar"])
        self.assertEqual(
            taglist.to_api_repr(),
            {"names": ["foo", "bar"]},
        )
        taglist2 = self._make_one(names=("foo", "bar"))
        self.assertEqual(
            taglist2.to_api_repr(),
            {"names": ["foo", "bar"]},
        )

    def test___eq___wrong_type(self):
        policy = self._make_one(names=["foo"])
        other = object()
        self.assertNotEqual(policy, other)
        self.assertEqual(policy, mock.ANY)

    def test___eq___names_mismatch(self):
        policy = self._make_one(names=["foo", "bar"])
        other = self._make_one(names=["bar", "baz"])
        self.assertNotEqual(policy, other)

    def test___hash__set_equality(self):
        policy1 = self._make_one(["foo", "bar"])
        policy2 = self._make_one(["bar", "baz"])
        set_one = {policy1, policy2}
        set_two = {policy1, policy2}
        self.assertEqual(set_one, set_two)

    def test___hash__not_equals(self):
        policy1 = self._make_one(["foo", "bar"])
        policy2 = self._make_one(["bar", "baz"])
        set_one = {policy1}
        set_two = {policy2}
        self.assertNotEqual(set_one, set_two)

    def test___repr__no_tags(self):
        policy = self._make_one()
        assert repr(policy) == "PolicyTagList(names=())"

    def test___repr__with_tags(self):
        policy1 = self._make_one(["foo", "bar", "baz"])
        policy2 = self._make_one(["baz", "bar", "foo"])
        expected_repr = "PolicyTagList(names=('bar', 'baz', 'foo'))"  # alphabetical

        assert repr(policy1) == expected_repr
        assert repr(policy2) == expected_repr

    def test___repr__evaluable_no_tags(self):
        policy = self._make_one(names=[])
        policy_repr = repr(policy)

        evaled_policy = eval(policy_repr)

        assert policy == evaled_policy

    def test___repr__evaluable_with_tags(self):
        policy = self._make_one(names=["foo", "bar"])
        policy_repr = repr(policy)

        evaled_policy = eval(policy_repr)

        assert policy == evaled_policy


@pytest.mark.parametrize(
    "api,expect,key2",
    [
        (
            dict(name="n", type="NUMERIC"),
            ("n", "NUMERIC", None, None, None),
            ("n", "NUMERIC"),
        ),
        (
            dict(name="n", type="NUMERIC", precision=9),
            ("n", "NUMERIC", 9, None, None),
            ("n", "NUMERIC(9)"),
        ),
        (
            dict(name="n", type="NUMERIC", precision=9, scale=2),
            ("n", "NUMERIC", 9, 2, None),
            ("n", "NUMERIC(9, 2)"),
        ),
        (
            dict(name="n", type="BIGNUMERIC"),
            ("n", "BIGNUMERIC", None, None, None),
            ("n", "BIGNUMERIC"),
        ),
        (
            dict(name="n", type="BIGNUMERIC", precision=40),
            ("n", "BIGNUMERIC", 40, None, None),
            ("n", "BIGNUMERIC(40)"),
        ),
        (
            dict(name="n", type="BIGNUMERIC", precision=40, scale=2),
            ("n", "BIGNUMERIC", 40, 2, None),
            ("n", "BIGNUMERIC(40, 2)"),
        ),
        (
            dict(name="n", type="STRING"),
            ("n", "STRING", None, None, None),
            ("n", "STRING"),
        ),
        (
            dict(name="n", type="STRING", maxLength=9),
            ("n", "STRING", None, None, 9),
            ("n", "STRING(9)"),
        ),
        (
            dict(name="n", type="BYTES"),
            ("n", "BYTES", None, None, None),
            ("n", "BYTES"),
        ),
        (
            dict(name="n", type="BYTES", maxLength=9),
            ("n", "BYTES", None, None, 9),
            ("n", "BYTES(9)"),
        ),
        (
            dict(name="n", type="RANGE", rangeElementType=dict(type="DATE")),
            ("n", "RANGE", None, None, None),
            ("n", "RANGE<DATE>"),
        ),
        (
            dict(name="n", type="RANGE", rangeElementType=dict(type="DATETIME")),
            ("n", "RANGE", None, None, None),
            ("n", "RANGE<DATETIME>"),
        ),
        (
            dict(name="n", type="RANGE", rangeElementType=dict(type="TIMESTAMP")),
            ("n", "RANGE", None, None, None),
            ("n", "RANGE<TIMESTAMP>"),
        ),
    ],
)
def test_from_api_repr_parameterized(api, expect, key2):
    from google.cloud.bigquery.schema import SchemaField

    field = SchemaField.from_api_repr(api)

    assert (
        field.name,
        field.field_type,
        field.precision,
        field.scale,
        field.max_length,
    ) == expect

    assert field._key()[:2] == key2


@pytest.mark.parametrize(
    "field,api",
    [
        (
            dict(name="n", field_type="NUMERIC"),
            dict(name="n", type="NUMERIC", mode="NULLABLE"),
        ),
        (
            dict(name="n", field_type="NUMERIC", precision=9),
            dict(
                name="n",
                type="NUMERIC",
                mode="NULLABLE",
                precision=9,
            ),
        ),
        (
            dict(name="n", field_type="NUMERIC", precision=9, scale=2),
            dict(
                name="n",
                type="NUMERIC",
                mode="NULLABLE",
                precision=9,
                scale=2,
            ),
        ),
        (
            dict(name="n", field_type="BIGNUMERIC"),
            dict(name="n", type="BIGNUMERIC", mode="NULLABLE"),
        ),
        (
            dict(name="n", field_type="BIGNUMERIC", precision=40),
            dict(
                name="n",
                type="BIGNUMERIC",
                mode="NULLABLE",
                precision=40,
            ),
        ),
        (
            dict(name="n", field_type="BIGNUMERIC", precision=40, scale=2),
            dict(
                name="n",
                type="BIGNUMERIC",
                mode="NULLABLE",
                precision=40,
                scale=2,
            ),
        ),
        (
            dict(name="n", field_type="STRING"),
            dict(name="n", type="STRING", mode="NULLABLE"),
        ),
        (
            dict(name="n", field_type="STRING", max_length=9),
            dict(
                name="n",
                type="STRING",
                mode="NULLABLE",
                maxLength=9,
            ),
        ),
        (
            dict(name="n", field_type="BYTES"),
            dict(name="n", type="BYTES", mode="NULLABLE"),
        ),
        (
            dict(name="n", field_type="BYTES", max_length=9),
            dict(
                name="n",
                type="BYTES",
                mode="NULLABLE",
                maxLength=9,
            ),
        ),
    ],
)
def test_to_api_repr_parameterized(field, api):
    from google.cloud.bigquery.schema import SchemaField

    assert SchemaField(**field).to_api_repr() == api


class TestForeignTypeInfo:
    """Tests for ForeignTypeInfo objects."""

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.schema import ForeignTypeInfo

        return ForeignTypeInfo

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    @pytest.mark.parametrize(
        "type_system,expected",
        [
            (None, None),
            ("TYPE_SYSTEM_UNSPECIFIED", "TYPE_SYSTEM_UNSPECIFIED"),
            ("HIVE", "HIVE"),
        ],
    )
    def test_ctor_valid_input(self, type_system, expected):
        result = self._make_one(type_system=type_system)

        assert result.type_system == expected

    def test_ctor_invalid_input(self):
        with pytest.raises(TypeError) as e:
            self._make_one(type_system=123)

        # Looking for the first word from the string "Pass <variable> as..."
        assert "Pass " in str(e.value)

    @pytest.mark.parametrize(
        "type_system,expected",
        [
            ("TYPE_SYSTEM_UNSPECIFIED", {"typeSystem": "TYPE_SYSTEM_UNSPECIFIED"}),
            ("HIVE", {"typeSystem": "HIVE"}),
            (None, {"typeSystem": None}),
        ],
    )
    def test_to_api_repr(self, type_system, expected):
        result = self._make_one(type_system=type_system)

        assert result.to_api_repr() == expected

    def test_from_api_repr(self):
        """GIVEN an api representation of a ForeignTypeInfo object (i.e. api_repr)
        WHEN converted into a ForeignTypeInfo object using from_api_repr()
        THEN it will have the same representation in dict format as a ForeignTypeInfo
        object made directly (via _make_one()) and represented in dict format.
        """
        api_repr = {
            "typeSystem": "TYPE_SYSTEM_UNSPECIFIED",
        }

        expected = self._make_one(
            type_system="TYPE_SYSTEM_UNSPECIFIED",
        )

        klass = self._get_target_class()
        result = klass.from_api_repr(api_repr)

        # We convert both to dict format because these classes do not have a
        # __eq__() method to facilitate direct equality comparisons.
        assert result.to_api_repr() == expected.to_api_repr()


class TestSerDeInfo:
    """Tests for the SerDeInfo class."""

    @staticmethod
    def _get_target_class():
        return schema.SerDeInfo

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    @pytest.mark.parametrize(
        "serialization_library,name,parameters",
        [
            ("testpath.to.LazySimpleSerDe", None, None),
            ("testpath.to.LazySimpleSerDe", "serde_name", None),
            ("testpath.to.LazySimpleSerDe", None, {"key": "value"}),
            ("testpath.to.LazySimpleSerDe", "serde_name", {"key": "value"}),
        ],
    )
    def test_ctor_valid_input(self, serialization_library, name, parameters):
        serde_info = self._make_one(
            serialization_library=serialization_library,
            name=name,
            parameters=parameters,
        )
        assert serde_info.serialization_library == serialization_library
        assert serde_info.name == name
        assert serde_info.parameters == parameters

    @pytest.mark.parametrize(
        "serialization_library,name,parameters",
        [
            (123, None, None),
            ("testpath.to.LazySimpleSerDe", 123, None),
            ("testpath.to.LazySimpleSerDe", None, ["test", "list"]),
            ("testpath.to.LazySimpleSerDe", None, 123),
        ],
    )
    def test_ctor_invalid_input(self, serialization_library, name, parameters):
        with pytest.raises(TypeError) as e:
            self._make_one(
                serialization_library=serialization_library,
                name=name,
                parameters=parameters,
            )
        # Looking for the first word from the string "Pass <variable> as..."
        assert "Pass " in str(e.value)

    def test_to_api_repr(self):
        serde_info = self._make_one(
            serialization_library="testpath.to.LazySimpleSerDe",
            name="serde_name",
            parameters={"key": "value"},
        )
        expected_repr = {
            "serializationLibrary": "testpath.to.LazySimpleSerDe",
            "name": "serde_name",
            "parameters": {"key": "value"},
        }
        assert serde_info.to_api_repr() == expected_repr

    def test_from_api_repr(self):
        """GIVEN an api representation of a SerDeInfo object (i.e. api_repr)
        WHEN converted into a SerDeInfo object using from_api_repr()
        THEN it will have the same representation in dict format as a SerDeInfo
        object made directly (via _make_one()) and represented in dict format.
        """
        api_repr = {
            "serializationLibrary": "testpath.to.LazySimpleSerDe",
            "name": "serde_name",
            "parameters": {"key": "value"},
        }

        expected = self._make_one(
            serialization_library="testpath.to.LazySimpleSerDe",
            name="serde_name",
            parameters={"key": "value"},
        )

        klass = self._get_target_class()
        result = klass.from_api_repr(api_repr)

        # We convert both to dict format because these classes do not have a
        # __eq__() method to facilitate direct equality comparisons.
        assert result.to_api_repr() == expected.to_api_repr()


class TestStorageDescriptor:
    """Tests for the StorageDescriptor class."""

    @staticmethod
    def _get_target_class():
        return schema.StorageDescriptor

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    serdeinfo_resource = {
        "serialization_library": "testpath.to.LazySimpleSerDe",
        "name": "serde_lib_name",
        "parameters": {"key": "value"},
    }

    SERDEINFO = schema.SerDeInfo("PLACEHOLDER").from_api_repr(serdeinfo_resource)

    STORAGEDESCRIPTOR = {
        "inputFormat": "testpath.to.OrcInputFormat",
        "locationUri": "gs://test/path/",
        "outputFormat": "testpath.to.OrcOutputFormat",
        "serDeInfo": SERDEINFO.to_api_repr(),
    }

    @pytest.mark.parametrize(
        "input_format,location_uri,output_format,serde_info",
        [
            (None, None, None, None),
            ("testpath.to.OrcInputFormat", None, None, None),
            (None, "gs://test/path/", None, None),
            (None, None, "testpath.to.OrcOutputFormat", None),
            (None, None, None, SERDEINFO),
            (
                "testpath.to.OrcInputFormat",
                "gs://test/path/",
                "testpath.to.OrcOutputFormat",
                SERDEINFO,  # uses SERDEINFO class format
            ),
            (
                "testpath.to.OrcInputFormat",
                "gs://test/path/",
                "testpath.to.OrcOutputFormat",
                serdeinfo_resource,  # uses api resource format (dict)
            ),
        ],
    )
    def test_ctor_valid_input(
        self, input_format, location_uri, output_format, serde_info
    ):
        storage_descriptor = self._make_one(
            input_format=input_format,
            location_uri=location_uri,
            output_format=output_format,
            serde_info=serde_info,
        )
        assert storage_descriptor.input_format == input_format
        assert storage_descriptor.location_uri == location_uri
        assert storage_descriptor.output_format == output_format
        if isinstance(serde_info, schema.SerDeInfo):
            assert (
                storage_descriptor.serde_info.to_api_repr() == serde_info.to_api_repr()
            )
        elif isinstance(serde_info, dict):
            assert storage_descriptor.serde_info.to_api_repr() == serde_info
        else:
            assert storage_descriptor.serde_info is None

    @pytest.mark.parametrize(
        "input_format,location_uri,output_format,serde_info",
        [
            (123, None, None, None),
            (None, 123, None, None),
            (None, None, 123, None),
            (None, None, None, 123),
        ],
    )
    def test_ctor_invalid_input(
        self, input_format, location_uri, output_format, serde_info
    ):
        with pytest.raises(TypeError) as e:
            self._make_one(
                input_format=input_format,
                location_uri=location_uri,
                output_format=output_format,
                serde_info=serde_info,
            )

        # Looking for the first word from the string "Pass <variable> as..."
        assert "Pass " in str(e.value)

    def test_to_api_repr(self):
        storage_descriptor = self._make_one(
            input_format="input_format",
            location_uri="location_uri",
            output_format="output_format",
            serde_info=self.SERDEINFO,
        )
        expected_repr = {
            "inputFormat": "input_format",
            "locationUri": "location_uri",
            "outputFormat": "output_format",
            "serDeInfo": self.SERDEINFO.to_api_repr(),
        }
        assert storage_descriptor.to_api_repr() == expected_repr

    def test_from_api_repr(self):
        """GIVEN an api representation of a StorageDescriptor (i.e. STORAGEDESCRIPTOR)
        WHEN converted into a StorageDescriptor using from_api_repr() and
        displayed as a dict
        THEN it will have the same representation a StorageDescriptor created
        directly (via the _make_one() func) and displayed as a dict.
        """

        # generate via STORAGEDESCRIPTOR
        resource = self.STORAGEDESCRIPTOR
        result = self._get_target_class().from_api_repr(resource)
        # result = klass.from_api_repr(resource)

        expected = self._make_one(
            input_format="testpath.to.OrcInputFormat",
            location_uri="gs://test/path/",
            output_format="testpath.to.OrcOutputFormat",
            serde_info=self.SERDEINFO,
        )
        assert result.to_api_repr() == expected.to_api_repr()
