# Copyright 2018 Google LLC
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

import unittest.mock as mock

import google.auth.credentials
import pydata_google_auth
import pytest

import bigquery_magics


def test_context_with_default_credentials():
    """When Application Default Credentials are set, the context credentials
    will be created the first time it is called
    """
    bigquery_magics.context._credentials = None
    bigquery_magics.context._project = None

    project = "prahj-ekt"
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch.object(
        pydata_google_auth,
        "default",
        autospec=True,
        return_value=(credentials_mock, project),
    )
    with default_patch as default_mock:
        assert bigquery_magics.context.credentials is credentials_mock
        assert bigquery_magics.context.project == project

    assert default_mock.call_count == 2


def test_context_credentials_and_project_can_be_set_explicitly():
    project1 = "one-project-55564"
    project2 = "other-project-52569"
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch.object(
        pydata_google_auth,
        "default",
        autospec=True,
        return_value=(credentials_mock, project1),
    )
    with default_patch as default_mock:
        bigquery_magics.context.credentials = credentials_mock
        bigquery_magics.context.project = project2

    assert bigquery_magics.context.project == project2
    assert bigquery_magics.context.credentials is credentials_mock
    # default should not be called if credentials & project are explicitly set
    assert default_mock.call_count == 0


def test_context_set_default_variable():
    assert bigquery_magics.context.default_variable is None

    bigquery_magics.context.default_variable = "_bq_df"
    assert bigquery_magics.context.default_variable == "_bq_df"

    bigquery_magics.context.default_variable = None
    assert bigquery_magics.context.default_variable is None


@pytest.mark.parametrize("engine", ["pandas", "bigframes"])
def test_context_set_engine(monkeypatch, engine):
    monkeypatch.setattr(bigquery_magics.context, "engine", engine)
    assert bigquery_magics.context.engine == engine


def test_context_set_invalid_engine(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr(bigquery_magics.context, "engine", "whatever")
