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
import tempfile
from unittest import mock

import pytest  # type: ignore
from cryptography.hazmat.primitives.asymmetric import ec

from google.auth import dpop, exceptions, transport
from google.auth.dpop import SoftwareDPoPSigner
from google.oauth2 import _client, dpop_credentials, reauth
from google.oauth2 import credentials as _oauth2_credentials

_TOKEN_URI = "https://oauth2.googleapis.com/token"
_REFRESH_TOKEN = "refresh_token"
_CLIENT_ID = "client_id"
_CLIENT_SECRET = "client_secret"
_ACCESS_TOKEN = "access-token-123"

_SUCCESS_RESPONSE_DATA = {
    "access_token": "new-access-token",
    "refresh_token": "new-refresh-token",
    "expires_in": 3600,
}

_NONCE_HEADERS = {"DPoP-Nonce": "server-nonce-xyz"}


class TestDPoPCredentials(object):
    TOKEN_URI = _TOKEN_URI
    REFRESH_TOKEN = _REFRESH_TOKEN
    CLIENT_ID = _CLIENT_ID
    CLIENT_SECRET = _CLIENT_SECRET

    @classmethod
    def make_dpop_signer(cls, key_id=None):
        """Create a SoftwareDPoPSigner backed by a fresh EC P-256 key."""
        private_key = ec.generate_private_key(ec.SECP256R1())
        return SoftwareDPoPSigner(private_key, key_id=key_id)

    @classmethod
    def make_credentials(cls, dpop_signer=None, dpop_nonce=None):
        """Create a DPoPCredentials instance for testing."""
        return dpop_credentials.DPoPCredentials(
            token=_ACCESS_TOKEN,
            dpop_signer=dpop_signer,
            dpop_nonce=dpop_nonce,
            refresh_token=cls.REFRESH_TOKEN,
            token_uri=cls.TOKEN_URI,
            client_id=cls.CLIENT_ID,
            client_secret=cls.CLIENT_SECRET,
        )

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------

    def test_constructor(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="nonce1")

        assert creds.token == _ACCESS_TOKEN
        assert creds.dpop_signer is signer
        assert creds.dpop_nonce == "nonce1"
        assert creds.refresh_token == self.REFRESH_TOKEN
        assert creds.token_uri == self.TOKEN_URI
        assert creds.client_id == self.CLIENT_ID
        assert creds.client_secret == self.CLIENT_SECRET

    def test_constructor_without_signer(self):
        creds = self.make_credentials()

        assert creds.dpop_signer is None
        assert creds.dpop_nonce is None

    def test_constructor_with_callable_signer_factory(self):
        signer = self.make_dpop_signer()
        factory_called = [0]

        def signer_factory():
            factory_called[0] += 1
            return signer

        creds = self.make_credentials(dpop_signer=signer_factory)

        assert creds._dpop_signer is None
        assert creds._dpop_signer_factory is not None
        assert factory_called[0] == 0

        # Access property: should invoke factory once and cache.
        assert creds.dpop_signer is signer
        assert factory_called[0] == 1
        assert creds._dpop_signer is signer
        assert creds._dpop_signer_factory is None

        # Subsequent accesses use cached signer.
        assert creds.dpop_signer is signer
        assert factory_called[0] == 1

    def test_dpop_signer_property(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)

        assert creds.dpop_signer is signer

    def test_dpop_nonce_property(self):
        creds = self.make_credentials(dpop_nonce="test-nonce")

        assert creds.dpop_nonce == "test-nonce"

    # ------------------------------------------------------------------
    # Pickle round-trip
    # ------------------------------------------------------------------

    def test_pickle_excludes_signer(self):
        """__getstate__ must drop _dpop_signer (unpicklable key material)."""
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="n1")

        state = creds.__getstate__()

        assert "_dpop_signer" not in state
        assert state["_dpop_nonce"] == "n1"

    def test_pickle_with_callable_factory(self):
        """__getstate__ and __setstate__ must handle callable signer factories."""
        import pickle

        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=lambda: signer, dpop_nonce="n1")

        state = creds.__getstate__()
        assert "_dpop_signer" not in state
        assert "_dpop_signer_factory" not in state

        pickled = pickle.dumps(creds)
        restored = pickle.loads(pickled)

        assert restored.dpop_signer is None
        assert restored._dpop_signer_factory is None
        assert restored.dpop_nonce == "n1"

    def test_pickle_roundtrip_preserves_nonce(self):
        """Pickle → unpickle must preserve nonce and set signer to None."""
        import pickle

        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="n1")

        pickled = pickle.dumps(creds)
        restored = pickle.loads(pickled)

        assert isinstance(restored, dpop_credentials.DPoPCredentials)
        assert restored.dpop_nonce == "n1"
        assert restored.dpop_signer is None
        assert restored.token == _ACCESS_TOKEN
        assert restored.client_id == self.CLIENT_ID

    def test_pickle_roundtrip_without_dpop(self):
        """DPoPCredentials with no signer/nonce survives pickle."""
        import pickle

        creds = self.make_credentials()

        restored = pickle.loads(pickle.dumps(creds))

        assert isinstance(restored, dpop_credentials.DPoPCredentials)
        assert restored.dpop_signer is None
        assert restored.dpop_nonce is None
        assert restored.token == _ACCESS_TOKEN

    def test_dpop_signer_setter(self):
        """dpop_signer setter allows re-attaching a signer after unpickle."""
        creds = self.make_credentials()
        assert creds.dpop_signer is None

        signer = self.make_dpop_signer()
        creds.dpop_signer = signer

        assert creds.dpop_signer is signer

    def test_pickle_then_reattach_signer(self):
        """Full flow: pickle, unpickle, re-attach signer, verify usable."""
        import pickle

        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="n1")

        restored = pickle.loads(pickle.dumps(creds))
        assert restored.dpop_signer is None

        new_signer = self.make_dpop_signer()
        restored.dpop_signer = new_signer

        assert restored.dpop_signer is new_signer
        assert restored.dpop_nonce == "n1"

    # ------------------------------------------------------------------
    # _apply() — always uses Bearer (Google APIs require it)
    # ------------------------------------------------------------------

    def test_apply_with_signer_uses_bearer(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        headers = {}

        creds._apply(headers)

        assert headers["authorization"] == "Bearer {}".format(_ACCESS_TOKEN)

    def test_apply_without_signer(self):
        creds = self.make_credentials()
        headers = {}

        creds._apply(headers)

        assert headers["authorization"] == "Bearer {}".format(_ACCESS_TOKEN)

    # ------------------------------------------------------------------
    # _after_refresh()
    # ------------------------------------------------------------------

    def test_after_refresh_injects_dpop_proof(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="after-nonce")
        request = mock.create_autospec(transport.Request)
        headers = {}

        creds._after_refresh(request, "GET", "https://api.example.com/data", headers)

        assert "DPoP" in headers
        proof = headers["DPoP"]
        # DPoP proof is a compact JWS: header.payload.signature
        parts = proof.split(".")
        assert len(parts) == 3

    def test_after_refresh_no_signer(self):
        creds = self.make_credentials()
        request = mock.create_autospec(transport.Request)
        headers = {}

        creds._after_refresh(request, "GET", "https://api.example.com/data", headers)

        assert "DPoP" not in headers

    def test_after_refresh_no_token(self):
        signer = self.make_dpop_signer()
        creds = dpop_credentials.DPoPCredentials(
            token=None,
            dpop_signer=signer,
            refresh_token=self.REFRESH_TOKEN,
            token_uri=self.TOKEN_URI,
            client_id=self.CLIENT_ID,
            client_secret=self.CLIENT_SECRET,
        )
        request = mock.create_autospec(transport.Request)
        headers = {}

        creds._after_refresh(request, "GET", "https://api.example.com/data", headers)

        assert "DPoP" not in headers

    @mock.patch.object(_oauth2_credentials.Credentials, "_after_refresh", autospec=True)
    def test_after_refresh_calls_super(self, mock_parent_after_refresh):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        request = mock.create_autospec(transport.Request)
        headers = {}

        creds._after_refresh(request, "GET", "https://api.example.com/data", headers)

        # Verify super()._after_refresh() was called, which is
        # required for Regional Access Boundary support.
        mock_parent_after_refresh.assert_called_once_with(
            creds, request, "GET", "https://api.example.com/data", headers
        )

    # ------------------------------------------------------------------
    # before_request() integration (refresh → _after_refresh → apply)
    # ------------------------------------------------------------------

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_before_request_full_cycle(self, mock_token_request):
        """Verifies the complete before_request() flow produces both
        Authorization: Bearer and DPoP headers on the outgoing request.
        """
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        # Expire the token so before_request triggers a refresh.
        creds.token = None
        creds.expiry = None
        request = mock.create_autospec(transport.Request)

        mock_token_request.return_value = (
            True,
            _SUCCESS_RESPONSE_DATA,
            None,
            _NONCE_HEADERS,
        )

        headers = {}
        creds.before_request(
            request, "GET", "https://api.example.com/resource", headers
        )

        # Bearer token in Authorization header.
        assert headers["authorization"] == "Bearer new-access-token"

        # DPoP proof in DPoP header.
        assert "DPoP" in headers
        parts = headers["DPoP"].split(".")
        assert len(parts) == 3

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_before_request_valid_token_skips_refresh(self, mock_token_request):
        """When the token is valid, before_request() should skip refresh
        but still apply the Bearer token.
        """
        import datetime

        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        # Set a far-future expiry so token is valid.
        creds.expiry = datetime.datetime.max

        headers = {}
        creds.before_request(
            mock.create_autospec(transport.Request),
            "POST",
            "https://api.example.com/data",
            headers,
        )

        # No refresh should have occurred.
        mock_token_request.assert_not_called()

        # Bearer header is applied.
        assert headers["authorization"] == "Bearer {}".format(_ACCESS_TOKEN)

    # ------------------------------------------------------------------
    # _call_refresh_grant()
    # ------------------------------------------------------------------

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_happy_path(self, mock_token_request):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        request = mock.create_autospec(transport.Request)

        mock_token_request.return_value = (
            True,
            _SUCCESS_RESPONSE_DATA,
            None,
            _NONCE_HEADERS,
        )

        result = creds._call_refresh_grant(
            request,
            self.TOKEN_URI,
            self.REFRESH_TOKEN,
            self.CLIENT_ID,
            self.CLIENT_SECRET,
        )

        # Verify the endpoint was called once.
        assert mock_token_request.call_count == 1

        call_kwargs = mock_token_request.call_args
        # Verify DPoP header was sent.
        sent_headers = call_kwargs[1].get("headers") or call_kwargs[0][3]
        assert "DPoP" in sent_headers

        # Verify return_response_headers=True was passed.
        assert call_kwargs[1]["return_response_headers"] is True

        # Verify the result contains the expected tokens.
        access_token, refresh_token, expiry, response_data, rapt = result
        assert access_token == "new-access-token"
        assert refresh_token == "new-refresh-token"

        # Verify nonce was captured from response headers.
        assert creds.dpop_nonce == "server-nonce-xyz"

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_nonce_challenge(self, mock_token_request):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        request = mock.create_autospec(transport.Request)

        # First call: use_dpop_nonce error with a nonce header.
        # Second call: success.
        mock_token_request.side_effect = [
            (
                False,
                {"error": "use_dpop_nonce"},
                False,
                {"DPoP-Nonce": "retry-nonce-abc"},
            ),
            (
                True,
                _SUCCESS_RESPONSE_DATA,
                None,
                {"DPoP-Nonce": "final-nonce-def"},
            ),
        ]

        result = creds._call_refresh_grant(
            request,
            self.TOKEN_URI,
            self.REFRESH_TOKEN,
            self.CLIENT_ID,
            self.CLIENT_SECRET,
        )

        # Verify two calls were made (initial + retry).
        assert mock_token_request.call_count == 2

        # Verify nonce was updated to the final value.
        assert creds.dpop_nonce == "final-nonce-def"

        access_token = result[0]
        assert access_token == "new-access-token"

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_nonce_captured_on_success(self, mock_token_request):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        request = mock.create_autospec(transport.Request)

        mock_token_request.return_value = (
            True,
            _SUCCESS_RESPONSE_DATA,
            None,
            {"DPoP-Nonce": "captured-nonce"},
        )

        creds._call_refresh_grant(
            request,
            self.TOKEN_URI,
            self.REFRESH_TOKEN,
            self.CLIENT_ID,
            self.CLIENT_SECRET,
        )

        assert creds.dpop_nonce == "captured-nonce"

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_error(self, mock_token_request):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        request = mock.create_autospec(transport.Request)

        mock_token_request.return_value = (
            False,
            {"error": "invalid_grant", "error_description": "Token expired"},
            False,
            {},
        )

        with pytest.raises(exceptions.RefreshError):
            creds._call_refresh_grant(
                request,
                self.TOKEN_URI,
                self.REFRESH_TOKEN,
                self.CLIENT_ID,
                self.CLIENT_SECRET,
            )

    def test_refresh_without_signer_raises(self):
        creds = self.make_credentials()  # no signer
        request = mock.create_autospec(transport.Request)

        with pytest.raises(ValueError, match="requires a dpop_signer"):
            creds._call_refresh_grant(
                request,
                self.TOKEN_URI,
                self.REFRESH_TOKEN,
                self.CLIENT_ID,
                self.CLIENT_SECRET,
            )

    @mock.patch("google.oauth2.reauth.get_rapt_token")
    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_rapt_challenge_with_reauth_enabled(
        self, mock_token_request, mock_get_rapt
    ):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        creds._enable_reauth_refresh = True
        request = mock.create_autospec(transport.Request)
        mock_get_rapt.return_value = "rapt-token-123"

        # First call: RAPT challenge.
        # Second call: success after RAPT is included.
        mock_token_request.side_effect = [
            (
                False,
                {
                    "error": reauth._REAUTH_NEEDED_ERROR,
                    "error_subtype": reauth._REAUTH_NEEDED_ERROR_RAPT_REQUIRED,
                },
                False,
                {},
            ),
            (
                True,
                _SUCCESS_RESPONSE_DATA,
                None,
                _NONCE_HEADERS,
            ),
        ]

        result = creds._call_refresh_grant(
            request,
            self.TOKEN_URI,
            self.REFRESH_TOKEN,
            self.CLIENT_ID,
            self.CLIENT_SECRET,
        )

        # Verify reauth.get_rapt_token was called.
        mock_get_rapt.assert_called_once_with(
            request,
            self.CLIENT_ID,
            self.CLIENT_SECRET,
            self.REFRESH_TOKEN,
            self.TOKEN_URI,
            scopes=None,
        )

        # Two calls to the endpoint: initial + retry with RAPT.
        assert mock_token_request.call_count == 2

        # Verify the second call includes the rapt token in the body.
        second_call_body = mock_token_request.call_args_list[1][0][2]
        assert second_call_body["rapt"] == "rapt-token-123"

        access_token = result[0]
        assert access_token == "new-access-token"

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_rapt_challenge_without_reauth_raises(self, mock_token_request):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        creds._enable_reauth_refresh = False
        request = mock.create_autospec(transport.Request)

        mock_token_request.return_value = (
            False,
            {
                "error": reauth._REAUTH_NEEDED_ERROR,
                "error_subtype": reauth._REAUTH_NEEDED_ERROR_INVALID_RAPT,
            },
            False,
            {},
        )

        with pytest.raises(exceptions.RefreshError, match="Reauthentication"):
            creds._call_refresh_grant(
                request,
                self.TOKEN_URI,
                self.REFRESH_TOKEN,
                self.CLIENT_ID,
                self.CLIENT_SECRET,
            )

    @mock.patch("google.oauth2.reauth.get_rapt_token")
    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_rapt_challenge_invalid_rapt_subtype(
        self, mock_token_request, mock_get_rapt
    ):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        creds._enable_reauth_refresh = True
        request = mock.create_autospec(transport.Request)
        mock_get_rapt.return_value = "rapt-token-456"

        mock_token_request.side_effect = [
            (
                False,
                {
                    "error": reauth._REAUTH_NEEDED_ERROR,
                    "error_subtype": reauth._REAUTH_NEEDED_ERROR_INVALID_RAPT,
                },
                False,
                {},
            ),
            (
                True,
                _SUCCESS_RESPONSE_DATA,
                None,
                {},
            ),
        ]

        result = creds._call_refresh_grant(
            request,
            self.TOKEN_URI,
            self.REFRESH_TOKEN,
            self.CLIENT_ID,
            self.CLIENT_SECRET,
        )

        mock_get_rapt.assert_called_once()
        assert result[0] == "new-access-token"

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_with_scopes_passed_to_body(self, mock_token_request):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        request = mock.create_autospec(transport.Request)

        mock_token_request.return_value = (
            True,
            _SUCCESS_RESPONSE_DATA,
            None,
            {},
        )

        creds._call_refresh_grant(
            request,
            self.TOKEN_URI,
            self.REFRESH_TOKEN,
            self.CLIENT_ID,
            self.CLIENT_SECRET,
            scopes=["email", "profile"],
        )

        call_body = mock_token_request.call_args[0][2]
        assert call_body["scope"] == "email profile"

    @mock.patch("google.oauth2._client._token_endpoint_request_no_throw")
    def test_refresh_with_rapt_token_passed_to_body(self, mock_token_request):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)
        request = mock.create_autospec(transport.Request)

        mock_token_request.return_value = (
            True,
            _SUCCESS_RESPONSE_DATA,
            None,
            {},
        )

        creds._call_refresh_grant(
            request,
            self.TOKEN_URI,
            self.REFRESH_TOKEN,
            self.CLIENT_ID,
            self.CLIENT_SECRET,
            rapt_token="existing-rapt",
        )

        call_body = mock_token_request.call_args[0][2]
        assert call_body["rapt"] == "existing-rapt"

    # ------------------------------------------------------------------
    # _make_copy()
    # ------------------------------------------------------------------

    def test_make_copy_preserves_dpop_fields(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="copy-nonce")

        copy = creds._make_copy()

        assert copy.dpop_signer is signer
        assert copy.dpop_nonce == "copy-nonce"
        assert copy.refresh_token == self.REFRESH_TOKEN
        assert copy.token_uri == self.TOKEN_URI
        assert copy.client_id == self.CLIENT_ID
        assert copy.client_secret == self.CLIENT_SECRET
        assert isinstance(copy, dpop_credentials.DPoPCredentials)

    # ------------------------------------------------------------------
    # to_json()
    # ------------------------------------------------------------------

    def test_to_json_includes_dpop_metadata(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="json-nonce")

        result = json.loads(creds.to_json())

        assert result["dpop_nonce"] == "json-nonce"
        assert "dpop_thumbprint" in result
        assert result["dpop_thumbprint"] == signer.thumbprint

    def test_to_json_includes_key_id(self):
        signer = self.make_dpop_signer(key_id="my-key-id")
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="nonce")

        result = json.loads(creds.to_json())

        assert result["dpop_key_id"] == "my-key-id"
        assert result["dpop_thumbprint"] == signer.thumbprint

    def test_to_json_no_private_key_material(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)

        raw = creds.to_json()

        # Private EC key components must never appear in the JSON.
        assert '"d"' not in raw
        assert '"p"' not in raw
        assert '"q"' not in raw
        assert "PRIVATE KEY" not in raw

    def test_to_json_without_signer(self):
        creds = self.make_credentials()

        result = json.loads(creds.to_json())

        assert "dpop_thumbprint" not in result
        assert "dpop_key_id" not in result
        assert "dpop_nonce" not in result

    # ------------------------------------------------------------------
    # from_authorized_user_info()
    # ------------------------------------------------------------------

    def test_from_authorized_user_info_with_signer(self):
        signer = self.make_dpop_signer()
        info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": self.REFRESH_TOKEN,
        }

        creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
            info, dpop_signer=signer
        )

        assert isinstance(creds, dpop_credentials.DPoPCredentials)
        assert creds.dpop_signer is signer
        assert creds.client_id == self.CLIENT_ID
        assert creds.client_secret == self.CLIENT_SECRET
        assert creds.refresh_token == self.REFRESH_TOKEN

    def test_from_authorized_user_info_nonce_from_info(self):
        info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": self.REFRESH_TOKEN,
            "dpop_nonce": "saved-nonce",
        }

        creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(info)

        assert creds.dpop_nonce == "saved-nonce"

    def test_from_authorized_user_info_missing_fields_raises(self):
        info = {
            "client_id": self.CLIENT_ID,
            # Missing client_secret and refresh_token.
        }

        with pytest.raises(ValueError, match="missing"):
            dpop_credentials.DPoPCredentials.from_authorized_user_info(info)

    def test_from_authorized_user_info_thumbprint_mismatch_raises(self):
        signer = self.make_dpop_signer()
        wrong_key = ec.generate_private_key(ec.SECP256R1())
        wrong_signer = SoftwareDPoPSigner(wrong_key)
        info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": self.REFRESH_TOKEN,
            "dpop_thumbprint": signer.thumbprint,
        }

        with pytest.raises(ValueError, match="does not match"):
            dpop_credentials.DPoPCredentials.from_authorized_user_info(
                info, dpop_signer=wrong_signer
            )

    def test_from_authorized_user_info_thumbprint_match_succeeds(self):
        signer = self.make_dpop_signer()
        info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": self.REFRESH_TOKEN,
            "dpop_thumbprint": signer.thumbprint,
        }

        creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
            info, dpop_signer=signer
        )

        assert creds.dpop_signer is signer

    def test_from_authorized_user_info_no_saved_thumbprint_skips_check(self):
        signer = self.make_dpop_signer()
        info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": self.REFRESH_TOKEN,
        }

        creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
            info, dpop_signer=signer
        )

        assert creds.dpop_signer is signer

    def test_from_authorized_user_info_with_callable_factory_match(self):
        signer = self.make_dpop_signer()
        factory_called = [0]

        def factory():
            factory_called[0] += 1
            return signer

        info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": self.REFRESH_TOKEN,
            "dpop_thumbprint": signer.thumbprint,
        }

        creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
            info, dpop_signer=factory
        )

        assert factory_called[0] == 0
        assert creds.dpop_signer is signer
        assert factory_called[0] == 1

    def test_from_authorized_user_info_with_callable_factory_mismatch_raises(self):
        signer = self.make_dpop_signer()
        wrong_key = ec.generate_private_key(ec.SECP256R1())
        wrong_signer = SoftwareDPoPSigner(wrong_key)

        info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": self.REFRESH_TOKEN,
            "dpop_thumbprint": signer.thumbprint,
        }

        creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
            info, dpop_signer=lambda: wrong_signer
        )

        with pytest.raises(ValueError, match="does not match"):
            _ = creds.dpop_signer

    def test_from_authorized_user_info_with_callable_factory_no_saved_thumbprint(self):
        signer = self.make_dpop_signer()
        info = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": self.REFRESH_TOKEN,
        }

        creds = dpop_credentials.DPoPCredentials.from_authorized_user_info(
            info, dpop_signer=lambda: signer
        )

        assert creds.dpop_signer is signer

    def test_from_authorized_user_file_with_callable_factory(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write(creds.to_json())
            tmp_path = f.name

        try:
            loaded = dpop_credentials.DPoPCredentials.from_authorized_user_file(
                tmp_path, dpop_signer=lambda: signer
            )
            assert loaded.dpop_signer is signer
        finally:
            os.remove(tmp_path)

    # ------------------------------------------------------------------
    # from_authorized_user_file()
    # ------------------------------------------------------------------

    def test_from_authorized_user_file_roundtrip(self):
        signer = self.make_dpop_signer()
        creds = self.make_credentials(dpop_signer=signer, dpop_nonce="roundtrip-nonce")

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write(creds.to_json())
            tmp_path = f.name

        try:
            loaded = dpop_credentials.DPoPCredentials.from_authorized_user_file(
                tmp_path, dpop_signer=signer
            )

            assert isinstance(loaded, dpop_credentials.DPoPCredentials)
            assert loaded.dpop_signer is signer
            assert loaded.dpop_nonce == "roundtrip-nonce"
            assert loaded.client_id == self.CLIENT_ID
            assert loaded.client_secret == self.CLIENT_SECRET
            assert loaded.refresh_token == self.REFRESH_TOKEN
        finally:
            os.unlink(tmp_path)


class TestExtractDpopNonce(object):
    """Tests for dpop.extract_dpop_nonce() helper."""

    def test_extracts_nonce_exact_case(self):
        headers = {"DPoP-Nonce": "abc"}

        result = dpop.extract_dpop_nonce(headers)

        assert result == "abc"

    def test_extracts_nonce_lowercase(self):
        headers = {"dpop-nonce": "abc"}

        result = dpop.extract_dpop_nonce(headers)

        assert result == "abc"

    def test_returns_none_when_absent(self):
        headers = {"other": "header"}

        result = dpop.extract_dpop_nonce(headers)

        assert result is None

    def test_returns_none_for_empty_headers(self):
        result = dpop.extract_dpop_nonce({})

        assert result is None

    def test_returns_none_for_none(self):
        result = dpop.extract_dpop_nonce(None)

        assert result is None


class TestTokenEndpointRequestNoThrowWithResponseHeaders(object):
    """Tests for the return_response_headers flag on
    _client._token_endpoint_request_no_throw.
    """

    @classmethod
    def _make_mock_response(cls, status=200, data=None, headers=None):
        """Create a mock HTTP response object."""
        response = mock.Mock()
        response.status = status
        body = json.dumps(data or {}).encode("utf-8")
        response.data = body
        response.headers = headers or {}
        return response

    def test_returns_3_tuple_by_default(self):
        request = mock.create_autospec(transport.Request)
        request.return_value = self._make_mock_response(
            status=200,
            data={"access_token": "tok"},
            headers={"X-Custom": "val"},
        )

        result = _client._token_endpoint_request_no_throw(
            request,
            _TOKEN_URI,
            {"grant_type": "authorization_code"},
        )

        # Default: 3-tuple (success, data, retryable_error).
        assert len(result) == 3
        assert result[0] is True
        assert result[1]["access_token"] == "tok"

    def test_returns_4_tuple_when_requested(self):
        response_headers = {"DPoP-Nonce": "server-nonce", "X-Other": "value"}
        request = mock.create_autospec(transport.Request)
        request.return_value = self._make_mock_response(
            status=200,
            data={"access_token": "tok"},
            headers=response_headers,
        )

        result = _client._token_endpoint_request_no_throw(
            request,
            _TOKEN_URI,
            {"grant_type": "authorization_code"},
            return_response_headers=True,
        )

        # With return_response_headers=True: 4-tuple.
        assert len(result) == 4
        assert result[0] is True
        assert result[1]["access_token"] == "tok"
        assert result[2] is None
        assert result[3]["DPoP-Nonce"] == "server-nonce"

    def test_response_headers_on_error(self):
        error_headers = {"DPoP-Nonce": "error-nonce"}
        request = mock.create_autospec(transport.Request)
        request.return_value = self._make_mock_response(
            status=400,
            data={"error": "invalid_grant"},
            headers=error_headers,
        )

        result = _client._token_endpoint_request_no_throw(
            request,
            _TOKEN_URI,
            {"grant_type": "authorization_code"},
            return_response_headers=True,
            can_retry=False,
        )

        assert len(result) == 4
        assert result[0] is False
        assert result[1]["error"] == "invalid_grant"
        assert result[3]["DPoP-Nonce"] == "error-nonce"
