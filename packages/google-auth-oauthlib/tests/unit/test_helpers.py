# Copyright 2017 Google Inc.
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

import datetime
import json
import os
from unittest import mock

import google.oauth2.credentials
import pytest
from google.auth import external_account_authorized_user

from google_auth_oauthlib import helpers

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CLIENT_SECRETS_FILE = os.path.join(DATA_DIR, "client_secrets.json")

with open(CLIENT_SECRETS_FILE, "r") as fh:
    CLIENT_SECRETS_INFO = json.load(fh)


def test_session_from_client_config_web():
    session, config = helpers.session_from_client_config(
        CLIENT_SECRETS_INFO, scopes=mock.sentinel.scopes
    )

    assert config == CLIENT_SECRETS_INFO
    assert session.client_id == CLIENT_SECRETS_INFO["web"]["client_id"]
    assert session.scope == mock.sentinel.scopes


def test_session_from_client_config_installed():
    info = {"installed": CLIENT_SECRETS_INFO["web"]}
    session, config = helpers.session_from_client_config(
        info, scopes=mock.sentinel.scopes
    )
    assert config == info
    assert session.client_id == info["installed"]["client_id"]
    assert session.scope == mock.sentinel.scopes


def test_session_from_client_config_bad_format():
    with pytest.raises(ValueError):
        helpers.session_from_client_config({}, scopes=[])


def test_session_from_client_config_missing_keys():
    with pytest.raises(ValueError):
        helpers.session_from_client_config({"web": {}}, scopes=[])


def test_session_from_client_secrets_file():
    session, config = helpers.session_from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=mock.sentinel.scopes
    )
    assert config == CLIENT_SECRETS_INFO
    assert session.client_id == CLIENT_SECRETS_INFO["web"]["client_id"]
    assert session.scope == mock.sentinel.scopes


@pytest.fixture
def session():
    session, _ = helpers.session_from_client_config(
        CLIENT_SECRETS_INFO, scopes=mock.sentinel.scopes
    )
    yield session


def test_credentials_from_session(session):
    session.token = {
        "access_token": mock.sentinel.access_token,
        "refresh_token": mock.sentinel.refresh_token,
        "id_token": mock.sentinel.id_token,
        "expires_at": 643969200.0,
    }

    credentials = helpers.credentials_from_session(session, CLIENT_SECRETS_INFO["web"])

    assert isinstance(credentials, google.oauth2.credentials.Credentials)
    assert credentials.token == mock.sentinel.access_token
    assert credentials.expiry == datetime.datetime(1990, 5, 29, 8, 20, 0)
    assert credentials._refresh_token == mock.sentinel.refresh_token
    assert credentials.id_token == mock.sentinel.id_token
    assert credentials._client_id == CLIENT_SECRETS_INFO["web"]["client_id"]
    assert credentials._client_secret == CLIENT_SECRETS_INFO["web"]["client_secret"]
    assert credentials._token_uri == CLIENT_SECRETS_INFO["web"]["token_uri"]
    assert credentials.scopes == session.scope
    assert credentials.granted_scopes is None


def test_credentials_from_session_granted_scopes(session):
    granted_scopes = ["scope1", "scope2"]
    session.token = {
        "access_token": mock.sentinel.access_token,
        "refresh_token": mock.sentinel.refresh_token,
        "id_token": mock.sentinel.id_token,
        "expires_at": 643969200.0,
        "scope": granted_scopes,
    }

    credentials = helpers.credentials_from_session(session, CLIENT_SECRETS_INFO["web"])

    assert isinstance(credentials, google.oauth2.credentials.Credentials)
    assert credentials.token == mock.sentinel.access_token
    assert credentials.expiry == datetime.datetime(1990, 5, 29, 8, 20, 0)
    assert credentials._refresh_token == mock.sentinel.refresh_token
    assert credentials.id_token == mock.sentinel.id_token
    assert credentials._client_id == CLIENT_SECRETS_INFO["web"]["client_id"]
    assert credentials._client_secret == CLIENT_SECRETS_INFO["web"]["client_secret"]
    assert credentials._token_uri == CLIENT_SECRETS_INFO["web"]["token_uri"]
    assert credentials.scopes == session.scope
    assert credentials.granted_scopes == granted_scopes


def test_credentials_from_session_3pi(session):
    session.token = {
        "access_token": mock.sentinel.access_token,
        "refresh_token": mock.sentinel.refresh_token,
        "id_token": mock.sentinel.id_token,
        "expires_at": 643969200.0,
    }

    client_secrets_info = CLIENT_SECRETS_INFO["web"].copy()
    client_secrets_info["3pi"] = True
    client_secrets_info["token_info_url"] = (
        "https://accounts.google.com/o/oauth2/introspect"
    )
    credentials = helpers.credentials_from_session(session, client_secrets_info)

    assert isinstance(credentials, external_account_authorized_user.Credentials)
    assert credentials.token == mock.sentinel.access_token
    assert credentials.expiry == datetime.datetime(1990, 5, 29, 8, 20, 0)
    assert credentials._refresh_token == mock.sentinel.refresh_token
    assert credentials._client_id == CLIENT_SECRETS_INFO["web"]["client_id"]
    assert credentials._client_secret == CLIENT_SECRETS_INFO["web"]["client_secret"]
    assert credentials._token_url == CLIENT_SECRETS_INFO["web"]["token_uri"]
    assert (
        credentials._token_info_url == "https://accounts.google.com/o/oauth2/introspect"
    )
    assert credentials.scopes == session.scope


def test_bad_credentials(session):
    with pytest.raises(ValueError):
        helpers.credentials_from_session(session)
