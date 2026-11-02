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

from .helpers import make_connection, make_client, dataset_polymorphic
import google.api_core.exceptions
from google.cloud.bigquery.retry import DEFAULT_TIMEOUT
import pytest


@dataset_polymorphic
def test_delete_dataset(make_dataset, get_reference, client, PROJECT, DS_ID):
    dataset = make_dataset(PROJECT, DS_ID)
    PATH = "projects/%s/datasets/%s" % (PROJECT, DS_ID)
    conn = client._connection = make_connection({})
    client.delete_dataset(dataset, timeout=7.5)
    conn.api_request.assert_called_with(
        method="DELETE", path="/%s" % PATH, query_params={}, timeout=7.5
    )


@dataset_polymorphic
def test_delete_dataset_delete_contents(
    make_dataset, get_reference, client, PROJECT, DS_ID
):
    PATH = "projects/%s/datasets/%s" % (PROJECT, DS_ID)
    conn = client._connection = make_connection({})
    dataset = make_dataset(PROJECT, DS_ID)
    client.delete_dataset(dataset, delete_contents=True)
    conn.api_request.assert_called_with(
        method="DELETE",
        path="/%s" % PATH,
        query_params={"deleteContents": "true"},
        timeout=DEFAULT_TIMEOUT,
    )


def test_delete_dataset_wrong_type(client):
    with pytest.raises(TypeError):
        client.delete_dataset(42)


def test_delete_dataset_w_not_found_ok_false(PROJECT, DS_ID):
    path = "/projects/{}/datasets/{}".format(PROJECT, DS_ID)
    http = object()
    client = make_client(_http=http)
    conn = client._connection = make_connection(
        google.api_core.exceptions.NotFound("dataset not found")
    )

    with pytest.raises(google.api_core.exceptions.NotFound):
        client.delete_dataset(DS_ID)

    conn.api_request.assert_called_with(
        method="DELETE", path=path, query_params={}, timeout=DEFAULT_TIMEOUT
    )


def test_delete_dataset_w_not_found_ok_true(PROJECT, DS_ID):
    path = "/projects/{}/datasets/{}".format(PROJECT, DS_ID)
    http = object()
    client = make_client(_http=http)
    conn = client._connection = make_connection(
        google.api_core.exceptions.NotFound("dataset not found")
    )
    client.delete_dataset(DS_ID, not_found_ok=True)
    conn.api_request.assert_called_with(
        method="DELETE", path=path, query_params={}, timeout=DEFAULT_TIMEOUT
    )
