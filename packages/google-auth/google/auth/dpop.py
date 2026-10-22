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

"""Demonstrating Proof-of-Possession (DPoP) support per RFC 9449.

This module provides the abstract base class :class:`DPoPSigner` and a
concrete implementation :class:`SoftwareDPoPSigner`, as well as
cryptographic helpers for creating DPoP proof JWTs and computing
RFC 7638 JWK thumbprints.

Third-party keystores (such as hardware tokens, TPMs, YubiKeys,
PKCS#11 devices, or cloud KMS) can be integrated by subclassing
:class:`DPoPSigner` and implementing its :attr:`algorithm`,
:attr:`public_jwk`, and :meth:`sign` methods.
"""

import abc
import hashlib
import json
import time
import urllib.parse
import uuid

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa
from cryptography.hazmat.primitives.asymmetric.utils import (
    decode_dss_signature,
    encode_dss_signature,
)

from google.auth import _helpers, exceptions


def compute_jwk_thumbprint(jwk):
    """Computes the RFC 7638 SHA-256 JSON Web Key (JWK) Thumbprint.

    The thumbprint is calculated by canonicalizing the required public
    key members in lexicographical order, encoding as UTF-8 JSON with no
    extra whitespace, and computing the unpadded URL-safe base64 SHA-256
    hash.

    Args:
        jwk (Mapping[str, Any]): The public JWK dictionary.

    Returns:
        str: The base64url-encoded SHA-256 thumbprint (used for
        ``dpop_jkt``).

    Raises:
        google.auth.exceptions.InvalidValue: If the JWK is missing
            required fields for its key type.
    """
    kty = jwk.get("kty")
    if kty == "EC":
        required = ["crv", "kty", "x", "y"]
    elif kty == "RSA":
        required = ["e", "kty", "n"]
    else:
        raise exceptions.InvalidValue(
            "Unsupported key type '{}' for JWK thumbprint calculation.".format(kty)
        )

    for field in required:
        if field not in jwk:
            raise exceptions.InvalidValue(
                "JWK is missing required field '{}' for key type '{}'.".format(
                    field, kty
                )
            )

    canonical_dict = {field: jwk[field] for field in required}
    canonical_json = json.dumps(
        canonical_dict, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")

    digest = hashlib.sha256(canonical_json).digest()
    return _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")


def compute_access_token_hash(access_token):
    """Computes the RFC 9449 access token hash (``ath`` claim).

    The ``ath`` claim value is the unpadded base64url encoding of the
    SHA-256 hash of the ASCII-encoded access token string.

    Args:
        access_token (Union[str, bytes]): The access token.

    Returns:
        str: Base64url-encoded SHA-256 hash of the token.
    """
    token_bytes = _helpers.to_bytes(access_token)
    digest = hashlib.sha256(token_bytes).digest()
    return _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")


def compute_auth_code_jti(code):
    """Computes the DPoP ``jti`` claim for authorization code exchange.

    Google's DPoP implementation requires
    ``jti = BASE64URL(SHA-256(code))`` for authorization code exchanges
    to cryptographically bind the proof to the issued authorization code.

    Args:
        code (Union[str, bytes]): The authorization code received from
            Google.

    Returns:
        str: Unpadded Base64URL-encoded SHA-256 hash of the
        authorization code.
    """
    code_bytes = _helpers.to_bytes(code)
    digest = hashlib.sha256(code_bytes).digest()
    return _helpers.unpadded_urlsafe_b64encode(digest).decode("ascii")


def normalize_dpop_url(url):
    """Normalizes a URL for the DPoP ``htu`` claim per RFC 9449 §4.3.

    The URL is normalized to lowercase scheme and host, with the path
    preserved and any query string or fragment stripped.

    Args:
        url (str): The target HTTP URI.

    Returns:
        str: The normalized URI without query parameters or fragment.
    """
    parsed = urllib.parse.urlsplit(url)
    scheme = parsed.scheme.lower()
    netloc = parsed.netloc.lower()
    path = parsed.path or "/"
    return urllib.parse.urlunsplit((scheme, netloc, path, "", ""))


def der_to_raw_ecdsa_signature(der_signature, curve_byte_size=32):
    """Converts an ASN.1 DER ECDSA signature to raw (R || S) JWS format.

    Many hardware keystores, PKCS#11 libraries, and OS security APIs
    output ECDSA signatures in ASN.1 DER format.  JWS (RFC 7515
    Section 3.4) and DPoP mandate raw (R || S) signature bytes.

    Args:
        der_signature (bytes): The ASN.1 DER-encoded ECDSA signature.
        curve_byte_size (int): The coordinate size in bytes (32 for
            P-256/ES256, 48 for P-384/ES384).  Default is 32.

    Returns:
        bytes: Raw (R || S) concatenated byte signature of length
        ``2 * curve_byte_size``.
    """
    r, s = decode_dss_signature(der_signature)
    return r.to_bytes(curve_byte_size, byteorder="big") + s.to_bytes(
        curve_byte_size, byteorder="big"
    )


def raw_to_der_ecdsa_signature(raw_signature):
    """Converts a raw (R || S) ECDSA signature to ASN.1 DER format.

    Args:
        raw_signature (bytes): The raw concatenated (R || S) signature.

    Returns:
        bytes: ASN.1 DER-encoded signature.
    """
    half_len = len(raw_signature) // 2
    r = int.from_bytes(raw_signature[:half_len], byteorder="big")
    s = int.from_bytes(raw_signature[half_len:], byteorder="big")
    return encode_dss_signature(r, s)


class DPoPSigner(metaclass=abc.ABCMeta):
    """Abstract base class for DPoP signers.

    This interface allows custom keystore backends — such as TPMs,
    YubiKeys, smart cards (PKCS#11), Apple Secure Enclave, Windows CNG,
    or Cloud KMS — to supply DPoP signatures without exposing private
    key material.
    """

    @property
    @abc.abstractmethod
    def algorithm(self):
        """str: The JWS signing algorithm (e.g. ``'ES256'``, ``'RS256'``)."""
        raise NotImplementedError("Derived classes must implement algorithm")

    @property
    @abc.abstractmethod
    def public_jwk(self):
        """Mapping[str, Any]: The public key as an RFC 7517 JWK dict.

        Must NOT contain any private key components (e.g. ``'d'``,
        ``'p'``, ``'q'``).
        """
        raise NotImplementedError("Derived classes must implement public_jwk")

    @property
    def key_id(self):
        """Optional[str]: An identifier for this key."""
        return None  # pragma: NO COVER

    @property
    def thumbprint(self):
        """str: RFC 7638 SHA-256 JWK thumbprint."""
        return compute_jwk_thumbprint(self.public_jwk)

    @abc.abstractmethod
    def sign(self, data):
        """Signs the input bytes.

        For ECDSA algorithms (e.g. ES256), the return value MUST be raw
        concatenated (R || S) bytes per RFC 7515 Section 3.4 (e.g. 64
        bytes for P-256), not ASN.1 DER.  See
        :func:`der_to_raw_ecdsa_signature`.

        Args:
            data (bytes): The ASCII data to sign (typically
                ``b'<b64url_header>.<b64url_payload>'``).

        Returns:
            bytes: The signature bytes.
        """
        raise NotImplementedError("Derived classes must implement sign")

    def create_proof(
        self,
        method,
        url,
        nonce=None,
        access_token=None,
        jti=None,
        extra_claims=None,
    ):
        """Creates a signed RFC 9449 DPoP proof JWT.

        Args:
            method (str): The HTTP method (e.g. ``'POST'``, ``'GET'``).
            url (str): The target HTTP URI.
            nonce (Optional[str]): A server-provided DPoP nonce, if
                available.
            access_token (Optional[Union[str, bytes]]): The access token
                to bind via the ``ath`` claim per RFC 9449 §4.3.
                Google resource servers currently ignore this header
                entirely; it is included for forward compatibility.
            jti (Optional[str]): Explicit unique JWT ID.  If omitted, a
                random UUIDv4 is generated.  For Google OAuth code
                exchange, this MUST be ``compute_auth_code_jti(code)``.
            extra_claims (Optional[Mapping[str, Any]]): Additional
                custom claims to include in the payload.

        Returns:
            str: The compact serialized DPoP proof JWT
            (``<header>.<payload>.<sig>``).
        """
        header = {
            "typ": "dpop+jwt",
            "alg": self.algorithm,
            "jwk": dict(self.public_jwk),
        }

        payload = {
            "jti": jti or str(uuid.uuid4()),
            "htm": method.upper(),
            "htu": normalize_dpop_url(url),
            "iat": int(time.time()),
        }

        if nonce:
            payload["nonce"] = nonce

        if access_token:
            payload["ath"] = compute_access_token_hash(access_token)

        if extra_claims:
            payload.update(extra_claims)

        header_b64 = _helpers.unpadded_urlsafe_b64encode(
            json.dumps(header, separators=(",", ":")).encode("utf-8")
        )
        payload_b64 = _helpers.unpadded_urlsafe_b64encode(
            json.dumps(payload, separators=(",", ":")).encode("utf-8")
        )

        signing_input = header_b64 + b"." + payload_b64
        signature = self.sign(signing_input)
        sig_b64 = _helpers.unpadded_urlsafe_b64encode(signature)

        return (header_b64 + b"." + payload_b64 + b"." + sig_b64).decode("ascii")


class SoftwareDPoPSigner(DPoPSigner):
    """Concrete software-backed DPoP signer using ``cryptography``.

    Supports NIST curves (P-256 for ES256, P-384 for ES384) and RSA
    (RS256).

    The private key must be created externally and supplied either as a
    ``cryptography`` key object (via the constructor) or as PEM data
    (via :meth:`from_pem`).

    .. tip:: Generating a key with ``openssl``

        .. code-block:: bash

            # ES256 (recommended)
            openssl ecparam -name prime256v1 -genkey -noout \\
                -out dpop_key.pem

            # ES384
            openssl ecparam -name secp384r1 -genkey -noout \\
                -out dpop_key.pem

            # RS256
            openssl genrsa -out dpop_key.pem 2048

    .. note::

        For production deployments, prefer a hardware-backed signer
        (YubiKey, TPM, Cloud KMS) by subclassing :class:`DPoPSigner`.
        Software keys are suitable for development and testing.

    Args:
        private_key (Union[ec.EllipticCurvePrivateKey,
            rsa.RSAPrivateKey]): The private key.
        key_id (Optional[str]): An optional key identifier.

    Raises:
        google.auth.exceptions.InvalidValue: If the key type or curve
            is not supported.
    """

    def __init__(self, private_key, key_id=None):
        """
        Args:
            private_key (Union[ec.EllipticCurvePrivateKey,
                rsa.RSAPrivateKey]): The private key.
            key_id (Optional[str]): An optional key identifier.
        """
        self._private_key = private_key
        self._key_id = key_id

        if isinstance(private_key, ec.EllipticCurvePrivateKey):
            curve = private_key.curve
            if isinstance(curve, ec.SECP256R1):
                self._alg = "ES256"
                self._crv_size = 32
                crv_name = "P-256"
            elif isinstance(curve, ec.SECP384R1):
                self._alg = "ES384"
                self._crv_size = 48
                crv_name = "P-384"
            else:
                raise exceptions.InvalidValue(
                    "Unsupported elliptic curve: {}".format(curve.name)
                )

            pub_numbers = private_key.public_key().public_numbers()
            x_bytes = pub_numbers.x.to_bytes(self._crv_size, byteorder="big")
            y_bytes = pub_numbers.y.to_bytes(self._crv_size, byteorder="big")

            self._public_jwk = {
                "kty": "EC",
                "crv": crv_name,
                "x": _helpers.unpadded_urlsafe_b64encode(x_bytes).decode("ascii"),
                "y": _helpers.unpadded_urlsafe_b64encode(y_bytes).decode("ascii"),
            }
        elif isinstance(private_key, rsa.RSAPrivateKey):
            self._alg = "RS256"
            self._crv_size = None
            pub_numbers = private_key.public_key().public_numbers()
            e_bytes = pub_numbers.e.to_bytes(
                (pub_numbers.e.bit_length() + 7) // 8, byteorder="big"
            )
            n_bytes = pub_numbers.n.to_bytes(
                (pub_numbers.n.bit_length() + 7) // 8, byteorder="big"
            )

            self._public_jwk = {
                "kty": "RSA",
                "n": _helpers.unpadded_urlsafe_b64encode(n_bytes).decode("ascii"),
                "e": _helpers.unpadded_urlsafe_b64encode(e_bytes).decode("ascii"),
            }
        else:
            raise exceptions.InvalidValue(
                "Unsupported private key type: {}".format(type(private_key))
            )

    @property
    def algorithm(self):
        """str: The JWS signing algorithm name."""
        return self._alg

    @property
    def public_jwk(self):
        """Mapping[str, Any]: The public JWK dictionary."""
        return self._public_jwk

    @property
    def key_id(self):
        """Optional[str]: The key identifier."""
        return self._key_id

    @property
    def private_key(self):
        """Union[ec.EllipticCurvePrivateKey, rsa.RSAPrivateKey]: The
        underlying private key object."""
        return self._private_key

    def sign(self, data):
        """Signs the input bytes using the private key.

        Args:
            data (bytes): The data to sign.

        Returns:
            bytes: The signature bytes (raw R||S for EC, PKCS1v15 for
            RSA).

        Raises:
            google.auth.exceptions.InvalidValue: If the private key
                type is not supported.
        """
        if isinstance(self._private_key, ec.EllipticCurvePrivateKey):
            sha_algo = hashes.SHA256() if self._alg == "ES256" else hashes.SHA384()
            der_sig = self._private_key.sign(data, ec.ECDSA(sha_algo))
            return der_to_raw_ecdsa_signature(der_sig, self._crv_size)
        elif isinstance(self._private_key, rsa.RSAPrivateKey):
            return self._private_key.sign(
                data,
                padding.PKCS1v15(),
                hashes.SHA256(),
            )
        else:
            raise exceptions.InvalidValue(
                "Unsupported private key type for signing."
            )  # pragma: NO COVER

    @classmethod
    def from_pem(cls, pem_bytes, password=None, key_id=None):
        """Loads a signer from PEM-encoded private key data.

        Args:
            pem_bytes (Union[str, bytes]): The PEM private key data.
            password (Optional[bytes]): Passphrase if the key is
                encrypted.
            key_id (Optional[str]): Optional key identifier.

        Returns:
            SoftwareDPoPSigner: The constructed signer.

        Raises:
            google.auth.exceptions.InvalidValue: If the loaded key is
                not an EC or RSA private key.
        """
        pem_data = _helpers.to_bytes(pem_bytes)
        key = serialization.load_pem_private_key(pem_data, password=password)
        if not isinstance(
            key,
            (
                ec.EllipticCurvePrivateKey,
                rsa.RSAPrivateKey,
            ),
        ):
            raise exceptions.InvalidValue(
                "Loaded key must be an EC or RSA private key, got {}".format(type(key))
            )
        return cls(key, key_id=key_id)


def extract_dpop_nonce(headers):
    """Extracts the ``DPoP-Nonce`` header value (case-insensitive).

    Args:
        headers (Mapping[str, str]): HTTP response headers.

    Returns:
        Optional[str]: The nonce value, or ``None`` if not present.
    """
    if not headers:
        return None
    for key in headers:
        if key.lower() == "dpop-nonce":
            return headers[key]
    return None
