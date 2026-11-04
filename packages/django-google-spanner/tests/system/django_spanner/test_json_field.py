# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import unittest

from django.db import connection
from django.test import TransactionTestCase

from django_spanner import USE_EMULATOR
from tests.system.django_spanner.utils import (
    setup_database,
    setup_instance,
    teardown_database,
    teardown_instance,
)

from .models import Detail


@unittest.skipIf(USE_EMULATOR, "Jsonfield is not implemented in emulator.")
class TestJsonField(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        setup_instance()
        setup_database()
        with connection.schema_editor() as editor:
            # Create the tables
            editor.create_model(Detail)

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as editor:
            # delete the table
            editor.delete_model(Detail)
        teardown_database()
        teardown_instance()

    def test_insert_and_fetch_value(self):
        """
        Tests model object creation with Detail model.
        Inserting json data into the model and retrieving it.
        """
        json_data = Detail(value={"name": "Jakob", "age": "26"})
        json_data.save()
        qs1 = Detail.objects.all()
        self.assertEqual(qs1[0].value, {"name": "Jakob", "age": "26"})
        # Delete data from Detail table.
        Detail.objects.all().delete()
