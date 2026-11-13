# -*- coding: utf-8 -*-
#
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pathlib
import re
import time
import uuid

from create_test_config import set_test_config
from google.api_core import datetime_helpers
from google.api_core.exceptions import AlreadyExists, ResourceExhausted
from google.cloud.spanner_v1 import Client
from google.cloud.spanner_v1.database import Database
from google.cloud.spanner_v1.instance import Instance

USE_EMULATOR = os.getenv("SPANNER_EMULATOR_HOST") is not None

PROJECT = os.getenv(
    "GOOGLE_CLOUD_PROJECT",
    os.getenv("PROJECT_ID", "emulator-test-project"),
)
CLIENT = None

if USE_EMULATOR:
    from google.auth.credentials import AnonymousCredentials

    CLIENT = Client(project=PROJECT, credentials=AnonymousCredentials())
else:
    CLIENT = Client(project=PROJECT)


def delete_stale_test_instances():
    """Delete test instances that are older than four hours."""
    cutoff = int(time.time()) - 4 * 60 * 60
    instances_pbs = CLIENT.list_instances(
        "labels.python-spanner-sqlalchemy-systest:true"
    )
    for instance_pb in instances_pbs:
        instance = Instance.from_pb(instance_pb, CLIENT)
        if "created" not in instance.labels:
            continue
        create_time = int(instance.labels["created"])
        if create_time > cutoff:
            continue
        try:
            instance.delete()
            time.sleep(5)  # Sleep for 5 seconds to give time for cooldown.
        except ResourceExhausted:
            print(
                "Unable to drop stale instance '{}'. May need manual delete.".format(
                    instance.instance_id
                )
            )


def delete_stale_test_databases():
    """Delete test databases that are older than 4 hours.

    Uses a .stale_cleanup_done sentinel file gate to ensure this global sweep
    runs exactly once at the start of a test run across parallel/parametrized sessions,
    preventing concurrent sessions from interfering with each other.
    """
    marker = pathlib.Path(".stale_cleanup_done")
    if marker.exists():
        return

    try:
        marker.touch(exist_ok=False)
    except FileExistsError:
        return  # Another parallel process already performed cleanup

    cutoff = (int(time.time()) - 4 * 60 * 60) * 1000
    instance = CLIENT.instance("sqlalchemy-dialect-test")
    if not instance.exists():
        return
    database_pbs = instance.list_databases()
    for database_pb in database_pbs:
        database = Database.from_pb(database_pb, instance)

        # Parse creation time from database ID first (e.g. "sp_test_1787069488_a3f2b1")
        create_time = None
        match = re.match(r"sp_test_(\d+)", database.database_id)
        if match:
            ts_str = match.group(1)
            ts_val = int(ts_str)
            if len(ts_str) == 10:
                create_time = ts_val * 1000
            else:
                create_time = ts_val
        elif database_pb.create_time is not None:
            create_time = datetime_helpers.to_milliseconds(database_pb.create_time)

        if create_time is None or create_time > cutoff:
            continue
        try:
            database.drop()
        except ResourceExhausted:
            print(
                "Unable to drop stale database '{}'. May need manual delete.".format(
                    database.database_id
                )
            )


def create_test_instance():
    """Create test instance and a session-isolated ephemeral test database.

    To prevent cross-session test pollution and parallel execution race conditions,
    each test session generates a unique database ID combining a 10-digit timestamp
    and a 6-character random hex suffix (conforming to Spanner's regex: ^[a-z][a-z0-9_]{1,29}$).
    """
    instance_id = "sqlalchemy-dialect-test"
    instance = CLIENT.instance(instance_id)
    if not instance.exists():
        instance_config = f"projects/{PROJECT}/instanceConfigs/regional-us-east1"
        if USE_EMULATOR:
            configs = list(CLIENT.list_instance_configs())
            instance_config = configs[0].name
        create_time = str(int(time.time()))
        labels = {"python-spanner-sqlalchemy-systest": "true", "created": create_time}

        instance = CLIENT.instance(instance_id, instance_config, labels=labels)

        try:
            created_op = instance.create()
            created_op.result(1800)  # block until completion
        except AlreadyExists:
            pass  # instance was already created

    # Generate a session-isolated unique database ID within Spanner 30-char limit
    # Format: sp_test_{timestamp_in_seconds}_{rand_hex6} (compliant with Spanner naming: ^[a-z][a-z0-9_]{1,29}$)
    creation_timestamp = time.time()
    timestamp_part = str(int(creation_timestamp))
    rand_part = uuid.uuid4().hex[:6]
    database_id = f"sp_test_{timestamp_part}_{rand_part}"

    try:
        database = instance.database(database_id)
        created_op = database.create()
        created_op.result(1800)
    except AlreadyExists:
        pass  # database was already created

    set_test_config(PROJECT, instance_id, database_id)


def main(argv):
    config_filename = argv[0] if argv else os.getenv("SQLALCHEMY_SPANNER_CONFIG", "test.cfg")
    os.environ["SQLALCHEMY_SPANNER_CONFIG"] = config_filename

    delete_stale_test_databases()
    create_test_instance()


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
