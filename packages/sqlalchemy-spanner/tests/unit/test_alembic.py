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

import importlib.util
import sys
from unittest import mock

from alembic.ddl import base as ddl_base
from sqlalchemy import String, TextClause, event
from sqlalchemy.testing import eq_
from sqlalchemy.testing.plugin.plugin_base import fixtures

from google.cloud.sqlalchemy_spanner import sqlalchemy_spanner


class TestAlembicTest(fixtures.TestBase):
    def test_visit_column_nullable_with_not_null_column(self):
        ddl = sqlalchemy_spanner.visit_column_nullable(
            ddl_base.ColumnNullable(
                name="tbl", column_name="col", nullable=False, existing_type=String(256)
            ),
            sqlalchemy_spanner.SpannerDDLCompiler(
                sqlalchemy_spanner.SpannerDialect(), None
            ),
        )
        eq_(ddl, "ALTER TABLE tbl ALTER COLUMN col STRING(256) NOT NULL")

    def test_visit_column_nullable_with_nullable_column(self):
        ddl = sqlalchemy_spanner.visit_column_nullable(
            ddl_base.ColumnNullable(
                name="tbl", column_name="col", nullable=True, existing_type=String(256)
            ),
            sqlalchemy_spanner.SpannerDDLCompiler(
                sqlalchemy_spanner.SpannerDialect(), None
            ),
        )
        eq_(ddl, "ALTER TABLE tbl ALTER COLUMN col STRING(256)")

    def test_visit_column_nullable_with_default(self):
        ddl = sqlalchemy_spanner.visit_column_nullable(
            ddl_base.ColumnNullable(
                name="tbl",
                column_name="col",
                nullable=False,
                existing_type=String(256),
                existing_server_default=TextClause("GENERATE_UUID()"),
            ),
            sqlalchemy_spanner.SpannerDDLCompiler(
                sqlalchemy_spanner.SpannerDialect(), None
            ),
        )
        eq_(
            ddl,
            "ALTER TABLE tbl "
            "ALTER COLUMN col "
            "STRING(256) NOT NULL DEFAULT (GENERATE_UUID())",
        )

    def test_visit_column_type(self):
        ddl = sqlalchemy_spanner.visit_column_type(
            ddl_base.ColumnType(
                name="tbl",
                column_name="col",
                type_=String(256),
                existing_nullable=True,
            ),
            sqlalchemy_spanner.SpannerDDLCompiler(
                sqlalchemy_spanner.SpannerDialect(), None
            ),
        )
        eq_(ddl, "ALTER TABLE tbl ALTER COLUMN col STRING(256)")

    def test_visit_column_type_with_default(self):
        ddl = sqlalchemy_spanner.visit_column_type(
            ddl_base.ColumnType(
                name="tbl",
                column_name="col",
                type_=String(256),
                existing_nullable=False,
                existing_server_default=TextClause("GENERATE_UUID()"),
            ),
            sqlalchemy_spanner.SpannerDDLCompiler(
                sqlalchemy_spanner.SpannerDialect(), None
            ),
        )
        eq_(
            ddl,
            "ALTER TABLE tbl "
            "ALTER COLUMN col "
            "STRING(256) NOT NULL DEFAULT (GENERATE_UUID())",
        )

    def test_dialect_import_without_alembic(self):
        """Verify that sqlalchemy_spanner imports cleanly when Alembic is unavailable.

        Why we test this way instead of calling importlib.reload(sqlalchemy_spanner):
        1. Setting sys.modules["alembic.ddl.base"] = None via mock.patch.dict causes
           Python to raise ModuleNotFoundError (a subclass of ImportError) when
           sqlalchemy_spanner attempts to import from alembic.ddl.base.
        2. Calling importlib.reload(sqlalchemy_spanner) would re-execute the module
           in-place inside the existing sqlalchemy_spanner.__dict__. That has two
           undesirable side effects:
           - Functions defined during the initial import (like visit_column_nullable)
             remain in sqlalchemy_spanner.__dict__ even if skipped on reload.
           - Classes (like SpannerIdentifierPreparer) are recreated with new class
             identities in sqlalchemy_spanner.__dict__, which breaks other test
             modules (such as test_dialect.py) that already imported SpannerDialect
             before the reload and rely on super(SpannerIdentifierPreparer, self).
        3. Creating a fresh module object via importlib.util.module_from_spec and
           executing the loader into that isolated namespace tests a clean import
           without mutating the shared sqlalchemy_spanner module in sys.modules.
        """
        with mock.patch.dict(sys.modules, {"alembic.ddl.base": None}):
            module = importlib.util.module_from_spec(sqlalchemy_spanner.__spec__)
            sqlalchemy_spanner.__spec__.loader.exec_module(module)
            # Executing the module registers module.reset_connection on the shared
            # SQLAlchemy Pool class via @listens_for(Pool, "reset"); remove that
            # temporary listener so global Pool state stays clean for other tests.
            event.remove(sqlalchemy_spanner.Pool, "reset", module.reset_connection)
            assert not module.HAS_ALEMBIC_INSTALLED
            assert not hasattr(module, "visit_column_nullable")
