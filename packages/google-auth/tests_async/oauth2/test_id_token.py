# Copyright 2020 Google Inc.
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

import google.auth.compute_engine._metadata
from google.auth import _helpers, crypt, environment_vars, exceptions, jwt
from google.oauth2 import _id_token_async as id_token
from google.oauth2 import _service_account_async
from google.oauth2 import id_token as sync_id_token
from tests.oauth2 import test_id_token


def make_request(status, data=None):
    response = mock.AsyncMock(spec=["transport.Response"])
    response.status = status

    if data is not None:
        response.data = mock.AsyncMock(spec=["__call__", "read"])
        response.content = mock.AsyncMock(
            spec=["__call__"], return_value=json.dumps(data).encode("utf-8")
        )

    request = mock.AsyncMock(spec=["transport.Request"])
    request.return_value = response
    return request


@pytest.mark.asyncio
async def test__fetch_certs_success():
    certs = {"1": "cert"}
    request = make_request(200, certs)

    returned_certs = await id_token._fetch_certs(request, mock.sentinel.cert_url)

    request.assert_called_once_with(mock.sentinel.cert_url, method="GET")
    assert returned_certs == certs


@pytest.mark.asyncio
async def test__fetch_certs_failure():
    request = make_request(404)

    with pytest.raises(exceptions.TransportError):
        await id_token._fetch_certs(request, mock.sentinel.cert_url)

    request.assert_called_once_with(mock.sentinel.cert_url, method="GET")


@mock.patch("google.auth.jwt.decode", autospec=True)
@mock.patch("google.oauth2._id_token_async._fetch_certs", autospec=True)
@pytest.mark.asyncio
async def test_verify_token(_fetch_certs, decode):
    result = await id_token.verify_token(mock.sentinel.token, mock.sentinel.request)

    assert result == decode.return_value
    _fetch_certs.assert_called_once_with(
        mock.sentinel.request, sync_id_token._GOOGLE_OAUTH2_CERTS_URL
    )
    decode.assert_called_once_with(
        mock.sentinel.token,
        certs=_fetch_certs.return_value,
        audience=None,
        clock_skew_in_seconds=0,
    )


@mock.patch("google.auth.jwt.decode", autospec=True)
@mock.patch("google.oauth2._id_token_async._fetch_certs", autospec=True)
@pytest.mark.asyncio
async def test_verify_token_clock_skew(_fetch_certs, decode):
    result = await id_token.verify_token(
        mock.sentinel.token, mock.sentinel.request, clock_skew_in_seconds=10
    )

    assert result == decode.return_value
    _fetch_certs.assert_called_once_with(
        mock.sentinel.request, sync_id_token._GOOGLE_OAUTH2_CERTS_URL
    )
    decode.assert_called_once_with(
        mock.sentinel.token,
        certs=_fetch_certs.return_value,
        audience=None,
        clock_skew_in_seconds=10,
    )


@mock.patch("google.auth.jwt.decode", autospec=True)
@mock.patch("google.oauth2._id_token_async._fetch_certs", autospec=True)
@pytest.mark.asyncio
async def test_verify_token_args(_fetch_certs, decode):
    result = await id_token.verify_token(
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


@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_oauth2_token(verify_token):
    verify_token.return_value = {"iss": "accounts.google.com"}
    result = await id_token.verify_oauth2_token(
        mock.sentinel.token, mock.sentinel.request, audience=mock.sentinel.audience
    )

    assert result == verify_token.return_value
    verify_token.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        certs_url=sync_id_token._GOOGLE_OAUTH2_CERTS_URL,
        clock_skew_in_seconds=0,
    )


@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_oauth2_token_clock_skew(verify_token):
    verify_token.return_value = {"iss": "accounts.google.com"}
    result = await id_token.verify_oauth2_token(
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
        certs_url=sync_id_token._GOOGLE_OAUTH2_CERTS_URL,
        clock_skew_in_seconds=10,
    )


@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_oauth2_token_invalid_iss(verify_token):
    verify_token.return_value = {"iss": "invalid_issuer"}

    with pytest.raises(exceptions.GoogleAuthError):
        await id_token.verify_oauth2_token(
            mock.sentinel.token, mock.sentinel.request, audience=mock.sentinel.audience
        )


@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_firebase_token(verify_token):
    verify_token.return_value = {
        "aud": "my-project-id",
        "iss": "https://securetoken.google.com/my-project-id",
        "sub": "my-user-id",
    }
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        result = await id_token.verify_firebase_token(
            mock.sentinel.token, mock.sentinel.request, audience=mock.sentinel.audience
        )

    assert result == verify_token.return_value
    verify_token.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=mock.sentinel.audience,
        certs_url=sync_id_token._GOOGLE_APIS_CERTS_URL,
        clock_skew_in_seconds=0,
    )


@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_firebase_token_clock_skew(verify_token):
    verify_token.return_value = {
        "aud": "my-project-id",
        "iss": "https://securetoken.google.com/my-project-id",
        "sub": "my-user-id",
    }
    result = await id_token.verify_firebase_token(
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
        certs_url=sync_id_token._GOOGLE_APIS_CERTS_URL,
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
@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_firebase_token_invalid_iss(verify_token, invalid_payload):
    verify_token.return_value = invalid_payload

    with pytest.raises(exceptions.InvalidValue, match="Wrong issuer"):
        await id_token.verify_firebase_token(
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
@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_firebase_token_missing_aud(verify_token, invalid_payload):
    verify_token.return_value = invalid_payload

    with pytest.raises(
        exceptions.InvalidValue, match="Token does not contain a valid 'aud' claim"
    ):
        await id_token.verify_firebase_token(
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
@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_firebase_token_invalid_sub(verify_token, invalid_payload):
    verify_token.return_value = invalid_payload

    with pytest.raises(
        exceptions.InvalidValue, match="Token does not contain a valid 'sub' claim"
    ):
        await id_token.verify_firebase_token(
            mock.sentinel.token,
            mock.sentinel.request,
            audience=mock.sentinel.audience,
        )


@pytest.mark.parametrize("audience", [None, "", []])
@mock.patch("google.oauth2._id_token_async.verify_token", autospec=True)
@pytest.mark.asyncio
async def test_verify_firebase_token_warns_without_audience(verify_token, audience):
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
        result = await id_token.verify_firebase_token(
            mock.sentinel.token, mock.sentinel.request, audience=audience
        )

    assert len(record) == 1
    assert record[0].filename == __file__
    assert result == verify_token.return_value
    verify_token.assert_called_once_with(
        mock.sentinel.token,
        mock.sentinel.request,
        audience=audience,
        certs_url=sync_id_token._GOOGLE_APIS_CERTS_URL,
        clock_skew_in_seconds=0,
    )


@pytest.mark.parametrize("alg", ["ES256", "ES384"])
@pytest.mark.asyncio
async def test_verify_firebase_token_mismatched_alg_for_rsa_certs(alg):
    with open(test_id_token.PUBLIC_CERT_FILE, "r") as fh:
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
        await id_token.verify_firebase_token(token, request, audience="my-project-id")


@pytest.mark.asyncio
async def test_verify_firebase_token_end_to_end():
    with open(test_id_token.PRIVATE_KEY_FILE, "rb") as fh:
        private_key = fh.read()
    with open(test_id_token.PUBLIC_CERT_FILE, "r") as fh:
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

    result = await id_token.verify_firebase_token(
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
        await id_token.verify_firebase_token(
            cross_tenant_token, request, audience="my-project-id"
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "call_kwargs,expected_bind_id_token",
    [
        ({}, None),
        ({"bind_id_token": None}, None),
        ({"bind_id_token": True}, True),
        ({"bind_id_token": False}, False),
    ],
)
async def test_fetch_id_token_from_metadata_server(
    monkeypatch, call_kwargs, expected_bind_id_token
):
    monkeypatch.delenv(environment_vars.CREDENTIALS, raising=False)

    def mock_init(
        self, request, audience, use_metadata_identity_endpoint, bind_id_token
    ):
        assert use_metadata_identity_endpoint
        assert bind_id_token is expected_bind_id_token
        self.token = "id_token"

    with mock.patch("google.auth.compute_engine._metadata.ping", return_value=True):
        with mock.patch.multiple(
            google.auth.compute_engine.IDTokenCredentials,
            __init__=mock_init,
            refresh=mock.Mock(),
        ):
            request = mock.AsyncMock()
            token = await id_token.fetch_id_token(
                request,
                "https://pubsub.googleapis.com",
                **call_kwargs,
            )
            assert token == "id_token"


@pytest.mark.asyncio
@pytest.mark.parametrize("bind_id_token", [None, True, False])
async def test_fetch_id_token_from_explicit_cred_json_file(monkeypatch, bind_id_token):
    monkeypatch.setenv(environment_vars.CREDENTIALS, test_id_token.SERVICE_ACCOUNT_FILE)

    async def mock_refresh(self, request):
        self.token = "id_token"

    with mock.patch.object(
        _service_account_async.IDTokenCredentials, "refresh", mock_refresh
    ):
        request = mock.AsyncMock()
        token = await id_token.fetch_id_token(
            request, "https://pubsub.googleapis.com", bind_id_token=bind_id_token
        )
        assert token == "id_token"


@pytest.mark.asyncio
async def test_fetch_id_token_no_cred_exists(monkeypatch):
    monkeypatch.delenv(environment_vars.CREDENTIALS, raising=False)

    with mock.patch(
        "google.auth.compute_engine._metadata.ping",
        side_effect=exceptions.TransportError(),
    ):
        with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
            request = mock.AsyncMock()
            await id_token.fetch_id_token(request, "https://pubsub.googleapis.com")
        assert excinfo.match(
            r"Neither metadata server or valid service account credentials are found."
        )

    with mock.patch("google.auth.compute_engine._metadata.ping", return_value=False):
        with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
            request = mock.AsyncMock()
            await id_token.fetch_id_token(request, "https://pubsub.googleapis.com")
        assert excinfo.match(
            r"Neither metadata server or valid service account credentials are found."
        )


@pytest.mark.asyncio
async def test_fetch_id_token_invalid_cred_file(monkeypatch):
    not_json_file = os.path.join(
        os.path.dirname(__file__), "../../tests/data/public_cert.pem"
    )
    monkeypatch.setenv(environment_vars.CREDENTIALS, not_json_file)

    with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
        request = mock.AsyncMock()
        await id_token.fetch_id_token(request, "https://pubsub.googleapis.com")
    assert excinfo.match(
        r"GOOGLE_APPLICATION_CREDENTIALS is not valid service account credentials."
    )


@pytest.mark.asyncio
async def test_fetch_id_token_invalid_cred_type(monkeypatch):
    user_credentials_file = os.path.join(
        os.path.dirname(__file__), "../../tests/data/authorized_user.json"
    )
    monkeypatch.setenv(environment_vars.CREDENTIALS, user_credentials_file)

    with mock.patch("google.auth.compute_engine._metadata.ping", return_value=False):
        with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
            request = mock.AsyncMock()
            await id_token.fetch_id_token(request, "https://pubsub.googleapis.com")
        assert excinfo.match(
            r"Neither metadata server or valid service account credentials are found."
        )


@pytest.mark.asyncio
async def test_fetch_id_token_invalid_cred_path(monkeypatch):
    not_json_file = os.path.join(
        os.path.dirname(__file__), "../../tests/data/not_exists.json"
    )
    monkeypatch.setenv(environment_vars.CREDENTIALS, not_json_file)

    with pytest.raises(exceptions.DefaultCredentialsError) as excinfo:
        request = mock.AsyncMock()
        await id_token.fetch_id_token(request, "https://pubsub.googleapis.com")
    assert excinfo.match(
        r"GOOGLE_APPLICATION_CREDENTIALS path is either not found or invalid."
    )
