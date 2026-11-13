# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
#
import datetime
import os
import uuid

import pytest

TEST_FAMILY = "test-family"
TEST_FAMILY_2 = "test-family-2"
TEST_AGGREGATE_FAMILY = "test-aggregate-family"

# authorized view subset to allow all qualifiers
ALLOW_ALL = ""
ALL_QUALIFIERS = {"qualifier_prefixes": [ALLOW_ALL]}


class SystemTestRunner:
    """
    configures a system test class with configuration for clusters/tables/etc

    used by standard system tests, and metrics tests
    """

    @pytest.fixture(scope="session", autouse=True)
    def cleanup_old_instances(self, project_id):
        """
        Automatically deletes any test instances older than 1 day.
        """
        from google.cloud.environment_vars import BIGTABLE_EMULATOR

        from tests.system.utils import clear_stale_instances

        if os.getenv(BIGTABLE_EMULATOR):
            return

        clear_stale_instances(project_id, "python-bigtable-tests", older_than_days=1)

    @pytest.fixture(scope="session")
    def init_table_id(self, start_timestamp):
        """
        The table_id to use when creating a new test table

        Args
            start_timestamp: accessed when building table to ensure timestamp data is loaded before tests are run
        """
        return f"test-table-{uuid.uuid4().hex}"

    @pytest.fixture(scope="session")
    def cluster_config(self, project_id):
        """
        Configuration for the clusters to use when creating a new instance
        """
        from google.cloud.bigtable_admin_v2 import types

        cluster = {
            "test-cluster": types.Cluster(
                location=f"projects/{project_id}/locations/us-central1-b",
                serve_nodes=1,
            )
        }
        return cluster

    @pytest.fixture(scope="session")
    def column_family_config(self):
        """
        specify column families to create when creating a new test table
        """
        from google.cloud.bigtable_admin_v2 import types

        int_aggregate_type = types.Type.Aggregate(
            input_type=types.Type(int64_type={"encoding": {"big_endian_bytes": {}}}),
            sum={},
        )
        return {
            TEST_FAMILY: types.ColumnFamily(),
            TEST_FAMILY_2: types.ColumnFamily(),
            TEST_AGGREGATE_FAMILY: types.ColumnFamily(
                value_type=types.Type(aggregate_type=int_aggregate_type)
            ),
        }

    @pytest.fixture(scope="session")
    def start_timestamp(self):
        """
        A timestamp taken before any tests are run. Used to fetch back metrics relevant to the tests
        """
        return datetime.datetime.now(datetime.timezone.utc)

    @pytest.fixture(scope="session")
    def admin_client(self):
        """
        Client for interacting with Table and Instance admin APIs
        """
        from google.cloud.bigtable.client import Client

        client = Client(admin=True)
        yield client

    @pytest.fixture(scope="session")
    def instance_id(self, admin_client, project_id, cluster_config):
        """
        Returns BIGTABLE_TEST_INSTANCE if set, otherwise creates a new temporary instance for the test session
        """
        from google.api_core import exceptions
        from google.cloud.environment_vars import BIGTABLE_EMULATOR

        from google.cloud.bigtable_admin_v2 import types

        # use user-specified instance if available
        user_specified_instance = os.getenv("BIGTABLE_TEST_INSTANCE")
        if user_specified_instance:
            print("Using user-specified instance: {}".format(user_specified_instance))
            yield user_specified_instance
            return

        # create a new temporary test instance
        instance_id = f"python-bigtable-tests-{uuid.uuid4().hex[:6]}"
        if os.getenv(BIGTABLE_EMULATOR):
            # don't create instance if in emulator mode
            yield instance_id
        else:
            try:
                try:
                    operation = admin_client.instance_admin_client.create_instance(
                        parent=f"projects/{project_id}",
                        instance_id=instance_id,
                        instance=types.Instance(
                            display_name="Test Instance",
                            # labels={"python-system-test": "true"},
                        ),
                        clusters=cluster_config,
                    )
                    operation.result(timeout=240)
                except exceptions.AlreadyExists:
                    pass
                yield instance_id
            finally:
                try:
                    admin_client.instance_admin_client.delete_instance(
                        name=f"projects/{project_id}/instances/{instance_id}"
                    )
                except Exception as e:
                    print(f"Failed to delete instance {instance_id}: {e}")

    @pytest.fixture(scope="session")
    def column_split_config(self):
        """
        specify initial splits to create when creating a new test table
        """
        return [(num * 1000).to_bytes(8, "big") for num in range(1, 10)]

    @pytest.fixture(scope="session")
    def table_id(
        self,
        admin_client,
        project_id,
        instance_id,
        column_family_config,
        init_table_id,
        column_split_config,
    ):
        """
        Returns BIGTABLE_TEST_TABLE if set, otherwise creates a new temporary table for the test session

        Args:
          - admin_client: Client for interacting with the Table Admin API. Supplied by the admin_client fixture.
          - project_id: The project ID of the GCP project to test against. Supplied by the project_id fixture.
          - instance_id: The ID of the Bigtable instance to test against. Supplied by the instance_id fixture.
          - init_column_families: A list of column families to initialize the table with, if pre-initialized table is not given with BIGTABLE_TEST_TABLE.
                Supplied by the init_column_families fixture.
          - init_table_id: The table ID to give to the test table, if pre-initialized table is not given with BIGTABLE_TEST_TABLE.
                Supplied by the init_table_id fixture.
          - column_split_config: A list of row keys to use as initial splits when creating the test table.
        """
        from google.api_core import exceptions, retry

        # use user-specified instance if available
        user_specified_table = os.getenv("BIGTABLE_TEST_TABLE")
        if user_specified_table:
            print("Using user-specified table: {}".format(user_specified_table))
            yield user_specified_table
            return

        retry = retry.Retry(
            predicate=retry.if_exception_type(exceptions.FailedPrecondition)
        )
        parent_path = f"projects/{project_id}/instances/{instance_id}"
        try:
            try:
                print(f"Creating table: {parent_path}/tables/{init_table_id}")
                admin_client.table_admin_client.create_table(
                    request={
                        "parent": parent_path,
                        "table_id": init_table_id,
                        "table": {"column_families": column_family_config},
                        "initial_splits": [{"key": key} for key in column_split_config],
                    },
                    retry=retry,
                )
            except exceptions.AlreadyExists:
                pass
            yield init_table_id
        finally:
            print(f"Deleting table: {parent_path}/tables/{init_table_id}")
            try:
                admin_client.table_admin_client.delete_table(
                    name=f"{parent_path}/tables/{init_table_id}"
                )
            except Exception as e:
                print(f"Failed to delete table {init_table_id}: {e}")

    @pytest.fixture(scope="session")
    def authorized_view_id(
        self,
        admin_client,
        project_id,
        instance_id,
        table_id,
    ):
        """
        Creates and returns a new temporary authorized view for the test session

        Args:
          - admin_client: Client for interacting with the Table Admin API. Supplied by the admin_client fixture.
          - project_id: The project ID of the GCP project to test against. Supplied by the project_id fixture.
          - instance_id: The ID of the Bigtable instance to test against. Supplied by the instance_id fixture.
          - table_id: The ID of the table to create the authorized view for. Supplied by the table_id fixture.
        """
        from google.api_core import exceptions, retry

        retry = retry.Retry(
            predicate=retry.if_exception_type(exceptions.FailedPrecondition)
        )
        new_view_id = uuid.uuid4().hex[:8]
        parent_path = f"projects/{project_id}/instances/{instance_id}/tables/{table_id}"
        new_path = f"{parent_path}/authorizedViews/{new_view_id}"
        try:
            try:
                print(f"Creating view: {new_path}")
                admin_client.table_admin_client.create_authorized_view(
                    request={
                        "parent": parent_path,
                        "authorized_view_id": new_view_id,
                        "authorized_view": {
                            "subset_view": {
                                "row_prefixes": [ALLOW_ALL],
                                "family_subsets": {
                                    TEST_FAMILY: ALL_QUALIFIERS,
                                    TEST_FAMILY_2: ALL_QUALIFIERS,
                                    TEST_AGGREGATE_FAMILY: ALL_QUALIFIERS,
                                },
                            },
                        },
                    },
                    retry=retry,
                )
            except exceptions.AlreadyExists:
                pass
            except exceptions.MethodNotImplemented:
                # will occur when run in emulator. Pass empty id
                new_view_id = None
            yield new_view_id
        finally:
            if new_view_id:
                print(f"Deleting view: {new_path}")
                try:
                    admin_client.table_admin_client.delete_authorized_view(
                        name=new_path
                    )
                except Exception as e:
                    print(f"Failed to delete view {new_view_id}: {e}")

    @pytest.fixture(scope="session")
    def project_id(self, client):
        """Returns the project ID from the client."""
        yield client.project
