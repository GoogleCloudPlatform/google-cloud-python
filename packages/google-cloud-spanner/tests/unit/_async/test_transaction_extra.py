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

import unittest
from unittest import mock

from google.cloud.spanner_v1._async.transaction import Transaction
from google.cloud.spanner_v1._helpers import _make_value_pb
from google.cloud.spanner_v1.types import Mutation, RequestOptions, TransactionOptions


class TestTransactionExtra(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.db = mock.MagicMock()
        self.db.name = "projects/p/instances/i/databases/d"
        self.db.spanner_api = mock.AsyncMock()
        self.db._route_to_leader_enabled = True
        self.db._instance._client._query_options = None
        self.db._instance._client._client_context = None

        self.db.with_error_augmentation.return_value = ([], mock.MagicMock())
        self.db._next_nth_request = 1
        self.db._channel_id = 1

        self.session = mock.MagicMock()
        self.session._database = self.db
        self.session.name = "projects/p/instances/i/databases/d/sessions/s"
        self.session.is_multiplexed = False
        self.session.default_transaction_options = None

    async def test_execute_request_already_committed(self):
        # coverage for line 133
        txn = Transaction(self.session)
        txn.committed = object()
        with self.assertRaisesRegex(ValueError, "Transaction already committed"):
            await txn._execute_request(None, None, None)

    async def test_execute_request_already_rolled_back(self):
        # coverage for line 135
        txn = Transaction(self.session)
        txn.rolled_back = True
        with self.assertRaisesRegex(ValueError, "Transaction already rolled back"):
            await txn._execute_request(None, None, None)

    async def test_rollback_already_committed(self):
        # coverage for line 166
        txn = Transaction(self.session)
        txn.committed = object()
        with self.assertRaisesRegex(ValueError, "Transaction already committed"):
            await txn.rollback()

    async def test_rollback_already_rolled_back(self):
        # coverage for line 168
        txn = Transaction(self.session)
        txn.rolled_back = True
        with self.assertRaisesRegex(ValueError, "Transaction already rolled back"):
            await txn.rollback()

    async def test_rollback_with_route_to_leader(self):
        # coverage for lines 176-181
        txn = Transaction(self.session)
        txn._transaction_id = b"tid"
        self.db._route_to_leader_enabled = True
        self.db.spanner_api.rollback = mock.AsyncMock()

        await txn.rollback()
        self.assertTrue(self.db.spanner_api.rollback.called)

    async def test_commit_already_committed_or_rolled_back(self):
        # coverage for lines 267, 269
        txn = Transaction(self.session)
        txn.committed = object()
        with self.assertRaisesRegex(ValueError, "Transaction already committed"):
            await txn.commit()

        txn = Transaction(self.session)
        txn.rolled_back = True
        with self.assertRaisesRegex(ValueError, "Transaction already rolled back"):
            await txn.commit()

    async def test_commit_mutations_only_not_begun(self):
        # coverage for line 274
        txn = Transaction(self.session)
        # No mutations, no _transaction_id
        with self.assertRaisesRegex(ValueError, "Transaction has not begun"):
            await txn.commit()

    async def test_commit_with_request_options_dict(self):
        # coverage for lines 279, 281-284
        txn = Transaction(self.session)
        txn._transaction_id = b"tid"

        resp = mock.MagicMock()
        resp._pb.HasField.return_value = False
        self.db.spanner_api.commit = mock.AsyncMock(return_value=resp)

        ro = {"priority": RequestOptions.Priority.PRIORITY_HIGH}
        await txn.commit(request_options=ro)
        self.assertTrue(self.db.spanner_api.commit.called)

    async def test_commit_retry_and_precommit_token(self):
        # coverage for lines 332-339 (before_next_retry) and 351-367 (precommit_token)
        from google.api_core.exceptions import InternalServerError

        from google.cloud.spanner_v1.types import MultiplexedSessionPrecommitToken

        txn = Transaction(self.session)
        txn._transaction_id = b"tid"

        # Mock commit response with precommit_token
        token_pb = MultiplexedSessionPrecommitToken(precommit_token=b"token", seq_num=1)
        resp_with_token = mock.MagicMock()
        resp_with_token.precommit_token = token_pb
        # Sequence of HasField calls: first False (for initial commit), then True (to enter precommit retry block), then False (for final)
        resp_with_token._pb.HasField.return_value = True

        final_resp = mock.MagicMock()
        final_resp.commit_timestamp = object()
        final_resp._pb.HasField.return_value = False

        self.db.spanner_api.commit.side_effect = [
            InternalServerError("RST_STREAM"),
            resp_with_token,
            final_resp,
        ]

        with mock.patch(
            "google.cloud.spanner_v1._async._helpers.asyncio.sleep"
        ) as sleep_mock:
            await txn.commit()

        self.assertEqual(self.db.spanner_api.commit.call_count, 3)
        sleep_mock.assert_called_once_with(2)

    async def test_execute_update_request_options_dict(self):
        # coverage for line 503
        from google.cloud.spanner_v1.types import MultiplexedSessionPrecommitToken

        txn = Transaction(self.session)
        txn._transaction_id = b"tid"
        txn._precommit_token = MultiplexedSessionPrecommitToken(seq_num=0)

        resp = mock.MagicMock()
        token_pb = MultiplexedSessionPrecommitToken(seq_num=1)
        resp.precommit_token = token_pb
        resp.metadata.transaction.precommit_token = token_pb
        # Avoid issues with result_set_pb.metadata.transaction unpacking if any
        resp.metadata.transaction.id = b"tid"
        resp._pb.HasField.return_value = True
        self.db.spanner_api.execute_sql = mock.AsyncMock(return_value=resp)

        ro = {"priority": RequestOptions.Priority.PRIORITY_HIGH}
        await txn.execute_update("UPDATE t SET c=1", request_options=ro)
        self.assertTrue(self.db.spanner_api.execute_sql.called)

        # branch for request_options is None
        await txn.execute_update("UPDATE t SET c=1", request_options=None)

    async def test_batch_update_request_options_dict(self):
        # coverage for line 657
        txn = Transaction(self.session)
        txn._transaction_id = b"tid"

        resp = mock.MagicMock()
        self.db.spanner_api.execute_batch_dml = mock.AsyncMock(return_value=resp)

        ro = {"priority": RequestOptions.Priority.PRIORITY_HIGH}
        await txn.batch_update(["UPDATE t SET c=1"], request_options=ro)
        self.assertTrue(self.db.spanner_api.execute_batch_dml.called)

        # branch for request_options is None
        await txn.batch_update(["UPDATE t SET c=1"], request_options=None)

    async def test_begin_transaction_already_committed_or_rolled_back(self):
        # coverage for lines 748, 750
        txn = Transaction(self.session)
        txn.committed = object()
        with self.assertRaisesRegex(ValueError, "Transaction is already committed"):
            await txn._begin_transaction()

        txn = Transaction(self.session)
        txn.rolled_back = True
        with self.assertRaisesRegex(ValueError, "Transaction is already rolled back"):
            await txn._begin_transaction()

    def test_get_mutation_for_begin_multiplexed_logic(self):
        # coverage for lines 788-797
        from google.protobuf.struct_pb2 import ListValue

        self.session.is_multiplexed = True
        txn = Transaction(self.session)

        m_insert = Mutation(
            insert=Mutation.Write(
                table="t", columns=["c"], values=[ListValue(values=[_make_value_pb(1)])]
            )
        )
        m_delete = Mutation(delete=Mutation.Delete(table="t"))

        # Test case where it picks non-insert mutation
        txn._mutations = [m_insert, m_delete]
        mut = txn._get_mutation_for_begin_mutations_only_transaction()
        self.assertEqual(mut, m_delete)

        # Test case where it picks insert with largest values
        m_insert_large = Mutation(
            insert=Mutation.Write(
                table="t",
                columns=["c"],
                values=[
                    ListValue(values=[_make_value_pb(1)]),
                    ListValue(values=[_make_value_pb(2)]),
                ],
            )
        )
        txn._mutations = [m_insert, m_insert_large]
        mut = txn._get_mutation_for_begin_mutations_only_transaction()
        self.assertEqual(mut, m_insert_large)

    def test_default_transaction_options(self):
        # coverage for lines 832-854
        from google.cloud.spanner_v1._async.transaction import DefaultTransactionOptions

        opts = DefaultTransactionOptions()
        self.assertIsNotNone(opts.default_read_write_transaction_options)
        self.assertEqual(
            opts.isolation_level,
            TransactionOptions.IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED,
        )
