# Copyright 2026 Google LLC All rights reserved.
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

from unittest import mock

from sqlalchemy.testing import eq_
from sqlalchemy.testing.plugin.plugin_base import fixtures

from google.cloud import spanner_dbapi
from google.cloud.sqlalchemy_spanner.sqlalchemy_spanner import (
    SpannerDialect,
    SpannerExecutionContext,
    reset_connection,
)


class SqlAlchemyTimeoutTest(fixtures.TestBase):
    def test_reset_connection_preserves_default_timeout(self):
        dbapi_conn = mock.MagicMock(spec=spanner_dbapi.Connection)
        dbapi_conn.timeout = 30.0
        dbapi_conn.inside_transaction = False

        reset_connection(dbapi_conn, None)

        eq_(dbapi_conn.timeout, 30.0)

    def test_pre_exec_sets_cursor_timeout(self):
        context = SpannerExecutionContext()
        context.execution_options = {"timeout": 45.0}
        context.cursor = mock.MagicMock()
        context.cursor.timeout = None

        dbapi_conn = mock.MagicMock(spec=spanner_dbapi.Connection)
        dbapi_conn.timeout = 25.0
        context._dbapi_connection = mock.MagicMock()
        context._dbapi_connection.connection = dbapi_conn

        context.pre_exec()

        eq_(context.cursor.timeout, 45.0)
        eq_(dbapi_conn.timeout, 25.0)

    def test_query_without_timeout_does_not_alter_cursor_or_connection_timeout(self):
        dialect = SpannerDialect()
        dbapi_conn = mock.MagicMock(spec=spanner_dbapi.Connection)
        dbapi_conn.timeout = 25.0

        context = SpannerExecutionContext()
        context.dialect = dialect
        context.execution_options = {}
        context.cursor = mock.MagicMock()
        context.cursor.timeout = None
        context._dbapi_connection = mock.MagicMock()
        context._dbapi_connection.connection = dbapi_conn

        context.pre_exec()

        eq_(context.cursor.timeout, None)
        eq_(dbapi_conn.timeout, 25.0)
