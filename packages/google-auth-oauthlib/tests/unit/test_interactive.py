# Copyright 2019 Google LLC
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

import socket
from unittest import mock

import pytest


def test_find_open_port_finds_start_port(monkeypatch):
    from google_auth_oauthlib import interactive as module_under_test

    monkeypatch.setattr(socket, "socket", mock.create_autospec(socket.socket))
    port = module_under_test.find_open_port(9999)
    assert port == 9999


def test_find_open_port_finds_stop_port(monkeypatch):
    from google_auth_oauthlib import interactive as module_under_test

    socket_instance = mock.create_autospec(socket.socket, instance=True)

    def mock_socket(family, type_):
        return socket_instance

    monkeypatch.setattr(socket, "socket", mock_socket)
    socket_instance.listen.side_effect = [socket.error] * 99 + [None]
    port = module_under_test.find_open_port(9000, stop=9100)
    assert port == 9099


def test_find_open_port_returns_none(monkeypatch):
    from google_auth_oauthlib import interactive as module_under_test

    socket_instance = mock.create_autospec(socket.socket, instance=True)

    def mock_socket(family, type_):
        return socket_instance

    monkeypatch.setattr(socket, "socket", mock_socket)
    socket_instance.listen.side_effect = socket.error
    port = module_under_test.find_open_port(9000)
    assert port is None
    socket_instance.listen.assert_has_calls(mock.call(1) for _ in range(100))


def test_is_port_open_ipv6_checks(monkeypatch):
    import errno

    from google_auth_oauthlib import interactive as module_under_test

    sock4 = mock.create_autospec(socket.socket, instance=True)
    sock6 = mock.MagicMock()

    def make_sock(family, type_):
        if family == socket.AF_INET6:
            return sock6
        return sock4

    monkeypatch.setattr(socket, "socket", make_sock)

    sock6.__enter__.return_value.connect_ex.return_value = 0
    assert not module_under_test.is_port_open(8085)

    def mock_socket_fn(family, type_):
        if family == socket.AF_INET6:
            raise OSError(errno.EAFNOSUPPORT, "IPv6 disabled")
        return sock4

    monkeypatch.setattr(socket, "socket", mock_socket_fn)
    assert module_under_test.is_port_open(8085)


def test_get_user_credentials():
    from google_auth_oauthlib import flow
    from google_auth_oauthlib import interactive as module_under_test

    mock_flow_instance = mock.create_autospec(flow.InstalledAppFlow, instance=True)

    with mock.patch(
        "google_auth_oauthlib.flow.InstalledAppFlow", autospec=True
    ) as mock_flow:
        mock_flow.from_client_config.return_value = mock_flow_instance
        module_under_test.get_user_credentials(
            ["scopes"], "some-client-id", "shh-secret"
        )

    mock_flow.from_client_config.assert_called_once_with(mock.ANY, scopes=["scopes"])
    actual_client_config = mock_flow.from_client_config.call_args[0][0]
    assert actual_client_config["installed"]["client_id"] == "some-client-id"
    assert actual_client_config["installed"]["client_secret"] == "shh-secret"
    mock_flow_instance.run_local_server.assert_called_once()


def test_get_user_credentials_raises_connectionerror(monkeypatch):
    from google_auth_oauthlib import flow
    from google_auth_oauthlib import interactive as module_under_test

    def mock_find_open_port(start=8080, stop=None):
        return None

    monkeypatch.setattr(module_under_test, "find_open_port", mock_find_open_port)
    mock_flow = mock.create_autospec(flow.InstalledAppFlow, instance=True)

    with (
        mock.patch(
            "google_auth_oauthlib.flow.InstalledAppFlow", autospec=True
        ) as mock_flow,
        pytest.raises(ConnectionError),
    ):
        mock_flow.from_client_config.return_value = mock_flow
        module_under_test.get_user_credentials(
            ["scopes"], "some-client-id", "shh-secret"
        )

    mock_flow.run_local_server.assert_not_called()
