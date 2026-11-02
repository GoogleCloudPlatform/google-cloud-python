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

import datetime

import pytest


import google.cloud._helpers
import google.cloud.bigquery.model

KMS_KEY_NAME = "projects/1/locations/us/keyRings/1/cryptoKeys/1"


@pytest.fixture
def target_class():
    from google.cloud.bigquery import Model

    return Model


@pytest.fixture
def object_under_test(target_class):
    return target_class("project-id.dataset_id.model_id")


def test_ctor(target_class):
    from google.cloud.bigquery import ModelReference

    ref = ModelReference.from_string("my-proj.my_dset.my_model")
    got = target_class(ref)
    assert got.reference == ref


def test_ctor_string(target_class):
    from google.cloud.bigquery import ModelReference

    model_id = "my-proj.my_dset.my_model"
    ref = ModelReference.from_string(model_id)
    got = target_class(model_id)
    assert got.reference == ref


def test_from_api_repr(target_class):
    from google.cloud.bigquery import ModelReference

    creation_time = datetime.datetime(
        2010, 5, 19, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    modified_time = datetime.datetime(
        2011, 10, 1, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    expiration_time = datetime.datetime(
        2012, 12, 21, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    resource = {
        "modelReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "modelId": "my_model",
        },
        "location": "US",
        "etag": "abcdefg",
        "creationTime": str(google.cloud._helpers._millis(creation_time)),
        "lastModifiedTime": str(google.cloud._helpers._millis(modified_time)),
        "expirationTime": str(google.cloud._helpers._millis(expiration_time)),
        "description": "A friendly description.",
        "friendlyName": "A friendly name.",
        "modelType": "LOGISTIC_REGRESSION",
        "labels": {"greeting": "こんにちは"},
        "trainingRuns": [
            {
                "trainingOptions": {"initialLearnRate": 1.0},
                "startTime": str(
                    google.cloud._helpers._datetime_to_rfc3339(creation_time)
                ),
            },
            {
                "trainingOptions": {"initialLearnRate": 0.5},
                "startTime": str(
                    google.cloud._helpers._datetime_to_rfc3339(modified_time)
                ),
            },
            {
                "trainingOptions": {"initialLearnRate": 0.25},
                "startTime": str(
                    google.cloud._helpers._datetime_to_rfc3339(expiration_time)
                ),
            },
        ],
        "bestTrialId": "123",
        "featureColumns": [],
        "encryptionConfiguration": {"kmsKeyName": KMS_KEY_NAME},
    }
    got = target_class.from_api_repr(resource)

    assert got.project == "my-project"
    assert got.dataset_id == "my_dataset"
    assert got.model_id == "my_model"
    assert got.reference == ModelReference.from_string("my-project.my_dataset.my_model")
    assert got.path == "/projects/my-project/datasets/my_dataset/models/my_model"
    assert got.location == "US"
    assert got.etag == "abcdefg"
    assert got.created == creation_time
    assert got.modified == modified_time
    assert got.expires == expiration_time
    assert got.description == "A friendly description."
    assert got.friendly_name == "A friendly name."
    assert got.model_type == "LOGISTIC_REGRESSION"
    assert got.labels == {"greeting": "こんにちは"}
    assert got.encryption_configuration.kms_key_name == KMS_KEY_NAME
    assert got.best_trial_id == 123
    assert got.training_runs[0]["trainingOptions"]["initialLearnRate"] == 1.0
    assert (
        google.cloud._helpers._rfc3339_to_datetime(got.training_runs[0]["startTime"])
        == creation_time
    )
    assert got.training_runs[1]["trainingOptions"]["initialLearnRate"] == 0.5
    assert (
        google.cloud._helpers._rfc3339_to_datetime(got.training_runs[1]["startTime"])
        == modified_time
    )
    assert got.training_runs[2]["trainingOptions"]["initialLearnRate"] == 0.25
    assert (
        google.cloud._helpers._rfc3339_to_datetime(got.training_runs[2]["startTime"])
        == expiration_time
    )
    assert got.transform_columns == []


def test_from_api_repr_w_minimal_resource(target_class):
    from google.cloud.bigquery import ModelReference

    resource = {
        "modelReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "modelId": "my_model",
        }
    }
    got = target_class.from_api_repr(resource)
    assert got.reference == ModelReference.from_string("my-project.my_dataset.my_model")
    assert got.location is None
    assert got.etag is None
    assert got.created is None
    assert got.modified is None
    assert got.expires is None
    assert got.description is None
    assert got.friendly_name is None
    assert got.model_type == "MODEL_TYPE_UNSPECIFIED"
    assert got.labels == {}
    assert got.encryption_configuration is None
    assert len(got.training_runs) == 0
    assert len(got.feature_columns) == 0
    assert len(got.label_columns) == 0
    assert got.best_trial_id is None


def test_from_api_repr_w_unknown_fields(target_class):
    from google.cloud.bigquery import ModelReference

    resource = {
        "modelReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "modelId": "my_model",
        },
        "thisFieldIsNotInTheProto": "just ignore me",
    }
    got = target_class.from_api_repr(resource)
    assert got.reference == ModelReference.from_string("my-project.my_dataset.my_model")
    assert got._properties == resource


def test_from_api_repr_w_unknown_type(target_class):
    from google.cloud.bigquery import ModelReference

    resource = {
        "modelReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "modelId": "my_model",
        },
        "modelType": "BE_A_GOOD_ROLE_MODEL",  # This model type does not exist.
    }
    got = target_class.from_api_repr(resource)
    assert got.reference == ModelReference.from_string("my-project.my_dataset.my_model")
    assert got.model_type == "BE_A_GOOD_ROLE_MODEL"  # No checks for invalid types.
    assert got._properties == resource


def test_from_api_repr_w_missing_reference(target_class):
    resource = {}
    got = target_class.from_api_repr(resource)
    assert got.reference is None
    assert got._properties == resource


@pytest.mark.parametrize(
    "resource,filter_fields,expected",
    [
        (
            {
                "friendlyName": "hello",
                "description": "world",
                "expirationTime": "12345",
                "labels": {"a-label": "a-value"},
            },
            ["description"],
            {"description": "world"},
        ),
        (
            {"friendlyName": "hello", "description": "world"},
            ["friendlyName"],
            {"friendlyName": "hello"},
        ),
        (
            {
                "friendlyName": "hello",
                "description": "world",
                "expirationTime": "12345",
                "labels": {"a-label": "a-value"},
            },
            ["expires"],
            {"expirationTime": "12345"},
        ),
        (
            {
                "friendlyName": "hello",
                "description": "world",
                "expirationTime": None,
                "labels": {"a-label": "a-value"},
            },
            ["expires"],
            {"expirationTime": None},
        ),
        (
            {
                "friendlyName": "hello",
                "description": "world",
                "expirationTime": None,
                "labels": {"a-label": "a-value"},
            },
            ["labels"],
            {"labels": {"a-label": "a-value"}},
        ),
        (
            {
                "friendlyName": "hello",
                "description": "world",
                "expirationTime": None,
                "labels": {"a-label": "a-value"},
                "encryptionConfiguration": {"kmsKeyName": KMS_KEY_NAME},
            },
            ["encryptionConfiguration"],
            {"encryptionConfiguration": {"kmsKeyName": KMS_KEY_NAME}},
        ),
    ],
)
def test_build_resource(object_under_test, resource, filter_fields, expected):
    object_under_test._properties = resource
    got = object_under_test._build_resource(filter_fields)
    assert got == expected


def test_feature_columns(object_under_test):
    from google.cloud.bigquery import standard_sql

    object_under_test._properties["featureColumns"] = [
        {"name": "col_1", "type": {"typeKind": "STRING"}},
        {"name": "col_2", "type": {"typeKind": "FLOAT64"}},
    ]
    expected = [
        standard_sql.StandardSqlField(
            "col_1",
            standard_sql.StandardSqlDataType(standard_sql.StandardSqlTypeNames.STRING),
        ),
        standard_sql.StandardSqlField(
            "col_2",
            standard_sql.StandardSqlDataType(standard_sql.StandardSqlTypeNames.FLOAT64),
        ),
    ]
    assert object_under_test.feature_columns == expected


def test_from_api_repr_w_transform_columns(target_class):
    resource = {
        "modelReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "modelId": "my_model",
        },
        "transformColumns": [
            {
                "name": "transform_name",
                "type": {"typeKind": "INT64"},
                "transformSql": "transform_sql",
            }
        ],
    }
    got = target_class.from_api_repr(resource)
    assert len(got.transform_columns) == 1
    transform_column = got.transform_columns[0]
    assert isinstance(transform_column, google.cloud.bigquery.model.TransformColumn)
    assert transform_column.name == "transform_name"


def test_transform_column_name():
    transform_columns = google.cloud.bigquery.model.TransformColumn(
        {"name": "is_female"}
    )
    assert transform_columns.name == "is_female"


def test_transform_column_transform_sql():
    transform_columns = google.cloud.bigquery.model.TransformColumn(
        {"transformSql": "is_female"}
    )
    assert transform_columns.transform_sql == "is_female"


def test_transform_column_type():
    transform_columns = google.cloud.bigquery.model.TransformColumn(
        {"type": {"typeKind": "BOOL"}}
    )
    assert transform_columns.type_.type_kind == "BOOL"


def test_transform_column_type_none():
    transform_columns = google.cloud.bigquery.model.TransformColumn({})
    assert transform_columns.type_ is None


def test_transform_column_from_api_repr_with_unknown_properties():
    transform_column = google.cloud.bigquery.model.TransformColumn.from_api_repr(
        {
            "name": "is_female",
            "type": {"typeKind": "BOOL"},
            "transformSql": "is_female",
            "test": "one",
        }
    )
    assert transform_column._properties == {
        "name": "is_female",
        "type": {"typeKind": "BOOL"},
        "transformSql": "is_female",
        "test": "one",
    }


def test_label_columns(object_under_test):
    from google.cloud.bigquery import standard_sql

    object_under_test._properties["labelColumns"] = [
        {"name": "col_1", "type": {"typeKind": "STRING"}},
        {"name": "col_2", "type": {"typeKind": "FLOAT64"}},
    ]
    expected = [
        standard_sql.StandardSqlField(
            "col_1",
            standard_sql.StandardSqlDataType(standard_sql.StandardSqlTypeNames.STRING),
        ),
        standard_sql.StandardSqlField(
            "col_2",
            standard_sql.StandardSqlDataType(standard_sql.StandardSqlTypeNames.FLOAT64),
        ),
    ]
    assert object_under_test.label_columns == expected


def test_set_description(object_under_test):
    assert not object_under_test.description
    object_under_test.description = "A model description."
    assert object_under_test.description == "A model description."
    object_under_test.description = None
    assert not object_under_test.description


def test_set_expires(object_under_test):
    assert not object_under_test.expires
    expiration_time = datetime.datetime(
        2012, 12, 21, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    object_under_test.expires = expiration_time
    assert object_under_test.expires == expiration_time
    object_under_test.expires = None
    assert not object_under_test.expires


def test_set_friendly_name(object_under_test):
    assert not object_under_test.friendly_name
    object_under_test.friendly_name = "A model name."
    assert object_under_test.friendly_name == "A model name."
    object_under_test.friendly_name = None
    assert not object_under_test.friendly_name


def test_set_labels(object_under_test):
    assert object_under_test.labels == {}
    object_under_test.labels["data_owner"] = "someteam"
    assert object_under_test.labels == {"data_owner": "someteam"}
    del object_under_test.labels["data_owner"]
    assert object_under_test.labels == {}


def test_replace_labels(object_under_test):
    assert object_under_test.labels == {}
    object_under_test.labels = {"data_owner": "someteam"}
    assert object_under_test.labels == {"data_owner": "someteam"}
    labels = {}
    object_under_test.labels = labels
    assert object_under_test.labels is labels
    object_under_test.labels = None
    assert object_under_test.labels == {}


def test_set_encryption_configuration(object_under_test):
    from google.cloud.bigquery.encryption_configuration import EncryptionConfiguration

    assert not object_under_test.encryption_configuration
    object_under_test.encryption_configuration = EncryptionConfiguration(
        kms_key_name=KMS_KEY_NAME
    )
    assert object_under_test.encryption_configuration.kms_key_name == KMS_KEY_NAME
    object_under_test.encryption_configuration = None
    assert not object_under_test.encryption_configuration


def test_repr(target_class):
    model = target_class("my-proj.my_dset.my_model")
    got = repr(model)
    assert got == (
        "Model(reference=ModelReference("
        "project_id='my-proj', dataset_id='my_dset', model_id='my_model'))"
    )


def test_to_api_repr(target_class):
    model = target_class("my-proj.my_dset.my_model")
    resource = {
        "etag": "abcdefg",
        "modelReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "modelId": "my_model",
        },
        "creationTime": "1274284800000",
        "lastModifiedTime": "1317484800000",
        "modelType": "LOGISTIC_REGRESSION",
        "trainingRuns": [
            {
                "trainingOptions": {"initialLearnRate": 1.0},
                "startTime": "2010-05-19T16:00:00Z",
            },
            {
                "trainingOptions": {"initialLearnRate": 0.5},
                "startTime": "2011-10-01T16:00:00Z",
            },
            {
                "trainingOptions": {"initialLearnRate": 0.25},
                "startTime": "2012-12-21T16:00:00Z",
            },
        ],
        "description": "A friendly description.",
        "location": "US",
        "friendlyName": "A friendly name.",
        "labels": {"greeting": "こんにちは"},
        "expirationTime": "1356105600000",
        "encryptionConfiguration": {
            "kmsKeyName": "projects/1/locations/us/keyRings/1/cryptoKeys/1"
        },
    }
    model._properties = resource
    got = model.to_api_repr()
    assert got == resource
