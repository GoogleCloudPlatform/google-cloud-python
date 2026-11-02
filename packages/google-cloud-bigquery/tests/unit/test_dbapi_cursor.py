# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import functools
import operator as op
import unittest
from unittest import mock

import google.cloud.bigquery.table as bq_table
import pytest
from google.api_core import exceptions

from tests.unit.helpers import _to_pyarrow


class TestCursor(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.dbapi import Cursor

        return Cursor

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _mock_client(
        self,
        rows=None,
        schema=None,
        num_dml_affected_rows=None,
        dry_run_job=False,
        total_bytes_processed=0,
        total_rows=None,
        destination_table="test-project.test_dataset.test_table",
    ):
        from google.cloud.bigquery import client

        if total_rows is None:
            total_rows = 0
            if rows is not None:
                total_rows = len(rows)

        table = bq_table.TableReference.from_string(destination_table)
        mock_client = mock.create_autospec(client.Client)
        mock_job = self._mock_job(
            total_rows=total_rows,
            schema=schema,
            num_dml_affected_rows=num_dml_affected_rows,
            dry_run=dry_run_job,
            total_bytes_processed=total_bytes_processed,
            rows=self._mock_rows(
                rows,
                total_rows=total_rows,
                schema=schema,
                num_dml_affected_rows=num_dml_affected_rows,
                table=table,
            ),
        )
        mock_client.get_job.return_value = mock_job
        mock_client.query.return_value = mock_job
        mock_client.query_and_wait.return_value = self._mock_rows(
            rows,
            total_rows=total_rows,
            schema=schema,
            num_dml_affected_rows=num_dml_affected_rows,
            # Sometimes all the results will be available in the initial
            # response, in which case may be no job and no destination table.
            table=table if rows is not None and total_rows > len(rows) else None,
        )

        # Assure that the REST client gets used, not the BQ Storage client.
        mock_client._ensure_bqstorage_client.return_value = None

        return mock_client

    def _mock_bqstorage_client(self, rows=None, stream_count=0):
        from google.cloud import bigquery_storage

        if rows is None:
            rows = []

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        mock_read_session = mock.MagicMock(
            streams=[
                bigquery_storage.types.ReadStream(name="streams/stream_{}".format(i))
                for i in range(stream_count)
            ]
        )

        mock_client.create_read_session.return_value = mock_read_session

        mock_rows_stream = mock.MagicMock()
        mock_rows_stream.rows.return_value = iter(rows)
        mock_client.read_rows.return_value = mock_rows_stream

        return mock_client

    def _mock_job(
        self,
        total_rows=0,
        schema=None,
        num_dml_affected_rows=None,
        dry_run=False,
        total_bytes_processed=0,
        rows=None,
    ):
        from google.cloud.bigquery import job

        mock_job = mock.create_autospec(job.QueryJob)
        mock_job.error_result = None
        mock_job.state = "DONE"
        mock_job.dry_run = dry_run

        if dry_run:
            mock_job.result.side_effect = exceptions.NotFound
            mock_job.total_bytes_processed = total_bytes_processed
        else:
            mock_job.result.return_value = rows
            mock_job._query_results = self._mock_results(
                total_rows=total_rows,
                schema=schema,
                num_dml_affected_rows=num_dml_affected_rows,
            )
            mock_job.destination.project = "P"
            mock_job.destination.to_bqstorage.return_value = (
                "projects/P/datasets/DS/tables/T"
            )

        if num_dml_affected_rows is None:
            mock_job.statement_type = None  # API sends back None for SELECT
        else:
            mock_job.statement_type = "UPDATE"

        return mock_job

    def _mock_rows(
        self, rows, total_rows=0, schema=None, num_dml_affected_rows=None, table=None
    ):
        mock_rows = mock.create_autospec(bq_table.RowIterator, instance=True)
        mock_rows.__iter__.return_value = rows
        mock_rows._table = table
        mock_rows._should_use_bqstorage = functools.partial(
            bq_table.RowIterator._should_use_bqstorage,
            mock_rows,
        )
        mock_rows._is_almost_completely_cached = functools.partial(
            bq_table.RowIterator._is_almost_completely_cached,
            mock_rows,
        )
        mock_rows.max_results = None
        type(mock_rows).job_id = mock.PropertyMock(return_value="test-job-id")
        type(mock_rows).location = mock.PropertyMock(return_value="test-location")
        type(mock_rows).num_dml_affected_rows = mock.PropertyMock(
            return_value=num_dml_affected_rows
        )
        type(mock_rows).total_rows = mock.PropertyMock(return_value=total_rows)
        type(mock_rows).schema = mock.PropertyMock(return_value=schema)
        return mock_rows

    def _mock_results(self, total_rows=0, schema=None, num_dml_affected_rows=None):
        from google.cloud.bigquery import query

        mock_results = mock.create_autospec(query._QueryResults)
        mock_results.schema = schema
        mock_results.num_dml_affected_rows = num_dml_affected_rows
        mock_results.total_rows = total_rows
        return mock_results

    def test_ctor(self):
        from google.cloud.bigquery.dbapi import Cursor, connect

        connection = connect(self._mock_client())
        cursor = self._make_one(connection)
        self.assertIsInstance(cursor, Cursor)
        self.assertIs(cursor.connection, connection)

    def test_close(self):
        from google.cloud.bigquery.dbapi import connect

        connection = connect(self._mock_client())
        cursor = connection.cursor()

        # Simulate that cursor has data/references
        cursor._query_data = mock.Mock()
        cursor._query_rows = mock.Mock()

        cursor.close()

        self.assertTrue(cursor._closed)
        self.assertIsNone(cursor._query_data)
        self.assertIsNone(cursor._query_rows)

    def test_raises_error_if_closed(self):
        from google.cloud.bigquery.dbapi import connect
        from google.cloud.bigquery.dbapi.exceptions import ProgrammingError

        connection = connect(self._mock_client())
        cursor = connection.cursor()
        cursor.close()

        method_names = (
            "close",
            "execute",
            "executemany",
            "fetchall",
            "fetchmany",
            "fetchone",
            "setinputsizes",
            "setoutputsize",
            "__iter__",
        )

        for method in method_names:
            with self.assertRaisesRegex(
                ProgrammingError, r"Operating on a closed cursor\."
            ):
                getattr(cursor, method)()

    def test_fetchone_wo_execute_raises_error(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(self._mock_client())
        cursor = connection.cursor()
        self.assertRaises(dbapi.Error, cursor.fetchone)

    def test_fetchone_w_row(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(self._mock_client(rows=[(1,)]))
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        row = cursor.fetchone()
        self.assertEqual(row, (1,))
        self.assertIsNone(cursor.fetchone())

    def test_fetchmany_wo_execute_raises_error(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(self._mock_client())
        cursor = connection.cursor()
        self.assertRaises(dbapi.Error, cursor.fetchmany)

    def test_fetchmany_w_row(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(self._mock_client(rows=[(1,)]))
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        rows = cursor.fetchmany()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], (1,))

    def test_fetchmany_w_size(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(
            self._mock_client(rows=[(1, 2, 3), (4, 5, 6), (7, 8, 9)])
        )
        cursor = connection.cursor()
        cursor.execute("SELECT a, b, c;")
        rows = cursor.fetchmany(size=2)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], (1, 2, 3))
        self.assertEqual(rows[1], (4, 5, 6))
        second_page = cursor.fetchmany(size=2)
        self.assertEqual(len(second_page), 1)
        self.assertEqual(second_page[0], (7, 8, 9))
        third_page = cursor.fetchmany(size=2)
        self.assertEqual(third_page, [])

    def test_fetchmany_w_arraysize(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(
            self._mock_client(rows=[(1, 2, 3), (4, 5, 6), (7, 8, 9)])
        )
        cursor = connection.cursor()
        cursor.execute("SELECT a, b, c;")
        cursor.arraysize = 2
        rows = cursor.fetchmany()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], (1, 2, 3))
        self.assertEqual(rows[1], (4, 5, 6))
        second_page = cursor.fetchmany()
        self.assertEqual(len(second_page), 1)
        self.assertEqual(second_page[0], (7, 8, 9))
        third_page = cursor.fetchmany()
        self.assertEqual(third_page, [])

    def test_fetchall_wo_execute_raises_error(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(self._mock_client())
        cursor = connection.cursor()
        self.assertRaises(dbapi.Error, cursor.fetchall)

    def test_fetchall_w_row(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(self._mock_client(rows=[(1,)]))
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        self.assertIsNone(cursor.description)
        self.assertEqual(cursor.rowcount, 1)
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], (1,))

    def test_fetchall_w_bqstorage_client_fetch_success(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import dbapi

        # use unordered data to also test any non-determenistic key order in dicts
        row_data = [
            bq_table.Row(
                [1.4, 1.1, 1.3, 1.2], {"bar": 3, "baz": 2, "foo": 1, "quux": 0}
            ),
            bq_table.Row(
                [2.4, 2.1, 2.3, 2.2], {"bar": 3, "baz": 2, "foo": 1, "quux": 0}
            ),
        ]
        bqstorage_streamed_rows = [
            {
                "bar": _to_pyarrow(1.2),
                "foo": _to_pyarrow(1.1),
                "quux": _to_pyarrow(1.4),
                "baz": _to_pyarrow(1.3),
            },
            {
                "bar": _to_pyarrow(2.2),
                "foo": _to_pyarrow(2.1),
                "quux": _to_pyarrow(2.4),
                "baz": _to_pyarrow(2.3),
            },
        ]

        mock_client = self._mock_client(rows=row_data)
        mock_bqstorage_client = self._mock_bqstorage_client(
            stream_count=1,
            rows=bqstorage_streamed_rows,
        )
        mock_client._ensure_bqstorage_client.return_value = mock_bqstorage_client

        connection = dbapi.connect(
            client=mock_client,
            bqstorage_client=mock_bqstorage_client,
        )
        cursor = connection.cursor()
        cursor.execute("SELECT foo, bar FROM some_table")

        rows = cursor.fetchall()

        # the default client was not used
        mock_client.list_rows.assert_not_called()

        # check the data returned
        field_value = op.itemgetter(1)
        sorted_row_data = [sorted(row.items(), key=field_value) for row in rows]
        expected_row_data = [
            [("foo", 1.1), ("bar", 1.2), ("baz", 1.3), ("quux", 1.4)],
            [("foo", 2.1), ("bar", 2.2), ("baz", 2.3), ("quux", 2.4)],
        ]

        self.assertEqual(sorted_row_data, expected_row_data)

    def test_fetchall_w_bqstorage_client_fetch_no_rows(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        from google.cloud.bigquery import dbapi

        mock_client = self._mock_client(
            rows=[],
            # Assume there are many more pages of data to look at so that the
            # BQ Storage API is necessary.
            total_rows=1000,
        )
        mock_bqstorage_client = self._mock_bqstorage_client(stream_count=0)
        mock_client._ensure_bqstorage_client.return_value = mock_bqstorage_client

        connection = dbapi.connect(
            client=mock_client,
            bqstorage_client=mock_bqstorage_client,
        )
        cursor = connection.cursor()
        cursor.execute("SELECT foo, bar FROM some_table")

        rows = cursor.fetchall()

        # # the default client was not used
        mock_client.list_rows.assert_not_called()

        # check the data returned
        self.assertEqual(rows, [])

    def test_fetchall_w_bqstorage_client_fetch_error_no_fallback(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        from google.cloud.bigquery import dbapi

        row_data = [bq_table.Row([1.1, 1.2], {"foo": 0, "bar": 1})]

        def fake_ensure_bqstorage_client(bqstorage_client=None, **kwargs):
            return bqstorage_client

        mock_client = self._mock_client(
            rows=row_data,
            # Assume there are many more pages of data to look at so that the
            # BQ Storage API is necessary.
            total_rows=1000,
        )
        mock_client._ensure_bqstorage_client.side_effect = fake_ensure_bqstorage_client
        mock_bqstorage_client = self._mock_bqstorage_client(
            stream_count=1,
            rows=row_data,
        )
        no_access_error = exceptions.Forbidden("invalid credentials")
        mock_bqstorage_client.create_read_session.side_effect = no_access_error

        connection = dbapi.connect(
            client=mock_client,
            bqstorage_client=mock_bqstorage_client,
        )
        cursor = connection.cursor()
        cursor.execute("SELECT foo, bar FROM some_table")

        with self.assertRaisesRegex(exceptions.Forbidden, "invalid credentials"):
            cursor.fetchall()

        # the default client was not used
        mock_client.list_rows.assert_not_called()

    def test_fetchall_w_bqstorage_client_no_arrow_compression(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        pytest.importorskip("pyarrow")
        from google.cloud import bigquery_storage
        from google.cloud.bigquery import dbapi

        # Use unordered data to also test any non-determenistic key order in dicts.
        row_data = [bq_table.Row([1.2, 1.1], {"bar": 1, "foo": 0})]
        bqstorage_streamed_rows = [{"bar": _to_pyarrow(1.2), "foo": _to_pyarrow(1.1)}]

        def fake_ensure_bqstorage_client(bqstorage_client=None, **kwargs):
            return bqstorage_client

        mock_client = self._mock_client(
            rows=row_data,
            # Assume there are many more pages of data to look at so that the
            # BQ Storage API is necessary.
            total_rows=1000,
            destination_table="P.DS.T",
        )
        mock_client._ensure_bqstorage_client.side_effect = fake_ensure_bqstorage_client
        mock_bqstorage_client = self._mock_bqstorage_client(
            stream_count=1,
            rows=bqstorage_streamed_rows,
        )

        connection = dbapi.connect(
            client=mock_client,
            bqstorage_client=mock_bqstorage_client,
        )
        cursor = connection.cursor()
        cursor.execute("SELECT foo, bar FROM some_table")

        with mock.patch(
            "google.cloud.bigquery.dbapi.cursor._ARROW_COMPRESSION_SUPPORT", new=False
        ):
            rows = cursor.fetchall()

        mock_client.list_rows.assert_not_called()  # The default client was not used.

        # Check the BQ Storage session config.
        expected_session = bigquery_storage.ReadSession(
            table="projects/P/datasets/DS/tables/T",
            data_format=bigquery_storage.DataFormat.ARROW,
        )
        mock_bqstorage_client.create_read_session.assert_called_once_with(
            parent="projects/P",
            read_session=expected_session,
            max_stream_count=1,
            retry=None,
            timeout=None,
        )

        # Check the data returned.
        field_value = op.itemgetter(1)
        sorted_row_data = [sorted(row.items(), key=field_value) for row in rows]
        expected_row_data = [[("foo", 1.1), ("bar", 1.2)]]

        self.assertEqual(sorted_row_data, expected_row_data)

    def test_execute_custom_job_id(self):
        from google.cloud.bigquery.dbapi import connect

        client = self._mock_client(rows=[], num_dml_affected_rows=0)
        connection = connect(client)
        cursor = connection.cursor()
        cursor.execute("SELECT 1;", job_id="foo")
        args, kwargs = client.query.call_args
        self.assertEqual(args[0], "SELECT 1;")
        self.assertEqual(kwargs["job_id"], "foo")

    def test_execute_w_default_config(self):
        from google.cloud.bigquery.dbapi import connect

        client = self._mock_client(rows=[], num_dml_affected_rows=0)
        connection = connect(client)
        cursor = connection.cursor()

        cursor.execute("SELECT 1;", job_id="foo")

        _, kwargs = client.query.call_args
        used_config = kwargs["job_config"]
        self.assertIsNone(used_config)

    def test_execute_custom_job_config_wo_default_config(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.dbapi import connect

        config = job.QueryJobConfig(use_legacy_sql=True)
        client = self._mock_client(rows=[], num_dml_affected_rows=0)
        connection = connect(client)
        cursor = connection.cursor()
        cursor.execute("SELECT 1;", job_id="foo", job_config=config)
        args, kwargs = client.query.call_args
        self.assertEqual(args[0], "SELECT 1;")
        self.assertEqual(kwargs["job_id"], "foo")
        self.assertEqual(kwargs["job_config"], config)

    def test_execute_custom_job_config_w_default_config(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.dbapi import connect

        client = self._mock_client(rows=[], num_dml_affected_rows=0)
        connection = connect(client)
        cursor = connection.cursor()
        config = job.QueryJobConfig(use_legacy_sql=True)

        cursor.execute("SELECT 1;", job_id="foo", job_config=config)

        _, kwargs = client.query.call_args
        used_config = kwargs["job_config"]
        expected_config = job.QueryJobConfig(
            use_legacy_sql=True,  # the config passed to execute() prevails
            query_parameters=[],
        )
        self.assertEqual(used_config._properties, expected_config._properties)

    def test_execute_w_dml(self):
        from google.cloud.bigquery.dbapi import connect

        connection = connect(self._mock_client(rows=[], num_dml_affected_rows=12))
        cursor = connection.cursor()
        cursor.execute("DELETE FROM UserSessions WHERE user_id = 'test';")
        rows = cursor.fetchall()
        self.assertIsNone(cursor.description)
        self.assertEqual(cursor.rowcount, 12)
        self.assertEqual(rows, [])

    def test_execute_w_query(self):
        from google.cloud.bigquery import dbapi
        from google.cloud.bigquery.schema import SchemaField

        connection = dbapi.connect(
            self._mock_client(
                rows=[("hello", "world", 1), ("howdy", "y'all", 2)],
                schema=[
                    SchemaField("a", "STRING", mode="NULLABLE"),
                    SchemaField("b", "STRING", mode="REQUIRED"),
                    SchemaField("c", "INTEGER", mode="NULLABLE"),
                ],
            )
        )
        cursor = connection.cursor()
        cursor.execute("SELECT a, b, c FROM hello_world WHERE d > 3;")

        # Verify the description.
        self.assertEqual(len(cursor.description), 3)
        a_name, a_type, _, _, _, _, a_null_ok = cursor.description[0]
        self.assertEqual(a_name, "a")
        self.assertEqual(a_type, "STRING")
        self.assertEqual(a_type, dbapi.STRING)
        self.assertTrue(a_null_ok)
        b_name, b_type, _, _, _, _, b_null_ok = cursor.description[1]
        self.assertEqual(b_name, "b")
        self.assertEqual(b_type, "STRING")
        self.assertEqual(b_type, dbapi.STRING)
        self.assertFalse(b_null_ok)
        c_name, c_type, _, _, _, _, c_null_ok = cursor.description[2]
        self.assertEqual(c_name, "c")
        self.assertEqual(c_type, "INTEGER")
        self.assertEqual(c_type, dbapi.NUMBER)
        self.assertTrue(c_null_ok)

        # Verify the results.
        self.assertEqual(cursor.rowcount, 2)
        row = cursor.fetchone()
        self.assertEqual(row, ("hello", "world", 1))
        row = cursor.fetchone()
        self.assertEqual(row, ("howdy", "y'all", 2))
        row = cursor.fetchone()
        self.assertIsNone(row)

    def test_execute_w_query_dry_run(self):
        from google.cloud.bigquery import dbapi
        from google.cloud.bigquery.job import QueryJobConfig
        from google.cloud.bigquery.schema import SchemaField

        connection = dbapi.connect(
            self._mock_client(
                rows=[],
                schema=[
                    SchemaField("a", "STRING", mode="NULLABLE"),
                    SchemaField("b", "STRING", mode="REQUIRED"),
                    SchemaField("c", "INTEGER", mode="NULLABLE"),
                ],
                dry_run_job=True,
                total_bytes_processed=12345,
            )
        )
        cursor = connection.cursor()

        cursor.execute(
            "SELECT a, b, c FROM hello_world WHERE d > 3;",
            job_config=QueryJobConfig(dry_run=True),
        )

        self.assertEqual(cursor.rowcount, 0)
        self.assertIsNotNone(cursor.description)
        rows = cursor.fetchall()
        self.assertEqual(list(rows), [])

    def test_execute_raises_if_result_raises(self):
        import google.cloud.exceptions
        from google.cloud.bigquery import client
        from google.cloud.bigquery.dbapi import connect, exceptions

        client = mock.create_autospec(client.Client)
        client.query_and_wait.side_effect = google.cloud.exceptions.GoogleCloudError("")
        connection = connect(client)
        cursor = connection.cursor()

        with self.assertRaises(exceptions.DatabaseError):
            cursor.execute("SELECT 1")

    def test_executemany_w_dml(self):
        from google.cloud.bigquery.dbapi import connect

        connection = connect(self._mock_client(rows=[], num_dml_affected_rows=12))
        cursor = connection.cursor()
        cursor.executemany(
            "DELETE FROM UserSessions WHERE user_id = %s;",
            (("test",), ("anothertest",)),
        )
        self.assertIsNone(cursor.description)
        self.assertEqual(cursor.rowcount, 24)  # 24 because 2 * 12 because cumulatve.

    def test_executemany_empty(self):
        from google.cloud.bigquery.dbapi import connect

        connection = connect(self._mock_client(rows=[], num_dml_affected_rows=12))
        cursor = connection.cursor()
        cursor.executemany((), ())
        self.assertIsNone(cursor.description)
        self.assertEqual(cursor.rowcount, -1)

    def test_is_iterable(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(
            self._mock_client(rows=[("hello", "there", 7), ("good", "bye", -3)])
        )
        cursor = connection.cursor()
        cursor.execute("SELECT foo, bar, baz FROM hello_world WHERE baz < 42;")

        rows_iter = iter(cursor)

        row = next(rows_iter)
        self.assertEqual(row, ("hello", "there", 7))
        row = next(rows_iter)
        self.assertEqual(row, ("good", "bye", -3))
        self.assertRaises(StopIteration, next, rows_iter)

        self.assertEqual(
            list(cursor),
            [],
            "Iterating again over the same results should produce no rows.",
        )

    def test_query_job_wo_execute(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(self._mock_client())
        cursor = connection.cursor()
        self.assertIsNone(cursor.query_job)

    def test_query_job_w_execute(self):
        from google.cloud.bigquery import QueryJob, dbapi

        connection = dbapi.connect(self._mock_client())
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        self.assertIsInstance(cursor.query_job, QueryJob)

    def test_query_job_w_execute_no_job(self):
        from google.cloud.bigquery import dbapi

        connection = dbapi.connect(self._mock_client())
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")

        # Simulate jobless execution.
        type(cursor._query_rows).job_id = mock.PropertyMock(return_value=None)

        self.assertIsNone(cursor.query_job)

    def test_query_job_w_executemany(self):
        from google.cloud.bigquery import QueryJob, dbapi

        connection = dbapi.connect(self._mock_client())
        cursor = connection.cursor()
        cursor.executemany("SELECT %s;", (("1",), ("2",)))
        self.assertIsInstance(cursor.query_job, QueryJob)

    def test__format_operation_w_dict(self):
        from google.cloud.bigquery.dbapi import cursor

        parameter_types = {}
        formatted_operation, parameter_types = cursor._format_operation(
            "SELECT %(somevalue)s, %(a `weird` one:STRING)s;",
            {"somevalue": "hi", "a `weird` one": "world"},
        )
        self.assertEqual(
            formatted_operation, "SELECT @`somevalue`, @`a \\`weird\\` one`;"
        )
        self.assertEqual(parameter_types, {"a `weird` one": "STRING"})

    def test__format_operation_w_wrong_dict(self):
        from google.cloud.bigquery import dbapi
        from google.cloud.bigquery.dbapi import cursor

        self.assertRaises(
            dbapi.ProgrammingError,
            cursor._format_operation,
            "SELECT %(somevalue)s, %(othervalue)s;",
            {"somevalue-not-here": "hi", "othervalue": "world"},
        )

    def test__format_operation_w_redundant_dict_key(self):
        from google.cloud.bigquery.dbapi import cursor

        formatted_operation, _ = cursor._format_operation(
            "SELECT %(somevalue)s;", {"somevalue": "foo", "value-not-used": "bar"}
        )
        self.assertEqual(formatted_operation, "SELECT @`somevalue`;")

    def test__format_operation_w_sequence(self):
        from google.cloud.bigquery.dbapi import cursor

        formatted_operation, _ = cursor._format_operation(
            "SELECT %s, %s;", ("hello", "world")
        )
        self.assertEqual(formatted_operation, "SELECT ?, ?;")

    def test__format_operation_w_too_short_sequence(self):
        from google.cloud.bigquery import dbapi
        from google.cloud.bigquery.dbapi import cursor

        self.assertRaises(
            dbapi.ProgrammingError,
            cursor._format_operation,
            "SELECT %s, %s;",
            ("hello",),
        )

    def test__format_operation_w_too_long_sequence(self):
        from google.cloud.bigquery import dbapi
        from google.cloud.bigquery.dbapi import cursor

        self.assertRaises(
            dbapi.ProgrammingError,
            cursor._format_operation,
            "SELECT %s, %s;",
            ("hello", "world", "everyone"),
        )

    def test__format_operation_w_empty_dict(self):
        from google.cloud.bigquery.dbapi import cursor

        formatted_operation, _ = cursor._format_operation("SELECT '%f'", {})
        self.assertEqual(formatted_operation, "SELECT '%f'")

    def test__format_operation_wo_params_single_percent(self):
        from google.cloud.bigquery.dbapi import cursor

        formatted_operation, _ = cursor._format_operation("SELECT '%'", {})
        self.assertEqual(formatted_operation, "SELECT '%'")

    def test__format_operation_wo_params_double_percents(self):
        from google.cloud.bigquery.dbapi import cursor

        formatted_operation, _ = cursor._format_operation("SELECT '%%'", {})
        self.assertEqual(formatted_operation, "SELECT '%'")

    def test__format_operation_unescaped_percent_w_dict_param(self):
        from google.cloud.bigquery import dbapi
        from google.cloud.bigquery.dbapi import cursor

        self.assertRaises(
            dbapi.ProgrammingError,
            cursor._format_operation,
            "SELECT %(foo)s, '100 %';",
            {"foo": "bar"},
        )

    def test__format_operation_unescaped_percent_w_list_param(self):
        from google.cloud.bigquery import dbapi
        from google.cloud.bigquery.dbapi import cursor

        self.assertRaises(
            dbapi.ProgrammingError,
            cursor._format_operation,
            "SELECT %s, %s, '100 %';",
            ["foo", "bar"],
        )

    def test__format_operation_no_placeholders(self):
        from google.cloud.bigquery import dbapi
        from google.cloud.bigquery.dbapi import cursor

        self.assertRaises(
            dbapi.ProgrammingError,
            cursor._format_operation,
            "SELECT 42",
            ["foo", "bar"],
        )


@pytest.mark.parametrize(
    "inp,expect",
    [
        ("", ("", None)),
        ("values(%(foo)s, %(bar)s)", ("values(%(foo)s, %(bar)s)", {})),
        (
            "values('%%(oof:INT64)s', %(foo)s, %(bar)s)",
            ("values('%%(oof:INT64)s', %(foo)s, %(bar)s)", {}),
        ),
        (
            "values(%(foo:INT64)s, %(bar)s)",
            ("values(%(foo)s, %(bar)s)", dict(foo="INT64")),
        ),
        (
            "values('%%(oof:INT64)s, %(foo:INT64)s, %(foo)s)",
            ("values('%%(oof:INT64)s, %(foo)s, %(foo)s)", dict(foo="INT64")),
        ),
        (
            "values(%(foo:INT64)s, %(foo:INT64)s)",
            ("values(%(foo)s, %(foo)s)", dict(foo="INT64")),
        ),
        (
            "values(%(foo:INT64)s, %(bar:NUMERIC)s) 100 %",
            ("values(%(foo)s, %(bar)s) 100 %", dict(foo="INT64", bar="NUMERIC")),
        ),
        (" %s %()s %(:int64)s ", (" %s %s %s ", [None, None, "int64"])),
        (" %%s %s %()s %(:int64)s ", (" %%s %s %s %s ", [None, None, "int64"])),
        (
            "values(%%%(foo:INT64)s, %(bar)s)",
            ("values(%%%(foo)s, %(bar)s)", dict(foo="INT64")),
        ),
        (
            "values(%%%%(foo:INT64)s, %(bar)s)",
            ("values(%%%%(foo:INT64)s, %(bar)s)", dict()),
        ),
        (
            "values(%%%%%(foo:INT64)s, %(bar)s)",
            ("values(%%%%%(foo)s, %(bar)s)", dict(foo="INT64")),
        ),
        (
            "values(%%%%%(foo:struct<x_1 string, y_ int64>)s, %(bar)s)",
            ("values(%%%%%(foo)s, %(bar)s)", dict(foo="struct<x_1 string, y_ int64>")),
        ),
        (
            "values(%%%%%(foo:struct<x string, y int64>)s, %(bar)s)",
            ("values(%%%%%(foo)s, %(bar)s)", dict(foo="struct<x string, y int64>")),
        ),
        (
            "values(%%%%%(foo:struct<x string(10), y int64>)s, %(bar)s)",
            ("values(%%%%%(foo)s, %(bar)s)", dict(foo="struct<x string(10), y int64>")),
        ),
        (
            "values(%(foo:struct<x string(10), y numeric(2, 9)>)s, %(bar)s)",
            (
                "values(%(foo)s, %(bar)s)",
                dict(foo="struct<x string(10), y numeric(2, 9)>"),
            ),
        ),
        (
            "values(%(foo:struct<x string(10) , y numeric(2, 9)>)s, %(bar)s)",
            (
                "values(%(foo)s, %(bar)s)",
                dict(foo="struct<x string(10) , y numeric(2, 9)>"),
            ),
        ),
        (
            "values(%(foo:string(10))s, %(bar)s)",
            ("values(%(foo)s, %(bar)s)", dict(foo="string(10)")),
        ),
    ],
)
def test__extract_types(inp, expect):
    from google.cloud.bigquery.dbapi.cursor import _extract_types as et

    assert et(inp) == expect


@pytest.mark.parametrize(
    "match,inp",
    [
        (
            "Conflicting types for foo: numeric and int64.",
            " %(foo:numeric)s %(foo:int64)s ",
        ),
        (r"' %s %\(foo\)s ' mixes named and unamed parameters.", " %s %(foo)s "),
        (r"' %\(foo\)s %s ' mixes named and unamed parameters.", " %(foo)s %s "),
    ],
)
def test__extract_types_fail(match, inp):
    from google.cloud.bigquery.dbapi import exceptions
    from google.cloud.bigquery.dbapi.cursor import _extract_types as et

    with pytest.raises(exceptions.ProgrammingError, match=match):
        et(inp)
