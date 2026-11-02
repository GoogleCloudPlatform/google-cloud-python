# Copyright 2021 The sqlalchemy-bigquery Authors
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import base64
import json
from unittest import mock

import google.auth
import google.auth.credentials
import pytest
from google.oauth2 import service_account

from sqlalchemy_bigquery import _helpers


class AnonymousCredentialsWithProject(google.auth.credentials.AnonymousCredentials):
    """Fake credentials to trick isinstance"""

    def __init__(self, project):
        super().__init__()
        self.project_id = project

    def with_scopes(self, scopes):
        return self


@pytest.fixture(scope="session")
def module_under_test():
    from sqlalchemy_bigquery import _helpers

    return _helpers


def test_create_bigquery_client_with_credentials_path(monkeypatch, module_under_test):
    mock_service_account = mock.create_autospec(service_account.Credentials)
    mock_service_account.from_service_account_file.return_value = (
        AnonymousCredentialsWithProject("service-account-project")
    )
    monkeypatch.setattr(service_account, "Credentials", mock_service_account)

    bqclient = module_under_test.create_bigquery_client(
        credentials_path="path/to/key.json",
    )

    assert bqclient.project == "service-account-project"


def test_create_bigquery_client_with_credentials_path_respects_project(
    monkeypatch, module_under_test
):
    """Test that project_id is used, even when there is a default project.

    https://github.com/googleapis/python-bigquery-sqlalchemy/issues/48
    """
    mock_service_account = mock.create_autospec(service_account.Credentials)
    mock_service_account.from_service_account_file.return_value = (
        AnonymousCredentialsWithProject("service-account-project")
    )
    monkeypatch.setattr(service_account, "Credentials", mock_service_account)

    bqclient = module_under_test.create_bigquery_client(
        credentials_path="path/to/key.json",
        project_id="connection-url-project",
    )

    assert bqclient.project == "connection-url-project"


def test_create_bigquery_client_with_credentials_info(monkeypatch, module_under_test):
    mock_service_account = mock.create_autospec(service_account.Credentials)
    mock_service_account.from_service_account_info.return_value = (
        AnonymousCredentialsWithProject("service-account-project")
    )
    monkeypatch.setattr(service_account, "Credentials", mock_service_account)

    bqclient = module_under_test.create_bigquery_client(
        credentials_info={
            "type": "service_account",
            "project_id": "service-account-project",
        },
    )

    assert bqclient.project == "service-account-project"


def test_create_bigquery_client_with_credentials_info_respects_project(
    monkeypatch, module_under_test
):
    """Test that project_id is used, even when there is a default project.

    https://github.com/googleapis/python-bigquery-sqlalchemy/issues/48
    """
    mock_service_account = mock.create_autospec(service_account.Credentials)
    mock_service_account.from_service_account_info.return_value = (
        AnonymousCredentialsWithProject("service-account-project")
    )
    monkeypatch.setattr(service_account, "Credentials", mock_service_account)

    bqclient = module_under_test.create_bigquery_client(
        credentials_info={
            "type": "service_account",
            "project_id": "service-account-project",
        },
        project_id="connection-url-project",
    )

    assert bqclient.project == "connection-url-project"


def test_create_bigquery_client_with_credentials_base64(monkeypatch, module_under_test):
    mock_service_account = mock.create_autospec(service_account.Credentials)
    mock_service_account.from_service_account_info.return_value = (
        AnonymousCredentialsWithProject("service-account-project")
    )
    monkeypatch.setattr(service_account, "Credentials", mock_service_account)

    credentials_info = (
        {"type": "service_account", "project_id": "service-account-project"},
    )

    credentials_base64 = base64.b64encode(json.dumps(credentials_info).encode())

    bqclient = module_under_test.create_bigquery_client(
        credentials_base64=credentials_base64
    )

    assert bqclient.project == "service-account-project"


def test_create_bigquery_client_with_credentials_base64_respects_project(
    monkeypatch, module_under_test
):
    """Test that project_id is used, even when there is a default project.

    https://github.com/googleapis/python-bigquery-sqlalchemy/issues/48
    """
    mock_service_account = mock.create_autospec(service_account.Credentials)
    mock_service_account.from_service_account_info.return_value = (
        AnonymousCredentialsWithProject("service-account-project")
    )
    monkeypatch.setattr(service_account, "Credentials", mock_service_account)

    credentials_info = (
        {"type": "service_account", "project_id": "service-account-project"},
    )

    credentials_base64 = base64.b64encode(json.dumps(credentials_info).encode())

    bqclient = module_under_test.create_bigquery_client(
        credentials_base64=credentials_base64,
        project_id="connection-url-project",
    )

    assert bqclient.project == "connection-url-project"


def test_create_bigquery_client_with_default_credentials(
    monkeypatch, module_under_test
):
    def mock_default_credentials(*args, **kwargs):
        return (google.auth.credentials.AnonymousCredentials(), "default-project")

    monkeypatch.setattr(google.auth, "default", mock_default_credentials)

    bqclient = module_under_test.create_bigquery_client()

    assert bqclient.project == "default-project"


def test_create_bigquery_client_with_default_credentials_respects_project(
    monkeypatch, module_under_test
):
    """Test that project_id is used, even when there is a default project.

    https://github.com/googleapis/python-bigquery-sqlalchemy/issues/48
    """

    def mock_default_credentials(*args, **kwargs):
        return (google.auth.credentials.AnonymousCredentials(), "default-project")

    monkeypatch.setattr(google.auth, "default", mock_default_credentials)

    bqclient = module_under_test.create_bigquery_client(
        project_id="connection-url-project",
    )

    assert bqclient.project == "connection-url-project"


def test_substitute_string_re(module_under_test):
    import re

    foo_to_baz = module_under_test.substitute_string_re_method(
        "foo", flags=re.IGNORECASE, repl="baz"
    )
    assert (
        foo_to_baz(object(), "some foo and FOO is good") == "some baz and baz is good"
    )


def test_substitute_re_func(module_under_test):
    import re

    @module_under_test.substitute_re_method("foo", re.IGNORECASE)
    def Foo_to_bar(self, m):
        return "bar"

    assert (
        Foo_to_bar(object(), "some foo and FOO is good") == "some bar and bar is good"
    )

    @module_under_test.substitute_re_method("foo")
    def foo_to_bar(self, m, x="bar"):
        return x

    assert (
        foo_to_bar(object(), "some foo and FOO is good") == "some bar and FOO is good"
    )

    assert (
        foo_to_bar(object(), "some foo and FOO is good", "hah")
        == "some hah and FOO is good"
    )

    assert (
        foo_to_bar(object(), "some foo and FOO is good", x="hah")
        == "some hah and FOO is good"
    )

    assert foo_to_bar.__name__ == "foo_to_bar"


def test_substitute_re_func_self(module_under_test):
    class Replacer:
        def __init__(self, x):
            self.x = x

        @module_under_test.substitute_re_method("foo")
        def foo_to_bar(self, m):
            return self.x

    assert (
        Replacer("hah").foo_to_bar("some foo and FOO is good")
        == "some hah and FOO is good"
    )


@pytest.mark.parametrize(
    "user_agent, expected_user_agent",
    [
        (None, f"sqlalchemy/{_helpers.sqlalchemy.__version__}"),
        ("my-user-agent", "my-user-agent"),
    ],
)
def test_google_client_info(user_agent, expected_user_agent):
    client_info = _helpers.google_client_info(user_agent=user_agent)
    assert client_info.to_user_agent().startswith(expected_user_agent)
