#  Copyright 2026 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""Helper functions for system tests."""

import os

import pytest

SPANNER_EMULATOR_HOST = os.environ.get("SPANNER_EMULATOR_HOST")
TEST_ON_PROD = not bool(SPANNER_EMULATOR_HOST)

# As of June 2026, this package is in 'Planning' status.
# The CI/CD system does not yet have a SPANNER_EMULATOR_HOST active for this package,
# so running tests on production is the default. This fallback and skip logic acts
# as a safety measure until an emulator is available or production credentials are fully configured.
if TEST_ON_PROD:
    PROJECT_ID = (
        os.environ.get("SPANNER_PROJECT_ID")
        or os.environ.get("GOOGLE_CLOUD_PROJECT")
        or os.environ.get("PROJECT_ID")
    )
    INSTANCE_ID = os.environ.get("SPANNER_INSTANCE_ID") or os.environ.get(
        "GOOGLE_CLOUD_TESTS_SPANNER_INSTANCE"
    )
    DATABASE_ID = os.environ.get("SPANNER_DATABASE_ID")

    if not PROJECT_ID or not INSTANCE_ID or not DATABASE_ID:
        pytest.skip(
            "SPANNER_PROJECT_ID, SPANNER_INSTANCE_ID, and SPANNER_DATABASE_ID (or standard fallbacks) "
            "must be set when running tests on production.",
            allow_module_level=True,
        )
else:
    PROJECT_ID = "test-project"
    INSTANCE_ID = "test-instance"
    DATABASE_ID = "test-db"

PROD_TEST_CONNECTION_STRING = (
    f"projects/{PROJECT_ID}/instances/{INSTANCE_ID}/databases/{DATABASE_ID}"
)

EMULATOR_TEST_CONNECTION_STRING = (
    f"{SPANNER_EMULATOR_HOST}"
    f"projects/{PROJECT_ID}"
    f"/instances/{INSTANCE_ID}"
    f"/databases/{DATABASE_ID}"
    "?autoConfigEmulator=true"
)


def setup_test_env() -> None:
    if not TEST_ON_PROD:
        print(f"Set SPANNER_EMULATOR_HOST to {os.environ['SPANNER_EMULATOR_HOST']}")
    print(f"Using Connection String: {get_test_connection_string()}")


def get_test_connection_string() -> str:
    if TEST_ON_PROD:
        return PROD_TEST_CONNECTION_STRING
    return EMULATOR_TEST_CONNECTION_STRING
