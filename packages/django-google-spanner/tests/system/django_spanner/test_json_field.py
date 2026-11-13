# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.db import connection, models
from django.test import TransactionTestCase

from tests.system.django_spanner.utils import (
    setup_database,
    setup_instance,
    teardown_database,
    teardown_instance,
)

from .models import Detail


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
        json_null = Detail(value=models.Value(None, models.JSONField()))
        json_null.save()
        json_prim = Detail(value="hello")
        json_prim.save()

        by_key = list(Detail.objects.filter(value__name="Jakob"))
        self.assertEqual(len(by_key), 1)
        self.assertEqual(by_key[0].value, {"name": "Jakob", "age": "26"})

        by_has_key = list(Detail.objects.filter(value__has_key="name"))
        self.assertEqual(len(by_has_key), 1)
        self.assertEqual(by_has_key[0].value, {"name": "Jakob", "age": "26"})

        by_json_null = list(
            Detail.objects.filter(value=models.Value(None, models.JSONField()))
        )
        self.assertEqual(len(by_json_null), 1)
        self.assertIsNone(by_json_null[0].value)

        by_none_exact = list(Detail.objects.filter(value=None))
        self.assertEqual(len(by_none_exact), 1)
        self.assertEqual(by_none_exact[0].id, json_null.id)
        self.assertIsNone(by_none_exact[0].value)

        by_sql_null = list(Detail.objects.filter(value__isnull=True))
        self.assertEqual(len(by_sql_null), 0)

        by_prim = list(Detail.objects.filter(value="hello"))
        self.assertEqual(len(by_prim), 1)
        self.assertEqual(by_prim[0].value, "hello")

        # Delete data from Detail table.
        Detail.objects.all().delete()
