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

import os
import unittest

import google.cloud.spanner_v1.types.result_set as result_set
import google.cloud.spanner_v1.types.type as spanner_type
import grpc
from django.db import connections
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.cloud.spanner_dbapi.parsed_statement import AutocommitDmlMode
from google.cloud.spanner_v1 import (
    Client,
    PingingPool,
    ResultSet,
    TypeCode,
)
from google.cloud.spanner_v1.database import Database
from google.cloud.spanner_v1.instance import Instance

from tests.mockserver_tests.mock_database_admin import DatabaseAdminServicer

# TODO: Replace this with the mock server in the Spanner client lib
from tests.mockserver_tests.mock_spanner import (
    SpannerServicer,
    start_mock_server,
)
from tests.settings import DATABASES


def add_result(sql: str, result: ResultSet):
    MockServerTestBase.spanner_service.mock_spanner.add_result(sql, result)


def add_update_count(
    sql: str,
    count: int,
    dml_mode: AutocommitDmlMode = AutocommitDmlMode.TRANSACTIONAL,
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
                                        name="id",
                                        type=spanner_type.Type(
                                            dict(code=spanner_type.TypeCode.INT64)
                                        ),
                                    )
                                ),
                                spanner_type.StructType.Field(
                                    dict(
                                        name="first_name",
                                        type=spanner_type.Type(
                                            dict(code=spanner_type.TypeCode.STRING)
                                        ),
                                    )
                                ),
                                spanner_type.StructType.Field(
                                    dict(
                                        name="last_name",
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
                "Jane",
                "Doe",
            ),
            (
                "2",
                "John",
                "Doe",
            ),
        ]
    )
    add_result(sql, result)


class MockServerTestBase(unittest.TestCase):
    server: grpc.Server = None
    spanner_service: SpannerServicer = None
    database_admin_service: DatabaseAdminServicer = None
    port: int = None
    _client = None
    _instance = None
    _database = None
    _pool = None

    @classmethod
    def setup_class(cls):
        cls._original_emulator_host = os.environ.pop("SPANNER_EMULATOR_HOST", None)
        os.environ["GOOGLE_CLOUD_PROJECT"] = "mockserver-project"
        (
            MockServerTestBase.server,
            MockServerTestBase.spanner_service,
            MockServerTestBase.database_admin_service,
            MockServerTestBase.port,
        ) = start_mock_server()

    @classmethod
    def teardown_class(cls):
        if cls._original_emulator_host is not None:
            os.environ["SPANNER_EMULATOR_HOST"] = cls._original_emulator_host
        if MockServerTestBase.server is not None:
            MockServerTestBase.server.stop(grace=None)
            MockServerTestBase.server = None

    def setup_method(self, test_method):
        for db, config in DATABASES.items():
            if config["ENGINE"] == "django_spanner":
                connections[db].settings_dict["OPTIONS"]["client"] = self.client
                connections[db].settings_dict["OPTIONS"]["pool"] = self.pool

    def teardown_method(self, test_method):
        for db, config in DATABASES.items():
            if config["ENGINE"] == "django_spanner":
                connections[db].close()
        MockServerTestBase.spanner_service.clear_requests()
        MockServerTestBase.database_admin_service.clear_requests()
        self._client = None
        self._instance = None
        self._database = None
        self._pool = None

    @property
    def client(self) -> Client:
        if self._client is None:
            self._client = Client(
                project=os.environ["GOOGLE_CLOUD_PROJECT"],
                credentials=AnonymousCredentials(),
                client_options=ClientOptions(
                    api_endpoint="localhost:" + str(MockServerTestBase.port),
                ),
            )
        return self._client

    @property
    def pool(self):
        if self._pool is None:
            self._pool = PingingPool(size=10)
        return self._pool

    @property
    def instance(self) -> Instance:
        if self._instance is None:
            self._instance = self.client.instance("test-instance")
        return self._instance

    @property
    def database(self) -> Database:
        if self._database is None:
            self._database = self.instance.database(
                "test-database", pool=PingingPool(size=10)
            )
        return self._database
