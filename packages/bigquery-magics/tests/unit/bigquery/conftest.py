# Copyright 2025 Google LLC
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

from unittest import mock

import google.auth.credentials
import pytest
import test_utils.imports  # google-cloud-testutils

import bigquery_magics


@pytest.fixture()
def ipython_ns_cleanup():
    """A helper to clean up user namespace after the test

    for the duration of the test scope.
    """
    names_to_clean = []  # pairs (IPython_instance, name_to_clean)

    yield names_to_clean

    for ip, name in names_to_clean:
        if name in ip.user_ns:
            del ip.user_ns[name]


@pytest.fixture(scope="session")
def missing_bq_storage():
    """Provide a patcher that can make the bigquery storage import to fail."""

    def fail_if(name, globals, locals, fromlist, level):
        # NOTE: *very* simplified, assuming a straightforward absolute import
        return "bigquery_storage" in name or (
            fromlist is not None and "bigquery_storage" in fromlist
        )

    return test_utils.imports.maybe_fail_import(predicate=fail_if)


@pytest.fixture(scope="session")
def missing_grpcio_lib():
    """Provide a patcher that can make the gapic library import to fail."""

    def fail_if(name, globals, locals, fromlist, level):
        # NOTE: *very* simplified, assuming a straightforward absolute import
        return "gapic_v1" in name or (fromlist is not None and "gapic_v1" in fromlist)

    return test_utils.imports.maybe_fail_import(predicate=fail_if)


@pytest.fixture
def mock_credentials(monkeypatch):
    credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_project", "test-project")
    monkeypatch.setattr(bigquery_magics.context, "_credentials", credentials)


@pytest.fixture
def set_bigframes_engine_in_context(monkeypatch):
    monkeypatch.setattr(bigquery_magics.context, "engine", "bigframes")
