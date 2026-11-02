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
import google.cloud.spanner_v1.types.result_set as result_set
import google.cloud.spanner_v1.types.type as spanner_type
import pytest
from google.cloud.spanner_v1 import (
    CommitRequest,
    CreateSessionRequest,
    ExecuteSqlRequest,
    TransactionOptions,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.testing import eq_, is_instance_of

from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_result,
)

ISOLATION_LEVEL_UNSPECIFIED = (
    TransactionOptions.IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED
)


class TestIsolationLevel(MockServerTestBase):
    def test_default_isolation_level(self):
        from tests.mockserver_tests.isolation_level_model import Singer

        self.add_insert_result("INSERT INTO singers (name) VALUES (@a0) THEN RETURN id")
        engine = self.create_engine()

        with Session(engine) as session:
            singer = Singer(name="Test")
            session.add(singer)
            session.commit()
        self.verify_isolation_level(
            TransactionOptions.IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED
        )

    def test_engine_isolation_level(self):
        from tests.mockserver_tests.isolation_level_model import Singer

        self.add_insert_result("INSERT INTO singers (name) VALUES (@a0) THEN RETURN id")
        engine = create_engine(
            "spanner:///projects/p/instances/i/databases/d",
            connect_args={"client": self.client, "logger": MockServerTestBase.logger},
            isolation_level="REPEATABLE READ",
        )

        with Session(engine) as session:
            singer = Singer(name="Test")
            session.add(singer)
            session.commit()
        self.verify_isolation_level(TransactionOptions.IsolationLevel.REPEATABLE_READ)

    def test_execution_options_isolation_level(self):
        from tests.mockserver_tests.isolation_level_model import Singer

        self.add_insert_result("INSERT INTO singers (name) VALUES (@a0) THEN RETURN id")
        engine = self.create_engine()

        with Session(
            engine.execution_options(isolation_level="repeatable read")
        ) as session:
            singer = Singer(name="Test")
            session.add(singer)
            session.commit()
        self.verify_isolation_level(TransactionOptions.IsolationLevel.REPEATABLE_READ)

    def test_override_engine_isolation_level(self):
        from tests.mockserver_tests.isolation_level_model import Singer

        self.add_insert_result("INSERT INTO singers (name) VALUES (@a0) THEN RETURN id")
        engine = create_engine(
            "spanner:///projects/p/instances/i/databases/d",
            connect_args={"client": self.client, "logger": MockServerTestBase.logger},
            isolation_level="REPEATABLE READ",
        )

        with Session(
            engine.execution_options(isolation_level="SERIALIZABLE")
        ) as session:
            singer = Singer(name="Test")
            session.add(singer)
            session.commit()
        self.verify_isolation_level(TransactionOptions.IsolationLevel.SERIALIZABLE)

    def test_auto_commit(self):
        from tests.mockserver_tests.isolation_level_model import Singer

        self.add_insert_result("INSERT INTO singers (name) VALUES (@a0) THEN RETURN id")
        engine = create_engine(
            "spanner:///projects/p/instances/i/databases/d",
            connect_args={
                "client": self.client,
                "logger": MockServerTestBase.logger,
                "ignore_transaction_warnings": True,
            },
        )

        with Session(
            engine.execution_options(
                isolation_level="AUTOCOMMIT", ignore_transaction_warnings=True
            )
        ) as session:
            singer = Singer(name="Test")
            session.add(singer)
            session.commit()

        # Verify the requests that we got.
        requests = self.spanner_service.requests
        eq_(3, len(requests))
        is_instance_of(requests[0], CreateSessionRequest)
        is_instance_of(requests[1], ExecuteSqlRequest)
        is_instance_of(requests[2], CommitRequest)
        execute_request: ExecuteSqlRequest = requests[1]
        eq_(
            TransactionOptions(
                dict(
                    isolation_level=ISOLATION_LEVEL_UNSPECIFIED,
                    read_write=TransactionOptions.ReadWrite(),
                )
            ),
            execute_request.transaction.begin,
        )

    def test_invalid_isolation_level(self):
        from tests.mockserver_tests.isolation_level_model import Singer

        engine = self.create_engine()
        with pytest.raises(ValueError):
            with Session(engine.execution_options(isolation_level="foo")) as session:
                singer = Singer(name="Test")
                session.add(singer)
                session.commit()

    def verify_isolation_level(self, level):
        # Verify the requests that we got.
        requests = self.spanner_service.requests
        # Dialect now inlines BeginTransaction into the first statement.
        eq_(3, len(requests))
        is_instance_of(requests[0], CreateSessionRequest)
        is_instance_of(requests[1], ExecuteSqlRequest)
        is_instance_of(requests[2], CommitRequest)
        execute_request: ExecuteSqlRequest = requests[1]
        eq_(
            TransactionOptions(
                dict(
                    isolation_level=level,
                    read_write=TransactionOptions.ReadWrite(),
                )
            ),
            execute_request.transaction.begin,
        )

    def add_insert_result(self, sql):
        result = result_set.ResultSet(
            dict(
                metadata=result_set.ResultSetMetadata(
                    dict(
                        row_type=spanner_type.StructType(
                            dict(
                                fields=[
                                    spanner_type.StructType.Field(
                                        dict(
                                            name="id",
                                            type=spanner_type.Type(
                                                dict(code=spanner_type.TypeCode.INT64)
                                            ),
                                        )
                                    )
                                ]
                            )
                        )
                    )
                ),
                stats=result_set.ResultSetStats(
                    dict(
                        row_count_exact=1,
                    )
                ),
            )
        )
        result.rows.extend([("987654321",)])
        add_result(sql, result)
