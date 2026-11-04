# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import os
import time

from django.core.management import call_command
from django.db import connection
from google.api_core import exceptions
from google.cloud.spanner_v1 import Client
from google.cloud.spanner_v1.instance import Backup, Instance
from test_utils.retry import RetryErrors

from django_spanner import USE_EMULATOR
from django_spanner.creation import DatabaseCreation

CREATE_INSTANCE = os.getenv("GOOGLE_CLOUD_TESTS_CREATE_SPANNER_INSTANCE") is not None

SPANNER_OPERATION_TIMEOUT_IN_SECONDS = int(
    os.getenv("SPANNER_OPERATION_TIMEOUT_IN_SECONDS", 60)
)
EXISTING_INSTANCES = []
INSTANCE_ID = os.environ.get(
    "GOOGLE_CLOUD_TESTS_SPANNER_INSTANCE", "spanner-django-python-systest"
)
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "emulator-test-project")
DATABASE_NAME = os.getenv("DJANGO_SPANNER_DB", "django_test_db")


class Config(object):
    """Run-time configuration to be modified at set-up.

    This is a mutable stand-in to allow test set-up to modify
    global state.
    """

    CLIENT = None
    INSTANCE_CONFIG = None
    INSTANCE = None
    DATABASE = None


def _list_instances():
    return list(Config.CLIENT.list_instances())


def setup_instance():
    if USE_EMULATOR:
        from google.auth.credentials import AnonymousCredentials

        Config.CLIENT = Client(project=PROJECT_ID, credentials=AnonymousCredentials())
    else:
        Config.CLIENT = Client()

    retry = RetryErrors(exceptions.ServiceUnavailable)

    configs = list(retry(Config.CLIENT.list_instance_configs)())

    instances = retry(_list_instances)()
    EXISTING_INSTANCES[:] = instances

    # Delete test instances that are older than an hour.
    cutoff = int(time.time()) - 1 * 60 * 60
    instance_pbs = Config.CLIENT.list_instances("labels.python-spanner-systests:true")
    for instance_pb in instance_pbs:
        instance = Instance.from_pb(instance_pb, Config.CLIENT)
        if "created" not in instance.labels:
            continue
        create_time = int(instance.labels["created"])
        if create_time > cutoff:
            continue
        if not USE_EMULATOR:
            # Instance cannot be deleted while backups exist.
            for backup_pb in instance.list_backups():
                backup = Backup.from_pb(backup_pb, instance)
                backup.delete()
        instance.delete()

    if CREATE_INSTANCE:
        if not USE_EMULATOR:
            # Defend against back-end returning configs for regions we aren't
            # actually allowed to use.
            configs = [config for config in configs if "-us-" in config.name]

        if not configs:
            raise ValueError("List instance configs failed in module set up.")

        Config.INSTANCE_CONFIG = configs[0]
        config_name = configs[0].name
        create_time = str(int(time.time()))
        labels = {"django-spanner-systests": "true", "created": create_time}

        Config.INSTANCE = Config.CLIENT.instance(
            INSTANCE_ID, config_name, labels=labels
        )
        if not Config.INSTANCE.exists():
            created_op = Config.INSTANCE.create()
            created_op.result(
                SPANNER_OPERATION_TIMEOUT_IN_SECONDS
            )  # block until completion
        else:
            Config.INSTANCE.reload()

    else:
        Config.INSTANCE = Config.CLIENT.instance(INSTANCE_ID)
        Config.INSTANCE.reload()


def teardown_instance():
    if CREATE_INSTANCE:
        Config.INSTANCE.delete()


def setup_database():
    Config.DATABASE = Config.INSTANCE.database(DATABASE_NAME)
    if not Config.DATABASE.exists():
        creation = DatabaseCreation(connection)
        creation._create_test_db(verbosity=0, autoclobber=False, keepdb=True)

    # Running migrations on the db.
    call_command("migrate", interactive=False)


def teardown_database():
    from django.db import connections

    connections.close_all()

    Config.DATABASE = Config.INSTANCE.database(DATABASE_NAME)
    if Config.DATABASE.exists():
        Config.DATABASE.drop()

    # Clear the global client cache to avoid Stale Session errors
    # when the next test class creates a new database.
    try:
        import django_spanner.base

        django_spanner.base._SPANNER_CLIENT_CACHE = None
    except ImportError:
        pass
