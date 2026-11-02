# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import datetime
import unittest

from django.db import connection
from django.db.utils import IntegrityError
from django.test import TransactionTestCase
from django.utils import timezone

from django_spanner import USE_EMULATOR
from tests.system.django_spanner.utils import (
    setup_database,
    setup_instance,
    teardown_database,
    teardown_instance,
)

from .models import Event


@unittest.skipIf(USE_EMULATOR, "Check Constraint is not implemented in emulator.")
class TestCheckConstraint(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        setup_instance()
        setup_database()
        with connection.schema_editor() as editor:
            # Create the table
            editor.create_model(Event)

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as editor:
            # delete the table
            editor.delete_model(Event)
        teardown_database()
        teardown_instance()

    def test_insert_valid_value(self):
        """
        Tests model object creation with Event model.
        """
        now = timezone.now()
        now_plus_10 = now + datetime.timedelta(minutes=10)
        event_valid = Event(start_date=now, end_date=now_plus_10)
        event_valid.save()
        qs1 = Event.objects.filter().values("start_date")
        self.assertEqual(qs1[0]["start_date"], now)
        # Delete data from Event table.
        Event.objects.all().delete()

    def test_insert_invalid_value(self):
        """
        Tests model object creation with invalid data in Event model.
        """
        now = timezone.now()
        now_minus_1_day = now - timezone.timedelta(days=1)
        event_invalid = Event(start_date=now, end_date=now_minus_1_day)
        with self.assertRaises(IntegrityError):
            event_invalid.save()
