# Copyright 2026 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import os
from unittest import mock

from django.db.backends.base.creation import BaseDatabaseCreation

from django_spanner.creation import DatabaseCreation
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass


class TestCreation(SpannerSimpleTestClass):
    def test_create_test_db_returns_db_name_without_private_flag(self):
        creation = DatabaseCreation(self.connection)

        with mock.patch.object(
            BaseDatabaseCreation,
            "create_test_db",
            return_value="test_database_id",
        ):
            result = creation.create_test_db(verbosity=0, autoclobber=True)

        self.assertEqual(result, "test_database_id")
        self.assertFalse(hasattr(self.connection, "_batch_ddl_in_schema_editor"))

    def test_create_test_db_marks_skips_when_env_set(self):
        creation = DatabaseCreation(self.connection)

        with (
            mock.patch.dict(os.environ, {"RUNNING_SPANNER_BACKEND_TESTS": "1"}),
            mock.patch.object(creation, "mark_skips") as mock_mark_skips,
            mock.patch.object(
                BaseDatabaseCreation,
                "create_test_db",
                return_value="test_database_id",
            ),
        ):
            result = creation.create_test_db(verbosity=0, autoclobber=True)

        self.assertEqual(result, "test_database_id")
        mock_mark_skips.assert_called_once_with()
