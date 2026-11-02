# Copyright 2026 Google LLC All rights reserved.
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

from google.protobuf import struct_pb2

from google.cloud.spanner_v1._helpers import (
    _merge_client_context,
    _merge_request_options,
)
from google.cloud.spanner_v1.types import (
    ExecuteSqlRequest,
    RequestOptions,
)


class TestClientContext(unittest.TestCase):
    def test__merge_client_context_both_none(self):
        self.assertIsNone(_merge_client_context(None, None))

    def test__merge_client_context_base_none(self):
        merge = RequestOptions.ClientContext(
            secure_context={"a": struct_pb2.Value(string_value="A")}
        )
        result = _merge_client_context(None, merge)
        self.assertEqual(result.secure_context["a"], "A")

    def test__merge_client_context_merge_none(self):
        base = RequestOptions.ClientContext(
            secure_context={"a": struct_pb2.Value(string_value="A")}
        )
        result = _merge_client_context(base, None)
        self.assertEqual(result.secure_context["a"], "A")

    def test__merge_client_context_both_set(self):
        base = RequestOptions.ClientContext(
            secure_context={
                "a": struct_pb2.Value(string_value="A"),
                "b": struct_pb2.Value(string_value="B1"),
            }
        )
        merge = RequestOptions.ClientContext(
            secure_context={
                "b": struct_pb2.Value(string_value="B2"),
                "c": struct_pb2.Value(string_value="C"),
            }
        )
        result = _merge_client_context(base, merge)
        self.assertEqual(result.secure_context["a"], "A")
        self.assertEqual(result.secure_context["b"], "B2")
        self.assertEqual(result.secure_context["c"], "C")

    def test__merge_request_options_with_client_context(self):
        request_options = RequestOptions(priority=RequestOptions.Priority.PRIORITY_LOW)
        client_context = RequestOptions.ClientContext(
            secure_context={"a": struct_pb2.Value(string_value="A")}
        )

        result = _merge_request_options(request_options, client_context)

        self.assertEqual(result.priority, RequestOptions.Priority.PRIORITY_LOW)
        self.assertEqual(result.client_context.secure_context["a"], "A")

    def test_client_init_with_client_context(self):
        from google.cloud.spanner_v1.client import Client

        project = "PROJECT"
        credentials = mock.Mock(spec=["_resource_prefix__"])
        with (
            mock.patch("google.auth.default", return_value=(credentials, project)),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_enable_builtin_metrics_env",
                return_value=False,
            ),
        ):
            client_context = {
                "secure_context": {"a": struct_pb2.Value(string_value="A")}
            }
            client = Client(
                project=project,
                client_context=client_context,
                disable_builtin_metrics=True,
            )

        self.assertIsInstance(client._client_context, RequestOptions.ClientContext)
        self.assertEqual(client._client_context.secure_context["a"], "A")

    def test_snapshot_execute_sql_propagates_client_context(self):
        from google.cloud.spanner_v1.snapshot import Snapshot

        session = mock.Mock(spec=["name", "_database"])
        session.name = "session-name"
        database = session._database = mock.Mock()
        database.name = "database-name"
        database._route_to_leader_enabled = False
        database._directed_read_options = None

        client = database._instance._client = mock.Mock()
        client._query_options = None
        client._client_context = RequestOptions.ClientContext(
            secure_context={"client": struct_pb2.Value(string_value="from-client")}
        )

        snapshot_context = RequestOptions.ClientContext(
            secure_context={"snapshot": struct_pb2.Value(string_value="from-snapshot")}
        )
        snapshot = Snapshot(session, client_context=snapshot_context)

        with mock.patch.object(snapshot, "_get_streamed_result_set") as mocked:
            snapshot.execute_sql("SELECT 1")
            kwargs = mocked.call_args.kwargs
            request = kwargs["request"]
            self.assertIsInstance(request, ExecuteSqlRequest)
            self.assertEqual(
                request.request_options.client_context.secure_context["client"],
                "from-client",
            )
            self.assertEqual(
                request.request_options.client_context.secure_context["snapshot"],
                "from-snapshot",
            )

    def test_transaction_commit_propagates_client_context(self):
        from google.cloud.spanner_v1.transaction import Transaction
        from google.cloud.spanner_v1.types import (
            CommitRequest,
            CommitResponse,
            MultiplexedSessionPrecommitToken,
        )

        session = mock.Mock(spec=["name", "_database", "is_multiplexed"])
        session.name = "session-name"
        session.is_multiplexed = False
        database = session._database = mock.Mock()
        database.name = "projects/p/instances/i/databases/d"
        database._route_to_leader_enabled = False
        database.log_commit_stats = False
        database.with_error_augmentation.return_value = (None, mock.MagicMock())
        database._next_nth_request = 1

        client = database._instance._client = mock.Mock()
        client._client_context = RequestOptions.ClientContext(
            secure_context={"client": struct_pb2.Value(string_value="from-client")}
        )

        transaction_context = RequestOptions.ClientContext(
            secure_context={"txn": struct_pb2.Value(string_value="from-txn")}
        )
        transaction = Transaction(session, client_context=transaction_context)
        transaction._transaction_id = b"tx-id"

        api = database.spanner_api = mock.Mock()

        token = MultiplexedSessionPrecommitToken(seq_num=1)
        response = CommitResponse(precommit_token=token)

        def side_effect(f, **kw):
            return f()

        api.commit.return_value = response

        with mock.patch(
            "google.cloud.spanner_v1.transaction._retry", side_effect=side_effect
        ):
            transaction.commit()

        args, kwargs = api.commit.call_args
        request = kwargs["request"]
        self.assertIsInstance(request, CommitRequest)
        self.assertEqual(
            request.request_options.client_context.secure_context["client"],
            "from-client",
        )
        self.assertEqual(
            request.request_options.client_context.secure_context["txn"], "from-txn"
        )

    def test_snapshot_execute_sql_request_level_override(self):
        from google.cloud.spanner_v1.snapshot import Snapshot

        session = mock.Mock(spec=["name", "_database"])
        session.name = "session-name"
        database = session._database = mock.Mock()
        database.name = "database-name"
        database._route_to_leader_enabled = False
        database._directed_read_options = None

        client = database._instance._client = mock.Mock()
        client._query_options = None
        client._client_context = RequestOptions.ClientContext(
            secure_context={"a": struct_pb2.Value(string_value="from-client")}
        )

        snapshot_context = RequestOptions.ClientContext(
            secure_context={
                "a": struct_pb2.Value(string_value="from-snapshot"),
                "b": struct_pb2.Value(string_value="B"),
            }
        )
        snapshot = Snapshot(session, client_context=snapshot_context)

        request_options = RequestOptions(
            client_context=RequestOptions.ClientContext(
                secure_context={"a": struct_pb2.Value(string_value="from-request")}
            )
        )

        with mock.patch.object(snapshot, "_get_streamed_result_set") as mocked:
            snapshot.execute_sql("SELECT 1", request_options=request_options)
            kwargs = mocked.call_args.kwargs
            request = kwargs["request"]
            self.assertEqual(
                request.request_options.client_context.secure_context["a"],
                "from-request",
            )
            self.assertEqual(
                request.request_options.client_context.secure_context["b"], "B"
            )

    def test_batch_commit_propagates_client_context(self):
        from google.cloud.spanner_v1 import DefaultTransactionOptions
        from google.cloud.spanner_v1.batch import Batch
        from google.cloud.spanner_v1.types import CommitRequest, CommitResponse

        session = mock.Mock(spec=["name", "_database"])
        session.name = "session-name"
        database = session._database = mock.Mock()
        database.name = "database-name"
        database._route_to_leader_enabled = False
        database.log_commit_stats = False
        database.default_transaction_options = DefaultTransactionOptions()
        database.with_error_augmentation.return_value = (None, mock.MagicMock())
        database._next_nth_request = 1
        client = database._instance._client = mock.Mock()
        client._client_context = RequestOptions.ClientContext(
            secure_context={"client": struct_pb2.Value(string_value="from-client")}
        )

        batch_context = RequestOptions.ClientContext(
            secure_context={"batch": struct_pb2.Value(string_value="from-batch")}
        )
        batch = Batch(session, client_context=batch_context)

        api = database.spanner_api = mock.Mock()
        response = CommitResponse()
        api.commit.return_value = response

        batch.commit()

        args, kwargs = api.commit.call_args
        request = kwargs["request"]
        self.assertIsInstance(request, CommitRequest)
        self.assertEqual(
            request.request_options.client_context.secure_context["client"],
            "from-client",
        )
        self.assertEqual(
            request.request_options.client_context.secure_context["batch"], "from-batch"
        )

    def test_transaction_execute_update_propagates_client_context(self):
        from google.cloud.spanner_v1.transaction import Transaction
        from google.cloud.spanner_v1.types import (
            ExecuteSqlRequest,
            MultiplexedSessionPrecommitToken,
            ResultSet,
        )

        session = mock.Mock(spec=["name", "_database", "_precommit_token"])
        session.name = "session-name"
        database = session._database = mock.Mock()
        database.name = "database-name"
        database._route_to_leader_enabled = False
        database.with_error_augmentation.return_value = (None, mock.MagicMock())
        database._next_nth_request = 1

        client = database._instance._client = mock.Mock()
        client._query_options = None
        client._client_context = RequestOptions.ClientContext(
            secure_context={"client": struct_pb2.Value(string_value="from-client")}
        )

        transaction_context = RequestOptions.ClientContext(
            secure_context={"txn": struct_pb2.Value(string_value="from-txn")}
        )
        transaction = Transaction(session, client_context=transaction_context)
        transaction._transaction_id = b"tx-id"
        transaction._precommit_token = MultiplexedSessionPrecommitToken(seq_num=1)

        database.spanner_api = mock.Mock()
        response = ResultSet(
            precommit_token=MultiplexedSessionPrecommitToken(seq_num=2)
        )

        with mock.patch.object(transaction, "_execute_request", return_value=response):
            transaction.execute_update("UPDATE T SET C = 1")

            args, kwargs = transaction._execute_request.call_args
            request = args[1]
            self.assertIsInstance(request, ExecuteSqlRequest)
            self.assertEqual(
                request.request_options.client_context.secure_context["client"],
                "from-client",
            )
            self.assertEqual(
                request.request_options.client_context.secure_context["txn"], "from-txn"
            )

    def test_mutation_groups_batch_write_propagates_client_context(self):
        from google.cloud.spanner_v1.batch import MutationGroups
        from google.cloud.spanner_v1.types import BatchWriteRequest

        session = mock.Mock(spec=["name", "_database"])
        session.name = "session-name"
        database = session._database = mock.Mock()
        database.name = "database-name"
        database._route_to_leader_enabled = False
        database.with_error_augmentation.return_value = (None, mock.MagicMock())
        database.metadata_with_request_id.return_value = []
        database._next_nth_request = 1

        client = database._instance._client = mock.Mock()
        client._client_context = RequestOptions.ClientContext(
            secure_context={"client": struct_pb2.Value(string_value="from-client")}
        )

        mg_context = RequestOptions.ClientContext(
            secure_context={"mg": struct_pb2.Value(string_value="from-mg")}
        )
        mg = MutationGroups(session, client_context=mg_context)

        api = database.spanner_api = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_v1._helpers._retry", side_effect=lambda f, **kw: f()
        ):
            mg.batch_write()

        args, kwargs = api.batch_write.call_args
        request = kwargs["request"]
        self.assertIsInstance(request, BatchWriteRequest)
        self.assertEqual(
            request.request_options.client_context.secure_context["client"],
            "from-client",
        )
        self.assertEqual(
            request.request_options.client_context.secure_context["mg"], "from-mg"
        )

    def test_batch_snapshot_propagates_client_context(self):
        from google.cloud.spanner_v1.database import BatchSnapshot

        database = mock.Mock()
        database.name = "database-name"
        client = database._instance._client = mock.Mock()
        client._query_options = None
        client._client_context = RequestOptions.ClientContext(
            secure_context={"client": struct_pb2.Value(string_value="from-client")}
        )

        batch_context = RequestOptions.ClientContext(
            secure_context={"batch": struct_pb2.Value(string_value="from-batch")}
        )
        batch_snapshot = BatchSnapshot(database, client_context=batch_context)

        session = mock.Mock(spec=["name", "_database", "session_id", "snapshot"])
        session.name = "session-name"
        session.session_id = "session-id"
        database.sessions_manager.get_session.return_value = session

        snapshot = mock.Mock()
        session.snapshot.return_value = snapshot

        batch_snapshot.execute_sql("SELECT 1")

        session.snapshot.assert_called_once()
        kwargs = session.snapshot.call_args.kwargs
        self.assertEqual(kwargs["client_context"], batch_context)

    def test_database_snapshot_propagates_client_context(self):
        from google.cloud.spanner_v1.database import Database

        instance = mock.Mock()
        instance._client = mock.Mock()
        instance._client._query_options = None
        instance._client._client_context = None

        database = Database("db", instance)
        with mock.patch(
            "google.cloud.spanner_v1.database.SnapshotCheckout"
        ) as mocked_checkout:
            client_context = {
                "secure_context": {"a": struct_pb2.Value(string_value="A")}
            }
            database.snapshot(client_context=client_context)

            mocked_checkout.assert_called_once_with(
                database, client_context=client_context
            )

    def test_transaction_rollback_propagates_client_context_is_not_supported(self):
        # Verify that rollback DOES NOT take client_context as it's not in RollbackRequest
        from google.cloud.spanner_v1.transaction import Transaction

        session = mock.Mock(spec=["name", "_database"])
        session.name = "session-name"
        database = session._database = mock.Mock()
        database.name = "database-name"
        database._route_to_leader_enabled = False
        database.with_error_augmentation.return_value = (None, mock.MagicMock())
        database._next_nth_request = 1

        transaction = Transaction(session)
        transaction._transaction_id = b"tx-id"

        api = database.spanner_api = mock.Mock()

        transaction.rollback()

        args, kwargs = api.rollback.call_args
        self.assertEqual(kwargs["session"], "session-name")
        self.assertEqual(kwargs["transaction_id"], b"tx-id")
        # Ensure no request_options or client_context passed to rollback
        self.assertNotIn("request_options", kwargs)


if __name__ == "__main__":
    unittest.main()
