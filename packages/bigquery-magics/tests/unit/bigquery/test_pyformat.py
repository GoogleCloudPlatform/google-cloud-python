# Copyright 2025 Google LLC
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

from __future__ import annotations

from typing import List
from unittest import mock

import pytest
from IPython.testing import globalipapp


@pytest.mark.parametrize(
    ("sql_template", "expected"),
    (
        (
            "{my_project}.{my_dataset}.{my_table}",
            ["my_project", "my_dataset", "my_table"],
        ),
        (
            "{{not a format variable}}",
            [],
        ),
    ),
)
def test_parse_fields(sql_template: str, expected: List[str]):
    import bigquery_magics.pyformat

    fields = bigquery_magics.pyformat._parse_fields(sql_template)
    fields.sort()
    expected.sort()
    assert fields == expected


@pytest.mark.usefixtures("mock_credentials")
def test_pyformat_with_unsupported_type_raises_typeerror(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    ipython_ns_cleanup.extend(
        [
            (ip, "my_object"),
        ]
    )
    ip.user_ns["my_object"] = object()

    sql = "SELECT {my_object}"

    with pytest.raises(TypeError, match="my_object has unsupported type: "):
        ip.run_cell_magic("bigquery", "--pyformat", sql)


@pytest.mark.usefixtures("mock_credentials")
def test_pyformat_with_missing_variable_raises_keyerror():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    sql = "SELECT {my_object}"

    with pytest.raises(KeyError, match="my_object"):
        ip.run_cell_magic("bigquery", "--pyformat", sql)


@pytest.mark.usefixtures("mock_credentials")
def test_pyformat_with_no_variables():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    sql = "SELECT '{{escaped curly brackets}}'"
    expected_sql = "SELECT '{escaped curly brackets}'"

    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--pyformat", sql)
        run_query_mock.assert_called_once_with(mock.ANY, expected_sql, mock.ANY)


@pytest.mark.usefixtures("mock_credentials")
def test_pyformat_with_query_string_replaces_variables(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    ipython_ns_cleanup.extend(
        [
            # String
            (ip, "project"),
            (ip, "dataset"),
            (ip, "table"),
            (ip, "my_string"),
            # Float
            (ip, "max_value"),
            # Integer
            (ip, "year"),
            # Unused, unsupported types shouldn't raise.
            (ip, "my_object"),
        ]
    )
    ip.user_ns["project"] = "pyformat-project"
    ip.user_ns["dataset"] = "pyformat_dataset"
    ip.user_ns["table"] = "pyformat_table"
    ip.user_ns["my_string"] = "some string value"
    ip.user_ns["max_value"] = 2.25
    ip.user_ns["year"] = 2025
    ip.user_ns["my_object"] = object()

    sql = """
    SELECT {year} - year  AS age,
    @myparam AS myparam,
    '{{my_string}}' AS escaped_string,
    FROM `{project}.{dataset}.{table}`
    WHERE height < {max_value}
    """
    expected_sql = """
    SELECT 2025 - year  AS age,
    @myparam AS myparam,
    '{my_string}' AS escaped_string,
    FROM `pyformat-project.pyformat_dataset.pyformat_table`
    WHERE height < 2.25
    """.strip()

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--pyformat --params {'myparam': 42}", sql)
        run_query_mock.assert_called_once_with(mock.ANY, expected_sql, mock.ANY)


@pytest.mark.usefixtures("mock_credentials")
def test_pyformat_with_query_dollar_variable_replaces_variables(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    ipython_ns_cleanup.extend(
        [
            (ip, "custom_query"),
            (ip, "my_string"),
        ]
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    sql = "SELECT 42, '{my_string}'"
    expected_sql = "SELECT 42, 'This is a test'"
    ip.user_ns["my_string"] = "This is a test"
    ip.user_ns["custom_query"] = sql

    cell_body = "$custom_query"  # Referring to an existing variable name (custom_query)

    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--pyformat", cell_body)
        run_query_mock.assert_called_once_with(mock.ANY, expected_sql, mock.ANY)


@pytest.mark.usefixtures("mock_credentials")
def test_without_pyformat_doesnt_modify_curly_brackets(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    ipython_ns_cleanup.extend(
        [
            (ip, "my_string"),
        ]
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    sql = "SELECT 42, '{my_string}'"
    expected_sql = "SELECT 42, '{my_string}'"  # No pyformat means no escaping needed.
    ip.user_ns["my_string"] = "This is a test"

    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "", sql)
        run_query_mock.assert_called_once_with(mock.ANY, expected_sql, mock.ANY)
