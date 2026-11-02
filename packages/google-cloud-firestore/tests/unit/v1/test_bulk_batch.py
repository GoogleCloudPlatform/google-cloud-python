# Copyright 2021 Google LLC All rights reserved.
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

import mock


def _make_bulk_write_batch(*args, **kwargs):
    from google.cloud.firestore_v1.bulk_batch import BulkWriteBatch

    return BulkWriteBatch(*args, **kwargs)


def test_bulkwritebatch_ctor():
    batch = _make_bulk_write_batch(mock.sentinel.client)
    assert batch._client is mock.sentinel.client
    assert batch._write_pbs == []
    assert batch.write_results is None


def _write_helper(retry=None, timeout=None):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import firestore, write

    # Create a minimal fake GAPIC with a dummy result.
    firestore_api = mock.Mock(spec=["batch_write"])
    write_response = firestore.BatchWriteResponse(
        write_results=[write.WriteResult(), write.WriteResult()],
    )
    firestore_api.batch_write.return_value = write_response
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Attach the fake GAPIC to a real client.
    client = _make_client("grand")
    client._firestore_api_internal = firestore_api

    # Actually make a batch with some mutations and call commit().
    batch = _make_bulk_write_batch(client)
    document1 = client.document("a", "b")
    assert document1 not in batch
    batch.create(document1, {"ten": 10, "buck": "ets"})
    assert document1 in batch
    document2 = client.document("c", "d", "e", "f")
    batch.delete(document2)
    write_pbs = batch._write_pbs[::]

    resp = batch.commit(**kwargs)
    assert resp.write_results == list(write_response.write_results)
    assert batch.write_results == resp.write_results
    # Make sure batch has no more "changes".
    assert batch._write_pbs == []

    # Verify the mocks.
    firestore_api.batch_write.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": write_pbs,
            "labels": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


def test_bulkwritebatch_write():
    _write_helper()


def test_bulkwritebatch_write_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0

    _write_helper(retry=retry, timeout=timeout)


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_client(project="seventy-nine"):
    from google.cloud.firestore_v1.client import Client

    credentials = _make_credentials()
    return Client(project=project, credentials=credentials)
