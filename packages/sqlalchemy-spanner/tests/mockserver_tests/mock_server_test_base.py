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
import logging

import google.cloud.spanner_v1.types.result_set as result_set
import google.cloud.spanner_v1.types.type as spanner_type
import grpc
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.cloud.spanner_dbapi.parsed_statement import AutocommitDmlMode
from google.cloud.spanner_v1 import (
    Client,
    ResultSet,
    TypeCode,
)
from google.cloud.spanner_v1.database import Database
from google.cloud.spanner_v1.instance import Instance
from sqlalchemy import Engine, create_engine
from sqlalchemy.testing.plugin.plugin_base import fixtures

from tests.mockserver_tests.mock_database_admin import DatabaseAdminServicer

# TODO: Replace this with the mock server in the Spanner client lib
from tests.mockserver_tests.mock_spanner import SpannerServicer, start_mock_server


def add_result(sql: str, result: ResultSet):
    MockServerTestBase.spanner_service.mock_spanner.add_result(sql, result)


def add_update_count(
    sql: str, count: int, dml_mode: AutocommitDmlMode = AutocommitDmlMode.TRANSACTIONAL
):
    if dml_mode == AutocommitDmlMode.PARTITIONED_NON_ATOMIC:
        stats = dict(row_count_lower_bound=count)
    else:
        stats = dict(row_count_exact=count)
    result = result_set.ResultSet(dict(stats=result_set.ResultSetStats(stats)))
    add_result(sql, result)


def add_select1_result():
    add_single_result("select 1", "c", TypeCode.INT64, [("1",)])


def add_single_result(
    sql: str, column_name: str, type_code: spanner_type.TypeCode, row
):
    result = result_set.ResultSet(
        dict(
            metadata=result_set.ResultSetMetadata(
                dict(
                    row_type=spanner_type.StructType(
                        dict(
                            fields=[
                                spanner_type.StructType.Field(
                                    dict(
                                        name=column_name,
                                        type=spanner_type.Type(dict(code=type_code)),
                                    )
                                )
                            ]
                        )
                    )
                )
            ),
        )
    )
    result.rows.extend(row)
    MockServerTestBase.spanner_service.mock_spanner.add_result(sql, result)


def add_singer_query_result(sql: str):
    result = result_set.ResultSet(
        dict(
            metadata=result_set.ResultSetMetadata(
                dict(
                    row_type=spanner_type.StructType(
                        dict(
                            fields=[
                                spanner_type.StructType.Field(
                                    dict(
                                        name="singers_id",
                                        type=spanner_type.Type(
                                            dict(code=spanner_type.TypeCode.INT64)
                                        ),
                                    )
                                ),
                                spanner_type.StructType.Field(
                                    dict(
                                        name="singers_name",
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
                "1",
                "Jane Doe",
            ),
            (
                "2",
                "John Doe",
            ),
        ]
    )
    add_result(sql, result)


class MockServerTestBase(fixtures.TestBase):
    server: grpc.Server = None
    spanner_service: SpannerServicer = None
    database_admin_service: DatabaseAdminServicer = None
    port: int = None
    logger: logging.Logger = None

    @classmethod
    def setup_class(cls):
        MockServerTestBase.logger = logging.getLogger("level warning")
        MockServerTestBase.logger.setLevel(logging.WARN)
        (
            MockServerTestBase.server,
            MockServerTestBase.spanner_service,
            MockServerTestBase.database_admin_service,
            MockServerTestBase.port,
        ) = start_mock_server()

    @classmethod
    def teardown_class(cls):
        if MockServerTestBase.server is not None:
            MockServerTestBase.server.stop(grace=None)
            MockServerTestBase.server = None

    def setup_method(self):
        self._client = None
        self._instance = None
        self._database = None
        _ = self.database

    def teardown_method(self):
        MockServerTestBase.spanner_service.clear_requests()
        MockServerTestBase.database_admin_service.clear_requests()

    def create_engine(self) -> Engine:
        return create_engine(
            "spanner:///projects/p/instances/i/databases/d",
            connect_args={"client": self.client, "logger": MockServerTestBase.logger},
        )

    @property
    def client(self) -> Client:
        if self._client is None:
            self._client = Client(
                project="p",
                credentials=AnonymousCredentials(),
                client_options=ClientOptions(
                    api_endpoint="localhost:" + str(MockServerTestBase.port),
                ),
            )
        return self._client

    @property
    def instance(self) -> Instance:
        if self._instance is None:
            self._instance = self.client.instance("i")
        return self._instance

    @property
    def database(self) -> Database:
        logger = logging.getLogger("level warning")
        logger.setLevel(logging.WARN)
        if self._database is None:
            self._database = self.instance.database("d", logger=logger)
        return self._database
