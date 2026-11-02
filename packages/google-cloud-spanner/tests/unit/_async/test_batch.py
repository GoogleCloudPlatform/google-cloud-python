# Copyright 2024 Google LLC All rights reserved.
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

import datetime
import unittest
from datetime import timezone
from unittest import mock

from google.cloud._helpers import UTC, _datetime_to_pb_timestamp

from google.cloud.spanner_v1 import (
    BatchWriteResponse,
    CommitResponse,
    RequestOptions,
    TransactionOptions,
)
from google.cloud.spanner_v1._async.batch import Batch, MutationGroups, _BatchBase
from google.cloud.spanner_v1._helpers import _make_list_value_pb, _make_value_pb
from google.cloud.spanner_v1.keyset import KeySet

TABLE_NAME = "citizens"
COLUMNS = ["email", "first_name", "last_name", "age"]
VALUES = [
    ["phred@exammple.com", "Phred", "Phlyntstone", 32],
    ["bharney@example.com", "Bharney", "Rhubble", 31],
]


class Test_BatchBase(unittest.IsolatedAsyncioTestCase):
    def _getTargetClass(self):
        return _BatchBase

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_ctor(self):
        session = mock.Mock()
        base = self._make_one(session)
        self.assertIs(base._session, session)
        self.assertEqual(len(base._mutations), 0)

    def test_resource_info_with_database(self):
        session = mock.Mock()
        mock_db = mock.Mock(spec=["_resource_info"])
        mock_db._resource_info = {"project": "p", "instance": "i", "database": "d"}
        session._database = mock_db
        base = self._make_one(session)
        self.assertEqual(base._resource_info, mock_db._resource_info)

    def test_resource_info_fallback(self):
        session = mock.Mock()
        mock_db = mock.Mock(spec=["_instance", "database_id"])
        mock_db._instance = mock.Mock(spec=["_client", "instance_id"])
        mock_db._instance.instance_id = "i"
        mock_db._instance._client = mock.Mock(spec=["project"])
        mock_db._instance._client.project = "p"
        mock_db.database_id = "d"
        session._database = mock_db
        base = self._make_one(session)
        self.assertEqual(
            base._resource_info,
            {"project": "p", "instance": "i", "database": "d"},
        )

    def test_resource_info_none(self):
        base = self._make_one(None)
        self.assertIsNone(base._resource_info)

    def test_insert(self):
        session = mock.Mock()
        base = self._make_one(session)
        base.insert(TABLE_NAME, columns=COLUMNS, values=VALUES)
        self.assertEqual(len(base._mutations), 1)
        self.assertTrue(base._mutations[0].insert.table == TABLE_NAME)

    def test_update(self):
        session = mock.Mock()
        base = self._make_one(session)
        base.update(TABLE_NAME, columns=COLUMNS, values=VALUES)
        self.assertEqual(len(base._mutations), 1)
        self.assertTrue(base._mutations[0].update.table == TABLE_NAME)

    def test_insert_or_update(self):
        session = mock.Mock()
        base = self._make_one(session)
        base.insert_or_update(TABLE_NAME, columns=COLUMNS, values=VALUES)
        self.assertEqual(len(base._mutations), 1)
        self.assertTrue(base._mutations[0].insert_or_update.table == TABLE_NAME)

    def test_replace(self):
        session = mock.Mock()
        base = self._make_one(session)
        base.replace(TABLE_NAME, columns=COLUMNS, values=VALUES)
        self.assertEqual(len(base._mutations), 1)
        self.assertTrue(base._mutations[0].replace.table == TABLE_NAME)

    def test_delete(self):
        keyset = KeySet(keys=[[0]])
        session = mock.Mock()
        base = self._make_one(session)
        base.delete(TABLE_NAME, keyset=keyset)
        self.assertEqual(len(base._mutations), 1)
        self.assertEqual(base._mutations[0].delete.table, TABLE_NAME)

    def test_send(self):
        queue = "TestQueue"
        key = [2]
        payload = "Hello, Queues!"
        session = mock.Mock()
        base = self._make_one(session)
        base.send(queue=queue, key=key, payload=payload)
        self.assertEqual(len(base._mutations), 1)
        self.assertEqual(base._mutations[0].send.queue, queue)
        self.assertEqual(base._mutations[0].send._pb.payload, _make_value_pb(payload))
        self.assertEqual(base._mutations[0].send._pb.key, _make_list_value_pb(key))

    def test_ack(self):
        queue = "TestQueue"
        key = [2]
        session = mock.Mock()
        base = self._make_one(session)
        base.ack(queue=queue, key=key)
        self.assertEqual(len(base._mutations), 1)
        self.assertEqual(base._mutations[0].ack.queue, queue)
        self.assertEqual(base._mutations[0].ack._pb.key, _make_list_value_pb(key))


class TestBatch(unittest.IsolatedAsyncioTestCase):
    def _getTargetClass(self):
        return Batch

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _make_session(self):
        database = mock.Mock()
        database.name = "db_name"
        database.spanner_api = mock.AsyncMock()
        database.default_transaction_options = mock.Mock()
        database.default_transaction_options.default_read_write_transaction_options = (
            TransactionOptions()
        )
        database.with_error_augmentation.return_value = ([], mock.MagicMock())
        database._route_to_leader_enabled = True

        session = mock.Mock()
        session._database = database
        session.name = "session_name"

        # Mock the hierarchy for _client_context
        # Use a real ClientContext or None
        session._database._instance._client._client_context = None

        return session

    async def test_commit_already_committed(self):
        session = self._make_session()
        batch = self._make_one(session)
        batch.committed = object()
        with self.assertRaises(ValueError):
            await batch.commit()

    async def test_commit_ok(self):
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)

        session = self._make_session()
        session._database.spanner_api.commit.return_value = response

        batch = self._make_one(session)
        batch.insert(TABLE_NAME, COLUMNS, VALUES)

        committed = await batch.commit()
        self.assertEqual(committed, now)
        self.assertEqual(batch.committed, committed)

    async def test_commit_w_options(self):
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)

        session = self._make_session()
        # Mock with_error_augmentation to return (metadata, mock_context_manager)
        session._database.with_error_augmentation.return_value = ([], mock.MagicMock())
        session._database.spanner_api.commit.return_value = response

        batch = self._make_one(session)
        ro = {"priority": RequestOptions.Priority.PRIORITY_HIGH}
        await batch.commit(
            request_options=ro, max_commit_delay=datetime.timedelta(milliseconds=100)
        )

        self.assertTrue(session._database.spanner_api.commit.called)
        call_args = session._database.spanner_api.commit.call_args
        self.assertEqual(
            call_args.kwargs["request"].request_options.priority,
            RequestOptions.Priority.PRIORITY_HIGH,
        )

    async def test_commit_route_leader_disabled(self):
        # coverage for line 231 (else branch)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)

        session = self._make_session()
        session._database._route_to_leader_enabled = False
        session._database.spanner_api.commit.return_value = response

        batch = self._make_one(session)
        await batch.commit()

        self.assertTrue(session._database.spanner_api.commit.called)

    async def test_context_mgr_success(self):
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)

        session = self._make_session()
        session._database.with_error_augmentation.return_value = ([], mock.MagicMock())
        session._database.spanner_api.commit.return_value = response

        batch = self._make_one(session)
        async with batch:
            batch.insert(TABLE_NAME, COLUMNS, VALUES)

        self.assertEqual(batch.committed, now)

    async def test_context_mgr_failure(self):
        session = self._make_session()
        batch = self._make_one(session)

        class _BailOut(Exception):
            pass

        with self.assertRaises(_BailOut):
            async with batch:
                raise _BailOut()

        self.assertIsNone(batch.committed)

    async def test_context_mgr_already_committed(self):
        batch = self._make_one(self._make_session())
        batch.committed = object()
        with self.assertRaises(ValueError):
            async with batch:
                pass


class TestMutationGroups(unittest.IsolatedAsyncioTestCase):
    def _getTargetClass(self):
        return MutationGroups

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _make_session(self):
        database = mock.Mock()
        database.name = "db_name"
        database.spanner_api = mock.AsyncMock()
        database._route_to_leader_enabled = True
        database.metadata_with_request_id.return_value = []

        session = mock.Mock()
        session._database = database
        session.name = "session_name"

        # Mock the hierarchy for _client_context
        session._database._instance._client._client_context = None
        session._database._instance._client.project = "project"
        session._database._instance.instance_id = "instance"
        session._database.database_id = "database"

        return session

    def test_resource_info_with_database(self):
        session = mock.Mock()
        mock_db = mock.Mock(spec=["_resource_info"])
        mock_db._resource_info = {"project": "p", "instance": "i", "database": "d"}
        session._database = mock_db
        groups = self._make_one(session)
        self.assertEqual(groups._resource_info, mock_db._resource_info)

    def test_resource_info_fallback(self):
        session = mock.Mock()
        mock_db = mock.Mock(spec=["_instance", "database_id"])
        mock_db._instance = mock.Mock(spec=["_client", "instance_id"])
        mock_db._instance.instance_id = "i"
        mock_db._instance._client = mock.Mock(spec=["project"])
        mock_db._instance._client.project = "p"
        mock_db.database_id = "d"
        session._database = mock_db
        groups = self._make_one(session)
        self.assertEqual(
            groups._resource_info,
            {"project": "p", "instance": "i", "database": "d"},
        )

    def test_resource_info_none(self):
        groups = self._make_one(None)
        self.assertIsNone(groups._resource_info)

    async def test_batch_write_ok(self):
        session = self._make_session()

        from google.rpc.status_pb2 import Status

        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = BatchWriteResponse(
            commit_timestamp=now_pb, indexes=[0], status=Status(code=0)
        )

        # mock list of responses
        session._database.spanner_api.batch_write.return_value = [response]

        groups = self._make_one(session)
        group = groups.group()
        group.insert(TABLE_NAME, COLUMNS, VALUES)

        res_iter = await groups.batch_write()
        self.assertEqual(len(res_iter), 1)
        self.assertEqual(res_iter[0], response)
        self.assertTrue(groups.committed)

    async def test_batch_write_already_committed(self):
        groups = self._make_one(self._make_session())
        groups.committed = True
        with self.assertRaises(ValueError):
            await groups.batch_write()

    async def test_batch_write_w_options(self):
        session = self._make_session()
        session._database.spanner_api.batch_write.return_value = []

        groups = self._make_one(session)
        ro = {"priority": RequestOptions.Priority.PRIORITY_LOW}
        await groups.batch_write(
            request_options=ro, exclude_txn_from_change_streams=True
        )

        self.assertTrue(session._database.spanner_api.batch_write.called)
        call_args = session._database.spanner_api.batch_write.call_args
        # RequestOptions is built from dict
        self.assertEqual(
            call_args.kwargs["request"].request_options.priority,
            RequestOptions.Priority.PRIORITY_LOW,
        )
        self.assertTrue(call_args.kwargs["request"].exclude_txn_from_change_streams)

    async def test_batch_write_route_leader_disabled(self):
        # coverage for line 402 (else branch)
        session = self._make_session()
        session._database._route_to_leader_enabled = False
        session._database.spanner_api.batch_write.return_value = []

        groups = self._make_one(session)
        await groups.batch_write()

        self.assertTrue(session._database.spanner_api.batch_write.called)

    async def test_batch_write_w_invalid_options(self):
        groups = self._make_one(self._make_session())
        with self.assertRaises(ValueError):
            await groups.batch_write(request_options={"invalid": 1})
