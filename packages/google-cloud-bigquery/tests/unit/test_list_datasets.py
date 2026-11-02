# Copyright 2021 Google LLC
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

from unittest import mock

import pytest

from google.cloud.bigquery.retry import DEFAULT_TIMEOUT
from .helpers import make_connection


@pytest.mark.parametrize(
    "extra,query", [({}, {}), (dict(page_size=42), dict(maxResults=42))]
)
def test_list_datasets_defaults(client, PROJECT, extra, query):
    from google.cloud.bigquery.dataset import DatasetListItem

    DATASET_1 = "dataset_one"
    DATASET_2 = "dataset_two"
    PATH = "projects/%s/datasets" % PROJECT
    TOKEN = "TOKEN"
    DATA = {
        "nextPageToken": TOKEN,
        "datasets": [
            {
                "kind": "bigquery#dataset",
                "id": "%s:%s" % (PROJECT, DATASET_1),
                "datasetReference": {"datasetId": DATASET_1, "projectId": PROJECT},
                "friendlyName": None,
            },
            {
                "kind": "bigquery#dataset",
                "id": "%s:%s" % (PROJECT, DATASET_2),
                "datasetReference": {"datasetId": DATASET_2, "projectId": PROJECT},
                "friendlyName": "Two",
            },
        ],
    }
    conn = client._connection = make_connection(DATA)

    iterator = client.list_datasets(**extra)
    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        page = next(iterator.pages)

    final_attributes.assert_called_once_with({"path": "/%s" % PATH}, client, None)
    datasets = list(page)
    token = iterator.next_page_token

    assert len(datasets) == len(DATA["datasets"])
    for found, expected in zip(datasets, DATA["datasets"]):
        assert isinstance(found, DatasetListItem)
        assert found.full_dataset_id == expected["id"]
        assert found.friendly_name == expected["friendlyName"]
    assert token == TOKEN

    conn.api_request.assert_called_once_with(
        method="GET", path="/%s" % PATH, query_params=query, timeout=DEFAULT_TIMEOUT
    )


def test_list_datasets_w_project_and_timeout(client, PROJECT):
    conn = client._connection = make_connection({})

    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        list(client.list_datasets(project="other-project", timeout=7.5))

    final_attributes.assert_called_once_with(
        {"path": "/projects/other-project/datasets"}, client, None
    )

    conn.api_request.assert_called_once_with(
        method="GET",
        path="/projects/other-project/datasets",
        query_params={},
        timeout=7.5,
    )


def test_list_datasets_explicit_response_missing_datasets_key(client, PROJECT):
    PATH = "projects/%s/datasets" % PROJECT
    TOKEN = "TOKEN"
    FILTER = "FILTER"
    DATA = {}
    conn = client._connection = make_connection(DATA)

    iterator = client.list_datasets(
        include_all=True, filter=FILTER, max_results=3, page_token=TOKEN
    )
    with mock.patch(
        "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
    ) as final_attributes:
        page = next(iterator.pages)

    final_attributes.assert_called_once_with({"path": "/%s" % PATH}, client, None)
    datasets = list(page)
    token = iterator.next_page_token

    assert len(datasets) == 0
    assert token is None

    conn.api_request.assert_called_once_with(
        method="GET",
        path="/%s" % PATH,
        query_params={
            "all": True,
            "filter": FILTER,
            "maxResults": 3,
            "pageToken": TOKEN,
        },
        timeout=DEFAULT_TIMEOUT,
    )
