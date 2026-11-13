# Copyright 2026 Google LLC
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

import functools
import os
import tempfile

import pytest


@pytest.fixture(scope="session", autouse=True)
def _default_app_profile():
    """Default ``get_table`` to ``BIGTABLE_TEST_APP_PROFILE`` when set."""
    profile = os.getenv("BIGTABLE_TEST_APP_PROFILE") or os.getenv("CBT_APP_PROFILE_ID")
    if not profile:
        yield
        return

    from google.cloud.bigtable.data._async.client import BigtableDataClientAsync
    from google.cloud.bigtable.data._sync_autogen.client import BigtableDataClient

    patched = []
    for cls in (BigtableDataClientAsync, BigtableDataClient):
        original = cls.get_table

        def make_wrapper(orig):
            @functools.wraps(orig)
            def get_table(self, instance_id, table_id, *args, **kwargs):
                if not args and "app_profile_id" not in kwargs:
                    kwargs["app_profile_id"] = profile
                return orig(self, instance_id, table_id, *args, **kwargs)

            return get_table

        cls.get_table = make_wrapper(original)
        patched.append((cls, original))

    yield

    for cls, original in patched:
        cls.get_table = original


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "accelerator: integration tests for the Cloud Bigtable accelerator",
    )
    config.addinivalue_line(
        "markers", "slow: longer-running accelerator tests (leak loops, stress)"
    )


@pytest.fixture
def tmp_bin_dir():
    with tempfile.TemporaryDirectory(prefix="accel-test-bin-") as d:
        yield d
