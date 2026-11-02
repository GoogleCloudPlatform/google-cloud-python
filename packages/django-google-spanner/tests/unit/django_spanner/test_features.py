# Copyright 2026 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django_spanner.features import DatabaseFeatures
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass


class TestFeatures(SpannerSimpleTestClass):
    def test_introspected_field_types(self):
        features = DatabaseFeatures(self.connection)
        field_types = features.introspected_field_types
        self.assertEqual(field_types["BigIntegerField"], "IntegerField")
        self.assertEqual(field_types["BigAutoField"], "AutoField")
        self.assertEqual(field_types["SmallAutoField"], "AutoField")
        self.assertEqual(field_types["SmallIntegerField"], "IntegerField")
        self.assertEqual(field_types["PositiveBigIntegerField"], "IntegerField")
        self.assertEqual(field_types["PositiveIntegerField"], "IntegerField")
        self.assertEqual(field_types["PositiveSmallIntegerField"], "IntegerField")
        self.assertEqual(field_types["DurationField"], "IntegerField")

    def test_spanner_specific_feature_flags(self):
        features = DatabaseFeatures(self.connection)
        self.assertTrue(features.supports_any_value)
        self.assertTrue(features.supports_covering_indexes)
        self.assertTrue(features.supports_stored_generated_columns)
        self.assertTrue(features.supports_composite_primary_keys)
        self.assertFalse(features.supports_subqueries_in_group_by)
        self.assertFalse(features.supports_order_by_nulls_modifier)
        self.assertFalse(features.supports_expression_indexes)
        self.assertFalse(features.uses_savepoints)
        self.assertFalse(features.can_rollback_tests)
        self.assertEqual(features.max_query_params, 900)
        self.assertTrue(features.requires_literal_defaults)
