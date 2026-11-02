# Copyright 2017 Google LLC All rights reserved.
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

from google.cloud.spanner import Client

from .streaming_utils import INSTANCE_NAME as STREAMING_INSTANCE

STANDARD_INSTANCE = "google-cloud-python-systest"


def scrub_instances(client):
    for instance in client.list_instances():
        if instance.name == STREAMING_INSTANCE:
            print("Not deleting streaming instance: {}".format(STREAMING_INSTANCE))
            continue
        elif instance.name == STANDARD_INSTANCE:
            print("Not deleting standard instance: {}".format(STANDARD_INSTANCE))
        else:
            print("deleting instance: {}".format(instance.name))
            instance.delete()


if __name__ == "__main__":
    client = Client()
    scrub_instances(client)
