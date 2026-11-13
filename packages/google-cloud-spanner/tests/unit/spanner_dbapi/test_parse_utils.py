# Copyright 2020 Google LLC All rights reserved.
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

import sys
import unittest

from google.cloud.spanner_dbapi.parse_utils import (
    SPANNER_RESERVED_KEYWORDS,
    classify_statement,
    escape_name,
)
from google.cloud.spanner_dbapi.parsed_statement import (
    ClientSideStatementType,
    ParsedStatement,
    Statement,
    StatementType,
)
from google.cloud.spanner_v1 import JsonObject, param_types


class TestParseUtils(unittest.TestCase):
    skip_condition = sys.version_info[0] < 3
    skip_message = "Subtests are not supported in Python 2"

    def test_classify_stmt(self):
        cases = (
            ("SELECT 1", StatementType.QUERY),
            ("SELECT s.SongName FROM Songs AS s", StatementType.QUERY),
            ("(SELECT s.SongName FROM Songs AS s)", StatementType.QUERY),
            (
                "WITH sq AS (SELECT SchoolID FROM Roster) SELECT * from sq",
                StatementType.QUERY,
            ),
            (
                "GRAPH FinGraph MATCH (n) RETURN LABELS(n) AS label, n.id",
                StatementType.QUERY,
            ),
            ("FROM Produce |> WHERE item != 'bananas'", StatementType.QUERY),
            (
                "CREATE TABLE django_content_type (id STRING(64) NOT NULL, name STRING(100) "
                "NOT NULL, app_label STRING(100) NOT NULL, model STRING(100) NOT NULL) PRIMARY KEY(id)",
                StatementType.DDL,
            ),
            (
                "CREATE INDEX SongsBySingerAlbumSongNameDesc ON "
                "Songs(SingerId, AlbumId, SongName DESC), INTERLEAVE IN Albums",
                StatementType.DDL,
            ),
            ("CREATE INDEX SongsBySongName ON Songs(SongName)", StatementType.DDL),
            (
                "CREATE INDEX AlbumsByAlbumTitle2 ON Albums(AlbumTitle) STORING (MarketingBudget)",
                StatementType.DDL,
            ),
            ("CREATE ROLE parent", StatementType.DDL),
            ("commit", StatementType.CLIENT_SIDE),
            ("begin", StatementType.CLIENT_SIDE),
            ("start", StatementType.CLIENT_SIDE),
            ("begin isolation level serializable", StatementType.CLIENT_SIDE),
            ("start isolation level serializable", StatementType.CLIENT_SIDE),
            ("begin isolation level repeatable read", StatementType.CLIENT_SIDE),
            ("start isolation level repeatable read", StatementType.CLIENT_SIDE),
            ("begin transaction", StatementType.CLIENT_SIDE),
            ("start transaction", StatementType.CLIENT_SIDE),
            (
                "begin transaction isolation level serializable",
                StatementType.CLIENT_SIDE,
            ),
            (
                "start transaction isolation level serializable",
                StatementType.CLIENT_SIDE,
            ),
            (
                "begin transaction isolation level repeatable read",
                StatementType.CLIENT_SIDE,
            ),
            (
                "start transaction isolation level repeatable read",
                StatementType.CLIENT_SIDE,
            ),
            ("rollback", StatementType.CLIENT_SIDE),
            (" commit   TRANSACTION ", StatementType.CLIENT_SIDE),
            (" rollback TRANSACTION ", StatementType.CLIENT_SIDE),
            ("  SHOW   VARIABLE COMMIT_TIMESTAMP  ", StatementType.CLIENT_SIDE),
            ("SHOW VARIABLE READ_TIMESTAMP", StatementType.CLIENT_SIDE),
            ("SET DATA_BOOST_ENABLED = TRUE", StatementType.CLIENT_SIDE),
            ("SHOW VARIABLE DATA_BOOST_ENABLED", StatementType.CLIENT_SIDE),
            ("SET AUTO_PARTITION_MODE = TRUE", StatementType.CLIENT_SIDE),
            ("SHOW VARIABLE AUTO_PARTITION_MODE", StatementType.CLIENT_SIDE),
            ("GRANT SELECT ON TABLE Singers TO ROLE parent", StatementType.DDL),
            ("REVOKE SELECT ON TABLE Singers TO ROLE parent", StatementType.DDL),
            ("GRANT ROLE parent TO ROLE child", StatementType.DDL),
            ("INSERT INTO table (col1) VALUES (1)", StatementType.INSERT),
            ("INSERT table (col1) VALUES (1)", StatementType.INSERT),
            ("INSERT OR UPDATE table (col1) VALUES (1)", StatementType.INSERT),
            ("INSERT OR IGNORE table (col1) VALUES (1)", StatementType.INSERT),
            ("UPDATE table SET col1 = 1 WHERE col1 = NULL", StatementType.UPDATE),
            ("delete from table WHERE col1 = 2", StatementType.UPDATE),
            ("delete from table WHERE col1 in (select 1)", StatementType.UPDATE),
            ("dlete from table where col1 = 2", StatementType.UNKNOWN),
            ("udpate table set col2=1 where col1 = 2", StatementType.UNKNOWN),
            ("begin foo", StatementType.UNKNOWN),
            ("begin transaction foo", StatementType.UNKNOWN),
            ("begin transaction isolation level", StatementType.UNKNOWN),
            ("begin transaction repeatable read", StatementType.UNKNOWN),
            (
                "begin transaction isolation level repeatable read foo",
                StatementType.UNKNOWN,
            ),
            (
                "begin transaction isolation level unspecified",
                StatementType.UNKNOWN,
            ),
            ("commit foo", StatementType.UNKNOWN),
            ("commit transaction foo", StatementType.UNKNOWN),
            ("rollback foo", StatementType.UNKNOWN),
            ("rollback transaction foo", StatementType.UNKNOWN),
            ("show variable", StatementType.UNKNOWN),
            ("show variable read_timestamp foo", StatementType.UNKNOWN),
            ("INSERTs INTO table (col1) VALUES (1)", StatementType.UNKNOWN),
            ("UPDATEs table SET col1 = 1 WHERE col1 = NULL", StatementType.UNKNOWN),
            ("DELETEs from table WHERE col1 = 2", StatementType.UNKNOWN),
        )

        for query, want_class in cases:
            self.assertEqual(
                classify_statement(query).statement_type, want_class, query
            )

    def test_begin_isolation_level(self):
        parsed_statement = classify_statement("begin")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("begin"),
                ClientSideStatementType.BEGIN,
                [],
            ),
        )
        parsed_statement = classify_statement("begin isolation level serializable")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("begin isolation level serializable"),
                ClientSideStatementType.BEGIN,
                ["serializable"],
            ),
        )
        parsed_statement = classify_statement("begin isolation level repeatable read")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("begin isolation level repeatable read"),
                ClientSideStatementType.BEGIN,
                ["repeatable read"],
            ),
        )
        parsed_statement = classify_statement(
            "begin isolation    level   repeatable    read    "
        )
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("begin isolation    level   repeatable    read"),
                ClientSideStatementType.BEGIN,
                ["repeatable    read"],
            ),
        )

    def test_partition_query_classify_stmt(self):
        parsed_statement = classify_statement(
            " PARTITION  SELECT s.SongName FROM Songs AS s  "
        )
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("PARTITION  SELECT s.SongName FROM Songs AS s"),
                ClientSideStatementType.PARTITION_QUERY,
                ["SELECT s.SongName FROM Songs AS s"],
            ),
        )

    def test_run_partition_classify_stmt(self):
        parsed_statement = classify_statement(" RUN  PARTITION  bj2bjb2j2bj2ebbh  ")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("RUN  PARTITION  bj2bjb2j2bj2ebbh"),
                ClientSideStatementType.RUN_PARTITION,
                ["bj2bjb2j2bj2ebbh"],
            ),
        )

    def test_run_partition_classify_stmt_long_id(self):
        # Regression test for "Maximum grouping depth exceeded" with sqlparse
        long_id = "a" * 5000
        query = f"RUN PARTITION {long_id}"
        parsed_statement = classify_statement(query)
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement(query),
                ClientSideStatementType.RUN_PARTITION,
                [long_id],
            ),
        )

    def test_run_partition_classify_stmt_incomplete(self):
        # "RUN PARTITION" without ID should be classified as UNKNOWN (not None)
        # because it falls through the specific check and sqlparse handles it.
        query = "RUN PARTITION"
        parsed_statement = classify_statement(query)
        self.assertEqual(parsed_statement.statement_type, StatementType.UNKNOWN)
        self.assertEqual(parsed_statement.statement.sql, query)

    def test_run_partitioned_query_classify_stmt(self):
        parsed_statement = classify_statement(
            " RUN PARTITIONED  QUERY  SELECT s.SongName FROM Songs AS s  "
        )
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("RUN PARTITIONED  QUERY  SELECT s.SongName FROM Songs AS s"),
                ClientSideStatementType.RUN_PARTITIONED_QUERY,
                ["SELECT s.SongName FROM Songs AS s"],
            ),
        )

    def test_set_autocommit_dml_mode_stmt(self):
        parsed_statement = classify_statement(
            "  set autocommit_dml_mode = PARTITIONED_NON_ATOMIC  "
        )
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("set autocommit_dml_mode = PARTITIONED_NON_ATOMIC"),
                ClientSideStatementType.SET_AUTOCOMMIT_DML_MODE,
                ["PARTITIONED_NON_ATOMIC"],
            ),
        )

    def test_set_data_boost_enabled_stmt(self):
        parsed_statement = classify_statement("  set data_boost_enabled = true  ")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("set data_boost_enabled = true"),
                ClientSideStatementType.SET_DATA_BOOST_ENABLED,
                ["true"],
            ),
        )
        parsed_statement = classify_statement("SET DATA_BOOST_ENABLED = FALSE")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("SET DATA_BOOST_ENABLED = FALSE"),
                ClientSideStatementType.SET_DATA_BOOST_ENABLED,
                ["FALSE"],
            ),
        )

    def test_show_data_boost_enabled_stmt(self):
        parsed_statement = classify_statement("  show  variable data_boost_enabled  ")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("show  variable data_boost_enabled"),
                ClientSideStatementType.SHOW_DATA_BOOST_ENABLED,
                [],
            ),
        )

        parsed_statement = classify_statement("SHOW VARIABLE DATA_BOOST_ENABLED;")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("SHOW VARIABLE DATA_BOOST_ENABLED;"),
                ClientSideStatementType.SHOW_DATA_BOOST_ENABLED,
                [],
            ),
        )

    def test_set_auto_partition_mode_stmt(self):
        parsed_statement = classify_statement("SET AUTO_PARTITION_MODE = TRUE")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("SET AUTO_PARTITION_MODE = TRUE"),
                ClientSideStatementType.SET_AUTO_PARTITION_MODE,
                ["TRUE"],
            ),
        )

        parsed_statement = classify_statement("set auto_partition_mode = false")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("set auto_partition_mode = false"),
                ClientSideStatementType.SET_AUTO_PARTITION_MODE,
                ["false"],
            ),
        )

        parsed_statement = classify_statement("SET AUTO_PARTITION_MODE = TRUE;")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("SET AUTO_PARTITION_MODE = TRUE;"),
                ClientSideStatementType.SET_AUTO_PARTITION_MODE,
                ["TRUE;"],
            ),
        )

    def test_show_auto_partition_mode_stmt(self):
        parsed_statement = classify_statement("  show  variable auto_partition_mode  ")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("show  variable auto_partition_mode"),
                ClientSideStatementType.SHOW_AUTO_PARTITION_MODE,
                [],
            ),
        )

        parsed_statement = classify_statement("SHOW VARIABLE AUTO_PARTITION_MODE;")
        self.assertEqual(
            parsed_statement,
            ParsedStatement(
                StatementType.CLIENT_SIDE,
                Statement("SHOW VARIABLE AUTO_PARTITION_MODE;"),
                ClientSideStatementType.SHOW_AUTO_PARTITION_MODE,
                [],
            ),
        )

    @unittest.skipIf(skip_condition, skip_message)
    def test_sql_pyformat_args_to_spanner(self):
        from google.cloud.spanner_dbapi.parse_utils import sql_pyformat_args_to_spanner

        cases = [
            (
                (
                    "SELECT * from t WHERE f1=%s, f2 = %s, f3=%s",
                    (10, "abc", "y**$22l3f"),
                ),
                (
                    "SELECT * from t WHERE f1=@a0, f2 = @a1, f3=@a2",
                    {"a0": 10, "a1": "abc", "a2": "y**$22l3f"},
                ),
            ),
            (
                (
                    "INSERT INTO t (f1, f2, f2) VALUES (%s, %s, %s)",
                    ("app", "name", "applied"),
                ),
                (
                    "INSERT INTO t (f1, f2, f2) VALUES (@a0, @a1, @a2)",
                    {"a0": "app", "a1": "name", "a2": "applied"},
                ),
            ),
            (
                (
                    "INSERT INTO t (f1, f2, f2) VALUES (%(f1)s, %(f2)s, %(f3)s)",
                    {"f1": "app", "f2": "name", "f3": "applied"},
                ),
                (
                    "INSERT INTO t (f1, f2, f2) VALUES (@a0, @a1, @a2)",
                    {"a0": "app", "a1": "name", "a2": "applied"},
                ),
            ),
            (
                # Intentionally using a dict with more keys than will be resolved.
                ("SELECT * from t WHERE f1=%(f1)s", {"f1": "app", "f2": "name"}),
                ("SELECT * from t WHERE f1=@a0", {"a0": "app"}),
            ),
            (
                # No args to replace, we MUST return the original params dict
                # since it might be useful to pass to the next user.
                ("SELECT * from t WHERE id=10", {"f1": "app", "f2": "name"}),
                ("SELECT * from t WHERE id=10", {"f1": "app", "f2": "name"}),
            ),
            (
                # Preserves Unicode in identifiers and trailing WHERE predicates
                (
                    "SELECT * FROM `Tëst` WHERE tenant_id = %s",
                    ("tenant_1",),
                ),
                (
                    "SELECT * FROM `Tëst` WHERE tenant_id = @a0",
                    {"a0": "tenant_1"},
                ),
            ),
            (
                # Preserves Unicode in string literals without backticking or truncating
                (
                    "SELECT * FROM users WHERE dept = 'café' AND tenant_id = %s",
                    ("tenant_1",),
                ),
                (
                    "SELECT * FROM users WHERE dept = 'café' AND tenant_id = @a0",
                    {"a0": "tenant_1"},
                ),
            ),
            (
                # Preserves percent escaping (%% -> %) alongside parameters
                (
                    "SELECT * FROM users WHERE name LIKE 'A%%' AND age > %s",
                    (21,),
                ),
                (
                    "SELECT * FROM users WHERE name LIKE 'A%' AND age > @a0",
                    {"a0": 21},
                ),
            ),
            (
                # Preserves Unicode in unparameterized queries (params=None)
                (
                    "SELECT * FROM users WHERE city = 'München' AND active = true",
                    None,
                ),
                (
                    "SELECT * FROM users WHERE city = 'München' AND active = true",
                    None,
                ),
            ),
            (
                # Preserves Unicode in dict-based named parameters and literals
                (
                    "SELECT * FROM users WHERE name = %(name)s AND dept = 'café'",
                    {"name": "Alice"},
                ),
                (
                    "SELECT * FROM users WHERE name = @a0 AND dept = 'café'",
                    {"a0": "Alice"},
                ),
            ),
        ]
        for (sql_in, params), sql_want in cases:
            with self.subTest(sql=sql_in):
                got_sql, got_named_args = sql_pyformat_args_to_spanner(sql_in, params)
                want_sql, want_named_args = sql_want
                self.assertEqual(got_sql, want_sql, "SQL does not match")
                self.assertEqual(
                    got_named_args, want_named_args, "Named args do not match"
                )

    @unittest.skipIf(skip_condition, skip_message)
    def test_sql_pyformat_args_to_spanner_invalid(self):
        from google.cloud.spanner_dbapi import exceptions
        from google.cloud.spanner_dbapi.parse_utils import sql_pyformat_args_to_spanner

        cases = [
            (
                "SELECT * from t WHERE f1=%s, f2 = %s, f3=%s, extra=%s",
                (10, "abc", "y**$22l3f"),
            )
        ]
        for sql, params in cases:
            with self.subTest(sql=sql):
                self.assertRaisesRegex(
                    exceptions.Error,
                    "pyformat_args mismatch",
                    lambda: sql_pyformat_args_to_spanner(sql, params),
                )

    @unittest.skipIf(skip_condition, skip_message)
    def test_get_param_types(self):
        import datetime
        import decimal

        from google.cloud.spanner_dbapi.parse_utils import (
            DateStr,
            TimestampStr,
            get_param_types,
        )

        params = {
            "a1": 10,
            "b1": "string",
            # Note: We only want a value and not a type for this.
            # Instead, we let Spanner infer the correct type (FLOAT64 or FLOAT32)
            "c1": 10.39,
            "d1": TimestampStr("2005-08-30T01:01:01.000001Z"),
            "e1": DateStr("2019-12-05"),
            "f1": True,
            "g1": datetime.datetime(2011, 9, 1, 13, 20, 30),
            "h1": datetime.date(2011, 9, 1),
            "i1": b"bytes",
            "j1": None,
            "k1": decimal.Decimal("3.194387483193242e+19"),
            "l1": JsonObject({"key": "value"}),
        }
        want_types = {
            "a1": param_types.INT64,
            "b1": param_types.STRING,
            "d1": param_types.TIMESTAMP,
            "e1": param_types.DATE,
            "f1": param_types.BOOL,
            "g1": param_types.TIMESTAMP,
            "h1": param_types.DATE,
            "i1": param_types.BYTES,
            "k1": param_types.NUMERIC,
            "l1": param_types.JSON,
        }
        got_types = get_param_types(params)
        self.assertEqual(got_types, want_types)

    def test_get_param_types_none(self):
        from google.cloud.spanner_dbapi.parse_utils import get_param_types

        self.assertEqual(get_param_types(None), None)

    @unittest.skipIf(skip_condition, skip_message)
    def test_ensure_where_clause(self):
        from google.cloud.spanner_dbapi.parse_utils import ensure_where_clause

        cases = (
            "UPDATE a SET a.b=10 FROM articles a JOIN d c ON a.ai = c.ai WHERE c.ci = 1",
            "UPDATE T SET A = 1 WHERE C1 = 1 AND C2 = 2",
            "UPDATE T SET r=r*0.9 WHERE id IN (SELECT id FROM items WHERE r / w >= 1.3 AND q > 100)",
        )
        err_cases = (
            "UPDATE (SELECT * FROM A JOIN c ON ai.id = c.id WHERE cl.ci = 1) SET d=5",
            "DELETE * FROM TABLE",
        )
        for sql in cases:
            with self.subTest(sql=sql):
                ensure_where_clause(sql)

        for sql in err_cases:
            with self.subTest(sql=sql):
                self.assertEqual(ensure_where_clause(sql), sql + " WHERE 1=1")

    @unittest.skipIf(skip_condition, skip_message)
    def test_escape_name(self):
        cases = (
            ("SELECT", "`SELECT`"),
            ("dashed-value", "`dashed-value`"),
            ("with space", "`with space`"),
            ("name", "`name`"),
            ("", ""),
            ("``", "``"),
            ("col`; DROP TABLE t; -- x", "`col\\`; DROP TABLE t; -- x`"),
            ("table`name", "`table\\`name`"),
            ("`", "`\\``"),
            ("col/*comment*/name", "`col/*comment*/name`"),
            ("123column", "`123column`"),
            ("col;select", "`col;select`"),
            ("test\\", "`test\\\\`"),
            ("my_schema.my_table", "`my_schema`.`my_table`"),
            ("my-schema.my-table", "`my-schema`.`my-table`"),
            ("catalog.schema.table.column", "`catalog`.`schema`.`table`.`column`"),
            ("`my_table`", "`my_table`"),
            ("`my_schema`.`my_table`", "`my_schema`.`my_table`"),
            ("`table.with.dots`", "`table.with.dots`"),
            ("`table.with.dots`.col", "`table.with.dots`.`col`"),
            ("col.`table.with.dots`", "`col`.`table.with.dots`"),
            ("`my.schema`.`my.table`", "`my.schema`.`my.table`"),
            ("café", "`café`"),
            ("col_ñ", "`col_ñ`"),
            ("`col\\`name`", "`col\\`name`"),
            ("`col\\`; DROP TABLE users; --`", "`col\\`; DROP TABLE users; --`"),
            (
                "`col\\\\`; DROP TABLE users; --`",
                "`\\`col\\\\\\\\\\`; DROP TABLE users; --\\``",
            ),
        )
        for name, want in cases:
            with self.subTest(name=name):
                got = escape_name(name)
                self.assertEqual(got, want)
                # Verify idempotency: escaping an already-escaped output returns the same result.
                self.assertEqual(escape_name(got), want)

    @unittest.skipIf(skip_condition, skip_message)
    def test_escape_name_invalid_control_characters(self):
        invalid_identifiers = (
            "table\nname",
            "table\rname",
            "table\0name",
            "table\tname",
            "table\x1fname",
            "table\x7fname",
            "schema\n.table",
            "schema.table\0",
        )
        for identifier in invalid_identifiers:
            with self.subTest(identifier=identifier):
                with self.assertRaises(ValueError):
                    escape_name(identifier)

    @unittest.skipIf(skip_condition, skip_message)
    def test_escape_name_invalid_qualified_identifiers(self):
        invalid_qualified = (
            ".",
            "...",
            "table.",
            ".table",
            "schema..table",
            "schema.`unclosed.table.`other",
        )
        for identifier in invalid_qualified:
            with self.subTest(identifier=identifier):
                with self.assertRaises(ValueError):
                    escape_name(identifier)

    @unittest.skipIf(skip_condition, skip_message)
    def test_escape_name_invalid_types(self):
        invalid_types = (None, 123, 45.67, b"bytes_name", ["list"])
        for identifier in invalid_types:
            with self.subTest(identifier=identifier):
                with self.assertRaises(TypeError):
                    escape_name(identifier)

    @unittest.skipIf(skip_condition, skip_message)
    def test_spanner_reserved_keywords_compatibility(self):
        # Verify that SPANNER_RESERVED_KEYWORDS is exported with recent additions
        # for backwards compatibility with downstream consumers (e.g. sqlalchemy-spanner).
        self.assertIn("GRAPH_TABLE", SPANNER_RESERVED_KEYWORDS)
        self.assertIn("QUALIFY", SPANNER_RESERVED_KEYWORDS)

    def test_classify_statement_preserves_unicode_and_predicates(self):
        # Scoped SELECT with Unicode identifier preserves WHERE clause
        query = "SELECT * FROM `Tëst` WHERE tenant_id = %s"
        parsed = classify_statement(query, ("tenant_1",))
        self.assertEqual(
            parsed.statement.sql, "SELECT * FROM `Tëst` WHERE tenant_id = @a0"
        )
        self.assertEqual(parsed.statement.params, {"a0": "tenant_1"})
        self.assertEqual(parsed.statement_type, StatementType.QUERY)

        # Scoped DELETE with Unicode identifier does not drop WHERE or append WHERE 1=1
        query = "DELETE FROM `Tëst` WHERE id = %s"
        parsed = classify_statement(query, (42,))
        self.assertEqual(parsed.statement.sql, "DELETE FROM `Tëst` WHERE id = @a0")
        self.assertEqual(parsed.statement.params, {"a0": 42})
        self.assertEqual(parsed.statement_type, StatementType.UPDATE)
        self.assertNotIn("WHERE 1=1", parsed.statement.sql)

        # Scoped UPDATE with Unicode in SET clause does not convert WHERE clause to WHERE 1=1
        query = "UPDATE users SET note = 'Café' WHERE id = %s"
        parsed = classify_statement(query, (42,))
        self.assertEqual(
            parsed.statement.sql, "UPDATE users SET note = 'Café' WHERE id = @a0"
        )
        self.assertEqual(parsed.statement.params, {"a0": 42})
        self.assertEqual(parsed.statement_type, StatementType.UPDATE)
        self.assertNotIn("WHERE 1=1", parsed.statement.sql)

        # Scoped UPDATE with Unicode literal preserves literal and WHERE clause
        query = "UPDATE users SET status = 'active' WHERE name = 'José' AND id = %s"
        parsed = classify_statement(query, (1,))
        self.assertEqual(
            parsed.statement.sql,
            "UPDATE users SET status = 'active' WHERE name = 'José' AND id = @a0",
        )
        self.assertEqual(parsed.statement.params, {"a0": 1})
        self.assertEqual(parsed.statement_type, StatementType.UPDATE)
        self.assertNotIn("WHERE 1=1", parsed.statement.sql)

        # Adjacent punctuation with Unicode identifiers does not swallow punctuation
        query = "SELECT `tätä`, id FROM users WHERE id = %s"
        parsed = classify_statement(query, (1,))
        self.assertEqual(
            parsed.statement.sql,
            "SELECT `tätä`, id FROM users WHERE id = @a0",
        )
        self.assertEqual(parsed.statement.params, {"a0": 1})

    def test_classify_statement_does_not_add_dummy_where(self):
        """classify_statement must classify statements without mutating them or adding WHERE 1=1."""
        query = "UPDATE users SET active = true"
        parsed = classify_statement(query)
        self.assertEqual(parsed.statement.sql, query)
        self.assertEqual(parsed.statement_type, StatementType.UPDATE)

        delete_query = "DELETE FROM users"
        parsed = classify_statement(delete_query)
        self.assertEqual(parsed.statement.sql, delete_query)
        self.assertEqual(parsed.statement_type, StatementType.UPDATE)

    def test_ensure_where_clause_is_idempotent(self):
        """ensure_where_clause must not append duplicate WHERE clauses if called repeatedly."""
        from google.cloud.spanner_dbapi.parse_utils import ensure_where_clause

        sql = "UPDATE users SET active = true"
        with_where = ensure_where_clause(sql)
        self.assertEqual(with_where, "UPDATE users SET active = true WHERE 1=1")
        # Second invocation must be a no-op
        self.assertEqual(ensure_where_clause(with_where), with_where)
        self.assertNotIn("WHERE 1=1 WHERE 1=1", ensure_where_clause(with_where))
