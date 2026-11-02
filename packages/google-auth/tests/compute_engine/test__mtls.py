# -*- coding: utf-8 -*-
#
# Copyright 2024 Google LLC
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
#

from pathlib import Path
from unittest import mock

import pytest  # type: ignore
import requests

from google.auth import environment_vars, exceptions
from google.auth.compute_engine import _mtls


@pytest.fixture
def mock_mds_mtls_config():
    return _mtls.MdsMtlsConfig(
        ca_cert_path=Path("/fake/ca.crt"),
        client_combined_cert_path=Path("/fake/client.key"),
    )


@mock.patch("os.name", "nt")
def test__MdsMtlsConfig_windows_defaults():
    config = _mtls.MdsMtlsConfig()
    assert (
        str(config.ca_cert_path)
        == "C:/ProgramData/Google/ComputeEngine/mds-mtls-root.crt"
    )
    assert (
        str(config.client_combined_cert_path)
        == "C:/ProgramData/Google/ComputeEngine/mds-mtls-client.key"
    )


@mock.patch("os.name", "posix")
def test__MdsMtlsConfig_non_windows_defaults():
    config = _mtls.MdsMtlsConfig()
    assert str(config.ca_cert_path) == "/run/google-mds-mtls/root.crt"
    assert str(config.client_combined_cert_path) == "/run/google-mds-mtls/client.key"


def test__parse_mds_mode_default(monkeypatch):
    monkeypatch.delenv(environment_vars.GCE_METADATA_MTLS_MODE, raising=False)
    assert _mtls._parse_mds_mode() == _mtls.MdsMtlsMode.NONE


@pytest.mark.parametrize(
    "mode_str, expected_mode",
    [
        ("strict", _mtls.MdsMtlsMode.STRICT),
        ("none", _mtls.MdsMtlsMode.NONE),
        ("default", _mtls.MdsMtlsMode.DEFAULT),
        ("STRICT", _mtls.MdsMtlsMode.STRICT),
    ],
)
def test__parse_mds_mode_valid(monkeypatch, mode_str, expected_mode):
    monkeypatch.setenv(environment_vars.GCE_METADATA_MTLS_MODE, mode_str)
    assert _mtls._parse_mds_mode() == expected_mode


def test__parse_mds_mode_invalid(monkeypatch):
    monkeypatch.setenv(environment_vars.GCE_METADATA_MTLS_MODE, "invalid_mode")
    with pytest.raises(ValueError):
        _mtls._parse_mds_mode()


@mock.patch("google.auth.compute_engine._mtls.os.path.exists")
def test__certs_exist_true(mock_exists, mock_mds_mtls_config):
    mock_exists.return_value = True
    assert _mtls._certs_exist(mock_mds_mtls_config) is True


@mock.patch("google.auth.compute_engine._mtls.os.path.exists")
def test__certs_exist_false(mock_exists, mock_mds_mtls_config):
    mock_exists.return_value = False
    assert _mtls._certs_exist(mock_mds_mtls_config) is False


@pytest.mark.parametrize(
    "mtls_mode, certs_exist, expected_result",
    [
        ("strict", True, True),
        ("strict", False, exceptions.MutualTLSChannelError),
        ("none", True, False),
        ("none", False, False),
        ("default", True, True),
        ("default", False, False),
    ],
)
@mock.patch("google.auth.compute_engine._mtls.os.path.exists")
def test_should_use_mds_mtls(
    mock_exists, monkeypatch, mtls_mode, certs_exist, expected_result
):
    monkeypatch.setenv(environment_vars.GCE_METADATA_MTLS_MODE, mtls_mode)
    mock_exists.return_value = certs_exist

    if isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            _mtls.should_use_mds_mtls()
    else:
        assert _mtls.should_use_mds_mtls() is expected_result


@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_init(mock_ssl_context, mock_mds_mtls_config):
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)
    mock_ssl_context.assert_called_once()
    adapter.ssl_context.load_verify_locations.assert_called_once_with(
        cafile=mock_mds_mtls_config.ca_cert_path
    )
    adapter.ssl_context.load_cert_chain.assert_called_once_with(
        certfile=mock_mds_mtls_config.client_combined_cert_path, password=""
    )


@mock.patch("ssl.create_default_context")
@mock.patch("requests.adapters.HTTPAdapter.init_poolmanager")
def test_mds_mtls_adapter_init_poolmanager(
    mock_init_poolmanager, mock_ssl_context, mock_mds_mtls_config
):
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)
    mock_init_poolmanager.assert_called_with(
        10, 10, block=False, ssl_context=adapter.ssl_context
    )


@mock.patch("ssl.create_default_context")
@mock.patch("requests.adapters.HTTPAdapter.proxy_manager_for")
def test_mds_mtls_adapter_proxy_manager_for(
    mock_proxy_manager_for, mock_ssl_context, mock_mds_mtls_config
):
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)
    adapter.proxy_manager_for("test_proxy")
    mock_proxy_manager_for.assert_called_once_with(
        "test_proxy", ssl_context=adapter.ssl_context
    )


@mock.patch("requests.adapters.HTTPAdapter.send")  # Patch the PARENT class method
@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_session_request(
    mock_ssl_context, mock_super_send, mock_mds_mtls_config
):
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)
    session = requests.Session()
    session.mount("https://", adapter)

    # Setup the parent class send return value
    response = requests.Response()
    response.status_code = 200
    mock_super_send.return_value = response

    response = session.get("https://fake-mds.com")

    # Assert that the request was successful
    assert response.status_code == 200
    mock_super_send.assert_called_once()


@mock.patch("requests.adapters.HTTPAdapter.send")
@mock.patch("google.auth.compute_engine._mtls._parse_mds_mode")
@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_send_success(
    mock_ssl_context, mock_parse_mds_mode, mock_super_send, mock_mds_mtls_config
):
    """Test the explicit 'happy path' where mTLS succeeds without error."""
    mock_parse_mds_mode.return_value = _mtls.MdsMtlsMode.DEFAULT
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)

    # Setup the parent class send return value to be successful (200 OK)
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_super_send.return_value = mock_response

    request = requests.Request(method="GET", url="https://fake-mds.com").prepare()

    # Call send directly
    response = adapter.send(request)

    # Verify we got the response back and no fallback happened
    assert response == mock_response
    mock_super_send.assert_called_once()


@mock.patch("google.auth.compute_engine._mtls.HTTPAdapter")
@mock.patch("google.auth.compute_engine._mtls._parse_mds_mode")
@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_send_fallback_default_mode(
    mock_ssl_context, mock_parse_mds_mode, mock_http_adapter_class, mock_mds_mtls_config
):
    mock_parse_mds_mode.return_value = _mtls.MdsMtlsMode.DEFAULT
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)

    mock_fallback_send = mock.Mock()
    mock_http_adapter_class.return_value.send = mock_fallback_send

    # Simulate SSLError on the super().send() call
    with mock.patch(
        "requests.adapters.HTTPAdapter.send", side_effect=requests.exceptions.SSLError
    ):
        request = requests.Request(method="GET", url="https://fake-mds.com").prepare()
        adapter.send(request)

    # Check that fallback to HTTPAdapter.send occurred
    mock_http_adapter_class.assert_called_once()
    mock_fallback_send.assert_called_once()
    fallback_request = mock_fallback_send.call_args[0][0]
    assert fallback_request.url == "http://fake-mds.com/"


@mock.patch("google.auth.compute_engine._mtls.HTTPAdapter")
@mock.patch("google.auth.compute_engine._mtls._parse_mds_mode")
@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_send_fallback_http_error(
    mock_ssl_context, mock_parse_mds_mode, mock_http_adapter_class, mock_mds_mtls_config
):
    mock_parse_mds_mode.return_value = _mtls.MdsMtlsMode.DEFAULT
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)

    mock_fallback_send = mock.Mock()
    mock_http_adapter_class.return_value.send = mock_fallback_send

    # Simulate HTTPError on the super().send() call
    mock_mtls_response = requests.Response()
    mock_mtls_response.status_code = 404
    with mock.patch(
        "requests.adapters.HTTPAdapter.send", return_value=mock_mtls_response
    ):
        request = requests.Request(method="GET", url="https://fake-mds.com").prepare()
        adapter.send(request)

    # Check that fallback to HTTPAdapter.send occurred
    mock_http_adapter_class.assert_called_once()
    mock_fallback_send.assert_called_once()
    fallback_request = mock_fallback_send.call_args[0][0]
    assert fallback_request.url == "http://fake-mds.com/"


@mock.patch("google.auth.compute_engine._mtls._parse_mds_mode")
@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_send_fallback_connection_error(
    mock_ssl_context, mock_parse_mds_mode, mock_mds_mtls_config
):
    mock_parse_mds_mode.return_value = _mtls.MdsMtlsMode.DEFAULT
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)

    mock_mtls_response = mock.Mock(spec=requests.Response)
    mock_mtls_response.status_code = 200

    with mock.patch(
        "requests.adapters.HTTPAdapter.send",
        side_effect=[requests.exceptions.ConnectionError, mock_mtls_response],
    ):
        request = requests.Request(method="GET", url="https://fake-mds.com").prepare()
        response = adapter.send(request)

    assert response == mock_mtls_response
    assert request.url == "http://fake-mds.com/"


@mock.patch("google.auth.compute_engine._mtls._parse_mds_mode")
@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_send_fallback_timeout(
    mock_ssl_context, mock_parse_mds_mode, mock_mds_mtls_config
):
    mock_parse_mds_mode.return_value = _mtls.MdsMtlsMode.DEFAULT
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)

    mock_mtls_response = mock.Mock(spec=requests.Response)
    mock_mtls_response.status_code = 200

    with mock.patch(
        "requests.adapters.HTTPAdapter.send",
        side_effect=[requests.exceptions.Timeout, mock_mtls_response],
    ):
        request = requests.Request(method="GET", url="https://fake-mds.com").prepare()
        response = adapter.send(request)

    assert response == mock_mtls_response
    assert request.url == "http://fake-mds.com/"


@mock.patch("requests.adapters.HTTPAdapter.send")
@mock.patch("google.auth.compute_engine._mtls._parse_mds_mode")
@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_send_no_fallback_other_exception(
    mock_ssl_context, mock_parse_mds_mode, mock_http_adapter_send, mock_mds_mtls_config
):
    mock_parse_mds_mode.return_value = _mtls.MdsMtlsMode.DEFAULT
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)

    mock_http_adapter_send.side_effect = ValueError("Unhandled exception")
    request = requests.Request(method="GET", url="https://fake-mds.com").prepare()
    with pytest.raises(ValueError, match="Unhandled exception"):
        adapter.send(request)

    mock_http_adapter_send.assert_called_once()


@mock.patch("google.auth.compute_engine._mtls._parse_mds_mode")
@mock.patch("ssl.create_default_context")
def test_mds_mtls_adapter_send_no_fallback_strict_mode(
    mock_ssl_context, mock_parse_mds_mode, mock_mds_mtls_config
):
    mock_parse_mds_mode.return_value = _mtls.MdsMtlsMode.STRICT
    adapter = _mtls.MdsMtlsAdapter(mock_mds_mtls_config)

    # Simulate SSLError on the super().send() call
    with mock.patch(
        "requests.adapters.HTTPAdapter.send", side_effect=requests.exceptions.SSLError
    ):
        request = requests.Request(method="GET", url="https://fake-mds.com").prepare()
        with pytest.raises(requests.exceptions.SSLError):
            adapter.send(request)
