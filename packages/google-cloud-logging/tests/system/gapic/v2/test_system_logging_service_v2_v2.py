# Copyright 2018 Google LLC
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
import time

import google.auth
import pytest
from google.api import monitored_resource_pb2

from google.cloud import logging_v2


class TestSystemLoggingServiceV2(object):
    def test_write_log_entries(self):
        # Use GOOGLE_CLOUD_PROJECT or PROJECT_ID
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get(
            "PROJECT_ID"
        )

        # Guard: Skip if project or credentials are missing
        # This prevents the "prerelease_deps" job from failing
        if not project_id or "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
            pytest.skip(
                "System tests require GOOGLE_CLOUD_PROJECT and GOOGLE_APPLICATION_CREDENTIALS"
            )

        # Instantiate the client
        # Since we've confirmed the env var exists, this call is now safe
        client = logging_v2.services.logging_service_v2.LoggingServiceV2Client()

        log_name = client.log_path(project_id, "test-{0}".format(time.time()))
        resource = {}
        labels = {}
        entries = []

        response = client.write_log_entries(
            entries=entries,
            log_name=log_name,
            resource=resource,
            labels=labels,
        )
