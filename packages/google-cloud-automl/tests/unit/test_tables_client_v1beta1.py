# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pandas
import pytest
from google.api_core import exceptions
from google.auth.credentials import AnonymousCredentials
from google.protobuf import struct_pb2 as struct

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.types import data_items, data_types

PROJECT = "project"
REGION = "region"
LOCATION_PATH = "projects/{}/locations/{}".format(PROJECT, REGION)


class TestTablesClient(object):
    def tables_client(
        self, client_attrs={}, prediction_client_attrs={}, gcs_client_attrs={}
    ):
        client_mock = mock.Mock(**client_attrs)
        prediction_client_mock = mock.Mock(**prediction_client_attrs)
        gcs_client_mock = mock.Mock(**gcs_client_attrs)
        return automl_v1beta1.TablesClient(
            client=client_mock,
            prediction_client=prediction_client_mock,
            gcs_client=gcs_client_mock,
            project=PROJECT,
            region=REGION,
        )

    def test_list_datasets_empty(self):
        client = self.tables_client(
            client_attrs={
                "list_datasets.return_value": [],
                "location_path.return_value": LOCATION_PATH,
            },
            prediction_client_attrs={},
        )
        ds = client.list_datasets()

        request = automl_v1beta1.ListDatasetsRequest(parent=LOCATION_PATH)
        client.auto_ml_client.list_datasets.assert_called_with(request=request)
        assert ds == []

    def test_list_datasets_not_empty(self):
        datasets = ["some_dataset"]
        client = self.tables_client(
            client_attrs={
                "list_datasets.return_value": datasets,
                "location_path.return_value": LOCATION_PATH,
            },
            prediction_client_attrs={},
        )
        ds = client.list_datasets()

        request = automl_v1beta1.ListDatasetsRequest(parent=LOCATION_PATH)
        client.auto_ml_client.list_datasets.assert_called_with(request=request)
        assert len(ds) == 1
        assert ds[0] == "some_dataset"

    def test_get_dataset_no_value(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.get_dataset()
        client.auto_ml_client.get_dataset.assert_not_called()

    def test_get_dataset_name(self):
        dataset_actual = "dataset"
        client = self.tables_client({"get_dataset.return_value": dataset_actual}, {})
        dataset = client.get_dataset(dataset_name="my_dataset")
        client.auto_ml_client.get_dataset.assert_called_with(
            request=automl_v1beta1.GetDatasetRequest(name="my_dataset")
        )
        assert dataset == dataset_actual

    def test_get_no_dataset(self):
        client = self.tables_client(
            {"get_dataset.side_effect": exceptions.NotFound("err")}, {}
        )
        with pytest.raises(exceptions.NotFound):
            client.get_dataset(dataset_name="my_dataset")
        client.auto_ml_client.get_dataset.assert_called_with(
            request=automl_v1beta1.GetDatasetRequest(name="my_dataset")
        )

    def test_get_dataset_from_empty_list(self):
        client = self.tables_client({"list_datasets.return_value": []}, {})
        with pytest.raises(exceptions.NotFound):
            client.get_dataset(dataset_display_name="my_dataset")

    def test_get_dataset_from_list_not_found(self):
        client = self.tables_client(
            {"list_datasets.return_value": [mock.Mock(display_name="not_it")]}, {}
        )
        with pytest.raises(exceptions.NotFound):
            client.get_dataset(dataset_display_name="my_dataset")

    def test_get_dataset_from_list(self):
        client = self.tables_client(
            {
                "list_datasets.return_value": [
                    mock.Mock(display_name="not_it"),
                    mock.Mock(display_name="my_dataset"),
                ]
            },
            {},
        )
        dataset = client.get_dataset(dataset_display_name="my_dataset")
        assert dataset.display_name == "my_dataset"

    def test_get_dataset_from_list_ambiguous(self):
        client = self.tables_client(
            {
                "list_datasets.return_value": [
                    mock.Mock(display_name="my_dataset"),
                    mock.Mock(display_name="not_my_dataset"),
                    mock.Mock(display_name="my_dataset"),
                ]
            },
            {},
        )
        with pytest.raises(ValueError):
            client.get_dataset(dataset_display_name="my_dataset")

    def test_create_dataset(self):
        client = self.tables_client(
            {
                "location_path.return_value": LOCATION_PATH,
                "create_dataset.return_value": mock.Mock(display_name="name"),
            },
            {},
        )
        metadata = {"primary_table_spec_id": "1234"}
        dataset = client.create_dataset("name", metadata=metadata)

        client.auto_ml_client.create_dataset.assert_called_with(
            request=automl_v1beta1.CreateDatasetRequest(
                parent=LOCATION_PATH,
                dataset={"display_name": "name", "tables_dataset_metadata": metadata},
            )
        )
        assert dataset.display_name == "name"

    def test_delete_dataset(self):
        dataset = mock.Mock()
        dataset.configure_mock(name="name")
        client = self.tables_client({"delete_dataset.return_value": None}, {})
        client.delete_dataset(dataset=dataset)
        client.auto_ml_client.delete_dataset.assert_called_with(
            request=automl_v1beta1.DeleteDatasetRequest(name="name")
        )

    def test_delete_dataset_not_found(self):
        client = self.tables_client({"list_datasets.return_value": []}, {})
        client.delete_dataset(dataset_display_name="not_found")
        client.auto_ml_client.delete_dataset.assert_not_called()

    def test_delete_dataset_name(self):
        client = self.tables_client({"delete_dataset.return_value": None}, {})
        client.delete_dataset(dataset_name="name")
        client.auto_ml_client.delete_dataset.assert_called_with(
            request=automl_v1beta1.DeleteDatasetRequest(name="name")
        )

    def test_export_not_found(self):
        client = self.tables_client({"list_datasets.return_value": []}, {})
        with pytest.raises(exceptions.NotFound):
            client.export_data(dataset_display_name="name", gcs_input_uris="uri")

        client.auto_ml_client.export_data.assert_not_called()

    def test_export_gcs_uri(self):
        client = self.tables_client({"export_data.return_value": None}, {})
        client.export_data(dataset_name="name", gcs_output_uri_prefix="uri")
        client.auto_ml_client.export_data.assert_called_with(
            request=automl_v1beta1.ExportDataRequest(
                name="name",
                output_config={"gcs_destination": {"output_uri_prefix": "uri"}},
            )
        )

    def test_export_bq_uri(self):
        client = self.tables_client({"export_data.return_value": None}, {})
        client.export_data(dataset_name="name", bigquery_output_uri="uri")
        client.auto_ml_client.export_data.assert_called_with(
            request=automl_v1beta1.ExportDataRequest(
                name="name",
                output_config={"bigquery_destination": {"output_uri": "uri"}},
            )
        )

    def test_import_not_found(self):
        client = self.tables_client({"list_datasets.return_value": []}, {})
        with pytest.raises(exceptions.NotFound):
            client.import_data(dataset_display_name="name", gcs_input_uris="uri")

        client.auto_ml_client.import_data.assert_not_called()

    def test_import_pandas_dataframe(self):
        client = self.tables_client(
            gcs_client_attrs={
                "bucket_name": "my_bucket",
                "upload_pandas_dataframe.return_value": "uri",
            }
        )
        dataframe = pandas.DataFrame({})
        client.import_data(
            project=PROJECT,
            region=REGION,
            dataset_name="name",
            pandas_dataframe=dataframe,
        )
        client.gcs_client.ensure_bucket_exists.assert_called_with(PROJECT, REGION)
        client.gcs_client.upload_pandas_dataframe.assert_called_with(dataframe)
        client.auto_ml_client.import_data.assert_called_with(
            request=automl_v1beta1.ImportDataRequest(
                name="name", input_config={"gcs_source": {"input_uris": ["uri"]}}
            )
        )

    def test_import_pandas_dataframe_init_gcs(self):
        client = automl_v1beta1.TablesClient(
            client=mock.Mock(),
            prediction_client=mock.Mock(),
            project=PROJECT,
            region=REGION,
            credentials=AnonymousCredentials(),
        )

        dataframe = pandas.DataFrame({})
        patch = mock.patch(
            "google.cloud.automl_v1beta1.services.tables.tables_client.gcs_client.GcsClient",
            bucket_name="my_bucket",
        )
        with patch as MockGcsClient:
            mockInstance = MockGcsClient.return_value
            mockInstance.upload_pandas_dataframe.return_value = "uri"

            client.import_data(dataset_name="name", pandas_dataframe=dataframe)

            assert client.gcs_client is mockInstance
            client.gcs_client.ensure_bucket_exists.assert_called_with(PROJECT, REGION)
            client.gcs_client.upload_pandas_dataframe.assert_called_with(dataframe)
            client.auto_ml_client.import_data.assert_called_with(
                request=automl_v1beta1.ImportDataRequest(
                    name="name", input_config={"gcs_source": {"input_uris": ["uri"]}}
                )
            )

    def test_import_gcs_uri(self):
        client = self.tables_client({"import_data.return_value": None}, {})
        client.import_data(dataset_name="name", gcs_input_uris="uri")
        client.auto_ml_client.import_data.assert_called_with(
            request=automl_v1beta1.ImportDataRequest(
                name="name", input_config={"gcs_source": {"input_uris": ["uri"]}}
            )
        )

    def test_import_gcs_uris(self):
        client = self.tables_client({"import_data.return_value": None}, {})
        client.import_data(dataset_name="name", gcs_input_uris=["uri", "uri"])
        client.auto_ml_client.import_data.assert_called_with(
            request=automl_v1beta1.ImportDataRequest(
                name="name", input_config={"gcs_source": {"input_uris": ["uri", "uri"]}}
            )
        )

    def test_import_bq_uri(self):
        client = self.tables_client({"import_data.return_value": None}, {})
        client.import_data(dataset_name="name", bigquery_input_uri="uri")
        client.auto_ml_client.import_data.assert_called_with(
            request=automl_v1beta1.ImportDataRequest(
                name="name", input_config={"bigquery_source": {"input_uri": "uri"}}
            )
        )

    def test_list_table_specs(self):
        client = self.tables_client({"list_table_specs.return_value": None}, {})
        client.list_table_specs(dataset_name="name")
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )

    def test_list_table_specs_not_found(self):
        client = self.tables_client(
            {"list_table_specs.side_effect": exceptions.NotFound("not found")}, {}
        )
        with pytest.raises(exceptions.NotFound):
            client.list_table_specs(dataset_name="name")
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )

    def test_get_table_spec(self):
        client = self.tables_client({}, {})
        client.get_table_spec("name")
        client.auto_ml_client.get_table_spec.assert_called_with(
            request=automl_v1beta1.GetTableSpecRequest(name="name")
        )

    def test_get_column_spec(self):
        client = self.tables_client({}, {})
        client.get_column_spec("name")
        client.auto_ml_client.get_column_spec.assert_called_with(
            request=automl_v1beta1.GetColumnSpecRequest(name="name")
        )

    def test_list_column_specs(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [],
            },
            {},
        )
        client.list_column_specs(dataset_name="name")
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )

    def test_update_column_spec_not_found(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")

        column_spec = automl_v1beta1.ColumnSpec(
            name="column",
            display_name="column",
            data_type=automl_v1beta1.DataType(type_code=automl_v1beta1.TypeCode.STRING),
        )

        client = self.tables_client(
            client_attrs={
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec],
            },
            prediction_client_attrs={},
        )
        with pytest.raises(exceptions.NotFound):
            client.update_column_spec(dataset_name="name", column_spec_name="column2")
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_column_spec.assert_not_called()

    def test_update_column_spec_display_name_not_found(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")

        column_spec = automl_v1beta1.ColumnSpec(
            name="column",
            display_name="column",
            data_type=automl_v1beta1.DataType(type_code=automl_v1beta1.TypeCode.STRING),
        )
        client = self.tables_client(
            client_attrs={
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec],
            },
            prediction_client_attrs={},
        )
        with pytest.raises(exceptions.NotFound):
            client.update_column_spec(
                dataset_name="name", column_spec_display_name="column2"
            )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_column_spec.assert_not_called()

    def test_update_column_spec_name_no_args(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")

        column_spec = automl_v1beta1.ColumnSpec(
            name="column/2",
            display_name="column",
            data_type=automl_v1beta1.DataType(
                type_code=automl_v1beta1.TypeCode.FLOAT64
            ),
        )

        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec],
            },
            {},
        )
        client.update_column_spec(dataset_name="name", column_spec_name="column/2")
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_column_spec.assert_called_with(
            request=automl_v1beta1.UpdateColumnSpecRequest(
                column_spec={
                    "name": "column/2",
                    "data_type": {"type_code": automl_v1beta1.TypeCode.FLOAT64},
                }
            )
        )

    def test_update_column_spec_no_args(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")

        column_spec = automl_v1beta1.ColumnSpec(
            name="column",
            display_name="column",
            data_type=automl_v1beta1.DataType(
                type_code=automl_v1beta1.TypeCode.FLOAT64
            ),
        )

        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec],
            },
            {},
        )
        client.update_column_spec(
            dataset_name="name", column_spec_display_name="column"
        )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_column_spec.assert_called_with(
            request=automl_v1beta1.UpdateColumnSpecRequest(
                column_spec={
                    "name": "column",
                    "data_type": {"type_code": automl_v1beta1.TypeCode.FLOAT64},
                }
            )
        )

    def test_update_column_spec_nullable(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")

        column_spec = automl_v1beta1.ColumnSpec(
            name="column",
            display_name="column",
            data_type=automl_v1beta1.DataType(
                type_code=automl_v1beta1.TypeCode.FLOAT64
            ),
        )

        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec],
            },
            {},
        )
        client.update_column_spec(
            dataset_name="name", column_spec_display_name="column", nullable=True
        )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_column_spec.assert_called_with(
            request=automl_v1beta1.UpdateColumnSpecRequest(
                column_spec={
                    "name": "column",
                    "data_type": {
                        "type_code": automl_v1beta1.TypeCode.FLOAT64,
                        "nullable": True,
                    },
                }
            )
        )

    def test_update_column_spec_type_code(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec = automl_v1beta1.ColumnSpec(
            name="column",
            display_name="column",
            data_type=automl_v1beta1.DataType(
                type_code=automl_v1beta1.TypeCode.FLOAT64
            ),
        )
        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec],
            },
            {},
        )
        client.update_column_spec(
            dataset_name="name",
            column_spec_display_name="column",
            type_code=automl_v1beta1.TypeCode.ARRAY,
        )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_column_spec.assert_called_with(
            request=automl_v1beta1.UpdateColumnSpecRequest(
                column_spec={
                    "name": "column",
                    "data_type": {"type_code": automl_v1beta1.TypeCode.ARRAY},
                }
            )
        )

    def test_update_column_spec_type_code_nullable(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec = automl_v1beta1.ColumnSpec(
            name="column",
            display_name="column",
            data_type=automl_v1beta1.DataType(
                type_code=automl_v1beta1.TypeCode.FLOAT64
            ),
        )
        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec],
            },
            {},
        )
        client.update_column_spec(
            dataset_name="name",
            nullable=True,
            column_spec_display_name="column",
            type_code=automl_v1beta1.TypeCode.ARRAY,
        )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_column_spec.assert_called_with(
            request=automl_v1beta1.UpdateColumnSpecRequest(
                column_spec={
                    "name": "column",
                    "data_type": {
                        "type_code": automl_v1beta1.TypeCode.ARRAY,
                        "nullable": True,
                    },
                }
            )
        )

    def test_update_column_spec_type_code_nullable_false(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec = automl_v1beta1.ColumnSpec(
            name="column",
            display_name="column",
            data_type=automl_v1beta1.DataType(
                type_code=automl_v1beta1.TypeCode.FLOAT64
            ),
        )
        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec],
            },
            {},
        )
        client.update_column_spec(
            dataset_name="name",
            nullable=False,
            column_spec_display_name="column",
            type_code=automl_v1beta1.TypeCode.FLOAT64,
        )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_column_spec.assert_called_with(
            request=automl_v1beta1.UpdateColumnSpecRequest(
                column_spec={
                    "name": "column",
                    "data_type": {
                        "type_code": automl_v1beta1.TypeCode.FLOAT64,
                        "nullable": False,
                    },
                }
            )
        )

    def test_set_target_column_table_not_found(self):
        client = self.tables_client(
            {"list_table_specs.side_effect": exceptions.NotFound("err")}, {}
        )
        with pytest.raises(exceptions.NotFound):
            client.set_target_column(
                dataset_name="name", column_spec_display_name="column2"
            )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_not_called()
        client.auto_ml_client.update_dataset.assert_not_called()

    def test_set_target_column_not_found(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec_mock = mock.Mock()
        column_spec_mock.configure_mock(name="column/1", display_name="column")
        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_mock],
            },
            {},
        )
        with pytest.raises(exceptions.NotFound):
            client.set_target_column(
                dataset_name="name", column_spec_display_name="column2"
            )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_dataset.assert_not_called()

    def test_set_target_column(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec_mock = mock.Mock()
        column_spec_mock.configure_mock(name="column/1", display_name="column")
        dataset_mock = mock.Mock()
        tables_dataset_metadata_mock = mock.Mock()
        tables_dataset_metadata_mock.configure_mock(
            target_column_spec_id="2",
            weight_column_spec_id="2",
            ml_use_column_spec_id="3",
        )
        dataset_mock.configure_mock(
            name="dataset", tables_dataset_metadata=tables_dataset_metadata_mock
        )
        client = self.tables_client(
            {
                "get_dataset.return_value": dataset_mock,
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_mock],
            },
            {},
        )
        client.set_target_column(dataset_name="name", column_spec_display_name="column")
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_dataset.assert_called_with(
            request=automl_v1beta1.UpdateDatasetRequest(
                dataset={
                    "name": "dataset",
                    "tables_dataset_metadata": {
                        "target_column_spec_id": "1",
                        "weight_column_spec_id": "2",
                        "ml_use_column_spec_id": "3",
                    },
                }
            )
        )

    def test_set_weight_column_table_not_found(self):
        client = self.tables_client(
            {"list_table_specs.side_effect": exceptions.NotFound("err")}, {}
        )
        try:
            client.set_weight_column(
                dataset_name="name", column_spec_display_name="column2"
            )
        except exceptions.NotFound:
            pass
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_not_called()
        client.auto_ml_client.update_dataset.assert_not_called()

    def test_set_weight_column_not_found(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec_mock = mock.Mock()
        column_spec_mock.configure_mock(name="column/1", display_name="column")
        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_mock],
            },
            {},
        )
        with pytest.raises(exceptions.NotFound):
            client.set_weight_column(
                dataset_name="name", column_spec_display_name="column2"
            )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_dataset.assert_not_called()

    def test_set_weight_column(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec_mock = mock.Mock()
        column_spec_mock.configure_mock(name="column/2", display_name="column")
        dataset_mock = mock.Mock()
        tables_dataset_metadata_mock = mock.Mock()
        tables_dataset_metadata_mock.configure_mock(
            target_column_spec_id="1",
            weight_column_spec_id="1",
            ml_use_column_spec_id="3",
        )
        dataset_mock.configure_mock(
            name="dataset", tables_dataset_metadata=tables_dataset_metadata_mock
        )
        client = self.tables_client(
            {
                "get_dataset.return_value": dataset_mock,
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_mock],
            },
            {},
        )
        client.set_weight_column(dataset_name="name", column_spec_display_name="column")
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_dataset.assert_called_with(
            request=automl_v1beta1.UpdateDatasetRequest(
                dataset={
                    "name": "dataset",
                    "tables_dataset_metadata": {
                        "target_column_spec_id": "1",
                        "weight_column_spec_id": "2",
                        "ml_use_column_spec_id": "3",
                    },
                }
            )
        )

    def test_clear_weight_column(self):
        dataset_mock = mock.Mock()
        tables_dataset_metadata_mock = mock.Mock()
        tables_dataset_metadata_mock.configure_mock(
            target_column_spec_id="1",
            weight_column_spec_id="2",
            ml_use_column_spec_id="3",
        )
        dataset_mock.configure_mock(
            name="dataset", tables_dataset_metadata=tables_dataset_metadata_mock
        )
        client = self.tables_client({"get_dataset.return_value": dataset_mock}, {})
        client.clear_weight_column(dataset_name="name")
        client.auto_ml_client.update_dataset.assert_called_with(
            request=automl_v1beta1.UpdateDatasetRequest(
                dataset={
                    "name": "dataset",
                    "tables_dataset_metadata": {
                        "target_column_spec_id": "1",
                        "weight_column_spec_id": None,
                        "ml_use_column_spec_id": "3",
                    },
                }
            )
        )

    def test_set_test_train_column_table_not_found(self):
        client = self.tables_client(
            {"list_table_specs.side_effect": exceptions.NotFound("err")}, {}
        )
        with pytest.raises(exceptions.NotFound):
            client.set_test_train_column(
                dataset_name="name", column_spec_display_name="column2"
            )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_not_called()
        client.auto_ml_client.update_dataset.assert_not_called()

    def test_set_test_train_column_not_found(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec_mock = mock.Mock()
        column_spec_mock.configure_mock(name="column/1", display_name="column")
        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_mock],
            },
            {},
        )
        with pytest.raises(exceptions.NotFound):
            client.set_test_train_column(
                dataset_name="name", column_spec_display_name="column2"
            )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_dataset.assert_not_called()

    def test_set_test_train_column(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec_mock = mock.Mock()
        column_spec_mock.configure_mock(name="column/3", display_name="column")
        dataset_mock = mock.Mock()
        tables_dataset_metadata_mock = mock.Mock()
        tables_dataset_metadata_mock.configure_mock(
            target_column_spec_id="1",
            weight_column_spec_id="2",
            ml_use_column_spec_id="2",
        )
        dataset_mock.configure_mock(
            name="dataset", tables_dataset_metadata=tables_dataset_metadata_mock
        )
        client = self.tables_client(
            {
                "get_dataset.return_value": dataset_mock,
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_mock],
            },
            {},
        )
        client.set_test_train_column(
            dataset_name="name", column_spec_display_name="column"
        )
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_dataset.assert_called_with(
            request=automl_v1beta1.UpdateDatasetRequest(
                dataset={
                    "name": "dataset",
                    "tables_dataset_metadata": {
                        "target_column_spec_id": "1",
                        "weight_column_spec_id": "2",
                        "ml_use_column_spec_id": "3",
                    },
                }
            )
        )

    def test_clear_test_train_column(self):
        dataset_mock = mock.Mock()
        tables_dataset_metadata_mock = mock.Mock()
        tables_dataset_metadata_mock.configure_mock(
            target_column_spec_id="1",
            weight_column_spec_id="2",
            ml_use_column_spec_id="2",
        )
        dataset_mock.configure_mock(
            name="dataset", tables_dataset_metadata=tables_dataset_metadata_mock
        )
        client = self.tables_client({"get_dataset.return_value": dataset_mock}, {})
        client.clear_test_train_column(dataset_name="name")
        client.auto_ml_client.update_dataset.assert_called_with(
            request=automl_v1beta1.UpdateDatasetRequest(
                dataset={
                    "name": "dataset",
                    "tables_dataset_metadata": {
                        "target_column_spec_id": "1",
                        "weight_column_spec_id": "2",
                        "ml_use_column_spec_id": None,
                    },
                }
            )
        )

    def test_set_time_column(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec_mock = mock.Mock()
        column_spec_mock.configure_mock(name="column/3", display_name="column")
        dataset_mock = mock.Mock()
        dataset_mock.configure_mock(name="dataset")
        client = self.tables_client(
            {
                "get_dataset.return_value": dataset_mock,
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_mock],
            },
            {},
        )
        client.set_time_column(dataset_name="name", column_spec_display_name="column")
        client.auto_ml_client.list_table_specs.assert_called_with(
            request=automl_v1beta1.ListTableSpecsRequest(parent="name")
        )
        client.auto_ml_client.list_column_specs.assert_called_with(
            request=automl_v1beta1.ListColumnSpecsRequest(parent="table")
        )
        client.auto_ml_client.update_table_spec.assert_called_with(
            request=automl_v1beta1.UpdateTableSpecRequest(
                table_spec={"name": "table", "time_column_spec_id": "3"}
            )
        )

    def test_clear_time_column(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        dataset_mock = mock.Mock()
        dataset_mock.configure_mock(name="dataset")
        client = self.tables_client(
            {
                "get_dataset.return_value": dataset_mock,
                "list_table_specs.return_value": [table_spec_mock],
            },
            {},
        )
        client.clear_time_column(dataset_name="name")
        client.auto_ml_client.update_table_spec.assert_called_with(
            request=automl_v1beta1.UpdateTableSpecRequest(
                table_spec={"name": "table", "time_column_spec_id": None}
            )
        )

    def test_get_model_evaluation(self):
        client = self.tables_client({}, {})
        client.get_model_evaluation(model_evaluation_name="x")
        client.auto_ml_client.get_model_evaluation.assert_called_with(
            request=automl_v1beta1.GetModelEvaluationRequest(name="x")
        )

    def test_list_model_evaluations_empty(self):
        client = self.tables_client({"list_model_evaluations.return_value": []}, {})
        ds = client.list_model_evaluations(model_name="model")
        client.auto_ml_client.list_model_evaluations.assert_called_with(
            request=automl_v1beta1.ListModelEvaluationsRequest(parent="model")
        )
        assert ds == []

    def test_list_model_evaluations_not_empty(self):
        evaluations = ["eval"]
        client = self.tables_client(
            {
                "list_model_evaluations.return_value": evaluations,
                "location_path.return_value": LOCATION_PATH,
            },
            {},
        )
        ds = client.list_model_evaluations(model_name="model")
        client.auto_ml_client.list_model_evaluations.assert_called_with(
            request=automl_v1beta1.ListModelEvaluationsRequest(parent="model")
        )
        assert len(ds) == 1
        assert ds[0] == "eval"

    def test_list_models_empty(self):
        client = self.tables_client(
            {
                "list_models.return_value": [],
                "location_path.return_value": LOCATION_PATH,
            },
            {},
        )
        ds = client.list_models()

        client.auto_ml_client.list_models.assert_called_with(
            request=automl_v1beta1.ListModelsRequest(parent=LOCATION_PATH)
        )
        assert ds == []

    def test_list_models_not_empty(self):
        models = ["some_model"]
        client = self.tables_client(
            {
                "list_models.return_value": models,
                "location_path.return_value": LOCATION_PATH,
            },
            {},
        )
        ds = client.list_models()

        client.auto_ml_client.list_models.assert_called_with(
            request=automl_v1beta1.ListModelsRequest(parent=LOCATION_PATH)
        )
        assert len(ds) == 1
        assert ds[0] == "some_model"

    def test_get_model_name(self):
        model_actual = "model"
        client = self.tables_client({"get_model.return_value": model_actual}, {})
        model = client.get_model(model_name="my_model")
        client.auto_ml_client.get_model.assert_called_with(name="my_model")
        assert model == model_actual

    def test_get_no_model(self):
        client = self.tables_client(
            {"get_model.side_effect": exceptions.NotFound("err")}, {}
        )
        with pytest.raises(exceptions.NotFound):
            client.get_model(model_name="my_model")
        client.auto_ml_client.get_model.assert_called_with(name="my_model")

    def test_get_model_from_empty_list(self):
        client = self.tables_client({"list_models.return_value": []}, {})
        with pytest.raises(exceptions.NotFound):
            client.get_model(model_display_name="my_model")

    def test_get_model_from_list_not_found(self):
        client = self.tables_client(
            {"list_models.return_value": [mock.Mock(display_name="not_it")]}, {}
        )
        with pytest.raises(exceptions.NotFound):
            client.get_model(model_display_name="my_model")

    def test_get_model_from_list(self):
        client = self.tables_client(
            {
                "list_models.return_value": [
                    mock.Mock(display_name="not_it"),
                    mock.Mock(display_name="my_model"),
                ]
            },
            {},
        )
        model = client.get_model(model_display_name="my_model")
        assert model.display_name == "my_model"

    def test_get_model_from_list_ambiguous(self):
        client = self.tables_client(
            {
                "list_models.return_value": [
                    mock.Mock(display_name="my_model"),
                    mock.Mock(display_name="not_my_model"),
                    mock.Mock(display_name="my_model"),
                ]
            },
            {},
        )
        with pytest.raises(ValueError):
            client.get_model(model_display_name="my_model")

    def test_delete_model(self):
        model = mock.Mock()
        model.configure_mock(name="name")
        client = self.tables_client({"delete_model.return_value": None}, {})
        client.delete_model(model=model)
        client.auto_ml_client.delete_model.assert_called_with(
            request=automl_v1beta1.DeleteModelRequest(name="name")
        )

    def test_delete_model_not_found(self):
        client = self.tables_client({"list_models.return_value": []}, {})
        client.delete_model(model_display_name="not_found")
        client.auto_ml_client.delete_model.assert_not_called()

    def test_delete_model_name(self):
        client = self.tables_client({"delete_model.return_value": None}, {})
        client.delete_model(model_name="name")
        client.auto_ml_client.delete_model.assert_called_with(
            request=automl_v1beta1.DeleteModelRequest(name="name")
        )

    def test_deploy_model_no_args(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.deploy_model()
        client.auto_ml_client.deploy_model.assert_not_called()

    def test_deploy_model(self):
        client = self.tables_client({}, {})
        client.deploy_model(model_name="name")
        client.auto_ml_client.deploy_model.assert_called_with(
            request=automl_v1beta1.DeployModelRequest(name="name")
        )

    def test_deploy_model_not_found(self):
        client = self.tables_client({"list_models.return_value": []}, {})
        with pytest.raises(exceptions.NotFound):
            client.deploy_model(model_display_name="name")
        client.auto_ml_client.deploy_model.assert_not_called()

    def test_undeploy_model(self):
        client = self.tables_client({}, {})
        client.undeploy_model(model_name="name")
        client.auto_ml_client.undeploy_model.assert_called_with(
            request=automl_v1beta1.UndeployModelRequest(name="name")
        )

    def test_undeploy_model_not_found(self):
        client = self.tables_client({"list_models.return_value": []}, {})
        with pytest.raises(exceptions.NotFound):
            client.undeploy_model(model_display_name="name")
        client.auto_ml_client.undeploy_model.assert_not_called()

    def test_create_model(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")
        column_spec_mock = mock.Mock()
        column_spec_mock.configure_mock(name="column/2", display_name="column")
        client = self.tables_client(
            {
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_mock],
                "location_path.return_value": LOCATION_PATH,
            },
            {},
        )
        client.create_model(
            "my_model", dataset_name="my_dataset", train_budget_milli_node_hours=1000
        )
        client.auto_ml_client.create_model.assert_called_with(
            request=automl_v1beta1.CreateModelRequest(
                parent=LOCATION_PATH,
                model={
                    "display_name": "my_model",
                    "dataset_id": "my_dataset",
                    "tables_model_metadata": {"train_budget_milli_node_hours": 1000},
                },
            )
        )

    def test_create_model_include_columns(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")

        column_spec_1 = automl_v1beta1.ColumnSpec(
            name="column/1", display_name="column1"
        )
        column_spec_2 = automl_v1beta1.ColumnSpec(
            name="column/2", display_name="column2"
        )

        client = self.tables_client(
            client_attrs={
                "list_table_specs.return_value": [
                    automl_v1beta1.TableSpec(name="table")
                ],
                "list_column_specs.return_value": [column_spec_1, column_spec_2],
                "location_path.return_value": LOCATION_PATH,
            },
            prediction_client_attrs={},
        )
        client.create_model(
            "my_model",
            dataset_name="my_dataset",
            include_column_spec_names=["column1"],
            train_budget_milli_node_hours=1000,
        )
        client.auto_ml_client.create_model.assert_called_with(
            request=automl_v1beta1.CreateModelRequest(
                parent=LOCATION_PATH,
                model=automl_v1beta1.Model(
                    display_name="my_model",
                    dataset_id="my_dataset",
                    tables_model_metadata=automl_v1beta1.TablesModelMetadata(
                        train_budget_milli_node_hours=1000,
                        input_feature_column_specs=[column_spec_1],
                    ),
                ),
            )
        )

    def test_create_model_exclude_columns(self):
        table_spec_mock = mock.Mock()
        # name is reserved in use of __init__, needs to be passed here
        table_spec_mock.configure_mock(name="table")

        column_spec_1 = automl_v1beta1.ColumnSpec(
            name="column/1", display_name="column1"
        )
        column_spec_2 = automl_v1beta1.ColumnSpec(
            name="column/2", display_name="column2"
        )
        client = self.tables_client(
            client_attrs={
                "list_table_specs.return_value": [table_spec_mock],
                "list_column_specs.return_value": [column_spec_1, column_spec_2],
                "location_path.return_value": LOCATION_PATH,
            },
            prediction_client_attrs={},
        )
        client.create_model(
            "my_model",
            dataset_name="my_dataset",
            exclude_column_spec_names=["column1"],
            train_budget_milli_node_hours=1000,
        )
        client.auto_ml_client.create_model.assert_called_with(
            request=automl_v1beta1.CreateModelRequest(
                parent=LOCATION_PATH,
                model=automl_v1beta1.Model(
                    display_name="my_model",
                    dataset_id="my_dataset",
                    tables_model_metadata=automl_v1beta1.TablesModelMetadata(
                        train_budget_milli_node_hours=1000,
                        input_feature_column_specs=[column_spec_2],
                    ),
                ),
            )
        )

    def test_create_model_invalid_hours_small(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.create_model(
                "my_model", dataset_name="my_dataset", train_budget_milli_node_hours=1
            )
        client.auto_ml_client.create_model.assert_not_called()

    def test_create_model_invalid_hours_large(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.create_model(
                "my_model",
                dataset_name="my_dataset",
                train_budget_milli_node_hours=1000000,
            )
        client.auto_ml_client.create_model.assert_not_called()

    def test_create_model_invalid_no_dataset(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.create_model("my_model", train_budget_milli_node_hours=1000)
        client.auto_ml_client.get_dataset.assert_not_called()
        client.auto_ml_client.create_model.assert_not_called()

    def test_create_model_invalid_include_exclude(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.create_model(
                "my_model",
                dataset_name="my_dataset",
                include_column_spec_names=["a"],
                exclude_column_spec_names=["b"],
                train_budget_milli_node_hours=1000,
            )
        client.auto_ml_client.get_dataset.assert_not_called()
        client.auto_ml_client.create_model.assert_not_called()

    def test_predict_from_array(self):
        data_type = mock.Mock(type_code=data_types.TypeCode.CATEGORY)
        column_spec = mock.Mock(display_name="a", data_type=data_type)
        model_metadata = mock.Mock(input_feature_column_specs=[column_spec])
        model = mock.Mock()
        model.configure_mock(tables_model_metadata=model_metadata, name="my_model")
        client = self.tables_client({"get_model.return_value": model}, {})
        client.predict(["1"], model_name="my_model")

        # append each row value separately until issue is resovled
        # https://github.com/googleapis/proto-plus-python/issues/104
        row = data_items.Row()
        row.values.append(struct.Value(string_value="1"))
        payload = data_items.ExamplePayload(row=row)

        client.prediction_client.predict.assert_called_with(
            request=automl_v1beta1.PredictRequest(
                name="my_model", payload=payload, params=None
            )
        )

    def test_predict_from_dict(self):
        data_type = mock.Mock(type_code=data_types.TypeCode.CATEGORY)
        column_spec_a = mock.Mock(display_name="a", data_type=data_type)
        column_spec_b = mock.Mock(display_name="b", data_type=data_type)
        model_metadata = mock.Mock(
            input_feature_column_specs=[column_spec_a, column_spec_b]
        )
        model = mock.Mock()
        model.configure_mock(tables_model_metadata=model_metadata, name="my_model")
        client = self.tables_client({"get_model.return_value": model}, {})
        client.predict({"a": "1", "b": "2"}, model_name="my_model")

        # append each row value separately until issue is resovled
        # https://github.com/googleapis/proto-plus-python/issues/104
        row = data_items.Row()
        row.values.append(struct.Value(string_value="1"))
        row.values.append(struct.Value(string_value="2"))

        payload = data_items.ExamplePayload(row=row)

        client.prediction_client.predict.assert_called_with(
            request=automl_v1beta1.PredictRequest(
                name="my_model", payload=payload, params=None
            )
        )

    def test_predict_from_dict_with_feature_importance(self):
        data_type = mock.Mock(type_code=data_types.TypeCode.CATEGORY)
        column_spec_a = mock.Mock(display_name="a", data_type=data_type)
        column_spec_b = mock.Mock(display_name="b", data_type=data_type)
        model_metadata = mock.Mock(
            input_feature_column_specs=[column_spec_a, column_spec_b]
        )
        model = mock.Mock()
        model.configure_mock(tables_model_metadata=model_metadata, name="my_model")
        client = self.tables_client({"get_model.return_value": model}, {})
        client.predict(
            {"a": "1", "b": "2"}, model_name="my_model", feature_importance=True
        )

        # append each row value separately until issue is resovled
        # https://github.com/googleapis/proto-plus-python/issues/104
        row = data_items.Row()
        row.values.append(struct.Value(string_value="1"))
        row.values.append(struct.Value(string_value="2"))

        payload = data_items.ExamplePayload(row=row)

        client.prediction_client.predict.assert_called_with(
            request=automl_v1beta1.PredictRequest(
                name="my_model", payload=payload, params={"feature_importance": "true"}
            )
        )

    def test_predict_from_dict_missing(self):
        data_type = mock.Mock(type_code=data_types.TypeCode.CATEGORY)
        column_spec_a = mock.Mock(display_name="a", data_type=data_type)
        column_spec_b = mock.Mock(display_name="b", data_type=data_type)
        model_metadata = mock.Mock(
            input_feature_column_specs=[column_spec_a, column_spec_b]
        )
        model = mock.Mock()
        model.configure_mock(tables_model_metadata=model_metadata, name="my_model")
        client = self.tables_client({"get_model.return_value": model}, {})
        client.predict({"a": "1"}, model_name="my_model")

        # append each row value separately until issue is resovled
        # https://github.com/googleapis/proto-plus-python/issues/104
        row = data_items.Row()
        row.values.append(struct.Value(string_value="1"))
        row.values.append(struct.Value(null_value=struct.NullValue.NULL_VALUE))

        payload = data_items.ExamplePayload(row=row)

        client.prediction_client.predict.assert_called_with(
            request=automl_v1beta1.PredictRequest(
                name="my_model", payload=payload, params=None
            )
        )

    def test_predict_all_types(self):
        float_type = mock.Mock(type_code=data_types.TypeCode.FLOAT64)
        timestamp_type = mock.Mock(type_code=data_types.TypeCode.TIMESTAMP)
        string_type = mock.Mock(type_code=data_types.TypeCode.STRING)
        array_type = mock.Mock(
            type_code=data_types.TypeCode.ARRAY,
            list_element_type=mock.Mock(type_code=data_types.TypeCode.FLOAT64),
        )

        struct_type = mock.Mock(
            type_code=data_types.TypeCode.STRUCT,
            struct_type=data_types.StructType(
                fields={
                    "a": data_types.DataType(type_code=data_types.TypeCode.CATEGORY),
                    "b": data_types.DataType(type_code=data_types.TypeCode.CATEGORY),
                }
            ),
        )
        category_type = mock.Mock(type_code=data_types.TypeCode.CATEGORY)
        column_spec_float = mock.Mock(display_name="float", data_type=float_type)
        column_spec_timestamp = mock.Mock(
            display_name="timestamp", data_type=timestamp_type
        )
        column_spec_string = mock.Mock(display_name="string", data_type=string_type)
        column_spec_array = mock.Mock(display_name="array", data_type=array_type)
        column_spec_struct = mock.Mock(display_name="struct", data_type=struct_type)
        column_spec_category = mock.Mock(
            display_name="category", data_type=category_type
        )
        column_spec_null = mock.Mock(display_name="null", data_type=category_type)
        model_metadata = mock.Mock(
            input_feature_column_specs=[
                column_spec_float,
                column_spec_timestamp,
                column_spec_string,
                column_spec_array,
                column_spec_struct,
                column_spec_category,
                column_spec_null,
            ]
        )
        model = mock.Mock()
        model.configure_mock(tables_model_metadata=model_metadata, name="my_model")
        client = self.tables_client({"get_model.return_value": model}, {})
        client.predict(
            {
                "float": 1.0,
                "timestamp": "EST",
                "string": "text",
                "array": [1],
                "struct": {"a": "label_a", "b": "label_b"},
                "category": "a",
                "null": None,
            },
            model_name="my_model",
        )
        struct_pb = struct.Struct()
        struct_pb.fields["a"].CopyFrom(struct.Value(string_value="label_a"))
        struct_pb.fields["b"].CopyFrom(struct.Value(string_value="label_b"))

        # append each row value separately until issue is resovled
        # https://github.com/googleapis/proto-plus-python/issues/104
        row = data_items.Row()
        values = [
            struct.Value(number_value=1.0),
            struct.Value(string_value="EST"),
            struct.Value(string_value="text"),
            struct.Value(
                list_value=struct.ListValue(values=[struct.Value(number_value=1.0)])
            ),
            struct.Value(struct_value=struct_pb),
            struct.Value(string_value="a"),
            struct.Value(null_value=struct.NullValue.NULL_VALUE),
        ]
        for v in values:
            row.values.append(v)

        payload = data_items.ExamplePayload(row=row)

        client.prediction_client.predict.assert_called_with(
            request=automl_v1beta1.PredictRequest(
                name="my_model", payload=payload, params=None
            )
        )

    def test_predict_from_array_missing(self):
        data_type = mock.Mock(type_code=data_types.TypeCode.CATEGORY)
        column_spec = mock.Mock(display_name="a", data_type=data_type)
        model_metadata = mock.Mock(input_feature_column_specs=[column_spec])
        model = mock.Mock()
        model.configure_mock(tables_model_metadata=model_metadata, name="my_model")
        client = self.tables_client({"get_model.return_value": model}, {})
        with pytest.raises(ValueError):
            client.predict([], model_name="my_model")
        client.prediction_client.predict.assert_not_called()

    def test_batch_predict_pandas_dataframe(self):
        client = self.tables_client(
            gcs_client_attrs={
                "bucket_name": "my_bucket",
                "upload_pandas_dataframe.return_value": "gs://input",
            }
        )
        dataframe = pandas.DataFrame({})
        client.batch_predict(
            project=PROJECT,
            region=REGION,
            model_name="my_model",
            pandas_dataframe=dataframe,
            gcs_output_uri_prefix="gs://output",
        )

        client.gcs_client.ensure_bucket_exists.assert_called_with(PROJECT, REGION)
        client.gcs_client.upload_pandas_dataframe.assert_called_with(dataframe)

        client.prediction_client.batch_predict.assert_called_with(
            request=automl_v1beta1.BatchPredictRequest(
                name="my_model",
                input_config={"gcs_source": {"input_uris": ["gs://input"]}},
                output_config={"gcs_destination": {"output_uri_prefix": "gs://output"}},
            )
        )

    def test_batch_predict_pandas_dataframe_init_gcs(self):
        client = automl_v1beta1.TablesClient(
            client=mock.Mock(),
            prediction_client=mock.Mock(),
            project=PROJECT,
            region=REGION,
            credentials=AnonymousCredentials(),
        )

        dataframe = pandas.DataFrame({})
        patch = mock.patch(
            "google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient",
            bucket_name="my_bucket",
        )
        with patch as MockGcsClient:
            mockInstance = MockGcsClient.return_value
            mockInstance.upload_pandas_dataframe.return_value = "gs://input"

            dataframe = pandas.DataFrame({})
            client.batch_predict(
                model_name="my_model",
                pandas_dataframe=dataframe,
                gcs_output_uri_prefix="gs://output",
            )

            client.gcs_client.ensure_bucket_exists.assert_called_with(PROJECT, REGION)
            client.gcs_client.upload_pandas_dataframe.assert_called_with(dataframe)

            client.prediction_client.batch_predict.assert_called_with(
                request=automl_v1beta1.BatchPredictRequest(
                    name="my_model",
                    input_config={"gcs_source": {"input_uris": ["gs://input"]}},
                    output_config={
                        "gcs_destination": {"output_uri_prefix": "gs://output"}
                    },
                )
            )

    def test_batch_predict_gcs(self):
        client = self.tables_client({}, {})
        client.batch_predict(
            model_name="my_model",
            gcs_input_uris="gs://input",
            gcs_output_uri_prefix="gs://output",
        )
        client.prediction_client.batch_predict.assert_called_with(
            request=automl_v1beta1.BatchPredictRequest(
                name="my_model",
                input_config={"gcs_source": {"input_uris": ["gs://input"]}},
                output_config={"gcs_destination": {"output_uri_prefix": "gs://output"}},
            )
        )

    def test_batch_predict_bigquery(self):
        client = self.tables_client({}, {})
        client.batch_predict(
            model_name="my_model",
            bigquery_input_uri="bq://input",
            bigquery_output_uri="bq://output",
        )
        client.prediction_client.batch_predict.assert_called_with(
            request=automl_v1beta1.BatchPredictRequest(
                name="my_model",
                input_config={"bigquery_source": {"input_uri": "bq://input"}},
                output_config={"bigquery_destination": {"output_uri": "bq://output"}},
            )
        )

    def test_batch_predict_bigquery_with_params(self):
        client = self.tables_client({}, {})
        client.batch_predict(
            model_name="my_model",
            bigquery_input_uri="bq://input",
            bigquery_output_uri="bq://output",
            params={"feature_importance": "true"},
        )

        client.prediction_client.batch_predict.assert_called_with(
            request=automl_v1beta1.BatchPredictRequest(
                name="my_model",
                input_config={"bigquery_source": {"input_uri": "bq://input"}},
                output_config={"bigquery_destination": {"output_uri": "bq://output"}},
                params={"feature_importance": "true"},
            )
        )

    def test_batch_predict_mixed(self):
        client = self.tables_client({}, {})
        client.batch_predict(
            model_name="my_model",
            gcs_input_uris="gs://input",
            bigquery_output_uri="bq://output",
        )
        client.prediction_client.batch_predict.assert_called_with(
            request=automl_v1beta1.BatchPredictRequest(
                name="my_model",
                input_config={"gcs_source": {"input_uris": ["gs://input"]}},
                output_config={"bigquery_destination": {"output_uri": "bq://output"}},
            )
        )

    def test_batch_predict_missing_input_gcs_uri(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.batch_predict(
                model_name="my_model",
                gcs_input_uris=None,
                gcs_output_uri_prefix="gs://output",
            )
        client.prediction_client.batch_predict.assert_not_called()

    def test_batch_predict_missing_input_bigquery_uri(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.batch_predict(
                model_name="my_model",
                bigquery_input_uri=None,
                gcs_output_uri_prefix="gs://output",
            )
        client.prediction_client.batch_predict.assert_not_called()

    def test_batch_predict_missing_output_gcs_uri(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.batch_predict(
                model_name="my_model",
                gcs_input_uris="gs://input",
                gcs_output_uri_prefix=None,
            )
        client.prediction_client.batch_predict.assert_not_called()

    def test_batch_predict_missing_output_bigquery_uri(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.batch_predict(
                model_name="my_model",
                gcs_input_uris="gs://input",
                bigquery_output_uri=None,
            )
        client.prediction_client.batch_predict.assert_not_called()

    def test_batch_predict_missing_model(self):
        client = self.tables_client({"list_models.return_value": []}, {})
        with pytest.raises(exceptions.NotFound):
            client.batch_predict(
                model_display_name="my_model",
                gcs_input_uris="gs://input",
                gcs_output_uri_prefix="gs://output",
            )
        client.prediction_client.batch_predict.assert_not_called()

    def test_batch_predict_no_model(self):
        client = self.tables_client({}, {})
        with pytest.raises(ValueError):
            client.batch_predict(
                gcs_input_uris="gs://input", gcs_output_uri_prefix="gs://output"
            )
        client.auto_ml_client.list_models.assert_not_called()
        client.prediction_client.batch_predict.assert_not_called()

    def test_auto_ml_client_credentials(self):
        credentials_mock = mock.Mock()
        patch_auto_ml_client = mock.patch(
            "google.cloud.automl_v1beta1.services.tables.tables_client.AutoMlClient"
        )
        with patch_auto_ml_client as MockAutoMlClient:
            automl_v1beta1.TablesClient(credentials=credentials_mock)
        _, auto_ml_client_kwargs = MockAutoMlClient.call_args
        assert "credentials" in auto_ml_client_kwargs
        assert auto_ml_client_kwargs["credentials"] == credentials_mock

    def test_prediction_client_credentials(self):
        credentials_mock = mock.Mock()
        patch_prediction_client = mock.patch(
            "google.cloud.automl_v1beta1.services.tables.tables_client.PredictionServiceClient"
        )
        with patch_prediction_client as MockPredictionClient:
            automl_v1beta1.TablesClient(credentials=credentials_mock)
        _, prediction_client_kwargs = MockPredictionClient.call_args
        assert "credentials" in prediction_client_kwargs
        assert prediction_client_kwargs["credentials"] == credentials_mock

    def test_prediction_client_client_info(self):
        credentials_mock = mock.Mock()
        client_info_mock = mock.Mock()
        client_mock = mock.Mock()
        patch_prediction_client = mock.patch(
            "google.cloud.automl_v1beta1.services.tables.tables_client.PredictionServiceClient"
        )
        with patch_prediction_client as MockPredictionClient:
            automl_v1beta1.TablesClient(
                credentials=credentials_mock,
                client=client_mock,
                client_info=client_info_mock,
            )
        _, prediction_client_kwargs = MockPredictionClient.call_args
        assert "client_info" in prediction_client_kwargs
        assert prediction_client_kwargs["client_info"] == client_info_mock
