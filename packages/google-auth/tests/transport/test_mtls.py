# Copyright 2020 Google LLC
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

import contextlib
import ssl
from unittest import mock

import pytest  # type: ignore

from google.auth import exceptions
from google.auth.transport import _mtls_helper, mtls


@mock.patch("google.auth.transport._mtls_helper._get_cert_config_path")
@mock.patch("google.auth.transport._mtls_helper._check_config_path")
def test_has_default_client_cert_source_with_context_aware_metadata(
    mock_check, mock_get_cert
):
    """
    Directly tests the logic: if CONTEXT_AWARE_METADATA_PATH is found, return True.
    """

    # Setup: _get_cert_config_path returns None, so it falls back to context aware metadata
    mock_get_cert.return_value = None

    def side_effect(path):
        if path == _mtls_helper.CONTEXT_AWARE_METADATA_PATH:
            return "/path/to/context_aware_metadata.json"
        return None

    mock_check.side_effect = side_effect

    # Execute
    result = mtls.has_default_client_cert_source(True)

    # Assert
    assert result is True
    mock_get_cert.assert_called_once_with(None, True)
    mock_check.assert_any_call(_mtls_helper.CONTEXT_AWARE_METADATA_PATH)


@mock.patch("google.auth.transport._mtls_helper._get_cert_config_path")
@mock.patch("google.auth.transport._mtls_helper._check_config_path")
def test_has_default_client_cert_source_without_context_aware(
    mock_check, mock_get_cert
):
    """
    Tests that if include_context_aware is False, it skips checking CONTEXT_AWARE_METADATA_PATH.
    """
    mock_get_cert.return_value = None

    result = mtls.has_default_client_cert_source(include_context_aware=False)

    assert result is False
    mock_get_cert.assert_called_once_with(None, False)
    mock_check.assert_not_called()


@mock.patch(
    "google.auth.transport._mtls_helper._load_json_file",
    return_value={
        "cert_configs": {"workload": {"cert_path": "cert.pem", "key_path": "key.pem"}}
    },
)
@mock.patch("google.auth.transport._mtls_helper._check_config_path")
@mock.patch("google.auth.transport._mtls_helper._get_cert_config_path")
def test_has_default_client_cert_source_falls_back(
    mock_get_cert, mock_check, mock_load_json
):
    """
    Tests that it checks X.509 WIF first, and if found, returns True without checking context aware metadata.
    """

    # Setup: First path is valid
    mock_get_cert.return_value = "/path/to/default_cert.json"

    # Execute
    result = mtls.has_default_client_cert_source(True)

    # Assert
    assert result is True
    # Verify the sequence of calls
    mock_get_cert.assert_called_once_with(None, True)
    mock_check.assert_not_called()


@mock.patch(
    "google.auth.transport._mtls_helper._load_json_file",
    return_value={
        "cert_configs": {"workload": {"cert_path": "cert.pem", "key_path": "key.pem"}}
    },
    autospec=True,
)
@mock.patch("google.auth.transport._mtls_helper._get_cert_config_path", autospec=True)
@mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
def test_has_default_client_cert_source_env_var_success(
    check_config_path, get_cert_config_path, mock_load_json
):
    check_config_path.return_value = None
    get_cert_config_path.return_value = "/absolute/path/to/cert.json"

    assert mtls.has_default_client_cert_source(True)

    get_cert_config_path.assert_called_with(None, True)


@mock.patch("google.auth.transport._mtls_helper._get_cert_config_path", autospec=True)
@mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
def test_has_default_client_cert_source_env_var_invalid_config_path(
    check_config_path, get_cert_config_path
):
    check_config_path.return_value = None
    get_cert_config_path.return_value = None

    assert not mtls.has_default_client_cert_source(True)


@mock.patch("google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True)
@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
def test_default_client_cert_source(
    has_default_client_cert_source, get_client_cert_and_key
):
    # Test default client cert source doesn't exist.
    has_default_client_cert_source.return_value = False
    with pytest.raises(exceptions.MutualTLSChannelError):
        mtls.default_client_cert_source()

    # The following tests will assume default client cert source exists.
    has_default_client_cert_source.return_value = True

    # Test good callback.
    get_client_cert_and_key.return_value = (True, b"cert", b"key")
    callback = mtls.default_client_cert_source()
    assert callback() == (b"cert", b"key")

    # Test bad callback which throws exception.
    get_client_cert_and_key.side_effect = ValueError()
    callback = mtls.default_client_cert_source()
    with pytest.raises(exceptions.MutualTLSChannelError):
        callback()

    # Test bad callback which throws ClientCertError.
    get_client_cert_and_key.side_effect = exceptions.ClientCertError()
    callback = mtls.default_client_cert_source()
    with pytest.raises(exceptions.ClientCertError):
        callback()


@mock.patch(
    "google.auth.transport._mtls_helper.get_client_ssl_credentials", autospec=True
)
@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
def test_default_client_encrypted_cert_source(
    has_default_client_cert_source, get_client_ssl_credentials
):
    # Test default client cert source doesn't exist.
    has_default_client_cert_source.return_value = False
    with pytest.raises(exceptions.MutualTLSChannelError):
        mtls.default_client_encrypted_cert_source("cert_path", "key_path")

    # The following tests will assume default client cert source exists.
    has_default_client_cert_source.return_value = True

    # Test good callback.
    get_client_ssl_credentials.return_value = (True, b"cert", b"key", b"passphrase")
    callback = mtls.default_client_encrypted_cert_source("cert_path", "key_path")
    with mock.patch("google.auth.transport.mtls.open", mock.mock_open()) as mock_file:
        assert callback() == ("cert_path", "key_path", b"passphrase")
        mock_file.assert_any_call("cert_path", "wb")
        mock_file.assert_any_call("key_path", "wb")

    # Test bad callback which throws exception.
    get_client_ssl_credentials.side_effect = exceptions.ClientCertError()
    callback = mtls.default_client_encrypted_cert_source("cert_path", "key_path")
    with pytest.raises(exceptions.MutualTLSChannelError):
        callback()


@mock.patch("google.auth.transport._mtls_helper.check_use_client_cert", autospec=True)
def test_should_use_client_cert(check_use_client_cert):
    check_use_client_cert.return_value = mock.Mock()
    assert mtls.should_use_client_cert()

    check_use_client_cert.return_value = False
    assert not mtls.should_use_client_cert()


@contextlib.contextmanager
def _fake_secure_paths(cert_bytes, key_bytes, passphrase=None):
    yield "cert_path", "key_path", passphrase


@mock.patch(
    "google.auth.transport._mtls_helper.secure_cert_key_paths",
    side_effect=_fake_secure_paths,
)
def test_load_client_cert_into_context_success(mock_secure_paths):
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    result = mtls._load_client_cert_into_context(
        mock_ctx, b"cert", b"key", passphrase=b"passphrase"
    )
    assert result is None
    mock_secure_paths.assert_called_once_with(b"cert", b"key", passphrase=b"passphrase")
    mock_ctx.load_cert_chain.assert_called_once_with(
        certfile="cert_path", keyfile="key_path", password=b"passphrase"
    )


@mock.patch(
    "google.auth.transport._mtls_helper.secure_cert_key_paths",
    side_effect=_fake_secure_paths,
)
def test_load_client_cert_into_context_success_no_passphrase(mock_secure_paths):
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    result = mtls._load_client_cert_into_context(mock_ctx, b"cert", b"key")
    assert result is None
    mock_secure_paths.assert_called_once_with(b"cert", b"key", passphrase=None)
    mock_ctx.load_cert_chain.assert_called_once_with(
        certfile="cert_path", keyfile="key_path", password=None
    )


@pytest.mark.parametrize(
    "exception",
    [
        ssl.SSLError("mock error message"),
        OSError("mock error message"),
        ValueError("mock error message"),
        RuntimeError("mock error message"),
        TypeError("mock error message"),
    ],
)
@mock.patch(
    "google.auth.transport._mtls_helper.secure_cert_key_paths",
    side_effect=_fake_secure_paths,
)
def test_load_client_cert_into_context_error(mock_secure_paths, exception):
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    mock_ctx.load_cert_chain.side_effect = exception
    with pytest.raises(exceptions.MutualTLSChannelError) as exc_info:
        mtls._load_client_cert_into_context(mock_ctx, b"cert", b"key")
    assert "mock error message" in str(exc_info.value)
    assert isinstance(exc_info.value.__cause__, type(exception))


@pytest.mark.parametrize("invalid_ctx", [None, object()])
def test_load_client_cert_into_context_invalid_ctx(invalid_ctx):
    with pytest.raises(exceptions.MutualTLSChannelError) as exc_info:
        mtls._load_client_cert_into_context(invalid_ctx, b"cert", b"key")
    assert (
        "The provided context object is invalid or does not support loading certificate chains"
        in str(exc_info.value)
    )
    assert exc_info.value.__cause__ is None


@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
def test_load_default_client_cert_disabled(mock_should_use):
    mock_should_use.return_value = False
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    assert mtls.load_default_client_cert(mock_ctx) is False
    mock_ctx.load_cert_chain.assert_not_called()


@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
def test_load_default_client_cert_no_source(mock_should_use, mock_has_source):
    mock_should_use.return_value = True
    mock_has_source.return_value = False
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    assert mtls.load_default_client_cert(mock_ctx) is False
    mock_ctx.load_cert_chain.assert_not_called()


@mock.patch(
    "google.auth.transport._mtls_helper.get_client_ssl_credentials", autospec=True
)
@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
def test_load_default_client_cert_no_cert(
    mock_should_use, mock_has_source, mock_get_credentials
):
    mock_should_use.return_value = True
    mock_has_source.return_value = True
    mock_get_credentials.return_value = (False, None, None, None)
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    assert mtls.load_default_client_cert(mock_ctx) is False
    mock_ctx.load_cert_chain.assert_not_called()


@mock.patch(
    "google.auth.transport._mtls_helper.secure_cert_key_paths",
    side_effect=_fake_secure_paths,
)
@mock.patch(
    "google.auth.transport._mtls_helper.get_client_ssl_credentials", autospec=True
)
@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
def test_load_default_client_cert_success(
    mock_should_use, mock_has_source, mock_get_credentials, mock_secure_paths
):
    mock_should_use.return_value = True
    mock_has_source.return_value = True
    mock_get_credentials.return_value = (True, b"cert", b"key", b"passphrase")
    mock_ctx = mock.Mock(spec=ssl.SSLContext)

    assert mtls.load_default_client_cert(mock_ctx) is True
    mock_ctx.load_cert_chain.assert_called_once_with(
        certfile="cert_path", keyfile="key_path", password=b"passphrase"
    )


@mock.patch(
    "google.auth.transport._mtls_helper.get_client_ssl_credentials", autospec=True
)
@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
def test_load_default_client_cert_propagates_client_cert_error(
    mock_should_use, mock_has_source, mock_get_credentials
):
    mock_should_use.return_value = True
    mock_has_source.return_value = True
    mock_get_credentials.side_effect = exceptions.ClientCertError("credentials failure")
    mock_ctx = mock.Mock(spec=ssl.SSLContext)

    with pytest.raises(exceptions.MutualTLSChannelError) as exc_info:
        mtls.load_default_client_cert(mock_ctx)
    assert "credentials failure" in str(exc_info.value)
    assert isinstance(exc_info.value.__cause__, exceptions.ClientCertError)


@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
@mock.patch("google.auth.transport.mtls.load_default_client_cert", autospec=True)
@mock.patch("ssl.create_default_context", autospec=True)
def test_get_default_ssl_context_configured(
    mock_create_context, mock_load_default, mock_should_use, mock_has_source
):
    mock_should_use.return_value = True
    mock_has_source.return_value = True
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    mock_create_context.return_value = mock_ctx
    mock_load_default.return_value = True

    result = mtls.get_default_ssl_context()

    assert result == mock_ctx
    mock_create_context.assert_called_once_with(ssl.Purpose.SERVER_AUTH)
    mock_load_default.assert_called_once_with(mock_ctx)


@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
@mock.patch("google.auth.transport.mtls.load_default_client_cert", autospec=True)
@mock.patch("ssl.create_default_context", autospec=True)
def test_get_default_ssl_context_unconfigured(
    mock_create_context, mock_load_default, mock_should_use, mock_has_source
):
    mock_should_use.return_value = True
    mock_has_source.return_value = True
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    mock_create_context.return_value = mock_ctx
    mock_load_default.return_value = False

    result = mtls.get_default_ssl_context()

    assert result is None
    mock_create_context.assert_called_once_with(ssl.Purpose.SERVER_AUTH)
    mock_load_default.assert_called_once_with(mock_ctx)


@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
@mock.patch("google.auth.transport.mtls.load_default_client_cert", autospec=True)
@mock.patch("ssl.create_default_context", autospec=True)
def test_get_default_ssl_context_exception(
    mock_create_context, mock_load_default, mock_should_use, mock_has_source
):
    mock_should_use.return_value = True
    mock_has_source.return_value = True
    mock_ctx = mock.Mock(spec=ssl.SSLContext)
    mock_create_context.return_value = mock_ctx
    mock_load_default.side_effect = exceptions.MutualTLSChannelError(
        "mock error message"
    )

    with pytest.raises(exceptions.MutualTLSChannelError) as exc_info:
        mtls.get_default_ssl_context()
    assert "mock error message" in str(exc_info.value)


@pytest.mark.parametrize(
    "env_val,client_cert_available,expected",
    [
        ("always", True, True),
        ("always", False, True),
        ("never", True, False),
        ("never", False, False),
        ("auto", True, True),
        ("auto", False, False),
        (None, True, True),  # Defaults to auto
        (None, False, False),  # Defaults to auto
        ("ALWAYS", True, True),
        ("ALWAYS", False, True),
        ("NEVER", True, False),
        ("NEVER", False, False),
        ("AUTO", True, True),
        ("AUTO", False, False),
        ("", True, True),
        ("", False, False),
    ],
)
@mock.patch("google.auth.transport.mtls.getenv", autospec=True)
def test_should_use_mtls_endpoint(
    mock_getenv, env_val, client_cert_available, expected
):
    mock_getenv.side_effect = lambda var, default=None: (
        env_val
        if (var == "GOOGLE_API_USE_MTLS_ENDPOINT" and env_val is not None)
        else default
    )
    result = mtls.should_use_mtls_endpoint(client_cert_available)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_value",
    [
        "invalid_value",
        "   ",
        "\t",
    ],
)
@mock.patch("google.auth.transport.mtls.getenv", autospec=True)
def test_should_use_mtls_endpoint_invalid_value(mock_getenv, invalid_value):
    mock_getenv.side_effect = lambda var, default=None: (
        invalid_value if var == "GOOGLE_API_USE_MTLS_ENDPOINT" else default
    )
    with pytest.raises(exceptions.MutualTLSChannelError) as exc_info:
        mtls.should_use_mtls_endpoint(True)
    assert "Unsupported GOOGLE_API_USE_MTLS_ENDPOINT value" in str(exc_info.value)
    assert f"'{invalid_value.strip().lower()}'" in str(exc_info.value)


@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
@mock.patch("google.auth.transport.mtls.getenv", autospec=True)
def test_should_use_mtls_endpoint_default_client_cert(
    mock_getenv, mock_should_use_client_cert
):
    mock_getenv.side_effect = lambda var, default=None: (
        "auto" if var == "GOOGLE_API_USE_MTLS_ENDPOINT" else default
    )
    mock_should_use_client_cert.return_value = True
    assert mtls.should_use_mtls_endpoint() is True
    mock_should_use_client_cert.assert_called_once()

    mock_should_use_client_cert.reset_mock()

    mock_should_use_client_cert.return_value = False
    assert mtls.should_use_mtls_endpoint() is False
    mock_should_use_client_cert.assert_called_once()


@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
def test_get_default_ssl_context_not_should_use(mock_has_default, mock_should_use):
    mock_should_use.return_value = False
    mock_has_default.return_value = True

    result = mtls.get_default_ssl_context()
    assert result is None


@mock.patch("google.auth.transport.mtls.should_use_client_cert", autospec=True)
@mock.patch("google.auth.transport.mtls.has_default_client_cert_source", autospec=True)
def test_get_default_ssl_context_no_default_source(mock_has_default, mock_should_use):
    mock_should_use.return_value = True
    mock_has_default.return_value = False

    result = mtls.get_default_ssl_context()
    assert result is None


@mock.patch(
    "google.auth.transport._mtls_helper._get_cert_config_path",
    return_value=None,
    autospec=True,
)
@mock.patch(
    "google.auth._agent_identity_utils._is_certificate_file_ready",
    return_value=True,
    autospec=True,
)
def test_has_default_client_cert_source_gke_bundle(mock_is_ready, mock_get_cert):
    assert mtls.has_default_client_cert_source(include_context_aware=False) is True
    mock_is_ready.assert_called_once_with(_mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH)


@mock.patch(
    "google.auth.transport._mtls_helper._load_json_file",
    return_value={"cert_configs": {}},
    autospec=True,
)
@mock.patch(
    "google.auth.transport._mtls_helper._get_cert_config_path",
    return_value="/home/user/.config/gcloud/certificate_config.json",
    autospec=True,
)
@mock.patch(
    "google.auth._agent_identity_utils._is_certificate_file_ready",
    return_value=True,
    autospec=True,
)
def test_has_default_client_cert_source_config_without_workload_no_gke_fallback(
    mock_is_ready, mock_get_cert, mock_load_json
):
    assert mtls.has_default_client_cert_source(include_context_aware=False) is False
    mock_is_ready.assert_not_called()


@pytest.mark.parametrize(
    "side_effect",
    [
        exceptions.ClientCertError("Invalid JSON"),
        OSError("Permission denied"),
    ],
)
@mock.patch(
    "google.auth.transport._mtls_helper._load_json_file",
    autospec=True,
)
@mock.patch(
    "google.auth.transport._mtls_helper._get_cert_config_path",
    return_value="/home/user/.config/gcloud/certificate_config.json",
    autospec=True,
)
@mock.patch(
    "google.auth._agent_identity_utils._is_certificate_file_ready",
    return_value=True,
    autospec=True,
)
def test_has_default_client_cert_source_malformed_config_no_gke_fallback(
    mock_is_ready, mock_get_cert, mock_load_json, side_effect
):
    mock_load_json.side_effect = side_effect

    assert mtls.has_default_client_cert_source(include_context_aware=False) is True
    mock_is_ready.assert_not_called()
