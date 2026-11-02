# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from google.cloud import bigquery


@pytest.fixture
def target_class():
    from google.cloud.bigquery.routine import RoutineArgument

    return RoutineArgument


def test_ctor(target_class):
    data_type = bigquery.standard_sql.StandardSqlDataType(
        type_kind=bigquery.StandardSqlTypeNames.INT64
    )
    actual_arg = target_class(
        name="field_name", kind="FIXED_TYPE", mode="IN", data_type=data_type
    )
    assert actual_arg.name == "field_name"
    assert actual_arg.kind == "FIXED_TYPE"
    assert actual_arg.mode == "IN"
    assert actual_arg.data_type == data_type


def test_from_api_repr(target_class):
    resource = {
        "argumentKind": "FIXED_TYPE",
        "dataType": {"typeKind": "INT64"},
        "mode": "IN",
        "name": "field_name",
    }
    actual_arg = target_class.from_api_repr(resource)
    assert actual_arg.name == "field_name"
    assert actual_arg.kind == "FIXED_TYPE"
    assert actual_arg.mode == "IN"
    assert actual_arg.data_type == bigquery.standard_sql.StandardSqlDataType(
        type_kind=bigquery.StandardSqlTypeNames.INT64
    )


def test_from_api_repr_w_minimal_resource(target_class):
    resource = {}
    actual_arg = target_class.from_api_repr(resource)
    assert actual_arg.name is None
    assert actual_arg.kind is None
    assert actual_arg.mode is None
    assert actual_arg.data_type is None


def test_from_api_repr_w_unknown_fields(target_class):
    resource = {"thisFieldIsNotInTheProto": "just ignore me"}
    actual_arg = target_class.from_api_repr(resource)
    assert actual_arg._properties is resource


def test_eq(target_class):
    data_type = bigquery.standard_sql.StandardSqlDataType(
        type_kind=bigquery.StandardSqlTypeNames.INT64
    )
    arg = target_class(
        name="field_name", kind="FIXED_TYPE", mode="IN", data_type=data_type
    )
    arg_too = target_class(
        name="field_name", kind="FIXED_TYPE", mode="IN", data_type=data_type
    )
    assert arg == arg_too
    assert not (arg != arg_too)

    other_arg = target_class()
    assert not (arg == other_arg)
    assert arg != other_arg

    notanarg = object()
    assert not (arg == notanarg)
    assert arg != notanarg


def test_repr(target_class):
    arg = target_class(name="field_name", kind="FIXED_TYPE", mode="IN", data_type=None)
    actual_repr = repr(arg)
    assert actual_repr == (
        "RoutineArgument(data_type=None, kind='FIXED_TYPE', mode='IN', name='field_name')"
    )
