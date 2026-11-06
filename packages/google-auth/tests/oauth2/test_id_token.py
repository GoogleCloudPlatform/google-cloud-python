# Copyright 2014 Google Inc.
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
import json
import os
import warnings
from unittest import mock

import pytest  # type: ignore

from google.auth import (
    _helpers,
    crypt,
    environment_vars,
    exceptions,
    impersonated_credentials,
    jwt,
    transport,
)
from google.oauth2 import id_token, service_account

PRIVATE_KEY_FILE = os.path.join(os.path.dirname(__file__), "../data/privatekey.pem")

PUBLIC_CERT_FILE = os.path.join(os.path.dirname(__file__), "../data/public_cert.pem")

SERVICE_ACCOUNT_FILE = os.path.join(
    os.path.dirname(__file__), "../data/service_account.json"
)

IMPERSONATED_SERVICE_ACCOUNT_FILE = os.path.join(
    os.path.dirname(__file__),
    "../data/impersonated_service_account_authorized_user_source.json",
)

ID_TOKEN_AUDIENCE = "https://pubsub.googleapis.com"


def make_request(status, data=None):
    response = mock.create_autospec(transport.Response, instance=True)
    response.status = status

    if data is not None:
        response.data = json.dumps(data).encode("utf-8")

    request = mock.create_autospec(transport.Request)
    request.return_value = response
    return request


def test__fetch_certs_success():
    certs = {"1": "cert"}
    request = make_request(200, certs)

    returned_certs = id_token._fetch_certs(request, mock.sentinel.cert_url)

    request.assert_called_once_with(mock.sentinel.cert_url, method="GET")
    assert returned_certs == certs


def test__fetch_certs_failure():
    request = make_request(404)

    with pytest.raises(exceptions.TransportError):
        id_token._fetch_certs(request, mock.sentinel.cert_url)

    request.assert_called_once_with(mock.sentinel.cert_url, method="GET")


@mock.patch("google.auth.jwt.decode", autospec=True)
@mock.patch("google.oauth2.id_token._fetch_certs", autospec=True)
def test_verify_token(_fetch_certs, decode):
    result = id_token.verify_token(mock.sentinel.token, mock.sentinel.request)

    assert result == decode.return_value
    _fetch_certs.assert_called_once_with(
        mock.sentinel.request, id_token._GOOGLE_OAUTH2_CERTS_URL
    )
    decode.assert_called_once_with(
        mock.sentinel.token,
        certs=_fetch_certs.return_value,
        audience=None,
        clock_skew_in_seconds=0,
    )


@mock.patch("google.oauth2.id_token._fetch_certs", autospec=True)
@mock.patch("jwt.api_jwk.PyJWKSet", autospec=True)
@mock.patch("jwt.get_unverified_header", autospec=True)
@mock.patch("jwt.decode", autospec=True)
def test_verify_token_jwk(decode, get_unverified_header, py_jwk_set, _fetch_certs):
    certs_url = "abc123"
    data = {"keys": [{"alg": "RS256"}]}
    _fetch_certs.return_value = data
    get_unverified_header.return_value = {"kid": "mock-kid"}

    mock_key = mock.MagicMock()
    mock_key.key_id = "mock-kid"
    mock_key.public_key_use = "sig"
    mock_key.key = mock.sentinel.key
    mock_key.algorithm_name = "mock-alg"
    py_jwk_set.from_dict.return_value.keys = [mock_key]
    result = id_token.verify_token(
        mock.sentinel.token, mock.sentinel.request, certs_url=certs_url
    )
    assert result == decode.return_value
    py_jwk_set.from_dict.assert_called_once_with(data)
    get_unverified_header.assert_called_once_with(mock.sentinel.token)

    _fetch_certs.assert_called_once_with(mock.sentinel.request, certs_url)
    decode.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.key,
        algorithms=["mock-alg"],
        audience=None,
    )


@mock.patch("google.oauth2.id_token._fetch_certs", autospec=True)
@mock.patch("jwt.api_jwk.PyJWKSet", autospec=True)
@mock.patch("jwt.get_unverified_header", autospec=True)
@mock.patch("jwt.decode", autospec=True)
def test_verify_token_jwk_missing_kid(
    decode, get_unverified_header, py_jwk_set, _fetch_certs
):
    from jwt.exceptions import PyJWKClientError

    certs_url = "abc123"
    data = {"keys": [{"alg": "RS256"}]}
    _fetch_certs.return_value = data
    get_unverified_header.return_value = {"kid": "mock-kid"}

    mock_key = mock.MagicMock()
    mock_key.key_id = "different-kid"
    mock_key.public_key_use = "sig"
    mock_key.key = mock.sentinel.key
    mock_key.algorithm_name = "mock-alg"
    py_jwk_set.from_dict.return_value.keys = [mock_key]

    with pytest.raises(
        PyJWKClientError, match='Unable to find a signing key that matches: "mock-kid"'
    ):
        id_token.verify_token(
            mock.sentinel.token, mock.sentinel.request, certs_url=certs_url
        )


@mock.patch("google.auth.jwt.decode", autospec=True)
@mock.patch("google.oauth2.id_token._fetch_certs", autospec=True)
def test_verify_token_args(_fetch_certs, decode):
    result = id_token.verify_token(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        certs_url=mock.sentinel.certs_url,
    )

    assert result == decode.return_value
    _fetch_certs.assert_called_once_with(mock.sentinel.request, mock.sentinel.certs_url)
    decode.assert_called_once_with(
        mock.sentinel.token,
        certs=_fetch_certs.return_value,
        audience=mock.sentinel.audience,
        clock_skew_in_seconds=0,
    )


@mock.patch("google.auth.jwt.decode", autospec=True)
@mock.patch("google.oauth2.id_token._fetch_certs", autospec=True)
def test_verify_token_clock_skew(_fetch_certs, decode):
    result = id_token.verify_token(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        certs_url=mock.sentinel.certs_url,
        clock_skew_in_seconds=10,
    )

    assert result == decode.return_value
    _fetch_certs.assert_called_once_with(mock.sentinel.request, mock.sentinel.certs_url)
    decode.assert_called_once_with(
        mock.sentinel.token,
        certs=_fetch_certs.return_value,
        audience=mock.sentinel.audience,
        clock_skew_in_seconds=10,
    )


@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_oauth2_token(verify_token):
    verify_token.return_value = {"iss": "accounts.google.com"}
    result = id_token.verify_oauth2_token(
        mock.sentinel.token, mock.sentinel.request, audience=mock.sentinel.audience
    )

    assert result == verify_token.return_value
    verify_token.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        certs_url=id_token._GOOGLE_OAUTH2_CERTS_URL,
        clock_skew_in_seconds=0,
    )


@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_oauth2_token_clock_skew(verify_token):
    verify_token.return_value = {"iss": "accounts.google.com"}
    result = id_token.verify_oauth2_token(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        clock_skew_in_seconds=10,
    )

    assert result == verify_token.return_value
    verify_token.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        certs_url=id_token._GOOGLE_OAUTH2_CERTS_URL,
        clock_skew_in_seconds=10,
    )


@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_oauth2_token_invalid_iss(verify_token):
    verify_token.return_value = {"iss": "invalid_issuer"}

    with pytest.raises(exceptions.GoogleAuthError):
        id_token.verify_oauth2_token(
            mock.sentinel.token, mock.sentinel.request, audience=mock.sentinel.audience
        )


@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_firebase_token(verify_token):
    verify_token.return_value = {
        "aud": "my-project-id",
        "iss": "https://securetoken.google.com/my-project-id",
        "sub": "my-user-id",
    }
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        result = id_token.verify_firebase_token(
            mock.sentinel.token, mock.sentinel.request, audience=mock.sentinel.audience
        )

    assert result == verify_token.return_value
    verify_token.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        certs_url=id_token._GOOGLE_APIS_CERTS_URL,
        clock_skew_in_seconds=0,
    )


@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_firebase_token_clock_skew(verify_token):
    verify_token.return_value = {
        "aud": "my-project-id",
        "iss": "https://securetoken.google.com/my-project-id",
        "sub": "my-user-id",
    }
    result = id_token.verify_firebase_token(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        clock_skew_in_seconds=10,
    )

    assert result == verify_token.return_value
    verify_token.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        certs_url=id_token._GOOGLE_APIS_CERTS_URL,
        clock_skew_in_seconds=10,
    )


@pytest.mark.parametrize(
    "invalid_payload",
    [
        {"aud": "my-project-id"},
        {
            "aud": "my-project-id",
            "iss": "https://securetoken.google.com/other-project-id",
        },
    ],
)
@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_firebase_token_invalid_iss(verify_token, invalid_payload):
    verify_token.return_value = invalid_payload

    with pytest.raises(exceptions.InvalidValue, match="Wrong issuer"):
        id_token.verify_firebase_token(
            mock.sentinel.token,
            mock.sentinel.request,
            audience=mock.sentinel.audience,
        )


@pytest.mark.parametrize(
    "invalid_payload",
    [
        {"iss": "https://securetoken.google.com/"},
        {"aud": "", "iss": "https://securetoken.google.com/"},
        {
            "aud": ["my-project-id"],
            "iss": "https://securetoken.google.com/my-project-id",
        },
    ],
)
@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_firebase_token_missing_aud(verify_token, invalid_payload):
    verify_token.return_value = invalid_payload

    with pytest.raises(
        exceptions.InvalidValue, match="Token does not contain a valid 'aud' claim"
    ):
        id_token.verify_firebase_token(
            mock.sentinel.token,
            mock.sentinel.request,
            audience=mock.sentinel.audience,
        )


@pytest.mark.parametrize(
    "invalid_payload",
    [
        {
            "aud": "my-project-id",
            "iss": "https://securetoken.google.com/my-project-id",
        },
        {
            "aud": "my-project-id",
            "iss": "https://securetoken.google.com/my-project-id",
            "sub": "",
        },
        {
            "aud": "my-project-id",
            "iss": "https://securetoken.google.com/my-project-id",
            "sub": 123,
        },
    ],
)
@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_firebase_token_invalid_sub(verify_token, invalid_payload):
    verify_token.return_value = invalid_payload

    with pytest.raises(
        exceptions.InvalidValue, match="Token does not contain a valid 'sub' claim"
    ):
        id_token.verify_firebase_token(
            mock.sentinel.token,
            mock.sentinel.request,
            audience=mock.sentinel.audience,
        )


@pytest.mark.parametrize("audience", [None, "", []])
@mock.patch("google.oauth2.id_token.verify_token", autospec=True)
def test_verify_firebase_token_warns_without_audience(verify_token, audience):
    verify_token.return_value = {
        "aud": "my-project-id",
        "iss": "https://securetoken.google.com/my-project-id",
        "sub": "my-user-id",
    }

    with pytest.warns(
        UserWarning,
        match=(
            "Calling verify_firebase_token without an 'audience' leaves the "
            "token's audience claim unverified"
        ),
    ) as record:
        result = id_token.verify_firebase_token(
            mock.sentinel.token, mock.sentinel.request, audience=audience
        )

    assert len(record) == 1
    assert record[0].filename == __file__
    assert result == verify_token.return_value
    verify_token.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=audience,
        certs_url=id_token._GOOGLE_APIS_CERTS_URL,
        clock_skew_in_seconds=0,
    )


@pytest.mark.parametrize("alg", ["ES256", "ES384"])
def test_verify_firebase_token_mismatched_alg_for_rsa_certs(alg):
    with open(PUBLIC_CERT_FILE, "r") as fh:
        public_cert = fh.read()
    request = make_request(200, {"1": public_cert})
    header = base64.urlsafe_b64encode(
        json.dumps({"alg": alg, "kid": "1", "typ": "JWT"}).encode("utf-8")
    )
    payload = base64.urlsafe_b64encode(
        json.dumps(
            {
                "aud": "my-project-id",
                "iss": "https://securetoken.google.com/my-project-id",
                "sub": "my-user-id",
            }
        ).encode("utf-8")
    )
    sig = base64.urlsafe_b64encode(b"sig")
    token = b".".join([header, payload, sig])

    with pytest.raises(
        exceptions.InvalidValue,
        match="Certificate key type does not match signature algorithm {}".format(alg),
    ):
        id_token.verify_firebase_token(token, request, audience="my-project-id")


def test_verify_firebase_token_end_to_end():
    with open(PRIVATE_KEY_FILE, "rb") as fh:
        private_key = fh.read()
    with open(PUBLIC_CERT_FILE, "r") as fh:
        public_cert = fh.read()

    signer = crypt.RSASigner.from_string(private_key, "1")
    now = _helpers.datetime_to_secs(_helpers.utcnow())

    valid_payload = {
        "aud": "my-project-id",
        "iss": "https://securetoken.google.com/my-project-id",
        "sub": "my-user-id",
        "iat": now,
        "exp": now + 300,
    }
    valid_token = jwt.encode(signer, valid_payload)
    request = make_request(200, {"1": public_cert})

    result = id_token.verify_firebase_token(
        valid_token, request, audience="my-project-id"
    )
    assert result == valid_payload

    cross_tenant_token = jwt.encode(
        signer,
        {
            "aud": "other-project-id",
            "iss": "https://securetoken.google.com/other-project-id",
            "sub": "my-user-id",
            "iat": now,
            "exp": now + 300,
        },
    )
    request = make_request(200, {"1": public_cert})
    with pytest.raises(exceptions.InvalidValue, match="Token has wrong audience"):
        id_token.verify_firebase_token(
            cross_tenant_token, request, audience="my-project-id"
        )


def test_fetch_id_token_credentials_optional_request(monkeypatch):
    monkeypatch.delenv(environment_vars.CREDENTIALS, raising=False)

    # Test a request object is created if not provided
    with mock.patch("google.auth.compute_engine._metadata.ping", return_value=True):
        with mock.patch(
            "google.auth.compute_engine.IDTokenCredentials.__init__", return_value=None
        ):
            with mock.patch(
                "google.auth.transport.requests.Request.__init__", return_value=None
            ) as mock_request:
                id_token.fetch_id_token_credentials(ID_TOKEN_AUDIENCE)
            mock_request.assert_called()


@pytest.mark.parametrize(
    "call_kwargs,expected_bind_id_token",
    [
        ({}, None),
        ({"bind_id_token": None}, None),
        ({"bind_id_token": True}, True),
        ({"bind_id_token": False}, False),
    ],
)
def test_fetch_id_token_credentials_from_metadata_server(
    monkeypatch, call_kwargs, expected_bind_id_token
):
    monkeypatch.delenv(environment_vars.CREDENTIALS, raising=False)

    mock_req = mock.Mock()

    with mock.patch("google.auth.compute_engine._metadata.ping", return_value=True):
        with mock.patch(
            "google.auth.compute_engine.IDTokenCredentials.__init__", return_value=None
        ) as mock_init:
            id_token.fetch_id_token_credentials(
                ID_TOKEN_AUDIENCE, request=mock_req, **call_kwargs
            )
        mock_init.assert_called_once_with(
            mock_req,
            ID_TOKEN_AUDIENCE,
            use_metadata_identity_endpoint=True,
            bind_id_token=expected_bind_id_token,
        )


@pytest.mark.parametrize("bind_id_token", [None, True, False])
def test_fetch_id_token_credentials_from_explicit_cred_json_file(
    monkeypatch, bind_id_token
):
    monkeypatch.setenv(environment_vars.CREDENTIALS, SERVICE_ACCOUNT_FILE)

    cred = id_token.fetch_id_token_credentials(
        ID_TOKEN_AUDIENCE, bind_id_token=bind_id_token
    )
    assert isinstance(cred, service_account.IDTokenCredentials)
    assert cred._target_audience == ID_TOKEN_AUDIENCE


@pytest.mark.parametrize("bind_id_token", [None, True, False])
def test_fetch_id_token_credentials_from_impersonated_cred_json_file(
    monkeypatch, bind_id_token
):
    monkeypatch.setenv(environment_vars.CREDENTIALS, IMPERSONATED_SERVICE_ACCOUNT_FILE)

    cred = id_token.fetch_id_token_credentials(
        ID_TOKEN_AUDIENCE, bind_id_token=bind_id_token
    )
    assert isinstance(cred, impersonated_credentials.IDTokenCredentials)
    assert cred._target_audience == ID_TOKEN_AUDIENCE


def test_fetch_id_token_credentials_no_cred_exists(monkeypatch):
    monkeypatch.delenv(environment_vars.CREDENTIALS, raising=False)

    with mock.patch(
        "google.auth.compute_engine._metadata.ping",
        side_effect=exceptions.TransportError(),
    ):
        with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
            id_token.fetch_id_token_credentials(ID_TOKEN_AUDIENCE)
        assert excinfo.match(
            r"Neither metadata server or valid service account credentials are found."
        )

    with mock.patch("google.auth.compute_engine._metadata.ping", return_value=False):
        with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
            id_token.fetch_id_token_credentials(ID_TOKEN_AUDIENCE)
        assert excinfo.match(
            r"Neither metadata server or valid service account credentials are found."
        )


def test_fetch_id_token_credentials_invalid_cred_file_type(monkeypatch):
    user_credentials_file = os.path.join(
        os.path.dirname(__file__), "../data/authorized_user.json"
    )
    monkeypatch.setenv(environment_vars.CREDENTIALS, user_credentials_file)

    with mock.patch("google.auth.compute_engine._metadata.ping", return_value=False):
        with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
            id_token.fetch_id_token_credentials(ID_TOKEN_AUDIENCE)
        assert excinfo.match(
            r"Neither metadata server or valid service account credentials are found."
        )


def test_fetch_id_token_credentials_invalid_json(monkeypatch):
    not_json_file = os.path.join(os.path.dirname(__file__), "../data/public_cert.pem")
    monkeypatch.setenv(environment_vars.CREDENTIALS, not_json_file)

    with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
        id_token.fetch_id_token_credentials(ID_TOKEN_AUDIENCE)
    assert excinfo.match(
        r"GOOGLE_APPLICATION_CREDENTIALS is not valid service account credentials."
    )


def test_fetch_id_token_credentials_invalid_cred_path(monkeypatch):
    not_json_file = os.path.join(os.path.dirname(__file__), "../data/not_exists.json")
    monkeypatch.setenv(environment_vars.CREDENTIALS, not_json_file)

    with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
        id_token.fetch_id_token_credentials(ID_TOKEN_AUDIENCE)
    assert excinfo.match(
        r"GOOGLE_APPLICATION_CREDENTIALS path is either not found or invalid."
    )


@pytest.mark.parametrize(
    "call_kwargs,expected_bind_id_token",
    [
        ({}, None),
        ({"bind_id_token": None}, None),
        ({"bind_id_token": True}, True),
        ({"bind_id_token": False}, False),
    ],
)
def test_fetch_id_token(call_kwargs, expected_bind_id_token):
    mock_cred = mock.MagicMock()
    mock_cred.token = "token"

    mock_req = mock.Mock()

    with mock.patch(
        "google.oauth2.id_token.fetch_id_token_credentials", return_value=mock_cred
    ) as mock_fetch:
        token = id_token.fetch_id_token(mock_req, ID_TOKEN_AUDIENCE, **call_kwargs)
    mock_fetch.assert_called_once_with(
        ID_TOKEN_AUDIENCE, request=mock_req, bind_id_token=expected_bind_id_token
    )
    mock_cred.refresh.assert_called_once_with(mock_req)
    assert token == "token"
