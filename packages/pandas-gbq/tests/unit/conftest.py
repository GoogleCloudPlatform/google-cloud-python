# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

from unittest import mock

import pytest


def mock_get_credentials(*args, **kwargs):
    import google.auth.credentials

    mock_credentials = mock.create_autospec(google.auth.credentials.Credentials)
    return mock_credentials, "default-project"


@pytest.fixture
def mock_service_account_credentials():
    import google.oauth2.service_account

    mock_credentials = mock.create_autospec(google.oauth2.service_account.Credentials)
    return mock_credentials


@pytest.fixture
def mock_compute_engine_credentials():
    import google.auth.compute_engine

    mock_credentials = mock.create_autospec(google.auth.compute_engine.Credentials)
    return mock_credentials


@pytest.fixture(autouse=True)
def no_auth(monkeypatch):
    import pydata_google_auth

    monkeypatch.setattr(pydata_google_auth, "default", mock_get_credentials)


@pytest.fixture(autouse=True, scope="function")
def reset_context():
    import pandas_gbq

    pandas_gbq.context.credentials = None
    pandas_gbq.context.project = None


@pytest.fixture(autouse=True)
def mock_bigquery_client(monkeypatch):
    import google.cloud.bigquery

    mock_client = mock.create_autospec(google.cloud.bigquery.Client)
    # Constructor returns the mock itself, so this mock can be treated as the
    # constructor or the instance.
    mock_client.return_value = mock_client
    monkeypatch.setattr(google.cloud.bigquery, "Client", mock_client)
    mock_client.reset_mock()

    return mock_client
