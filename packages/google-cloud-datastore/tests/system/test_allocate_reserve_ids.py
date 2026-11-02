# Copyright 2011 Google LLC
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

import warnings

import pytest

from . import _helpers


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_allocate_ids(datastore_client, database_id):
    num_ids = 10
    allocated_keys = datastore_client.allocate_ids(
        datastore_client.key("Kind"),
        num_ids,
    )
    assert len(allocated_keys) == num_ids

    unique_ids = set()
    for key in allocated_keys:
        unique_ids.add(key.id)
        assert key.name is None
        assert key.id is not None

    assert len(unique_ids) == num_ids


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_reserve_ids_sequential(datastore_client, database_id):
    num_ids = 10
    key = datastore_client.key("Kind", 1234)

    # Smoke test to make sure it doesn't blow up. No return value or
    # verifiable side effect to verify.
    datastore_client.reserve_ids_sequential(key, num_ids)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_reserve_ids_deprecated(datastore_client, database_id):
    num_ids = 10
    key = datastore_client.key("Kind", 1234)

    with warnings.catch_warnings(record=True) as warned:
        datastore_client.reserve_ids(key, num_ids)

    assert len(warned) == 1
    assert warned[0].category is DeprecationWarning
    assert "reserve_ids_sequential" in str(warned[0].message)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_reserve_ids_multi(datastore_client, database_id):
    key1 = datastore_client.key("Kind", 1234)
    key2 = datastore_client.key("Kind", 1235)

    # Smoke test to make sure it doesn't blow up. No return value or
    # verifiable side effect to verify.
    datastore_client.reserve_ids_multi([key1, key2])
