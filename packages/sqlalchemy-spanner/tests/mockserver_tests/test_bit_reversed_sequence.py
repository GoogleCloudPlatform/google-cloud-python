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

import google.cloud.spanner_v1.types.result_set as result_set
import google.cloud.spanner_v1.types.type as spanner_type
from google.cloud.spanner_admin_database_v1 import UpdateDatabaseDdlRequest
from google.cloud.spanner_v1 import (
    CommitRequest,
    CreateSessionRequest,
    ExecuteSqlRequest,
    ResultSet,
)
from sqlalchemy.orm import Session
from sqlalchemy.testing import eq_, is_instance_of, is_not_none

from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_result,
)


class TestBitReversedSequence(MockServerTestBase):
    def test_create_table(self):
        from tests.mockserver_tests.bit_reversed_sequence_model import Base

        add_result(
            """SELECT true
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA="" AND TABLE_NAME="singers"
LIMIT 1
""",
            ResultSet(),
        )
        add_result(
            """SELECT true
                FROM INFORMATION_SCHEMA.SEQUENCES
                WHERE NAME="singer_id"
                AND SCHEMA=""
                LIMIT 1""",
            ResultSet(),
        )
        engine = self.create_engine()
        Base.metadata.create_all(engine)
        requests = self.database_admin_service.requests
        eq_(1, len(requests))
        is_instance_of(requests[0], UpdateDatabaseDdlRequest)
        eq_(2, len(requests[0].statements))
        eq_(
            "CREATE SEQUENCE singer_id OPTIONS "
            "(sequence_kind = 'bit_reversed_positive')",
            requests[0].statements[0],
        )
        eq_(
            "CREATE TABLE singers (\n"
            "\tid INT64 NOT NULL DEFAULT "
            "(GET_NEXT_SEQUENCE_VALUE(SEQUENCE singer_id)), \n"
            "\tname STRING(MAX) NOT NULL\n"
            ") PRIMARY KEY (id)",
            requests[0].statements[1],
        )

    def test_insert_row(self):
        from tests.mockserver_tests.bit_reversed_sequence_model import Singer

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
        result.rows.extend(["1"])

        add_result(
            "INSERT INTO singers (id, name) "
            "VALUES ( GET_NEXT_SEQUENCE_VALUE(SEQUENCE singer_id), @a0) "
            "THEN RETURN id",
            result,
        )
        engine = self.create_engine()

        with Session(engine) as session:
            singer = Singer(name="Test")
            session.add(singer)
            # Flush the session to send the insert statement to the database.
            session.flush()
            eq_(1, singer.id)
            session.commit()
        # Verify the requests that we got.
        requests = self.spanner_service.requests
        # Dialect now inlines BeginTransaction into the first statement.
        eq_(3, len(requests))
        is_instance_of(requests[0], CreateSessionRequest)
        is_instance_of(requests[1], ExecuteSqlRequest)
        is_instance_of(requests[2], CommitRequest)
        is_not_none(requests[1].transaction.begin)  # First request inlines begin
