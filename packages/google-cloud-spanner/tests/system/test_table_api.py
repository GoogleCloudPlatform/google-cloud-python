# Copyright 2021 Google LLC All rights reserved.
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
from google.api_core import exceptions

from google.cloud import spanner_v1
from google.cloud.spanner_admin_database_v1 import DatabaseDialect


def test_table_exists(shared_database):
    table = shared_database.table("all_types")
    assert table.exists()


def test_table_exists_not_found(shared_database):
    table = shared_database.table("table_does_not_exist")
    assert not table.exists()


def test_table_exists_reload_database_dialect(
    shared_instance, shared_database, not_emulator
):
    database = shared_instance.database(shared_database.database_id)
    database.reload()
    assert database.database_dialect != DatabaseDialect.DATABASE_DIALECT_UNSPECIFIED
    table = database.table("all_types")
    assert table.exists()
    assert database.database_dialect != DatabaseDialect.DATABASE_DIALECT_UNSPECIFIED


def test_db_list_tables(shared_database):
    tables = shared_database.list_tables()
    table_ids = set(table.table_id for table in tables)
    assert "contacts" in table_ids
    # assert "contact_phones" in table_ids
    assert "all_types" in table_ids


def test_db_list_tables_reload(shared_database):
    for table in shared_database.list_tables():
        assert table.exists()
        schema = table.schema
        assert isinstance(schema, list)


def test_table_reload_miss(shared_database):
    table = shared_database.table("table_does_not_exist")
    with pytest.raises(exceptions.NotFound):
        table.reload()


def test_table_schema(shared_database, database_dialect):
    table = shared_database.table("all_types")
    schema = table.schema
    expected = [
        ("pkey", spanner_v1.TypeCode.INT64),
        ("int_value", spanner_v1.TypeCode.INT64),
        ("bool_value", spanner_v1.TypeCode.BOOL),
        ("bytes_value", spanner_v1.TypeCode.BYTES),
        ("float_value", spanner_v1.TypeCode.FLOAT64),
        ("string_value", spanner_v1.TypeCode.STRING),
        ("timestamp_value", spanner_v1.TypeCode.TIMESTAMP),
        ("date_value", spanner_v1.TypeCode.DATE),
        ("int_array", spanner_v1.TypeCode.ARRAY),
    ]
    expected = (
        expected[:-2] if database_dialect == DatabaseDialect.POSTGRESQL else expected
    )
    found = {field.name: field.type_.code for field in schema}

    for field_name, type_code in expected:
        assert found[field_name] == type_code
