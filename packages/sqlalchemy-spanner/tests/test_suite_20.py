# -*- coding: utf-8 -*-
#
# Copyright 2023 Google LLC
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

import decimal
import operator
import os
import random
import time
from datetime import timezone
from unittest import mock

import pytest
import sqlalchemy
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.spanner_v1 import Client, RequestOptions
from sqlalchemy import (
    FLOAT,
    Boolean,
    Float,
    ForeignKey,
    Index,
    LargeBinary,
    MetaData,
    String,
    create_engine,
    event,
    exists,
    inspect,
    literal,
    literal_column,
    select,
    testing,
    types,
    union,
    util,
)
from sqlalchemy.engine import Inspector, ObjectKind, ObjectScope
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship
from sqlalchemy.schema import DDL, Computed
from sqlalchemy.sql.expression import cast
from sqlalchemy.testing import (
    config,
    emits_warning,
    engines,
    eq_,
    fixtures,
    is_instance_of,
    is_true,
    provide_metadata,
    requires,
)
from sqlalchemy.testing.fixtures import (
    ComputedReflectionFixtureTest as _ComputedReflectionFixtureTest,
)
from sqlalchemy.testing.provision import temp_table_keyword_args
from sqlalchemy.testing.schema import Column, Table
from sqlalchemy.testing.suite.test_cte import *  # noqa: F401, F403
from sqlalchemy.testing.suite.test_cte import CTETest as _CTETest
from sqlalchemy.testing.suite.test_ddl import *  # noqa: F401, F403
from sqlalchemy.testing.suite.test_ddl import (
    FutureTableDDLTest as _FutureTableDDLTest,
)
from sqlalchemy.testing.suite.test_ddl import (
    LongNameBlowoutTest as _LongNameBlowoutTest,
)
from sqlalchemy.testing.suite.test_ddl import TableDDLTest as _TableDDLTest
from sqlalchemy.testing.suite.test_dialect import *  # noqa: F401, F403
from sqlalchemy.testing.suite.test_dialect import (
    DifficultParametersTest as _DifficultParametersTest,
)
from sqlalchemy.testing.suite.test_dialect import (
    EscapingTest as _EscapingTest,
)
from sqlalchemy.testing.suite.test_dialect import (
    ReturningGuardsTest as _ReturningGuardsTest,
)
from sqlalchemy.testing.suite.test_insert import *  # noqa: F401, F403
from sqlalchemy.testing.suite.test_insert import (
    InsertBehaviorTest as _InsertBehaviorTest,
)
from sqlalchemy.testing.suite.test_reflection import *  # noqa: F401, F403
from sqlalchemy.testing.suite.test_reflection import (
    ComponentReflectionTest as _ComponentReflectionTest,
)
from sqlalchemy.testing.suite.test_reflection import (  # noqa: F401, F403
    ComponentReflectionTestExtra as _ComponentReflectionTestExtra,
)
from sqlalchemy.testing.suite.test_reflection import (
    CompositeKeyReflectionTest as _CompositeKeyReflectionTest,
)
from sqlalchemy.testing.suite.test_reflection import (
    ComputedReflectionTest as _ComputedReflectionTest,
)
from sqlalchemy.testing.suite.test_reflection import (
    HasIndexTest as _HasIndexTest,
)
from sqlalchemy.testing.suite.test_reflection import (
    HasTableTest as _HasTableTest,
)
from sqlalchemy.testing.suite.test_reflection import (
    QuotedNameArgumentTest as _QuotedNameArgumentTest,
)
from sqlalchemy.testing.suite.test_results import *  # noqa: F401, F403
from sqlalchemy.testing.suite.test_results import (
    RowFetchTest as _RowFetchTest,
)
from sqlalchemy.testing.suite.test_select import (
    BitwiseTest as _BitwiseTest,
)  # noqa: F401, F403
from sqlalchemy.testing.suite.test_select import (  # noqa: F401, F403
    CompoundSelectTest as _CompoundSelectTest,
)
from sqlalchemy.testing.suite.test_select import (
    ExistsTest as _ExistsTest,
)
from sqlalchemy.testing.suite.test_select import (
    FetchLimitOffsetTest as _FetchLimitOffsetTest,
)
from sqlalchemy.testing.suite.test_select import (
    IdentityAutoincrementTest as _IdentityAutoincrementTest,
)
from sqlalchemy.testing.suite.test_select import (
    IsOrIsNotDistinctFromTest as _IsOrIsNotDistinctFromTest,
)
from sqlalchemy.testing.suite.test_select import (
    LikeFunctionsTest as _LikeFunctionsTest,
)
from sqlalchemy.testing.suite.test_select import (
    OrderByLabelTest as _OrderByLabelTest,
)
from sqlalchemy.testing.suite.test_select import (
    PostCompileParamsTest as _PostCompileParamsTest,
)
from sqlalchemy.testing.suite.test_select import (
    SameNamedSchemaTableTest as _SameNamedSchemaTableTest,
)
from sqlalchemy.testing.suite.test_sequence import (
    HasSequenceTest as _HasSequenceTest,
)
from sqlalchemy.testing.suite.test_sequence import (
    HasSequenceTestEmpty as _HasSequenceTestEmpty,
)
from sqlalchemy.testing.suite.test_sequence import (
    SequenceTest as _SequenceTest,
)  # noqa: F401, F403
from sqlalchemy.testing.suite.test_types import (  # noqa: F401, F403
    BooleanTest as _BooleanTest,
)  # noqa: F401, F403
from sqlalchemy.testing.suite.test_types import (
    DateTest as _DateTest,
)
from sqlalchemy.testing.suite.test_types import (
    DateTimeCoercedToDateTimeTest as _DateTimeCoercedToDateTimeTest,
)
from sqlalchemy.testing.suite.test_types import (  # noqa: F401
    DateTimeHistoricTest,
    TimestampMicrosecondsTest,
    _LiteralRoundTripFixture,
)
from sqlalchemy.testing.suite.test_types import (
    DateTimeMicrosecondsTest as _DateTimeMicrosecondsTest,
)
from sqlalchemy.testing.suite.test_types import (
    DateTimeTest as _DateTimeTest,
)
from sqlalchemy.testing.suite.test_types import (
    IntegerTest as _IntegerTest,
)
from sqlalchemy.testing.suite.test_types import (
    JSONTest as _JSONTest,
)
from sqlalchemy.testing.suite.test_types import (
    NumericTest as _NumericTest,
)
from sqlalchemy.testing.suite.test_types import (
    StringTest as _StringTest,
)
from sqlalchemy.testing.suite.test_types import (
    TextTest as _TextTest,
)
from sqlalchemy.testing.suite.test_types import (
    TimeMicrosecondsTest as _TimeMicrosecondsTest,
)
from sqlalchemy.testing.suite.test_types import (
    TimeTest as _TimeTest,
)
from sqlalchemy.testing.suite.test_types import (
    UnicodeTextTest as _UnicodeTextTest,
)
from sqlalchemy.testing.suite.test_types import (
    UnicodeVarcharTest as _UnicodeVarcharTest,
)
from sqlalchemy.testing.suite.test_types import (
    _DateFixture as __DateFixture,
)
from sqlalchemy.testing.suite.test_types import (
    _UnicodeFixture as __UnicodeFixture,
)
from sqlalchemy.testing.suite.test_unicode_ddl import *  # noqa: F401, F403
from sqlalchemy.testing.suite.test_update_delete import *  # noqa: F401, F403
from sqlalchemy.testing.suite.test_update_delete import (
    SimpleUpdateDeleteTest as _SimpleUpdateDeleteTest,
)
from sqlalchemy.types import Integer, Numeric, Text

from google.cloud import spanner_dbapi
from google.cloud.sqlalchemy_spanner import version as sqlalchemy_spanner_version
from tests._helpers import (
    get_db_url,
    get_project,
)

try:
    # SQLAlchemy 2.1+ removed test_deprecations from sqlalchemy.testing.suite.
    # Guard this import so the test suite remains compatible with both 2.0.x and 2.1+.
    # Tell flake8 to ignore F401 (unused import) and F403 (wildcard import) since
    # pytest discovers the imported SQLAlchemy compliance test classes at module scope.
    from sqlalchemy.testing.suite.test_deprecations import *  # noqa: F401, F403
except ModuleNotFoundError:
    pass

config.test_schema = ""


class BooleanTest(_BooleanTest):
    @pytest.mark.skip(
        "The original test case was split into 2 parts: "
        "test_render_literal_bool_true and test_render_literal_bool_false"
    )
    def test_render_literal_bool(self):
        pass

    def test_render_literal_bool_true(self, literal_round_trip_spanner):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        literal_round_trip_spanner(Boolean(), [True], [True])

    def test_render_literal_bool_false(self, literal_round_trip_spanner):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        literal_round_trip_spanner(Boolean(), [False], [False])

    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_whereclause(self):
        pass


class BitwiseTest(_BitwiseTest):
    @pytest.mark.skip("Causes too many problems with other tests")
    def test_bitwise(self, case, expected, connection):
        pass


class ComponentReflectionTestExtra(_ComponentReflectionTestExtra):
    @testing.requires.table_reflection
    def test_nullable_reflection(self, connection, metadata):
        t = Table(
            "t",
            metadata,
            Column("a", Integer, nullable=True),
            Column("b", Integer, nullable=False),
        )
        t.create(connection)
        connection.connection.commit()
        eq_(
            dict(
                (col["name"], col["nullable"])
                for col in inspect(connection).get_columns("t")
            ),
            {"a": True, "b": False},
        )

    def _type_round_trip(self, connection, metadata, *types):
        t = Table(
            "t", metadata, *[Column("t%d" % i, type_) for i, type_ in enumerate(types)]
        )
        t.create(connection)
        connection.connection.commit()

        return [c["type"] for c in inspect(connection).get_columns("t")]

    @testing.requires.table_reflection
    def test_numeric_reflection(self, connection, metadata):
        """
        SPANNER OVERRIDE:

        Spanner defines NUMERIC type with the constant precision=38
        and scale=9. Overriding the test to check if the NUMERIC
        column is successfully created and has dimensions
        correct for Cloud Spanner.
        """
        for typ in self._type_round_trip(connection, metadata, Numeric(18, 5)):
            assert isinstance(typ, Numeric)
            eq_(typ.precision, 38)
            eq_(typ.scale, 9)

    @testing.requires.table_reflection
    def test_binary_reflection(self, connection, metadata):
        """
        Check that a BYTES column with an explicitly
        set size is correctly reflected.
        """
        for typ in self._type_round_trip(connection, metadata, LargeBinary(20)):
            assert isinstance(typ, LargeBinary)
            eq_(typ.length, 20)

    @testing.requires.table_reflection
    def test_string_length_reflection(self, connection, metadata):
        typ = self._type_round_trip(connection, metadata, types.String(52))[0]
        assert isinstance(typ, types.String)


class ComputedReflectionFixtureTest(_ComputedReflectionFixtureTest):
    @classmethod
    def define_tables(cls, metadata):
        """SPANNER OVERRIDE:

        Avoid using default values for computed columns.
        """
        Table(
            "computed_default_table",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("normal", Integer),
            Column("computed_col", Integer, Computed("normal + 42")),
            Column("with_default", Integer),
        )

        t = Table(
            "computed_column_table",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("normal", Integer),
            Column("computed_no_flag", Integer, Computed("normal + 42")),
        )

        if testing.requires.computed_columns_virtual.enabled:
            t.append_column(
                Column(
                    "computed_virtual",
                    Integer,
                    Computed("normal + 2", persisted=False),
                )
            )
        if testing.requires.computed_columns_stored.enabled:
            t.append_column(
                Column(
                    "computed_stored",
                    Integer,
                    Computed("normal - 42", persisted=True),
                )
            )


class ComputedReflectionTest(_ComputedReflectionTest, ComputedReflectionFixtureTest):
    @testing.requires.schemas
    def test_get_column_returns_persisted_with_schema(self):
        insp = inspect(config.db)

        cols = insp.get_columns("computed_column_table", schema=config.test_schema)
        data = {c["name"]: c for c in cols}

        self.check_column(
            data,
            "computed_no_flag",
            "normal+42",
            testing.requires.computed_columns_default_persisted.enabled,
        )
        if testing.requires.computed_columns_virtual.enabled:
            self.check_column(
                data,
                "computed_virtual",
                "normal/2",
                False,
            )
        if testing.requires.computed_columns_stored.enabled:
            self.check_column(
                data,
                "computed_stored",
                "normal-42",
                True,
            )

    @pytest.mark.skip("Default values are not supported.")
    def test_computed_col_default_not_set(self):
        pass

    def test_get_column_returns_computed(self):
        """
        SPANNER OVERRIDE:

        In Spanner all the generated columns are STORED,
        meaning there are no persisted and not persisted
        (in the terms of the SQLAlchemy) columns. The
        method override omits the persistence reflection checks.
        """
        insp = inspect(config.db)

        cols = insp.get_columns("computed_default_table")
        data = {c["name"]: c for c in cols}
        for key in ("id", "normal", "with_default"):
            is_true("computed" not in data[key])
        compData = data["computed_col"]
        is_true("computed" in compData)
        is_true("sqltext" in compData["computed"])
        eq_(self.normalize(compData["computed"]["sqltext"]), "normal+42")

    def test_create_not_null_computed_column(self, connection):
        """
        SPANNER TEST:

        Check that on creating a computed column with a NOT NULL
        clause the clause is set in front of the computed column
        statement definition and doesn't cause failures.
        """
        metadata = MetaData()

        Table(
            "Singers",
            metadata,
            Column("SingerId", String(36), primary_key=True, nullable=False),
            Column("FirstName", String(200)),
            Column("LastName", String(200), nullable=False),
            Column(
                "FullName",
                String(400),
                Computed("COALESCE(FirstName || ' ', '') || LastName"),
                nullable=False,
            ),
        )

        metadata.create_all(connection)


class ComponentReflectionTest(_ComponentReflectionTest):
    @pytest.mark.skip("Skip")
    def test_not_existing_table(self, method, connection):
        pass

    @classmethod
    def define_tables(cls, metadata):
        cls.define_reflected_tables(metadata, None)

    @classmethod
    def define_views(cls, metadata, schema):
        table_info = {
            "dingalings": [
                "dingaling_id",
                "address_id",
                "data",
                "id_user",
            ],
            "users": ["user_id", "test1", "test2"],
            "email_addresses": ["address_id", "remote_user_id", "email_address"],
        }
        if testing.requires.self_referential_foreign_keys.enabled:
            table_info["users"] = table_info["users"] + ["parent_user_id"]
        if testing.requires.materialized_views.enabled:
            materialized = {"dingalings"}
        else:
            materialized = set()
        for table_name in ("users", "email_addresses", "dingalings"):
            fullname = table_name
            if schema:
                fullname = f"{schema}.{table_name}"
            view_name = fullname + "_v"
            prefix = "MATERIALIZED " if table_name in materialized else ""
            columns = ""
            for column in table_info[table_name]:
                stmt = table_name + "." + column + " AS " + column
                if columns:
                    columns = columns + ", " + stmt
                else:
                    columns = stmt
            query = f"""CREATE {prefix}VIEW {view_name}
                SQL SECURITY INVOKER
                AS SELECT {columns}
                FROM {fullname}"""

            event.listen(metadata, "after_create", DDL(query))
            if table_name in materialized:
                index_name = "mat_index"
                if schema and testing.against("oracle"):
                    index_name = f"{schema}.{index_name}"
                idx = f"CREATE INDEX {index_name} ON {view_name}(data)"
                event.listen(metadata, "after_create", DDL(idx))
            event.listen(metadata, "before_drop", DDL(f"DROP {prefix}VIEW {view_name}"))

    @classmethod
    def define_reflected_tables(cls, metadata, schema):
        if schema:
            schema_prefix = schema + "."
        else:
            schema_prefix = ""

        if testing.requires.self_referential_foreign_keys.enabled:
            users = Table(
                "users",
                metadata,
                Column("user_id", sqlalchemy.INT, primary_key=True),
                Column("test1", sqlalchemy.CHAR(5), nullable=False),
                Column("test2", sqlalchemy.Float(5), nullable=False),
                Column(
                    "parent_user_id",
                    sqlalchemy.Integer,
                    sqlalchemy.ForeignKey(
                        "%susers.user_id" % schema_prefix, name="user_id_fk"
                    ),
                ),
                schema=schema,
                test_needs_fk=True,
            )
        else:
            users = Table(
                "users",
                metadata,
                Column("user_id", sqlalchemy.INT, primary_key=True),
                Column("test1", sqlalchemy.CHAR(5), nullable=False),
                Column("test2", sqlalchemy.Float(5), nullable=False),
                schema=schema,
                test_needs_fk=True,
            )

        Table(
            "dingalings",
            metadata,
            Column("dingaling_id", sqlalchemy.Integer, primary_key=True),
            Column(
                "address_id",
                sqlalchemy.Integer,
                sqlalchemy.ForeignKey("%semail_addresses.address_id" % schema_prefix),
            ),
            Column(
                "id_user",
                sqlalchemy.Integer,
                sqlalchemy.ForeignKey("%susers.user_id" % schema_prefix),
            ),
            Column("data", sqlalchemy.String(30)),
            schema=schema,
            test_needs_fk=True,
        )
        Table(
            "email_addresses",
            metadata,
            Column("address_id", sqlalchemy.Integer, primary_key=True),
            Column(
                "remote_user_id",
                sqlalchemy.Integer,
                sqlalchemy.ForeignKey(users.c.user_id),
            ),
            Column("email_address", sqlalchemy.String(20)),
            sqlalchemy.PrimaryKeyConstraint("address_id", name="email_ad_pk"),
            schema=schema,
            test_needs_fk=True,
        )
        Table(
            "comment_test",
            metadata,
            Column("id", sqlalchemy.Integer, primary_key=True, comment="id comment"),
            Column("data", sqlalchemy.String(20), comment="data % comment"),
            Column(
                "d2",
                sqlalchemy.String(20),
                comment=r"""Comment types type speedily ' " \ '' Fun!""",
            ),
            schema=schema,
            comment=r"""the test % ' " \ table comment""",
        )
        Table(
            "no_constraints",
            metadata,
            Column("data", sqlalchemy.String(20)),
            schema=schema,
        )

        if testing.requires.cross_schema_fk_reflection.enabled:
            if schema is None:
                Table(
                    "local_table",
                    metadata,
                    Column("id", sqlalchemy.Integer, primary_key=True),
                    Column("data", sqlalchemy.String(20)),
                    Column(
                        "remote_id",
                        ForeignKey("%s.remote_table_2.id" % testing.config.test_schema),
                    ),
                    test_needs_fk=True,
                    schema=config.db.dialect.default_schema_name,
                )
            else:
                Table(
                    "remote_table",
                    metadata,
                    Column("id", sqlalchemy.Integer, primary_key=True),
                    Column(
                        "local_id",
                        ForeignKey(
                            "%s.local_table.id" % config.db.dialect.default_schema_name
                        ),
                    ),
                    Column("data", sqlalchemy.String(20)),
                    schema=schema,
                    test_needs_fk=True,
                )
                Table(
                    "remote_table_2",
                    metadata,
                    Column("id", sqlalchemy.Integer, primary_key=True),
                    Column("data", sqlalchemy.String(20)),
                    schema=schema,
                    test_needs_fk=True,
                )

        if testing.requires.index_reflection.enabled:
            sqlalchemy.Index("users_t_idx", users.c.test1, users.c.test2, unique=True)
            sqlalchemy.Index(
                "users_all_idx", users.c.user_id, users.c.test2, users.c.test1
            )

            if not schema:
                # test_needs_fk is at the moment to force MySQL InnoDB
                noncol_idx_test_nopk = Table(
                    "noncol_idx_test_nopk",
                    metadata,
                    Column("id", sqlalchemy.Integer, primary_key=True),
                    Column("q", sqlalchemy.String(5)),
                    test_needs_fk=True,
                    extend_existing=True,
                )

                noncol_idx_test_pk = Table(
                    "noncol_idx_test_pk",
                    metadata,
                    Column("id", sqlalchemy.Integer, primary_key=True),
                    Column("q", sqlalchemy.String(5)),
                    test_needs_fk=True,
                    extend_existing=True,
                )

                if testing.requires.indexes_with_ascdesc.enabled:
                    sqlalchemy.Index("noncol_idx_nopk", noncol_idx_test_nopk.c.q.desc())
                    sqlalchemy.Index("noncol_idx_pk", noncol_idx_test_pk.c.q.desc())

        if testing.requires.view_column_reflection.enabled and not bool(
            os.environ.get("SPANNER_EMULATOR_HOST")
        ):
            cls.define_views(metadata, schema)

    @testing.combinations(
        (False, False),
        (False, True, testing.requires.schemas),
        (True, False, testing.requires.view_reflection),
        (
            True,
            True,
            testing.requires.schemas + testing.requires.view_reflection,
        ),
        argnames="use_views,use_schema",
    )
    def test_get_columns(self, connection, use_views, use_schema):
        if use_views and bool(os.environ.get("SPANNER_EMULATOR_HOST")):
            pytest.skip("Skipped on emulator")

        schema = None

        users, addresses = (self.tables.users, self.tables.email_addresses)
        if use_views:
            table_names = ["users_v", "email_addresses_v", "dingalings_v"]
        else:
            table_names = ["users", "email_addresses"]

        insp = inspect(connection)
        for table_name, table in zip(table_names, (users, addresses)):
            schema_name = schema
            cols = insp.get_columns(table_name, schema=schema_name)
            is_true(len(cols) > 0, len(cols))

            # should be in order

            for i, col in enumerate(table.columns):
                eq_(col.name, cols[i]["name"])
                ctype = cols[i]["type"].__class__
                ctype_def = col.type
                if isinstance(ctype_def, sqlalchemy.types.TypeEngine):
                    ctype_def = ctype_def.__class__

                # Oracle returns Date for DateTime.

                if testing.against("oracle") and ctype_def in (
                    types.Date,
                    types.DateTime,
                ):
                    ctype_def = types.Date

                # assert that the desired type and return type share
                # a base within one of the generic types.

                is_true(
                    len(
                        set(ctype.__mro__)
                        .intersection(ctype_def.__mro__)
                        .intersection(
                            [
                                types.Integer,
                                types.Numeric,
                                types.Float,
                                types.DateTime,
                                types.Date,
                                types.Time,
                                types.String,
                                types._Binary,
                            ]
                        )
                    )
                    > 0,
                    "%s(%s), %s(%s)" % (col.name, col.type, cols[i]["name"], ctype),
                )

                if not col.primary_key:
                    assert cols[i]["default"] is None

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    @testing.requires.view_reflection
    def test_get_view_definition(
        self,
        connection,
    ):
        schema = None
        insp = inspect(connection)
        for view in ["users_v", "email_addresses_v", "dingalings_v"]:
            v = insp.get_view_definition(view, schema=schema)
            is_true(bool(v))

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    @testing.requires.view_reflection
    def test_get_view_definition_does_not_exist(self, connection):
        super().test_get_view_definition_does_not_exist(connection)

    def filter_name_values():
        return testing.combinations(True, False, argnames="use_filter")

    @filter_name_values()
    @testing.requires.index_reflection
    def test_get_multi_indexes(
        self,
        get_multi_exp,
        use_filter,
        schema=None,
        scope=ObjectScope.DEFAULT,
        kind=ObjectKind.TABLE,
    ):
        """
        SPANNER OVERRIDE:

        Spanner doesn't support indexes on views and
        doesn't support temporary tables, so real tables are
        used for testing. As the original test expects only real
        tables to be read, and in Spanner all the tables are real,
        expected results override is required.
        """
        insp, kws, exp = get_multi_exp(
            schema,
            scope,
            kind,
            use_filter,
            Inspector.get_indexes,
            self.exp_indexes,
        )
        _ignore_tables = [
            (None, "comment_test"),
            (None, "dingalings"),
            (None, "email_addresses"),
            (None, "no_constraints"),
        ]
        exp = {k: v for k, v in exp.items() if k not in _ignore_tables}

        for kw in kws:
            insp.clear_cache()
            result = insp.get_multi_indexes(**kw)
            self._check_table_dict(result, exp, self._required_index_keys)

    def exp_pks(
        self,
        schema=None,
        scope=ObjectScope.ANY,
        kind=ObjectKind.ANY,
        filter_names=None,
    ):
        def pk(*cols, name=mock.ANY, comment=None):
            return {
                "constrained_columns": list(cols),
                "name": name,
                "comment": comment,
            }

        empty = pk(name=None)
        if testing.requires.materialized_views_reflect_pk.enabled:
            materialized = {(schema, "dingalings_v"): pk("dingaling_id")}
        else:
            materialized = {(schema, "dingalings_v"): empty}
        views = {
            (schema, "email_addresses_v"): empty,
            (schema, "users_v"): empty,
            (schema, "user_tmp_v"): empty,
        }
        self._resolve_views(views, materialized)
        tables = {
            (schema, "users"): pk("user_id"),
            (schema, "dingalings"): pk("dingaling_id"),
            (schema, "email_addresses"): pk(
                "address_id", name="email_ad_pk", comment="ea pk comment"
            ),
            (schema, "comment_test"): pk("id"),
            (schema, "no_constraints"): empty,
            (schema, "local_table"): pk("id"),
            (schema, "remote_table"): pk("id"),
            (schema, "remote_table_2"): pk("id"),
            (schema, "noncol_idx_test_nopk"): pk("id"),
            (schema, "noncol_idx_test_pk"): pk("id"),
            (schema, self.temp_table_name()): pk("id"),
        }
        if not testing.requires.reflects_pk_names.enabled:
            for val in tables.values():
                if val["name"] is not None:
                    val["name"] = mock.ANY
        res = self._resolve_kind(kind, tables, views, materialized)
        res = self._resolve_names(schema, scope, filter_names, res)
        return res

    @filter_name_values()
    @testing.requires.primary_key_constraint_reflection
    def test_get_multi_pk_constraint(
        self,
        get_multi_exp,
        use_filter,
        schema=None,
        scope=ObjectScope.DEFAULT,
        kind=ObjectKind.TABLE,
    ):
        """
        SPANNER OVERRIDE:

        Spanner doesn't support temporary tables, so real tables are
        used for testing. As the original test expects only real
        tables to be read, and in Spanner all the tables are real,
        expected results override is required.
        """
        insp, kws, exp = get_multi_exp(
            schema,
            scope,
            kind,
            use_filter,
            Inspector.get_pk_constraint,
            self.exp_pks,
        )
        _ignore_tables = [(None, "no_constraints")]
        exp = {k: v for k, v in exp.items() if k not in _ignore_tables}

        for kw in kws:
            insp.clear_cache()
            result = insp.get_multi_pk_constraint(**kw)
            self._check_table_dict(result, exp, self._required_pk_keys, make_lists=True)

    def exp_fks(
        self,
        schema=None,
        scope=ObjectScope.ANY,
        kind=ObjectKind.ANY,
        filter_names=None,
    ):
        class tt:
            def __eq__(self, other):
                return other is None or config.db.dialect.default_schema_name == other

        def fk(
            cols,
            ref_col,
            ref_table,
            ref_schema=schema,
            name=mock.ANY,
            comment=None,
        ):
            return {
                "constrained_columns": cols,
                "referred_columns": ref_col,
                "name": name,
                "options": mock.ANY,
                "referred_schema": ref_schema if ref_schema is not None else tt(),
                "referred_table": ref_table,
                "comment": comment,
            }

        materialized = {}
        views = {}
        self._resolve_views(views, materialized)
        tables = {
            (schema, "users"): [
                fk(["parent_user_id"], ["user_id"], "users", name="user_id_fk")
            ],
            (schema, "dingalings"): [
                fk(["address_id"], ["address_id"], "email_addresses"),
                fk(["id_user"], ["user_id"], "users"),
            ],
            (schema, "email_addresses"): [fk(["remote_user_id"], ["user_id"], "users")],
            (schema, "local_table"): [
                fk(
                    ["remote_id"],
                    ["id"],
                    "remote_table_2",
                    ref_schema=config.test_schema,
                )
            ],
            (schema, "remote_table"): [
                fk(["local_id"], ["id"], "local_table", ref_schema=None)
            ],
        }
        if not testing.requires.self_referential_foreign_keys.enabled:
            tables[(schema, "users")].clear()
        if not testing.requires.named_constraints.enabled:
            for vals in tables.values():
                for val in vals:
                    if val["name"] is not mock.ANY:
                        val["name"] = mock.ANY

        res = self._resolve_kind(kind, tables, views, materialized)
        res = self._resolve_names(schema, scope, filter_names, res)
        return res

    @filter_name_values()
    @testing.requires.foreign_key_constraint_reflection
    def test_get_multi_foreign_keys(
        self,
        get_multi_exp,
        use_filter,
        schema=None,
        scope=ObjectScope.DEFAULT,
        kind=ObjectKind.TABLE,
    ):
        """
        SPANNER OVERRIDE:

        Spanner doesn't support temporary tables, so real tables are
        used for testing. As the original test expects only real
        tables to be read, and in Spanner all the tables are real,
        expected results override is required.
        """
        insp, kws, exp = get_multi_exp(
            schema,
            scope,
            kind,
            use_filter,
            Inspector.get_foreign_keys,
            self.exp_fks,
        )
        for kw in kws:
            insp.clear_cache()
            result = insp.get_multi_foreign_keys(**kw)
            self._adjust_sort(result, exp, lambda d: tuple(d["constrained_columns"]))
            self._check_table_dict(
                {
                    key: sorted(value, key=lambda x: x["constrained_columns"])
                    for key, value in result.items()
                },
                {
                    key: sorted(value, key=lambda x: x["constrained_columns"])
                    for key, value in exp.items()
                },
                self._required_fk_keys,
            )

    def test_get_foreign_keys_quoted_name(self, connection, metadata):
        pass

    def test_get_indexes_quoted_name(self, connection, metadata):
        pass

    def test_get_unique_constraints_quoted_name(self, connection, metadata):
        pass

    def exp_columns(
        self,
        schema=None,
        scope=ObjectScope.ANY,
        kind=ObjectKind.ANY,
        filter_names=None,
    ):
        def col(name, auto=False, default=mock.ANY, comment=None, nullable=True):
            res = {
                "name": name,
                "autoincrement": auto,
                "type": mock.ANY,
                "default": default,
                "comment": comment,
                "nullable": nullable,
            }
            if auto == "omit":
                res.pop("autoincrement")
            return res

        def pk(name, **kw):
            kw = {"auto": True, "default": mock.ANY, "nullable": False, **kw}
            return col(name, **kw)

        materialized = {
            (schema, "dingalings_v"): [
                col("dingaling_id", auto="omit", nullable=mock.ANY),
                col("address_id"),
                col("id_user"),
                col("data"),
            ]
        }
        views = {
            (schema, "email_addresses_v"): [
                col("address_id", auto="omit", nullable=mock.ANY),
                col("remote_user_id"),
                col("email_address"),
            ],
            (schema, "users_v"): [
                col("user_id", auto="omit", nullable=mock.ANY),
                col("test1", nullable=mock.ANY),
                col("test2", nullable=mock.ANY),
                col("parent_user_id"),
            ],
            (schema, "user_tmp_v"): [
                col("id", auto="omit", nullable=mock.ANY),
                col("name"),
                col("foo"),
            ],
        }
        self._resolve_views(views, materialized)
        tables = {
            (schema, "users"): [
                pk("user_id"),
                col("test1", nullable=False),
                col("test2", nullable=False),
                col("parent_user_id"),
            ],
            (schema, "dingalings"): [
                pk("dingaling_id"),
                col("address_id"),
                col("id_user"),
                col("data"),
            ],
            (schema, "email_addresses"): [
                pk("address_id"),
                col("remote_user_id"),
                col("email_address"),
            ],
            (schema, "comment_test"): [
                pk("id", comment="id comment"),
                col("data", comment="data % comment"),
                col(
                    "d2",
                    comment=r"""Comment types type speedily ' " \ '' Fun!""",
                ),
            ],
            (schema, "no_constraints"): [col("data")],
            (schema, "local_table"): [pk("id"), col("data"), col("remote_id")],
            (schema, "remote_table"): [pk("id"), col("local_id"), col("data")],
            (schema, "remote_table_2"): [pk("id"), col("data")],
            (schema, "noncol_idx_test_nopk"): [pk("id"), col("q")],
            (schema, "noncol_idx_test_pk"): [pk("id"), col("q")],
            (schema, self.temp_table_name()): [
                pk("id"),
                col("name"),
                col("foo"),
            ],
        }
        res = self._resolve_kind(kind, tables, views, materialized)
        res = self._resolve_names(schema, scope, filter_names, res)
        return res

    @filter_name_values()
    def test_get_multi_columns(
        self,
        get_multi_exp,
        use_filter,
        schema=None,
        scope=ObjectScope.DEFAULT,
        kind=ObjectKind.TABLE,
    ):
        """
        SPANNER OVERRIDE:

        Spanner doesn't support temporary tables, so real tables are
        used for testing. As the original test expects only real
        tables to be read, and in Spanner all the tables are real,
        expected results override is required.
        """
        _ignore_tables = [
            "bitwise",
        ]

        insp, kws, exp = get_multi_exp(
            schema,
            scope,
            kind,
            use_filter,
            Inspector.get_columns,
            self.exp_columns,
        )

        for kw in kws:
            insp.clear_cache()
            result = insp.get_multi_columns(**kw)
            for t in _ignore_tables:
                result.pop((schema, t), None)
            self._check_table_dict(result, exp, self._required_column_keys)

    @pytest.mark.skip(
        "Requires an introspection method to be implemented in SQLAlchemy first"
    )
    def test_get_multi_unique_constraints(self):
        pass

    @pytest.mark.skip(
        "Requires an introspection method to be implemented in SQLAlchemy first"
    )
    def test_get_multi_check_constraints(self):
        pass

    @testing.combinations((False,), argnames="use_schema")
    @testing.requires.foreign_key_constraint_reflection
    def test_get_foreign_keys(self, connection, use_schema):
        if use_schema:
            schema = config.test_schema
        else:
            schema = None

        users, addresses = (self.tables.users, self.tables.email_addresses)
        insp = inspect(connection)
        expected_schema = schema
        # users

        if testing.requires.self_referential_foreign_keys.enabled:
            users_fkeys = insp.get_foreign_keys(users.name, schema=schema)
            fkey1 = users_fkeys[0]

            with testing.requires.named_constraints.fail_if():
                eq_(fkey1["name"], "user_id_fk")

            eq_(fkey1["referred_schema"], expected_schema)
            eq_(fkey1["referred_table"], users.name)
            eq_(fkey1["referred_columns"], ["user_id"])
            if testing.requires.self_referential_foreign_keys.enabled:
                eq_(fkey1["constrained_columns"], ["parent_user_id"])

        # addresses
        addr_fkeys = insp.get_foreign_keys(addresses.name, schema=schema)
        fkey1 = addr_fkeys[0]

        with testing.requires.implicitly_named_constraints.fail_if():
            self.assert_(fkey1["name"] is not None)

        eq_(fkey1["referred_schema"], expected_schema)
        eq_(fkey1["referred_table"], users.name)
        eq_(fkey1["referred_columns"], ["user_id"])
        eq_(fkey1["constrained_columns"], ["remote_user_id"])

    @testing.combinations(
        None,
        ("foreign_key", testing.requires.foreign_key_constraint_reflection),
        argnames="order_by",
    )
    @testing.combinations(
        (True, testing.requires.schemas), False, argnames="use_schema"
    )
    def test_get_table_names(self, connection, order_by, use_schema):
        schema = None

        _ignore_tables = [
            "account",
            "alembic_version",
            "bitwise",
            "bytes_table",
            "comment_test",
            "date_table",
            "noncol_idx_test_pk",
            "noncol_idx_test_nopk",
            "local_table",
            "remote_table",
            "remote_table_2",
            "text_table",
            "user_tmp",
            "no_constraints",
        ]

        insp = inspect(connection)

        if order_by:
            tables = [
                rec[0] for rec in insp.get_sorted_table_and_fkc_names(schema) if rec[0]
            ]
        else:
            tables = insp.get_table_names(schema)
        table_names = [t for t in tables if t not in _ignore_tables]

        if order_by == "foreign_key":
            answer = ["users", "email_addresses", "dingalings"]
            eq_(table_names, answer)
        else:
            answer = ["dingalings", "email_addresses", "users"]
            eq_(sorted(table_names), answer)

    @classmethod
    def define_temp_tables(cls, metadata):
        """
        SPANNER OVERRIDE:

        In Cloud Spanner unique indexes are used instead of directly
        creating unique constraints. Overriding the test to replace
        constraints with indexes in testing data.
        """
        kw = temp_table_keyword_args(config, config.db)
        user_tmp = Table(
            "user_tmp",
            metadata,
            Column("id", sqlalchemy.INT, primary_key=True),
            Column("name", sqlalchemy.VARCHAR(50)),
            Column("foo", sqlalchemy.INT),
            sqlalchemy.Index("user_tmp_uq", "name", unique=True),
            sqlalchemy.Index("user_tmp_ix", "foo"),
            extend_existing=True,
            **kw,
        )
        if (
            testing.requires.view_reflection.enabled
            and testing.requires.temporary_views.enabled
        ):
            event.listen(
                user_tmp,
                "after_create",
                DDL("create temporary view user_tmp_v as select * from user_tmp"),
            )
            event.listen(user_tmp, "before_drop", DDL("drop view user_tmp_v"))

    @testing.provide_metadata
    def test_reflect_string_column_max_len(self, connection):
        """
        SPANNER SPECIFIC TEST:

        In Spanner column of the STRING type can be
        created with size defined as MAX. The test
        checks that such a column is correctly reflected.
        """
        metadata = MetaData()
        Table("text_table", metadata, Column("TestColumn", Text, nullable=False))
        metadata.create_all(connection)

        Table("text_table", metadata, autoload=True)

    def test_reflect_bytes_column_max_len(self, connection):
        """
        SPANNER SPECIFIC TEST:

        In Spanner column of the BYTES type can be
        created with size defined as MAX. The test
        checks that such a column is correctly reflected.
        """
        metadata = MetaData()
        Table(
            "bytes_table",
            metadata,
            Column("TestColumn", LargeBinary, nullable=False),
        )
        metadata.create_all(connection)

        Table("bytes_table", metadata, autoload=True)

    @testing.requires.unique_constraint_reflection
    def test_get_unique_constraints(self, metadata, connection, use_schema=False):
        # SQLite dialect needs to parse the names of the constraints
        # separately from what it gets from PRAGMA index_list(), and
        # then matches them up.  so same set of column_names in two
        # constraints will confuse it.    Perhaps we should no longer
        # bother with index_list() here since we have the whole
        # CREATE TABLE?

        if use_schema:
            schema = config.test_schema
        else:
            schema = None
        uniques = sorted(
            [
                {"name": "unique_a", "column_names": ["a"]},
                {"name": "unique_a_b_c", "column_names": ["a", "b", "c"]},
                {"name": "unique_c_a_b", "column_names": ["c", "a", "b"]},
                {"name": "unique_asc_key", "column_names": ["asc", "key"]},
                {"name": "i.have.dots", "column_names": ["b"]},
                {"name": "i have spaces", "column_names": ["c"]},
            ],
            key=operator.itemgetter("name"),
        )
        table = Table(
            "testtbl",
            metadata,
            Column("id", sqlalchemy.INT, primary_key=True),
            Column("a", String(20)),
            Column("b", String(30)),
            Column("c", Integer),
            # reserved identifiers
            Column("asc", String(30)),
            Column("key", String(30)),
            sqlalchemy.Index("unique_a", "a", unique=True),
            sqlalchemy.Index("unique_a_b_c", "a", "b", "c", unique=True),
            sqlalchemy.Index("unique_c_a_b", "c", "a", "b", unique=True),
            sqlalchemy.Index("unique_asc_key", "asc", "key", unique=True),
            schema=schema,
        )
        table.create(connection)
        connection.connection.commit()

        inspector = inspect(connection)
        reflected = sorted(
            inspector.get_unique_constraints("testtbl", schema=schema),
            key=operator.itemgetter("name"),
        )

        names_that_duplicate_index = set()

        for orig, refl in zip(uniques, reflected):
            # Different dialects handle duplicate index and constraints
            # differently, so ignore this flag
            dupe = refl.pop("duplicates_index", None)
            if dupe:
                names_that_duplicate_index.add(dupe)
            eq_(orig, refl)

        reflected_metadata = MetaData()
        reflected = Table(
            "testtbl",
            reflected_metadata,
            autoload_with=connection,
            schema=schema,
        )

        # test "deduplicates for index" logic.   MySQL and Oracle
        # "unique constraints" are actually unique indexes (with possible
        # exception of a unique that is a dupe of another one in the case
        # of Oracle).  make sure # they aren't duplicated.
        idx_names = set([idx.name for idx in reflected.indexes])
        uq_names = set(
            [
                uq.name
                for uq in reflected.constraints
                if isinstance(uq, sqlalchemy.UniqueConstraint)
            ]
        ).difference(["unique_c_a_b"])

        assert not idx_names.intersection(uq_names)
        if names_that_duplicate_index:
            eq_(names_that_duplicate_index, idx_names)
            eq_(uq_names, set())

    @testing.provide_metadata
    def test_unique_constraint_raises(self, connection):
        """
        Checking that unique constraint creation
        fails due to a ProgrammingError.
        """
        metadata = MetaData()
        Table(
            "user_tmp_failure",
            metadata,
            Column("id", sqlalchemy.INT, primary_key=True),
            Column("name", sqlalchemy.VARCHAR(50)),
            sqlalchemy.UniqueConstraint("name", name="user_tmp_uq"),
        )

        with pytest.raises(spanner_dbapi.exceptions.ProgrammingError):
            metadata.create_all(connection)

    @testing.provide_metadata
    def _test_get_table_names(self, schema=None, table_type="table", order_by=None):
        """
        SPANNER OVERRIDE:

        Spanner doesn't support temporary tables, so real tables are
        used for testing. As the original test expects only real
        tables to be read, and in Spanner all the tables are real,
        expected results override is required.
        """
        _ignore_tables = [
            "bitwise",
            "comment_test",
            "noncol_idx_test_pk",
            "noncol_idx_test_nopk",
            "local_table",
            "remote_table",
            "remote_table_2",
            "no_constraints",
        ]
        meta = self.metadata

        insp = inspect(meta.bind)

        if table_type == "view" and not bool(os.environ.get("SPANNER_EMULATOR_HOST")):
            table_names = insp.get_view_names(schema)
            table_names.sort()
            answer = ["email_addresses_v", "users_v"]
            eq_(sorted(table_names), answer)
        else:
            if order_by:
                tables = [
                    rec[0]
                    for rec in insp.get_sorted_table_and_fkc_names(schema)
                    if rec[0]
                ]
            else:
                tables = insp.get_table_names(schema)
            table_names = [t for t in tables if t not in _ignore_tables]

            if order_by == "foreign_key":
                answer = {"dingalings", "email_addresses", "user_tmp", "users"}
                eq_(set(table_names), answer)
            else:
                answer = ["dingalings", "email_addresses", "user_tmp", "users"]
                eq_(sorted(table_names), answer)

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    def test_get_view_names(self, connection, use_schema=False):
        insp = inspect(connection)
        schema = None
        table_names = insp.get_view_names(schema)
        if testing.requires.materialized_views.enabled:
            eq_(sorted(table_names), ["email_addresses_v", "users_v"])
            eq_(insp.get_materialized_view_names(schema), ["dingalings_v"])
        else:
            answer = ["dingalings_v", "email_addresses_v", "users_v"]
            eq_(sorted(table_names), answer)

    @pytest.mark.skip("Spanner doesn't support temporary tables")
    def test_get_temp_table_indexes(self):
        pass

    @pytest.mark.skip("Spanner doesn't support temporary tables")
    def test_get_temp_table_unique_constraints(self):
        pass

    @pytest.mark.skip("Spanner doesn't support temporary tables")
    def test_get_temp_table_columns(self):
        pass

    @pytest.mark.skip("Spanner doesn't support temporary tables")
    def test_reflect_table_temp_table(self, connection):
        pass

    def exp_indexes(
        self,
        schema=None,
        scope=ObjectScope.ANY,
        kind=ObjectKind.ANY,
        filter_names=None,
    ):
        def idx(
            *cols,
            name,
            unique=False,
            column_sorting=None,
            duplicates=False,
            fk=False,
        ):
            fk_req = testing.requires.foreign_keys_reflect_as_index
            dup_req = testing.requires.unique_constraints_reflect_as_index
            if (fk and not fk_req.enabled) or (duplicates and not dup_req.enabled):
                return ()
            res = {
                "unique": unique,
                "column_names": list(cols),
                "name": name,
                "dialect_options": mock.ANY,
                "include_columns": [],
            }
            if column_sorting:
                res["column_sorting"] = {"q": "desc"}
            if duplicates:
                res["duplicates_constraint"] = name
            return [res]

        materialized = {(schema, "dingalings_v"): []}
        views = {
            (schema, "email_addresses_v"): [],
            (schema, "users_v"): [],
            (schema, "user_tmp_v"): [],
        }
        self._resolve_views(views, materialized)
        if materialized:
            materialized[(schema, "dingalings_v")].extend(idx("data", name="mat_index"))
        tables = {
            (schema, "users"): [
                *idx("parent_user_id", name="user_id_fk", fk=True),
                *idx("user_id", "test2", "test1", name="users_all_idx"),
                *idx("test1", "test2", name="users_t_idx", unique=True),
            ],
            (schema, "dingalings"): [
                *idx("data", name=mock.ANY, unique=True, duplicates=True),
                *idx("id_user", name=mock.ANY, fk=True),
                *idx(
                    "address_id",
                    "dingaling_id",
                    name="zz_dingalings_multiple",
                    unique=True,
                    duplicates=True,
                ),
            ],
            (schema, "email_addresses"): [
                *idx("email_address", name=mock.ANY),
                *idx("remote_user_id", name=mock.ANY, fk=True),
            ],
            (schema, "comment_test"): [],
            (schema, "no_constraints"): [],
            (schema, "local_table"): [*idx("remote_id", name=mock.ANY, fk=True)],
            (schema, "remote_table"): [*idx("local_id", name=mock.ANY, fk=True)],
            (schema, "remote_table_2"): [],
            (schema, "noncol_idx_test_nopk"): [
                *idx(
                    "q",
                    name="noncol_idx_nopk",
                    column_sorting={"q": "desc"},
                )
            ],
            (schema, "noncol_idx_test_pk"): [
                *idx("q", name="noncol_idx_pk", column_sorting={"q": "desc"})
            ],
            (schema, self.temp_table_name()): [
                *idx("foo", name="user_tmp_ix"),
                *idx(
                    "name",
                    name=f"user_tmp_uq_{config.ident}",
                    duplicates=True,
                    unique=True,
                ),
            ],
        }
        if (
            not testing.requires.indexes_with_ascdesc.enabled
            or not testing.requires.reflect_indexes_with_ascdesc.enabled
        ):
            tables[(schema, "noncol_idx_test_nopk")].clear()
            tables[(schema, "noncol_idx_test_pk")].clear()
        res = self._resolve_kind(kind, tables, views, materialized)
        res = self._resolve_names(schema, scope, filter_names, res)
        return res

    def _check_list(self, result, exp, req_keys=None, msg=None):
        if req_keys is None:
            eq_(result, exp, msg)
        else:
            eq_(len(result), len(exp), msg)
            for r, e in zip(result, exp):
                for k in set(r) | set(e):
                    if (k in req_keys and (k in r and k in e)) or (k in r and k in e):
                        if isinstance(r[k], list):
                            r[k].sort()
                            e[k].sort()
                        eq_(r[k], e[k], f"{msg} - {k} - {r}")

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    @testing.combinations(True, False, argnames="use_schema")
    @testing.combinations((True, testing.requires.views), False, argnames="views")
    def test_metadata(self, connection, use_schema, views):
        m = MetaData()
        schema = None
        m.reflect(connection, schema=schema, views=views, resolve_fks=False)

        insp = inspect(connection)
        tables = insp.get_table_names(schema)
        if views:
            tables += insp.get_view_names(schema)
            try:
                tables += insp.get_materialized_view_names(schema)
            except NotImplementedError:
                pass
        if schema is not None:
            tables = [f"{schema}.{t}" for t in tables]
        eq_(sorted(m.tables), sorted(tables))


class CompositeKeyReflectionTest(_CompositeKeyReflectionTest):
    @testing.requires.foreign_key_constraint_reflection
    def test_fk_column_order(self, connection):
        """
        SPANNER OVERRIDE:

        Spanner column usage reflection doesn't support determenistic
        ordering. Overriding the test to check that columns are
        reflected correctly, without considering their order.
        """
        # test for issue #5661
        insp = inspect(connection)
        foreign_keys = insp.get_foreign_keys(self.tables.tb2.name)
        eq_(len(foreign_keys), 1)
        fkey1 = foreign_keys[0]
        eq_(set(fkey1.get("referred_columns")), {"name", "id", "attr"})
        eq_(set(fkey1.get("constrained_columns")), {"pname", "pid", "pattr"})


@pytest.mark.skip("Spanner doesn't support quotes in table names.")
class QuotedNameArgumentTest(_QuotedNameArgumentTest):
    pass


class _DateFixture(__DateFixture):
    compare = None

    @classmethod
    def define_tables(cls, metadata):
        """
        SPANNER OVERRIDE:

        Cloud Spanner doesn't support auto incrementing ids feature,
        which is used by the original test. Overriding the test data
        creation method to disable autoincrement and make id column
        nullable.
        """

        class Decorated(sqlalchemy.TypeDecorator):
            impl = cls.datatype
            cache_ok = True

        Table(
            "date_table",
            metadata,
            Column("id", Integer, primary_key=True, nullable=True),
            Column("date_data", cls.datatype),
            Column("decorated_date_data", Decorated),
        )


class DateTest(_DateTest):
    """
    SPANNER OVERRIDE:

    DateTest tests used same class method to create table, so to avoid those failures
    and maintain DRY concept just inherit the class to run tests successfully.
    """

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    def test_null_bound_comparison(self):
        super().test_null_bound_comparison()

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    def test_null(self, connection):
        super().test_null(connection)


class CTETest(_CTETest):
    @classmethod
    def define_tables(cls, metadata):
        """
        The original method creates a foreign key without a name,
        which causes troubles on test cleanup. Overriding the
        method to explicitly set a foreign key name.
        """
        Table(
            "some_table",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("data", String(50)),
            Column("parent_id", ForeignKey("some_table.id", name="fk_some_table")),
        )

        Table(
            "some_other_table",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("data", String(50)),
            Column("parent_id", Integer),
        )

    @pytest.mark.skip("INSERT from WITH subquery is not supported")
    def test_insert_from_select_round_trip(self):
        """
        The test checks if an INSERT can be done from a cte, like:

        WITH some_cte AS (...)
        INSERT INTO some_other_table (... SELECT * FROM some_cte)

        Such queries are not supported by Spanner.
        """
        pass

    @pytest.mark.skip("DELETE from WITH subquery is not supported")
    def test_delete_scalar_subq_round_trip(self):
        """
        The test checks if a DELETE can be done from a cte, like:

        WITH some_cte AS (...)
        DELETE FROM some_other_table (... SELECT * FROM some_cte)

        Such queries are not supported by Spanner.
        """
        pass

    @pytest.mark.skip("DELETE from WITH subquery is not supported")
    def test_delete_from_round_trip(self):
        """
        The test checks if a DELETE can be done from a cte, like:

        WITH some_cte AS (...)
        DELETE FROM some_other_table (... SELECT * FROM some_cte)

        Such queries are not supported by Spanner.
        """
        pass

    @pytest.mark.skip("UPDATE from WITH subquery is not supported")
    def test_update_from_round_trip(self):
        """
        The test checks if an UPDATE can be done from a cte, like:

        WITH some_cte AS (...)
        UPDATE some_other_table
        SET (... SELECT * FROM some_cte)

        Such queries are not supported by Spanner.
        """
        pass

    @pytest.mark.skip("WITH RECURSIVE subqueries are not supported")
    def test_select_recursive_round_trip(self):
        pass


class DateTimeMicrosecondsTest(_DateTimeMicrosecondsTest, DateTest):
    @pytest.mark.skip("Spanner dates are time zone independent")
    def test_select_direct(self):
        pass

    def test_round_trip(self):
        """
        SPANNER OVERRIDE:

        Spanner converts timestamp into `%Y-%m-%dT%H:%M:%S.%fZ` format, so to avoid
        assert failures convert datetime input to the desire timestamp format.
        """
        date_table = self.tables.date_table

        with config.db.connect() as connection:
            connection.execute(date_table.insert(), {"date_data": self.data, "id": 250})
            row = connection.execute(select(date_table.c.date_data)).first()

        compare = self.compare or self.data.astimezone(timezone.utc)
        compare = compare.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        eq_(row[0].rfc3339(), compare)
        assert isinstance(row[0], DatetimeWithNanoseconds)

    def test_round_trip_decorated(self, connection):
        """
        SPANNER OVERRIDE:

        Spanner converts timestamp into `%Y-%m-%dT%H:%M:%S.%fZ` format, so to avoid
        assert failures convert datetime input to the desire timestamp format.
        """
        date_table = self.tables.date_table

        connection.execute(
            date_table.insert(), {"id": 1, "decorated_date_data": self.data}
        )

        row = connection.execute(select(date_table.c.decorated_date_data)).first()

        compare = self.compare or self.data.astimezone(timezone.utc)
        compare = compare.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        eq_(row[0].rfc3339(), compare)
        assert isinstance(row[0], DatetimeWithNanoseconds)

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    def test_null_bound_comparison(self):
        super().test_null_bound_comparison()

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    def test_null(self, connection):
        super().test_null(connection)


class DateTimeTest(_DateTimeTest, DateTimeMicrosecondsTest):
    """
    SPANNER OVERRIDE:

    DateTimeTest tests have the same failures same as DateTimeMicrosecondsTest tests,
    so to avoid those failures and maintain DRY concept just inherit the class to run
    tests successfully.
    """

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    def test_null_bound_comparison(self):
        super().test_null_bound_comparison()

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    def test_null(self, connection):
        super().test_null(connection)

    @pytest.mark.skip("Spanner dates are time zone independent")
    def test_select_direct(self):
        pass


@pytest.mark.skip("Not supported by Spanner")
class DifficultParametersTest(_DifficultParametersTest):
    pass


class FetchLimitOffsetTest(_FetchLimitOffsetTest):
    @pytest.mark.skip("Spanner doesn't support composite LIMIT and OFFSET clauses")
    def test_expr_limit(self, connection):
        pass

    @pytest.mark.skip("Spanner doesn't support composite LIMIT and OFFSET clauses")
    def test_expr_offset(self, connection):
        pass

    @pytest.mark.skip("Spanner doesn't support composite LIMIT and OFFSET clauses")
    def test_expr_limit_offset(self, connection):
        pass

    @pytest.mark.skip("Spanner doesn't support composite LIMIT and OFFSET clauses")
    def test_expr_limit_simple_offset(self, connection):
        pass

    @pytest.mark.skip("Spanner doesn't support composite LIMIT and OFFSET clauses")
    def test_simple_limit_expr_offset(self, connection):
        pass

    @pytest.mark.skip("Spanner doesn't support composite LIMIT and OFFSET clauses")
    def test_bound_offset(self, connection):
        pass

    @pytest.mark.skipif(
        bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
    )
    def test_limit_render_multiple_times(self, connection):
        table = self.tables.some_table
        stmt = select(table.c.id).limit(1).scalar_subquery()

        u = union(select(stmt), select(stmt)).subquery().select()

        self._assert_result(
            connection,
            u,
            [(1,)],
        )

    @testing.requires.offset
    def test_simple_offset(self, connection):
        table = self.tables.some_table
        self._assert_result(
            connection,
            select(table).order_by(table.c.id).offset(2),
            [(3, 3, 4), (4, 4, 5), (5, 4, 6)],
        )


@pytest.mark.skip("Spanner doesn't support autoincrement")
class IdentityAutoincrementTest(_IdentityAutoincrementTest):
    pass


@pytest.mark.skip("Spanner doesn't support returning")
class ReturningGuardsTest(_ReturningGuardsTest):
    pass


@pytest.mark.skip("Spanner doesn't support user made schemas")
class SameNamedSchemaTableTest(_SameNamedSchemaTableTest):
    pass


class EscapingTest(_EscapingTest):
    @provide_metadata
    def test_percent_sign_round_trip(self):
        """Test that the DBAPI accommodates for escaped / nonescaped
        percent signs in a way that matches the compiler

        SPANNER OVERRIDE
        Cloud Spanner supports tables with empty primary key, but
        only single one row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        m = self.metadata
        t = Table("t", m, Column("data", String(50)))
        t.create(config.db)
        with config.db.begin() as conn:
            conn.execute(t.insert(), dict(data="some % value"))

            eq_(
                conn.scalar(
                    select(t.c.data).where(t.c.data == literal_column("'some % value'"))
                ),
                "some % value",
            )

            conn.execute(t.delete())
            conn.execute(t.insert(), dict(data="some %% other value"))
            eq_(
                conn.scalar(
                    select(t.c.data).where(
                        t.c.data == literal_column("'some %% other value'")
                    )
                ),
                "some %% other value",
            )


class ExistsTest(_ExistsTest):
    def test_select_exists(self, connection):
        """
        SPANNER OVERRIDE:

        The original test is trying to execute a query like:

        SELECT ...
        WHERE EXISTS (SELECT ...)

        SELECT WHERE without FROM clause is not supported by Spanner.
        Rewriting the test to force it to generate a query like:

        SELECT EXISTS (SELECT ...)
        """
        stuff = self.tables.stuff
        eq_(
            connection.execute(
                select(exists().where(stuff.c.data == "some data"))
            ).fetchall(),
            [(True,)],
        )

    def test_select_exists_false(self, connection):
        """
        SPANNER OVERRIDE:

        The original test is trying to execute a query like:

        SELECT ...
        WHERE EXISTS (SELECT ...)

        SELECT WHERE without FROM clause is not supported by Spanner.
        Rewriting the test to force it to generate a query like:

        SELECT EXISTS (SELECT ...)
        """
        stuff = self.tables.stuff
        eq_(
            connection.execute(
                select(exists().where(stuff.c.data == "no data"))
            ).fetchall(),
            [(False,)],
        )


class TableDDLTest(_TableDDLTest):
    @pytest.mark.skip(
        "Spanner table name must start with an uppercase or lowercase letter"
    )
    def test_underscore_names(self):
        pass

    @pytest.mark.skip("Table names incuding schemas are not supported by Spanner")
    def test_create_table_schema(self):
        pass


class FutureTableDDLTest(_FutureTableDDLTest):
    @pytest.mark.skip("Table names incuding schemas are not supported by Spanner")
    def test_create_table_schema(self):
        pass

    @pytest.mark.skip(
        "Spanner table name must start with an uppercase or lowercase letter"
    )
    def test_underscore_names(self):
        pass


@pytest.mark.skip("Max identifier length in Spanner is 128")
class LongNameBlowoutTest(_LongNameBlowoutTest):
    pass


@pytest.mark.skip("Spanner doesn't support Time data type.")
class TimeTests(_TimeMicrosecondsTest, _TimeTest):
    pass


@pytest.mark.skip("Spanner doesn't coerce dates from datetime.")
class DateTimeCoercedToDateTimeTest(_DateTimeCoercedToDateTimeTest):
    pass


class IntegerTest(_IntegerTest):
    @provide_metadata
    def _round_trip(self, datatype, data):
        """
        SPANNER OVERRIDE:

        This is the helper method for integer class tests which creates a table and
        performs an insert operation.
        Cloud Spanner supports tables with an empty primary key, but only one
        row can be inserted into such a table - following insertions will fail with
        `400 id must not be NULL in table date_table`.
        Overriding the tests and adding a manual primary key value to avoid the same
        failures.
        """
        metadata = self.metadata
        int_table = Table(
            "integer_table",
            metadata,
            Column("id", Integer, primary_key=True, test_needs_autoincrement=True),
            Column("integer_data", datatype),
        )

        metadata.create_all(config.db)

        config.db.execute(int_table.insert(), {"id": 1, "integer_data": data})

        row = config.db.execute(select(int_table.c.integer_data)).first()

        eq_(row, (data,))

        if util.py3k:
            assert isinstance(row[0], int)
        else:
            assert isinstance(row[0], (long, int))  # noqa

    def _huge_ints():
        return testing.combinations(
            2147483649,  # 32 bits
            2147483648,  # 32 bits
            2147483647,  # 31 bits
            2147483646,  # 31 bits
            -2147483649,  # 32 bits
            -2147483648,  # 32 interestingly, asyncpg accepts this one as int32
            -2147483647,  # 31
            -2147483646,  # 31
            0,
            1376537018368127,
            -1376537018368127,
            argnames="intvalue",
        )

    @_huge_ints()
    def test_huge_int_auto_accommodation(self, connection, intvalue):
        """
        Spanner does not allow query to have FROM clause without a WHERE clause
        """
        eq_(
            connection.scalar(select(intvalue)),
            intvalue,
        )

    def test_literal(self, literal_round_trip_spanner):
        literal_round_trip_spanner(Integer, [5], [5])


class _UnicodeFixture(__UnicodeFixture):
    @classmethod
    def define_tables(cls, metadata):
        """
        SPANNER OVERRIDE:

        Cloud Spanner doesn't support auto incrementing ids feature,
        which is used by the original test. Overriding the test data
        creation method to disable autoincrement and make id column
        nullable.
        """
        Table(
            "unicode_table",
            metadata,
            Column("id", Integer, primary_key=True, nullable=True),
            Column("unicode_data", cls.datatype),
        )

    def test_round_trip_executemany(self, connection):
        """
        SPANNER OVERRIDE

        Cloud Spanner supports tables with empty primary key, but
        only single one row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        unicode_table = self.tables.unicode_table

        connection.execute(
            unicode_table.insert(),
            [{"id": i, "unicode_data": self.data} for i in range(1, 4)],
        )

        rows = connection.execute(select(unicode_table.c.unicode_data)).fetchall()
        eq_(rows, [(self.data,) for i in range(1, 4)])
        for row in rows:
            assert isinstance(row[0], str)

    @pytest.mark.skip("Spanner doesn't support non-ascii characters")
    def test_literal(self):
        pass

    @pytest.mark.skip("Spanner doesn't support non-ascii characters")
    def test_literal_non_ascii(self):
        pass


class UnicodeVarcharTest(_UnicodeFixture, _UnicodeVarcharTest):
    """
    SPANNER OVERRIDE:

    UnicodeVarcharTest class inherits the __UnicodeFixture class's tests,
    so to avoid those failures and maintain DRY concept just inherit the class to run
    tests successfully.
    """

    pass


class UnicodeTextTest(_UnicodeFixture, _UnicodeTextTest):
    """
    SPANNER OVERRIDE:

    UnicodeTextTest class inherits the __UnicodeFixture class's tests,
    so to avoid those failures and maintain DRY concept just inherit the class to run
    tests successfully.
    """

    pass


class RowFetchTest(_RowFetchTest):
    def test_row_w_scalar_select(self, connection):
        """
        SPANNER OVERRIDE:

        Cloud Spanner returns a DatetimeWithNanoseconds() for date
        data types. Overriding the test to use a DatetimeWithNanoseconds
        type value as an expected result.
        --------------

        test that a scalar select as a column is returned as such
        and that type conversion works OK.

        (this is half a SQLAlchemy Core test and half to catch database
        backends that may have unusual behavior with scalar selects.)
        """
        datetable = self.tables.has_dates
        s = select(datetable.alias("x").c.today).scalar_subquery()
        s2 = select(datetable.c.id, s.label("somelabel"))
        row = connection.execute(s2).first()

        eq_(
            row.somelabel,
            DatetimeWithNanoseconds(2006, 5, 12, 12, 0, 0).astimezone(timezone.utc),
        )


class InsertBehaviorTest(_InsertBehaviorTest):
    @pytest.mark.skip("Spanner doesn't support empty inserts")
    def test_empty_insert(self):
        pass

    @pytest.mark.skip("Spanner doesn't support empty inserts")
    def test_empty_insert_multiple(self):
        pass

    @pytest.mark.skip("Spanner doesn't support auto increment")
    def test_insert_from_select_autoinc(self):
        pass

    @pytest.mark.skip("Spanner does not support auto increment")
    def test_no_results_for_non_returning_insert(self, connection, style, executemany):
        pass

    def test_autoclose_on_insert(self):
        """
        SPANNER OVERRIDE:

        Cloud Spanner doesn't support tables with an auto increment primary key,
        following insertions will fail with `400 id must not be NULL in table
        autoinc_pk`.

        Overriding the tests and adding a manual primary key value to avoid the same
        failures.
        """
        if (
            hasattr(config.requirements, "returning")
            and config.requirements.returning.enabled
        ):
            engine = engines.testing_engine(options={"implicit_returning": False})
        else:
            engine = config.db

        with engine.begin() as conn:
            r = conn.execute(
                self.tables.autoinc_pk.insert(), dict(id=1, data="some data")
            )

        assert r._soft_closed
        assert not r.closed
        assert r.is_insert
        assert not r.returns_rows

    def test_autoclose_on_insert_implicit_returning(self, connection):
        """
        SPANNER OVERRIDE:

        Cloud Spanner doesn't support tables with an auto increment primary key,
        following insertions will fail with `400 id must not be NULL in table
        autoinc_pk`.

        Overriding the tests and adding a manual primary key value to avoid the same
        failures.
        """
        r = connection.execute(
            # return_defaults() ensures RETURNING will be used,
            # new in 2.0 as sqlite/mariadb offer both RETURNING and
            # cursor.lastrowid
            self.tables.autoinc_pk.insert().return_defaults(),
            dict(id=2, data="some data"),
        )
        assert r._soft_closed
        assert not r.closed
        assert r.is_insert

        # Spanner does not return any rows in this case, because the primary key
        # is not auto-generated.
        assert not r.returns_rows


class BytesTest(_LiteralRoundTripFixture, fixtures.TestBase):
    __backend__ = True

    def test_nolength_binary(self):
        metadata = MetaData()
        foo = Table("foo", metadata, Column("one", LargeBinary))

        foo.create(config.db)
        foo.drop(config.db)


class StringTest(_StringTest):
    @pytest.mark.skip("Spanner doesn't support non-ascii characters")
    def test_literal_non_ascii(self):
        pass

    def test_dont_truncate_rightside(
        self, metadata, connection, expr=None, expected=None
    ):
        t = Table(
            "t",
            metadata,
            Column("x", String(2)),
            Column("id", Integer, primary_key=True),
        )
        t.create(connection)
        connection.connection.commit()
        connection.execute(
            t.insert(),
            [{"x": "AB", "id": 1}, {"x": "BC", "id": 2}, {"x": "AC", "id": 3}],
        )
        combinations = [("%B%", ["AB", "BC"]), ("A%C", ["AC"]), ("A%C%Z", [])]

        for args in combinations:
            eq_(
                connection.scalars(select(t.c.x).where(t.c.x.like(args[0]))).all(),
                args[1],
            )

    def test_literal(self, literal_round_trip_spanner):
        # note that in Python 3, this invokes the Unicode
        # datatype for the literal part because all strings are unicode
        literal_round_trip_spanner(String(40), ["some text"], ["some text"])

    def test_literal_quoting(self, literal_round_trip_spanner):
        data = """some 'text' hey "hi there" that's text"""
        literal_round_trip_spanner(String(40), [data], [data])

    def test_literal_backslashes(self, literal_round_trip_spanner):
        data = r"backslash one \ backslash two \\ end"
        literal_round_trip_spanner(String(40), [data], [data])


class TextTest(_TextTest):
    @classmethod
    def define_tables(cls, metadata):
        """
        SPANNER OVERRIDE:

        Cloud Spanner doesn't support auto incrementing ids feature,
        which is used by the original test. Overriding the test data
        creation method to disable autoincrement and make id column
        nullable.
        """
        Table(
            "text_table",
            metadata,
            Column("id", Integer, primary_key=True, nullable=True),
            Column("text_data", Text),
        )

    @pytest.mark.skip("Spanner doesn't support non-ascii characters")
    def test_literal_non_ascii(self):
        pass

    @pytest.mark.skip("Not supported by Spanner")
    def test_text_roundtrip(self, connection):
        pass

    @pytest.mark.skip("Not supported by Spanner")
    def test_text_empty_strings(self, connection):
        pass

    @pytest.mark.skip("Not supported by Spanner")
    def test_text_null_strings(self, connection):
        pass

    def test_literal(self, literal_round_trip_spanner):
        literal_round_trip_spanner(Text, ["some text"], ["some text"])

    def test_literal_quoting(self, literal_round_trip_spanner):
        data = """some 'text' hey "hi there" that's text"""
        literal_round_trip_spanner(Text, [data], [data])

    def test_literal_backslashes(self, literal_round_trip_spanner):
        data = r"backslash one \ backslash two \\ end"
        literal_round_trip_spanner(Text, [data], [data])

    def test_literal_percentsigns(self, literal_round_trip_spanner):
        data = r"percent % signs %% percent"
        literal_round_trip_spanner(Text, [data], [data])


class NumericTest(_NumericTest):
    @testing.fixture
    def do_numeric_test(self, metadata, connection):
        @testing.emits_warning(r".*does \*not\* support Decimal objects natively")
        def run(type_, input_, output, filter_=None, check_scale=False):
            t = Table(
                "t",
                metadata,
                Column("x", type_),
                Column("id", Integer, primary_key=True),
            )
            t.create(connection)
            connection.connection.commit()
            connection.execute(
                t.insert(), [{"x": x, "id": i} for i, x in enumerate(input_)]
            )

            result = {row[0] for row in connection.execute(t.select())}
            output = set(output)
            if filter_:
                result = set(filter_(x) for x in result)
                output = set(filter_(x) for x in output)
            eq_(result, output)
            if check_scale:
                eq_([str(x) for x in result], [str(x) for x in output])

        return run

    @emits_warning(r".*does \*not\* support Decimal objects natively")
    def test_render_literal_numeric(self, literal_round_trip_spanner):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        literal_round_trip_spanner(
            Numeric(precision=8, scale=4),
            [decimal.Decimal("15.7563")],
            [decimal.Decimal("15.7563")],
        )

    @emits_warning(r".*does \*not\* support Decimal objects natively")
    def test_render_literal_numeric_asfloat(self, literal_round_trip_spanner):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        literal_round_trip_spanner(
            Numeric(precision=8, scale=4, asdecimal=False),
            [decimal.Decimal("15.7563")],
            [15.7563],
        )

    def test_render_literal_float(self, literal_round_trip_spanner):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        literal_round_trip_spanner(
            Float(4),
            [decimal.Decimal("15.7563")],
            [15.7563],
            filter_=lambda n: n is not None and round(n, 5) or None,
        )

    @requires.precision_generic_float_type
    def test_float_custom_scale(self, do_numeric_test):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        do_numeric_test(
            Float(None, decimal_return_scale=7, asdecimal=True),
            [decimal.Decimal("15.7563827"), decimal.Decimal("15.7563827")],
            [decimal.Decimal("15.7563827")],
            check_scale=True,
        )

    def test_numeric_as_decimal(self, do_numeric_test):
        """
        SPANNER OVERRIDE:

        Spanner throws an error 400 Value has type FLOAT64 which cannot be
        inserted into column x, which has type NUMERIC for value 15.7563.
        Overriding the test to remove the failure case.
        """
        do_numeric_test(
            Numeric(precision=8, scale=4),
            [decimal.Decimal("15.7563"), decimal.Decimal("15.7563")],
            [decimal.Decimal("15.7563")],
        )

    def test_numeric_as_float(self, do_numeric_test):
        """
        SPANNER OVERRIDE:

        Spanner throws an error 400 Value has type FLOAT64 which cannot be
        inserted into column x, which has type NUMERIC for value 15.7563.
        Overriding the test to remove the failure case.
        """
        do_numeric_test(
            Numeric(precision=8, scale=4, asdecimal=False),
            [decimal.Decimal("15.7563"), decimal.Decimal("15.7563")],
            [15.7563],
        )

    @requires.floats_to_four_decimals
    def test_float_as_decimal(self, do_numeric_test):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        do_numeric_test(
            Float(precision=8, asdecimal=True),
            [decimal.Decimal("15.7563"), decimal.Decimal("15.7563"), None],
            [decimal.Decimal("15.7563"), None],
            filter_=lambda n: n is not None and round(n, 4) or None,
        )

    def test_float_as_float(self, do_numeric_test):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        do_numeric_test(
            Float(precision=8),
            [decimal.Decimal("15.7563"), decimal.Decimal("15.7563")],
            [15.7563],
            filter_=lambda n: n is not None and round(n, 5) or None,
        )

    @testing.requires.literal_float_coercion
    def test_float_coerce_round_trip(self, connection):
        expr = 15.7563

        val = connection.scalar(select(cast(literal(expr), FLOAT)))
        eq_(val, expr)

    @requires.precision_numerics_general
    def test_precision_decimal(self, do_numeric_test):
        """
        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.

        Remove an extra digits after decimal point as cloud spanner is
        capable of representing an exact numeric value with a precision
        of 38 and scale of 9.
        """
        numbers = set(
            [
                decimal.Decimal("54.246451650"),
                decimal.Decimal("0.004354"),
                decimal.Decimal("900.0"),
            ]
        )
        do_numeric_test(Numeric(precision=18, scale=9), numbers, numbers)

    @testing.requires.precision_numerics_enotation_large
    def test_enotation_decimal_large(self, do_numeric_test):
        """test exceedingly large decimals.

        SPANNER OVERRIDE:

        Cloud Spanner supports tables with an empty primary key, but
        only a single row can be inserted into such a table -
        following insertions will fail with `Row [] already exists".
        Overriding the test to avoid the same failure.
        """
        numbers = set(
            [
                decimal.Decimal("4E+8"),
                decimal.Decimal("5748E+15"),
                decimal.Decimal("1.521E+15"),
                decimal.Decimal("000000000.1E+9"),
            ]
        )
        do_numeric_test(Numeric(precision=25, scale=2), numbers, numbers)

    @testing.requires.precision_numerics_enotation_large
    def test_enotation_decimal(self, do_numeric_test):
        """test exceedingly small decimals.

        Decimal reports values with E notation when the exponent
        is greater than 6.

        SPANNER OVERRIDE:

        Remove extra digits after decimal point as Cloud Spanner is
        capable of representing an exact numeric value with a precision
        of 38 and scale of 9.
        """
        numbers = set(
            [
                decimal.Decimal("1E-2"),
                decimal.Decimal("1E-3"),
                decimal.Decimal("1E-4"),
                decimal.Decimal("1E-5"),
                decimal.Decimal("1E-6"),
                decimal.Decimal("1E-7"),
                decimal.Decimal("1E-8"),
                decimal.Decimal("0.105940696"),
                decimal.Decimal("0.005940696"),
                decimal.Decimal("0.000000696"),
                decimal.Decimal("0.700000696"),
                decimal.Decimal("696E-9"),
            ]
        )
        do_numeric_test(Numeric(precision=38, scale=9), numbers, numbers)


class LikeFunctionsTest(_LikeFunctionsTest):
    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_contains_autoescape(self):
        pass

    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_contains_autoescape_escape(self):
        pass

    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_contains_escape(self):
        pass

    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_endswith_autoescape(self):
        pass

    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_endswith_escape(self):
        pass

    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_endswith_autoescape_escape(self):
        pass

    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_startswith_autoescape(self):
        pass

    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_startswith_escape(self):
        pass

    @pytest.mark.skip("Spanner doesn't support LIKE ESCAPE clause")
    def test_startswith_autoescape_escape(self):
        pass

    def test_escape_keyword_raises(self):
        """Check that ESCAPE keyword causes an exception when used."""
        with pytest.raises(NotImplementedError):
            col = self.tables.some_table.c.data
            self._test(col.contains("b##cde", escape="#"), {7})


@pytest.mark.skip("Spanner doesn't support IS DISTINCT FROM clause")
class IsOrIsNotDistinctFromTest(_IsOrIsNotDistinctFromTest):
    pass


@pytest.mark.skip("Spanner doesn't bizarre characters in foreign key names")
class BizarroCharacterFKResolutionTest(fixtures.TestBase):
    pass


class BizarroCharacterTest(fixtures.TestBase):
    @pytest.mark.skip("Bizarre characters in foreign key names are not supported")
    def test_fk_ref(self, testing_engine):
        pass


class IsolationLevelTest(fixtures.TestBase):
    @pytest.mark.skip("Cloud Spanner does not support different isolation levels")
    def test_dialect_user_setting_is_restored(self, testing_engine):
        pass


class OrderByLabelTest(_OrderByLabelTest):
    @pytest.mark.skip(
        "Spanner requires an alias for the GROUP BY list when specifying derived "
        "columns also used in SELECT"
    )
    def test_group_by_composed(self):
        pass


class CompoundSelectTest(_CompoundSelectTest):
    """
    See: https://github.com/googleapis/python-spanner/issues/347
    """

    @pytest.mark.skip(
        "Spanner DBAPI incorrectly classify the statement starting with brackets."
    )
    def test_limit_offset_selectable_in_unions(self):
        pass

    @pytest.mark.skip(
        "Spanner DBAPI incorrectly classify the statement starting with brackets."
    )
    def test_order_by_selectable_in_unions(self):
        pass


class TestQueryHints(fixtures.TablesTest):
    """
    Compile a complex query with JOIN and check that
    the table hint was set into the right place.
    """

    __backend__ = True

    def test_complex_query_table_hints(self):
        EXPECTED_QUERY = (
            "SELECT users.id, users.name \nFROM users @{FORCE_INDEX=table_1_by_int_idx}"
            " JOIN addresses ON users.id = addresses.user_id "
            "\nWHERE users.name IN (__[POSTCOMPILE_name_1])"
        )

        Base = declarative_base()
        engine = create_engine(
            "spanner:///projects/project-id/instances/instance-id/databases/database-id"
        )

        class User(Base):
            __tablename__ = "users"
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            addresses = relationship("Address", backref="user")

        class Address(Base):
            __tablename__ = "addresses"
            id = Column(Integer, primary_key=True)
            email = Column(String(50))
            user_id = Column(Integer, ForeignKey("users.id"))

        session = Session(engine)

        query = session.query(User)
        query = query.with_hint(
            selectable=User, text="@{FORCE_INDEX=table_1_by_int_idx}"
        )

        query = query.filter(User.name.in_(["val1", "val2"]))
        query = query.join(Address)

        assert str(query.statement.compile(session.bind)) == EXPECTED_QUERY


class InterleavedTablesTest(fixtures.TestBase):
    """
    Check that CREATE TABLE statements for interleaved tables are correctly
    generated.
    """

    def setUp(self):
        self._engine = create_engine(
            "spanner:///projects/appdev-soda-spanner-staging/instances/"
            "sqlalchemy-dialect-test/databases/compliance-test"
        )
        self._metadata = MetaData()

    def test_interleave(self):
        EXP_QUERY = (
            "\nCREATE TABLE client (\n\tteam_id INT64 NOT NULL, "
            "\n\tclient_id INT64 NOT NULL, "
            "\n\tclient_name STRING(16) NOT NULL"
            "\n) PRIMARY KEY (team_id, client_id),"
            "\nINTERLEAVE IN PARENT team\n\n"
        )
        client = Table(
            "client",
            self._metadata,
            Column("team_id", Integer, primary_key=True),
            Column("client_id", Integer, primary_key=True),
            Column("client_name", String(16), nullable=False),
            spanner_interleave_in="team",
        )
        with mock.patch("google.cloud.spanner_dbapi.cursor.Cursor.execute") as execute:
            client.create(self._engine)
            execute.assert_called_once_with(EXP_QUERY, [])

    def test_interleave_on_delete_cascade(self):
        EXP_QUERY = (
            "\nCREATE TABLE client (\n\tteam_id INT64 NOT NULL, "
            "\n\tclient_id INT64 NOT NULL, "
            "\n\tclient_name STRING(16) NOT NULL"
            "\n) PRIMARY KEY (team_id, client_id),"
            "\nINTERLEAVE IN PARENT team ON DELETE CASCADE\n\n"
        )
        client = Table(
            "client",
            self._metadata,
            Column("team_id", Integer, primary_key=True),
            Column("client_id", Integer, primary_key=True),
            Column("client_name", String(16), nullable=False),
            spanner_interleave_in="team",
            spanner_interleave_on_delete_cascade=True,
        )
        with mock.patch("google.cloud.spanner_dbapi.cursor.Cursor.execute") as execute:
            client.create(self._engine)
            execute.assert_called_once_with(EXP_QUERY, [])


class UserAgentTest(fixtures.TestBase):
    """Check that SQLAlchemy dialect uses correct user agent."""

    def setUp(self):
        self._engine = create_engine(
            "spanner:///projects/appdev-soda-spanner-staging/instances/"
            "sqlalchemy-dialect-test/databases/compliance-test"
        )
        self._metadata = MetaData()

    def test_user_agent(self):
        with self._engine.connect() as connection:
            assert (
                connection.connection.instance._client._client_info.user_agent
                == f"gl-sqlalchemy-spanner/{sqlalchemy_spanner_version.__version__}"
            )


class SimpleUpdateDeleteTest(_SimpleUpdateDeleteTest):
    """
    SPANNER OVERRIDE:

    Spanner doesn't support `rowcount` property. These
    test cases overrides omit `rowcount` checks.
    """

    def test_delete(self, connection):
        t = self.tables.plain_pk
        r = connection.execute(t.delete().where(t.c.id == 2))
        assert not r.is_insert
        assert not r.returns_rows
        eq_(
            connection.execute(t.select().order_by(t.c.id)).fetchall(),
            [(1, "d1"), (3, "d3")],
        )

    def test_update(self, connection):
        t = self.tables.plain_pk
        r = connection.execute(t.update().where(t.c.id == 2), dict(data="d2_new"))
        assert not r.is_insert
        assert not r.returns_rows

        eq_(
            connection.execute(t.select().order_by(t.c.id)).fetchall(),
            [(1, "d1"), (2, "d2_new"), (3, "d3")],
        )


class HasIndexTest(_HasIndexTest):
    __backend__ = True
    kind = testing.combinations("dialect", "inspector", argnames="kind")

    @classmethod
    def define_tables(cls, metadata):
        tt = Table(
            "test_table",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("data", String(50)),
            Column("data2", String(50)),
        )
        sqlalchemy.Index("my_idx", tt.c.data)

    @kind
    def test_has_index(self, kind, connection, metadata):
        meth = self._has_index(kind, connection)
        assert meth("test_table", "my_idx")
        assert not meth("test_table", "my_idx_s")
        assert not meth("nonexistent_table", "my_idx")
        assert not meth("test_table", "nonexistent_idx")

        assert not meth("test_table", "my_idx_2")
        assert not meth("test_table_2", "my_idx_3")
        idx = Index("my_idx_2", self.tables.test_table.c.data2)
        tbl = Table(
            "test_table_2",
            metadata,
            Column("foo", Integer, primary_key=True),
            Index("my_idx_3", "foo"),
        )
        idx.create(connection)
        tbl.create(connection)

        try:
            if kind == "inspector":
                assert not meth("test_table", "my_idx_2")
                assert not meth("test_table_2", "my_idx_3")
                meth.__self__.clear_cache()
            connection.connection.commit()
            assert meth("test_table", "my_idx_2") is True
            assert meth("test_table_2", "my_idx_3") is True
        finally:
            tbl.drop(connection)
            idx.drop(connection)
            connection.connection.commit()
            self.tables["test_table"].indexes.remove(idx)

    @pytest.mark.skip("Not supported by Cloud Spanner")
    @kind
    def test_has_index_schema(self, kind, connection):
        pass


class HasTableTest(_HasTableTest):
    @classmethod
    def define_tables(cls, metadata):
        Table(
            "test_table",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("data", String(50)),
        )

    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_table_nonexistent_schema(self):
        pass

    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_table_schema(self):
        pass

    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_multi_table_schema(self):
        pass

    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_table_cache(self):
        pass

    @testing.requires.views
    def test_has_table_view(self, connection):
        pass

    @testing.requires.views
    def test_has_table_view_schema(self, connection):
        pass


class PostCompileParamsTest(_PostCompileParamsTest):
    def test_execute(self):
        table = self.tables.some_table

        stmt = select(table.c.id).where(
            table.c.x == sqlalchemy.bindparam("q", literal_execute=True)
        )

        with self.sql_execution_asserter() as asserter:
            with config.db.connect() as conn:
                conn.execute(stmt, dict(q=10))

        asserter.assert_(
            sqlalchemy.testing.assertsql.CursorSQL(
                "SELECT some_table.id \nFROM some_table \nWHERE some_table.x = 10",
                [] if config.db.dialect.positional else {},
            )
        )

    def test_execute_expanding_plus_literal_execute(self):
        table = self.tables.some_table

        stmt = select(table.c.id).where(
            table.c.x.in_(
                sqlalchemy.bindparam("q", expanding=True, literal_execute=True)
            )
        )

        with self.sql_execution_asserter() as asserter:
            with config.db.connect() as conn:
                conn.execute(stmt, dict(q=[5, 6, 7]))

        asserter.assert_(
            sqlalchemy.testing.assertsql.CursorSQL(
                "SELECT some_table.id \nFROM some_table "
                "\nWHERE some_table.x IN (5, 6, 7)",
                [] if config.db.dialect.positional else {},
            )
        )

    @testing.requires.tuple_in
    def test_execute_tuple_expanding_plus_literal_execute(self):
        table = self.tables.some_table

        stmt = select(table.c.id).where(
            sqlalchemy.tuple_(table.c.x, table.c.y).in_(
                sqlalchemy.bindparam("q", expanding=True, literal_execute=True)
            )
        )

        with self.sql_execution_asserter() as asserter:
            with config.db.connect() as conn:
                conn.execute(stmt, dict(q=[(5, 10), (12, 18)]))

        asserter.assert_(
            sqlalchemy.testing.assertsql.CursorSQL(
                "SELECT some_table.id \nFROM some_table "
                "\nWHERE (some_table.x, some_table.y) "
                "IN (%s(5, 10), (12, 18))"
                % ("VALUES " if config.db.dialect.tuple_in_values else ""),
                () if config.db.dialect.positional else {},
            )
        )

    @testing.requires.tuple_in
    def test_execute_tuple_expanding_plus_literal_heterogeneous_execute(self):
        table = self.tables.some_table

        stmt = select(table.c.id).where(
            sqlalchemy.tuple_(table.c.x, table.c.z).in_(
                sqlalchemy.bindparam("q", expanding=True, literal_execute=True)
            )
        )

        with self.sql_execution_asserter() as asserter:
            with config.db.connect() as conn:
                conn.execute(stmt, dict(q=[(5, "z1"), (12, "z3")]))

        asserter.assert_(
            sqlalchemy.testing.assertsql.CursorSQL(
                "SELECT some_table.id \nFROM some_table "
                "\nWHERE (some_table.x, some_table.z) "
                "IN (%s(5, 'z1'), (12, 'z3'))"
                % ("VALUES " if config.db.dialect.tuple_in_values else ""),
                () if config.db.dialect.positional else {},
            )
        )


@pytest.mark.skipif(
    bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
)
class JSONTest(_JSONTest):
    @pytest.mark.skip("Values without keys are not supported.")
    def test_single_element_round_trip(self, element):
        pass

    def _test_round_trip(self, data_element, connection):
        data_table = self.tables.data_table

        connection.execute(
            data_table.insert(),
            {"id": random.randint(1, 100000000), "name": "row1", "data": data_element},
        )

        row = connection.execute(select(data_table.c.data)).first()

        eq_(row, (data_element,))

    def test_unicode_round_trip(self):
        # note we include Unicode supplementary characters as well
        with config.db.connect() as conn:
            conn.execute(
                self.tables.data_table.insert(),
                {
                    "id": random.randint(1, 100000000),
                    "name": "r1",
                    "data": {
                        "réve🐍 illé": "réve🐍 illé",
                        "data": {"k1": "drôl🐍e"},
                    },
                },
            )

            eq_(
                conn.scalar(select(self.tables.data_table.c.data)),
                {
                    "réve🐍 illé": "réve🐍 illé",
                    "data": {"k1": "drôl🐍e"},
                },
            )

    @pytest.mark.skip("Parameterized types are not supported.")
    def test_eval_none_flag_orm(self):
        pass

    @pytest.mark.skip(
        "Spanner JSON_VALUE() always returns STRING, "
        "thus, this test case can't be executed."
    )
    def test_index_typed_comparison(self):
        pass

    @pytest.mark.skip(
        "Spanner JSON_VALUE() always returns STRING, "
        "thus, this test case can't be executed."
    )
    def test_path_typed_comparison(self):
        pass

    @pytest.mark.skip(
        "Spanner JSON_VALUE() always returns STRING, "
        "thus, this test case can't be executed."
    )
    def test_index_cross_casts(self):
        pass

    @pytest.mark.skip("Custom JSON de-/serializers are not supported.")
    def test_round_trip_custom_json(self):
        pass

    def _index_fixtures(fn):
        fn = testing.combinations(
            ("boolean", True),
            ("boolean", False),
            ("boolean", None),
            ("string", "some string"),
            ("string", None),
            ("integer", 15),
            ("integer", 1),
            ("integer", 0),
            ("integer", None),
            ("float", 28.5),
            ("float", None),
            id_="sa",
        )(fn)
        return fn

    @_index_fixtures
    def test_index_typed_access(self, datatype, value):
        data_table = self.tables.data_table
        data_element = {"key1": value}
        with config.db.connect() as conn:
            conn.execute(
                data_table.insert(),
                {
                    "id": random.randint(1, 100000000),
                    "name": "row1",
                    "data": data_element,
                    "nulldata": data_element,
                },
            )

            expr = data_table.c.data["key1"]
            expr = getattr(expr, "as_%s" % datatype)()

            roundtrip = conn.scalar(select(expr))
            if roundtrip in ("true", "false", None):
                roundtrip = str(roundtrip).capitalize()

            eq_(str(roundtrip), str(value))

    @pytest.mark.skip(
        "Spanner doesn't support type casts inside JSON_VALUE() function."
    )
    def test_round_trip_json_null_as_json_null(self):
        pass

    @pytest.mark.skip(
        "Spanner doesn't support type casts inside JSON_VALUE() function."
    )
    def test_round_trip_none_as_json_null(self):
        pass

    @pytest.mark.skip(
        "Spanner doesn't support type casts inside JSON_VALUE() function."
    )
    def test_round_trip_none_as_sql_null(self):
        pass


class ExecutionOptionsRequestPriorotyTest(fixtures.TestBase):
    def setUp(self):
        self._engine = create_engine(get_db_url(), pool_size=1)
        metadata = MetaData()

        self._table = Table(
            "execution_options2",
            metadata,
            Column("opt_id", Integer, primary_key=True),
            Column("opt_name", String(16), nullable=False),
        )

        metadata.create_all(self._engine)
        time.sleep(1)

    def test_request_priority(self):
        PRIORITY = RequestOptions.Priority.PRIORITY_MEDIUM
        with self._engine.connect().execution_options(
            request_priority=PRIORITY
        ) as connection:
            connection.execute(select(self._table)).fetchall()

        with self._engine.connect() as connection:
            assert connection.connection.request_priority is None

        engine = create_engine("sqlite:///database")
        with engine.connect() as connection:
            pass


class CreateEngineWithClientObjectTest(fixtures.TestBase):
    def test_create_engine_w_valid_client_object(self):
        """
        SPANNER TEST:

        Check that we can connect to SqlAlchemy
        by passing custom Client object.
        """
        client = Client(project=get_project())
        engine = create_engine(get_db_url(), connect_args={"client": client})
        with engine.connect() as connection:
            assert connection.connection.instance._client == client

    def test_create_engine_w_invalid_client_object(self):
        """
        SPANNER TEST:

        Check that if project id in url and custom Client
        Object passed to enginer mismatch, error is thrown.
        """
        client = Client(project="project_id")
        engine = create_engine(get_db_url(), connect_args={"client": client})

        with pytest.raises(ValueError):
            engine.connect()


class CreateEngineWithoutDatabaseTest(fixtures.TestBase):
    def test_create_engine_wo_database(self):
        """
        SPANNER TEST:

        Check that we can connect to SqlAlchemy
        without passing database id in the
        connection URL.
        """
        engine = create_engine(get_db_url().split("/database")[0])
        with engine.connect() as connection:
            assert connection.connection.database is None


class ReturningTest(fixtures.TestBase):
    def setUp(self):
        self._engine = create_engine(get_db_url())
        metadata = MetaData()

        self._table = Table(
            "returning_test",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("data", String(16), nullable=False),
        )

        metadata.create_all(self._engine)

    def test_returning_for_insert_and_update(self):
        random_id = random.randint(1, 1000)
        with self._engine.begin() as connection:
            stmt = (
                self._table.insert()
                .values(id=random_id, data="some % value")
                .returning(self._table.c.id)
            )
            row = connection.execute(stmt).fetchall()
            eq_(
                row,
                [(random_id,)],
            )

        with self._engine.begin() as connection:
            update_text = "some + value"
            stmt = (
                self._table.update()
                .values(data=update_text)
                .where(self._table.c.id == random_id)
                .returning(self._table.c.data)
            )
            row = connection.execute(stmt).fetchall()
            eq_(
                row,
                [(update_text,)],
            )


@pytest.mark.skipif(
    bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
)
class SequenceTest(_SequenceTest):
    @classmethod
    def define_tables(cls, metadata):
        Table(
            "seq_pk",
            metadata,
            Column(
                "id",
                Integer,
                sqlalchemy.Sequence("tab_id_seq"),
                primary_key=True,
            ),
            Column("data", String(50)),
        )

        Table(
            "seq_opt_pk",
            metadata,
            Column(
                "id",
                Integer,
                sqlalchemy.Sequence("tab_id_seq_opt", data_type=Integer, optional=True),
                primary_key=True,
            ),
            Column("data", String(50)),
        )

        Table(
            "seq_no_returning",
            metadata,
            Column(
                "id",
                Integer,
                sqlalchemy.Sequence("noret_id_seq"),
                primary_key=True,
            ),
            Column("data", String(50)),
            implicit_returning=False,
        )

    def test_insert_lastrowid(self, connection):
        r = connection.execute(self.tables.seq_pk.insert(), dict(data="some data"))
        assert len(r.inserted_primary_key) == 1
        is_instance_of(r.inserted_primary_key[0], int)

    def test_nextval_direct(self, connection):
        r = connection.execute(self.tables.seq_pk.c.id.default)
        is_instance_of(r, int)

    def _assert_round_trip(self, table, conn):
        row = conn.execute(table.select()).first()
        id, name = row
        is_instance_of(id, int)
        eq_(name, "some data")

    @testing.combinations((True,), (False,), argnames="implicit_returning")
    @testing.requires.schemas
    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_insert_roundtrip_translate(self, connection, implicit_returning):
        pass

    @testing.requires.schemas
    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_nextval_direct_schema_translate(self, connection):
        pass


@pytest.mark.skipif(
    bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
)
class HasSequenceTest(_HasSequenceTest):
    @classmethod
    def define_tables(cls, metadata):
        sqlalchemy.Sequence("user_id_seq", metadata=metadata)
        sqlalchemy.Sequence(
            "other_seq", metadata=metadata, nomaxvalue=True, nominvalue=True
        )
        Table(
            "user_id_table",
            metadata,
            Column("id", Integer, primary_key=True),
        )

    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_sequence_cache(self, connection, metadata):
        pass

    @testing.requires.schemas
    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_sequence_schema(self, connection):
        pass

    @testing.requires.schemas
    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_sequence_schemas_neg(self, connection):
        pass

    @testing.requires.schemas
    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_sequence_default_not_in_remote(self, connection):
        pass

    @testing.requires.schemas
    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_has_sequence_remote_not_in_default(self, connection):
        pass

    @testing.requires.schemas
    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_get_sequence_names_no_sequence_schema(self, connection):
        pass

    @testing.requires.schemas
    @pytest.mark.skip("Not supported by Cloud Spanner")
    def test_get_sequence_names_sequences_schema(self, connection):
        pass


@pytest.mark.skipif(
    bool(os.environ.get("SPANNER_EMULATOR_HOST")), reason="Skipped on emulator"
)
class HasSequenceTestEmpty(_HasSequenceTestEmpty):
    def test_get_sequence_names_no_sequence(self, connection):
        super().test_get_sequence_names_no_sequence(connection)
