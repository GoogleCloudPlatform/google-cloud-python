# Copyright 2021 The sqlalchemy-bigquery Authors
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import base64
import json
import os

import pytest


@pytest.fixture(scope="session")
def module_under_test():
    from sqlalchemy_bigquery import _helpers

    return _helpers


@pytest.fixture
def credentials_path():
    if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
        pytest.skip("GOOGLE_APPLICATION_CREDENTIALS must be set")
    return os.environ["GOOGLE_APPLICATION_CREDENTIALS"]


@pytest.fixture
def credentials_info(credentials_path):
    with open(credentials_path) as credentials_file:
        return json.load(credentials_file)


@pytest.fixture
def credentials_base64(credentials_path):
    with open(credentials_path) as credentials_file:
        return base64.b64encode(credentials_file.read().encode()).decode()


def test_create_bigquery_client_with_credentials_path(
    module_under_test, credentials_path, credentials_info
):
    bqclient = module_under_test.create_bigquery_client(
        credentials_path=credentials_path
    )
    assert bqclient.project == credentials_info["project_id"]


def test_create_bigquery_client_with_credentials_path_respects_project(
    module_under_test, credentials_path
):
    """Test that project_id is used, even when there is a default project.

    https://github.com/googleapis/python-bigquery-sqlalchemy/issues/48
    """
    bqclient = module_under_test.create_bigquery_client(
        credentials_path=credentials_path,
        project_id="connection-url-project",
    )
    assert bqclient.project == "connection-url-project"


def test_create_bigquery_client_with_credentials_info(
    module_under_test, credentials_info
):
    bqclient = module_under_test.create_bigquery_client(
        credentials_info=credentials_info
    )
    assert bqclient.project == credentials_info["project_id"]


def test_create_bigquery_client_with_credentials_info_respects_project(
    module_under_test, credentials_info
):
    """Test that project_id is used, even when there is a default project.

    https://github.com/googleapis/python-bigquery-sqlalchemy/issues/48
    """
    bqclient = module_under_test.create_bigquery_client(
        credentials_info=credentials_info,
        project_id="connection-url-project",
    )
    assert bqclient.project == "connection-url-project"


def test_create_bigquery_client_with_credentials_base64(
    module_under_test, credentials_base64, credentials_info
):
    bqclient = module_under_test.create_bigquery_client(
        credentials_base64=credentials_base64
    )
    assert bqclient.project == credentials_info["project_id"]


def test_create_bigquery_client_with_credentials_base64_respects_project(
    module_under_test, credentials_base64
):
    """Test that project_id is used, even when there is a default project.

    https://github.com/googleapis/python-bigquery-sqlalchemy/issues/48
    """
    bqclient = module_under_test.create_bigquery_client(
        credentials_base64=credentials_base64,
        project_id="connection-url-project",
    )
    assert bqclient.project == "connection-url-project"


def test_create_bigquery_client_with_user_agent(module_under_test):
    user_agent = "test_user_agent"

    bqclient = module_under_test.create_bigquery_client(user_agent=user_agent)

    assert bqclient._connection._client_info.user_agent == user_agent
