# Copyright 2015 Google LLC
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

import copy
import warnings

import pytest

from .helpers import _Base


class TestLoadJobConfig(_Base):
    JOB_TYPE = "load"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import LoadJobConfig

        return LoadJobConfig

    def test_ctor_w_properties(self):
        config = self._get_target_class()(
            allow_jagged_rows=True, allow_quoted_newlines=True
        )

        self.assertTrue(config.allow_jagged_rows)
        self.assertTrue(config.allow_quoted_newlines)

    def test_allow_jagged_rows_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.allow_jagged_rows)

    def test_allow_jagged_rows_hit(self):
        config = self._get_target_class()()
        config._properties["load"]["allowJaggedRows"] = True
        self.assertTrue(config.allow_jagged_rows)

    def test_allow_jagged_rows_setter(self):
        config = self._get_target_class()()
        config.allow_jagged_rows = True
        self.assertTrue(config._properties["load"]["allowJaggedRows"])

    def test_allow_quoted_newlines_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.allow_quoted_newlines)

    def test_allow_quoted_newlines_hit(self):
        config = self._get_target_class()()
        config._properties["load"]["allowQuotedNewlines"] = True
        self.assertTrue(config.allow_quoted_newlines)

    def test_allow_quoted_newlines_setter(self):
        config = self._get_target_class()()
        config.allow_quoted_newlines = True
        self.assertTrue(config._properties["load"]["allowQuotedNewlines"])

    def test_autodetect_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.autodetect)

    def test_autodetect_hit(self):
        config = self._get_target_class()()
        config._properties["load"]["autodetect"] = True
        self.assertTrue(config.autodetect)

    def test_autodetect_setter(self):
        config = self._get_target_class()()
        config.autodetect = True
        self.assertTrue(config._properties["load"]["autodetect"])

    def test_clustering_fields_miss(self):
        config = self._get_target_class()()
        self.assertIsNone(config.clustering_fields)

    def test_clustering_fields_hit(self):
        config = self._get_target_class()()
        fields = ["email", "postal_code"]
        config._properties["load"]["clustering"] = {"fields": fields}
        self.assertEqual(config.clustering_fields, fields)

    def test_clustering_fields_setter(self):
        fields = ["email", "postal_code"]
        config = self._get_target_class()()
        config.clustering_fields = fields
        self.assertEqual(config._properties["load"]["clustering"], {"fields": fields})

    def test_clustering_fields_setter_w_none(self):
        config = self._get_target_class()()
        fields = ["email", "postal_code"]
        config._properties["load"]["clustering"] = {"fields": fields}
        config.clustering_fields = None
        self.assertIsNone(config.clustering_fields)
        self.assertNotIn("clustering", config._properties["load"])

    def test_create_disposition_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.create_disposition)

    def test_create_disposition_hit(self):
        from google.cloud.bigquery.job import CreateDisposition

        disposition = CreateDisposition.CREATE_IF_NEEDED
        config = self._get_target_class()()
        config._properties["load"]["createDisposition"] = disposition
        self.assertEqual(config.create_disposition, disposition)

    def test_create_disposition_setter(self):
        from google.cloud.bigquery.job import CreateDisposition

        disposition = CreateDisposition.CREATE_IF_NEEDED
        config = self._get_target_class()()
        config.create_disposition = disposition
        self.assertEqual(config._properties["load"]["createDisposition"], disposition)

    def test_connection_properties(self):
        from google.cloud.bigquery.query import ConnectionProperty

        config = self._get_target_class()()
        self.assertEqual(len(config.connection_properties), 0)

        session_id = ConnectionProperty("session_id", "abcd")
        time_zone = ConnectionProperty("time_zone", "America/Chicago")
        config.connection_properties = [session_id, time_zone]
        self.assertEqual(len(config.connection_properties), 2)
        self.assertEqual(config.connection_properties[0].key, "session_id")
        self.assertEqual(config.connection_properties[0].value, "abcd")
        self.assertEqual(config.connection_properties[1].key, "time_zone")
        self.assertEqual(config.connection_properties[1].value, "America/Chicago")

    def test_create_session(self):
        config = self._get_target_class()()
        self.assertIsNone(config.create_session)
        config.create_session = True
        self.assertTrue(config.create_session)

    def test_decimal_target_types_miss(self):
        config = self._get_target_class()()
        self.assertIsNone(config.decimal_target_types)

    def test_decimal_target_types_hit(self):
        from google.cloud.bigquery.enums import DecimalTargetType

        config = self._get_target_class()()
        decimal_target_types = [DecimalTargetType.NUMERIC, DecimalTargetType.STRING]
        config._properties["load"]["decimalTargetTypes"] = decimal_target_types

        expected = frozenset(decimal_target_types)
        self.assertEqual(config.decimal_target_types, expected)

    def test_decimal_target_types_setter(self):
        from google.cloud.bigquery.enums import DecimalTargetType

        decimal_target_types = (DecimalTargetType.NUMERIC, DecimalTargetType.BIGNUMERIC)
        config = self._get_target_class()()
        config.decimal_target_types = decimal_target_types
        self.assertEqual(
            config._properties["load"]["decimalTargetTypes"],
            list(decimal_target_types),
        )

    def test_decimal_target_types_setter_w_none(self):
        from google.cloud.bigquery.enums import DecimalTargetType

        config = self._get_target_class()()
        decimal_target_types = [DecimalTargetType.BIGNUMERIC]
        config._properties["load"]["decimalTargetTypes"] = decimal_target_types

        config.decimal_target_types = None

        self.assertIsNone(config.decimal_target_types)
        self.assertNotIn("decimalTargetTypes", config._properties["load"])

        config.decimal_target_types = None  # No error if unsetting an unset property.

    def test_destination_encryption_configuration_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.destination_encryption_configuration)

    def test_destination_encryption_configuration_hit(self):
        from google.cloud.bigquery.encryption_configuration import (
            EncryptionConfiguration,
        )

        kms_key_name = "kms-key-name"
        encryption_configuration = EncryptionConfiguration(kms_key_name)
        config = self._get_target_class()()
        config._properties["load"]["destinationEncryptionConfiguration"] = {
            "kmsKeyName": kms_key_name
        }
        self.assertEqual(
            config.destination_encryption_configuration, encryption_configuration
        )

    def test_destination_encryption_configuration_setter(self):
        from google.cloud.bigquery.encryption_configuration import (
            EncryptionConfiguration,
        )

        kms_key_name = "kms-key-name"
        encryption_configuration = EncryptionConfiguration(kms_key_name)
        config = self._get_target_class()()
        config.destination_encryption_configuration = encryption_configuration
        expected = {"kmsKeyName": kms_key_name}
        self.assertEqual(
            config._properties["load"]["destinationEncryptionConfiguration"], expected
        )

    def test_destination_encryption_configuration_setter_w_none(self):
        kms_key_name = "kms-key-name"
        config = self._get_target_class()()
        config._properties["load"]["destinationEncryptionConfiguration"] = {
            "kmsKeyName": kms_key_name
        }
        config.destination_encryption_configuration = None
        self.assertIsNone(config.destination_encryption_configuration)
        self.assertNotIn(
            "destinationEncryptionConfiguration", config._properties["load"]
        )

    def test_destination_table_description_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.destination_table_description)

    def test_destination_table_description_hit(self):
        description = "Description"
        config = self._get_target_class()()
        config._properties["load"]["destinationTableProperties"] = {
            "description": description
        }
        self.assertEqual(config.destination_table_description, description)

    def test_destination_table_description_setter(self):
        description = "Description"
        config = self._get_target_class()()
        config.destination_table_description = description
        expected = {"description": description}
        self.assertEqual(
            config._properties["load"]["destinationTableProperties"], expected
        )

    def test_destination_table_description_setter_w_fn_already(self):
        description = "Description"
        friendly_name = "Friendly Name"
        config = self._get_target_class()()
        config._properties["load"]["destinationTableProperties"] = {
            "friendlyName": friendly_name
        }
        config.destination_table_description = description
        expected = {"friendlyName": friendly_name, "description": description}
        self.assertEqual(
            config._properties["load"]["destinationTableProperties"], expected
        )

    def test_destination_table_description_w_none(self):
        description = "Description"
        friendly_name = "Friendly Name"
        config = self._get_target_class()()
        config._properties["load"]["destinationTableProperties"] = {
            "description": description,
            "friendlyName": friendly_name,
        }
        config.destination_table_description = None
        expected = {"friendlyName": friendly_name}
        self.assertEqual(
            config._properties["load"]["destinationTableProperties"], expected
        )

    def test_destination_table_friendly_name_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.destination_table_friendly_name)

    def test_destination_table_friendly_name_hit(self):
        friendly_name = "Friendly Name"
        config = self._get_target_class()()
        config._properties["load"]["destinationTableProperties"] = {
            "friendlyName": friendly_name
        }
        self.assertEqual(config.destination_table_friendly_name, friendly_name)

    def test_destination_table_friendly_name_setter(self):
        friendly_name = "Friendly Name"
        config = self._get_target_class()()
        config.destination_table_friendly_name = friendly_name
        expected = {"friendlyName": friendly_name}
        self.assertEqual(
            config._properties["load"]["destinationTableProperties"], expected
        )

    def test_destination_table_friendly_name_setter_w_descr_already(self):
        friendly_name = "Friendly Name"
        description = "Description"
        config = self._get_target_class()()
        config._properties["load"]["destinationTableProperties"] = {
            "description": description
        }
        config.destination_table_friendly_name = friendly_name
        expected = {"friendlyName": friendly_name, "description": description}
        self.assertEqual(
            config._properties["load"]["destinationTableProperties"], expected
        )

    def test_destination_table_friendly_name_w_none(self):
        friendly_name = "Friendly Name"
        description = "Description"
        config = self._get_target_class()()
        config._properties["load"]["destinationTableProperties"] = {
            "description": description,
            "friendlyName": friendly_name,
        }
        config.destination_table_friendly_name = None
        expected = {"description": description}
        self.assertEqual(
            config._properties["load"]["destinationTableProperties"], expected
        )

    def test_encoding_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.encoding)

    def test_encoding_hit(self):
        from google.cloud.bigquery.job import Encoding

        encoding = Encoding.UTF_8
        config = self._get_target_class()()
        config._properties["load"]["encoding"] = encoding
        self.assertEqual(config.encoding, encoding)

    def test_encoding_setter(self):
        from google.cloud.bigquery.job import Encoding

        encoding = Encoding.UTF_8
        config = self._get_target_class()()
        config.encoding = encoding
        self.assertEqual(config._properties["load"]["encoding"], encoding)

    def test_field_delimiter_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.field_delimiter)

    def test_field_delimiter_hit(self):
        field_delimiter = "|"
        config = self._get_target_class()()
        config._properties["load"]["fieldDelimiter"] = field_delimiter
        self.assertEqual(config.field_delimiter, field_delimiter)

    def test_field_delimiter_setter(self):
        field_delimiter = "|"
        config = self._get_target_class()()
        config.field_delimiter = field_delimiter
        self.assertEqual(config._properties["load"]["fieldDelimiter"], field_delimiter)

    def test_hive_partitioning_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.hive_partitioning)

    def test_hive_partitioning_hit(self):
        from google.cloud.bigquery.external_config import HivePartitioningOptions

        config = self._get_target_class()()
        config._properties["load"]["hivePartitioningOptions"] = {
            "sourceUriPrefix": "http://foo/bar",
            "mode": "STRINGS",
        }
        result = config.hive_partitioning
        self.assertIsInstance(result, HivePartitioningOptions)
        self.assertEqual(result.source_uri_prefix, "http://foo/bar")
        self.assertEqual(result.mode, "STRINGS")

    def test_hive_partitioning_setter(self):
        from google.cloud.bigquery.external_config import HivePartitioningOptions

        hive_partitioning = HivePartitioningOptions()
        hive_partitioning.source_uri_prefix = "http://foo/bar"
        hive_partitioning.mode = "AUTO"

        config = self._get_target_class()()
        config.hive_partitioning = hive_partitioning
        self.assertEqual(
            config._properties["load"]["hivePartitioningOptions"],
            {"sourceUriPrefix": "http://foo/bar", "mode": "AUTO"},
        )

        config.hive_partitioning = None
        self.assertIsNone(config._properties["load"]["hivePartitioningOptions"])

    def test_hive_partitioning_invalid_type(self):
        config = self._get_target_class()()

        with self.assertRaises(TypeError):
            config.hive_partitioning = {"mode": "AUTO"}

    def test_ignore_unknown_values_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.ignore_unknown_values)

    def test_ignore_unknown_values_hit(self):
        config = self._get_target_class()()
        config._properties["load"]["ignoreUnknownValues"] = True
        self.assertTrue(config.ignore_unknown_values)

    def test_ignore_unknown_values_setter(self):
        config = self._get_target_class()()
        config.ignore_unknown_values = True
        self.assertTrue(config._properties["load"]["ignoreUnknownValues"])

    def test_json_extension_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.json_extension)

    def test_json_extension_hit(self):
        config = self._get_target_class()()
        config._properties["load"]["jsonExtension"] = "GEOJSON"
        self.assertEqual(config.json_extension, "GEOJSON")

    def test_json_extension_setter(self):
        config = self._get_target_class()()
        self.assertFalse(config.json_extension)
        config.json_extension = "GEOJSON"
        self.assertTrue(config.json_extension)
        self.assertEqual(config._properties["load"]["jsonExtension"], "GEOJSON")

    def test_to_api_repr_includes_json_extension(self):
        config = self._get_target_class()()
        config._properties["load"]["jsonExtension"] = "GEOJSON"
        api_repr = config.to_api_repr()
        self.assertIn("jsonExtension", api_repr["load"])
        self.assertEqual(api_repr["load"]["jsonExtension"], "GEOJSON")

    def test_max_bad_records_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.max_bad_records)

    def test_max_bad_records_hit(self):
        max_bad_records = 13
        config = self._get_target_class()()
        config._properties["load"]["maxBadRecords"] = max_bad_records
        self.assertEqual(config.max_bad_records, max_bad_records)

    def test_max_bad_records_setter(self):
        max_bad_records = 13
        config = self._get_target_class()()
        config.max_bad_records = max_bad_records
        self.assertEqual(config._properties["load"]["maxBadRecords"], max_bad_records)

    def test_null_marker_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.null_marker)

    def test_null_marker_hit(self):
        null_marker = "XXX"
        config = self._get_target_class()()
        config._properties["load"]["nullMarker"] = null_marker
        self.assertEqual(config.null_marker, null_marker)

    def test_null_marker_setter(self):
        null_marker = "XXX"
        config = self._get_target_class()()
        config.null_marker = null_marker
        self.assertEqual(config._properties["load"]["nullMarker"], null_marker)

    def test_null_markers_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.null_markers)

    def test_null_markers_hit(self):
        null_markers = ["", "NA"]
        config = self._get_target_class()()
        config._properties["load"]["nullMarkers"] = null_markers
        self.assertEqual(config.null_markers, null_markers)

    def test_null_markers_setter(self):
        null_markers = ["", "NA"]
        config = self._get_target_class()()
        config.null_markers = null_markers
        self.assertEqual(config._properties["load"]["nullMarkers"], null_markers)

    def test_preserve_ascii_control_characters_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.preserve_ascii_control_characters)

    def test_preserve_ascii_control_characters_hit(self):
        config = self._get_target_class()()
        config._properties["load"]["preserveAsciiControlCharacters"] = True
        self.assertTrue(config.preserve_ascii_control_characters)

    def test_preserve_ascii_control_characters_setter(self):
        config = self._get_target_class()()
        config.preserve_ascii_control_characters = True
        self.assertTrue(config._properties["load"]["preserveAsciiControlCharacters"])

    def test_projection_fields_miss(self):
        config = self._get_target_class()()
        self.assertIsNone(config.projection_fields)

    def test_projection_fields_hit(self):
        config = self._get_target_class()()
        fields = ["email", "postal_code"]
        config.projection_fields = fields
        self.assertEqual(config._properties["load"]["projectionFields"], fields)
        self.assertEqual(config.projection_fields, fields)

    def test_quote_character_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.quote_character)

    def test_quote_character_hit(self):
        quote_character = "'"
        config = self._get_target_class()()
        config._properties["load"]["quote"] = quote_character
        self.assertEqual(config.quote_character, quote_character)

    def test_quote_character_setter(self):
        quote_character = "'"
        config = self._get_target_class()()
        config.quote_character = quote_character
        self.assertEqual(config._properties["load"]["quote"], quote_character)

    def test_schema_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.schema)

    def test_schema_hit(self):
        from google.cloud.bigquery.schema import SchemaField

        config = self._get_target_class()()
        all_props_repr = {
            "mode": "REQUIRED",
            "name": "foo",
            "type": "INTEGER",
            "description": "Foo",
        }
        minimal_repr = {"name": "bar", "type": "STRING"}
        config._properties["load"]["schema"] = {
            "fields": [all_props_repr, minimal_repr]
        }
        all_props, minimal = config.schema
        self.assertEqual(all_props, SchemaField.from_api_repr(all_props_repr))
        self.assertEqual(minimal, SchemaField.from_api_repr(minimal_repr))

    def test_schema_setter_fields(self):
        from google.cloud.bigquery.schema import SchemaField

        config = self._get_target_class()()
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        age = SchemaField("age", "INTEGER", mode="REQUIRED")
        config.schema = [full_name, age]
        full_name_repr = {
            "name": "full_name",
            "type": "STRING",
            "mode": "REQUIRED",
        }
        age_repr = {
            "name": "age",
            "type": "INTEGER",
            "mode": "REQUIRED",
        }
        self.assertEqual(
            config._properties["load"]["schema"], {"fields": [full_name_repr, age_repr]}
        )

    def test_schema_setter_valid_mappings_list(self):
        config = self._get_target_class()()

        full_name_repr = {
            "name": "full_name",
            "type": "STRING",
            "mode": "REQUIRED",
        }
        age_repr = {
            "name": "age",
            "type": "INTEGER",
            "mode": "REQUIRED",
        }
        schema = [full_name_repr, age_repr]
        config.schema = schema
        self.assertEqual(
            config._properties["load"]["schema"], {"fields": [full_name_repr, age_repr]}
        )

    def test_schema_setter_allows_unknown_properties(self):
        config = self._get_target_class()()

        schema = [
            {
                "name": "full_name",
                "type": "STRING",
                "mode": "REQUIRED",
                "someNewProperty": "test-value",
            },
            {
                "name": "age",
                # Note: This type should be included, too. Avoid client-side
                # validation, as it could prevent backwards-compatible
                # evolution of the server-side behavior.
                "typo": "INTEGER",
                "mode": "REQUIRED",
                "anotherNewProperty": "another-test",
            },
        ]

        # Make sure the setter doesn't mutate schema.
        expected_schema = copy.deepcopy(schema)

        config.schema = schema

        # _properties should include all fields, including unknown ones.
        assert config._properties["load"]["schema"]["fields"] == expected_schema

    def test_schema_setter_unsetting_schema(self):
        from google.cloud.bigquery.schema import SchemaField

        config = self._get_target_class()()
        config._properties["load"]["schema"] = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
        ]

        config.schema = None
        self.assertNotIn("schema", config._properties["load"])
        config.schema = None  # no error, idempotent operation

    def test_schema_update_options_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.schema_update_options)

    def test_schema_update_options_hit(self):
        from google.cloud.bigquery.job import SchemaUpdateOption

        options = [
            SchemaUpdateOption.ALLOW_FIELD_ADDITION,
            SchemaUpdateOption.ALLOW_FIELD_RELAXATION,
        ]
        config = self._get_target_class()()
        config._properties["load"]["schemaUpdateOptions"] = options
        self.assertEqual(config.schema_update_options, options)

    def test_schema_update_options_setter(self):
        from google.cloud.bigquery.job import SchemaUpdateOption

        options = [
            SchemaUpdateOption.ALLOW_FIELD_ADDITION,
            SchemaUpdateOption.ALLOW_FIELD_RELAXATION,
        ]
        config = self._get_target_class()()
        config.schema_update_options = options
        self.assertEqual(config._properties["load"]["schemaUpdateOptions"], options)

    def test_skip_leading_rows_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.skip_leading_rows)

    def test_skip_leading_rows_hit_w_str(self):
        skip_leading_rows = 1
        config = self._get_target_class()()
        config._properties["load"]["skipLeadingRows"] = str(skip_leading_rows)
        self.assertEqual(config.skip_leading_rows, skip_leading_rows)

    def test_skip_leading_rows_hit_w_integer(self):
        skip_leading_rows = 1
        config = self._get_target_class()()
        config._properties["load"]["skipLeadingRows"] = skip_leading_rows
        self.assertEqual(config.skip_leading_rows, skip_leading_rows)

    def test_skip_leading_rows_setter(self):
        skip_leading_rows = 1
        config = self._get_target_class()()
        config.skip_leading_rows = skip_leading_rows
        self.assertEqual(
            config._properties["load"]["skipLeadingRows"], str(skip_leading_rows)
        )

    def test_source_format_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.source_format)

    def test_source_format_hit(self):
        from google.cloud.bigquery.job import SourceFormat

        source_format = SourceFormat.CSV
        config = self._get_target_class()()
        config._properties["load"]["sourceFormat"] = source_format
        self.assertEqual(config.source_format, source_format)

    def test_source_format_setter(self):
        from google.cloud.bigquery.job import SourceFormat

        source_format = SourceFormat.CSV
        config = self._get_target_class()()
        config.source_format = source_format
        self.assertEqual(config._properties["load"]["sourceFormat"], source_format)

    def test_range_partitioning_w_none(self):
        object_under_test = self._get_target_class()()
        assert object_under_test.range_partitioning is None

    def test_range_partitioning_w_value(self):
        object_under_test = self._get_target_class()()
        object_under_test._properties["load"]["rangePartitioning"] = {
            "field": "column_one",
            "range": {"start": 1, "end": 1000, "interval": 10},
        }
        object_under_test.range_partitioning.field == "column_one"
        object_under_test.range_partitioning.range_.start == 1
        object_under_test.range_partitioning.range_.end == 1000
        object_under_test.range_partitioning.range_.interval == 10

    def test_range_partitioning_setter(self):
        from google.cloud.bigquery.table import PartitionRange
        from google.cloud.bigquery.table import RangePartitioning

        object_under_test = self._get_target_class()()
        object_under_test.range_partitioning = RangePartitioning(
            field="column_one", range_=PartitionRange(start=1, end=1000, interval=10)
        )
        object_under_test.range_partitioning.field == "column_one"
        object_under_test.range_partitioning.range_.start == 1
        object_under_test.range_partitioning.range_.end == 1000
        object_under_test.range_partitioning.range_.interval == 10

    def test_range_partitioning_setter_w_none(self):
        object_under_test = self._get_target_class()()
        object_under_test.range_partitioning = None
        assert object_under_test.range_partitioning is None

    def test_range_partitioning_setter_w_wrong_type(self):
        object_under_test = self._get_target_class()()
        with pytest.raises(ValueError, match="RangePartitioning"):
            object_under_test.range_partitioning = object()

    def test_time_partitioning_miss(self):
        config = self._get_target_class()()
        self.assertIsNone(config.time_partitioning)

    def test_time_partitioning_hit(self):
        from google.cloud.bigquery.table import TimePartitioning
        from google.cloud.bigquery.table import TimePartitioningType

        field = "creation_date"
        year_ms = 86400 * 1000 * 365
        config = self._get_target_class()()
        config._properties["load"]["timePartitioning"] = {
            "type": TimePartitioningType.DAY,
            "field": field,
            "expirationMs": str(year_ms),
            "requirePartitionFilter": False,
        }
        with warnings.catch_warnings(record=True) as warned:
            expected = TimePartitioning(
                type_=TimePartitioningType.DAY,
                field=field,
                expiration_ms=year_ms,
                require_partition_filter=False,
            )
        self.assertEqual(config.time_partitioning, expected)

        assert len(warned) == 1
        warning = warned[0]
        assert "TimePartitioning.require_partition_filter" in str(warning)

    def test_time_partitioning_setter(self):
        from google.cloud.bigquery.table import TimePartitioning
        from google.cloud.bigquery.table import TimePartitioningType

        field = "creation_date"
        year_ms = 86400 * 1000 * 365

        with warnings.catch_warnings(record=True) as warned:
            time_partitioning = TimePartitioning(
                type_=TimePartitioningType.DAY,
                field=field,
                expiration_ms=year_ms,
                require_partition_filter=False,
            )

        config = self._get_target_class()()
        config.time_partitioning = time_partitioning
        expected = {
            "type": TimePartitioningType.DAY,
            "field": field,
            "expirationMs": str(year_ms),
            "requirePartitionFilter": False,
        }
        self.assertEqual(config._properties["load"]["timePartitioning"], expected)

        assert len(warned) == 1
        warning = warned[0]
        assert "TimePartitioning.require_partition_filter" in str(warning)

    def test_time_partitioning_setter_w_none(self):
        from google.cloud.bigquery.table import TimePartitioningType

        field = "creation_date"
        year_ms = 86400 * 1000 * 365
        config = self._get_target_class()()
        config._properties["load"]["timePartitioning"] = {
            "type": TimePartitioningType.DAY,
            "field": field,
            "expirationMs": str(year_ms),
            "requirePartitionFilter": False,
        }
        config.time_partitioning = None
        self.assertIsNone(config.time_partitioning)
        self.assertNotIn("timePartitioning", config._properties["load"])

    def test_use_avro_logical_types(self):
        config = self._get_target_class()()
        self.assertIsNone(config.use_avro_logical_types)

    def test_use_avro_logical_types_setter(self):
        config = self._get_target_class()()
        config.use_avro_logical_types = True
        self.assertTrue(config._properties["load"]["useAvroLogicalTypes"])

    def test_write_disposition_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.write_disposition)

    def test_write_disposition_hit(self):
        from google.cloud.bigquery.job import WriteDisposition

        write_disposition = WriteDisposition.WRITE_TRUNCATE
        config = self._get_target_class()()
        config._properties["load"]["writeDisposition"] = write_disposition
        self.assertEqual(config.write_disposition, write_disposition)

    def test_write_disposition_setter(self):
        from google.cloud.bigquery.job import WriteDisposition

        write_disposition = WriteDisposition.WRITE_TRUNCATE
        config = self._get_target_class()()
        config.write_disposition = write_disposition
        self.assertEqual(
            config._properties["load"]["writeDisposition"], write_disposition
        )

    def test_source_column_match_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.source_column_match)

    def test_source_column_match_hit(self):
        from google.cloud.bigquery.enums import SourceColumnMatch

        option_enum = SourceColumnMatch.NAME
        config = self._get_target_class()()
        # Assume API stores the string value of the enum
        config._properties["load"]["sourceColumnMatch"] = option_enum.value
        self.assertEqual(config.source_column_match, option_enum)

    def test_source_column_match_setter(self):
        from google.cloud.bigquery.enums import SourceColumnMatch

        option_enum = SourceColumnMatch.POSITION
        config = self._get_target_class()()
        config.source_column_match = option_enum
        # Assert that the string value of the enum is stored
        self.assertEqual(
            config._properties["load"]["sourceColumnMatch"], option_enum.value
        )
        option_str = "NAME"
        config.source_column_match = option_str
        self.assertEqual(config._properties["load"]["sourceColumnMatch"], option_str)

    def test_source_column_match_setter_invalid_type(self):
        config = self._get_target_class()()
        with self.assertRaises(TypeError):
            config.source_column_match = 3.14

    def test_date_format_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.date_format)

    def test_date_format_hit(self):
        date_format = "%Y-%m-%d"
        config = self._get_target_class()()
        config._properties["load"]["dateFormat"] = date_format
        self.assertEqual(config.date_format, date_format)

    def test_date_format_setter(self):
        date_format = "YYYY/MM/DD"
        config = self._get_target_class()()
        config.date_format = date_format
        self.assertEqual(config._properties["load"]["dateFormat"], date_format)

    def test_datetime_format_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.datetime_format)

    def test_datetime_format_hit(self):
        datetime_format = "%Y-%m-%dT%H:%M:%S"
        config = self._get_target_class()()
        config._properties["load"]["datetimeFormat"] = datetime_format
        self.assertEqual(config.datetime_format, datetime_format)

    def test_datetime_format_setter(self):
        datetime_format = "YYYY/MM/DD HH24:MI:SS"
        config = self._get_target_class()()
        config.datetime_format = datetime_format
        self.assertEqual(config._properties["load"]["datetimeFormat"], datetime_format)

    def test_time_zone_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.time_zone)

    def test_time_zone_hit(self):
        time_zone = "UTC"
        config = self._get_target_class()()
        config._properties["load"]["timeZone"] = time_zone
        self.assertEqual(config.time_zone, time_zone)

    def test_time_zone_setter(self):
        time_zone = "America/New_York"
        config = self._get_target_class()()
        config.time_zone = time_zone
        self.assertEqual(config._properties["load"]["timeZone"], time_zone)

    def test_time_format_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.time_format)

    def test_time_format_hit(self):
        time_format = "%H:%M:%S"
        config = self._get_target_class()()
        config._properties["load"]["timeFormat"] = time_format
        self.assertEqual(config.time_format, time_format)

    def test_time_format_setter(self):
        time_format = "HH24:MI:SS"
        config = self._get_target_class()()
        config.time_format = time_format
        self.assertEqual(config._properties["load"]["timeFormat"], time_format)

    def test_timestamp_format_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.timestamp_format)

    def test_timestamp_format_hit(self):
        timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        config = self._get_target_class()()
        config._properties["load"]["timestampFormat"] = timestamp_format
        self.assertEqual(config.timestamp_format, timestamp_format)

    def test_timestamp_format_setter(self):
        timestamp_format = "YYYY/MM/DD HH24:MI:SS.FF6 TZR"
        config = self._get_target_class()()
        config.timestamp_format = timestamp_format
        self.assertEqual(
            config._properties["load"]["timestampFormat"], timestamp_format
        )

    def test_parquet_options_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.parquet_options)

    def test_parquet_options_hit(self):
        config = self._get_target_class()()
        config._properties["load"]["parquetOptions"] = dict(
            enumAsString=True, enableListInference=False
        )
        self.assertTrue(config.parquet_options.enum_as_string)
        self.assertFalse(config.parquet_options.enable_list_inference)

    def test_parquet_options_setter(self):
        from google.cloud.bigquery.format_options import ParquetOptions

        parquet_options = ParquetOptions.from_api_repr(
            dict(enumAsString=False, enableListInference=True)
        )
        config = self._get_target_class()()

        config.parquet_options = parquet_options
        self.assertEqual(
            config._properties["load"]["parquetOptions"],
            {"enumAsString": False, "enableListInference": True},
        )

    def test_parquet_options_setter_clearing(self):
        config = self._get_target_class()()
        config._properties["load"]["parquetOptions"] = dict(
            enumAsString=False, enableListInference=True
        )

        config.parquet_options = None
        self.assertNotIn("parquetOptions", config._properties["load"])

    def test_column_name_character_map_missing(self):
        from google.cloud.bigquery.job.load import ColumnNameCharacterMap

        config = self._get_target_class()()
        self.assertEqual(
            config.column_name_character_map,
            ColumnNameCharacterMap.COLUMN_NAME_CHARACTER_MAP_UNSPECIFIED,
        )

    def test_column_name_character_map_hit(self):
        from google.cloud.bigquery.job.load import ColumnNameCharacterMap

        config = self._get_target_class()()
        config._properties["load"]["columnNameCharacterMap"] = "STRICT"
        self.assertEqual(
            config.column_name_character_map,
            ColumnNameCharacterMap.STRICT,
        )

    def test_column_name_character_map_setter(self):
        from google.cloud.bigquery.job.load import ColumnNameCharacterMap

        config = self._get_target_class()()
        config.column_name_character_map = "V1"
        self.assertEqual(
            config._properties["load"]["columnNameCharacterMap"],
            ColumnNameCharacterMap.V1,
        )

    def test_column_name_character_map_none(self):
        from google.cloud.bigquery.job.load import ColumnNameCharacterMap

        config = self._get_target_class()()
        config.column_name_character_map = None
        self.assertEqual(
            config._properties["load"]["columnNameCharacterMap"],
            ColumnNameCharacterMap.COLUMN_NAME_CHARACTER_MAP_UNSPECIFIED,
        )

    RESOURCE = {
        "load": {
            "allowJaggedRows": True,
            "createDisposition": "CREATE_NEVER",
            "encoding": "UTF-8",
            "fieldDelimiter": ",",
            "ignoreUnknownValues": True,
            "maxBadRecords": 10,
            "nullMarker": "\\N",
            "quote": '"',
            "schema": {
                "fields": [
                    {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "age", "type": "INTEGER", "mode": "NULLABLE"},
                ]
            },
            "skipLeadingRows": "1",
            "sourceFormat": "CSV",
            "timePartitioning": {
                "type": "DAY",
                "field": "transaction_date",
            },
            "useAvroLogicalTypes": True,
            "writeDisposition": "WRITE_TRUNCATE",
            "dateFormat": "%Y-%m-%d",
            "timeZone": "America/New_York",
            "parquetOptions": {"enableListInference": True},
            "columnNameCharacterMap": "V2",
            "someNewField": "some-value",
            "timestampTargetPrecision": [6, 12],
        }
    }

    def test_timestamp_target_precision_missing(self):
        config = self._get_target_class()()
        self.assertIsNone(config.timestamp_target_precision)

    def test_timestamp_target_precision_hit(self):
        timestamp_target_precision = [6, 12]
        config = self._get_target_class()()
        config._properties["load"][
            "timestampTargetPrecision"
        ] = timestamp_target_precision
        self.assertEqual(config.timestamp_target_precision, timestamp_target_precision)

    def test_timestamp_target_precision_setter(self):
        timestamp_target_precision = [6, 12]
        config = self._get_target_class()()
        config.timestamp_target_precision = timestamp_target_precision
        self.assertEqual(
            config._properties["load"]["timestampTargetPrecision"],
            timestamp_target_precision,
        )

    def test_timestamp_target_precision_setter_w_none(self):
        timestamp_target_precision = [6, 12]
        config = self._get_target_class()()
        config._properties["load"][
            "timestampTargetPrecision"
        ] = timestamp_target_precision
        config.timestamp_target_precision = None
        self.assertFalse("timestampTargetPrecision" in config._properties["load"])

    def test_from_api_repr(self):
        from google.cloud.bigquery.job import (
            CreateDisposition,
            LoadJobConfig,
            SourceFormat,
            WriteDisposition,
        )
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import TimePartitioning, TimePartitioningType

        from google.cloud.bigquery.job.load import ColumnNameCharacterMap

        config = LoadJobConfig.from_api_repr(self.RESOURCE)

        self.assertTrue(config.allow_jagged_rows)
        self.assertEqual(config.create_disposition, CreateDisposition.CREATE_NEVER)
        self.assertEqual(config.encoding, "UTF-8")
        self.assertEqual(config.field_delimiter, ",")
        self.assertTrue(config.ignore_unknown_values)
        self.assertEqual(config.max_bad_records, 10)
        self.assertEqual(config.null_marker, "\\N")
        self.assertEqual(config.quote_character, '"')
        self.assertEqual(
            config.schema,
            [SchemaField("name", "STRING"), SchemaField("age", "INTEGER")],
        )
        self.assertEqual(config.skip_leading_rows, 1)
        self.assertEqual(config.source_format, SourceFormat.CSV)
        self.assertEqual(
            config.time_partitioning,
            TimePartitioning(type_=TimePartitioningType.DAY, field="transaction_date"),
        )
        self.assertTrue(config.use_avro_logical_types)
        self.assertEqual(config.write_disposition, WriteDisposition.WRITE_TRUNCATE)
        self.assertEqual(config.date_format, "%Y-%m-%d")
        self.assertEqual(config.time_zone, "America/New_York")
        self.assertTrue(config.parquet_options.enable_list_inference)
        self.assertEqual(config.column_name_character_map, ColumnNameCharacterMap.V2)
        self.assertEqual(config._properties["load"]["someNewField"], "some-value")
        self.assertEqual(config.timestamp_target_precision, [6, 12])

    def test_to_api_repr(self):
        from google.cloud.bigquery.job import (
            CreateDisposition,
            LoadJobConfig,
            SourceFormat,
            WriteDisposition,
        )
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import TimePartitioning, TimePartitioningType
        from google.cloud.bigquery.format_options import ParquetOptions
        from google.cloud.bigquery.job.load import ColumnNameCharacterMap

        config = LoadJobConfig()
        config.allow_jagged_rows = True
        config.create_disposition = CreateDisposition.CREATE_NEVER
        config.encoding = "UTF-8"
        config.field_delimiter = ","
        config.ignore_unknown_values = True
        config.max_bad_records = 10
        config.null_marker = r"\N"
        config.quote_character = '"'
        config.schema = [SchemaField("name", "STRING"), SchemaField("age", "INTEGER")]
        config.skip_leading_rows = 1
        config.source_format = SourceFormat.CSV
        config.time_partitioning = TimePartitioning(
            type_=TimePartitioningType.DAY, field="transaction_date"
        )
        config.use_avro_logical_types = True
        config.write_disposition = WriteDisposition.WRITE_TRUNCATE
        config.date_format = "%Y-%m-%d"
        config.time_zone = "America/New_York"
        parquet_options = ParquetOptions()
        parquet_options.enable_list_inference = True
        config.parquet_options = parquet_options
        config.column_name_character_map = ColumnNameCharacterMap.V2
        config._properties["load"]["someNewField"] = "some-value"
        config.timestamp_target_precision = [6, 12]

        api_repr = config.to_api_repr()

        expected = self.RESOURCE
        self.assertEqual(api_repr, expected)
