# Copyright 2016 Google LLC
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

import http.client as http_client
import os
from unittest import mock

import pytest  # type: ignore
import urllib3  # type: ignore

import google.auth.credentials
import google.auth.transport._mtls_helper
import google.auth.transport.urllib3
from google.auth import environment_vars, exceptions
from google.oauth2 import service_account
from tests.transport import compliance

CERT_MOCK_VAL = b"-----BEGIN CERTIFICATE-----\nMIIDIzCCAgugAwIBAgIJAMfISuBQ5m+5MA0GCSqGSIb3DQEBBQUAMBUxEzARBgNV\nBAMTCnVuaXQtdGVzdHMwHhcNMTExMjA2MTYyNjAyWhcNMjExMjAzMTYyNjAyWjAV\nMRMwEQYDVQQDEwp1bml0LXRlc3RzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\nCgKCAQEA4ej0p7bQ7L/r4rVGUz9RN4VQWoej1Bg1mYWIDYslvKrk1gpj7wZgkdmM\n7oVK2OfgrSj/FCTkInKPqaCR0gD7K80q+mLBrN3PUkDrJQZpvRZIff3/xmVU1Wer\nuQLFJjnFb2dqu0s/FY/2kWiJtBCakXvXEOb7zfbINuayL+MSsCGSdVYsSliS5qQp\ngyDap+8b5fpXZVJkq92hrcNtbkg7hCYUJczt8n9hcCTJCfUpApvaFQ18pe+zpyl4\n+WzkP66I28hniMQyUlA1hBiskT7qiouq0m8IOodhv2fagSZKjOTTU2xkSBc//fy3\nZpsL7WqgsZS7Q+0VRK8gKfqkxg5OYQIDAQABo3YwdDAdBgNVHQ4EFgQU2RQ8yO+O\ngN8oVW2SW7RLrfYd9jEwRQYDVR0jBD4wPIAU2RQ8yO+OgN8oVW2SW7RLrfYd9jGh\nGaQXMBUxEzARBgNVBAMTCnVuaXQtdGVzdHOCCQDHyErgUOZvuTAMBgNVHRMEBTAD\nAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQBRv+M/6+FiVu7KXNjFI5pSN17OcW5QUtPr\nodJMlWrJBtynn/TA1oJlYu3yV5clc/71Vr/AxuX5xGP+IXL32YDF9lTUJXG/uUGk\n+JETpKmQviPbRsvzYhz4pf6ZIOZMc3/GIcNq92ECbseGO+yAgyWUVKMmZM0HqXC9\novNslqe0M8C1sLm1zAR5z/h/litE7/8O2ietija3Q/qtl2TOXJdCA6sgjJX2WUql\nybrC55ct18NKf3qhpcEkGQvFU40rVYApJpi98DiZPYFdx1oBDp/f4uZ3ojpxRVFT\ncDwcJLfNRCPUhormsY7fDS9xSyThiHsW9mjJYdcaKQkwYZ0F11yB\n-----END CERTIFICATE-----\n"
KEY_MOCK_VAL = b"-----BEGIN ENCRYPTED PRIVATE KEY-----\nMIHeMEkGCSqGSIb3DQEFDTA8MBsGCSqGSIb3DQEFDDAOBAj9XnJ2h78QVAICCAAw\nHQYJYIZIAWUDBAECBBBeiiOF2LnLzq/wjb/viwMwBIGQk28Zkfj2EIk42bgc7UzC\nSf98qssCVhsIYz0Xa3eSATg8Cpn83YieaBeyxdk/tXTnrOhxMV/vt7T98kWhaGbH\n5Z9CdGVLfes0UFvVJqrlk6vcf2sOnLCGbrn78HS+ayrGOCRSCd/7+dnEiB/7Um1B\nMk6BBJHsLEnZZSHyfrw8jvYgVmcSBy/WdY0pqldD/+4D\n-----END ENCRYPTED PRIVATE KEY-----\n"


class TestRequestResponse(compliance.RequestResponseTests):
    def make_request(self):
        http = urllib3.PoolManager()
        return google.auth.transport.urllib3.Request(http)

    def test_timeout(self):
        http = mock.create_autospec(urllib3.PoolManager)
        request = google.auth.transport.urllib3.Request(http)
        request(url="http://example.com", method="GET", timeout=5)

        assert http.request.call_args[1]["timeout"] == 5


def test__make_default_http_with_certifi():
    http = google.auth.transport.urllib3._make_default_http()
    assert "cert_reqs" in http.connection_pool_kw


@mock.patch.object(google.auth.transport.urllib3, "certifi", new=None)
def test__make_default_http_without_certifi():
    http = google.auth.transport.urllib3._make_default_http()
    assert "cert_reqs" not in http.connection_pool_kw


class CredentialsStub(google.auth.credentials.Credentials):
    def __init__(self, token="token"):
        super(CredentialsStub, self).__init__()
        self.token = token

    def apply(self, headers, token=None):
        headers["authorization"] = self.token

    def before_request(self, request, method, url, headers):
        self.apply(headers)

    def refresh(self, request):
        self.token += "1"

    def with_quota_project(self, quota_project_id):
        raise NotImplementedError()


class HttpStub(object):
    def __init__(self, responses, headers=None):
        self.responses = responses
        self.requests = []
        self.headers = headers or {}

    def urlopen(self, method, url, body=None, headers=None, **kwargs):
        self.requests.append((method, url, body, headers, kwargs))
        return self.responses.pop(0)

    def clear(self):
        pass


class ResponseStub(object):
    def __init__(self, status=http_client.OK, data=None):
        self.status = status
        self.data = data


class TestMakeMutualTlsHttp(object):
    def test_success(self):
        http = google.auth.transport.urllib3._make_mutual_tls_http(
            pytest.public_cert_bytes, pytest.private_key_bytes
        )
        assert isinstance(http, urllib3.PoolManager)

    def test_crypto_error(self):
        with pytest.raises(exceptions.MutualTLSChannelError):
            google.auth.transport.urllib3._make_mutual_tls_http(
                b"invalid cert", b"invalid key"
            )

    @mock.patch("google.auth.transport.urllib3._mtls_helper.secure_cert_key_paths")
    def test_setup_error_raises_mutual_tls_channel_error(self, mock_secure_paths):
        mock_secure_paths.side_effect = OSError("Disk full")
        with pytest.raises(exceptions.MutualTLSChannelError) as exc_info:
            google.auth.transport.urllib3._make_mutual_tls_http(b"cert", b"key")
        assert "Failed to configure client certificate" in str(exc_info.value)
        assert isinstance(exc_info.value.__cause__, OSError)


class TestAuthorizedHttp(object):
    TEST_URL = "http://example.com"

    def test_authed_http_defaults(self):
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            mock.sentinel.credentials
        )

        assert authed_http.credentials == mock.sentinel.credentials
        assert isinstance(authed_http.http, urllib3.PoolManager)

    def test_urlopen_no_refresh(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        response = ResponseStub()
        http = HttpStub([response])

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )

        result = authed_http.urlopen("GET", self.TEST_URL)

        assert result == response
        assert credentials.before_request.called
        assert not credentials.refresh.called
        assert http.requests == [
            ("GET", self.TEST_URL, None, {"authorization": "token"}, {})
        ]

    def test_urlopen_refresh(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        final_response = ResponseStub(status=http_client.OK)
        # First request will 401, second request will succeed.
        http = HttpStub([ResponseStub(status=http_client.UNAUTHORIZED), final_response])

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )

        authed_http = authed_http.urlopen("GET", "http://example.com")

        assert authed_http == final_response
        assert credentials.before_request.call_count == 2
        assert credentials.refresh.called
        assert http.requests == [
            ("GET", self.TEST_URL, None, {"authorization": "token"}, {}),
            ("GET", self.TEST_URL, None, {"authorization": "token1"}, {}),
        ]

    def test_urlopen_no_default_host(self):
        credentials = mock.create_autospec(service_account.Credentials)

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(credentials)

        authed_http.credentials._create_self_signed_jwt.assert_called_once_with(None)

    def test_urlopen_with_default_host(self):
        default_host = "pubsub.googleapis.com"
        credentials = mock.create_autospec(service_account.Credentials)

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, default_host=default_host
        )

        authed_http.credentials._create_self_signed_jwt.assert_called_once_with(
            "https://{}/".format(default_host)
        )

    def test_proxies(self):
        http = mock.create_autospec(urllib3.PoolManager)
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(None, http=http)

        with authed_http:
            pass

        assert http.__enter__.called
        assert http.__exit__.called

        authed_http.headers = mock.sentinel.headers
        assert authed_http.headers == http.headers

    @mock.patch("google.auth.transport.urllib3._make_mutual_tls_http", autospec=True)
    def test_configure_mtls_channel_with_callback(self, mock_make_mutual_tls_http):
        callback = mock.Mock()
        callback.return_value = (pytest.public_cert_bytes, pytest.private_key_bytes)

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock(), http=mock.Mock()
        )

        with pytest.warns(UserWarning):
            with mock.patch.dict(
                os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
            ):
                is_mtls = authed_http.configure_mtls_channel(callback)

        assert is_mtls
        mock_make_mutual_tls_http.assert_called_once_with(
            cert=pytest.public_cert_bytes, key=pytest.private_key_bytes
        )

    @mock.patch("google.auth.transport.urllib3._make_mutual_tls_http", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
    )
    def test_configure_mtls_channel_with_metadata(
        self, mock_get_client_cert_and_key, mock_make_mutual_tls_http
    ):
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock()
        )

        mock_get_client_cert_and_key.return_value = (
            True,
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )
        with mock.patch.dict(
            os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
        ):
            is_mtls = authed_http.configure_mtls_channel()

        assert is_mtls
        mock_get_client_cert_and_key.assert_called_once()
        mock_make_mutual_tls_http.assert_called_once_with(
            cert=pytest.public_cert_bytes, key=pytest.private_key_bytes
        )

    @mock.patch("google.auth.transport.urllib3._make_mutual_tls_http", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
    )
    def test_configure_mtls_channel_closes_old_poolmanager(
        self, mock_get_client_cert_and_key, mock_make_mutual_tls_http
    ):
        mock_get_client_cert_and_key.return_value = (
            True,
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

        old_http = mock.create_autospec(urllib3.PoolManager)
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock(), http=old_http
        )

        with mock.patch.dict(
            os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
        ):
            is_mtls = authed_http.configure_mtls_channel()

        assert is_mtls
        old_http.clear.assert_called_once()
        mock_make_mutual_tls_http.assert_called_once_with(
            cert=pytest.public_cert_bytes, key=pytest.private_key_bytes
        )

    @mock.patch("google.auth.transport.urllib3._make_mutual_tls_http", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
    )
    def test_configure_mtls_channel_with_none_http(
        self, mock_get_client_cert_and_key, mock_make_mutual_tls_http
    ):
        mock_get_client_cert_and_key.return_value = (
            True,
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock()
        )
        authed_http.http = None  # Force old_http to be None

        with mock.patch.dict(
            os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
        ):
            is_mtls = authed_http.configure_mtls_channel()

        assert is_mtls
        mock_make_mutual_tls_http.assert_called_once_with(
            cert=pytest.public_cert_bytes, key=pytest.private_key_bytes
        )

    @mock.patch("google.auth.transport.urllib3._make_mutual_tls_http", autospec=True)
    @mock.patch(
        "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
    )
    def test_configure_mtls_channel_non_mtls(
        self, mock_get_client_cert_and_key, mock_make_mutual_tls_http
    ):
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock()
        )

        mock_get_client_cert_and_key.return_value = (False, None, None)
        with mock.patch.dict(
            os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
        ):
            is_mtls = authed_http.configure_mtls_channel()

        assert not is_mtls
        # If client certificate and key are not found, the transport falls back to
        # a standard connection. _is_mtls must be False to reflect this fallback state.
        assert authed_http._is_mtls is False
        mock_get_client_cert_and_key.assert_called_once()
        mock_make_mutual_tls_http.assert_not_called()

    @mock.patch(
        "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
    )
    def test_configure_mtls_channel_exceptions(self, mock_get_client_cert_and_key):
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock()
        )

        mock_get_client_cert_and_key.side_effect = exceptions.ClientCertError()
        with pytest.raises(exceptions.MutualTLSChannelError):
            with mock.patch.dict(
                os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
            ):
                authed_http.configure_mtls_channel()
        assert authed_http._is_mtls is False

        mock_get_client_cert_and_key.side_effect = OSError("Mock file read error")
        with pytest.raises(exceptions.MutualTLSChannelError):
            with mock.patch.dict(
                os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
            ):
                authed_http.configure_mtls_channel()
        assert authed_http._is_mtls is False

    @mock.patch(
        "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
    )
    @mock.patch(
        "google.auth.transport.urllib3.urllib3.util.ssl_.create_urllib3_context",
        autospec=True,
    )
    def test_configure_mtls_channel_cert_loading_exceptions(
        self, mock_create_urllib3_context, mock_get_client_cert_and_key
    ):
        import ssl

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock()
        )

        mock_get_client_cert_and_key.return_value = (
            True,
            pytest.public_cert_bytes,
            pytest.private_key_bytes,
        )

        for exception_type in [ValueError("error"), ssl.SSLError("error")]:
            mock_ctx = mock.Mock()
            mock_ctx.load_cert_chain.side_effect = exception_type
            mock_create_urllib3_context.return_value = mock_ctx

            with pytest.raises(exceptions.MutualTLSChannelError):
                with mock.patch.dict(
                    os.environ,
                    {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"},
                ):
                    authed_http.configure_mtls_channel()
            assert authed_http._is_mtls is False

            assert not authed_http._is_mtls

    @mock.patch(
        "google.auth.transport._mtls_helper._get_cert_config_path", return_value=None
    )
    @mock.patch(
        "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
    )
    @mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "false",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "false",
            "GOOGLE_API_CERTIFICATE_CONFIG": "",
            "CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH": "",
        },
    )
    def test_configure_mtls_channel_without_client_cert_env(
        self, get_client_cert_and_key, mock_get_cert_config_path
    ):
        callback = mock.Mock()

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock(), http=mock.Mock()
        )

        env_to_patch = {
            environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "",
            environment_vars.CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE: "",
            environment_vars.GOOGLE_API_CERTIFICATE_CONFIG: "",
            environment_vars.CLOUDSDK_CONTEXT_AWARE_CERTIFICATE_CONFIG_FILE_PATH: "",
        }
        with mock.patch.dict(os.environ, env_to_patch):
            # Test the callback is not called if GOOGLE_API_USE_CLIENT_CERTIFICATE is not set.
            is_mtls = authed_http.configure_mtls_channel(callback)
            assert not is_mtls
            callback.assert_not_called()

            # Test ADC client cert is not used if GOOGLE_API_USE_CLIENT_CERTIFICATE is not set.
            is_mtls = authed_http.configure_mtls_channel(callback)
            assert not is_mtls
            get_client_cert_and_key.assert_not_called()

    def test_clear_pool_on_del(self):
        http = mock.create_autospec(urllib3.PoolManager)
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            mock.sentinel.credentials, http=http
        )
        authed_http.__del__()
        http.clear.assert_called_with()

        authed_http.http = None
        authed_http.__del__()
        # Expect it to not crash

    @mock.patch("google.auth.transport.urllib3._make_mutual_tls_http", autospec=True)
    @mock.patch("google.auth.transport.urllib3._make_default_http", autospec=True)
    def test_cert_rotation_when_cert_mismatch_and_mtls_endpoint_used(
        self, mock_make_default_http, mock_make_mutual_tls_http
    ):
        credentials = mock.Mock(wraps=CredentialsStub())
        final_response = ResponseStub(status=http_client.OK)

        # We simulate the HTTP stub rotation. When mTLS http is created, we return rotated_http.
        rotated_http = HttpStub([final_response])
        mock_make_mutual_tls_http.return_value = rotated_http

        http = HttpStub([ResponseStub(status=http_client.UNAUTHORIZED)])

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )

        old_cert = b"-----BEGIN CERTIFICATE-----\nMIIBdTCCARqgAwIBAgIJAOYVvu/axMxvMAoGCCqGSM49BAMCMCcxJTAjBgNVBAMM\nHEdvb2dsZSBFbmRwb2ludCBWZXJpZmljYXRpb24wHhcNMjUwNzMwMjMwNjA4WhcN\nMjYwNzMxMjMwNjA4WjAnMSUwIwYDVQQDDBxHb29nbGUgRW5kcG9pbnQgVmVyaWZp\nY2F0aW9uMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEbtr18gkEtwPow2oqyZsU\n4KLwFaLFlRlYv55UATS3QTDykDnIufC42TJCnqFRYhwicwpE2jnUV+l9g3Voias8\nraMvMC0wCQYDVR0TBAIwADALBgNVHQ8EBAMCB4AwEwYDVR0lBAwwCgYIKwYBBQUH\nAwIwCgYIKoZIzj0EAwIDSQAwRgIhAKcjW6dmF1YCksXPgDPlPu/nSnOjb3qCcivz\n/Jxq2zoeAiEA7/aNxcEoCGS3hwMIXoaaD/vPcZOOopKSyqXCvxRooKQ=\n-----END CERTIFICATE-----\n"

        # New certificate and key to simulate rotation.
        new_cert = pytest.public_cert_bytes
        new_key = pytest.private_key_bytes
        # Set _cached_cert to a callable that returns the old certificate.
        authed_http._cached_cert = old_cert
        authed_http._is_mtls = True
        # Mock call_client_cert_callback to return the new certificate.
        with mock.patch.object(
            google.auth.transport._mtls_helper,
            "call_client_cert_callback",
            return_value=(new_cert, new_key),
        ) as mock_callback:
            # mTLS endpoint is used, and client cert env var is true
            with mock.patch.dict(
                os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
            ):
                result = authed_http.urlopen(
                    "GET", "http://example.mtls.googleapis.com"
                )

        # Asserts to verify the behavior.
        assert result == final_response
        assert credentials.refresh.called
        assert credentials.refresh.call_count == 1
        assert mock_callback.called
        mock_make_mutual_tls_http.assert_called_once_with(cert=new_cert, key=new_key)

    def test_no_cert_rotation_when_cert_match_and_mtls_endpoint_used(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        final_response = ResponseStub(status=http_client.UNAUTHORIZED)
        http = HttpStub(
            [
                ResponseStub(status=http_client.UNAUTHORIZED),
                ResponseStub(status=http_client.UNAUTHORIZED),
                ResponseStub(status=http_client.UNAUTHORIZED),
            ]
        )
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )
        old_cert = CERT_MOCK_VAL

        new_cert = old_cert
        new_key = KEY_MOCK_VAL
        # Set _cached_cert to a callable that returns the same certificate.
        authed_http._cached_cert = old_cert
        authed_http._is_mtls = True
        # Mock call_client_cert_callback to return the certificate.
        with mock.patch.object(
            google.auth.transport._mtls_helper,
            "call_client_cert_callback",
            return_value=(new_cert, new_key),
        ):
            # mTLS endpoint is used
            result = authed_http.urlopen("GET", "http://example.mtls.googleapis.com")

        # Asserts to verify the behavior.
        assert credentials.refresh.call_count == 2
        assert result.status == final_response.status

    def test_no_cert_match_check_when_mtls_endpoint_not_used(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        final_response = ResponseStub(status=http_client.UNAUTHORIZED)
        http = HttpStub(
            [
                ResponseStub(status=http_client.UNAUTHORIZED),
                ResponseStub(status=http_client.UNAUTHORIZED),
                ResponseStub(status=http_client.UNAUTHORIZED),
            ]
        )
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )
        authed_http._is_mtls = False
        new_cert = CERT_MOCK_VAL
        new_key = KEY_MOCK_VAL

        # Mock call_client_cert_callback to return the certificate.
        with mock.patch.object(
            google.auth.transport._mtls_helper,
            "call_client_cert_callback",
            return_value=(new_cert, new_key),
        ) as mock_callback:
            # non-mTLS endpoint is used
            result = authed_http.urlopen("GET", "http://example.googleapis.com")

        # Asserts to verify the behavior.
        assert not mock_callback.called
        assert result.status == final_response.status

    def test_no_cert_rotation_when_no_unauthorized_response(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        final_response = ResponseStub(status=http_client.UPGRADE_REQUIRED)

        # Response is set to code other than 401(Unauthorized).
        http = HttpStub([ResponseStub(status=http_client.UPGRADE_REQUIRED)])
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )
        authed_http._is_mtls = True
        with mock.patch.dict(
            os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
        ):
            # mTLS endpoint is used
            result = authed_http.urlopen("GET", "http://example.mtls.googleapis.com")
        assert result.status == final_response.status
        assert not credentials.refresh.called
        assert credentials.refresh.call_count == 0

    def test_cert_rotation_failure_raises_error(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        http = HttpStub([ResponseStub(status=http_client.UNAUTHORIZED)])

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )

        old_cert = b"-----BEGIN CERTIFICATE-----\nMIIBdTCCARqgAwIBAgIJAOYVvu/axMxvMAoGCCqGSM49BAMCMCcxJTAjBgNVBAMM\nHEdvb2dsZSBFbmRwb2ludCBWZXJpZmljYXRpb24wHhcNMjUwNzMwMjMwNjA4WhcN\nMjYwNzMxMjMwNjA4WjAnMSUwIwYDVQQDDBxHb29nbGUgRW5kcG9pbnQgVmVyaWZp\nY2F0aW9uMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEbtr18gkEtwPow2oqyZsU\n4KLwFaLFlRlYv55UATS3QTDykDnIufC42TJCnqFRYhwicwpE2jnUV+l9g3Voias8\nraMvMC0wCQYDVR0TBAIwADALBgNVHQ8EBAMCB4AwEwYDVR0lBAwwCgYIKwYBBQUH\nAwIwCgYIKoZIzj0EAwIDSQAwRgIhAKcjW6dmF1YCksXPgDPlPu/nSnOjb3qCcivz\n/Jxq2zoeAiEA7/aNxcEoCGS3hwMIXoaaD/vPcZOOopKSyqXCvxRooKQ=\n-----END CERTIFICATE-----\n"

        # New certificate and key to simulate rotation.
        new_cert = CERT_MOCK_VAL
        new_key = KEY_MOCK_VAL
        authed_http._cached_cert = old_cert
        authed_http._is_mtls = True

        # Mock call_client_cert_callback to return the new certificate.
        with mock.patch.object(
            google.auth.transport._mtls_helper,
            "check_parameters_for_unauthorized_response",
            return_value=(new_cert, new_key, "old_fingerprint", "new_fingerprint"),
        ) as mock_check_params:
            with mock.patch.object(
                authed_http,
                "configure_mtls_channel",
                side_effect=Exception("Failed to reconfigure"),
            ) as mock_reconfigure:
                with pytest.raises(exceptions.MutualTLSChannelError):
                    authed_http.urlopen("GET", "https://example.mtls.googleapis.com")

                mock_check_params.assert_called_once()
                mock_reconfigure.assert_called_once()
                credentials.refresh.assert_not_called()

    def test_cert_rotation_check_params_fails(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        http = HttpStub([ResponseStub(status=http_client.UNAUTHORIZED)])

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )
        authed_http._is_mtls = True
        authed_http._cached_cert = b"cached_cert"

        with mock.patch(
            "google.auth.transport.urllib3._mtls_helper.check_parameters_for_unauthorized_response",
            side_effect=Exception("check_params failed"),
        ) as mock_check_params:
            with pytest.raises(Exception, match="check_params failed"):
                authed_http.urlopen("GET", "http://example.mtls.googleapis.com")

            mock_check_params.assert_called_once()
            credentials.refresh.assert_not_called()

    def test_cert_rotation_logic_skipped_on_other_refresh_status_codes(self):
        """
        Tests that the code can handle a refresh triggered by a status code
        other than 401 (UNAUTHORIZED). This covers the 'else' branch of the
        'if response.status_code == http_client.UNAUTHORIZED' check
        """
        credentials = mock.Mock(wraps=CredentialsStub())
        # Configure the session to treat 503 (Service Unavailable) as a refreshable error
        custom_codes = [http_client.SERVICE_UNAVAILABLE]

        # Return 503 first, then 200
        http = HttpStub(
            [
                ResponseStub(status=http_client.SERVICE_UNAVAILABLE),
                ResponseStub(status=http_client.OK),
            ]
        )

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http, refresh_status_codes=custom_codes
        )

        # Enable mTLS to prove it is skipped despite being enabled
        authed_http._is_mtls = True
        mtls_url = "https://mtls.googleapis.com/test"

        with mock.patch(
            "google.auth.transport.urllib3._mtls_helper", autospec=True
        ) as mock_helper:
            authed_http.urlopen("GET", mtls_url)

            # Assert refresh happened (Outer Check was True)
            assert credentials.refresh.called

            # Assert mTLS check logic was SKIPPED (Inner Check was False)
            assert not mock_helper.check_parameters_for_unauthorized_response.called

    @pytest.mark.parametrize(
        "non_mtls_url",
        [
            "https://storage.googleapis.com/bucket/mtls.googleapis.com",
            "https://my-service-xyz-uc.a.run.app/mtls.run.app",
        ],
    )
    def test_cert_rotation_skipped_on_non_mtls_url(self, non_mtls_url):
        """
        Tests that mTLS cert rotation is skipped on non-mTLS URLs even if
        mTLS is enabled and an UNAUTHORIZED (401) response is received.
        """
        credentials = mock.Mock(wraps=CredentialsStub())
        http = HttpStub(
            [
                ResponseStub(status=http_client.UNAUTHORIZED),
                ResponseStub(status=http_client.OK),
            ]
        )
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )
        authed_http._is_mtls = True
        authed_http._cached_cert = b"cached_cert"

        with mock.patch.object(
            google.auth.transport._mtls_helper,
            "check_parameters_for_unauthorized_response",
        ) as mock_check_params:
            authed_http.urlopen("GET", non_mtls_url)

            # Assert refresh happened
            assert credentials.refresh.called

            # Assert mTLS check logic was SKIPPED
            assert not mock_check_params.called

    @pytest.mark.parametrize(
        "mtls_url",
        [
            "https://storage.p.googleapis.com/b/my-bucket",
            "https://my-service-123456.us-central1.mtls.run.app/v1",
        ],
    )
    def test_cert_rotation_triggered_on_mtls_url(self, mtls_url):
        """
        Tests that mTLS cert rotation IS triggered on Private Service Connect
        (PSC) and Cloud Run mTLS endpoints when an UNAUTHORIZED (401) response
        is received.
        """
        credentials = mock.Mock(wraps=CredentialsStub())
        http = HttpStub(
            [
                ResponseStub(status=http_client.UNAUTHORIZED),
                ResponseStub(status=http_client.OK),
            ]
        )
        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials, http=http
        )
        authed_http._is_mtls = True
        authed_http._cached_cert = b"cached_cert"

        with mock.patch.object(
            google.auth.transport._mtls_helper,
            "check_parameters_for_unauthorized_response",
            return_value=(b"new_cert", b"new_key", "old_fp", "old_fp"),
        ) as mock_check_params:
            authed_http.urlopen("GET", mtls_url)

            # Assert mTLS check logic was called on PSC / Cloud Run mTLS endpoint
            mock_check_params.assert_called_once()
            assert credentials.refresh.called

    @mock.patch("google.auth.transport.urllib3._make_mutual_tls_http", autospec=True)
    def test_configure_mtls_channel_subsequent_failure(self, mock_make_mutual_tls_http):
        callback = mock.Mock()
        callback.return_value = (pytest.public_cert_bytes, pytest.private_key_bytes)

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock()
        )

        with mock.patch.dict(
            os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
        ):
            is_mtls = authed_http.configure_mtls_channel(callback)

        assert is_mtls
        assert authed_http._is_mtls

        # Subsequent call fails
        with mock.patch(
            "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
        ) as mock_get_client_cert_and_key:
            mock_get_client_cert_and_key.side_effect = exceptions.ClientCertError()

            with pytest.raises(exceptions.MutualTLSChannelError):
                with mock.patch.dict(
                    os.environ,
                    {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"},
                ):
                    authed_http.configure_mtls_channel()

        # Verify it retains its previous mTLS state and connection pool
        assert authed_http._is_mtls
        assert isinstance(authed_http.http, mock.Mock)

    @mock.patch("google.auth.transport.urllib3._make_mutual_tls_http", autospec=True)
    def test_configure_mtls_channel_subsequent_disabled(
        self, mock_make_mutual_tls_http
    ):
        callback = mock.Mock()
        callback.return_value = (pytest.public_cert_bytes, pytest.private_key_bytes)

        authed_http = google.auth.transport.urllib3.AuthorizedHttp(
            credentials=mock.Mock()
        )

        with mock.patch.dict(
            os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
        ):
            is_mtls = authed_http.configure_mtls_channel(callback)

        assert is_mtls
        assert authed_http._is_mtls

        # Subsequent call returns no client certificate (disabled)
        with mock.patch(
            "google.auth.transport._mtls_helper.get_client_cert_and_key", autospec=True
        ) as mock_get_client_cert_and_key:
            mock_get_client_cert_and_key.return_value = (False, None, None)

            with mock.patch.dict(
                os.environ, {environment_vars.GOOGLE_API_USE_CLIENT_CERTIFICATE: "true"}
            ):
                is_mtls = authed_http.configure_mtls_channel()

        # Verify mTLS is disabled and standard PoolManager is restored
        assert not is_mtls
        assert not authed_http._is_mtls
        assert isinstance(authed_http.http, urllib3.PoolManager)
