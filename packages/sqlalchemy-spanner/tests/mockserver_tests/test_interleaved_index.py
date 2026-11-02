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

from google.cloud.spanner_admin_database_v1 import UpdateDatabaseDdlRequest
from google.cloud.spanner_v1 import (
    FixedSizePool,
    ResultSet,
)
from sqlalchemy import create_engine
from sqlalchemy.testing import eq_, is_instance_of

from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_result,
)


class TestNullFilteredIndex(MockServerTestBase):
    """Ensure we emit correct DDL for not null filtered indexes."""

    def test_create_table(self):
        from tests.mockserver_tests.interleaved_index import Base

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
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA="" AND TABLE_NAME="albums"
LIMIT 1
""",
            ResultSet(),
        )
        add_result(
            """SELECT true
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA="" AND TABLE_NAME="tracks"
LIMIT 1
""",
            ResultSet(),
        )
        engine = create_engine(
            "spanner:///projects/p/instances/i/databases/d",
            connect_args={"client": self.client, "pool": FixedSizePool(size=10)},
        )
        Base.metadata.create_all(engine)
        requests = self.database_admin_service.requests
        eq_(1, len(requests))
        is_instance_of(requests[0], UpdateDatabaseDdlRequest)
        eq_(4, len(requests[0].statements))
        eq_(
            "CREATE TABLE singers (\n"
            "\tsinger_id STRING(36) NOT NULL, \n"
            "\tfirst_name STRING(MAX) NOT NULL, \n"
            "\tlast_name STRING(MAX) NOT NULL\n"
            ") PRIMARY KEY (singer_id)",
            requests[0].statements[0],
        )
        eq_(
            "CREATE TABLE albums (\n"
            "\tsinger_id STRING(36) NOT NULL, \n"
            "\talbum_id STRING(36) NOT NULL, \n"
            "\talbum_title STRING(MAX) NOT NULL, \n"
            "\tFOREIGN KEY(singer_id) REFERENCES singers (singer_id)\n"
            ") PRIMARY KEY (singer_id, album_id),\n"
            "INTERLEAVE IN PARENT singers ON DELETE CASCADE",
            requests[0].statements[1],
        )
        eq_(
            "CREATE TABLE tracks (\n"
            "\tsinger_id STRING(36) NOT NULL, \n"
            "\talbum_id STRING(36) NOT NULL, \n"
            "\ttrack_id STRING(36) NOT NULL, \n"
            "\tsong_name STRING(MAX) NOT NULL, \n"
            "\tFOREIGN KEY(singer_id) REFERENCES singers (singer_id), \n"
            "\tFOREIGN KEY(album_id) REFERENCES albums (album_id)\n"
            ") PRIMARY KEY (singer_id, album_id, track_id),\n"
            "INTERLEAVE IN PARENT albums ON DELETE CASCADE",
            requests[0].statements[2],
        )
        eq_(
            "CREATE INDEX idx_name ON tracks "
            "(singer_id, album_id, song_name), "
            "INTERLEAVE IN albums",
            requests[0].statements[3],
        )
