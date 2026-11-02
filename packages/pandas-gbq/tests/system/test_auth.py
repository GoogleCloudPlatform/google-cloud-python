# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""System tests for fetching Google BigQuery credentials."""

import os
from unittest import mock

import pytest

from pandas_gbq import auth

IS_RUNNING_ON_CI = "KOKORO_BUILD_ID" in os.environ


def mock_default_credentials(scopes=None, request=None):
    return (None, None)


def test_should_be_able_to_get_valid_credentials(project_id):
    credentials, _ = auth.get_credentials(project_id=project_id)
    assert credentials.valid


@pytest.mark.skipif(
    IS_RUNNING_ON_CI, reason="end-user auth requires human intervention"
)
def test_get_credentials_bad_file_returns_user_credentials(project_id, monkeypatch):
    import google.auth
    from google.auth.credentials import Credentials

    monkeypatch.setattr(google.auth, "default", mock_default_credentials)

    with mock.patch("__main__.open", side_effect=IOError()):
        credentials, _ = auth.get_credentials(
            project_id=project_id, auth_local_webserver=True
        )
    assert isinstance(credentials, Credentials)


@pytest.mark.skipif(
    IS_RUNNING_ON_CI, reason="end-user auth requires human intervention"
)
def test_get_credentials_user_credentials_with_reauth(project_id, monkeypatch):
    import google.auth

    monkeypatch.setattr(google.auth, "default", mock_default_credentials)

    credentials, _ = auth.get_credentials(
        project_id=project_id, reauth=True, auth_local_webserver=True
    )
    assert credentials.valid


@pytest.mark.skipif(
    IS_RUNNING_ON_CI, reason="end-user auth requires human intervention"
)
def test_get_credentials_user_credentials(project_id, monkeypatch):
    import google.auth

    monkeypatch.setattr(google.auth, "default", mock_default_credentials)

    credentials, _ = auth.get_credentials(
        project_id=project_id, auth_local_webserver=True
    )
    assert credentials.valid
