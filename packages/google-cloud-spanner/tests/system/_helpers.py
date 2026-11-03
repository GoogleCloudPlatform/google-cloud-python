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

import operator
import os
import time
import uuid

from google.api_core import datetime_helpers, exceptions
from test_utils import retry

from google.cloud.spanner_v1 import instance as instance_mod
from tests import _fixtures

CREATE_INSTANCE_ENVVAR = "GOOGLE_CLOUD_TESTS_CREATE_SPANNER_INSTANCE"
CREATE_INSTANCE = os.getenv(CREATE_INSTANCE_ENVVAR, "false").lower() == "true"

INSTANCE_ID_ENVVAR = "GOOGLE_CLOUD_TESTS_SPANNER_INSTANCE"
INSTANCE_ID_DEFAULT = "google-cloud-python-systest"
INSTANCE_ID = os.environ.get(INSTANCE_ID_ENVVAR, INSTANCE_ID_DEFAULT)

API_ENDPOINT_ENVVAR = "GOOGLE_CLOUD_TESTS_SPANNER_HOST"
API_ENDPOINT = os.getenv(API_ENDPOINT_ENVVAR)

SKIP_BACKUP_TESTS_ENVVAR = "SKIP_BACKUP_TESTS"
SKIP_BACKUP_TESTS = os.getenv(SKIP_BACKUP_TESTS_ENVVAR) is not None

INSTANCE_OPERATION_TIMEOUT_IN_SECONDS = int(
    os.getenv("SPANNER_INSTANCE_OPERATION_TIMEOUT_IN_SECONDS", 560)
)
DATABASE_OPERATION_TIMEOUT_IN_SECONDS = int(
    os.getenv("SPANNER_DATABASE_OPERATION_TIMEOUT_IN_SECONDS", 120)
)
BACKUP_OPERATION_TIMEOUT_IN_SECONDS = int(
    os.getenv("SPANNER_BACKUP_OPERATION_TIMEOUT_IN_SECONDS", 1200)
)
DATABASE_CLEANUP_CUTOFF_IN_SECONDS = int(
    os.getenv("SPANNER_DATABASE_CLEANUP_CUTOFF_IN_SECONDS", 3 * 60 * 60)
)

USE_EMULATOR_ENVVAR = "SPANNER_EMULATOR_HOST"
USE_EMULATOR = os.getenv(USE_EMULATOR_ENVVAR) is not None

DATABASE_DIALECT_ENVVAR = "SPANNER_DATABASE_DIALECT"
DATABASE_DIALECT = os.getenv(DATABASE_DIALECT_ENVVAR)

EMULATOR_PROJECT_ENVVAR = "GCLOUD_PROJECT"
EMULATOR_PROJECT_DEFAULT = "emulator-test-project"
EMULATOR_PROJECT = os.getenv(EMULATOR_PROJECT_ENVVAR, EMULATOR_PROJECT_DEFAULT)

USE_SPANNER_OMNI_ENVVAR = "SPANNER_OMNI"
SPANNER_OMNI = os.getenv(USE_SPANNER_OMNI_ENVVAR)
USE_SPANNER_OMNI = SPANNER_OMNI is not None

CA_CERTIFICATE_ENVVAR = "CA_CERTIFICATE"
CA_CERTIFICATE = os.getenv(CA_CERTIFICATE_ENVVAR)
CLIENT_CERTIFICATE_ENVVAR = "CLIENT_CERTIFICATE"
CLIENT_CERTIFICATE = os.getenv(CLIENT_CERTIFICATE_ENVVAR)
CLIENT_KEY_ENVVAR = "CLIENT_KEY"
CLIENT_KEY = os.getenv(CLIENT_KEY_ENVVAR)
USE_PLAIN_TEXT = CA_CERTIFICATE is None

SPANNER_OMNI_USER_ENVVAR = "SPANNER_OMNI_USER"
SPANNER_OMNI_USER = os.getenv(SPANNER_OMNI_USER_ENVVAR)
SPANNER_OMNI_PASSWORD_ENVVAR = "SPANNER_OMNI_PASSWORD"
SPANNER_OMNI_PASSWORD = os.getenv(SPANNER_OMNI_PASSWORD_ENVVAR)

SPANNER_OMNI_INSTANCE = "default"

DDL_STATEMENTS = (
    _fixtures.PG_DDL_STATEMENTS
    if DATABASE_DIALECT == "POSTGRESQL"
    else (
        _fixtures.EMULATOR_DDL_STATEMENTS if USE_EMULATOR else _fixtures.DDL_STATEMENTS
    )
)

PROTO_COLUMNS_DDL_STATEMENTS = _fixtures.PROTO_COLUMNS_DDL_STATEMENTS

retry_true = retry.RetryResult(operator.truth)
retry_false = retry.RetryResult(operator.not_)

retry_503 = retry.RetryErrors(exceptions.ServiceUnavailable)
retry_429_503 = retry.RetryErrors(
    exceptions.TooManyRequests, exceptions.ServiceUnavailable, 8
)
retry_maybe_aborted_txn = retry.RetryErrors(exceptions.Aborted)
retry_maybe_conflict = retry.RetryErrors(exceptions.Conflict)


def _has_all_ddl(database):
    # Predicate to test for EC completion.
    return len(database.ddl_statements) == len(DDL_STATEMENTS)


retry_has_all_dll = retry.RetryInstanceState(_has_all_ddl)


def scrub_referencing_databases(to_scrub, db_list):
    for db_name in db_list:
        db = to_scrub.database(db_name.split("/")[-1])
        try:
            retry_429_503(db.delete)()
        except exceptions.NotFound:  # lost the race
            pass


def scrub_instance_backups(to_scrub):
    try:
        for backup_pb in to_scrub.list_backups():
            # Backup cannot be deleted while referencing databases exist.
            scrub_referencing_databases(to_scrub, backup_pb.referencing_databases)
            bkp = instance_mod.Backup.from_pb(backup_pb, to_scrub)
            try:
                # Instance cannot be deleted while backups exist.
                retry_429_503(bkp.delete)()
            except exceptions.NotFound:  # lost the race
                pass
    except exceptions.MethodNotImplemented:
        # The CI emulator raises 501:  local versions seem fine.
        pass


def scrub_instance_ignore_not_found(to_scrub):
    """Helper for func:`cleanup_old_instances`"""
    scrub_instance_backups(to_scrub)

    for database_pb in to_scrub.list_databases():
        db = to_scrub.database(database_pb.name.split("/")[-1])
        db.reload()
        try:
            if db.enable_drop_protection:
                db.enable_drop_protection = False
                operation = db.update(["enable_drop_protection"])
                operation.result(DATABASE_OPERATION_TIMEOUT_IN_SECONDS)
        except exceptions.NotFound:
            pass

    try:
        retry_429_503(to_scrub.delete)()
    except exceptions.NotFound:
        pass


def cleanup_old_instances(spanner_client):
    cutoff = int(time.time()) - 3 * 60 * 60  # three hour ago
    instance_filter = "labels.python-spanner-systests:true"

    for instance_pb in spanner_client.list_instances(filter_=instance_filter):
        instance = instance_mod.Instance.from_pb(instance_pb, spanner_client)

        if "created" in instance.labels:
            create_time = int(instance.labels["created"])

            if create_time <= cutoff:
                scrub_instance_ignore_not_found(instance)


def cleanup_stale_databases(
    instance, cutoff_seconds=DATABASE_CLEANUP_CUTOFF_IN_SECONDS
):
    """Delete stale databases in the given instance older than cutoff_seconds."""
    cutoff_milliseconds = (int(time.time()) - cutoff_seconds) * 1000

    for database_pb in instance.list_databases():
        if database_pb.create_time is not None:
            create_time_milliseconds = datetime_helpers.to_milliseconds(
                database_pb.create_time
            )

            if create_time_milliseconds < cutoff_milliseconds:
                database = instance.database(database_pb.name.split("/")[-1])
                try:
                    database.reload()
                    if database.enable_drop_protection:
                        database.enable_drop_protection = False
                        operation = database.update(["enable_drop_protection"])
                        operation.result(DATABASE_OPERATION_TIMEOUT_IN_SECONDS)
                    database.drop()
                except exceptions.NotFound:
                    pass
                except exceptions.GoogleAPIError:
                    # Ignore other API errors during cleanup
                    pass


def unique_id(prefix, separator="-"):
    # Database name size: Spanner database names are limited to 30 characters.
    # See: https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#createdatabaserequest
    return f"{prefix}{separator}{uuid.uuid4().hex[:13]}"


class FauxCall:
    def __init__(self, code, details="FauxCall"):
        self._code = code
        self._details = details

    def initial_metadata(self):
        return {}

    def trailing_metadata(self):
        return {}

    def code(self):
        return self._code

    def details(self):
        return self._details
