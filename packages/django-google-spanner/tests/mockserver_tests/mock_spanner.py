# Copyright 2025 Google LLC All rights reserved.
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

import base64
from concurrent import futures

import google.cloud.spanner_v1.types.commit_response as commit
import google.cloud.spanner_v1.types.result_set as result_set
import google.cloud.spanner_v1.types.spanner as spanner
import google.cloud.spanner_v1.types.transaction as transaction
import grpc
from google.cloud.spanner_v1 import (
    ExecuteSqlRequest,
    ResultSetMetadata,
    TransactionOptions,
)
from google.protobuf import empty_pb2

import tests.mockserver_tests.spanner_database_admin_pb2_grpc as database_admin_grpc
import tests.mockserver_tests.spanner_pb2_grpc as spanner_grpc
from tests.mockserver_tests.mock_database_admin import DatabaseAdminServicer


class MockSpanner:
    def __init__(self):
        self.results = {}

    def add_result(self, sql: str, result: result_set.ResultSet):
        self.results[sql.lower().strip()] = result

    def get_result(self, sql: str) -> result_set.ResultSet:
        result = self.results.get(sql.lower().strip())
        if result is None:
            raise ValueError(f"No result found for {sql}")
        return result

    def get_result_as_partial_result_sets(
        self, sql: str, started_transaction: transaction.Transaction
    ) -> [result_set.PartialResultSet]:
        result: result_set.ResultSet = self.get_result(sql)
        partials = []
        first = True
        if len(result.rows) == 0:
            partial = result_set.PartialResultSet()
            partial.metadata = ResultSetMetadata(result.metadata)
            partials.append(partial)
        else:
            for row in result.rows:
                partial = result_set.PartialResultSet()
                if first:
                    partial.metadata = ResultSetMetadata(result.metadata)
                partial.values.extend(row)
                partials.append(partial)
        partials[len(partials) - 1].stats = result.stats
        if started_transaction:
            partials[0].metadata.transaction = started_transaction
        return partials


# An in-memory mock Spanner server that can be used for testing.
class SpannerServicer(spanner_grpc.SpannerServicer):
    def __init__(self):
        self._requests = []
        self.session_counter = 0
        self.sessions = {}
        self.transaction_counter = 0
        self.transactions = {}
        self._mock_spanner = MockSpanner()

    @property
    def mock_spanner(self):
        return self._mock_spanner

    @property
    def requests(self):
        return self._requests

    def clear_requests(self):
        self._requests = []

    def CreateSession(self, request, context):
        self._requests.append(request)
        return self.__create_session(request.database, request.session)

    def BatchCreateSessions(self, request, context):
        self._requests.append(request)
        sessions = []
        for i in range(request.session_count):
            sessions.append(
                self.__create_session(request.database, request.session_template)
            )
        return spanner.BatchCreateSessionsResponse(dict(session=sessions))

    def __create_session(self, database: str, session_template: spanner.Session):
        self.session_counter += 1
        session = spanner.Session()
        session.name = database + "/sessions/" + str(self.session_counter)
        session.multiplexed = session_template.multiplexed
        session.labels.MergeFrom(session_template.labels)
        session.creator_role = session_template.creator_role
        self.sessions[session.name] = session
        return session

    def GetSession(self, request, context):
        self._requests.append(request)
        return spanner.Session()

    def ListSessions(self, request, context):
        self._requests.append(request)
        return [spanner.Session()]

    def DeleteSession(self, request, context):
        self._requests.append(request)
        return empty_pb2.Empty()

    def ExecuteSql(self, request, context):
        self._requests.append(request)
        return result_set.ResultSet()

    def ExecuteStreamingSql(self, request: ExecuteSqlRequest, context):
        self._requests.append(request)
        started_transaction = None
        if not request.transaction.begin == TransactionOptions():
            started_transaction = self.__create_transaction(
                request.session, request.transaction.begin
            )
        partials = self.mock_spanner.get_result_as_partial_result_sets(
            request.sql, started_transaction
        )
        for result in partials:
            yield result

    def ExecuteBatchDml(self, request, context):
        self._requests.append(request)
        response = spanner.ExecuteBatchDmlResponse()
        started_transaction = None
        if not request.transaction.begin == TransactionOptions():
            started_transaction = self.__create_transaction(
                request.session, request.transaction.begin
            )
        first = True
        for statement in request.statements:
            result = self.mock_spanner.get_result(statement.sql)
            if first and started_transaction is not None:
                result = result_set.ResultSet(
                    self.mock_spanner.get_result(statement.sql)
                )
                result.metadata = ResultSetMetadata(result.metadata)
                result.metadata.transaction = started_transaction
            response.result_sets.append(result)
        return response

    def Read(self, request, context):
        self._requests.append(request)
        return result_set.ResultSet()

    def StreamingRead(self, request, context):
        self._requests.append(request)
        for result in [
            result_set.PartialResultSet(),
            result_set.PartialResultSet(),
        ]:
            yield result

    def BeginTransaction(self, request, context):
        self._requests.append(request)
        return self.__create_transaction(request.session, request.options)

    def __create_transaction(
        self, session: str, options: TransactionOptions
    ) -> transaction.Transaction:
        session = self.sessions[session]
        if session is None:
            raise ValueError(f"Session not found: {session}")
        self.transaction_counter += 1
        id_bytes = bytes(
            f"{session.name}/transactions/{self.transaction_counter}", "UTF-8"
        )
        transaction_id = base64.urlsafe_b64encode(id_bytes)
        self.transactions[transaction_id] = options
        return transaction.Transaction(dict(id=transaction_id))

    def Commit(self, request, context):
        self._requests.append(request)
        tx = self.transactions[request.transaction_id]
        if tx is None:
            raise ValueError(f"Transaction not found: {request.transaction_id}")
        del self.transactions[request.transaction_id]
        return commit.CommitResponse()

    def Rollback(self, request, context):
        self._requests.append(request)
        return empty_pb2.Empty()

    def PartitionQuery(self, request, context):
        self._requests.append(request)
        return spanner.PartitionResponse()

    def PartitionRead(self, request, context):
        self._requests.append(request)
        return spanner.PartitionResponse()

    def BatchWrite(self, request, context):
        self._requests.append(request)
        for result in [
            spanner.BatchWriteResponse(),
            spanner.BatchWriteResponse(),
        ]:
            yield result


def start_mock_server() -> (
    grpc.Server,
    SpannerServicer,
    DatabaseAdminServicer,
    int,
):
    # Create a gRPC server.
    spanner_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the Spanner services to the gRPC server.
    spanner_servicer = SpannerServicer()
    spanner_grpc.add_SpannerServicer_to_server(spanner_servicer, spanner_server)
    database_admin_servicer = DatabaseAdminServicer()
    database_admin_grpc.add_DatabaseAdminServicer_to_server(
        database_admin_servicer, spanner_server
    )

    # Start the server on a random port.
    port = spanner_server.add_insecure_port("[::]:0")
    spanner_server.start()
    return spanner_server, spanner_servicer, database_admin_servicer, port
