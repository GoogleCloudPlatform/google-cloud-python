# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import atexit
import os
import time

from django.conf import settings
from django.db import connections
from google.api_core import exceptions
from google.cloud.spanner_v1 import Client
from google.cloud.spanner_v1.database import Database

from django_spanner import USE_EMULATOR

SPANNER_OPERATION_TIMEOUT_IN_SECONDS = int(
    os.getenv("SPANNER_OPERATION_TIMEOUT_IN_SECONDS", 240)
)
INSTANCE_ID = os.environ.get(
    "GOOGLE_CLOUD_TESTS_SPANNER_INSTANCE",
    settings.DATABASES["default"]["INSTANCE"],
)
PROJECT_ID = os.getenv(
    "GOOGLE_CLOUD_PROJECT",
    settings.DATABASES["default"]["PROJECT"],
)


class Config(object):
    """Run-time configuration to be modified at set-up.

    This is a mutable stand-in to allow test set-up to modify
    global state.
    """

    CLIENT = None
    INSTANCE = None
    DATABASE = None


def _cleanup_stale_databases(instance):
    """Drop stale dj_sys_<timestamp>_* databases older than 1 hour."""
    cutoff = int(time.time()) - 1 * 60 * 60
    try:
        for db_pb in instance.list_databases():
            db = Database.from_pb(db_pb, instance)
            parts = db.database_id.split("_")
            if len(parts) >= 3 and parts[0] == "dj" and parts[1] == "sys":
                try:
                    created_ts = int(parts[2])
                except ValueError:
                    continue
                if created_ts < cutoff:
                    try:
                        db.drop()
                    except Exception:
                        pass
    except Exception:
        pass


def setup_instance():
    if Config.INSTANCE is not None:
        return

    if USE_EMULATOR:
        from google.auth.credentials import AnonymousCredentials

        Config.CLIENT = Client(project=PROJECT_ID, credentials=AnonymousCredentials())
        configs = list(Config.CLIENT.list_instance_configs())
        if not configs:
            raise ValueError("List instance configs failed in module set up.")
        Config.INSTANCE = Config.CLIENT.instance(INSTANCE_ID, configs[0].name)
        if not Config.INSTANCE.exists():
            created_op = Config.INSTANCE.create()
            created_op.result(SPANNER_OPERATION_TIMEOUT_IN_SECONDS)
        else:
            Config.INSTANCE.reload()
    else:
        Config.CLIENT = Client(project=PROJECT_ID)
        Config.INSTANCE = Config.CLIENT.instance(INSTANCE_ID)
        Config.INSTANCE.reload()
        _cleanup_stale_databases(Config.INSTANCE)


def teardown_instance():
    pass


def setup_database():
    if Config.DATABASE is not None:
        return

    active_db_name = connections["default"].settings_dict["NAME"]
    Config.DATABASE = Config.INSTANCE.database(active_db_name)
    if not Config.DATABASE.exists():
        try:
            created_op = Config.DATABASE.create()
            created_op.result(SPANNER_OPERATION_TIMEOUT_IN_SECONDS)
        except exceptions.AlreadyExists:
            pass


def teardown_database():
    connections.close_all()


def _cleanup_test_resources():
    connections.close_all()
    if Config.DATABASE is not None:
        try:
            if Config.DATABASE.exists():
                Config.DATABASE.drop()
        except Exception:
            pass
        Config.DATABASE = None


atexit.register(_cleanup_test_resources)
