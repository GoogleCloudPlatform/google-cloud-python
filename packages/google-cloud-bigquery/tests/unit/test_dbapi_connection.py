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

import gc
import unittest
from unittest import mock

import pytest


class TestConnection(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.dbapi import Connection

        return Connection

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _mock_client(self):
        from google.cloud.bigquery import client

        mock_client = mock.create_autospec(client.Client)
        return mock_client

    def _mock_bqstorage_client(self):
        # Assumption: bigquery_storage exists. It's the test's responisbility to
        # not use this helper or skip itself if bqstorage is not installed.
        from google.cloud import bigquery_storage

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        mock_client.transport.close = mock.Mock()
        mock_client.transport._grpc_channel = mock.Mock(spec=["close"])
        return mock_client

    def test_ctor_wo_bqstorage_client(self):
        from google.cloud.bigquery.dbapi import Connection

        mock_client = self._mock_client()
        mock_client._ensure_bqstorage_client.return_value = None

        connection = self._make_one(client=mock_client)
        self.assertIsInstance(connection, Connection)
        self.assertIs(connection._client, mock_client)
        self.assertIs(connection._bqstorage_client, None)

    def test_ctor_w_bqstorage_client(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        from google.cloud.bigquery.dbapi import Connection

        mock_client = self._mock_client()
        mock_bqstorage_client = self._mock_bqstorage_client()
        mock_client._ensure_bqstorage_client.return_value = mock_bqstorage_client

        connection = self._make_one(
            client=mock_client,
            bqstorage_client=mock_bqstorage_client,
        )

        mock_client._ensure_bqstorage_client.assert_called_once_with(
            mock_bqstorage_client
        )
        self.assertIsInstance(connection, Connection)
        self.assertIs(connection._client, mock_client)
        self.assertIs(connection._bqstorage_client, mock_bqstorage_client)

    @mock.patch("google.cloud.bigquery.Client", autospec=True)
    def test_connect_wo_client(self, mock_client):
        from google.cloud.bigquery.dbapi import Connection, connect

        connection = connect()
        self.assertIsInstance(connection, Connection)
        self.assertIsNotNone(connection._client)
        self.assertIsNotNone(connection._bqstorage_client)

    def test_connect_w_client(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        from google.cloud.bigquery.dbapi import Connection, connect

        mock_client = self._mock_client()
        mock_bqstorage_client = self._mock_bqstorage_client()
        mock_client._ensure_bqstorage_client.return_value = mock_bqstorage_client

        connection = connect(client=mock_client)

        mock_client._ensure_bqstorage_client.assert_called_once_with()
        self.assertIsInstance(connection, Connection)
        self.assertIs(connection._client, mock_client)
        self.assertIs(connection._bqstorage_client, mock_bqstorage_client)

    def test_connect_w_both_clients(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        from google.cloud.bigquery.dbapi import Connection, connect

        mock_client = self._mock_client()
        mock_bqstorage_client = self._mock_bqstorage_client()
        mock_client._ensure_bqstorage_client.return_value = mock_bqstorage_client

        connection = connect(
            client=mock_client,
            bqstorage_client=mock_bqstorage_client,
        )

        mock_client._ensure_bqstorage_client.assert_called_once_with(
            mock_bqstorage_client
        )
        self.assertIsInstance(connection, Connection)
        self.assertIs(connection._client, mock_client)
        self.assertIs(connection._bqstorage_client, mock_bqstorage_client)

    def test_connect_prefer_bqstorage_client_false(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        from google.cloud.bigquery.dbapi import Connection, connect

        mock_client = self._mock_client()
        mock_bqstorage_client = self._mock_bqstorage_client()
        mock_client._ensure_bqstorage_client.return_value = mock_bqstorage_client

        connection = connect(
            client=mock_client,
            bqstorage_client=mock_bqstorage_client,
            prefer_bqstorage_client=False,
        )

        mock_client._ensure_bqstorage_client.assert_not_called()
        self.assertIsInstance(connection, Connection)
        self.assertIs(connection._client, mock_client)
        self.assertIs(connection._bqstorage_client, None)

    def test_raises_error_if_closed(self):
        from google.cloud.bigquery.dbapi.exceptions import ProgrammingError

        connection = self._make_one(client=self._mock_client())

        connection.close()

        for method in ("close", "commit", "cursor"):
            with self.assertRaisesRegex(
                ProgrammingError, r"Operating on a closed connection\."
            ):
                getattr(connection, method)()

    def _verify_close_closes_all_created_bigquery_clients(
        self, simulate_no_grpc_channel=False
    ):
        pytest.importorskip("google.cloud.bigquery_storage")
        client = self._mock_client()
        bqstorage_client = self._mock_bqstorage_client()

        if simulate_no_grpc_channel:
            bqstorage_client.transport._grpc_channel = None

        client_patcher = mock.patch(
            "google.cloud.bigquery.dbapi.connection.bigquery.Client",
            return_value=client,
        )
        bqstorage_client_patcher = mock.patch.object(
            client,
            "_ensure_bqstorage_client",
            return_value=bqstorage_client,
        )

        with client_patcher, bqstorage_client_patcher:
            connection = self._make_one(client=None, bqstorage_client=None)

        connection.close()

        self.assertTrue(client.close.called)
        self.assertTrue(bqstorage_client.transport.close.called)

        if not simulate_no_grpc_channel:
            self.assertTrue(bqstorage_client.transport._grpc_channel.close.called)

    def test_close_closes_all_created_bigquery_clients(self):
        self._verify_close_closes_all_created_bigquery_clients(
            simulate_no_grpc_channel=False
        )

    def test_close_closes_all_created_bigquery_clients_no_grpc_channel(self):
        self._verify_close_closes_all_created_bigquery_clients(
            simulate_no_grpc_channel=True
        )

    def test_close_does_not_close_bigquery_clients_passed_to_it(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        client = self._mock_client()
        bqstorage_client = self._mock_bqstorage_client()
        connection = self._make_one(client=client, bqstorage_client=bqstorage_client)

        connection.close()

        self.assertFalse(client.close.called)
        self.assertFalse(bqstorage_client.transport.close.called)
        self.assertFalse(bqstorage_client.transport._grpc_channel.close.called)

    def test_close_closes_all_created_cursors(self):
        connection = self._make_one(client=self._mock_client())
        cursor_1 = connection.cursor()
        cursor_2 = connection.cursor()
        self.assertFalse(cursor_1._closed)
        self.assertFalse(cursor_2._closed)

        connection.close()

        self.assertTrue(cursor_1._closed)
        self.assertTrue(cursor_2._closed)

    def test_close_closes_only_open_created_cursors(self):
        connection = self._make_one(client=self._mock_client())
        cursor_1 = connection.cursor()
        cursor_2 = connection.cursor()
        self.assertFalse(cursor_1._closed)
        self.assertFalse(cursor_2._closed)

        cursor_1.close()
        self.assertTrue(cursor_1._closed)
        cursor_1.close = mock.MagicMock()

        connection.close()

        self.assertFalse(cursor_1.close.called)
        self.assertTrue(cursor_2._closed)

    def test_does_not_keep_cursor_instances_alive(self):
        from google.cloud.bigquery.dbapi import Cursor

        connection = self._make_one(client=self._mock_client())
        cursor_1 = connection.cursor()  # noqa
        cursor_2 = connection.cursor()
        cursor_3 = connection.cursor()  # noqa

        del cursor_2

        # Connections should not hold strong references to the Cursor instances
        # they created, unnecessarily keeping them alive.
        gc.collect()
        cursor_count = 0
        for obj in gc.get_objects():
            try:
                if isinstance(obj, Cursor):
                    cursor_count += 1
            except ReferenceError:  # pragma: NO COVER
                pass
        self.assertEqual(cursor_count, 2)

    def test_commit(self):
        connection = self._make_one(client=self._mock_client())
        # commit() is a no-op, there is nothing to test.
        connection.commit()

    def test_cursor(self):
        from google.cloud.bigquery.dbapi import Cursor

        connection = self._make_one(client=self._mock_client())
        cursor = connection.cursor()
        self.assertIsInstance(cursor, Cursor)
        self.assertIs(cursor.connection, connection)
