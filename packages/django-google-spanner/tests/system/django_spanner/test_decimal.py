# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from decimal import Decimal

from django.db import connection
from django.test import TransactionTestCase

from tests.system.django_spanner.utils import (
    setup_database,
    setup_instance,
    teardown_database,
    teardown_instance,
)

from .models import Author, Number


class TestDecimal(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        setup_instance()
        setup_database()
        with connection.schema_editor() as editor:
            # Create the tables
            editor.create_model(Author)
            editor.create_model(Number)

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as editor:
            # delete the table
            editor.delete_model(Author)
            editor.delete_model(Number)
        teardown_database()
        teardown_instance()

    def rating_transform(self, value):
        return value["rating"]

    def values_transform(self, value):
        return value.num

    def assertValuesEqual(self, queryset, expected_values, transformer, ordered=True):
        self.assertQuerySetEqual(queryset, expected_values, transformer, ordered)

    def test_insert_and_search_decimal_value(self):
        """
        Tests model object creation with Author model.
        """
        author_kent = Author(
            first_name="Arthur",
            last_name="Kent",
            rating=Decimal("4.1"),
        )
        author_kent.save()
        qs1 = Author.objects.filter(rating__gte=3).values("rating")
        self.assertValuesEqual(
            qs1,
            [Decimal("4.1")],
            self.rating_transform,
        )
        # Delete data from Author table.
        Author.objects.all().delete()

    def test_decimal_filter(self):
        """
        Tests decimal filter query.
        """
        # Insert data into Number table.
        Number.objects.bulk_create(
            Number(num=Decimal(i) / Decimal(10)) for i in range(10)
        )
        qs1 = Number.objects.filter(num__lte=Decimal(2) / Decimal(10))
        self.assertValuesEqual(
            qs1,
            [Decimal(i) / Decimal(10) for i in range(3)],
            self.values_transform,
            ordered=False,
        )
        # Delete data from Number table.
        Number.objects.all().delete()

    def test_decimal_precision_limit(self):
        """
        Tests decimal object precission limit.
        """
        num_val = Number(num=Decimal(1) / Decimal(3))
        with self.assertRaises(ValueError):
            num_val.save()

    def test_decimal_update(self):
        """
        Tests decimal object update.
        """
        author_kent = Author(
            first_name="Arthur",
            last_name="Kent",
            rating=Decimal("4.1"),
        )
        author_kent.save()
        author_kent.rating = Decimal("4.2")
        author_kent.save()
        qs1 = Author.objects.filter(rating__gte=Decimal("4.2")).values("rating")
        self.assertValuesEqual(
            qs1,
            [Decimal("4.2")],
            self.rating_transform,
        )
        # Delete data from Author table.
        Author.objects.all().delete()
