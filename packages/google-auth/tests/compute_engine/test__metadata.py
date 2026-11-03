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

import datetime
import http.client as http_client
import importlib
import json
import os
from unittest import mock

import pytest  # type: ignore
import requests

from google.auth import _helpers, environment_vars, exceptions, transport
from google.auth.compute_engine import _metadata
from google.auth.transport import requests as google_auth_requests

PATH = "instance/service-accounts/default"

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
SMBIOS_PRODUCT_NAME_FILE = os.path.join(DATA_DIR, "smbios_product_name")
SMBIOS_PRODUCT_NAME_NONEXISTENT_FILE = os.path.join(
    DATA_DIR, "smbios_product_name_nonexistent"
)
SMBIOS_PRODUCT_NAME_NON_GOOGLE = os.path.join(
    DATA_DIR, "smbios_product_name_non_google"
)

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

ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE = "gl-python/<python-version> auth/<library-version> auth-request-type/at cred-type/mds"
MDS_PING_METRICS_HEADER_VALUE = (
    "gl-python/<python-version> auth/<library-version> auth-request-type/mds"
)
MDS_PING_REQUEST_HEADER = {
    "metadata-flavor": "Google",
    "x-goog-api-client": MDS_PING_METRICS_HEADER_VALUE,
}


def make_request(data, status=http_client.OK, headers=None, retry=False):
    response = mock.create_autospec(transport.Response, instance=True)
    response.status = status
    response.data = _helpers.to_bytes(data)
    response.headers = headers or {}

    request = mock.create_autospec(transport.Request)
    if retry:
        request.side_effect = [exceptions.TransportError(), response]
    else:
        request.return_value = response

    return request


def test_detect_gce_residency_linux_success():
    _metadata._GCE_PRODUCT_NAME_FILE = SMBIOS_PRODUCT_NAME_FILE
    assert _metadata.detect_gce_residency_linux()


def test_detect_gce_residency_linux_non_google():
    _metadata._GCE_PRODUCT_NAME_FILE = SMBIOS_PRODUCT_NAME_NON_GOOGLE
    assert not _metadata.detect_gce_residency_linux()


def test_detect_gce_residency_linux_nonexistent():
    _metadata._GCE_PRODUCT_NAME_FILE = SMBIOS_PRODUCT_NAME_NONEXISTENT_FILE
    assert not _metadata.detect_gce_residency_linux()


def test_is_on_gce_ping_success():
    request = make_request("", headers=_metadata._METADATA_HEADERS)
    assert _metadata.is_on_gce(request)


def test_is_on_gce_no_gce_check():
    request = make_request("", headers=_metadata._METADATA_HEADERS)

    os.environ[environment_vars.NO_GCE_CHECK] = "true"
    importlib.reload(_metadata)

    try:
        assert not _metadata.is_on_gce(request)
        assert request.call_count == 0
    finally:
        del os.environ[environment_vars.NO_GCE_CHECK]
        importlib.reload(_metadata)


@mock.patch("os.name", new="nt")
def test_is_on_gce_windows_success():
    request = make_request("", headers={_metadata._METADATA_FLAVOR_HEADER: "meep"})
    assert not _metadata.is_on_gce(request)


@mock.patch("os.name", new="posix")
def test_is_on_gce_linux_success():
    request = make_request("", headers={_metadata._METADATA_FLAVOR_HEADER: "meep"})
    _metadata._GCE_PRODUCT_NAME_FILE = SMBIOS_PRODUCT_NAME_FILE
    assert _metadata.is_on_gce(request)


@mock.patch("google.auth.metrics.mds_ping", return_value=MDS_PING_METRICS_HEADER_VALUE)
def test_ping_success(mock_metrics_header_value):
    request = make_request("", headers=_metadata._METADATA_HEADERS)

    assert _metadata.ping(request)

    request.assert_called_once_with(
        method="GET",
        url="http://169.254.169.254",
        headers=MDS_PING_REQUEST_HEADER,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


@mock.patch("google.auth.metrics.mds_ping", return_value=MDS_PING_METRICS_HEADER_VALUE)
def test_ping_success_retry(mock_metrics_header_value):
    request = make_request("", headers=_metadata._METADATA_HEADERS, retry=True)

    assert _metadata.ping(request)

    request.assert_called_with(
        method="GET",
        url="http://169.254.169.254",
        headers=MDS_PING_REQUEST_HEADER,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert request.call_count == 2


@mock.patch("time.sleep", return_value=None)
def test_ping_failure_bad_flavor(mock_sleep):
    request = make_request("", headers={_metadata._METADATA_FLAVOR_HEADER: "meep"})

    assert not _metadata.ping(request)


@mock.patch("time.sleep", return_value=None)
def test_ping_failure_connection_failed(mock_sleep):
    request = make_request("")
    request.side_effect = exceptions.TransportError()

    assert not _metadata.ping(request)


@mock.patch("google.auth.metrics.mds_ping", return_value=MDS_PING_METRICS_HEADER_VALUE)
def test_ping_success_custom_root(mock_metrics_header_value):
    request = make_request("", headers=_metadata._METADATA_HEADERS)

    fake_ip = "1.2.3.4"
    os.environ[environment_vars.GCE_METADATA_IP] = fake_ip
    importlib.reload(_metadata)

    try:
        assert _metadata.ping(request)
    finally:
        del os.environ[environment_vars.GCE_METADATA_IP]
        importlib.reload(_metadata)

    request.assert_called_once_with(
        method="GET",
        url="http://" + fake_ip,
        headers=MDS_PING_REQUEST_HEADER,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


@mock.patch("time.sleep", return_value=None)
@mock.patch("google.auth.metrics.mds_ping", return_value=MDS_PING_METRICS_HEADER_VALUE)
def test_ping_failure_custom_retry(mock_metrics_header_value, _mock_sleep):
    request = make_request("")
    request.side_effect = exceptions.TransportError()

    os.environ[environment_vars.GCE_METADATA_DETECT_RETRIES] = "10"
    importlib.reload(_metadata)

    try:
        _metadata.ping(request)
    finally:
        del os.environ[environment_vars.GCE_METADATA_DETECT_RETRIES]
        importlib.reload(_metadata)

    assert request.call_count == 10


def test_get_success_json():
    key, value = "foo", "bar"

    data = json.dumps({key: value})
    request = make_request(data, headers={"content-type": "application/json"})

    result = _metadata.get(request, PATH)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert result[key] == value


def test_get_success_json_content_type_charset():
    key, value = "foo", "bar"

    data = json.dumps({key: value})
    request = make_request(
        data, headers={"content-type": "application/json; charset=UTF-8"}
    )

    result = _metadata.get(request, PATH)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert result[key] == value


@mock.patch("time.sleep", return_value=None)
def test_get_success_retry(mock_sleep):
    key, value = "foo", "bar"

    data = json.dumps({key: value})
    request = make_request(
        data, headers={"content-type": "application/json"}, retry=True
    )

    result = _metadata.get(request, PATH)

    request.assert_called_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert request.call_count == 2
    assert result[key] == value


def test_get_success_text():
    data = "foobar"
    request = make_request(data, headers={"content-type": "text/plain"})

    result = _metadata.get(request, PATH)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert result == data


def test_get_success_params():
    data = "foobar"
    request = make_request(data, headers={"content-type": "text/plain"})
    params = {"recursive": "true"}

    result = _metadata.get(request, PATH, params=params)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/"
        + PATH
        + "?recursive=true",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert result == data


def test_get_success_recursive_and_params():
    data = "foobar"
    request = make_request(data, headers={"content-type": "text/plain"})
    params = {"recursive": "false"}
    result = _metadata.get(request, PATH, recursive=True, params=params)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/"
        + PATH
        + "?recursive=true",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert result == data


def test_get_success_recursive():
    data = "foobar"
    request = make_request(data, headers={"content-type": "text/plain"})

    result = _metadata.get(request, PATH, recursive=True)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/"
        + PATH
        + "?recursive=true",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert result == data


def test_get_success_custom_root_new_variable():
    request = make_request("{}", headers={"content-type": "application/json"})

    fake_root = "another.metadata.service"
    os.environ[environment_vars.GCE_METADATA_HOST] = fake_root
    importlib.reload(_metadata)

    try:
        _metadata.get(request, PATH)
    finally:
        del os.environ[environment_vars.GCE_METADATA_HOST]
        importlib.reload(_metadata)

    request.assert_called_once_with(
        method="GET",
        url="http://{}/computeMetadata/v1/{}".format(fake_root, PATH),
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


def test_get_success_custom_root_old_variable():
    request = make_request("{}", headers={"content-type": "application/json"})

    fake_root = "another.metadata.service"
    os.environ[environment_vars.GCE_METADATA_ROOT] = fake_root
    importlib.reload(_metadata)

    try:
        _metadata.get(request, PATH)
    finally:
        del os.environ[environment_vars.GCE_METADATA_ROOT]
        importlib.reload(_metadata)

    request.assert_called_once_with(
        method="GET",
        url="http://{}/computeMetadata/v1/{}".format(fake_root, PATH),
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


def test_get_success_custom_root():
    request = make_request("{}", headers={"content-type": "application/json"})

    fake_root = "http://another.metadata.service"

    _metadata.get(request, PATH, root=fake_root)

    request.assert_called_once_with(
        method="GET",
        url="{}/{}".format(fake_root, PATH),
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


@mock.patch("time.sleep", return_value=None)
def test_get_failure(mock_sleep):
    request = make_request("Metadata error", status=http_client.NOT_FOUND)

    with pytest.raises(exceptions.TransportError) as excinfo:
        _metadata.get(request, PATH)

    assert excinfo.match(r"Metadata error")

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


def test_get_return_none_for_not_found_error():
    request = make_request("Metadata error", status=http_client.NOT_FOUND)

    assert _metadata.get(request, PATH, return_none_for_not_found_error=True) is None

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


@mock.patch("time.sleep", return_value=None)
def test_get_failure_connection_failed(mock_sleep):
    request = make_request("")
    request.side_effect = exceptions.TransportError("failure message")

    with pytest.raises(exceptions.TransportError) as excinfo:
        _metadata.get(request, PATH)

    assert excinfo.match(
        r"Compute Engine Metadata server unavailable. Last exception: failure message"
    )

    request.assert_called_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert request.call_count == 5


@mock.patch("time.sleep", return_value=None)
def test_get_too_many_requests_retryable_error_failure(_mock_sleep):
    request = make_request("too many requests", status=http_client.TOO_MANY_REQUESTS)

    with pytest.raises(exceptions.TransportError) as excinfo:
        _metadata.get(request, PATH)

    assert excinfo.match(
        r"Compute Engine Metadata server unavailable. Response status: 429\nResponse details:\ntoo many requests"
    )

    request.assert_called_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert request.call_count == 5


def test_get_failure_bad_json():
    request = make_request("{", headers={"content-type": "application/json"})

    with pytest.raises(exceptions.TransportError) as excinfo:
        _metadata.get(request, PATH)

    assert excinfo.match(r"invalid JSON")

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH,
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


def test_get_body_with_get_method_raises_value_error():
    request = make_request("{}")

    with pytest.raises(
        ValueError, match="Request body cannot be specified with GET method."
    ):
        _metadata.get(request, PATH, method="GET", body=b"some_body")

    request.assert_not_called()


@mock.patch("time.sleep", return_value=None)
def test_get_post_retry_preserves_method_body_and_headers(mock_sleep):
    response_503 = mock.create_autospec(transport.Response, instance=True)
    response_503.status = http_client.SERVICE_UNAVAILABLE
    response_503.data = _helpers.to_bytes("Service Unavailable")
    response_503.headers = {}

    response_ok = mock.create_autospec(transport.Response, instance=True)
    response_ok.status = http_client.OK
    response_ok.data = _helpers.to_bytes(
        json.dumps({"access_token": "bound_token", "expires_in": 3600})
    )
    response_ok.headers = {"content-type": "application/json"}

    request = mock.create_autospec(transport.Request)
    request.side_effect = [
        response_503,
        exceptions.TransportError("transient transport error"),
        response_ok,
    ]

    expected_body = json.dumps({"certificate_chain": "fake_pem_chain"}).encode("utf-8")
    result = _metadata.get(
        request,
        PATH,
        method="POST",
        body=expected_body,
        headers={"Content-Type": "application/json"},
    )

    assert result == {"access_token": "bound_token", "expires_in": 3600}
    assert request.call_count == 3
    for call_args in request.call_args_list:
        _, kwargs = call_args
        assert kwargs["method"] == "POST"
        assert kwargs["body"] == expected_body
        assert kwargs["headers"]["Content-Type"] == "application/json"
        assert kwargs["headers"][_metadata._METADATA_FLAVOR_HEADER] == "Google"


def test_get_project_id():
    project = "example-project"
    request = make_request(project, headers={"content-type": "text/plain"})

    project_id = _metadata.get_project_id(request)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/project/project-id",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert project_id == project


def test_get_universe_domain_success():
    request = make_request(
        "fake_universe_domain", headers={"content-type": "text/plain"}
    )

    universe_domain = _metadata.get_universe_domain(request)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/universe/universe-domain",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert universe_domain == "fake_universe_domain"


def test_get_universe_domain_success_empty_response():
    request = make_request("", headers={"content-type": "text/plain"})

    universe_domain = _metadata.get_universe_domain(request)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/universe/universe-domain",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert universe_domain == "googleapis.com"


def test_get_universe_domain_not_found():
    # Test that if the universe domain endpoint returns 404 error, we should
    # use googleapis.com as the universe domain
    request = make_request("not found", status=http_client.NOT_FOUND)

    universe_domain = _metadata.get_universe_domain(request)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/universe/universe-domain",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert universe_domain == "googleapis.com"


@mock.patch("time.sleep", return_value=None)
def test_get_universe_domain_retryable_error_failure(_mock_sleep):
    # Test that if the universe domain endpoint returns a retryable error
    # we should retry.
    #
    # In this case, the error persists, and we still fail after retrying.
    request = make_request("too many requests", status=http_client.TOO_MANY_REQUESTS)

    with pytest.raises(exceptions.TransportError) as excinfo:
        _metadata.get_universe_domain(request)

    assert excinfo.match(r"Compute Engine Metadata server unavailable")

    request.assert_called_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/universe/universe-domain",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert request.call_count == 5


def test_get_universe_domain_retryable_error_success():
    # Test that if the universe domain endpoint returns a retryable error
    # we should retry.
    #
    # In this case, the error is temporary, and we succeed after retrying.
    request_error = make_request(
        "too many requests", status=http_client.TOO_MANY_REQUESTS
    )
    request_ok = make_request(
        "fake_universe_domain", headers={"content-type": "text/plain"}
    )

    class _RequestErrorOnce:
        """This class forwards the request parameters to `request_error` once.

        All subsequent calls are forwarded to `request_ok`.
        """

        def __init__(self, request_error, request_ok):
            self._request_error = request_error
            self._request_ok = request_ok
            self._call_index = 0

        def request(self, *args, **kwargs):
            if self._call_index == 0:
                self._call_index += 1
                return self._request_error(*args, **kwargs)

            return self._request_ok(*args, **kwargs)

    request = _RequestErrorOnce(request_error, request_ok).request

    universe_domain = _metadata.get_universe_domain(request)

    request_error.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/universe/universe-domain",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    request_ok.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/universe/universe-domain",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )

    assert universe_domain == "fake_universe_domain"


def test_get_universe_domain_other_error():
    # Test that if the universe domain endpoint returns an error other than 404
    # we should throw the error
    request = make_request("unauthorized", status=http_client.UNAUTHORIZED)

    with pytest.raises(exceptions.TransportError) as excinfo:
        _metadata.get_universe_domain(request)

    assert excinfo.match(r"unauthorized")

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/universe/universe-domain",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


@mock.patch(
    "google.auth.metrics.token_request_access_token_mds",
    return_value=ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE,
)
@mock.patch("google.auth._helpers.utcnow", return_value=datetime.datetime.min)
def test_get_service_account_token(utcnow, mock_metrics_header_value):
    ttl = 500
    request = make_request(
        json.dumps({"access_token": "token", "expires_in": ttl}),
        headers={"content-type": "application/json"},
    )

    token, expiry = _metadata.get_service_account_token(request)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/" + PATH + "/token",
        headers={
            "metadata-flavor": "Google",
            "x-goog-api-client": ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE,
        },
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert token == "token"
    assert expiry == utcnow() + datetime.timedelta(seconds=ttl)


@mock.patch(
    "google.auth.metrics.token_request_access_token_mds",
    return_value=ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE,
)
@mock.patch("google.auth._helpers.utcnow", return_value=datetime.datetime.min)
def test_get_service_account_token_with_scopes_list(utcnow, mock_metrics_header_value):
    ttl = 500
    request = make_request(
        json.dumps({"access_token": "token", "expires_in": ttl}),
        headers={"content-type": "application/json"},
    )

    token, expiry = _metadata.get_service_account_token(request, scopes=["foo", "bar"])

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/"
        + PATH
        + "/token"
        + "?scopes=foo%2Cbar",
        headers={
            "metadata-flavor": "Google",
            "x-goog-api-client": ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE,
        },
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert token == "token"
    assert expiry == utcnow() + datetime.timedelta(seconds=ttl)


@mock.patch(
    "google.auth.metrics.token_request_access_token_mds",
    return_value=ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE,
)
@mock.patch("google.auth._helpers.utcnow", return_value=datetime.datetime.min)
def test_get_service_account_token_with_scopes_string(
    utcnow, mock_metrics_header_value
):
    ttl = 500
    request = make_request(
        json.dumps({"access_token": "token", "expires_in": ttl}),
        headers={"content-type": "application/json"},
    )

    token, expiry = _metadata.get_service_account_token(request, scopes="foo,bar")

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/"
        + PATH
        + "/token"
        + "?scopes=foo%2Cbar",
        headers={
            "metadata-flavor": "Google",
            "x-goog-api-client": ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE,
        },
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )
    assert token == "token"
    assert expiry == utcnow() + datetime.timedelta(seconds=ttl)


@mock.patch("google.auth._agent_identity_utils.should_request_bound_token")
@mock.patch(
    "google.auth._agent_identity_utils.get_agent_identity_certificate_and_bytes"
)
@mock.patch(
    "google.auth.metrics.token_request_access_token_mds",
    return_value=ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE,
)
@mock.patch("google.auth._helpers.utcnow", return_value=datetime.datetime.min)
def test_get_service_account_token_with_bound_token(
    utcnow,
    mock_metrics_header_value,
    mock_get_cert_and_bytes,
    mock_should_request,
):
    # Test the successful path where a certificate is found and a bound token
    # is requested.
    mock_cert = mock.sentinel.cert
    mock_cert_bytes = b"fake_cert_bytes"
    mock_get_cert_and_bytes.return_value = (mock_cert, mock_cert_bytes)
    mock_should_request.return_value = True

    token_response = json.dumps({"access_token": "token", "expires_in": 3600})
    request = make_request(token_response, headers={"content-type": "application/json"})

    _metadata.get_service_account_token(request)

    mock_get_cert_and_bytes.assert_called_once()
    mock_should_request.assert_called_once_with(mock_cert)

    request.assert_called_once()
    _, kwargs = request.call_args
    assert kwargs["method"] == "POST"
    assert kwargs["body"] == json.dumps(
        {"certificate_chain": mock_cert_bytes.decode("utf-8")}
    ).encode("utf-8")
    assert kwargs["headers"]["Content-Type"] == "application/json"


@mock.patch(
    "google.auth._agent_identity_utils.get_agent_identity_certificate_and_bytes"
)
def test_get_service_account_token_no_cert(mock_get_cert_and_bytes):
    # Test that a standard GET request without a body is sent when no certificate is found.
    mock_get_cert_and_bytes.return_value = (None, None)
    token_response = json.dumps({"access_token": "token", "expires_in": 3600})
    request = make_request(token_response, headers={"content-type": "application/json"})

    _metadata.get_service_account_token(request)

    request.assert_called_once()
    _, kwargs = request.call_args
    assert kwargs["method"] == "GET"
    assert "body" not in kwargs
    assert "Content-Type" not in kwargs["headers"]


@mock.patch("google.auth._agent_identity_utils.should_request_bound_token")
@mock.patch(
    "google.auth._agent_identity_utils.get_agent_identity_certificate_and_bytes"
)
def test_get_service_account_token_should_not_bind(
    mock_get_cert_and_bytes, mock_should_request
):
    # Test that a standard GET request without a body is sent when a cert is found but should not be used.
    mock_get_cert_and_bytes.return_value = (mock.sentinel.cert, b"fake_cert_bytes")
    mock_should_request.return_value = False
    token_response = json.dumps({"access_token": "token", "expires_in": 3600})
    request = make_request(token_response, headers={"content-type": "application/json"})

    _metadata.get_service_account_token(request)

    request.assert_called_once()
    _, kwargs = request.call_args
    assert kwargs["method"] == "GET"
    assert "body" not in kwargs
    assert "Content-Type" not in kwargs["headers"]


@mock.patch(
    "google.auth._agent_identity_utils.get_agent_identity_certificate_and_bytes"
)
def test__build_token_request_options_unbound(mock_get_cert_and_bytes):
    method, body, headers = _metadata._build_token_request_options(
        ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE, bind_token=False
    )

    mock_get_cert_and_bytes.assert_not_called()
    assert method == "GET"
    assert body is None
    assert headers == {"x-goog-api-client": ACCESS_TOKEN_REQUEST_METRICS_HEADER_VALUE}


def test_get_service_account_info():
    key, value = "foo", "bar"
    request = make_request(
        json.dumps({key: value}), headers={"content-type": "application/json"}
    )

    info = _metadata.get_service_account_info(request)

    request.assert_called_once_with(
        method="GET",
        url="http://metadata.google.internal/computeMetadata/v1/"
        + PATH
        + "/?recursive=true",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )

    assert info[key] == value


def test__get_metadata_root_mtls():
    assert (
        _metadata._get_metadata_root(use_mtls=True)
        == "https://metadata.google.internal/computeMetadata/v1/"
    )


def test__get_metadata_root_no_mtls():
    assert (
        _metadata._get_metadata_root(use_mtls=False)
        == "http://metadata.google.internal/computeMetadata/v1/"
    )


def test__get_metadata_ip_root_mtls():
    assert _metadata._get_metadata_ip_root(use_mtls=True) == "https://169.254.169.254"


def test__get_metadata_ip_root_no_mtls():
    assert _metadata._get_metadata_ip_root(use_mtls=False) == "http://169.254.169.254"


@mock.patch("google.auth.compute_engine._mtls.MdsMtlsAdapter")
def test__prepare_request_for_mds_mtls(mock_mds_mtls_adapter):
    request = google_auth_requests.Request(mock.create_autospec(requests.Session))
    _metadata._prepare_request_for_mds(request, use_mtls=True)
    mock_mds_mtls_adapter.assert_called_once()
    assert request.session.mount.call_count == len(_metadata._GCE_DEFAULT_MDS_HOSTS)


def test__prepare_request_for_mds_no_mtls():
    request = mock.Mock()
    _metadata._prepare_request_for_mds(request, use_mtls=False)
    request.session.mount.assert_not_called()


@mock.patch("google.auth.metrics.mds_ping", return_value=MDS_PING_METRICS_HEADER_VALUE)
@mock.patch("google.auth.compute_engine._mtls.MdsMtlsAdapter")
@mock.patch("google.auth.compute_engine._mtls.should_use_mds_mtls", return_value=True)
@mock.patch("google.auth.transport.requests.Request")
def test_ping_mtls(
    mock_request, mock_should_use_mtls, mock_mds_mtls_adapter, mock_metrics_header_value
):
    response = mock.create_autospec(transport.Response, instance=True)
    response.status = http_client.OK
    response.headers = _metadata._METADATA_HEADERS
    mock_request.return_value = response

    assert _metadata.ping(mock_request)

    mock_should_use_mtls.assert_called_once()
    mock_mds_mtls_adapter.assert_called_once()
    mock_request.assert_called_once_with(
        url="https://169.254.169.254",
        method="GET",
        headers=MDS_PING_REQUEST_HEADER,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


@mock.patch("google.auth.compute_engine._mtls.MdsMtlsAdapter")
@mock.patch("google.auth.compute_engine._mtls.should_use_mds_mtls", return_value=True)
@mock.patch("google.auth.transport.requests.Request")
def test_get_mtls(mock_request, mock_should_use_mtls, mock_mds_mtls_adapter):
    response = mock.create_autospec(transport.Response, instance=True)
    response.status = http_client.OK
    response.data = _helpers.to_bytes("{}")
    response.headers = {"content-type": "application/json"}
    mock_request.return_value = response

    _metadata.get(mock_request, "some/path")

    mock_should_use_mtls.assert_called_once()
    mock_mds_mtls_adapter.assert_called_once()
    mock_request.assert_called_once_with(
        url="https://metadata.google.internal/computeMetadata/v1/some/path",
        method="GET",
        headers=_metadata._METADATA_HEADERS,
        timeout=_metadata._METADATA_DEFAULT_TIMEOUT,
    )


@pytest.mark.parametrize(
    "mds_mode, metadata_host, expect_exception",
    [
        (_metadata._mtls.MdsMtlsMode.STRICT, _metadata._GCE_DEFAULT_HOST, False),
        (_metadata._mtls.MdsMtlsMode.STRICT, _metadata._GCE_DEFAULT_MDS_IP, False),
        (_metadata._mtls.MdsMtlsMode.STRICT, "custom.host", True),
        (_metadata._mtls.MdsMtlsMode.NONE, "custom.host", False),
        (_metadata._mtls.MdsMtlsMode.DEFAULT, _metadata._GCE_DEFAULT_HOST, False),
        (_metadata._mtls.MdsMtlsMode.DEFAULT, _metadata._GCE_DEFAULT_MDS_IP, False),
    ],
)
@mock.patch("google.auth.compute_engine._mtls._parse_mds_mode")
def test_validate_gce_mds_configured_environment(
    mock_parse_mds_mode, mds_mode, metadata_host, expect_exception
):
    mock_parse_mds_mode.return_value = mds_mode
    with mock.patch(
        "google.auth.compute_engine._metadata._GCE_METADATA_HOST", new=metadata_host
    ):
        if expect_exception:
            with pytest.raises(exceptions.MutualTLSChannelError):
                _metadata._validate_gce_mds_configured_environment()
        else:
            _metadata._validate_gce_mds_configured_environment()
    mock_parse_mds_mode.assert_called_once()


@mock.patch("google.auth.compute_engine._mtls.MdsMtlsAdapter")
def test__prepare_request_for_mds_mtls_session_exists(mock_mds_mtls_adapter):
    mock_session = mock.create_autospec(requests.Session)
    request = google_auth_requests.Request(mock_session)
    _metadata._prepare_request_for_mds(request, use_mtls=True)

    mock_mds_mtls_adapter.assert_called_once()
    assert mock_session.mount.call_count == len(_metadata._GCE_DEFAULT_MDS_HOSTS)


@mock.patch("google.auth.compute_engine._mtls.MdsMtlsAdapter")
def test__prepare_request_for_mds_mtls_no_session(mock_mds_mtls_adapter):
    request = google_auth_requests.Request(None)
    # Explicitly set session to None to avoid a session being created in the Request constructor.
    request.session = None

    with mock.patch("requests.Session") as mock_session_class:
        _metadata._prepare_request_for_mds(request, use_mtls=True)

        mock_session_class.assert_called_once()
        mock_mds_mtls_adapter.assert_called_once()
        assert request.session.mount.call_count == len(_metadata._GCE_DEFAULT_MDS_HOSTS)


@mock.patch("google.auth.compute_engine._mtls.MdsMtlsAdapter")
def test__prepare_request_for_mds_mtls_http_request(mock_mds_mtls_adapter):
    """
    http requests should be ignored.
    Regression test for https://github.com/googleapis/google-cloud-python/issues/16035
    """
    from google.auth.transport import _http_client

    request = _http_client.Request()
    _metadata._prepare_request_for_mds(request, use_mtls=True)

    assert mock_mds_mtls_adapter.call_count == 0


def test__is_service_account_email():
    # Valid email formats
    assert (
        _metadata._is_service_account_email("my-sa@my-project.iam.gserviceaccount.com")
        is True
    )
    assert (
        _metadata._is_service_account_email("my-sa@my-project.iam.GSERVICEACCOUNT.COM")
        is True
    )

    # Empty inputs and standard string placeholders
    assert _metadata._is_service_account_email("test@example.com") is False
    assert _metadata._is_service_account_email("default") is False
    assert _metadata._is_service_account_email("") is False
    assert _metadata._is_service_account_email(None) is False

    # Workload identity principal URI formats
    assert (
        _metadata._is_service_account_email(
            "principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-project.svc.id.goog/subject/ns/my-namespace/sa/my-kubernetes-sa"
        )
        is False
    )

    # Workforce or workload pool identifier paths
    assert _metadata._is_service_account_email("my-gcp-project.svc.id.goog") is False
