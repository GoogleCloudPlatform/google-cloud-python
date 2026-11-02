#!/usr/bin/env python3

# Copyright 2020 Google LLC.

# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import math
import os
import random
import time

from google.cloud.spanner_v1 import Client

REGION = "regional-us-central1"
WORKER_INDEX = int(os.getenv("DJANGO_WORKER_INDEX", 0))
WORKER_COUNT = int(os.getenv("DJANGO_WORKER_COUNT", 1))


class TestInstance:
    def __enter__(self):
        project = os.getenv(
            "GOOGLE_CLOUD_PROJECT",
            os.getenv("PROJECT_ID", "emulator-test-project"),
        )

        client = Client(project=project)

        config = f"{client.project_name}/instanceConfigs/{REGION}"

        name = "sp-dj-test-{}-{}".format(str(WORKER_INDEX), str(int(time.time())))

        self._instance = client.instance(name, config)
        created_op = self._instance.create()
        created_op.result(120)  # block until completion
        return name

    def __exit__(self, exc, exc_value, traceback):
        self._instance.delete()


if WORKER_INDEX >= WORKER_COUNT:
    print(
        "WORKER_INDEX ({wi}) > WORKER_COUNT ({wc})".format(
            wi=WORKER_INDEX,
            wc=WORKER_COUNT,
        )
    )
    exit()

with open("django_test_apps.txt", "r") as file:
    all_apps = file.read().split("\n")

apps_per_worker = math.ceil(len(all_apps) / WORKER_COUNT)

start_index = min(WORKER_INDEX * apps_per_worker, len(all_apps))
end_index = min(start_index + apps_per_worker, len(all_apps))

test_apps = all_apps[start_index:end_index]
print("test apps: ", test_apps)

if not test_apps:
    exit()

delay = random.randint(10, 60)
print("creating instance with delay: {} seconds".format(delay))
time.sleep(delay)

suite = os.environ.get("DJANGO_TEST_SUITE", "./django_test_suite_6.0.sh")
with TestInstance() as instance_name:
    os.system(
        """DJANGO_TEST_APPS="{apps}" SPANNER_TEST_INSTANCE={instance} bash {suite}""".format(
            apps=" ".join(test_apps), instance=instance_name, suite=suite
        )
    )
