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

import json
import os

import pytest

from google.auth import _helpers, dpop, exceptions
from google.oauth2 import credentials as oauth2_credentials
from google.oauth2 import dpop_credentials

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, "../data")
DPOP_AUTHORIZED_USER_FILE = os.path.join(DATA_DIR, "dpop_authorized_user.json")
DPOP_KEY_FILE = os.path.join(DATA_DIR, "dpop_key.pem")
DPOP_BAD_KEY_FILE = os.path.join(DATA_DIR, "dpop_bad_key.pem")
USERINFO_URL = "https://openidconnect.googleapis.com/v1/userinfo"


class _BadSignatureSigner(dpop.DPoPSigner):
    """ES256 signer with a valid public JWK that produces invalid signatures."""

    def __init__(self, inner_signer):
        self._inner = inner_signer

    @property
    def algorithm(self):
        return self._inner.algorithm

    @property
    def public_jwk(self):
        return self._inner.public_jwk

    def sign(self, data):
        return b"\x00" * 64


def _load_dpop_authorized_user():
    if not os.path.isfile(DPOP_AUTHORIZED_USER_FILE):
        pytest.skip(
            "DPoP authorized user fixture (dpop_authorized_user.json) not found in "
            "system_tests/data. See CONTRIBUTING.rst for setup."
        )
    with open(DPOP_AUTHORIZED_USER_FILE, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _load_signer(key_path, label):
    if not os.path.isfile(key_path):
        pytest.skip(
            "{label} ({name}) not found in system_tests/data. "
            "See CONTRIBUTING.rst for openssl key generation instructions.".format(
                label=label, name=os.path.basename(key_path)
            )
        )
    with open(key_path, "rb") as fh:
        return dpop.SoftwareDPoPSigner.from_pem(fh.read())


def _assert_token_valid(creds, token_info):
    assert creds.token
    assert creds.valid

    info = token_info(creds.token)
    assert "scope" in info
    assert _helpers.string_to_scopes(info["scope"])
    assert int(info["expires_in"]) > 0


def test_dpop_refresh_with_software_key(http_request, token_info):
    info = _load_dpop_authorized_user()
    good_signer = _load_signer(DPOP_KEY_FILE, "DPoP software key fixture")

    creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
        info, dpop_signer=good_signer
    )
    creds.token = None
    creds.expiry = None

    creds.refresh(http_request)

    _assert_token_valid(creds, token_info)


def test_dpop_refresh_without_cached_nonce(http_request, token_info):
    info = dict(_load_dpop_authorized_user())
    info.pop("dpop_nonce", None)
    good_signer = _load_signer(DPOP_KEY_FILE, "DPoP software key fixture")

    creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
        info, dpop_signer=good_signer
    )
    creds.token = None
    creds.expiry = None
    assert creds.dpop_nonce is None

    creds.refresh(http_request)

    _assert_token_valid(creds, token_info)
    assert creds.dpop_nonce


def test_dpop_refresh_recovers_from_stale_nonce(http_request, token_info):
    info = dict(_load_dpop_authorized_user())
    stale_nonce = "stale-invalid-dpop-nonce"
    info["dpop_nonce"] = stale_nonce
    good_signer = _load_signer(DPOP_KEY_FILE, "DPoP software key fixture")

    creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
        info, dpop_signer=good_signer
    )
    creds.token = None
    creds.expiry = None
    assert creds.dpop_nonce == stale_nonce

    creds.refresh(http_request)

    _assert_token_valid(creds, token_info)
    assert creds.dpop_nonce
    assert creds.dpop_nonce != stale_nonce


def test_dpop_refresh_with_deferred_signer_factory(http_request, token_info):
    info = _load_dpop_authorized_user()
    _load_signer(DPOP_KEY_FILE, "DPoP software key fixture")
    factory_calls = [0]

    def signer_factory():
        factory_calls[0] += 1
        return _load_signer(DPOP_KEY_FILE, "DPoP software key fixture")

    creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
        info, dpop_signer=signer_factory
    )
    creds.token = None
    creds.expiry = None
    assert factory_calls[0] == 0

    creds.refresh(http_request)

    assert factory_calls[0] == 1
    _assert_token_valid(creds, token_info)


def test_dpop_authenticated_request(authenticated_request):
    info = _load_dpop_authorized_user()
    good_signer = _load_signer(DPOP_KEY_FILE, "DPoP software key fixture")

    creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
        info, dpop_signer=good_signer
    )
    creds.token = None
    creds.expiry = None

    # First request triggers DPoP refresh via before_request() and sends Bearer
    # Authorization (without a DPoP header) to the resource endpoint.
    authed_request = authenticated_request(creds)
    response = authed_request(url=USERINFO_URL, method="GET")
    assert response.status == 200
    assert creds.token
    assert creds.valid
    payload = json.loads(response.data.decode("utf-8"))
    assert "sub" in payload or "email" in payload


def test_dpop_bound_refresh_fails_without_dpop(http_request):
    info = _load_dpop_authorized_user()

    # Plain OAuth2 Credentials send no DPoP header; a DPoP-bound refresh token
    # must be rejected by Google's token endpoint.
    plain_creds = oauth2_credentials.Credentials.from_authorized_user_info(info)
    plain_creds.token = None
    plain_creds.expiry = None

    with pytest.raises(exceptions.RefreshError):
        plain_creds.refresh(http_request)


def test_dpop_invalid_proof_signature_rejected(http_request):
    info = dict(_load_dpop_authorized_user())
    good_signer = _load_signer(DPOP_KEY_FILE, "DPoP software key fixture")

    info.pop("dpop_thumbprint", None)
    bad_sig_signer = _BadSignatureSigner(good_signer)

    creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
        info, dpop_signer=bad_sig_signer
    )
    creds.token = None
    creds.expiry = None

    with pytest.raises(exceptions.RefreshError):
        creds.refresh(http_request)


def test_dpop_bound_refresh_good_vs_bad_key(http_request, token_info):
    info = _load_dpop_authorized_user()
    good_signer = _load_signer(DPOP_KEY_FILE, "DPoP software key fixture")
    bad_signer = _load_signer(DPOP_BAD_KEY_FILE, "Mismatched DPoP software key fixture")
    assert bad_signer.thumbprint != good_signer.thumbprint

    # Good bound EC P-256 key succeeds against oauth2.googleapis.com/token.
    good_creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
        info, dpop_signer=good_signer
    )
    good_creds.token = None
    good_creds.expiry = None
    good_creds.refresh(http_request)
    _assert_token_valid(good_creds, token_info)

    # Mismatched EC P-256 key fails client-side if dpop_thumbprint is present.
    if info.get("dpop_thumbprint"):
        with pytest.raises(ValueError, match="thumbprint"):
            dpop_credentials.DPoPCredentials.from_authorized_user_info(
                info, dpop_signer=bad_signer
            )

    # Without the client-side thumbprint check, the server must reject the wrong key.
    unbound_metadata = dict(info)
    unbound_metadata.pop("dpop_thumbprint", None)
    bad_creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
        unbound_metadata, dpop_signer=bad_signer
    )
    bad_creds.token = None
    bad_creds.expiry = None
    with pytest.raises(exceptions.RefreshError):
        bad_creds.refresh(http_request)
