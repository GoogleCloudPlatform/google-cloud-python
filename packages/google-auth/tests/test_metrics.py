# Copyright 2014 Google Inc.
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

import platform
from unittest import mock

import pytest

from google.auth import metrics, version


def test_add_metric_header():
    headers = {}
    metrics.add_metric_header(headers, None)
    assert headers == {}

    headers = {"x-goog-api-client": "foo"}
    metrics.add_metric_header(headers, "bar")
    assert headers == {"x-goog-api-client": "foo bar"}

    headers = {}
    metrics.add_metric_header(headers, "bar")
    assert headers == {"x-goog-api-client": "bar"}


@mock.patch.object(platform, "python_version", return_value="<python-version>")
def test_versions(mock_python_version):
    version_save = version.__version__
    version.__version__ = "<library-version>"
    assert (
        metrics.python_and_auth_lib_version()
        == "gl-python/<python-version> auth/<library-version>"
    )
    version.__version__ = version_save


@pytest.mark.parametrize(
    "func, expected_suffix",
    [
        (metrics.token_request_access_token_mds, "auth-request-type/at cred-type/mds"),
        (metrics.token_request_id_token_mds, "auth-request-type/it cred-type/mds"),
        (
            metrics.token_request_access_token_impersonate,
            "auth-request-type/at cred-type/imp",
        ),
        (
            metrics.token_request_id_token_impersonate,
            "auth-request-type/it cred-type/imp",
        ),
        (
            metrics.token_request_access_token_sa_assertion,
            "auth-request-type/at cred-type/sa",
        ),
        (
            metrics.token_request_id_token_sa_assertion,
            "auth-request-type/it cred-type/sa",
        ),
        (metrics.token_request_user, "cred-type/u"),
        (metrics.mds_ping, "auth-request-type/mds"),
        (metrics.reauth_start, "auth-request-type/re-start"),
        (metrics.reauth_continue, "auth-request-type/re-cont"),
    ],
)
@mock.patch(
    "google.auth.metrics.python_and_auth_lib_version",
    return_value="gl-python/<python-version> auth/<library-version>",
)
def test_metric_values(mock_python_and_auth_lib_version, func, expected_suffix):
    # mock_python_and_auth_lib_version is injected by mock.patch but is not
    # explicitly referenced in the test body as the mock behaves as configured.
    expected = (
        f"gl-python/<python-version> auth/<library-version> {expected_suffix}".strip()
    )
    assert func() == expected


@mock.patch(
    "google.auth.metrics.python_and_auth_lib_version",
    return_value="gl-python/<python-version> auth/<library-version>",
)
def test_byoid_metric_header(mock_python_and_auth_lib_version):
    # mock_python_and_auth_lib_version is injected by mock.patch but is not
    # explicitly referenced in the test body as the mock behaves as configured.
    metrics_options = {}
    assert (
        metrics.byoid_metrics_header(metrics_options)
        == "gl-python/<python-version> auth/<library-version> google-byoid-sdk"
    )
    metrics_options["testKey"] = "testValue"
    assert (
        metrics.byoid_metrics_header(metrics_options)
        == "gl-python/<python-version> auth/<library-version> google-byoid-sdk testKey/testValue"
    )
