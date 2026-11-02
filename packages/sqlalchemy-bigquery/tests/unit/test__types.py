# Copyright 2025 Google LLC
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

import pytest
from google.cloud.bigquery.schema import SchemaField

from sqlalchemy_bigquery._types import _get_transitive_schema_fields


def create_schema_field_from_dict(schema_dict):
    """
    Helper function to create a SchemaField object from a dictionary representation.
    """
    api_repr = {
        "name": schema_dict["name"],
        "type": schema_dict["type"],
        "mode": schema_dict.get("mode", "NULLABLE"),
        "fields": [
            create_schema_field_from_dict(sf_dict).to_api_repr()
            for sf_dict in schema_dict.get("fields", [])
        ],
    }
    return SchemaField.from_api_repr(api_repr)


test_cases = [
    (
        "STRUCT field, not REPEATED, with sub-fields, should recurse",
        [
            create_schema_field_from_dict(
                {
                    "name": "s1",
                    "type": "STRUCT",
                    "mode": "NULLABLE",
                    "fields": [
                        {"name": "child1", "type": "STRING", "mode": "NULLABLE"}
                    ],
                }
            )
        ],
        ["s1", "s1.child1"],
    ),
    (
        "RECORD field (alias for STRUCT), not REPEATED, with sub-fields, should recurse",
        [
            create_schema_field_from_dict(
                {
                    "name": "r1",
                    "type": "RECORD",
                    "mode": "NULLABLE",
                    "fields": [
                        {"name": "child_r1", "type": "INTEGER", "mode": "NULLABLE"}
                    ],
                }
            )
        ],
        ["r1", "r1.child_r1"],
    ),
    (
        "STRUCT field, REPEATED, with sub-fields, should NOT recurse",
        [
            create_schema_field_from_dict(
                {
                    "name": "s2",
                    "type": "STRUCT",
                    "mode": "REPEATED",
                    "fields": [
                        {"name": "child2", "type": "STRING", "mode": "NULLABLE"}
                    ],
                }
            )
        ],
        ["s2"],
    ),
    (
        "Non-STRUCT field (STRING), not REPEATED, should NOT recurse",
        [
            create_schema_field_from_dict(
                {"name": "f1", "type": "STRING", "mode": "NULLABLE"}
            )
        ],
        ["f1"],
    ),
    (
        "Non-STRUCT field (INTEGER), REPEATED, should NOT recurse",
        [
            create_schema_field_from_dict(
                {"name": "f2", "type": "INTEGER", "mode": "REPEATED"}
            )
        ],
        ["f2"],
    ),
    (
        "Deeply nested STRUCT, not REPEATED, should recurse fully",
        [
            create_schema_field_from_dict(
                {
                    "name": "s_outer",
                    "type": "STRUCT",
                    "mode": "NULLABLE",
                    "fields": [
                        {
                            "name": "s_inner1",
                            "type": "STRUCT",
                            "mode": "NULLABLE",
                            "fields": [
                                {
                                    "name": "s_leaf1",
                                    "type": "STRING",
                                    "mode": "NULLABLE",
                                }
                            ],
                        },
                        {"name": "s_sibling", "type": "INTEGER", "mode": "NULLABLE"},
                        {
                            "name": "s_inner2_repeated_struct",
                            "type": "STRUCT",
                            "mode": "REPEATED",
                            "fields": [
                                {
                                    "name": "s_leaf2_ignored",
                                    "type": "BOOLEAN",
                                    "mode": "NULLABLE",
                                }
                            ],
                        },
                    ],
                }
            )
        ],
        [
            "s_outer",
            "s_outer.s_inner1",
            "s_outer.s_inner1.s_leaf1",
            "s_outer.s_sibling",
            "s_outer.s_inner2_repeated_struct",
        ],
    ),
    (
        "STRUCT field, not REPEATED, but no sub-fields, should not error and not recurse further",
        [
            create_schema_field_from_dict(
                {"name": "s3", "type": "STRUCT", "mode": "NULLABLE", "fields": []}
            )
        ],
        ["s3"],
    ),
    (
        "Multiple top-level fields with mixed conditions",
        [
            create_schema_field_from_dict(
                {"name": "id", "type": "INTEGER", "mode": "REQUIRED"}
            ),
            create_schema_field_from_dict(
                {
                    "name": "user_profile",
                    "type": "STRUCT",
                    "mode": "NULLABLE",
                    "fields": [
                        {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                        {
                            "name": "addresses",
                            "type": "RECORD",
                            "mode": "REPEATED",
                            "fields": [
                                {
                                    "name": "street",
                                    "type": "STRING",
                                    "mode": "NULLABLE",
                                },
                                {"name": "city", "type": "STRING", "mode": "NULLABLE"},
                            ],
                        },
                    ],
                }
            ),
            create_schema_field_from_dict(
                {"name": "tags", "type": "STRING", "mode": "REPEATED"}
            ),
        ],
        ["id", "user_profile", "user_profile.name", "user_profile.addresses", "tags"],
    ),
    (
        "Empty input list of fields",
        [],
        [],
    ),
    (
        "Field type not in STRUCT_FIELD_TYPES and mode is REPEATED",
        [
            create_schema_field_from_dict(
                {"name": "f_arr", "type": "FLOAT", "mode": "REPEATED"}
            )
        ],
        ["f_arr"],
    ),
    (
        "Field type not in STRUCT_FIELD_TYPES and mode is not REPEATED",
        [
            create_schema_field_from_dict(
                {"name": "f_single", "type": "DATE", "mode": "NULLABLE"}
            )
        ],
        ["f_single"],
    ),
]


@pytest.mark.parametrize(
    "description, input_fields_list, expected_field_names", test_cases
)
def test_get_transitive_schema_fields_conditions(
    description, input_fields_list, expected_field_names
):
    """
    Tests the _get_transitive_schema_fields function, focusing on the conditional logic
    `if field.field_type in STRUCT_FIELD_TYPES and field.mode != "REPEATED":`.
    """
    result_fields = _get_transitive_schema_fields(input_fields_list)
    result_names = [field.name for field in result_fields]
    assert result_names == expected_field_names, description
