# Copyright 2016 Google LLC All rights reserved.
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

import os

from google.cloud.spanner_v1 import Client

if os.getenv(
    "SPANNER_EMULATOR_HOST"
):  # otherwise instance will be created by parallelize_tests
    project = os.getenv(
        "GOOGLE_CLOUD_PROJECT",
        os.getenv("PROJECT_ID", "emulator-test-project"),
    )

    client = Client(project=project)

    config = f"{client.project_name}/instanceConfigs/regional-us-central1"

    instance = client.instance("google-cloud-django-backend-tests", config)
    created_op = instance.create()
    created_op.result(30)  # block until completion
