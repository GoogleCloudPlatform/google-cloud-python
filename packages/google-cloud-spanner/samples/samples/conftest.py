# Copyright 2021 Google LLC All rights reserved.
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
"""Shared pytest fixtures."""

import time
import uuid

from google.api_core import exceptions
from google.cloud import spanner_admin_database_v1
from google.cloud.spanner_admin_database_v1.types.common import DatabaseDialect
from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
from google.cloud.spanner_v1 import backup, client, database, instance
import pytest
from test_utils import retry

INSTANCE_CREATION_TIMEOUT = 560  # seconds

OPERATION_TIMEOUT_SECONDS = 120  # seconds

retry_429 = retry.RetryErrors(exceptions.ResourceExhausted, delay=15)
retry_cleanup = retry.RetryErrors(
    (exceptions.ResourceExhausted, exceptions.FailedPrecondition), max_tries=6, delay=15
)


@pytest.fixture(scope="module")
def database_dialect():
    """Database dialect to be used for this sample.

    The dialect is used to initialize the dialect for the database.
    It can either be GoogleStandardSql or PostgreSql.
    """
    # By default, we consider GOOGLE_STANDARD_SQL dialect. Other specific tests
    # can override this if required.
    return DatabaseDialect.GOOGLE_STANDARD_SQL


@pytest.fixture(scope="session")
def spanner_client():
    """Shared client used across all samples in a session."""
    return client.Client()


def scrub_instance_ignore_not_found(to_scrub):
    """Robustly delete an instance, its databases, and backups."""
    try:
        for database_pb in to_scrub.list_databases():
            try:
                database.Database.from_pb(database_pb, to_scrub).drop()
            except exceptions.GoogleAPICallError:
                pass

        for backup_pb in to_scrub.list_backups():
            try:
                b = backup.Backup.from_pb(backup_pb, to_scrub)
                retry_cleanup(b.delete)()
            except exceptions.GoogleAPICallError:
                pass

        retry_cleanup(to_scrub.delete)()
    except exceptions.GoogleAPICallError:
        pass


@pytest.fixture(scope="session")
def cleanup_old_instances(spanner_client):
    """Delete instances, created by samples, that are older than 4 hours."""
    cutoff = int(time.time()) - 4 * 60 * 60
    instance_filter = "labels.cloud_spanner_samples:true"

    for instance_pb in spanner_client.list_instances(filter_=instance_filter):
        inst = instance.Instance.from_pb(instance_pb, spanner_client)

        if "created" in inst.labels:
            create_time = int(inst.labels["created"])

            if create_time <= cutoff:
                scrub_instance_ignore_not_found(inst)


@pytest.fixture(scope="session")
def instance_id():
    """Unique id for the instance used in samples."""
    return f"test-instance-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="session")
def multi_region_instance_id():
    """Unique id for the multi-region instance used in samples."""
    return f"multi-instance-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="session")
def instance_config(spanner_client):
    return "{}/instanceConfigs/{}".format(
        spanner_client.project_name, "regional-us-central1"
    )


@pytest.fixture(scope="session")
def multi_region_instance_config(spanner_client):
    return "{}/instanceConfigs/{}".format(spanner_client.project_name, "nam3")


@pytest.fixture(scope="session")
def proto_descriptor_file():
    import os

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "testdata/descriptors.pb")
    file = open(filename, "rb")
    yield file.read()
    file.close()


@pytest.fixture(scope="session")
def sample_instance(
    spanner_client,
    cleanup_old_instances,
    instance_id,
    instance_config,
):
    operation = spanner_client.instance_admin_api.create_instance(
        parent=spanner_client.project_name,
        instance_id=instance_id,
        instance=spanner_instance_admin.Instance(
            config=instance_config,
            display_name="This is a display name.",
            node_count=1,
            labels={
                "cloud_spanner_samples": "true",
                "sample_name": "shared-samples",
                "created": str(int(time.time())),
            },
            edition=spanner_instance_admin.Instance.Edition.ENTERPRISE_PLUS,  # Optional
        ),
    )
    operation.result(INSTANCE_CREATION_TIMEOUT)  # block until completion

    sample_instance = spanner_client.instance(instance_id)

    # Eventual consistency check
    retry_found = retry.RetryResult(bool)
    retry_found(sample_instance.exists)()

    yield sample_instance

    scrub_instance_ignore_not_found(sample_instance)


@pytest.fixture(scope="session")
def multi_region_instance(
    spanner_client,
    cleanup_old_instances,
    multi_region_instance_id,
    multi_region_instance_config,
):
    multi_region_instance = spanner_client.instance(
        multi_region_instance_id,
        multi_region_instance_config,
        labels={
            "cloud_spanner_samples": "true",
            "sample_name": "shared-samples",
            "created": str(int(time.time())),
        },
    )
    op = retry_429(multi_region_instance.create)()
    op.result(INSTANCE_CREATION_TIMEOUT)  # block until completion

    # Eventual consistency check
    retry_found = retry.RetryResult(bool)
    retry_found(multi_region_instance.exists)()

    yield multi_region_instance

    scrub_instance_ignore_not_found(multi_region_instance)


@pytest.fixture(scope="module")
def database_id():
    """Id for the database used in samples.

    Sample testcase modules can override as needed.
    """
    return f"my-db-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def proto_columns_database(
    spanner_client,
    sample_instance,
    proto_columns_database_id,
    proto_columns_database_ddl,
    database_dialect,
):
    if database_dialect == DatabaseDialect.GOOGLE_STANDARD_SQL:
        sample_database = sample_instance.database(
            proto_columns_database_id,
            ddl_statements=proto_columns_database_ddl,
        )

        if not sample_database.exists():
            operation = sample_database.create()
            operation.result(OPERATION_TIMEOUT_SECONDS)

        yield sample_database

        sample_database.drop()


@pytest.fixture(scope="module")
def bit_reverse_sequence_database_id():
    """Id for the database used in bit reverse sequence samples.

    Sample testcase modules can override as needed.
    """
    return "sequence-database-id"


@pytest.fixture(scope="module")
def database_ddl():
    """Sequence of DDL statements used to set up the database.

    Sample testcase modules can override as needed.
    """
    return []


def create_sample_database(
    spanner_client, sample_instance, database_id, database_ddl, database_dialect
):
    if database_dialect == DatabaseDialect.POSTGRESQL:
        sample_database = sample_instance.database(
            database_id,
            database_dialect=DatabaseDialect.POSTGRESQL,
        )

        if not sample_database.exists():
            operation = sample_database.create()
            operation.result(OPERATION_TIMEOUT_SECONDS)

        request = spanner_admin_database_v1.UpdateDatabaseDdlRequest(
            database=sample_database.name,
            statements=database_ddl,
        )

        operation = spanner_client.database_admin_api.update_database_ddl(request)
        operation.result(OPERATION_TIMEOUT_SECONDS)

        yield sample_database

        sample_database.drop()
        return

    sample_database = sample_instance.database(
        database_id,
        ddl_statements=database_ddl,
    )

    if not sample_database.exists():
        operation = sample_database.create()
        operation.result(OPERATION_TIMEOUT_SECONDS)

    yield sample_database

    sample_database.drop()


@pytest.fixture(scope="module")
def sample_database(
    spanner_client, sample_instance, database_id, database_ddl, database_dialect
):
    yield from create_sample_database(
        spanner_client, sample_instance, database_id, database_ddl, database_dialect
    )


@pytest.fixture(scope="module")
def sample_multi_region_database(
    spanner_client, multi_region_instance, database_id, database_ddl, database_dialect
):
    yield from create_sample_database(
        spanner_client,
        multi_region_instance,
        database_id,
        database_ddl,
        database_dialect,
    )


@pytest.fixture(scope="module")
def bit_reverse_sequence_database(
    spanner_client, sample_instance, bit_reverse_sequence_database_id, database_dialect
):
    if database_dialect == DatabaseDialect.POSTGRESQL:
        bit_reverse_sequence_database = sample_instance.database(
            bit_reverse_sequence_database_id,
            database_dialect=DatabaseDialect.POSTGRESQL,
        )

        if not bit_reverse_sequence_database.exists():
            operation = bit_reverse_sequence_database.create()
            operation.result(OPERATION_TIMEOUT_SECONDS)

        yield bit_reverse_sequence_database

        bit_reverse_sequence_database.drop()
        return

    bit_reverse_sequence_database = sample_instance.database(
        bit_reverse_sequence_database_id
    )

    if not bit_reverse_sequence_database.exists():
        operation = bit_reverse_sequence_database.create()
        operation.result(OPERATION_TIMEOUT_SECONDS)

    yield bit_reverse_sequence_database

    bit_reverse_sequence_database.drop()


@pytest.fixture(scope="module")
def kms_key_name(spanner_client):
    return "projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}".format(
        spanner_client.project,
        "us-central1",
        "spanner-test-keyring",
        "spanner-test-cmek",
    )


@pytest.fixture(scope="module")
def kms_key_names(spanner_client):
    kms_key_names_list = []
    # this list of cloud-regions correspond to `nam3`
    for cloud_region in ["us-east1", "us-east4", "us-central1"]:
        kms_key_names_list.append(
            "projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}".format(
                spanner_client.project,
                cloud_region,
                "spanner-test-keyring",
                "spanner-test-cmek",
            )
        )
    return kms_key_names_list
