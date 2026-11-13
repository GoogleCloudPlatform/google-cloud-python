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
import sys


def set_test_config(
    project, instance, database, user=None, password=None, host=None, port=None
):
    config = configparser.ConfigParser()
    if (
        user is not None
        and password is not None
        and host is not None
        and port is not None
    ):
        url = (
            f"spanner+spanner://{user}:{password}@{host}:{port}"
            f"/projects/{project}/instances/{instance}/"
            f"databases/{database}"
        )
    else:
        url = (
            f"spanner+spanner:///projects/{project}/instances/{instance}/"
            f"databases/{database}"
        )
    config.add_section("db")
    config["db"]["default"] = url

    config_filename = os.getenv("SQLALCHEMY_SPANNER_CONFIG", "test.cfg")
    with open(config_filename, "w") as configfile:
        config.write(configfile)


def main(argv):
    project = argv[0]
    instance = argv[1]
    database = argv[2]
    if len(argv) == 7:
        user = argv[3]
        password = argv[4]
        host = argv[5]
        port = argv[6]
    else:
        user = None
        password = None
        host = None
        port = None
    set_test_config(project, instance, database, user, password, host, port)


if __name__ == "__main__":
    main(sys.argv[1:])
