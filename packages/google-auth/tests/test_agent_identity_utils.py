# Copyright 2025 Google LLC
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

import base64
import hashlib
import json
import os
import stat
import urllib.parse
from unittest import mock

import pytest
from cryptography import x509

from google.auth import _agent_identity_utils, environment_vars, exceptions
from google.auth.transport import _mtls_helper

# A mock PEM-encoded certificate without an Agent Identity SPIFFE ID.
NON_AGENT_IDENTITY_CERT_BYTES = (
    b"-----BEGIN CERTIFICATE-----\n"
    b"MIIDIzCCAgugAwIBAgIJAMfISuBQ5m+5MA0GCSqGSIb3DQEBBQUAMBUxEzARBgNV\n"
    b"BAMTCnVuaXQtdGVzdHMwHhcNMTExMjA2MTYyNjAyWhcNMjExMjAzMTYyNjAyWjAV\n"
    b"MRMwEQYDVQQDEwp1bml0LXRlc3RzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n"
    b"CgKCAQEA4ej0p7bQ7L/r4rVGUz9RN4VQWoej1Bg1mYWIDYslvKrk1gpj7wZgkdmM\n"
    b"7oVK2OfgrSj/FCTkInKPqaCR0gD7K80q+mLBrN3PUkDrJQZpvRZIff3/xmVU1Wer\n"
    b"uQLFJjnFb2dqu0s/FY/2kWiJtBCakXvXEOb7zfbINuayL+MSsCGSdVYsSliS5qQp\n"
    b"gyDap+8b5fpXZVJkq92hrcNtbkg7hCYUJczt8n9hcCTJCfUpApvaFQ18pe+zpyl4\n"
    b"+WzkP66I28hniMQyUlA1hBiskT7qiouq0m8IOodhv2fagSZKjOTTU2xkSBc//fy3\n"
    b"ZpsL7WqgsZS7Q+0VRK8gKfqkxg5OYQIDAQABo3YwdDAdBgNVHQ4EFgQU2RQ8yO+O\n"
    b"gN8oVW2SW7RLrfYd9jEwRQYDVR0jBD4wPIAU2RQ8yO+OgN8oVW2SW7RLrfYd9jGh\n"
    b"GaQXMBUxEzARBgNVBAMTCnVuaXQtdGVzdHOCCQDHyErgUOZvuTAMBgNVHRMEBTAD\n"
    b"AQH/MA0GCSqGSIb3DQEBBQUAA4IBAQBRv+M/6+FiVu7KXNjFI5pSN17OcW5QUtPr\n"
    b"odJMlWrJBtynn/TA1oJlYu3yV5clc/71Vr/AxuX5xGP+IXL32YDF9lTUJXG/uUGk\n"
    b"+JETpKmQviPbRsvzYhz4pf6ZIOZMc3/GIcNq92ECbseGO+yAgyWUVKMmZM0HqXC9\n"
    b"ovNslqe0M8C1sLm1zAR5z/h/litE7/8O2ietija3Q/qtl2TOXJdCA6sgjJX2WUql\n"
    b"ybrC55ct18NKf3qhpcEkGQvFU40rVYApJpi98DiZPYFdx1oBDp/f4uZ3ojpxRVFT\n"
    b"cDwcJLfNRCPUhormsY7fDS9xSyThiHsW9mjJYdcaKQkwYZ0F11yB\n"
    b"-----END CERTIFICATE-----\n"
)


# Synthetic self-signed test certificate (CN=agent-identity-test) with SAN URI
# "spiffe://agents.global.proj-12345.system.id.goog/workload".
# To regenerate safely, use cryptography.x509.CertificateBuilder with a
# throwaway key (discard the private key; never commit it) and a dummy project
# ID in the SPIFFE URI.
AGENT_IDENTITY_CERT_BYTES = (
    b"-----BEGIN CERTIFICATE-----\n"
    b"MIIDEjCCAfqgAwIBAgIUKZAXnXnxf8hsn+ojS1N8bN3hXrUwDQYJKoZIhvcNAQEL\n"
    b"BQAwHjEcMBoGA1UEAwwTYWdlbnQtaWRlbnRpdHktdGVzdDAeFw0yNDAxMDEwMDAw\n"
    b"MDBaFw0zNDAxMDEwMDAwMDBaMB4xHDAaBgNVBAMME2FnZW50LWlkZW50aXR5LXRl\n"
    b"c3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC+3eSHkp1oBj7rFehL\n"
    b"5VJmBF9KLZ5PXQuZNYrGSpxGJ0Dx1T5ancrl8e66AfAepw9O4zdA+8Afub39PQLh\n"
    b"wMTEY3O9Uqetch+2apkwXQ+yYpnorgMwqykY77ptApA8WPHzEOj58FPtyC4UqXJ7\n"
    b"YKVpN92lVi1l73XBn6axo/q72KjeEdssR6UMtAd3dbGqY3af/AZNppJWRmCMWs8Z\n"
    b"oAuxTH5LqYuxwvCDfYLpmQSbv4IJ/UBjkvjRIlzPo2zHg9PMdf/j6Bg9n3kkFaVH\n"
    b"Oep+Zm+DtdT8JvwnG3sQ8Qn/ZCqU0z3DkT//XaElAikLwr/1MFrVHhfrYEWnDvuy\n"
    b"9PHxAgMBAAGjSDBGMEQGA1UdEQQ9MDuGOXNwaWZmZTovL2FnZW50cy5nbG9iYWwu\n"
    b"cHJvai0xMjM0NS5zeXN0ZW0uaWQuZ29vZy93b3JrbG9hZDANBgkqhkiG9w0BAQsF\n"
    b"AAOCAQEAWEyBk7TbetWeQTYEdJwH/pNmiqoCzDYcqCSuNqJhrItHuLmSAlKBGCz6\n"
    b"I6ptzY6vT7ARXoW07ivf9Ffl3TMUDLjd5Tkfn1q8JjyM1Ugbfuq7rdF2g9+5h6wg\n"
    b"tjeV10LqAimr+fFaNvRiGsMfokuwPyUKYe/9d6x5NhcTTNgMQDG5SWnRe1JqPy94\n"
    b"GKilWCyzDl4qzHAU5gc7lZ/6WKbYPwjJDDT4/d3AvNx1O/cQCG7Mz4veDuG2Jqh+\n"
    b"FPUqQ4G9RL4zdPuXlbKfSknkmZWld1+adyitai6BzDCG9zkEEVJmLE2/e3XvNC93\n"
    b"fa2asspu5y/ViCmPS0J2rzWEk7zI5w==\n"
    b"-----END CERTIFICATE-----\n"
)


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    monkeypatch.delenv(
        environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE,
        raising=False,
    )
    monkeypatch.delenv(
        environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE,
        raising=False,
    )
    monkeypatch.delenv(
        environment_vars.GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN,
        raising=False,
    )
    monkeypatch.delenv(
        environment_vars.GOOGLE_API_PREVENT_AGENT_TOKEN_SHARING_FOR_GCP_SERVICES,
        raising=False,
    )


class TestAgentIdentityUtils:
    @mock.patch("cryptography.x509.load_pem_x509_certificate")
    def test_parse_certificate(self, mock_load_cert):
        mock_load_cert.return_value = mock.sentinel.cert
        result = _agent_identity_utils.parse_certificate(b"cert_bytes")
        mock_load_cert.assert_called_once_with(b"cert_bytes")
        assert result == mock.sentinel.cert

    @pytest.mark.parametrize("invalid_input", [b"", None])
    def test_parse_certificate_empty_or_none_raises_value_error(self, invalid_input):
        with pytest.raises(
            ValueError, match="Certificate bytes cannot be empty or None"
        ):
            _agent_identity_utils.parse_certificate(invalid_input)

    @pytest.mark.parametrize(
        "second_cert_block",
        [
            # Valid Base64, invalid ASN.1 DER
            b"-----BEGIN CERTIFICATE-----\n"
            + base64.b64encode(b"not valid asn1 der payload")
            + b"\n-----END CERTIFICATE-----\n",
            # Corrupted Base64
            b"-----BEGIN CERTIFICATE-----\n!!!not_base64!!!\n-----END CERTIFICATE-----\n",
            # Non-UTF-8 bytes
            b"-----BEGIN CERTIFICATE-----\n\xff\xfe\xfd\n-----END CERTIFICATE-----\n",
            # Truncated block missing END CERTIFICATE
            b"-----BEGIN CERTIFICATE-----\nMIIB\n",
            # Truncated block missing BEGIN CERTIFICATE
            b"MIIB\n-----END CERTIFICATE-----\n",
        ],
    )
    def test_parse_certificate_full_chain_rejects_malformed_intermediate(
        self, second_cert_block
    ):
        chain_bytes = NON_AGENT_IDENTITY_CERT_BYTES + second_cert_block
        with pytest.raises(ValueError):
            _agent_identity_utils.parse_certificate(chain_bytes)

    def test_is_certificate_file_ready_empty_path(self):
        result = _agent_identity_utils._is_certificate_file_ready("")
        assert result is False

    def test_is_in_well_known_dir_empty_path(self):
        assert _agent_identity_utils._is_in_well_known_dir("") is False

    def test_is_in_well_known_dir_resolves_symlinks(self, tmpdir, monkeypatch):
        real_run_dir = tmpdir.mkdir("run")
        var_dir = tmpdir.mkdir("var")
        symlink_var_run = var_dir.join("run")
        os.symlink(str(real_run_dir), str(symlink_var_run))

        well_known_via_symlink = os.path.join(
            str(symlink_var_run),
            "secrets",
            "workload-spiffe-credentials",
            "certificates.pem",
        )
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            well_known_via_symlink,
        )

        resolved_cert_path = os.path.join(
            str(real_run_dir),
            "secrets",
            "workload-spiffe-credentials",
            "certificates.pem",
        )
        assert _agent_identity_utils._is_in_well_known_dir(resolved_cert_path) is True

    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path",
        return_value=None,
    )
    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=False,
    )
    def test_get_agent_identity_certificate_path_empty_env(
        self, mock_is_ready, mock_get_config
    ):
        result = _agent_identity_utils.get_agent_identity_certificate_path()
        assert result is None
        mock_is_ready.assert_called_once_with(_mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH)

    @mock.patch("google.auth._agent_identity_utils.time.sleep")
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path",
        return_value=None,
    )
    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=True,
    )
    def test_get_agent_identity_certificate_path_gke_bundle_fallback(
        self, mock_is_ready, mock_get_config, mock_sleep
    ):
        result = _agent_identity_utils.get_agent_identity_certificate_path()
        assert result == _mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH
        mock_is_ready.assert_called_once_with(_mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH)
        mock_sleep.assert_not_called()

    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path",
        return_value=None,
    )
    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        side_effect=PermissionError("Access denied"),
    )
    def test_get_agent_identity_certificate_path_gke_bundle_permission_error(
        self, mock_is_ready, mock_get_config
    ):
        result = _agent_identity_utils.get_agent_identity_certificate_path()
        assert result is None
        mock_is_ready.assert_called_once_with(_mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH)

    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path",
        return_value="/home/user/.config/gcloud/certificate_config.json",
    )
    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=True,
    )
    def test_get_agent_identity_certificate_path_no_gke_fallback_when_implicit_config_exists(
        self, mock_is_ready, mock_get_config
    ):
        result = _agent_identity_utils.get_agent_identity_certificate_path()
        assert result is None
        mock_get_config.assert_called_once()
        mock_is_ready.assert_not_called()

    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=True,
    )
    def test_get_agent_identity_certificate_path_no_gke_fallback_when_context_aware_env_set(
        self, mock_is_ready, monkeypatch
    ):
        monkeypatch.setenv(
            environment_vars.CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH,
            "/missing/context_aware.json",
        )
        result = _agent_identity_utils.get_agent_identity_certificate_path()
        assert result is None
        mock_is_ready.assert_not_called()

    @mock.patch("google.auth._agent_identity_utils.os.path.commonpath")
    @mock.patch(
        "google.auth._agent_identity_utils._get_cert_path_with_optional_polling"
    )
    def test_get_agent_identity_certificate_path_value_error(
        self, mock_get_cert, mock_commonpath, monkeypatch
    ):
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, "/path/to/config.json"
        )
        mock_commonpath.side_effect = ValueError("Different drives")
        mock_get_cert.return_value = "cert_path"

        result = _agent_identity_utils.get_agent_identity_certificate_path()
        assert result == "cert_path"
        mock_get_cert.assert_called_once_with("/path/to/config.json", False)

    @mock.patch(
        "google.auth._agent_identity_utils._get_cert_path_with_optional_polling"
    )
    def test_get_agent_identity_certificate_path_prefix_false_positive(
        self, mock_get_cert, monkeypatch, tmpdir
    ):
        base_dir = str(tmpdir)
        well_known_dir = os.path.join(base_dir, "workload-spiffe-credentials")
        well_known_path = os.path.join(well_known_dir, "certificates.pem")

        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            well_known_path,
        )

        fake_dir = os.path.join(base_dir, "workload-spiffe-credentials-fake")
        fake_config_path = os.path.join(fake_dir, "config.json")

        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, fake_config_path
        )
        mock_get_cert.return_value = "cert_path"

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        assert result == "cert_path"
        mock_get_cert.assert_called_once_with(fake_config_path, False)

    @mock.patch("google.auth._agent_identity_utils.os.stat")
    def test_is_certificate_file_ready_permission_error(self, mock_stat):
        mock_stat.side_effect = PermissionError("Permission denied")
        with pytest.raises(PermissionError):
            _agent_identity_utils._is_certificate_file_ready("/path/to/cert")

    @mock.patch("google.auth._agent_identity_utils.os.stat")
    def test_is_certificate_file_ready_os_error(self, mock_stat):
        mock_stat.side_effect = OSError("Not found")
        # Should swallow the OSError and return False
        result = _agent_identity_utils._is_certificate_file_ready("/path/to/cert")
        assert result is False

    @mock.patch("google.auth._agent_identity_utils.os.stat")
    def test_is_certificate_file_ready_not_a_file(self, mock_stat):
        mock_stat.return_value = mock.MagicMock(st_mode=stat.S_IFDIR, st_size=4096)
        result = _agent_identity_utils._is_certificate_file_ready("/path/to/cert")
        assert result is False

    def test__is_agent_identity_certificate_invalid(self):
        cert = _agent_identity_utils.parse_certificate(NON_AGENT_IDENTITY_CERT_BYTES)
        assert not _agent_identity_utils._is_agent_identity_certificate(cert)

    @pytest.mark.parametrize(
        "spiffe_id",
        [
            "spiffe://agents.global.proj-12345.system.id.goog/workload",
            "spiffe://agents.global.org-12345.system.id.goog/workload",
            "spiffe://agents-nonprod.global.proj-12345.system.id.goog/workload",
            "spiffe://agents-nonprod.global.org-12345.system.id.goog/workload",
        ],
    )
    def test__is_agent_identity_certificate_valid_spiffe(self, spiffe_id):
        mock_cert = mock.MagicMock()
        mock_ext = mock.MagicMock()
        mock_san_value = mock.MagicMock()
        mock_cert.extensions.get_extension_for_oid.return_value = mock_ext
        mock_ext.value = mock_san_value
        mock_san_value.get_values_for_type.return_value = [spiffe_id]
        assert _agent_identity_utils._is_agent_identity_certificate(mock_cert)

    def test__is_agent_identity_certificate_non_matching_spiffe(self):
        mock_cert = mock.MagicMock()
        mock_ext = mock.MagicMock()
        mock_san_value = mock.MagicMock()
        mock_cert.extensions.get_extension_for_oid.return_value = mock_ext
        mock_ext.value = mock_san_value
        mock_san_value.get_values_for_type.return_value = [
            "spiffe://other.domain.com/workload"
        ]
        assert not _agent_identity_utils._is_agent_identity_certificate(mock_cert)

    def test__is_agent_identity_certificate_no_san(self):
        mock_cert = mock.MagicMock()
        mock_cert.extensions.get_extension_for_oid.side_effect = x509.ExtensionNotFound(
            "Test extension not found", None
        )
        assert not _agent_identity_utils._is_agent_identity_certificate(mock_cert)

    def test__is_agent_identity_certificate_not_spiffe_uri(self):
        mock_cert = mock.MagicMock()
        mock_ext = mock.MagicMock()
        mock_san_value = mock.MagicMock()
        mock_cert.extensions.get_extension_for_oid.return_value = mock_ext
        mock_ext.value = mock_san_value
        mock_san_value.get_values_for_type.return_value = ["https://example.com"]
        assert not _agent_identity_utils._is_agent_identity_certificate(mock_cert)

    def test_calculate_certificate_fingerprint(self):
        mock_cert = mock.MagicMock()
        mock_cert.public_bytes.return_value = b"der-bytes"

        # Expected: base64 (standard), unpadded, then URL-encoded
        base64_fingerprint = base64.b64encode(
            hashlib.sha256(b"der-bytes").digest()
        ).decode("utf-8")
        unpadded_base64_fingerprint = base64_fingerprint.rstrip("=")
        expected_fingerprint = urllib.parse.quote(unpadded_base64_fingerprint)

        fingerprint = _agent_identity_utils.calculate_certificate_fingerprint(mock_cert)

        assert fingerprint == expected_fingerprint

    @pytest.mark.parametrize(
        "primary,fallback,expected",
        [
            # Default (both unset) -> not opted out
            (None, None, False),
            # Explicit opt-in / non-false values on primary -> not opted out
            ("true", None, False),
            ("TRUE", None, False),
            ("1", None, False),
            ("invalid", None, False),
            ("", None, False),
            # Explicit opt-out via primary (including surrounding whitespace) -> opted out
            ("false", None, True),
            ("FALSE", None, True),
            (" false ", None, True),
            (" FALSE\n", None, True),
            # Primary overrides fallback
            ("false", "true", True),
            ("true", "false", False),
            # Empty or whitespace-only string on primary falls back to secondary
            ("", " false ", True),
            ("   ", " false ", True),
            # Fallback when primary is unset
            (None, "false", True),
            (None, "true", False),
        ],
    )
    def test_is_bound_token_opted_out(self, monkeypatch, primary, fallback, expected):
        if primary is not None:
            monkeypatch.setenv(
                environment_vars.GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN,
                primary,
            )
        if fallback is not None:
            monkeypatch.setenv(
                environment_vars.GOOGLE_API_PREVENT_AGENT_TOKEN_SHARING_FOR_GCP_SERVICES,
                fallback,
            )
        assert _agent_identity_utils._is_bound_token_opted_out() is expected

    @mock.patch("google.auth._agent_identity_utils._is_agent_identity_certificate")
    def test_should_request_bound_token(self, mock_is_agent, monkeypatch):
        # Agent cert, opted in
        mock_is_agent.return_value = True
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN,
            "true",
        )
        assert _agent_identity_utils.should_request_bound_token(mock.sentinel.cert)

        # Agent cert, opted out
        mock_is_agent.reset_mock()
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN,
            "false",
        )
        assert not _agent_identity_utils.should_request_bound_token(mock.sentinel.cert)
        mock_is_agent.assert_not_called()

        # Non-agent cert, opted in
        mock_is_agent.return_value = False
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN,
            "true",
        )
        assert not _agent_identity_utils.should_request_bound_token(mock.sentinel.cert)
        mock_is_agent.assert_called_once_with(mock.sentinel.cert)

    @mock.patch("google.auth._agent_identity_utils._is_agent_identity_certificate")
    def test_should_request_bound_token_explicit_use_client_cert_false(
        self, mock_is_agent, monkeypatch
    ):
        mock_is_agent.return_value = True
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE,
            "false",
        )
        assert not _agent_identity_utils.should_request_bound_token(mock.sentinel.cert)
        mock_is_agent.assert_not_called()

    @mock.patch("google.auth._agent_identity_utils._is_agent_identity_certificate")
    def test_should_request_bound_token_explicit_use_client_cert_invalid(
        self, mock_is_agent, monkeypatch
    ):
        mock_is_agent.return_value = True
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE,
            "foo",
        )
        assert not _agent_identity_utils.should_request_bound_token(mock.sentinel.cert)
        mock_is_agent.assert_not_called()

    @mock.patch("google.auth._agent_identity_utils._is_agent_identity_certificate")
    def test_should_request_bound_token_auto_enablement(self, mock_is_agent):
        mock_is_agent.return_value = True
        assert _agent_identity_utils.should_request_bound_token(mock.sentinel.cert)

    def test_get_agent_identity_certificate_path_success(self, tmpdir, monkeypatch):
        cert_path = tmpdir.join("cert.pem")
        cert_path.write("cert_content")
        config_path = tmpdir.join("config.json")
        config_path.write(
            json.dumps({"cert_configs": {"workload": {"cert_path": str(cert_path)}}})
        )
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        result = _agent_identity_utils.get_agent_identity_certificate_path()
        assert result == str(cert_path)

    @mock.patch("time.sleep")
    @mock.patch("google.auth._agent_identity_utils.os.path.exists")
    def test_get_agent_identity_certificate_path_retry(
        self, mock_exists, mock_sleep, tmpdir, monkeypatch
    ):
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(tmpdir.join("certificates.pem")),
        )
        config_path = tmpdir.join("config.json")
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        # File doesn't exist initially
        mock_exists.return_value = False

        with pytest.raises(exceptions.RefreshError):
            _agent_identity_utils.get_agent_identity_certificate_path()

        assert mock_sleep.call_count == len(_agent_identity_utils._POLLING_INTERVALS)

    @mock.patch("time.sleep")
    @mock.patch("google.auth._agent_identity_utils._is_certificate_file_ready")
    def test_get_agent_identity_certificate_path_retry_success(
        self, mock_is_ready, mock_sleep, tmpdir, monkeypatch
    ):
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(tmpdir.join("certificates.pem")),
        )
        cert_path_str = str(tmpdir.join("cert.pem"))
        config_path = tmpdir.join("config.json")
        config_path.write(
            json.dumps({"cert_configs": {"workload": {"cert_path": cert_path_str}}})
        )
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        # First attempt: file missing/not ready. Second attempt: succeeds.
        mock_is_ready.side_effect = [False, True]

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        assert result == cert_path_str
        assert mock_sleep.call_count == 1
        assert mock_is_ready.call_count == 2

    @mock.patch("time.sleep")
    @mock.patch("google.auth._agent_identity_utils._is_certificate_file_ready")
    def test_get_agent_identity_certificate_path_config_retry_success(
        self, mock_is_ready, mock_sleep, tmpdir, monkeypatch
    ):
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(tmpdir.join("certificates.pem")),
        )
        cert_path_str = str(tmpdir.join("cert.pem"))
        config_path = tmpdir.join("config.json")
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        mock_is_ready.return_value = True

        def write_config(*args, **kwargs):
            config_path.write(
                json.dumps({"cert_configs": {"workload": {"cert_path": cert_path_str}}})
            )

        # First attempt: config file missing. Sleep side effect creates it.
        mock_sleep.side_effect = write_config

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        assert result == cert_path_str
        assert mock_sleep.call_count == 1
        assert mock_is_ready.call_count == 1

    @mock.patch("time.sleep")
    @mock.patch("google.auth._agent_identity_utils.os.path.exists")
    def test_get_agent_identity_certificate_path_failure(
        self, mock_exists, mock_sleep, tmpdir, monkeypatch
    ):
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(tmpdir.join("certificates.pem")),
        )
        config_path = tmpdir.join("non_existent_config.json")
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        # Simulate workload env (well_known_dir exists) to avoid fail-fast
        mock_exists.return_value = False

        with pytest.raises(exceptions.RefreshError) as excinfo:
            _agent_identity_utils.get_agent_identity_certificate_path()

        assert "not found after multiple retries" in str(excinfo.value)
        assert environment_vars.GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN in str(
            excinfo.value
        )
        assert mock_sleep.call_count == len(_agent_identity_utils._POLLING_INTERVALS)

    @mock.patch("time.sleep")
    @mock.patch("google.auth._agent_identity_utils.os.path.exists")
    def test_get_agent_identity_certificate_path_fail_fast_config_missing(
        self, mock_exists, mock_sleep, tmpdir, monkeypatch
    ):
        # Simulate config path outside well-known dir where config file does not exist.
        well_known_path = tmpdir.mkdir("well_known").join("certificates.pem")
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(well_known_path),
        )

        config_path = tmpdir.mkdir("custom").join("custom_config.json")
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        mock_exists.return_value = False

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("time.sleep")
    def test_get_agent_identity_certificate_path_fail_fast_cert_missing(
        self, mock_sleep, tmpdir, monkeypatch
    ):
        # Simulate config path outside well-known dir where config is valid but cert is missing.
        well_known_path = tmpdir.mkdir("well_known_cert").join("certificates.pem")
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(well_known_path),
        )

        custom_dir = tmpdir.mkdir("custom_cert")
        config_path = custom_dir.join("custom_config.json")
        cert_path_str = str(custom_dir.join("cert.pem"))

        config_path.write(
            json.dumps({"cert_configs": {"workload": {"cert_path": cert_path_str}}})
        )
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("time.sleep")
    def test_get_agent_identity_certificate_path_well_known_config_external_missing_cert_no_poll(
        self, mock_sleep, tmpdir, monkeypatch
    ):
        well_known_dir = tmpdir.mkdir("workload-spiffe-credentials")
        external_dir = tmpdir.mkdir("external_certs")
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(well_known_dir.join("certificates.pem")),
        )
        config_path = well_known_dir.join("config.json")
        config_path.write(
            json.dumps(
                {
                    "cert_configs": {
                        "workload": {
                            "cert_path": str(external_dir.join("missing_cert.pem"))
                        }
                    }
                }
            )
        )
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("time.sleep")
    def test_get_agent_identity_certificate_path_cert_not_found(
        self, mock_sleep, tmpdir, monkeypatch
    ):
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(tmpdir.join("certificates.pem")),
        )
        cert_path_str = str(tmpdir.join("cert.pem"))
        config_path = tmpdir.join("config.json")
        config_path.write(
            json.dumps({"cert_configs": {"workload": {"cert_path": cert_path_str}}})
        )
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        with pytest.raises(exceptions.RefreshError):
            _agent_identity_utils.get_agent_identity_certificate_path()

        assert mock_sleep.call_count == len(_agent_identity_utils._POLLING_INTERVALS)

    @mock.patch("time.sleep")
    def test_get_agent_identity_certificate_path_non_workload_config(
        self, mock_sleep, tmpdir, monkeypatch
    ):
        config_path = tmpdir.join("config.json")
        config_path.write(
            json.dumps({"cert_configs": {"pkcs11": {"module": "some_module"}}})
        )
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        # Should return None immediately without polling
        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("time.sleep")
    def test_get_agent_identity_certificate_path_invalid_json(
        self, mock_sleep, tmpdir, monkeypatch
    ):
        config_path = tmpdir.join("config.json")
        config_path.write("{invalid_json: true}")  # Invalid JSON missing quotes
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        # Should return None immediately without polling/sleeping
        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("time.sleep")
    def test_get_agent_identity_certificate_path_non_dict_json(
        self, mock_sleep, tmpdir, monkeypatch
    ):
        config_path = tmpdir.join("config.json")
        config_path.write(json.dumps(["not", "a", "dict"]))  # Valid JSON list
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        # Should fail fast immediately and return None without polling
        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("time.sleep")
    def test_get_agent_identity_certificate_path_workload_config_missing_cert_path(
        self, mock_sleep, tmpdir, monkeypatch
    ):
        config_path = tmpdir.join("config.json")
        config_path.write(json.dumps({"cert_configs": {"workload": {}}}))
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        # Should return None immediately without polling
        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("time.sleep")
    @mock.patch("google.auth._agent_identity_utils.os.path.exists")
    def test_get_agent_identity_certificate_path_permission_error_config(
        self, mock_exists, mock_sleep, tmpdir, monkeypatch
    ):
        config_path = tmpdir.join("config.json")
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )
        # Mock os.path.exists so ECP workstation fail-fast is not triggered
        mock_exists.return_value = True

        # Mocking open to raise PermissionError
        mock_open = mock.mock_open()
        mock_open.side_effect = PermissionError("Permission denied")

        with mock.patch("builtins.open", mock_open):
            result = _agent_identity_utils.get_agent_identity_certificate_path()

        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("time.sleep")
    @mock.patch("google.auth._agent_identity_utils._is_certificate_file_ready")
    def test_get_agent_identity_certificate_path_permission_error_cert_file(
        self, mock_is_ready, mock_sleep, tmpdir, monkeypatch
    ):
        well_known_path = tmpdir.mkdir("well_known").join("certificates.pem")
        monkeypatch.setattr(
            "google.auth._agent_identity_utils._WELL_KNOWN_CERT_PATH",
            str(well_known_path),
        )

        config_path = tmpdir.mkdir("custom").join("custom_config.json")
        cert_path_str = str(tmpdir.join("cert.pem"))
        config_path.write(
            json.dumps({"cert_configs": {"workload": {"cert_path": cert_path_str}}})
        )
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, str(config_path)
        )

        # Mock _is_certificate_file_ready to raise PermissionError
        mock_is_ready.side_effect = PermissionError("Permission denied")

        result = _agent_identity_utils.get_agent_identity_certificate_path()

        assert result is None
        mock_sleep.assert_not_called()

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_success(
        self, mock_get_path, tmpdir
    ):
        cert_file = tmpdir.join("cert.pem")
        cert_file.write_binary(NON_AGENT_IDENTITY_CERT_BYTES)
        mock_get_path.return_value = str(cert_file)

        (
            cert,
            cert_bytes,
        ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()

        assert isinstance(cert, x509.Certificate)
        assert cert_bytes == NON_AGENT_IDENTITY_CERT_BYTES

    @pytest.mark.parametrize("key_index", [0, 1, 2])
    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_combined_bundle(
        self, mock_get_path, tmpdir, key_index
    ):
        non_utf8_bag_attrs = b"Bag Attributes\n    friendlyName: \xff\xfe\n"
        private_key_pem = (
            b"-----BEGIN PRIVATE KEY-----\n"
            b"MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC3\n"
            b"-----END PRIVATE KEY-----\n"
        )
        blocks = [
            AGENT_IDENTITY_CERT_BYTES.rstrip(b"\n") + b"   \n",
            NON_AGENT_IDENTITY_CERT_BYTES,
        ]
        blocks.insert(key_index, private_key_pem)
        cert_file = tmpdir.join("credentialbundle.pem")
        cert_file.write_binary(non_utf8_bag_attrs + b"".join(blocks))
        mock_get_path.return_value = str(cert_file)

        (
            cert,
            cert_bytes,
        ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()

        expected_certs = AGENT_IDENTITY_CERT_BYTES + NON_AGENT_IDENTITY_CERT_BYTES
        assert isinstance(cert, x509.Certificate)
        assert _agent_identity_utils._is_agent_identity_certificate(cert)
        assert cert_bytes == expected_certs
        assert cert_bytes.decode("utf-8") == expected_certs.decode("utf-8")

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_no_cert_blocks(
        self, mock_get_path, tmpdir
    ):
        cert_file = tmpdir.join("empty_or_key_only.pem")
        cert_file.write_binary(
            b"-----BEGIN PRIVATE KEY-----\nMIIB\n-----END PRIVATE KEY-----\n"
        )
        mock_get_path.return_value = str(cert_file)

        with pytest.warns(UserWarning, match="No PEM certificate blocks found"):
            (
                cert,
                cert_bytes,
            ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()

        assert cert is None
        assert cert_bytes is None

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_os_error(
        self, mock_get_path, tmpdir
    ):
        missing_cert_file = tmpdir.join("deleted_during_rotation.pem")
        mock_get_path.return_value = str(missing_cert_file)

        with pytest.warns(
            UserWarning, match="Failed to read agent identity certificate file"
        ):
            (
                cert,
                cert_bytes,
            ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()

        assert cert is None
        assert cert_bytes is None

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_corrupt_cert_value_error(
        self, mock_get_path, tmpdir
    ):
        cert_file = tmpdir.join("corrupt_cert.pem")
        cert_file.write_binary(
            b"-----BEGIN CERTIFICATE-----\nnot_valid_base64_or_der\n-----END CERTIFICATE-----\n"
        )
        mock_get_path.return_value = str(cert_file)

        with pytest.warns(
            UserWarning, match="Failed to parse agent identity certificate"
        ):
            (
                cert,
                cert_bytes,
            ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()

        assert cert is None
        assert cert_bytes is None

    @pytest.mark.parametrize(
        "corrupt_intermediate",
        [
            b"-----BEGIN CERTIFICATE-----\n"
            + base64.b64encode(b"invalid_asn1_der_intermediate")
            + b"\n-----END CERTIFICATE-----\n",
            b"-----BEGIN CERTIFICATE-----\ntruncated_without_end_marker\n",
        ],
    )
    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_corrupt_intermediate_warns(
        self, mock_get_path, corrupt_intermediate, tmpdir
    ):
        cert_file = tmpdir.join("chain_with_corrupt_intermediate.pem")
        cert_file.write_binary(AGENT_IDENTITY_CERT_BYTES + corrupt_intermediate)
        mock_get_path.return_value = str(cert_file)

        with pytest.warns(
            UserWarning, match="Failed to parse agent identity certificate"
        ):
            (
                cert,
                cert_bytes,
            ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()

        assert cert is None
        assert cert_bytes is None

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_opted_out(
        self, mock_get_path, monkeypatch
    ):
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN,
            "false",
        )
        (
            cert,
            cert_bytes,
        ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()
        assert cert is None
        assert cert_bytes is None
        mock_get_path.assert_not_called()

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_no_path(self, mock_get_path):
        mock_get_path.return_value = None
        (
            cert,
            cert_bytes,
        ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()
        assert cert is None
        assert cert_bytes is None
        mock_get_path.assert_called_once()

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_use_client_cert_false(
        self, mock_get_path, monkeypatch
    ):
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE,
            "false",
        )
        (
            cert,
            cert_bytes,
        ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()
        assert cert is None
        assert cert_bytes is None
        mock_get_path.assert_not_called()

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_use_client_cert_invalid(
        self, mock_get_path, monkeypatch
    ):
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE,
            "foo",
        )
        (
            cert,
            cert_bytes,
        ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()
        assert cert is None
        assert cert_bytes is None
        mock_get_path.assert_not_called()

    def test_get_cached_cert_fingerprint_no_cert(self):
        with pytest.raises(ValueError, match="mTLS connection is not configured."):
            _agent_identity_utils.get_cached_cert_fingerprint(None)

    def test_get_cached_cert_fingerprint_with_cert(self):
        fingerprint = _agent_identity_utils.get_cached_cert_fingerprint(
            NON_AGENT_IDENTITY_CERT_BYTES
        )
        assert isinstance(fingerprint, str)


class TestAgentIdentityUtilsNoCryptography:
    @pytest.fixture(autouse=True)
    def mock_cryptography_import(self):
        with mock.patch.dict(
            "sys.modules",
            {
                "cryptography": None,
                "cryptography.hazmat": None,
                "cryptography.hazmat.primitives": None,
                "cryptography.hazmat.primitives.serialization": None,
            },
        ):
            yield

    def test_parse_certificate_raises_import_error(self):
        with pytest.raises(ImportError, match="The cryptography library is required"):
            _agent_identity_utils.parse_certificate(b"cert_bytes")

    def test_is_agent_identity_certificate_raises_import_error(self):
        with pytest.raises(ImportError, match="The cryptography library is required"):
            _agent_identity_utils._is_agent_identity_certificate(mock.sentinel.cert)

    def test_calculate_certificate_fingerprint_raises_import_error(self):
        with pytest.raises(ImportError, match="The cryptography library is required"):
            _agent_identity_utils.calculate_certificate_fingerprint(mock.sentinel.cert)

    @mock.patch("google.auth._agent_identity_utils.get_agent_identity_certificate_path")
    def test_get_agent_identity_certificate_and_bytes_warns_without_cryptography(
        self, mock_get_path, tmpdir
    ):
        cert_file = tmpdir.join("cert.pem")
        cert_file.write_binary(AGENT_IDENTITY_CERT_BYTES)
        mock_get_path.return_value = str(cert_file)

        with pytest.warns(UserWarning, match="The cryptography library is required"):
            (
                cert,
                cert_bytes,
            ) = _agent_identity_utils.get_agent_identity_certificate_and_bytes()

        assert cert is None
        assert cert_bytes is None
