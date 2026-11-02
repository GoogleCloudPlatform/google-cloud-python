# Copyright 2022 Google LLC All rights reserved.
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

import threading

import mock
from google.api_core import gapic_v1
from google.protobuf.struct_pb2 import Struct

from google.cloud.spanner_v1 import (
    DefaultTransactionOptions,
    DirectedReadOptions,
    ExecuteBatchDmlRequest,
    ExecuteBatchDmlResponse,
    ExecuteSqlRequest,
    PartialResultSet,
    ReadRequest,
    RequestOptions,
    ResultSet,
    ResultSetMetadata,
    ResultSetStats,
    StructType,
    TransactionOptions,
    TransactionSelector,
    Type,
    TypeCode,
    param_types,
)
from google.cloud.spanner_v1._helpers import (
    AtomicCounter,
    _augment_errors_with_request_id,
    _make_value_pb,
    _merge_query_options,
    _metadata_with_request_id,
    _metadata_with_request_id_and_req_id,
)
from google.cloud.spanner_v1.keyset import KeySet
from google.cloud.spanner_v1.request_id_header import REQ_RAND_PROCESS_ID
from google.cloud.spanner_v1.types import transaction as transaction_type
from tests._helpers import OpenTelemetryBase

TABLE_NAME = "citizens"
COLUMNS = ["email", "first_name", "last_name", "age"]
VALUES = [
    ["phred@exammple.com", "Phred", "Phlyntstone", 32],
    ["bharney@example.com", "Bharney", "Rhubble", 31],
]
DML_QUERY = """\
INSERT INTO citizens(first_name, last_name, age)
VALUES ("Phred", "Phlyntstone", 32)
"""
DML_QUERY_WITH_PARAM = """
INSERT INTO citizens(first_name, last_name, age)
VALUES ("Phred", "Phlyntstone", @age)
"""
SQL_QUERY = """\
SELECT first_name, last_name, age FROM citizens ORDER BY age"""
SQL_QUERY_WITH_PARAM = """
SELECT first_name, last_name, email FROM citizens WHERE age <= @max_age"""
PARAMS = {"age": 30}
PARAM_TYPES = {"age": Type(code=TypeCode.INT64)}
KEYS = [["bharney@example.com"], ["phred@example.com"]]
KEYSET = KeySet(keys=KEYS)
INDEX = "email-address-index"
LIMIT = 20
MODE = 2
RETRY = gapic_v1.method.DEFAULT
TIMEOUT = gapic_v1.method.DEFAULT
DIRECTED_READ_OPTIONS = {
    "include_replicas": {
        "replica_selections": [
            {
                "location": "us-west1",
                "type_": DirectedReadOptions.ReplicaSelection.Type.READ_ONLY,
            },
        ],
        "auto_failover_disabled": True,
    },
}
insert_dml = "INSERT INTO table(pkey, desc) VALUES (%pkey, %desc)"
insert_params = {"pkey": 12345, "desc": "DESCRIPTION"}
insert_param_types = {"pkey": param_types.INT64, "desc": param_types.STRING}
update_dml = 'UPDATE table SET desc = desc + "-amended"'
delete_dml = "DELETE FROM table WHERE desc IS NULL"

dml_statements = [
    (insert_dml, insert_params, insert_param_types),
    update_dml,
    delete_dml,
]


class TestTransaction(OpenTelemetryBase):
    PROJECT_ID = "project-id"
    INSTANCE_ID = "instance-id"
    INSTANCE_NAME = "projects/" + PROJECT_ID + "/instances/" + INSTANCE_ID
    DATABASE_ID = "database-id"
    DATABASE_NAME = INSTANCE_NAME + "/databases/" + DATABASE_ID
    SESSION_ID = "session-id"
    SESSION_NAME = DATABASE_NAME + "/sessions/" + SESSION_ID
    TRANSACTION_ID = b"DEADBEEF"
    TRANSACTION_TAG = "transaction-tag"

    BASE_ATTRIBUTES = {
        "db.type": "spanner",
        "db.url": "spanner.googleapis.com",
        "db.instance": "testing",
        "net.host.name": "spanner.googleapis.com",
    }

    def _getTargetClass(self):
        from google.cloud.spanner_v1.transaction import Transaction

        return Transaction

    def _make_one(self, session, *args, **kwargs):
        transaction = self._getTargetClass()(session, *args, **kwargs)
        session._transaction = transaction
        return transaction

    def _make_spanner_api(self):
        from google.cloud.spanner_v1 import SpannerClient

        return mock.create_autospec(SpannerClient, instance=True)

    def _assert_concurrent_transaction_invariants(
        self, call_args_list, expected_count=2
    ):
        self.assertEqual(len(call_args_list), expected_count)

        begin_calls = []
        reused_calls = []

        for call in call_args_list:
            request = call.kwargs["request"]
            pb_transaction = request.transaction._pb
            if pb_transaction.HasField("begin"):
                begin_calls.append(call)
            elif pb_transaction.id:
                reused_calls.append(call)

        self.assertEqual(
            len(begin_calls),
            1,
            "Exactly one concurrent thread must initiate the transaction.",
        )
        self.assertEqual(
            len(reused_calls),
            expected_count - 1,
            f"Remaining {expected_count - 1} thread(s) must reuse the transaction ID.",
        )

    def _execute_update_helper(
        self,
        transaction,
        api,
        count=0,
        query_options=None,
        exclude_txn_from_change_streams=False,
        isolation_level=TransactionOptions.IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED,
        read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.READ_LOCK_MODE_UNSPECIFIED,
    ):
        stats_pb = ResultSetStats(row_count_exact=1)

        transaction_pb = transaction_type.Transaction(id=self.TRANSACTION_ID)
        metadata_pb = ResultSetMetadata(transaction=transaction_pb)
        api.execute_sql.return_value = ResultSet(stats=stats_pb, metadata=metadata_pb)

        transaction.transaction_tag = self.TRANSACTION_TAG
        transaction.exclude_txn_from_change_streams = exclude_txn_from_change_streams
        transaction.isolation_level = isolation_level
        transaction.read_lock_mode = read_lock_mode
        transaction._execute_sql_request_count = count

        row_count = transaction.execute_update(
            DML_QUERY_WITH_PARAM,
            PARAMS,
            PARAM_TYPES,
            query_mode=MODE,
            query_options=query_options,
            request_options=RequestOptions(),
            retry=RETRY,
            timeout=TIMEOUT,
        )
        self.assertEqual(row_count, count + 1)

    def _execute_update_expected_request(
        self,
        database,
        query_options=None,
        begin=True,
        count=0,
        exclude_txn_from_change_streams=False,
        isolation_level=TransactionOptions.IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED,
        read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.READ_LOCK_MODE_UNSPECIFIED,
    ):
        if begin is True:
            expected_transaction = TransactionSelector(
                begin=TransactionOptions(
                    read_write=TransactionOptions.ReadWrite(
                        read_lock_mode=read_lock_mode
                    ),
                    exclude_txn_from_change_streams=exclude_txn_from_change_streams,
                    isolation_level=isolation_level,
                )
            )
        else:
            expected_transaction = TransactionSelector(id=self.TRANSACTION_ID)

        expected_params = Struct(
            fields={key: _make_value_pb(value) for (key, value) in PARAMS.items()}
        )

        expected_query_options = database._instance._client._query_options
        if query_options:
            expected_query_options = _merge_query_options(
                expected_query_options, query_options
            )
        expected_request_options = RequestOptions()
        expected_request_options.transaction_tag = self.TRANSACTION_TAG

        expected_request = ExecuteSqlRequest(
            session=self.SESSION_NAME,
            sql=DML_QUERY_WITH_PARAM,
            transaction=expected_transaction,
            params=expected_params,
            param_types=PARAM_TYPES,
            query_mode=MODE,
            query_options=expected_query_options,
            request_options=expected_request_options,
            seqno=count,
        )

        return expected_request

    def _execute_sql_helper(
        self,
        transaction,
        api,
        count=0,
        partition=None,
        sql_count=0,
        query_options=None,
        directed_read_options=None,
        concurrent=False,
    ):
        VALUES = [["bharney", "rhubbyl", 31], ["phred", "phlyntstone", 32]]
        VALUE_PBS = [[_make_value_pb(item) for item in row] for row in VALUES]
        struct_type_pb = StructType(
            fields=[
                StructType.Field(name="first_name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="last_name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="age", type_=Type(code=TypeCode.INT64)),
            ]
        )
        transaction_pb = transaction_type.Transaction(id=self.TRANSACTION_ID)
        metadata_pb = ResultSetMetadata(
            row_type=struct_type_pb, transaction=transaction_pb
        )
        stats_pb = ResultSetStats(
            query_stats=Struct(fields={"rows_returned": _make_value_pb(2)})
        )
        result_sets = [
            PartialResultSet(metadata=metadata_pb),
            PartialResultSet(stats=stats_pb),
        ]
        for i in range(len(result_sets)):
            result_sets[i].values.extend(VALUE_PBS[i])
        api.execute_streaming_sql.side_effect = lambda *a, **kw: _MockIterator(
            *result_sets
        )
        if not concurrent:
            transaction._execute_sql_request_count = sql_count
            transaction._read_request_count = count

        result_set = transaction.execute_sql(
            SQL_QUERY_WITH_PARAM,
            PARAMS,
            PARAM_TYPES,
            query_mode=MODE,
            query_options=query_options,
            request_options=RequestOptions(),
            partition=partition,
            retry=RETRY,
            timeout=TIMEOUT,
            directed_read_options=directed_read_options,
        )

        if not concurrent:
            self.assertEqual(transaction._read_request_count, count + 1)

        self.assertEqual(list(result_set), VALUES)
        self.assertEqual(result_set.metadata, metadata_pb)
        self.assertEqual(result_set.stats, stats_pb)
        if not concurrent:
            self.assertEqual(transaction._execute_sql_request_count, sql_count + 1)

    def _execute_sql_expected_request(
        self,
        database,
        partition=None,
        query_options=None,
        begin=True,
        sql_count=0,
        transaction_tag=False,
        directed_read_options=None,
    ):
        if begin is True:
            expected_transaction = TransactionSelector(
                begin=TransactionOptions(read_write=TransactionOptions.ReadWrite())
            )
        else:
            expected_transaction = TransactionSelector(id=self.TRANSACTION_ID)

        expected_params = Struct(
            fields={key: _make_value_pb(value) for (key, value) in PARAMS.items()}
        )

        expected_query_options = database._instance._client._query_options
        if query_options:
            expected_query_options = _merge_query_options(
                expected_query_options, query_options
            )

        expected_request_options = RequestOptions()

        if transaction_tag is True:
            expected_request_options.transaction_tag = self.TRANSACTION_TAG
        else:
            expected_request_options.transaction_tag = None

        expected_request = ExecuteSqlRequest(
            session=self.SESSION_NAME,
            sql=SQL_QUERY_WITH_PARAM,
            transaction=expected_transaction,
            params=expected_params,
            param_types=PARAM_TYPES,
            query_mode=MODE,
            query_options=expected_query_options,
            request_options=expected_request_options,
            partition_token=partition,
            seqno=sql_count,
            directed_read_options=directed_read_options,
        )

        return expected_request

    def _read_helper(
        self,
        transaction,
        api,
        count=0,
        partition=None,
        directed_read_options=None,
        concurrent=False,
    ):
        VALUES = [["bharney", 31], ["phred", 32]]
        VALUE_PBS = [[_make_value_pb(item) for item in row] for row in VALUES]
        struct_type_pb = StructType(
            fields=[
                StructType.Field(name="name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="age", type_=Type(code=TypeCode.INT64)),
            ]
        )

        transaction_pb = transaction_type.Transaction(id=self.TRANSACTION_ID)
        metadata_pb = ResultSetMetadata(
            row_type=struct_type_pb, transaction=transaction_pb
        )

        stats_pb = ResultSetStats(
            query_stats=Struct(fields={"rows_returned": _make_value_pb(2)})
        )
        result_sets = [
            PartialResultSet(metadata=metadata_pb),
            PartialResultSet(stats=stats_pb),
        ]
        for i in range(len(result_sets)):
            result_sets[i].values.extend(VALUE_PBS[i])

        api.streaming_read.side_effect = lambda *a, **kw: _MockIterator(*result_sets)
        if not concurrent:
            transaction._read_request_count = count

        if partition is not None:  # 'limit' and 'partition' incompatible
            result_set = transaction.read(
                TABLE_NAME,
                COLUMNS,
                KEYSET,
                index=INDEX,
                partition=partition,
                retry=RETRY,
                timeout=TIMEOUT,
                request_options=RequestOptions(),
                directed_read_options=directed_read_options,
            )
        else:
            result_set = transaction.read(
                TABLE_NAME,
                COLUMNS,
                KEYSET,
                index=INDEX,
                limit=LIMIT,
                retry=RETRY,
                timeout=TIMEOUT,
                request_options=RequestOptions(),
                directed_read_options=directed_read_options,
            )

        if not concurrent:
            self.assertEqual(transaction._read_request_count, count + 1)

        self.assertEqual(list(result_set), VALUES)
        self.assertEqual(result_set.metadata, metadata_pb)
        self.assertEqual(result_set.stats, stats_pb)

    def _read_helper_expected_request(
        self,
        partition=None,
        begin=True,
        count=0,
        transaction_tag=False,
        directed_read_options=None,
    ):
        if begin is True:
            expected_transaction = TransactionSelector(
                begin=TransactionOptions(read_write=TransactionOptions.ReadWrite())
            )
        else:
            expected_transaction = TransactionSelector(id=self.TRANSACTION_ID)

        if partition is not None:
            expected_limit = 0
        else:
            expected_limit = LIMIT

        # Transaction tag is ignored for read request.
        expected_request_options = RequestOptions()

        if transaction_tag is True:
            expected_request_options.transaction_tag = self.TRANSACTION_TAG
        else:
            expected_request_options.transaction_tag = None

        expected_request = ReadRequest(
            session=self.SESSION_NAME,
            table=TABLE_NAME,
            columns=COLUMNS,
            key_set=KEYSET._to_pb(),
            transaction=expected_transaction,
            index=INDEX,
            limit=expected_limit,
            partition_token=partition,
            request_options=expected_request_options,
            directed_read_options=directed_read_options,
        )

        return expected_request

    def _batch_update_helper(
        self,
        transaction,
        database,
        api,
        error_after=None,
        count=0,
    ):
        from google.rpc.status_pb2 import Status

        stats_pbs = [
            ResultSetStats(row_count_exact=1),
            ResultSetStats(row_count_exact=2),
            ResultSetStats(row_count_exact=3),
        ]
        if error_after is not None:
            stats_pbs = stats_pbs[:error_after]
            expected_status = Status(code=400)
        else:
            expected_status = Status(code=200)
        expected_row_counts = [stats.row_count_exact for stats in stats_pbs]
        transaction_pb = transaction_type.Transaction(id=self.TRANSACTION_ID)
        metadata_pb = ResultSetMetadata(transaction=transaction_pb)
        result_sets_pb = [
            ResultSet(stats=stats_pb, metadata=metadata_pb) for stats_pb in stats_pbs
        ]

        response = ExecuteBatchDmlResponse(
            status=expected_status,
            result_sets=result_sets_pb,
        )

        api.execute_batch_dml.return_value = response
        transaction.transaction_tag = self.TRANSACTION_TAG
        transaction._execute_sql_request_count = count

        status, row_counts = transaction.batch_update(
            dml_statements, request_options=RequestOptions()
        )

        self.assertEqual(status, expected_status)
        self.assertEqual(row_counts, expected_row_counts)

    def _batch_update_expected_request(self, begin=True, count=0):
        if begin is True:
            expected_transaction = TransactionSelector(
                begin=TransactionOptions(read_write=TransactionOptions.ReadWrite())
            )
        else:
            expected_transaction = TransactionSelector(id=self.TRANSACTION_ID)

        expected_insert_params = Struct(
            fields={
                key: _make_value_pb(value) for (key, value) in insert_params.items()
            }
        )
        expected_statements = [
            ExecuteBatchDmlRequest.Statement(
                sql=insert_dml,
                params=expected_insert_params,
                param_types=insert_param_types,
            ),
            ExecuteBatchDmlRequest.Statement(sql=update_dml),
            ExecuteBatchDmlRequest.Statement(sql=delete_dml),
        ]

        expected_request_options = RequestOptions()
        expected_request_options.transaction_tag = self.TRANSACTION_TAG

        expected_request = ExecuteBatchDmlRequest(
            session=self.SESSION_NAME,
            transaction=expected_transaction,
            statements=expected_statements,
            seqno=count,
            request_options=expected_request_options,
        )

        return expected_request

    def test_transaction_should_include_begin_with_first_update(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_update_helper(transaction=transaction, api=api)

        api.execute_sql.assert_called_once_with(
            request=self._execute_update_expected_request(database=database),
            retry=RETRY,
            timeout=TIMEOUT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.1.1.1",
                ),
            ],
        )

    def test_transaction_should_include_begin_with_first_query(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_sql_helper(transaction=transaction, api=api)

        api.execute_streaming_sql.assert_called_once_with(
            request=self._execute_sql_expected_request(database=database),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            timeout=TIMEOUT,
            retry=RETRY,
        )

    def test_transaction_should_include_begin_with_first_read(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._read_helper(transaction=transaction, api=api)

        api.streaming_read.assert_called_once_with(
            request=self._read_helper_expected_request(),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            retry=RETRY,
            timeout=TIMEOUT,
        )

    def test_transaction_should_include_begin_with_first_batch_update(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._batch_update_helper(transaction=transaction, database=database, api=api)
        api.execute_batch_dml.assert_called_once_with(
            request=self._batch_update_expected_request(),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            retry=RETRY,
            timeout=TIMEOUT,
        )

    def test_transaction_should_include_begin_w_exclude_txn_from_change_streams_with_first_update(
        self,
    ):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_update_helper(
            transaction=transaction, api=api, exclude_txn_from_change_streams=True
        )

        api.execute_sql.assert_called_once_with(
            request=self._execute_update_expected_request(
                database=database, exclude_txn_from_change_streams=True
            ),
            retry=RETRY,
            timeout=TIMEOUT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_transaction_should_include_begin_w_isolation_level_with_first_update(
        self,
    ):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_update_helper(
            transaction=transaction,
            api=api,
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
        )

        api.execute_sql.assert_called_once_with(
            request=self._execute_update_expected_request(
                database=database,
                isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
            ),
            retry=RETRY,
            timeout=TIMEOUT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_transaction_should_include_begin_w_read_lock_mode_with_first_update(
        self,
    ):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_update_helper(
            transaction=transaction,
            api=api,
            read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
        )

        api.execute_sql.assert_called_once_with(
            request=self._execute_update_expected_request(
                database=database,
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
            retry=RETRY,
            timeout=TIMEOUT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_transaction_should_include_begin_w_isolation_level_and_read_lock_mode_with_first_update(
        self,
    ):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_update_helper(
            transaction=transaction,
            api=api,
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
            read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.PESSIMISTIC,
        )

        api.execute_sql.assert_called_once_with(
            request=self._execute_update_expected_request(
                database=database,
                isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.PESSIMISTIC,
            ),
            retry=RETRY,
            timeout=TIMEOUT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_transaction_should_use_transaction_id_if_error_with_first_batch_update(
        self,
    ):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._batch_update_helper(
            transaction=transaction, database=database, api=api, error_after=2
        )
        api.execute_batch_dml.assert_called_once_with(
            request=self._batch_update_expected_request(begin=True),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            retry=RETRY,
            timeout=TIMEOUT,
        )
        self._execute_update_helper(transaction=transaction, api=api)
        api.execute_sql.assert_called_once_with(
            request=self._execute_update_expected_request(
                database=database, begin=False
            ),
            retry=gapic_v1.method.DEFAULT,
            timeout=gapic_v1.method.DEFAULT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_transaction_should_use_transaction_id_returned_by_first_query(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_sql_helper(transaction=transaction, api=api)
        api.execute_streaming_sql.assert_called_once_with(
            request=self._execute_sql_expected_request(database=database),
            retry=gapic_v1.method.DEFAULT,
            timeout=gapic_v1.method.DEFAULT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

        self._execute_update_helper(transaction=transaction, api=api)
        api.execute_sql.assert_called_once_with(
            request=self._execute_update_expected_request(
                database=database, begin=False
            ),
            retry=gapic_v1.method.DEFAULT,
            timeout=gapic_v1.method.DEFAULT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_transaction_should_use_transaction_id_returned_by_first_update(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_update_helper(transaction=transaction, api=api)
        api.execute_sql.assert_called_once_with(
            request=self._execute_update_expected_request(database=database),
            retry=gapic_v1.method.DEFAULT,
            timeout=gapic_v1.method.DEFAULT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

        self._execute_sql_helper(transaction=transaction, api=api)
        api.execute_streaming_sql.assert_called_once_with(
            request=self._execute_sql_expected_request(
                database=database, begin=False, transaction_tag=True
            ),
            retry=gapic_v1.method.DEFAULT,
            timeout=gapic_v1.method.DEFAULT,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_transaction_execute_sql_w_directed_read_options(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)

        self._execute_sql_helper(
            transaction=transaction,
            api=api,
            directed_read_options=DIRECTED_READ_OPTIONS,
        )
        api.execute_streaming_sql.assert_called_once_with(
            request=self._execute_sql_expected_request(
                database=database, directed_read_options=DIRECTED_READ_OPTIONS
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            retry=gapic_v1.method.DEFAULT,
            timeout=gapic_v1.method.DEFAULT,
        )

    def test_transaction_streaming_read_w_directed_read_options(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)

        self._read_helper(
            transaction=transaction,
            api=api,
            directed_read_options=DIRECTED_READ_OPTIONS,
        )
        api.streaming_read.assert_called_once_with(
            request=self._read_helper_expected_request(
                directed_read_options=DIRECTED_READ_OPTIONS
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            retry=RETRY,
            timeout=TIMEOUT,
        )

    def test_transaction_should_use_transaction_id_returned_by_first_read(self):
        database = _Database()
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._read_helper(transaction=transaction, api=api)
        api.streaming_read.assert_called_once_with(
            request=self._read_helper_expected_request(),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            retry=RETRY,
            timeout=TIMEOUT,
        )

        self._batch_update_helper(transaction=transaction, database=database, api=api)
        api.execute_batch_dml.assert_called_once_with(
            request=self._batch_update_expected_request(begin=False),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
            retry=RETRY,
            timeout=TIMEOUT,
        )

    def test_transaction_should_use_transaction_id_returned_by_first_batch_update(self):
        database = _Database()
        api = database.spanner_api = self._make_spanner_api()
        session = _Session(database)
        transaction = self._make_one(session)
        self._batch_update_helper(transaction=transaction, database=database, api=api)
        api.execute_batch_dml.assert_called_once_with(
            request=self._batch_update_expected_request(),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            retry=RETRY,
            timeout=TIMEOUT,
        )
        self._read_helper(transaction=transaction, api=api)
        api.streaming_read.assert_called_once_with(
            request=self._read_helper_expected_request(
                begin=False, transaction_tag=True
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
            retry=RETRY,
            timeout=TIMEOUT,
        )

    def test_transaction_for_concurrent_statement_should_begin_one_transaction_with_execute_update(
        self,
    ):
        database = _Database()
        api = database.spanner_api = self._make_spanner_api()
        session = _Session(database)
        transaction = self._make_one(session)
        threads = []
        threads.append(
            threading.Thread(
                target=self._execute_update_helper,
                kwargs={"transaction": transaction, "api": api},
            )
        )
        threads.append(
            threading.Thread(
                target=self._execute_update_helper,
                kwargs={"transaction": transaction, "api": api},
            )
        )
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self._batch_update_helper(transaction=transaction, database=database, api=api)

        self._assert_concurrent_transaction_invariants(
            api.execute_sql.call_args_list, 2
        )
        self.assertEqual(api.execute_batch_dml.call_count, 1)

    def test_transaction_for_concurrent_statement_should_begin_one_transaction_with_batch_update(
        self,
    ):
        database = _Database()
        api = database.spanner_api = self._make_spanner_api()
        session = _Session(database)
        transaction = self._make_one(session)
        threads = []
        threads.append(
            threading.Thread(
                target=self._batch_update_helper,
                kwargs={"transaction": transaction, "database": database, "api": api},
            )
        )
        threads.append(
            threading.Thread(
                target=self._batch_update_helper,
                kwargs={"transaction": transaction, "database": database, "api": api},
            )
        )
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self._execute_update_helper(transaction=transaction, api=api)
        self.assertEqual(api.execute_sql.call_count, 1)

        self._assert_concurrent_transaction_invariants(
            api.execute_batch_dml.call_args_list, 2
        )

    def test_transaction_for_concurrent_statement_should_begin_one_transaction_with_read(
        self,
    ):
        self.maxDiff = None
        database = _Database()
        api = database.spanner_api = self._make_spanner_api()
        session = _Session(database)
        transaction = self._make_one(session)
        threads = []
        threads.append(
            threading.Thread(
                target=self._read_helper,
                kwargs={"transaction": transaction, "api": api, "concurrent": True},
            )
        )
        threads.append(
            threading.Thread(
                target=self._read_helper,
                kwargs={"transaction": transaction, "api": api, "concurrent": True},
            )
        )
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self._execute_update_helper(transaction=transaction, api=api)

        self.assertEqual(api.execute_sql.call_count, 1)
        self._assert_concurrent_transaction_invariants(
            api.streaming_read.call_args_list, 2
        )

    def test_transaction_for_concurrent_statement_should_begin_one_transaction_with_query(
        self,
    ):
        database = _Database()
        api = database.spanner_api = self._make_spanner_api()
        session = _Session(database)
        transaction = self._make_one(session)
        threads = []
        threads.append(
            threading.Thread(
                target=self._execute_sql_helper,
                kwargs={"transaction": transaction, "api": api, "concurrent": True},
            )
        )
        threads.append(
            threading.Thread(
                target=self._execute_sql_helper,
                kwargs={"transaction": transaction, "api": api, "concurrent": True},
            )
        )
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self._execute_update_helper(transaction=transaction, api=api)

        self.assertEqual(api.execute_sql.call_count, 1)
        self._assert_concurrent_transaction_invariants(
            api.execute_streaming_sql.call_args_list, 2
        )

    def test_transaction_should_execute_sql_with_route_to_leader_disabled(self):
        database = _Database()
        database._route_to_leader_enabled = False
        session = _Session(database)
        api = database.spanner_api = self._make_spanner_api()
        transaction = self._make_one(session)
        self._execute_sql_helper(transaction=transaction, api=api)

        api.execute_streaming_sql.assert_called_once_with(
            request=self._execute_sql_expected_request(database=database),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
            timeout=TIMEOUT,
            retry=RETRY,
        )


class _Client(object):
    NTH_CLIENT = AtomicCounter()

    def __init__(self):
        from google.cloud.spanner_v1 import ExecuteSqlRequest

        self.project = "project-id"
        self._query_options = ExecuteSqlRequest.QueryOptions(optimizer_version="1")
        self.directed_read_options = None
        self.default_transaction_options = DefaultTransactionOptions()
        self._client_context = None
        self._nth_client_id = _Client.NTH_CLIENT.increment()
        self._nth_request = AtomicCounter()

    @property
    def _next_nth_request(self):
        return self._nth_request.increment()


class _Instance(object):
    def __init__(self):
        self._client = _Client()
        self.instance_id = "test-instance"
        self.experimental_host = None


class _Database(object):
    def __init__(self):
        self.name = "testing"
        self.database_id = "test-database"
        self._instance = _Instance()
        self._route_to_leader_enabled = True
        self._directed_read_options = None
        self.default_transaction_options = DefaultTransactionOptions()

    @property
    def _next_nth_request(self):
        return self._instance._client._next_nth_request

    @property
    def _nth_client_id(self):
        return self._instance._client._nth_client_id

    def metadata_with_request_id(
        self, nth_request, nth_attempt, prior_metadata=[], span=None
    ):
        return _metadata_with_request_id(
            self._nth_client_id,
            self._channel_id,
            nth_request,
            nth_attempt,
            prior_metadata,
            span,
        )

    def metadata_and_request_id(
        self, nth_request, nth_attempt, prior_metadata=[], span=None
    ):
        return _metadata_with_request_id_and_req_id(
            self._nth_client_id,
            self._channel_id,
            nth_request,
            nth_attempt,
            prior_metadata,
            span,
        )

    @property
    def _channel_id(self):
        return 1

    def with_error_augmentation(
        self, nth_request, nth_attempt, prior_metadata=[], span=None
    ):
        metadata, request_id = _metadata_with_request_id_and_req_id(
            self._nth_client_id,
            self._channel_id,
            nth_request,
            nth_attempt,
            prior_metadata,
            span,
        )
        return metadata, _augment_errors_with_request_id(request_id)


class _Session(object):
    _transaction = None

    def __init__(self, database=None, name=TestTransaction.SESSION_NAME):
        self._database = database
        self.name = name

    @property
    def session_id(self):
        return self.name


class _MockIterator(object):
    def __init__(self, *values, **kw):
        self._iter_values = iter(values)
        self._fail_after = kw.pop("fail_after", False)
        self._error = kw.pop("error", Exception)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._iter_values)
        except StopIteration:
            if self._fail_after:
                raise self._error
            raise

    next = __next__
