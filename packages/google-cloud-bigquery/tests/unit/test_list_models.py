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

import pytest

from google.cloud.bigquery.retry import DEFAULT_TIMEOUT
from .helpers import make_connection, dataset_polymorphic


def test_list_models_empty_w_timeout(client, PROJECT, DS_ID):
    path = "/projects/{}/datasets/{}/models".format(PROJECT, DS_ID)
    conn = client._connection = make_connection({})

    dataset_id = "{}.{}".format(PROJECT, DS_ID)
    iterator = client.list_models(dataset_id, timeout=7.5)
    page = next(iterator.pages)
    models = list(page)
    token = iterator.next_page_token

    assert models == []
    assert token is None
    conn.api_request.assert_called_once_with(
        method="GET", path=path, query_params={}, timeout=7.5
    )


@pytest.mark.parametrize(
    "extra,query", [({}, {}), (dict(page_size=42), dict(maxResults=42))]
)
@dataset_polymorphic
def test_list_models_defaults(
    make_dataset,
    get_reference,
    client,
    PROJECT,
    DS_ID,
    extra,
    query,
):
    from google.cloud.bigquery.model import Model

    MODEL_1 = "model_one"
    MODEL_2 = "model_two"
    PATH = "projects/%s/datasets/%s/models" % (PROJECT, DS_ID)
    TOKEN = "TOKEN"
    DATA = {
        "nextPageToken": TOKEN,
        "models": [
            {
                "modelReference": {
                    "modelId": MODEL_1,
                    "datasetId": DS_ID,
                    "projectId": PROJECT,
                }
            },
            {
                "modelReference": {
                    "modelId": MODEL_2,
                    "datasetId": DS_ID,
                    "projectId": PROJECT,
                }
            },
        ],
    }

    conn = client._connection = make_connection(DATA)
    dataset = make_dataset(PROJECT, DS_ID)

    iterator = client.list_models(dataset, **extra)
    assert iterator.dataset == get_reference(dataset)
    page = next(iterator.pages)
    models = list(page)
    token = iterator.next_page_token

    assert len(models) == len(DATA["models"])
    for found, expected in zip(models, DATA["models"]):
        assert isinstance(found, Model)
        assert found.model_id == expected["modelReference"]["modelId"]
    assert token == TOKEN

    conn.api_request.assert_called_once_with(
        method="GET", path="/%s" % PATH, query_params=query, timeout=DEFAULT_TIMEOUT
    )


def test_list_models_wrong_type(client):
    with pytest.raises(TypeError):
        client.list_models(42)
