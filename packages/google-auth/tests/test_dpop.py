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
import hashlib
import json
import unittest.mock as mock

import pytest
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa

from google.auth import _helpers, dpop, exceptions

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _b64url_decode(data):
    """Base64url-decode without padding."""
    if isinstance(data, str):
        data = data.encode("ascii")
    padding_needed = 4 - len(data) % 4
    if padding_needed != 4:
        data += b"=" * padding_needed
    return base64.urlsafe_b64decode(data)


def _decode_jwt(token):
    """Decode a compact JWT into (header_dict, payload_dict, sig_bytes)."""
    parts = token.split(".")
    header = json.loads(_b64url_decode(parts[0]))
    payload = json.loads(_b64url_decode(parts[1]))
    signature = _b64url_decode(parts[2])
    return header, payload, signature


# ---------------------------------------------------------------------------
# Test classes
# ---------------------------------------------------------------------------


class TestComputeJwkThumbprint(object):
    """Tests for :func:`dpop.compute_jwk_thumbprint`."""

    @classmethod
    def make_ec256_signer(cls):
        key = ec.generate_private_key(ec.SECP256R1())
        return dpop.SoftwareDPoPSigner(key)

    @classmethod
    def make_ec384_signer(cls):
        key = ec.generate_private_key(ec.SECP384R1())
        return dpop.SoftwareDPoPSigner(key)

    @classmethod
    def make_rsa_signer(cls):
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        return dpop.SoftwareDPoPSigner(key)

    def test_ec256_thumbprint_matches_manual_computation(self):
        signer = self.make_ec256_signer()
        jwk = signer.public_jwk
        # Manually compute expected thumbprint.
        canonical = {
            "crv": jwk["crv"],
            "kty": jwk["kty"],
            "x": jwk["x"],
            "y": jwk["y"],
        }
        canonical_json = json.dumps(
            canonical, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        digest = hashlib.sha256(canonical_json).digest()
        expected = _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")

        result = dpop.compute_jwk_thumbprint(jwk)
        assert result == expected

    def test_ec384_thumbprint(self):
        signer = self.make_ec384_signer()
        jwk = signer.public_jwk
        result = dpop.compute_jwk_thumbprint(jwk)
        # Thumbprint is a non-empty base64url string.
        assert isinstance(result, str)
        assert len(result) > 0
        # SHA-256 digest is 32 bytes → 43 base64url characters.
        assert len(result) == 43

    def test_rsa_thumbprint(self):
        signer = self.make_rsa_signer()
        jwk = signer.public_jwk
        # Manually compute expected thumbprint using RSA required fields.
        canonical = {
            "e": jwk["e"],
            "kty": jwk["kty"],
            "n": jwk["n"],
        }
        canonical_json = json.dumps(
            canonical, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        digest = hashlib.sha256(canonical_json).digest()
        expected = _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")

        result = dpop.compute_jwk_thumbprint(jwk)
        assert result == expected

    def test_missing_required_field_raises(self):
        # An EC JWK missing the "x" field.
        jwk = {"kty": "EC", "crv": "P-256", "y": "some_y_value"}
        with pytest.raises(exceptions.InvalidValue, match="missing required"):
            dpop.compute_jwk_thumbprint(jwk)

    def test_unsupported_key_type_raises(self):
        jwk = {"kty": "OKP", "crv": "Ed25519", "x": "abc"}
        with pytest.raises(exceptions.InvalidValue, match="Unsupported key type"):
            dpop.compute_jwk_thumbprint(jwk)

    def test_none_key_type_raises(self):
        jwk = {"crv": "P-256", "x": "abc", "y": "def"}
        with pytest.raises(exceptions.InvalidValue, match="Unsupported key type"):
            dpop.compute_jwk_thumbprint(jwk)


class TestComputeAccessTokenHash(object):
    """Tests for :func:`dpop.compute_access_token_hash`."""

    def test_known_token_hash(self):
        token = "test-access-token-12345"
        digest = hashlib.sha256(token.encode("ascii")).digest()
        expected = _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")
        result = dpop.compute_access_token_hash(token)
        assert result == expected

    def test_bytes_input(self):
        token = b"bytes-access-token"
        digest = hashlib.sha256(token).digest()
        expected = _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")
        result = dpop.compute_access_token_hash(token)
        assert result == expected

    def test_hash_is_base64url_string(self):
        result = dpop.compute_access_token_hash("some-token")
        assert isinstance(result, str)
        # Should be 43 characters (256 bits base64url without padding).
        assert len(result) == 43


class TestComputeAuthCodeJti(object):
    """Tests for :func:`dpop.compute_auth_code_jti`."""

    def test_known_code_hash(self):
        code = "4/0AQSTgQF_auth_code_example"
        digest = hashlib.sha256(code.encode("ascii")).digest()
        expected = _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")
        result = dpop.compute_auth_code_jti(code)
        assert result == expected

    def test_bytes_input(self):
        code = b"auth-code-bytes"
        digest = hashlib.sha256(code).digest()
        expected = _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")
        result = dpop.compute_auth_code_jti(code)
        assert result == expected


class TestNormalizeDpopUrl(object):
    """Tests for :func:`dpop.normalize_dpop_url`."""

    def test_strips_query_string(self):
        url = "https://example.com/path?foo=bar&baz=qux"
        result = dpop.normalize_dpop_url(url)
        assert result == "https://example.com/path"

    def test_strips_fragment(self):
        url = "https://example.com/path#section"
        result = dpop.normalize_dpop_url(url)
        assert result == "https://example.com/path"

    def test_lowercases_scheme_and_host(self):
        url = "HTTPS://Example.COM/Path"
        result = dpop.normalize_dpop_url(url)
        assert result == "https://example.com/Path"

    def test_preserves_path(self):
        url = "https://example.com/api/v1/Resource"
        result = dpop.normalize_dpop_url(url)
        assert result == "https://example.com/api/v1/Resource"

    def test_adds_trailing_slash_when_path_empty(self):
        url = "https://example.com"
        result = dpop.normalize_dpop_url(url)
        assert result == "https://example.com/"

    def test_strips_query_and_fragment_together(self):
        url = "https://example.com/path?q=1#frag"
        result = dpop.normalize_dpop_url(url)
        assert result == "https://example.com/path"

    def test_preserves_port(self):
        url = "https://example.com:8443/resource"
        result = dpop.normalize_dpop_url(url)
        assert result == "https://example.com:8443/resource"


class TestDerRawEcdsaConversion(object):
    """Tests for DER ↔ raw ECDSA signature conversion."""

    @classmethod
    def make_ec256_key(cls):
        return ec.generate_private_key(ec.SECP256R1())

    @classmethod
    def make_ec384_key(cls):
        return ec.generate_private_key(ec.SECP384R1())

    def test_roundtrip_p256(self):
        key = self.make_ec256_key()
        data = b"test data to sign"
        der_sig = key.sign(data, ec.ECDSA(hashes.SHA256()))
        raw_sig = dpop.der_to_raw_ecdsa_signature(der_sig, 32)
        der_sig_again = dpop.raw_to_der_ecdsa_signature(raw_sig)
        raw_sig_again = dpop.der_to_raw_ecdsa_signature(der_sig_again, 32)
        assert raw_sig == raw_sig_again

    def test_roundtrip_p384(self):
        key = self.make_ec384_key()
        data = b"test data to sign"
        der_sig = key.sign(data, ec.ECDSA(hashes.SHA384()))
        raw_sig = dpop.der_to_raw_ecdsa_signature(der_sig, 48)
        der_sig_again = dpop.raw_to_der_ecdsa_signature(raw_sig)
        raw_sig_again = dpop.der_to_raw_ecdsa_signature(der_sig_again, 48)
        assert raw_sig == raw_sig_again

    def test_p256_raw_length(self):
        key = self.make_ec256_key()
        data = b"hello"
        der_sig = key.sign(data, ec.ECDSA(hashes.SHA256()))
        raw_sig = dpop.der_to_raw_ecdsa_signature(der_sig, 32)
        assert len(raw_sig) == 64

    def test_p384_raw_length(self):
        key = self.make_ec384_key()
        data = b"hello"
        der_sig = key.sign(data, ec.ECDSA(hashes.SHA384()))
        raw_sig = dpop.der_to_raw_ecdsa_signature(der_sig, 48)
        assert len(raw_sig) == 96

    def test_der_roundtrip_verifies(self):
        """Verify that a DER→raw→DER signature still passes verification."""
        key = self.make_ec256_key()
        data = b"verify me"
        der_sig = key.sign(data, ec.ECDSA(hashes.SHA256()))
        raw_sig = dpop.der_to_raw_ecdsa_signature(der_sig, 32)
        der_sig_back = dpop.raw_to_der_ecdsa_signature(raw_sig)
        # Should not raise.
        key.public_key().verify(der_sig_back, data, ec.ECDSA(hashes.SHA256()))


class TestDPoPSigner(object):
    """Tests for the abstract :class:`dpop.DPoPSigner`."""

    def test_cannot_instantiate_directly(self):
        with pytest.raises(TypeError):
            dpop.DPoPSigner()

    def test_thumbprint_property_uses_compute_jwk_thumbprint(self):
        """thumbprint delegates to compute_jwk_thumbprint."""
        ec_key = ec.generate_private_key(ec.SECP256R1())
        signer = dpop.SoftwareDPoPSigner(ec_key)
        expected = dpop.compute_jwk_thumbprint(signer.public_jwk)
        assert signer.thumbprint == expected

    def test_key_id_defaults_to_none(self):
        ec_key = ec.generate_private_key(ec.SECP256R1())
        signer = dpop.SoftwareDPoPSigner(ec_key)
        assert signer.key_id is None


class TestSoftwareDPoPSigner(object):
    """Tests for :class:`dpop.SoftwareDPoPSigner`."""

    @classmethod
    def make_ec256_key(cls):
        return ec.generate_private_key(ec.SECP256R1())

    @classmethod
    def make_ec384_key(cls):
        return ec.generate_private_key(ec.SECP384R1())

    @classmethod
    def make_rsa_key(cls):
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

    # -- ES256 ---------------------------------------------------------------

    def test_es256_algorithm(self):
        signer = dpop.SoftwareDPoPSigner(self.make_ec256_key())
        assert signer.algorithm == "ES256"

    def test_es256_public_jwk_has_required_fields(self):
        signer = dpop.SoftwareDPoPSigner(self.make_ec256_key())
        jwk = signer.public_jwk
        assert jwk["kty"] == "EC"
        assert jwk["crv"] == "P-256"
        assert "x" in jwk
        assert "y" in jwk
        # Must NOT contain private key material.
        assert "d" not in jwk

    def test_es256_sign_produces_valid_output(self):
        key = self.make_ec256_key()
        signer = dpop.SoftwareDPoPSigner(key)
        data = b"data to sign"
        sig = signer.sign(data)
        # Raw R||S for P-256 must be 64 bytes.
        assert len(sig) == 64

    def test_es256_sign_verify_roundtrip(self):
        key = self.make_ec256_key()
        signer = dpop.SoftwareDPoPSigner(key)
        data = b"roundtrip test data"
        raw_sig = signer.sign(data)
        der_sig = dpop.raw_to_der_ecdsa_signature(raw_sig)
        # Should not raise.
        key.public_key().verify(der_sig, data, ec.ECDSA(hashes.SHA256()))

    # -- ES384 ---------------------------------------------------------------

    def test_es384_algorithm(self):
        signer = dpop.SoftwareDPoPSigner(self.make_ec384_key())
        assert signer.algorithm == "ES384"

    def test_es384_public_jwk_curve(self):
        signer = dpop.SoftwareDPoPSigner(self.make_ec384_key())
        assert signer.public_jwk["crv"] == "P-384"

    def test_es384_sign_length(self):
        key = self.make_ec384_key()
        signer = dpop.SoftwareDPoPSigner(key)
        sig = signer.sign(b"data")
        # Raw R||S for P-384 must be 96 bytes.
        assert len(sig) == 96

    # -- RS256 ---------------------------------------------------------------

    def test_rs256_algorithm(self):
        signer = dpop.SoftwareDPoPSigner(self.make_rsa_key())
        assert signer.algorithm == "RS256"

    def test_rs256_public_jwk_has_required_fields(self):
        signer = dpop.SoftwareDPoPSigner(self.make_rsa_key())
        jwk = signer.public_jwk
        assert jwk["kty"] == "RSA"
        assert "n" in jwk
        assert "e" in jwk
        # Must NOT contain private key material.
        assert "d" not in jwk
        assert "p" not in jwk
        assert "q" not in jwk

    def test_rs256_sign_produces_output(self):
        key = self.make_rsa_key()
        signer = dpop.SoftwareDPoPSigner(key)
        sig = signer.sign(b"data")
        assert len(sig) > 0

    def test_rs256_sign_verify_roundtrip(self):
        key = self.make_rsa_key()
        signer = dpop.SoftwareDPoPSigner(key)
        data = b"roundtrip rsa test"
        sig = signer.sign(data)
        # Should not raise.
        key.public_key().verify(sig, data, padding.PKCS1v15(), hashes.SHA256())

    # -- Unsupported key types / curves --------------------------------------

    def test_unsupported_curve_raises(self):
        key = ec.generate_private_key(ec.SECP521R1())
        with pytest.raises(exceptions.InvalidValue, match="Unsupported"):
            dpop.SoftwareDPoPSigner(key)

    def test_unsupported_key_type_raises(self):
        from cryptography.hazmat.primitives.asymmetric import ed25519

        key = ed25519.Ed25519PrivateKey.generate()
        with pytest.raises(exceptions.InvalidValue, match="Unsupported"):
            dpop.SoftwareDPoPSigner(key)

    # -- from_pem ------------------------------------------------------------

    def test_from_pem_ec_key(self):
        key = self.make_ec256_key()
        pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        signer = dpop.SoftwareDPoPSigner.from_pem(pem)
        assert signer.algorithm == "ES256"
        assert signer.public_jwk["kty"] == "EC"

    def test_from_pem_rsa_key(self):
        key = self.make_rsa_key()
        pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        signer = dpop.SoftwareDPoPSigner.from_pem(pem)
        assert signer.algorithm == "RS256"
        assert signer.public_jwk["kty"] == "RSA"

    def test_from_pem_rejects_unsupported_key_type(self):
        from cryptography.hazmat.primitives.asymmetric import ed25519

        key = ed25519.Ed25519PrivateKey.generate()
        pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        with pytest.raises(exceptions.InvalidValue, match="EC or RSA"):
            dpop.SoftwareDPoPSigner.from_pem(pem)

    def test_from_pem_password_protected(self):
        key = self.make_ec256_key()
        password = b"test-password-123"
        pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password),
        )
        signer = dpop.SoftwareDPoPSigner.from_pem(pem, password=password)
        assert signer.algorithm == "ES256"

    def test_from_pem_string_input(self):
        key = self.make_ec256_key()
        pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        # Pass as str instead of bytes.
        signer = dpop.SoftwareDPoPSigner.from_pem(pem.decode("utf-8"))
        assert signer.algorithm == "ES256"

    def test_from_pem_with_key_id(self):
        key = self.make_ec256_key()
        pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        signer = dpop.SoftwareDPoPSigner.from_pem(pem, key_id="my-key-id")
        assert signer.key_id == "my-key-id"

    # -- Properties ----------------------------------------------------------

    def test_key_id_property(self):
        key = self.make_ec256_key()
        signer = dpop.SoftwareDPoPSigner(key, key_id="kid-123")
        assert signer.key_id == "kid-123"

    def test_key_id_default_none(self):
        key = self.make_ec256_key()
        signer = dpop.SoftwareDPoPSigner(key)
        assert signer.key_id is None

    def test_private_key_property(self):
        key = self.make_ec256_key()
        signer = dpop.SoftwareDPoPSigner(key)
        assert signer.private_key is key


class TestCreateProof(object):
    """Tests for :meth:`dpop.DPoPSigner.create_proof`."""

    FIXED_TIME = 1700000000
    FIXED_UUID = "test-uuid-1234-5678"

    @classmethod
    def make_ec256_signer(cls):
        key = ec.generate_private_key(ec.SECP256R1())
        return dpop.SoftwareDPoPSigner(key)

    @classmethod
    def make_rsa_signer(cls):
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        return dpop.SoftwareDPoPSigner(key)

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_creates_valid_jwt_structure(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof("POST", "https://example.com/token")
        parts = proof.split(".")
        assert len(parts) == 3
        # Each part should be non-empty.
        for part in parts:
            assert len(part) > 0

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_header_has_correct_fields(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof("POST", "https://example.com/token")
        header, _, _ = _decode_jwt(proof)
        assert header["typ"] == "dpop+jwt"
        assert header["alg"] == "ES256"
        assert "jwk" in header
        assert header["jwk"]["kty"] == "EC"
        assert header["jwk"]["crv"] == "P-256"
        assert "x" in header["jwk"]
        assert "y" in header["jwk"]

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_payload_has_required_fields(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof("POST", "https://example.com/token")
        _, payload, _ = _decode_jwt(proof)
        assert payload["jti"] == self.FIXED_UUID
        assert payload["htm"] == "POST"
        assert payload["htu"] == "https://example.com/token"
        assert payload["iat"] == self.FIXED_TIME

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_htm_is_uppercased(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof("post", "https://example.com/token")
        _, payload, _ = _decode_jwt(proof)
        assert payload["htm"] == "POST"

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_nonce_included_when_provided(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof(
            "POST",
            "https://example.com/token",
            nonce="server-nonce-xyz",
        )
        _, payload, _ = _decode_jwt(proof)
        assert payload["nonce"] == "server-nonce-xyz"

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_nonce_absent_when_not_provided(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof("POST", "https://example.com/token")
        _, payload, _ = _decode_jwt(proof)
        assert "nonce" not in payload

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_access_token_hash_included(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        access_token = "my-access-token"
        proof = signer.create_proof(
            "GET",
            "https://resource.example.com/api",
            access_token=access_token,
        )
        _, payload, _ = _decode_jwt(proof)
        expected_ath = dpop.compute_access_token_hash(access_token)
        assert payload["ath"] == expected_ath

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_ath_absent_when_no_access_token(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof("POST", "https://example.com/token")
        _, payload, _ = _decode_jwt(proof)
        assert "ath" not in payload

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_extra_claims_included(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof(
            "POST",
            "https://example.com/token",
            extra_claims={"custom_key": "custom_value", "num": 42},
        )
        _, payload, _ = _decode_jwt(proof)
        assert payload["custom_key"] == "custom_value"
        assert payload["num"] == 42

    @mock.patch("time.time", return_value=1700000000)
    def test_custom_jti_is_used(self, mock_time):
        signer = self.make_ec256_signer()
        custom_jti = "my-custom-jti-value"
        proof = signer.create_proof(
            "POST",
            "https://example.com/token",
            jti=custom_jti,
        )
        _, payload, _ = _decode_jwt(proof)
        assert payload["jti"] == custom_jti

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_url_is_normalized_in_htu(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof(
            "POST",
            "HTTPS://Example.COM/token?code=abc#frag",
        )
        _, payload, _ = _decode_jwt(proof)
        assert payload["htu"] == "https://example.com/token"

    def test_signature_verifies_ec256(self):
        """Verify the proof signature using the public key."""
        key = ec.generate_private_key(ec.SECP256R1())
        signer = dpop.SoftwareDPoPSigner(key)
        proof = signer.create_proof("POST", "https://example.com/token")
        parts = proof.split(".")
        signing_input = "{}.{}".format(parts[0], parts[1]).encode("ascii")
        raw_sig = _b64url_decode(parts[2])
        der_sig = dpop.raw_to_der_ecdsa_signature(raw_sig)
        # Should not raise.
        key.public_key().verify(der_sig, signing_input, ec.ECDSA(hashes.SHA256()))

    def test_signature_verifies_rsa(self):
        """Verify the proof signature using the RSA public key."""
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        signer = dpop.SoftwareDPoPSigner(key)
        proof = signer.create_proof("POST", "https://example.com/token")
        parts = proof.split(".")
        signing_input = "{}.{}".format(parts[0], parts[1]).encode("ascii")
        sig = _b64url_decode(parts[2])
        # Should not raise.
        key.public_key().verify(
            sig,
            signing_input,
            padding.PKCS1v15(),
            hashes.SHA256(),
        )

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_rsa_proof_header(self, mock_uuid, mock_time):
        signer = self.make_rsa_signer()
        proof = signer.create_proof("POST", "https://example.com/token")
        header, _, _ = _decode_jwt(proof)
        assert header["typ"] == "dpop+jwt"
        assert header["alg"] == "RS256"
        assert header["jwk"]["kty"] == "RSA"
        assert "n" in header["jwk"]
        assert "e" in header["jwk"]

    @mock.patch("time.time", return_value=1700000000)
    def test_auth_code_jti_flow(self, mock_time):
        """Test code exchange flow with compute_auth_code_jti."""
        signer = self.make_ec256_signer()
        code = "4/0AQSTgQF_some_code"
        jti = dpop.compute_auth_code_jti(code)
        proof = signer.create_proof(
            "POST",
            "https://oauth2.googleapis.com/token",
            jti=jti,
        )
        _, payload, _ = _decode_jwt(proof)
        assert payload["jti"] == jti
        # Verify jti matches the hash of the code.
        expected_jti = dpop.compute_auth_code_jti(code)
        assert payload["jti"] == expected_jti

    @mock.patch("time.time", return_value=1700000000)
    @mock.patch(
        "uuid.uuid4",
        return_value=mock.Mock(__str__=lambda self: "test-uuid-1234-5678"),
    )
    def test_jwk_in_header_matches_signer_public_jwk(self, mock_uuid, mock_time):
        signer = self.make_ec256_signer()
        proof = signer.create_proof("POST", "https://example.com/token")
        header, _, _ = _decode_jwt(proof)
        assert header["jwk"] == signer.public_jwk
