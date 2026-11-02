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

from google.cloud.spanner_v1 import (
    BeginTransactionRequest,
    CreateSessionRequest,
    ExecuteSqlRequest,
    TransactionOptions,
)
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.testing import eq_, is_instance_of

from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_singer_query_result,
)


class TestStaleReads(MockServerTestBase):
    def test_stale_read_multi_use(self):
        from tests.mockserver_tests.stale_read_model import Singer

        add_singer_query_result("SELECT singers.id, singers.name \nFROM singers")
        engine = self.create_engine()

        timestamp = datetime.datetime.fromtimestamp(1733328910)
        for i in range(2):
            with Session(
                engine.execution_options(
                    read_only=True,
                    staleness={"read_timestamp": timestamp},
                )
            ) as session:
                # Execute two queries in a read-only transaction.
                session.scalars(select(Singer)).all()
                session.scalars(select(Singer)).all()

        # Verify the requests that we got.
        requests = self.spanner_service.requests
        eq_(7, len(requests))
        is_instance_of(requests[0], CreateSessionRequest)
        is_instance_of(requests[1], BeginTransactionRequest)
        is_instance_of(requests[2], ExecuteSqlRequest)
        is_instance_of(requests[3], ExecuteSqlRequest)
        is_instance_of(requests[4], BeginTransactionRequest)
        is_instance_of(requests[5], ExecuteSqlRequest)
        is_instance_of(requests[6], ExecuteSqlRequest)
        # Verify that the transaction is a read-only transaction.
        for index in [1, 4]:
            begin_request: BeginTransactionRequest = requests[index]
            eq_(
                TransactionOptions(
                    dict(
                        read_only=TransactionOptions.ReadOnly(
                            dict(
                                read_timestamp={"seconds": 1733328910},
                                return_read_timestamp=True,
                            )
                        )
                    )
                ),
                begin_request.options,
            )

    def test_stale_read_single_use(self):
        from tests.mockserver_tests.stale_read_model import Singer

        add_singer_query_result("SELECT singers.id, singers.name \nFROM singers")
        engine = self.create_engine()

        with Session(
            engine.execution_options(
                isolation_level="AUTOCOMMIT",
                staleness={"max_staleness": {"seconds": 15}},
            )
        ) as session:
            # Execute two queries in autocommit.
            session.scalars(select(Singer)).all()
            session.scalars(select(Singer)).all()

        # Verify the requests that we got.
        requests = self.spanner_service.requests
        eq_(3, len(requests))
        is_instance_of(requests[0], CreateSessionRequest)
        is_instance_of(requests[1], ExecuteSqlRequest)
        is_instance_of(requests[2], ExecuteSqlRequest)
        # Verify that the requests use a stale read.
        for index in [1, 2]:
            execute_request: ExecuteSqlRequest = requests[index]
            eq_(
                TransactionOptions(
                    dict(
                        read_only=TransactionOptions.ReadOnly(
                            dict(
                                max_staleness={"seconds": 15},
                                return_read_timestamp=True,
                            )
                        )
                    )
                ),
                execute_request.transaction.single_use,
            )
