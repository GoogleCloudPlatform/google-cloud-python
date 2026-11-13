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

from google.cloud.spanner_v1 import (
    BatchCreateSessionsRequest,
    BurstyPool,
    CreateSessionRequest,
    FixedSizePool,
    PingingPool,
)
from tests.mockserver_tests.mock_server_test_base import MockServerTestBase


class TestPoolBinding(MockServerTestBase):
    def test_database_binding_of_fixed_size_pool(self):
        pool = FixedSizePool(
            size=1,
            default_timeout=500,
            database_role="parent",
        )
        database = self.instance.database("fixed_size_db", pool=pool)
        self.assertEqual(database._pool.database_role, "parent")
        self.assertIs(database._pool._database, database)

        # Verify that BatchCreateSessions was called with the creator_role.
        batch_create_requests = [
            request
            for request in self.spanner_service.requests
            if isinstance(request, BatchCreateSessionsRequest)
        ]
        self.assertEqual(len(batch_create_requests), 1)
        self.assertEqual(
            batch_create_requests[0].session_template.creator_role, "parent"
        )

        # Verify that a session checked out from the pool has the database_role
        # and matches the server-side session created with creator_role.
        session = pool.get()
        try:
            self.assertEqual(session.database_role, "parent")
            self.assertIn(session.name, self.spanner_service.sessions)
            server_session = self.spanner_service.sessions[session.name]
            self.assertEqual(server_session.creator_role, "parent")
        finally:
            pool.put(session)

    def test_database_binding_of_pinging_pool(self):
        pool = PingingPool(
            size=1,
            default_timeout=500,
            ping_interval=100,
            database_role="parent",
        )
        database = self.instance.database("binding_db", pool=pool)
        self.assertEqual(database._pool.database_role, "parent")
        self.assertIs(database._pool._database, database)

        # Verify that BatchCreateSessions was called with the creator_role.
        batch_create_requests = [
            request
            for request in self.spanner_service.requests
            if isinstance(request, BatchCreateSessionsRequest)
        ]
        self.assertEqual(len(batch_create_requests), 1)
        self.assertEqual(
            batch_create_requests[0].session_template.creator_role, "parent"
        )

        # Verify that a session checked out from the pool has the database_role
        # and matches the server-side session created with creator_role.
        session = pool.get()
        try:
            self.assertEqual(session.database_role, "parent")
            self.assertIn(session.name, self.spanner_service.sessions)
            server_session = self.spanner_service.sessions[session.name]
            self.assertEqual(server_session.creator_role, "parent")
        finally:
            pool.put(session)

    def test_database_binding_of_bursty_pool(self):
        pool = BurstyPool(
            target_size=1,
            database_role="parent",
        )
        database = self.instance.database("bursty_db", pool=pool)
        self.assertEqual(database._pool.database_role, "parent")
        self.assertIs(database._pool._database, database)

    def test_database_binding_with_database_role_on_database(self):
        pool = FixedSizePool(
            size=1,
            default_timeout=500,
        )
        database = self.instance.database(
            "db_role_on_database", pool=pool, database_role="parent"
        )
        self.assertEqual(database._pool.database_role, "parent")
        self.assertIs(database._pool._database, database)

        batch_create_requests = [
            request
            for request in self.spanner_service.requests
            if isinstance(request, BatchCreateSessionsRequest)
        ]
        self.assertEqual(len(batch_create_requests), 1)
        self.assertEqual(
            batch_create_requests[0].session_template.creator_role, "parent"
        )

        session = pool.get()
        try:
            self.assertEqual(session.database_role, "parent")
            self.assertIn(session.name, self.spanner_service.sessions)
            server_session = self.spanner_service.sessions[session.name]
            self.assertEqual(server_session.creator_role, "parent")
        finally:
            pool.put(session)

    def test_database_binding_pinging_pool_inherits_database_role(self):
        pool = PingingPool(
            size=1,
            default_timeout=500,
            ping_interval=100,
        )
        database = self.instance.database(
            "pinging_inherits_db", pool=pool, database_role="parent"
        )
        self.assertEqual(database._pool.database_role, "parent")
        self.assertIs(database._pool._database, database)

        batch_create_requests = [
            request
            for request in self.spanner_service.requests
            if isinstance(request, BatchCreateSessionsRequest)
        ]
        self.assertEqual(len(batch_create_requests), 1)
        self.assertEqual(
            batch_create_requests[0].session_template.creator_role, "parent"
        )

        session = pool.get()
        try:
            self.assertEqual(session.database_role, "parent")
            self.assertIn(session.name, self.spanner_service.sessions)
            server_session = self.spanner_service.sessions[session.name]
            self.assertEqual(server_session.creator_role, "parent")
        finally:
            pool.put(session)

    def test_database_binding_bursty_pool_inherits_database_role(self):
        pool = BurstyPool(
            target_size=1,
        )
        database = self.instance.database(
            "bursty_inherits_db", pool=pool, database_role="parent"
        )
        self.assertEqual(database._pool.database_role, "parent")
        self.assertIs(database._pool._database, database)

        session = pool.get()
        try:
            self.assertEqual(session.database_role, "parent")
            self.assertIn(session.name, self.spanner_service.sessions)
            server_session = self.spanner_service.sessions[session.name]
            self.assertEqual(server_session.creator_role, "parent")
            create_session_requests = [
                request
                for request in self.spanner_service.requests
                if isinstance(request, CreateSessionRequest)
            ]
            self.assertEqual(len(create_session_requests), 1)
            create_session_request = create_session_requests[0]
            creator_role = create_session_request.session.creator_role
            self.assertEqual(creator_role, "parent")
        finally:
            pool.put(session)

    def test_database_binding_pool_role_precedence(self):
        pool = FixedSizePool(
            size=1,
            default_timeout=500,
            database_role="pool-role",
        )
        database = self.instance.database(
            "role_precedence_db", pool=pool, database_role="database-role"
        )
        self.assertEqual(database.database_role, "database-role")
        self.assertEqual(database._pool.database_role, "pool-role")

        batch_create_requests = [
            request
            for request in self.spanner_service.requests
            if isinstance(request, BatchCreateSessionsRequest)
        ]
        self.assertEqual(len(batch_create_requests), 1)
        self.assertEqual(
            batch_create_requests[0].session_template.creator_role, "pool-role"
        )

        session = pool.get()
        try:
            self.assertEqual(session.database_role, "pool-role")
            self.assertIn(session.name, self.spanner_service.sessions)
            server_session = self.spanner_service.sessions[session.name]
            self.assertEqual(
                server_session.creator_role,
                "pool-role",
            )
        finally:
            pool.put(session)
