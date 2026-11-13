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

import os
import re
import sys
import tempfile
from unittest import mock

import pytest  # type: ignore
import urllib3.util
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

from google.auth import environment_vars, exceptions
from google.auth.transport import _mtls_helper

if not hasattr(os, "MFD_CLOEXEC"):
    setattr(os, "MFD_CLOEXEC", 1)

CERT_MOCK_VAL = b"cert"
KEY_MOCK_VAL = b"key"
CONTEXT_AWARE_METADATA = {"cert_provider_command": ["some command"]}
ENCRYPTED_EC_PRIVATE_KEY = b"""-----BEGIN ENCRYPTED PRIVATE KEY-----
MIH0MF8GCSqGSIb3DQEFDTBSMDEGCSqGSIb3DQEFDDAkBBClWcQyUELNC9Hjr+Sp
WK85AgIIADAMBggqhkiG9w0CCQUAMB0GCWCGSAFlAwQBKgQQ6uJeoqE7P9HtxAgS
n6rBFgSBkMRDYXLucNp7ew7LbQmkZCmjnRhgyw6b0dD3eK8f3jisj8UiR8aj9a2S
1FZiNHKLmI7hkZHH+d2DPWYhe/tf5SS4iLzpZogBehMv4UDNnNaj0dvQZgpnpciK
1H+0u/i+crc1WAGlemLAi7dktCCBTzeX19cRMGHie68rx1C82LHLZmefr7AEIVxp
uUoJ+sLhBw==
-----END ENCRYPTED PRIVATE KEY-----"""

EC_PUBLIC_KEY = b"""-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEwdsHzL05VUmqYJat2yGdbSHQAg49
Wc+fhwLH3b+SCC/2/TqPNDy9yMdMxMtEfZfKal2EaeE2erJrtu7WNfjD0Q==
-----END PUBLIC KEY-----"""

PASSPHRASE = b"""-----BEGIN PASSPHRASE-----
password
-----END PASSPHRASE-----"""
PASSPHRASE_VALUE = b"password"


def check_cert_and_key(content, expected_cert, expected_key):
    success = True

    cert_match = re.findall(_mtls_helper._CERT_REGEX, content)
    success = success and len(cert_match) >= 1 and b"".join(cert_match) == expected_cert

    key_match = re.findall(_mtls_helper._KEY_REGEX, content)
    success = success and len(key_match) == 1 and key_match[0] == expected_key

    return success


class TestCertAndKeyRegex(object):
    def test_cert_and_key(self):
        # Test single cert and single key
        assert check_cert_and_key(
            pytest.public_cert_bytes + pytest.private_key_bytes,
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )
        assert check_cert_and_key(
            pytest.private_key_bytes + pytest.public_cert_bytes,
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

        # Test cert chain and single key
        assert check_cert_and_key(
            pytest.public_cert_bytes
            + pytest.public_cert_bytes
            + pytest.private_key_bytes,
            pytest.public_cert_bytes + pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )
        assert check_cert_and_key(
            pytest.private_key_bytes
            + pytest.public_cert_bytes
            + pytest.public_cert_bytes,
            pytest.public_cert_bytes + pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )
        # Test interleaved key between certificates in a combined bundle
        assert check_cert_and_key(
            pytest.public_cert_bytes
            + pytest.private_key_bytes
            + pytest.public_cert_bytes,
            pytest.public_cert_bytes + pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

    def test_key(self):
        # Create some fake keys for regex check.
        KEY = b"""-----BEGIN PRIVATE KEY-----
        MIIBCgKCAQEA4ej0p7bQ7L/r4rVGUz9RN4VQWoej1Bg1mYWIDYslvKrk1gpj7wZg
        /fy3ZpsL7WqgsZS7Q+0VRK8gKfqkxg5OYQIDAQAB
        -----END PRIVATE KEY-----"""
        RSA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
        MIIBCgKCAQEA4ej0p7bQ7L/r4rVGUz9RN4VQWoej1Bg1mYWIDYslvKrk1gpj7wZg
        /fy3ZpsL7WqgsZS7Q+0VRK8gKfqkxg5OYQIDAQAB
        -----END RSA PRIVATE KEY-----"""
        EC_KEY = b"""-----BEGIN EC PRIVATE KEY-----
        MIIBCgKCAQEA4ej0p7bQ7L/r4rVGUz9RN4VQWoej1Bg1mYWIDYslvKrk1gpj7wZg
        /fy3ZpsL7WqgsZS7Q+0VRK8gKfqkxg5OYQIDAQAB
        -----END EC PRIVATE KEY-----"""

        assert check_cert_and_key(
            pytest.public_cert_bytes + KEY, pytest.public_cert_bytes, KEY
        )
        assert check_cert_and_key(
            pytest.public_cert_bytes + RSA_KEY, pytest.public_cert_bytes, RSA_KEY
        )
        assert check_cert_and_key(
            pytest.public_cert_bytes + EC_KEY, pytest.public_cert_bytes, EC_KEY
        )


class TestCheckConfigPath(object):
    def test_success(self):
        metadata_path = os.path.join(pytest.data_dir, "context_aware_metadata.json")
        returned_path = _mtls_helper._check_config_path(metadata_path)
        assert returned_path is not None

    def test_failure(self):
        metadata_path = os.path.join(pytest.data_dir, "not_exists.json")
        returned_path = _mtls_helper._check_config_path(metadata_path)
        assert returned_path is None


class TestReadMetadataFile(object):
    def test_success(self):
        metadata_path = os.path.join(pytest.data_dir, "context_aware_metadata.json")
        metadata = _mtls_helper._load_json_file(metadata_path)

        assert "cert_provider_command" in metadata

    def test_file_not_json(self):
        # read a file which is not json format.
        metadata_path = os.path.join(pytest.data_dir, "privatekey.pem")
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._load_json_file(metadata_path)


class TestRunCertProviderCommand(object):
    def create_mock_process(self, output, error):
        # There are two steps to execute a script with subprocess.Popen.
        # (1) process = subprocess.Popen([comannds])
        # (2) stdout, stderr = process.communicate()
        # This function creates a mock process which can be returned by a mock
        # subprocess.Popen. The mock process returns the given output and error
        # when mock_process.communicate() is called.
        mock_process = mock.Mock()
        attrs = {"communicate.return_value": (output, error), "returncode": 0}
        mock_process.configure_mock(**attrs)
        return mock_process

    @mock.patch("subprocess.Popen", autospec=True)
    def test_success(self, mock_popen):
        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes + pytest.private_key_bytes, b""
        )
        cert, key, passphrase = _mtls_helper._run_cert_provider_command(["command"])
        assert cert == pytest.public_cert_bytes
        assert key == pytest.private_key_bytes
        assert passphrase is None

        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes + ENCRYPTED_EC_PRIVATE_KEY + PASSPHRASE, b""
        )
        cert, key, passphrase = _mtls_helper._run_cert_provider_command(
            ["command"], expect_encrypted_key=True
        )
        assert cert == pytest.public_cert_bytes
        assert key == ENCRYPTED_EC_PRIVATE_KEY
        assert passphrase == PASSPHRASE_VALUE

    @mock.patch("subprocess.Popen", autospec=True)
    def test_success_with_cert_chain(self, mock_popen):
        PUBLIC_CERT_CHAIN_BYTES = pytest.public_cert_bytes + pytest.public_cert_bytes
        mock_popen.return_value = self.create_mock_process(
            PUBLIC_CERT_CHAIN_BYTES + pytest.private_key_bytes, b""
        )
        cert, key, passphrase = _mtls_helper._run_cert_provider_command(["command"])
        assert cert == PUBLIC_CERT_CHAIN_BYTES
        assert key == pytest.private_key_bytes
        assert passphrase is None

        mock_popen.return_value = self.create_mock_process(
            PUBLIC_CERT_CHAIN_BYTES + ENCRYPTED_EC_PRIVATE_KEY + PASSPHRASE, b""
        )
        cert, key, passphrase = _mtls_helper._run_cert_provider_command(
            ["command"], expect_encrypted_key=True
        )
        assert cert == PUBLIC_CERT_CHAIN_BYTES
        assert key == ENCRYPTED_EC_PRIVATE_KEY
        assert passphrase == PASSPHRASE_VALUE

    @pytest.mark.parametrize(
        "trailing_bytes",
        [
            b"-----BEGIN CERTIFICATE-----\nMIIB\n",
            b"MIIB\n-----END CERTIFICATE-----\n",
        ],
    )
    @mock.patch("subprocess.Popen", autospec=True)
    def test_truncated_cert_chain_raises_error(self, mock_popen, trailing_bytes):
        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes + trailing_bytes + pytest.private_key_bytes, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(["command"])

    @mock.patch("subprocess.Popen", autospec=True)
    def test_missing_cert(self, mock_popen):
        mock_popen.return_value = self.create_mock_process(
            pytest.private_key_bytes, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(["command"])

        mock_popen.return_value = self.create_mock_process(
            ENCRYPTED_EC_PRIVATE_KEY + PASSPHRASE, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(
                ["command"], expect_encrypted_key=True
            )

    @mock.patch("subprocess.Popen", autospec=True)
    def test_missing_key(self, mock_popen):
        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(["command"])

        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes + PASSPHRASE, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(
                ["command"], expect_encrypted_key=True
            )

    @mock.patch("subprocess.Popen", autospec=True)
    def test_missing_passphrase(self, mock_popen):
        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes + ENCRYPTED_EC_PRIVATE_KEY, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(
                ["command"], expect_encrypted_key=True
            )

    @mock.patch("subprocess.Popen", autospec=True)
    def test_passphrase_not_expected(self, mock_popen):
        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes + pytest.private_key_bytes + PASSPHRASE, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(["command"])

    @mock.patch("subprocess.Popen", autospec=True)
    def test_encrypted_key_expected(self, mock_popen):
        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes + pytest.private_key_bytes + PASSPHRASE, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(
                ["command"], expect_encrypted_key=True
            )

    @mock.patch("subprocess.Popen", autospec=True)
    def test_unencrypted_key_expected(self, mock_popen):
        mock_popen.return_value = self.create_mock_process(
            pytest.public_cert_bytes + ENCRYPTED_EC_PRIVATE_KEY, b""
        )
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(["command"])

    @mock.patch("subprocess.Popen", autospec=True)
    def test_cert_provider_returns_error(self, mock_popen):
        mock_popen.return_value = self.create_mock_process(b"", b"some error")
        mock_popen.return_value.returncode = 1
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(["command"])

    @mock.patch("subprocess.Popen", autospec=True)
    def test_popen_raise_exception(self, mock_popen):
        mock_popen.side_effect = OSError()
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._run_cert_provider_command(["command"])


class TestGetClientSslCredentials(object):
    @mock.patch(
        "google.auth.transport._mtls_helper._get_workload_cert_and_key", autospec=True
    )
    @mock.patch(
        "google.auth.transport._mtls_helper._run_cert_provider_command", autospec=True
    )
    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
    def test_success_with_context_aware_metadata(
        self,
        mock_check_config_path,
        mock_load_json_file,
        mock_run_cert_provider_command,
        mock_get_workload_cert_and_key,
    ):
        mock_check_config_path.return_value = "/path/to/config"
        mock_load_json_file.return_value = {"cert_provider_command": ["command"]}
        mock_run_cert_provider_command.return_value = (b"cert", b"key", None)
        mock_get_workload_cert_and_key.return_value = (None, None)
        has_cert, cert, key, passphrase = _mtls_helper.get_client_ssl_credentials()
        assert has_cert
        assert cert == b"cert"
        assert key == b"key"
        assert passphrase is None

    @mock.patch(
        "google.auth.transport._mtls_helper._read_cert_and_key_files", autospec=True
    )
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", autospec=True
    )
    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
    @mock.patch("os.path.exists", autospec=True)
    def test_success_with_certificate_config(
        self,
        mock_path_exists,
        mock_check_config_path,
        mock_load_json_file,
        mock_get_cert_config_path,
        mock_read_cert_and_key_files,
    ):
        mock_path_exists.return_value = True
        cert_config_path = "/path/to/config"
        mock_check_config_path.return_value = cert_config_path
        mock_load_json_file.return_value = {
            "cert_configs": {
                "workload": {"cert_path": "cert/path", "key_path": "key/path"}
            }
        }
        mock_get_cert_config_path.return_value = cert_config_path
        mock_read_cert_and_key_files.return_value = (
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

        has_cert, cert, key, passphrase = _mtls_helper.get_client_ssl_credentials()
        assert has_cert
        assert cert == pytest.public_cert_bytes
        assert key == pytest.private_key_bytes
        assert passphrase is None

    @mock.patch(
        "google.auth.transport._mtls_helper._get_workload_cert_and_key", autospec=True
    )
    @mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
    def test_success_without_metadata(
        self, mock_check_config_path, mock_get_workload_cert_and_key
    ):
        mock_check_config_path.return_value = False
        mock_get_workload_cert_and_key.return_value = (None, None)
        has_cert, cert, key, passphrase = _mtls_helper.get_client_ssl_credentials()
        assert not has_cert
        assert cert is None
        assert key is None
        assert passphrase is None

    @mock.patch(
        "google.auth.transport._mtls_helper._get_workload_cert_and_key", autospec=True
    )
    @mock.patch(
        "google.auth.transport._mtls_helper._run_cert_provider_command", autospec=True
    )
    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
    def test_success_with_encrypted_key(
        self,
        mock_check_config_path,
        mock_load_json_file,
        mock_run_cert_provider_command,
        mock_get_workload_cert_and_key,
    ):
        mock_check_config_path.return_value = "/path/to/config"
        mock_load_json_file.return_value = {"cert_provider_command": ["command"]}
        mock_run_cert_provider_command.return_value = (b"cert", b"key", b"passphrase")
        mock_get_workload_cert_and_key.return_value = (None, None)
        has_cert, cert, key, passphrase = _mtls_helper.get_client_ssl_credentials(
            generate_encrypted_key=True
        )
        assert has_cert
        assert cert == b"cert"
        assert key == b"key"
        assert passphrase == b"passphrase"
        mock_run_cert_provider_command.assert_called_once_with(
            ["command", "--with_passphrase"], expect_encrypted_key=True
        )

    @mock.patch(
        "google.auth.transport._mtls_helper._get_workload_cert_and_key", autospec=True
    )
    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
    def test_missing_cert_command(
        self,
        mock_check_config_path,
        mock_load_json_file,
        mock_get_workload_cert_and_key,
    ):
        mock_check_config_path.return_value = "/path/to/config"
        mock_load_json_file.return_value = {}
        mock_get_workload_cert_and_key.return_value = (None, None)
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper.get_client_ssl_credentials()

    @mock.patch(
        "google.auth.transport._mtls_helper._run_cert_provider_command", autospec=True
    )
    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper._get_workload_cert_and_key", autospec=True
    )
    def test_customize_context_aware_metadata_path(
        self,
        mock_get_workload_cert_and_key,
        mock_check_config_path,
        mock_load_json_file,
        mock_run_cert_provider_command,
    ):
        mock_get_workload_cert_and_key.return_value = (None, None)
        context_aware_metadata_path = "/path/to/metata/data"
        mock_check_config_path.return_value = context_aware_metadata_path
        mock_load_json_file.return_value = {"cert_provider_command": ["command"]}
        mock_run_cert_provider_command.return_value = (b"cert", b"key", None)

        has_cert, cert, key, passphrase = _mtls_helper.get_client_ssl_credentials(
            context_aware_metadata_path=context_aware_metadata_path
        )

        assert has_cert
        assert cert == b"cert"
        assert key == b"key"
        assert passphrase is None
        mock_check_config_path.assert_called_with(context_aware_metadata_path)
        mock_load_json_file.assert_called_with(context_aware_metadata_path)


class TestGetWorkloadCertAndKey(object):
    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", autospec=True
    )
    @mock.patch(
        "google.auth.transport._mtls_helper._read_cert_and_key_files", autospec=True
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_success(
        self,
        mock_path_exists,
        mock_read_cert_and_key_files,
        mock_get_cert_config_path,
        mock_load_json_file,
    ):
        mock_path_exists.return_value = True
        cert_config_path = "/path/to/cert"
        mock_get_cert_config_path.return_value = "/path/to/cert"
        mock_load_json_file.return_value = {
            "cert_configs": {
                "workload": {"cert_path": "cert/path", "key_path": "key/path"}
            }
        }
        mock_read_cert_and_key_files.return_value = (
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

        actual_cert, actual_key = _mtls_helper._get_workload_cert_and_key(
            cert_config_path
        )
        assert actual_cert == pytest.public_cert_bytes
        assert actual_key == pytest.private_key_bytes

    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", autospec=True
    )
    def test_file_not_found_returns_none(self, mock_get_cert_config_path):
        mock_get_cert_config_path.return_value = None

        actual_cert, actual_key = _mtls_helper._get_workload_cert_and_key()
        assert actual_cert is None
        assert actual_key is None

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", autospec=True
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_no_cert_configs(
        self, mock_path_exists, mock_get_cert_config_path, mock_load_json_file
    ):
        mock_path_exists.return_value = True
        mock_get_cert_config_path.return_value = "/path/to/cert"
        mock_load_json_file.return_value = {}

        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._get_workload_cert_and_key("")

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper.path.exists", autospec=True)
    def test_non_dict_cert_configs_raises_error(
        self, mock_path_exists, mock_load_json_file
    ):
        mock_path_exists.return_value = True

        for val in [None, [], "not_a_dict"]:
            mock_load_json_file.return_value = {"cert_configs": val}
            with pytest.raises(exceptions.ClientCertError):
                _mtls_helper._get_workload_cert_and_key(None)

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper.path.exists", autospec=True)
    def test_malformed_json_returns_error(self, mock_path_exists, mock_load_json_file):
        mock_path_exists.return_value = True

        for val in [None, [], "invalid_string"]:
            mock_load_json_file.return_value = val
            with pytest.raises(exceptions.ClientCertError):
                _mtls_helper._get_workload_cert_and_key(None)

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper.path.exists", autospec=True)
    def test_non_dict_workload_raises_error(
        self, mock_path_exists, mock_load_json_file
    ):
        mock_path_exists.return_value = True

        for invalid_workload in [None, 123, "not_a_dict"]:
            mock_load_json_file.return_value = {
                "cert_configs": {"workload": invalid_workload}
            }

            with pytest.raises(exceptions.ClientCertError):
                _mtls_helper._get_workload_cert_and_key(None)

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", autospec=True
    )
    def test_no_workload(self, mock_get_cert_config_path, mock_load_json_file):
        mock_get_cert_config_path.return_value = "/path/to/cert"
        mock_load_json_file.return_value = {"cert_configs": {}}

        actual_cert, actual_key = _mtls_helper._get_workload_cert_and_key("")
        assert actual_cert is None
        assert actual_key is None

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)  # noqa: E501
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path",
        autospec=True,
    )  # noqa: E501
    @mock.patch(
        "google.auth.transport._mtls_helper._read_cert_and_key_files",
        autospec=True,
    )  # noqa: E501
    @mock.patch("google.auth.transport._mtls_helper.path.exists", autospec=True)  # noqa: E501
    def test_no_workload_fallback_to_home(
        self,
        mock_path_exists,
        mock_read_cert_and_key_files,
        mock_get_cert_config_path,
        mock_load_json_file,
    ):
        ecp_path = "/etc/gcloud/certificate_config.json"
        home_path = os.path.join(
            _mtls_helper._cloud_sdk.get_config_path(),
            "certificate_config.json",
        )
        mock_get_cert_config_path.return_value = ecp_path

        def exists_side_effect(path):
            if path == home_path:
                return True
            return False

        mock_path_exists.side_effect = exists_side_effect

        def load_json_side_effect(path):
            if path == ecp_path:
                return {"cert_configs": {"pkcs11": {}}}
            elif path == home_path:
                return {
                    "cert_configs": {
                        "workload": {
                            "cert_path": "cert/path",
                            "key_path": "key/path",
                        }
                    }
                }
            return {}

        mock_load_json_file.side_effect = load_json_side_effect
        mock_read_cert_and_key_files.return_value = (
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

        actual_cert, actual_key = _mtls_helper._get_workload_cert_and_key(None)
        assert actual_cert == pytest.public_cert_bytes
        assert actual_key == pytest.private_key_bytes

        mock_get_cert_config_path.assert_called_once_with(None, True)
        mock_load_json_file.assert_has_calls(
            [mock.call(ecp_path), mock.call(home_path)]
        )
        mock_read_cert_and_key_files.assert_called_once_with("cert/path", "key/path")  # noqa: E501

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)  # noqa: E501
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path",
        autospec=True,
    )  # noqa: E501
    @mock.patch(
        "google.auth.transport._mtls_helper._read_cert_and_key_files",
        autospec=True,
    )  # noqa: E501
    @mock.patch("google.auth.transport._mtls_helper.path.exists", autospec=True)  # noqa: E501
    def test_no_workload_fallback_to_home_error(
        self,
        mock_path_exists,
        mock_read_cert_and_key_files,
        mock_get_cert_config_path,
        mock_load_json_file,
    ):
        ecp_path = "/etc/gcloud/certificate_config.json"
        home_path = os.path.join(
            _mtls_helper._cloud_sdk.get_config_path(),
            "certificate_config.json",
        )
        mock_get_cert_config_path.return_value = ecp_path

        def exists_side_effect(path):
            if path == home_path:
                return True
            return False

        mock_path_exists.side_effect = exists_side_effect

        def load_json_side_effect(path):
            if path == ecp_path:
                return {"cert_configs": {"pkcs11": {}}}
            elif path == home_path:
                raise exceptions.ClientCertError("mocked unreadable file")
            return {}

        mock_load_json_file.side_effect = load_json_side_effect

        actual_cert, actual_key = _mtls_helper._get_workload_cert_and_key(None)
        assert actual_cert is None
        assert actual_key is None

        mock_get_cert_config_path.assert_called_once_with(None, True)
        mock_load_json_file.assert_has_calls(
            [mock.call(ecp_path), mock.call(home_path)]
        )
        mock_read_cert_and_key_files.assert_not_called()

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)  # noqa: E501
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path",
        autospec=True,
    )
    @mock.patch("google.auth.transport._mtls_helper.path.exists", autospec=True)  # noqa: E501
    @mock.patch("os.path.normpath", autospec=True)
    def test_no_workload_fallback_avoided_same_path_normalization(
        self,
        mock_normpath,
        mock_path_exists,
        mock_get_cert_config_path,
        mock_load_json_file,
    ):
        ecp_path = "C:/Users/User/.config/gcloud/certificate_config.json"
        home_path = "C:\\Users\\User\\.config\\gcloud/certificate_config.json"
        mock_get_cert_config_path.return_value = ecp_path

        mock_path_exists.return_value = True

        # When resolving, the first file has no workload.
        mock_load_json_file.return_value = {"cert_configs": {"pkcs11": {}}}

        win_path = "C:\\Users\\User\\.config\\gcloud\\certificate_config.json"

        # Mock normpath to return the same string for both paths,
        # simulating Windows path normalization.
        def normpath_side_effect(path):
            if path in [ecp_path, home_path]:
                return win_path
            return path

        mock_normpath.side_effect = normpath_side_effect

        # Mock get_config_path to construct a path with backslashes
        with mock.patch(
            "google.auth._cloud_sdk.get_config_path",
            return_value="C:\\Users\\User\\.config\\gcloud",
        ):
            actual_cert, actual_key = _mtls_helper._get_workload_cert_and_key(None)  # noqa: E501

        assert actual_cert is None
        assert actual_key is None

        # Check that it resolved ECP path but never attempted to load
        # home_path (because it normalized to the same file).
        mock_get_cert_config_path.assert_called_once_with(None, True)
        mock_load_json_file.assert_called_once_with(ecp_path)

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", autospec=True
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_no_cert_file(
        self, mock_path_exists, mock_get_cert_config_path, mock_load_json_file
    ):
        mock_path_exists.return_value = True
        mock_get_cert_config_path.return_value = "/path/to/cert"
        mock_load_json_file.return_value = {
            "cert_configs": {"workload": {"key_path": "path/to/key"}}
        }

        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._get_workload_cert_and_key("")

    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", autospec=True
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_no_key_file(
        self, mock_path_exists, mock_get_cert_config_path, mock_load_json_file
    ):
        mock_path_exists.return_value = True
        mock_get_cert_config_path.return_value = "/path/to/cert"
        mock_load_json_file.return_value = {
            "cert_configs": {"workload": {"cert_path": "path/to/key"}}
        }

        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._get_workload_cert_and_key("")

    @pytest.mark.parametrize(
        "workload",
        [
            {"cert_path": None, "key_path": "path/to/key"},
            {"cert_path": "path/to/cert", "key_path": None},
            {"cert_path": None, "key_path": None},
            {"cert_path": "", "key_path": "path/to/key"},
            {"cert_path": "path/to/cert", "key_path": ""},
            {"cert_path": 123, "key_path": "path/to/key"},
            {"cert_path": "path/to/cert", "key_path": 123},
        ],
    )
    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", autospec=True
    )
    def test_invalid_cert_or_key_path_value(
        self,
        mock_get_cert_config_path,
        mock_load_json_file,
        workload,
    ):
        mock_get_cert_config_path.return_value = "/path/to/cert"
        mock_load_json_file.return_value = {"cert_configs": {"workload": workload}}

        with pytest.raises(
            exceptions.ClientCertError,
            match='Workload certificate configuration is missing "cert_path" or "key_path"',
        ):
            _mtls_helper._get_workload_cert_and_key("")


class TestReadCertAndKeyFile(object):
    def test_success(self):
        cert_path = os.path.join(pytest.data_dir, "public_cert.pem")
        key_path = os.path.join(pytest.data_dir, "privatekey.pem")

        actual_cert, actual_key = _mtls_helper._read_cert_and_key_files(
            cert_path, key_path
        )
        assert actual_cert == pytest.public_cert_bytes
        assert actual_key == pytest.private_key_bytes

    def test_no_cert_file(self):
        cert_path = "fake/file/path"
        key_path = os.path.join(pytest.data_dir, "privatekey.pem")
        with pytest.raises(FileNotFoundError):
            _mtls_helper._read_cert_and_key_files(cert_path, key_path)

    def test_no_key_file(self):
        cert_path = os.path.join(pytest.data_dir, "public_cert.pem")
        key_path = "fake/file/path"
        with pytest.raises(FileNotFoundError):
            _mtls_helper._read_cert_and_key_files(cert_path, key_path)

    def test_invalid_cert_file(self):
        cert_path = os.path.join(pytest.data_dir, "service_account.json")
        key_path = os.path.join(pytest.data_dir, "privatekey.pem")
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._read_cert_and_key_files(cert_path, key_path)

    def test_invalid_key_file(self):
        cert_path = os.path.join(pytest.data_dir, "public_cert.pem")
        key_path = os.path.join(pytest.data_dir, "public_cert.pem")
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._read_cert_and_key_files(cert_path, key_path)

    def test_combined_bundle_with_interleaved_key(self, tmp_path):
        bundle_file = tmp_path / "credentialbundle.pem"
        bundle_file.write_bytes(
            pytest.public_cert_bytes.rstrip(b"\n")
            + pytest.private_key_bytes
            + pytest.public_cert_bytes
        )
        actual_cert, actual_key = _mtls_helper._read_cert_and_key_files(
            str(bundle_file), str(bundle_file)
        )
        assert actual_cert == pytest.public_cert_bytes + pytest.public_cert_bytes
        assert actual_key == pytest.private_key_bytes

    def test_multiple_keys_raises_error(self, tmp_path):
        cert_path = os.path.join(pytest.data_dir, "public_cert.pem")
        key_file = tmp_path / "two_keys.pem"
        key_file.write_bytes(pytest.private_key_bytes + pytest.private_key_bytes)
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._read_cert_and_key_files(cert_path, str(key_file))

    @pytest.mark.parametrize(
        "trailing_bytes",
        [
            b"-----BEGIN CERTIFICATE-----\nMIIB\n",
            b"MIIB\n-----END CERTIFICATE-----\n",
        ],
    )
    def test_truncated_multi_cert_raises_error(self, tmp_path, trailing_bytes):
        cert_file = tmp_path / "truncated_chain.pem"
        cert_file.write_bytes(pytest.public_cert_bytes + trailing_bytes)
        key_path = os.path.join(pytest.data_dir, "privatekey.pem")
        with pytest.raises(exceptions.ClientCertError):
            _mtls_helper._read_cert_and_key_files(str(cert_file), key_path)


class TestGetCertConfigPath(object):
    def test_success_with_override(self):
        config_path = os.path.join(pytest.data_dir, "service_account.json")
        returned_path = _mtls_helper._get_cert_config_path(config_path)
        assert returned_path == config_path

    @mock.patch("google.auth.transport._mtls_helper._LOGGER.debug")
    def test_override_does_not_exist(self, mock_debug):
        config_path = "fake/file/path"
        returned_path = _mtls_helper._get_cert_config_path(config_path)
        assert returned_path is None
        mock_debug.assert_called_once_with(
            "Certificate configuration file explicitly specified via %s at %s does not exist",
            "function argument",
            "fake/file/path",
        )

    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_CERTIFICATE_CONFIG": "",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "",
        },
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_default(self, mock_path_exists):
        mock_path_exists.return_value = True
        returned_path = _mtls_helper._get_cert_config_path()
        expected_path = os.path.expanduser(
            os.path.join(
                _mtls_helper._cloud_sdk.get_config_path(), "certificate_config.json"
            )
        )
        assert returned_path == expected_path

    @mock.patch.dict(
        os.environ, {"GOOGLE_API_CERTIFICATE_CONFIG": "path/to/config/file"}
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_env_variable(self, mock_path_exists):
        mock_path_exists.return_value = True
        returned_path = _mtls_helper._get_cert_config_path()
        expected_path = "path/to/config/file"
        assert returned_path == expected_path

    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_CERTIFICATE_CONFIG": "",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "",
        },
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_default_file_does_not_exist(self, mock_path_exists):
        mock_path_exists.return_value = False
        returned_path = _mtls_helper._get_cert_config_path()
        assert returned_path is None

    def test_cert_config_path_precedence(self):
        # GOOGLE_API_CERTIFICATE_CONFIG takes precedence
        google_path = "/path/to/google/config"
        cloudsdk_path = "/path/to/cloudsdk/config"

        with mock.patch.dict(
            os.environ,
            {
                environment_vars.GOOGLE_API_CERTIFICATE_CONFIG: google_path,
                environment_vars.CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH: cloudsdk_path,
            },
        ):
            with mock.patch("os.path.exists", return_value=True):
                assert _mtls_helper._get_cert_config_path() == google_path

    def test_cert_config_path_fallback(self):
        # Fallback to CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH if GOOGLE_API_CERTIFICATE_CONFIG is unset
        cloudsdk_path = "/path/to/cloudsdk/config"

        with mock.patch.dict(
            os.environ,
            {
                environment_vars.CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH: cloudsdk_path
            },
        ):
            if environment_vars.GOOGLE_API_CERTIFICATE_CONFIG in os.environ:
                del os.environ[environment_vars.GOOGLE_API_CERTIFICATE_CONFIG]

            with mock.patch("os.path.exists", return_value=True):
                assert _mtls_helper._get_cert_config_path() == cloudsdk_path

    @mock.patch.dict(
        os.environ, {"GOOGLE_API_CERTIFICATE_CONFIG": "path/to/config/file"}
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_env_variable_file_does_not_exist(self, mock_path_exists):
        mock_path_exists.return_value = False
        returned_path = _mtls_helper._get_cert_config_path()
        assert returned_path is None

    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_CERTIFICATE_CONFIG": "",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "path/to/context/aware/config",
        },
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_cert_config_path_ignore_context_aware(self, mock_path_exists):
        mock_path_exists.return_value = True
        returned_path = _mtls_helper._get_cert_config_path(include_context_aware=False)
        expected_path = os.path.expanduser(
            os.path.join(
                _mtls_helper._cloud_sdk.get_config_path(), "certificate_config.json"
            )
        )
        assert returned_path == expected_path


class TestGetClientCertAndKey(object):
    def test_callback_success(self):
        callback = mock.Mock()
        callback.return_value = (pytest.public_cert_bytes, pytest.private_key_bytes)

        found_cert_key, cert, key = _mtls_helper.get_client_cert_and_key(callback)
        assert found_cert_key
        assert cert == pytest.public_cert_bytes
        assert key == pytest.private_key_bytes

    @mock.patch(
        "google.auth.transport._mtls_helper.get_client_ssl_credentials", autospec=True
    )
    def test_use_metadata(self, mock_get_client_ssl_credentials):
        mock_get_client_ssl_credentials.return_value = (
            True,
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
            None,
        )

        found_cert_key, cert, key = _mtls_helper.get_client_cert_and_key()
        assert found_cert_key
        assert cert == pytest.public_cert_bytes
        assert key == pytest.private_key_bytes


class TestDecryptPrivateKey(object):
    def test_success(self):
        decrypted_key = _mtls_helper.decrypt_private_key(
            ENCRYPTED_EC_PRIVATE_KEY, PASSPHRASE_VALUE
        )
        private_key = serialization.load_pem_private_key(decrypted_key, password=None)
        public_key = serialization.load_pem_public_key(EC_PUBLIC_KEY)

        # Test the decrypted key works by signing and verification.
        signature = private_key.sign(b"data", ec.ECDSA(hashes.SHA256()))
        public_key.verify(signature, b"data", ec.ECDSA(hashes.SHA256()))

    def test_success_string_inputs(self):
        decrypted_key = _mtls_helper.decrypt_private_key(
            ENCRYPTED_EC_PRIVATE_KEY.decode("utf-8"), PASSPHRASE_VALUE.decode("utf-8")
        )
        private_key = serialization.load_pem_private_key(decrypted_key, password=None)
        assert private_key

    def test_crypto_error(self):
        with pytest.raises(ValueError):
            _mtls_helper.decrypt_private_key(
                ENCRYPTED_EC_PRIVATE_KEY, b"wrong_password"
            )


class TestCheckUseClientCertEnv(object):
    @mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"})
    def test_env_var_explicit_true(self):
        assert _mtls_helper._check_use_client_cert_env() is True

    @mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "True"})
    def test_env_var_explicit_true_capitalized(self):
        assert _mtls_helper._check_use_client_cert_env() is True

    @mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"})
    def test_env_var_explicit_false(self):
        assert _mtls_helper._check_use_client_cert_env() is False

    @mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "garbage"})
    def test_env_var_explicit_garbage(self):
        assert _mtls_helper._check_use_client_cert_env() is False

    @mock.patch.dict(os.environ, {}, clear=True)
    def test_env_var_unset(self):
        assert _mtls_helper._check_use_client_cert_env() is None

    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "true",
        },
    )
    def test_env_var_fallback_true(self):
        assert _mtls_helper._check_use_client_cert_env() is True


class TestCheckUseClientCert(object):
    @mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"})
    def test_env_var_explicit_true(self):
        assert _mtls_helper.check_use_client_cert() is True

    @mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "True"})
    def test_env_var_explicit_true_capitalized(self):
        assert _mtls_helper.check_use_client_cert() is True

    @mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"})
    def test_env_var_explicit_false(self):
        assert _mtls_helper.check_use_client_cert() is False

    @mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "garbage"})
    def test_env_var_explicit_garbage(self):
        assert _mtls_helper.check_use_client_cert() is False

    @mock.patch("builtins.open", autospec=True)
    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "",
            "GOOGLE_API_CERTIFICATE_CONFIG": "/path/to/config",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "",
        },
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_config_file_success(self, mock_exists, mock_file):
        mock_exists.return_value = True
        # We manually apply mock_open here so we can keep autospec=True on the decorator
        mock_file.side_effect = mock.mock_open(
            read_data='{"cert_configs": {"workload": "exists"}}'
        )
        assert _mtls_helper.check_use_client_cert() is True

    @mock.patch("builtins.open", autospec=True)
    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "",
            "GOOGLE_API_CERTIFICATE_CONFIG": "/path/to/config",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "",
        },
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_config_file_missing_keys(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.side_effect = mock.mock_open(read_data='{"cert_configs": {}}')
        assert _mtls_helper.check_use_client_cert() is False

    @mock.patch("builtins.open", autospec=True)
    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "",
            "GOOGLE_API_CERTIFICATE_CONFIG": "/path/to/config",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "",
        },
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_config_file_bad_json(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.side_effect = mock.mock_open(read_data="{bad_json")
        assert _mtls_helper.check_use_client_cert() is False

    @mock.patch("builtins.open", autospec=True)
    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "",
            "GOOGLE_API_CERTIFICATE_CONFIG": "/path/does/not/exist",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "",
        },
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_config_file_not_found(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.side_effect = FileNotFoundError
        assert _mtls_helper.check_use_client_cert() is False

    @mock.patch("builtins.open", autospec=True)
    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "",
            "GOOGLE_API_CERTIFICATE_CONFIG": "/path/to/config",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "",
        },
    )
    @mock.patch("os.path.exists", autospec=True)
    def test_config_file_invalid_json_type(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_file.side_effect = mock.mock_open(read_data="[]")
        assert _mtls_helper.check_use_client_cert() is False

    @mock.patch("builtins.open", autospec=True)
    @mock.patch.dict(os.environ, {}, clear=True)
    @mock.patch("os.path.exists", autospec=True)
    def test_no_env_vars_set(self, mock_exists, mock_open):
        mock_exists.return_value = False
        mock_open.side_effect = FileNotFoundError()
        assert _mtls_helper.check_use_client_cert() is False

    def test_use_client_cert_precedence(self):
        # GOOGLE_API_USE_CLIENT_CERTIFICATE takes precedence
        with mock.patch.dict(
            os.environ,
            {
                environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true",
                environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE: "false",
            },
        ):
            assert _mtls_helper.check_use_client_cert() is True

        with mock.patch.dict(
            os.environ,
            {
                environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "false",
                environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE: "true",
            },
        ):
            assert _mtls_helper.check_use_client_cert() is False

    def test_use_client_cert_fallback(self):
        # Fallback to CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE if GOOGLE_API_USE_CLIENT_CERTIFICATE is unset
        with mock.patch.dict(
            os.environ,
            {environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE: "true"},
        ):
            # Ensure GOOGLE_API_USE_CLIENT_CERTIFICATE is not set
            if environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE in os.environ:
                del os.environ[environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE]
            assert _mtls_helper.check_use_client_cert() is True

        with mock.patch.dict(
            os.environ,
            {environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE: "false"},
        ):
            if environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE in os.environ:
                del os.environ[environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE]
            assert _mtls_helper.check_use_client_cert() is False

    @mock.patch("builtins.open", autospec=True)
    @mock.patch("os.path.exists", autospec=True)
    def test_check_use_client_cert_config_fallback(self, mock_exists, mock_file):
        mock_exists.return_value = True
        # Test fallback for config file when determining if client cert should be used
        cloudsdk_path = "/path/to/cloudsdk/config"

        mock_file.side_effect = mock.mock_open(
            read_data='{"cert_configs": {"workload": "exists"}}'
        )

        with mock.patch.dict(
            os.environ,
            {
                environment_vars.CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH: cloudsdk_path
            },
        ):
            if environment_vars.GOOGLE_API_CERTIFICATE_CONFIG in os.environ:
                del os.environ[environment_vars.GOOGLE_API_CERTIFICATE_CONFIG]
            if environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE in os.environ:
                del os.environ[environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE]
            if (
                environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE
                in os.environ
            ):
                del os.environ[
                    environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE
                ]

            assert _mtls_helper.check_use_client_cert() is True


class TestMtlsHelper:
    @mock.patch.object(_mtls_helper, "call_client_cert_callback")
    @mock.patch("google.auth.transport._mtls_helper._agent_identity_utils")
    def test_check_parameters_for_unauthorized_response_with_cached_cert(
        self, mock_agent_identity_utils, mock_call_client_cert_callback
    ):
        mock_call_client_cert_callback.return_value = (
            CERT_MOCK_VAL,
            KEY_MOCK_VAL,
        )
        mock_agent_identity_utils.get_cached_cert_fingerprint.return_value = (
            "cached_fingerprint"
        )
        mock_agent_identity_utils.calculate_certificate_fingerprint.return_value = (
            "current_fingerprint"
        )

        (
            cert,
            key,
            cached_fingerprint,
            current_fingerprint,
        ) = _mtls_helper.check_parameters_for_unauthorized_response(
            cached_cert=b"cached_cert_bytes"
        )

        assert cert == CERT_MOCK_VAL
        assert key == KEY_MOCK_VAL
        assert cached_fingerprint == "cached_fingerprint"
        assert current_fingerprint == "current_fingerprint"
        mock_call_client_cert_callback.assert_called_once()
        mock_agent_identity_utils.get_cached_cert_fingerprint.assert_called_once_with(
            b"cached_cert_bytes"
        )

    @mock.patch.object(_mtls_helper, "call_client_cert_callback")
    @mock.patch.object(_mtls_helper, "_agent_identity_utils")
    def test_check_parameters_for_unauthorized_response_without_cached_cert(
        self, mock_agent_identity_utils, mock_call_client_cert_callback
    ):
        mock_call_client_cert_callback.return_value = (
            CERT_MOCK_VAL,
            KEY_MOCK_VAL,
        )
        mock_agent_identity_utils.calculate_certificate_fingerprint.return_value = (
            "current_fingerprint"
        )

        (
            cert,
            key,
            cached_fingerprint,
            current_fingerprint,
        ) = _mtls_helper.check_parameters_for_unauthorized_response(cached_cert=None)

        assert cert == CERT_MOCK_VAL
        assert key == KEY_MOCK_VAL
        assert cached_fingerprint == "current_fingerprint"
        assert current_fingerprint == "current_fingerprint"
        mock_call_client_cert_callback.assert_called_once()
        mock_agent_identity_utils.get_cached_cert_fingerprint.assert_not_called()

    @mock.patch("google.auth.transport._mtls_helper.call_client_cert_callback")
    @mock.patch("google.auth.transport._mtls_helper._agent_identity_utils")
    def test_check_parameters_for_unauthorized_response_no_call_cert(
        self, mock_agent_identity_utils, mock_call_client_cert_callback
    ):
        mock_call_client_cert_callback.return_value = (None, None)

        result = _mtls_helper.check_parameters_for_unauthorized_response(
            cached_cert=CERT_MOCK_VAL
        )

        assert result == (None, None, None, None)
        mock_call_client_cert_callback.assert_called_once()
        mock_agent_identity_utils.parse_certificate.assert_not_called()

    @mock.patch("google.auth.transport._mtls_helper.get_client_ssl_credentials")
    def test_call_client_cert_callback(self, mock_get_client_ssl_credentials):
        mock_get_client_ssl_credentials.return_value = (
            True,
            b"cert_bytes",
            b"key_bytes",
            None,
        )

        cert, key = _mtls_helper.call_client_cert_callback()

        assert cert == b"cert_bytes"
        assert key == b"key_bytes"
        mock_get_client_ssl_credentials.assert_called_once_with(
            generate_encrypted_key=False
        )

    @mock.patch("subprocess.Popen", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper._load_json_file", autospec=True)
    @mock.patch("google.auth.transport._mtls_helper._check_config_path", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper._get_workload_cert_and_key", autospec=True
    )
    def test_call_client_cert_callback_secure_connect_unencrypted_key(
        self,
        mock_get_workload_cert_and_key,
        mock_check_config_path,
        mock_load_json_file,
        mock_popen,
    ):
        mock_get_workload_cert_and_key.return_value = (None, None)
        mock_check_config_path.return_value = "/path/to/config"
        mock_load_json_file.return_value = {"cert_provider_command": ["command"]}

        process = mock.Mock()
        process.configure_mock(
            **{
                "communicate.return_value": (
                    pytest.public_cert_bytes + pytest.private_key_bytes,
                    b"",
                ),
                "returncode": 0,
            }
        )
        mock_popen.return_value = process

        cert, key = _mtls_helper.call_client_cert_callback()

        assert cert == pytest.public_cert_bytes
        assert key == pytest.private_key_bytes


class TestSecureCertKeyPaths(object):
    def test_tier1_pass_through(self):
        with _mtls_helper.secure_cert_key_paths(
            "/path/to/cert", "/path/to/key", b"passphrase"
        ) as (cert_path, key_path, passphrase):
            assert cert_path == "/path/to/cert"
            assert key_path == "/path/to/key"
            assert passphrase == b"passphrase"

    @mock.patch.object(_mtls_helper, "_tempfile_cert_key_paths", autospec=True)
    def test_string_pem_payloads_converted_to_bytes(self, mock_tempfile_cm):
        mock_tempfile_ctx = mock.MagicMock()
        mock_tempfile_ctx.__enter__.return_value = (
            "/tmp/cert",
            "/tmp/key",
            b"new_pass",
        )
        mock_tempfile_cm.return_value = mock_tempfile_ctx

        cert_str = "-----BEGIN CERTIFICATE-----\n..."
        key_str = "-----BEGIN PRIVATE KEY-----\n..."

        # Temporarily mock sys.platform to something other than linux so memfd is skipped
        with mock.patch.object(sys, "platform", "win32"):
            with _mtls_helper.secure_cert_key_paths(
                cert_str, key_str, b"passphrase"
            ) as (cert_path, key_path, passphrase):
                assert cert_path == "/tmp/cert"
                assert key_path == "/tmp/key"
                assert passphrase == b"new_pass"

        mock_tempfile_cm.assert_called_once_with(
            cert_str.encode("utf-8"), key_str.encode("utf-8"), b"passphrase"
        )

    @mock.patch.object(sys, "platform", "linux")
    @mock.patch.object(os, "memfd_create", create=True)
    @mock.patch.object(_mtls_helper, "_memfd_cert_key_paths", autospec=True)
    def test_memfd_success(self, mock_memfd_cm, mock_memfd_create):
        mock_memfd_ctx = mock.MagicMock()
        mock_memfd_ctx.__enter__.return_value = (
            "/proc/self/fd/3",
            "/proc/self/fd/4",
        )
        mock_memfd_cm.return_value = mock_memfd_ctx

        with (
            mock.patch.object(os.path, "exists", return_value=True),
            mock.patch("builtins.open", mock.mock_open()),
        ):
            with _mtls_helper.secure_cert_key_paths(
                pytest.public_cert_bytes,
                pytest.private_key_bytes,
                b"passphrase",
            ) as (cert_path, key_path, passphrase):
                assert cert_path == "/proc/self/fd/3"
                assert key_path == "/proc/self/fd/4"
                assert passphrase == b"passphrase"
            assert mock_memfd_ctx.__exit__.called

    @mock.patch.object(sys, "platform", "linux")
    @mock.patch.object(os, "memfd_create", create=True)
    @mock.patch.object(_mtls_helper, "_memfd_cert_key_paths", autospec=True)
    @mock.patch.object(_mtls_helper, "_tempfile_cert_key_paths", autospec=True)
    def test_falls_back_to_tempfile_when_filesystem_restricted(
        self, mock_tempfile_cm, mock_memfd_cm, mock_memfd_create
    ):
        mock_memfd_ctx = mock.MagicMock()
        mock_memfd_ctx.__enter__.return_value = (
            "/proc/self/fd/3",
            "/proc/self/fd/4",
        )
        mock_memfd_cm.return_value = mock_memfd_ctx

        mock_tempfile_ctx = mock.MagicMock()
        mock_tempfile_ctx.__enter__.return_value = (
            "/tmp/cert",
            "/tmp/key",
            b"new_pass",
        )
        mock_tempfile_cm.return_value = mock_tempfile_ctx

        with mock.patch.object(os.path, "exists", return_value=False):
            with _mtls_helper.secure_cert_key_paths(
                pytest.public_cert_bytes, pytest.private_key_bytes, b"passphrase"
            ) as (cert_path, key_path, passphrase):
                assert cert_path == "/tmp/cert"
                assert key_path == "/tmp/key"
                assert passphrase == b"new_pass"
            mock_memfd_ctx.__exit__.assert_called_once_with(None, None, None)

    @mock.patch.object(sys, "platform", "linux")
    @mock.patch.object(os, "memfd_create", create=True)
    @mock.patch.object(_mtls_helper, "_memfd_cert_key_paths", autospec=True)
    @mock.patch.object(_mtls_helper, "_tempfile_cert_key_paths", autospec=True)
    def test_falls_back_to_tempfile_when_filesystem_unreadable(
        self, mock_tempfile_cm, mock_memfd_cm, mock_memfd_create
    ):
        mock_memfd_ctx = mock.MagicMock()
        mock_memfd_ctx.__enter__.return_value = (
            "/proc/self/fd/3",
            "/proc/self/fd/4",
        )
        mock_memfd_cm.return_value = mock_memfd_ctx

        mock_tempfile_ctx = mock.MagicMock()
        mock_tempfile_ctx.__enter__.return_value = (
            "/tmp/cert",
            "/tmp/key",
            b"new_pass",
        )
        mock_tempfile_cm.return_value = mock_tempfile_ctx

        with (
            mock.patch.object(os.path, "exists", return_value=True),
            mock.patch("builtins.open", mock.mock_open()) as mock_open,
        ):
            mock_open.side_effect = PermissionError("Permission denied")

            with _mtls_helper.secure_cert_key_paths(
                pytest.public_cert_bytes, pytest.private_key_bytes, b"passphrase"
            ) as (cert_path, key_path, passphrase):
                assert cert_path == "/tmp/cert"
                assert key_path == "/tmp/key"
                assert passphrase == b"new_pass"

            mock_memfd_ctx.__exit__.assert_called_once_with(None, None, None)

    @mock.patch.object(sys, "platform", "linux")
    @mock.patch.object(os, "memfd_create", create=True)
    @mock.patch.object(_mtls_helper, "_memfd_cert_key_paths", autospec=True)
    @mock.patch.object(_mtls_helper, "_tempfile_cert_key_paths", autospec=True)
    def test_falls_back_to_tempfile_when_memfd_fails(
        self, mock_tempfile_cm, mock_memfd_cm, mock_memfd_create
    ):
        mock_memfd_ctx = mock.MagicMock()
        mock_memfd_ctx.__enter__.side_effect = _mtls_helper._MemfdCreationError(
            "memfd failed"
        )
        mock_memfd_cm.return_value = mock_memfd_ctx

        mock_tempfile_ctx = mock.MagicMock()
        mock_tempfile_ctx.__enter__.return_value = (
            "/tmp/cert",
            "/tmp/key",
            b"new_pass",
        )
        mock_tempfile_cm.return_value = mock_tempfile_ctx

        with _mtls_helper.secure_cert_key_paths(
            pytest.public_cert_bytes, pytest.private_key_bytes, b"passphrase"
        ) as (cert_path, key_path, passphrase):
            assert cert_path == "/tmp/cert"
            assert key_path == "/tmp/key"
            assert passphrase == b"new_pass"

    @mock.patch.object(sys, "platform", "linux")
    @mock.patch.object(os, "memfd_create", create=True)
    @mock.patch.object(_mtls_helper, "_memfd_cert_key_paths", autospec=True)
    @mock.patch.object(_mtls_helper, "_tempfile_cert_key_paths", autospec=True)
    def test_tier3_fallback_failure_propagation(
        self, mock_tempfile_cm, mock_memfd_cm, mock_memfd_create
    ):
        mock_memfd_ctx = mock.MagicMock()
        mock_memfd_ctx.__enter__.side_effect = _mtls_helper._MemfdCreationError(
            "memfd failed"
        )
        mock_memfd_cm.return_value = mock_memfd_ctx

        mock_tempfile_ctx = mock.MagicMock()
        mock_tempfile_ctx.__enter__.side_effect = OSError("tempfile failed")
        mock_tempfile_cm.return_value = mock_tempfile_ctx

        with pytest.raises(OSError) as exc_info:
            with _mtls_helper.secure_cert_key_paths(
                pytest.public_cert_bytes, pytest.private_key_bytes, b"passphrase"
            ):
                pass

        assert "tempfile failed" in str(exc_info.value)

    @mock.patch.object(sys, "platform", "darwin")
    @mock.patch.object(_mtls_helper, "_tempfile_cert_key_paths", autospec=True)
    def test_uses_tempfile_directly_on_unsupported_os(self, mock_tempfile_cm):
        mock_tempfile_ctx = mock.MagicMock()
        mock_tempfile_ctx.__enter__.return_value = (
            "/tmp/cert",
            "/tmp/key",
            b"new_pass",
        )
        mock_tempfile_cm.return_value = mock_tempfile_ctx

        with _mtls_helper.secure_cert_key_paths(
            pytest.public_cert_bytes, pytest.private_key_bytes, b"passphrase"
        ) as (cert_path, key_path, passphrase):
            assert cert_path == "/tmp/cert"
            assert key_path == "/tmp/key"
            assert passphrase == b"new_pass"

    @mock.patch.object(sys, "platform", "darwin")
    @mock.patch.object(_mtls_helper, "_tempfile_cert_key_paths", autospec=True)
    def test_hybrid_inputs(self, mock_tempfile_cm):
        mock_tempfile_ctx = mock.MagicMock()
        mock_tempfile_ctx.__enter__.return_value = (
            None,
            "/tmp/key",
            b"new_pass",
        )
        mock_tempfile_cm.return_value = mock_tempfile_ctx

        with _mtls_helper.secure_cert_key_paths(
            "/pass/through/cert.pem", pytest.private_key_bytes, b"passphrase"
        ) as (cert_path, key_path, passphrase):
            assert cert_path == "/pass/through/cert.pem"
            assert key_path == "/tmp/key"
            assert passphrase == b"new_pass"


class TestMemfdCertKeyPaths(object):
    @mock.patch.object(os, "memfd_create", create=True)
    @mock.patch.object(os, "fdopen")
    @mock.patch.object(os, "close")
    def test_success_both_bytes(self, mock_close, mock_fdopen, mock_memfd_create):
        mock_memfd_create.side_effect = [10, 11]
        mock_file_cert = mock.mock_open().return_value
        mock_file_key = mock.mock_open().return_value
        mock_fdopen.side_effect = [mock_file_cert, mock_file_key]
        with _mtls_helper._memfd_cert_key_paths(b"cert", b"key") as (
            cert_path,
            key_path,
        ):
            assert cert_path == "/proc/self/fd/10"
            assert key_path == "/proc/self/fd/11"
        mock_fdopen.assert_has_calls(
            [mock.call(10, "wb", closefd=False), mock.call(11, "wb", closefd=False)]
        )
        mock_file_cert.write.assert_called_once_with(b"cert")
        mock_file_key.write.assert_called_once_with(b"key")
        assert mock_close.call_count == 2

    @mock.patch.object(os, "memfd_create", create=True)
    @mock.patch.object(os, "fdopen")
    @mock.patch.object(os, "close")
    def test_close_ignores_oserror(self, mock_close, mock_fdopen, mock_memfd_create):
        mock_memfd_create.return_value = 12
        mock_close.side_effect = OSError("close error")
        mock_file = mock.mock_open().return_value
        mock_fdopen.return_value = mock_file
        with _mtls_helper._memfd_cert_key_paths(b"cert", None) as (cert_path, key_path):
            assert cert_path == "/proc/self/fd/12"
            assert key_path is None
        mock_fdopen.assert_called_once_with(12, "wb", closefd=False)
        mock_file.write.assert_called_once_with(b"cert")
        mock_close.assert_called_once_with(12)

    @mock.patch.object(os, "memfd_create", create=True)
    @mock.patch.object(os, "fdopen")
    @mock.patch.object(os, "close")
    def test_write_oserror_prevents_fd_leak(
        self, mock_close, mock_fdopen, mock_memfd_create
    ):
        mock_memfd_create.return_value = 15
        mock_file = mock.mock_open().return_value
        mock_file.write.side_effect = OSError("write fault")
        mock_fdopen.return_value = mock_file
        with pytest.raises(OSError):
            with _mtls_helper._memfd_cert_key_paths(b"cert", None):
                pass
        mock_fdopen.assert_called_once_with(15, "wb", closefd=False)
        mock_file.write.assert_called_once_with(b"cert")
        mock_close.assert_called_once_with(15)

    @mock.patch.object(os, "memfd_create", create=True)
    def test_memfd_attribute_error(self, mock_memfd_create):
        # MFD_CLOEXEC missing on the system
        with mock.patch("os.MFD_CLOEXEC", create=True):
            del os.MFD_CLOEXEC
            with pytest.raises(_mtls_helper._MemfdCreationError):
                with _mtls_helper._memfd_cert_key_paths(b"cert", None):
                    pass


class TestTempfileCertKeyPaths(object):
    @mock.patch.object(os, "access", return_value=True)
    @mock.patch.object(os.path, "isdir", return_value=True)
    @mock.patch.object(_mtls_helper, "_encrypt_key_if_plaintext", autospec=True)
    def test_success_shm(
        self,
        mock_encrypt,
        mock_isdir,
        mock_access,
        tmpdir,
    ):
        original_mkstemp = tempfile.mkstemp

        def _redirect_mkstemp(dir=None):
            return original_mkstemp(dir=str(tmpdir))

        with mock.patch.object(
            tempfile, "mkstemp", side_effect=_redirect_mkstemp
        ) as mock_mkstemp:
            mock_encrypt.return_value = (b"encrypted_key", b"new_pass")

            with _mtls_helper._tempfile_cert_key_paths(b"cert", b"key", b"pass") as (
                cert_path,
                key_path,
                passphrase,
            ):
                assert cert_path.startswith(str(tmpdir))
                assert os.path.exists(cert_path)
                assert passphrase == b"new_pass"

                with open(cert_path, "rb") as f:
                    assert f.read() == b"cert"

                with open(key_path, "rb") as f:
                    assert f.read() == b"encrypted_key"

            # Organically verify secure cleanup occurred
            assert not os.path.exists(cert_path)
            assert not os.path.exists(key_path)

            mock_mkstemp.assert_has_calls(
                [mock.call(dir="/dev/shm"), mock.call(dir="/dev/shm")]
            )

    @mock.patch.object(os, "access", return_value=True)
    @mock.patch.object(os.path, "isdir", return_value=True)
    @mock.patch.object(_mtls_helper, "_encrypt_key_if_plaintext", autospec=True)
    def test_cleanup_on_keyboard_interrupt(
        self, mock_encrypt, mock_isdir, mock_access, tmpdir
    ):
        original_mkstemp = tempfile.mkstemp

        def _redirect_mkstemp(dir=None):
            return original_mkstemp(dir=str(tmpdir))

        with mock.patch.object(tempfile, "mkstemp", side_effect=_redirect_mkstemp):
            mock_encrypt.return_value = (b"encrypted_key", b"new_pass")

            with pytest.raises(KeyboardInterrupt):
                with mock.patch.object(
                    _mtls_helper,
                    "_secure_wipe_and_remove",
                    side_effect=KeyboardInterrupt("ctrl-c"),
                ):
                    with _mtls_helper._tempfile_cert_key_paths(
                        b"cert", b"key", b"pass"
                    ) as (cert_path, key_path, pwd):
                        # exiting the context manager triggers cleanup and raises KeyboardInterrupt
                        pass

            # Verify cert file is still cleaned up even if key cleanup raised KeyboardInterrupt
            assert not os.path.exists(cert_path)

    @mock.patch.object(os, "access", return_value=True)
    @mock.patch.object(os.path, "isdir", return_value=True)
    @mock.patch.object(_mtls_helper, "_encrypt_key_if_plaintext", autospec=True)
    def test_cleanup_on_key_write_error(
        self, mock_encrypt, mock_isdir, mock_access, tmpdir
    ):
        original_mkstemp = tempfile.mkstemp

        cert_path_ref = []

        def _redirect_mkstemp(dir=None):
            fd, path = original_mkstemp(dir=str(tmpdir))
            cert_path_ref.append(path)
            return fd, path

        with mock.patch.object(tempfile, "mkstemp", side_effect=_redirect_mkstemp):
            mock_encrypt.return_value = (b"encrypted_key", b"new_pass")

            original_fdopen = os.fdopen
            call_count = [0]

            def _failing_fdopen(fd, *args, **kwargs):
                call_count[0] += 1
                if call_count[0] == 2:
                    raise OSError("key write failed")
                return original_fdopen(fd, *args, **kwargs)

            with pytest.raises(OSError):
                with mock.patch("os.fdopen", side_effect=_failing_fdopen):
                    with _mtls_helper._tempfile_cert_key_paths(
                        b"cert", b"key", b"pass"
                    ):
                        pass

            assert len(cert_path_ref) > 0
            assert not os.path.exists(cert_path_ref[0])

    @mock.patch.object(os, "access", return_value=True)
    @mock.patch.object(os.path, "isdir", return_value=True)
    @mock.patch.object(_mtls_helper, "_encrypt_key_if_plaintext", autospec=True)
    def test_mkstemp_shm_oserror_fallback(
        self,
        mock_encrypt,
        mock_isdir,
        mock_access,
        tmpdir,
    ):
        original_mkstemp = tempfile.mkstemp
        call_count = [0]

        def _redirect_mkstemp(dir=None):
            call_count[0] += 1
            if call_count[0] % 2 != 0:
                raise OSError("No space left on device")
            return original_mkstemp(dir=str(tmpdir))

        with mock.patch.object(
            tempfile, "mkstemp", side_effect=_redirect_mkstemp
        ) as mock_mkstemp:
            mock_encrypt.return_value = (b"encrypted_key", b"new_pass")

            with _mtls_helper._tempfile_cert_key_paths(b"cert", b"key", b"pass") as (
                cert_path,
                key_path,
                passphrase,
            ):
                assert cert_path.startswith(str(tmpdir))
                assert os.path.exists(cert_path)
                assert passphrase == b"new_pass"

            mock_mkstemp.assert_has_calls(
                [
                    mock.call(dir="/dev/shm"),
                    mock.call(dir=None),
                    mock.call(dir="/dev/shm"),
                    mock.call(dir=None),
                ]
            )

            assert not os.path.exists(cert_path)
            assert not os.path.exists(key_path)

    @mock.patch.object(os, "access", return_value=True)
    @mock.patch.object(os.path, "isdir", return_value=True)
    @mock.patch.object(_mtls_helper, "_encrypt_key_if_plaintext", autospec=True)
    @mock.patch.object(_mtls_helper, "_secure_wipe_and_remove", autospec=True)
    def test_permission_error_loop_resilience(
        self,
        mock_wipe,
        mock_encrypt,
        mock_isdir,
        mock_access,
        tmpdir,
    ):
        original_mkstemp = tempfile.mkstemp

        def _redirect_mkstemp(dir=None):
            return original_mkstemp(dir=str(tmpdir))

        with mock.patch.object(tempfile, "mkstemp", side_effect=_redirect_mkstemp):
            mock_encrypt.return_value = (b"encrypted_key", b"new_pass")

            # Mock the secure wipe to fail with PermissionError to test resilience
            mock_wipe.side_effect = PermissionError("lock error")

            with _mtls_helper._tempfile_cert_key_paths(b"cert", b"key", b"pass") as (
                cert_path,
                key_path,
                passphrase,
            ):
                assert os.path.exists(cert_path)
                assert os.path.exists(key_path)

            # Organically verify cert_path was cleaned up despite PermissionError on key
            assert not os.path.exists(cert_path)


class TestEncryptKeyIfPlaintext(object):
    def test_encrypts_plaintext_key(self):
        encrypted_bytes, passphrase = _mtls_helper._encrypt_key_if_plaintext(
            pytest.private_key_bytes, b"my_passphrase"
        )
        assert passphrase == b"my_passphrase"
        assert encrypted_bytes != pytest.private_key_bytes
        assert b"ENCRYPTED PRIVATE KEY" in encrypted_bytes

        decrypted = serialization.load_pem_private_key(
            encrypted_bytes, password=b"my_passphrase"
        )
        assert decrypted

        original_key = serialization.load_pem_private_key(
            pytest.private_key_bytes, password=None
        )
        decrypted_bytes = decrypted.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        original_bytes = original_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        assert decrypted_bytes == original_bytes

    @mock.patch("secrets.token_hex", return_value="0123456789abcdef0123456789abcdef")
    def test_default_passphrase_generation(self, mock_secrets):
        encrypted_bytes, passphrase = _mtls_helper._encrypt_key_if_plaintext(
            pytest.private_key_bytes, None
        )
        assert passphrase == b"0123456789abcdef0123456789abcdef"
        assert b"ENCRYPTED PRIVATE KEY" in encrypted_bytes

    def test_returns_encrypted_key_asis(self):
        encrypted_bytes, passphrase = _mtls_helper._encrypt_key_if_plaintext(
            ENCRYPTED_EC_PRIVATE_KEY, b"passphrase"
        )
        assert encrypted_bytes == ENCRYPTED_EC_PRIVATE_KEY
        assert passphrase == b"passphrase"

    def test_encrypts_plaintext_key_string_passphrase(self):
        encrypted_bytes, passphrase = _mtls_helper._encrypt_key_if_plaintext(
            pytest.private_key_bytes, "my_passphrase_str"
        )
        assert passphrase == b"my_passphrase_str"
        assert encrypted_bytes != pytest.private_key_bytes
        assert b"ENCRYPTED PRIVATE KEY" in encrypted_bytes

        decrypted = serialization.load_pem_private_key(
            encrypted_bytes, password=b"my_passphrase_str"
        )
        original_key = serialization.load_pem_private_key(
            pytest.private_key_bytes, password=None
        )
        decrypted_bytes = decrypted.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        original_bytes = original_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        assert decrypted_bytes == original_bytes

    def test_returns_unsupported_algorithm_asis(self):
        import cryptography.exceptions

        invalid_bytes = b"not a valid key"
        with mock.patch(
            "cryptography.hazmat.primitives.serialization.load_pem_private_key"
        ) as load_mock:
            load_mock.side_effect = cryptography.exceptions.UnsupportedAlgorithm(
                "unsupported"
            )
            encrypted_bytes, passphrase = _mtls_helper._encrypt_key_if_plaintext(
                invalid_bytes, b"passphrase"
            )
            assert encrypted_bytes == invalid_bytes
            assert passphrase == b"passphrase"

    def test_returns_invalid_key_asis(self):
        invalid_bytes = b"not a valid key"
        encrypted_bytes, passphrase = _mtls_helper._encrypt_key_if_plaintext(
            invalid_bytes, b"passphrase"
        )
        assert encrypted_bytes == invalid_bytes
        assert passphrase == b"passphrase"


class TestSecureWipeAndRemove(object):
    @mock.patch.object(os.path, "exists", return_value=True)
    @mock.patch.object(os.path, "getsize", return_value=10)
    @mock.patch("builtins.open", autospec=True)
    @mock.patch.object(os, "fsync")
    @mock.patch.object(os, "remove")
    def test_success(
        self, mock_remove, mock_fsync, mock_open, mock_getsize, mock_exists
    ):
        mock_fh = mock.MagicMock()
        mock_fh.fileno.return_value = 1
        mock_open.return_value.__enter__.return_value = mock_fh

        _mtls_helper._secure_wipe_and_remove("/path/to/secret")

        mock_open.assert_called_once_with("/path/to/secret", "r+b")
        mock_fh.write.assert_called_once_with(b"\0" * 10)
        mock_fh.flush.assert_called_once()
        mock_fsync.assert_called_once()
        mock_remove.assert_called_once_with("/path/to/secret")

    @mock.patch.object(os.path, "exists", return_value=False)
    @mock.patch.object(os, "remove")
    def test_file_not_found(self, mock_remove, mock_exists):
        _mtls_helper._secure_wipe_and_remove("/path/to/nonexistent")

        mock_exists.assert_called_once_with("/path/to/nonexistent")
        mock_remove.assert_not_called()

    @mock.patch.object(os.path, "exists", return_value=True)
    @mock.patch.object(os.path, "getsize", return_value=10)
    @mock.patch("builtins.open", autospec=True)
    @mock.patch.object(os, "fsync")
    @mock.patch.object(os, "remove")
    def test_write_oserror_ignored(
        self, mock_remove, mock_fsync, mock_open, mock_getsize, mock_exists
    ):
        mock_fh = mock.MagicMock()
        mock_fh.fileno.return_value = 1
        mock_fh.write.side_effect = OSError("write fault")
        mock_open.return_value.__enter__.return_value = mock_fh

        _mtls_helper._secure_wipe_and_remove("/path/to/secret")

        mock_open.assert_called_once_with("/path/to/secret", "r+b")
        mock_fsync.assert_not_called()
        mock_remove.assert_called_once_with("/path/to/secret")

    @mock.patch.object(os.path, "exists", return_value=True)
    @mock.patch.object(os.path, "getsize", return_value=10)
    @mock.patch("builtins.open", autospec=True)
    @mock.patch.object(os, "fsync")
    @mock.patch.object(os, "remove")
    def test_remove_oserror_ignored(
        self, mock_remove, mock_fsync, mock_open, mock_getsize, mock_exists
    ):
        mock_fh = mock.MagicMock()
        mock_fh.fileno.return_value = 1
        mock_open.return_value.__enter__.return_value = mock_fh
        mock_remove.side_effect = OSError("remove fault")

        _mtls_helper._secure_wipe_and_remove("/path/to/secret")

        mock_open.assert_called_once_with("/path/to/secret", "r+b")
        mock_fh.flush.assert_called_once()
        mock_fsync.assert_called_once()
        mock_remove.assert_called_once_with("/path/to/secret")


class TestIsMtlsEndpoint(object):
    @pytest.mark.parametrize(
        "url",
        [
            "https://mtls.googleapis.com",
            "https://mtls.googleapis.com/",
            "https://mtls.googleapis.com/v1/projects",
            "https://mtls.sandbox.googleapis.com",
            "https://mtls.sandbox.googleapis.com/v1/projects",
            "https://pubsub.mtls.googleapis.com",
            "https://pubsub.mtls.googleapis.com/v1/projects/my-project",
            "https://storage.mtls.sandbox.googleapis.com/b/my-bucket",
            "https://my-service.us-east1.rep.mtls.googleapis.com/v1",
            "https://my-service.us-east1.rep.mtls.sandbox.googleapis.com/v1",
            "https://storage.p.googleapis.com/b/my-bucket",
            "https://my-custom-endpoint.p.googleapis.com/v1",
            "https://my-service.us-east1.p.googleapis.com/v1",
            "HTTP://PUBSUB.MTLS.GOOGLEAPIS.COM/V1",
            b"https://pubsub.mtls.googleapis.com",
            b"https://storage.p.googleapis.com/b/my-bucket",
            urllib3.util.parse_url("https://pubsub.mtls.googleapis.com/v1"),
            urllib3.util.parse_url("https://storage.p.googleapis.com/b/my-bucket"),
            "https://pubsub.mtls.googleapis.com.",
            "https://storage.p.googleapis.com./b/my-bucket",
            "https://mtls.googleapis.com.",
            "https://pubsub.mtls.googleapis.com:443/v1",
            "https://pubsub.mtls.googleapis.com:8443/v1",
            "https://storage.p.googleapis.com:443/b/my-bucket",
            "https://pubsub.mtls.googleapis.com/v1/projects?pageSize=10#frag",
            "https://pubsub.mtls.googleapis.com:443/v1/projects?pageSize=10&filter=foo#frag",
            "https://storage.p.googleapis.com:443/b/my-bucket?param=1#section",
            "https://mtls.googleapis.com:443/",
            "https://p.googleapis.com",
            "https://p.googleapis.com/",
            "https://p.googleapis.com:443/v1",
            "https://p.googleapis.com.",
            "https://mtls.run.app",
            "https://mtls.run.app/",
            "https://my-service-123456.us-central1.mtls.run.app",
            "https://my-service-123456.us-central1.mtls.run.app/v1/invocations",
            "https://tag---my-service-123456.us-central1.mtls.run.app.",
            b"https://my-service-123456.us-central1.mtls.run.app",
        ],
    )
    def test_is_mtls_endpoint_true(self, url):
        assert _mtls_helper.is_mtls_endpoint(url) is True

    @pytest.mark.parametrize(
        "url",
        [
            "https://storage.googleapis.com",
            "https://storage.googleapis.com.",
            "https://storage.googleapis.com:443/b/my-bucket",
            "https://storage.googleapis.com:443/bucket/mtls.googleapis.com?pageSize=10#frag",
            "https://storage.googleapis.com/bucket/mtls.googleapis.com",
            "https://my-service-xyz-uc.a.run.app",
            "https://my-service-123456.us-central1.run.app",
            "https://my-service-xyz-uc.a.run.app/mtls.run.app",
            "https://fake-mtls.run.app/v1",
            "https://fake-mtls.run.app.attacker.com/v1",
            "https://[2001:db8::1]:443/mtls.googleapis.com",
            "https://[::1]:8443/mtls.googleapis.com",
            "https://logging.googleapis.com/v2/entries?filter=mtls.googleapis.com",
            "https://logging.googleapis.com/v2/entries?filter=mtls.sandbox.googleapis.com",
            "https://logging.googleapis.com/v2/entries?filter=service.p.googleapis.com",
            "https://example.com/mtls.googleapis.com",
            "https://fake-mtls.googleapis.com.attacker.com/v1",
            "https://fake-p.googleapis.com.attacker.com/v1",
            "http://localhost:8080/",
            "http://localhost:8080/mtls.googleapis.com",
            b"https://storage.googleapis.com",
            b"https://storage.googleapis.com/bucket/mtls.googleapis.com",
            b"\xff\xfeinvalid",
            urllib3.util.parse_url("https://storage.googleapis.com/b/my-bucket"),
            urllib3.util.parse_url(
                "https://storage.googleapis.com/bucket/mtls.googleapis.com"
            ),
            "https://.",
            "https://[::1",
            "",
            None,
            123,
            "not a url",
        ],
    )
    def test_is_mtls_endpoint_false(self, url):
        assert _mtls_helper.is_mtls_endpoint(url) is False


class TestReadCredentialBundleFile(object):
    @pytest.mark.parametrize("key_index", [0, 1])
    def test_single_cert_and_key(self, tmpdir, key_index):
        bundle_file = tmpdir.join("x509.credential-bundle.private-key.pem")
        blocks = [pytest.public_cert_bytes]
        blocks.insert(key_index, pytest.private_key_bytes)
        bundle_file.write_binary(b"".join(blocks))

        with mock.patch("builtins.open", wraps=open) as mock_open:
            cert_bytes, key_bytes = _mtls_helper._read_credential_bundle_file(
                str(bundle_file)
            )
        mock_open.assert_called_once_with(str(bundle_file), "rb")
        assert cert_bytes == pytest.public_cert_bytes
        assert key_bytes == pytest.private_key_bytes

    @pytest.mark.parametrize("key_index", [0, 1, 2])
    def test_multi_cert_chain_and_key(self, tmpdir, key_index):
        bundle_file = tmpdir.join("x509.credential-bundle.private-key.pem")
        blocks = [
            pytest.public_cert_bytes.rstrip(b"\n") + b"  \n",
            pytest.public_cert_bytes,
        ]
        blocks.insert(key_index, pytest.private_key_bytes)
        bundle_file.write_binary(b"".join(blocks))

        cert_bytes, key_bytes = _mtls_helper._read_credential_bundle_file(
            str(bundle_file)
        )
        assert cert_bytes == pytest.public_cert_bytes + pytest.public_cert_bytes
        assert key_bytes == pytest.private_key_bytes

    def test_missing_cert_raises_error(self, tmpdir):
        bundle_file = tmpdir.join("key_only.pem")
        bundle_file.write_binary(pytest.private_key_bytes)

        with pytest.raises(exceptions.ClientCertError, match="at least one PEM"):
            _mtls_helper._read_credential_bundle_file(str(bundle_file))

    def test_missing_key_raises_error(self, tmpdir):
        bundle_file = tmpdir.join("cert_only.pem")
        bundle_file.write_binary(pytest.public_cert_bytes)

        with pytest.raises(
            exceptions.ClientCertError, match="a single PEM formatted private key"
        ):
            _mtls_helper._read_credential_bundle_file(str(bundle_file))

    def test_multiple_keys_raises_error(self, tmpdir):
        bundle_file = tmpdir.join("multi_key.pem")
        bundle_file.write_binary(
            pytest.public_cert_bytes
            + pytest.private_key_bytes
            + pytest.private_key_bytes
        )

        with pytest.raises(
            exceptions.ClientCertError, match="a single PEM formatted private key"
        ):
            _mtls_helper._read_credential_bundle_file(str(bundle_file))

    def test_os_error_propagates(self, tmpdir):
        missing_bundle = str(tmpdir.join("nonexistent_rotated_symlink.pem"))
        with pytest.raises(OSError):
            _mtls_helper._read_credential_bundle_file(missing_bundle)


class TestGkeCredentialBundleDiscovery(object):
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
    @mock.patch(
        "google.auth.transport._mtls_helper._read_credential_bundle_file",
        autospec=True,
    )
    def test_get_workload_cert_and_key_gke_fallback(
        self, mock_read_bundle, mock_is_ready, mock_get_config_path
    ):
        mock_read_bundle.return_value = (
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

        cert, key = _mtls_helper._get_workload_cert_and_key()
        assert cert == pytest.public_cert_bytes
        assert key == pytest.private_key_bytes
        mock_is_ready.assert_called_once_with(_mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH)
        mock_read_bundle.assert_called_once_with(
            _mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH
        )

    @mock.patch(
        "google.auth.transport._mtls_helper.path.exists",
        return_value=False,
        autospec=True,
    )
    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=True,
        autospec=True,
    )
    def test_get_workload_cert_and_key_no_gke_fallback_when_explicit_path_set(
        self, mock_is_ready, mock_exists
    ):
        cert, key = _mtls_helper._get_workload_cert_and_key("/missing/config.json")
        assert cert is None
        assert key is None
        mock_exists.assert_called_once_with("/missing/config.json")
        mock_is_ready.assert_not_called()

    @mock.patch(
        "google.auth.transport._mtls_helper.path.exists",
        return_value=False,
        autospec=True,
    )
    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=True,
        autospec=True,
    )
    def test_get_workload_cert_and_key_no_gke_fallback_when_explicit_env_set(
        self, mock_is_ready, mock_exists, monkeypatch
    ):
        monkeypatch.setenv(
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG, "/missing/config.json"
        )
        cert, key = _mtls_helper._get_workload_cert_and_key()
        assert cert is None
        assert key is None
        mock_exists.assert_called_once_with("/missing/config.json")
        mock_is_ready.assert_not_called()

    @pytest.mark.parametrize("include_context_aware", [True, False])
    @mock.patch(
        "google.auth.transport._mtls_helper.path.exists",
        return_value=False,
        autospec=True,
    )
    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=True,
        autospec=True,
    )
    def test_get_workload_cert_and_key_no_gke_fallback_when_context_aware_env_set(
        self, mock_is_ready, mock_exists, include_context_aware, monkeypatch
    ):
        monkeypatch.setenv(
            environment_vars.CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH,
            "/missing/context_aware_config.json",
        )
        cert, key = _mtls_helper._get_workload_cert_and_key(
            include_context_aware=include_context_aware
        )
        assert cert is None
        assert key is None
        assert mock_exists.call_count == 1
        mock_is_ready.assert_not_called()

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
    def test_check_use_client_cert_gke_auto_enabled(
        self, mock_is_ready, mock_get_config_path
    ):
        assert _mtls_helper.check_use_client_cert() is True
        mock_is_ready.assert_called_once_with(_mtls_helper._GKE_CREDENTIAL_BUNDLE_PATH)

    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=True,
        autospec=True,
    )
    def test_check_use_client_cert_gke_disabled_by_env(
        self, mock_is_ready, monkeypatch
    ):
        monkeypatch.setenv(environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE, "false")
        assert _mtls_helper.check_use_client_cert() is False
        mock_is_ready.assert_not_called()

    @mock.patch(
        "google.auth._agent_identity_utils._is_certificate_file_ready",
        return_value=True,
        autospec=True,
    )
    def test_no_gke_fallback_when_implicit_config_has_no_workload(
        self, mock_is_ready, tmpdir, monkeypatch
    ):
        config_file = tmpdir.join("certificate_config.json")
        config_file.write('{"cert_configs": {}}')
        monkeypatch.setattr(
            _mtls_helper._cloud_sdk, "get_config_path", lambda: str(tmpdir)
        )

        assert _mtls_helper._get_workload_cert_and_key() == (None, None)
        assert _mtls_helper.check_use_client_cert() is False
        mock_is_ready.assert_not_called()
