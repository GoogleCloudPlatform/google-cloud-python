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

import pytest
from google.cloud.exceptions import Conflict

from google.cloud import datastore

from . import _helpers


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_transaction_via_with_statement(
    datastore_client, entities_to_delete, database_id
):
    key = datastore_client.key("Company", "Google")
    entity = datastore.Entity(key=key)
    entity["url"] = "www.google.com"

    with datastore_client.transaction() as xact:
        result = datastore_client.get(entity.key)
        if result is None:
            xact.put(entity)
            entities_to_delete.append(entity)

    # This will always return after the transaction.
    retrieved_entity = datastore_client.get(key)

    entities_to_delete.append(retrieved_entity)
    assert retrieved_entity == entity


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
@pytest.mark.parametrize("first_call", ["get", "put", "delete"])
def test_transaction_begin_later(
    datastore_client, entities_to_delete, database_id, first_call
):
    """
    transactions with begin_later should call begin on first get rpc, or on commit
    """
    key = datastore_client.key("Company", "Google")
    entity = datastore.Entity(key=key)
    entity["url"] = "www.google.com"

    datastore_client.put(entity)
    result_entity = datastore_client.get(key)

    with datastore_client.transaction(begin_later=True) as xact:
        assert xact._id is None
        assert xact._status == xact._INITIAL
        if first_call == "get":
            datastore_client.get(entity.key)
            assert xact._status == xact._IN_PROGRESS
            assert xact._id is not None
        elif first_call == "put":
            xact.put(entity)
            assert xact._status == xact._INITIAL
        elif first_call == "delete":
            xact.delete(result_entity.key)
            assert xact._status == xact._INITIAL
    assert xact._status == xact._FINISHED

    entities_to_delete.append(result_entity)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
@pytest.mark.parametrize("raise_exception", [True, False])
def test_transaction_begin_later_noop(datastore_client, database_id, raise_exception):
    """
    empty begin later transactions should terminate quietly
    """
    try:
        with datastore_client.transaction(begin_later=True) as xact:
            assert xact._id is None
            assert xact._status == xact._INITIAL
            if raise_exception:
                raise RuntimeError("test")
    except RuntimeError:
        pass
    assert xact._status == xact._ABORTED
    assert xact._id is None


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_transaction_via_explicit_begin_get_commit(
    datastore_client, entities_to_delete, database_id
):
    # See
    # github.com/GoogleCloudPlatform/google-cloud-python/issues/1859
    # Note that this example lacks the threading which provokes the race
    # condition in that issue:  we are basically just exercising the
    # "explicit" path for using transactions.
    before_1 = 100
    before_2 = 0
    transfer_amount = 40

    key1 = datastore_client.key("account", "123")
    account1 = datastore.Entity(key=key1)
    account1["balance"] = before_1

    key2 = datastore_client.key("account", "234")
    account2 = datastore.Entity(key=key2)
    account2["balance"] = before_2

    datastore_client.put_multi([account1, account2])
    entities_to_delete.append(account1)
    entities_to_delete.append(account2)

    xact = datastore_client.transaction()
    xact.begin()
    from_account = datastore_client.get(key1, transaction=xact)
    to_account = datastore_client.get(key2, transaction=xact)
    from_account["balance"] -= transfer_amount
    to_account["balance"] += transfer_amount

    xact.put(from_account)
    xact.put(to_account)
    xact.commit()

    after1 = datastore_client.get(key1)
    after2 = datastore_client.get(key2)
    assert after1["balance"] == before_1 - transfer_amount
    assert after2["balance"] == before_2 + transfer_amount


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_failure_with_contention(datastore_client, entities_to_delete, database_id):
    contention_prop_name = "baz"
    local_client = _helpers.clone_client(datastore_client)

    # Insert an entity which will be retrieved in a transaction
    # and updated outside it with a contentious value.
    key = local_client.key("BreakTxn", 1234)
    orig_entity = datastore.Entity(key=key)
    orig_entity["foo"] = "bar"
    local_client.put(orig_entity)

    entities_to_delete.append(orig_entity)

    with local_client.transaction() as txn:
        entity_in_txn = local_client.get(key)

        # Update the original entity outside the transaction.
        orig_entity[contention_prop_name] = "outside"
        with pytest.raises(Conflict):
            datastore_client.put(orig_entity)

        # Try to update the entity which we already updated outside the
        # transaction.
        entity_in_txn[contention_prop_name] = "inside"
        txn.put(entity_in_txn)
    # now that transaction is complete, should be able to update outside
    datastore_client.put(orig_entity)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_failure_with_contention_no_context_manager(
    datastore_client, entities_to_delete, database_id
):
    contention_prop_name = "baz"
    local_client = _helpers.clone_client(datastore_client)

    # Insert an entity which will be retrieved in a transaction
    # and updated outside it with a contentious value.
    key = local_client.key("BreakTxnCM3", 1234)
    orig_entity = datastore.Entity(key=key)
    orig_entity["foo"] = "bar"
    local_client.put(orig_entity)

    entities_to_delete.append(orig_entity)

    txn = local_client.transaction()
    txn.begin()

    entity_in_txn = local_client.get(key, transaction=txn)

    # Update the original entity outside the transaction.
    # should fail due to contention
    orig_entity[contention_prop_name] = "outside"
    with pytest.raises(Conflict):
        datastore_client.put(orig_entity)

    # Try to update the entity inside the transaction
    entity_in_txn[contention_prop_name] = "inside"
    txn.put(entity_in_txn)
    txn.commit()

    # now that transaction is complete, should be able to update outside
    datastore_client.put(orig_entity)
