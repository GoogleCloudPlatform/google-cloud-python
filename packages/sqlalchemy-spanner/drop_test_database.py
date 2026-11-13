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

import configparser
import os
import pathlib
import re
import sys

from google.cloud.spanner_v1 import Client

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


def delete_test_database(config_filename="test.cfg"):
    """Delete the currently configured test database."""
    config = configparser.ConfigParser()
    config_path = pathlib.Path(config_filename)
    if config_path.exists():
        config.read(config_path)
    else:
        config.read("setup.cfg")

    db_url = config.get("db", "default")

    instance_id = re.findall(r"instances(.*?)databases", db_url)
    database_id = re.findall(r"databases(.*?)$", db_url)

    instance_id_str = "".join(instance_id).replace("/", "")
    database_id_str = "".join(database_id).replace("/", "")

    instance = CLIENT.instance(instance_id=instance_id_str)
    database = instance.database(database_id_str)
    database.drop()

    # Clean up session-specific config file
    if config_path.exists() and config_filename != "setup.cfg":
        try:
            config_path.unlink()
        except Exception:
            pass


def main(argv):
    config_filename = argv[0] if argv else os.getenv("SQLALCHEMY_SPANNER_CONFIG", "test.cfg")
    delete_test_database(config_filename)


if __name__ == "__main__":
    main(sys.argv[1:])
