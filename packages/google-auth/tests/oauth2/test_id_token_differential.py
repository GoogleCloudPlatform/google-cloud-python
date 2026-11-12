# Copyright 2026 Google LLC
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
import http.server
import json
import threading
import time
from unittest import mock

import pytest
import jwt as pyjwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from google.auth import exceptions
from google.auth.transport.requests import Request
from google.oauth2 import id_token


class CertsServer:
    def __init__(self, jwks_data, pem_data):
        self.jwks_bytes = json.dumps(jwks_data).encode("utf-8")
        self.pem_bytes = json.dumps(pem_data).encode("utf-8")
        self.mode = "jwks"

        parent = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                if parent.mode == "jwks":
                    self.wfile.write(parent.jwks_bytes)
                else:
                    self.wfile.write(parent.pem_bytes)

            def log_message(self, format, *args):
                pass

        self.server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
        self.port = self.server.server_port
        self.url = f"http://127.0.0.1:{self.port}/certs"
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def shutdown(self):
        self.server.shutdown()
        self.server.server_close()


@pytest.fixture(scope="module")
def crypto_env():
    """Generates synthetic RSA keypair and starts local mock certs server."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pub_numbers = private_key.public_key().public_numbers()

    def int_to_b64url(val):
        b = val.to_bytes((val.bit_length() + 7) // 8, byteorder="big")
        return base64.urlsafe_b64encode(b).decode("utf-8").rstrip("=")

    kid = "diff-test-key-1"
    jwk_dict = {
        "kty": "RSA",
        "alg": "RS256",
        "use": "sig",
        "kid": kid,
        "n": int_to_b64url(pub_numbers.n),
        "e": int_to_b64url(pub_numbers.e),
    }
    jwks_data = {"keys": [jwk_dict]}

    pub_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode("utf-8")
    pem_data = {kid: pub_pem}

    server = CertsServer(jwks_data, pem_data)
    req = Request()

    yield {
        "private_key": private_key,
        "kid": kid,
        "server": server,
        "req": req,
    }

    server.shutdown()


def _make_token(crypto_env, payload):
    return pyjwt.encode(
        payload,
        crypto_env["private_key"],
        algorithm="RS256",
        headers={"kid": crypto_env["kid"]},
    )


def test_differential_valid_token(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "my-client-app",
        "iat": now - 10,
        "exp": now + 3600,
    }
    token = _make_token(crypto_env, payload)

    # JWKS branch
    crypto_env["server"].mode = "jwks"
    info_jwks = id_token.verify_token(
        token, crypto_env["req"], audience="my-client-app", certs_url=crypto_env["server"].url
    )
    assert info_jwks["sub"] == "user-123"

    # PEM cert-mapping branch
    crypto_env["server"].mode = "pem"
    info_pem = id_token.verify_token(
        token, crypto_env["req"], audience="my-client-app", certs_url=crypto_env["server"].url
    )
    assert info_pem["sub"] == "user-123"


def test_differential_missing_exp_rejected(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "my-client-app",
        "iat": now - 10,
        # missing exp
    }
    token = _make_token(crypto_env, payload)

    # JWKS verification must reject missing exp
    crypto_env["server"].mode = "jwks"
    with pytest.raises(pyjwt.MissingRequiredClaimError) as exc_info:
        id_token.verify_token(
            token, crypto_env["req"], audience="my-client-app", certs_url=crypto_env["server"].url
        )
    assert "exp" in str(exc_info.value)

    # PEM cert-mapping must reject missing exp
    crypto_env["server"].mode = "pem"
    with pytest.raises(exceptions.MalformedError) as exc_info:
        id_token.verify_token(
            token, crypto_env["req"], audience="my-client-app", certs_url=crypto_env["server"].url
        )
    assert "exp" in str(exc_info.value)


def test_differential_missing_iat_rejected(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "my-client-app",
        "exp": now + 3600,
        # missing iat
    }
    token = _make_token(crypto_env, payload)

    # JWKS verification must reject missing iat
    crypto_env["server"].mode = "jwks"
    with pytest.raises(pyjwt.MissingRequiredClaimError) as exc_info:
        id_token.verify_token(
            token, crypto_env["req"], audience="my-client-app", certs_url=crypto_env["server"].url
        )
    assert "iat" in str(exc_info.value)

    # PEM cert-mapping must reject missing iat
    crypto_env["server"].mode = "pem"
    with pytest.raises(exceptions.MalformedError) as exc_info:
        id_token.verify_token(
            token, crypto_env["req"], audience="my-client-app", certs_url=crypto_env["server"].url
        )
    assert "iat" in str(exc_info.value)


def test_differential_clock_skew_expired_within_leeway(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "my-client-app",
        "iat": now - 1000,
        "exp": now - 300,  # expired 5 minutes ago
    }
    token = _make_token(crypto_env, payload)

    # With 10 minutes leeway, both must accept
    crypto_env["server"].mode = "jwks"
    info_jwks = id_token.verify_token(
        token,
        crypto_env["req"],
        audience="my-client-app",
        certs_url=crypto_env["server"].url,
        clock_skew_in_seconds=600,
    )
    assert info_jwks["sub"] == "user-123"

    crypto_env["server"].mode = "pem"
    info_pem = id_token.verify_token(
        token,
        crypto_env["req"],
        audience="my-client-app",
        certs_url=crypto_env["server"].url,
        clock_skew_in_seconds=600,
    )
    assert info_pem["sub"] == "user-123"


def test_differential_clock_skew_expired_outside_leeway(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "my-client-app",
        "iat": now - 1000,
        "exp": now - 600,  # expired 10 minutes ago
    }
    token = _make_token(crypto_env, payload)

    # With 5 minutes leeway, both must reject
    crypto_env["server"].mode = "jwks"
    with pytest.raises(pyjwt.ExpiredSignatureError):
        id_token.verify_token(
            token,
            crypto_env["req"],
            audience="my-client-app",
            certs_url=crypto_env["server"].url,
            clock_skew_in_seconds=300,
        )

    crypto_env["server"].mode = "pem"
    with pytest.raises(exceptions.InvalidValue):
        id_token.verify_token(
            token,
            crypto_env["req"],
            audience="my-client-app",
            certs_url=crypto_env["server"].url,
            clock_skew_in_seconds=300,
        )


def test_differential_clock_skew_future_iat_within_leeway(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "my-client-app",
        "iat": now + 300,  # issued 5 minutes in future
        "exp": now + 3600,
    }
    token = _make_token(crypto_env, payload)

    # With 10 minutes leeway, both must accept
    crypto_env["server"].mode = "jwks"
    info_jwks = id_token.verify_token(
        token,
        crypto_env["req"],
        audience="my-client-app",
        certs_url=crypto_env["server"].url,
        clock_skew_in_seconds=600,
    )
    assert info_jwks["sub"] == "user-123"

    crypto_env["server"].mode = "pem"
    info_pem = id_token.verify_token(
        token,
        crypto_env["req"],
        audience="my-client-app",
        certs_url=crypto_env["server"].url,
        clock_skew_in_seconds=600,
    )
    assert info_pem["sub"] == "user-123"


def test_differential_clock_skew_future_iat_outside_leeway(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "my-client-app",
        "iat": now + 600,  # issued 10 minutes in future
        "exp": now + 3600,
    }
    token = _make_token(crypto_env, payload)

    # With 5 minutes leeway, both must reject
    crypto_env["server"].mode = "jwks"
    with pytest.raises(pyjwt.ImmatureSignatureError):
        id_token.verify_token(
            token,
            crypto_env["req"],
            audience="my-client-app",
            certs_url=crypto_env["server"].url,
            clock_skew_in_seconds=300,
        )

    crypto_env["server"].mode = "pem"
    with pytest.raises(exceptions.InvalidValue):
        id_token.verify_token(
            token,
            crypto_env["req"],
            audience="my-client-app",
            certs_url=crypto_env["server"].url,
            clock_skew_in_seconds=300,
        )


def test_differential_audience_mismatch(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "intended-aud",
        "iat": now - 10,
        "exp": now + 3600,
    }
    token = _make_token(crypto_env, payload)

    crypto_env["server"].mode = "jwks"
    with pytest.raises(pyjwt.InvalidAudienceError):
        id_token.verify_token(
            token,
            crypto_env["req"],
            audience="wrong-aud",
            certs_url=crypto_env["server"].url,
        )

    crypto_env["server"].mode = "pem"
    with pytest.raises(exceptions.InvalidValue):
        id_token.verify_token(
            token,
            crypto_env["req"],
            audience="wrong-aud",
            certs_url=crypto_env["server"].url,
        )


def test_differential_signature_tampered(crypto_env):
    now = int(time.time())
    payload = {
        "iss": "https://accounts.google.com",
        "sub": "user-123",
        "aud": "my-client-app",
        "iat": now - 10,
        "exp": now + 3600,
    }
    token = _make_token(crypto_env, payload)
    parts = token.split(".")
    tampered_sig = parts[2][:-2] + ("aa" if parts[2][-2:] != "aa" else "bb")
    tampered_token = f"{parts[0]}.{parts[1]}.{tampered_sig}"

    crypto_env["server"].mode = "jwks"
    with pytest.raises(pyjwt.DecodeError):
        id_token.verify_token(
            tampered_token,
            crypto_env["req"],
            audience="my-client-app",
            certs_url=crypto_env["server"].url,
        )

    crypto_env["server"].mode = "pem"
    with pytest.raises(exceptions.MalformedError):
        id_token.verify_token(
            tampered_token,
            crypto_env["req"],
            audience="my-client-app",
            certs_url=crypto_env["server"].url,
        )
