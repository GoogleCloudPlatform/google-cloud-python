# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""OPAQUE protocol cryptographic utilities for Spanner Omni authentication."""

from __future__ import annotations

import hashlib
import hmac
import secrets
from typing import Optional, Tuple

try:
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF
except ImportError as err:
    raise ImportError(
        "The 'cryptography' package is required for Spanner Omni authentication. "
        "Please install it with 'pip install google-cloud-spanner[omni]'."
    ) from err

from google.cloud.spanner_v1.omni.proto import login_pb2

LOGIN_DOMAIN_SEPARATION_TAG = b"Spanner-Omni-Login"
AUTH_KEY_INFO = b"AuthKey"
EXPORT_KEY_INFO = b"ExportKey"
PRIVATE_KEY_INFO = b"PrivateKey"
MASKING_KEY_INFO = b"MaskingKey"
DIFFIE_HELLMAN_KEY_INFO = b"OPAQUE-DeriveDiffieHellmanKeyPair"

NONCE_LENGTH = 32
MAC_TAG_LENGTH = 32
PUBLIC_KEY_LENGTH = 33
EXPECTED_ENVELOPE_SIZE = PUBLIC_KEY_LENGTH + NONCE_LENGTH + MAC_TAG_LENGTH  # 97

# NIST P-256 (secp256r1) Curve Constants
P = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
A = (P - 3) % P
B = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
Z = (P - 10) % P
ORDER = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
GX = 0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296
GY = 0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5
G = (GX, GY)
P_MINUS_1_OVER_2 = (P - 1) // 2
P_PLUS_1_OVER_4 = (P + 1) // 4


def _clear(b: Optional[bytearray]) -> None:
    """Zeroizes a mutable bytearray in place."""
    if b is not None:
        for i in range(len(b)):
            b[i] = 0


def point_add(
    p1: Optional[Tuple[int, int]], p2: Optional[Tuple[int, int]]
) -> Optional[Tuple[int, int]]:
    """Adds two points on the P-256 elliptic curve."""
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        if (y1 + y2) % P == 0:
            return None
        lam = ((3 * x1 * x1 + A) * pow(2 * y1, P - 2, P)) % P
    else:
        lam = ((y2 - y1) * pow(x2 - x1, P - 2, P)) % P
    x3 = (lam * lam - x1 - x2) % P
    y3 = (lam * (x1 - x3) - y1) % P
    return (x3, y3)


def point_mul(pt: Optional[Tuple[int, int]], k: int) -> Optional[Tuple[int, int]]:
    """Multiplies a point on the P-256 elliptic curve by a scalar k."""
    if pt is None or k == 0:
        return None
    res = None
    curr = pt
    while k > 0:
        if k & 1:
            res = point_add(res, curr)
        curr = point_add(curr, curr)
        k >>= 1
    return res


def marshal_compressed(pt: Optional[Tuple[int, int]]) -> bytes:
    """Encodes a P-256 curve point into 33-byte compressed SEC1 format."""
    if pt is None:
        raise ValueError("Point at infinity cannot be compressed")
    x, y = pt
    prefix = b"\x02" if (y % 2 == 0) else b"\x03"
    return prefix + x.to_bytes(32, "big")


def unmarshal_compressed(data: bytes) -> Tuple[int, int]:
    """Decodes a 33-byte compressed SEC1 format point on P-256."""
    if len(data) != 33:
        raise ValueError(f"Invalid compressed point length: {len(data)}")
    prefix = data[0]
    if prefix not in (2, 3):
        raise ValueError(f"Invalid compressed point prefix: {prefix}")
    x = int.from_bytes(data[1:], "big")
    if x >= P:
        raise ValueError("x coordinate exceeds field prime")
    rhs = (pow(x, 3, P) + A * x + B) % P
    y = pow(rhs, P_PLUS_1_OVER_4, P)
    if (pow(y, 2, P) - rhs) % P != 0:
        raise ValueError("Point is not on curve")
    if (y % 2) != (prefix & 1):
        y = (P - y) % P
    return (x, y)


def expand_message_xmd(msg: bytes, dst: bytes, len_in_bytes: int) -> bytes:
    """Implements expand_message_xmd for SHA-256 per RFC 9380 Section 5.3.1."""
    if len(dst) > 255:
        dst = hashlib.sha256(b"H2C-OVERSIZE-DST-" + dst).digest()
    dst_len = bytes([len(dst)])
    b_in_bytes = 32
    ell = (len_in_bytes + b_in_bytes - 1) // b_in_bytes
    z_pad = b"\x00" * 64
    lib_str = len_in_bytes.to_bytes(2, "big")
    h = hashlib.sha256()
    h.update(z_pad)
    h.update(msg)
    h.update(lib_str)
    h.update(b"\x00")
    h.update(dst)
    h.update(dst_len)
    b0 = h.digest()
    b1 = hashlib.sha256(b0 + b"\x01" + dst + dst_len).digest()
    res = bytearray(b1)
    prev = b1
    for i in range(2, ell + 1):
        tmp = bytes(x ^ y for x, y in zip(b0, prev))
        bi = hashlib.sha256(tmp + bytes([i]) + dst + dst_len).digest()
        res.extend(bi)
        prev = bi
    return bytes(res[:len_in_bytes])


def map_to_curve_sswu(u: int) -> Tuple[int, int]:
    """Implements Simplified SWU mapping for P-256 per RFC 9380 Section 6.6.2."""
    u2 = (u * u) % P
    tv1 = (Z * u2) % P
    tv2 = (tv1 * tv1 + tv1) % P
    tv3 = (B * (tv2 + 1)) % P

    if tv2 != 0:
        tv4 = (-tv2) % P
    else:
        tv4 = Z
    tv4 = (tv4 * A) % P

    tv4_inv = pow(tv4, P - 2, P)
    x1 = (tv3 * tv4_inv) % P

    gx1 = (pow(x1, 3, P) + A * x1 + B) % P
    e1 = pow(gx1, P_MINUS_1_OVER_2, P)
    is_square = e1 == 1 or gx1 == 0

    if is_square:
        x = x1
        y = pow(gx1, P_PLUS_1_OVER_4, P)
    else:
        x = (tv1 * x1) % P
        gx2 = (pow(x, 3, P) + A * x + B) % P
        y = pow(gx2, P_PLUS_1_OVER_4, P)

    if (u & 1) != (y & 1):
        y = (P - y) % P
    return (x, y)


def hash_to_curve_p256(msg: bytes, dst: bytes) -> Tuple[int, int]:
    """Implements P256_XMD:SHA-256_SSWU_RO_ hash-to-curve per RFC 9380 Section 8.2."""
    ub = expand_message_xmd(msg, dst, 96)
    u0 = int.from_bytes(ub[:48], "big") % P
    u1 = int.from_bytes(ub[48:], "big") % P
    q0 = map_to_curve_sswu(u0)
    q1 = map_to_curve_sswu(u1)
    res = point_add(q0, q1)
    if res is None:
        raise ValueError("Hash to curve produced point at infinity")
    return res


def nonce() -> bytes:
    """Generates a 32-byte cryptographically secure random nonce."""
    return secrets.token_bytes(NONCE_LENGTH)


def sha256_hash(data: bytes) -> bytes:
    """Computes the SHA-256 digest of input data."""
    return hashlib.sha256(data).digest()


def hmac_sha256(key: bytes, message: bytes) -> bytes:
    """Computes HMAC-SHA-256."""
    return hmac.new(key, message, hashlib.sha256).digest()


def mac(key: bytes, data: bytes) -> bytes:
    """Computes a 32-byte MAC tag using HMAC-SHA-256."""
    return hmac_sha256(key, data)[:MAC_TAG_LENGTH]


def xor_bytes(a: bytes, b: bytes) -> bytes:
    """Computes bitwise XOR of two equal-length byte sequences."""
    if len(a) != len(b):
        raise ValueError(f"Byte sequences must have equal length: {len(a)} != {len(b)}")
    return (int.from_bytes(a, "big") ^ int.from_bytes(b, "big")).to_bytes(len(a), "big")


def concat(*arrays: bytes) -> bytes:
    """Concatenates multiple byte sequences."""
    return b"".join(arrays)


def expand(input_key_material: bytes, info: bytes, size: int) -> bytes:
    """Expands key material using HKDF with SHA-256."""
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=size,
        salt=b"",
        info=info,
    )
    return hkdf.derive(input_key_material)


def extract(input_key_material: bytes) -> bytes:
    """Extracts key material using HKDF with label 'Extract'."""
    return expand(input_key_material, b"Extract", 32)


def _validate_hash_parameters(hash_parameters) -> None:
    if hash_parameters is None:
        raise ValueError("hash_parameters cannot be None")
    if hasattr(hash_parameters, "HasField"):
        if not hash_parameters.HasField("argon2_id_parameters"):
            raise ValueError(
                "hash_parameters must contain non-nil argon2_id_parameters"
            )
        argon2_params = hash_parameters.argon2_id_parameters
    else:
        argon2_params = getattr(hash_parameters, "argon2_id_parameters", None)
        if argon2_params is None:
            raise ValueError(
                "hash_parameters must contain non-nil argon2_id_parameters"
            )

    if not (1 <= argon2_params.iteration_count <= 10):
        raise ValueError(
            f"Invalid Argon2Id iteration count: {argon2_params.iteration_count} (must be between 1 and 10)"
        )
    if not (8 <= argon2_params.memory_usage <= 65536):
        raise ValueError(
            f"Invalid Argon2Id memory usage: {argon2_params.memory_usage} (must be between 8 and 65536 KB)"
        )
    if not (1 <= argon2_params.parallelism <= 255):
        raise ValueError(
            f"Invalid Argon2Id parallelism: {argon2_params.parallelism} (must be between 1 and 255)"
        )
    if not (8 <= argon2_params.hash_size <= 512):
        raise ValueError(
            f"Invalid Argon2Id hash size: {argon2_params.hash_size} (must be between 8 and 512)"
        )


def stretch(input_bytes: bytes, hash_parameters) -> bytes:
    """Stretches the OPRF evaluation using Argon2id with server hash parameters."""
    _validate_hash_parameters(hash_parameters)
    argon2_params = hash_parameters.argon2_id_parameters

    salt = expand(input_bytes, b"Stretch", int(argon2_params.hash_size))
    argon2 = Argon2id(
        salt=salt,
        length=int(argon2_params.hash_size),
        iterations=int(argon2_params.iteration_count),
        lanes=int(argon2_params.parallelism),
        memory_cost=int(argon2_params.memory_usage),
    )
    return argon2.derive(input_bytes)


def random_oracle_sha256(x: bytes, max_val: int) -> bytes:
    """Iterative SHA-256 random oracle reduction mod max_val."""
    hash_output_length = 256
    output_bit_length = max_val.bit_length() + hash_output_length
    iter_count = (output_bit_length + hash_output_length - 1) // hash_output_length
    if iter_count > 255:
        raise ValueError(
            f"Domain bit length must not be greater than 65280: {output_bit_length}"
        )
    excess_bit_count = (iter_count * hash_output_length) - output_bit_length
    hash_output = 0
    for i in range(1, iter_count + 1):
        hash_output <<= hash_output_length
        bignum_bytes = bytes([i]) + x
        hashed_string = hashlib.sha256(bignum_bytes).digest()
        new_big_num = int.from_bytes(hashed_string, "big")
        hash_output += new_big_num

    hash_output >>= excess_bit_count
    hash_output %= max_val

    scalar_len = hash_output_length // 8
    max_len = (max_val.bit_length() + 7) // 8
    if max_len > scalar_len:
        scalar_len = max_len
    return hash_output.to_bytes(scalar_len, "big")


def derive_key_pair(seed: bytes, info: bytes) -> Tuple[bytes, bytes]:
    """Derives an ECDH public/private keypair from a seed and info string."""
    derive_input = seed + info
    priv_bytes = random_oracle_sha256(derive_input, ORDER)
    priv_int = int.from_bytes(priv_bytes, "big")
    if priv_int == 0:
        priv_int = 1
        priv_bytes = (1).to_bytes(32, "big")
    pub_point = point_mul(G, priv_int)
    pub_bytes = marshal_compressed(pub_point)
    return pub_bytes, priv_bytes


def diffie_hellman(priv_bytes: bytes, pub_bytes: bytes) -> bytes:
    """Computes the ECDH shared point peer_pub * priv."""
    pt = unmarshal_compressed(pub_bytes)
    priv_int = int.from_bytes(priv_bytes, "big")
    shared_pt = point_mul(pt, priv_int)
    return marshal_compressed(shared_pt)


def blind(password: bytes, blind_scalar: Optional[bytes] = None) -> Tuple[bytes, bytes]:
    """Blinds the password point using a random or provided scalar."""
    if len(password) == 0:
        raise ValueError("Password cannot be empty")
    pt = hash_to_curve_p256(password, LOGIN_DOMAIN_SEPARATION_TAG)
    if blind_scalar is None:
        while True:
            r = secrets.randbelow(ORDER)
            if r != 0:
                break
        blind_scalar = r.to_bytes(32, "big")
    else:
        r = int.from_bytes(blind_scalar, "big")
    blinded_pt = point_mul(pt, r)
    return marshal_compressed(blinded_pt), blind_scalar


def finalize(blind_scalar: bytes, evaluated_message: bytes) -> bytes:
    """Finalizes the OPRF output by multiplying with r^-1 mod Order."""
    if len(blind_scalar) == 0:
        raise ValueError("Blind scalar cannot be empty")
    r = int.from_bytes(blind_scalar, "big")
    r_inv = pow(r, ORDER - 2, ORDER)
    eval_pt = unmarshal_compressed(evaluated_message)
    res_pt = point_mul(eval_pt, r_inv)
    return marshal_compressed(res_pt)


def derive_secret(
    input_key_material: bytes, label: bytes, transcript_hash: bytes
) -> bytes:
    """Derives a secret labeled with 'OPAQUE-'."""
    info = b"OPAQUE-" + label + transcript_hash
    return expand(input_key_material, info, 32)


def derive_shared_keys(
    input_key_material: bytes, preamble: bytes
) -> Tuple[bytes, bytes, bytes]:
    """Derives the km2 (server MAC), km3 (client MAC), and sessionKey."""
    prk = extract(input_key_material)
    preamble_hash = sha256_hash(preamble)
    handshake_secret = derive_secret(prk, b"HandshakeSecret", preamble_hash)
    session_key = derive_secret(prk, b"SessionKey", preamble_hash)
    km2 = derive_secret(handshake_secret, b"ServerMAC", b"")
    km3 = derive_secret(handshake_secret, b"ClientMAC", b"")
    return km2, km3, session_key


def recover_client(
    username: str,
    randomized_password: bytes,
    envelope_nonce: bytes,
    auth_tag: bytes,
    server_public_key: bytes,
) -> Tuple[bytes, bytes]:
    """Recovers the client's export key and private key from the envelope."""
    auth_key = expand(randomized_password, envelope_nonce + AUTH_KEY_INFO, 32)
    export_key = expand(randomized_password, envelope_nonce + EXPORT_KEY_INFO, 32)
    seed = expand(randomized_password, envelope_nonce + PRIVATE_KEY_INFO, 32)
    _, client_private_key = derive_key_pair(seed, DIFFIE_HELLMAN_KEY_INFO)

    expected_tag = mac(
        auth_key, envelope_nonce + server_public_key + username.encode("utf-8")
    )
    if len(auth_tag) != len(expected_tag) or not hmac.compare_digest(
        expected_tag, auth_tag
    ):
        raise ValueError("Auth tag mismatch")
    return export_key, client_private_key


class UserAuthenticator:
    """Manages the client state and key exchanges for OPAQUE login authentication."""

    def clear(self) -> None:
        """Zeroizes and clears all sensitive cryptographic state."""
        _clear(self._password)
        self._password = None
        _clear(self._blind)
        self._blind = None
        _clear(self._client_private_keyshare)
        self._client_private_keyshare = None

    def __del__(self) -> None:
        self.clear()

    def __init__(self, username: str, password: str | bytes, hash_parameters):
        self.username = None
        self._password: Optional[bytearray] = None
        self.hash_parameters = None
        self._blind: Optional[bytearray] = None
        self._client_nonce: Optional[bytes] = None
        self._client_public_keyshare: Optional[bytes] = None
        self._client_private_keyshare: Optional[bytearray] = None

        if not username:
            raise ValueError("username cannot be empty")
        if isinstance(password, str):
            password = password.encode("utf-8")
        if len(password) == 0:
            raise ValueError("password cannot be empty")
        if hash_parameters is None:
            raise ValueError("hash_parameters cannot be None")
        _validate_hash_parameters(hash_parameters)

        self.username = username
        self._password = bytearray(password)
        self.hash_parameters = hash_parameters

    def initial_request(self) -> login_pb2.LoginRequest:
        """Generates the initial OPAQUE login request."""
        if self._password is None:
            raise ValueError("Authenticator already used or password not available")

        try:
            blinded_message, blind_scalar = blind(self._password)
            self._blind = bytearray(blind_scalar)

            self._client_nonce = nonce()
            random_nonce = nonce()

            pub_key, priv_key = derive_key_pair(random_nonce, DIFFIE_HELLMAN_KEY_INFO)
            self._client_public_keyshare = pub_key
            self._client_private_keyshare = bytearray(priv_key)

            initial_opaque_req = login_pb2.InitialOpaqueLoginRequest(
                blinded_message=blinded_message,
                client_nonce=self._client_nonce,
                client_public_keyshare=self._client_public_keyshare,
            )
            opaque_req = login_pb2.OpaqueLoginRequest(
                initial_request=initial_opaque_req
            )
            return login_pb2.LoginRequest(
                username=self.username,
                opaque_request=opaque_req,
            )
        finally:
            _clear(self._password)
            self._password = None

    def final_request(
        self, initial_response: login_pb2.LoginResponse
    ) -> login_pb2.LoginRequest:
        """Generates the final OPAQUE login request containing the client MAC."""
        if initial_response is None:
            raise ValueError("initial_response cannot be None")
        if (
            self._client_public_keyshare is None
            or self._client_nonce is None
            or self._client_private_keyshare is None
            or self._blind is None
        ):
            raise ValueError(
                "Authenticator not initialized; initial_request must be called first"
            )

        if (
            not hasattr(initial_response, "HasField")
            or not initial_response.HasField("opaque_response")
            or not initial_response.opaque_response.HasField("initial_response")
        ):
            raise ValueError("Expected initial opaque response from server")

        initial_opaque_resp = initial_response.opaque_response.initial_response

        evaluated_message = initial_opaque_resp.evaluated_message
        masking_nonce = initial_opaque_resp.masking_nonce
        masked_response = initial_opaque_resp.masked_response
        server_nonce = initial_opaque_resp.server_nonce
        server_mac = initial_opaque_resp.server_mac
        server_public_keyshare = initial_opaque_resp.server_public_keyshare

        if len(masked_response) != EXPECTED_ENVELOPE_SIZE:
            raise ValueError(
                f"Invalid masked response length: got {len(masked_response)}, want {EXPECTED_ENVELOPE_SIZE}"
            )

        try:
            oprf = finalize(self._blind, evaluated_message)
            stretched_oprf = stretch(oprf, self.hash_parameters)
            randomized_password = extract(concat(oprf, stretched_oprf))

            masking_key = expand(randomized_password, MASKING_KEY_INFO, 32)
            credential_response_pad = expand(
                masking_key,
                concat(masking_nonce, b"CredentialResponsePad"),
                len(masked_response),
            )
            serialized_envelope = xor_bytes(masked_response, credential_response_pad)
            if len(serialized_envelope) != EXPECTED_ENVELOPE_SIZE:
                raise ValueError(
                    f"Invalid serialized envelope length: got {len(serialized_envelope)}, want {EXPECTED_ENVELOPE_SIZE}"
                )

            server_public_key = serialized_envelope[:PUBLIC_KEY_LENGTH]
            envelope_nonce = serialized_envelope[
                PUBLIC_KEY_LENGTH : PUBLIC_KEY_LENGTH + NONCE_LENGTH
            ]
            auth_tag = serialized_envelope[
                PUBLIC_KEY_LENGTH + NONCE_LENGTH : EXPECTED_ENVELOPE_SIZE
            ]

            export_key, client_private_key = recover_client(
                self.username,
                randomized_password,
                envelope_nonce,
                auth_tag,
                server_public_key,
            )

            dh1 = diffie_hellman(self._client_private_keyshare, server_public_keyshare)
            dh2 = diffie_hellman(self._client_private_keyshare, server_public_key)
            dh3 = diffie_hellman(client_private_key, server_public_keyshare)

            input_key_material = concat(dh1, dh2, dh3)

            preamble = concat(
                b"OPAQUEv1-",
                self.username.encode("utf-8"),
                self._client_nonce,
                self._client_public_keyshare,
                server_public_key,
                evaluated_message,
                server_nonce,
                server_public_keyshare,
            )

            km2, km3, _ = derive_shared_keys(input_key_material, preamble)

            hashed_preamble = sha256_hash(preamble)
            expected_server_mac = mac(km2, hashed_preamble)
            if len(server_mac) != len(expected_server_mac) or not hmac.compare_digest(
                expected_server_mac, server_mac
            ):
                raise ValueError("Server MAC mismatch")

            client_mac = mac(km3, sha256_hash(concat(preamble, expected_server_mac)))

            final_opaque_req = login_pb2.FinalOpaqueLoginRequest(client_mac=client_mac)
            opaque_req = login_pb2.OpaqueLoginRequest(final_request=final_opaque_req)
            return login_pb2.LoginRequest(
                username=self.username,
                opaque_request=opaque_req,
            )
        finally:
            _clear(self._blind)
            self._blind = None
            _clear(self._client_private_keyshare)
            self._client_private_keyshare = None
