# Copyright 2017 Google LLC
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

"""Depopulate spanner databases with data for streaming system tests."""

# Import relative to the script's directory
from streaming_utils import DATABASE_NAME, INSTANCE_NAME, print_func

from google.cloud.spanner import Client


def remove_database(client):
    instance = client.instance(INSTANCE_NAME)

    if not instance.exists():
        print_func("Instance does not exist: {}".format(INSTANCE_NAME))
        return

    print_func("Instance exists: {}".format(INSTANCE_NAME))
    instance.reload()

    database = instance.database(DATABASE_NAME)

    if not database.exists():
        print_func("Database does not exist: {}".format(DATABASE_NAME))
        return
    print_func("Dropping database: {}".format(DATABASE_NAME))
    database.drop()


if __name__ == "__main__":
    client = Client()
    remove_database(client)
