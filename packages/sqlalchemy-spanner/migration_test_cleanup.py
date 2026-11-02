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

import re
import sys

from google.cloud import spanner


def main(argv):
    db_url = argv[0]

    project = re.findall(r"projects(.*?)instances", db_url)
    instance_id = re.findall(r"instances(.*?)databases", db_url)
    database_id = re.findall(r"databases(.*?)$", db_url)

    client = spanner.Client(project="".join(project).replace("/", ""))
    instance = client.instance(instance_id="".join(instance_id).replace("/", ""))
    database = instance.database("".join(database_id).replace("/", ""))

    database.update_ddl(
        ["DROP TABLE IF EXISTS account", "DROP TABLE IF EXISTS alembic_version"]
    ).result(120)


if __name__ == "__main__":
    main(sys.argv[1:])
