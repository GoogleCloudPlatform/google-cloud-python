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
import io
import sys
from unittest import mock

import pytest
from alembic.ddl import base as ddl_base
from sqlalchemy import (
    Column,
    Index,
    Integer,
    MetaData,
    String,
    Table,
    TextClause,
    event,
    exc,
    schema,
    text,
)
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
            assert not hasattr(module, "SpannerImpl")

    def test_visit_create_index_with_storing_columns(self):
        compiler = sqlalchemy_spanner.SpannerDDLCompiler(
            sqlalchemy_spanner.SpannerDialect(), None
        )
        t = Table("tbl", MetaData(), Column("c1", Integer), Column("c2", String(50)))
        idx = Index("ix_test", t.c.c1, spanner_storing=["c2"])
        ddl = compiler.visit_create_index(schema.CreateIndex(idx))
        eq_(ddl, "CREATE INDEX ix_test ON tbl (c1) STORING (c2)")

    def test_visit_create_index_with_storing_columns_missing_from_table(self):
        compiler = sqlalchemy_spanner.SpannerDDLCompiler(
            sqlalchemy_spanner.SpannerDialect(), None
        )
        # Mimics Alembic's op.create_index where table only has indexed columns
        t = Table("tbl", MetaData(), Column("c1", Integer))
        idx = Index("ix_test", t.c.c1, spanner_storing=["c2"])
        ddl = compiler.visit_create_index(schema.CreateIndex(idx))
        eq_(ddl, "CREATE INDEX ix_test ON tbl (c1) STORING (c2)")

    def test_spanner_impl_create_index_appends_missing_columns(self):
        from alembic.migration import MigrationContext

        dialect = sqlalchemy_spanner.SpannerDialect()
        impl = MigrationContext.configure(
            dialect=dialect, opts={"as_sql": True, "output_buffer": io.StringIO()}
        ).impl

        t = Table("tbl", MetaData(), Column("c1", Integer))
        idx = Index("ix_test", t.c.c1, spanner_storing=["c2", "c3"])
        assert "c2" not in t.c
        assert "c3" not in t.c

        impl.create_index(idx)
        assert "c2" in t.c
        assert "c3" in t.c

    def test_spanner_impl_compare_indexes(self):
        from alembic.migration import MigrationContext

        dialect = sqlalchemy_spanner.SpannerDialect()
        impl = MigrationContext.configure(dialect=dialect).impl

        t = Table(
            "tbl",
            MetaData(),
            Column("c1", Integer),
            Column("c2", String(50)),
            Column("c3", String(50)),
        )
        ix_no_storing = Index("ix", t.c.c1)
        ix_storing = Index("ix", t.c.c1, spanner_storing=["c2", "c3"])
        ix_reordered = Index("ix", t.c.c1, spanner_storing=["c3", "c2"])
        ix_different = Index("ix", t.c.c1, spanner_storing=["c2"])

        # Identical or reordered storing columns compare equal
        eq_(impl.compare_indexes(ix_no_storing, Index("ix", t.c.c1)).is_equal, True)
        eq_(
            impl.compare_indexes(
                ix_storing, Index("ix", t.c.c1, spanner_storing=["c2", "c3"])
            ).is_equal,
            True,
        )
        eq_(impl.compare_indexes(ix_storing, ix_reordered).is_equal, True)

        # Added, removed, or changed storing columns return is_different
        eq_(impl.compare_indexes(ix_storing, ix_no_storing).is_different, True)
        eq_(impl.compare_indexes(ix_no_storing, ix_storing).is_different, True)
        eq_(impl.compare_indexes(ix_storing, ix_different).is_different, True)

    def test_visit_create_index_with_column_objects_in_storing(self):
        compiler = sqlalchemy_spanner.SpannerDDLCompiler(
            sqlalchemy_spanner.SpannerDialect(), None
        )
        t = Table("tbl", MetaData(), Column("c1", Integer), Column("c2", String(50)))
        idx = Index("ix_test", t.c.c1, spanner_storing=[t.c.c2])
        ddl = compiler.visit_create_index(schema.CreateIndex(idx))
        eq_(ddl, "CREATE INDEX ix_test ON tbl (c1) STORING (c2)")

    def test_spanner_impl_compare_indexes_super_different(self):
        from alembic.migration import MigrationContext

        dialect = sqlalchemy_spanner.SpannerDialect()
        impl = MigrationContext.configure(dialect=dialect).impl

        t = Table(
            "tbl",
            MetaData(),
            Column("c1", Integer),
            Column("c2", Integer),
        )
        # Key column differs
        ix1 = Index("ix", t.c.c1)
        ix2 = Index("ix", t.c.c2)
        eq_(impl.compare_indexes(ix1, ix2).is_different, True)

        # Uniqueness differs
        ix_unique = Index("ix", t.c.c1, unique=True)
        ix_non_unique = Index("ix", t.c.c1, unique=False)
        eq_(impl.compare_indexes(ix_unique, ix_non_unique).is_different, True)

    def test_spanner_impl_compare_indexes_with_column_objects(self):
        from alembic.migration import MigrationContext

        dialect = sqlalchemy_spanner.SpannerDialect()
        impl = MigrationContext.configure(dialect=dialect).impl

        t = Table(
            "tbl",
            MetaData(),
            Column("c1", Integer),
            Column("c2", Integer),
        )
        ix1 = Index("ix", t.c.c1, spanner_storing=[t.c.c2])
        ix2 = Index("ix", t.c.c1, spanner_storing=["c2"])
        eq_(impl.compare_indexes(ix1, ix2).is_equal, True)

    def test_spanner_impl_create_index_edge_cases(self):
        from alembic.migration import MigrationContext

        dialect = sqlalchemy_spanner.SpannerDialect()
        impl = MigrationContext.configure(
            dialect=dialect, opts={"as_sql": True, "output_buffer": io.StringIO()}
        ).impl

        # 1. col already exists in table.c
        t1 = Table("tbl1", MetaData(), Column("c1", Integer), Column("c2", Integer))
        idx1 = Index("ix_test1", t1.c.c1, spanner_storing=["c2"])
        impl.create_index(idx1)
        eq_(len([c for c in t1.c if c.name == "c2"]), 1)

        # 2. col is a Column object not in table.c
        t2 = Table("tbl2", MetaData(), Column("c1", Integer))
        c_ext = Column("c_ext", Integer)
        idx2 = Index("ix_test2", t2.c.c1, spanner_storing=[c_ext])
        impl.create_index(idx2)
        assert "c_ext" in t2.c

        # 3. index.table is None
        idx3 = Index("ix_test3", text("c1"), spanner_storing=["c2"])
        idx3.table = None
        with pytest.raises(exc.CompileError):
            impl.create_index(idx3)
