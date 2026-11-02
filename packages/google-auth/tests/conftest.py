# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
from unittest import mock

import pytest  # type: ignore

from google.auth import environment_vars
from google.auth.transport import _mtls_helper


def pytest_configure():
    """Load public certificate and private key."""
    pytest.data_dir = os.path.join(os.path.dirname(__file__), "data")

    with open(os.path.join(pytest.data_dir, "privatekey.pem"), "rb") as fh:
        pytest.private_key_bytes = fh.read()

    with open(os.path.join(pytest.data_dir, "public_cert.pem"), "rb") as fh:
        pytest.public_cert_bytes = fh.read()

    _mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH = os.path.join(
        pytest.data_dir, "nonexistent_gke_credential_bundle.pem"
    )


@pytest.fixture(autouse=True)
def clean_cert_config_env(monkeypatch, tmp_path):
    monkeypatch.delenv(
        environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE,
        raising=False,
    )
    monkeypatch.delenv(
        environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE,
        raising=False,
    )
    monkeypatch.delenv(
        environment_vars.GOOGLE_API_CERTIFICATE_CONFIG,
        raising=False,
    )
    monkeypatch.delenv(
        environment_vars.CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH,
        raising=False,
    )
    monkeypatch.setattr(
        _mtls_helper,
        "_GKE_CREDENTIAL_BUNDLE_PATH",
        str(tmp_path / "gke" / "credential" / "bundle" / "path"),
    )


@pytest.fixture
def mock_non_existent_module(monkeypatch):
    """Mocks a non-existing module in sys.modules.

    Additionally mocks any non-existing modules specified in the dotted path.
    """

    def _mock_non_existent_module(path):
        parts = path.split(".")
        partial = []
        for part in parts:
            partial.append(part)
            current_module = ".".join(partial)
            if current_module not in sys.modules:
                monkeypatch.setitem(sys.modules, current_module, mock.MagicMock())

    return _mock_non_existent_module
