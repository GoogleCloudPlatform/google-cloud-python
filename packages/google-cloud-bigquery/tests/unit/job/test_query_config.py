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

import pytest

from .helpers import _Base


class TestQueryJobConfig(_Base):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import QueryJobConfig

        return QueryJobConfig

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        config = self._make_one()
        self.assertEqual(config._properties, {"query": {}})

    def test_ctor_w_none(self):
        config = self._make_one()
        config.default_dataset = None
        config.destination = None
        self.assertIsNone(config.default_dataset)
        self.assertIsNone(config.destination)

    def test_ctor_w_properties(self):
        config = self._get_target_class()(use_query_cache=False, use_legacy_sql=True)

        self.assertFalse(config.use_query_cache)
        self.assertTrue(config.use_legacy_sql)

    def test_ctor_w_string_default_dataset(self):
        from google.cloud.bigquery import dataset

        default_dataset = "default-proj.default_dset"
        config = self._get_target_class()(default_dataset=default_dataset)
        expected = dataset.DatasetReference.from_string(default_dataset)
        self.assertEqual(config.default_dataset, expected)

    def test_ctor_w_string_destinaton(self):
        from google.cloud.bigquery import table

        destination = "dest-proj.dest_dset.dest_tbl"
        config = self._get_target_class()(destination=destination)
        expected = table.TableReference.from_string(destination)
        self.assertEqual(config.destination, expected)

    def test_default_dataset_w_string(self):
        from google.cloud.bigquery import dataset

        default_dataset = "default-proj.default_dset"
        config = self._make_one()
        config.default_dataset = default_dataset
        expected = dataset.DatasetReference.from_string(default_dataset)
        self.assertEqual(config.default_dataset, expected)

    def test_default_dataset_w_dataset(self):
        from google.cloud.bigquery import dataset

        default_dataset = "default-proj.default_dset"
        expected = dataset.DatasetReference.from_string(default_dataset)
        config = self._make_one()
        config.default_dataset = dataset.Dataset(expected)
        self.assertEqual(config.default_dataset, expected)

    def test_destinaton_w_string(self):
        from google.cloud.bigquery import table

        destination = "dest-proj.dest_dset.dest_tbl"
        config = self._make_one()
        config.destination = destination
        expected = table.TableReference.from_string(destination)
        self.assertEqual(config.destination, expected)

    def test_range_partitioning_w_none(self):
        object_under_test = self._get_target_class()()
        assert object_under_test.range_partitioning is None

    def test_range_partitioning_w_value(self):
        object_under_test = self._get_target_class()()
        object_under_test._properties["query"]["rangePartitioning"] = {
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

    def test_time_partitioning(self):
        from google.cloud.bigquery import table

        time_partitioning = table.TimePartitioning(
            type_=table.TimePartitioningType.DAY, field="name"
        )
        config = self._make_one()
        config.time_partitioning = time_partitioning
        # TimePartitioning should be configurable after assigning
        time_partitioning.expiration_ms = 10000

        self.assertEqual(config.time_partitioning.type_, table.TimePartitioningType.DAY)
        self.assertEqual(config.time_partitioning.field, "name")
        self.assertEqual(config.time_partitioning.expiration_ms, 10000)

        config.time_partitioning = None
        self.assertIsNone(config.time_partitioning)

    def test_clustering_fields(self):
        fields = ["email", "postal_code"]
        config = self._get_target_class()()
        config.clustering_fields = fields
        self.assertEqual(config.clustering_fields, fields)

        config.clustering_fields = None
        self.assertIsNone(config.clustering_fields)

    def test_connection_properties(self):
        from google.cloud.bigquery.job.query import ConnectionProperty

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

    def test_incremental_results(self):
        config = self._get_target_class()()
        config.write_incremental_results = True
        self.assertEqual(config.write_incremental_results, True)

    def test_max_slots(self):
        config = self._get_target_class()()
        config.max_slots = 99
        self.assertEqual(config.max_slots, 99)

    def test_create_session(self):
        config = self._get_target_class()()
        self.assertIsNone(config.create_session)
        config.create_session = True
        self.assertTrue(config.create_session)

    def test_from_api_repr_empty(self):
        klass = self._get_target_class()
        config = klass.from_api_repr({})
        self.assertIsNone(config.dry_run)
        self.assertIsNone(config.use_legacy_sql)
        self.assertIsNone(config.default_dataset)
        self.assertIsNone(config.destination)
        self.assertIsNone(config.destination_encryption_configuration)

    def test_from_api_repr_normal(self):
        from google.cloud.bigquery.dataset import DatasetReference

        resource = {
            "query": {
                "useLegacySql": True,
                "query": "no property for me",
                "defaultDataset": {
                    "projectId": "someproject",
                    "datasetId": "somedataset",
                },
                "someNewProperty": "I should be saved, too.",
            },
            "dryRun": True,
        }
        klass = self._get_target_class()

        config = klass.from_api_repr(resource)

        self.assertTrue(config.use_legacy_sql)
        self.assertEqual(
            config.default_dataset, DatasetReference("someproject", "somedataset")
        )
        self.assertTrue(config.dry_run)
        # Make sure unknown properties propagate.
        self.assertEqual(config._properties["query"]["query"], "no property for me")
        self.assertEqual(
            config._properties["query"]["someNewProperty"], "I should be saved, too."
        )

    def test_to_api_repr_normal(self):
        from google.cloud.bigquery.dataset import DatasetReference

        config = self._make_one()
        config.use_legacy_sql = True
        config.default_dataset = DatasetReference("someproject", "somedataset")
        config.dry_run = False
        config._properties["someNewProperty"] = "Woohoo, alpha stuff."

        resource = config.to_api_repr()

        self.assertFalse(resource["dryRun"])
        self.assertTrue(resource["query"]["useLegacySql"])
        self.assertEqual(
            resource["query"]["defaultDataset"]["projectId"], "someproject"
        )
        self.assertEqual(
            resource["query"]["defaultDataset"]["datasetId"], "somedataset"
        )
        # Make sure unknown properties propagate.
        self.assertEqual(resource["someNewProperty"], "Woohoo, alpha stuff.")

    def test_to_api_repr_with_encryption(self):
        from google.cloud.bigquery.encryption_configuration import (
            EncryptionConfiguration,
        )

        config = self._make_one()
        config.destination_encryption_configuration = EncryptionConfiguration(
            kms_key_name=self.KMS_KEY_NAME
        )
        resource = config.to_api_repr()
        self.assertEqual(
            resource,
            {
                "query": {
                    "destinationEncryptionConfiguration": {
                        "kmsKeyName": self.KMS_KEY_NAME
                    }
                }
            },
        )

    def test_to_api_repr_with_encryption_none(self):
        config = self._make_one()
        config.destination_encryption_configuration = None
        resource = config.to_api_repr()
        self.assertEqual(
            resource, {"query": {"destinationEncryptionConfiguration": None}}
        )

    def test_from_api_repr_with_encryption(self):
        resource = {
            "query": {
                "destinationEncryptionConfiguration": {"kmsKeyName": self.KMS_KEY_NAME}
            }
        }
        klass = self._get_target_class()
        config = klass.from_api_repr(resource)
        self.assertEqual(
            config.destination_encryption_configuration.kms_key_name, self.KMS_KEY_NAME
        )

    def test_to_api_repr_with_script_options_none(self):
        config = self._make_one()
        config.script_options = None

        resource = config.to_api_repr()

        self.assertEqual(resource, {"query": {"scriptOptions": None}})
        self.assertIsNone(config.script_options)

    def test_to_api_repr_with_script_options(self):
        from google.cloud.bigquery import KeyResultStatementKind
        from google.cloud.bigquery import ScriptOptions

        config = self._make_one()
        config.script_options = ScriptOptions(
            statement_timeout_ms=60,
            statement_byte_budget=999,
            key_result_statement=KeyResultStatementKind.FIRST_SELECT,
        )

        resource = config.to_api_repr()

        expected_script_options_repr = {
            "statementTimeoutMs": "60",
            "statementByteBudget": "999",
            "keyResultStatement": KeyResultStatementKind.FIRST_SELECT,
        }
        self.assertEqual(
            resource, {"query": {"scriptOptions": expected_script_options_repr}}
        )

    def test_from_api_repr_with_script_options(self):
        from google.cloud.bigquery import KeyResultStatementKind
        from google.cloud.bigquery import ScriptOptions

        resource = {
            "query": {
                "scriptOptions": {
                    "statementTimeoutMs": "42",
                    "statementByteBudget": "123",
                    "keyResultStatement": KeyResultStatementKind.LAST,
                },
            },
        }
        klass = self._get_target_class()

        config = klass.from_api_repr(resource)

        script_options = config.script_options
        self.assertIsInstance(script_options, ScriptOptions)
        self.assertEqual(script_options.statement_timeout_ms, 42)
        self.assertEqual(script_options.statement_byte_budget, 123)
        self.assertEqual(
            script_options.key_result_statement, KeyResultStatementKind.LAST
        )
