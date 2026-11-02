# Copyright 2021 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import mock

from google.cloud.bigquery.dataset import Dataset, DatasetReference
from .helpers import make_connection, dataset_polymorphic, make_client
import google.cloud.bigquery.dataset
from google.cloud.bigquery.retry import DEFAULT_TIMEOUT
import pytest


@dataset_polymorphic
def test_create_dataset_minimal(make_dataset, get_reference, client, PROJECT, DS_ID):
    PATH = "projects/%s/datasets" % PROJECT
    RESOURCE = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "%s:%s" % (PROJECT, DS_ID),
    }
    conn = client._connection = make_connection(RESOURCE)

    dataset = make_dataset(PROJECT, DS_ID)
    after = client.create_dataset(dataset, timeout=7.5)

    assert after.dataset_id == DS_ID
    assert after.project == PROJECT
    assert after.etag == RESOURCE["etag"]
    assert after.full_dataset_id == RESOURCE["id"]

    conn.api_request.assert_called_once_with(
        method="POST",
        path="/%s" % PATH,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
        },
        timeout=7.5,
    )


def test_create_dataset_w_attrs(client, PROJECT, DS_ID):
    from google.cloud.bigquery.dataset import AccessEntry

    PATH = "projects/%s/datasets" % PROJECT
    DESCRIPTION = "DESC"
    FRIENDLY_NAME = "FN"
    LOCATION = "US"
    USER_EMAIL = "phred@example.com"
    LABELS = {"color": "red"}
    VIEW = {
        "projectId": "my-proj",
        "datasetId": "starry-skies",
        "tableId": "northern-hemisphere",
    }
    DEFAULT_ROUNDING_MODE = "ROUND_HALF_EVEN"
    RESOURCE_TAGS = {"123456789012/foo": "bar"}
    RESOURCE = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "%s:%s" % (PROJECT, DS_ID),
        "description": DESCRIPTION,
        "friendlyName": FRIENDLY_NAME,
        "location": LOCATION,
        "defaultTableExpirationMs": "3600",
        "labels": LABELS,
        "access": [{"role": "OWNER", "userByEmail": USER_EMAIL}, {"view": VIEW}],
        "defaultRoundingMode": DEFAULT_ROUNDING_MODE,
        "resourceTags": RESOURCE_TAGS,
    }
    conn = client._connection = make_connection(RESOURCE)
    entries = [
        AccessEntry("OWNER", "userByEmail", USER_EMAIL),
        AccessEntry(None, "view", VIEW),
    ]

    ds_ref = DatasetReference(PROJECT, DS_ID)
    before = Dataset(ds_ref)
    before.access_entries = entries
    before.description = DESCRIPTION
    before.friendly_name = FRIENDLY_NAME
    before.default_table_expiration_ms = 3600
    before.location = LOCATION
    before.labels = LABELS
    before.resource_tags = RESOURCE_TAGS
    before.default_rounding_mode = DEFAULT_ROUNDING_MODE
    after = client.create_dataset(before)
    assert after.dataset_id == DS_ID
    assert after.project == PROJECT
    assert after.etag == RESOURCE["etag"]
    assert after.full_dataset_id == RESOURCE["id"]
    assert after.description == DESCRIPTION
    assert after.friendly_name == FRIENDLY_NAME
    assert after.location == LOCATION
    assert after.default_table_expiration_ms == 3600
    assert after.labels == LABELS
    assert after.default_rounding_mode == DEFAULT_ROUNDING_MODE
    assert after.resource_tags == RESOURCE_TAGS

    conn.api_request.assert_called_once_with(
        method="POST",
        path="/%s" % PATH,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "description": DESCRIPTION,
            "friendlyName": FRIENDLY_NAME,
            "location": LOCATION,
            "defaultTableExpirationMs": "3600",
            "defaultRoundingMode": DEFAULT_ROUNDING_MODE,
            "access": [
                {"role": "OWNER", "userByEmail": USER_EMAIL},
                {"view": VIEW, "role": None},
            ],
            "labels": LABELS,
            "resourceTags": RESOURCE_TAGS,
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_w_custom_property(client, PROJECT, DS_ID):
    # The library should handle sending properties to the API that are not
    # yet part of the library

    path = "/projects/%s/datasets" % PROJECT
    resource = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "newAlphaProperty": "unreleased property",
    }
    conn = client._connection = make_connection(resource)

    ds_ref = DatasetReference(PROJECT, DS_ID)
    before = Dataset(ds_ref)
    before._properties["newAlphaProperty"] = "unreleased property"
    after = client.create_dataset(before)

    assert after.dataset_id == DS_ID
    assert after.project == PROJECT
    assert after._properties["newAlphaProperty"] == "unreleased property"

    conn.api_request.assert_called_once_with(
        method="POST",
        path=path,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "newAlphaProperty": "unreleased property",
            "labels": {},
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_w_client_location_wo_dataset_location(PROJECT, DS_ID, LOCATION):
    PATH = "projects/%s/datasets" % PROJECT
    RESOURCE = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "%s:%s" % (PROJECT, DS_ID),
        "location": LOCATION,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(RESOURCE)

    ds_ref = DatasetReference(PROJECT, DS_ID)
    before = Dataset(ds_ref)
    after = client.create_dataset(before)

    assert after.dataset_id == DS_ID
    assert after.project == PROJECT
    assert after.etag == RESOURCE["etag"]
    assert after.full_dataset_id == RESOURCE["id"]
    assert after.location == LOCATION

    conn.api_request.assert_called_once_with(
        method="POST",
        path="/%s" % PATH,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
            "location": LOCATION,
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_w_client_location_w_dataset_location(PROJECT, DS_ID, LOCATION):
    PATH = "projects/%s/datasets" % PROJECT
    OTHER_LOCATION = "EU"
    RESOURCE = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "%s:%s" % (PROJECT, DS_ID),
        "location": OTHER_LOCATION,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(RESOURCE)

    ds_ref = DatasetReference(PROJECT, DS_ID)
    before = Dataset(ds_ref)
    before.location = OTHER_LOCATION
    after = client.create_dataset(before)

    assert after.dataset_id == DS_ID
    assert after.project == PROJECT
    assert after.etag == RESOURCE["etag"]
    assert after.full_dataset_id == RESOURCE["id"]
    assert after.location == OTHER_LOCATION

    conn.api_request.assert_called_once_with(
        method="POST",
        path="/%s" % PATH,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
            "location": OTHER_LOCATION,
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_w_reference(PROJECT, DS_ID, LOCATION):
    path = "/projects/%s/datasets" % PROJECT
    resource = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "%s:%s" % (PROJECT, DS_ID),
        "location": LOCATION,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(resource)
    dataset = client.create_dataset(DatasetReference(PROJECT, DS_ID))

    assert dataset.dataset_id == DS_ID
    assert dataset.project == PROJECT
    assert dataset.etag == resource["etag"]
    assert dataset.full_dataset_id == resource["id"]
    assert dataset.location == LOCATION

    conn.api_request.assert_called_once_with(
        method="POST",
        path=path,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
            "location": LOCATION,
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_w_fully_qualified_string(PROJECT, DS_ID, LOCATION):
    path = "/projects/%s/datasets" % PROJECT
    resource = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "%s:%s" % (PROJECT, DS_ID),
        "location": LOCATION,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(resource)
    dataset = client.create_dataset("{}.{}".format(PROJECT, DS_ID))

    assert dataset.dataset_id == DS_ID
    assert dataset.project == PROJECT
    assert dataset.etag == resource["etag"]
    assert dataset.full_dataset_id == resource["id"]
    assert dataset.location == LOCATION

    conn.api_request.assert_called_once_with(
        method="POST",
        path=path,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
            "location": LOCATION,
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_w_string(PROJECT, DS_ID, LOCATION):
    path = "/projects/%s/datasets" % PROJECT
    resource = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "%s:%s" % (PROJECT, DS_ID),
        "location": LOCATION,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(resource)
    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        dataset = client.create_dataset(DS_ID)

    final_attributes.assert_called_once_with({"path": path}, client, None)

    assert dataset.dataset_id == DS_ID
    assert dataset.project == PROJECT
    assert dataset.etag == resource["etag"]
    assert dataset.full_dataset_id == resource["id"]
    assert dataset.location == LOCATION

    conn.api_request.assert_called_once_with(
        method="POST",
        path=path,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
            "location": LOCATION,
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_alreadyexists_w_exists_ok_false(PROJECT, DS_ID, LOCATION):
    client = make_client(location=LOCATION)
    client._connection = make_connection(
        google.api_core.exceptions.AlreadyExists("dataset already exists")
    )

    with pytest.raises(google.api_core.exceptions.AlreadyExists):
        client.create_dataset(DS_ID)


def test_create_dataset_alreadyexists_w_exists_ok_true(PROJECT, DS_ID, LOCATION):
    post_path = "/projects/{}/datasets".format(PROJECT)
    get_path = "/projects/{}/datasets/{}".format(PROJECT, DS_ID)
    resource = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "{}:{}".format(PROJECT, DS_ID),
        "location": LOCATION,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(
        google.api_core.exceptions.AlreadyExists("dataset already exists"), resource
    )
    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        dataset = client.create_dataset(DS_ID, exists_ok=True)

    final_attributes.assert_called_with({"path": get_path}, client, None)

    assert dataset.dataset_id == DS_ID
    assert dataset.project == PROJECT
    assert dataset.etag == resource["etag"]
    assert dataset.full_dataset_id == resource["id"]
    assert dataset.location == LOCATION

    conn.api_request.assert_has_calls(
        [
            mock.call(
                method="POST",
                path=post_path,
                data={
                    "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
                    "labels": {},
                    "location": LOCATION,
                },
                timeout=DEFAULT_TIMEOUT,
            ),
            mock.call(
                method="GET",
                path=get_path,
                timeout=DEFAULT_TIMEOUT,
                query_params={},
            ),
        ]
    )


def test_create_dataset_with_default_rounding_mode_if_value_is_none(
    PROJECT, DS_ID, LOCATION
):
    default_rounding_mode = None
    path = "/projects/%s/datasets" % PROJECT
    resource = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "{}:{}".format(PROJECT, DS_ID),
        "location": LOCATION,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(resource)

    ds_ref = DatasetReference(PROJECT, DS_ID)
    before = Dataset(ds_ref)
    before.default_rounding_mode = default_rounding_mode
    after = client.create_dataset(before)

    assert after.dataset_id == DS_ID
    assert after.project == PROJECT
    assert after.default_rounding_mode is None

    conn.api_request.assert_called_once_with(
        method="POST",
        path=path,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
            "location": LOCATION,
            "defaultRoundingMode": "ROUNDING_MODE_UNSPECIFIED",
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_with_default_rounding_mode_if_value_is_not_string(
    PROJECT, DS_ID, LOCATION
):
    default_rounding_mode = 10
    ds_ref = DatasetReference(PROJECT, DS_ID)
    dataset = Dataset(ds_ref)
    with pytest.raises(ValueError) as e:
        dataset.default_rounding_mode = default_rounding_mode
    assert str(e.value) == "Pass a string, or None"


def test_create_dataset_with_default_rounding_mode_if_value_is_not_in_possible_values(
    PROJECT, DS_ID
):
    default_rounding_mode = "ROUND_HALF_AWAY_FROM_ZEROS"
    ds_ref = DatasetReference(PROJECT, DS_ID)
    dataset = Dataset(ds_ref)
    with pytest.raises(ValueError) as e:
        dataset.default_rounding_mode = default_rounding_mode
    assert (
        str(e.value)
        == "rounding mode needs to be one of ROUNDING_MODE_UNSPECIFIED,ROUND_HALF_AWAY_FROM_ZERO,ROUND_HALF_EVEN"
    )


def test_create_dataset_with_default_rounding_mode_if_value_is_in_possible_values(
    PROJECT, DS_ID, LOCATION
):
    default_rounding_mode = "ROUND_HALF_AWAY_FROM_ZERO"
    path = "/projects/%s/datasets" % PROJECT
    resource = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "{}:{}".format(PROJECT, DS_ID),
        "location": LOCATION,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(resource)

    ds_ref = DatasetReference(PROJECT, DS_ID)
    before = Dataset(ds_ref)
    before.default_rounding_mode = default_rounding_mode
    after = client.create_dataset(before)

    assert after.dataset_id == DS_ID
    assert after.project == PROJECT
    assert after.default_rounding_mode is None

    conn.api_request.assert_called_once_with(
        method="POST",
        path=path,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
            "location": LOCATION,
            "defaultRoundingMode": default_rounding_mode,
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_with_max_time_travel_hours(PROJECT, DS_ID, LOCATION):
    path = "/projects/%s/datasets" % PROJECT
    max_time_travel_hours = 24 * 3

    resource = {
        "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
        "etag": "etag",
        "id": "{}:{}".format(PROJECT, DS_ID),
        "location": LOCATION,
        "maxTimeTravelHours": max_time_travel_hours,
    }
    client = make_client(location=LOCATION)
    conn = client._connection = make_connection(resource)

    ds_ref = DatasetReference(PROJECT, DS_ID)
    before = Dataset(ds_ref)
    before.max_time_travel_hours = max_time_travel_hours
    after = client.create_dataset(before)
    assert after.dataset_id == DS_ID
    assert after.project == PROJECT
    assert after.max_time_travel_hours == max_time_travel_hours

    conn.api_request.assert_called_once_with(
        method="POST",
        path=path,
        data={
            "datasetReference": {"projectId": PROJECT, "datasetId": DS_ID},
            "labels": {},
            "location": LOCATION,
            "maxTimeTravelHours": max_time_travel_hours,
        },
        timeout=DEFAULT_TIMEOUT,
    )


def test_create_dataset_with_max_time_travel_hours_not_multiple_of_24(
    PROJECT, DS_ID, LOCATION
):
    ds_ref = DatasetReference(PROJECT, DS_ID)
    dataset = Dataset(ds_ref)
    with pytest.raises(ValueError) as e:
        dataset.max_time_travel_hours = 50
    assert str(e.value) == "Time Travel Window should be multiple of 24"


def test_create_dataset_with_max_time_travel_hours_is_less_than_2_days(
    PROJECT, DS_ID, LOCATION
):
    ds_ref = DatasetReference(PROJECT, DS_ID)
    dataset = Dataset(ds_ref)
    with pytest.raises(ValueError) as e:
        dataset.max_time_travel_hours = 24
    assert (
        str(e.value)
        == "Time Travel Window should be from 48 to 168 hours (2 to 7 days)"
    )


def test_create_dataset_with_max_time_travel_hours_is_greater_than_7_days(
    PROJECT, DS_ID, LOCATION
):
    ds_ref = DatasetReference(PROJECT, DS_ID)
    dataset = Dataset(ds_ref)
    with pytest.raises(ValueError) as e:
        dataset.max_time_travel_hours = 192
    assert (
        str(e.value)
        == "Time Travel Window should be from 48 to 168 hours (2 to 7 days)"
    )


def test_create_dataset_with_max_time_travel_hours_is_not_int(PROJECT, DS_ID, LOCATION):
    ds_ref = DatasetReference(PROJECT, DS_ID)
    dataset = Dataset(ds_ref)
    with pytest.raises(ValueError) as e:
        dataset.max_time_travel_hours = "50"
    assert str(e.value) == "max_time_travel_hours must be an integer. Got 50"
