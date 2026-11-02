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

import uuid
from unittest import mock

import google.cloud.spanner_v1.types.result_set as result_set
import google.cloud.spanner_v1.types.type as spanner_type
import sqlalchemy
from google.cloud.spanner_v1 import (
    CommitRequest,
    CreateSessionRequest,
    ExecuteSqlRequest,
    RollbackRequest,
)
from sqlalchemy.orm import Session
from sqlalchemy.testing import eq_, is_instance_of, is_not_none

from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_result,
)


class TestInsertmany(MockServerTestBase):
    @mock.patch.object(uuid, "uuid4", mock.MagicMock(side_effect=["a", "b"]))
    def test_insertmany_with_uuid_sentinels(self):
        """Ensures one bulk insert for ORM objects distinguished by uuid."""
        from tests.mockserver_tests.insertmany_model import SingerUUID

        self.add_uuid_insert_result(
            "INSERT INTO singers_uuid (id, name) "
            "VALUES (@a0, @a1), (@a2, @a3) "
            "THEN RETURN inserted_at, id"
        )
        engine = self.create_engine()

        with Session(engine) as session:
            session.add(SingerUUID(name="a"))
            session.add(SingerUUID(name="b"))
            session.commit()

        # Verify the requests that we got.
        requests = self.spanner_service.requests
        # Dialect now inlines BeginTransaction into the first statement.
        eq_(3, len(requests))
        is_instance_of(requests[0], CreateSessionRequest)
        is_instance_of(requests[1], ExecuteSqlRequest)
        is_instance_of(requests[2], CommitRequest)
        is_not_none(requests[1].transaction.begin)  # First request inlines begin

    def test_no_insertmany_with_bit_reversed_id(self):
        """Ensures we don't try to bulk insert rows with bit-reversed PKs.

        SQLAlchemy's insertmany support requires either incrementing
        PKs or client-side supplied sentinel values such as UUIDs.
        Spanner's bit-reversed integer PKs don't meet the ordering
        requirement, so we need to make sure we don't try to bulk
        insert with them.
        """
        from tests.mockserver_tests.insertmany_model import SingerIntID

        self.add_int_id_insert_result(
            "INSERT INTO singers_int_id (name) VALUES (@a0) THEN RETURN id, inserted_at"
        )
        engine = self.create_engine()

        with Session(engine) as session:
            session.add(SingerIntID(name="a"))
            session.add(SingerIntID(name="b"))
            try:
                session.commit()
            except sqlalchemy.exc.SAWarning:
                # This will fail because we're returning the same PK
                # for two rows. The mock server doesn't currently
                # support associating the same query with two
                # different results. For our purposes that's okay --
                # we just want to ensure we generate two INSERTs, not
                # one.
                pass

        # Verify the requests that we got.
        requests = self.spanner_service.requests
        # Dialect now inlines BeginTransaction into the first statement.
        eq_(4, len(requests))
        is_instance_of(requests[0], CreateSessionRequest)
        is_instance_of(requests[1], ExecuteSqlRequest)
        is_instance_of(requests[2], ExecuteSqlRequest)
        is_instance_of(requests[3], RollbackRequest)
        is_not_none(requests[1].transaction.begin)  # First request inlines begin

    def add_uuid_insert_result(self, sql):
        result = result_set.ResultSet(
            dict(
                metadata=result_set.ResultSetMetadata(
                    dict(
                        row_type=spanner_type.StructType(
                            dict(
                                fields=[
                                    spanner_type.StructType.Field(
                                        dict(
                                            name="inserted_at",
                                            type=spanner_type.Type(
                                                dict(
                                                    code=spanner_type.TypeCode.TIMESTAMP
                                                )
                                            ),
                                        )
                                    ),
                                    spanner_type.StructType.Field(
                                        dict(
                                            name="id",
                                            type=spanner_type.Type(
                                                dict(code=spanner_type.TypeCode.STRING)
                                            ),
                                        )
                                    ),
                                ]
                            )
                        )
                    )
                ),
            )
        )
        result.rows.extend(
            [
                (
                    "2020-06-02T23:58:40Z",
                    "a",
                ),
                (
                    "2020-06-02T23:58:41Z",
                    "b",
                ),
            ]
        )
        add_result(sql, result)

    def add_int_id_insert_result(self, sql):
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
                                    ),
                                    spanner_type.StructType.Field(
                                        dict(
                                            name="inserted_at",
                                            type=spanner_type.Type(
                                                dict(
                                                    code=spanner_type.TypeCode.TIMESTAMP
                                                )
                                            ),
                                        )
                                    ),
                                ]
                            )
                        )
                    )
                ),
            )
        )
        result.rows.extend(
            [
                (
                    "1",
                    "2020-06-02T23:58:40Z",
                ),
            ]
        )
        add_result(sql, result)
