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


def test_list_routines_empty_w_timeout(client):
    conn = client._connection = make_connection({})

    iterator = client.list_routines("test-routines.test_routines", timeout=7.5)
    page = next(iterator.pages)
    routines = list(page)
    token = iterator.next_page_token

    assert routines == []
    assert token is None
    conn.api_request.assert_called_once_with(
        method="GET",
        path="/projects/test-routines/datasets/test_routines/routines",
        query_params={},
        timeout=7.5,
    )


@pytest.mark.parametrize(
    "extra,query", [({}, {}), (dict(page_size=42), dict(maxResults=42))]
)
@dataset_polymorphic
def test_list_routines_defaults(
    make_dataset, get_reference, client, PROJECT, extra, query
):
    from google.cloud.bigquery.routine import Routine

    project_id = PROJECT
    dataset_id = "test_routines"
    path = f"/projects/{PROJECT}/datasets/test_routines/routines"
    routine_1 = "routine_one"
    routine_2 = "routine_two"
    token = "TOKEN"
    resource = {
        "nextPageToken": token,
        "routines": [
            {
                "routineReference": {
                    "routineId": routine_1,
                    "datasetId": dataset_id,
                    "projectId": project_id,
                }
            },
            {
                "routineReference": {
                    "routineId": routine_2,
                    "datasetId": dataset_id,
                    "projectId": project_id,
                }
            },
        ],
    }

    conn = client._connection = make_connection(resource)
    dataset = make_dataset(client.project, dataset_id)

    iterator = client.list_routines(dataset, **extra)
    assert iterator.dataset == get_reference(dataset)
    page = next(iterator.pages)
    routines = list(page)
    actual_token = iterator.next_page_token

    assert len(routines) == len(resource["routines"])
    for found, expected in zip(routines, resource["routines"]):
        assert isinstance(found, Routine)
        assert found.routine_id == expected["routineReference"]["routineId"]
    assert actual_token == token

    conn.api_request.assert_called_once_with(
        method="GET", path=path, query_params=query, timeout=DEFAULT_TIMEOUT
    )


def test_list_routines_wrong_type(client):
    with pytest.raises(TypeError):
        client.list_routines(42)
