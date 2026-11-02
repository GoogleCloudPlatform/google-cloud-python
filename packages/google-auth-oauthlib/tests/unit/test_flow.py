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

import concurrent.futures
import datetime
import json
import logging
import os
import re
import socket
import time
import urllib
import webbrowser
import wsgiref.simple_server
from functools import partial
from unittest import mock

import pytest
import requests

from google_auth_oauthlib import flow

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CLIENT_SECRETS_FILE = os.path.join(DATA_DIR, "client_secrets.json")

with open(CLIENT_SECRETS_FILE, "r") as fh:
    CLIENT_SECRETS_INFO = json.load(fh)

VALID_PKCE_VERIFIER_REGEX = r"^[A-Za-z0-9-._~]{128}$"
VALID_CODE_CHALLENGE_REGEX = r"^[A-Za-z0-9-_]{43}$"


class TestFlow(object):
    def test_from_client_secrets_file(self):
        instance = flow.Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, scopes=mock.sentinel.scopes
        )
        assert instance.client_config == CLIENT_SECRETS_INFO["web"]
        assert (
            instance.oauth2session.client_id == CLIENT_SECRETS_INFO["web"]["client_id"]
        )
        assert instance.oauth2session.scope == mock.sentinel.scopes

    def test_from_client_secrets_file_with_redirect_uri(self):
        instance = flow.Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=mock.sentinel.scopes,
            redirect_uri=mock.sentinel.redirect_uri,
        )
        assert (
            instance.redirect_uri
            == instance.oauth2session.redirect_uri
            == mock.sentinel.redirect_uri
        )

    def test_from_client_config_installed(self):
        client_config = {"installed": CLIENT_SECRETS_INFO["web"]}
        instance = flow.Flow.from_client_config(
            client_config, scopes=mock.sentinel.scopes
        )
        assert instance.client_config == client_config["installed"]
        assert (
            instance.oauth2session.client_id == client_config["installed"]["client_id"]
        )
        assert instance.oauth2session.scope == mock.sentinel.scopes

    def test_from_client_config_with_redirect_uri(self):
        client_config = {"installed": CLIENT_SECRETS_INFO["web"]}
        instance = flow.Flow.from_client_config(
            client_config,
            scopes=mock.sentinel.scopes,
            redirect_uri=mock.sentinel.redirect_uri,
        )
        assert (
            instance.redirect_uri
            == instance.oauth2session.redirect_uri
            == mock.sentinel.redirect_uri
        )

    def test_from_client_config_bad_format(self):
        with pytest.raises(ValueError):
            flow.Flow.from_client_config({}, scopes=mock.sentinel.scopes)

    @pytest.fixture
    def instance(self):
        yield flow.Flow.from_client_config(
            CLIENT_SECRETS_INFO, scopes=mock.sentinel.scopes
        )

    def test_redirect_uri(self, instance):
        instance.redirect_uri = mock.sentinel.redirect_uri
        assert (
            instance.redirect_uri
            == instance.oauth2session.redirect_uri
            == mock.sentinel.redirect_uri
        )

    def test_authorization_url(self, instance):
        scope = "scope_one"
        instance.oauth2session.scope = [scope]
        authorization_url_patch = mock.patch.object(
            instance.oauth2session,
            "authorization_url",
            wraps=instance.oauth2session.authorization_url,
        )

        with authorization_url_patch as authorization_url_spy:
            url, _ = instance.authorization_url(prompt="consent")

            assert CLIENT_SECRETS_INFO["web"]["auth_uri"] in url
            assert scope in url
            assert "code_challenge=" in url
            assert "code_challenge_method=S256" in url
            authorization_url_spy.assert_called_with(
                CLIENT_SECRETS_INFO["web"]["auth_uri"],
                access_type="offline",
                prompt="consent",
                code_challenge=mock.ANY,
                code_challenge_method="S256",
            )

    def test_authorization_url_code_verifier(self, instance):
        scope = "scope_one"
        instance.oauth2session.scope = [scope]
        instance.code_verifier = "amanaplanacanalpanama"
        authorization_url_patch = mock.patch.object(
            instance.oauth2session,
            "authorization_url",
            wraps=instance.oauth2session.authorization_url,
        )

        with authorization_url_patch as authorization_url_spy:
            url, _ = instance.authorization_url(prompt="consent")

            assert CLIENT_SECRETS_INFO["web"]["auth_uri"] in url
            assert scope in url
            authorization_url_spy.assert_called_with(
                CLIENT_SECRETS_INFO["web"]["auth_uri"],
                access_type="offline",
                prompt="consent",
                code_challenge="2yN0TOdl0gkGwFOmtfx3f913tgEaLM2d2S0WlmG1Z6Q",
                code_challenge_method="S256",
            )

    def test_authorization_url_access_type(self, instance):
        scope = "scope_one"
        instance.oauth2session.scope = [scope]
        instance.code_verifier = "amanaplanacanalpanama"
        authorization_url_patch = mock.patch.object(
            instance.oauth2session,
            "authorization_url",
            wraps=instance.oauth2session.authorization_url,
        )

        with authorization_url_patch as authorization_url_spy:
            url, _ = instance.authorization_url(access_type="meep")

            assert CLIENT_SECRETS_INFO["web"]["auth_uri"] in url
            assert scope in url
            authorization_url_spy.assert_called_with(
                CLIENT_SECRETS_INFO["web"]["auth_uri"],
                access_type="meep",
                code_challenge="2yN0TOdl0gkGwFOmtfx3f913tgEaLM2d2S0WlmG1Z6Q",
                code_challenge_method="S256",
            )

    def test_authorization_url_generated_verifier(self):
        scope = "scope_one"
        instance = flow.Flow.from_client_config(
            CLIENT_SECRETS_INFO, scopes=[scope], autogenerate_code_verifier=True
        )
        authorization_url_path = mock.patch.object(
            instance.oauth2session,
            "authorization_url",
            wraps=instance.oauth2session.authorization_url,
        )

        with authorization_url_path as authorization_url_spy:
            instance.authorization_url()

            _, kwargs = authorization_url_spy.call_args_list[0]
            assert kwargs["code_challenge_method"] == "S256"
            assert len(instance.code_verifier) == 128
            assert len(kwargs["code_challenge"]) == 43
            assert re.fullmatch(VALID_PKCE_VERIFIER_REGEX, instance.code_verifier)
            assert re.fullmatch(VALID_CODE_CHALLENGE_REGEX, kwargs["code_challenge"])

    def test_fetch_token(self, instance):
        instance.code_verifier = "amanaplanacanalpanama"
        fetch_token_patch = mock.patch.object(
            instance.oauth2session,
            "fetch_token",
            autospec=True,
            return_value=mock.sentinel.token,
        )

        with fetch_token_patch as fetch_token_mock:
            token = instance.fetch_token(code=mock.sentinel.code)

            assert token == mock.sentinel.token
            fetch_token_mock.assert_called_with(
                CLIENT_SECRETS_INFO["web"]["token_uri"],
                client_secret=CLIENT_SECRETS_INFO["web"]["client_secret"],
                code=mock.sentinel.code,
                code_verifier="amanaplanacanalpanama",
            )

    def test_credentials(self, instance):
        instance.oauth2session.token = {
            "access_token": mock.sentinel.access_token,
            "refresh_token": mock.sentinel.refresh_token,
            "id_token": mock.sentinel.id_token,
            "expires_at": 643969200.0,
        }

        credentials = instance.credentials

        assert credentials.token == mock.sentinel.access_token
        assert credentials.expiry == datetime.datetime(1990, 5, 29, 8, 20, 0)
        assert credentials._refresh_token == mock.sentinel.refresh_token
        assert credentials.id_token == mock.sentinel.id_token
        assert credentials._client_id == CLIENT_SECRETS_INFO["web"]["client_id"]
        assert credentials._client_secret == CLIENT_SECRETS_INFO["web"]["client_secret"]
        assert credentials._token_uri == CLIENT_SECRETS_INFO["web"]["token_uri"]

    def test_authorized_session(self, instance):
        instance.oauth2session.token = {
            "access_token": mock.sentinel.access_token,
            "refresh_token": mock.sentinel.refresh_token,
            "id_token": mock.sentinel.id_token,
            "expires_at": 643969200.0,
        }

        session = instance.authorized_session()

        assert session.credentials.token == mock.sentinel.access_token


class TestInstalledAppFlow(object):
    SCOPES = ["email", "profile"]
    REDIRECT_REQUEST_PATH = "/?code=code&state=state"
    AUDIENCE = "dummy-audience"

    @pytest.fixture
    def instance(self):
        yield flow.InstalledAppFlow.from_client_config(
            CLIENT_SECRETS_INFO, scopes=self.SCOPES
        )

    @pytest.fixture
    def port(self):
        # Creating a new server at the same port will result in
        # a 'Address already in use' error for a brief
        # period of time after the socket has been closed.
        # Work around this in the tests by letting the OS pick an available port each time.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("localhost", 0))
            return s.getsockname()[1]

    @pytest.fixture
    def socket(self, port):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Enable SO_REUSEADDR
        s.bind(("localhost", port))
        yield s
        s.close()

    @pytest.fixture
    def mock_fetch_token(self, instance):
        def set_token(*args, **kwargs):
            instance.oauth2session.token = {
                "access_token": mock.sentinel.access_token,
                "refresh_token": mock.sentinel.refresh_token,
                "id_token": mock.sentinel.id_token,
                "expires_at": 643969200.0,
            }

        fetch_token_patch = mock.patch.object(
            instance.oauth2session, "fetch_token", autospec=True, side_effect=set_token
        )

        with fetch_token_patch as fetch_token_mock:
            yield fetch_token_mock

    @pytest.mark.webtest
    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    def test_run_local_server(self, webbrowser_mock, instance, mock_fetch_token, port):
        auth_redirect_url = urllib.parse.urljoin(
            f"http://localhost:{port}", self.REDIRECT_REQUEST_PATH
        )

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(partial(instance.run_local_server, port=port))

            while not future.done():
                try:
                    requests.get(auth_redirect_url)
                except requests.ConnectionError:  # pragma: NO COVER
                    pass

            credentials = future.result()

        assert credentials.token == mock.sentinel.access_token
        assert credentials._refresh_token == mock.sentinel.refresh_token
        assert credentials.id_token == mock.sentinel.id_token
        assert webbrowser_mock.get().open.called
        assert instance.redirect_uri == f"http://localhost:{port}/"
        assert re.fullmatch(VALID_PKCE_VERIFIER_REGEX, instance.code_verifier)
        expected_auth_response = auth_redirect_url.replace("http", "https")
        mock_fetch_token.assert_called_with(
            CLIENT_SECRETS_INFO["web"]["token_uri"],
            client_secret=CLIENT_SECRETS_INFO["web"]["client_secret"],
            authorization_response=expected_auth_response,
            code_verifier=mock.ANY,
            audience=None,
        )

    @pytest.mark.webtest
    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    def test_run_local_server_audience(
        self, webbrowser_mock, instance, mock_fetch_token, port
    ):
        auth_redirect_url = urllib.parse.urljoin(
            f"http://localhost:{port}", self.REDIRECT_REQUEST_PATH
        )

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(
                partial(
                    instance.run_local_server, port=port, token_audience=self.AUDIENCE
                )
            )

            while not future.done():
                try:
                    requests.get(auth_redirect_url)
                except requests.ConnectionError:  # pragma: NO COVER
                    pass

            credentials = future.result()

        assert credentials.token == mock.sentinel.access_token
        assert credentials._refresh_token == mock.sentinel.refresh_token
        assert credentials.id_token == mock.sentinel.id_token
        assert webbrowser_mock.get().open.called
        assert instance.redirect_uri == f"http://localhost:{port}/"

        expected_auth_response = auth_redirect_url.replace("http", "https")
        mock_fetch_token.assert_called_with(
            CLIENT_SECRETS_INFO["web"]["token_uri"],
            client_secret=CLIENT_SECRETS_INFO["web"]["client_secret"],
            authorization_response=expected_auth_response,
            code_verifier=mock.ANY,
            audience=self.AUDIENCE,
        )

    @pytest.mark.webtest
    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    def test_run_local_server_code_verifier(
        self, webbrowser_mock, instance, mock_fetch_token, port
    ):
        auth_redirect_url = urllib.parse.urljoin(
            f"http://localhost:{port}", self.REDIRECT_REQUEST_PATH
        )
        instance.code_verifier = "amanaplanacanalpanama"

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(
                partial(
                    instance.run_local_server,
                    port=port,
                    redirect_uri_trailing_slash=False,
                )
            )

            while not future.done():
                try:
                    requests.get(auth_redirect_url)
                except requests.ConnectionError:  # pragma: NO COVER
                    pass

            credentials = future.result()

        assert credentials.token == mock.sentinel.access_token
        assert credentials._refresh_token == mock.sentinel.refresh_token
        assert credentials.id_token == mock.sentinel.id_token
        assert webbrowser_mock.get().open.called
        assert instance.redirect_uri == f"http://localhost:{port}"

        expected_auth_response = auth_redirect_url.replace("http", "https")
        mock_fetch_token.assert_called_with(
            CLIENT_SECRETS_INFO["web"]["token_uri"],
            client_secret=CLIENT_SECRETS_INFO["web"]["client_secret"],
            authorization_response=expected_auth_response,
            code_verifier="amanaplanacanalpanama",
            audience=None,
        )

    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    @mock.patch("wsgiref.simple_server.make_server", autospec=True)
    def test_run_local_server_no_browser(
        self, make_server_mock, webbrowser_mock, instance, mock_fetch_token
    ):
        def assign_last_request_uri(host, port, wsgi_app, **kwargs):
            wsgi_app.last_request_uri = self.REDIRECT_REQUEST_PATH
            return mock.Mock()

        make_server_mock.side_effect = assign_last_request_uri

        instance.run_local_server(open_browser=False)

        assert not webbrowser_mock.get().open.called

    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    @mock.patch("wsgiref.simple_server.make_server", autospec=True)
    def test_run_local_server_bind_addr(
        self, make_server_mock, webbrowser_mock, instance, mock_fetch_token
    ):
        def assign_last_request_uri(host, port, wsgi_app, **kwargs):
            wsgi_app.last_request_uri = self.REDIRECT_REQUEST_PATH
            return mock.Mock()

        make_server_mock.side_effect = assign_last_request_uri

        my_ip = socket.gethostbyname(socket.gethostname())
        instance.run_local_server(bind_addr=my_ip, host="localhost")

        assert webbrowser_mock.get().open.called
        name, args, kwargs = make_server_mock.mock_calls[0]
        assert args[0] == my_ip

    @pytest.mark.webtest
    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    def test_run_local_server_occupied_port(
        self, webbrowser_mock, instance, mock_fetch_token, port, socket
    ):
        # socket fixture is already bound to http://localhost:port
        with pytest.raises(OSError):
            instance.run_local_server(port=port, timeout_seconds=1)

    @pytest.mark.webtest
    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    def test_run_local_server_exclusive_port(
        self, webbrowser_mock, instance, mock_fetch_token, port
    ):
        """Verify that while run_local_server is running, another socket cannot bind to its port."""
        auth_redirect_url = urllib.parse.urljoin(
            f"http://localhost:{port}", self.REDIRECT_REQUEST_PATH
        )

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(partial(instance.run_local_server, port=port))
            time.sleep(0.2)

            hijack_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hijack_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                with pytest.raises(OSError):
                    hijack_socket.bind(("localhost", port))
            finally:
                hijack_socket.close()
                while not future.done():
                    try:
                        requests.get(auth_redirect_url)
                    except requests.ConnectionError:  # pragma: NO COVER
                        pass

            credentials = future.result()

        assert credentials.token == mock.sentinel.access_token

    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    @mock.patch("wsgiref.simple_server.make_server", autospec=True)
    def test_run_local_server_uses_exclusive_server_class(
        self, make_server_mock, webbrowser_mock, instance
    ):
        server_mock = mock.MagicMock()
        make_server_mock.return_value = server_mock

        with pytest.raises(Exception):
            instance.run_local_server(port=0)

        make_server_mock.assert_called_once()
        assert (
            make_server_mock.call_args.kwargs.get("server_class")
            is flow._ExclusiveWSGIServer
        )

    @mock.patch("google_auth_oauthlib.flow.webbrowser.get", autospec=True)
    @mock.patch("wsgiref.simple_server.make_server", autospec=True)
    def test_local_server_socket_cleanup(
        self, make_server_mock, webbrowser_mock, instance
    ):
        server_mock = mock.MagicMock()
        make_server_mock.return_value = server_mock
        webbrowser_mock.side_effect = webbrowser.Error("Browser not found")

        with pytest.raises(webbrowser.Error):
            instance.run_local_server()

        server_mock.server_close.assert_called_once()

    @mock.patch("builtins.print")
    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    def test_run_local_server_logs_and_prints_url(
        self, webbrowser_mock, print_mock, instance, mock_fetch_token, port, caplog
    ):
        auth_redirect_url = urllib.parse.urljoin(
            f"http://localhost:{port}", self.REDIRECT_REQUEST_PATH
        )

        # Configure caplog to capture INFO logs
        caplog.set_level(logging.INFO, logger="google_auth_oauthlib.flow")

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(partial(instance.run_local_server, port=port))

            while not future.done():
                try:
                    requests.get(auth_redirect_url)
                except requests.ConnectionError:
                    pass

            future.result()

        # Verify log message
        assert "Please visit this URL" in caplog.text
        assert urllib.parse.quote(instance.redirect_uri, safe="") in caplog.text

        # Verify print message
        print_mock.assert_called_once()
        assert "Please visit this URL" in print_mock.call_args[0][0]
        assert (
            urllib.parse.quote(instance.redirect_uri, safe="")
            in print_mock.call_args[0][0]
        )

    @mock.patch("google_auth_oauthlib.flow.webbrowser", autospec=True)
    @mock.patch("wsgiref.simple_server.make_server", autospec=True)
    def test_run_local_server_timeout(
        self, make_server_mock, webbrowser_mock, instance, mock_fetch_token
    ):
        mock_server = mock.Mock()
        make_server_mock.return_value = mock_server

        # handle_request does nothing (simulating timeout), so last_request_uri remains None
        mock_server.handle_request.return_value = None

        with pytest.raises(flow.WSGITimeoutError):
            instance.run_local_server(timeout_seconds=1)

        webbrowser_mock.get.assert_called_with(None)
        webbrowser_mock.get.return_value.open.assert_called_once()


class TestExclusiveWSGIServer(object):
    def test_exclusive_wsgi_server_bind_windows(self):
        with (
            mock.patch("sys.platform", "win32"),
            mock.patch("google_auth_oauthlib.flow.socket") as mock_socket,
        ):
            mock_socket.SOL_SOCKET = socket.SOL_SOCKET
            mock_socket.SO_EXCLUSIVEADDRUSE = getattr(socket, "SO_EXCLUSIVEADDRUSE", 1)
            mock_socket.AF_INET = socket.AF_INET
            mock_socket.AF_INET6 = socket.AF_INET6
            mock_socket.SOCK_STREAM = socket.SOCK_STREAM
            mock_socket.socket.return_value.__enter__.return_value.connect_ex.return_value = 1

            server = flow._ExclusiveWSGIServer(
                ("localhost", 8085), flow._WSGIRequestHandler, bind_and_activate=False
            )
            server.socket = mock.Mock()

            with mock.patch.object(wsgiref.simple_server.WSGIServer, "server_bind"):
                server.server_bind()
                server.socket.setsockopt.assert_called_once_with(
                    mock_socket.SOL_SOCKET, mock_socket.SO_EXCLUSIVEADDRUSE, 1
                )
                server._ipv6_socket.setsockopt.assert_called_once_with(
                    mock_socket.SOL_SOCKET, mock_socket.SO_EXCLUSIVEADDRUSE, 1
                )
                server._ipv6_socket.bind.assert_called_once_with(("::1", 8085))
                server.server_close()
                assert server._ipv6_socket is None

    def test_exclusive_wsgi_server_bind_non_windows(self):
        with mock.patch("sys.platform", "linux"):
            server = flow._ExclusiveWSGIServer(
                ("localhost", 0), flow._WSGIRequestHandler, bind_and_activate=False
            )
            server.socket = mock.Mock()

            with mock.patch.object(wsgiref.simple_server.WSGIServer, "server_bind"):
                server.server_bind()
                server.socket.setsockopt.assert_not_called()
                server.server_close()

    def test_exclusive_wsgi_server_detects_existing_listeners(self):
        with (
            mock.patch("sys.platform", "win32"),
            mock.patch("google_auth_oauthlib.flow.socket") as mock_socket,
        ):
            mock_socket.SOL_SOCKET = socket.SOL_SOCKET
            mock_socket.SO_EXCLUSIVEADDRUSE = 1
            mock_socket.AF_INET = socket.AF_INET
            mock_socket.AF_INET6 = socket.AF_INET6
            mock_socket.SOCK_STREAM = socket.SOCK_STREAM

            server = flow._ExclusiveWSGIServer(
                ("localhost", 8085), flow._WSGIRequestHandler, bind_and_activate=False
            )
            server.socket = mock.Mock()

            # 1. Pre-existing IPv6 listener on ::1 / [::]
            mock_socket.socket.return_value.__enter__.return_value.connect_ex.return_value = 0
            with mock.patch.object(wsgiref.simple_server.WSGIServer, "server_bind"):
                with pytest.raises(OSError):
                    server.server_bind()

            # 2. is_listener_present returns False when socket() raises OSError
            mock_socket.socket.side_effect = OSError("socket error")
            assert not flow._ExclusiveWSGIServer.is_listener_present(
                socket.AF_INET6, "::1", 8085
            )

    def test_exclusive_wsgi_server_ipv4_literal_ignores_ipv6(self):
        # An address literal is served verbatim in redirect_uri, so the browser
        # never resolves `localhost` and `::1` is irrelevant.
        server = flow._ExclusiveWSGIServer(
            ("127.0.0.1", 8085), flow._WSGIRequestHandler, bind_and_activate=False
        )
        server.socket = mock.Mock()

        with (
            mock.patch.object(wsgiref.simple_server.WSGIServer, "server_bind"),
            mock.patch.object(
                flow._ExclusiveWSGIServer, "is_listener_present", return_value=True
            ) as is_listener_present,
        ):
            server.server_bind()

        is_listener_present.assert_not_called()
        assert server._ipv6_socket is None

    def test_exclusive_wsgi_server_ipv6_bind_errors(self):
        import errno

        server = flow._ExclusiveWSGIServer(
            ("localhost", 8085), flow._WSGIRequestHandler, bind_and_activate=False
        )
        server.socket = mock.Mock()

        with (
            mock.patch.object(wsgiref.simple_server.WSGIServer, "server_bind"),
            mock.patch.object(
                flow._ExclusiveWSGIServer, "is_listener_present", return_value=False
            ),
            mock.patch("google_auth_oauthlib.flow.socket") as mock_socket,
        ):
            mock_socket.AF_INET6 = socket.AF_INET6
            mock_socket.SOCK_STREAM = socket.SOCK_STREAM

            # 1. Ignored when socket(AF_INET6) itself raises EAFNOSUPPORT
            mock_socket.socket.side_effect = OSError(
                errno.EAFNOSUPPORT, "IPv6 disabled in kernel"
            )
            server.server_bind()
            assert server._ipv6_socket is None

            # 2. Non-fatal when bind(("::1", ...)) fails but no listener is present
            mock_socket.socket.side_effect = None
            mock_socket.socket.return_value.bind.side_effect = OSError(
                errno.EADDRINUSE, "Held by non-listening socket"
            )
            server.server_bind()
            assert server._ipv6_socket is None
