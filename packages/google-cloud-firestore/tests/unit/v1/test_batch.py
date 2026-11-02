# Copyright 2017 Google LLC All rights reserved.
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
import pytest


def _make_write_batch(*args, **kwargs):
    from google.cloud.firestore_v1.batch import WriteBatch

    return WriteBatch(*args, **kwargs)


def test_writebatch_ctor():
    batch = _make_write_batch(mock.sentinel.client)
    assert batch._client is mock.sentinel.client
    assert batch._write_pbs == []
    assert batch.write_results is None
    assert batch.commit_time is None


def _commit_helper(retry=None, timeout=None):
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import firestore, write

    # Create a minimal fake GAPIC with a dummy result.
    firestore_api = mock.Mock(spec=["commit"])
    timestamp = timestamp_pb2.Timestamp(seconds=1234567, nanos=123456798)
    commit_response = firestore.CommitResponse(
        write_results=[write.WriteResult(), write.WriteResult()],
        commit_time=timestamp,
    )
    firestore_api.commit.return_value = commit_response
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Attach the fake GAPIC to a real client.
    client = _make_client("grand")
    client._firestore_api_internal = firestore_api

    # Actually make a batch with some mutations and call commit().
    batch = _make_write_batch(client)
    document1 = client.document("a", "b")
    batch.create(document1, {"ten": 10, "buck": "ets"})
    document2 = client.document("c", "d", "e", "f")
    batch.delete(document2)
    assert len(batch) == 2
    write_pbs = batch._write_pbs[::]

    write_results = batch.commit(**kwargs)
    assert write_results == list(commit_response.write_results)
    assert batch.write_results == write_results
    assert batch.commit_time.timestamp_pb() == timestamp
    # Make sure batch has no more "changes".
    assert batch._write_pbs == []

    # Verify the mocks.
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": write_pbs,
            "transaction": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


def test_writebatch_commit():
    _commit_helper()


def test_writebatch_commit_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0

    _commit_helper(retry=retry, timeout=timeout)


def test_writebatch_as_context_mgr_wo_error():
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1.types import firestore, write

    firestore_api = mock.Mock(spec=["commit"])
    timestamp = timestamp_pb2.Timestamp(seconds=1234567, nanos=123456798)
    commit_response = firestore.CommitResponse(
        write_results=[write.WriteResult(), write.WriteResult()],
        commit_time=timestamp,
    )
    firestore_api.commit.return_value = commit_response
    client = _make_client()
    client._firestore_api_internal = firestore_api
    batch = _make_write_batch(client)
    document1 = client.document("a", "b")
    document2 = client.document("c", "d", "e", "f")

    with batch as ctx_mgr:
        assert ctx_mgr is batch
        ctx_mgr.create(document1, {"ten": 10, "buck": "ets"})
        ctx_mgr.delete(document2)
        write_pbs = batch._write_pbs[::]

    assert batch.write_results == list(commit_response.write_results)
    assert batch.commit_time.timestamp_pb() == timestamp
    # Make sure batch has no more "changes".
    assert batch._write_pbs == []

    # Verify the mocks.
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": write_pbs,
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


def test_writebatch_as_context_mgr_w_error():
    firestore_api = mock.Mock(spec=["commit"])
    client = _make_client()
    client._firestore_api_internal = firestore_api
    batch = _make_write_batch(client)
    document1 = client.document("a", "b")
    document2 = client.document("c", "d", "e", "f")

    with pytest.raises(RuntimeError):
        with batch as ctx_mgr:
            ctx_mgr.create(document1, {"ten": 10, "buck": "ets"})
            ctx_mgr.delete(document2)
            raise RuntimeError("testing")

    # batch still has its changes, as _exit_ (and commit) is not invoked
    # changes are preserved so commit can be retried
    assert batch.write_results is None
    assert batch.commit_time is None
    assert len(batch._write_pbs) == 2

    firestore_api.commit.assert_not_called()


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_client(project="seventy-nine"):
    from google.cloud.firestore_v1.client import Client

    credentials = _make_credentials()
    return Client(project=project, credentials=credentials)
