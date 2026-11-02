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

import google.cloud.bigquery.schema


def create_field(mode="NULLABLE", type_="IGNORED", name="test_field", **kwargs):
    return google.cloud.bigquery.schema.SchemaField(name, type_, mode=mode, **kwargs)


@pytest.fixture
def mut():
    from google.cloud.bigquery import _helpers

    return _helpers


@pytest.fixture
def object_under_test(mut):
    return mut.DATA_FRAME_CELL_DATA_PARSER


def test_json_to_py_doesnt_parse_json(object_under_test):
    coerced = object_under_test.json_to_py('{"key":"value"}', create_field())
    assert coerced == '{"key":"value"}'


def test_json_to_py_repeated_doesnt_parse_json(object_under_test):
    coerced = object_under_test.json_to_py('{"key":"value"}', create_field("REPEATED"))
    assert coerced == '{"key":"value"}'


def test_record_to_py_doesnt_parse_json(object_under_test):
    subfield = create_field(type_="JSON", name="json")
    field = create_field(fields=[subfield])
    value = {"f": [{"v": '{"key":"value"}'}]}
    coerced = object_under_test.record_to_py(value, field)
    assert coerced == {"json": '{"key":"value"}'}


def test_record_to_py_doesnt_parse_repeated_json(object_under_test):
    subfield = create_field("REPEATED", "JSON", name="json")
    field = create_field("REQUIRED", fields=[subfield])
    value = {
        "f": [
            {
                "v": [
                    {"v": '{"key":"value0"}'},
                    {"v": '{"key":"value1"}'},
                    {"v": '{"key":"value2"}'},
                ]
            }
        ]
    }
    coerced = object_under_test.record_to_py(value, field)
    assert coerced == {
        "json": ['{"key":"value0"}', '{"key":"value1"}', '{"key":"value2"}']
    }
