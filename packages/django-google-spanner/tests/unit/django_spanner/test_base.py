# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from unittest import mock

from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass


class TestBase(SpannerSimpleTestClass):
    def setUp(self):
        super().setUp()
        import django_spanner.base

        django_spanner.base._SPANNER_CLIENT_CACHE = None
        self.client_patcher = mock.patch("django_spanner.base.spanner.Client")
        self.mock_client = self.client_patcher.start()
        self.mock_client.return_value.instance.return_value.instance_id = (
            self.INSTANCE_ID
        )
        self.addCleanup(self.client_patcher.stop)

    def test_property_instance(self):
        with mock.patch("django_spanner.base.spanner") as mock_spanner:
            mock_spanner.Client = mock_client = mock.MagicMock()
            mock_client.return_value.instance = mock_instance = mock.MagicMock()
            _ = self.db_wrapper.instance
            # Instance should be called on the return value of Client()
            self.assertTrue(mock_instance.called)

    def test_property_nodb_connection(self):
        with self.assertRaises(NotImplementedError):
            self.db_wrapper._nodb_connection()

    def test_get_connection_params(self):
        params = self.db_wrapper.get_connection_params()

        self.assertEqual(params["project"], self.PROJECT)
        self.assertEqual(params["instance_id"], self.INSTANCE_ID)
        self.assertEqual(params["database_id"], self.DATABASE_ID)
        self.assertEqual(params["user_agent"], self.USER_AGENT)
        self.assertEqual(params["option"], self.OPTIONS["option"])

    def test_get_new_connection(self):
        self.db_wrapper.Database = mock_database = mock.MagicMock()
        mock_database.connect = mock_connection = mock.MagicMock()
        conn_params = {"test_param": "dummy"}
        self.db_wrapper.get_new_connection(conn_params)
        mock_connection.assert_called_once_with(
            self.INSTANCE_ID,
            client=mock_database.connect.call_args[1]["client"],
            **conn_params,
        )

    def test_init_connection_state(self):
        from google.cloud.spanner_dbapi.connection import Connection

        self.db_wrapper.connection = mock_connection = Connection(
            self.db_wrapper.instance, "dummy_db"
        )
        mock_connection.close = mock_close = mock.MagicMock()
        self.db_wrapper.init_connection_state()
        mock_close.assert_called_once_with()

    def test_create_cursor(self):
        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.cursor = mock_cursor = mock.MagicMock()
        self.db_wrapper.create_cursor()
        mock_cursor.assert_called_once_with()

    def test_set_autocommit(self):
        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.autocommit = False
        self.db_wrapper._set_autocommit(True)
        self.assertEqual(mock_connection.autocommit, True)

    def test_is_usable(self):
        self.db_wrapper.connection = None
        self.assertFalse(self.db_wrapper.is_usable())

        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.is_closed = True
        self.assertFalse(self.db_wrapper.is_usable())

        mock_connection.is_closed = False
        self.assertTrue(self.db_wrapper.is_usable())

    def test_is_usable_with_error(self):
        from google.cloud.spanner_dbapi.exceptions import Error

        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.cursor = mock.MagicMock(side_effect=Error)
        self.assertFalse(self.db_wrapper.is_usable())

    def test_start_transaction_under_autocommit(self):
        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.cursor = mock_cursor = mock.MagicMock()
        self.db_wrapper._start_transaction_under_autocommit()
        mock_cursor.assert_called_once_with()
